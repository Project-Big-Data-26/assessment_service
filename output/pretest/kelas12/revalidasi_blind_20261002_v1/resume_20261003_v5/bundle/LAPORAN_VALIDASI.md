# Validasi ulang soal kelas 12 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v8-blind-sma12-key-verified`. Rubrik: `math-rubric-3x4x3-v6-sma12-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 12 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 12, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 32; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 27, "knowing": 4, "reasoning": 1}, "knowledgeDimension": {"conceptual": 9, "procedural": 23, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 19, "Medium": 13, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 26, "knowing": 4, "reasoning": 1}, "knowledgeDimension": {"conceptual": 9, "procedural": 22, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 19, "Medium": 12, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 31, "revision_required": 1}`.
Run awal sukses: 96/96; adjudikasi: 14; token sukses tercatat: 291,834.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 19 | 19 | [Easy.json](difficulty/Easy.json) |
| Medium | 13 | 12 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 12, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 12, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 12. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `ddce171a6063467f30bcf924`

Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 1, 1, 2, 6, …, …

| Opsi | Isi |
|---|---|
| A | 24, 120 |
| B | 1, 3 |
| C | $\frac{1}{4}$, $\frac{1}{16}$ |
| D | 4, 4 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pola barisan adalah perkalian dengan bilangan asli yang berurutan: 1x1=1, 1x2=2, 2x3=6. Maka suku berikutnya adalah 6x4=24 dan 24x5=120.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `641a35435d963d4ebd4b73ac898233fdf42664fe6c96af48c56036af6da00432`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2095 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2069 |
| 3 | success | valid / verified | applying | procedural | Easy | 2104 |

Run 1 — solusi: Pola barisan adalah perkalian dengan bilangan asli yang berurutan: 1x1=1, 1x2=2, 2x3=6. Maka suku berikutnya adalah 6x4=24 dan 24x5=120.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola rekursif (perkalian dengan pengali yang meningkat) dari deret yang diberikan. Ini adalah proses applying karena siswa menerapkan prosedur pengenalan pola untuk menentukan suku berikutnya.. Bukti: 1, 1, 2, 6, …, …; pola perkalian bertambah: x1,x2,x3,x4,x5
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur barisan bilangan dan prinsip pola perkalian, yang termasuk dalam kategori pengetahuan konseptual.. Bukti: 1, 1, 2, 6, …, …
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola yang digunakan (faktorial/perkalian berurutan) cukup standar dan hanya memerlukan dua langkah perhitungan sederhana untuk menemukan dua suku berikutnya.. Bukti: 1, 1, 2, 6, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan operasi perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi barisan diajarkan di kelas 12, soal ini menggunakan pola yang sangat sederhana dan familiar, sehingga tingkat kesulitannya rendah untuk siswa SMA. |

Run 2 — solusi: Pola barisan adalah perkalian dengan bilangan asli yang berurutan: 1x1=1, 1x2=2, 2x3=6. Maka suku berikutnya adalah 6x4=24 dan 24x5=120.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola rekursif (perkalian dengan bilangan asli yang meningkat) dari deret yang diberikan. Ini melibatkan identifikasi pola, yang merupakan proses applying konsep barisan.. Bukti: 1, 1, 2, 6, …, …
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pola bilangan (konseptual) dan penerapan algoritma perkalian untuk menentukan suku berikutnya (prosedural). Fokus utamanya adalah memahami struktur pola tersebut.. Bukti: 1, 1, 2, 6
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola yang diberikan cukup sederhana dan familiar bagi siswa SMA. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 1, 1, 2, 6, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan operasi perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi barisan adalah kurikulum SMA, tingkat kesulitan soal ini sangat rendah karena pola perkalian (faktorial) adalah pola dasar yang sering ditemui. |

Run 3 — solusi: Pola barisan adalah perkalian dengan bilangan asli yang berurutan: 1x1=1, 1x2=2, 2x3=6. Maka suku berikutnya adalah 6x4=24 dan 24x5=120.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola rekursif (perkalian dengan bilangan asli yang meningkat) dari barisan yang diberikan. Ini adalah proses mengenali pola dan menerapkan aturan tersebut untuk menentukan suku berikutnya.. Bukti: 1, 1, 2, 6, …, …
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep barisan bilangan dan kemampuan menerapkan aturan pola (prosedur) untuk menemukan suku berikutnya.. Bukti: 1, 1, 2, 6, …, …
- Intended difficulty `classify/Easy`: Soal ini termasuk kategori mudah karena pola yang digunakan (perkalian berurutan) cukup standar dan familiar bagi siswa SMA, serta tidak memerlukan langkah-langkah yang kompleks.. Bukti: 1, 1, 2, 6, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola barisan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi barisan diajarkan di kelas 11/12, tingkat kesulitan soal ini sangat rendah untuk standar kelas 12 karena hanya melibatkan operasi perkalian sederhana dengan pola yang jelas. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3543`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengenali pola rekursif (perkalian dengan pengali yang meningkat) dari deret yang diberikan. Ini adalah proses applying karena siswa menerapkan prosedur pengenalan pola untuk menentukan suku berikutnya.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang struktur barisan bilangan dan prinsip pola perkalian, yang termasuk dalam kategori pengetahuan konseptual.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena pola yang digunakan (faktorial/perkalian berurutan) cukup standar dan hanya memerlukan dua langkah perhitungan sederhana untuk menemukan dua suku berikutnya.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan operasi perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi barisan diajarkan di kelas 12, soal ini menggunakan pola yang sangat sederhana dan familiar, sehingga tingkat kesulitannya rendah untuk siswa SMA. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 1, 1, 2, 6, …, …
Pilihan: A. 24, 120
B. 1, 3
C. $\frac{1}{4}$, $\frac{1}{16}$
D. 4, 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `577daf905630d2b50cdcacfa`

Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …

| Opsi | Isi |
|---|---|
| A | 24, 120 |
| B | $\frac{1}{4}$, $\frac{1}{16}$ |
| C | 4, 4 |
| D | 1, 3 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Barisan 4, 4, 4, 4, ... adalah barisan konstan dengan suku ke-n (Un) = 4. Maka, suku berikutnya tetap 4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9de549f232b11aebb0f4a039fc417124a63cd481ba7a93636292d1c8a7450159`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1982 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1987 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2017 |

Run 1 — solusi: Barisan 4, 4, 4, 4, ... adalah barisan konstan dengan suku ke-n (Un) = 4. Maka, suku berikutnya tetap 4.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola barisan konstan yang sangat sederhana (mengingat/mengenali pola).. Bukti: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual dasar mengenai barisan bilangan konstan.. Bukti: 4, 4, 4, 4, …, …
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, tidak memerlukan perhitungan kompleks atau strategi khusus, hanya pengenalan pola yang langsung.. Bukti: 4, 4, 4, 4, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola barisan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Meskipun untuk kelas 12, soal ini terlalu sederhana dan tidak mencerminkan standar kompetensi kelas 12 yang seharusnya lebih kompleks. |

Run 2 — solusi: Barisan 4, 4, 4, 4, ... adalah barisan konstan dengan suku ke-n (Un) = 4 untuk setiap n. Oleh karena itu, dua suku berikutnya tetap 4 dan 4.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta pengenalan pola sederhana (barisan konstan) yang merupakan proses langsung tanpa memerlukan strategi kompleks.. Bukti: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep barisan konstan sebagai bagian dari pengetahuan konseptual tentang pola bilangan.. Bukti: 4, 4, 4, 4, …, …
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan prosedurnya sangat familiar bagi siswa SMA, tidak memerlukan langkah perhitungan yang berarti.. Bukti: 4, 4, 4, 4, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola barisan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini terlalu sederhana untuk standar kelas 12, namun secara teknis valid sebagai pengenalan pola barisan. |

Run 3 — solusi: Barisan 4, 4, 4, 4, ... adalah barisan konstan dengan suku ke-n (Un) = 4 untuk setiap n. Oleh karena itu, dua suku berikutnya tetap 4 dan 4.
- Domain kognitif `classify/knowing`: Soal ini hanya memerlukan pengenalan pola barisan konstan yang sangat sederhana. Siswa hanya perlu mengenali bahwa nilai suku tidak berubah, yang merupakan proses kognitif tingkat dasar (knowing).. Bukti: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep barisan konstan sebagai salah satu jenis barisan bilangan, yang merupakan pemahaman konseptual dasar.. Bukti: 4, 4, 4, 4, …, …
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan tidak memerlukan perhitungan kompleks atau strategi khusus. Prosedurnya langsung dan familiar bagi siswa kelas 12.. Bukti: 4, 4, 4, 4, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola barisan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Meskipun untuk kelas 12, soal ini terlalu sederhana dan tidak mencerminkan tingkat kesulitan yang diharapkan untuk jenjang tersebut. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
Pilihan: A. 24, 120
B. $\frac{1}{4}$, $\frac{1}{16}$
C. 4, 4
D. 1, 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `cde1c3bcaf6c566fa0d0dfde`

Jika Un menyatakan suku ke-n suatu barisan aritmetika dan diketahui U 6 - U 8 + U 10 - U 12 + U 14 = 20, berapa jumlah 19 suku pertama barisan tersebut?

| Opsi | Isi |
|---|---|
| A | 380 |
| B | 20 |
| C | 360 |
| D | 190 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: U6-U8+U10-U12+U14 = (a+5b)-(a+7b)+(a+9b)-(a+11b)+(a+13b) = a+9b = 20. S19 = 19/2 * (2a + 18b) = 19 * (a+9b) = 19 * 20 = 380.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `118014424a201852dcf592098187f8cb344542d694919020051399f6a1897245`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3116 |
| 2 | success | valid / verified | applying | procedural | Medium | 2928 |
| 3 | success | valid / verified | applying | procedural | Medium | 3186 |

Run 1 — solusi: U6-U8+U10-U12+U14 = (a+5b)-(a+7b)+(a+9b)-(a+11b)+(a+13b) = a+9b = 20. S19 = 19/2 * (2a + 18b) = 19 * (a+9b) = 19 * 20 = 380.
- Domain kognitif `classify/applying`: Siswa perlu menyederhanakan ekspresi aljabar barisan aritmetika untuk menemukan nilai suku tengah (U10) dan menghubungkannya dengan rumus jumlah suku ke-n (Sn).. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama
- Dimensi pengetahuan `classify/procedural`: Menggunakan rumus umum suku ke-n dan rumus jumlah n suku pertama barisan aritmetika.. Bukti: Un menyatakan suku ke-n suatu barisan aritmetika
- Intended difficulty `classify/Medium`: Soal memerlukan manipulasi aljabar rutin untuk menyederhanakan deret aritmetika. Langkah-langkahnya standar dan familiar bagi siswa kelas 12.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus suku ke-n dan jumlah n suku pertama barisan aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi barisan aritmetika adalah standar kelas 12. Soal ini menguji pemahaman konsep dasar deret dengan sedikit manipulasi aljabar. |

Run 2 — solusi: U6-U8+U10-U12+U14 = (a+5b)-(a+7b)+(a+9b)-(a+11b)+(a+13b) = a+9b = 20. Rumus jumlah n suku pertama: Sn = n/2(2a+(n-1)b). Maka S19 = 19/2(2a+18b) = 19(a+9b). Substitusi nilai: 19 * 20 = 380.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus suku ke-n dan jumlah n suku pertama deret aritmetika, serta melakukan manipulasi aljabar untuk menyederhanakan ekspresi yang diberikan.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus deret aritmetika untuk menyelesaikan masalah.. Bukti: Un menyatakan suku ke-n suatu barisan aritmetika; jumlah 19 suku pertama
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah rutin: menyederhanakan persamaan deret untuk mendapatkan nilai a+9b, kemudian menggunakan rumus jumlah deret. Tingkat kesulitan menengah karena memerlukan manipulasi aljabar sebelum substitusi.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus suku ke-n dan jumlah n suku pertama deret aritmetika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar kurikulum kelas 12 untuk materi deret aritmetika, menguji kemampuan manipulasi aljabar dasar. |

Run 3 — solusi: U6-U8+U10-U12+U14 = (a+5b)-(a+7b)+(a+9b)-(a+11b)+(a+13b) = a+9b = 20. S19 = 19/2 * (2a+18b) = 19(a+9b) = 19 * 20 = 380.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat untuk menyederhanakan ekspresi aljabar barisan aritmetika dan menghubungkannya dengan rumus jumlah suku ke-n.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman konseptual tentang struktur barisan aritmetika dan prosedur manipulasi aljabar untuk menyederhanakan suku-suku yang diberikan.. Bukti: Un menyatakan suku ke-n suatu barisan aritmetika; jumlah 19 suku pertama
- Intended difficulty `classify/Medium`: Soal memerlukan manipulasi aljabar rutin untuk menyederhanakan deret aritmetika. Siswa harus mengenali pola a+9b dan menghubungkannya dengan rumus S19. Langkah-langkahnya rutin dan terstruktur.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus suku ke-n dan jumlah n suku pertama barisan aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan manipulasi aljabar pada barisan aritmetika dengan lancar. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika Un menyatakan suku ke-n suatu barisan aritmetika dan diketahui U 6 - U 8 + U 10 - U 12 + U 14 = 20, berapa jumlah 19 suku pertama barisan tersebut?
Pilihan: A. 380
B. 20
C. 360
D. 190
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `6e5ddb2020e2a12b1ecf2b03`

Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.

| Opsi | Isi |
|---|---|
| A | 635 |
| B | 315 |
| C | 310 |
| D | 320 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Rumus jumlah n suku pertama deret geometri adalah Sn = a(r^n - 1)/(r - 1). Dengan a = 5, r = 2, dan n = 6, maka S6 = 5(2^6 - 1)/(2 - 1) = 5(64 - 1)/1 = 5(63) = 315.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f67035c799da5176abb80e8b8f676e50bc45b31cef97632e201507df3f9095c8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2155 |
| 2 | success | valid / verified | applying | procedural | Easy | 2146 |
| 3 | success | valid / verified | applying | procedural | Easy | 2145 |

Run 1 — solusi: Rumus jumlah n suku pertama deret geometri adalah Sn = a(r^n - 1)/(r - 1). Dengan a = 5, r = 2, dan n = 6, maka S6 = 5(2^6 - 1)/(2 - 1) = 5(64 - 1)/1 = 5(63) = 315.
- Domain kognitif `classify/applying`: Soal ini meminta penerapan langsung rumus jumlah deret geometri yang sudah baku. Siswa hanya perlu mensubstitusi nilai yang diketahui ke dalam rumus Sn.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur perhitungan jumlah deret geometri.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan prosedur yang sangat familiar bagi siswa kelas 12. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jumlah deret geometri dan operasi perpangkatan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi deret geometri adalah materi standar SMA. Soal ini adalah aplikasi langsung rumus tanpa modifikasi, sehingga tergolong mudah. |

Run 2 — solusi: Rumus jumlah n suku pertama deret geometri adalah Sn = a(r^n - 1) / (r - 1). Dengan a = 5, r = 2, dan n = 6, maka S6 = 5(2^6 - 1) / (2 - 1) = 5(64 - 1) / 1 = 5(63) = 315.
- Domain kognitif `classify/applying`: Soal ini meminta penerapan langsung rumus jumlah deret geometri yang sudah baku. Siswa hanya perlu mensubstitusi nilai yang diketahui ke dalam rumus tanpa perlu strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau prosedur perhitungan jumlah deret geometri.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan prosedur yang sangat familiar bagi siswa kelas 12. Tidak ada kendala atau langkah nonrutin yang diperlukan.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jumlah deret geometri |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi deret geometri adalah materi dasar yang sudah dipelajari dan merupakan prosedur standar di tingkat SMA. |

Run 3 — solusi: Rumus jumlah n suku pertama deret geometri adalah Sn = a(r^n - 1) / (r - 1). Diketahui a = 5, r = 2, n = 6. Maka S6 = 5(2^6 - 1) / (2 - 1) = 5(64 - 1) / 1 = 5 * 63 = 315.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus jumlah deret geometri yang sudah diketahui parameternya. Siswa hanya perlu mensubstitusi nilai ke dalam rumus baku.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau prosedur perhitungan jumlah deret geometri.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan substitusi nilai ke dalam rumus yang sudah dikenal di tingkat SMA.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jumlah deret geometri |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi deret geometri adalah materi standar kelas 12 yang prosedurnya sangat familiar dan tidak memerlukan langkah non-rutin. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
Pilihan: A. 635
B. 315
C. 310
D. 320
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `50f81b2d500c6fab49401822`

Raka mengikuti program Youth Creative Entrepreneur di sekolahnya. Untuk membeli peralatan produksi awal, ia memperoleh dana talangan usaha sebesar Rp2.500.000,00 dari koperasi pemuda. Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun dan memberikan keringanan berupa angsuran bulanan tetap selama 2 tahun agar para peserta tidak terbebani. Sebagai bentuk tanggung jawab finansial, Raka perlu menghitung besar cicilan bulanan yang harus ia bayarkan agar pinjaman tersebut lunas sesuai perjanjian. Berapakah cicilan yang harus dibayarkan Raka setiap bulan?

| Opsi | Isi |
|---|---|
| A | Rp104.166,67 |
| B | Rp112.500,00 |
| C | Rp108.333,33 |
| D | Rp225.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bunga total = M x i x t = 2.500.000 x 0,04 x 2 = 200.000. Total pengembalian = 2.500.000 + 200.000 = 2.700.000. Cicilan per bulan = 2.700.000 / 24 = 112.500.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f5a5643552921ef92fa42254053711ceee921cd8da02040cf785297c79c2f2e8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2289 |
| 2 | success | valid / verified | applying | procedural | Easy | 2345 |
| 3 | success | valid / verified | applying | procedural | Easy | 3663 |

Run 1 — solusi: Bunga total = M x i x t = 2.500.000 x 0,04 x 2 = 200.000. Total pengembalian = 2.500.000 + 200.000 = 2.700.000. Cicilan per bulan = 2.700.000 / 24 = 112.500.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur bunga tunggal, menghitung total bunga, menambahkan ke pokok, dan membagi dengan durasi waktu (24 bulan). Ini adalah penerapan prosedur rutin pada situasi keuangan.. Bukti: Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun; Raka perlu menghitung besar cicilan bulanan
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang algoritma bunga tunggal dan langkah-langkah perhitungan angsuran tetap.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus bunga tunggal standar dan melakukan pembagian sederhana. Tidak ada kendala non-rutin atau integrasi konsep yang kompleks.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga tunggal dan operasi aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah standar kelas 12. Prosedur yang diminta sangat langsung dan familiar bagi siswa. |

Run 2 — solusi: Bunga total = M x p x n = 2.500.000 x 0,04 x 2 = 200.000. Total pengembalian = 2.500.000 + 200.000 = 2.700.000. Cicilan per bulan = 2.700.000 / (2 x 12) = 2.700.000 / 24 = 112.500.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model bunga tunggal, menghitung total bunga selama 2 tahun, menambahkan ke pokok pinjaman, lalu membagi dengan jumlah bulan. Ini adalah penerapan prosedur rutin pada situasi keuangan.. Bukti: Raka memperoleh dana talangan usaha sebesar Rp2.500.000,00; Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang algoritma perhitungan bunga tunggal dan pembagian proporsional untuk angsuran.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus bunga tunggal (B=M.i.n) dan membagi total pinjaman dengan durasi waktu dalam bulan. Tidak ada kendala kompleks atau strategi nonrutin.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bunga tunggal dan konversi tahun ke bulan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah standar kelas 12. Prosedur perhitungan langsung dan familiar bagi siswa. |

Run 3 — solusi: Bunga = 2.500.000 * 4% * 2 = 200.000. Total = 2.500.000 + 200.000 = 2.700.000. Cicilan = 2.700.000 / 24 = 112.500.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus bunga tunggal dan membagi total pinjaman dengan durasi waktu. Ini adalah penerapan prosedur rutin.. Bukti: Raka perlu menghitung besar cicilan bulanan; Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan penggunaan algoritma bunga tunggal dan pembagian aritmatika dasar.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun
- Intended difficulty `classify/Easy`: Soal menggunakan rumus bunga tunggal standar dengan langkah-langkah yang jelas dan familiar bagi siswa kelas 12.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus bunga tunggal dan konversi tahun ke bulan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah dasar keuangan di kelas 12, soal ini tidak memiliki jebakan non-rutin. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Raka mengikuti program Youth Creative Entrepreneur di sekolahnya. Untuk membeli peralatan produksi awal, ia memperoleh dana talangan usaha sebesar Rp2.500.000,00 dari koperasi pemuda. Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun dan memberikan keringanan berupa angsuran bulanan tetap selama 2 tahun agar para peserta tidak terbebani. Sebagai bentuk tanggung jawab finansial, Raka perlu menghitung besar cicilan bulanan yang harus ia bayarkan agar pinjaman tersebut lunas sesuai perjanjian. Berapakah cicilan yang harus dibayarkan Raka setiap bulan?
Pilihan: A. Rp104.166,67
B. Rp112.500,00
C. Rp108.333,33
D. Rp225.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `ada21d81536b4020ff184696`

Angga adalah seorang siswa SMA yang rajin dan memiliki semangat menabung. Setelah menerima hadiah ulang tahun berupa uang tunai sebesar Rp1.000.000,00 dari orang tuanya, ia memutuskan untuk tidak menghabiskannya begitu saja. Ia pergi ke bank dan membuka rekening tabungan khusus pelajar. Petugas bank menjelaskan bahwa tabungannya akan mendapatkan bunga tetap sebesar 5% setiap tahun dari saldo awal. Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun. Tabel 1.5 Perhitungan Nilai Tabungan Angga: Tahun 1, Bunga 5% × 1.000.000 = 50.000, Nilai Uang 1.000.000 + 50.000 = 1.050.000. Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...<br><br>Berapa nilai total tabungan Angga pada akhir tahun kedua?

| Opsi | Isi |
|---|---|
| A | Rp1.150.000,00 |
| B | Rp1.050.000,00 |
| C | Rp1.100.000,00 |
| D | Rp1.102.500,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bunga tunggal per tahun = 5% x Rp1.000.000,00 = Rp50.000,00. Saldo akhir tahun ke-2 = Saldo akhir tahun ke-1 + bunga tahun ke-2 = Rp1.050.000,00 + Rp50.000,00 = Rp1.100.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `463c42a408c439163b604750da8148095cfded9b8d388268eaa2e39da30921f4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2293 |
| 2 | success | valid / verified | applying | procedural | Easy | 2280 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2270 |

Run 1 — solusi: Bunga tunggal per tahun = 5% x Rp1.000.000,00 = Rp50.000,00. Saldo akhir tahun ke-2 = Saldo akhir tahun ke-1 + bunga tahun ke-2 = Rp1.050.000,00 + Rp50.000,00 = Rp1.100.000,00.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan konsep bunga tunggal sederhana dengan melanjutkan pola perhitungan yang sudah diberikan dalam tabel. Siswa hanya perlu melakukan operasi penjumlahan dasar setelah mengidentifikasi besaran bunga yang konstan.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip bunga tunggal di mana bunga dihitung berdasarkan modal awal (bukan saldo berjalan), yang merupakan konsep dasar dalam matematika keuangan.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan langsung. Siswa diberikan skema perhitungan yang jelas dan hanya perlu melanjutkan satu langkah perhitungan sederhana. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun; Tabel 1.5 Perhitungan Nilai Tabungan Angga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 12, soal ini sangat mendasar karena hanya melibatkan aritmatika sederhana dengan konsep bunga tunggal yang sudah dijelaskan langkah-langkahnya dalam soal. |

Run 2 — solusi: Bunga tunggal per tahun adalah 5% dari Rp1.000.000,00 = Rp50.000,00. Saldo akhir tahun ke-1 = Rp1.050.000,00. Saldo akhir tahun ke-2 = Saldo akhir tahun ke-1 + Bunga = Rp1.050.000,00 + Rp50.000,00 = Rp1.100.000,00.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep bunga tunggal sederhana dengan mengikuti pola yang sudah diberikan dalam tabel. Proses ini bersifat rutin dan langsung.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung bunga tunggal dan akumulasi saldo secara bertahap.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena pola perhitungan sudah disediakan dalam tabel. Siswa hanya perlu melanjutkan satu langkah perhitungan rutin.. Bukti: Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun; Tabel 1.5 Perhitungan Nilai Tabungan Angga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar (penjumlahan dan persentase). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah topik dasar kelas 12. Soal ini memberikan skema tabel yang sangat membantu, sehingga beban kognitif sangat rendah. |

Run 3 — solusi: Bunga tunggal per tahun tetap sebesar 5% dari modal awal (Rp1.000.000,00) = Rp50.000,00. Saldo akhir tahun ke-2 = Saldo akhir tahun ke-1 + Bunga tahun ke-2 = Rp1.050.000,00 + Rp50.000,00 = Rp1.100.000,00.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan konsep bunga tunggal sederhana dengan menambahkan bunga tetap ke saldo sebelumnya. Proses ini bersifat rutin dan langsung.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip bunga tunggal (bunga dihitung dari modal awal, bukan saldo berjalan) untuk menyelesaikan soal.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena menggunakan prosedur bunga tunggal yang sangat familiar, instruksi eksplisit, dan struktur tabel yang memandu langkah penyelesaian.. Bukti: Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun; Tabel 1.5 Perhitungan Nilai Tabungan Angga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi aritmatika dan konsep bunga tunggal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah topik dasar kelas 12. Soal ini tidak menuntut analisis kompleks, hanya aplikasi langsung dari definisi bunga tunggal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4082`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep bunga tunggal sederhana dengan melanjutkan pola perhitungan yang sudah diberikan dalam tabel. Proses ini bersifat rutin dan langsung.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami prinsip bunga tunggal di mana bunga dihitung berdasarkan modal awal (bukan saldo berjalan), yang merupakan konsep dasar dalam matematika keuangan.
- Intended difficulty `Easy`: Soal ini bersifat prosedural dan langsung. Siswa diberikan skema perhitungan yang jelas dan hanya perlu melanjutkan satu langkah perhitungan sederhana. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 12, soal ini sangat mendasar karena hanya melibatkan aritmatika sederhana dengan konsep bunga tunggal yang sudah dijelaskan langkah-langkahnya dalam soal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Angga adalah seorang siswa SMA yang rajin dan memiliki semangat menabung. Setelah menerima hadiah ulang tahun berupa uang tunai sebesar Rp1.000.000,00 dari orang tuanya, ia memutuskan untuk tidak menghabiskannya begitu saja. Ia pergi ke bank dan membuka rekening tabungan khusus pelajar. Petugas bank menjelaskan bahwa tabungannya akan mendapatkan bunga tetap sebesar 5% setiap tahun dari saldo awal. Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun. Tabel 1.5 Perhitungan Nilai Tabungan Angga: Tahun 1, Bunga 5% × 1.000.000 = 50.000, Nilai Uang 1.000.000 + 50.000 = 1.050.000. Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...

Berapa nilai total tabungan Angga pada akhir tahun kedua?
Pilihan: A. Rp1.150.000,00
B. Rp1.050.000,00
C. Rp1.100.000,00
D. Rp1.102.500,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d215f8aa8bc3bed140f75b0b`

Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.<br><br>d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

| Opsi | Isi |
|---|---|
| A | Uang Gigih lebih banyak, selisihnya Rp9.000,00 |
| B | Uang Gigih lebih banyak, selisihnya Rp92.741,00 |
| C | Uang Firman lebih banyak, selisihnya Rp92.741,00 |
| D | Sama banyak, selisihnya Rp0,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Firman (bunga tunggal): 10.000.000 * (1 + 0,03 * 5) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1,03)^5 = 11.592.741. Selisih: 11.592.741 - 11.500.000 = 92.741.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `110623e536979ba77c9f2c11f29da07111040b83d2b19174b3a520a209fb0402`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2504 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2470 |
| 3 | success | valid / verified | applying | procedural | Medium | 2459 |

Run 1 — solusi: Firman (bunga tunggal): 10.000.000 * (1 + 0,03 * 5) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1 + 0,03)^5 = 10.000.000 * 1,1592741 = 11.592.741. Selisih: 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan mendasar antara skema bunga tunggal (Firman) dan bunga majemuk (Gigih), kemudian menerapkan rumus yang sesuai untuk masing-masing skema dalam konteks investasi jangka panjang.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga ke rekening tabungan; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bunga dihitung dan diakumulasikan (bunga tunggal vs majemuk) serta kemampuan prosedural untuk menghitung nilai akhir investasi.. Bukti: bunga 3% per tahun; Setiap tahun bank mengirim bunga ke rekening tabungan; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus membedakan dua konsep bunga yang berbeda (tunggal vs majemuk) dan melakukan perhitungan untuk kedua skema tersebut sebelum membandingkannya. Ini melibatkan pemilihan prosedur yang tepat dan perhitungan yang sedikit lebih kompleks daripada sekadar satu langkah.. Bukti: Firman menyimpan uang... bunga 3% per tahun; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bunga tunggal dan bunga majemuk, serta operasi aritmatika dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena membandingkan dua model pertumbuhan uang yang umum dipelajari dalam materi keuangan matematika. |

Run 2 — solusi: Firman (bunga tunggal): M_n = M_0(1 + n*i) = 10.000.000(1 + 5*0,03) = 11.500.000. Gigih (bunga majemuk): M_n = M_0(1 + i)^n = 10.000.000(1,03)^5 = 10.000.000(1,1592740743) = 11.592.741. Selisih = 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan skema bunga (tunggal vs majemuk) dari deskripsi naratif, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan untuk membandingkan hasil akhir.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga ke rekening tabungan; Gigih... meminta bank untuk menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip konseptual bunga tunggal (bunga tidak diakumulasi ke pokok) dan bunga majemuk (bunga diakumulasi ke pokok) untuk menentukan model matematika yang relevan.. Bukti: bunga 3% per tahun; Setiap tahun bank mengirim bunga ke rekening tabungan; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus membedakan dua konsep bunga yang berbeda dari narasi, menerapkan dua rumus yang berbeda, dan melakukan perhitungan aritmatika yang melibatkan eksponen (bunga majemuk).. Bukti: Firman menyimpan uang... bunga 3% per tahun; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bunga tunggal dan bunga majemuk, operasi aritmatika dasar, dan penggunaan eksponen. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena membandingkan dua model keuangan yang merupakan standar kurikulum keuangan matematika SMA. |

Run 3 — solusi: Firman (bunga tunggal): 10.000.000 * (1 + 0,03 * 5) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1,03)^5 = 11.592.741. Selisih: 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan skema bunga (tunggal vs majemuk) dan menerapkan rumus yang sesuai untuk kedua skema tersebut, kemudian menghitung selisihnya. Ini adalah penerapan konsep bunga pada situasi rutin.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga tunggal; Gigih... menambahkan bunganya ke dalam nilai depositonya... bunga majemuk; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung bunga tunggal dan bunga majemuk serta prinsip konseptual di balik perbedaan akumulasi nilai uang dari kedua metode tersebut.. Bukti: bunga 3% per tahun; bunga tunggal; bunga majemuk
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua prosedur rutin yang berbeda (bunga tunggal dan majemuk) dan membandingkan hasilnya. Siswa harus memilih rumus yang tepat untuk masing-masing skenario.. Bukti: Firman menyimpan uang... bunga 3% per tahun; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan bunga majemuk. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena membandingkan dua model keuangan yang umum dipelajari di tingkat SMA. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4389`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi perbedaan skema bunga (tunggal vs majemuk) dari deskripsi naratif, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan untuk membandingkan hasil akhir.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami prinsip konseptual bunga tunggal (bunga tidak diakumulasi ke pokok) dan bunga majemuk (bunga diakumulasi ke pokok) untuk menentukan model matematika yang relevan.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus membedakan dua konsep bunga yang berbeda dari narasi, menerapkan dua rumus yang berbeda, dan melakukan perhitungan aritmatika yang melibatkan eksponen (bunga majemuk).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bunga tunggal dan bunga majemuk, operasi aritmatika dasar, dan penggunaan eksponen. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena membandingkan dua model keuangan yang merupakan standar kurikulum keuangan matematika SMA. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Bunga
Tipe soal: multiple_choice
Stimulus: -
Soal: Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.

d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
Pilihan: A. Uang Gigih lebih banyak, selisihnya Rp9.000,00
B. Uang Gigih lebih banyak, selisihnya Rp92.741,00
C. Uang Firman lebih banyak, selisihnya Rp92.741,00
D. Sama banyak, selisihnya Rp0,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `b599e139114197a77a84c95d`

Pak Roni merupakan anggota koperasi simpan pinjam. Pak Roni menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun.<br><br>Berapa jumlah simpanan Pak Roni setelah 5 tahun?

| Opsi | Isi |
|---|---|
| A | Rp15.750.000,00 |
| B | Rp15.075.000,00 |
| C | Rp16.500.000,00 |
| D | Rp750.000,00 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bunga = 15.000.000 * 1% * 5 = 750.000. Modal akhir = 15.000.000 + 750.000 = 15.750.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `14d15e2d181b42379978393ae344d90c4779e2f84b6917bfedd253e5abfbdd7e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2926 |
| 2 | success | valid / verified | applying | procedural | Easy | 2996 |
| 3 | success | valid / verified | applying | procedural | Easy | 2724 |

Run 1 — solusi: Bunga = 15.000.000 * 1% * 5 = 750.000. Modal akhir = 15.000.000 + 750.000 = 15.750.000.
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan rumus bunga tunggal sederhana (M * i * n) dan menjumlahkannya dengan modal awal. Ini adalah proses rutin.. Bukti: menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep bunga tunggal dan bagaimana menggunakannya dalam perhitungan keuangan sederhana.. Bukti: bunga koperasi 1% per tahun; jumlah simpanan Pak Roni setelah 5 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan rumus standar bunga tunggal dengan angka yang sederhana. Tidak ada kendala atau strategi non-rutin.. Bukti: bunga koperasi 1% per tahun; setelah 5 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan operasi aritmatika dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 sebagai pengingat konsep dasar keuangan, namun secara kognitif sangat mudah. |

Run 2 — solusi: Bunga = 15.000.000 * 1% * 5 = 750.000. Modal akhir = 15.000.000 + 750.000 = 15.750.000.
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan rumus bunga tunggal sederhana (M + M*i*t) yang merupakan prosedur rutin.. Bukti: menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang perhitungan bunga tunggal.. Bukti: bunga koperasi 1% per tahun; jumlah simpanan Pak Roni setelah 5 tahun
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan satu rumus bunga tunggal tanpa variasi atau kendala tambahan.. Bukti: bunga koperasi 1% per tahun; setelah 5 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan operasi aritmatika persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sangat mudah untuk kelas 12, hanya melibatkan substitusi rumus dasar. |

Run 3 — solusi: Bunga = 15.000.000 * 1% * 5 = 750.000. Total simpanan = 15.000.000 + 750.000 = 15.750.000.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus bunga tunggal (M + M*i*t) pada situasi keuangan yang rutin dan sederhana.. Bukti: menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma perhitungan bunga tunggal yang sudah baku.. Bukti: bunga koperasi 1% per tahun; jumlah simpanan Pak Roni setelah 5 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu prosedur perhitungan bunga tunggal yang langsung, tanpa kendala atau integrasi konsep yang kompleks.. Bukti: bunga koperasi 1% per tahun; setelah 5 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan operasi aritmatika dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi bunga tunggal adalah dasar keuangan kelas 12. Soal ini tidak memerlukan strategi nonrutin atau pemahaman mendalam, sehingga dikategorikan mudah. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Suku Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Roni merupakan anggota koperasi simpan pinjam. Pak Roni menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun.

Berapa jumlah simpanan Pak Roni setelah 5 tahun?
Pilihan: A. Rp15.750.000,00
B. Rp15.075.000,00
C. Rp16.500.000,00
D. Rp750.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `5a320ce9d400ac199d8082a9`

Pak Bayu merupakan anggota koperasi "Maju Bersama". Beliau menyimpan modal awal sebesar Rp1.000.000,00 di koperasi tersebut. Koperasi memberikan bunga tunggal sebesar 18% per tahun untuk simpanan anggota. Pak Bayu menyimpan modalnya selama 8 bulan.<br><br>Hitunglah berapa besar bunga yang akan diterima dan berapa total simpanan Pak Bayu setelah 8 bulan?

| Opsi | Isi |
|---|---|
| A | Bunga Rp1.440.000,00, total simpanan Rp2.440.000,00 |
| B | Bunga Rp120.000,00, total simpanan Rp1.120.000,00 |
| C | Bunga Rp126.492,00, total simpanan Rp1.126.492,00 |
| D | Bunga Rp120.000,00, total simpanan Rp120.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bunga = Modal x (suku bunga per tahun / 12) x waktu (bulan) = 1.000.000 x (18%/12) x 8 = 1.000.000 x 1,5% x 8 = 120.000. Total simpanan = Modal + Bunga = 1.000.000 + 120.000 = 1.120.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ceab0ca4a7384c2b88c55d6ced80a3a2689f17f065d64a2f726059f9f866c5aa`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2318 |
| 2 | success | valid / verified | applying | procedural | Easy | 2340 |
| 3 | success | valid / verified | applying | procedural | Easy | 2313 |

Run 1 — solusi: Bunga = Modal x (suku bunga per tahun / 12) x waktu (bulan) = 1.000.000 x (18%/12) x 8 = 1.000.000 x 1,5% x 8 = 120.000. Total simpanan = Modal + Bunga = 1.000.000 + 120.000 = 1.120.000.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur bunga tunggal yang tepat, mengonversi suku bunga tahunan ke bulanan, dan menerapkan rumus bunga tunggal serta penjumlahan modal. Ini adalah penerapan prosedur rutin pada situasi keuangan sederhana.. Bukti: Koperasi memberikan bunga tunggal sebesar 18% per tahun; Pak Bayu menyimpan modalnya selama 8 bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan bunga tunggal dan urutan langkah untuk mendapatkan total simpanan.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan familiar bagi siswa kelas 12. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan bunga tunggal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah materi standar kelas 12 yang prosedurnya sangat familiar dan langsung. |

Run 2 — solusi: Bunga = Modal x suku bunga per bulan x lama bulan = 1.000.000 x (18%/12) x 8 = 1.000.000 x 0,015 x 8 = 120.000. Total simpanan = Modal + Bunga = 1.000.000 + 120.000 = 1.120.000.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur bunga tunggal yang tepat, mengonversi satuan waktu (tahun ke bulan), dan menerapkan rumus bunga tunggal untuk situasi rutin.. Bukti: Koperasi memberikan bunga tunggal sebesar 18% per tahun; Pak Bayu menyimpan modalnya selama 8 bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang perhitungan bunga tunggal dan konversi periode waktu yang relevan.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas (konversi bunga, hitung bunga, jumlahkan dengan modal). Tidak ada kendala kompleks atau strategi nonrutin.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan aritmatika persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah standar kurikulum kelas 12. Soal ini adalah aplikasi langsung dari rumus tanpa modifikasi variabel yang rumit. |

Run 3 — solusi: Bunga (B) = M x i x t = 1.000.000 x (18%/12) x 8 = 1.000.000 x 0,015 x 8 = 120.000. Total simpanan = M + B = 1.000.000 + 120.000 = 1.120.000.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur bunga tunggal yang tepat, mengonversi satuan waktu (tahun ke bulan), dan menerapkan rumus bunga tunggal untuk situasi rutin.. Bukti: Koperasi memberikan bunga tunggal sebesar 18% per tahun; Pak Bayu menyimpan modalnya selama 8 bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perhitungan bunga tunggal dan konversi satuan waktu yang relevan.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan rumus bunga tunggal dengan penyesuaian satuan waktu yang sederhana.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan konversi satuan waktu (tahun ke bulan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah standar kurikulum kelas 12. Soal ini menggunakan prosedur standar tanpa jebakan kompleks, sehingga tergolong mudah bagi siswa kelas 12. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Suku Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Bayu merupakan anggota koperasi "Maju Bersama". Beliau menyimpan modal awal sebesar Rp1.000.000,00 di koperasi tersebut. Koperasi memberikan bunga tunggal sebesar 18% per tahun untuk simpanan anggota. Pak Bayu menyimpan modalnya selama 8 bulan.

Hitunglah berapa besar bunga yang akan diterima dan berapa total simpanan Pak Bayu setelah 8 bulan?
Pilihan: A. Bunga Rp1.440.000,00, total simpanan Rp2.440.000,00
B. Bunga Rp120.000,00, total simpanan Rp1.120.000,00
C. Bunga Rp126.492,00, total simpanan Rp1.126.492,00
D. Bunga Rp120.000,00, total simpanan Rp120.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `affcbcedba377489f39a2309`

Seluruh bank di suatu wilayah menawarkan deposito dengan bunga 5%–7% per tahun. Bank XYZ termasuk salah satu bank di wilayah tersebut dengan Ahmad dan Maya sebagai nasabahnya. Ahmad telah menjadi nasabah selama 5 tahun dan Maya telah menjadi nasabah selama 10 tahun.<br><br>Jika saldo deposito Ahmad menjadi Rp26.764.500,00, uang yang disetorkan oleh Ahmad mula-mula adalah ....

| Opsi | Isi |
|---|---|
| A | Rp24.000.000,00 |
| B | Rp22.000.000,00 |
| C | Rp18.000.000,00 |
| D | Rp20.000.000,00 |

Kunci sumber: `D`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal tidak dapat diselesaikan secara pasti karena suku bunga tidak ditentukan (hanya rentang 5-7%). Jika diasumsikan 5%, PV = 26.764.500 / (1,05)^5 ≈ 20.970.686. Jika diasumsikan 7%, PV = 26.764.500 / (1,07)^5 ≈ 19.086.565. Tidak ada informasi yang cukup untuk memilih satu nilai spesifik atau membenarkan opsi D.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `505e3216464b17c0df41f9f597b8f8981443ee911081ea500d6c07b2b2189230`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | applying | procedural | Medium | 2431 |
| 2 | success | concern / conflict | applying | procedural | Medium | 2339 |
| 3 | success | concern / conflict | applying | procedural | Medium | 2341 |

Run 1 — solusi: Bunga majemuk: A = P(1+i)^n. Dengan i=5% (asumsi terendah) dan n=5, P = 26.764.500 / (1,05)^5 = 20.970.686. Hasil ini tidak mendekati opsi D (20.000.000) secara akurat. Soal tidak memiliki informasi cukup untuk menentukan suku bunga spesifik atau membenarkan pembulatan yang digunakan.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur bunga majemuk dan menerapkan rumus nilai sekarang (present value) untuk mencari modal awal, yang merupakan proses applying.. Bukti: Ahmad telah menjadi nasabah selama 5 tahun; saldo deposito Ahmad menjadi Rp26.764.500,00; bunga 5%–7% per tahun
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara modal awal, suku bunga, periode, dan saldo akhir (konsep bunga majemuk) serta menerapkan algoritma perhitungannya.. Bukti: bunga 5%–7% per tahun; saldo deposito Ahmad menjadi Rp26.764.500,00
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan prosedur bunga majemuk dan manipulasi aljabar dasar. Namun, karena adanya ambiguitas data (rentang bunga) dan ketidakakuratan opsi jawaban, tingkat kesulitan teknis menjadi tidak terdefinisi dengan baik.. Bukti: bunga 5%–7% per tahun; Ahmad telah menjadi nasabah selama 5 tahun; saldo deposito Ahmad menjadi Rp26.764.500,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bunga majemuk dan penggunaan kalkulator/logaritma untuk eksponen. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Secara teoretis, ini adalah soal rutin kelas 12, namun cacat pada data soal membuatnya sulit diselesaikan dengan logika matematika yang konsisten. |

Run 2 — solusi: Soal tidak dapat diselesaikan secara pasti karena suku bunga tidak ditentukan (hanya rentang 5-7%). Jika diasumsikan 5%, PV = 26.764.500 / (1,05)^5 = 20.970.686. Jika diasumsikan 7%, PV = 26.764.500 / (1,07)^5 = 19.086.565. Tidak ada informasi yang cukup untuk memilih satu nilai spesifik.
- Domain kognitif `classify/applying`: Siswa diharapkan menerapkan rumus bunga majemuk PV = FV / (1+i)^n. Namun, karena variabel i (suku bunga) tidak ditentukan secara spesifik, siswa tidak dapat melakukan perhitungan yang valid.. Bukti: menawarkan deposito dengan bunga 5%–7% per tahun; uang yang disetorkan oleh Ahmad mula-mula adalah
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang rumus bunga majemuk, namun gagal menyediakan data faktual yang cukup untuk eksekusi.. Bukti: deposito dengan bunga 5%–7% per tahun; saldo deposito Ahmad menjadi Rp26.764.500,00
- Intended difficulty `classify/Medium`: Secara struktur, ini adalah soal rutin bunga majemuk. Namun, karena ambiguitas data (rentang bunga), soal ini cacat secara konten.. Bukti: bunga 5%–7% per tahun; nasabah selama 5 tahun; saldo deposito Ahmad menjadi Rp26.764.500,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus bunga majemuk PV = FV / (1+i)^n |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini seharusnya mudah bagi siswa kelas 12 jika data lengkap, namun menjadi tidak valid karena kurangnya informasi spesifik mengenai suku bunga. |

Run 3 — solusi: Soal tidak dapat diselesaikan secara pasti karena suku bunga tidak spesifik (rentang 5-7%). Jika diasumsikan 5%, PV = 26.764.500 / (1,05)^5 ≈ 20.970.686. Nilai ini tidak sama dengan opsi D (20.000.000).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus bunga majemuk PV = FV / (1+i)^n untuk mencari nilai awal (present value).. Bukti: Bank XYZ termasuk salah satu bank di wilayah tersebut dengan bunga 5%–7% per tahun; uang yang disetorkan oleh Ahmad mula-mula adalah
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma perhitungan bunga majemuk untuk menyelesaikan masalah keuangan.. Bukti: deposito dengan bunga 5%–7% per tahun; saldo deposito Ahmad menjadi Rp26.764.500,00
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemilihan prosedur bunga majemuk dan penanganan ketidakpastian data (rentang bunga), meskipun eksekusi akhirnya terhambat oleh data yang tidak konsisten.. Bukti: bunga 5%–7% per tahun; nasabah selama 5 tahun; saldo deposito Ahmad menjadi Rp26.764.500,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bunga majemuk dan penggunaan kalkulator/logaritma untuk mencari nilai awal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah standar kelas 12. Kesulitan muncul dari ambiguitas data bunga yang diberikan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4203`.
Konten: `concern`; kunci: `conflict`; masalah: Soal memberikan rentang suku bunga (5%–7%) tanpa menentukan suku bunga spesifik yang digunakan oleh Bank XYZ, sehingga perhitungan nilai awal (present value) tidak dapat ditentukan secara pasti.; Opsi jawaban yang tersedia tidak konsisten dengan perhitungan bunga majemuk standar menggunakan rentang bunga yang diberikan. Sebagai contoh, dengan bunga 5%, PV = 26.764.500 / (1,05)^5 ≈ 20.970.686, dan dengan bunga 7%, PV ≈ 19.086.565. Tidak ada opsi yang mendekati hasil perhitungan ini secara akurat.; Kunci jawaban D (20.000.000) tidak dapat dibenarkan secara matematis dari data yang tersedia..
- Domain kognitif `applying`: Siswa diharapkan menerapkan rumus bunga majemuk PV = FV / (1+i)^n untuk mencari nilai awal. Namun, karena variabel i (suku bunga) tidak ditentukan secara spesifik, siswa tidak dapat melakukan perhitungan yang valid.
- Dimensi pengetahuan `procedural`: Siswa harus memahami hubungan antara modal awal, suku bunga, periode, dan saldo akhir (konsep bunga majemuk) serta menerapkan algoritma perhitungannya.
- Intended difficulty `Medium`: Secara struktur, ini adalah soal rutin bunga majemuk. Namun, karena ambiguitas data (rentang bunga) dan ketidakakuratan opsi, soal ini cacat secara konten.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus bunga majemuk PV = FV / (1+i)^n |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini seharusnya rutin bagi siswa kelas 12, namun menjadi tidak valid karena kurangnya informasi spesifik mengenai suku bunga. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Seluruh bank di suatu wilayah menawarkan deposito dengan bunga 5%–7% per tahun. Bank XYZ termasuk salah satu bank di wilayah tersebut dengan Ahmad dan Maya sebagai nasabahnya. Ahmad telah menjadi nasabah selama 5 tahun dan Maya telah menjadi nasabah selama 10 tahun.

Jika saldo deposito Ahmad menjadi Rp26.764.500,00, uang yang disetorkan oleh Ahmad mula-mula adalah ....
Pilihan: A. Rp24.000.000,00
B. Rp22.000.000,00
C. Rp18.000.000,00
D. Rp20.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal memberikan rentang suku bunga (5%–7%) tanpa menentukan suku bunga spesifik yang digunakan oleh Bank XYZ, sehingga perhitungan nilai awal (present value) tidak dapat ditentukan secara pasti.; Opsi jawaban yang tersedia tidak konsisten dengan perhitungan bunga majemuk standar menggunakan rentang bunga yang diberikan. Sebagai contoh, dengan bunga 5%, PV = 26.764.500 / (1,05)^5 ≈ 20.970.686, dan dengan bunga 7%, PV ≈ 19.086.565. Tidak ada opsi yang mendekati hasil perhitungan ini secara akurat.; Kunci jawaban D (20.000.000) tidak dapat dibenarkan secara matematis dari data yang tersedia..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `36b2b05ba07a1b3dfb573f9e`

Seseorang berinvestasi saham di suatu aplikasi online. Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.

| Opsi | Isi |
|---|---|
| A | Rp6.612.500,00 |
| B | Rp7.604.375,00 |
| C | Rp8.573.750,00 |
| D | Rp7.250.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Menggunakan rumus bunga majemuk: Mn = M0(1 + i)^n. Diketahui M0 = 5.000.000, i = 0,15, dan n = 3. Maka, Mn = 5.000.000 * (1 + 0,15)^3 = 5.000.000 * (1,15)^3 = 5.000.000 * 1,520875 = 7.604.375.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c73e201470dc5fa9804efd3bc367c0debed6f06dbd66fc615ff71115edac46c8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2189 |
| 2 | success | valid / verified | applying | procedural | Easy | 2211 |
| 3 | success | valid / verified | applying | procedural | Easy | 2207 |

Run 1 — solusi: Menggunakan rumus bunga majemuk: Mn = M0(1 + i)^n. Diketahui M0 = 5.000.000, i = 0,15, dan n = 3. Maka, Mn = 5.000.000 * (1 + 0,15)^3 = 5.000.000 * (1,15)^3 = 5.000.000 * 1,520875 = 7.604.375.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan rumus bunga majemuk secara langsung dengan nilai yang sudah ditentukan dalam soal.. Bukti: Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau prosedur perhitungan bunga majemuk.. Bukti: suku bunga majemuk 15% per tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan substitusi nilai ke dalam rumus bunga majemuk yang sudah umum dipelajari di kelas 12.. Bukti: Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan penggunaan rumus Mn = M0(1+i)^n. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 12 yang menguji kemampuan komputasi dasar bunga majemuk tanpa variasi kompleksitas. |

Run 2 — solusi: Menggunakan rumus bunga majemuk Mn = M0(1 + i)^n. Diketahui M0 = 5.000.000, i = 0,15, dan n = 3. Maka Mn = 5.000.000 * (1 + 0,15)^3 = 5.000.000 * (1,15)^3 = 5.000.000 * 1,520875 = 7.604.375.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga majemuk yang sudah dipelajari untuk menghitung nilai akhir modal. Ini adalah prosedur rutin yang langsung.. Bukti: Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau prosedur perhitungan bunga majemuk.. Bukti: suku bunga majemuk 15% per tahun; Hitunglah nilai akhir modal tersebut setelah 3 tahun
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus bunga majemuk dengan variabel yang sudah jelas. Tidak ada langkah tambahan atau jebakan yang kompleks.. Bukti: Modal usaha yang diberikan sebesar Rp5.000.000,00.; suku bunga majemuk 15% per tahun.; setelah 3 tahun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan penggunaan rumus Mn = M0(1+i)^n. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 sebagai soal latihan rutin mengenai bunga majemuk dengan angka yang standar. |

Run 3 — solusi: Menggunakan rumus bunga majemuk Mn = P(1 + i)^n. Diketahui P = 5.000.000, i = 0,15, dan n = 3. Maka Mn = 5.000.000 * (1 + 0,15)^3 = 5.000.000 * (1,15)^3 = 5.000.000 * 1,520875 = 7.604.375.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus bunga majemuk yang sudah dipelajari di kelas 12. Siswa hanya perlu mengidentifikasi variabel dan memasukkannya ke dalam rumus.. Bukti: Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang penggunaan rumus bunga majemuk untuk menghitung nilai akhir investasi.. Bukti: suku bunga majemuk 15% per tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan rumus Mn = P(1+i)^n tanpa modifikasi atau langkah tambahan yang kompleks.. Bukti: Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan penggunaan kalkulator/perkalian desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah standar kurikulum kelas 12. Soal ini adalah aplikasi langsung rumus dasar tanpa variasi periode atau anuitas. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang berinvestasi saham di suatu aplikasi online. Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.
Pilihan: A. Rp6.612.500,00
B. Rp7.604.375,00
C. Rp8.573.750,00
D. Rp7.250.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `1bc4c0c055bdae30032aa047`

Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.<br><br>Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan.

| Opsi | Isi |
|---|---|
| A | 41 |
| B | 44 |
| C | 42 |
| D | 43 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `43`.
Solusi minimum hasil AI: FV = A * [((1+i)^n - 1) / i]. Diketahui FV=100.000.000, A=2.000.000, i=0,09/12=0,0075. Maka 100.000.000 = 2.000.000 * [((1,0075)^n - 1) / 0,0075]. 50 = ((1,0075)^n - 1) / 0,0075. 0,375 = (1,0075)^n - 1. 1,375 = (1,0075)^n. n = log(1,375) / log(1,0075) ≈ 42,75. Karena harus mencapai target, n dibulatkan ke atas menjadi 43.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `de62ce6b3f644f4bb9b35eb769b13ef6d31bdac30ba2dfcdb146cc4757298032`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2355 |
| 2 | success | valid / verified | applying | procedural | Medium | 2296 |
| 3 | success | valid / verified | applying | procedural | Medium | 2394 |

Run 1 — solusi: FV = A * [((1+i)^n - 1) / i]. Diketahui FV=100.000.000, A=2.000.000, i=0,09/12=0,0075. Maka 100.000.000 = 2.000.000 * [((1,0075)^n - 1) / 0,0075]. 50 = ((1,0075)^n - 1) / 0,0075. 0,375 = (1,0075)^n - 1. 1,375 = (1,0075)^n. n = log(1,375) / log(1,0075) ≈ 42,75. Karena harus mencapai target, n dibulatkan ke atas menjadi 43.
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus anuitas yang tepat (Future Value of Ordinary Annuity), melakukan konversi suku bunga tahunan ke bulanan, dan menyelesaikan persamaan logaritma untuk mencari n, kemudian melakukan pembulatan yang tepat sesuai konteks masalah.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus anuitas dan teknik penyelesaian persamaan eksponensial/logaritma dalam konteks keuangan.. Bukti: memberikan bunga 9% per tahun; rumus FV anuitas untuk n
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: konversi suku bunga, pemilihan rumus anuitas yang tepat, manipulasi aljabar untuk isolasi variabel n, dan interpretasi hasil pembulatan dalam konteks nyata (mencapai target).. Bukti: bunga 9% per tahun; Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep anuitas, logaritma, dan konversi suku bunga. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menerapkan rumus keuangan dan menyelesaikan persamaan logaritma sederhana dalam konteks investasi. |

Run 2 — solusi: FV = A * [((1+i)^n - 1) / i]. 100.000.000 = 2.000.000 * [((1+0,0075)^n - 1) / 0,0075]. 50 = (1,0075^n - 1) / 0,0075. 0,375 = 1,0075^n - 1. 1,375 = 1,0075^n. n = log(1,375) / log(1,0075) ≈ 42,6. Karena harus mencapai target, dibulatkan ke atas menjadi 43 bulan.
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus anuitas yang tepat (Future Value of Ordinary Annuity), melakukan konversi suku bunga tahunan ke bulanan, dan menyelesaikan persamaan logaritma untuk mencari n.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus anuitas dan manipulasi aljabar untuk variabel waktu (n).. Bukti: memberikan bunga 9% per tahun; rumus FV anuitas untuk n
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi suku bunga (tahunan ke bulanan), pemilihan rumus anuitas yang tepat, dan penyelesaian logaritma untuk n, yang merupakan prosedur rutin namun melibatkan beberapa langkah.. Bukti: bunga 9% per tahun; Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep anuitas, logaritma dasar, dan konversi satuan bunga. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menerapkan rumus keuangan majemuk/anuitas dan menyelesaikan persamaan eksponensial/logaritma sederhana. |

Run 3 — solusi: Target FV = 100.000.000, A = 2.000.000, i = 9%/12 = 0,0075. Rumus FV anuitas biasa: FV = A * ((1+i)^n - 1) / i. 100.000.000 = 2.000.000 * ((1,0075)^n - 1) / 0,0075. 50 = ((1,0075)^n - 1) / 0,0075. 0,375 = (1,0075)^n - 1. 1,375 = (1,0075)^n. n = log(1,375) / log(1,0075) ≈ 42,78. Karena harus mencapai target, dibulatkan ke atas menjadi 43 bulan.
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus anuitas yang tepat (Future Value), melakukan konversi suku bunga tahunan ke bulanan, dan menyelesaikan persamaan logaritma untuk mencari n, kemudian melakukan pembulatan yang tepat sesuai konteks target tabungan.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang penggunaan rumus anuitas dan konversi satuan waktu/bunga, serta pemahaman konseptual tentang bagaimana bunga majemuk bekerja dalam akumulasi tabungan.. Bukti: bunga 9% per tahun; Rp2.000.000,00 setiap bulan; rumus FV anuitas
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: konversi suku bunga, pemilihan rumus anuitas yang tepat, manipulasi aljabar (logaritma), dan interpretasi hasil pembulatan dalam konteks keuangan (pembulatan ke atas untuk mencapai target).. Bukti: bunga 9% per tahun; Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung agar dapat mencapai targetnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bunga majemuk, rumus anuitas, logaritma dasar. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menangani perhitungan keuangan dengan logaritma dan pembulatan konteks nyata. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.

Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan.
Pilihan: A. 41
B. 44
C. 42
D. 43
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `6e3411514cf1a09e78e56ecd`

Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.<br><br>Nilai masa depan dari tabungannya setelah empat tahun adalah ....

| Opsi | Isi |
|---|---|
| A | Rp115.000.000,00 |
| B | Rp113.000.000,00 |
| C | Rp114.000.000,00 |
| D | Rp112.000.000,00 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: FV = PMT * [(1 + i)^n - 1] / i. PMT = 2.000.000, i = 0,09/12 = 0,0075, n = 4 * 12 = 48. FV = 2.000.000 * [(1,0075)^48 - 1] / 0,0075 = 2.000.000 * [1,431405 - 1] / 0,0075 = 2.000.000 * 57,52066 = 115.041.320. Dibulatkan menjadi Rp115.000.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `58d52c904af93aae7fc24523a7f684cdef507a1e990d96d0d296583ed44fd400`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2419 |
| 2 | success | valid / verified | applying | procedural | Medium | 2399 |
| 3 | success | valid / verified | applying | procedural | Medium | 2416 |

Run 1 — solusi: FV = PMT * [(1 + i)^n - 1] / i. PMT = 2.000.000, i = 0,09/12 = 0,0075, n = 4 * 12 = 48. FV = 2.000.000 * [(1,0075)^48 - 1] / 0,0075 = 2.000.000 * [1,431405 - 1] / 0,0075 = 2.000.000 * 57,52066 = 115.041.320. Dibulatkan menjadi Rp115.000.000,00.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah anuitas biasa (ordinary annuity), memilih rumus nilai masa depan (future value) yang tepat, melakukan konversi suku bunga tahunan ke bulanan, dan menghitung hasilnya.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; bunga 9% per tahun; Nilai masa depan dari tabungannya setelah empat tahun adalah
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur algoritma keuangan (anuitas) untuk menyelesaikan masalah nilai masa depan.. Bukti: Nilai masa depan dari tabungannya; bunga 9% per tahun; setiap bulan
- Intended difficulty `classify/Medium`: Soal ini bersifat rutin bagi siswa kelas 12 yang mempelajari matematika keuangan. Langkah-langkahnya jelas: konversi periode bunga, identifikasi rumus, dan substitusi nilai.. Bukti: bunga 9% per tahun; setiap bulan; setelah empat tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep anuitas, konversi suku bunga tahunan ke bulanan, dan penggunaan rumus nilai masa depan anuitas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi anuitas adalah standar kurikulum kelas 12. Soal ini memerlukan ketelitian dalam konversi satuan waktu dan bunga, namun prosedurnya sangat standar. |

Run 2 — solusi: FV = PMT * [(1 + i)^n - 1] / i. PMT = 2.000.000, i = 0,09/12 = 0,0075, n = 4 * 12 = 48. FV = 2.000.000 * [(1,0075)^48 - 1] / 0,0075 = 2.000.000 * [1,431405 - 1] / 0,0075 = 2.000.000 * 57,5206 = 115.041.200. Dibulatkan menjadi Rp115.000.000,00.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model anuitas biasa (ordinary annuity), mengonversi suku bunga tahunan ke bulanan, menentukan jumlah periode, dan menerapkan rumus nilai masa depan (future value). Ini adalah penerapan prosedur rutin dalam konteks keuangan.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; bunga 9% per tahun; Nilai masa depan dari tabungannya setelah empat tahun
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep anuitas dan penggunaan rumus matematika keuangan yang relevan untuk menghitung nilai masa depan.. Bukti: Nilai masa depan dari tabungannya; bunga 9% per tahun; setiap bulan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi satuan waktu dan bunga (tahunan ke bulanan) serta pemilihan rumus yang tepat, namun prosedurnya bersifat rutin dan familiar bagi siswa kelas 12.. Bukti: bunga 9% per tahun; setiap bulan; setelah empat tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep barisan dan deret geometri, pemahaman dasar bunga majemuk, dan rumus anuitas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan perhitungan anuitas sederhana dengan konversi periode yang rutin. |

Run 3 — solusi: Menggunakan rumus nilai masa depan anuitas biasa (Ordinary Annuity): FV = PMT * [(1 + i)^n - 1] / i. Diketahui PMT = 2.000.000, i = 0,09/12 = 0,0075, dan n = 4 * 12 = 48 bulan. FV = 2.000.000 * [(1 + 0,0075)^48 - 1] / 0,0075 = 2.000.000 * [1,431405 - 1] / 0,0075 = 2.000.000 * 57,52067 = 115.041.340. Dibulatkan menjadi Rp115.000.000,00.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah anuitas biasa (ordinary annuity), mengonversi suku bunga tahunan ke bulanan, menentukan jumlah periode, dan menerapkan rumus nilai masa depan yang relevan.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; bunga 9% per tahun; Nilai masa depan dari tabungannya setelah empat tahun
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus anuitas untuk menghitung nilai masa depan tabungan.. Bukti: Nilai masa depan dari tabungannya setelah empat tahun adalah
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi satuan waktu dan bunga (tahunan ke bulanan) serta menerapkan rumus anuitas yang melibatkan perhitungan eksponensial, yang merupakan langkah rutin namun memerlukan ketelitian dalam pemilihan prosedur.. Bukti: bunga 9% per tahun; setiap bulan; setelah empat tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan rumus anuitas biasa. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi anuitas adalah standar kurikulum kelas 12. Soal ini memerlukan konversi unit yang rutin namun krusial, sesuai dengan tingkat kesulitan menengah untuk jenjang SMA. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.

Nilai masa depan dari tabungannya setelah empat tahun adalah ....
Pilihan: A. Rp115.000.000,00
B. Rp113.000.000,00
C. Rp114.000.000,00
D. Rp112.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `e10756708fd7c9e1c3bf5ae2`

Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.<br><br>Hitung total bunga keseluruhan.

| Opsi | Isi |
|---|---|
| A | Rp960.000,00 |
| B | Rp320.016,00 |
| C | Rp280.014,00 |
| D | Rp480.000,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Pinjaman Rp12.000.000 diangsur 6 bulan (pokok tetap), maka angsuran pokok per bulan = 12.000.000/6 = 2.000.000. Bunga per bulan = 8%/12 = 2/3% per bulan. Bunga bulan ke-n = (Sisa Pokok) x (2/3%). Sisa pokok bulan 1-6: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Total bunga = (12+10+8+6+4+2)jt x (2/3%) = 42.000.000 x 0,006666... = 280.000. Catatan: Perhitungan sumber (280.014) menggunakan pembulatan bunga per bulan yang sedikit berbeda, namun secara konsep metode pokok tetap adalah yang benar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `73e893a5585206a3ec7b80d3b1c89b17a898b704fc9f1e618e63548f89bd97d2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2382 |
| 2 | success | valid / verified | applying | procedural | Medium | 2371 |
| 3 | success | valid / verified | applying | procedural | Medium | 2299 |

Run 1 — solusi: Pinjaman Rp12.000.000 diangsur 6 bulan (pokok tetap), maka angsuran pokok per bulan = 12.000.000/6 = 2.000.000. Bunga per bulan = 8%/12 = 2/3% per bulan. Bunga bulan ke-n = (Sisa Pokok) x (2/3%). Sisa pokok bulan 1-6: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Total bunga = (12+10+8+6+4+2)jt x (2/3%) = 42.000.000 x 0,006666... = 280.000. Catatan: Perhitungan sumber (280.014) menggunakan pembulatan bunga per bulan yang sedikit berbeda, namun secara konsep metode pokok tetap adalah yang benar.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep 'pokok tetap' (angsuran pokok konstan) dan bagaimana bunga dihitung berdasarkan sisa pokok yang menurun setiap bulan, bukan bunga tunggal sederhana.. Bukti: diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang perhitungan bunga pada sistem angsuran pokok tetap, yang memerlukan konversi suku bunga tahunan ke bulanan dan penerapan algoritma bunga pada sisa pokok.. Bukti: pokok tetap; bunga 8% per tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung menggunakan rumus bunga tunggal sederhana (yang akan menghasilkan jawaban salah). Siswa harus memahami mekanisme angsuran pokok tetap (sisa pokok menurun) dan melakukan perhitungan bunga secara bertahap atau menggunakan deret aritmatika untuk total bunga.. Bukti: diangsur selama 6 bulan (pokok tetap); bunga 8% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga, aritmatika dasar, dan pemahaman sistem angsuran pokok tetap. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan antara bunga tunggal sederhana dengan bunga yang dihitung berdasarkan sisa pokok (pokok tetap), yang merupakan materi standar keuangan matematika. |

Run 2 — solusi: Pokok pinjaman Rp12.000.000 dibagi 6 bulan = Rp2.000.000/bulan. Sisa pokok tiap bulan: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Bunga per bulan = (8%/12) * sisa pokok. Total bunga = (8%/12) * (12+10+8+6+4+2)jt = (0,006667) * 42jt = Rp280.014.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep angsuran pokok tetap di mana sisa utang menurun setiap bulan, lalu mengintegrasikan perhitungan bunga bulanan yang proporsional terhadap sisa utang tersebut. Ini melibatkan pemilihan prosedur yang tepat (bunga majemuk/berkala pada sisa pokok) daripada sekadar bunga tunggal sederhana.. Bukti: diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun; Hitung total bunga keseluruhan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana bunga dihitung dalam skema angsuran pokok tetap, yang memerlukan konversi suku bunga tahunan ke bulanan dan penerapan algoritma penjumlahan bunga pada sisa pokok yang menurun.. Bukti: diangsur selama 6 bulan (pokok tetap); bunga 8% per tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung menggunakan rumus bunga tunggal sederhana. Mereka harus memahami mekanisme 'pokok tetap' (penurunan sisa utang) dan melakukan perhitungan berulang atau deret aritmatika untuk bunga bulanan, yang merupakan langkah rutin namun memerlukan ketelitian dalam pemilihan prosedur.. Bukti: diangsur selama 6 bulan (pokok tetap); bunga 8% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga, konversi satuan waktu (tahun ke bulan), dan pemahaman skema angsuran pokok tetap. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan skema bunga pada pinjaman. Soal ini menuntut pemahaman bahwa 'pokok tetap' mengubah basis perhitungan bunga setiap periode, yang merupakan materi standar keuangan di kelas 12. |

Run 3 — solusi: Pokok pinjaman Rp12.000.000 diangsur 6 bulan, maka angsuran pokok per bulan = 12.000.000/6 = 2.000.000. Sisa pokok tiap bulan: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Bunga per bulan = 8%/12 = 0,6667% per bulan. Total bunga = (12jt+10jt+8jt+6jt+4jt+2jt) * 0,006667 = 42.000.000 * 0,006667 = 280.014.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep bunga majemuk/bunga atas sisa pokok (declining balance) dan mengintegrasikan prosedur perhitungan bunga bulanan yang menurun, bukan sekadar bunga tunggal sederhana.. Bukti: diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang bagaimana bunga dihitung berdasarkan sisa pokok pinjaman yang menurun secara periodik.. Bukti: diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan pemilihan prosedur yang tepat (bunga atas sisa pokok) dan melakukan beberapa langkah perhitungan rutin yang saling terkait, bukan sekadar satu operasi bunga tunggal.. Bukti: diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bunga per tahun ke per bulan, konsep angsuran pokok tetap. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan perhitungan bunga flat vs bunga atas sisa pokok. Soal ini menguji ketelitian dalam menerapkan bunga pada sisa pokok yang menurun. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.

Hitung total bunga keseluruhan.
Pilihan: A. Rp960.000,00
B. Rp320.016,00
C. Rp280.014,00
D. Rp480.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `7f246f52d9fc331e3e277809`

Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.<br><br>Hitung angsuran pokok per bulan.

| Opsi | Isi |
|---|---|
| A | Rp2.960.000,00 |
| B | Rp1.500.000,00 |
| C | Rp1.000.000,00 |
| D | Rp2.000.000,00 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Dalam sistem angsuran pokok tetap, angsuran pokok per bulan dihitung dengan membagi total pinjaman dengan jumlah periode angsuran. Angsuran pokok = Rp12.000.000,00 / 6 bulan = Rp2.000.000,00 per bulan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3cbd18b2ead28e6128c2ef4843881d43ac1ba900be07333a8fe8be351de1ff46`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2126 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2141 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2109 |

Run 1 — solusi: Angsuran pokok per bulan dihitung dengan membagi total pinjaman dengan jangka waktu angsuran. Angsuran pokok = Rp12.000.000,00 / 6 bulan = Rp2.000.000,00 per bulan.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi konsep angsuran pokok tetap dan melakukan pembagian sederhana antara total pinjaman dengan durasi waktu.. Bukti: meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap); Hitung angsuran pokok per bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang bagaimana angsuran pokok tetap dihitung dalam konteks pinjaman.. Bukti: angsuran selama 6 bulan (pokok tetap)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan satu operasi pembagian sederhana. Tidak ada kendala kompleks atau integrasi konsep yang menantang.. Bukti: Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep angsuran pokok tetap. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun untuk kelas 12, soal ini terlalu sederhana karena hanya menuntut pembagian dasar tanpa melibatkan perhitungan bunga majemuk atau anuitas yang sebenarnya. |

Run 2 — solusi: Angsuran pokok per bulan untuk sistem pokok tetap dihitung dengan membagi total pinjaman dengan jumlah periode angsuran. Angsuran pokok = Rp12.000.000,00 / 6 = Rp2.000.000,00.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung dari definisi angsuran pokok tetap, yaitu membagi total pinjaman dengan jumlah periode. Siswa hanya perlu mengenali prosedur dasar tanpa perlu mengintegrasikan bunga ke dalam perhitungan angsuran pokok.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap); Hitung angsuran pokok per bulan.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep 'pokok tetap' dalam konteks pinjaman untuk mengetahui bahwa bunga tidak memengaruhi besaran angsuran pokok per bulan.. Bukti: angsur selama 6 bulan (pokok tetap)
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah perhitungan sederhana. Informasi bunga 8% per tahun merupakan distraktor yang tidak relevan untuk menghitung angsuran pokok.. Bukti: Rp12.000.000,00; diangsur selama 6 bulan (pokok tetap)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar pembagian dan konsep pinjaman pokok tetap. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi kelas 12, soal ini hanya menguji pemahaman dasar aritmatika dan definisi istilah keuangan yang sangat mendasar, sehingga tergolong mudah. |

Run 3 — solusi: Angsuran pokok per bulan untuk sistem pokok tetap dihitung dengan membagi total pinjaman dengan jumlah periode angsuran. Angsuran pokok = Rp12.000.000,00 / 6 bulan = Rp2.000.000,00.
- Domain kognitif `classify/knowing`: Soal meminta perhitungan langsung berdasarkan definisi angsuran pokok tetap. Siswa hanya perlu mengidentifikasi nilai pokok dan periode, lalu melakukan pembagian sederhana.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap); Hitung angsuran pokok per bulan.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dasar angsuran pokok tetap dalam konteks pinjaman untuk menentukan prosedur perhitungan yang tepat.. Bukti: pokok tetap
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah perhitungan (pembagian). Informasi bunga 8% per tahun adalah distraktor karena pertanyaan hanya menanyakan angsuran pokok.. Bukti: Rp12.000.000,00; diangsur selama 6 bulan (pokok tetap)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep angsuran pokok tetap. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 12, hanya memerlukan pembagian sederhana tanpa melibatkan perhitungan bunga majemuk atau anuitas yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3636`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya meminta penerapan langsung dari definisi angsuran pokok tetap. Siswa hanya perlu mengidentifikasi nilai pokok dan periode, lalu melakukan pembagian sederhana. Tidak ada strategi nonrutin atau integrasi konsep yang diperlukan.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep 'pokok tetap' untuk membedakannya dari anuitas, sehingga mereka tahu bahwa bunga tidak memengaruhi besaran angsuran pokok per bulan.
- Intended difficulty `Easy`: Soal ini bersifat prosedural langsung dengan satu langkah perhitungan. Informasi bunga 8% per tahun adalah distraktor yang tidak relevan untuk menghitung angsuran pokok.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep angsuran pokok tetap. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi kelas 12, soal ini hanya menguji pemahaman dasar aritmatika dan definisi istilah keuangan yang sangat mendasar, sehingga tergolong mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.

Hitung angsuran pokok per bulan.
Pilihan: A. Rp2.960.000,00
B. Rp1.500.000,00
C. Rp1.000.000,00
D. Rp2.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `a4ded83d90999b1517dcec47`

Bu Tania adalah pemilik usaha toko elektronik yang telah berkembang pesat di kotanya. Usahanya menghasilkan omzet rata-rata sebesar Rp120.000.000,00 per bulan. Ia memiliki 10 orang karyawan dengan gaji rata-rata Rp4.000.000,00, serta pengeluaran rutin lainnya sebesar Rp25.000.000,00 per bulan.<br><br>Kini Bu Tania ingin memperluas usahanya ke kota lain dan membutuhkan tambahan modal. Ia mengajukan kredit ke Bank Sentosa, dan mendapat brosur simulasi angsuran kredit seperti tabel berikut.<br><br>\| Pinjaman \| 12 bulan \| 24 bulan \| 36 bulan \| 48 bulan \| 60 bulan \|<br>\|---\|---\|---\|---\|---\|---\|<br>\| Rp10.000.000,00 \| Rp874.515,00 \| Rp456.847,00 \| - \| - \| - \|<br>\| Rp25.000.000,00 \| Rp2.186.287,00 \| Rp1.142.119,00 \| - \| - \| - \|<br>\| Rp30.000.000,00 \| Rp2.623.545,00 \| Rp1.370.542,00 \| - \| - \| - \|<br>\| Rp40.000.000,00 \| Rp3.498.059,00 \| Rp1.827.390,00 \| - \| - \| - \|<br>\| Rp50.000.000,00 \| Rp4.372.574,00 \| Rp2.284.237,00 \| - \| - \| - \|<br>\| Rp60.000.000,00 \| Rp5.247.089,00 \| Rp2.741.085,00 \| Rp1.907.984,00 \| - \| - \|<br>\| Rp70.000.000,00 \| Rp6.121.603,00 \| Rp3.197.932,00 \| Rp2.225.981,00 \| - \| - \|<br>\| Rp80.000.000,00 \| Rp6.996.118,00 \| Rp3.654.780,00 \| Rp2.543.978,00 \| - \| - \|<br>\| Rp100.000.000,00 \| Rp8.745.148,00 \| Rp4.568.474,00 \| Rp3.179.973,00 \| Rp2.488.504,00 \| - \|<br>\| Rp130.000.000,00 \| Rp11.368.693,00 \| Rp5.939.017,00 \| Rp4.133.965,00 \| Rp3.235.055,00 \| Rp2.698.586,00 \|<br>\| Rp150.000.000,00 \| Rp13.117.722,00 \| Rp6.852.711,00 \| Rp4.769.959,00 \| Rp3.732.756,00 \| Rp3.113.753,00 \|<br><br>Bu Tania memutuskan bahwa angsuran maksimal yang dapat ia bayarkan per bulan tidak lebih dari 20% dari total pendapatan bersih per bulan jika mengangsur selama 12 bulan. Namun, jika mengambil angsuran lebih dari 12 bulan (24, 36, 48, atau 60 bulan) tidak lebih dari 10% dari total pendapatan bersih per bulan.<br><br>Andaikan Bu Tania mengambil pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan, Setelah membuka cabang baru, Bu Tania merekrut 5 orang karyawan tambahan dengan besaran gaji yang sama seperti karyawan sebelumnya (Rp4.000.000,00 per orang). Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?

| Opsi | Isi |
|---|---|
| A | Rp138.745.148,00 |
| B | Rp75.000.000,00 |
| C | Rp83.745.148,00 |
| D | Rp55.000.000,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Pendapatan bersih awal = 120jt - (10*4jt + 25jt) = 55jt. Target bersih = 2*55jt = 110jt. Tambahan bersih yang dibutuhkan = 110jt - 55jt = 55jt. Beban baru = gaji 5 karyawan (20jt) + cicilan (8.745.148) = 28.745.148. Omzet tambahan = 55jt + 28.745.148 = 83.745.148.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `593868eeb3d0959ce33ec4763845040a0dd759c0f1b6f70b61c6d435a78790b2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 4815 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3552 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3544 |

Run 1 — solusi: Pendapatan bersih awal = 120jt - (10*4jt + 25jt) = 55jt. Target bersih = 2*55jt = 110jt. Tambahan bersih yang dibutuhkan = 110jt - 55jt = 55jt. Beban baru = gaji 5 karyawan (20jt) + cicilan (8.745.148) = 28.745.148. Omzet tambahan = 55jt + 28.745.148 = 83.745.148.
- Domain kognitif `classify/applying`: Siswa harus mengintegrasikan informasi keuangan (pendapatan, beban, cicilan) untuk menyusun strategi perhitungan target omzet. Ini melibatkan pemahaman hubungan antar variabel keuangan dalam situasi bisnis.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat; omzet minimal yang harus diperoleh dari cabang baru
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang bagaimana pendapatan bersih dihitung (Pendapatan - Beban) dan bagaimana beban baru (cicilan dan gaji) mempengaruhi target pendapatan.. Bukti: omzet rata-rata; pengeluaran rutin; angsuran kredit
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan prosedur yang tepat dan integrasi beberapa variabel (gaji, cicilan, target laba). Ini adalah tugas rutin yang memerlukan penggabungan langkah-langkah.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat; omzet minimal yang harus diperoleh dari cabang baru

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar dan konsep dasar laba bersih (pendapatan dikurangi beban). |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengelola data keuangan sederhana. Soal ini menuntut ketelitian dalam mengidentifikasi beban baru dan target laba. |

Run 2 — solusi: Pendapatan bersih awal = 120jt - (10*4jt) - 25jt = 55jt. Target bersih baru = 2 * 55jt = 110jt. Tambahan bersih yang diperlukan = 110jt - 55jt = 55jt. Beban baru = Gaji 5 karyawan (5 * 4jt = 20jt) + Cicilan pinjaman 100jt tenor 12 bln (8.745.148). Omzet minimal cabang baru = Tambahan bersih + Beban baru = 55jt + 20jt + 8.745.148 = 83.745.148.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi keuangan (pendapatan, pengeluaran, cicilan) untuk menyusun strategi perhitungan omzet yang memenuhi target pendapatan bersih baru. Ini melibatkan pemahaman hubungan antar variabel keuangan.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya; omzet minimal yang harus diperoleh dari cabang baru
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pendapatan bersih (omzet dikurangi biaya operasional dan cicilan) dan bagaimana variabel-variabel tersebut saling berhubungan dalam konteks bisnis.. Bukti: omzet rata-rata sebesar Rp120.000.000,00; pendapatan bersih total Bu Tania menjadi dua kali lipat
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan prosedur yang tepat untuk menghitung pendapatan bersih dan mengintegrasikan beberapa komponen biaya (gaji, cicilan) untuk mencapai target. Ini adalah tugas rutin yang memerlukan ketelitian dalam mengelola beberapa variabel.. Bukti: 10 orang karyawan dengan gaji rata-rata Rp4.000.000,00; rekrut 5 orang karyawan tambahan; pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aritmatika keuangan (pendapatan bersih = omzet - biaya) dan kemampuan membaca tabel angsuran. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengelola perhitungan keuangan bisnis sederhana yang melibatkan beberapa variabel biaya dan cicilan, yang merupakan aplikasi langsung dari materi keuangan. |

Run 3 — solusi: Pendapatan bersih awal = 120jt - (10*4jt) - 25jt = 55jt. Target bersih baru = 2 * 55jt = 110jt. Tambahan bersih yang dibutuhkan = 110jt - 55jt = 55jt. Beban baru = Gaji 5 karyawan (5*4jt = 20jt) + Cicilan pinjaman (8.745.148). Omzet minimal = Tambahan bersih + Beban baru = 55jt + 20jt + 8.745.148 = 83.745.148.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi keuangan (pendapatan, pengeluaran, gaji, cicilan) untuk menyusun model matematika sederhana guna mencapai target pendapatan bersih. Ini melibatkan pemilihan prosedur aritmatika yang tepat dalam konteks bisnis.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya; rekrut 5 orang karyawan tambahan; pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pendapatan bersih (omzet dikurangi beban) dan bagaimana variabel baru (cicilan, gaji tambahan) mempengaruhi struktur tersebut.. Bukti: omzet rata-rata sebesar Rp120.000.000,00 per bulan; pendapatan bersih total Bu Tania menjadi dua kali lipat
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin yang saling terkait (menghitung pendapatan awal, menentukan target, mengidentifikasi beban baru dari tabel, dan menjumlahkan). Tidak ada strategi nonrutin yang kompleks.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya; rekrut 5 orang karyawan tambahan; pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep pendapatan bersih, dan kemampuan membaca tabel angsuran. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 12 karena menggabungkan literasi finansial dengan aritmatika dasar dalam konteks bisnis yang relevan, menuntut ketelitian dalam mengidentifikasi semua komponen beban. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman dengan Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Bu Tania adalah pemilik usaha toko elektronik yang telah berkembang pesat di kotanya. Usahanya menghasilkan omzet rata-rata sebesar Rp120.000.000,00 per bulan. Ia memiliki 10 orang karyawan dengan gaji rata-rata Rp4.000.000,00, serta pengeluaran rutin lainnya sebesar Rp25.000.000,00 per bulan.

Kini Bu Tania ingin memperluas usahanya ke kota lain dan membutuhkan tambahan modal. Ia mengajukan kredit ke Bank Sentosa, dan mendapat brosur simulasi angsuran kredit seperti tabel berikut.

| Pinjaman | 12 bulan | 24 bulan | 36 bulan | 48 bulan | 60 bulan |
|---|---|---|---|---|---|
| Rp10.000.000,00 | Rp874.515,00 | Rp456.847,00 | - | - | - |
| Rp25.000.000,00 | Rp2.186.287,00 | Rp1.142.119,00 | - | - | - |
| Rp30.000.000,00 | Rp2.623.545,00 | Rp1.370.542,00 | - | - | - |
| Rp40.000.000,00 | Rp3.498.059,00 | Rp1.827.390,00 | - | - | - |
| Rp50.000.000,00 | Rp4.372.574,00 | Rp2.284.237,00 | - | - | - |
| Rp60.000.000,00 | Rp5.247.089,00 | Rp2.741.085,00 | Rp1.907.984,00 | - | - |
| Rp70.000.000,00 | Rp6.121.603,00 | Rp3.197.932,00 | Rp2.225.981,00 | - | - |
| Rp80.000.000,00 | Rp6.996.118,00 | Rp3.654.780,00 | Rp2.543.978,00 | - | - |
| Rp100.000.000,00 | Rp8.745.148,00 | Rp4.568.474,00 | Rp3.179.973,00 | Rp2.488.504,00 | - |
| Rp130.000.000,00 | Rp11.368.693,00 | Rp5.939.017,00 | Rp4.133.965,00 | Rp3.235.055,00 | Rp2.698.586,00 |
| Rp150.000.000,00 | Rp13.117.722,00 | Rp6.852.711,00 | Rp4.769.959,00 | Rp3.732.756,00 | Rp3.113.753,00 |

Bu Tania memutuskan bahwa angsuran maksimal yang dapat ia bayarkan per bulan tidak lebih dari 20% dari total pendapatan bersih per bulan jika mengangsur selama 12 bulan. Namun, jika mengambil angsuran lebih dari 12 bulan (24, 36, 48, atau 60 bulan) tidak lebih dari 10% dari total pendapatan bersih per bulan.

Andaikan Bu Tania mengambil pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan, Setelah membuka cabang baru, Bu Tania merekrut 5 orang karyawan tambahan dengan besaran gaji yang sama seperti karyawan sebelumnya (Rp4.000.000,00 per orang). Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?
Pilihan: A. Rp138.745.148,00
B. Rp75.000.000,00
C. Rp83.745.148,00
D. Rp55.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `b5d6c979c2045301a3560ae7`

Seseorang meminjam uang sebesar Rp10.000.000,00 selama setengah tahun dengan suku bunga 8% per bulan. Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3 (dalam satuan Rp100.000,00).<br><br>\| Bulan \| Jumlah Pinjaman Awal Bulan \| Bunga Pinjaman \| Angsuran Pinjaman \| Jumlah Pinjaman Akhir Bulan \|<br>\|---\|---\|---\|---\|---\|<br>\| 1 \| 100 \| 8 \| 14 \| 86 \|<br>\| 2 \| 86 \| 6,88 \| 15,12 \| 70,88 \|<br>\| 3 \| 70,88 \| 5,7604 \| 16,32 \| 54,5504 \|<br><br>Besar anuitas pada sistem angsuran tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Rp2.300.000,00 |
| B | Rp2.000.000,00 |
| C | Rp2.100.000,00 |
| D | Rp2.200.000,00 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel bulan ke-2: Bunga = 6,88; Angsuran = 15,12. Anuitas = 6,88 + 15,12 = 22 (dalam satuan Rp100.000,00). Jadi, 22 x Rp100.000,00 = Rp2.200.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3d6aaa7a15f4fb0412da82d1b6f6351c7cb38d9ebe1ce987b64204fb6ce88ba4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2316 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2394 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2354 |

Run 1 — solusi: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel bulan ke-2: Bunga = 6,88; Angsuran = 15,12. Anuitas = 6,88 + 15,12 = 22 (dalam satuan Rp100.000,00). Jadi, 22 x Rp100.000,00 = Rp2.200.000,00.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep anuitas sebagai penjumlahan bunga dan angsuran pokok, kemudian memilih data yang tepat dari tabel untuk melakukan perhitungan.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang komponen anuitas (bunga + angsuran) dan kemampuan membaca data dari tabel keuangan.. Bukti: Berikut dalam tabel rencana angsuran pinjaman tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya meminta pemahaman definisi anuitas dan ekstraksi data dari tabel yang sudah disediakan. Beban perhitungan sangat rendah.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang tabel angsuran dan definisi anuitas (bunga + angsuran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi anuitas adalah standar kelas 12. Soal ini hanya menuntut pemahaman definisi dasar tanpa kompleksitas perhitungan atau strategi non-rutin. |

Run 2 — solusi: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel bulan ke-1: Bunga (8) + Angsuran (14) = 22. Berdasarkan tabel bulan ke-2: Bunga (6,88) + Angsuran (15,12) = 22. Karena 22 dalam satuan Rp100.000,00, maka anuitas = Rp2.200.000,00.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep anuitas sebagai jumlah bunga dan angsuran pokok, lalu memilih data yang relevan dari tabel untuk melakukan perhitungan sederhana.. Bukti: Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3; Besar anuitas pada sistem angsuran tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang komponen anuitas (bunga + angsuran) dan kemampuan membaca data dari tabel.. Bukti: Bunga Pinjaman \| Angsuran Pinjaman; Besar anuitas pada sistem angsuran tersebut adalah
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu memahami definisi anuitas dan melakukan penjumlahan sederhana dari data yang sudah tersedia secara eksplisit di tabel.. Bukti: Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3; Besar anuitas pada sistem angsuran tersebut adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen angsuran (bunga dan angsuran pokok) dan kemampuan membaca tabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi anuitas adalah standar kelas 12. Soal ini bersifat prosedural langsung dengan data yang sudah disediakan dalam tabel, sehingga beban kognitifnya rendah. |

Run 3 — solusi: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel bulan ke-1: 8 + 14 = 22. Bulan ke-2: 6,88 + 15,12 = 22. Bulan ke-3: 5,7604 + 16,32 = 22,0804. Terdapat sedikit pembulatan pada tabel, namun nilai anuitas yang konsisten adalah 22 (satuan Rp100.000,00) atau Rp2.200.000,00.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar anuitas sebagai penjumlahan bunga dan angsuran pokok, kemudian memilih data yang relevan dari tabel untuk melakukan perhitungan sederhana.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang komponen penyusun anuitas dalam tabel amortisasi pinjaman.. Bukti: Bunga Pinjaman \| Angsuran Pinjaman
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu memahami definisi anuitas dan melakukan operasi penjumlahan sederhana dari data yang sudah tersedia secara eksplisit dalam tabel.. Bukti: Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen pinjaman (bunga dan angsuran pokok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi anuitas adalah standar kelas 12. Soal ini hanya meminta ekstraksi dan operasi aritmatika dasar dari tabel yang diberikan, sehingga beban kognitifnya rendah. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman dengan Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang meminjam uang sebesar Rp10.000.000,00 selama setengah tahun dengan suku bunga 8% per bulan. Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3 (dalam satuan Rp100.000,00).

| Bulan | Jumlah Pinjaman Awal Bulan | Bunga Pinjaman | Angsuran Pinjaman | Jumlah Pinjaman Akhir Bulan |
|---|---|---|---|---|
| 1 | 100 | 8 | 14 | 86 |
| 2 | 86 | 6,88 | 15,12 | 70,88 |
| 3 | 70,88 | 5,7604 | 16,32 | 54,5504 |

Besar anuitas pada sistem angsuran tersebut adalah ....
Pilihan: A. Rp2.300.000,00
B. Rp2.000.000,00
C. Rp2.100.000,00
D. Rp2.200.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `c51d2c28576452736fad772a`

Untuk menggalakkan program koperasi berdaya guna, beberapa koperasi akan memberikan pinjaman masing-masing sebesar Rp50.000.000,00 kepada pengurus desa untuk modal pembangunan. Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun, sedangkan Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun.<br><br>Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi. Manakah yang lebih menguntungkan?

| Opsi | Isi |
|---|---|
| A | Koperasi A (nilai akhir Rp59.702.615,00) lebih menguntungkan dibanding Koperasi B (Rp56.308.121,00) |
| B | Koperasi A dan Koperasi B menghasilkan nilai akhir yang sama besar |
| C | Koperasi B (nilai akhir Rp56.308.121,00) lebih menguntungkan dibanding Koperasi A (Rp59.702.615,00) |
| D | Koperasi B lebih menguntungkan karena periode pinjamannya lebih singkat |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Nilai akhir (A) = P(1+r)^n. Koperasi A: 50.000.000 * (1,03)^6 = 59.702.615. Koperasi B: 50.000.000 * (1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121 untuk B, yang merupakan hasil 50.000.000 * (1,02)^6. Terdapat ketidakkonsistenan pada data soal vs kunci untuk Koperasi B, namun perbandingan A > B tetap valid).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3ce33a169b038f14803329eec2af538e1aee974164211068c2dadc0cd2bbac1a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2394 |
| 2 | success | valid / verified | applying | procedural | Easy | 2444 |
| 3 | success | valid / verified | applying | procedural | Easy | 2452 |

Run 1 — solusi: Nilai akhir (A) = P(1+r)^n. Koperasi A: 50.000.000 * (1,03)^6 = 59.702.615. Koperasi B: 50.000.000 * (1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121 untuk B, yang merupakan hasil 50.000.000 * (1,02)^6. Terdapat ketidakkonsistenan pada data soal vs kunci untuk Koperasi B, namun perbandingan A > B tetap valid).
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus bunga majemuk yang tepat, melakukan substitusi nilai, dan membandingkan dua hasil perhitungan. Ini adalah penerapan prosedur rutin dalam konteks keuangan.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun; Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perhitungan bunga majemuk dan perbandingan nilai akhir.. Bukti: suku bunga sebesar 3% per tahun selama 6 tahun; suku bunga sebesar 2% per tahun selama 4 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus bunga majemuk standar dua kali dan membandingkan hasilnya. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus bunga majemuk M = M0(1+i)^n |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah standar kurikulum kelas 12. Prosedur perhitungan langsung dan familiar bagi siswa. |

Run 2 — solusi: Nilai akhir (M_n) dihitung dengan rumus bunga majemuk M_n = M_0(1+i)^n. Koperasi A: 50.000.000 * (1,03)^6 = 59.702.615. Koperasi B: 50.000.000 * (1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121, namun perhitungan manual 50jt * 1,02^4 = 54.121.608. Terdapat ketidaksesuaian nilai pada kunci, namun kesimpulan A > B tetap valid).
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur perhitungan bunga majemuk yang tepat untuk dua skenario berbeda dan membandingkan hasilnya. Ini melibatkan penerapan rumus pada situasi rutin.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun; Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami prinsip bunga majemuk dan menerapkannya dalam perhitungan nilai akhir.. Bukti: suku bunga sebesar 3% per tahun selama 6 tahun; suku bunga sebesar 2% per tahun selama 4 tahun
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang melibatkan substitusi nilai ke dalam rumus bunga majemuk standar dan perbandingan dua nilai. Tidak ada kendala nonrutin atau integrasi representasi yang kompleks.. Bukti: pinjaman masing-masing sebesar Rp50.000.000,00; Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan penggunaan kalkulator/operasi hitung eksponen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah standar kelas 12. Soal ini bersifat langsung (direct application) tanpa modifikasi variabel yang rumit. |

Run 3 — solusi: Nilai akhir (M) dihitung dengan rumus bunga majemuk M = P(1+i)^n. Koperasi A: M_A = 50.000.000 * (1,03)^6 = 59.702.615. Koperasi B: M_B = 50.000.000 * (1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121 yang merupakan hasil 50.000.000 * (1,02)^4 = 54.121.608, namun 50.000.000 * (1,02)^4 = 54.121.608. Terdapat kesalahan hitung pada kunci sumber untuk B, namun perbandingan A > B tetap valid).
- Domain kognitif `classify/applying`: Siswa perlu memilih dan menerapkan rumus bunga majemuk untuk dua skenario berbeda, kemudian membandingkan hasilnya. Ini adalah penerapan prosedur rutin dalam situasi keuangan.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun; Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan bunga majemuk dan perbandingan nilai akhir, yang merupakan pengetahuan prosedural.. Bukti: suku bunga sebesar 3% per tahun selama 6 tahun; nilai akhir yang akan didapat
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya meminta penerapan rumus bunga majemuk standar (M = P(1+i)^n) pada dua kasus yang diberikan secara eksplisit. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan penggunaan kalkulator/operasi perpangkatan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan sudah familiar dengan perhitungan bunga majemuk sebagai bagian dari materi keuangan matematika. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Parameter Investasi dan Pinjaman
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk menggalakkan program koperasi berdaya guna, beberapa koperasi akan memberikan pinjaman masing-masing sebesar Rp50.000.000,00 kepada pengurus desa untuk modal pembangunan. Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun, sedangkan Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun.

Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi. Manakah yang lebih menguntungkan?
Pilihan: A. Koperasi A (nilai akhir Rp59.702.615,00) lebih menguntungkan dibanding Koperasi B (Rp56.308.121,00)
B. Koperasi A dan Koperasi B menghasilkan nilai akhir yang sama besar
C. Koperasi B (nilai akhir Rp56.308.121,00) lebih menguntungkan dibanding Koperasi A (Rp59.702.615,00)
D. Koperasi B lebih menguntungkan karena periode pinjamannya lebih singkat
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `7672dd47336c772dbd3a318a`

Suatu aplikasi pinjaman online memberikan pinjaman sebesar Rp10.000.000,00 dengan suku bunga 2% per tahun. Periode pinjaman selama 24 bulan. Berapakah nilai akhir pengembalian pinjaman tersebut?

| Opsi | Isi |
|---|---|
| A | Rp10.200.000,00 |
| B | Rp10.404.000,00 |
| C | Rp10.612.000,00 |
| D | Rp10.000.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pinjaman (P) = 10.000.000, suku bunga (i) = 2% per tahun, periode (n) = 24 bulan = 2 tahun. Menggunakan rumus bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = 10.404.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9e6bf772849b21b4169b204d4b5c16895f134abd19a1c84ad23774958b892015`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2188 |
| 2 | success | valid / verified | applying | procedural | Easy | 2192 |
| 3 | success | valid / verified | applying | procedural | Easy | 2227 |

Run 1 — solusi: Pinjaman (P) = 10.000.000, suku bunga (i) = 2% per tahun, periode (n) = 24 bulan = 2 tahun. Menggunakan rumus bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = 10.404.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model bunga majemuk yang sesuai untuk pinjaman jangka panjang dan mengonversi satuan waktu (bulan ke tahun) sebelum menerapkan rumus.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan; nilai akhir pengembalian pinjaman
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman prosedural tentang penggunaan rumus bunga majemuk dan konversi satuan waktu yang relevan.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan satu prosedur rutin (bunga majemuk) dengan konversi waktu sederhana. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bunga majemuk dan konversi satuan waktu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 seharusnya sudah familiar dengan perhitungan bunga majemuk sederhana dan konversi periode waktu. |

Run 2 — solusi: Pinjaman awal (P) = 10.000.000, suku bunga (i) = 2% per tahun, periode (n) = 24 bulan = 2 tahun. Menggunakan rumus bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = 10.404.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model bunga majemuk yang sesuai untuk pinjaman jangka panjang, mengonversi satuan waktu (bulan ke tahun), dan menerapkan rumus bunga majemuk secara langsung.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan; nilai akhir pengembalian pinjaman
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus bunga majemuk dan pemahaman konseptual mengenai konversi periode waktu dalam konteks keuangan.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan penerapan rumus standar bunga majemuk dengan konversi satuan waktu yang sederhana (24 bulan = 2 tahun).. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bunga majemuk dan konversi satuan waktu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan sudah familiar dengan perhitungan bunga majemuk sederhana sebagai bagian dari materi keuangan matematika. |

Run 3 — solusi: Pinjaman (P) = 10.000.000, suku bunga (i) = 2% per tahun, periode (n) = 24 bulan = 2 tahun. Menggunakan rumus bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = 10.404.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa periode 24 bulan harus dikonversi ke tahun (2 tahun) dan menerapkan rumus bunga majemuk yang sesuai untuk menghitung nilai akhir.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan; nilai akhir pengembalian pinjaman
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus bunga majemuk dan konversi satuan waktu yang tepat dalam konteks keuangan.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan konversi satuan waktu sederhana dan penerapan langsung rumus bunga majemuk yang sudah familiar bagi siswa kelas 12.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bunga majemuk dan konversi satuan waktu (bulan ke tahun). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah standar kurikulum kelas 12. Soal ini tidak memiliki jebakan kompleks atau syarat tambahan yang rumit. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Parameter Investasi dan Pinjaman
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu aplikasi pinjaman online memberikan pinjaman sebesar Rp10.000.000,00 dengan suku bunga 2% per tahun. Periode pinjaman selama 24 bulan. Berapakah nilai akhir pengembalian pinjaman tersebut?
Pilihan: A. Rp10.200.000,00
B. Rp10.404.000,00
C. Rp10.612.000,00
D. Rp10.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `052c617a1f0c63d479f466ab`

Sepuluh orang siswa memiliki tinggi yang berbeda. Guru olahraga menginginkan mereka berbaris menyamping dengan syarat tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya. Berapa banyaknya cara membuat barisan sesuai ketentuan itu?

| Opsi | Isi |
|---|---|
| A | 1.024 cara |
| B | 256 cara |
| C | 512 cara |
| D | 3.628.800 cara |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `512`.
Solusi minimum hasil AI: Urutkan siswa dari terpendek ke tertinggi (h1 < h2 < ... < h10). Siswa terpendek (h1) diletakkan di posisi mana saja. Untuk siswa berikutnya (h2), ia harus diletakkan di ujung kiri atau kanan barisan yang sudah terbentuk agar tidak diapit dua orang yang lebih tinggi. Pola ini berlanjut untuk h3 sampai h9. Setiap siswa (h2 sampai h9) memiliki 2 pilihan posisi (ujung kiri atau kanan). Siswa h10 diletakkan di posisi terakhir yang tersisa (1 pilihan). Total cara = 2^(10-1) = 2^9 = 512.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3433614bbbf4829e1217520c030de57946b999fba75f74efb100f3278fbb9813`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2249 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 2182 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2226 |

Run 1 — solusi: Misalkan siswa diurutkan dari terpendek ke tertinggi (h1 < h2 < ... < h10). Siswa terpendek (h1) harus berada di ujung (kiri atau kanan). Setelah h1 ditempatkan, h2 juga harus berada di ujung barisan yang tersisa (kiri atau kanan), dan seterusnya hingga h9. Siswa tertinggi (h10) akan mengisi posisi terakhir yang tersisa. Untuk setiap siswa dari h1 hingga h9, terdapat 2 pilihan posisi (ujung kiri atau ujung kanan dari barisan yang terbentuk). Maka total cara adalah 2^(10-1) = 2^9 = 512.
- Domain kognitif `classify/reasoning`: Siswa perlu menyadari pola konstruksi barisan (menempatkan siswa dari yang terpendek ke tertinggi) untuk memenuhi syarat "tidak diapit dua siswa lebih tinggi". Ini memerlukan pemahaman konseptual tentang bagaimana syarat tersebut membatasi posisi setiap elemen secara berurutan, bukan sekadar menerapkan rumus permutasi standar.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang syarat posisi dalam barisan. Siswa harus memahami hubungan antara urutan tinggi badan dan batasan posisi agar syarat "tidak diapit" terpenuhi, yang mengarah pada pola eksponensial.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman pola konstruktif (induktif) untuk memecahkan masalah kombinatorika yang tidak bisa diselesaikan dengan rumus permutasi/kombinasi standar secara langsung. Siswa harus melakukan penalaran logis untuk menemukan pola 2^(n-1).. Bukti: Sepuluh orang siswa memiliki tinggi yang berbeda; tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan pemahaman urutan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 12, masalah ini menuntut penalaran di luar rumus permutasi rutin, namun masih dalam cakupan logika dasar yang diharapkan pada materi pencacahan. |

Run 2 — solusi: Urutkan siswa dari terpendek ke tertinggi. Siswa terpendek (1) harus di ujung. Siswa ke-2 harus di ujung barisan yang terbentuk (kiri atau kanan). Siswa ke-3 juga harus di ujung barisan yang terbentuk, dan seterusnya hingga siswa ke-9. Setiap siswa dari ke-2 sampai ke-9 memiliki 2 pilihan posisi (ujung kiri atau ujung kanan dari barisan yang sudah terbentuk). Siswa ke-10 (tertinggi) hanya memiliki 1 posisi tersisa. Total cara = 2^(10-1) = 2^9 = 512.
- Domain kognitif `classify/reasoning`: Siswa perlu menyadari bahwa syarat 'tidak diapit oleh dua siswa yang lebih tinggi' memaksa barisan terbentuk dengan menempatkan siswa dari yang terpendek ke tertinggi di ujung-ujung barisan yang tersisa. Ini memerlukan penalaran logis tentang konstruksi barisan, bukan sekadar menerapkan rumus permutasi standar.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip konstruksi barisan (konsep) dan menerapkannya untuk menentukan pola penempatan siswa (prosedural), namun inti masalahnya terletak pada pemahaman hubungan antar elemen dalam barisan.. Bukti: Berapa banyaknya cara membuat barisan sesuai ketentuan itu?
- Intended difficulty `classify/Hard`: Soal ini memerlukan pemahaman mendalam tentang syarat yang diberikan. Siswa tidak bisa langsung menggunakan rumus permutasi 10!, melainkan harus membangun logika penempatan satu per satu. Ini adalah masalah non-rutin bagi kebanyakan siswa kelas 12.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan pemahaman urutan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun perhitungannya sederhana (2^9), logika di balik syarat 'tidak diapit' sangat menantang dan jarang ditemui dalam latihan rutin sekolah, sehingga dikategorikan Hard. |

Run 3 — solusi: Urutkan siswa dari terpendek ke tertinggi (h1 < h2 < ... < h10). Siswa terpendek (h1) diletakkan di posisi mana saja. Untuk siswa berikutnya (h2), ia harus diletakkan di ujung kiri atau kanan barisan yang sudah terbentuk agar tidak diapit dua orang yang lebih tinggi. Pola ini berlanjut untuk h3 sampai h9. Setiap siswa (h2 sampai h9) memiliki 2 pilihan posisi (ujung kiri atau kanan). Siswa h10 diletakkan di posisi terakhir yang tersisa (1 pilihan). Total cara = 2 * 2 * ... * 2 (sebanyak 9 kali) = 2^9 = 512.
- Domain kognitif `classify/reasoning`: Soal ini memerlukan pemahaman konsep konstruksi barisan dengan kendala (syarat posisi). Siswa harus menyadari bahwa untuk memenuhi syarat, setiap siswa baru harus ditempatkan di ujung barisan yang sudah terbentuk. Ini adalah strategi nonrutin yang memerlukan penalaran logis tentang urutan penempatan, bukan sekadar permutasi standar.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip konstruktif dalam pencacahan (aturan pengisian tempat) dan bagaimana kendala 'tidak diapit' membatasi pilihan posisi, yang merupakan pemahaman konseptual tentang struktur barisan.. Bukti: Berapa banyaknya cara membuat barisan sesuai ketentuan itu?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemilihan prosedur yang tepat (konstruksi dari siswa terpendek ke tertinggi) dan pemahaman pola 2^(n-1). Meskipun langkahnya rutin setelah strategi ditemukan, menemukan strategi tersebut merupakan tantangan bagi siswa kelas 12.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan aturan pengisian tempat. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menuntut kemampuan berpikir logis di luar rumus permutasi standar yang sering diajarkan, sesuai dengan kompetensi kelas 12 dalam memecahkan masalah pencacahan dengan kendala. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Hard": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4138`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini memerlukan penalaran logis untuk menyadari bahwa syarat 'tidak diapit' memaksa setiap siswa baru (saat diurutkan dari terpendek) untuk selalu menempati posisi ujung dari barisan yang sudah terbentuk. Ini adalah strategi nonrutin yang mengintegrasikan pemahaman urutan dan aturan pengisian tempat.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami hubungan konseptual antara urutan tinggi badan dan batasan posisi agar syarat 'tidak diapit' terpenuhi, yang mengarah pada pola konstruktif eksponensial.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan pemilihan strategi konstruktif yang tepat. Meskipun perhitungannya sederhana (2^9), menemukan strategi bahwa setiap siswa harus diletakkan di ujung barisan yang terbentuk merupakan tantangan nonrutin bagi siswa kelas 12.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan pemahaman urutan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini menuntut penalaran di luar rumus permutasi rutin, namun masih dalam cakupan logika dasar yang diharapkan pada materi pencacahan kelas 12. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Aturan Pengisian Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Sepuluh orang siswa memiliki tinggi yang berbeda. Guru olahraga menginginkan mereka berbaris menyamping dengan syarat tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya. Berapa banyaknya cara membuat barisan sesuai ketentuan itu?
Pilihan: A. 1.024 cara
B. 256 cara
C. 512 cara
D. 3.628.800 cara
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `439575e9c1a8bdff1255c8d5`

Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda yang digunakan sehari-hari sebagai pakaian bekerja. Jika Arkan membuat setelan yang berbeda saat mengenakannya dalam bekerja, tentukan banyak setelan berbeda yang dibuat.

| Opsi | Isi |
|---|---|
| A | 15 setelan |
| B | 12 setelan |
| C | 20 setelan |
| D | 60 setelan |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menggunakan aturan perkalian untuk kejadian saling bebas: 5 kemeja * 4 celana * 3 sepatu = 60 setelan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9939210f7829425d5e20ea4a73bc413aa20ae4ba9c6503f1cbda86bb5ecabcb9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1998 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2017 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2045 |

Run 1 — solusi: Menggunakan aturan perkalian untuk kejadian saling bebas: 5 kemeja * 4 celana * 3 sepatu = 60 setelan.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali situasi sebagai penerapan aturan perkalian dasar untuk kejadian yang saling bebas, yang merupakan prosedur langsung.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian dalam kombinatorika dasar.. Bukti: tentukan banyak setelan berbeda yang dibuat
- Intended difficulty `classify/Easy`: Soal ini adalah aplikasi langsung dari aturan perkalian dasar tanpa kendala tambahan, sehingga termasuk kategori mudah bagi siswa kelas 12.. Bukti: 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan perkalian dasar (kaidah pencacahan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi dasar kombinatorika yang sudah dipelajari sejak kelas 10/11, sehingga bagi siswa kelas 12 ini adalah prosedur yang sangat familiar. |

Run 2 — solusi: Menggunakan aturan perkalian untuk kejadian saling bebas: 5 kemeja x 4 celana x 3 pasang sepatu = 60 setelan.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali situasi sebagai penerapan aturan perkalian dasar untuk kejadian yang saling bebas, yang merupakan prosedur standar dalam materi pencacahan.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan aturan perkalian untuk menentukan banyaknya kombinasi dari beberapa kategori objek.. Bukti: aturan perkalian untuk tiga kejadian saling bebas
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan angka kecil, dan hanya memerlukan satu langkah penerapan aturan perkalian tanpa kendala tambahan.. Bukti: 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu; tentukan banyak setelan berbeda

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan perkalian (counting principle). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan pengenalan dasar aturan pencacahan yang sudah dipelajari di awal bab, sehingga bagi siswa kelas 12 ini adalah prosedur yang sangat rutin. |

Run 3 — solusi: Menggunakan aturan perkalian untuk kejadian yang saling bebas: 5 kemeja × 4 celana × 3 sepatu = 60 setelan.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung aturan perkalian dasar untuk menentukan banyaknya kombinasi dari tiga kategori objek yang berbeda. Siswa hanya perlu mengenali situasi sebagai aturan perkalian dan melakukan operasi hitung sederhana.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip dasar aturan perkalian (fundamental counting principle) sebagai prosedur untuk menghitung kombinasi objek.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari aturan perkalian dasar yang sangat familiar bagi siswa kelas 12. Tidak ada kendala tambahan atau skenario kompleks.. Bukti: 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu; tentukan banyak setelan berbeda

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan perkalian (aturan pengisian tempat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar aturan pencacahan yang biasanya diperkenalkan di awal materi kombinatorika, sehingga tingkat kesulitannya rendah untuk siswa kelas 12. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Aturan Pengisian Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda yang digunakan sehari-hari sebagai pakaian bekerja. Jika Arkan membuat setelan yang berbeda saat mengenakannya dalam bekerja, tentukan banyak setelan berbeda yang dibuat.
Pilihan: A. 15 setelan
B. 12 setelan
C. 20 setelan
D. 60 setelan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `cd21884f9b39f41443039e69`

Swalayan AAmart mengeluarkan kupon hadiah dengan kode berbentuk bilangan yang disusun dari angka 1, 2, 2, 6, dan 8. Jika kupon-kupon tersebut disusun berdasarkan kodenya mulai dari yang terkecil sampai dengan yang terbesar, maka kupon dengan kode lebih besar daripada 62000 sebanyak ....

| Opsi | Isi |
|---|---|
| A | 19 kupon |
| B | 21 kupon |
| C | 24 kupon |
| D | 20 kupon |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `21`.
Solusi minimum hasil AI: Total bilangan > 62000: 1) Digit pertama 8: sisa {1,2,2,6} disusun 4!/2! = 12. 2) Digit pertama 6, kedua 8: sisa {1,2,2} disusun 3!/2! = 3. 3) Digit pertama 6, kedua 2: sisa {1,2,8} disusun 3! = 6. Total = 12 + 3 + 6 = 21.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3f1a45436492602dfdb52068668d5ff482e84031f222090dfc767e108861ce86`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3076 |
| 2 | success | valid / verified | applying | procedural | Medium | 3620 |
| 3 | success | valid / verified | applying | procedural | Medium | 3589 |

Run 1 — solusi: Total bilangan > 62000: 1) Digit pertama 8: sisa {1,2,2,6} disusun 4!/2! = 12. 2) Digit pertama 6, kedua 8: sisa {1,2,2} disusun 3!/2! = 3. 3) Digit pertama 6, kedua 2: sisa {1,2,8} disusun 3! = 6. Total = 12 + 3 + 6 = 21.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus permutasi dengan unsur yang sama dan melakukan partisi kasus berdasarkan digit pertama dan kedua untuk memenuhi syarat lebih besar dari 62000.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kode lebih besar daripada 62000
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang permutasi unsur sama dan prinsip aturan penjumlahan untuk kasus-kasus yang terpisah.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kode lebih besar daripada 62000
- Intended difficulty `classify/Medium`: Soal memerlukan pemecahan masalah menjadi beberapa kasus (digit pertama 8, digit pertama 6-8, digit pertama 6-2) dan ketelitian dalam menangani angka yang berulang (angka 2).. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kode lebih besar daripada 62000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Permutasi unsur sama, aturan perkalian, dan prinsip dasar pencacahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan standar kompetensi kelas 12 mengenai permutasi dengan unsur yang sama dan penyelesaian masalah kontekstual. |

Run 2 — solusi: Total permutations > 62000: (1) Starts with 8: 4!/2! = 12. (2) Starts with 68: 3!/2! = 3. (3) Starts with 62: 3! = 6. Total = 12 + 3 + 6 = 21.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur permutasi dengan pengulangan dan menerapkannya pada kasus-kasus yang berbeda (awalan 8, 68, dan 62) untuk mendapatkan total susunan.. Bukti: disusun berdasarkan kodenya mulai dari yang terkecil sampai dengan yang terbesar; kupon dengan kode lebih besar daripada 62000
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman algoritma permutasi dengan objek berulang (angka 2) dalam konteks penyusunan bilangan.. Bukti: angka 1, 2, 2, 6, dan 8
- Intended difficulty `classify/Medium`: Soal dikategorikan Medium karena memerlukan pemecahan masalah menjadi beberapa kasus (awalan 8, 68, 62) dan penanganan objek berulang, yang merupakan langkah rutin namun memerlukan ketelitian.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; lebih besar daripada 62000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Permutasi dengan objek berulang |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena melibatkan analisis kasus pada permutasi yang merupakan materi standar. |

Run 3 — solusi: Total permutations of {1, 2, 2, 6, 8} starting with 8: 4!/2! = 12. Starting with 68: 3!/2! = 3. Starting with 62: 3! = 6. Total = 12 + 3 + 6 = 21.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus permutasi dengan pengulangan dan melakukan analisis kasus berdasarkan batasan nilai (lebih besar dari 62000).. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kupon dengan kode lebih besar daripada 62000
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman prosedur permutasi dengan objek yang sama (angka 2 berulang) dan urutan.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemecahan masalah menjadi beberapa kasus (berdasarkan digit pertama dan kedua) serta penerapan rumus permutasi dengan pengulangan yang tepat.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; lebih besar daripada 62000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Permutasi dengan pengulangan |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan analisis kasus sistematis pada masalah kombinatorika. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Permutasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Swalayan AAmart mengeluarkan kupon hadiah dengan kode berbentuk bilangan yang disusun dari angka 1, 2, 2, 6, dan 8. Jika kupon-kupon tersebut disusun berdasarkan kodenya mulai dari yang terkecil sampai dengan yang terbesar, maka kupon dengan kode lebih besar daripada 62000 sebanyak ....
Pilihan: A. 19 kupon
B. 21 kupon
C. 24 kupon
D. 20 kupon
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `4c33984e92f3e85b5396ba7f`

Ada tujuh orang siswa akan membentuk barisan. Tentukan banyaknya susunan barisan yang mungkin terjadi.

| Opsi | Isi |
|---|---|
| A | 720 susunan |
| B | 40.320 susunan |
| C | 5.040 susunan |
| D | 49 susunan |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Banyaknya susunan 7 orang siswa dalam barisan adalah permutasi dari 7 objek berbeda, yaitu 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5.040.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5c5c94d53714656a5746b5a2c34e8eedfa34028dfece49c67764054d94802bc8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1952 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1957 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1998 |

Run 1 — solusi: Banyaknya susunan 7 orang dalam barisan adalah permutasi dari 7 objek berbeda, yaitu 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5.040.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus permutasi n objek (n!) untuk menyusun 7 orang dalam barisan. Siswa hanya perlu mengenali situasi sebagai permutasi linear sederhana dan menghitung faktorialnya.. Bukti: tujuh orang siswa akan membentuk barisan; banyaknya susunan barisan yang mungkin terjadi
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep permutasi linear sebagai cara menyusun n objek berbeda dalam urutan tertentu.. Bukti: tujuh orang siswa akan membentuk barisan
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur standar yang sangat familiar bagi siswa kelas 12. Tidak ada kendala tambahan, syarat khusus, atau kompleksitas dalam penyusunan.. Bukti: tujuh orang siswa akan membentuk barisan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar faktorial dan permutasi linear. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar permutasi yang merupakan materi awal kelas 12. Tidak memerlukan integrasi strategi atau analisis kendala. |

Run 2 — solusi: Banyaknya susunan barisan dari 7 orang siswa yang berbeda adalah permutasi dari 7 objek, yaitu 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5.040.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus permutasi n objek (n!) untuk n=7. Siswa hanya perlu mengenali situasi sebagai permutasi linear dan melakukan perhitungan faktorial dasar.. Bukti: tujuh orang siswa akan membentuk barisan; banyaknya susunan barisan yang mungkin terjadi
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang cara menghitung permutasi linear dari sekumpulan objek yang berbeda.. Bukti: tujuh orang siswa akan membentuk barisan
- Intended difficulty `classify/Easy`: Soal ini sangat standar dan langsung, hanya memerlukan satu langkah perhitungan faktorial tanpa kendala tambahan atau variasi.. Bukti: tujuh orang siswa akan membentuk barisan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar faktorial dan permutasi linear. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar permutasi yang biasanya diperkenalkan di awal materi kombinatorika kelas 12, tidak memerlukan analisis kompleks. |

Run 3 — solusi: Banyaknya susunan barisan dari 7 orang siswa adalah permutasi 7 objek berbeda, yaitu 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5.040.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus permutasi n objek (n!) untuk menyusun barisan. Siswa hanya perlu mengenali bahwa ini adalah masalah permutasi dasar dan melakukan perhitungan faktorial.. Bukti: Ada tujuh orang siswa akan membentuk barisan. Tentukan banyaknya susunan barisan yang mungkin terjadi.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep permutasi (konseptual) dan menerapkan algoritma faktorial (prosedural) untuk menyelesaikan masalah.. Bukti: Tentukan banyaknya susunan barisan yang mungkin terjadi.
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang sangat familiar bagi siswa kelas 12. Tidak ada kendala tambahan, syarat khusus, atau kompleksitas yang memerlukan strategi nonrutin.. Bukti: Ada tujuh orang siswa akan membentuk barisan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep faktorial dan permutasi dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan dasar permutasi yang rutin diberikan di kelas 12, tidak memerlukan integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3317`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung rumus permutasi n objek (n!) untuk menyusun 7 orang dalam barisan. Siswa hanya perlu mengenali situasi sebagai permutasi linear sederhana dan melakukan perhitungan faktorial.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami konsep permutasi linear sebagai cara menyusun n objek berbeda dalam urutan tertentu dan menerapkan algoritma faktorial.
- Intended difficulty `Easy`: Soal ini adalah prosedur standar yang sangat familiar bagi siswa kelas 12. Tidak ada kendala tambahan, syarat khusus, atau kompleksitas dalam penyusunan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar faktorial dan permutasi linear. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar permutasi yang merupakan materi awal kelas 12. Tidak memerlukan integrasi strategi atau analisis kendala. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Permutasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada tujuh orang siswa akan membentuk barisan. Tentukan banyaknya susunan barisan yang mungkin terjadi.
Pilihan: A. 720 susunan
B. 40.320 susunan
C. 5.040 susunan
D. 49 susunan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `e9e9f310f9de364e628b69a2`

Terdapat sepuluh orang pergi ketempat wisata dengan mengendarai 3 mobil berkapasitas 4 orang dan tiga orang diantarannya adalah pemilik mobil. Jika setiap mobil dikemudikan oleh pemiliknya dan di setiap mobil minimal ada satu penumpang selain pengemudi, banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang di ketiga mobil tersebut ada ....

| Opsi | Isi |
|---|---|
| A | 1.190 cara |
| B | 1.050 cara |
| C | 840 cara |
| D | 700 cara |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `1.050`.
Solusi minimum hasil AI: Total penumpang 7 orang. Kapasitas sisa tiap mobil 3 kursi. Syarat: minimal 1 penumpang per mobil. Partisi 7 ke dalam 3 kelompok (maks 3, min 1): (3,3,1) dan (3,2,2). Untuk (3,3,1): ada 3 permutasi posisi mobil (3,3,1; 3,1,3; 1,3,3). Banyak cara = 3 * (7!/(3!3!1!)) = 3 * 140 = 420. Untuk (3,2,2): ada 3 permutasi posisi mobil (3,2,2; 2,3,2; 2,2,3). Banyak cara = 3 * (7!/(3!2!2!)) = 3 * 210 = 630. Total = 420 + 630 = 1.050.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b40022c47ed0a22d9964a163ca4411d303d8d5d7f2e3578cffaf0b4e9f861ac`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2384 |
| 2 | success | valid / verified | applying | procedural | Medium | 2442 |
| 3 | success | valid / verified | applying | procedural | Medium | 2362 |

Run 1 — solusi: Total penumpang 7 orang. Kapasitas sisa tiap mobil 3 kursi. Syarat: minimal 1 penumpang per mobil. Partisi 7 ke dalam 3 kelompok (maks 3, min 1): (3,3,1) dan (3,2,2). Untuk (3,3,1): ada 3 permutasi posisi mobil (3,3,1; 3,1,3; 1,3,3). Banyak cara = 3 * (7!/(3!3!1!)) = 3 * 140 = 420. Untuk (3,2,2): ada 3 permutasi posisi mobil (3,2,2; 2,3,2; 2,2,3). Banyak cara = 3 * (7!/(3!2!2!)) = 3 * 210 = 630. Total = 420 + 630 = 1.050.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kendala (kapasitas dan syarat minimal) dan menyusun strategi partisi bilangan (7 penumpang ke 3 mobil) sebelum menerapkan rumus kombinasi/permutasi. Ini melibatkan pemilihan prosedur yang tepat untuk kasus partisi dengan batasan.. Bukti: setiap mobil dikemudikan oleh pemiliknya; di setiap mobil minimal ada satu penumpang selain pengemudi; banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prinsip kombinatorika (partisi dan permutasi kelompok) untuk menyelesaikan masalah alokasi dengan batasan tertentu.. Bukti: banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang kendala (kapasitas dan syarat minimal) dan kemampuan memecah masalah menjadi kasus-kasus partisi yang mungkin (3,3,1 dan 3,2,2). Ini adalah tugas rutin yang memerlukan pemilihan prosedur yang cermat.. Bukti: 3 mobil berkapasitas 4 orang; tiga orang diantarannya adalah pemilik mobil; di setiap mobil minimal ada satu penumpang selain pengemudi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar kombinatorika, permutasi, dan partisi bilangan. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Masalah ini menuntut ketelitian dalam membagi 7 penumpang ke dalam 3 wadah dengan batasan kapasitas dan syarat minimal, yang merupakan standar kompetensi kelas 12. |

Run 2 — solusi: Tersisa 7 penumpang untuk 3 mobil. Kapasitas tambahan tiap mobil adalah 3 kursi. Syarat: minimal 1 penumpang per mobil. Kemungkinan distribusi (penumpang per mobil): (3,3,1) atau (3,2,2). Untuk (3,3,1): ada 3 permutasi posisi mobil, yaitu (3,3,1), (3,1,3), (1,3,3). Banyak cara: 3 * (7! / (3!3!1!)) = 3 * 420 = 1260. Tunggu, koreksi: (3,3,1) berarti 3 mobil, 2 mobil isi 3, 1 mobil isi 1. Banyak cara = 3C1 * 7C3 * 4C3 * 1C1 = 3 * 35 * 4 = 420. Untuk (3,2,2): 3 mobil, 1 mobil isi 3, 2 mobil isi 2. Banyak cara = 3C1 * 7C3 * 4C2 * 2C2 = 3 * 35 * 6 = 630. Total = 420 + 630 = 1050.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi kendala (kapasitas dan syarat minimal penumpang), membagi kasus distribusi penumpang (partisi bilangan 7 ke dalam 3 slot dengan batas 1-3), dan menerapkan rumus kombinasi untuk setiap kasus. Ini memerlukan pemilihan prosedur yang tepat dan integrasi beberapa langkah rutin.. Bukti: setiap mobil dikemudikan oleh pemiliknya; di setiap mobil minimal ada satu penumpang selain pengemudi; banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip dasar kombinasi dan bagaimana menerapkannya dalam konteks pembagian kelompok dengan batasan (constraint) tertentu.. Bukti: banyaknya kemungkinan komposisi berbeda; minimal ada satu penumpang selain pengemudi
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah rutin yang saling terkait (partisi bilangan dan kombinasi) serta pemilihan prosedur yang tepat untuk menangani kendala kapasitas dan syarat minimal penumpang.. Bukti: 3 mobil berkapasitas 4 orang; tiga orang diantarannya adalah pemilik mobil; minimal ada satu penumpang selain pengemudi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar kombinasi, permutasi, dan partisi bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu memecahkan masalah kombinatorika dengan kendala sederhana melalui pembagian kasus. |

Run 3 — solusi: Tersisa 7 penumpang untuk 3 mobil (kapasitas tambahan 3 per mobil). Syarat: minimal 1 penumpang per mobil. Kemungkinan partisi 7 ke dalam 3 mobil (maks 3): (3,3,1) dan (3,2,2). Untuk (3,3,1): ada 3 permutasi mobil, cara susun = 3 * (7!/(3!3!1!)) = 3 * 140 = 420. Untuk (3,2,2): ada 3 permutasi mobil, cara susun = 3 * (7!/(3!2!2!)) = 3 * 210 = 630. Total = 420 + 630 = 1.050.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kendala (kapasitas dan syarat minimal), menentukan partisi bilangan yang mungkin (3,3,1 dan 3,2,2), dan menerapkan rumus kombinasi/permutasi grup untuk menghitung susunan yang valid. Ini melibatkan pemilihan prosedur yang tepat untuk situasi rutin yang dimodifikasi.. Bukti: setiap mobil dikemudikan oleh pemiliknya; di setiap mobil minimal ada satu penumpang selain pengemudi; banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami prinsip dasar pencacahan dan bagaimana menerapkan kombinasi pada pembagian kelompok dengan batasan kapasitas dan syarat minimum.. Bukti: banyaknya kemungkinan komposisi berbeda; minimal ada satu penumpang
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung menggunakan rumus kombinasi standar. Mereka harus melakukan analisis kasus (partisi bilangan) untuk memenuhi kendala kapasitas dan syarat minimal, lalu menghitung permutasi kelompok yang mungkin. Ini memerlukan integrasi beberapa langkah rutin.. Bukti: 3 mobil berkapasitas 4 orang; tiga orang diantarannya adalah pemilik mobil; minimal ada satu penumpang selain pengemudi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan, kombinasi, dan partisi bilangan. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menangani masalah kombinatorika dengan kendala tambahan seperti ini sebagai bagian dari materi peluang/pencacahan. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Terdapat sepuluh orang pergi ketempat wisata dengan mengendarai 3 mobil berkapasitas 4 orang dan tiga orang diantarannya adalah pemilik mobil. Jika setiap mobil dikemudikan oleh pemiliknya dan di setiap mobil minimal ada satu penumpang selain pengemudi, banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang di ketiga mobil tersebut ada ....
Pilihan: A. 1.190 cara
B. 1.050 cara
C. 840 cara
D. 700 cara
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `42af439f72392b9d1118073a`

Pada suatu Olimpiade Matematika, peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia. Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan.

| Opsi | Isi |
|---|---|
| A | 6.720 |
| B | 40 |
| C | 70 |
| D | 56 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Masalah ini adalah pemilihan 5 soal dari 8 soal yang tersedia tanpa memperhatikan urutan, sehingga menggunakan rumus kombinasi C(n, r) = n! / (r!(n-r)!). Maka, C(8, 5) = 8! / (5! * 3!) = (8 * 7 * 6) / (3 * 2 * 1) = 56.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `da951f000cb547a35db970de8cf39108e21d2a45fd87525a89ca6d69fdb2977e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2021 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2033 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2046 |

Run 1 — solusi: Masalah ini adalah pemilihan 5 soal dari 8 soal yang tersedia tanpa memperhatikan urutan, sehingga menggunakan rumus kombinasi C(n, r) = n! / (r!(n-r)!). C(8, 5) = 8! / (5! * 3!) = (8 * 7 * 6) / (3 * 2 * 1) = 56.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa urutan pengerjaan soal tidak diperhatikan (kombinasi) dan menerapkan rumus kombinasi yang sesuai untuk situasi rutin pemilihan objek.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia; Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus kombinasi untuk menyelesaikan masalah pemilihan objek.. Bukti: 5 soal dari 8 soal yang tersedia; banyaknya jenis pilihan soal
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam materi kombinatorika kelas 12. Siswa hanya perlu mengenali situasi sebagai kombinasi dan menghitung nilainya.. Bukti: 5 soal dari 8 soal yang tersedia; banyaknya jenis pilihan soal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar kombinasi dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar yang sering ditemui dalam kurikulum kelas 12 untuk materi kombinasi. |

Run 2 — solusi: Masalah ini adalah pemilihan 5 soal dari 8 soal yang tersedia tanpa memperhatikan urutan, sehingga menggunakan rumus kombinasi C(n, r) = n! / (r!(n-r)!). Maka, C(8, 5) = 8! / (5! * 3!) = (8 * 7 * 6) / (3 * 2 * 1) = 56.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini adalah masalah kombinasi (memilih subset tanpa urutan) dan menerapkan rumus kombinasi yang sesuai. Ini adalah penerapan prosedur standar dalam konteks rutin.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia; Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip kombinasi sebagai cara untuk menghitung pemilihan objek tanpa memperhatikan urutan, yang merupakan konsep dasar dalam materi pencacahan.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menggunakan prosedur yang sangat familiar bagi siswa kelas 12 dalam materi kombinatorika. Tidak ada kendala tambahan atau skenario kompleks.. Bukti: mengerjakan 5 soal dari 8 soal yang tersedia

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar faktorial dan rumus kombinasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar yang sering ditemui dalam kurikulum kelas 12 untuk menguji pemahaman dasar tentang kombinasi. |

Run 3 — solusi: Masalah ini adalah pemilihan 5 soal dari 8 soal yang tersedia tanpa memperhatikan urutan, sehingga menggunakan rumus kombinasi C(n, r) = n! / (r!(n-r)!). Maka, C(8, 5) = 8! / (5! * 3!) = (8 * 7 * 6) / (3 * 2 * 1) = 56.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini adalah masalah kombinasi (pemilihan tanpa urutan) dan menerapkan rumus kombinasi yang sesuai. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia; Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip kombinasi sebagai cara untuk menghitung pemilihan objek tanpa memperhatikan urutan, yang merupakan konsep dasar dalam materi pencacahan.. Bukti: 5 soal dari 8 soal yang tersedia; banyaknya jenis pilihan soal
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 12. Tidak ada kendala tambahan atau skenario kompleks yang memerlukan strategi non-rutin.. Bukti: mengerjakan 5 soal dari 8 soal yang tersedia

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang faktorial dan rumus kombinasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan standar untuk materi kombinasi di kelas 12, dengan prosedur yang sangat familiar dan beban kognitif yang rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3534`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi bahwa urutan pengerjaan soal tidak diperhatikan (kombinasi) dan menerapkan rumus kombinasi yang sesuai untuk situasi rutin pemilihan objek.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus kombinasi untuk menyelesaikan masalah pemilihan objek.
- Intended difficulty `Easy`: Soal ini merupakan prosedur standar dalam materi kombinatorika kelas 12. Siswa hanya perlu mengenali situasi sebagai kombinasi dan menghitung nilainya.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar kombinasi dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar yang sering ditemui dalam kurikulum kelas 12 untuk materi kombinasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada suatu Olimpiade Matematika, peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia. Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan.
Pilihan: A. 6.720
B. 40
C. 70
D. 56
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `d4a29da533d9881db57e7c74`

Tim futsal SMA Abhipraya dijadwalkan mengikuti 3 pertandingan awal dalam turnamen dengan sistem poin. Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6 berdasarkan data latihan dan uji coba. Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.

| Opsi | Isi |
|---|---|
| A | 0,216 |
| B | 0,6 |
| C | 0,432 |
| D | 0,36 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menggunakan rumus distribusi binomial: P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a7aa62686b746829e95c631c4d52cd7ecdecb6cfd0121acd4f8960c735569f8f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2789 |
| 2 | success | valid / verified | applying | procedural | Easy | 2875 |
| 3 | success | valid / verified | applying | procedural | Easy | 2069 |

Run 1 — solusi: Menggunakan rumus peluang binomial: P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Siswa perlu memilih dan menerapkan rumus peluang binomial untuk situasi rutin yang diberikan.. Bukti: Peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara peluang kejadian tunggal dan distribusi binomial untuk menyelesaikan masalah.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; tepat 2 dari 3 pertandingan
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus binomial yang sudah familiar bagi siswa kelas 12. Langkah-langkahnya rutin dan tidak memerlukan strategi nonrutin.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; tepat 2 dari 3 pertandingan pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian saling bebas dan rumus distribusi binomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang binomial adalah standar kurikulum kelas 12. Soal ini menguji pemahaman dasar tanpa kompleksitas tambahan. |

Run 2 — solusi: P(X=2) = C(3,2) * (0.6)^2 * (0.4)^1 = 3 * 0.36 * 0.4 = 0.432
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai distribusi binomial dan menerapkan rumus peluang binomial untuk menghitung hasil. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman tentang prinsip peluang kejadian majemuk (binomial) dan penggunaan rumus kombinasi dalam konteks peluang.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung rumus binomial. Siswa kelas 12 diharapkan sudah familiar dengan rumus ini. Tidak ada kendala non-rutin atau integrasi representasi yang kompleks.. Bukti: 3 pertandingan awal; tepat 2 dari 3 pertandingan pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian saling bebas dan rumus kombinasi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi standar rumus binomial yang diajarkan di kelas 12. Prosedurnya bersifat rutin bagi siswa yang mempelajari materi peluang. |

Run 3 — solusi: Menggunakan distribusi binomial dengan n=3, k=2, p=0,6, dan q=0,4. Peluang = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai percobaan binomial, memilih rumus yang tepat, dan menerapkan prosedur perhitungan rutin untuk mendapatkan hasil.. Bukti: Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma distribusi binomial (prosedural) dan konsep peluang kejadian majemuk (konseptual).. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; tepat 2 dari 3 pertandingan
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus binomial yang sudah umum diajarkan di kelas 12. Tidak ada kendala non-rutin atau integrasi representasi yang kompleks.. Bukti: 3 pertandingan awal; Peluang menang... 0,6; tepat 2 dari 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian saling bebas dan rumus dasar distribusi binomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang binomial adalah standar kurikulum kelas 12. Soal ini bersifat prosedural langsung tanpa modifikasi konteks yang menyulitkan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3515`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi situasi sebagai percobaan binomial, memilih rumus yang tepat, dan menerapkan prosedur perhitungan rutin untuk mendapatkan hasil.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma distribusi binomial (prosedural) dan konsep peluang kejadian majemuk (konseptual).
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung dari rumus binomial yang sudah umum diajarkan di kelas 12. Tidak ada kendala non-rutin atau integrasi representasi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian saling bebas dan rumus dasar distribusi binomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang binomial adalah standar kurikulum kelas 12. Soal ini bersifat prosedural langsung tanpa modifikasi konteks yang menyulitkan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Penerapan Permutasi dan Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Tim futsal SMA Abhipraya dijadwalkan mengikuti 3 pertandingan awal dalam turnamen dengan sistem poin. Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6 berdasarkan data latihan dan uji coba. Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.
Pilihan: A. 0,216
B. 0,6
C. 0,432
D. 0,36
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `eded99210de8f3efd55fe9df`

Guru IPA menjelaskan bahwa kenyamanan belajar dipengaruhi oleh kualitas udara, yang tergantung pada suhu (t) dan kelembaban (h). Dalam penelitian kecil di kelas, ditemukan bahwa pengaruh suhu dua kali lebih besar dibanding kelembaban, dan model total pengaruhnya adalah $(2t+h)^5$. Jika suatu waktu suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian. Berapakah total kontribusi kombinasi tersebut?

| Opsi | Isi |
|---|---|
| A | 80 |
| B | 32 |
| C | 10 |
| D | 40 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `80`.
Solusi minimum hasil AI: Ekspansi binomial (2t+h)^5 menggunakan rumus umum C(n,k) * a^(n-k) * b^k. Untuk suku t^3 h^2, kita gunakan n=5, k=2 (untuk h^2) atau k=3 (untuk t^3). Koefisiennya adalah C(5,3) * (2)^3 * (1)^2 = 10 * 8 * 1 = 80.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ae1c4ef6469bdbb8ec21397f066984d3f5b11f065396e968217b92765998036a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3176 |
| 2 | success | valid / verified | applying | procedural | Medium | 2989 |
| 3 | success | valid / verified | applying | procedural | Easy | 3000 |

Run 1 — solusi: Ekspansi binomial (2t+h)^5 adalah sum_{k=0}^5 C(5,k)(2t)^{5-k}(h)^k. Untuk suku t^3h^2, pilih k=2. Koefisiennya adalah C(5,2) * 2^3 = 10 * 8 = 80.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema binomial untuk menentukan koefisien suku tertentu dalam ekspansi polinomial.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus teorema binomial.. Bukti: model total pengaruhnya adalah (2t+h)^5
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan prosedur yang tepat (teorema binomial) dan melakukan perhitungan rutin untuk menemukan koefisien suku tertentu.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial Newton |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menggunakan teorema binomial untuk ekspansi sederhana. |

Run 2 — solusi: Menggunakan teorema binomial (2t+h)^5, suku dengan t^3 h^2 adalah C(5,3) * (2t)^3 * (h)^2 = 10 * 8 * t^3 h^2 = 80 t^3 h^2. Koefisiennya adalah 80.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema binomial untuk mencari koefisien suku tertentu dalam ekspansi polinomial.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan teorema binomial untuk menentukan koefisien suku.. Bukti: model total pengaruhnya adalah (2t+h)^5
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman teorema binomial. Ini adalah prosedur rutin bagi siswa kelas 12, namun memerlukan ketelitian dalam mengidentifikasi koefisien (2^3) dan kombinasi (C(5,3)).. Bukti: (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial Newton |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi binomial merupakan bagian dari kurikulum kelas 12. Prosedur ini standar namun memerlukan ketelitian dalam mengalikan koefisien binomial dengan pangkat dari konstanta. |

Run 3 — solusi: Ekspansi binomial (2t+h)^5 menggunakan rumus C(n,k) * a^(n-k) * b^k. Untuk suku t^3 h^2, kita gunakan n=5, k=2 (atau n-k=3): C(5,3) * (2t)^3 * (h)^2 = 10 * 8t^3 * h^2 = 80t^3 h^2. Koefisiennya adalah 80.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema binomial untuk mencari koefisien suku tertentu dalam ekspansi. Ini adalah penerapan prosedur rutin (teorema binomial) pada konteks yang diberikan.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang struktur ekspansi binomial dan penerapan algoritma koefisien binomial.. Bukti: model total pengaruhnya adalah (2t+h)^5
- Intended difficulty `classify/Easy`: Soal ini memerlukan penerapan langsung rumus binomial. Langkah-langkahnya rutin (identifikasi n, k, dan koefisien). Tidak ada kendala non-rutin.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial Newton |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi binomial adalah standar kelas 12. Soal ini adalah aplikasi langsung rumus tanpa modifikasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3581`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan teorema binomial untuk menentukan koefisien suku tertentu dalam ekspansi polinomial. Ini adalah penerapan prosedur rutin pada konteks yang diberikan.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang penggunaan rumus teorema binomial untuk menentukan koefisien suku.
- Intended difficulty `Easy`: Soal memerlukan penerapan langsung rumus binomial. Langkah-langkahnya rutin (identifikasi n, k, dan koefisien). Tidak ada kendala non-rutin atau integrasi representasi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial Newton |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi binomial adalah standar kelas 12. Soal ini adalah aplikasi langsung rumus tanpa modifikasi kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Penerapan Permutasi dan Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Guru IPA menjelaskan bahwa kenyamanan belajar dipengaruhi oleh kualitas udara, yang tergantung pada suhu (t) dan kelembaban (h). Dalam penelitian kecil di kelas, ditemukan bahwa pengaruh suhu dua kali lebih besar dibanding kelembaban, dan model total pengaruhnya adalah $(2t+h)^5$. Jika suatu waktu suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian. Berapakah total kontribusi kombinasi tersebut?
Pilihan: A. 80
B. 32
C. 10
D. 40
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `6353e1b1ac73792bd65d8bcc`

Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.<br><br>Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?

| Opsi | Isi |
|---|---|
| A | Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$ |
| B | Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$ |
| C | Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$ |
| D | Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: P(dobel) = 6/36 = 1/6. P(jumlah 6) = {(1,5), (2,4), (3,3), (4,2), (5,1)} = 5/36. Karena lemparan pertama dan kedua saling bebas, peluang gabungan = P(dobel) × P(jumlah 6) = 1/6 × 5/36 = 5/216.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `31c91b0d985f47100518a5becd15458162e23c316275bdf54b02dcb93a6b55b5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2158 |
| 2 | success | valid / verified | applying | procedural | Easy | 2203 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2198 |

Run 1 — solusi: Kejadian A (muncul angka dobel) dan B (jumlah mata dadu 6) adalah kejadian saling bebas. P(A) = 6/36 = 1/6. P(B) = 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Peluang gabungan = P(A) * P(B) = 1/6 * 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep kejadian saling bebas dan menerapkan aturan perkalian untuk dua kejadian yang terpisah, yang merupakan penerapan prosedur rutin dalam peluang.. Bukti: aturan perkalian dapat digunakan; peluang ini dapat terjadi
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang prinsip dasar aturan perkalian dalam peluang (konseptual) dan penerapannya dalam perhitungan (prosedural).. Bukti: aturan perkalian dapat digunakan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Siswa hanya perlu mengidentifikasi dua kejadian independen, menghitung peluang masing-masing, dan mengalikannya.. Bukti: melemparkan sepasang dadu; mendapatkan angka dobel; mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal pada pelemparan dua dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk (saling bebas) adalah standar kurikulum SMA kelas 12. Prosedur perhitungan peluang dadu merupakan latihan dasar yang familiar. |

Run 2 — solusi: P(dobel) = 6/36 = 1/6. P(jumlah 6) = {(1,5), (2,4), (3,3), (4,2), (5,1)} = 5/36. Karena lemparan pertama dan kedua saling bebas, peluang gabungan = P(dobel) × P(jumlah 6) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi independensi dua kejadian dan menerapkan aturan perkalian peluang, yang merupakan penerapan prosedur rutin dalam konteks peluang majemuk.. Bukti: Jelaskan mengapa aturan perkalian dapat digunakan; Berapa peluangnya?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip dasar peluang kejadian saling bebas (konseptual) dan menerapkan algoritma perkalian peluang (prosedural).. Bukti: aturan perkalian dapat digunakan; peluang ini dapat terjadi
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Siswa hanya perlu menghitung ruang sampel untuk dua kejadian sederhana dan mengalikannya. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: melemparkan sepasang dadu; mendapatkan angka dobel; mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel dua dadu dan aturan perkalian peluang kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah standar kurikulum kelas 12. Soal ini menguji pemahaman dasar tanpa variasi yang menantang. |

Run 3 — solusi: Kejadian A (muncul angka dobel) dan B (jumlah mata dadu 6) adalah kejadian saling bebas. P(A) = 6/36 = 1/6. P(B) = 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Peluang gabungan = P(A) x P(B) = 1/6 x 5/36 = 5/216.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi sifat kejadian saling bebas (konseptual) dan menerapkan aturan perkalian peluang (prosedural) untuk dua kejadian yang berbeda. Ini termasuk dalam kategori applying karena siswa harus memilih dan menerapkan prosedur yang tepat pada situasi rutin.. Bukti: Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep kejadian saling bebas dan prinsip perkalian dalam peluang untuk menyelesaikan masalah ini.. Bukti: aturan perkalian dapat digunakan; peluang ini dapat terjadi
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam materi peluang kejadian majemuk. Siswa hanya perlu menghitung peluang masing-masing kejadian sederhana dan mengalikannya. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: melemparkan sepasang dadu; mendapatkan angka dobel; mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian sederhana pada pelemparan dua dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian saling bebas adalah standar kurikulum kelas 12. Soal ini bersifat langsung dan tidak memerlukan analisis mendalam. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3743`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas dan menerapkan aturan perkalian peluang. Ini adalah penerapan prosedur rutin dalam konteks peluang majemuk.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang prinsip kejadian saling bebas (konseptual) dan penggunaan algoritma perkalian peluang (prosedural).
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Siswa hanya perlu menghitung peluang masing-masing kejadian sederhana dan mengalikannya. Tidak ada kendala kompleks atau strategi nonrutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal pada pelemparan dua dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk (saling bebas) adalah standar kurikulum SMA kelas 12. Prosedur perhitungan peluang dadu merupakan latihan dasar yang familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Aturan Perkalian
Tipe soal: multiple_choice
Stimulus: -
Soal: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.

Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
Pilihan: A. Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$
B. Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$
C. Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$
D. Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `802d8b32ff2e7869391e39e1`

Mahira mulai mengunduh jadwal pertandingan sepak bola Piala Dunia yang akan datang dimulai dari babak perempat final. Berikut bagan yang diperoleh Mahira. Selanjutnya, Mahira memberikan jajak pendapat kepada teman-temannya yang dahulu rutin menonton pertandingan sepak bola dan menikmati permainan tersebut. Berdasarkan jajak pendapat yang dilakukan Mahira, ia dapat menghitung peluang masing-masing tim tersebut untuk menang di babak perempat final, seperti yang ditunjukkan pada tabel berikut ini. Namun, semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya, yang terdiri dari semifinal dan final.<br><br>\|**Prakiraan Perempat Final Piala Dunia**\|\|<br>\|---\|---\|<br>\|Asal Negara\|Peluang Menang\|<br>\|Uruguay\|0,5\|<br>\|Prancis\|0,5\|<br>\|Brazil\|0,8\|<br>\|Belgia\|0,2\|<br>\|Swedia\|0,3\|<br>\|Inggris\|0,7\|<br>\|Rusia\|0,4\|<br>\|Kroasia\|0,6\|<br><br>Berdasarkan bagan pertandingan Piala Dunia dan tabel peluang yang dikumpulkan data oleh Mahira menunjukkan bahwa peluang Inggris untuk memenangkan turnamen tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 0,343 |
| B | 0,125 |
| C | 0,175 |
| D | 1 |

![Gambar sumber soal 29](<../../../images/kelas12_panduan_siswa_kelas12.pdf-0154-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Peluang Inggris juara = P(menang perempat final) * P(menang semifinal) * P(menang final). Berdasarkan tabel, P(menang perempat final) = 0,7. Berdasarkan teks, P(menang semifinal) = 0,5 dan P(menang final) = 0,5. Maka, peluang = 0,7 * 0,5 * 0,5 = 0,175.
Gambar sumber: images/kelas12_panduan_siswa_kelas12.pdf-0154-01.png. Transkripsi visual: Bagan turnamen sistem gugur dimulai dari perempat final, berlanjut ke semifinal, final, dan juara. Inggris berada di perempat final melawan Swedia.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `33b478b5314cf393effe8ee282cdb55085a9128410f4d80d28dcf629bc9e607f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3539 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3538 |
| 3 | success | valid / verified | applying | procedural | Medium | 3546 |

Run 1 — solusi: Peluang Inggris juara = P(menang perempat final) x P(menang semifinal) x P(menang final). Berdasarkan tabel, P(menang perempat final) = 0,7. Berdasarkan teks, P(menang semifinal) = 0,5 dan P(menang final) = 0,5. Maka, peluang = 0,7 * 0,5 * 0,5 = 0,175.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi tahapan turnamen (perempat final, semifinal, final) dan mengalikan peluang kejadian saling bebas yang berurutan untuk mencapai hasil akhir.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prinsip perkalian peluang untuk kejadian majemuk yang berurutan dalam konteks turnamen.. Bukti: peluang masing-masing tim tersebut untuk menang di babak perempat final; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman struktur turnamen dan penerapan aturan perkalian peluang. Langkah-langkahnya rutin namun memerlukan integrasi data dari tabel dan teks.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan perkalian peluang untuk kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena menguji pemahaman peluang majemuk dalam konteks nyata yang memerlukan interpretasi bagan dan tabel. |

Run 2 — solusi: Peluang Inggris juara = P(menang perempat final) x P(menang semifinal) x P(menang final). Diketahui P(menang perempat final) = 0,7. P(menang semifinal) = 0,5. P(menang final) = 0,5. Maka, 0,7 x 0,5 x 0,5 = 0,175.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari tabel (peluang perempat final) dan teks (peluang semifinal dan final) untuk menghitung peluang kejadian majemuk yang saling bebas. Ini adalah penerapan konsep peluang pada situasi rutin.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip perkalian peluang untuk kejadian majemuk yang berurutan dalam sistem gugur.. Bukti: peluang masing-masing tim tersebut untuk menang di babak perempat final; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman struktur turnamen dan penerapan aturan perkalian peluang. Langkah-langkahnya rutin dan prosedural.. Bukti: peluang masing-masing tim tersebut untuk menang di babak perempat final; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk (aturan perkalian) dan pembacaan bagan turnamen. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengidentifikasi tahapan turnamen dan menerapkan aturan perkalian peluang untuk kejadian berurutan. |

Run 3 — solusi: Peluang Inggris juara = P(menang perempat final) x P(menang semifinal) x P(menang final). Berdasarkan tabel, P(menang perempat final) = 0,7. Berdasarkan teks, P(menang semifinal) = 0,5 dan P(menang final) = 0,5. Jadi, 0,7 x 0,5 x 0,5 = 0,175.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan data dari tabel (peluang perempat final) dengan informasi teks (peluang semifinal dan final) untuk menghitung peluang kejadian majemuk yang saling bebas.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prinsip perkalian peluang untuk kejadian majemuk (independen) dalam konteks turnamen.. Bukti: peluang masing-masing tim tersebut untuk menang di babak perempat final; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman struktur turnamen dan penerapan aturan perkalian peluang. Langkah-langkahnya rutin dan prosedural bagi siswa kelas 12.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk (aturan perkalian) dan pembacaan tabel/bagan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menuntut siswa mengidentifikasi tahapan turnamen (perempat final, semifinal, final) dan mengalikan peluang yang relevan. Ini adalah standar kemampuan kelas 12 dalam menerapkan aturan peluang. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5205`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi tahapan turnamen (perempat final, semifinal, final) dan mengalikan peluang kejadian saling bebas yang berurutan untuk mencapai hasil akhir.
- Dimensi pengetahuan `procedural`: Siswa menerapkan prinsip perkalian peluang untuk kejadian majemuk yang berurutan dalam konteks turnamen.
- Intended difficulty `Medium`: Soal memerlukan pemahaman struktur turnamen dan penerapan aturan perkalian peluang. Langkah-langkahnya rutin namun memerlukan integrasi data dari tabel dan teks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan perkalian peluang untuk kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena menguji pemahaman peluang majemuk dalam konteks nyata yang memerlukan interpretasi bagan dan tabel. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Suatu Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Mahira mulai mengunduh jadwal pertandingan sepak bola Piala Dunia yang akan datang dimulai dari babak perempat final. Berikut bagan yang diperoleh Mahira. Selanjutnya, Mahira memberikan jajak pendapat kepada teman-temannya yang dahulu rutin menonton pertandingan sepak bola dan menikmati permainan tersebut. Berdasarkan jajak pendapat yang dilakukan Mahira, ia dapat menghitung peluang masing-masing tim tersebut untuk menang di babak perempat final, seperti yang ditunjukkan pada tabel berikut ini. Namun, semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya, yang terdiri dari semifinal dan final.

|**Prakiraan Perempat Final Piala Dunia**||
|---|---|
|Asal Negara|Peluang Menang|
|Uruguay|0,5|
|Prancis|0,5|
|Brazil|0,8|
|Belgia|0,2|
|Swedia|0,3|
|Inggris|0,7|
|Rusia|0,4|
|Kroasia|0,6|

Berdasarkan bagan pertandingan Piala Dunia dan tabel peluang yang dikumpulkan data oleh Mahira menunjukkan bahwa peluang Inggris untuk memenangkan turnamen tersebut adalah ....
Pilihan: A. 0,343
B. 0,125
C. 0,175
D. 1
Transkripsi visual: Bagan turnamen sistem gugur dimulai dari perempat final, berlanjut ke semifinal, final, dan juara. Inggris berada di perempat final melawan Swedia.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `e6f2f945c5e535887f5e64bc`

Jika tiga dadu standar bersisi enam dilempar bersama-sama, berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12?

| Opsi | Isi |
|---|---|
| A | $\frac{1}{36}$ |
| B | $\frac{1}{216}$ |
| C | $\frac{1}{18}$ |
| D | $\frac{25}{216}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Ruang sampel n(S) = 6^3 = 216. Kombinasi angka (x,y,z) dengan 1<=x,y,z<=6 yang berjumlah 12: (6,5,1) ada 6 permutasi, (6,4,2) ada 6, (6,3,3) ada 3, (5,5,2) ada 3, (5,4,3) ada 6, (4,4,4) ada 1. Total kejadian n(E) = 6+6+3+3+6+1 = 25. Peluang = 25/216.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `23a435f733be354fb945d94b35181ea167ffd4e279384e6388aab09f4d044a2a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2273 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2195 |
| 3 | success | valid / verified | applying | procedural | Medium | 2180 |

Run 1 — solusi: Ruang sampel n(S) = 6^3 = 216. Kejadian jumlah 12: (1,5,6)x6=6, (1,6,5)x6=6, (2,4,6)x6=6, (2,5,5)x3=3, (3,3,6)x3=3, (3,4,5)x6=6, (4,4,4)x1=1. Total kombinasi: (6,5,1) -> 6 permutasi, (6,4,2) -> 6, (5,5,2) -> 3, (5,4,3) -> 6, (4,4,4) -> 1, (6,3,3) -> 3. Total = 25. Peluang = 25/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel dan menghitung banyaknya kejadian yang memenuhi syarat jumlah 12 dengan mempertimbangkan urutan (permutasi) dari kombinasi angka yang mungkin. Ini melibatkan penerapan konsep peluang kejadian majemuk secara sistematis.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama; peluang jumlah total dadu pada ketiga pelemparan sama dengan 12
- Dimensi pengetahuan `classify/procedural`: Siswa harus menerapkan prosedur sistematis untuk mencacah ruang sampel dan kejadian yang diinginkan (menggunakan prinsip permutasi/kombinasi atau daftar terstruktur) untuk menghitung peluang.. Bukti: tiga dadu standar bersisi enam; peluang jumlah total dadu
- Intended difficulty `classify/Medium`: Soal ini memerlukan ketelitian dalam mencacah semua kemungkinan kombinasi angka yang berjumlah 12 dan memperhitungkan permutasi dari setiap kombinasi tersebut. Ini adalah langkah rutin namun memerlukan ketelitian tinggi agar tidak ada yang terlewat.. Bukti: tiga dadu standar bersisi enam; jumlah total dadu pada ketiga pelemparan sama dengan 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, aturan perkalian, dan permutasi sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan pencacahan sistematis untuk kejadian pada ruang sampel yang cukup besar (216) tanpa kesalahan. |

Run 2 — solusi: Ruang sampel n(S) = 6^3 = 216. Kejadian jumlah 12 dari 3 dadu (x+y+z=12, 1<=x,y,z<=6): (6,5,1)x6=6, (6,4,2)x6=6, (6,3,3)x3=3, (5,5,2)x3=3, (5,4,3)x6=6, (4,4,4)x1=1. Total n(E) = 6+6+3+3+6+1 = 25. Peluang = 25/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel dan menghitung banyaknya kejadian yang memenuhi syarat jumlah 12 dengan memperhatikan urutan (permutasi dengan pengulangan/kombinasi). Ini adalah penerapan prosedur peluang pada situasi rutin.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama; peluang jumlah total dadu pada ketiga pelemparan sama dengan 12
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman tentang prinsip dasar pencacahan dan konsep peluang kejadian majemuk pada ruang sampel diskrit.. Bukti: peluang jumlah total dadu pada ketiga pelemparan sama dengan 12
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan ketelitian dalam mendaftar semua kombinasi angka yang mungkin berjumlah 12 dengan memperhatikan urutan (permutasi), yang merupakan langkah rutin namun membutuhkan kecermatan agar tidak ada yang terlewat.. Bukti: tiga dadu standar bersisi enam; jumlah total dadu pada ketiga pelemparan sama dengan 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan konsep peluang kejadian. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan enumerasi sistematis untuk ruang sampel yang relatif kecil (216) dan memahami bahwa urutan dadu berpengaruh. |

Run 3 — solusi: Ruang sampel n(S) = 6^3 = 216. Kombinasi angka yang berjumlah 12: (6,5,1)x6=6, (6,4,2)x6=6, (6,3,3)x3=3, (5,5,2)x3=3, (5,4,3)x6=6, (4,4,4)x1=1. Total kejadian = 6+6+3+3+6+1 = 25. Peluang = 25/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel dan menghitung banyaknya kejadian yang memenuhi syarat jumlah 12 dengan mempertimbangkan urutan (permutasi) dari kombinasi angka yang mungkin. Ini adalah penerapan prosedur peluang pada situasi rutin.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama; berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12
- Dimensi pengetahuan `classify/procedural`: Siswa harus menerapkan algoritma perhitungan peluang kejadian majemuk dengan ruang sampel yang terdefinisi dengan baik.. Bukti: peluang jumlah total dadu; tiga dadu standar bersisi enam
- Intended difficulty `classify/Medium`: Soal ini memerlukan ketelitian dalam mendaftar semua kombinasi yang mungkin berjumlah 12 dan menghitung permutasi untuk setiap kombinasi tersebut. Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: tiga dadu standar bersisi enam; jumlah total dadu pada ketiga pelemparan sama dengan 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel, dan permutasi sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan enumerasi sistematis untuk kejadian dengan ruang sampel yang cukup besar (216) namun masih terjangkau. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4064`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur sistematis untuk mencacah ruang sampel dan kejadian yang diinginkan (permutasi dari kombinasi angka) untuk menghitung peluang. Ini adalah penerapan konsep peluang pada situasi rutin.
- Dimensi pengetahuan `procedural`: Siswa harus menerapkan algoritma perhitungan peluang kejadian majemuk dengan ruang sampel yang terdefinisi dengan baik.
- Intended difficulty `Medium`: Soal ini memerlukan ketelitian dalam mendaftar semua kombinasi yang mungkin berjumlah 12 dan menghitung permutasi untuk setiap kombinasi tersebut. Ini melibatkan beberapa langkah rutin yang saling terkait.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel, dan permutasi sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan enumerasi sistematis untuk kejadian dengan ruang sampel yang cukup besar (216) namun masih terjangkau. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Suatu Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika tiga dadu standar bersisi enam dilempar bersama-sama, berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12?
Pilihan: A. $\frac{1}{36}$
B. $\frac{1}{216}$
C. $\frac{1}{18}$
D. $\frac{25}{216}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `3631e6eb715153077f0dac66`

Suatu dompet berisi 4 keping uang logam seribu rupiah dan 3 keping uang logam lima ratus rupiah. Dompet kedua berisi 3 keping uang logam seribu rupiah dan 5 keping uang lima ratus ripuah. Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.<br><br>Jika kemudian diambil sekeping uang logam dari dompet kedua, berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?

| Opsi | Isi |
|---|---|
| A | $\frac{38}{63}$ |
| B | $\frac{5}{8}$ |
| C | $\frac{3}{7}$ |
| D | $\frac{20}{63}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `38/63`.
Solusi minimum hasil AI: Misal A kejadian koin 1000 dipindah (P(A)=4/7), B kejadian koin 500 dipindah (P(B)=3/7). Jika A terjadi, dompet 2 berisi 4 koin 1000 dan 5 koin 500 (total 9), P(500\|A)=5/9. Jika B terjadi, dompet 2 berisi 3 koin 1000 dan 6 koin 500 (total 9), P(500\|B)=6/9. Peluang total = P(A)P(500\|A) + P(B)P(500\|B) = (4/7)(5/9) + (3/7)(6/9) = 20/63 + 18/63 = 38/63.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b81224b363d097e916a4372506e02d12aa9f155879822f9ca43cc1f0173caf4e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2357 |
| 2 | success | valid / verified | applying | procedural | Medium | 2307 |
| 3 | success | valid / verified | applying | procedural | Medium | 2287 |

Run 1 — solusi: Misal A kejadian koin 1000 dipindah (P(A)=4/7), B kejadian koin 500 dipindah (P(B)=3/7). Jika A terjadi, dompet 2 berisi 4 koin 1000 dan 5 koin 500 (total 9), P(500\|A)=5/9. Jika B terjadi, dompet 2 berisi 3 koin 1000 dan 6 koin 500 (total 9), P(500\|B)=6/9. Peluang total = P(A)P(500\|A) + P(B)P(500\|B) = (4/7)(5/9) + (3/7)(6/9) = 20/63 + 18/63 = 38/63.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua skenario yang saling lepas (pemindahan koin 1000 atau 500), menghitung peluang masing-masing skenario, menyesuaikan komposisi dompet kedua, dan menerapkan aturan peluang total. Ini adalah penerapan prosedur rutin dalam situasi majemuk.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang peluang bersyarat dan peluang kejadian majemuk, serta prosedur perhitungan peluang total.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang perubahan ruang sampel setelah perpindahan objek. Siswa harus melakukan dua langkah perhitungan peluang yang saling terkait (peluang pemindahan dan peluang pengambilan kedua). Ini adalah standar untuk tingkat menengah.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; dompet kedua berisi 3 keping uang logam seribu rupiah dan 5 keping uang lima ratus ripuah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal, penjumlahan dan perkalian peluang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena melibatkan analisis kejadian majemuk dengan perubahan kondisi (perpindahan objek) yang memerlukan ketelitian dalam menghitung ruang sampel baru. |

Run 2 — solusi: Misal A1 kejadian terambil 1000 dari dompet 1 (P=4/7), A2 kejadian terambil 500 dari dompet 1 (P=3/7). Jika A1 terjadi, dompet 2 berisi 4 (1000) dan 5 (500), P(500\|A1)=5/9. Jika A2 terjadi, dompet 2 berisi 3 (1000) dan 6 (500), P(500\|A2)=6/9. Peluang total = (4/7 * 5/9) + (3/7 * 6/9) = 20/63 + 18/63 = 38/63.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi dua skenario yang saling lepas (pemindahan koin 1000 atau 500) dan menghitung peluang bersyarat untuk masing-masing skenario sebelum menjumlahkannya. Ini adalah penerapan prosedur peluang majemuk yang rutin namun memerlukan ketelitian dalam mengintegrasikan dua tahap kejadian.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan penjumlahan dan perkalian peluang pada kejadian majemuk yang melibatkan perubahan ruang sampel.. Bukti: peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua tahap kejadian yang saling bergantung (perubahan komposisi dompet kedua setelah pemindahan). Siswa harus melakukan perhitungan peluang bersyarat dan penjumlahan peluang, yang merupakan prosedur rutin namun memerlukan pemilihan langkah yang tepat.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian tunggal, peluang bersyarat dasar, dan aturan penjumlahan/perkalian peluang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena menguji pemahaman tentang perubahan ruang sampel akibat kejadian sebelumnya, yang merupakan standar kompetensi peluang majemuk. |

Run 3 — solusi: Misal A1 kejadian terambil 1000 dari dompet 1 (P=4/7), A2 kejadian terambil 500 dari dompet 1 (P=3/7). Jika A1 terjadi, dompet 2 berisi 4x1000, 5x500 (total 9), P(500\|A1)=5/9. Jika A2 terjadi, dompet 2 berisi 3x1000, 6x500 (total 9), P(500\|A2)=6/9. Peluang total = (4/7 * 5/9) + (3/7 * 6/9) = 20/63 + 18/63 = 38/63.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua skenario yang saling lepas berdasarkan koin yang dipindahkan, menghitung peluang bersyarat untuk setiap skenario, dan menjumlahkannya. Ini adalah penerapan prosedur peluang kejadian majemuk yang rutin.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; Jika kemudian diambil sekeping uang logam dari dompet kedua, berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip peluang total dan peluang bersyarat untuk menyelesaikan masalah yang melibatkan perubahan ruang sampel.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang perubahan komposisi dompet kedua setelah pemindahan koin. Ini melibatkan dua langkah rutin (menghitung peluang pemindahan dan peluang pengambilan kedua) yang saling terkait.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; Jika kemudian diambil sekeping uang logam dari dompet kedua

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal, penjumlahan peluang, peluang bersyarat dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah peluang bersyarat dengan dua tahap adalah standar untuk kelas 12, memerlukan ketelitian dalam memperbarui ruang sampel. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4395`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi dua skenario yang saling lepas (pemindahan koin 1000 atau 500), menghitung peluang masing-masing skenario, menyesuaikan komposisi dompet kedua, dan menerapkan aturan peluang total. Ini adalah penerapan prosedur rutin dalam situasi majemuk.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang peluang bersyarat dan peluang kejadian majemuk, serta prosedur perhitungan peluang total.
- Intended difficulty `Medium`: Soal memerlukan pemahaman tentang perubahan ruang sampel setelah perpindahan objek. Siswa harus melakukan dua langkah perhitungan peluang yang saling terkait (peluang pemindahan dan peluang pengambilan kedua). Ini adalah standar untuk tingkat menengah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal, penjumlahan dan perkalian peluang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena melibatkan analisis kejadian majemuk dengan perubahan kondisi (perpindahan objek) yang memerlukan ketelitian dalam menghitung ruang sampel baru. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Kejadian Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu dompet berisi 4 keping uang logam seribu rupiah dan 3 keping uang logam lima ratus rupiah. Dompet kedua berisi 3 keping uang logam seribu rupiah dan 5 keping uang lima ratus ripuah. Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.

Jika kemudian diambil sekeping uang logam dari dompet kedua, berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
Pilihan: A. $\frac{38}{63}$
B. $\frac{5}{8}$
C. $\frac{3}{7}$
D. $\frac{20}{63}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `4f4ccc08a9a611e7c44d48a3`

Suatu kantong berisi enam bola merah dan empat bola biru. Dari kantong tersebut akan diambil dua bola berturut-turut.<br><br>Berapa peluang terambilnya dua bola biru, jika: a. dengan pengembalian, dan

| Opsi | Isi |
|---|---|
| A | $\frac{4}{5}$ |
| B | $\frac{2}{15}$ |
| C | $\frac{2}{5}$ |
| D | $\frac{4}{25}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Total bola = 6 merah + 4 biru = 10. Peluang terambil bola biru pertama (P1) = 4/10 = 2/5. Karena dengan pengembalian, peluang terambil bola biru kedua (P2) tetap 4/10 = 2/5. Peluang dua bola biru = P1 x P2 = (2/5) x (2/5) = 4/25.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e4f0319249f91f0b03164cef613d0f8b67c18caa390f3c65b6981c134f88a93`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2079 |
| 2 | success | valid / verified | applying | procedural | Easy | 2058 |
| 3 | success | valid / verified | applying | procedural | Easy | 2059 |

Run 1 — solusi: Total bola = 6 merah + 4 biru = 10. Peluang terambil bola biru pertama (P1) = 4/10 = 2/5. Karena dengan pengembalian, peluang terambil bola biru kedua (P2) tetap 4/10 = 2/5. Peluang dua bola biru = P1 x P2 = (2/5) x (2/5) = 4/25.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi konsep peluang kejadian majemuk saling bebas (dengan pengembalian) dan menerapkan rumus perkalian peluang dasar.. Bukti: Suatu kantong berisi enam bola merah dan empat bola biru.; diambil dua bola berturut-turut.; dengan pengembalian
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana aturan pengembalian mempengaruhi ruang sampel dan perhitungan peluang kejadian majemuk.. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk materi peluang kelas 12. Prosedur yang digunakan langsung (perkalian peluang kejadian bebas) tanpa kendala kompleks.. Bukti: enam bola merah dan empat bola biru; diambil dua bola berturut-turut; dengan pengembalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian peluang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dengan pengembalian adalah standar dasar kurikulum SMA kelas 12, tidak memerlukan strategi nonrutin. |

Run 2 — solusi: Total bola = 6 merah + 4 biru = 10. Peluang terambil bola biru pertama (P1) = 4/10 = 2/5. Karena pengambilan dengan pengembalian, peluang terambil bola biru kedua (P2) tetap 4/10 = 2/5. Peluang dua bola biru = P1 x P2 = (2/5) x (2/5) = 4/25.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang kejadian majemuk yang saling bebas (dengan pengembalian) dengan mengalikan peluang masing-masing kejadian.. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian peluang untuk kejadian independen.. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus peluang kejadian saling bebas. Prosedurnya familiar dan langkah-langkahnya sangat terbatas.. Bukti: diambil dua bola berturut-turut; dengan pengembalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian peluang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah standar kelas 12. Soal ini tidak memiliki kompleksitas tambahan, sehingga tergolong mudah. |

Run 3 — solusi: Total bola = 10. Peluang terambil bola biru pada pengambilan pertama (P1) = 4/10 = 2/5. Karena dengan pengembalian, peluang terambil bola biru pada pengambilan kedua (P2) tetap 4/10 = 2/5. Peluang kedua bola biru = P1 * P2 = (2/5) * (2/5) = 4/25.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian untuk kejadian saling bebas (independen) dalam konteks peluang majemuk. Ini adalah prosedur standar yang rutin.. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar peluang kejadian majemuk yang saling bebas (konseptual) dan penerapannya dalam perhitungan (prosedural).. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan prosedur yang familiar bagi siswa kelas 12, dan hanya melibatkan satu konsep utama (peluang kejadian saling bebas).. Bukti: dua bola berturut-turut; dengan pengembalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian peluang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah standar kurikulum kelas 12. Soal ini merupakan aplikasi langsung dari definisi kejadian saling bebas. |

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Kejadian Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu kantong berisi enam bola merah dan empat bola biru. Dari kantong tersebut akan diambil dua bola berturut-turut.

Berapa peluang terambilnya dua bola biru, jika: a. dengan pengembalian, dan
Pilihan: A. $\frac{4}{5}$
B. $\frac{2}{15}$
C. $\frac{2}{5}$
D. $\frac{4}{25}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
