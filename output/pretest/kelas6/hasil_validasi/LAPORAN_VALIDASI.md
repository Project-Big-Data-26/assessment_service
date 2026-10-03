# Validasi ulang soal kelas 6 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v4-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v2-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 6 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model lama dipakai untuk menunjukkan ketidaksepakatan; tidak diberikan kembali ke Gemini.

Jumlah soal: 25; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 20, "reasoning": 4, "knowing": 1}, "knowledgeDimension": {"procedural": 8, "conceptual": 16, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 16, "Medium": 9, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 20, "reasoning": 4, "knowing": 1}, "knowledgeDimension": {"procedural": 8, "conceptual": 16, "factual": 1}, "intendedDifficulty": {"Easy": 16, "Medium": 9}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 25}`.
Run awal sukses: 75/75; adjudikasi: 4; token sukses tercatat: 151,874.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
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
Solusi minimum hasil AI: 4 dikali 3/4 sama dengan 12/4, yang disederhanakan menjadi 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7268235690d0c4469a70eb8aa99f5618523356e8c03cb234e94bcc72e26a70a1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1382 |
| 2 | success | valid / verified | applying | procedural | Easy | 1345 |
| 3 | success | valid / verified | applying | procedural | Easy | 1386 |

Run 1 — solusi: 4 dikali 3/4 sama dengan 12/4, yang disederhanakan menjadi 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi perkalian bilangan asli dengan pecahan yang merupakan prosedur rutin dalam kurikulum kelas 6.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m; Berapa meter panjang potongan pita seluruhnya
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian bilangan asli dengan pecahan.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya melibatkan satu operasi perkalian pecahan sederhana yang sudah diajarkan di kelas 6.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m; Berapa meter panjang potongan pita seluruhnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar perkalian pecahan dan penyederhanaan pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian bilangan asli dengan pecahan adalah materi standar kelas 6 yang bersifat langsung. |

Run 2 — solusi: 4 * (3/4) = 12/4 = 3 meter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi perkalian bilangan asli dengan pecahan yang merupakan prosedur rutin di kelas 6.. Bukti: Hani membuat 4 potong pita dengan panjang masing-masing 3/4 m; Berapa meter panjang potongan pita seluruhnya
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian bilangan bulat dengan pecahan.. Bukti: 4 potong pita; panjang masing-masing 3/4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan satu langkah operasi perkalian pecahan sederhana yang sudah dipelajari di kelas 6.. Bukti: 4 potong pita; panjang masing-masing 3/4 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep perkalian bilangan asli dengan pecahan biasa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian bilangan asli dengan pecahan adalah materi dasar kelas 6 yang sudah sering dilatih. |

Run 3 — solusi: 4 * (3/4) = 12/4 = 3 meter.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi perkalian bilangan asli dengan pecahan untuk menyelesaikan masalah rutin yang kontekstual.. Bukti: Hani membuat 4 potong pita dengan panjang masing-masing 3/4 m; Berapa meter panjang potongan pita seluruhnya
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perkalian bilangan bulat dengan pecahan.. Bukti: 4 potong pita dengan panjang masing-masing 3/4 m
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang menggunakan representasi familiar dan operasi dasar, sesuai untuk tingkat kelas 6.. Bukti: 4 potong pita; panjang masing-masing 3/4 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau perkalian bilangan asli dengan pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian pecahan dengan bilangan asli adalah materi standar kelas 5/6, soal ini bersifat langsung tanpa jebakan kompleks. |

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
Solusi minimum hasil AI: 2/15 * 75 = (2 * 75) / 15 = 150 / 15 = 10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a50e366d76f752b7e3618f1e7ba410b141060cb9f894f42d3585fc780117d3c0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1382 |
| 2 | success | valid / verified | applying | procedural | Easy | 1386 |
| 3 | success | valid / verified | applying | procedural | Easy | 1400 |

Run 1 — solusi: 2/15 * 75 = (2 * 75) / 15 = 150 / 15 = 10.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur perkalian pecahan dengan bilangan bulat dalam konteks rutin.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian pecahan dengan bilangan bulat.. Bukti: 2/15 bagian dari 75
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan satu operasi perkalian pecahan, dan konteksnya sangat familiar bagi siswa kelas 6.. Bukti: 2/15 bagian dari 75

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian pecahan dengan bilangan bulat |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi perkalian pecahan dengan bilangan bulat adalah materi standar kelas 6 yang bersifat prosedural langsung. |

Run 2 — solusi: 2/15 * 75 = (2 * 75) / 15 = 150 / 15 = 10.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi perkalian pecahan terhadap bilangan bulat dalam konteks rutin yang sudah familiar.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian pecahan dengan bilangan bulat.. Bukti: 2/15 bagian dari 75
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan satu langkah operasi perkalian pecahan, dan angka yang digunakan cukup sederhana untuk siswa kelas 6.. Bukti: 75 kue pastel; 2/15 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian pecahan dengan bilangan bulat |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi perkalian pecahan adalah materi standar kelas 6 yang disajikan dalam bentuk soal cerita langsung tanpa jebakan kompleks. |

Run 3 — solusi: Banyak kue yang dikonsumsi = (2/15) * 75 = 2 * (75 / 15) = 2 * 5 = 10 kue.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur perkalian pecahan dengan bilangan bulat yang merupakan prosedur rutin dan langsung.. Bukti: Sebanyak 2/15 bagian dari 75 pastel tersebut telah dikonsumsi
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian pecahan dengan bilangan bulat (prosedural).. Bukti: 2/15 bagian dari 75
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya melibatkan satu operasi perkalian pecahan, dan angka yang digunakan cukup sederhana untuk siswa kelas 6.. Bukti: 75 kue pastel; 2/15 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan sebagai bagian dari keseluruhan dan operasi perkalian pecahan dengan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian pecahan dengan bilangan bulat adalah materi standar kelas 6 yang bersifat prosedural langsung. |

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
Solusi minimum hasil AI: Membagi pecahan dengan bilangan asli: 2/4 : 3 = 2/(4 x 3) = 2/12 = 1/6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menyebutkan', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `45a366966209461e26e58a055fcadda7b852b3b7b93653c0c3223d6823af1510`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1524 |
| 2 | success | valid / verified | applying | procedural | Easy | 1524 |
| 3 | success | valid / verified | applying | procedural | Easy | 1517 |

Run 1 — solusi: Membagi pecahan dengan bilangan asli: 2/4 : 3 = 2/(4 x 3) = 2/12 = 1/6.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian pecahan dengan bilangan bulat dalam konteks pembagian adil (fair sharing). Ini adalah penerapan langsung dari konsep pembagian pecahan.. Bukti: membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pembagian pecahan dengan bilangan bulat.. Bukti: 2/4 : 3 = 2/12 = 1/6
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan prosedur rutin pembagian pecahan dengan bilangan bulat yang sudah dipelajari di kelas 6. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi pembagian pecahan dengan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pembagian pecahan adalah standar kurikulum kelas 6. Soal ini menggunakan angka sederhana dan konteks pembagian yang umum. |

Run 2 — solusi: Membagi 2/4 dengan 3 sama dengan 2/4 dikali 1/3, yaitu 2/12. Disederhanakan menjadi 1/6.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian pecahan dengan bilangan bulat dalam konteks pembagian adil (fair sharing). Ini adalah penerapan prosedur rutin.. Bukti: membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pembagian pecahan dengan bilangan bulat.. Bukti: 2/4 dibagi 3; 2/4 * 1/3 = 2/12 = 1/6
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar pembagian pecahan yang diajarkan di kelas 6. Langkah-langkahnya rutin dan tidak memerlukan strategi kompleks.. Bukti: membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan, operasi pembagian pecahan dengan bilangan bulat, dan penyederhanaan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian pecahan dengan bilangan bulat adalah materi standar kelas 6. Soal ini langsung menguji pemahaman algoritma tersebut tanpa konteks yang mengecoh. |

Run 3 — solusi: Membagi 2/4 dengan 3 sama dengan 2/4 dikali 1/3, yaitu 2/12, yang disederhanakan menjadi 1/6.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian pecahan dengan bilangan bulat dalam konteks pembagian adil, yang merupakan penerapan konsep rutin.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian pecahan dengan bilangan bulat.. Bukti: membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur standar pembagian pecahan dengan bilangan bulat yang umum diajarkan di kelas 6. Beban kognitif rendah karena konteksnya langsung dan prosedurnya rutin.. Bukti: Pak Rudi membagi 2/4 bagian tanah miliknya kepada 3 orang anaknya secara adil.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan dan operasi pembagian pecahan dengan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pembagian pecahan adalah kurikulum standar kelas 6. Soal ini bersifat langsung tanpa jebakan kompleks. |

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
Solusi minimum hasil AI: 6 dibagi 3/4 sama dengan 6 dikali 4/3, yaitu 24/3 = 8.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f0aa88334eb1a87676a49b0cc29c2a3be3f075626b086fef565f02dc8aa2d463`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1454 |
| 2 | success | valid / verified | applying | procedural | Easy | 1437 |
| 3 | success | valid / verified | applying | procedural | Easy | 1420 |

Run 1 — solusi: 6 dibagi 3/4 sama dengan 6 dikali 4/3, yaitu 24/3 = 8.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian pecahan dalam konteks masalah sehari-hari yang rutin. Ini adalah penerapan konsep pembagian pecahan.. Bukti: Rina memiliki 6 kg gula pasir; Setiap adonan kue bolu membutuhkan 3/4 kg gula pasir; Berapa banyak kue bolu yang dibuat oleh Rina?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma pembagian pecahan (mengalikan dengan kebalikan pembagi).. Bukti: 6 dibagi 3/4; 6 dikali 4/3
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin pembagian pecahan yang umum diajarkan di kelas 6. Prosedurnya langsung dan tidak memerlukan strategi nonrutin.. Bukti: 6 kg gula pasir; 3/4 kg gula pasir; Berapa banyak kue bolu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat dengan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian pecahan adalah materi standar kelas 6. Soal ini menggunakan angka sederhana dan konteks yang familiar. |

Run 2 — solusi: 6 dibagi 3/4 sama dengan 6 dikali 4/3, hasilnya 24/3 = 8.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian pecahan dalam konteks kehidupan sehari-hari yang rutin.. Bukti: Rina memiliki 6 kg gula pasir; Setiap adonan kue bolu membutuhkan 3/4 kg gula pasir; Berapa banyak kue bolu yang dibuat oleh Rina?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian pecahan (mengalikan dengan kebalikan).. Bukti: 6 / (3/4) = 6 * (4/3)
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang umum di kelas 6, dengan beban kognitif rendah.. Bukti: 6 kg gula pasir; 3/4 kg gula pasir; Berapa banyak kue bolu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian pecahan dan perkalian bilangan bulat dengan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian pecahan adalah materi standar kelas 6, soal ini menggunakan konteks yang sangat umum dan prosedural. |

Run 3 — solusi: 6 dibagi 3/4 sama dengan 6 dikali 4/3, yaitu 24/3 = 8.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian pecahan dalam konteks masalah sehari-hari yang rutin.. Bukti: Rina memiliki 6 kg gula pasir; Setiap adonan kue bolu membutuhkan 3/4 kg gula pasir; Berapa banyak kue bolu yang dibuat oleh Rina?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian pecahan.. Bukti: 6 dibagi 3/4 = 6 dikali 4/3
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin pembagian pecahan yang umum diajarkan di kelas 6 dengan satu operasi utama.. Bukti: 6 kg gula pasir; 3/4 kg gula pasir; Berapa banyak kue bolu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian pecahan dan perkalian pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian bilangan bulat dengan pecahan adalah materi standar kelas 6 yang bersifat rutin. |

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

![Gambar sumber soal 5](<../images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Konversi semua satuan ke gram: Natrium 88,6 mg = 0,0886 g. Membandingkan nilai: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Jadi, Natrium adalah yang terkecil.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png. Transkripsi visual: Label Informasi Nilai Gizi mencantumkan: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a75218d1fdd799ac65db51228142951a1e6c41a241ee0af3382621b944590b60`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2678 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2721 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2702 |

Run 1 — solusi: Konversi semua satuan ke gram: Natrium 88,6 mg = 0,0886 g. Membandingkan nilai: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Jadi, Natrium adalah yang terkecil.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai desimal dengan satuan yang berbeda (g dan mg), yang memerlukan pemahaman konsep konversi satuan dan perbandingan bilangan desimal.. Bukti: Kandungan zat apakah yang paling kecil komposisinya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar satuan massa (gram ke miligram) dan perbandingan nilai desimal.. Bukti: Natrium 88,6 mg; Protein 1,3 g
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka tanpa melakukan konversi satuan terlebih dahulu. Terdapat jebakan pada satuan (mg vs g) yang memerlukan ketelitian.. Bukti: Natrium 88,6 mg; Protein 1,3 g; Lemak total 5,4 g; Karbohidrat 28,6 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan massa (gram ke miligram) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan konversi satuan dasar dan membandingkan bilangan desimal dalam konteks kehidupan sehari-hari. |

Run 2 — solusi: Konversi satuan: 88,6 mg = 0,0886 g. Membandingkan nilai dalam gram: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Nilai terkecil adalah Natrium (88,6 mg).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang konversi satuan (mg ke g) dan membandingkan nilai desimal untuk menentukan yang terkecil, yang merupakan penerapan prosedur pada situasi rutin.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang hubungan antar satuan (konversi) dan perbandingan nilai desimal, yang merupakan pengetahuan konseptual.. Bukti: 88,6 mg = 0,0886 g
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka mentah (88,6 vs 1,3). Mereka harus melakukan konversi satuan terlebih dahulu sebelum membandingkan, yang merupakan langkah rutin namun krusial.. Bukti: 88,6 mg; 1,3 g, 5,4 g, 28,6 g, 2,7 g

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
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan konversi satuan dasar dan membandingkan bilangan desimal dalam konteks kehidupan sehari-hari. |

Run 3 — solusi: Konversi semua satuan ke gram: Natrium 88,6 mg = 0,0886 g. Membandingkan nilai: 0,0886 g (Natrium) < 1,3 g (Protein) < 2,7 g (Serat) < 5,4 g (Lemak) < 28,6 g (Karbohidrat). Jadi, yang terkecil adalah Natrium.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang konversi satuan (mg ke g) dan membandingkan nilai desimal untuk menentukan yang terkecil.. Bukti: Kandungan zat apakah yang paling kecil komposisinya
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antar satuan massa (gram dan miligram) dan perbandingan nilai desimal.. Bukti: Natrium 88,6 mg; Protein 1,3 g
- Intended difficulty `classify/Medium`: Soal ini memerlukan konversi satuan yang konsisten sebelum membandingkan angka desimal. Ini adalah tugas rutin bagi siswa kelas 6 namun memerlukan ketelitian dalam memperhatikan satuan yang berbeda.. Bukti: Natrium 88,6 mg; Protein 1,3 g; Lemak total 5,4 g; Karbohidrat 28,6 g

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
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu membaca tabel dan memahami perbedaan satuan (mg vs g) dalam konteks kehidupan sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 160/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.117348; applying=0.882652; reasoning=0.000000 | applying | 0.882652 | 0.329149 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.013228; conceptual=0.964859; procedural=0.021913; metacognitive=0.000000 | conceptual | 0.964859 | 0.126565 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.766542; Medium=0.223976; Hard=0.009481 | Easy | 0.766542 | 0.530744 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.882652; −Σp ln(p) = 0.361608; H = 0.361608/ln(3) = 0.329149; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.964859; −Σp ln(p) = 0.175457; H = 0.175457/ln(4) = 0.126565; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.766542; −Σp ln(p) = 0.583082; H = 0.583082/ln(3) = 0.530744; T = 0.953328.


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
Transkripsi visual: Label Informasi Nilai Gizi mencantumkan: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg.
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
Solusi minimum hasil AI: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Maka yang terjauh adalah Arman (3,7) dan terdekat adalah Didi (2,9).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ab8f543b22957422aa67cca38a01368a6dd18c5cf8f87917f6ff2d9450b6ca2a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2021 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1496 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2198 |

Run 1 — solusi: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Maka yang terjauh adalah Arman (3,7) dan terdekat adalah Didi (2,9).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang perbandingan bilangan desimal untuk mengurutkan nilai. Ini adalah proses applying karena melibatkan penggunaan konsep perbandingan pada situasi rutin.. Bukti: Arman berhasil melompat sejauh 3,7 m; Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman tentang nilai tempat dan urutan bilangan desimal (konsep).. Bukti: 3,7 m; 2,9 m; 3,6 m
- Intended difficulty `classify/Easy`: Soal ini melibatkan perbandingan langsung tiga bilangan desimal. Ini adalah prosedur rutin bagi siswa kelas 6.. Bukti: 3,7 m; 2,9 m; 3,6 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan desimal |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan desimal dengan satu angka di belakang koma adalah materi dasar kelas 6. |

Run 2 — solusi: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Terjauh adalah 3,7 (Arman), terdekat adalah 2,9 (Didi).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang urutan bilangan desimal untuk menentukan nilai terbesar dan terkecil dalam konteks pengukuran.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat dan perbandingan bilangan desimal.. Bukti: 3,7 m; 2,9 m; 3,6 m
- Intended difficulty `classify/Easy`: Soal ini melibatkan perbandingan langsung tiga bilangan desimal satu angka di belakang koma, yang merupakan prosedur rutin bagi siswa kelas 6.. Bukti: Arman berhasil melompat sejauh 3,7 m. Sementara itu, Didi berhasil melompat sejauh 2,9 m dan Bayu melompat sejauh 3,6 m.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan desimal dan cara membandingkan dua bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan desimal adalah materi dasar kelas 6. Soal ini tidak memiliki jebakan kompleks selain kesalahan umum dalam membandingkan angka persepuluhan. |

Run 3 — solusi: Membandingkan nilai desimal: 3,7 > 3,6 > 2,9. Maka yang terjauh adalah Arman (3,7 m) dan yang terdekat adalah Didi (2,9 m).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perbandingan bilangan desimal untuk mengurutkan data dan menentukan nilai ekstrem (terjauh dan terdekat) dalam situasi rutin.. Bukti: Arman berhasil melompat sejauh 3,7 m; Didi berhasil melompat sejauh 2,9 m; Bayu melompat sejauh 3,6 m
- Dimensi pengetahuan `classify/conceptual`: Memahami hubungan urutan antar bilangan desimal berdasarkan nilai tempat.. Bukti: 3,7 m; 2,9 m; 3,6 m
- Intended difficulty `classify/Easy`: Soal melibatkan perbandingan langsung tiga bilangan desimal dengan satu angka di belakang koma. Prosedur ini sangat rutin dan familiar bagi siswa kelas 6.. Bukti: Arman berhasil melompat sejauh 3,7 m; Didi berhasil melompat sejauh 2,9 m; Bayu melompat sejauh 3,6 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan desimal adalah materi dasar kelas 6 yang rutin. |

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
Solusi minimum hasil AI: Selisih = 3/10 - 1/8 = 12/40 - 5/40 = 7/40.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ebbbe2dca8111a18604f135a0ca1c4118939df48aafe82d4720fb9633806a2de`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1415 |
| 2 | success | valid / verified | applying | procedural | Medium | 1387 |
| 3 | success | valid / verified | applying | procedural | Medium | 1395 |

Run 1 — solusi: Selisih = 3/10 - 1/8 = 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat (menyamakan penyebut) untuk menyelesaikan operasi pengurangan pecahan dengan penyebut berbeda, yang merupakan penerapan rutin.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan pecahan yang memerlukan langkah-langkah prosedural seperti mencari KPK dan menyesuaikan pembilang.. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait (menentukan KPK, mengubah pecahan, melakukan pengurangan) yang merupakan standar kompetensi kelas 6.. Bukti: 1/8 bagian; 3/10 bagian; selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan operasi pengurangan pecahan dengan penyebut berbeda. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Operasi pecahan dengan penyebut berbeda adalah materi inti kelas 6. Soal ini menuntut ketelitian dalam prosedur standar tanpa jebakan konseptual yang rumit. |

Run 2 — solusi: Selisih = 3/10 - 1/8 = 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat (menyamakan penyebut) untuk menyelesaikan operasi pengurangan pecahan yang berbeda penyebut.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan pecahan dengan penyebut berbeda, yang merupakan pengetahuan prosedural.. Bukti: penggunaan bahasa Indonesia 1/8 bagian; penggunaan bahasa daerah 3/10 bagian
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan langkah rutin (menyamakan penyebut) dan operasi pengurangan pecahan, yang merupakan standar kompetensi kelas 6.. Bukti: 1/8 bagian; 3/10 bagian; selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan operasi pengurangan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Operasi pecahan dengan penyebut berbeda adalah materi inti kelas 6, menuntut ketelitian dalam konversi penyebut. |

Run 3 — solusi: Selisih = 3/10 - 1/8 = 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat (menyamakan penyebut) untuk menyelesaikan operasi pengurangan pecahan dengan penyebut berbeda, yang merupakan aplikasi konsep pecahan dalam konteks rutin.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan pecahan dengan penyebut yang berbeda.. Bukti: pengurangan pecahan; 3/10 - 1/8
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin (mencari KPK, mengubah pecahan ke penyebut yang sama, melakukan pengurangan) yang saling terkait.. Bukti: 1/8 bagian; 3/10 bagian; selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai, KPK, dan operasi pengurangan pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 6 diharapkan sudah menguasai operasi hitung pecahan dengan penyebut berbeda sebagai bagian dari kurikulum standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
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
Solusi minimum hasil AI: Rasio bianglala terhadap roller coaster adalah 4:3. Diketahui roller coaster = 24. Maka bianglala = (4/3) * 24 = 32.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5ab4bbebc25abc1b2551393bc04e3baf8a33782ac6f1b160061aec592dfb5a0c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1556 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1525 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1550 |

Run 1 — solusi: Rasio bianglala terhadap roller coaster adalah 4:3. Diketahui roller coaster = 24. Maka bianglala = (4/3) * 24 = 32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio untuk menentukan nilai yang belum diketahui berdasarkan nilai yang sudah diketahui (roller coaster = 24). Ini adalah prosedur rutin dalam konteks rasio.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua kuantitas (rasio).. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin untuk mencari nilai dalam rasio dengan satu faktor pengali yang jelas. Tidak ada langkah non-rutin atau integrasi representasi yang kompleks.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Roller coaster 24

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan perkalian/pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 6 karena rasio adalah topik standar dan prosedur yang digunakan adalah perkalian/pembagian dasar. |

Run 2 — solusi: Rasio Bianglala:Roller coaster = 4:3. Jumlah Roller coaster = 24. Faktor pengali = 24 / 3 = 8. Jumlah Bianglala = 4 * 8 = 32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio untuk menentukan nilai yang belum diketahui berdasarkan nilai yang sudah ada, yang merupakan prosedur rutin dalam topik rasio.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua kuantitas (konsep rasio).. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin yang umum di kelas 6, yaitu mencari nilai berdasarkan rasio yang diketahui dengan satu langkah pengali.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Roller coaster 24

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian/perkalian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi rasio adalah standar kurikulum kelas 6. Soal ini menggunakan angka yang sederhana dan prosedur yang langsung. |

Run 3 — solusi: Rasio Bianglala:Roller coaster = 4:3. Karena Roller coaster = 24, maka faktor pengali adalah 24/3 = 8. Jumlah Bianglala = 4 * 8 = 32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio untuk menentukan nilai yang belum diketahui berdasarkan nilai yang sudah ada, yang merupakan prosedur rutin dalam konteks rasio.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Berapakah banyak pengunjung yang antre di wahana bianglala
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua kuantitas (rasio), yang merupakan pengetahuan konseptual.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin (mencari nilai berdasarkan rasio) yang umum diajarkan di kelas 6. Langkah-langkahnya jelas dan tidak memerlukan strategi nonrutin.. Bukti: rasio pengunjung yang antre di wahana bianglala terhadap roller coaster adalah 4 : 3; Roller coaster = 24

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan perkalian/pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi rasio adalah kurikulum standar kelas 6. Soal ini menggunakan angka yang sederhana dan prosedur yang langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
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
Solusi minimum hasil AI: Rasio minuman terhadap teman adalah 6 liter : 15 teman = 2 : 5. Untuk 10 teman, kebutuhan minuman = (10 / 5) * 2 = 4 liter.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6865692ff9091dcd027214a0b1ef1325735d995330737b7948ff5e5e5c8ff081`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1468 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1442 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1458 |

Run 1 — solusi: Rasio minuman terhadap teman adalah 6 liter : 15 teman = 2 : 5. Untuk 10 teman, kebutuhan minuman = (10 / 5) * 2 = 4 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menyelesaikan masalah rutin dalam konteks kehidupan sehari-hari.. Bukti: Banyu menyiapkan 6 liter minuman untuk 15 orang teman; berapa liter minuman yang harus disiapkan untuk 10 orang
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (rasio) antara dua besaran.. Bukti: 6 liter minuman untuk 15 orang teman; rasio minuman terhadap tamu 6 : 15
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin perbandingan senilai yang umum diajarkan di kelas 6 dengan angka yang sederhana.. Bukti: 6 liter minuman untuk 15 orang teman; 10 orang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pecahan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Masalah rasio senilai adalah materi standar kelas 6. Prosedur penyelesaiannya langsung dan tidak memerlukan strategi non-rutin. |

Run 2 — solusi: Rasio minuman terhadap teman adalah 6 liter : 15 teman = 2 liter : 5 teman. Untuk 10 teman, kebutuhan minuman adalah (10/5) * 2 liter = 4 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menyelesaikan masalah rutin yang melibatkan perbandingan dua besaran.. Bukti: 6 liter untuk 15 orang; berapa liter minuman yang harus disiapkan untuk 10 orang
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip rasio dan proporsi sebagai hubungan antar variabel.. Bukti: 6 liter untuk 15 orang; rasio minuman terhadap tamu
- Intended difficulty `classify/Easy`: Masalah ini merupakan penerapan langsung dari konsep rasio senilai dengan angka yang sederhana, cocok untuk tingkat kelas 6.. Bukti: 6 liter untuk 15 orang; 10 orang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pecahan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah rasio proporsional adalah materi standar kelas 6 dengan tingkat kompleksitas yang rendah. |

Run 3 — solusi: Rasio minuman terhadap teman adalah 6:15 atau 2:5. Untuk 10 teman, kebutuhan minuman adalah (10/15) * 6 = 4 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menyelesaikan masalah rutin dalam konteks kehidupan sehari-hari.. Bukti: 6 liter minuman untuk 15 orang teman; berapa liter minuman yang harus disiapkan untuk 10 orang
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep rasio) dan penggunaan algoritma untuk mencari nilai yang hilang.. Bukti: 6 liter minuman untuk 15 orang teman; berapa liter minuman yang harus disiapkan
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang melibatkan perbandingan senilai. Siswa kelas 6 diharapkan sudah familiar dengan konsep rasio dan proporsi sederhana.. Bukti: 6 liter minuman untuk 15 orang teman; 10 orang; berapa liter minuman

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pecahan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah perbandingan senilai adalah materi standar kelas 6 yang diselesaikan dengan prosedur rutin. |

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
Solusi minimum hasil AI: Rasio pupuk per bibit adalah 5 gram / 2 bibit = 2,5 gram/bibit. Untuk 11 bibit, pupuk yang diperlukan adalah 11 bibit * 2,5 gram/bibit = 27,5 gram.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4ccf56b7604d2ce03f5e46955269fd7d3838abd5aafbf3eeec95c764574ef4fc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 1526 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1517 |
| 3 | success | valid / verified | applying | procedural | Medium | 1530 |

Run 1 — solusi: Rasio bibit terhadap pupuk adalah 2:5. Untuk 11 bibit, pupuk yang diperlukan adalah (11/2) * 5 = 5,5 * 5 = 27,5 gram.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep proporsi atau rasio senilai untuk menyelesaikan masalah rutin ini.. Bukti: Apabila kalian menanam 2 bibit tanaman diperlukan 5 gram pupuk.; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua besaran (bibit dan pupuk), yang merupakan pengetahuan konseptual.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman
- Intended difficulty `classify/Medium`: Soal ini melibatkan prosedur rutin perbandingan senilai dengan angka yang tidak bulat sempurna (11/2), namun masih dalam cakupan standar kelas 6.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; 11 bibit tanaman

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar rasio dan perkalian pecahan/desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari rasio dan proporsi. Soal ini menuntut penerapan algoritma rasio yang umum. |

Run 2 — solusi: Rasio pupuk per bibit adalah 5/2 = 2,5 gram per bibit. Untuk 11 bibit, pupuk yang diperlukan adalah 11 * 2,5 = 27,5 gram.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk situasi rutin yang melibatkan perbandingan dua besaran.. Bukti: diperlukan 5 gram pupuk. Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua variabel (bibit dan pupuk).. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan perhitungan rasio yang tidak menghasilkan bilangan bulat (faktor pengali 5,5), sehingga memerlukan ketelitian lebih daripada sekadar kelipatan bilangan bulat sederhana.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; 11 bibit tanaman

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, perkalian pecahan atau desimal, dan konsep proporsi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 6 karena rasio dan proporsi adalah materi standar, namun penggunaan angka yang menghasilkan desimal meningkatkan tuntutan kognitif dibanding soal rasio dasar. |

Run 3 — solusi: Rasio pupuk per bibit adalah 5/2 = 2,5 gram/bibit. Untuk 11 bibit, pupuk yang diperlukan adalah 11 x 2,5 = 27,5 gram.
- Domain kognitif `classify/applying`: Siswa perlu memilih dan menerapkan prosedur perbandingan senilai (proporsi) untuk menyelesaikan masalah rutin yang melibatkan rasio.. Bukti: Apabila kalian menanam 2 bibit tanaman diperlukan 5 gram pupuk. Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik perbandingan senilai (proporsionalitas) yang merupakan prosedur standar dalam matematika.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; Berapa gram pupuk yang diperlukan jika akan menanam 11 bibit tanaman?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah rutin (menentukan rasio satuan atau faktor pengali) dan memerlukan pemahaman konsep proporsi, bukan sekadar operasi aritmatika tunggal.. Bukti: 2 bibit tanaman diperlukan 5 gram pupuk; 11 bibit tanaman

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan operasi perkalian/pembagian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 6 SD yang sedang mempelajari perbandingan senilai. Tingkat kesulitan menengah karena melibatkan bilangan yang menghasilkan desimal (2,5) dan faktor pengali non-integer (5,5). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3007`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep perbandingan senilai (proporsi) untuk menyelesaikan masalah rutin ini. Ini adalah penerapan prosedur standar dalam situasi yang diberikan.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua besaran, yang merupakan konsep dasar dalam rasio.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya rutin, angka yang digunakan (11 dan 2) menghasilkan faktor pengali desimal (5,5) atau rasio satuan desimal (2,5), yang meningkatkan tuntutan kognitif dibandingkan soal rasio dengan angka bulat sederhana.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar rasio, proporsi, dan operasi perkalian/pembagian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 6 SD yang sedang mempelajari perbandingan senilai. Tingkat kesulitan menengah karena melibatkan bilangan yang menghasilkan desimal, menuntut ketelitian lebih. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
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
Solusi minimum hasil AI: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air (faktor pengali 8/4 = 2), maka jumlah jahe adalah 12 x 2 = 24 buah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `06ed5ee55db595bbbb5b3e1c50142b8059c1dee11867a794c86b7bb29a0ce112`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1477 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1517 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1475 |

Run 1 — solusi: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air (faktor pengali 8/4 = 2), maka jumlah jahe adalah 12 x 2 = 24 buah.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menentukan jumlah bahan yang proporsional dengan perubahan volume air.. Bukti: Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep rasio) antara dua variabel.. Bukti: Bahan membuat Wedang Jahe untuk 4 liter air: 12 Jahe merah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 6 karena melibatkan perbandingan senilai sederhana dengan faktor pengali bilangan bulat yang mudah.. Bukti: 4 liter air: 12 Jahe merah; 8 liter air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan perkalian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perbandingan senilai dengan kelipatan bilangan bulat adalah materi standar kelas 6 yang rutin. |

Run 2 — solusi: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air, faktor pengalinya adalah 8/4 = 2. Maka, jumlah jahe yang dibutuhkan adalah 12 x 2 = 24 buah.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menentukan jumlah bahan yang proporsional dengan peningkatan volume air.. Bukti: Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional (konsep rasio) antara dua besaran.. Bukti: Bahan membuat Wedang Jahe untuk 4 liter air: 12 Jahe merah
- Intended difficulty `classify/Easy`: Soal ini menggunakan angka yang sederhana dan hubungan kelipatan yang jelas (8 adalah dua kali 4), sehingga prosedurnya sangat rutin bagi siswa kelas 6.. Bukti: 4 liter air: 12 Jahe merah; membuat wedang jahe sebanyak 8 liter air

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
| gradeRelativeRationale | Konsep perbandingan senilai adalah materi standar kelas 6, dan angka yang digunakan memudahkan perhitungan tanpa perlu alat bantu. |

Run 3 — solusi: Rasio air terhadap jahe adalah 4 liter : 12 jahe. Untuk 8 liter air (2 kali lipat dari 4 liter), jumlah jahe yang diperlukan adalah 12 x 2 = 24 jahe.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio senilai untuk menentukan jumlah bahan yang proporsional dengan perubahan volume air.. Bukti: Berapa buah jahe merah yang diperlukan jika kalian akan membuat wedang jahe sebanyak 8 liter air?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara dua besaran (konsep rasio).. Bukti: Bahan membuat Wedang Jahe untuk 4 liter air: 12 Jahe merah
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang melibatkan satu keputusan utama (menentukan faktor pengali rasio) dengan angka yang sederhana.. Bukti: 4 liter air: 12 Jahe merah; 8 liter air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbandingan senilai dan perkalian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah diajarkan konsep rasio dan perbandingan senilai sebagai materi standar. |

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
Solusi minimum hasil AI: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan, maka 36/6 = 6 kali. Lengkuas = 1,5 tahun = 18 bulan, maka 36/18 = 2 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `39c44177324fd7190804c2e83e2b844d98dbd30d6a3d4fea195ab8d1360397d7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1619 |
| 2 | success | valid / verified | applying | procedural | Medium | 1655 |
| 3 | success | valid / verified | applying | procedural | Medium | 1634 |

Run 1 — solusi: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan, maka 36/6 = 6 kali. Lengkuas = 1,5 tahun = 18 bulan, maka 36/18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio dan konversi satuan waktu (tahun ke bulan) untuk membandingkan masa panen, yang merupakan penerapan prosedur rutin.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antar satuan waktu dan penggunaan algoritma pembagian untuk menentukan rasio.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah; Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan waktu yang konsisten (tahun ke bulan) sebelum melakukan operasi pembagian. Ini adalah prosedur rutin yang melibatkan beberapa langkah terkait.. Bukti: 1,5 tahun; 3 tahun; 6 bulan; Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan operasi pembagian dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan konversi satuan waktu dan perbandingan sederhana sebagai bagian dari kurikulum matematika dasar. |

Run 2 — solusi: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Frekuensi kencur = 36 / 6 = 6 kali. Lengkuas = 1,5 tahun = 18 bulan. Frekuensi lengkuas = 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur konversi satuan waktu (tahun ke bulan) dan menerapkan operasi pembagian untuk menentukan rasio frekuensi panen dalam durasi yang sama.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan prosedur konversi satuan waktu yang konsisten (tahun ke bulan) untuk membandingkan durasi panen tanaman yang berbeda.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah; Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan waktu yang berbeda (tahun ke bulan) sebelum melakukan pembagian. Ini adalah tugas rutin yang melibatkan beberapa langkah terkait.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah; Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan waktu (tahun ke bulan) dan konsep pembagian sebagai rasio. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan konversi satuan waktu dan operasi hitung dasar untuk membandingkan dua besaran. |

Run 3 — solusi: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Frekuensi kencur = 36 / 6 = 6 kali. Lengkuas = 1,5 tahun = 18 bulan. Frekuensi lengkuas = 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur konversi satuan waktu (tahun ke bulan) dan menerapkan operasi pembagian untuk membandingkan rasio waktu panen, yang merupakan penerapan konsep dalam situasi rutin.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antar satuan waktu (konseptual) dan penggunaan algoritma pembagian untuk menentukan frekuensi (prosedural).. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah; Berapa kali kencur dan lengkuas dapat dipanen
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi satuan waktu yang konsisten sebelum melakukan perbandingan rasio, melibatkan beberapa langkah rutin yang saling terkait.. Bukti: 1,5 tahun; 3 tahun; 6 bulan; Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan operasi pembagian dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu melakukan konversi satuan waktu dan perbandingan sederhana, namun soal ini menuntut ketelitian dalam menyamakan satuan sebelum membagi. |

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
Solusi minimum hasil AI: Waktu = (3.000 kata / 1.200 kata) * 1 jam = 2,5 jam.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0808ee1e4ac29d55701632d0b226ebebfc64fbbd380d538da1f1d9036345f74f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1368 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1235 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1401 |

Run 1 — solusi: Waktu = (3.000 kata / 1.200 kata) * 1 jam = 2,5 jam.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio atau perbandingan senilai untuk menyelesaikan masalah rutin ini.. Bukti: Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara jumlah kata dan waktu.. Bukti: 1.200 kata dalam waktu 1 jam; 3.000 kata
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin perbandingan senilai yang umum diajarkan di kelas 6 dengan beban kalkulasi yang rendah.. Bukti: 1.200 kata dalam waktu 1 jam; 3.000 kata

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah perbandingan senilai sederhana adalah standar kompetensi kelas 6. |

Run 2 — solusi: Rasio kecepatan adalah 1.200 kata/jam. Untuk 3.000 kata, waktu yang diperlukan adalah 3.000 / 1.200 = 2,5 jam.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio atau perbandingan senilai untuk menyelesaikan masalah rutin.. Bukti: Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman tentang hubungan proporsional antara jumlah kata dan waktu.. Bukti: 1.200 kata dalam waktu 1 jam; 3.000 kata
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah perbandingan senilai standar yang rutin bagi siswa kelas 6.. Bukti: 1.200 kata dalam waktu 1 jam; 3.000 kata

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah perbandingan senilai adalah materi standar kelas 6 yang diselesaikan dengan prosedur pembagian sederhana. |

Run 3 — solusi: Waktu = (3.000 kata / 1.200 kata) * 1 jam = 2,5 jam.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio atau perbandingan senilai untuk menyelesaikan masalah rutin ini.. Bukti: Seorang penulis berita dapat mengetik sebanyak 1.200 kata dalam waktu 1 jam.; Berapa lama waktu yang diperlukan untuk menuliskan 3.000 kata?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan proporsional antara jumlah kata dan waktu, yang merupakan konsep dasar dalam rasio.. Bukti: 1.200 kata dalam waktu 1 jam; 3.000 kata
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin perbandingan senilai dengan angka yang relatif sederhana, sesuai untuk tingkat kelas 6.. Bukti: 1.200 kata dalam waktu 1 jam; 3.000 kata

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan pembagian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah perbandingan senilai adalah materi standar kelas 6 yang diselesaikan dengan prosedur rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

![Gambar sumber soal 14](<../images/kelas6_panduan_siswa_kelas6.pdf-0098-07.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Terdapat 4 kubus yang terlihat jelas (merah muda, hijau, ungu, kuning). Kubus merah muda berada di atas, sehingga memerlukan 1 kubus penyangga di bawahnya yang tidak terlihat dari sudut pandang ini. Total = 4 + 1 = 5 kubus.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0098-07.png. Transkripsi visual: Gambar menunjukkan struktur isometrik yang terdiri dari kubus-kubus. Terlihat 4 kubus di permukaan: 1 kubus merah muda di atas, 1 kubus hijau di kiri atas, 1 kubus ungu di kiri bawah, dan 1 kubus kuning di kanan bawah. Struktur ini memerlukan satu kubus tambahan di bagian belakang bawah kubus merah muda untuk menopang kubus merah muda tersebut agar tidak melayang, sehingga totalnya adalah 5 kubus.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6bced3f48d162fa9e2e3215dcc4afc660f2ad0ce3b1c566d0a6f74900e3e0136`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2631 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2603 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2632 |

Run 1 — solusi: Terdapat 4 kubus yang terlihat jelas (merah muda, hijau, ungu, kuning). Kubus merah muda berada di atas, sehingga memerlukan 1 kubus penyangga di bawahnya yang tidak terlihat dari sudut pandang ini. Total = 4 + 1 = 5 kubus.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan penalaran spasial untuk menyimpulkan keberadaan kubus yang tidak terlihat (tersembunyi) berdasarkan struktur fisik yang logis, bukan sekadar menghitung objek yang tampak.. Bukti: Berapa kubus yang diperlukan?; selain 4 kubus yang tampak berwarna, ada 1 kubus tersembunyi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur spasial dan hubungan antar bagian dalam bangun ruang (konsep volume/susunan kubus), bukan sekadar menghafal fakta atau mengikuti prosedur algoritma standar.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut
- Intended difficulty `classify/Medium`: Soal ini memerlukan kemampuan visualisasi spasial untuk mengidentifikasi bagian yang tidak terlihat. Bagi siswa kelas 6, ini adalah tugas yang menuntut penalaran di luar pengamatan langsung.. Bukti: ada 1 kubus tersembunyi di bagian belakang yang menopang susunan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan susunan kubus. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan Medium karena siswa harus melakukan inferensi spasial (membayangkan bagian tersembunyi) yang melampaui sekadar menghitung objek yang terlihat. |

Run 2 — solusi: Struktur terdiri dari 4 kubus yang terlihat (1 merah muda, 1 hijau, 1 ungu, 1 kuning). Untuk membentuk susunan yang stabil seperti pada gambar, diperlukan 1 kubus tambahan di bagian belakang sebagai penopang. Total = 4 + 1 = 5 kubus.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan penalaran spasial untuk mengidentifikasi kubus yang tersembunyi (tidak terlihat langsung) berdasarkan struktur yang tampak, yang merupakan bentuk integrasi informasi visual.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut; Berapa kubus yang diperlukan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur ruang dan bagaimana objek 3D disusun, bukan sekadar menghafal fakta atau mengikuti algoritma prosedural.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut
- Intended difficulty `classify/Medium`: Soal ini memerlukan penalaran spasial untuk membayangkan bagian yang tidak terlihat. Bagi siswa kelas 6, ini adalah tugas yang menantang karena melibatkan visualisasi 3D.. Bukti: Berapa kubus yang diperlukan?; lupa 1 kubus tersembunyi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang kubus dan visualisasi objek 3D. |
| dependentSteps | 2 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan Medium karena siswa harus melakukan inferensi spasial (membayangkan kubus tersembunyi) yang tidak langsung terlihat, melampaui sekadar menghitung objek yang tampak. |

Run 3 — solusi: Terdapat 4 kubus yang terlihat secara visual. Karena kubus merah muda di posisi atas tidak memiliki tumpuan di bawahnya dalam pandangan 2D, diperlukan 1 kubus tersembunyi di belakang untuk menopang struktur tersebut. Total: 4 + 1 = 5 kubus.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan penalaran spasial untuk menyimpulkan keberadaan kubus yang tidak terlihat (tersembunyi) berdasarkan prinsip stabilitas struktur, bukan sekadar menghitung objek yang tampak.. Bukti: Berapa kubus yang diperlukan?; selain 4 kubus yang tampak berwarna, ada 1 kubus tersembunyi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur ruang dan bagaimana objek 3D disusun, yang melampaui sekadar prosedur menghitung.. Bukti: Tentukan cara menyusun kubus untuk membentuk bangun berikut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan penalaran spasial untuk mengidentifikasi bagian yang tidak terlihat (hidden parts) dalam representasi 3D, yang merupakan langkah tambahan di luar pengamatan langsung.. Bukti: Berapa kubus yang diperlukan?; selain 4 kubus yang tampak berwarna, ada 1 kubus tersembunyi

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
| gradeRelativeRationale | Untuk kelas 6, kemampuan memvisualisasikan objek tersembunyi dalam struktur kubus adalah tantangan yang sesuai untuk melatih penalaran spasial. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 142/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000067; applying=0.999933; reasoning=0.000000 | applying | 0.999933 | 0.000649 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.180073; conceptual=0.787301; procedural=0.032626; metacognitive=0.000000 | conceptual | 0.787301 | 0.439056 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.677727; Medium=0.317265; Hard=0.005008 | Easy | 0.677727 | 0.595654 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999933; −Σp ln(p) = 0.000714; H = 0.000714/ln(3) = 0.000649; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.787301; −Σp ln(p) = 0.608661; H = 0.608661/ln(4) = 0.439056; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.677727; −Σp ln(p) = 0.654393; H = 0.654393/ln(3) = 0.595654; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan struktur isometrik yang terdiri dari kubus-kubus. Terlihat 4 kubus di permukaan: 1 kubus merah muda di atas, 1 kubus hijau di kiri atas, 1 kubus ungu di kiri bawah, dan 1 kubus kuning di kanan bawah. Struktur ini memerlukan satu kubus tambahan di bagian belakang bawah kubus merah muda untuk menopang kubus merah muda tersebut agar tidak melayang, sehingga totalnya adalah 5 kubus.
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

![Gambar sumber soal 15](<../images/kelas6_panduan_siswa_kelas6.pdf-0098-00.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Gambar memperlihatkan tumpukan vertikal dengan dua garis pemisah horizontal, yang membagi objek menjadi 3 bagian balok yang identik.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0098-00.png. Transkripsi visual: Gambar menunjukkan sebuah bangun ruang berbentuk tumpukan vertikal yang terdiri dari tiga balok identik yang disusun ke atas, dengan garis pemisah horizontal yang jelas antara setiap balok.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `13b51b4bf9f74fad6b547d0c88c529eb36c065c4f24877a1a880ecaefc0fb40a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2479 |
| 2 | success | valid / verified | knowing | factual | Easy | 2433 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2432 |

Run 1 — solusi: Visualisasi menunjukkan tumpukan vertikal dengan tiga segmen yang jelas, yang masing-masing merepresentasikan satu balok. Jadi, totalnya adalah 3 balok.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengenali dan menghitung jumlah objek yang terlihat secara langsung dalam representasi visual, yang merupakan proses kognitif tingkat dasar.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?; gambar menunjukkan tiga balok identik yang ditumpuk vertikal
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang objek geometris sederhana dan kemampuan untuk mengidentifikasi komponen penyusunnya secara visual.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung tanpa perhitungan kompleks atau strategi khusus.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan dasar mengenali bentuk bangun ruang dan menghitung objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 6, soal ini terlalu mudah karena hanya melibatkan pengamatan visual satu langkah tanpa konsep geometri yang mendalam. |

Run 2 — solusi: Visualisasi menunjukkan tumpukan vertikal dengan tiga segmen yang jelas, sehingga total balok adalah 3.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengenali dan menghitung jumlah komponen visual yang terlihat secara langsung tanpa perlu strategi atau manipulasi kompleks.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang pengenalan objek geometris sederhana dan jumlah komponennya.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan observasi visual langsung terhadap tumpukan objek yang jelas.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?

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
| gradeRelativeRationale | Untuk kelas 6, soal ini terlalu sederhana karena hanya memerlukan pengamatan visual langsung tanpa analisis geometri yang mendalam. |

Run 3 — solusi: Visualisasi menunjukkan tumpukan vertikal dengan dua garis pemisah horizontal, yang membagi objek menjadi 3 balok identik.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengenali dan menghitung jumlah objek visual yang terlihat secara langsung tanpa perlu melakukan operasi matematika atau strategi kompleks.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dasar bangun ruang dan bagaimana objek-objek tersebut disusun (kategori objek).. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan observasi visual langsung terhadap objek yang tidak tertutup atau tersembunyi.. Bukti: Berapa balok yang dibutuhkan untuk menyusun bangun ruang berikut?

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
| gradeRelativeRationale | Untuk kelas 6, soal ini terlalu mendasar karena hanya melibatkan pengenalan visual sederhana tanpa tantangan spasial atau perhitungan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3643`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya memerlukan pengenalan visual langsung terhadap objek yang disajikan tanpa perlu strategi atau manipulasi kognitif yang kompleks.
- Dimensi pengetahuan `factual`: Soal ini menguji pengenalan objek geometris sederhana dan kemampuan menghitung komponen visual yang terlihat secara langsung.
- Intended difficulty `Easy`: Soal ini sangat mendasar, hanya memerlukan observasi visual langsung terhadap tumpukan objek yang jelas tanpa tantangan spasial atau perhitungan.

Profil difficulty hasil adjudikasi:

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
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 6, soal ini terlalu sederhana karena hanya melibatkan pengamatan visual satu langkah tanpa konsep geometri yang mendalam. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 90/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.220523; applying=0.779477; reasoning=0.000000 | applying | 0.779477 | 0.480214 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.692302; conceptual=0.300466; procedural=0.007232; metacognitive=0.000000 | factual | 0.692302 | 0.469969 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.876615; Medium=0.120943; Hard=0.002441 | Easy | 0.876615 | 0.350995 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.779477; −Σp ln(p) = 0.527569; H = 0.527569/ln(3) = 0.480214; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.692302; −Σp ln(p) = 0.651515; H = 0.651515/ln(4) = 0.469969; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.876615; −Σp ln(p) = 0.385608; H = 0.385608/ln(3) = 0.350995; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah bangun ruang berbentuk tumpukan vertikal yang terdiri dari tiga balok identik yang disusun ke atas, dengan garis pemisah horizontal yang jelas antara setiap balok.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `b56626ecf5289108fa7302f7`

Berikut adalah sebuah dadu. Gambar berikut adalah dadu yang sama yang dilihat dari arah berbeda.<br><br>Jika mata dadu pada dua sisi yang berlawanan berjumlah 7, ada berapa mata dadu pada sisi yang kosong?

| Opsi | Isi |
|---|---|
| A | 3 mata dadu |
| B | 4 mata dadu |
| C | 1 mata dadu |
| D | 2 mata dadu |

![Gambar sumber soal 16](<../images/kelas6_panduan_siswa_kelas6.pdf-0104-02.png>)


![Gambar sumber soal 16](<../images/kelas6_panduan_siswa_kelas6.pdf-0104-06.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Dadu memiliki 6 sisi dengan angka 1-6. Sisi yang terlihat pada kedua gambar adalah 6, 5, 4. Sisi yang berlawanan dengan 6 adalah 1 (6+1=7), berlawanan dengan 5 adalah 2 (5+2=7), dan berlawanan dengan 4 adalah 3 (4+3=7). Karena 1, 2, 4, 5, 6 sudah teridentifikasi, maka sisi kosong haruslah 3.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0104-02.png, images/kelas6_panduan_siswa_kelas6.pdf-0104-06.png. Transkripsi visual: Dua gambar dadu yang sama. Gambar 1 menunjukkan sisi dengan 6, 4, dan 5 mata dadu. Gambar 2 menunjukkan sisi dengan 6, 5, dan satu sisi kosong yang tidak terlihat di gambar 1. Aturan dadu standar: sisi berlawanan berjumlah 7.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5eefefd96b99ecaf05fc00d75e88c2e4dd203a29d266092ddf477411004853f2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 3798 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 3832 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3849 |

Run 1 — solusi: Dadu memiliki 6 sisi dengan angka 1-6. Sisi yang terlihat pada kedua gambar adalah 6, 5, 4. Sisi yang berlawanan dengan 6 adalah 1 (6+1=7), berlawanan dengan 5 adalah 2 (5+2=7), dan berlawanan dengan 4 adalah 3 (4+3=7). Karena 1, 2, 4, 5, 6 sudah teridentifikasi, maka sisi kosong haruslah 3.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi dari dua perspektif visual dadu dan menerapkan aturan konsep dadu standar (jumlah sisi berlawanan adalah 7) untuk menyimpulkan nilai sisi yang tidak terlihat.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7; ada berapa mata dadu pada sisi yang kosong?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip atau struktur konsep dadu standar, di mana hubungan antara sisi-sisi yang berlawanan bersifat tetap.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7
- Intended difficulty `classify/Medium`: Soal ini memerlukan penalaran spasial untuk menghubungkan dua tampilan objek yang berbeda dan menerapkan aturan deduktif sederhana. Ini melampaui prosedur rutin satu langkah.. Bukti: Gambar berikut adalah dadu yang sama yang dilihat dari arah berbeda; sisi yang kosong

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang dadu standar dan konsep penjumlahan hingga 7. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, tugas visualisasi spasial ini menuntut kemampuan menghubungkan dua representasi visual, yang merupakan tantangan kognitif menengah. |

Run 2 — solusi: Sisi yang terlihat adalah 4, 5, dan 6. Sisi berlawanan dari 6 adalah 1 (7-6=1). Sisi berlawanan dari 5 adalah 2 (7-5=2). Sisi yang tersisa untuk sisi kosong adalah 3.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi visual dari dua orientasi dadu yang berbeda dan menerapkan aturan konsep dadu (jumlah sisi berlawanan adalah 7) untuk menyimpulkan nilai sisi yang tidak terlihat.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7, ada berapa mata dadu pada sisi yang kosong?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip atau struktur konsep dadu standar, bukan sekadar menghafal fakta atau mengikuti algoritma prosedural murni.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7
- Intended difficulty `classify/Medium`: Soal ini memerlukan penalaran spasial untuk menghubungkan dua representasi visual dan menerapkan aturan deduktif. Ini melampaui prosedur rutin sederhana.. Bukti: Gambar berikut adalah dadu yang sama yang dilihat dari arah berbeda.; ada berapa mata dadu pada sisi yang kosong?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang dadu standar dan konsep penjumlahan hingga 7. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, ini adalah soal penalaran yang menantang namun dapat diakses karena melibatkan visualisasi spasial dasar yang sesuai dengan kurikulum geometri/spasial. |

Run 3 — solusi: Sisi yang terlihat pada dadu adalah 4, 5, dan 6. Sisi yang berlawanan dengan 4 adalah 3 (karena 4+3=7), sisi berlawanan dengan 5 adalah 2 (karena 5+2=7), dan sisi berlawanan dengan 6 adalah 1 (karena 6+1=7). Sisi kosong pada gambar 2 adalah sisi yang belum terlihat di antara angka 1, 2, 3, 4, 5, 6. Karena 1, 2, 4, 5, 6 sudah teridentifikasi posisinya, maka sisi kosong adalah 3.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi visual dari dua orientasi dadu yang berbeda dan menerapkan aturan konsep dadu standar (jumlah sisi berlawanan adalah 7) untuk menyimpulkan nilai sisi yang tidak terlihat.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7; ada berapa mata dadu pada sisi yang kosong?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat geometris dadu standar dan hubungan antar sisi, bukan sekadar menghafal fakta atau menjalankan algoritma prosedural murni.. Bukti: Jika mata dadu pada dua sisi yang berlawanan berjumlah 7
- Intended difficulty `classify/Medium`: Soal ini memerlukan penalaran spasial untuk menghubungkan dua perspektif objek yang sama. Ini melampaui prosedur rutin karena siswa harus memetakan sisi yang terlihat ke sisi yang tersembunyi.. Bukti: Gambar berikut adalah dadu yang sama yang dilihat dari arah berbeda; ada berapa mata dadu pada sisi yang kosong?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang dadu standar dan penjumlahan hingga 7. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, soal ini menantang kemampuan visualisasi spasial namun masih dalam lingkup kemampuan kognitif yang diharapkan pada tingkat sekolah dasar akhir. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 140/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000034; applying=0.999966; reasoning=0.000000 | applying | 0.999966 | 0.000347 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.025704; conceptual=0.969572; procedural=0.004724; metacognitive=0.000000 | conceptual | 0.969572 | 0.107742 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.724350; Medium=0.270722; Hard=0.004928 | Easy | 0.724350 | 0.558443 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999966; −Σp ln(p) = 0.000381; H = 0.000381/ln(3) = 0.000347; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.969572; −Σp ln(p) = 0.149362; H = 0.149362/ln(4) = 0.107742; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.724350; −Σp ln(p) = 0.613512; H = 0.613512/ln(3) = 0.558443; T = 0.953328.


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
Transkripsi visual: Dua gambar dadu yang sama. Gambar 1 menunjukkan sisi dengan 6, 4, dan 5 mata dadu. Gambar 2 menunjukkan sisi dengan 6, 5, dan satu sisi kosong yang tidak terlihat di gambar 1. Aturan dadu standar: sisi berlawanan berjumlah 7.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
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
Solusi minimum hasil AI: Jarak horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Jarak vertikal dari 1 ke 2 adalah 1 langkah. Total langkah = 2 + 1 = 3 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `99fae968e625de5a26ff19443b55cea1748dec06e0abc4c1d1d810d02e8373b2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1481 |
| 2 | success | valid / verified | applying | procedural | Medium | 1510 |
| 3 | success | valid / verified | applying | procedural | Medium | 1528 |

Run 1 — solusi: Jarak horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Jarak vertikal dari 1 ke 2 adalah 1 langkah. Total langkah = 2 + 1 = 3 kali rebahan.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada bidang koordinat dan menerjemahkan jarak antar titik menjadi jumlah langkah (roll) kubus, yang merupakan penerapan konsep pada situasi rutin.. Bukti: dipindahkan ke (D,2); direbahkan ke salah satu sisi tegaknya; Berapa kali kubus tersebut direbahkan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara koordinat grid dan pergerakan fisik objek (kubus) dalam ruang dua dimensi.. Bukti: sistem berpetak; jarak antara garis-garis horizontal dan garis-garis vertikal
- Intended difficulty `classify/Easy`: Soal ini memerlukan pemahaman spasial dasar dan perhitungan langkah yang rutin bagi siswa kelas 6, dengan beban kognitif yang rendah.. Bukti: (F,1) dan akan dipindahkan ke (D,2); tidak boleh diangkat, tetapi direbahkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius dan konsep jarak antar titik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 6 karena melibatkan navigasi grid sederhana yang merupakan materi standar, tanpa kompleksitas strategi non-rutin. |

Run 2 — solusi: Jarak horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Jarak vertikal dari 1 ke 2 adalah 1 langkah. Total langkah = 2 + 1 = 3.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada bidang koordinat dan menerjemahkan jarak antar titik menjadi jumlah langkah (roll) yang diperlukan, yang merupakan penerapan prosedur pada situasi rutin.. Bukti: kubus terletak pada (F,1) dan akan dipindahkan ke (D,2); Berapa kali kubus tersebut direbahkan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara jarak pada sistem koordinat dan jumlah langkah fisik (prosedur) yang diperlukan untuk memindahkan objek.. Bukti: Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman koordinat dan perhitungan langkah dalam dua dimensi (horizontal dan vertikal) yang digabungkan, bukan sekadar operasi satu arah.. Bukti: F,1; D,2; Berapa kali kubus tersebut direbahkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius dan konsep jarak antar titik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 6 sudah mempelajari koordinat kartesius; soal ini menguji kemampuan mereka menerapkan konsep tersebut dalam konteks pergerakan objek. |

Run 3 — solusi: Jarak horizontal dari F ke D adalah 2 satuan (F ke E, E ke D). Jarak vertikal dari 1 ke 2 adalah 1 satuan. Total langkah rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jarak pada sistem koordinat (grid) dan menerapkan konsep pergerakan objek (kubus) yang direbahkan, yang merupakan penerapan prosedur rutin pada situasi spasial.. Bukti: kubus terletak pada (F,1) dan akan dipindahkan ke (D,2); Berapa kali kubus tersebut direbahkan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara jarak pada grid dan jumlah langkah pergerakan objek, yang merupakan konsep prosedural dalam navigasi grid.. Bukti: jarak antara garis-garis horizontal dan garis-garis vertikal; Berapa kali kubus tersebut direbahkan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman koordinat kartesius sederhana dan translasi spasial, namun prosedurnya rutin dan tidak melibatkan strategi non-rutin yang kompleks.. Bukti: kubus terletak pada (F,1) dan akan dipindahkan ke (D,2); tidak boleh diangkat, tetapi direbahkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat grid dan konsep jarak. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 6 karena melibatkan pemahaman koordinat dan logika pergerakan sederhana yang umum diajarkan pada tingkat tersebut. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `2990`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep jarak pada sistem koordinat grid untuk menentukan jumlah langkah (roll) yang diperlukan. Ini adalah penerapan prosedur rutin pada situasi spasial.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana menerjemahkan jarak koordinat menjadi jumlah langkah fisik (roll) pada grid.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan integrasi dua dimensi pergerakan (horizontal dan vertikal) pada sistem koordinat, yang sedikit lebih kompleks daripada pergerakan satu arah, namun tetap merupakan prosedur rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat grid dan konsep jarak. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 6 karena melibatkan pemahaman koordinat dan logika pergerakan sederhana yang umum diajarkan pada tingkat tersebut. |

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
Solusi minimum hasil AI: Jarak horizontal dari B ke D adalah 2 langkah (B ke C, C ke D). Jarak vertikal dari 6 ke 3 adalah 3 langkah (6 ke 5, 5 ke 4, 4 ke 3). Jadi, 2 langkah ke kanan dan 3 langkah ke bawah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c7174b449e706d6b4b898882e14eeb3ea02c74e56fa3a320e5e428e262680aa4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1508 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1473 |
| 3 | success | valid / verified | applying | procedural | Easy | 1450 |

Run 1 — solusi: Jarak horizontal dari B ke D adalah 2 langkah (B ke C, C ke D). Jarak vertikal dari 6 ke 3 adalah 3 langkah (6-5, 5-4, 4-3). Jadi, 2 langkah ke kanan dan 3 langkah ke bawah.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang sistem koordinat petak untuk menentukan perpindahan horizontal dan vertikal. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang bagaimana koordinat (huruf dan angka) merepresentasikan posisi dan bagaimana menghitung selisih langkah antar posisi tersebut, yang merupakan pengetahuan prosedural.. Bukti: Dengan sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun.
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin yang familiar bagi siswa kelas 6 dalam membaca koordinat kartesius sederhana. Tidak ada jebakan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat (baris dan kolom/huruf dan angka). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah terbiasa dengan sistem koordinat sederhana. Menghitung selisih langkah adalah keterampilan dasar yang sesuai untuk tingkat kesulitan rendah. |

Run 2 — solusi: Jarak horizontal dari B ke D adalah 2 langkah (B ke C, C ke D). Jarak vertikal dari 6 ke 3 adalah 3 langkah (6-5-4-3). Jadi, 2 langkah ke kanan dan 3 langkah ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman sistem koordinat sederhana untuk menentukan perpindahan posisi. Ini adalah penerapan prosedur rutin pada situasi yang familiar.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana koordinat (huruf dan angka) merepresentasikan posisi dalam sistem grid, yang merupakan pengetahuan konseptual tentang sistem koordinat.. Bukti: Dengan sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun.
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu keputusan utama (menghitung selisih posisi). Tidak ada kompleksitas strategi atau integrasi representasi yang tinggi.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius sederhana (grid). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah sangat familiar dengan konsep koordinat grid sederhana, sehingga soal ini termasuk kategori mudah. |

Run 3 — solusi: Jarak horizontal dari B ke D adalah 2 langkah (B ke C, C ke D). Jarak vertikal dari 6 ke 3 adalah 3 langkah (6 ke 5, 5 ke 4, 4 ke 3). Maka, 2 langkah ke kanan dan 3 langkah ke bawah.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep sistem koordinat untuk menentukan perpindahan posisi pada grid, yang merupakan prosedur rutin.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur menghitung selisih posisi pada sistem koordinat kartesius sederhana.. Bukti: sistem berpetak dapat ditentukan jarak horizontal/ mendatar dan jarak vertikal/menurun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 6, melibatkan perhitungan selisih sederhana pada sumbu horizontal dan vertikal tanpa kompleksitas tambahan.. Bukti: Tentukan jarak antara titik-titik berikut: dari (B,6) ke (D,3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat dan konsep jarak pada grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi koordinat adalah standar kelas 6, soal ini langsung menguji pemahaman dasar tanpa jebakan logika yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2907`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur rutin untuk menghitung selisih posisi pada sistem koordinat grid sederhana.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau teknik menghitung langkah dalam sistem koordinat.
- Intended difficulty `Easy`: Soal ini bersifat rutin, menggunakan representasi grid yang familiar, dan hanya memerlukan perhitungan selisih sederhana tanpa kendala yang saling berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat (grid) dan konsep jarak. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi koordinat adalah standar kelas 6. Soal ini menguji pemahaman dasar tanpa jebakan logika yang rumit. |

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

![Gambar sumber soal 19](<../images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, elemen berikutnya dalam urutan adalah kelinci.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Baris b menampilkan urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Pola berulang setiap tiga elemen: {kupu-kupu, kelinci, kelinci}.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6d6e6637c4983c26ea53fcbef10bd67f0ac0f70a1b5ffd681484320df7ed88d2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2587 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2592 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2617 |

Run 1 — solusi: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, elemen berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengenali aturan pengulangan dalam urutan visual dan menerapkan aturan tersebut untuk memprediksi elemen berikutnya. Ini adalah proses applying karena melibatkan penerapan konsep pola rutin.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan konsep dasar dalam matematika pola.. Bukti: Amati setiap pola berikut; pola berulang tiga gambar
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana untuk siswa kelas 6. Pola berulang tiga elemen adalah tugas yang sangat rutin dan familiar, dengan beban kognitif yang rendah.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

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
| distractorQuality | weak |
| gradeRelativeRationale | Tingkat kesulitan ini jauh di bawah ekspektasi kelas 6, lebih sesuai untuk tingkat awal sekolah dasar. |

Run 2 — solusi: Pola baris b adalah pengulangan tiga gambar: kupu-kupu, kelinci, kelinci. Urutan yang diberikan berakhir pada kupu-kupu, sehingga gambar berikutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengenali struktur pengulangan (kupu-kupu, kelinci, kelinci) dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses penerapan pola rutin.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating pattern), yang merupakan pengetahuan konseptual tentang struktur urutan.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar dan rutin, melibatkan pengenalan pola visual sederhana dengan satu aturan pengulangan yang jelas. Sangat mudah bagi siswa kelas 6.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya

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
| gradeRelativeRationale | Materi pola visual seperti ini biasanya diajarkan di kelas rendah (SD awal). Untuk kelas 6, ini dikategorikan sangat mudah. |

Run 3 — solusi: Pola berulang setiap tiga gambar (kupu-kupu, kelinci, kelinci). Urutan yang diberikan berakhir pada kupu-kupu, sehingga gambar berikutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pengulangan dalam urutan gambar (pola) dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses penerapan konsep pola yang rutin.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan pengetahuan konseptual tentang bagaimana elemen-elemen disusun dalam urutan.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana untuk siswa kelas 6. Pola berulang tiga elemen sangat familiar dan langsung, tidak memerlukan strategi kompleks atau perhitungan.. Bukti: b. [kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu]

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
| gradeRelativeRationale | Tingkat kesulitan ini jauh di bawah standar kelas 6, karena pola visual berulang adalah materi dasar yang biasanya diajarkan di kelas rendah. |

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
| Domain kognitif | knowing=0.000152; applying=0.999848; reasoning=0.000000 | applying | 0.999848 | 0.001356 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.014403; conceptual=0.983600; procedural=0.001997; metacognitive=0.000000 | conceptual | 0.983600 | 0.064741 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.760360; Medium=0.233902; Hard=0.005738 | Easy | 0.760360 | 0.525890 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999848; −Σp ln(p) = 0.001490; H = 0.001490/ln(3) = 0.001356; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.983600; −Σp ln(p) = 0.089750; H = 0.089750/ln(4) = 0.064741; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.760360; −Σp ln(p) = 0.577749; H = 0.577749/ln(3) = 0.525890; T = 0.953328.


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
Transkripsi visual: Baris b menampilkan urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Pola berulang setiap tiga elemen: {kupu-kupu, kelinci, kelinci}.
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

![Gambar sumber soal 20](<../images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Identifikasi visual kepingan: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total 7 keping sesuai dengan opsi C.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png. Transkripsi visual: Gambar menunjukkan sebuah perahu yang disusun dari 7 keping tangram: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua sedang, 1 persegi hijau muda, 1 segitiga oranye kecil, 1 jajargenjang kuning, dan 1 segitiga merah muda.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `857f1f893f4b1eb7f05574452e9d494a71459326bf306010661691beee6a8b4f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2693 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2669 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2602 |

Run 1 — solusi: Identifikasi visual kepingan: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total 7 keping sesuai dengan opsi C.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengklasifikasikan bentuk-bentuk geometris yang menyusun gambar kompleks (perahu). Ini memerlukan pengenalan sifat-sifat bangun datar (segitiga, persegi, jajargenjang) dalam konteks komposisi, yang masuk dalam kategori applying.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang kategori bangun datar dan bagaimana mereka membentuk struktur yang lebih besar (komposisi/dekomposisi), yang merupakan pengetahuan konseptual.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi visual langsung dari bentuk-bentuk dasar yang sudah dikenal siswa kelas 6. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

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
| gradeRelativeRationale | Siswa kelas 6 sudah sangat familiar dengan tangram dan klasifikasi bangun datar sederhana. |

Run 2 — solusi: Identifikasi visual: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total 7 keping sesuai opsi C.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan mengklasifikasikan bentuk geometris secara visual dari komposisi bangun yang kompleks, yang merupakan proses applying konsep geometri dasar.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang kategori dan sifat-sifat bangun datar (segitiga, persegi, jajargenjang) dalam konteks dekomposisi.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi visual langsung dari bentuk-bentuk dasar yang sudah dikenal siswa kelas 6 tanpa perhitungan rumit.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat bangun datar dasar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah sangat familiar dengan pengenalan bentuk geometri dasar dan dekomposisi sederhana. |

Run 3 — solusi: Identifikasi visual kepingan: 5 segitiga, 1 persegi, 1 jajargenjang. Opsi C sesuai dengan hitungan ini.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan mengklasifikasikan bentuk geometris dari komposisi yang diberikan, yang merupakan proses applying konsep bangun datar.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang kategori dan sifat-sifat bangun datar (konseptual) dalam konteks dekomposisi.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi visual langsung dari bentuk-bentuk dasar yang sudah dikenal siswa kelas 6.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat dasar bangun datar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah sangat familiar dengan bentuk tangram dan klasifikasi bangun datar sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 220/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.114365; applying=0.885635; reasoning=0.000000 | applying | 0.885635 | 0.323630 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.016709; conceptual=0.968774; procedural=0.014517; metacognitive=0.000000 | conceptual | 0.968774 | 0.115809 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.679915; Medium=0.310844; Hard=0.009242 | Easy | 0.679915 | 0.608769 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.885635; −Σp ln(p) = 0.355544; H = 0.355544/ln(3) = 0.323630; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.968774; −Σp ln(p) = 0.160546; H = 0.160546/ln(4) = 0.115809; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.679915; −Σp ln(p) = 0.668801; H = 0.668801/ln(3) = 0.608769; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah perahu yang disusun dari 7 keping tangram: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua sedang, 1 persegi hijau muda, 1 segitiga oranye kecil, 1 jajargenjang kuning, dan 1 segitiga merah muda.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
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
Solusi minimum hasil AI: Definisi belah ketupat mensyaratkan empat sisi sama panjang, sedangkan jajargenjang hanya mensyaratkan sisi berhadapan sejajar. Karena jajargenjang tidak harus memiliki empat sisi sama panjang, maka tidak semua jajargenjang adalah belah ketupat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d03ca352e44c3e5918af76493437b9721862a2cc7a9967c37f2017ecfa8d0700`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 1487 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 1479 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 1460 |

Run 1 — solusi: Definisi belah ketupat mensyaratkan empat sisi sama panjang, sedangkan jajargenjang hanya mensyaratkan sisi berhadapan sejajar. Karena jajargenjang tidak harus memiliki empat sisi sama panjang, maka tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Siswa perlu memahami hubungan hierarkis antar bangun datar (inklusi kelas) dan membedakan syarat perlu dan cukup dari definisi belah ketupat dan jajargenjang.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur konsep geometri dan hubungan antar kategori bangun datar.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep yang mendalam tentang sifat-sifat bangun datar, bukan sekadar menghafal. Siswa harus mampu melakukan penalaran logis tentang inklusi kelas.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?; jajargenjang tidak harus memiliki empat sisi yang sama panjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, membedakan sifat-sifat bangun datar dan memahami relasi antar himpunan bangun datar adalah materi standar yang menuntut pemahaman konseptual menengah. |

Run 2 — solusi: Definisi belah ketupat mensyaratkan keempat sisi sama panjang, sedangkan jajargenjang hanya mensyaratkan sisi berhadapan sejajar. Karena jajargenjang tidak harus memiliki empat sisi sama panjang, maka tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami hubungan hierarkis antar bangun datar (klasifikasi inklusif) dan membedakan sifat-sifat yang menjadi syarat perlu dan cukup, yang masuk dalam kategori reasoning.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur konsep dan hubungan antar kategori bangun datar (belah ketupat sebagai subset dari jajargenjang).. Bukti: Membandingkan Ciri-Ciri Segi Empat
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konseptual mendalam tentang sifat bangun datar. Meskipun terlihat sederhana, ini bukan sekadar hafalan, melainkan kemampuan membedakan syarat cukup dan perlu dalam geometri.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, memahami hierarki bangun datar adalah standar kurikulum, namun sering menjadi miskonsepsi sehingga tingkat kesulitannya menengah. |

Run 3 — solusi: Definisi belah ketupat adalah jajargenjang dengan empat sisi sama panjang. Jajargenjang umum tidak harus memiliki empat sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Siswa perlu memahami hubungan hierarkis antara bangun datar (klasifikasi inklusif) dan membedakan sifat-sifat yang diperlukan (necessary conditions) untuk sebuah bangun disebut belah ketupat.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur konsep geometri dan hubungan antar kategori bangun datar.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman konseptual tentang sifat-sifat bangun datar. Meskipun terlihat sederhana, ini adalah konsep yang sering disalahpahami oleh siswa kelas 6 terkait inklusi kelas bangun datar.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan sudah mengenal klasifikasi bangun datar, namun membedakan sifat yang membatasi (seperti panjang sisi) memerlukan penalaran konseptual yang lebih dalam daripada sekadar menghafal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

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
Solusi minimum hasil AI: Koin memiliki dua sisi yang identik dalam peluang munculnya, yaitu 1/2 untuk gambar dan 1/2 untuk angka, sehingga peluang keduanya sama besar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `08aed1707c074c33e7f686fe4756140be723b9bd5cc516012777116401316525`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1441 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1531 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1450 |

Run 1 — solusi: Koin memiliki dua sisi yang identik dalam peluang munculnya, yaitu 1/2 untuk gambar dan 1/2 untuk angka, sehingga peluang keduanya sama besar.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan konsep dasar peluang pada situasi koin yang adil, yang merupakan penerapan konsep rutin dalam probabilitas.. Bukti: lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka; kedua sisi koin memiliki peluang yang sama untuk muncul
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar probabilitas bahwa koin yang adil memiliki peluang 50:50 untuk setiap sisi.. Bukti: peluang yang sama untuk muncul
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman dasar tentang peluang koin yang adil. Siswa hanya perlu mengenali konsep peluang yang sama besar tanpa perhitungan kompleks.. Bukti: lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka; kedua sisi koin memiliki peluang yang sama untuk muncul

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
| gradeRelativeRationale | Konsep peluang koin adalah materi standar kelas 6 yang bersifat langsung dan tidak memerlukan strategi non-rutin. |

Run 2 — solusi: Koin memiliki dua sisi yang identik dalam peluang munculnya, yaitu 1/2 untuk gambar dan 1/2 untuk angka. Oleh karena itu, peluang keduanya sama besar, sehingga pernyataan bahwa salah satu lebih mudah muncul adalah salah.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengevaluasi pernyataan tentang peluang koin dan memilih alasan yang benar secara matematis, yang melibatkan penerapan konsep dasar peluang pada situasi rutin.. Bukti: menentukan apakah kelompok kalian setuju atau tidak setuju dengan setiap pernyataan berikut; koin hanya punya 2 sisi dan lemparannya acak, sehingga peluang sisi gambar dan sisi angka sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai prinsip dasar peluang (bahwa koin yang adil memiliki peluang 50:50 untuk setiap sisi), yang merupakan konsep fundamental dalam probabilitas.. Bukti: peluang sisi gambar dan sisi angka sama besar
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan mendasar bagi siswa kelas 6 yang baru mempelajari peluang. Siswa hanya perlu memahami sifat koin yang adil tanpa perhitungan kompleks.. Bukti: Saat melempar koin, lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka.; koin hanya punya 2 sisi dan lemparannya acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian sederhana (50:50). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep peluang koin adalah materi pengantar yang sangat standar di kelas 6, sehingga tingkat kesulitannya rendah. |

Run 3 — solusi: Koin memiliki dua sisi yang identik secara peluang dalam lemparan acak, sehingga peluang muncul sisi gambar sama dengan peluang muncul sisi angka (1/2).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang teoretis pada koin yang adil (fair coin) dan menolak miskonsepsi tentang faktor eksternal (berat atau cara lempar).. Bukti: Tidak setuju, karena kedua sisi koin memiliki peluang yang sama untuk muncul
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar peluang (konsep bahwa dua kejadian yang mungkin pada koin memiliki probabilitas yang sama).. Bukti: peluang yang sama untuk muncul
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena menguji pemahaman dasar tentang peluang kejadian sederhana yang sudah menjadi pengetahuan umum di kelas 6.. Bukti: lebih mudah untuk mendapatkan sisi gambar dibandingkan sisi angka; kedua sisi koin memiliki peluang yang sama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian sederhana (50:50). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep peluang koin adalah materi standar kelas 6 yang bersifat intuitif dan tidak memerlukan perhitungan kompleks. |

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
Solusi minimum hasil AI: Dadu memiliki 8 sisi yang semuanya bertuliskan angka 5. Karena tidak ada sisi bertuliskan angka 2, maka kejadian munculnya angka 2 adalah kejadian mustahil (peluang = 0).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `54c7b6384600857a440da960a548d2cf0ccb5dcae8bd9f95f8c3f5e67178928f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1477 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1399 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1408 |

Run 1 — solusi: Dadu memiliki 8 sisi yang semuanya bertuliskan angka 5. Karena tidak ada sisi bertuliskan angka 2, maka kejadian munculnya angka 2 adalah kejadian mustahil (peluang = 0).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang (kejadian mustahil) dan menerapkannya pada konteks dadu yang tidak standar. Ini melibatkan penerapan konsep pada situasi rutin.. Bukti: seluruh 8 sisi bertuliskan angka 5; peluang munculnya angka 2
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian mustahil) dan bagaimana mengkategorikannya dalam skala peluang.. Bukti: skala peluang; seluruh 8 sisi bertuliskan angka 5
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi bahwa angka 2 tidak ada dalam ruang sampel, sehingga peluangnya adalah nol (tidak mungkin). Tidak ada perhitungan kompleks atau strategi nonrutin.. Bukti: seluruh 8 sisi bertuliskan angka 5; peluang munculnya angka 2

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
| gradeRelativeRationale | Untuk kelas 6, konsep peluang dasar seperti kejadian mustahil adalah materi standar yang rutin. |

Run 2 — solusi: Dadu memiliki 8 sisi yang semuanya bernilai 5. Karena tidak ada sisi bernilai 2, maka kejadian munculnya angka 2 adalah kejadian mustahil (peluang = 0).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep dasar peluang (kejadian mustahil) pada situasi yang diberikan.. Bukti: seluruh 8 sisi bertuliskan angka 5; peluang munculnya angka 2
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar peluang dan kategori skala peluang.. Bukti: skala peluang; seluruh 8 sisi bertuliskan angka 5
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 6 yang telah mempelajari skala peluang dasar.. Bukti: seluruh 8 sisi bertuliskan angka 5; peluang munculnya angka 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang skala peluang (pasti, mungkin, tidak mungkin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep peluang kejadian mustahil adalah materi standar kelas 6 yang tidak memerlukan perhitungan kompleks. |

Run 3 — solusi: Dadu memiliki 8 sisi yang semuanya bernomor 5. Karena tidak ada sisi bernomor 2, maka kejadian munculnya angka 2 adalah kejadian mustahil (peluang = 0).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang (kejadian mustahil) dan menerapkannya pada konteks yang diberikan untuk menentukan kategori skala peluang.. Bukti: seluruh 8 sisi bertuliskan angka 5; peluang munculnya angka 2
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi kejadian mustahil dalam skala peluang.. Bukti: skala peluang; seluruh 8 sisi bertuliskan angka 5
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman dasar tentang peluang kejadian mustahil tanpa memerlukan perhitungan kompleks.. Bukti: seluruh 8 sisi bertuliskan angka 5; peluang munculnya angka 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang skala peluang (pasti, mungkin, tidak mungkin). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep peluang kejadian mustahil adalah materi standar kelas 6 yang dapat diselesaikan dengan logika sederhana. |

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
Solusi minimum hasil AI: Peluang dadu kubus mendapatkan angka 3 adalah 1/6 (sekitar 0,167). Peluang dadu piramida mendapatkan angka 3 adalah 1/4 (0,25). Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['menerapkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec932ad1e570d969994ace585eea370641832ffcdda952c3077653b75975ba5d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 1622 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 1658 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 1645 |

Run 1 — solusi: Peluang dadu kubus mendapatkan angka 3 adalah 1/6 (sekitar 0,167). Peluang dadu piramida mendapatkan angka 3 adalah 1/4 (0,25). Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep peluang (jumlah kejadian yang diinginkan dibagi total ruang sampel) untuk membandingkan dua situasi yang berbeda, yang merupakan proses penalaran.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara ruang sampel dan peluang kejadian, yang merupakan konsep dasar dalam teori probabilitas.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep peluang dasar dan perbandingan pecahan. Meskipun melibatkan perbandingan, prosedurnya rutin bagi siswa kelas 6 yang sudah mempelajari peluang.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai perbandingan kejadian yang diinginkan terhadap total kemungkinan. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu membandingkan pecahan sederhana dalam konteks peluang. Soal ini menuntut siswa untuk tidak sekadar melihat angka, tetapi memahami hubungan proporsional. |

Run 2 — solusi: Peluang muncul angka 3 pada dadu kubus adalah 1/6 (sekitar 0,167), sedangkan pada dadu piramida adalah 1/4 (0,25). Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep peluang (rasio kejadian terhadap ruang sampel) untuk membandingkan dua situasi yang berbeda, yang merupakan proses penalaran.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang; Jelaskan alasan atas pilihan kalian
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana ukuran ruang sampel mempengaruhi probabilitas suatu kejadian.. Bukti: peluang terbesar untuk menang; Dadu kubus dengan sisi... 1, 2, 3, 4, 5, 6; Dadu piramida dengan sisi... 1, 2, 3, 4
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk membandingkan dua pecahan dengan penyebut berbeda dalam konteks peluang, yang merupakan tantangan standar untuk kelas 6.. Bukti: Pilih dadu yang kalian akan gunakan; Jelaskan alasan atas pilihan kalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai rasio kejadian/ruang sampel dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 diharapkan mampu membandingkan peluang sederhana. Soal ini memerlukan pemilihan prosedur yang tepat (menghitung rasio) dan membandingkan hasilnya. |

Run 3 — solusi: Peluang dadu kubus mendapatkan angka 3 adalah 1/6. Peluang dadu piramida mendapatkan angka 3 adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang lebih besar.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep peluang (rasio kejadian terhadap ruang sampel) dan membandingkan dua pecahan untuk menentukan strategi yang optimal.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar; Jelaskan alasan atas pilihan kalian
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami struktur konsep peluang sebagai rasio dan hubungan antara ukuran ruang sampel dengan nilai peluang.. Bukti: peluang terbesar untuk menang; Dadu kubus dengan sisi... 1, 2, 3, 4, 5, 6; Dadu piramida dengan sisi... 1, 2, 3, 4
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman konsep peluang yang lebih dalam daripada sekadar menghitung, karena siswa harus membandingkan dua ruang sampel yang berbeda untuk membuat keputusan.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar; Jelaskan alasan atas pilihan kalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai rasio (kejadian/total) dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 6, membandingkan peluang dengan ruang sampel berbeda adalah tantangan yang sesuai untuk menguji pemahaman konseptual, bukan sekadar hafalan rumus. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

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

![Gambar sumber soal 25](<../images/kelas6_panduan_siswa_kelas6.pdf-0134-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Peluang kejadian pada roda putar sebanding dengan luas juringnya. Secara visual, juring 'Maryam' adalah yang paling luas dibandingkan juring lainnya, sehingga Maryam memiliki peluang menang paling besar.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0134-01.png. Transkripsi visual: Sebuah roda putar dibagi menjadi empat juring dengan ukuran berbeda. Juring berwarna biru muda bertuliskan 'Maryam' menempati area terbesar (lebih dari setengah lingkaran). Juring berwarna oranye bertuliskan 'Abdillah' menempati area yang cukup besar. Juring berwarna hijau bertuliskan 'Reimon' dan juring berwarna oranye kemerahan bertuliskan 'Tuti' menempati area yang lebih kecil.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 6 / Matematika SD Kelas 6. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `52db94cfbe74e14deeee451bf320ce84dc20d97c06e317f24e863acb303822a6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2582 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2593 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2573 |

Run 1 — solusi: Peluang kejadian pada roda putar sebanding dengan luas juringnya. Secara visual, juring 'Maryam' adalah yang paling luas dibandingkan juring lainnya, sehingga Maryam memiliki peluang menang paling besar.
- Domain kognitif `classify/applying`: Siswa perlu mengaitkan konsep peluang dengan representasi visual (luas juring). Ini adalah penerapan konsep peluang dasar pada situasi rutin.. Bukti: tentukan siapa yang memiliki peluang menang paling besar; roda putar seperti di gambar
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara luas juring (konsep geometris) dengan peluang kejadian (konsep statistik).. Bukti: peluang menang paling besar; roda putar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin untuk kelas 6, hanya memerlukan observasi visual sederhana tanpa perhitungan numerik yang rumit.. Bukti: roda putar seperti di gambar; tentukan siapa yang memiliki peluang menang paling besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai bagian dari keseluruhan dan kemampuan membandingkan luas juring secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah familiar dengan konsep peluang sederhana dan interpretasi diagram lingkaran/roda putar. |

Run 2 — solusi: Peluang kejadian pada roda putar sebanding dengan luas juringnya. Secara visual, juring bertuliskan 'Maryam' adalah yang paling luas dibandingkan juring lainnya, sehingga Maryam memiliki peluang menang paling besar.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang bahwa luas juring berbanding lurus dengan peluang kejadian, kemudian menerapkan pemahaman tersebut untuk membandingkan luas juring secara visual.. Bukti: tentukan siapa yang memiliki peluang menang paling besar; roda putar yang dibuat
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara luas daerah (juring) dengan peluang kejadian pada roda putar.. Bukti: peluang menang paling besar; roda putar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan perbandingan visual langsung tanpa perhitungan numerik yang rumit atau strategi non-rutin.. Bukti: roda putar yang dibuat; tentukan siapa yang memiliki peluang menang paling besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sederhana dan perbandingan luas daerah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah familiar dengan konsep peluang sederhana dan interpretasi visual data, sehingga soal ini berada pada tingkat kesulitan yang sesuai untuk kategori mudah. |

Run 3 — solusi: Peluang kejadian pada roda putar sebanding dengan luas juringnya. Secara visual, juring bertuliskan 'Maryam' memiliki luas paling besar dibandingkan juring lainnya, sehingga Maryam memiliki peluang menang paling besar.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar peluang bahwa luas juring berbanding lurus dengan peluang kejadian, kemudian menerapkan pemahaman tersebut untuk membandingkan luas visual juring pada roda putar.. Bukti: tentukan siapa yang memiliki peluang menang paling besar; roda putar yang dibuat
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara luas area (juring) dan peluang kejadian sederhana.. Bukti: peluang menang paling besar; roda putar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan observasi visual langsung untuk membandingkan ukuran juring tanpa perlu melakukan perhitungan numerik yang kompleks.. Bukti: roda putar yang dibuat; tentukan siapa yang memiliki peluang menang paling besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bahwa peluang berkaitan dengan luas bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 6 sudah familiar dengan konsep peluang sederhana dan interpretasi diagram/grafik visual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 171/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.001771; conceptual=0.994911; procedural=0.003318; metacognitive=0.000000 | conceptual | 0.994911 | 0.025419 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.555898; Medium=0.428219; Hard=0.015882 | Easy | 0.555898 | 0.687578 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.994911; −Σp ln(p) = 0.035238; H = 0.035238/ln(4) = 0.025419; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.555898; −Σp ln(p) = 0.755382; H = 0.755382/ln(3) = 0.687578; T = 0.953328.


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
Transkripsi visual: Sebuah roda putar dibagi menjadi empat juring dengan ukuran berbeda. Juring berwarna biru muda bertuliskan 'Maryam' menempati area terbesar (lebih dari setengah lingkaran). Juring berwarna oranye bertuliskan 'Abdillah' menempati area yang cukup besar. Juring berwarna hijau bertuliskan 'Reimon' dan juring berwarna oranye kemerahan bertuliskan 'Tuti' menempati area yang lebih kecil.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
