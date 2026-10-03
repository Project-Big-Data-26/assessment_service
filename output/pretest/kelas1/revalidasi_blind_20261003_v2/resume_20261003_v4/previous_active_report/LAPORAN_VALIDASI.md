# Validasi ulang soal kelas 1 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 72/150 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v4-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v2-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 1 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model lama dipakai untuk menunjukkan ketidaksepakatan; tidak diberikan kembali ke Gemini.

Jumlah soal: 50; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 26, "knowing": 13, "applying": 11, "reasoning": 0}, "knowledgeDimension": {"undecided": 26, "factual": 6, "conceptual": 7, "procedural": 11, "metacognitive": 0}, "intendedDifficulty": {"undecided": 26, "Easy": 22, "Medium": 2, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 13, "applying": 11, "reasoning": 0}, "knowledgeDimension": {"factual": 6, "conceptual": 7, "procedural": 11, "metacognitive": 0}, "intendedDifficulty": {"Easy": 22, "Medium": 2, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"llm_retry_or_manual_review": 26, "pending_expert_review": 24}`.
Run awal sukses: 72/150; adjudikasi: 11; token sukses tercatat: 153,306.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 22 | 22 | [Easy.json](difficulty/Easy.json) |
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

![Gambar sumber soal 1](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0027-06.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0027-06.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8d73a0dc86e145659daadb63288a1d70870a55db73f3f5d3df1e99597c5564fa`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 93/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `28bc514789457f83d4d75614b1d48093282fef89d172f5889ad4cac88b3a3f6c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `aded1ab9ecb9a5ad0e341f2a`

Buah mana yang jumlahnya lebih banyak?

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan |
| B | B (jeruk) |
| C | Sama banyak |
| D | A (mangga) |

![Gambar sumber soal 3](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 6 > 4, maka kotak B lebih banyak.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png. Transkripsi visual: Terdapat dua kotak berlabel A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7340044427e5d71399d187a9b20d06580337e11cea87daa2d2cad4fdfe65a870`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `71dcf3a05499a6d3e660d279`

Buah mana yang jumlahnya lebih sedikit?

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan |
| B | A (mangga) |
| C | Sama banyak |
| D | B (jeruk) |

![Gambar sumber soal 4](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 4 < 6, maka kotak A (mangga) memiliki jumlah lebih sedikit.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png. Transkripsi visual: Terdapat dua kotak, A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f6fe712ed737d791fc399743b8a2f0ccdf6943578e44745af90551a98613151`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `a035dee2caefafa52096496e`

Lengkapi urutan bilangan berikut: 1, 2, ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 1 |
| C | 0 |
| D | 4 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ddcfd7d6d5a4d5a0899e283323fb1644eed9d7e98bea8881d36266c4cdb7dbc1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `593cbed3be61dd6c967e770c`

Lengkapi urutan bilangan berikut: 4, 5, ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 4 |
| C | 6 |
| D | 7 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3f9988a477ab817186a366186859ee85deabd180003a5c075e17927ef680856e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `82267daa87c52ac8b3876098`

Temukan pasangan bilangan berikut.<br><br>Temukan pasangan bilangan berikut. Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?

| Opsi | Isi |
|---|---|
| A | 5 dan 3 |
| B | 4 dan 4 |
| C | 3 dan 6 |
| D | 4 dan 5 |

![Gambar sumber soal 7](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0043-04.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0043-04.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3828053e57b2a542f836eebbac2cc6260de24986adf123e526a4f7597dfe1403`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 74/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `ddae4518c6926e380356e576`

Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 2 |
| C | 4 |
| D | 1 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `209e1846f8094d890ec9788ba369d7a66077a4e955b6c8a8dbdf9514b591a0b6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `ef1c6489a0d0caf13ccb067e`

Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.

| Opsi | Isi |
|---|---|
| A | 4 mobil kuning, 5 mobil merah, semuanya 9 mobil |
| B | 4 mobil kuning, 4 mobil merah, semuanya 9 mobil |
| C | 4 mobil kuning, 4 mobil merah, semuanya 8 mobil |
| D | 5 mobil kuning, 4 mobil merah, semuanya 9 mobil |

![Gambar sumber soal 9](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0058-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menghitung jumlah mobil kuning (4), menghitung jumlah mobil merah (4), lalu menjumlahkan keduanya (4 + 4 = 8).
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0058-03.png. Transkripsi visual: Terdapat dua kelompok mobil. Kelompok kiri berisi 4 mobil berwarna kuning. Kelompok kanan berisi 4 mobil berwarna merah. Soal meminta siswa mengisi jumlah mobil kuning, jumlah mobil merah, dan total seluruh mobil.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8cb692d8fca01c2911f1256917b983cf484910bfa707290e7330d474794f6d14`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `f00f8cf40ab22284c6d216e4`

Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain. Mereka bermain bergantian.<br><br>Berapa jumlah anak sekarang?

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 6 |
| C | 8 |
| D | 4 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `543cbc7d1e12c8d882ad7e98fbc0d77d0b2ef8a69606fff0c5b910530f96bc3e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6163722c5e529b6a3c4c251554dc60d794a5eb7805b80c9a6059319063dc05b5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a1dcc411d94c79b1428719ee9c349533c0529ede7562d249b3ec679fb6c7e992`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `018e7b45e13d10afc8e87d48`

Ada 3 sepeda Ada 1 becak.<br><br>Berapa jumlah semua rodanya?

| Opsi | Isi |
|---|---|
| A | 9 roda |
| B | 10 roda |
| C | 6 roda |
| D | 8 roda |

![Gambar sumber soal 13](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0081-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0081-01.png. Transkripsi visual: Terdapat 3 sepeda (masing-masing dengan 2 roda) dan 1 becak (dengan 3 roda) di jalan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1f833c8b0ecd4eb31cf9207f85e7fbc623d0c1218f8cbf2b0e4e3085e82bc63f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dc6e657c2d796e973f64cab165218a28df33db4a1bbd7cb6c2bbc1b1b636db80`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `adaec31c66c75d9c825ad888`

9 - ... = 7. Lengkapi operasi pengurangannya.

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 16 |
| C | 2 |
| D | 7 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e69bfbbb915266dc2802de5c5fac0f94f9a35c017ce9629399639880be5b69ea`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 59/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41fb0023e17d3c1a2acf03fbc35202320f24c1539eb3cc5a1fe1a2f9ea96c801`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `7aa38a3601f61c91adbf30d4`

Isilah titik-titik di bawah ini.<br><br> 6 – 4 = .... . Tulis hasil pengurangannya.

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 2 |
| C | 6 |
| D | 3 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8c8ee6ef1826b625d07900b4b96792702edfaa04425f7d03e4c40d071d46f0ce`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 71/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `dde0b5654f117861d23c7988`

0 1 2 3 4 5 6 7 8 9 10<br><br>Hitunglah. 9 – 3 =

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 3 |
| C | 6 |
| D | 5 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aba0a211ca4c61f8fcd0d4ff83d32c10a32c7e60b62bd2f05225d953c9fcf005`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `121d38127e273c2f06bd5f8e625c2903fcd8f1b97ff36683aaa14bc83ab77324`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `f6fcf5836947ff740007f70e`

Isilah titik-titik di bawah ini.<br><br>2 + 6 = ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | 26 |
| C | 9 |
| D | 8 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c25499890891f690a4b418ceb036b0654e7265713dbe1afcc396d6e20405d369`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `808582396e3489bd50f5c434466f54c849fcc9e0fe1b2f50232ec4c8f827176e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `66c0a95a0b034cd7425ce9e1ec3d88eb3102f5a9988ac92442555547edfe7030`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `355049fbd1c523a25cd2de3d`

Apa bentuk dari gambar berikut?

| Opsi | Isi |
|---|---|
| A | Bentuk bintang |
| B | Segi empat |
| C | Segitiga |
| D | Bentuk lengkung |

![Gambar sumber soal 23](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0134-03.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0134-03.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `88c0c04d66c7a48f680c9cc89217f37588da950474a0b9fa73a9f03f7fd5b80f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 57/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `83dd4d12892fc170e56f4e1b`

Pasangkan bentuk dengan namanya. Bangun keempat dari atas.

| Opsi | Isi |
|---|---|
| A | Bentuk lengkung |
| B | Bentuk bintang |
| C | Segi empat |
| D | Segitiga |

![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-01.png>)


![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-02.png>)


![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-03.png>)


![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bangun keempat dari atas adalah lingkaran merah. Lingkaran memiliki sisi lengkung dan tidak memiliki sudut, sehingga sesuai dengan deskripsi 'Bentuk lengkung'.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0153-01.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-02.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-03.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-04.png. Transkripsi visual: Terdapat empat bangun datar yang disusun vertikal dari atas ke bawah: 1. Persegi berwarna biru, 2. Segitiga berwarna ungu, 3. Persegi panjang berwarna biru, 4. Lingkaran berwarna merah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f24990388808ccc8e48ed63ad617f4a34080b4d9eb94df00eec32d5d0dbd6a7f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `98891851d1e28d6d8482ab94`

Pilih jawaban yang benar. Bangun yang satu kelompok dengan gambar di atas.

| Opsi | Isi |
|---|---|
| A | Persegi panjang berwarna ungu |
| B | Segitiga terbalik berwarna ungu |
| C | Persegi berwarna ungu |
| D | Oval berwarna ungu |

![Gambar sumber soal 25](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0143-05.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0143-05.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4843635a3ce1ce4733ab943370829f0690fd516e1b19e3a19c2c5f663e8a753e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `7bde28fb9ff374327ad9c3ae`

Bangun yang satu warna dengan gambar di atas.

| Opsi | Isi |
|---|---|
| A | Persegi berwarna ungu |
| B | Oval berwarna hijau |
| C | Persegi panjang berwarna biru |
| D | Segitiga terbalik berwarna merah muda |

![Gambar sumber soal 26](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0144-00.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0144-00.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e483808428b8b4e4d5d873472db0917eca372d133b6f07d9dba09789a8f76eb1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `aaf396a280df35704272b0d3`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 8 |
| C | 4 |
| D | 5 |

![Gambar sumber soal 27](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a37bb22d388aceb1ce772d24c29f18062135ea70dfc416ae2353ea0b24ce3927`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 63/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `595d20d8c4a6f9418dc496b0`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

| Opsi | Isi |
|---|---|
| A | 8 |
| B | 0 |
| C | 1 |
| D | 2 |

![Gambar sumber soal 28](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d42d8749fa7ba544250b1aa0b4b5a5e705274c150d716a27c9bff97cdd0b183f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 62/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `77f3a2e1b230dac593d46f2821f8035288f386534c17bb656fddd549f2170427`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `667035e13b735c918c39e19b21873fbd258cd37da96268770759705296775828`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `22566b5bb03c2de75ee541bdbc2426a8b2a7d0f508940024f431b8103e158468`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `02bd8bfdfd682bd80aa5f426`

Lengkapi urutan bilangan berikut.<br><br>20, ...., 18

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 19 |
| C | 21 |
| D | 17 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8451484d6a55d894bb4f646cb11d0a956810da4c10644b1dc2460364668cb20b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `fb13c7e49793c36315b9e324`

Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.<br><br>.... puluhan dan .... satuan = ....

| Opsi | Isi |
|---|---|
| A | 1 puluhan dan 5 satuan = 15 |
| B | 0 puluhan dan 15 satuan = 15 |
| C | 1 puluhan dan 6 satuan = 16 |
| D | 1 puluhan dan 4 satuan = 14 |

![Gambar sumber soal 33](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0175-03.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0175-03.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `61306683a0edc24150d1a8cb5178bccd1b30067d54baed477f0e772565c65b1e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 99/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `daa41e2808537d493a6c0994`

Hitunglah dan isi tabelnya.<br><br>Nilai tempat 14 = .... puluhan dan .... satuan

| Opsi | Isi |
|---|---|
| A | 1 puluhan dan 4 satuan |
| B | 1 puluhan dan 3 satuan |
| C | 4 puluhan dan 1 satuan |
| D | 0 puluhan dan 14 satuan |

![Gambar sumber soal 34](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0175-04.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0175-04.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e1d6b3efb1b98365fcbe91dc0a04d24d8711117e404ae57ffecde17a44544423`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 84/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8033d883ba2c5a0920f213e162e9eb2871485c6e9c5615feeda7401eb9640023`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eefde0832abc8c1f812cd03a1a31094edb25c861642a5ad877c4bab549702640`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f952ac18255d2f8027b25dacae02dd43b6017e6da7ffdeeb08fa991304b6991`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4240274822d77119f03e650517b2781293bc6cbd30d797cb3a5519d83270a962`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8b06f5cbe3683f666688563bd2a26215bbdfb6d1f35092e84e0e70733c9e7792`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b9286a2185815d733cea4c7fb4e8c52720cfba7c22449960f6989b1fa53b4f4d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `80d1844d6b8b7f2d4e32fac770fcb8b8191211326e1882f35ca957447ecf18a7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c44dc01b049dfe14e5f2d64abc28a6ab4ff41bf727bcc546af7e36b9ac309737`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `ff83d65211d6e4aa98e13b06`

Perhatikan gambar berikut.<br><br>Urutan bunga dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | B, C, A |
| B | C, A, B |
| C | A, C, B |
| D | A, B, C |

![Gambar sumber soal 43](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0218-01.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0218-01.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1d71dc20dffa0c1ca39268b9f0ca03cfbff8e9996ad0a1b4f91e7f3f88fde840`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 90/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `dc65bbd6611c904972206f6c`

Burung yang terbang paling tinggi adalah ....

| Opsi | Isi |
|---|---|
| A | Ketiga burung terbang sama tinggi |
| B | C |
| C | B |
| D | A |

![Gambar sumber soal 44](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0219-07.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0219-07.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec82e7cefc25d0cab1a9df99ae2fb76321cb94b7471b8163427372c81c67d0b1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `75434d44f2b377da3027e153`

Temukan panjang pensil berikut. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.<br><br>Urutan pensil dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | A, C, B |
| B | A, B, C |
| C | B, C, A |
| D | C, A, B |

![Gambar sumber soal 45](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2291dd26f064247473b2e7252879b9ebfdffb6c55588d472c42480f892122f13`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 109/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `62785ac6ff0622ab70a94b13`

Temukan panjang pita berikut. Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.<br><br>Pita B lebih .... dari pita C.

| Opsi | Isi |
|---|---|
| A | panjang |
| B | pendek |
| C | tinggi |
| D | besar |

![Gambar sumber soal 46](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0228-03.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0228-03.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `51883b3ef28433f2693e1b4d34528365a822cd3235648eb1fdd339c8c194af84`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 77/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `5e007b54e25f6f72efa82174`

Amati gambar buah-buahan. Lengkapi daftarnya. Daftar Buah-buahan: Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.<br><br>Buah yang paling banyak adalah ...

| Opsi | Isi |
|---|---|
| A | Apel |
| B | Mangga |
| C | Jambu |
| D | Jeruk |

![Gambar sumber soal 47](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0238-11.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0238-11.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `55a6a7a04534dfd6ed401ca7c1ddf6e1ac73b9b3a6fa83f28ac19cdcbd8674f7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 92/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `17ba235cdc9fddc600303514`

Perhatikan tabel dan jawablah pertanyaannya.<br><br>Apa nama kue yang paling disukai?

| Opsi | Isi |
|---|---|
| A | Kue Cucur |
| B | Kue Lapis |
| C | Kue Talam |
| D | Kue Bugis |

![Gambar sumber soal 48](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0238-12.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0238-12.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `388c5236d41289b516a985e749bc73f59a80dd55fc98d42adfbe02b2fe2231d4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `e7d8a29f2e3a28f99529dfc8`

Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Lengkapi setiap kalimat berikut.<br><br>Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 3 |
| C | 4 |
| D | 1 |

![Gambar sumber soal 49](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `60fe0ae5c4b6f1dad9839e96494ac97dad362fabf0bbd115f3a6caf7b2eef12e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 76/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 50. Soal `8812007076d1edea9f050f6f`

Ibu membeli buah di pasar. Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.<br><br>Buah yang paling sedikit adalah ...

| Opsi | Isi |
|---|---|
| A | Belimbing |
| B | Jeruk |
| C | Apel |
| D | Mangga |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ca139453787190dec36bb8912ebd55ff4531e3c662175dee41f326c70b921322`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 75/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
