# Validasi ulang soal kelas 6 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sd-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 6 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model dipakai sebagai diagnostik; tidak diberikan kembali ke Gemini.

Jumlah soal: 25; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 20, "reasoning": 3, "knowing": 2}, "knowledgeDimension": {"procedural": 9, "conceptual": 15, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 16, "Medium": 9, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 20, "reasoning": 3, "knowing": 2}, "knowledgeDimension": {"procedural": 9, "conceptual": 15, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 16, "Medium": 9, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 25}`.
Run awal sukses: 75/75; adjudikasi: 8; token sukses tercatat: 249,617.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 16 | 16 | [Easy.json](difficulty/Easy.json) |
| Medium | 9 | 9 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `88621a8df02c5a5b537e9255`

Hani membuat 4 potong pita dengan panjang masing-masing $\frac{3}{4}$ m.<br><br>b. Berapa meter panjang potongan pita seluruhnya yang dimiliki Hani?

| Opsi | Isi |
|---|---|
| A | 12 m |
| B | 3 m |
| C | 4 $\frac{3}{4}$ m |
| D | $\frac{3}{16}$ m |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Panjang total pita = 4 x (3/4) m = 12/4 m = 3 m.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2bac760f519ddf4d374536223e07b5e62f00b10c3cd43cc3080e4cef78ef6cd4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2277 |
| 2 | success | valid / verified | applying | procedural | Easy | 2272 |
| 3 | success | valid / verified | applying | procedural | Easy | 2278 |

Run 1 — solusi: Panjang total pita = 4 x (3/4) m = 12/4 m = 3 m.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur perkalian bilangan asli dengan pecahan biasa dalam konteks rutin. Siswa hanya perlu mengenali operasi yang tepat (perkalian) dan melakukan perhitungan dasar.. Bukti: Hani membuat 4 potong pita dengan panjang masing-masing 3/4 m.; Berapa meter panjang potongan pita seluruhnya yang dimiliki Hani?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritme perkalian bilangan asli dengan pecahan, yang merupakan bagian dari prosedur matematika.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengalikan 4 dengan 3/4. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Hani membuat 4 potong pita dengan panjang masing-masing 3/4 m.; Berapa meter panjang potongan pita seluruhnya yang dimiliki Hani?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian bilangan asli dengan pecahan biasa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian pecahan adalah materi standar kelas 6. Soal ini adalah penerapan langsung tanpa langkah tambahan atau jebakan konseptual. |

Run 2 — solusi: Panjang total pita adalah 4 dikali 3/4 m, yaitu (4 * 3) / 4 = 12 / 4 = 3 m.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur perkalian bilangan asli dengan pecahan biasa yang sudah dipelajari di kelas 6. Prosedur ini bersifat langsung dan rutin.. Bukti: Hani membuat 4 potong pita dengan panjang masing-masing 3/4 m; Berapa meter panjang potongan pita seluruhnya
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritme perkalian bilangan asli dengan pecahan untuk menyelesaikan masalah ini.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep perkalian pecahan. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan beban kognitif rendah bagi siswa kelas 6.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m; Berapa meter panjang potongan pita seluruhnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian bilangan asli dengan pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian pecahan adalah materi standar kelas 6. Soal ini tidak memerlukan langkah tambahan atau penalaran kompleks. |

Run 3 — solusi: Panjang total pita adalah 4 dikali 3/4 meter. 4 x (3/4) = 12/4 = 3 meter.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur perkalian bilangan asli dengan pecahan yang sudah dipelajari di kelas 6. Soal ini bersifat rutin dan langsung.. Bukti: Hani membuat 4 potong pita dengan panjang masing-masing 3/4 m.; Berapa meter panjang potongan pita seluruhnya
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prosedur perkalian pecahan untuk menyelesaikan masalah ini.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep perkalian pecahan. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan hanya memerlukan satu langkah operasi hitung dasar.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m.; Berapa meter panjang potongan pita seluruhnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian bilangan asli dengan pecahan biasa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah terbiasa dengan operasi perkalian pecahan sederhana. Soal ini tidak menuntut perencanaan kompleks atau integrasi konsep yang sulit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 106/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000017 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.038572; conceptual=0.950013; procedural=0.011414; metacognitive=0.000000 | conceptual | 0.950013 | 0.162544 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.822835; Medium=0.174787; Hard=0.002378 | Easy | 0.822835 | 0.436625 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000019; H = 0.000019/ln(3) = 0.000017; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.950013; −Σp ln(p) = 0.225333; H = 0.225333/ln(4) = 0.162544; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.822835; −Σp ln(p) = 0.479682; H = 0.479682/ln(3) = 0.436625; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Perkalian Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Hani membuat 4 potong pita dengan panjang masing-masing $\frac{3}{4}$ m.

b. Berapa meter panjang potongan pita seluruhnya yang dimiliki Hani?
Pilihan: A. 12 m
B. 3 m
C. 4 $\frac{3}{4}$ m
D. $\frac{3}{16}$ m
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `b455e76a421c6174b0215cbf`

Fina membuat 75 kue pastel untuk acara keluarganya. Sebanyak $\frac{2}{15}$ bagian dari 75 pastel tersebut telah dikonsumsi oleh keluarganya selama acara berlangsung. Tentukan:<br><br>a. Banyaknya kue pastel yang sudah dikonsumsi oleh keluarga Fina.

| Opsi | Isi |
|---|---|
| A | 10 kue pastel |
| B | 150 kue pastel |
| C | 65 kue pastel |
| D | 5 kue pastel |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Banyak kue yang dikonsumsi = 2/15 * 75 = 2 * (75 / 15) = 2 * 5 = 10 kue.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c78f9fc30ae533cdeed5c08ace25bf3ad9a8f2d4095977d66880ad6393f3c2d3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2844 |
| 2 | success | valid / verified | applying | procedural | Easy | 2875 |
| 3 | success | valid / verified | applying | procedural | Easy | 2945 |

Run 1 — solusi: Banyak kue yang dikonsumsi = 2/15 * 75 = 2 * (75 / 15) = 2 * 5 = 10 kue.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep perkalian pecahan dengan bilangan bulat untuk mencari nilai bagian dari suatu kuantitas. Ini adalah prosedur rutin dalam matematika kelas 6.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian pecahan dengan bilangan bulat yang sudah dipelajari.. Bukti: 2/15 bagian dari 75
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan jalur penyelesaian yang jelas. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi non-rutin.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian pecahan dengan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep perkalian pecahan dengan bilangan bulat yang merupakan materi standar kelas 6. Jalur penyelesaian tunggal dan jelas tanpa tuntutan integrasi tinggi. |

Run 2 — solusi: 2/15 * 75 = (75 / 15) * 2 = 5 * 2 = 10 kue pastel.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perkalian pecahan dengan bilangan bulat dalam konteks masalah sehari-hari yang rutin.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi; Tentukan: a. Banyaknya kue pastel yang sudah dikonsumsi
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian pecahan dengan bilangan bulat untuk menyelesaikan masalah.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep perkalian pecahan. Jalur penyelesaian sangat jelas, hanya memerlukan satu langkah operasi hitung dasar, dan tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi; Tentukan: a. Banyaknya kue pastel yang sudah dikonsumsi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian pecahan dengan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari perkalian pecahan. Soal ini adalah prosedur standar yang tidak memerlukan perencanaan langkah tambahan. |

Run 3 — solusi: 2/15 * 75 = (75 / 15) * 2 = 5 * 2 = 10 kue pastel.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perkalian pecahan dengan bilangan bulat untuk menyelesaikan masalah rutin dalam konteks sehari-hari.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi; Tentukan: a. Banyaknya kue pastel yang sudah dikonsumsi
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian pecahan dengan bilangan bulat untuk mendapatkan hasil.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep perkalian pecahan dengan bilangan bulat. Jalur penyelesaian sangat jelas, hanya melibatkan satu operasi hitung utama, dan tidak ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi; Tentukan: a. Banyaknya kue pastel yang sudah dikonsumsi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep perkalian pecahan dengan bilangan bulat dan pembagian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari operasi hitung pecahan. Soal ini adalah latihan rutin yang langsung menguji pemahaman dasar tersebut tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 104/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.026073; conceptual=0.965224; procedural=0.008703; metacognitive=0.000000 | conceptual | 0.965224 | 0.123017 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.822526; Medium=0.170491; Hard=0.006983 | Easy | 0.822526 | 0.452370 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.965224; −Σp ln(p) = 0.170538; H = 0.170538/ln(4) = 0.123017; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.822526; −Σp ln(p) = 0.496979; H = 0.496979/ln(3) = 0.452370; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Perkalian Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Fina membuat 75 kue pastel untuk acara keluarganya. Sebanyak $\frac{2}{15}$ bagian dari 75 pastel tersebut telah dikonsumsi oleh keluarganya selama acara berlangsung. Tentukan:

a. Banyaknya kue pastel yang sudah dikonsumsi oleh keluarga Fina.
Pilihan: A. 10 kue pastel
B. 150 kue pastel
C. 65 kue pastel
D. 5 kue pastel
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `5f81ca1df4eea4a69b6fa218`

Pak Rudi membagi $\frac{2}{4}$ bagian tanah miliknya kepada 3 orang anaknya secara adil.<br><br>c. Berapa bagian tanah yang diperoleh masing-masing anak Pak Rudi? Tuliskan cara kalian menemukannya.

| Opsi | Isi |
|---|---|
| A | $\frac{1}{2}$ bagian, karena $\frac{2}{4}$ disederhanakan menjadi $\frac{1}{2}$ |
| B | $\frac{3}{2}$ bagian, karena $\frac{2}{4} \times 3 = \frac{6}{4}$ |
| C | $\frac{2}{7}$ bagian, karena penyebutnya dijumlahkan dengan 3 (4+3=7) |
| D | $\frac{1}{6}$ bagian, karena $\frac{2}{4} \div 3 = \frac{2}{12} = \frac{1}{6}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Membagi 2/4 bagian tanah kepada 3 anak berarti menghitung 2/4 : 3. Operasi pembagian pecahan dengan bilangan asli dilakukan dengan mengalikan penyebut dengan bilangan tersebut: 2/4 : 3 = 2 / (4 * 3) = 2/12. Menyederhanakan 2/12 dengan membagi pembilang dan penyebut dengan 2 menghasilkan 1/6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menyebutkan', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1eaf85ed74e9cd59f09194a169bce54248377c5c81b7356db595a4440414b79f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2468 |
| 2 | success | valid / verified | applying | procedural | Easy | 2455 |
| 3 | success | valid / verified | applying | procedural | Easy | 2464 |

Run 1 — solusi: Membagi 2/4 bagian tanah kepada 3 anak berarti menghitung 2/4 : 3. Operasi pembagian pecahan dengan bilangan asli dilakukan dengan mengalikan penyebut dengan bilangan tersebut: 2/4 : 3 = 2 / (4 * 3) = 2/12. Menyederhanakan 2/12 dengan membagi pembilang dan penyebut dengan 2 menghasilkan 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian pecahan dengan bilangan asli untuk menyelesaikan masalah pembagian adil yang rutin. Tidak ada strategi non-rutin yang diperlukan, hanya penerapan algoritma pembagian pecahan yang sudah dipelajari di kelas 6.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil; Berapa bagian tanah yang diperoleh masing-masing anak Pak Rudi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode pembagian pecahan dengan bilangan asli, yang merupakan bagian dari pengetahuan prosedural.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari prosedur pembagian pecahan yang umum diajarkan di kelas 6. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan beban kognitif rendah.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan dan operasi pembagian pecahan dengan bilangan asli. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pembagian pecahan adalah kurikulum standar kelas 6. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep yang sulit bagi siswa kelas 6. |

Run 2 — solusi: Masing-masing anak memperoleh bagian tanah sebesar (2/4) dibagi 3. Operasi pembagian pecahan dengan bilangan asli dilakukan dengan mengalikan penyebut dengan bilangan tersebut: 2 / (4 x 3) = 2/12. Setelah disederhanakan, 2/12 menjadi 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian pecahan dengan bilangan asli yang sudah dipelajari di kelas 6. Soal ini menuntut penerapan prosedur rutin untuk menyelesaikan masalah pembagian sederhana.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil.; Berapa bagian tanah yang diperoleh masing-masing anak Pak Rudi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode pembagian pecahan dengan bilangan bulat (procedural knowledge).. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari prosedur pembagian pecahan dengan bilangan asli yang merupakan materi standar kelas 6. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan beban kalkulasi sangat rendah.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan dan operasi pembagian pecahan dengan bilangan asli. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pembagian pecahan adalah kurikulum standar kelas 6. Soal ini tidak memerlukan penalaran kompleks atau integrasi konsep yang sulit, sehingga tingkat kesulitannya rendah bagi siswa kelas 6. |

Run 3 — solusi: Membagi 2/4 bagian tanah dengan 3 anak berarti menghitung 2/4 : 3. Operasi pembagian pecahan dengan bilangan asli dilakukan dengan mengalikan penyebut dengan bilangan tersebut: 2/4 : 3 = 2/(4 x 3) = 2/12. Menyederhanakan 2/12 dengan membagi pembilang dan penyebut dengan 2 menghasilkan 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian pecahan dengan bilangan asli yang sudah dipelajari di kelas 6. Soal ini menuntut penerapan konsep pembagian pecahan dalam konteks rutin.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil; Berapa bagian tanah yang diperoleh masing-masing anak Pak Rudi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme atau metode pembagian pecahan dengan bilangan bulat.. Bukti: membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari prosedur pembagian pecahan yang umum diajarkan di kelas 6. Jalur penyelesaiannya jelas (2/4 dibagi 3), tidak ada kendala yang berinteraksi, dan tidak memerlukan strategi nonrutin.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan, penyederhanaan pecahan, dan operasi pembagian pecahan dengan bilangan asli. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pembagian pecahan dengan bilangan asli adalah standar kurikulum kelas 6. Soal ini tidak memiliki kompleksitas tambahan, sehingga tingkat kesulitannya rendah bagi siswa kelas 6. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 237/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000017; applying=0.999983; reasoning=0.000000 | applying | 0.999983 | 0.000181 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000042; conceptual=0.978966; procedural=0.020992; metacognitive=0.000000 | conceptual | 0.978966 | 0.073822 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.448878; Medium=0.534699; Hard=0.016423 | Medium | 0.534699 | 0.693407 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999983; −Σp ln(p) = 0.000199; H = 0.000199/ln(3) = 0.000181; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.978966; −Σp ln(p) = 0.102340; H = 0.102340/ln(4) = 0.073822; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.534699; −Σp ln(p) = 0.761785; H = 0.761785/ln(3) = 0.693407; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Pembagian Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Rudi membagi $\frac{2}{4}$ bagian tanah miliknya kepada 3 orang anaknya secara adil.

c. Berapa bagian tanah yang diperoleh masing-masing anak Pak Rudi? Tuliskan cara kalian menemukannya.
Pilihan: A. $\frac{1}{2}$ bagian, karena $\frac{2}{4}$ disederhanakan menjadi $\frac{1}{2}$
B. $\frac{3}{2}$ bagian, karena $\frac{2}{4} \times 3 = \frac{6}{4}$
C. $\frac{2}{7}$ bagian, karena penyebutnya dijumlahkan dengan 3 (4+3=7)
D. $\frac{1}{6}$ bagian, karena $\frac{2}{4} \div 3 = \frac{2}{12} = \frac{1}{6}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Medium", "blindLabel": "Easy", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `a0855f2dc2ba10aa142bba57`

Rina memiliki 6 kg gula pasir. Rina akan membuat kue bolu. Setiap adonan kue bolu membutuhkan $\frac{3}{4}$ kg gula pasir.<br><br>Berapa banyak kue bolu yang dibuat oleh Rina?

| Opsi | Isi |
|---|---|
| A | 4,5 kue bolu |
| B | 24 kue bolu |
| C | 2 kue bolu |
| D | 8 kue bolu |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Banyak kue = 6 / (3/4) = 6 * (4/3) = 24 / 3 = 8 kue.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `36096c480c31cd9b1117882ba7f4783f77eb009af5a5b4fdf820297229153878`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2234 |
| 2 | success | valid / verified | applying | procedural | Easy | 2335 |
| 3 | success | valid / verified | applying | procedural | Easy | 2329 |

Run 1 — solusi: Banyak kue = 6 / (3/4) = 6 * (4/3) = 24 / 3 = 8 kue.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian bilangan bulat dengan pecahan yang sudah dipelajari di kelas 6. Soal ini bersifat rutin karena siswa hanya perlu mengidentifikasi operasi pembagian yang tepat untuk membagi total gula dengan kebutuhan per kue.. Bukti: Rina memiliki 6 kg gula pasir.; Setiap adonan kue bolu membutuhkan 3/4 kg gula pasir.; Berapa banyak kue bolu yang dibuat oleh Rina?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritme pembagian pecahan, yaitu mengalikan dengan kebalikan dari pembagi.. Bukti: 6 / (3/4) = 6 * (4/3)
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas (pembagian langsung). Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi non-rutin. Siswa hanya perlu menerapkan algoritme pembagian pecahan yang sudah familiar.. Bukti: Rina memiliki 6 kg gula pasir.; Setiap adonan kue bolu membutuhkan 3/4 kg gula pasir.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian pecahan dan operasi perkalian pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pembagian pecahan adalah standar kurikulum kelas 6. Soal ini tidak menuntut penalaran kompleks, hanya penerapan prosedur standar. |

Run 2 — solusi: Banyak kue = 6 / (3/4) = 6 * (4/3) = 24 / 3 = 8 kue.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian bilangan bulat dengan pecahan untuk menyelesaikan masalah kontekstual yang rutin. Tidak diperlukan strategi nonrutin atau penalaran kompleks.. Bukti: Rina memiliki 6 kg gula pasir.; Setiap adonan kue bolu membutuhkan 3/4 kg gula pasir.; Berapa banyak kue bolu yang dibuat oleh Rina?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman dan penerapan algoritma pembagian pecahan (mengalikan dengan kebalikan pembagi).. Bukti: 6 / (3/4) = 6 * (4/3)
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari konsep pembagian pecahan yang umum dipelajari di kelas 6. Jalur penyelesaiannya tunggal dan jelas, tidak ada kendala yang berinteraksi, dan beban kalkulasinya rendah.. Bukti: 6 kg gula pasir; 3/4 kg gula pasir; Berapa banyak kue bolu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian pecahan dan operasi perkalian pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pembagian pecahan adalah kurikulum standar kelas 6. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga termasuk kategori mudah bagi siswa kelas 6. |

Run 3 — solusi: Banyak kue = 6 / (3/4) = 6 * (4/3) = 24 / 3 = 8 kue.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian bilangan bulat dengan pecahan yang sudah dipelajari di kelas 6. Prosedur ini bersifat rutin dan langsung.. Bukti: Rina memiliki 6 kg gula pasir.; Setiap adonan kue bolu membutuhkan 3/4 kg gula pasir.; Berapa banyak kue bolu yang dibuat oleh Rina?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau metode pembagian pecahan (mengalikan dengan kebalikan pembagi).. Bukti: 6 / (3/4) = 6 * (4/3)
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep pembagian pecahan. Jalur penyelesaiannya jelas, tidak ada kendala yang berinteraksi, dan beban kalkulasinya rendah bagi siswa kelas 6.. Bukti: 6 kg gula pasir; 3/4 kg gula pasir; Berapa banyak kue bolu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian pecahan dan operasi perkalian pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian bilangan bulat dengan pecahan adalah materi standar kelas 6. Soal ini tidak menuntut perencanaan kompleks atau integrasi konsep yang sulit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 98/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000038; applying=0.999962; reasoning=0.000000 | applying | 0.999962 | 0.000382 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.106681; conceptual=0.873899; procedural=0.019420; metacognitive=0.000000 | conceptual | 0.873899 | 0.312401 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.871152; Medium=0.125088; Hard=0.003760 | Easy | 0.871152 | 0.365175 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999962; −Σp ln(p) = 0.000420; H = 0.000420/ln(3) = 0.000382; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.873899; −Σp ln(p) = 0.433080; H = 0.433080/ln(4) = 0.312401; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.871152; −Σp ln(p) = 0.401185; H = 0.401185/ln(3) = 0.365175; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Pembagian Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Rina memiliki 6 kg gula pasir. Rina akan membuat kue bolu. Setiap adonan kue bolu membutuhkan $\frac{3}{4}$ kg gula pasir.

Berapa banyak kue bolu yang dibuat oleh Rina?
Pilihan: A. 4,5 kue bolu
B. 24 kue bolu
C. 2 kue bolu
D. 8 kue bolu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `998e959414afdb8d9903faba`

Perhatikan gambar Informasi Nilai Gizi di salah satu kemasan makanan berikut. Pada informasi tersebut dituliskan komposisi kandungan protein, lemak, karbohidrat, serat pangan, dan natrium. Berdasarkan informasi tersebut, jawablah pertanyaan berikut ini.<br><br>b. Kandungan zat apakah yang paling kecil komposisinya dan berapakah komposisinya?

| Opsi | Isi |
|---|---|
| A | Natrium, 88,6 mg |
| B | Karbohidrat, 28,6 g |
| C | Serat Pangan, 2,7 g |
| D | Protein, 1,3 g |

![Gambar sumber soal 5](<../../../images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Konversi satuan: 88,6 mg = 0,0886 g. Membandingkan nilai dalam gram: 0,0886 (Natrium) < 1,3 (Protein) < 2,7 (Serat Pangan) < 5,4 (Lemak) < 28,6 (Karbohidrat). Jadi, yang terkecil adalah Natrium dengan 88,6 mg.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png. Transkripsi visual: Gambar menunjukkan label Informasi Nilai Gizi dengan data: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, dan Natrium 88,6 mg.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0d6a8c9d5ba14c7bf36567fcfa86070771bbc756329e8727cd55892737d19dc2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3665 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3678 |
| 3 | success | valid / verified | applying | conceptual | Medium | 4922 |

Run 1 — solusi: Konversi satuan: 88,6 mg = 0,0886 g. Membandingkan nilai dalam gram: 0,0886 (Natrium) < 1,3 (Protein) < 2,7 (Serat Pangan) < 5,4 (Lemak) < 28,6 (Karbohidrat). Jadi, yang terkecil adalah Natrium dengan 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai desimal dengan satuan yang berbeda (g dan mg). Ini memerlukan pemahaman konsep konversi satuan dasar dan perbandingan bilangan desimal, yang merupakan penerapan prosedur familiar dalam konteks nyata.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, dan Natrium 88,6 mg
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar satuan massa (gram dan miligram) serta perbandingan nilai desimal.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; 88,6 mg = 0,0886 g
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka 88,6 dengan 1,3; 5,4; 2,7; dan 28,6. Mereka harus menyadari perbedaan satuan (mg vs g) dan melakukan konversi atau penyamaan satuan terlebih dahulu sebelum membandingkan. Ini melibatkan beberapa langkah yang saling terkait.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Natrium 88,6 mg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan massa (mg ke g) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu mengonversi satuan massa dasar dan membandingkan desimal. Tantangan utama adalah jebakan satuan mg vs g yang memerlukan ketelitian. |

Run 2 — solusi: Konversi semua satuan ke gram: Natrium 88,6 mg = 0,0886 g. Membandingkan nilai: 0,0886 g (Natrium) < 1,3 g (Protein) < 2,7 g (Serat Pangan) < 5,4 g (Lemak) < 28,6 g (Karbohidrat). Jadi, yang terkecil adalah Natrium dengan 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai desimal dengan satuan yang berbeda (gram dan miligram). Ini memerlukan pemahaman konsep satuan dan perbandingan bilangan desimal, yang merupakan penerapan prosedur pada konteks rutin.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Natrium 88,6 mg; Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar satuan (mg ke g) dan perbandingan nilai desimal dalam konteks nyata.. Bukti: Natrium 88,6 mg; Protein 1,3 g
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka 88,6 dengan 1,3 tanpa melakukan konversi satuan terlebih dahulu. Terdapat kendala interaksi antara satuan (mg vs g) yang harus diselesaikan sebelum perbandingan dilakukan.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Natrium 88,6 mg; Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g

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
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan konversi satuan dasar dan membandingkan desimal. Tantangan utama adalah jebakan satuan mg vs g yang memerlukan ketelitian. |

Run 3 — solusi: Konversi satuan ke gram: Natrium 88,6 mg = 0,0886 g. Bandingkan nilai: 0,0886 g (Natrium) < 1,3 g (Protein) < 2,7 g (Serat Pangan) < 5,4 g (Lemak) < 28,6 g (Karbohidrat). Jadi, yang terkecil adalah Natrium, 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang perbandingan nilai desimal dan konversi satuan (mg ke g) untuk menentukan nilai terkecil dari data yang diberikan.. Bukti: Kandungan zat apakah yang paling kecil komposisinya
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antar satuan massa (gram dan miligram) dan prinsip perbandingan nilai desimal.. Bukti: Protein 1,3 g; Natrium 88,6 mg
- Intended difficulty `classify/Medium`: Soal menuntut siswa menyadari perbedaan satuan (mg vs g). Tanpa konversi, siswa mungkin salah memilih 1,3 g karena angka 1,3 terlihat lebih kecil dari 88,6. Ini adalah jebakan umum bagi siswa kelas 6.. Bukti: Natrium 88,6 mg; Protein 1,3 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perbandingan bilangan desimal dan konversi satuan massa dasar (mg ke g). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari desimal dan satuan berat. Kesulitan terletak pada ketelitian membandingkan nilai dengan satuan berbeda (mg vs g), bukan pada kompleksitas perhitungan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 164/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.003628; applying=0.996372; reasoning=0.000000 | applying | 0.996372 | 0.021854 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.030466; conceptual=0.941438; procedural=0.028096; metacognitive=0.000000 | conceptual | 0.941438 | 0.190102 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.795867; Medium=0.196694; Hard=0.007438 | Easy | 0.795867 | 0.489723 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996372; −Σp ln(p) = 0.024009; H = 0.024009/ln(3) = 0.021854; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.941438; −Σp ln(p) = 0.263537; H = 0.263537/ln(4) = 0.190102; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.795867; −Σp ln(p) = 0.538016; H = 0.538016/ln(3) = 0.489723; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Bilangan Desimal
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar Informasi Nilai Gizi di salah satu kemasan makanan berikut. Pada informasi tersebut dituliskan komposisi kandungan protein, lemak, karbohidrat, serat pangan, dan natrium. Berdasarkan informasi tersebut, jawablah pertanyaan berikut ini.

b. Kandungan zat apakah yang paling kecil komposisinya dan berapakah komposisinya?
Pilihan: A. Natrium, 88,6 mg
B. Karbohidrat, 28,6 g
C. Serat Pangan, 2,7 g
D. Protein, 1,3 g
Transkripsi visual: Gambar menunjukkan label Informasi Nilai Gizi dengan data: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, dan Natrium 88,6 mg.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `4d27f58bb8fe872a49e1bd5b`

Arman, Bayu, dan Didi mengikuti lomba lompat jauh. Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m. Siapakah yang melompat paling jauh dan paling dekat?

| Opsi | Isi |
|---|---|
| A | Paling jauh Arman, paling dekat Bayu |
| B | Paling jauh Bayu, paling dekat Didi |
| C | Paling jauh Arman, paling dekat Didi |
| D | Paling jauh Didi, paling dekat Bayu |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Nilai terbesar adalah 3,7 (Arman) dan nilai terkecil adalah 2,9 (Didi).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `159f2449707a156232b4e96cf29348125df8e28777ac4f702f441b1d1e69de5a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2380 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2358 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2361 |

Run 1 — solusi: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Nilai terbesar adalah 3,7 (Arman) dan nilai terkecil adalah 2,9 (Didi).
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan dan mengurutkan bilangan desimal untuk menentukan nilai maksimum dan minimum. Ini adalah penerapan langsung dari konsep perbandingan bilangan desimal yang sudah dipelajari di kelas 6.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat dan perbandingan bilangan desimal.. Bukti: 3,7 m; 2,9 m; 3,6 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan tiga bilangan desimal dengan satu angka di belakang koma. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan desimal persepuluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan desimal adalah materi dasar kelas 6. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep, sehingga dikategorikan mudah. |

Run 2 — solusi: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Nilai terbesar adalah 3,7 (Arman) dan nilai terkecil adalah 2,9 (Didi).
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan dan mengurutkan bilangan desimal untuk menentukan nilai maksimum dan minimum. Ini adalah penerapan langsung dari konsep perbandingan bilangan desimal yang sudah dipelajari di kelas 6.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat dan perbandingan bilangan desimal.. Bukti: Siapakah yang melompat paling jauh dan paling dekat?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan tiga bilangan desimal dengan satu angka di belakang koma. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan desimal persepuluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan desimal adalah materi dasar kelas 6. Soal ini tidak memerlukan perencanaan atau integrasi langkah yang rumit. |

Run 3 — solusi: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Nilai terbesar adalah 3,7 (Arman) dan nilai terkecil adalah 2,9 (Didi).
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengurutkan dan membandingkan tiga bilangan desimal untuk menentukan nilai maksimum dan minimum. Ini adalah prosedur langsung yang menggunakan konsep nilai tempat desimal.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat dan urutan bilangan desimal, yang merupakan konsep dasar dalam sistem bilangan.. Bukti: Siapakah yang melompat paling jauh dan paling dekat?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan tiga angka desimal yang memiliki jumlah digit yang sama. Tidak ada langkah perantara atau kendala yang kompleks.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat desimal persepuluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan desimal adalah materi standar kelas 6. Tugas ini bersifat rutin dan tidak memerlukan perencanaan langkah yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3887`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk membandingkan tiga bilangan desimal untuk menentukan nilai maksimum dan minimum. Ini adalah penerapan langsung dari konsep perbandingan bilangan desimal yang sudah dipelajari di kelas 6.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat dan perbandingan bilangan desimal.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan tiga bilangan desimal dengan satu angka di belakang koma. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan desimal persepuluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan desimal adalah materi dasar kelas 6. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep, sehingga dikategorikan mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 124/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.114765; conceptual=0.811195; procedural=0.074040; metacognitive=0.000000 | conceptual | 0.811195 | 0.440691 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.763560; Medium=0.232484; Hard=0.003956 | Easy | 0.763560 | 0.516146 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.811195; −Σp ln(p) = 0.610928; H = 0.610928/ln(4) = 0.440691; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.763560; −Σp ln(p) = 0.567044; H = 0.567044/ln(3) = 0.516146; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Bilangan Desimal
Tipe soal: multiple_choice
Stimulus: -
Soal: Arman, Bayu, dan Didi mengikuti lomba lompat jauh. Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m. Siapakah yang melompat paling jauh dan paling dekat?
Pilihan: A. Paling jauh Arman, paling dekat Bayu
B. Paling jauh Bayu, paling dekat Didi
C. Paling jauh Arman, paling dekat Didi
D. Paling jauh Didi, paling dekat Bayu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `3c69165f4b4cdf66760b5fe1`

Di daerah Nusa Tenggara Timur terdapat beberapa macam bahasa yang digunakan sehari-hari. Penggunaan bahasa Indonesia $\frac{1}{8}$ bagian. Penggunaan bahasa daerah $\frac{3}{10}$ bagian. Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?

| Opsi | Isi |
|---|---|
| A | $\frac{2}{40}$ |
| B | $\frac{2}{18}$ |
| C | $\frac{17}{40}$ |
| D | $\frac{7}{40}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menentukan selisih 3/10 dan 1/8. KPK dari 10 dan 8 adalah 40. 3/10 = 12/40 dan 1/8 = 5/40. Selisihnya adalah 12/40 - 5/40 = 7/40.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `13bf9699b5ce3db45ee035995e39e699dd5cbaf06e83b6696fe66d0d9d00df71`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2312 |
| 2 | success | valid / verified | applying | procedural | Easy | 2272 |
| 3 | success | valid / verified | applying | procedural | Easy | 2273 |

Run 1 — solusi: Menentukan selisih 3/10 dan 1/8. KPK dari 10 dan 8 adalah 40. 3/10 = 12/40 dan 1/8 = 5/40. Selisihnya adalah 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan pecahan dengan penyebut berbeda yang merupakan prosedur rutin dalam kurikulum kelas 6.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan pecahan yang memerlukan penyamaan penyebut (prosedural).. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung prosedur pengurangan pecahan dengan penyebut berbeda yang merupakan materi standar kelas 6. Jalur penyelesaian sangat jelas (menyamakan penyebut lalu mengurangkan) tanpa ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan pecahan dengan penyebut berbeda, konsep KPK. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan pecahan dengan penyebut berbeda adalah kompetensi dasar kelas 6. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga tingkat kesulitannya rendah bagi siswa kelas 6. |

Run 2 — solusi: Samakan penyebut dari 3/10 dan 1/8 menjadi 40. 3/10 = 12/40 dan 1/8 = 5/40. Selisihnya adalah 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan pecahan dengan penyebut berbeda yang sudah dipelajari di kelas 6. Ini adalah penerapan rutin dari konsep pecahan.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan pecahan (prosedural) yang memerlukan penyamaan penyebut (konseptual).. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena prosedurnya langsung dan familiar bagi siswa kelas 6. Tidak ada kendala kompleks atau langkah non-rutin.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan pecahan dengan penyebut berbeda. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan sudah mahir menyamakan penyebut dan melakukan operasi pengurangan pecahan sederhana. |

Run 3 — solusi: Samakan penyebut dari 3/10 dan 1/8 menjadi per 40. 3/10 = 12/40 dan 1/8 = 5/40. Selisihnya adalah 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur pengurangan pecahan dengan penyebut berbeda dalam konteks soal cerita sederhana. Ini adalah penerapan rutin dari konsep pecahan.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan pecahan, yang merupakan bagian dari pengetahuan prosedural.. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan operasi pengurangan pecahan dengan penyebut berbeda. Langkah-langkahnya standar dan familiar bagi siswa kelas 6.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan pecahan dengan penyebut berbeda. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari operasi hitung pecahan. Soal ini adalah aplikasi langsung dari prosedur tersebut tanpa kerumitan tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 149/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000023; applying=0.999977; reasoning=0.000000 | applying | 0.999977 | 0.000240 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000292; conceptual=0.971577; procedural=0.028132; metacognitive=0.000000 | conceptual | 0.971577 | 0.094385 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.689131; Medium=0.304784; Hard=0.006085 | Easy | 0.689131 | 0.591431 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999977; −Σp ln(p) = 0.000264; H = 0.000264/ln(3) = 0.000240; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.971577; −Σp ln(p) = 0.130845; H = 0.130845/ln(4) = 0.094385; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.689131; −Σp ln(p) = 0.649753; H = 0.649753/ln(3) = 0.591431; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Pengurangan Bilangan Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di daerah Nusa Tenggara Timur terdapat beberapa macam bahasa yang digunakan sehari-hari. Penggunaan bahasa Indonesia $\frac{1}{8}$ bagian. Penggunaan bahasa daerah $\frac{3}{10}$ bagian. Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?
Pilihan: A. $\frac{2}{40}$
B. $\frac{2}{18}$
C. $\frac{17}{40}$
D. $\frac{7}{40}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `6111d90e8a172592ecbf7d25`

Berikut daftar banyak pengunjung yang sedang antre di beberapa wahana di taman hiburan.<br><br>\|_Roller coaster_\|24\|<br>\|---\|---\|<br>\|Bianglala\|….\|<br>\|Komidi putar\|18\|<br>\|Rumah hantu\|….\|<br><br>b. Berapakah banyak pengunjung yang antre di wahana bianglala, jika diketahui rasio pengunjung yang antre di wahana bianglala terhadap _roller coaster_ adalah 4 : 3 ?

| Opsi | Isi |
|---|---|
| A | 12 orang |
| B | 32 orang |
| C | 18 orang |
| D | 6 orang |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Rasio bianglala : roller coaster = 4 : 3. Jumlah pengunjung roller coaster = 24. Faktor pengali = 24 / 3 = 8. Maka, jumlah pengunjung bianglala = 4 * 8 = 32.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `11b6e8c9675f159c0e0eff65bcf380820db8e0fdeef817929aecb481e7ab1845`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2465 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2467 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2469 |

Run 1 — solusi: Rasio bianglala : roller coaster = 4 : 3. Jumlah pengunjung roller coaster = 24. Faktor pengali = 24 / 3 = 8. Maka, jumlah pengunjung bianglala = 4 * 8 = 32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio untuk mencari nilai yang belum diketahui berdasarkan nilai yang sudah diketahui (roller coaster). Ini adalah penerapan prosedur rasio yang rutin pada konteks yang diberikan.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Berapakah banyak pengunjung yang antre di wahana bianglala
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep rasio dan bagaimana menggunakan faktor pengali untuk menyelesaikan masalah perbandingan senilai.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan dua langkah logis: menentukan faktor pengali dari rasio yang diketahui (24/3=8) dan menerapkannya pada rasio yang ditanyakan (4*8=32). Meskipun prosedurnya rutin, siswa harus memahami hubungan antara rasio dan nilai sebenarnya.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Roller coaster 24

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian/perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari rasio. Soal ini menuntut pemahaman hubungan bagian-ke-bagian yang merupakan standar kompetensi kelas 6. |

Run 2 — solusi: Rasio bianglala : roller coaster = 4 : 3. Diketahui jumlah pengunjung roller coaster = 24. Faktor pengali = 24 / 3 = 8. Maka, jumlah pengunjung bianglala = 4 * 8 = 32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio untuk mencari nilai yang belum diketahui berdasarkan rasio yang diberikan dan satu nilai yang sudah diketahui. Ini adalah penerapan prosedur rasio pada konteks rutin.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Berapakah banyak pengunjung yang antre di wahana bianglala
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (rasio) antara dua kuantitas, yang merupakan pengetahuan konseptual.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan pemilihan prosedur rasio yang tepat dan pemahaman hubungan antara rasio dan nilai sebenarnya. Siswa harus menentukan faktor pengali terlebih dahulu sebelum menghitung nilai akhir. Jalur penyelesaian jelas namun memerlukan dua langkah logis yang saling terkait.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; diketahui rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan perbandingan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari rasio. Soal ini menuntut pemahaman hubungan rasio yang merupakan standar kompetensi kelas 6, dengan tingkat kesulitan menengah karena memerlukan langkah perantara (mencari faktor pengali). |

Run 3 — solusi: Rasio Bianglala : Roller coaster = 4 : 3. Jumlah Roller coaster = 24. Faktor pengali = 24 / 3 = 8. Maka, jumlah Bianglala = 4 * 8 = 32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio untuk mencari nilai yang belum diketahui berdasarkan nilai yang sudah diketahui (roller coaster) dan perbandingan yang diberikan. Ini adalah penerapan prosedur rutin dalam konteks rasio.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Berapakah banyak pengunjung yang antre di wahana bianglala
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep rasio dan bagaimana menggunakannya untuk menentukan nilai kuantitas yang proporsional.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan dua langkah logis: menentukan faktor pengali dari rasio yang diketahui terhadap nilai aktual, lalu mengalikan faktor tersebut ke rasio yang ditanyakan. Meskipun prosedurnya rutin, siswa harus memahami hubungan proporsional antara rasio dan jumlah nyata.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Berapakah banyak pengunjung yang antre di wahana bianglala

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan proporsi, serta operasi perkalian dan pembagian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, konsep rasio adalah materi standar. Soal ini menuntut pemahaman hubungan proporsional yang merupakan inti dari materi rasio di tingkat ini, dengan tingkat kesulitan yang sesuai untuk latihan rutin. |

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
| Domain kognitif | knowing=0.000005; applying=0.999995; reasoning=0.000000 | applying | 0.999995 | 0.000061 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.007770; conceptual=0.856466; procedural=0.135764; metacognitive=0.000000 | conceptual | 0.856466 | 0.318505 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.676145; Medium=0.318346; Hard=0.005510 | Easy | 0.676145 | 0.598619 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999995; −Σp ln(p) = 0.000068; H = 0.000068/ln(3) = 0.000061; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.856466; −Σp ln(p) = 0.441542; H = 0.441542/ln(4) = 0.318505; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.676145; −Σp ln(p) = 0.657650; H = 0.657650/ln(3) = 0.598619; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Konsep Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Berikut daftar banyak pengunjung yang sedang antre di beberapa wahana di taman hiburan.

|_Roller coaster_|24|
|---|---|
|Bianglala|….|
|Komidi putar|18|
|Rumah hantu|….|

b. Berapakah banyak pengunjung yang antre di wahana bianglala, jika diketahui rasio pengunjung yang antre di wahana bianglala terhadap _roller coaster_ adalah 4 : 3 ?
Pilihan: A. 12 orang
B. 32 orang
C. 18 orang
D. 6 orang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `7181f282bc4df58e74ef5120`

Banyu ingin mengundang teman-teman datang ke rumah untuk merayakan ulang tahunnya. Banyu menyiapkan 6 liter minuman untuk 15 orang teman yang datang di pagi hari. Di siang hari, akan datang teman sebanyak 10 orang, berapa liter minuman yang harus disiapkan?

| Opsi | Isi |
|---|---|
| A | 5 liter |
| B | 6 liter |
| C | 4 liter |
| D | 9 liter |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Rasio minuman terhadap tamu adalah 6 liter : 15 orang = 2 : 5. Untuk 10 orang, kebutuhan minuman adalah (10 / 5) * 2 = 4 liter.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e4f97c5e3a0438f1ed344a2d74181c87be5d55956333669fd20842291dab0987`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2372 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2315 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2325 |

Run 1 — solusi: Rasio minuman terhadap tamu adalah 6 liter : 15 orang = 2 : 5. Untuk 10 orang, kebutuhan minuman adalah (10 / 5) * 2 = 4 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menentukan jumlah minuman yang dibutuhkan berdasarkan jumlah tamu yang berbeda. Ini adalah penerapan prosedur rutin dalam konteks proporsi.. Bukti: 6 liter minuman untuk 15 orang teman; di siang hari, akan datang teman sebanyak 10 orang, berapa liter minuman yang harus disiapkan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep rasio) dan penggunaan metode untuk menyelesaikannya (prosedural).. Bukti: 6 liter minuman untuk 15 orang teman; rasio minuman terhadap tamu 6 : 15 = 2 : 5
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah proporsi langsung yang standar untuk kelas 6. Jalur penyelesaiannya jelas (menentukan rasio atau faktor pengali), tidak melibatkan kendala yang rumit, dan menggunakan angka yang sederhana.. Bukti: 6 liter minuman untuk 15 orang teman; berapa liter minuman yang harus disiapkan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pecahan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah perbandingan senilai adalah materi standar kelas 6. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga termasuk kategori mudah. |

Run 2 — solusi: Rasio minuman terhadap tamu adalah 6 liter / 15 orang = 2/5 liter per orang. Untuk 10 orang, minuman yang dibutuhkan adalah 10 orang * (2/5 liter/orang) = 4 liter.
- Domain kognitif `classify/applying`: Siswa perlu memilih dan menerapkan konsep rasio senilai untuk menyelesaikan masalah dalam konteks rutin (proporsi).. Bukti: 6 liter minuman untuk 15 orang teman; berapa liter minuman yang harus disiapkan untuk 10 orang
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip rasio senilai (konsep) untuk menentukan nilai yang tidak diketahui.. Bukti: 6 liter minuman untuk 15 orang; 10 orang
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah proporsi sederhana yang familiar bagi siswa kelas 6. Jalur penyelesaiannya jelas (menentukan rasio atau faktor pengali) dan tidak memerlukan perencanaan langkah yang kompleks.. Bukti: 6 liter minuman untuk 15 orang; berapa liter minuman yang harus disiapkan untuk 10 orang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pecahan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah proporsi sederhana dengan angka yang mudah disederhanakan adalah materi standar kelas 6. |

Run 3 — solusi: Rasio minuman terhadap tamu adalah 6 liter : 15 orang = 2 : 5. Untuk 10 orang, kebutuhan minuman adalah (2/5) * 10 = 4 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menyelesaikan masalah proporsi sederhana dalam konteks sehari-hari yang rutin.. Bukti: 6 liter minuman untuk 15 orang teman; berapa liter minuman yang harus disiapkan untuk 10 orang
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip rasio dan proporsi untuk menentukan nilai yang tidak diketahui.. Bukti: 6 liter minuman untuk 15 orang; berapa liter minuman yang harus disiapkan
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung konsep rasio senilai. Jalur penyelesaiannya jelas (menentukan rasio satuan atau menggunakan faktor skala) dan tidak memerlukan perencanaan langkah yang kompleks atau integrasi kendala yang sulit bagi siswa kelas 6.. Bukti: 6 liter minuman untuk 15 orang; berapa liter minuman yang harus disiapkan untuk 10 orang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pecahan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah proporsi sederhana dengan angka yang mudah disederhanakan adalah materi standar kelas 6. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 97/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000006; applying=0.999994; reasoning=0.000000 | applying | 0.999994 | 0.000072 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.543805; conceptual=0.437879; procedural=0.018316; metacognitive=0.000000 | factual | 0.543805 | 0.552650 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.864137; Medium=0.132503; Hard=0.003360 | Easy | 0.864137 | 0.376050 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999994; −Σp ln(p) = 0.000079; H = 0.000079/ln(3) = 0.000072; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.543805; −Σp ln(p) = 0.766136; H = 0.766136/ln(4) = 0.552650; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.864137; −Σp ln(p) = 0.413133; H = 0.413133/ln(3) = 0.376050; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Konsep Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyu ingin mengundang teman-teman datang ke rumah untuk merayakan ulang tahunnya. Banyu menyiapkan 6 liter minuman untuk 15 orang teman yang datang di pagi hari. Di siang hari, akan datang teman sebanyak 10 orang, berapa liter minuman yang harus disiapkan?
Pilihan: A. 5 liter
B. 6 liter
C. 4 liter
D. 9 liter
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `3f380f04eb5445f529fb5d38`

Apabila kalian menanam 2 bibit tanaman diperlukan 5 gram pupuk. Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?

| Opsi | Isi |
|---|---|
| A | 27,5 gram |
| B | 55 gram |
| C | 14 gram |
| D | 5,5 gram |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rasio pupuk per bibit adalah 5 gram / 2 bibit = 2,5 gram/bibit. Untuk 11 bibit, pupuk yang diperlukan adalah 11 bibit x 2,5 gram/bibit = 27,5 gram.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bd69e39b523fc8e609a2752c299984b84add35e4139b761bd2ba316e5ee6554b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2462 |
| 2 | success | valid / verified | applying | procedural | Medium | 2409 |
| 3 | success | valid / verified | applying | procedural | Medium | 2433 |

Run 1 — solusi: Rasio pupuk per bibit adalah 5 gram / 2 bibit = 2,5 gram/bibit. Untuk 11 bibit, pupuk yang diperlukan adalah 11 bibit x 2,5 gram/bibit = 27,5 gram.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep rasio atau proporsi untuk menyelesaikan masalah kontekstual yang rutin. Siswa perlu mengidentifikasi hubungan proporsional antara jumlah bibit dan pupuk, lalu menerapkan prosedur perkalian/pembagian yang sesuai.. Bukti: Apabila kalian menanam 2 bibit tanaman diperlukan 5 gram pupuk. Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep rasio (proporsi) dan penggunaan algoritma perkalian/pembagian untuk menemukan nilai yang tidak diketahui dalam konteks yang sudah dipelajari.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya rutin (proporsi), siswa harus melakukan dua langkah: menentukan nilai satuan (atau faktor skala) dan mengalikannya dengan jumlah baru. Tidak ada bantuan langkah eksplisit, sehingga siswa harus memilih strategi sendiri.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; 11 bibit tanaman

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar rasio, perkalian dan pembagian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari rasio dan proporsi. Soal ini menuntut pemahaman hubungan proporsional yang merupakan standar kompetensi kelas 6, dengan beban hitung desimal yang sesuai. |

Run 2 — solusi: Rasio bibit terhadap pupuk adalah 2:5. Untuk 11 bibit, pupuk yang diperlukan adalah (11/2) * 5 = 5,5 * 5 = 27,5 gram.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menyelesaikan masalah proporsi yang tidak memiliki faktor pengali bilangan bulat sederhana (11/2 = 5,5). Ini adalah penerapan prosedur rutin dalam konteks proporsi.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritme atau metode proporsi (rasio senilai) untuk menemukan nilai yang tidak diketahui.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan konsep rasio yang memerlukan pemahaman hubungan proporsional. Meskipun prosedurnya rutin, faktor pengalinya (5,5) tidak bulat, yang meningkatkan tuntutan kognitif dibandingkan soal rasio dengan faktor pengali bilangan bulat sederhana.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, pecahan, dan perkalian desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, soal proporsi dengan hasil desimal menuntut ketelitian lebih tinggi daripada soal dengan hasil bulat, namun tetap merupakan prosedur standar yang diajarkan. |

Run 3 — solusi: Rasio bibit terhadap pupuk adalah 2:5. Untuk 11 bibit, pupuk yang diperlukan adalah (11/2) * 5 = 5,5 * 5 = 27,5 gram.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menyelesaikan masalah proporsi sederhana. Ini adalah penerapan prosedur rutin dalam konteks yang familiar.. Bukti: Apabila kalian menanam 2 bibit tanaman diperlukan 5 gram pupuk. Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep) dan penggunaan metode perhitungan rasio (prosedural).. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun konsep rasio adalah materi kelas 6, siswa harus melakukan perpindahan dari rasio dasar (2:5) ke nilai yang tidak bulat (11 bibit), yang memerlukan pemahaman tentang faktor pengali atau penggunaan pecahan/desimal dalam proporsi. Ini sedikit lebih menuntut daripada rasio dengan kelipatan bulat.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, pecahan, dan perkalian/pembagian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, menentukan nilai untuk 11 unit berdasarkan rasio 2 unit memerlukan pemahaman proporsi yang sedikit lebih kompleks daripada sekadar kelipatan bilangan bulat, namun masih dalam cakupan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 78/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.946496; applying=0.053504; reasoning=0.000000 | knowing | 0.946496 | 0.189972 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.570124; conceptual=0.403843; procedural=0.026033; metacognitive=0.000000 | factual | 0.570124 | 0.563739 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.893953; Medium=0.103838; Hard=0.002209 | Easy | 0.893953 | 0.317589 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.946496; −Σp ln(p) = 0.208706; H = 0.208706/ln(3) = 0.189972; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.570124; −Σp ln(p) = 0.781508; H = 0.781508/ln(4) = 0.563739; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.893953; −Σp ln(p) = 0.348908; H = 0.348908/ln(3) = 0.317589; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Konsep Kesamaan Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila kalian menanam 2 bibit tanaman diperlukan 5 gram pupuk. Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
Pilihan: A. 27,5 gram
B. 55 gram
C. 14 gram
D. 5,5 gram
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `d237c5faf543f6df53e2ce02`

Bahan membuat Wedang Jahe<br>untuk 4 liter air:<br>12 Jahe merah ukuran besar, geprek<br>8 batang serai, geprek<br>4 lemon, peras<br>20 cm kayu manis<br>20 cengkeh<br>250 gram gula aren<br><br><br>Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?

| Opsi | Isi |
|---|---|
| A | 48 buah |
| B | 16 buah |
| C | 12 buah |
| D | 24 buah |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air, faktor pengalinya adalah 8/4 = 2. Maka, jumlah jahe yang diperlukan adalah 12 x 2 = 24 buah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad0d0f155a7c29486f16e05f65c3105128804bcf462767e4d1de0fa0cd1583d1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2383 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2441 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2382 |

Run 1 — solusi: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air, faktor pengalinya adalah 8/4 = 2. Maka, jumlah jahe yang diperlukan adalah 12 x 2 = 24 buah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep rasio atau perbandingan senilai untuk menentukan jumlah bahan yang diperlukan dalam konteks rutin (resep minuman). Ini adalah penerapan prosedur proporsi yang familiar.. Bukti: Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua besaran (konsep rasio senilai) dan metode untuk menyelesaikannya.. Bukti: 4 liter air: 12 Jahe merah; 8 liter air
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hubungan antara 4 liter dan 8 liter sangat jelas (kelipatan 2). Siswa hanya perlu melakukan satu langkah perkalian sederhana setelah mengidentifikasi rasio. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: 4 liter air: 12 Jahe merah; 8 liter air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbandingan senilai dan perkalian bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 6, perbandingan senilai dengan faktor pengali bilangan bulat sederhana adalah materi dasar yang rutin. |

Run 2 — solusi: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air, faktor pengalinya adalah 8 / 4 = 2. Maka, jumlah jahe yang diperlukan adalah 12 x 2 = 24 buah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep rasio atau perbandingan senilai dalam konteks rutin. Mereka perlu mengidentifikasi hubungan proporsional antara volume air dan jumlah jahe, lalu menerapkan faktor pengali yang sesuai.. Bukti: 4 liter air: 12 Jahe merah; Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip perbandingan senilai (konsep) dan penggunaan prosedur perkalian untuk menyesuaikan kuantitas berdasarkan rasio yang diberikan.. Bukti: 4 liter air: 12 Jahe merah; Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hubungan antara 4 liter dan 8 liter sangat jelas (kelipatan 2). Siswa hanya perlu melakukan satu langkah perkalian sederhana setelah memahami rasio. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 4 liter air: 12 Jahe merah; 8 liter air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbandingan senilai dan perkalian bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 6, perbandingan senilai dengan angka yang sederhana (kelipatan bilangan bulat) merupakan materi standar yang rutin dan langsung. |

Run 3 — solusi: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air, faktor pengalinya adalah 8/4 = 2. Maka, jumlah jahe yang diperlukan adalah 12 x 2 = 24 buah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep rasio atau perbandingan senilai untuk menentukan jumlah bahan yang diperlukan berdasarkan perubahan volume air. Ini adalah penerapan prosedur proporsi yang rutin.. Bukti: Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep rasio) antara dua variabel (volume air dan jumlah jahe).. Bukti: 4 liter air: 12 Jahe merah; 8 liter air
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hubungan antara 4 liter dan 8 liter sangat jelas (kelipatan 2). Siswa hanya perlu melakukan satu langkah perkalian sederhana setelah mengidentifikasi rasio. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 4 liter air: 12 Jahe merah; 8 liter air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbandingan senilai dan perkalian bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 6, perbandingan senilai dengan faktor pengali bilangan bulat adalah materi dasar yang rutin dan langsung. |

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
| Domain kognitif | knowing=0.008608; applying=0.991392; reasoning=0.000000 | applying | 0.991392 | 0.045058 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.104966; conceptual=0.850546; procedural=0.044488; metacognitive=0.000000 | conceptual | 0.850546 | 0.369879 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.817673; Medium=0.178580; Hard=0.003747 | Easy | 0.817673 | 0.448900 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.991392; −Σp ln(p) = 0.049501; H = 0.049501/ln(3) = 0.045058; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.850546; −Σp ln(p) = 0.512761; H = 0.512761/ln(4) = 0.369879; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.817673; −Σp ln(p) = 0.493167; H = 0.493167/ln(3) = 0.448900; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Konsep Kesamaan Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Bahan membuat Wedang Jahe<br>untuk 4 liter air:<br>12 Jahe merah ukuran besar, geprek<br>8 batang serai, geprek<br>4 lemon, peras<br>20 cm kayu manis<br>20 cengkeh<br>250 gram gula aren<br>

Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
Pilihan: A. 48 buah
B. 16 buah
C. 12 buah
D. 24 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `5ac36027a356e7c09ecd5f9e`

Lalu, Ayah menjelaskan kepada Tigor mengenai waktu panen beberapa tanaman obat seperti pada Tabel 2.7 berikut.<br><br>Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah<br><br>\|Nama Tanaman Obat\|Masa Panen\|<br>\|---\|---\|<br>\|Kumis kucing\|12 minggu\|<br>\|Lengkuas\|1,5 tahun\|<br>\|Jahe merah\|3 bulan\|<br>\|Kencur\|6 bulan\|<br>\|Buah merah\|3 tahun\|<br>\|Kemangi\|30 hari\|<br><br>e. Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

| Opsi | Isi |
|---|---|
| A | Kencur 6 kali dan lengkuas 3 kali |
| B | Kencur 6 kali dan lengkuas 2 kali |
| C | Kencur 2 kali dan lengkuas 2 kali |
| D | Kencur 2 kali dan lengkuas 6 kali |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Lengkuas = 1,5 tahun = 18 bulan. Panen kencur dalam 36 bulan = 36 / 6 = 6 kali. Panen lengkuas dalam 36 bulan = 36 / 18 = 2 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `578ad534bd9ba41aea0b5d68565193bf28291633dd16fdc23a181b6c88756a71`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2493 |
| 2 | success | valid / verified | applying | procedural | Medium | 2575 |
| 3 | success | valid / verified | applying | procedural | Medium | 2520 |

Run 1 — solusi: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Lengkuas = 1,5 tahun = 18 bulan. Panen kencur dalam 36 bulan = 36 / 6 = 6 kali. Panen lengkuas dalam 36 bulan = 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat untuk menyamakan satuan waktu (tahun ke bulan) dan melakukan pembagian untuk menentukan frekuensi panen dalam durasi yang ditentukan. Ini adalah penerapan konsep rasio/perbandingan waktu dalam konteks rutin.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang konversi satuan waktu (tahun ke bulan) dan algoritma pembagian untuk menyelesaikan masalah.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi satuan waktu terlebih dahulu sebelum melakukan operasi pembagian. Siswa harus mengelola beberapa langkah (konversi, lalu pembagian) dan memastikan satuan yang digunakan konsisten (bulan).. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan pembagian bilangan cacah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan konversi satuan waktu dan perbandingan sederhana. Kesulitan terletak pada keharusan menyamakan satuan sebelum menghitung, yang merupakan langkah rutin namun memerlukan ketelitian. |

Run 2 — solusi: Masa panen buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan, maka dalam 36 bulan dapat panen 36/6 = 6 kali. Lengkuas = 1,5 tahun = 18 bulan, maka dalam 36 bulan dapat panen 36/18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi satuan waktu (tahun ke bulan) agar setara, kemudian melakukan pembagian untuk menentukan frekuensi panen dalam periode yang ditentukan. Ini adalah penerapan prosedur matematika pada konteks yang diberikan.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?; Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme konversi satuan waktu dan pembagian untuk memecahkan masalah rasio/frekuensi.. Bukti: Masa panen buah merah = 3 tahun = 36 bulan; Kencur 6 bulan, maka dalam 36 bulan dapat panen 36/6 = 6 kali
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan waktu (tahun ke bulan) sebelum melakukan pembagian. Siswa harus mengelola beberapa informasi dari tabel dan melakukan dua operasi pembagian yang berbeda. Ini adalah tugas rutin dengan beberapa langkah yang saling terkait.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?; Lengkuas 1,5 tahun; Kencur 6 bulan; Buah merah 3 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan pembagian bilangan cacah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu mengonversi satuan waktu dan membandingkan nilai. Kesulitan menengah muncul karena perlunya menyamakan satuan sebelum membagi, yang merupakan langkah rutin namun memerlukan ketelitian dalam mengelola data dari tabel. |

Run 3 — solusi: Masa panen buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan, maka dalam 36 bulan dapat panen 36 / 6 = 6 kali. Lengkuas = 1,5 tahun = 18 bulan, maka dalam 36 bulan dapat panen 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat untuk menyamakan satuan waktu (tahun ke bulan) dan menerapkan operasi pembagian untuk menentukan rasio atau frekuensi panen dalam durasi tertentu. Ini adalah penerapan konsep rasio/perbandingan dalam konteks rutin.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang konversi satuan waktu dan operasi pembagian untuk menyelesaikan masalah perbandingan.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah; Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Intended difficulty `classify/Medium`: Soal ini memerlukan konversi satuan waktu (tahun ke bulan) sebelum melakukan pembagian. Meskipun melibatkan beberapa langkah, prosedurnya familiar bagi siswa kelas 6 dan jalurnya sangat jelas tanpa kendala yang saling berinteraksi secara kompleks.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan waktu (tahun ke bulan) dan operasi pembagian dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari konversi satuan waktu dan perbandingan. Soal ini menuntut ketelitian dalam menyamakan satuan sebelum membagi, yang merupakan standar kompetensi kelas 6. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 176/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000017 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003979; conceptual=0.797322; procedural=0.198699; metacognitive=0.000000 | conceptual | 0.797322 | 0.377751 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.799161; Medium=0.193278; Hard=0.007561 | Easy | 0.799161 | 0.485866 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000019; H = 0.000019/ln(3) = 0.000017; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.797322; −Σp ln(p) = 0.523674; H = 0.523674/ln(4) = 0.377751; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.799161; −Σp ln(p) = 0.533778; H = 0.533778/ln(3) = 0.485866; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
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
Pilihan: A. Kencur 6 kali dan lengkuas 3 kali
B. Kencur 6 kali dan lengkuas 2 kali
C. Kencur 2 kali dan lengkuas 2 kali
D. Kencur 2 kali dan lengkuas 6 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `95f6663d851b5721a9dab809`

Seorang penulis berita dapat mengetik sebanyak 1.200 kata dalam waktu 1 jam.<br><br>b. Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?

| Opsi | Isi |
|---|---|
| A | 0,4 jam |
| B | 2,5 jam |
| C | 2 jam |
| D | 25 menit |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kecepatan mengetik adalah 1.200 kata/jam. Waktu yang diperlukan untuk 3.000 kata adalah 3.000 / 1.200 = 2,5 jam.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a136fdfbde804fc73db7b85715534070bddec0e38b4daba9d84ccb21668389f9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2319 |
| 2 | success | valid / verified | applying | procedural | Easy | 2328 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2339 |

Run 1 — solusi: Kecepatan mengetik adalah 1.200 kata/jam. Waktu yang diperlukan untuk 3.000 kata adalah 3.000 / 1.200 = 2,5 jam.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep rasio atau perbandingan senilai untuk menentukan waktu yang dibutuhkan berdasarkan kecepatan yang diketahui. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Seorang penulis berita dapat mengetik sebanyak 1.200 kata dalam waktu 1 jam.; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan proporsional antara jumlah kata dan waktu (konsep rasio) serta menerapkan algoritma pembagian untuk menyelesaikannya.. Bukti: 1.200 kata dalam waktu 1 jam; 3.000 kata
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep perbandingan senilai. Jalur penyelesaian sangat jelas (membagi total kata dengan kecepatan per jam). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 1.200 kata dalam waktu 1 jam; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian bilangan desimal/pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin perbandingan senilai yang sesuai untuk kelas 6. Tidak ada tuntutan perencanaan tinggi atau integrasi konsep yang kompleks. |

Run 2 — solusi: Kecepatan mengetik adalah 1.200 kata/jam. Waktu yang diperlukan untuk 3.000 kata adalah 3.000 / 1.200 = 2,5 jam.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep rasio atau perbandingan senilai untuk mencari nilai yang belum diketahui dalam konteks rutin.. Bukti: 1.200 kata dalam waktu 1 jam; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip perbandingan senilai (konseptual) untuk menyelesaikan masalah yang memerlukan algoritma pembagian (prosedural).. Bukti: 1.200 kata dalam waktu 1 jam; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep perbandingan senilai. Jalur penyelesaian sangat jelas (membagi total kata dengan kecepatan per jam). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 1.200 kata dalam waktu 1 jam; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian bilangan desimal/pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 6, perbandingan senilai adalah materi standar. Soal ini tidak menuntut perencanaan kompleks atau integrasi konsep, sehingga tergolong mudah. |

Run 3 — solusi: Kecepatan mengetik adalah 1.200 kata/jam. Waktu untuk 3.000 kata = 3.000 kata / 1.200 kata/jam = 2,5 jam.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep rasio atau perbandingan senilai untuk menentukan waktu yang diperlukan berdasarkan kecepatan yang diketahui. Ini adalah penerapan prosedur rutin dalam konteks yang familiar.. Bukti: 1.200 kata dalam waktu 1 jam; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep rasio) dan penggunaan metode pembagian untuk mencari nilai satuan atau faktor pengali.. Bukti: 1.200 kata dalam waktu 1 jam; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari konsep perbandingan senilai yang umum diajarkan di kelas 6. Jalur penyelesaiannya sangat jelas (pembagian sederhana), tidak ada kendala yang berinteraksi, dan tidak memerlukan strategi non-rutin.. Bukti: 1.200 kata dalam waktu 1 jam; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian bilangan cacah/desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar perbandingan senilai yang sesuai dengan kurikulum kelas 6. Tidak ada tuntutan perencanaan tinggi atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3874`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan konsep perbandingan senilai untuk menyelesaikan masalah rutin. Prosedur pembagian sederhana digunakan untuk mencari nilai yang tidak diketahui dalam konteks yang sudah familiar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep rasio) dan penggunaan algoritma pembagian untuk mencari nilai yang dicari.
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung dari konsep perbandingan senilai. Jalur penyelesaian sangat jelas (membagi total kata dengan kecepatan per jam). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian bilangan desimal/pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin perbandingan senilai yang sesuai untuk kelas 6. Tidak ada tuntutan perencanaan tinggi atau integrasi konsep yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 83/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000706; applying=0.999294; reasoning=0.000000 | applying | 0.999294 | 0.005303 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.641591; conceptual=0.318996; procedural=0.039413; metacognitive=0.000000 | factual | 0.641591 | 0.560247 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.905789; Medium=0.091995; Hard=0.002216 | Easy | 0.905789 | 0.293711 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999294; −Σp ln(p) = 0.005826; H = 0.005826/ln(3) = 0.005303; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.641591; −Σp ln(p) = 0.776667; H = 0.776667/ln(4) = 0.560247; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.905789; −Σp ln(p) = 0.322675; H = 0.322675/ln(3) = 0.293711; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Penerapan Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang penulis berita dapat mengetik sebanyak 1.200 kata dalam waktu 1 jam.

b. Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
Pilihan: A. 0,4 jam
B. 2,5 jam
C. 2 jam
D. 25 menit
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `3bf9372d09368f5209865eb3`

Tentukan cara menyusun kubus untuk membentuk bangun berikut. Berapa kubus yang diperlukan?

| Opsi | Isi |
|---|---|
| A | 6 kubus |
| B | 4 kubus |
| C | 5 kubus |
| D | 3 kubus |

![Gambar sumber soal 14](<../../../images/kelas6_panduan_siswa_kelas6.pdf-0098-07.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bangun tersebut terdiri dari 4 kubus yang terlihat (merah muda, hijau, ungu, kuning). Kubus merah muda berada di posisi yang lebih tinggi, sehingga harus ada kubus penyangga di bawahnya yang tidak terlihat secara langsung. Total kubus = 4 (terlihat) + 1 (tersembunyi) = 5 kubus.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0098-07.png. Transkripsi visual: Gambar menunjukkan susunan kubus isometrik. Terdapat 4 kubus yang terlihat jelas: satu kubus merah muda di atas, satu kubus hijau di kiri atas, satu kubus ungu di kiri bawah, dan satu kubus kuning di kanan bawah. Susunan ini membentuk struktur bertingkat di mana kubus merah muda berada di atas kubus lain yang tidak terlihat sepenuhnya, menunjukkan adanya kubus penyangga di bawahnya.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `482e965c22b889e8b087832f6c478936cc9e3ab32d8ba789425e877faf56944e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 3511 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 3572 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3535 |

Run 1 — solusi: Bangun tersebut terdiri dari 4 kubus yang terlihat (merah muda, hijau, ungu, kuning). Kubus merah muda berada di posisi yang lebih tinggi, sehingga harus ada kubus penyangga di bawahnya yang tidak terlihat secara langsung. Total kubus = 4 (terlihat) + 1 (tersembunyi) = 5 kubus.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan penalaran spasial untuk mengidentifikasi kubus yang tersembunyi berdasarkan struktur visual yang diberikan. Ini bukan sekadar menghitung objek yang tampak, melainkan memahami prinsip struktur 3D.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut. Berapa kubus yang diperlukan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur bangun ruang dan bagaimana objek 3D disusun dalam ruang, melampaui sekadar prosedur menghitung.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan penalaran spasial untuk membayangkan bagian yang tidak terlihat. Meskipun langkahnya sederhana (menambah 1 kubus tersembunyi), siswa harus mampu melakukan inferensi visual yang melampaui apa yang tampak langsung di gambar.. Bukti: Berapa kubus yang diperlukan?; catatan sumber: Benar: selain 4 kubus yang tampak berwarna, ada 1 kubus tersembunyi di bagian belakang yang menopang susunan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan visualisasi objek 3D. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, kemampuan visualisasi spasial adalah bagian dari kurikulum geometri. Menentukan jumlah kubus tersembunyi adalah tugas standar namun memerlukan ketelitian dalam membayangkan struktur internal. |

Run 2 — solusi: Terdapat 4 kubus yang terlihat secara langsung (merah muda, hijau, ungu, kuning). Kubus merah muda berada di posisi yang memerlukan penopang di bawahnya agar struktur tersebut terbentuk, sehingga terdapat 1 kubus tersembunyi. Total kubus = 4 + 1 = 5.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan penalaran spasial untuk mengidentifikasi kubus yang tidak terlihat (tersembunyi) berdasarkan struktur yang tampak. Ini bukan sekadar menghitung objek yang terlihat, melainkan memahami prinsip keterhubungan dan stabilitas struktur kubus.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut; Berapa kubus yang diperlukan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang geometri ruang dan bagaimana objek 3D disusun, melampaui sekadar prosedur menghitung atau fakta visual.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan penalaran spasial untuk membayangkan bagian yang tidak terlihat. Meskipun langkahnya sederhana (menambah 1), siswa harus melakukan inferensi visual yang melampaui informasi eksplisit pada gambar.. Bukti: Berapa kubus yang diperlukan?; catatan sumber: Benar: selain 4 kubus yang tampak berwarna, ada 1 kubus tersembunyi di bagian belakang yang menopang susunan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan perspektif isometrik. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan visualisasi spasial sederhana. Menghitung kubus tersembunyi adalah tugas standar untuk level ini, namun memerlukan ketelitian lebih daripada sekadar menghitung objek yang tampak. |

Run 3 — solusi: Terdapat 4 kubus yang terlihat jelas (merah muda, hijau, ungu, kuning). Kubus merah muda berada di posisi atas, yang secara logis memerlukan kubus penyangga di bawahnya yang tidak terlihat dari sudut pandang ini. Jadi, total kubus adalah 4 (terlihat) + 1 (tersembunyi) = 5 kubus.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan penalaran spasial untuk membayangkan struktur 3D yang tidak terlihat sepenuhnya (kubus tersembunyi) berdasarkan representasi visual yang diberikan. Ini melampaui sekadar mengingat atau menerapkan prosedur rutin, karena siswa harus menyimpulkan keberadaan elemen yang tidak tampak.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut. Berapa kubus yang diperlukan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur ruang dan bagaimana objek 3D disusun, bukan sekadar menghafal fakta atau mengikuti algoritme prosedural.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan penalaran spasial untuk mengidentifikasi bagian yang tidak terlihat. Meskipun langkahnya tidak banyak, siswa harus melakukan perpindahan representasi mental dari 2D ke 3D untuk menyimpulkan keberadaan kubus tersembunyi. Ini bukan sekadar menghitung objek yang tampak.. Bukti: Berapa kubus yang diperlukan?; catatan sumber: Benar: selain 4 kubus yang tampak berwarna, ada 1 kubus tersembunyi di bagian belakang yang menopang susunan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan visualisasi 3D. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan visualisasi spasial sederhana. Menghitung kubus yang tersembunyi adalah tugas standar untuk menguji pemahaman struktur ruang pada level ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 136/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000105; applying=0.999895; reasoning=0.000000 | applying | 0.999895 | 0.000968 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.195893; conceptual=0.800128; procedural=0.003979; metacognitive=0.000000 | conceptual | 0.800128 | 0.374921 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.755494; Medium=0.240403; Hard=0.004103 | Easy | 0.755494 | 0.525262 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999895; −Σp ln(p) = 0.001064; H = 0.001064/ln(3) = 0.000968; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.800128; −Σp ln(p) = 0.519750; H = 0.519750/ln(4) = 0.374921; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.755494; −Σp ln(p) = 0.577059; H = 0.577059/ln(3) = 0.525262; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Mengonstruksi dan Mengurai
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan cara menyusun kubus untuk membentuk bangun berikut. Berapa kubus yang diperlukan?
Pilihan: A. 6 kubus
B. 4 kubus
C. 5 kubus
D. 3 kubus
Transkripsi visual: Gambar menunjukkan susunan kubus isometrik. Terdapat 4 kubus yang terlihat jelas: satu kubus merah muda di atas, satu kubus hijau di kiri atas, satu kubus ungu di kiri bawah, dan satu kubus kuning di kanan bawah. Susunan ini membentuk struktur bertingkat di mana kubus merah muda berada di atas kubus lain yang tidak terlihat sepenuhnya, menunjukkan adanya kubus penyangga di bawahnya.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `8cc6d500c8e22d188c498acf`

Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?

| Opsi | Isi |
|---|---|
| A | 4 balok |
| B | 2 balok |
| C | 3 balok |
| D | 1 balok |

![Gambar sumber soal 15](<../../../images/kelas6_panduan_siswa_kelas6.pdf-0098-00.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Mengamati gambar, terdapat tiga lapisan balok yang disusun secara vertikal. Menghitung jumlah lapisan tersebut memberikan total 3 balok.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0098-00.png. Transkripsi visual: Gambar menunjukkan sebuah bangun ruang yang terdiri dari tiga balok identik yang disusun secara vertikal (bertumpuk) membentuk satu menara.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3fb41942528a2363a3163e5421596f204c419081080eb4fc37ad07d45a7d872b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3313 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3402 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3345 |

Run 1 — solusi: Mengamati gambar, terdapat tiga lapisan balok yang disusun secara vertikal. Menghitung jumlah lapisan tersebut memberikan total 3 balok.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menghitung jumlah objek (balok) yang terlihat secara langsung dalam sebuah representasi visual sederhana. Ini adalah tugas pengenalan visual dasar yang tidak memerlukan prosedur kompleks atau penalaran strategis.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep objek fisik sebagai unit penyusun bangun ruang (konseptual) dan melakukan penghitungan sederhana (faktual/prosedural dasar).. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana. Siswa hanya perlu menghitung jumlah balok yang terlihat secara eksplisit dalam tumpukan. Tidak ada kendala tersembunyi atau langkah yang saling bergantung.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 6, tugas menghitung objek visual sederhana ini berada di bawah tingkat kompetensi rata-rata, sehingga dikategorikan mudah. |

Run 2 — solusi: Mengamati gambar, terdapat tiga lapisan balok yang ditumpuk secara vertikal. Dengan menghitung jumlah lapisan tersebut, diperoleh total 3 balok.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menghitung jumlah komponen (balok) yang menyusun bangun ruang tersebut. Ini adalah tugas pengenalan visual langsung yang tidak memerlukan strategi kompleks atau penalaran mendalam, sehingga masuk dalam domain knowing.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?; gambar menunjukkan tiga balok identik yang ditumpuk vertikal
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dasar bangun ruang dan bagaimana objek-objek tersebut disusun atau dikomposisikan. Ini melibatkan pemahaman konseptual tentang struktur objek.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana. Siswa hanya perlu melakukan observasi visual langsung untuk menghitung jumlah balok yang terlihat. Tidak ada langkah-langkah yang saling bergantung, tidak ada strategi yang perlu dipilih, dan beban kognitifnya sangat rendah.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?; gambar menunjukkan tiga balok identik yang ditumpuk vertikal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan dasar menghitung objek visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 6, tugas menghitung objek visual sederhana seperti ini sangat mudah dan merupakan keterampilan dasar yang sudah dikuasai jauh sebelum kelas 6. |

Run 3 — solusi: Mengamati gambar, terdapat tiga lapisan balok yang ditumpuk secara vertikal. Dengan menghitung jumlah lapisan tersebut, diperoleh total 3 balok.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menghitung jumlah komponen (balok) yang menyusun bangun ruang tersebut. Ini adalah tugas pengenalan visual langsung yang tidak memerlukan prosedur kompleks atau penalaran non-rutin.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dasar bangun ruang dan bagaimana objek-objek tersebut disusun (diurai) menjadi komponen-komponen penyusunnya.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana. Siswa hanya perlu melakukan observasi visual langsung untuk menghitung jumlah balok yang terlihat jelas dalam tumpukan. Tidak ada langkah perencanaan, strategi, atau kendala yang harus dipecahkan.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan dasar menghitung objek visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 6, tugas menghitung objek visual sederhana ini sangat mudah dan merupakan keterampilan dasar yang sudah dikuasai jauh sebelum kelas 6. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 84/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.217998; applying=0.782002; reasoning=0.000000 | applying | 0.782002 | 0.477295 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.647104; conceptual=0.344516; procedural=0.008380; metacognitive=0.000000 | factual | 0.647104 | 0.496896 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.882149; Medium=0.115801; Hard=0.002050 | Easy | 0.882149 | 0.339482 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.782002; −Σp ln(p) = 0.524362; H = 0.524362/ln(3) = 0.477295; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.647104; −Σp ln(p) = 0.688844; H = 0.688844/ln(4) = 0.496896; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.882149; −Σp ln(p) = 0.372959; H = 0.372959/ln(3) = 0.339482; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Mengonstruksi dan Mengurai
Tipe soal: multiple_choice
Stimulus: -
Soal: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
Pilihan: A. 4 balok
B. 2 balok
C. 3 balok
D. 1 balok
Transkripsi visual: Gambar menunjukkan sebuah bangun ruang yang terdiri dari tiga balok identik yang disusun secara vertikal (bertumpuk) membentuk satu menara.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `b56626ecf5289108fa7302f7`

Berikut adalah sebuah dadu. Gambar berikut adalah dadu yang sama yang dilihat dari arah berbeda.<br><br>Jika mata dadu pada dua sisi yang berlawanan berjumlah 7, ada berapa mata dadu pada sisi yang kosong?

| Opsi | Isi |
|---|---|
| A | 3 mata dadu |
| B | 4 mata dadu |
| C | 1 mata dadu |
| D | 2 mata dadu |

![Gambar sumber soal 16](<../../../images/kelas6_panduan_siswa_kelas6.pdf-0104-02.png>)


![Gambar sumber soal 16](<../../../images/kelas6_panduan_siswa_kelas6.pdf-0104-06.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Dadu standar memiliki sisi 1-6. Diketahui sisi berlawanan berjumlah 7. Dari gambar, sisi yang terlihat adalah 4, 5, dan 6. Sisi yang berlawanan dengan 4 adalah 3, dengan 5 adalah 2, dan dengan 6 adalah 1. Sisi yang kosong pada gambar 2 adalah sisi yang berlawanan dengan 4, yaitu 3.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0104-02.png, images/kelas6_panduan_siswa_kelas6.pdf-0104-06.png. Transkripsi visual: Dua gambar dadu ditampilkan. Gambar 1 menunjukkan sisi atas (6), sisi depan (4), dan sisi samping (5). Gambar 2 menunjukkan sisi atas (6), sisi depan (5), dan sisi samping (kosong). Aturan dadu standar: jumlah sisi berlawanan adalah 7.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b8c5e91fb5ab22ebf301672c5dbf50916b1296aea7665ffb569991072f34bfb9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 4621 |
| 2 | success | valid / verified | applying | conceptual | Medium | 4798 |
| 3 | success | valid / verified | applying | conceptual | Medium | 4688 |

Run 1 — solusi: Dadu standar memiliki sisi 1-6. Diketahui sisi berlawanan berjumlah 7. Dari gambar, sisi yang terlihat adalah 4, 5, dan 6. Sisi yang berlawanan dengan 4 adalah 3, dengan 5 adalah 2, dan dengan 6 adalah 1. Sisi yang kosong pada gambar 2 adalah sisi yang berlawanan dengan 4, yaitu 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan dadu standar (jumlah sisi berlawanan adalah 7) untuk mengidentifikasi sisi yang tidak terlihat. Ini adalah penerapan konsep pada konteks rutin (dadu).. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7; ada berapa mata dadu pada sisi yang kosong?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau aturan dadu standar (jumlah sisi berlawanan adalah 7), yang merupakan pengetahuan konseptual.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7
- Intended difficulty `classify/Medium`: Soal ini memerlukan visualisasi spasial dasar dan penerapan aturan dadu. Siswa perlu mengidentifikasi sisi yang terlihat (4, 5, 6) dan menggunakan aturan jumlah 7 untuk menentukan sisi yang tersembunyi. Jalur penyelesaian jelas dan rutin bagi siswa kelas 6.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7; ada berapa mata dadu pada sisi yang kosong?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang dadu dan operasi penjumlahan/pengurangan sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan penalaran spasial sederhana dan menerapkan aturan yang diberikan dalam soal. |

Run 2 — solusi: Dadu standar memiliki angka 1 sampai 6. Sisi yang terlihat pada gambar adalah 4, 5, dan 6. Pasangan sisi berlawanan berjumlah 7, maka: 6 berlawanan dengan 1, 5 berlawanan dengan 2, dan 4 berlawanan dengan 3. Karena 1, 2, 4, 5, dan 6 sudah teridentifikasi, maka sisi yang tersisa adalah 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep sifat dadu standar (jumlah sisi berlawanan adalah 7) untuk mengidentifikasi angka yang hilang dari himpunan {1, 2, 3, 4, 5, 6}. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7; ada berapa mata dadu pada sisi yang kosong?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau aturan dadu standar (jumlah sisi berlawanan adalah 7), yang merupakan pengetahuan konseptual.. Bukti: mata dadu pada dua sisi yang berlawanan berjumlah 7
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan integrasi antara pengamatan visual (angka yang sudah terlihat) dan penerapan aturan konseptual (jumlah sisi berlawanan adalah 7) untuk menyimpulkan angka yang belum terlihat. Meskipun prosedurnya sederhana, siswa harus mengorganisir informasi yang ada.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7; ada berapa mata dadu pada sisi yang kosong?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang dadu standar dan operasi penjumlahan/pengurangan sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan penalaran spasial dasar dan deduksi sederhana berdasarkan aturan yang diberikan. |

Run 3 — solusi: Dadu standar memiliki angka 1 sampai 6. Sisi yang terlihat pada kedua gambar adalah 4, 5, dan 6. Sisi yang belum terlihat adalah 1, 2, dan 3. Karena aturan dadu standar adalah sisi berlawanan berjumlah 7, maka pasangan yang sudah terlihat adalah (6,1), (5,2), dan (4,3). Karena 6, 5, dan 4 sudah terlihat, maka pasangan yang tersisa untuk sisi yang belum terlihat adalah 1, 2, dan 3. Sisi kosong pada gambar 2 adalah sisi yang belum terlihat. Berdasarkan posisi, sisi kosong tersebut adalah 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan dadu standar (jumlah sisi berlawanan adalah 7) dan mengintegrasikan informasi visual dari dua orientasi dadu yang berbeda untuk mengidentifikasi sisi yang belum terlihat.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7; ada berapa mata dadu pada sisi yang kosong?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur dadu standar dan hubungan antar sisi.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7
- Intended difficulty `classify/Medium`: Soal ini memerlukan visualisasi spasial untuk menghubungkan dua orientasi dadu. Siswa harus mengidentifikasi sisi yang sudah terlihat (4, 5, 6) dan menyimpulkan sisi yang belum terlihat (1, 2, 3) berdasarkan aturan jumlah 7. Ini melibatkan beberapa langkah logis yang saling terkait.. Bukti: Gambar berikut adalah dadu yang sama yang dilihat dari arah berbeda.; Jika mata dadu pada dua sisi yang berlawanan berjumlah 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang dadu standar dan konsep penjumlahan hingga 7. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan penalaran spasial sederhana dan menerapkan aturan yang diberikan pada objek konkret seperti dadu. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 150/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000270; applying=0.999730; reasoning=0.000000 | applying | 0.999730 | 0.002263 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004490; conceptual=0.992756; procedural=0.002754; metacognitive=0.000000 | conceptual | 0.992756 | 0.034425 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.629905; Medium=0.363765; Hard=0.006329 | Easy | 0.629905 | 0.629005 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999730; −Σp ln(p) = 0.002486; H = 0.002486/ln(3) = 0.002263; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.992756; −Σp ln(p) = 0.047723; H = 0.047723/ln(4) = 0.034425; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.629905; −Σp ln(p) = 0.691032; H = 0.691032/ln(3) = 0.629005; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Visualisasi Spasial
Tipe soal: multiple_choice
Stimulus: -
Soal: Berikut adalah sebuah dadu. Gambar berikut adalah dadu yang sama yang dilihat dari arah berbeda.

Jika mata dadu pada dua sisi yang berlawanan berjumlah 7, ada berapa mata dadu pada sisi yang kosong?
Pilihan: A. 3 mata dadu
B. 4 mata dadu
C. 1 mata dadu
D. 2 mata dadu
Transkripsi visual: Dua gambar dadu ditampilkan. Gambar 1 menunjukkan sisi atas (6), sisi depan (4), dan sisi samping (5). Gambar 2 menunjukkan sisi atas (6), sisi depan (5), dan sisi samping (kosong). Aturan dadu standar: jumlah sisi berlawanan adalah 7.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `e81a665e38e1781b745677fd`

Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.<br><br>Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

| Opsi | Isi |
|---|---|
| A | 2 kali |
| B | 3 kali |
| C | 5 kali |
| D | 4 kali |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Posisi awal (F,1) ke (D,2). Perubahan horizontal: F ke D adalah 2 langkah (F-E, E-D). Perubahan vertikal: 1 ke 2 adalah 1 langkah. Total rebahan = 2 + 1 = 3 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e0fbcb41949a8b511d43acbdba9e4119e5f834bdcf47a80ec0c63ea69f2743e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2439 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2436 |
| 3 | success | valid / verified | applying | procedural | Medium | 2444 |

Run 1 — solusi: Posisi awal (F,1) ke (D,2). Perubahan horizontal: F ke D adalah 2 langkah (F-E, E-D). Perubahan vertikal: 1 ke 2 adalah 1 langkah. Total rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada bidang koordinat dan menerjemahkan jarak antar titik menjadi jumlah langkah (rebahan) kubus. Ini melibatkan penerapan konsep jarak pada konteks rutin pergerakan objek.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya.
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip dasar sistem koordinat dan pemahaman spasial tentang pergerakan objek (kubus) untuk menentukan jumlah langkah yang diperlukan.. Bukti: jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman spasial untuk mengintegrasikan dua dimensi pergerakan (horizontal dan vertikal) secara bersamaan. Siswa harus menghitung selisih langkah pada sumbu X dan sumbu Y, lalu menjumlahkannya. Meskipun prosedurnya rutin, siswa perlu melakukan perencanaan langkah yang saling terkait (dua langkah horizontal dan satu langkah vertikal) tanpa bantuan visual langsung.. Bukti: Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius dan konsep jarak antar titik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari koordinat. Tantangan terletak pada visualisasi pergerakan objek 3D (kubus) di atas grid 2D, yang menuntut integrasi dua arah pergerakan. |

Run 2 — solusi: Posisi awal (F,1) ke posisi akhir (D,2). Perubahan horizontal: F ke D adalah 2 langkah (F-E, E-D). Perubahan vertikal: 1 ke 2 adalah 1 langkah. Total rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada bidang koordinat dan menerjemahkan jarak antar koordinat menjadi jumlah langkah (rebahan) kubus. Ini adalah penerapan konsep jarak pada grid ke dalam konteks pergerakan objek.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip dasar sistem koordinat dan pemahaman spasial tentang pergerakan objek (kubus) pada grid untuk menyelesaikan masalah.. Bukti: sistem berpetak yang digunakan; Berapa kali kubus tersebut direbahkan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman spasial untuk memisahkan pergerakan horizontal dan vertikal pada grid. Siswa harus menentukan selisih posisi (F ke D dan 1 ke 2) dan menjumlahkannya. Meskipun prosedurnya rutin, siswa perlu mengintegrasikan dua dimensi pergerakan tersebut.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid dan konsep jarak antar titik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari koordinat. Tantangan terletak pada visualisasi pergerakan kubus di grid, namun langkah penyelesaiannya cukup jelas dan terstruktur. |

Run 3 — solusi: Posisi awal (F,1) ke posisi akhir (D,2). Perubahan horizontal: F ke D adalah 2 langkah (F->E->D). Perubahan vertikal: 1 ke 2 adalah 1 langkah. Total langkah rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep jarak pada sistem koordinat petak ke dalam konteks pergerakan fisik (rebahan kubus). Ini melibatkan pemilihan prosedur yang tepat untuk menghitung total langkah perpindahan, yang merupakan penerapan konsep dasar dalam situasi rutin.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang cara menghitung jarak pada grid (selisih koordinat) dan menerapkannya pada konteks pergerakan objek.. Bukti: Sistem berpetak yang digunakan.; Berapa kali kubus tersebut direbahkan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman tentang sistem koordinat dan translasi sederhana. Siswa harus mengintegrasikan dua dimensi pergerakan (horizontal dan vertikal) untuk mendapatkan jawaban total. Meskipun prosedurnya rutin, siswa perlu menyadari bahwa pergerakan pada grid 2D memerlukan penjumlahan langkah dari kedua sumbu.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid dan konsep jarak antar titik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari sistem koordinat. Soal ini menuntut pemahaman spasial sederhana untuk menghitung langkah total, yang sesuai dengan tingkat kemampuan kelas 6. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4209`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep jarak pada sistem koordinat petak ke dalam konteks pergerakan fisik (rebahan kubus). Ini melibatkan pemilihan prosedur yang tepat untuk menghitung total langkah perpindahan, yang merupakan penerapan konsep dasar dalam situasi rutin.
- Dimensi pengetahuan `procedural`: Siswa menggunakan pengetahuan prosedural tentang cara menghitung jarak pada grid (selisih koordinat) dan menerapkannya pada konteks pergerakan objek.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman spasial untuk mengintegrasikan dua dimensi pergerakan (horizontal dan vertikal) secara bersamaan. Siswa harus menghitung selisih langkah pada sumbu X dan sumbu Y, lalu menjumlahkannya. Meskipun prosedurnya rutin, siswa perlu melakukan perencanaan langkah yang saling terkait (dua langkah horizontal dan satu langkah vertikal) tanpa bantuan visual langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius dan konsep jarak antar titik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari koordinat. Tantangan terletak pada visualisasi pergerakan objek 3D (kubus) di atas grid 2D, yang menuntut integrasi dua arah pergerakan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 121/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001699; applying=0.998301; reasoning=0.000000 | applying | 0.998301 | 0.011410 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.163005; conceptual=0.807597; procedural=0.029398; metacognitive=0.000000 | conceptual | 0.807597 | 0.412572 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.789152; Medium=0.208113; Hard=0.002735 | Easy | 0.789152 | 0.482136 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998301; −Σp ln(p) = 0.012535; H = 0.012535/ln(3) = 0.011410; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.807597; −Σp ln(p) = 0.571946; H = 0.571946/ln(4) = 0.412572; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.789152; −Σp ln(p) = 0.529681; H = 0.529681/ln(3) = 0.482136; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Lokasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.

Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
Pilihan: A. 2 kali
B. 3 kali
C. 5 kali
D. 4 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `487c5870a0b95ed9a10da20f`

Jika diketahui titik awal dan titik akhir, dapat ditentukan jalur yang dapat ditempuh. Dengan sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun.<br><br>Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)

| Opsi | Isi |
|---|---|
| A | 2 langkah ke kanan dan 3 langkah ke bawah |
| B | 3 langkah ke kanan dan 3 langkah ke bawah |
| C | 2 langkah ke kiri dan 3 langkah ke atas |
| D | 3 langkah ke kanan dan 2 langkah ke bawah |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jarak horizontal dari B ke D adalah selisih posisi kolom: D - B = 2 langkah ke kanan. Jarak vertikal dari 6 ke 3 adalah selisih posisi baris: 6 - 3 = 3 langkah ke bawah. Jadi, 2 langkah ke kanan dan 3 langkah ke bawah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `78500c7626bae92958fe0af573eeafd52b7928b8714f3f22bdc9f2680324f26e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2323 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2324 |
| 3 | success | valid / verified | applying | procedural | Easy | 2312 |

Run 1 — solusi: Jarak horizontal dari B ke D adalah 2 langkah (B ke C, C ke D). Jarak vertikal dari 6 ke 3 adalah 6 - 3 = 3 langkah ke bawah. Jadi, 2 langkah ke kanan dan 3 langkah ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur dasar menentukan selisih posisi pada sistem koordinat petak. Ini adalah penerapan konsep lokasi yang rutin.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung jarak pada sistem koordinat petak.. Bukti: Dengan sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung selisih urutan huruf (B ke D) dan selisih angka (6 ke 3). Tidak ada kendala kompleks atau integrasi langkah yang sulit.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat petak dan urutan abjad/angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi koordinat adalah dasar kelas 6. Soal ini hanya meminta penghitungan selisih sederhana tanpa jebakan atau langkah tambahan. |

Run 2 — solusi: Jarak horizontal dari B ke D adalah selisih posisi kolom: D - B = 4 - 2 = 2 langkah ke kanan. Jarak vertikal dari 6 ke 3 adalah selisih posisi baris: 6 - 3 = 3 langkah ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur dasar untuk menentukan jarak pada sistem koordinat/petak dengan menghitung selisih posisi horizontal dan vertikal. Ini adalah penerapan konsep lokasi yang rutin.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip sistem koordinat sederhana (jarak antar titik pada grid), yang merupakan pengetahuan konseptual.. Bukti: Dengan sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung selisih posisi huruf (B ke D) dan angka (6 ke 3). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat/petak dan urutan abjad/angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi koordinat dasar adalah standar kelas 6. Soal ini tidak menuntut perencanaan kompleks, hanya pemahaman posisi pada grid. |

Run 3 — solusi: Jarak horizontal dari B ke D adalah 2 langkah (B ke C, C ke D). Jarak vertikal dari 6 ke 3 adalah 6 - 3 = 3 langkah ke bawah. Jadi, 2 langkah ke kanan dan 3 langkah ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman sistem koordinat sederhana untuk menentukan perpindahan horizontal dan vertikal. Ini adalah penerapan prosedur rutin pada konteks yang sudah dikenal.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung selisih koordinat pada sistem petak.. Bukti: Dengan sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung selisih posisi huruf (B ke D) dan angka (6 ke 3). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar urutan abjad dan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi koordinat sederhana adalah standar kelas 6. Soal ini tidak menuntut perencanaan kompleks, hanya pemahaman dasar tentang jarak pada grid. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3810`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur rutin untuk menentukan selisih posisi pada sistem koordinat petak. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung jarak atau selisih pada sistem koordinat petak.
- Intended difficulty `Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu menghitung selisih urutan huruf dan angka. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan langkah yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat petak dan urutan abjad/angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi koordinat adalah dasar kelas 6. Soal ini hanya meminta penghitungan selisih sederhana tanpa jebakan atau langkah tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 128/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.029817; applying=0.970183; reasoning=0.000000 | applying | 0.970183 | 0.122068 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.016190; conceptual=0.962766; procedural=0.021044; metacognitive=0.000000 | conceptual | 0.962766 | 0.133120 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.718132; Medium=0.275798; Hard=0.006070 | Easy | 0.718132 | 0.568000 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.970183; −Σp ln(p) = 0.134105; H = 0.134105/ln(3) = 0.122068; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.962766; −Σp ln(p) = 0.184544; H = 0.184544/ln(4) = 0.133120; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.718132; −Σp ln(p) = 0.624012; H = 0.624012/ln(3) = 0.568000; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Lokasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika diketahui titik awal dan titik akhir, dapat ditentukan jalur yang dapat ditempuh. Dengan sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun.

Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)
Pilihan: A. 2 langkah ke kanan dan 3 langkah ke bawah
B. 3 langkah ke kanan dan 3 langkah ke bawah
C. 2 langkah ke kiri dan 3 langkah ke atas
D. 3 langkah ke kanan dan 2 langkah ke bawah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `c5e424e9914591b1d5286ef0`

Amati setiap pola berikut. Lanjutkan polanya dengan melingkari gambar berikutnya.<br><br>Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.

| Opsi | Isi |
|---|---|
| A | heksagon |
| B | kupu-kupu |
| C | bunga |
| D | kelinci |

![Gambar sumber soal 19](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola pada baris b adalah pengulangan tiga gambar: {kupu-kupu, kelinci, kelinci}. Urutan yang diberikan adalah (kupu-kupu, kelinci, kelinci), (kupu-kupu, kelinci, kelinci), (kupu-kupu, ...). Maka gambar selanjutnya adalah kelinci.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Baris b menampilkan urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Pola ini berulang setiap tiga elemen: {kupu-kupu, kelinci, kelinci}. Setelah kupu-kupu terakhir, elemen berikutnya dalam urutan adalah kelinci.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2f7eb9c6b0216ef537f19eadffb024b53bc8175d300350f1c3b14aa56fe597f5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3555 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3540 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3511 |

Run 1 — solusi: Pola pada baris b adalah pengulangan tiga gambar: kupu-kupu, kelinci, kelinci. Urutan yang diberikan adalah: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Karena pola berulang setiap tiga gambar, setelah kupu-kupu, gambar berikutnya adalah kelinci.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan melanjutkan pola berulang sederhana. Ini adalah tugas pengenalan pola dasar yang memerlukan penerapan prosedur pengamatan langsung tanpa perlu strategi nonrutin atau penalaran kompleks.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya.; b. kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan pengetahuan konseptual dasar tentang keteraturan dalam urutan.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena pola berulang (kupu-kupu, kelinci, kelinci) sangat jelas dan langsung terlihat. Tidak ada langkah yang saling bergantung atau kendala yang harus diintegrasikan.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya.; b. kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu

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
| distractorQuality | weak |
| gradeRelativeRationale | Tugas ini jauh di bawah tingkat kognitif yang diharapkan untuk kelas 6, karena pola visual berulang adalah materi dasar yang biasanya diajarkan di kelas awal SD. |

Run 2 — solusi: Pola pada baris b adalah pengulangan tiga gambar: {kupu-kupu, kelinci, kelinci}. Urutan yang diberikan adalah (kupu-kupu, kelinci, kelinci), (kupu-kupu, kelinci, kelinci), (kupu-kupu, ...). Maka gambar selanjutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengulangan dalam urutan visual dan menerapkannya untuk menentukan elemen berikutnya. Ini adalah tugas pengenalan pola dasar yang melibatkan penerapan prosedur pengenalan urutan rutin.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya.; b. kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan prinsip dasar dalam matematika awal.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana untuk siswa kelas 6. Pola berulang tiga elemen sangat jelas dan familiar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategis yang kompleks.. Bukti: b. kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu

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
| gradeRelativeRationale | Meskipun soal ini secara teknis ditujukan untuk tingkat yang lebih rendah (biasanya kelas 1-2), untuk kelas 6 ini dikategorikan sangat mudah karena tidak menuntut kemampuan matematika tingkat lanjut. |

Run 3 — solusi: Pola baris b berulang setiap tiga gambar: kupu-kupu, kelinci, kelinci. Urutan yang diberikan adalah (kupu-kupu, kelinci, kelinci), (kupu-kupu, kelinci, kelinci), kupu-kupu. Maka gambar berikutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengulangan dalam urutan visual dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan prosedur pengenalan pola yang rutin.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya.; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pola berulang (konseptual) dan penerapan metode untuk melanjutkannya (prosedural).. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana untuk siswa kelas 6. Pola pengulangan tiga elemen sangat jelas dan tidak memerlukan perencanaan kompleks atau integrasi kendala yang sulit.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya.; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan ini sangat rendah untuk kelas 6, karena pola visual berulang adalah materi dasar yang biasanya sudah dikuasai jauh sebelum kelas 6. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5120`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk mengidentifikasi aturan pengulangan dalam urutan visual dan menerapkannya untuk menentukan elemen berikutnya. Ini adalah tugas pengenalan pola dasar yang melibatkan penerapan prosedur pengenalan urutan rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan pengetahuan konseptual dasar tentang keteraturan dalam urutan.
- Intended difficulty `Easy`: Soal ini sangat sederhana untuk siswa kelas 6. Pola berulang tiga elemen sangat jelas dan familiar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategis yang kompleks.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Meskipun soal ini secara teknis ditujukan untuk tingkat yang lebih rendah (biasanya kelas 1-2), untuk kelas 6 ini dikategorikan sangat mudah karena tidak menuntut kemampuan matematika tingkat lanjut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 147/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000003; applying=0.999997; reasoning=0.000000 | applying | 0.999997 | 0.000035 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004045; conceptual=0.994083; procedural=0.001872; metacognitive=0.000000 | conceptual | 0.994083 | 0.028813 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.675565; Medium=0.315835; Hard=0.008600 | Easy | 0.675565 | 0.609743 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999997; −Σp ln(p) = 0.000039; H = 0.000039/ln(3) = 0.000035; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.994083; −Σp ln(p) = 0.039944; H = 0.039944/ln(4) = 0.028813; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.675565; −Σp ln(p) = 0.669872; H = 0.669872/ln(3) = 0.609743; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Pola
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati setiap pola berikut. Lanjutkan polanya dengan melingkari gambar berikutnya.

Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.
Pilihan: A. heksagon
B. kupu-kupu
C. bunga
D. kelinci
Transkripsi visual: Baris b menampilkan urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Pola ini berulang setiap tiga elemen: {kupu-kupu, kelinci, kelinci}. Setelah kupu-kupu terakhir, elemen berikutnya dalam urutan adalah kelinci.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `8fe432cf4c0a120aab6def21`

\|**No**\|**Nama Bangun Datar**\|**Gambar**\|**Banyaknya**\|<br>\|---\|---\|---\|---\|<br>\|1<br>2\|Segitiga<br>...\|...\|...<br>...\|<br><br>Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :

| Opsi | Isi |
|---|---|
| A | Segitiga 5, trapesium 1, persegi 1 |
| B | Segitiga 6, persegi 1 |
| C | Segitiga 5, jajargenjang 1, persegi 1 |
| D | Segitiga 4, jajargenjang 1, persegi 1 |

![Gambar sumber soal 20](<../../../images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Identifikasi visual kepingan: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total: 5 segitiga, 1 persegi, 1 jajargenjang. Sesuai dengan opsi C.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png. Transkripsi visual: Gambar menunjukkan sebuah perahu yang tersusun dari 7 keping bangun datar berwarna: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua, 1 persegi hijau muda, 1 segitiga oranye, 1 jajargenjang kuning, dan 1 segitiga merah muda. Total kepingan: 5 segitiga, 1 persegi, 1 jajargenjang.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4a34d54f21bcc01e61fe7be3c6e5db05fdfe0ee4b55e14553f57ae3389880de7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3564 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3520 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3582 |

Run 1 — solusi: Identifikasi visual kepingan: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total: 5 segitiga, 1 persegi, 1 jajargenjang. Sesuai dengan opsi C.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (dekomposisi) dari gambar yang diberikan. Ini adalah tugas mengenali dan mengklasifikasikan bentuk geometris dasar, yang termasuk dalam domain knowing.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun datar (segitiga, persegi, jajargenjang) dan kemampuan mengenali bentuk-bentuk tersebut dalam komposisi visual.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah kepingan berdasarkan bentuknya. Tidak ada langkah rumit atau integrasi konsep yang menantang. Jalur penyelesaian sangat jelas dengan bantuan visual yang eksplisit.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

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
| gradeRelativeRationale | Tugas mengidentifikasi bentuk geometris dasar dalam tangram adalah materi standar kelas 6 yang bersifat rutin dan langsung. |

Run 2 — solusi: Mengidentifikasi dan menghitung setiap kepingan pada gambar: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total sesuai dengan opsi C.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan mengklasifikasikan bentuk-bentuk geometri dasar yang menyusun gambar kompleks (perahu). Ini adalah tugas pengenalan dan klasifikasi bentuk yang rutin.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan ciri-ciri bangun datar (segitiga, persegi, jajargenjang) untuk melakukan dekomposisi.. Bukti: Nama Bangun Datar; Banyaknya
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (identifikasi visual). Siswa hanya perlu mengenali bentuk dan menghitung jumlahnya. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar geometri (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi bentuk tangram adalah materi standar kelas rendah hingga menengah SD. Tidak ada tuntutan perencanaan atau integrasi yang tinggi. |

Run 3 — solusi: Mengidentifikasi dan menghitung setiap kepingan bangun datar pada gambar: terdapat 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Sesuai dengan opsi C.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengklasifikasikan bentuk-bentuk geometris yang menyusun gambar perahu. Ini adalah tugas pengenalan bentuk dasar dan penghitungan jumlah kepingan, yang merupakan penerapan langsung dari konsep pengenalan bangun datar.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang karakteristik dan kategori bangun datar (segitiga, persegi, jajargenjang) dalam konteks komposisi bentuk.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengamati gambar dan menghitung jumlah masing-masing jenis bangun datar. Tidak ada langkah perencanaan yang kompleks atau kendala yang saling berinteraksi. Tugas ini rutin bagi siswa kelas 6 yang sudah mengenal bentuk-bentuk dasar tangram.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar geometri (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas dekomposisi visual sederhana ini sesuai untuk kelas 6 sebagai latihan pengenalan bentuk, dengan tingkat kesulitan rendah karena tidak memerlukan perhitungan matematis lanjut atau analisis hubungan antar bentuk yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5062`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun dari gambar yang diberikan. Ini adalah tugas mengenali dan mengklasifikasikan bentuk geometris dasar, yang termasuk dalam domain knowing.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun datar (segitiga, persegi, jajargenjang) dan kemampuan mengenali bentuk-bentuk tersebut dalam komposisi visual.
- Intended difficulty `Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah kepingan berdasarkan bentuknya. Tidak ada langkah rumit atau integrasi konsep yang menantang. Jalur penyelesaian sangat jelas dengan bantuan visual yang eksplisit.

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
| gradeRelativeRationale | Tugas mengidentifikasi bentuk geometris dasar dalam tangram adalah materi standar kelas 6 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 235/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.048609; applying=0.951391; reasoning=0.000000 | applying | 0.951391 | 0.176949 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.029009; conceptual=0.954327; procedural=0.016664; metacognitive=0.000000 | conceptual | 0.954327 | 0.155479 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.690071; Medium=0.300122; Hard=0.009806 | Easy | 0.690071 | 0.603086 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.951391; −Σp ln(p) = 0.194398; H = 0.194398/ln(3) = 0.176949; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.954327; −Σp ln(p) = 0.215539; H = 0.215539/ln(4) = 0.155479; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.690071; −Σp ln(p) = 0.662557; H = 0.662557/ln(3) = 0.603086; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Komposisi dan Dekomposisi Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: |**No**|**Nama Bangun Datar**|**Gambar**|**Banyaknya**|
|---|---|---|---|
|1<br>2|Segitiga<br>...|...|...<br>...|

Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :
Pilihan: A. Segitiga 5, trapesium 1, persegi 1
B. Segitiga 6, persegi 1
C. Segitiga 5, jajargenjang 1, persegi 1
D. Segitiga 4, jajargenjang 1, persegi 1
Transkripsi visual: Gambar menunjukkan sebuah perahu yang tersusun dari 7 keping bangun datar berwarna: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua, 1 persegi hijau muda, 1 segitiga oranye, 1 jajargenjang kuning, dan 1 segitiga merah muda. Total kepingan: 5 segitiga, 1 persegi, 1 jajargenjang.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `4857ed456bf6383ee84ff085`

Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

| Opsi | Isi |
|---|---|
| A | Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang |
| B | Tidak, karena jajargenjang tidak memiliki sisi-sisi yang sejajar |
| C | Ya, karena sisi-sisi yang berhadapan pada jajargenjang sejajar |
| D | Ya, karena belah ketupat boleh disebut jajargenjang, maka sebaliknya juga boleh |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Belah ketupat adalah jajargenjang dengan empat sisi sama panjang. Jajargenjang hanya memerlukan dua pasang sisi sejajar. Karena tidak semua jajargenjang memiliki empat sisi sama panjang, maka tidak semua jajargenjang adalah belah ketupat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f0f80cc02903011b0ae32ba57f8eeb26e59f415ad61b0c44a76214988cdf7dc0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 3404 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3794 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3716 |

Run 1 — solusi: Belah ketupat adalah jajargenjang dengan empat sisi sama panjang. Jajargenjang hanya memerlukan dua pasang sisi sejajar. Karena tidak semua jajargenjang memiliki empat sisi sama panjang, maka tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan penalaran logis mengenai hubungan hierarki antara dua bangun datar berdasarkan sifat-sifat definisinya, bukan sekadar mengingat fakta.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi, klasifikasi, dan hubungan antar konsep geometri (segi empat).. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?
- Intended difficulty `classify/Medium`: Soal menuntut pemahaman konseptual tentang sifat bangun datar. Siswa harus membedakan syarat cukup dan syarat perlu dalam definisi geometri. Tingkat kesulitan sedang karena memerlukan pemahaman mendalam tentang hierarki bangun datar.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dan sifat-sifat jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan memahami klasifikasi bangun datar. Soal ini menguji pemahaman konseptual yang sering disalahpahami, sehingga menuntut lebih dari sekadar ingatan. |

Run 2 — solusi: Belah ketupat adalah jajargenjang dengan empat sisi sama panjang. Jajargenjang hanya memerlukan dua pasang sisi sejajar. Karena tidak semua jajargenjang memiliki empat sisi sama panjang, maka tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman definisi geometris untuk menentukan validitas hubungan inklusi antar bangun datar.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep tentang sifat-sifat bangun datar dan hubungan hierarkis di antara keduanya.. Bukti: belah ketupat; jajargenjang
- Intended difficulty `classify/Medium`: Soal menguji pemahaman konsep inklusi bangun datar yang sering membingungkan siswa, meskipun prosedurnya rutin.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dan sifat-sifat jajargenjang dan belah ketupat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan memahami klasifikasi bangun datar. Menentukan arah implikasi yang benar antara dua bangun datar yang berkerabat memerlukan ketelitian konseptual. |

Run 3 — solusi: Belah ketupat adalah jajargenjang dengan 4 sisi sama panjang. Jajargenjang tidak harus memiliki 4 sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Siswa harus menganalisis hubungan hierarkis antara dua bangun datar berdasarkan sifat-sifatnya (sisi sama panjang), bukan sekadar mengingat definisi.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang klasifikasi bangun datar dan hubungan antar sifat-sifat geometris (konsep inklusi).. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Intended difficulty `classify/Medium`: Memerlukan pemahaman konsep sifat bangun datar dan kemampuan membedakan syarat cukup vs syarat perlu dalam klasifikasi. Ini adalah tugas konseptual standar kelas 6.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan memahami hierarki bangun datar. Soal ini menguji pemahaman konsep tersebut tanpa perhitungan rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 2, "applying": 1} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3812`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus melakukan penalaran logis mengenai hubungan hierarki antara dua bangun datar berdasarkan sifat-sifat definisinya, bukan sekadar mengingat fakta.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman tentang definisi, klasifikasi, dan hubungan antar konsep geometri (segi empat).
- Intended difficulty `Medium`: Soal menuntut pemahaman konseptual tentang sifat bangun datar. Siswa harus membedakan syarat cukup dan syarat perlu dalam definisi geometri. Tingkat kesulitan sedang karena memerlukan pemahaman mendalam tentang hierarki bangun datar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dan sifat-sifat jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan memahami klasifikasi bangun datar. Soal ini menguji pemahaman konseptual yang sering disalahpahami, sehingga menuntut lebih dari sekadar ingatan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 128/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000004; applying=0.999996; reasoning=0.000000 | applying | 0.999996 | 0.000044 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.038832; conceptual=0.947241; procedural=0.013928; metacognitive=0.000000 | conceptual | 0.947241 | 0.170969 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.793341; Medium=0.200808; Hard=0.005851 | Easy | 0.793341 | 0.487997 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999996; −Σp ln(p) = 0.000048; H = 0.000048/ln(3) = 0.000044; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.947241; −Σp ln(p) = 0.237014; H = 0.237014/ln(4) = 0.170969; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.793341; −Σp ln(p) = 0.536119; H = 0.536119/ln(3) = 0.487997; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Membandingkan Ciri-Ciri Segi Empat
Tipe soal: multiple_choice
Stimulus: -
Soal: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?
Pilihan: A. Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang
B. Tidak, karena jajargenjang tidak memiliki sisi-sisi yang sejajar
C. Ya, karena sisi-sisi yang berhadapan pada jajargenjang sejajar
D. Ya, karena belah ketupat boleh disebut jajargenjang, maka sebaliknya juga boleh
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `4d0f79031c5c62d5b3028075`

Buatlah kelompok (3–4 siswa), kemudian tentukan apakah kelompok kalian setuju atau tidak setuju dengan setiap pernyataan berikut. Jika ada perbedaan pendapat, coba diskusikan!<br><br>Apakah kalian setuju atau tidak setuju dengan pernyataan berikut: "Saat melempar koin, lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka."?

| Opsi | Isi |
|---|---|
| A | Setuju, karena orang biasanya melempar dengan sisi gambar menghadap ke atas |
| B | Setuju, karena sisi gambar koin lebih berat sehingga lebih sering berada di atas |
| C | Tidak setuju, karena sisi angka jauh lebih sering muncul dibandingkan sisi gambar |
| D | Tidak setuju, karena kedua sisi koin memiliki peluang yang sama untuk muncul |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Koin memiliki dua sisi yang identik dalam hal peluang muncul saat dilempar secara acak. Peluang muncul sisi gambar adalah 1/2 dan peluang muncul sisi angka adalah 1/2. Karena 1/2 = 1/2, maka peluang keduanya sama besar. Pernyataan bahwa salah satu sisi lebih mudah muncul adalah salah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad9a2142e2d12e9b4093538a268b140b5cdc1567b65493e04b5778082571c3bf`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2456 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2339 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2438 |

Run 1 — solusi: Koin memiliki dua sisi yang identik dalam hal peluang muncul saat dilempar secara acak. Peluang muncul sisi gambar adalah 1/2 dan peluang muncul sisi angka adalah 1/2. Karena 1/2 = 1/2, maka peluang keduanya sama besar. Pernyataan bahwa salah satu sisi lebih mudah muncul adalah salah.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengevaluasi pernyataan tentang peluang kejadian sederhana (pelemparan koin) dan memilih alasan yang benar secara konseptual. Siswa perlu menerapkan pemahaman dasar tentang peluang teoretis (equally likely outcomes) untuk menolak pernyataan yang salah. Ini termasuk kategori applying karena siswa menerapkan konsep peluang dasar pada konteks rutin.. Bukti: Tidak setuju, karena kedua sisi koin memiliki peluang yang sama untuk muncul
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa mengenai prinsip dasar peluang (bahwa koin yang adil memiliki peluang 1/2 untuk setiap sisi). Ini adalah pemahaman tentang hubungan dan prinsip dasar dalam probabilitas, yang masuk dalam kategori konseptual.. Bukti: kedua sisi koin memiliki peluang yang sama untuk muncul
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah bagi siswa kelas 6 karena konsep peluang koin (50:50) adalah materi dasar yang familiar. Jalur penyelesaiannya langsung: memahami bahwa koin memiliki dua sisi dengan peluang yang sama. Tidak ada perhitungan kompleks atau kendala yang saling berinteraksi.. Bukti: Saat melempar koin, lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka.; Tidak setuju, karena kedua sisi koin memiliki peluang yang sama untuk muncul

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian sederhana (koin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar untuk koin adalah standar kurikulum kelas 6. Soal ini hanya menuntut pemahaman konsep dasar tanpa perhitungan rumit. |

Run 2 — solusi: Peluang muncul sisi gambar dan sisi angka pada koin yang adil adalah sama besar (1/2), sehingga pernyataan bahwa salah satu sisi lebih mudah muncul adalah tidak tepat.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengevaluasi pernyataan tentang peluang kejadian sederhana (pelemparan koin) dan memilih alasan yang benar secara konseptual. Ini melibatkan penerapan pemahaman dasar tentang peluang teoretis.. Bukti: Tidak setuju, karena kedua sisi koin memiliki peluang yang sama untuk muncul
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar peluang bahwa koin yang adil memiliki dua sisi dengan peluang yang sama (1/2), yang merupakan konsep fundamental dalam materi peluang.. Bukti: kedua sisi koin memiliki peluang yang sama untuk muncul
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena menguji pemahaman dasar tentang peluang kejadian sederhana yang familiar bagi siswa kelas 6. Jalur penyelesaiannya langsung, yaitu mengidentifikasi bahwa peluang munculnya sisi gambar dan angka adalah sama.. Bukti: Saat melempar koin, lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian sederhana (koin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah kurikulum standar kelas 6. Soal ini tidak memerlukan perhitungan kompleks, hanya pemahaman konsep dasar peluang teoretis. |

Run 3 — solusi: Koin memiliki dua sisi yang identik dalam hal peluang muncul saat dilempar secara acak. Peluang muncul sisi gambar adalah 1/2 dan peluang muncul sisi angka adalah 1/2. Karena 1/2 = 1/2, maka peluang keduanya sama besar. Pernyataan bahwa salah satu sisi lebih mudah muncul adalah salah.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengevaluasi pernyataan tentang peluang kejadian sederhana (pelemparan koin) dan memilih alasan yang benar secara konseptual. Siswa perlu menerapkan pemahaman dasar tentang peluang teoretis (bahwa koin adil memiliki peluang 1/2 untuk setiap sisi) untuk menolak pernyataan yang salah. Ini termasuk dalam domain applying karena siswa menggunakan konsep peluang dasar untuk menilai situasi.. Bukti: Tidak setuju, karena kedua sisi koin memiliki peluang yang sama untuk muncul
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai prinsip dasar peluang (bahwa koin memiliki dua sisi dengan peluang yang sama). Ini adalah pemahaman tentang hubungan dan prinsip dasar dalam probabilitas, yang masuk dalam kategori pengetahuan konseptual.. Bukti: kedua sisi koin memiliki peluang yang sama untuk muncul
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena konsep peluang koin (50:50) adalah materi dasar yang familiar bagi siswa kelas 6. Jalur penyelesaiannya langsung: memahami bahwa koin memiliki dua sisi yang setara peluangnya. Tidak ada perhitungan kompleks atau langkah-langkah yang saling bergantung yang rumit.. Bukti: Saat melempar koin, lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian sederhana (koin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang koin adalah pengenalan dasar probabilitas di kelas 6. Soal ini hanya menuntut pemahaman konsep dasar tanpa perhitungan matematis yang berat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 152/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.004527; applying=0.995473; reasoning=0.000000 | applying | 0.995473 | 0.026352 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.016741; conceptual=0.950795; procedural=0.032464; metacognitive=0.000000 | conceptual | 0.950795 | 0.164264 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.693056; Medium=0.302074; Hard=0.004870 | Easy | 0.693056 | 0.584050 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.995473; −Σp ln(p) = 0.028950; H = 0.028950/ln(3) = 0.026352; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.950795; −Σp ln(p) = 0.227719; H = 0.227719/ln(4) = 0.164264; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.693056; −Σp ln(p) = 0.641644; H = 0.641644/ln(3) = 0.584050; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Skala Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Buatlah kelompok (3–4 siswa), kemudian tentukan apakah kelompok kalian setuju atau tidak setuju dengan setiap pernyataan berikut. Jika ada perbedaan pendapat, coba diskusikan!

Apakah kalian setuju atau tidak setuju dengan pernyataan berikut: "Saat melempar koin, lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka."?
Pilihan: A. Setuju, karena orang biasanya melempar dengan sisi gambar menghadap ke atas
B. Setuju, karena sisi gambar koin lebih berat sehingga lebih sering berada di atas
C. Tidak setuju, karena sisi angka jauh lebih sering muncul dibandingkan sisi gambar
D. Tidak setuju, karena kedua sisi koin memiliki peluang yang sama untuk muncul
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `ae0b26d791fb6f944ce6405b`

Buatlah skala peluang untuk beberapa konteks berikut. ... d. Hasil melempar dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5.<br><br>Berdasarkan sisi-sisi dadu tersebut (seluruh 8 sisi bertuliskan angka 5), termasuk kategori apa peluang munculnya angka 2 pada skala peluang?

| Opsi | Isi |
|---|---|
| A | Mungkin |
| B | Tidak mungkin |
| C | Kurang mungkin |
| D | Pasti |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Dadu memiliki 8 sisi yang semuanya bernilai 5. Tidak ada sisi bernilai 2. Peluang munculnya angka 2 adalah 0/8 = 0, yang dalam skala peluang dikategorikan sebagai 'Tidak mungkin'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `07b9b076eef1517a061c74b273e8587fb852f98b701ac4012bcf34ff52f59b13`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2391 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2360 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2424 |

Run 1 — solusi: Dadu memiliki 8 sisi yang semuanya bernilai 5. Tidak ada sisi bernilai 2. Peluang munculnya angka 2 adalah 0/8 = 0, yang dalam skala peluang dikategorikan sebagai 'Tidak mungkin'.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang (kejadian mustahil) dengan mengaitkan kondisi fisik objek (dadu) dengan nilai probabilitas. Ini adalah penerapan konsep dasar peluang pada konteks yang diberikan.. Bukti: dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5; termasuk kategori apa peluang munculnya angka 2 pada skala peluang?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang skala peluang, khususnya definisi kejadian mustahil (peluang 0) dalam konteks sederhana.. Bukti: skala peluang; seluruh 8 sisi bertuliskan angka 5
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi bahwa angka 2 tidak ada dalam ruang sampel (semua sisi adalah 5), sehingga kejadian tersebut mustahil. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5; termasuk kategori apa peluang munculnya angka 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel dan skala peluang (pasti, mungkin, tidak mungkin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari konsep peluang dasar. Soal ini adalah aplikasi langsung dari definisi kejadian mustahil tanpa memerlukan perhitungan rumit atau perencanaan langkah yang panjang. |

Run 2 — solusi: Dadu memiliki 8 sisi yang semuanya bernomor 5. Karena tidak ada sisi bernomor 2, maka kejadian munculnya angka 2 adalah kejadian mustahil (peluang = 0). Dalam skala peluang, ini dikategorikan sebagai 'Tidak mungkin'.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang (kejadian mustahil) dan menerapkannya pada konteks yang diberikan. Ini adalah penerapan konsep peluang pada situasi rutin.. Bukti: dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5; termasuk kategori apa peluang munculnya angka 2
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar peluang (kejadian mustahil) dalam konteks skala peluang.. Bukti: skala peluang; peluang munculnya angka 2
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi bahwa angka 2 tidak ada dalam ruang sampel (semua sisi adalah 5), sehingga kejadian tersebut mustahil. Tidak ada langkah kompleks atau integrasi yang diperlukan.. Bukti: dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5; termasuk kategori apa peluang munculnya angka 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel dan skala peluang (pasti, mungkin, tidak mungkin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, mengidentifikasi kejadian mustahil dari ruang sampel yang homogen adalah tugas dasar yang rutin. |

Run 3 — solusi: Dadu memiliki 8 sisi yang semuanya bernomor 5. Tidak ada sisi bernomor 2. Karena kejadian munculnya angka 2 tidak memiliki ruang sampel yang mendukung (jumlah kejadian = 0), maka peluangnya adalah 0, yang dalam skala peluang dikategorikan sebagai 'Tidak mungkin'.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang, yaitu mengidentifikasi ruang sampel dan kejadian yang diharapkan. Soal meminta siswa mengklasifikasikan kejadian yang mustahil terjadi (muncul angka 2 pada dadu yang hanya berisi angka 5) ke dalam skala peluang yang sesuai.. Bukti: d. Hasil melempar dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5.; termasuk kategori apa peluang munculnya angka 2 pada skala peluang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang skala peluang (pasti, mungkin, tidak mungkin) dan penerapannya pada situasi konkret.. Bukti: termasuk kategori apa peluang munculnya angka 2 pada skala peluang?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengenali bahwa angka 2 tidak ada dalam daftar sisi dadu. Tidak ada perhitungan kompleks atau langkah yang saling bergantung; ini adalah penerapan langsung dari definisi 'tidak mungkin' dalam peluang.. Bukti: d. Hasil melempar dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5.; termasuk kategori apa peluang munculnya angka 2 pada skala peluang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang dan skala peluang (pasti, mungkin, tidak mungkin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari konsep dasar peluang. Soal ini bersifat langsung dan tidak memerlukan analisis mendalam atau perencanaan strategi, sehingga sesuai untuk kategori Easy. |

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
| Domain kognitif | knowing=0.003259; applying=0.996741; reasoning=0.000000 | applying | 0.996741 | 0.019950 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.056104; conceptual=0.924462; procedural=0.019434; metacognitive=0.000000 | conceptual | 0.924462 | 0.224198 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.719772; Medium=0.276390; Hard=0.003838 | Easy | 0.719772 | 0.558383 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996741; −Σp ln(p) = 0.021918; H = 0.021918/ln(3) = 0.019950; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.924462; −Σp ln(p) = 0.310804; H = 0.310804/ln(4) = 0.224198; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.719772; −Σp ln(p) = 0.613446; H = 0.613446/ln(3) = 0.558383; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Skala Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Buatlah skala peluang untuk beberapa konteks berikut. ... d. Hasil melempar dadu 8 sisi dengan masing-masing sisi sebagai berikut: 5, 5, 5, 5, 5, 5, 5, 5.

Berdasarkan sisi-sisi dadu tersebut (seluruh 8 sisi bertuliskan angka 5), termasuk kategori apa peluang munculnya angka 2 pada skala peluang?
Pilihan: A. Mungkin
B. Tidak mungkin
C. Kurang mungkin
D. Pasti
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `b0bcef02731ce1c1ec1f8a92`

- c. (Soal tantangan) Pilihan dadu<br><br>\|Pilihan 1\|Pilihan 2\|<br>\|---\|---\|<br>\|Dadu kubus dengan sisi sebagai\|Dadu piramida dengan sisi\|<br>\|berikut:\|sebagai berikut:\|<br>\|1, 2, 3, 4, 5, 6\|1, 2, 3, 4\|<br><br>Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!

| Opsi | Isi |
|---|---|
| A | Pilihan 2 (dadu piramida) |
| B | Keduanya sama besar karena sama-sama punya satu angka 3 |
| C | Tidak bisa ditentukan karena bentuk dadunya berbeda |
| D | Pilihan 1 (dadu kubus) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Peluang muncul angka 3 pada dadu kubus adalah 1/6. Peluang muncul angka 3 pada dadu piramida adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida (Pilihan 2) memberikan peluang menang yang lebih besar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menerapkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `561de60b7624edb24024b811d66001b2394686dc8fdaa49c3fe6e9d25e086ceb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2592 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2505 |
| 3 | success | valid / verified | applying | conceptual | Medium | 4011 |

Run 1 — solusi: Peluang muncul angka 3 pada dadu kubus adalah 1/6 (sekitar 0,167). Peluang muncul angka 3 pada dadu piramida adalah 1/4 (0,25). Karena 1/4 > 1/6, maka peluang menang lebih besar jika menggunakan dadu piramida (Pilihan 2).
- Domain kognitif `classify/reasoning`: Siswa diminta untuk membandingkan dua peluang kejadian yang berbeda (1/6 vs 1/4) dan memberikan justifikasi atas pilihan mereka. Ini melampaui sekadar mengingat atau menerapkan prosedur rutin, karena memerlukan pemahaman konsep peluang sebagai rasio kejadian terhadap ruang sampel dan kemampuan membandingkan pecahan tersebut untuk mengambil keputusan.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang peluang, yaitu hubungan antara jumlah kejadian yang diinginkan dengan total ruang sampel pada objek yang berbeda (dadu kubus vs dadu piramida).. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium. Siswa perlu mengidentifikasi ruang sampel yang berbeda untuk dua objek (6 sisi vs 4 sisi), menghitung peluang masing-masing (1/6 dan 1/4), dan membandingkan kedua pecahan tersebut. Meskipun konsepnya dasar, siswa harus melakukan beberapa langkah terstruktur tanpa bantuan eksplisit untuk menentukan peluang dan membandingkannya.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.; Syarat menangnya adalah mendapatkan angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai perbandingan kejadian terhadap ruang sampel dan perbandingan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, membandingkan peluang dengan ruang sampel yang berbeda memerlukan penalaran logis yang melampaui sekadar menghitung. Soal ini menuntut siswa membangun hubungan antara jumlah sisi dan peluang tanpa bantuan langkah-langkah, namun prosedurnya tetap standar untuk materi peluang. |

Run 2 — solusi: Peluang muncul angka 3 pada dadu kubus adalah 1/6. Peluang muncul angka 3 pada dadu piramida adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan dua peluang kejadian yang berbeda dan memilih yang lebih besar. Ini memerlukan penerapan konsep peluang dasar (jumlah kejadian yang diinginkan dibagi total ruang sampel) pada konteks perbandingan dua objek yang berbeda, yang masuk dalam kategori applying.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana ukuran ruang sampel (jumlah sisi dadu) mempengaruhi peluang suatu kejadian, bukan sekadar menghafal rumus atau melakukan prosedur rutin.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dua perhitungan peluang sederhana (1/6 dan 1/4) dan membandingkan keduanya. Meskipun konsepnya dasar, siswa perlu mengintegrasikan pemahaman tentang ruang sampel yang berbeda untuk mengambil keputusan, yang sedikit lebih kompleks daripada sekadar menghitung satu peluang.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.; Jelaskan alasan atas pilihan kalian!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai perbandingan kejadian yang diinginkan terhadap total ruang sampel. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu membandingkan pecahan dengan penyebut berbeda dan memahami konsep peluang sederhana. Soal ini menuntut penalaran logis sederhana di atas prosedur hitung. |

Run 3 — solusi: Peluang muncul angka 3 pada dadu kubus adalah 1/6. Peluang muncul angka 3 pada dadu piramida adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida (Pilihan 2) memberikan peluang menang lebih besar.
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep peluang (kejadian yang diharapkan dibagi total kejadian) pada dua objek berbeda dan membandingkan hasilnya untuk menentukan pilihan terbaik.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang; Syarat menangnya adalah mendapatkan angka 3
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman hubungan antara jumlah sisi (ruang sampel) dan peluang kejadian, bukan sekadar menghafal rumus.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang
- Intended difficulty `classify/Medium`: Soal memerlukan perbandingan dua pecahan dengan penyebut berbeda dalam konteks peluang. Siswa harus membangun rasio peluang untuk masing-masing dadu dan membandingkannya. Ini adalah tugas rutin bagi kelas 6 namun memerlukan integrasi konsep yang lebih dari sekadar ingatan.. Bukti: Pilihan 1 (dadu kubus) ... Pilihan 2 (dadu piramida); Syarat menangnya adalah mendapatkan angka 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang dan perbandingan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari perbandingan pecahan dan dasar peluang. Soal ini menguji pemahaman konsep tersebut tanpa beban komputasi yang berat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4281`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus mengintegrasikan konsep peluang (rasio kejadian terhadap ruang sampel) dengan perbandingan pecahan untuk mengambil keputusan. Ini melampaui prosedur rutin karena siswa harus membangun hubungan antara jumlah sisi dan peluang secara mandiri.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang bagaimana ukuran ruang sampel (jumlah sisi) berbanding terbalik dengan peluang suatu kejadian spesifik, yang merupakan prinsip dasar peluang.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium. Siswa perlu mengidentifikasi ruang sampel yang berbeda (6 vs 4), menghitung peluang masing-masing (1/6 dan 1/4), dan membandingkan pecahan tersebut. Meskipun konsepnya dasar, siswa harus melakukan beberapa langkah terstruktur tanpa bantuan eksplisit untuk menentukan peluang dan membandingkannya.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai perbandingan kejadian terhadap ruang sampel dan perbandingan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, membandingkan peluang dengan ruang sampel yang berbeda memerlukan penalaran logis yang melampaui sekadar menghitung. Soal ini menuntut siswa membangun hubungan antara jumlah sisi dan peluang tanpa bantuan langkah-langkah, namun prosedurnya tetap standar untuk materi peluang. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 170/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000007; applying=0.999993; reasoning=0.000000 | applying | 0.999993 | 0.000085 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004624; conceptual=0.987499; procedural=0.007877; metacognitive=0.000000 | conceptual | 0.987499 | 0.054417 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.610047; Medium=0.384449; Hard=0.005504 | Easy | 0.610047 | 0.635023 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999993; −Σp ln(p) = 0.000093; H = 0.000093/ln(3) = 0.000085; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.987499; −Σp ln(p) = 0.075438; H = 0.075438/ln(4) = 0.054417; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.610047; −Σp ln(p) = 0.697644; H = 0.697644/ln(3) = 0.635023; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Membandingkan Peluang Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: - c. (Soal tantangan) Pilihan dadu

|Pilihan 1|Pilihan 2|
|---|---|
|Dadu kubus dengan sisi sebagai|Dadu piramida dengan sisi|
|berikut:|sebagai berikut:|
|1, 2, 3, 4, 5, 6|1, 2, 3, 4|

Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!
Pilihan: A. Pilihan 2 (dadu piramida)
B. Keduanya sama besar karena sama-sama punya satu angka 3
C. Tidak bisa ditentukan karena bentuk dadunya berbeda
D. Pilihan 1 (dadu kubus)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `a09023c97aaa8c1be58c80f9`

Untuk melakukan pemilihan ketua kelas, kelas Dhien melakukan undian menggunakan roda putar seperti di gambar (bertuliskan nama Reimon, Abdillah, Maryam, Tuti).<br><br>Dengan roda putar yang dibuat, tentukan siapa yang memiliki peluang menang paling besar?

| Opsi | Isi |
|---|---|
| A | Tuti |
| B | Reimon |
| C | Maryam |
| D | Abdillah |

![Gambar sumber soal 25](<../../../images/kelas6_panduan_siswa_kelas6.pdf-0134-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Peluang jarum berhenti pada suatu bagian roda putar sebanding dengan luas juring tersebut. Dengan membandingkan luas keempat juring pada gambar, juring bertuliskan Maryam memiliki luas paling besar, sehingga Maryam memiliki peluang menang paling besar.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0134-01.png. Transkripsi visual: Sebuah roda putar berbentuk lingkaran dibagi menjadi empat juring dengan ukuran yang berbeda-beda. Juring-juring tersebut diberi label nama: Reimon (warna hijau), Abdillah (warna oranye muda), Tuti (warna oranye tua), dan Maryam (warna biru). Secara visual, juring berwarna biru yang bertuliskan Maryam memiliki luas yang paling besar dibandingkan dengan ketiga juring lainnya.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e867523b5e2344fa9393d6f2523a15e072dfa931dff2443ce63db41cff9e8f8c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 4319 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3472 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3512 |

Run 1 — solusi: Peluang jarum berhenti pada suatu bagian roda putar sebanding dengan luas juring tersebut. Dengan membandingkan luas keempat juring pada gambar, juring bertuliskan Maryam memiliki luas paling besar, sehingga Maryam memiliki peluang menang paling besar.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara luas juring lingkaran dengan peluang kejadian pada roda putar. Ini adalah penerapan konsep dasar peluang dalam konteks visual yang rutin.. Bukti: tentukan siapa yang memiliki peluang menang paling besar; roda putar seperti di gambar
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep bahwa peluang kejadian sebanding dengan luas daerah/juring pada roda putar, yang merupakan prinsip dasar dalam materi peluang.. Bukti: roda putar; peluang menang paling besar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) karena hanya memerlukan perbandingan visual sederhana antara luas juring. Tidak ada perhitungan numerik atau langkah-langkah kompleks yang diperlukan.. Bukti: roda putar seperti di gambar; tentukan siapa yang memiliki peluang menang paling besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep dasar peluang sebagai perbandingan bagian terhadap keseluruhan atau hubungan visual luas daerah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 6 sudah familiar dengan konsep peluang sederhana dan interpretasi visual. Soal ini hanya meminta perbandingan visual langsung tanpa perhitungan numerik yang kompleks, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Peluang kejadian pada roda putar ditentukan oleh luas juring. Semakin besar luas juring, semakin besar peluang jarum berhenti di juring tersebut. Berdasarkan gambar, juring bertuliskan 'Maryam' memiliki luas paling besar dibandingkan juring lainnya, sehingga Maryam memiliki peluang menang paling besar.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan representasi visual (luas juring) untuk menentukan peluang kejadian. Ini adalah penerapan konsep dasar peluang pada konteks rutin (roda putar).. Bukti: tentukan siapa yang memiliki peluang menang paling besar; roda putar yang dibuat
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara luas area (juring) dengan peluang kejadian pada roda putar.. Bukti: peluang menang paling besar; roda putar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan observasi visual langsung untuk membandingkan luas juring. Tidak ada perhitungan kompleks atau langkah-langkah yang saling bergantung.. Bukti: roda putar yang dibuat; tentukan siapa yang memiliki peluang menang paling besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbandingan luas area dan konsep peluang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah familiar dengan konsep peluang sederhana dan perbandingan visual. Soal ini tidak menuntut perhitungan matematis, hanya observasi visual yang langsung. |

Run 3 — solusi: Peluang kejadian pada roda putar ditentukan oleh luas juring. Dengan mengamati gambar, juring bertuliskan 'Maryam' memiliki luas area paling besar dibandingkan juring lainnya. Oleh karena itu, Maryam memiliki peluang menang paling besar.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan representasi visual (roda putar) untuk menentukan peluang terbesar. Ini adalah penerapan konsep peluang dasar pada konteks rutin (roda putar), sehingga masuk dalam kategori applying.. Bukti: tentukan siapa yang memiliki peluang menang paling besar; roda putar yang dibuat
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara luas area (juring) pada roda putar dengan peluang kejadian, bukan sekadar menghafal fakta atau melakukan prosedur perhitungan yang kompleks.. Bukti: peluang menang paling besar; roda putar
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan perbandingan visual langsung terhadap luas juring pada roda putar. Tidak ada perhitungan matematis yang rumit atau langkah-langkah yang saling bergantung.. Bukti: tentukan siapa yang memiliki peluang menang paling besar; roda putar yang dibuat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbandingan luas area dan konsep peluang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, membandingkan luas juring secara visual untuk menentukan peluang adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 178/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.009166; conceptual=0.988851; procedural=0.001983; metacognitive=0.000000 | conceptual | 0.988851 | 0.047922 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.710606; Medium=0.281645; Hard=0.007749 | Easy | 0.710606 | 0.580100 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.988851; −Σp ln(p) = 0.066434; H = 0.066434/ln(4) = 0.047922; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.710606; −Σp ln(p) = 0.637305; H = 0.637305/ln(3) = 0.580100; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 6
Topik: Matematika SD Kelas 6
Subtopik: Membandingkan Peluang Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk melakukan pemilihan ketua kelas, kelas Dhien melakukan undian menggunakan roda putar seperti di gambar (bertuliskan nama Reimon, Abdillah, Maryam, Tuti).

Dengan roda putar yang dibuat, tentukan siapa yang memiliki peluang menang paling besar?
Pilihan: A. Tuti
B. Reimon
C. Maryam
D. Abdillah
Transkripsi visual: Sebuah roda putar berbentuk lingkaran dibagi menjadi empat juring dengan ukuran yang berbeda-beda. Juring-juring tersebut diberi label nama: Reimon (warna hijau), Abdillah (warna oranye muda), Tuti (warna oranye tua), dan Maryam (warna biru). Secara visual, juring berwarna biru yang bertuliskan Maryam memiliki luas yang paling besar dibandingkan dengan ketiga juring lainnya.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
