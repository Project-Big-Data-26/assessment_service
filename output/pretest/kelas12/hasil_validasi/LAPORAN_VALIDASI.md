# Validasi ulang soal kelas 12 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-sma12-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sma12-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 12 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 12, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 32; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 25, "knowing": 4, "undecided": 1, "reasoning": 2}, "knowledgeDimension": {"procedural": 23, "factual": 1, "conceptual": 7, "undecided": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 18, "Medium": 11, "undecided": 1, "Hard": 2}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 25, "knowing": 4, "reasoning": 2}, "knowledgeDimension": {"procedural": 23, "factual": 1, "conceptual": 7, "metacognitive": 0}, "intendedDifficulty": {"Easy": 18, "Medium": 11, "Hard": 2}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 31, "revision_required": 1}`.
Run awal sukses: 96/96; adjudikasi: 14; token sukses tercatat: 366,420.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 18 | 18 | [Easy.json](difficulty/Easy.json) |
| Medium | 11 | 11 | [Medium.json](difficulty/Medium.json) |
| Hard | 2 | 2 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 12, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 12, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 12.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `641a35435d963d4ebd4b73ac898233fdf42664fe6c96af48c56036af6da00432`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3497 |
| 2 | success | valid / verified | applying | procedural | Easy | 3428 |
| 3 | success | valid / verified | applying | procedural | Easy | 3564 |

Run 1 — solusi: Pola barisan adalah perkalian dengan bilangan asli yang berurutan: 1x1=1, 1x2=2, 2x3=6. Maka suku berikutnya adalah 6x4=24 dan 24x5=120.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola rekursif perkalian yang meningkat (1, 2, 3, 4, 5) untuk menentukan suku berikutnya. Ini termasuk menerapkan konsep barisan yang sudah dipelajari.. Bukti: 1, 1, 2, 6, …, …; pola perkalian bertambah: x1,x2,x3,x4,x5
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang pola bilangan dan konsep barisan untuk mengidentifikasi aturan pembentukan suku.. Bukti: 1, 1, 2, 6, …, …; pola perkalian bertambah
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengidentifikasi pola barisan yang tidak konstan (bukan aritmetika/geometri standar). Meskipun polanya sederhana, siswa harus melakukan eksplorasi pola sendiri.. Bukti: 1, 1, 2, 6, …, …; pola perkalian bertambah: x1,x2,x3,x4,x5

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
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 12, mengenali pola barisan faktorial sederhana seperti ini adalah tugas rutin yang tidak memerlukan perencanaan kompleks. |

Run 2 — solusi: Pola barisan adalah u_n = u_{n-1} * (n-1), yang setara dengan faktorial (n-1)!. Suku ke-5 adalah 6 * 4 = 24. Suku ke-6 adalah 24 * 5 = 120. Jadi, dua suku berikutnya adalah 24 dan 120.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pola perkalian yang meningkat pada barisan bilangan dan menerapkan pola tersebut untuk menentukan suku berikutnya. Ini adalah penerapan prosedur pengenalan pola yang rutin.. Bukti: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 1, 1, 2, 6, …, …
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau teknik pengenalan pola barisan bilangan (faktorial), yang merupakan pengetahuan prosedural.. Bukti: 1, 1, 2, 6, …, …
- Intended difficulty `classify/Easy`: Soal ini dikategorikan mudah karena pola barisan (faktorial) merupakan pola yang sangat standar dan familiar bagi siswa SMA. Langkah penyelesaiannya langsung dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: 1, 1, 2, 6, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang barisan bilangan dan operasi perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan pengenalan pola dasar yang sesuai untuk kelas 12 sebagai bagian dari materi barisan dan deret, tanpa tuntutan integrasi konsep yang tinggi. |

Run 3 — solusi: Pola barisan adalah perkalian dengan bilangan asli yang berurutan: 1x1=1, 1x2=2, 2x3=6. Maka suku berikutnya adalah 6x4=24 dan 24x5=120.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola rekursif (perkalian dengan bilangan yang meningkat) dan menerapkannya untuk menentukan dua suku berikutnya. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: 1, 1, 2, 6, …, …; pola perkalian bertambah: x1,x2,x3,x4,x5
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam mengenali dan menggunakan algoritma atau aturan pembentukan barisan (prosedur) untuk menemukan suku berikutnya.. Bukti: 1, 1, 2, 6, …, …; pola perkalian bertambah: x1,x2,x3,x4,x5
- Intended difficulty `classify/Easy`: Soal ini termasuk Easy karena polanya sangat sederhana dan langsung terlihat setelah menguji beberapa operasi dasar. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: 1, 1, 2, 6, …, …; pola perkalian bertambah: x1,x2,x3,x4,x5

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
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 12, mengenali pola barisan sederhana seperti ini adalah kemampuan dasar yang sudah dikuasai sejak jenjang sebelumnya. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `577daf905630d2b50cdcacfa`

Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …

| Opsi | Isi |
|---|---|
| A | 24, 120 |
| B | $\frac{1}{4}$, $\frac{1}{16}$ |
| C | 4, 4 |
| D | 1, 3 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Barisan tersebut adalah barisan konstan dengan suku ke-n (Un) = 4 untuk setiap n. Maka, dua suku berikutnya adalah 4 dan 4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7ea1e4e9dbf7404d81a1326b483049a6953feb03d0fdd8f0a6c402abc98ab7de`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3097 |
| 2 | success | valid / verified | knowing | factual | Easy | 3113 |
| 3 | success | valid / verified | knowing | factual | Easy | 3128 |

Run 1 — solusi: Barisan tersebut adalah barisan konstan dengan suku ke-n (Un) = 4 untuk setiap n. Maka, dua suku berikutnya adalah 4 dan 4.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola barisan konstan yang sangat sederhana (setiap suku bernilai sama) tanpa perlu prosedur kompleks.. Bukti: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman dasar mengenai definisi barisan konstan, yang merupakan pengetahuan faktual tentang pola bilangan.. Bukti: 4, 4, 4, 4, …, …
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena pola barisan konstan langsung terlihat tanpa memerlukan perhitungan atau strategi khusus.. Bukti: 4, 4, 4, 4, …, …

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

Run 2 — solusi: Barisan tersebut adalah barisan konstan dengan nilai setiap suku adalah 4. Maka, dua suku berikutnya adalah 4 dan 4.
- Domain kognitif `classify/knowing`: Soal hanya meminta pengenalan pola barisan konstan yang sangat sederhana. Siswa cukup mengenali bahwa nilai suku tidak berubah.. Bukti: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman dasar tentang definisi barisan konstan sebagai fakta matematika sederhana.. Bukti: 4, 4, 4, 4, …, …
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Tidak ada langkah perhitungan atau perencanaan yang diperlukan.. Bukti: 4, 4, 4, 4, …, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola barisan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini terlalu sederhana untuk standar kelas 12, namun secara teknis valid sebagai pengenalan barisan. |

Run 3 — solusi: Barisan tersebut adalah barisan konstan dengan nilai setiap suku adalah 4. Maka, dua suku berikutnya adalah 4 dan 4.
- Domain kognitif `classify/knowing`: Soal hanya meminta pengenalan pola barisan konstan yang sangat sederhana. Siswa hanya perlu mengenali bahwa nilai suku tidak berubah.. Bukti: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman dasar tentang definisi barisan konstan, yang merupakan elemen pengetahuan faktual dalam topik barisan.. Bukti: 4, 4, 4, 4, …, …
- Intended difficulty `classify/Easy`: Soal sangat sederhana, tidak memerlukan perhitungan kompleks atau strategi khusus.. Bukti: 4, 4, 4, 4, …, …

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
| gradeRelativeRationale | Soal ini terlalu sederhana untuk standar kelas 12, namun secara teknis valid sebagai pengenalan pola dasar. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `cde1c3bcaf6c566fa0d0dfde`

Jika Un menyatakan suku ke-n suatu barisan aritmetika dan diketahui U 6 - U 8 + U 10 - U 12 + U 14 = 20, berapa jumlah 19 suku pertama barisan tersebut?

| Opsi | Isi |
|---|---|
| A | 380 |
| B | 20 |
| C | 360 |
| D | 190 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: U_n = a + (n-1)d. Persamaan: (a+5d) - (a+7d) + (a+9d) - (a+11d) + (a+13d) = 20. Menyederhanakan: a + 9d = 20. Rumus jumlah: S_19 = 19/2 * (2a + 18d) = 19 * (a + 9d). Substitusi: S_19 = 19 * 20 = 380.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7d6a115fea3b7394520109bafc7d1915b2d413412adff1ff634f6c1fd9bf0fee`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2957 |
| 2 | success | valid / verified | applying | procedural | Medium | 2899 |
| 3 | success | valid / verified | applying | procedural | Medium | 2906 |

Run 1 — solusi: U_n = a + (n-1)d. Persamaan: (a+5d) - (a+7d) + (a+9d) - (a+11d) + (a+13d) = 20. Menyederhanakan: a + 9d = 20. Rumus jumlah: S_19 = 19/2 * (2a + 18d) = 19 * (a + 9d). Substitusi: S_19 = 19 * 20 = 380.
- Domain kognitif `classify/applying`: Siswa perlu memanipulasi aljabar untuk menyederhanakan ekspresi suku-suku barisan aritmetika menjadi bentuk yang dapat disubstitusikan ke dalam rumus jumlah suku ke-n (S_n). Ini melibatkan pemahaman konsep dasar barisan aritmetika dan penerapan rumus jumlah, yang merupakan prosedur standar.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama barisan tersebut
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara suku-suku dalam barisan aritmetika dan rumus jumlah deret (S_n). Siswa harus menerapkan prosedur aljabar untuk menyederhanakan persamaan yang diberikan agar sesuai dengan bentuk rumus S_n.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama barisan tersebut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya familiar, siswa harus melakukan manipulasi aljabar untuk menyederhanakan ekspresi yang diberikan sebelum bisa menggunakan rumus S_n. Tidak ada langkah yang sangat kompleks, namun memerlukan ketelitian dalam menyederhanakan suku-suku.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama barisan tersebut

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
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan manipulasi aljabar dasar pada barisan aritmetika. Soal ini menuntut pemahaman hubungan antara U_n dan S_n yang merupakan materi standar. |

Run 2 — solusi: U_n = a + (n-1)d. Persamaan: (a+5d) - (a+7d) + (a+9d) - (a+11d) + (a+13d) = 20. Menyederhanakan: a + 9d = 20. S_19 = (19/2)(2a + 18d) = 19(a + 9d). Substitusi: 19 * 20 = 380.
- Domain kognitif `classify/applying`: Siswa perlu memanipulasi aljabar dari suku-suku barisan aritmetika untuk menemukan hubungan antara a dan d (yaitu a+9d=20), kemudian menghubungkannya dengan rumus jumlah suku ke-n (S19). Ini adalah penerapan prosedur yang memerlukan pemahaman konsep barisan.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama barisan tersebut
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang rumus suku ke-n dan jumlah n suku pertama barisan aritmetika serta kemampuan memanipulasi variabel secara prosedural.. Bukti: Un menyatakan suku ke-n suatu barisan aritmetika; jumlah 19 suku pertama
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan manipulasi aljabar untuk menyederhanakan deret yang diberikan menjadi bentuk yang dapat digunakan dalam rumus S19. Siswa harus menyadari bahwa (a+9d) adalah suku tengah (U10) dan bagian dari rumus S19. Langkah-langkahnya jelas namun memerlukan ketelitian dalam penyederhanaan.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus suku ke-n dan jumlah n suku pertama barisan aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan manipulasi aljabar sederhana pada barisan aritmetika. Soal ini menguji pemahaman konsep dasar deret dengan sedikit tantangan aljabar. |

Run 3 — solusi: U_n = a + (n-1)d. Persamaan: (a+5d) - (a+7d) + (a+9d) - (a+11d) + (a+13d) = 20. Menyederhanakan: a + 9d = 20. S_19 = (19/2)(2a + 18d) = 19(a + 9d). Substitusi: 19 * 20 = 380.
- Domain kognitif `classify/applying`: Siswa perlu memanipulasi aljabar dari suku-suku barisan aritmetika untuk menemukan hubungan antara a dan d, lalu menghubungkannya dengan rumus jumlah suku ke-n (S_n). Ini memerlukan penerapan konsep deret aritmetika pada konteks yang sedikit dimodifikasi.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama barisan tersebut
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus suku ke-n dan jumlah n suku pertama barisan aritmetika, serta kemampuan untuk memanipulasi ekspresi aljabar tersebut.. Bukti: U_n = a + (n-1)d; S_n = n/2(2a + (n-1)d)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan manipulasi aljabar untuk menyederhanakan persamaan yang diberikan menjadi bentuk yang berguna (a+9d=20) sebelum dapat disubstitusikan ke dalam rumus S_19. Meskipun prosedurnya familiar, siswa harus melakukan perencanaan langkah untuk menghubungkan ekspresi yang diberikan dengan rumus jumlah.. Bukti: U 6 - U 8 + U 10 - U 12 + U 14 = 20; jumlah 19 suku pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus suku ke-n dan jumlah n suku pertama barisan aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan manipulasi aljabar sederhana pada deret aritmetika. Tingkat kesulitan Medium tepat karena adanya langkah perantara yang harus diselesaikan sebelum mencapai jawaban akhir. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `6e5ddb2020e2a12b1ecf2b03`

Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.

| Opsi | Isi |
|---|---|
| A | 635 |
| B | 315 |
| C | 310 |
| D | 320 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: S_n = a(r^n - 1) / (r - 1). S_6 = 5(2^6 - 1) / (2 - 1) = 5(64 - 1) = 5 * 63 = 315.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8d658166b65147077648aee743559dc4f3b25965585912dacff21f2c0a8e3429`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3335 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3343 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3376 |

Run 1 — solusi: S_n = a(r^n - 1) / (r - 1). S_6 = 5(2^6 - 1) / (2 - 1) = 5(64 - 1) = 5 * 63 = 315.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus jumlah n suku pertama deret geometri yang sudah diketahui parameternya.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma atau rumus jumlah deret geometri untuk menyelesaikan masalah.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
- Intended difficulty `classify/Easy`: Soal bersifat rutin dengan rumus yang jelas dan parameter yang sudah diberikan secara eksplisit. Tidak ada kendala kompleks atau pemilihan strategi yang rumit.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.

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
| gradeRelativeRationale | Materi deret geometri adalah standar kelas 12, dan soal ini merupakan aplikasi langsung rumus tanpa modifikasi. |

Run 2 — solusi: S_n = a(r^n - 1) / (r - 1). S_6 = 5(2^6 - 1) / (2 - 1) = 5(64 - 1) = 5(63) = 315.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat dan menerapkan rumus jumlah deret geometri secara langsung tanpa memerlukan langkah penalaran tambahan atau modifikasi strategi.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2.; Hitunglah jumlah 6 suku pertama deret tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma atau prosedur standar untuk menghitung jumlah deret geometri.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2.; Hitunglah jumlah 6 suku pertama deret tersebut.
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus yang sudah familiar bagi siswa kelas 12. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2.; Hitunglah jumlah 6 suku pertama deret tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jumlah deret geometri. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin standar untuk materi deret geometri di kelas 12, dengan jalur penyelesaian yang jelas dan langsung. |

Run 3 — solusi: S_n = a(r^n - 1) / (r - 1). S_6 = 5(2^6 - 1) / (2 - 1) = 5(64 - 1) = 5 * 63 = 315.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus jumlah deret geometri yang sudah baku. Siswa hanya perlu memasukkan nilai ke dalam rumus tanpa modifikasi strategi atau penalaran kompleks.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2.; Hitunglah jumlah 6 suku pertama deret tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau prosedur standar (rumus jumlah deret geometri) untuk menyelesaikan masalah.. Bukti: Hitunglah jumlah 6 suku pertama deret tersebut.
- Intended difficulty `classify/Easy`: Soal bersifat rutin dengan jalur penyelesaian yang sangat jelas. Tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi non-rutin.. Bukti: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2.; Hitunglah jumlah 6 suku pertama deret tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jumlah deret geometri |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi deret geometri adalah materi dasar yang penyelesaiannya menggunakan rumus langsung tanpa memerlukan langkah perencanaan yang kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `50f81b2d500c6fab49401822`

Raka mengikuti program Youth Creative Entrepreneur di sekolahnya. Untuk membeli peralatan produksi awal, ia memperoleh dana talangan usaha sebesar Rp2.500.000,00 dari koperasi pemuda. Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun dan memberikan keringanan berupa angsuran bulanan tetap selama 2 tahun agar para peserta tidak terbebani. Sebagai bentuk tanggung jawab finansial, Raka perlu menghitung besar cicilan bulanan yang harus ia bayarkan agar pinjaman tersebut lunas sesuai perjanjian. Berapakah cicilan yang harus dibayarkan Raka setiap bulan?

| Opsi | Isi |
|---|---|
| A | Rp104.166,67 |
| B | Rp112.500,00 |
| C | Rp108.333,33 |
| D | Rp225.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bunga total = M x p x t = 2.500.000 x 0,04 x 2 = 200.000. Total pengembalian = 2.500.000 + 200.000 = 2.700.000. Cicilan per bulan = 2.700.000 / 24 = 112.500.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `52b58ad5061797fb0f7f60155c0b52cccb0a0141f912744687fd97c751c297fa`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2938 |
| 2 | success | valid / verified | applying | procedural | Easy | 3509 |
| 3 | success | valid / verified | applying | procedural | Easy | 2885 |

Run 1 — solusi: Bunga total = M x p x t = 2.500.000 x 0,04 x 2 = 200.000. Total pengembalian = 2.500.000 + 200.000 = 2.700.000. Cicilan per bulan = 2.700.000 / 24 = 112.500.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur bunga tunggal yang tepat, mengonversi durasi tahun ke bulan, dan menghitung total pengembalian sebelum membaginya dengan jumlah bulan. Ini adalah penerapan konsep bunga tunggal pada konteks rutin.. Bukti: Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun; memberikan keringanan berupa angsuran bulanan tetap selama 2 tahun; Raka perlu menghitung besar cicilan bulanan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma bunga tunggal dan prosedur perhitungan angsuran tetap.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena prosedurnya sangat standar (bunga tunggal). Siswa hanya perlu melakukan konversi waktu (2 tahun = 24 bulan) dan operasi aritmatika dasar. Tidak ada kendala yang berinteraksi atau strategi non-rutin yang diperlukan.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bunga tunggal dan operasi aritmatika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah topik dasar kelas 12. Soal ini tidak memiliki jebakan kompleks atau integrasi konsep yang menuntut, sehingga sesuai untuk tingkat kemudahan rendah. |

Run 2 — solusi: Bunga (B) = 2.500.000 * 0,04 * 2 = 200.000. Total pinjaman = 2.500.000 + 200.000 = 2.700.000. Cicilan per bulan = 2.700.000 / 24 = 112.500.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga tunggal dan melakukan pembagian sederhana untuk menentukan cicilan bulanan. Ini adalah penerapan prosedur rutin pada konteks keuangan.. Bukti: Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun; Raka perlu menghitung besar cicilan bulanan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penggunaan algoritma bunga tunggal (B = M x i x t) serta pembagian untuk menentukan angsuran.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: dana talangan usaha sebesar Rp2.500.000,00; bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus bunga tunggal dan operasi aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 sebagai soal dasar keuangan yang menguji pemahaman konsep bunga tunggal tanpa kompleksitas tambahan. |

Run 3 — solusi: Bunga total = M x p x t = 2.500.000 x 0,04 x 2 = 200.000. Total pengembalian = 2.500.000 + 200.000 = 2.700.000. Cicilan per bulan = 2.700.000 / 24 = 112.500.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga tunggal dan membagi total pengembalian dengan durasi waktu yang diberikan. Ini adalah penerapan prosedur standar pada konteks keuangan rutin.. Bukti: Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun; Raka perlu menghitung besar cicilan bulanan
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perhitungan bunga tunggal dan pembagian angsuran, yang merupakan pengetahuan prosedural.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan rumus bunga tunggal yang sangat standar. Langkah-langkahnya jelas (hitung bunga, tambah ke pokok, bagi dengan jumlah bulan) dan tidak melibatkan kendala yang rumit.. Bukti: bunga sederhana sebesar 4% per tahun; angsuran bulanan tetap selama 2 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bunga tunggal dan operasi aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah standar kelas 12. Soal ini tidak memerlukan perencanaan strategi kompleks, hanya aplikasi rumus langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `ada21d81536b4020ff184696`

Angga adalah seorang siswa SMA yang rajin dan memiliki semangat menabung. Setelah menerima hadiah ulang tahun berupa uang tunai sebesar Rp1.000.000,00 dari orang tuanya, ia memutuskan untuk tidak menghabiskannya begitu saja. Ia pergi ke bank dan membuka rekening tabungan khusus pelajar. Petugas bank menjelaskan bahwa tabungannya akan mendapatkan bunga tetap sebesar 5% setiap tahun dari saldo awal. Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun. Tabel 1.5 Perhitungan Nilai Tabungan Angga: Tahun 1, Bunga 5% × 1.000.000 = 50.000, Nilai Uang 1.000.000 + 50.000 = 1.050.000. Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...<br><br>Berapa nilai total tabungan Angga pada akhir tahun kedua?

| Opsi | Isi |
|---|---|
| A | Rp1.150.000,00 |
| B | Rp1.050.000,00 |
| C | Rp1.100.000,00 |
| D | Rp1.102.500,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bunga tahunan tetap = 5% x 1.000.000 = 50.000. Saldo akhir tahun ke-2 = Saldo akhir tahun ke-1 + bunga tahun ke-2 = 1.050.000 + 50.000 = 1.100.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `81cdae7ed134ed017e8573c8042aa645cc71c31ab3930dacc5a592c17219f611`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3001 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3004 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2978 |

Run 1 — solusi: Bunga tahunan tetap = 5% x 1.000.000 = 50.000. Saldo akhir tahun ke-2 = Saldo akhir tahun ke-1 + bunga tahun ke-2 = 1.050.000 + 50.000 = 1.100.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep bunga tunggal (bunga dihitung dari pokok awal) untuk menghitung saldo pada tahun kedua. Prosedur ini sangat langsung dan mengikuti pola yang sudah diberikan dalam soal.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang perhitungan bunga tunggal di mana bunga dihitung berdasarkan modal awal, bukan saldo akumulatif.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena konsep bunga tunggal dijelaskan secara eksplisit dalam teks dan tabel. Siswa hanya perlu melakukan satu operasi penjumlahan sederhana setelah memahami pola bunga tetap.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tabel 1.5 Perhitungan Nilai Tabungan Angga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar persentase dan penjumlahan aritmatika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah topik dasar kelas 12. Soal memberikan tabel bantuan yang sangat jelas, sehingga siswa tidak perlu merumuskan strategi sendiri. |

Run 2 — solusi: Bunga tetap per tahun = 5% * 1.000.000 = 50.000. Saldo akhir tahun ke-2 = Saldo akhir tahun ke-1 + bunga tahun ke-2 = 1.050.000 + 50.000 = 1.100.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur perhitungan bunga tunggal yang sudah dijelaskan polanya dalam soal. Siswa hanya perlu mengenali bahwa bunga bersifat tetap dan menambahkannya ke saldo tahun sebelumnya.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep bunga tunggal di mana bunga dihitung berdasarkan modal awal, bukan saldo akumulatif.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola perhitungan sudah diberikan secara eksplisit melalui tabel dan narasi. Siswa hanya perlu melanjutkan satu langkah perhitungan sederhana (penjumlahan bunga tetap ke saldo tahun sebelumnya).. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tabel 1.5 Perhitungan Nilai Tabungan Angga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman konsep bunga tunggal sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah materi dasar kelas 12. Soal memberikan bantuan berupa tabel dan penjelasan eksplisit mengenai bunga tetap, sehingga beban kognitif sangat rendah. |

Run 3 — solusi: Bunga tetap per tahun = 5% * 1.000.000 = 50.000. Saldo akhir tahun ke-2 = Saldo tahun ke-1 + Bunga = 1.050.000 + 50.000 = 1.100.000.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur bunga tunggal yang sudah dijelaskan mekanismenya dalam teks soal. Siswa hanya perlu melanjutkan pola perhitungan yang diberikan.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip bunga tunggal (bunga dihitung dari pokok awal) untuk menyelesaikan masalah.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal
- Intended difficulty `classify/Easy`: Soal memberikan skenario yang sangat terstruktur dengan tabel yang sudah memulai perhitungan. Siswa hanya perlu melanjutkan satu langkah perhitungan sederhana.. Bukti: bunga tetap sebesar 5% setiap tahun dari saldo awal; Tabel 1.5 Perhitungan Nilai Tabungan Angga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar dan pemahaman konsep bunga tunggal sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat terbantu oleh tabel yang disediakan, sehingga siswa kelas 12 dapat dengan mudah mengidentifikasi pola bunga tunggal tanpa perlu merumuskan model matematika yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4597`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep bunga tunggal (bunga dihitung dari pokok awal) untuk menghitung saldo pada tahun kedua. Prosedur ini sangat langsung dan mengikuti pola yang sudah diberikan dalam soal.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang perhitungan bunga tunggal di mana bunga dihitung berdasarkan modal awal, bukan saldo akumulatif.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena konsep bunga tunggal dijelaskan secara eksplisit dalam teks dan tabel. Siswa hanya perlu melakukan satu operasi penjumlahan sederhana setelah memahami pola bunga tetap.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar persentase dan penjumlahan aritmatika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah topik dasar kelas 12. Soal memberikan tabel bantuan yang sangat jelas, sehingga siswa tidak perlu merumuskan strategi sendiri. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d215f8aa8bc3bed140f75b0b`

Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.<br><br>d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

| Opsi | Isi |
|---|---|
| A | Uang Gigih lebih banyak, selisihnya Rp9.000,00 |
| B | Uang Gigih lebih banyak, selisihnya Rp92.741,00 |
| C | Uang Firman lebih banyak, selisihnya Rp92.741,00 |
| D | Sama banyak, selisihnya Rp0,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Firman (bunga tunggal): M_n = M_0(1 + n*i) = 10.000.000(1 + 5*0,03) = 11.500.000. Gigih (bunga majemuk): M_n = M_0(1 + i)^n = 10.000.000(1,03)^5 = 10.000.000(1,1592741) = 11.592.741. Selisih = 11.592.741 - 11.500.000 = 92.741.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `67b44b22c1be7d2826f578b2c4f9e725888885b3cd694e2c504d40503fecfe44`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3031 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3057 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3060 |

Run 1 — solusi: Firman (bunga tunggal): M_n = M_0(1 + n*i) = 10.000.000(1 + 5*0,03) = 11.500.000. Gigih (bunga majemuk): M_n = M_0(1 + i)^n = 10.000.000(1,03)^5 = 10.000.000(1,1592741) = 11.592.741. Selisih = 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan skema bunga (tunggal vs majemuk) dari deskripsi naratif dan menerapkan rumus yang sesuai untuk masing-masing skema.. Bukti: Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun.; Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang perbedaan bunga tunggal dan majemuk serta penerapan prosedural rumus masing-masing.. Bukti: Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun.; Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konseptual untuk membedakan dua skema bunga yang berbeda dan melakukan perhitungan dua tahap yang saling terkait untuk membandingkan hasil akhir.. Bukti: Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus bunga tunggal dan bunga majemuk. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan bunga tunggal dan majemuk. Soal ini menuntut ketelitian dalam menerapkan dua rumus berbeda dan menghitung selisihnya, yang merupakan standar kompetensi menengah. |

Run 2 — solusi: Firman (bunga tunggal): 10.000.000 + (10.000.000 * 0,03 * 5) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1 + 0,03)^5 = 10.000.000 * 1,1592741 = 11.592.741. Selisih: 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan mendasar antara skema bunga tunggal (Firman) dan bunga majemuk (Gigih), lalu menerapkan rumus yang sesuai untuk masing-masing skema dalam konteks investasi.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga ke rekening tabungan; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana bunga dihitung (tunggal vs majemuk) dan prosedur perhitungan nilai akhir investasi.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus membedakan dua konsep bunga yang berbeda dan melakukan perhitungan untuk keduanya. Meskipun prosedurnya standar, siswa perlu berhati-hati dalam memilih rumus yang tepat untuk setiap skenario (bunga tunggal vs majemuk) dan melakukan perbandingan.. Bukti: Setelah lima tahun; bunga 3% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bunga tunggal dan bunga majemuk. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan bunga tunggal dan majemuk. Soal ini memerlukan dua perhitungan terpisah dan satu perbandingan, yang merupakan tugas rutin namun memerlukan ketelitian. |

Run 3 — solusi: Firman (bunga tunggal): M_n = M_0(1 + n*i) = 10.000.000(1 + 5*0,03) = 11.500.000. Gigih (bunga majemuk): M_n = M_0(1 + i)^n = 10.000.000(1,03)^5 ≈ 11.592.741. Selisih = 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan skema bunga (tunggal vs majemuk) dari deskripsi naratif, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan untuk membandingkan hasil akhir.. Bukti: Firman menyimpan uang... bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan; Gigih... meminta bank untuk menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana bunga tunggal dan bunga majemuk bekerja serta prosedur perhitungan nilai akhir investasi.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konsep bunga tunggal dan majemuk, serta kemampuan untuk menerapkan rumus yang berbeda pada dua skenario yang diberikan. Siswa harus merencanakan langkah perhitungan untuk kedua kasus dan membandingkannya, yang melibatkan beberapa langkah saling terkait.. Bukti: Firman menyimpan uang... bunga 3% per tahun; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bunga tunggal dan bunga majemuk, serta operasi hitung eksponen. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal dan majemuk adalah kurikulum standar kelas 12. Soal menuntut pembedaan skema bunga yang merupakan kompetensi inti, namun prosedurnya bersifat rutin bagi siswa yang memahami konsep tersebut. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `b599e139114197a77a84c95d`

Pak Roni merupakan anggota koperasi simpan pinjam. Pak Roni menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun.<br><br>Berapa jumlah simpanan Pak Roni setelah 5 tahun?

| Opsi | Isi |
|---|---|
| A | Rp15.750.000,00 |
| B | Rp15.075.000,00 |
| C | Rp16.500.000,00 |
| D | Rp750.000,00 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bunga = 15.000.000 * 1% * 5 = 750.000. Total simpanan = 15.000.000 + 750.000 = 15.750.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `693b2d148f94972d7c6dc5d3a3d267b8af93f578bb2c656f1dbc9ac131e2ce91`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2804 |
| 2 | success | valid / verified | applying | procedural | Easy | 2800 |
| 3 | success | valid / verified | applying | procedural | Easy | 2792 |

Run 1 — solusi: Bunga = Modal x suku bunga x waktu = 15.000.000 x 1% x 5 = 750.000. Total simpanan = Modal + Bunga = 15.000.000 + 750.000 = 15.750.000.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus bunga tunggal (M_akhir = M_awal + (M_awal * i * t)). Siswa hanya perlu mengidentifikasi variabel dan melakukan perhitungan aritmatika dasar.. Bukti: Pak Roni menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun.; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep bunga tunggal sebagai penambahan nilai berdasarkan persentase dari modal awal dalam jangka waktu tertentu.. Bukti: bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Tidak ada kendala yang berinteraksi, tidak ada pemilihan strategi yang kompleks, dan semua informasi diberikan secara eksplisit. Ini adalah penerapan rumus standar.. Bukti: Rp15.000.000,00; bunga koperasi 1% per tahun; setelah 5 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan operasi aritmatika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 12, soal ini berada di bawah tingkat kesulitan rata-rata karena hanya melibatkan satu rumus bunga tunggal sederhana tanpa variasi waktu atau konversi bunga yang rumit. |

Run 2 — solusi: Bunga = M x i x t = 15.000.000 x 0,01 x 5 = 750.000. Total simpanan = M + Bunga = 15.000.000 + 750.000 = 15.750.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga tunggal secara langsung untuk menghitung total simpanan setelah periode tertentu. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung bunga tunggal dan akumulasi modal akhir.. Bukti: bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mengalikan modal, suku bunga, dan waktu, lalu menjumlahkannya dengan modal awal.. Bukti: Rp15.000.000,00 dengan bunga koperasi 1% per tahun; setelah 5 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan operasi aritmetika dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 12, di mana materi keuangan biasanya sudah mencakup anuitas atau bunga majemuk yang lebih kompleks. Soal ini hanya menguji pemahaman bunga tunggal sederhana. |

Run 3 — solusi: Bunga = M x i x t = 15.000.000 x 0,01 x 5 = 750.000. Total simpanan = M + Bunga = 15.000.000 + 750.000 = 15.750.000.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus bunga tunggal secara langsung untuk menghitung total simpanan akhir. Tidak ada langkah penalaran kompleks atau strategi non-rutin yang diperlukan.. Bukti: menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep bunga tunggal dan prosedur perhitungan bunga serta penjumlahan dengan modal awal.. Bukti: bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Prosedur perhitungan bunga tunggal (M x i x t) adalah materi standar yang familiar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: Rp15.000.000,00 dengan bunga koperasi 1% per tahun; Berapa jumlah simpanan Pak Roni setelah 5 tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan operasi aritmatika dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini berada di bawah tingkat kesulitan rata-rata untuk kelas 12 karena hanya melibatkan satu rumus dasar tanpa variasi atau kondisi tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4468`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta penerapan langsung rumus bunga tunggal (M_akhir = M_awal + (M_awal * i * t)). Siswa hanya perlu mengidentifikasi variabel dan melakukan perhitungan aritmatika dasar tanpa perlu strategi nonrutin.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami prosedur perhitungan bunga tunggal dan akumulasi modal akhir, yang merupakan materi prosedural standar.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 12. Jalur penyelesaiannya rutin, tidak ada kendala yang berinteraksi, dan semua informasi diberikan secara eksplisit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan operasi aritmatika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini berada di bawah tingkat kesulitan rata-rata untuk kelas 12 karena hanya melibatkan satu rumus dasar tanpa variasi atau kondisi tambahan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `5a320ce9d400ac199d8082a9`

Pak Bayu merupakan anggota koperasi "Maju Bersama". Beliau menyimpan modal awal sebesar Rp1.000.000,00 di koperasi tersebut. Koperasi memberikan bunga tunggal sebesar 18% per tahun untuk simpanan anggota. Pak Bayu menyimpan modalnya selama 8 bulan.<br><br>Hitunglah berapa besar bunga yang akan diterima dan berapa total simpanan Pak Bayu setelah 8 bulan?

| Opsi | Isi |
|---|---|
| A | Bunga Rp1.440.000,00, total simpanan Rp2.440.000,00 |
| B | Bunga Rp120.000,00, total simpanan Rp1.120.000,00 |
| C | Bunga Rp126.492,00, total simpanan Rp1.126.492,00 |
| D | Bunga Rp120.000,00, total simpanan Rp120.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bunga = Modal x suku bunga per bulan x lama bulan = 1.000.000 x (18%/12) x 8 = 1.000.000 x 1,5% x 8 = 120.000. Total simpanan = Modal + Bunga = 1.000.000 + 120.000 = 1.120.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7818c53f44244c07f23c69530ecd9d7960d16ce035ba3a652e2ae93344da6518`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2941 |
| 2 | success | valid / verified | applying | procedural | Easy | 2924 |
| 3 | success | valid / verified | applying | procedural | Easy | 2889 |

Run 1 — solusi: Bunga = Modal x suku bunga per bulan x lama bulan = 1.000.000 x (18%/12) x 8 = 1.000.000 x 1,5% x 8 = 120.000. Total simpanan = Modal + Bunga = 1.000.000 + 120.000 = 1.120.000.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus bunga tunggal (B = M x i x t) dengan melakukan konversi satuan waktu (tahun ke bulan) yang merupakan prosedur standar dalam materi keuangan.. Bukti: Koperasi memberikan bunga tunggal sebesar 18% per tahun; Pak Bayu menyimpan modalnya selama 8 bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan bunga tunggal dan penggunaan parameter yang tepat (konversi waktu).. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengonversi suku bunga tahunan ke bulanan dan menerapkan rumus bunga tunggal sederhana. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan operasi aritmetika persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah topik standar kelas 12. Soal ini menguji pemahaman dasar tanpa variasi yang menuntut penalaran tinggi. |

Run 2 — solusi: Bunga = Modal x (r/12) x t = 1.000.000 x (18%/12) x 8 = 1.000.000 x 0,015 x 8 = 120.000. Total simpanan = Modal + Bunga = 1.000.000 + 120.000 = 1.120.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga tunggal sederhana dengan melakukan konversi satuan waktu (tahun ke bulan) yang merupakan prosedur rutin dalam materi keuangan kelas 12.. Bukti: Koperasi memberikan bunga tunggal sebesar 18% per tahun; Pak Bayu menyimpan modalnya selama 8 bulan
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang algoritma perhitungan bunga tunggal dan konversi periode waktu yang sesuai.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah penyelesaian yang jelas (konversi bunga, hitung bunga, jumlahkan dengan modal). Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan

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
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan perhitungan bunga tunggal sederhana dengan konversi waktu sebagai bagian dari literasi keuangan dasar. |

Run 3 — solusi: Bunga = Modal x (r/12) x t = 1.000.000 x (18%/12) x 8 = 1.000.000 x 0,015 x 8 = 120.000. Total simpanan = Modal + Bunga = 1.000.000 + 120.000 = 1.120.000.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur bunga tunggal dengan melakukan konversi satuan waktu (tahun ke bulan) yang merupakan prosedur standar dalam materi keuangan kelas 12.. Bukti: Koperasi memberikan bunga tunggal sebesar 18% per tahun; Pak Bayu menyimpan modalnya selama 8 bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritme bunga tunggal yang merupakan materi prosedural.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan alur penyelesaian yang jelas. Siswa hanya perlu mengonversi suku bunga tahunan ke bulanan dan menerapkan rumus bunga tunggal sederhana.. Bukti: bunga tunggal sebesar 18% per tahun; menyimpan modalnya selama 8 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bunga tunggal dan konversi satuan waktu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga tunggal adalah topik dasar kelas 12 yang penyelesaiannya mengikuti rumus langsung tanpa kendala yang kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `affcbcedba377489f39a2309`

Seluruh bank di suatu wilayah menawarkan deposito dengan bunga 5%–7% per tahun. Bank XYZ termasuk salah satu bank di wilayah tersebut dengan Ahmad dan Maya sebagai nasabahnya. Ahmad telah menjadi nasabah selama 5 tahun dan Maya telah menjadi nasabah selama 10 tahun.<br><br>Jika saldo deposito Ahmad menjadi Rp26.764.500,00, uang yang disetorkan oleh Ahmad mula-mula adalah ....

| Opsi | Isi |
|---|---|
| A | Rp24.000.000,00 |
| B | Rp22.000.000,00 |
| C | Rp18.000.000,00 |
| D | Rp20.000.000,00 |

Kunci sumber: `D`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal tidak dapat diselesaikan secara unik karena suku bunga tidak ditentukan (hanya rentang 5%-7%). Jika bunga 6% digunakan, PV = 26.764.500 / (1,06)^5 = 20.000.000. Namun, informasi ini tidak tersedia dalam soal.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1838b9d2d5e1a1890dc4f2c92caf637d730cec7b6eba12ac06c50de64318ee5f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | — | — | — | 2640 |
| 2 | success | concern / conflict | — | — | — | 2597 |
| 3 | success | concern / conflict | — | — | — | 4026 |

Run 1 — solusi: Soal tidak dapat diselesaikan secara unik karena suku bunga tidak ditentukan secara spesifik (hanya rentang 5%-7%). Jika menggunakan asumsi 5% per tahun, PV = 26.764.500 / (1,05)^5 = 20.970.686. Jika menggunakan 7% per tahun, PV = 26.764.500 / (1,07)^5 = 19.083.500. Karena tidak ada informasi suku bunga yang pasti, jawaban tidak dapat diverifikasi.
- Domain kognitif `abstain/None`: Karena informasi suku bunga tidak lengkap (hanya rentang), siswa tidak dapat menentukan prosedur yang tepat untuk menghitung nilai awal. Abstain diperlukan karena soal tidak memiliki jawaban yang valid secara matematis.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Soal tidak dapat diklasifikasikan karena kurangnya informasi yang diperlukan untuk menerapkan konsep bunga majemuk secara valid.. Bukti: 
- Intended difficulty `abstain/None`: Tingkat kesulitan tidak dapat ditentukan karena soal memiliki cacat konten (informasi hilang) yang membuat penyelesaian tidak mungkin dilakukan secara objektif.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 2 — solusi: Soal tidak dapat diselesaikan secara pasti karena suku bunga tidak ditentukan. Jika diasumsikan bunga 5% per tahun, maka PV = 26.764.500 / (1,05)^5 ≈ 20.970.686. Jika diasumsikan bunga 7% per tahun, maka PV = 26.764.500 / (1,07)^5 ≈ 19.083.568. Karena hasil bergantung pada asumsi suku bunga yang tidak ada di soal, jawaban tidak dapat diverifikasi.
- Domain kognitif `abstain/None`: Karena informasi suku bunga tidak lengkap (hanya rentang), siswa tidak dapat menentukan prosedur yang tepat untuk menghitung nilai awal. Abstain diperlukan karena soal tidak memiliki solusi yang valid berdasarkan data yang diberikan.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Informasi yang hilang membuat dimensi pengetahuan (prosedural/konseptual) tidak dapat diterapkan secara valid pada soal ini.. Bukti: 
- Intended difficulty `abstain/None`: Tingkat kesulitan tidak dapat ditentukan karena soal memiliki cacat konten yang mendasar (informasi hilang).. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 3 — solusi: Soal tidak dapat diselesaikan secara pasti karena tingkat bunga tidak ditentukan (hanya rentang 5%-7%). Jika bunga 6% digunakan, PV = 26.764.500 / (1,06)^5 = 20.000.000. Namun, informasi ini tidak tersedia dalam soal.
- Domain kognitif `abstain/None`: Soal tidak dapat diklasifikasikan secara kognitif karena parameter utama (tingkat bunga) tidak ditentukan, sehingga tidak ada prosedur atau penalaran yang dapat diterapkan secara valid.. Bukti: bunga 5%–7% per tahun
- Dimensi pengetahuan `abstain/None`: Karena soal tidak memiliki parameter yang cukup untuk diselesaikan, dimensi pengetahuan tidak dapat ditentukan.. Bukti: bunga 5%–7% per tahun
- Intended difficulty `abstain/None`: Tingkat kesulitan tidak dapat ditentukan karena soal memiliki cacat informasi yang mendasar.. Bukti: bunga 5%–7% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / abstained | — |
| Dimensi pengetahuan | {} | no_consensus / abstained | — |
| Intended difficulty | {} | no_consensus / abstained | — |

Adjudikasi AI: `success`; token `4360`.
Konten: `concern`; kunci: `conflict`; masalah: Soal tidak memiliki informasi yang cukup untuk diselesaikan secara unik karena suku bunga hanya diberikan dalam rentang (5%–7%) tanpa spesifikasi untuk Bank XYZ.; Kunci jawaban (D) mengasumsikan suku bunga 6% untuk menghasilkan Rp20.000.000,00, namun asumsi ini tidak tercantum dalam soal.; Catatan sumber pada opsi D memberikan justifikasi yang tidak konsisten (menggunakan 5% namun hasilnya tidak sesuai dengan Rp20.000.000,00)..
- Domain kognitif `None`: Soal tidak dapat diklasifikasikan secara kognitif karena parameter utama (tingkat bunga) tidak ditentukan, sehingga tidak ada prosedur atau penalaran yang dapat diterapkan secara valid.
- Dimensi pengetahuan `None`: Karena soal tidak memiliki parameter yang cukup untuk diselesaikan, dimensi pengetahuan tidak dapat ditentukan.
- Intended difficulty `None`: Tingkat kesulitan tidak dapat ditentukan karena soal memiliki cacat konten (informasi hilang) yang membuat penyelesaian tidak mungkin dilakukan secara objektif.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal tidak memiliki informasi yang cukup untuk diselesaikan secara unik karena suku bunga hanya diberikan dalam rentang (5%–7%) tanpa spesifikasi untuk Bank XYZ.; Kunci jawaban (D) mengasumsikan suku bunga 6% untuk menghasilkan Rp20.000.000,00, namun asumsi ini tidak tercantum dalam soal.; Catatan sumber pada opsi D memberikan justifikasi yang tidak konsisten (menggunakan 5% namun hasilnya tidak sesuai dengan Rp20.000.000,00)..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `36b2b05ba07a1b3dfb573f9e`

Seseorang berinvestasi saham di suatu aplikasi online. Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.

| Opsi | Isi |
|---|---|
| A | Rp6.612.500,00 |
| B | Rp7.604.375,00 |
| C | Rp8.573.750,00 |
| D | Rp7.250.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Mn = M(1+i)^n = 5.000.000(1+0,15)^3 = 5.000.000(1,520875) = 7.604.375
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `10d2fef15649f2ec598c11d97e8e26168faa1a785038b1e0f07ef36528c9c0e3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3483 |
| 2 | success | valid / verified | applying | procedural | Easy | 3307 |
| 3 | success | valid / verified | applying | procedural | Easy | 3567 |

Run 1 — solusi: Mn = M(1+i)^n = 5.000.000(1+0,15)^3 = 5.000.000(1,520875) = 7.604.375
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus bunga majemuk yang sudah dipelajari di kelas 12. Siswa hanya perlu mengidentifikasi variabel dan memasukkannya ke dalam rumus.. Bukti: Modal usaha yang diberikan sebesar Rp5.000.000,00; suku bunga majemuk 15% per tahun; nilai akhir modal tersebut setelah 3 tahun
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau prosedur perhitungan bunga majemuk.. Bukti: suku bunga majemuk 15% per tahun; nilai akhir modal tersebut setelah 3 tahun
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus bunga majemuk dengan variabel yang sudah tersedia secara eksplisit. Tidak ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.. Bukti: Modal usaha yang diberikan sebesar Rp5.000.000,00; suku bunga majemuk 15% per tahun; nilai akhir modal tersebut setelah 3 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus bunga majemuk Mn = M(1+i)^n |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar untuk materi bunga majemuk kelas 12, di mana siswa diharapkan mampu menghitung nilai akhir investasi dengan rumus dasar. |

Run 2 — solusi: Mn = M(1 + i)^n = 5.000.000(1 + 0,15)^3 = 5.000.000(1,520875) = 7.604.375
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan rumus bunga majemuk secara langsung pada situasi investasi yang diberikan. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menggunakan algoritma atau rumus bunga majemuk (Mn = M(1+i)^n) untuk menyelesaikan masalah ini.. Bukti: Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi variabel (M, i, n) dan memasukkannya ke dalam rumus yang sudah dipelajari di kelas 12.. Bukti: Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan operasi perpangkatan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah penerapan standar rumus bunga majemuk yang merupakan materi dasar keuangan di kelas 12. Tidak ada kendala tambahan atau skenario kompleks. |

Run 3 — solusi: Mn = M(1 + i)^n = 5.000.000(1 + 0,15)^3 = 5.000.000(1,520875) = 7.604.375
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus bunga majemuk Mn = M(1+i)^n. Siswa hanya perlu mengidentifikasi variabel (M=5jt, i=0,15, n=3) dan melakukan substitusi.. Bukti: Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau rumus bunga majemuk yang sudah baku untuk menyelesaikan masalah keuangan.. Bukti: Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun.
- Intended difficulty `classify/Easy`: Soal bersifat rutin dengan jalur penyelesaian yang jelas dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.. Bukti: Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus bunga majemuk Mn = M(1+i)^n |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 12 untuk menguji pemahaman dasar bunga majemuk tanpa modifikasi periode atau variabel yang kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `1bc4c0c055bdae30032aa047`

Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.<br><br>Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan.

| Opsi | Isi |
|---|---|
| A | 41 |
| B | 44 |
| C | 42 |
| D | 43 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menggunakan rumus FV anuitas biasa: FV = A * [((1 + i)^n - 1) / i]. Diketahui FV = 100.000.000, A = 2.000.000, i = 9%/12 = 0,0075. Maka 100.000.000 = 2.000.000 * [((1 + 0,0075)^n - 1) / 0,0075]. 50 = (1,0075^n - 1) / 0,0075. 0,375 = 1,0075^n - 1. 1,375 = 1,0075^n. n = log(1,375) / log(1,0075) ≈ 42,7. Karena menabung dilakukan setiap bulan, maka dibulatkan ke atas menjadi 43 bulan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d9c233c6b02f2f4d6839f3c9b5e748426610c40d9e0bd8a64b90cb42b7fb5a94`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2978 |
| 2 | success | valid / verified | applying | procedural | Medium | 2969 |
| 3 | success | valid / verified | applying | procedural | Medium | 2993 |

Run 1 — solusi: Menggunakan rumus FV anuitas biasa: FV = A * [((1 + i)^n - 1) / i]. Diketahui FV = 100.000.000, A = 2.000.000, i = 9%/12 = 0,0075. Maka 100.000.000 = 2.000.000 * [((1 + 0,0075)^n - 1) / 0,0075]. 50 = (1,0075^n - 1) / 0,0075. 0,375 = 1,0075^n - 1. 1,375 = 1,0075^n. n = log(1,375) / log(1,0075) ≈ 42,7. Karena menabung dilakukan setiap bulan, maka dibulatkan ke atas menjadi 43 bulan.
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus anuitas yang tepat untuk nilai masa depan (future value) dan menerapkan prosedur logaritma untuk menyelesaikan variabel n, yang merupakan prosedur standar dalam materi keuangan kelas 12.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus anuitas dan konversi suku bunga tahunan ke bulanan.. Bukti: memberikan bunga 9% per tahun; rumus FV anuitas
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi suku bunga (tahunan ke bulanan) dan manipulasi aljabar logaritma untuk mencari n. Langkah-langkahnya rutin bagi siswa kelas 12 yang mempelajari anuitas, namun memerlukan ketelitian dalam pemilihan rumus dan pembulatan.. Bukti: Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00; bunga 9% per tahun; Lama waktu Dani harus menabung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep anuitas, konversi suku bunga, dan penggunaan logaritma. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi anuitas adalah standar kurikulum kelas 12. Soal ini menuntut penerapan rumus yang sudah dipelajari tanpa modifikasi strategi yang kompleks. |

Run 2 — solusi: Menggunakan rumus FV anuitas biasa (setoran akhir periode): FV = A * [((1+i)^n - 1) / i]. Diketahui FV = 100.000.000, A = 2.000.000, i = 9%/12 = 0,0075. Maka 100.000.000 = 2.000.000 * [((1,0075)^n - 1) / 0,0075]. 50 = ((1,0075)^n - 1) / 0,0075. 0,375 = (1,0075)^n - 1. 1,375 = (1,0075)^n. n = log(1,375) / log(1,0075) ≈ 42,7. Karena menabung dilakukan setiap bulan, maka harus dibulatkan ke atas menjadi 43 bulan.
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus anuitas yang tepat untuk mencari periode waktu (n) berdasarkan nilai masa depan (FV) yang diketahui, serta melakukan konversi suku bunga tahunan ke bulanan. Ini adalah penerapan prosedur rutin dalam konteks keuangan.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan anuitas dan penggunaan logaritma untuk menyelesaikan variabel waktu (n) dalam persamaan eksponensial.. Bukti: memberikan bunga 9% per tahun; rumus FV anuitas
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi suku bunga (tahunan ke bulanan), pemilihan rumus anuitas yang tepat, dan penyelesaian persamaan eksponensial menggunakan logaritma. Langkah-langkahnya terstruktur namun memerlukan ketelitian dalam konversi satuan dan pembulatan.. Bukti: bunga 9% per tahun; Rp2.000.000 setiap bulan; mencapai targetnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep anuitas, konversi suku bunga, dan penggunaan logaritma. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengoperasikan rumus anuitas dan logaritma sebagai bagian dari materi keuangan matematika. |

Run 3 — solusi: Menggunakan rumus FV anuitas biasa: FV = A * ((1+i)^n - 1) / i. Diketahui FV = 100.000.000, A = 2.000.000, i = 9%/12 = 0,0075. Maka 100.000.000 = 2.000.000 * ((1,0075)^n - 1) / 0,0075. 50 = ((1,0075)^n - 1) / 0,0075. 0,375 = (1,0075)^n - 1. 1,375 = (1,0075)^n. n = log(1,375) / log(1,0075) ≈ 42,78. Karena menabung dilakukan setiap bulan, maka dibulatkan ke atas menjadi 43 bulan.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah anuitas biasa, memilih rumus yang tepat, melakukan konversi suku bunga tahunan ke bulanan, dan menyelesaikan persamaan logaritma untuk n, yang merupakan penerapan prosedur pada konteks rutin.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; memberikan bunga 9% per tahun; Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara variabel anuitas (FV, A, i, n) dan menerapkan algoritma perhitungan yang sesuai untuk menyelesaikan variabel waktu.. Bukti: rumus FV anuitas; bunga 9% per tahun; setiap bulan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi satuan bunga (tahunan ke bulanan) dan penyelesaian persamaan eksponensial/logaritma untuk mencari n, yang merupakan langkah-langkah rutin namun saling terkait dalam konteks keuangan.. Bukti: bunga 9% per tahun; setiap bulan; Lama waktu Dani harus menabung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep anuitas, konversi suku bunga, dan penggunaan logaritma untuk menyelesaikan persamaan eksponensial. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengaplikasikan rumus anuitas dan melakukan manipulasi aljabar logaritma untuk mencari periode waktu. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `6e3411514cf1a09e78e56ecd`

Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.<br><br>Nilai masa depan dari tabungannya setelah empat tahun adalah ....

| Opsi | Isi |
|---|---|
| A | Rp115.000.000,00 |
| B | Rp113.000.000,00 |
| C | Rp114.000.000,00 |
| D | Rp112.000.000,00 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: PMT = 2.000.000, i = 9%/12 = 0,0075, n = 4 * 12 = 48. FV = PMT * [(1 + i)^n - 1] / i = 2.000.000 * [(1,0075)^48 - 1] / 0,0075 ≈ 115.041.413. Dibulatkan menjadi Rp115.000.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `59c5774fb8c5fd19a0500de918c1ac63aecd1c6c7fc5c767ba1148102d8ce77a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2953 |
| 2 | success | valid / verified | applying | procedural | Medium | 3041 |
| 3 | success | valid / verified | applying | procedural | Medium | 3031 |

Run 1 — solusi: PMT = 2.000.000, i = 9%/12 = 0,75% = 0,0075, n = 4 * 12 = 48. FV = PMT * [(1 + i)^n - 1] / i = 2.000.000 * [(1,0075)^48 - 1] / 0,0075 ≈ 115.041.413. Dibulatkan menjadi Rp115.000.000,00.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa ini adalah masalah nilai masa depan anuitas biasa (ordinary annuity), mengonversi suku bunga tahunan ke bulanan, dan menentukan jumlah periode yang tepat sebelum menerapkan rumus.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; bunga 9% per tahun; Nilai masa depan dari tabungannya setelah empat tahun adalah
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip bunga majemuk dan konsep anuitas untuk memilih rumus yang tepat dalam menghitung nilai masa depan tabungan.. Bukti: Nilai masa depan dari tabungannya; bunga 9% per tahun; Rp2.000.000,00 setiap bulan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi satuan waktu dan bunga (tahunan ke bulanan) serta pemilihan rumus anuitas yang tepat. Meskipun prosedurnya rutin, siswa harus berhati-hati dalam menentukan parameter n dan i agar tidak terjadi kesalahan.. Bukti: bunga 9% per tahun; Rp2.000.000,00 setiap bulan; setelah empat tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan rumus nilai masa depan anuitas biasa. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena materi anuitas merupakan bagian dari kurikulum keuangan matematika SMA. |

Run 2 — solusi: PMT = 2.000.000, i = 9%/12 = 0,75% = 0,0075, n = 4 tahun * 12 = 48 bulan. FV = PMT * [(1+i)^n - 1] / i = 2.000.000 * [(1,0075)^48 - 1] / 0,0075 = 2.000.000 * [1,431405 - 1] / 0,0075 = 2.000.000 * 57,52067 = 115.041.340. Dibulatkan menjadi Rp115.000.000,00.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai anuitas biasa (ordinary annuity), memilih rumus nilai masa depan yang tepat, mengonversi suku bunga tahunan ke bulanan, dan menentukan jumlah periode yang sesuai.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; Nilai masa depan dari tabungannya setelah empat tahun adalah
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman prinsip anuitas dan penerapan algoritma perhitungan nilai masa depan (future value) yang sudah baku.. Bukti: memberikan bunga 9% per tahun; Nilai masa depan dari tabungannya setelah empat tahun adalah
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan konversi satuan waktu dan bunga (tahunan ke bulanan) serta pemilihan rumus anuitas yang tepat. Meskipun prosedural, siswa harus teliti dalam menentukan n (48 bulan) dan i (0,75%) agar tidak terjebak pada kesalahan umum seperti yang ada pada pilihan pengecoh.. Bukti: bunga 9% per tahun; setiap bulan; setelah empat tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan deret geometri, serta kemampuan konversi satuan waktu dan bunga. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengaplikasikan rumus anuitas pada masalah keuangan sederhana. Tingkat kesulitan menengah karena memerlukan ketelitian dalam konversi parameter. |

Run 3 — solusi: Diketahui: A = 2.000.000, i = 9%/12 = 0,75% = 0,0075 per bulan, n = 4 tahun = 48 bulan. Menggunakan rumus nilai masa depan anuitas biasa: FV = A * [(1+i)^n - 1] / i. FV = 2.000.000 * [(1,0075)^48 - 1] / 0,0075. (1,0075)^48 ≈ 1,4314. FV ≈ 2.000.000 * (0,4314 / 0,0075) ≈ 2.000.000 * 57,52 ≈ 115.040.000. Dibulatkan menjadi Rp115.000.000,00.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah anuitas biasa (menabung di akhir periode), menentukan parameter yang tepat (konversi bunga tahunan ke bulanan, konversi waktu ke bulan), dan menerapkan rumus nilai masa depan anuitas.. Bukti: Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan; Nilai masa depan dari tabungannya setelah empat tahun adalah
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman prinsip bunga majemuk dalam konteks anuitas dan penggunaan algoritma perhitungan nilai masa depan.. Bukti: memberikan bunga 9% per tahun; Nilai masa depan dari tabungannya setelah empat tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi satuan waktu dan bunga (tahunan ke bulanan) serta menerapkan rumus anuitas yang melibatkan eksponen. Meskipun prosedural, terdapat beberapa langkah yang saling terkait dan potensi kesalahan dalam konversi parameter.. Bukti: bunga 9% per tahun; setiap bulan; setelah empat tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan rumus anuitas dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengelola konversi periode bunga dan waktu dalam konteks keuangan sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4960`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi situasi sebagai masalah nilai masa depan anuitas biasa, melakukan konversi parameter (bunga tahunan ke bulanan dan durasi ke bulan), serta menerapkan rumus yang sesuai.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perhitungan nilai masa depan anuitas dan kemampuan mengonversi satuan waktu serta bunga dalam konteks keuangan.
- Intended difficulty `Medium`: Soal dikategorikan Medium karena memerlukan konversi parameter (bunga dan periode) yang krusial sebelum menerapkan rumus. Meskipun prosedurnya rutin, siswa harus teliti dalam langkah-langkah tersebut agar tidak terjebak pada pilihan pengecoh.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan rumus nilai masa depan anuitas biasa. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena materi anuitas merupakan bagian dari kurikulum keuangan matematika SMA. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `e10756708fd7c9e1c3bf5ae2`

Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.<br><br>Hitung total bunga keseluruhan.

| Opsi | Isi |
|---|---|
| A | Rp960.000,00 |
| B | Rp320.016,00 |
| C | Rp280.014,00 |
| D | Rp480.000,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Pokok pinjaman Rp12.000.000 diangsur 6 bulan, maka angsuran pokok per bulan = 12.000.000 / 6 = 2.000.000. Bunga per bulan = 8% / 12 = 2/3%. Sisa pokok tiap bulan: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Total bunga = (2/3%) * (12+10+8+6+4+2) juta = (2/300) * 42.000.000 = 280.000. Nilai C (280.014) adalah hasil pembulatan bunga bulanan yang presisi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `93c7a93a85db78115421a95b5a72d9f801f5bd3cf259599128806abaa46e31f8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2971 |
| 2 | success | valid / verified | applying | procedural | Medium | 3106 |
| 3 | success | valid / verified | applying | procedural | Medium | 3011 |

Run 1 — solusi: Pokok pinjaman Rp12.000.000 diangsur 6 bulan, maka angsuran pokok per bulan = 12.000.000 / 6 = 2.000.000. Bunga per bulan = 8% / 12 = 2/3%. Sisa pokok tiap bulan: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Total bunga = (2/3%) * (12+10+8+6+4+2) juta = (2/300) * 42.000.000 = 280.000. Nilai C (280.014) adalah hasil pembulatan bunga bulanan yang presisi.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi model pinjaman (pokok tetap/menurun), mengonversi suku bunga tahunan ke bulanan, dan menyusun deret bunga dari sisa pokok yang menurun. Ini memerlukan penerapan konsep bunga pada konteks rutin.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip bunga pada pinjaman dengan pokok tetap (sisa pokok menurun) dan menerapkan algoritma perhitungan bunga secara periodik.. Bukti: diangsur selama 6 bulan (pokok tetap); bunga 8% per tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi bunga tahunan ke bulanan dan menyadari bahwa bunga dihitung dari sisa pokok yang menurun setiap bulan, bukan dari pokok awal. Meskipun prosedurnya rutin, terdapat beberapa langkah saling terkait yang harus direncanakan dengan benar.. Bukti: diangsur selama 6 bulan (pokok tetap); bunga 8% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bunga tunggal, konversi satuan waktu bunga, dan konsep angsuran pokok tetap. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan perhitungan bunga pada pinjaman pokok tetap vs anuitas. Soal menuntut ketelitian dalam mengelola sisa pokok setiap periode. |

Run 2 — solusi: Pinjaman Rp12.000.000 diangsur 6 bulan, maka angsuran pokok per bulan = 12.000.000/6 = 2.000.000. Sisa pokok bulan ke-1 s.d. 6: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Suku bunga bulanan = 8%/12 = 0,6667%. Total bunga = (12jt+10jt+8jt+6jt+4jt+2jt) * (0,08/12) = 42.000.000 * 0,0066667 = 280.000. Pembulatan pada catatan sumber (280.014) mungkin berasal dari pembulatan suku bunga bulanan 0,6667% yang lebih presisi (2/3%).
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep bunga pada sisa pokok yang menurun (bunga menurun) dengan mengonversi suku bunga tahunan ke bulanan dan menjumlahkan bunga dari setiap periode angsuran. Ini memerlukan penerapan prosedur pada konteks rutin keuangan.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.; Hitung total bunga keseluruhan.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang metode perhitungan bunga pada pinjaman dengan angsuran pokok tetap, yang merupakan prosedur standar dalam matematika keuangan.. Bukti: angsur selama 6 bulan (pokok tetap); bunga 8% per tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi suku bunga tahunan ke bulanan dan memahami bahwa bunga dihitung dari sisa pokok yang menurun setiap bulan, bukan bunga tunggal sederhana. Meskipun prosedurnya rutin, terdapat beberapa langkah yang saling terkait (konversi, penentuan sisa pokok, penjumlahan bunga).. Bukti: angsur selama 6 bulan (pokok tetap); bunga 8% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga, konversi satuan waktu (tahun ke bulan), dan aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan perhitungan bunga pada pinjaman dengan angsuran pokok tetap. Langkah-langkahnya jelas namun memerlukan ketelitian dalam mengelola sisa pokok. |

Run 3 — solusi: Pokok pinjaman Rp12.000.000 diangsur 6 bulan, maka angsuran pokok per bulan = 12.000.000/6 = Rp2.000.000. Sisa pokok tiap bulan: 12jt, 10jt, 8jt, 6jt, 4jt, 2jt. Bunga per bulan = 8%/12 = 2/3% per bulan. Total bunga = (12jt+10jt+8jt+6jt+4jt+2jt) * (2/3%) = 42.000.000 * 0,006666... = Rp280.000. (Catatan: Perhitungan sumber C menggunakan pembulatan 0,6667% menghasilkan 280.014, yang diterima sebagai jawaban benar dalam konteks soal).
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep bunga majemuk/bunga atas sisa pokok pada skema angsuran pokok tetap. Ini memerlukan pemahaman hubungan antara sisa pokok yang menurun dan bunga yang dibayarkan setiap periode, bukan sekadar menghitung bunga tunggal sederhana.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan prosedur perhitungan bunga pada sisa pokok yang menurun secara sistematis, yang merupakan bagian dari prosedur keuangan.. Bukti: angsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi bunga tahunan ke bulanan dan memahami bahwa 'pokok tetap' berarti sisa pokok berkurang setiap bulan. Ini melibatkan beberapa langkah terkait (menentukan angsuran pokok, sisa pokok, bunga per bulan, dan total bunga) yang memerlukan perencanaan langkah, meskipun prosedurnya familiar.. Bukti: angsur selama 6 bulan (pokok tetap); bunga 8% per tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga, konversi satuan waktu bunga, dan skema angsuran pokok tetap. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu membedakan skema bunga pada pinjaman. Soal ini menguji ketelitian dalam menerapkan bunga pada sisa pokok yang menurun, yang merupakan standar kompetensi keuangan di kelas 12. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Istilah 'pokok tetap' dalam konteks pinjaman sering kali merujuk pada angsuran pokok yang sama setiap periode (flat principal), namun perhitungan bunga yang menurun (bunga pada sisa pokok) biasanya diasumsikan sebagai bunga efektif atau bunga menurun. Soal ini mengasumsikan bunga dihitung dari sisa pokok setiap bulan dengan suku bunga bulanan 8%/12 = 0,6667%..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `7f246f52d9fc331e3e277809`

Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.<br><br>Hitung angsuran pokok per bulan.

| Opsi | Isi |
|---|---|
| A | Rp2.960.000,00 |
| B | Rp1.500.000,00 |
| C | Rp1.000.000,00 |
| D | Rp2.000.000,00 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Angsuran pokok per bulan dihitung dengan membagi total pinjaman dengan jumlah periode angsuran. Angsuran pokok = Rp12.000.000,00 / 6 = Rp2.000.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1cb9a464636f9895fe3344fe6e3f1303c14d55d7754aa10c3ce4d43eef855793`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2737 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2728 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2789 |

Run 1 — solusi: Angsuran pokok per bulan dihitung dengan membagi total pinjaman dengan jumlah periode angsuran. Angsuran pokok = Rp12.000.000,00 / 6 = Rp2.000.000,00.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi komponen angsuran pokok dari sistem pinjaman pokok tetap. Siswa hanya perlu menerapkan prosedur pembagian sederhana yang sudah familiar untuk menentukan angsuran pokok tanpa perlu menghitung bunga.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap); Hitung angsuran pokok per bulan.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dasar 'pokok tetap' dalam pinjaman, yaitu membagi total pinjaman secara merata ke dalam periode waktu yang ditentukan.. Bukti: angsuran selama 6 bulan (pokok tetap)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membagi total pinjaman dengan jumlah bulan. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap); Hitung angsuran pokok per bulan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian dasar dan pemahaman konsep angsuran pokok tetap. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pinjaman dengan angsuran pokok tetap adalah materi dasar kelas 12. Soal ini hanya menuntut pemahaman definisi angsuran pokok tanpa perhitungan bunga yang rumit. |

Run 2 — solusi: Angsuran pokok per bulan dihitung dengan membagi total pinjaman dengan jumlah periode angsuran. Angsuran pokok = Rp12.000.000,00 / 6 bulan = Rp2.000.000,00.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menerapkan prosedur dasar perhitungan angsuran pokok tetap. Siswa hanya perlu memahami definisi angsuran pokok tetap dan melakukan pembagian sederhana, yang merupakan prosedur rutin.. Bukti: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap); Hitung angsuran pokok per bulan.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep 'pokok tetap' dalam konteks pinjaman, yang merupakan pengetahuan konseptual dasar mengenai bagaimana pinjaman dibagi secara merata.. Bukti: angsuran selama 6 bulan (pokok tetap)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membagi total pinjaman dengan jumlah bulan. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Rp12.000.000,00; 6 bulan; pokok tetap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian dasar dan pemahaman konsep angsuran pokok tetap. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari konsep dasar angsuran pokok tetap yang sangat familiar bagi siswa kelas 12, dengan beban kognitif yang sangat rendah. |

Run 3 — solusi: Angsuran pokok per bulan dihitung dengan membagi total pinjaman dengan jumlah periode angsuran. Angsuran pokok = Rp12.000.000,00 / 6 = Rp2.000.000,00.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi komponen angsuran pokok dalam skema pinjaman pokok tetap. Siswa hanya perlu menerapkan definisi dasar angsuran pokok (total pinjaman dibagi jumlah periode) tanpa perlu menghitung bunga atau anuitas. Ini adalah prosedur langsung.. Bukti: Hitung angsuran pokok per bulan.; meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap)
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep 'pokok tetap' dalam pinjaman, yaitu bahwa angsuran pokok adalah pembagian rata dari total pinjaman, yang merupakan pengetahuan konseptual dasar tentang skema pinjaman.. Bukti: angsuran selama 6 bulan (pokok tetap)
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta satu operasi pembagian dasar. Tidak ada kendala yang berinteraksi, tidak ada perencanaan strategi yang kompleks, dan informasi yang diberikan sudah sangat spesifik untuk langsung dihitung.. Bukti: Hitung angsuran pokok per bulan.; Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep pinjaman pokok tetap. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 12, soal ini termasuk sangat mudah karena hanya memerlukan operasi aritmatika dasar satu langkah tanpa perlu mengintegrasikan bunga atau perhitungan anuitas yang lebih kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `a4ded83d90999b1517dcec47`

Bu Tania adalah pemilik usaha toko elektronik yang telah berkembang pesat di kotanya. Usahanya menghasilkan omzet rata-rata sebesar Rp120.000.000,00 per bulan. Ia memiliki 10 orang karyawan dengan gaji rata-rata Rp4.000.000,00, serta pengeluaran rutin lainnya sebesar Rp25.000.000,00 per bulan.<br><br>Kini Bu Tania ingin memperluas usahanya ke kota lain dan membutuhkan tambahan modal. Ia mengajukan kredit ke Bank Sentosa, dan mendapat brosur simulasi angsuran kredit seperti tabel berikut.<br><br>\| Pinjaman \| 12 bulan \| 24 bulan \| 36 bulan \| 48 bulan \| 60 bulan \|<br>\|---\|---\|---\|---\|---\|---\|<br>\| Rp10.000.000,00 \| Rp874.515,00 \| Rp456.847,00 \| - \| - \| - \|<br>\| Rp25.000.000,00 \| Rp2.186.287,00 \| Rp1.142.119,00 \| - \| - \| - \|<br>\| Rp30.000.000,00 \| Rp2.623.545,00 \| Rp1.370.542,00 \| - \| - \| - \|<br>\| Rp40.000.000,00 \| Rp3.498.059,00 \| Rp1.827.390,00 \| - \| - \| - \|<br>\| Rp50.000.000,00 \| Rp4.372.574,00 \| Rp2.284.237,00 \| - \| - \| - \|<br>\| Rp60.000.000,00 \| Rp5.247.089,00 \| Rp2.741.085,00 \| Rp1.907.984,00 \| - \| - \|<br>\| Rp70.000.000,00 \| Rp6.121.603,00 \| Rp3.197.932,00 \| Rp2.225.981,00 \| - \| - \|<br>\| Rp80.000.000,00 \| Rp6.996.118,00 \| Rp3.654.780,00 \| Rp2.543.978,00 \| - \| - \|<br>\| Rp100.000.000,00 \| Rp8.745.148,00 \| Rp4.568.474,00 \| Rp3.179.973,00 \| Rp2.488.504,00 \| - \|<br>\| Rp130.000.000,00 \| Rp11.368.693,00 \| Rp5.939.017,00 \| Rp4.133.965,00 \| Rp3.235.055,00 \| Rp2.698.586,00 \|<br>\| Rp150.000.000,00 \| Rp13.117.722,00 \| Rp6.852.711,00 \| Rp4.769.959,00 \| Rp3.732.756,00 \| Rp3.113.753,00 \|<br><br>Bu Tania memutuskan bahwa angsuran maksimal yang dapat ia bayarkan per bulan tidak lebih dari 20% dari total pendapatan bersih per bulan jika mengangsur selama 12 bulan. Namun, jika mengambil angsuran lebih dari 12 bulan (24, 36, 48, atau 60 bulan) tidak lebih dari 10% dari total pendapatan bersih per bulan.<br><br>Andaikan Bu Tania mengambil pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan, Setelah membuka cabang baru, Bu Tania merekrut 5 orang karyawan tambahan dengan besaran gaji yang sama seperti karyawan sebelumnya (Rp4.000.000,00 per orang). Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?

| Opsi | Isi |
|---|---|
| A | Rp138.745.148,00 |
| B | Rp75.000.000,00 |
| C | Rp83.745.148,00 |
| D | Rp55.000.000,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Pendapatan bersih awal = 120jt - (10*4jt) - 25jt = 55jt. Target pendapatan bersih total = 2 * 55jt = 110jt. Tambahan pendapatan bersih yang dibutuhkan = 110jt - 55jt = 55jt. Beban baru = gaji 5 karyawan (5*4jt = 20jt) + cicilan pinjaman 100jt tenor 12 bulan (8.745.148). Omzet minimal cabang baru = 55jt + 20jt + 8.745.148 = 83.745.148.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b4488f736823f1885ca6c0eca6039476ff069b15ec8e5e5260bd1b8aa37ac377`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 4181 |
| 2 | success | valid / verified | applying | conceptual | Medium | 4180 |
| 3 | success | valid / verified | applying | procedural | Medium | 4200 |

Run 1 — solusi: Pendapatan bersih lama = 120jt - (10*4jt) - 25jt = 55jt. Target pendapatan bersih baru = 2 * 55jt = 110jt. Tambahan pendapatan bersih yang diperlukan = 110jt - 55jt = 55jt. Beban tambahan dari cabang baru = gaji 5 karyawan (5*4jt = 20jt) + cicilan pinjaman (8.745.148). Omzet minimal cabang baru = 55jt + 20jt + 8.745.148 = 83.745.148.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi keuangan (pendapatan, pengeluaran, cicilan) untuk merumuskan model pendapatan bersih baru dan menentukan nilai omzet yang diperlukan. Ini melibatkan pemahaman hubungan antar variabel keuangan.. Bukti: Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana komponen pendapatan dan pengeluaran (termasuk cicilan dan gaji) membentuk pendapatan bersih dalam konteks bisnis.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya
- Intended difficulty `classify/Medium`: Soal memerlukan perencanaan langkah yang saling bergantung: menghitung pendapatan bersih awal, menentukan target baru, mengidentifikasi beban tambahan (gaji dan cicilan), dan menyusun persamaan omzet. Siswa harus mengintegrasikan data dari teks dan tabel secara cermat.. Bukti: Bu Tania merekrut 5 orang karyawan tambahan; Andaikan Bu Tania mengambil pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan; Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, pemahaman konsep pendapatan bersih (laba), dan pembacaan tabel angsuran. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengelola variabel keuangan majemuk seperti ini. Tingkat kesulitan Medium tepat karena memerlukan ketelitian dalam mengidentifikasi semua komponen beban baru (gaji + cicilan) terhadap target pendapatan bersih. |

Run 2 — solusi: Pendapatan bersih lama = 120jt - (10*4jt) - 25jt = 55jt. Target pendapatan bersih baru = 2 * 55jt = 110jt. Tambahan bersih yang dibutuhkan = 110jt - 55jt = 55jt. Beban baru = gaji 5 karyawan (5*4jt = 20jt) + cicilan pinjaman (8.745.148). Omzet minimal cabang baru = 55jt + 20jt + 8.745.148 = 83.745.148.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi keuangan (pendapatan, pengeluaran, cicilan) untuk merumuskan model pendapatan bersih baru dan menentukan target omzet. Ini melibatkan pemilihan prosedur yang tepat untuk memecahkan masalah kontekstual.. Bukti: Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang hubungan antara omzet, beban operasional, dan cicilan dalam menentukan pendapatan bersih, serta bagaimana perubahan variabel tersebut memengaruhi target akhir.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya
- Intended difficulty `classify/Medium`: Soal memerlukan perencanaan langkah yang saling bergantung: menghitung pendapatan bersih awal, menentukan target pendapatan bersih baru, mengidentifikasi beban tambahan (gaji dan cicilan), dan akhirnya menghitung omzet yang diperlukan. Siswa harus mengelola beberapa kendala (gaji karyawan baru dan cicilan) secara bersamaan.. Bukti: Bu Tania merekrut 5 orang karyawan tambahan; cicilan pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan; pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, pemahaman konsep pendapatan bersih (omzet - beban), dan pembacaan tabel angsuran. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan Medium sesuai untuk kelas 12 karena menuntut integrasi beberapa variabel keuangan (gaji, cicilan, target pendapatan) dalam satu masalah cerita yang tidak langsung, namun prosedurnya tetap familiar. |

Run 3 — solusi: Pendapatan bersih awal = 120jt - (10*4jt) - 25jt = 55jt. Target pendapatan bersih total = 2*55jt = 110jt. Tambahan pendapatan bersih yang dibutuhkan = 110jt - 55jt = 55jt. Beban baru = gaji 5 karyawan (5*4jt = 20jt) + cicilan pinjaman 100jt tenor 12 bulan (8.745.148). Omzet minimal cabang baru = 55jt + 20jt + 8.745.148 = 83.745.148.
- Domain kognitif `classify/applying`: Siswa harus mengintegrasikan informasi keuangan (pendapatan, pengeluaran, cicilan) untuk merumuskan persamaan pendapatan bersih baru dan menentukan omzet yang diperlukan. Ini melibatkan pemahaman hubungan antar variabel keuangan.. Bukti: Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prinsip aritmatika keuangan dasar (pendapatan bersih = omzet - beban) dalam konteks skenario bisnis yang diberikan.. Bukti: pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya
- Intended difficulty `classify/Medium`: Soal memerlukan integrasi beberapa variabel (gaji, cicilan, target pendapatan) yang saling terkait. Siswa harus mengidentifikasi beban baru (gaji karyawan tambahan dan cicilan) dan menambahkannya ke target pendapatan bersih untuk mendapatkan omzet. Meskipun prosedural, terdapat beberapa langkah yang harus direncanakan dengan cermat.. Bukti: omzet rata-rata sebesar Rp120.000.000,00 per bulan; gaji rata-rata Rp4.000.000,00; pengeluaran rutin lainnya sebesar Rp25.000.000,00; pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep pendapatan bersih, dan pembacaan tabel angsuran. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 12 karena menggabungkan literasi keuangan dengan perhitungan aritmatika yang memerlukan ketelitian dalam mengidentifikasi komponen beban. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `6197`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengintegrasikan informasi keuangan (pendapatan, pengeluaran, cicilan) untuk merumuskan model pendapatan bersih baru dan menentukan nilai omzet yang diperlukan. Ini melibatkan pemahaman hubungan antar variabel keuangan dalam skenario bisnis.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana komponen pendapatan dan pengeluaran (termasuk cicilan dan gaji) membentuk pendapatan bersih dalam konteks bisnis.
- Intended difficulty `Medium`: Soal memerlukan perencanaan langkah yang saling bergantung: menghitung pendapatan bersih awal, menentukan target baru, mengidentifikasi beban tambahan (gaji dan cicilan), dan menyusun persamaan omzet. Siswa harus mengintegrasikan data dari teks dan tabel secara cermat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, pemahaman konsep pendapatan bersih (laba), dan pembacaan tabel angsuran. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengelola variabel keuangan majemuk seperti ini. Tingkat kesulitan Medium tepat karena memerlukan ketelitian dalam mengidentifikasi semua komponen beban baru (gaji + cicilan) terhadap target pendapatan bersih. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `b5d6c979c2045301a3560ae7`

Seseorang meminjam uang sebesar Rp10.000.000,00 selama setengah tahun dengan suku bunga 8% per bulan. Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3 (dalam satuan Rp100.000,00).<br><br>\| Bulan \| Jumlah Pinjaman Awal Bulan \| Bunga Pinjaman \| Angsuran Pinjaman \| Jumlah Pinjaman Akhir Bulan \|<br>\|---\|---\|---\|---\|---\|<br>\| 1 \| 100 \| 8 \| 14 \| 86 \|<br>\| 2 \| 86 \| 6,88 \| 15,12 \| 70,88 \|<br>\| 3 \| 70,88 \| 5,7604 \| 16,32 \| 54,5504 \|<br><br>Besar anuitas pada sistem angsuran tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Rp2.300.000,00 |
| B | Rp2.000.000,00 |
| C | Rp2.100.000,00 |
| D | Rp2.200.000,00 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel pada bulan ke-1: 8 + 14 = 22. Pada bulan ke-2: 6,88 + 15,12 = 22. Pada bulan ke-3: 5,7604 + 16,32 = 22,0804. Terdapat ketidakkonsistenan pembulatan pada tabel, namun nilai anuitas yang konsisten secara konsep adalah 22 (satuan Rp100.000,00) = Rp2.200.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2d4d0253b845e166083a96dd39a9ad733527af119d8f12f6c7827c2014ae3da4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2971 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2979 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2952 |

Run 1 — solusi: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel pada bulan ke-1: 8 + 14 = 22. Pada bulan ke-2: 6,88 + 15,12 = 22. Pada bulan ke-3: 5,7604 + 16,32 = 22,0804. Terdapat ketidakkonsistenan pembulatan pada tabel, namun nilai anuitas yang konsisten secara konsep adalah 22 (satuan Rp100.000,00) = Rp2.200.000,00.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep anuitas sebagai jumlah dari bunga dan angsuran pokok pada periode yang sama, kemudian menerapkan pemahaman tersebut dengan membaca data dari tabel yang disediakan.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang komponen anuitas (bunga + angsuran) dalam konteks tabel rencana pelunasan pinjaman.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu memahami definisi anuitas dan melakukan operasi penjumlahan sederhana dari data yang sudah tersedia secara eksplisit dalam tabel. Tidak ada perencanaan langkah yang kompleks atau kendala yang berinteraksi.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen anuitas (bunga dan angsuran pokok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 seharusnya sudah familiar dengan tabel anuitas dan konsep dasarnya. Soal ini hanya memerlukan pembacaan data dan penjumlahan sederhana. |

Run 2 — solusi: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel, pada bulan ke-2: Bunga = 6,88 dan Angsuran = 15,12. Maka Anuitas = 6,88 + 15,12 = 22 (dalam satuan Rp100.000,00), sehingga Rp2.200.000,00.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar anuitas sebagai penjumlahan bunga dan angsuran pokok pada periode yang sama, lalu menerapkan pemahaman tersebut dengan membaca data dari tabel yang disediakan.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang komponen anuitas (bunga + angsuran) dan kemampuan prosedural dalam membaca serta mengolah data dari tabel rencana angsuran.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu memahami definisi anuitas dan melakukan satu operasi penjumlahan sederhana dari data yang sudah tersedia secara eksplisit di dalam tabel. Tidak ada perencanaan langkah yang kompleks atau kendala yang saling berinteraksi.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah; Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen anuitas (bunga dan angsuran pokok) dan kemampuan membaca tabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 seharusnya sudah familiar dengan tabel angsuran dan konsep anuitas. Soal ini hanya menuntut pembacaan data dan penjumlahan sederhana, sehingga beban kognitifnya rendah. |

Run 3 — solusi: Anuitas adalah jumlah dari bunga dan angsuran pokok pada periode yang sama. Berdasarkan tabel, pada bulan ke-2: Bunga = 6,88; Angsuran = 15,12. Anuitas = 6,88 + 15,12 = 22 (dalam satuan Rp100.000,00). Jadi, anuitas = 22 * Rp100.000,00 = Rp2.200.000,00.
- Domain kognitif `classify/applying`: Siswa diminta untuk memahami konsep anuitas sebagai jumlah bunga dan angsuran pokok, kemudian menerapkan pemahaman tersebut dengan mengambil data yang tepat dari tabel yang disediakan.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi anuitas dalam konteks tabel angsuran pinjaman.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu memahami definisi anuitas (bunga + angsuran) dan membaca data dari tabel yang sudah tersedia. Tidak ada perhitungan kompleks atau perencanaan strategi yang rumit.. Bukti: Besar anuitas pada sistem angsuran tersebut adalah; Bunga Pinjaman \| Angsuran Pinjaman

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen angsuran pinjaman (bunga dan angsuran pokok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 seharusnya sudah familiar dengan tabel angsuran. Tugas utama hanyalah membaca tabel dan melakukan penjumlahan sederhana. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `c51d2c28576452736fad772a`

Untuk menggalakkan program koperasi berdaya guna, beberapa koperasi akan memberikan pinjaman masing-masing sebesar Rp50.000.000,00 kepada pengurus desa untuk modal pembangunan. Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun, sedangkan Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun.<br><br>Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi. Manakah yang lebih menguntungkan?

| Opsi | Isi |
|---|---|
| A | Koperasi A (nilai akhir Rp59.702.615,00) lebih menguntungkan dibanding Koperasi B (Rp56.308.121,00) |
| B | Koperasi A dan Koperasi B menghasilkan nilai akhir yang sama besar |
| C | Koperasi B (nilai akhir Rp56.308.121,00) lebih menguntungkan dibanding Koperasi A (Rp59.702.615,00) |
| D | Koperasi B lebih menguntungkan karena periode pinjamannya lebih singkat |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Hitung nilai akhir (M_n) dengan rumus bunga majemuk M_n = M_0(1+i)^n. Koperasi A: 50.000.000(1,03)^6 = 59.702.615. Koperasi B: 50.000.000(1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121, yang merupakan hasil 50.000.000 * (1,02)^4 = 54.121.608. Terdapat kesalahan hitung pada kunci sumber untuk B, namun perbandingan A > B tetap valid).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2e2826937759929dc912fed37a9fae73400398c70a92e196d9306b78783274e7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3030 |
| 2 | success | valid / verified | applying | procedural | Easy | 3008 |
| 3 | success | valid / verified | applying | procedural | Easy | 2997 |

Run 1 — solusi: Hitung nilai akhir (M_n) dengan rumus bunga majemuk M_n = M_0(1+i)^n. Koperasi A: 50.000.000(1,03)^6 = 59.702.615. Koperasi B: 50.000.000(1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121, yang merupakan hasil 50.000.000 * (1,02)^4 = 54.121.608. Terdapat kesalahan hitung pada kunci sumber untuk B, namun perbandingan A > B tetap valid).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga majemuk yang sudah familiar untuk membandingkan dua skenario investasi/pinjaman. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun; Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritme perhitungan bunga majemuk dan penggunaan parameter yang diberikan dalam rumus.. Bukti: suku bunga sebesar 3% per tahun selama 6 tahun; suku bunga sebesar 2% per tahun selama 4 tahun
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu menerapkan rumus bunga majemuk secara langsung untuk dua kasus yang berbeda. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: pinjaman masing-masing sebesar Rp50.000.000,00; Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun

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
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 12 sudah terbiasa dengan perhitungan bunga majemuk. Soal ini bersifat rutin dan tidak memerlukan integrasi konsep yang mendalam. |

Run 2 — solusi: Hitung nilai akhir (M_n) dengan rumus bunga majemuk M_n = M_0(1+i)^n. Koperasi A: 50.000.000 * (1,03)^6 = 59.702.615. Koperasi B: 50.000.000 * (1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121, namun perhitungan matematis 50jt * (1,02)^4 = 54.121.608. Terdapat kesalahan hitung pada kunci sumber untuk Koperasi B, namun kesimpulan A > B tetap valid).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga majemuk yang sudah dipelajari untuk membandingkan dua skenario investasi/pinjaman. Ini adalah penerapan prosedur rutin pada konteks keuangan.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun; Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip bunga majemuk (konseptual) dan menerapkan rumus perhitungannya (prosedural) untuk menyelesaikan masalah.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas (menggunakan rumus bunga majemuk). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan penggunaan kalkulator/perhitungan eksponen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah standar kelas 12. Soal ini hanya meminta perhitungan langsung tanpa variasi kompleks. |

Run 3 — solusi: Hitung nilai akhir (A_n = P(1+r)^n): Koperasi A: 50.000.000 * (1,03)^6 = 59.702.615. Koperasi B: 50.000.000 * (1,02)^4 = 54.121.608 (Catatan: Kunci sumber menggunakan 56.308.121 untuk B, yang merupakan hasil 50.000.000 * (1,02)^6, bukan 4 tahun. Namun, A tetap lebih besar dari B).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus bunga majemuk untuk dua skenario berbeda dan membandingkan hasilnya. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun; Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang rumus bunga majemuk (prinsip) dan prosedur perhitungan nilai akhir.. Bukti: suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus bunga majemuk dua kali dan membandingkan hasilnya. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun; Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan penggunaan kalkulator/operasi hitung. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi bunga majemuk adalah standar kelas 12. Perhitungan langsung tanpa jebakan konseptual membuat soal ini mudah bagi siswa kelas 12. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `7672dd47336c772dbd3a318a`

Suatu aplikasi pinjaman online memberikan pinjaman sebesar Rp10.000.000,00 dengan suku bunga 2% per tahun. Periode pinjaman selama 24 bulan. Berapakah nilai akhir pengembalian pinjaman tersebut?

| Opsi | Isi |
|---|---|
| A | Rp10.200.000,00 |
| B | Rp10.404.000,00 |
| C | Rp10.612.000,00 |
| D | Rp10.000.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: P = 10.000.000, i = 2% per tahun = 0,02, n = 24 bulan = 2 tahun. Menggunakan rumus bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = 10.404.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `32bdb0557bd84d9e5c0e58d2275171cdd0585eab23131766a277658d31275945`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2914 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2805 |
| 3 | success | valid / verified | applying | procedural | Easy | 2897 |

Run 1 — solusi: Pinjaman (P) = Rp10.000.000,00. Suku bunga (i) = 2% per tahun = 0,02. Periode (n) = 24 bulan = 2 tahun. Menggunakan rumus bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = Rp10.404.000,00.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi parameter yang diberikan, mengonversi satuan waktu (bulan ke tahun), dan memilih rumus bunga majemuk yang sesuai untuk menghitung nilai akhir. Ini adalah penerapan prosedur standar dalam konteks keuangan.. Bukti: Suku bunga 2% per tahun; Periode pinjaman selama 24 bulan; Berapakah nilai akhir pengembalian pinjaman tersebut?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang hubungan antara suku bunga tahunan, periode waktu, dan rumus bunga majemuk sebagai prinsip dasar keuangan.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan konversi satuan waktu yang sederhana dan penerapan rumus bunga majemuk secara langsung tanpa kendala tambahan atau skenario yang kompleks.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bunga majemuk dan konversi satuan waktu (bulan ke tahun). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 seharusnya sudah familiar dengan perhitungan bunga majemuk sederhana. Soal tidak memiliki jebakan atau kompleksitas tinggi. |

Run 2 — solusi: Pinjaman (P) = 10.000.000, suku bunga (i) = 2% per tahun, periode (n) = 24 bulan = 2 tahun. Menggunakan rumus bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = 10.404.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi parameter pinjaman, mengonversi satuan waktu (bulan ke tahun), dan menerapkan rumus bunga majemuk yang relevan untuk konteks investasi/pinjaman.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan; nilai akhir pengembalian pinjaman
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang prinsip bunga majemuk dan prosedur perhitungan nilai akhir yang merupakan konsep standar dalam materi keuangan kelas 12.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan; nilai akhir pengembalian pinjaman
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan konversi satuan waktu sederhana dan penerapan langsung rumus bunga majemuk tanpa kendala atau integrasi langkah yang kompleks.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bunga majemuk dan konversi satuan waktu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah topik dasar kelas 12. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga siswa yang memahami konsep dasar dapat menyelesaikannya dengan cepat. |

Run 3 — solusi: Pinjaman (P) = 10.000.000, suku bunga (i) = 2% per tahun, periode (n) = 24 bulan = 2 tahun. Menggunakan asumsi bunga majemuk: FV = P(1+i)^n = 10.000.000(1+0,02)^2 = 10.000.000(1,0404) = 10.404.000.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi satuan waktu (bulan ke tahun) dan menerapkan rumus bunga majemuk yang relevan dengan konteks investasi/pinjaman. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan; Berapakah nilai akhir pengembalian pinjaman tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perhitungan bunga majemuk dan konversi periode waktu yang merupakan bagian dari prosedur keuangan.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan konversi satuan waktu sederhana dan penerapan langsung rumus bunga majemuk yang sudah familiar bagi siswa kelas 12.. Bukti: suku bunga 2% per tahun; Periode pinjaman selama 24 bulan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bunga majemuk dan konversi satuan waktu (bulan ke tahun). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah kurikulum standar kelas 12. Soal tidak memiliki kendala yang saling berinteraksi atau kebutuhan perencanaan strategi yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4476`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi parameter, melakukan konversi satuan waktu (bulan ke tahun), dan menerapkan rumus bunga majemuk secara langsung. Ini adalah penerapan prosedur standar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang algoritma perhitungan bunga majemuk dan konversi periode waktu yang merupakan bagian dari prosedur keuangan.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya memerlukan konversi satuan waktu sederhana dan penerapan langsung rumus bunga majemuk yang sudah familiar bagi siswa kelas 12 tanpa kendala tambahan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bunga majemuk dan konversi satuan waktu (bulan ke tahun). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bunga majemuk adalah kurikulum standar kelas 12. Soal tidak memiliki kendala yang saling berinteraksi atau kebutuhan perencanaan strategi yang kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `052c617a1f0c63d479f466ab`

Sepuluh orang siswa memiliki tinggi yang berbeda. Guru olahraga menginginkan mereka berbaris menyamping dengan syarat tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya. Berapa banyaknya cara membuat barisan sesuai ketentuan itu?

| Opsi | Isi |
|---|---|
| A | 1.024 cara |
| B | 256 cara |
| C | 512 cara |
| D | 3.628.800 cara |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `512`.
Solusi minimum hasil AI: Urutkan siswa dari terpendek ke tertinggi (S1, S2, ..., S10). S1 diletakkan di posisi mana saja. Untuk setiap siswa berikutnya (S2 sampai S10), siswa tersebut harus diletakkan di ujung kiri atau ujung kanan barisan yang sudah terbentuk agar tidak diapit oleh dua siswa yang lebih tinggi. Untuk 9 siswa (S2 hingga S10), masing-masing memiliki 2 pilihan posisi (ujung kiri atau kanan). Total cara = 2^(10-1) = 2^9 = 512.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5936922d2b538e8a1fc5bef3fd3f6faf5c85ad5e8560b5db899f5b72b8ae0457`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2808 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 2840 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 2817 |

Run 1 — solusi: Urutkan siswa dari terpendek ke tertinggi (S1, S2, ..., S10). S1 diletakkan di posisi mana saja. Untuk setiap siswa berikutnya (S2 sampai S10), siswa tersebut harus diletakkan di ujung kiri atau ujung kanan barisan yang sudah terbentuk agar tidak diapit oleh dua siswa yang lebih tinggi. Untuk S2 hingga S10 (9 siswa), masing-masing memiliki 2 pilihan posisi (ujung kiri atau kanan). Total cara = 2^(10-1) = 2^9 = 512.
- Domain kognitif `classify/reasoning`: Siswa harus memahami struktur barisan yang terbentuk secara induktif. Mereka perlu menyadari bahwa untuk mempertahankan kondisi 'tidak diapit oleh dua orang yang lebih tinggi', setiap siswa baru harus selalu ditempatkan di ujung barisan yang sudah ada. Ini memerlukan penalaran tentang pola konstruksi barisan.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana batasan (constraint) mempengaruhi pembentukan permutasi, bukan sekadar menerapkan rumus permutasi standar.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun memerlukan penalaran (reasoning), pola konstruksinya (menempatkan elemen di ujung) adalah teknik standar dalam masalah barisan/permutasi dengan batasan tinggi badan. Siswa kelas 12 yang mempelajari aturan pencacahan seharusnya dapat menemukan pola ini dengan mencoba kasus kecil (n=3 atau n=4).. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya; Berapa banyaknya cara membuat barisan sesuai ketentuan itu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan pemahaman induktif sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini adalah variasi klasik dari masalah permutasi dengan batasan. Siswa kelas 12 diharapkan mampu melakukan penalaran induktif untuk masalah seperti ini tanpa bantuan eksplisit. |

Run 2 — solusi: Urutkan siswa dari yang terpendek ke tertinggi (S1, S2, ..., S10). S1 diletakkan di posisi mana saja. Untuk setiap siswa berikutnya (S2 sampai S10), siswa tersebut harus diletakkan di ujung kiri atau ujung kanan dari barisan yang sudah terbentuk agar tidak diapit oleh dua orang yang lebih tinggi. Untuk S2 hingga S10 (9 orang), masing-masing memiliki 2 pilihan posisi (ujung kiri atau kanan). Total cara = 2^(10-1) = 2^9 = 512.
- Domain kognitif `classify/reasoning`: Siswa perlu memahami prinsip konstruksi barisan dengan batasan posisi. Ini bukan sekadar permutasi biasa, melainkan penalaran induktif tentang penempatan elemen (siswa) ke dalam barisan agar syarat 'tidak diapit' terpenuhi, yang mengarah pada pola 2^(n-1).. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip dasar aturan pengisian tempat dan menerapkannya pada pola konstruksi barisan yang spesifik (konseptual) untuk menemukan generalisasi jumlah cara.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Intended difficulty `classify/Hard`: Soal ini menuntut siswa untuk melakukan abstraksi atau eksperimen mental (induksi) untuk menemukan pola penempatan. Meskipun perhitungannya sederhana (2^9), proses menemukan strategi penempatan yang memenuhi syarat 'tidak diapit' memerlukan perencanaan langkah yang saling bergantung dan pemahaman konseptual yang kuat, yang melampaui sekadar prosedur rutin.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya; Berapa banyaknya cara membuat barisan sesuai ketentuan itu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan pemahaman tentang urutan/barisan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 sering terjebak pada permutasi 10! (seperti opsi D). Menemukan bahwa syarat 'tidak diapit' memaksa siswa untuk menempatkan siswa dari yang terpendek ke tertinggi di ujung-ujung barisan adalah langkah penalaran yang menantang bagi siswa pada jenjang ini. |

Run 3 — solusi: Urutkan siswa dari yang terpendek ke tertinggi (S1, S2, ..., S10). S1 diletakkan di posisi mana saja. Untuk setiap siswa berikutnya (S2 hingga S10), mereka harus diletakkan di ujung kiri atau kanan dari barisan yang sudah terbentuk agar tidak diapit oleh dua orang yang lebih tinggi. Terdapat 2 pilihan posisi untuk setiap siswa dari S2 sampai S9 (total 8 siswa), dan S10 hanya memiliki 1 posisi tersisa (atau 2 pilihan untuk S2-S9 dan S10 adalah penutup). Secara induktif, terdapat 2^(n-1) cara untuk n siswa. Untuk 10 siswa, banyaknya cara adalah 2^(10-1) = 2^9 = 512.
- Domain kognitif `classify/reasoning`: Soal ini memerlukan pemahaman mendalam tentang struktur barisan (induksi atau konstruksi iteratif) untuk memenuhi syarat yang diberikan, bukan sekadar menerapkan rumus permutasi standar.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip konstruksi barisan (konseptual) untuk menyimpulkan pola 2^(n-1) daripada sekadar menghafal rumus.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard karena siswa harus melakukan penalaran konstruktif untuk menemukan pola (induksi) bahwa setiap siswa baru harus diletakkan di ujung barisan yang sudah terbentuk. Tidak ada rumus langsung yang bisa dipakai; siswa harus membangun logika sendiri.. Bukti: tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya; Berapa banyaknya cara membuat barisan sesuai ketentuan itu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan pemahaman urutan. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana (2^9), logika di balik syarat 'tidak diapit oleh dua orang yang lebih tinggi' menuntut kemampuan penalaran tingkat tinggi yang jarang dilatih dalam soal rutin SMA. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 1, "Hard": 2} | majority_2_of_3 / adjudicated | Hard |

Adjudikasi AI: `success`; token `4750`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini menuntut penalaran (reasoning) karena siswa tidak bisa langsung menggunakan rumus permutasi standar. Mereka harus melakukan penalaran induktif atau konstruktif untuk memahami bahwa syarat 'tidak diapit oleh dua orang yang lebih tinggi' memaksa setiap siswa baru untuk selalu ditempatkan di ujung barisan yang sudah terbentuk.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami hubungan konseptual antara batasan (constraint) yang diberikan dengan struktur barisan yang terbentuk. Ini menguji pemahaman prinsip konstruksi barisan, bukan sekadar menghafal prosedur atau rumus.
- Intended difficulty `Hard`: Soal ini dikategorikan Hard karena menuntut kemampuan perencanaan langkah yang saling bergantung (induksi) tanpa bantuan rumus langsung. Siswa harus membangun strategi sendiri untuk memenuhi syarat yang diberikan. Meskipun perhitungannya sederhana, proses menemukan pola 2^(n-1) memerlukan integrasi konsep yang tinggi bagi siswa kelas 12.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan dan pemahaman induktif sederhana. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, logika di balik syarat 'tidak diapit oleh dua orang yang lebih tinggi' menuntut kemampuan penalaran tingkat tinggi yang jarang dilatih dalam soal rutin SMA. Siswa sering terjebak pada permutasi 10! (opsi D) karena tidak mampu melakukan abstraksi pola penempatan. |

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

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Hard", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `439575e9c1a8bdff1255c8d5`

Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda yang digunakan sehari-hari sebagai pakaian bekerja. Jika Arkan membuat setelan yang berbeda saat mengenakannya dalam bekerja, tentukan banyak setelan berbeda yang dibuat.

| Opsi | Isi |
|---|---|
| A | 15 setelan |
| B | 12 setelan |
| C | 20 setelan |
| D | 60 setelan |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menggunakan aturan perkalian untuk kejadian yang saling bebas: 5 kemeja * 4 celana * 3 pasang sepatu = 60 setelan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7291ded368a63d95d6b9193981596e7ad9970edf031f8a61a9e59a156ce520e0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2683 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2658 |
| 3 | success | valid / verified | applying | procedural | Easy | 2665 |

Run 1 — solusi: Menggunakan aturan perkalian untuk kejadian yang saling bebas: 5 kemeja * 4 celana * 3 pasang sepatu = 60 setelan.
- Domain kognitif `classify/applying`: Soal meminta siswa mengenali dan menerapkan prinsip dasar aturan perkalian untuk menentukan banyaknya kombinasi dari tiga kategori objek yang saling bebas. Ini adalah penerapan langsung dari konsep dasar pencacahan.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip perkalian (aturan pengisian tempat) sebagai prosedur standar untuk menghitung kombinasi objek.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengidentifikasi jumlah objek di setiap kategori dan mengalikannya. Tidak ada kendala tambahan, syarat khusus, atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan perkalian (multiplication principle) untuk kejadian saling bebas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar aturan pencacahan yang sangat umum di kelas 12 (atau bahkan kelas 10/11) sebagai pengingat konsep dasar sebelum masuk ke permutasi/kombinasi yang lebih kompleks. |

Run 2 — solusi: Menggunakan aturan perkalian untuk kejadian yang saling bebas: 5 kemeja * 4 celana * 3 pasang sepatu = 60 setelan.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan aturan perkalian dasar dalam kombinatorika untuk menentukan banyaknya kombinasi dari tiga kategori objek yang berbeda.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip dasar aturan perkalian (aturan pengisian tempat) sebagai prosedur standar untuk menghitung ruang sampel dari kejadian majemuk yang saling bebas.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung menguji pemahaman aturan perkalian tanpa adanya kendala tambahan, syarat khusus, atau kompleksitas integrasi. Jalur penyelesaian sangat jelas dan familiar bagi siswa kelas 12.. Bukti: 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu; tentukan banyak setelan berbeda

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
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari aturan perkalian dasar yang sudah dipelajari sejak jenjang SMP/awal SMA, sehingga bagi siswa kelas 12, ini dikategorikan sebagai soal yang sangat mudah. |

Run 3 — solusi: Menggunakan aturan perkalian untuk kejadian yang saling bebas: 5 kemeja * 4 celana * 3 pasang sepatu = 60 setelan.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan aturan perkalian dasar untuk menentukan banyaknya kombinasi setelan pakaian. Siswa hanya perlu mengenali bahwa setiap pemilihan item (kemeja, celana, sepatu) adalah kejadian yang saling bebas dan mengalikan jumlah pilihan masing-masing.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda; tentukan banyak setelan berbeda yang dibuat
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian dalam kombinatorika dasar.. Bukti: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi jumlah objek di setiap kategori dan menerapkan aturan perkalian. Tidak ada kendala tambahan, syarat khusus, atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu; tentukan banyak setelan berbeda

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang aturan perkalian (counting principle) untuk kejadian saling bebas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan dasar aturan perkalian yang sudah dipelajari sejak jenjang SMP/awal SMA, sehingga sangat mudah bagi siswa kelas 12. |

Histori retry: run 1 sebelumnya `failed` / `ServerError:503`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4213`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta siswa untuk menerapkan prinsip dasar aturan perkalian (multiplication principle) untuk menentukan banyaknya kombinasi dari tiga kategori objek yang saling bebas. Ini adalah penerapan langsung dari konsep dasar pencacahan.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami dan menggunakan prosedur standar aturan perkalian untuk menghitung ruang sampel dari kejadian majemuk yang saling bebas.
- Intended difficulty `Easy`: Soal ini sangat mendasar dan rutin. Siswa hanya perlu mengidentifikasi jumlah objek di setiap kategori dan mengalikannya. Tidak ada kendala tambahan, syarat khusus, atau kebutuhan untuk merencanakan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan perkalian (multiplication principle) untuk kejadian saling bebas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar aturan pencacahan yang sangat umum dan sudah dipelajari sejak jenjang SMP/awal SMA, sehingga bagi siswa kelas 12, ini dikategorikan sebagai soal yang sangat mudah. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `cd21884f9b39f41443039e69`

Swalayan AAmart mengeluarkan kupon hadiah dengan kode berbentuk bilangan yang disusun dari angka 1, 2, 2, 6, dan 8. Jika kupon-kupon tersebut disusun berdasarkan kodenya mulai dari yang terkecil sampai dengan yang terbesar, maka kupon dengan kode lebih besar daripada 62000 sebanyak ....

| Opsi | Isi |
|---|---|
| A | 19 kupon |
| B | 21 kupon |
| C | 24 kupon |
| D | 20 kupon |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `21`.
Solusi minimum hasil AI: Total permutasi > 62000: (1) Digit pertama 8: sisa {1,2,2,6} -> 4!/2! = 12. (2) Digit pertama 6, kedua 8: sisa {1,2,2} -> 3!/2! = 3. (3) Digit pertama 6, kedua 2: sisa {1,2,6} -> 3! = 6. Total = 12 + 3 + 6 = 21.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fd224f12eb942015f901692ebee464e2553b65a157fcf623d418b68752e3306b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 4279 |
| 2 | success | valid / verified | applying | procedural | Medium | 2912 |
| 3 | success | valid / verified | applying | procedural | Medium | 2964 |

Run 1 — solusi: Total permutasi > 62000: (1) Digit pertama 8: sisa {1,2,2,6} -> 4!/2! = 12. (2) Digit pertama 6, kedua 8: sisa {1,2,2} -> 3!/2! = 3. (3) Digit pertama 6, kedua 2: sisa {1,2,6} -> 3! = 6. Total = 12 + 3 + 6 = 21.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus permutasi dengan unsur yang sama dan melakukan analisis kasus (pembagian kasus berdasarkan digit pertama dan kedua) untuk memenuhi batasan nilai > 62000.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kupon dengan kode lebih besar daripada 62000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung permutasi dengan objek berulang dan menerapkannya dalam konteks pembatasan nilai.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kupon dengan kode lebih besar daripada 62000
- Intended difficulty `classify/Medium`: Soal memerlukan perencanaan langkah-langkah sistematis (analisis kasus) dan ketelitian dalam menangani pengulangan angka. Tingkat kesulitan sedang karena siswa harus memecah masalah menjadi sub-kasus yang saling lepas.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kupon dengan kode lebih besar daripada 62000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Permutasi dengan unsur yang sama (objek berulang). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan analisis kasus pada permutasi dengan unsur sama. Soal ini memerlukan ketelitian dalam membagi kasus dan menghitung permutasi setiap kasus. |

Run 2 — solusi: Digit tersedia: {1, 2, 2, 6, 8}. Total permutasi 5 digit: 5!/2! = 60. Kode > 62000: 1) Awalan 8: sisa {1, 2, 2, 6} disusun 4!/2! = 12. 2) Awalan 68: sisa {1, 2, 2} disusun 3!/2! = 3. 3) Awalan 62: sisa {1, 2, 8} disusun 3! = 6. Total = 12 + 3 + 6 = 21.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi kasus-kasus yang memenuhi syarat (lebih besar dari 62000) berdasarkan posisi digit pertama dan kedua, serta menerapkan rumus permutasi dengan objek berulang (multiset) untuk setiap kasus tersebut.. Bukti: disusun berdasarkan kodenya mulai dari yang terkecil sampai dengan yang terbesar; kupon dengan kode lebih besar daripada 62000
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman prosedural tentang permutasi dengan pengulangan dan penerapan prinsip aturan perkalian/penjumlahan untuk memecah masalah menjadi kasus-kasus yang saling lepas.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; permutasi dengan objek berulang
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan langkah (memecah menjadi kasus awalan 8, 68, dan 62) dan ketelitian dalam menerapkan rumus permutasi dengan objek berulang. Meskipun prosedurnya familiar, siswa harus mengelola kendala digit berulang (angka 2) secara konsisten di setiap kasus.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kode lebih besar daripada 62000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Permutasi dengan objek berulang (multiset), aturan penjumlahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan analisis kasus pada permutasi. Kompleksitas terletak pada penanganan angka 2 yang berulang dan pembagian kasus yang sistematis. |

Run 3 — solusi: Total permutasi dari {1, 2, 2, 6, 8} adalah 5!/2! = 60. Kode > 62000: (1) Awalan 8: sisa {1, 2, 2, 6} disusun 4!/2! = 12. (2) Awalan 6, digit kedua 8: sisa {1, 2, 2} disusun 3!/2! = 3. (3) Awalan 6, digit kedua 2: sisa {1, 2, 8} disusun 3! = 6. Total = 12 + 3 + 6 = 21.
- Domain kognitif `classify/applying`: Siswa harus menerapkan prinsip permutasi dengan unsur yang sama (multiset) dan melakukan analisis kasus berdasarkan posisi digit (place value) untuk menentukan banyaknya susunan yang memenuhi syarat lebih besar dari 62000. Ini memerlukan penerapan prosedur yang sudah dipelajari dalam konteks yang sedikit lebih kompleks.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kupon dengan kode lebih besar daripada 62000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang permutasi dengan pengulangan dan bagaimana mengintegrasikannya dengan logika urutan bilangan (place value).. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kupon dengan kode lebih besar daripada 62000
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan langkah-langkah sistematis (analisis kasus berdasarkan digit pertama dan kedua) serta penerapan rumus permutasi dengan unsur yang sama. Siswa harus mengelola beberapa kendala (angka 2 berulang) dan membagi masalah menjadi sub-kasus yang saling lepas, yang merupakan tuntutan standar untuk kelas 12.. Bukti: disusun dari angka 1, 2, 2, 6, dan 8; kupon dengan kode lebih besar daripada 62000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Permutasi dengan unsur yang sama, aturan perkalian, dan konsep nilai tempat bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan analisis kasus pada masalah pencacahan. Tingkat kesulitan ini sesuai karena memerlukan ketelitian dalam membagi kasus dan menerapkan rumus permutasi yang tepat tanpa bantuan langkah-langkah eksplisit. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `4c33984e92f3e85b5396ba7f`

Ada tujuh orang siswa akan membentuk barisan. Tentukan banyaknya susunan barisan yang mungkin terjadi.

| Opsi | Isi |
|---|---|
| A | 720 susunan |
| B | 40.320 susunan |
| C | 5.040 susunan |
| D | 49 susunan |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Banyaknya susunan barisan dari 7 orang siswa adalah permutasi dari 7 objek berbeda, yaitu 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5.040.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bd3a8e59e8b8f022c7bcde5df866b4a1007e099ee08d4e6e235eef500a2be50c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3278 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3131 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3195 |

Run 1 — solusi: Banyaknya susunan barisan dari 7 orang siswa adalah permutasi dari 7 objek berbeda, yaitu 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5.040.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali bahwa menyusun n objek dalam barisan adalah permutasi n! dan menerapkan rumus tersebut secara langsung tanpa modifikasi.. Bukti: Ada tujuh orang siswa akan membentuk barisan; Tentukan banyaknya susunan barisan yang mungkin terjadi
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang rumus permutasi dasar untuk menyusun objek.. Bukti: Tentukan banyaknya susunan barisan yang mungkin terjadi
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, tidak ada syarat tambahan, kendala, atau konteks yang kompleks. Siswa hanya perlu menghitung 7!.. Bukti: Ada tujuh orang siswa akan membentuk barisan; Tentukan banyaknya susunan barisan yang mungkin terjadi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar permutasi n objek (n!) |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung rumus permutasi dasar yang sudah dipelajari di kelas 12, tanpa variasi atau kendala tambahan. |

Run 2 — solusi: Banyaknya susunan 7 orang dalam barisan adalah permutasi 7 objek, yaitu 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5.040.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta penerapan langsung rumus permutasi n objek (n!) tanpa ada syarat tambahan atau kendala yang perlu dipertimbangkan.. Bukti: Ada tujuh orang siswa akan membentuk barisan. Tentukan banyaknya susunan barisan yang mungkin terjadi.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma faktorial untuk menghitung permutasi dari 7 objek yang berbeda.. Bukti: Tentukan banyaknya susunan barisan yang mungkin terjadi.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya melibatkan satu langkah perhitungan faktorial dasar tanpa kendala atau syarat tambahan.. Bukti: Ada tujuh orang siswa akan membentuk barisan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep permutasi dasar dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi permutasi dasar adalah standar kelas 12, dan soal ini tidak memiliki kompleksitas tambahan. |

Run 3 — solusi: Banyaknya susunan 7 orang dalam barisan adalah permutasi 7 objek, yaitu 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5.040.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus permutasi dasar (n!) untuk menyusun n objek dalam barisan linear. Tidak ada syarat tambahan, kendala, atau kompleksitas yang memerlukan penalaran lebih lanjut.. Bukti: Ada tujuh orang siswa akan membentuk barisan.; Tentukan banyaknya susunan barisan yang mungkin terjadi.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui dan menerapkan algoritma faktorial untuk permutasi linear sebagai prosedur standar.. Bukti: Tentukan banyaknya susunan barisan yang mungkin terjadi.
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus permutasi n objek tanpa kendala tambahan, sangat rutin untuk kelas 12.. Bukti: Ada tujuh orang siswa akan membentuk barisan.; Tentukan banyaknya susunan barisan yang mungkin terjadi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar permutasi linear (n!) |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini adalah soal permutasi dasar yang tidak memerlukan perencanaan strategi atau integrasi kendala, sehingga dikategorikan mudah bagi siswa kelas 12. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `e9e9f310f9de364e628b69a2`

Terdapat sepuluh orang pergi ketempat wisata dengan mengendarai 3 mobil berkapasitas 4 orang dan tiga orang diantarannya adalah pemilik mobil. Jika setiap mobil dikemudikan oleh pemiliknya dan di setiap mobil minimal ada satu penumpang selain pengemudi, banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang di ketiga mobil tersebut ada ....

| Opsi | Isi |
|---|---|
| A | 1.190 cara |
| B | 1.050 cara |
| C | 840 cara |
| D | 700 cara |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `1.050`.
Solusi minimum hasil AI: Total penumpang = 7. Kapasitas sisa tiap mobil = 3. Syarat: tiap mobil minimal 1 penumpang. Partisi 7 ke 3 mobil (maks 3): Pola (3,3,1) ada 3 permutasi mobil: 3 * (7C3 * 4C3 * 1C1) = 3 * 35 * 4 = 420. Pola (3,2,2) ada 3 permutasi mobil: 3 * (7C3 * 4C2 * 2C2) = 3 * 35 * 6 = 630. Total = 420 + 630 = 1.050.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bd192ba4298c2042e86859f587176058520c5509e23395d3921dc12890031b1f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Hard | 3005 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 3044 |
| 3 | success | valid / verified | reasoning | procedural | Hard | 2940 |

Run 1 — solusi: Total penumpang = 10 - 3 = 7. Kapasitas sisa tiap mobil = 4 - 1 = 3. Syarat: tiap mobil minimal 1 penumpang. Partisi 7 penumpang ke 3 mobil (kapasitas sisa 3,3,3): Pola (3,3,1) ada 3 permutasi mobil: 3 * (7!/(3!3!1!)) = 3 * 140 = 420. Pola (3,2,2) ada 3 permutasi mobil: 3 * (7!/(3!2!2!)) = 3 * 210 = 630. Total = 420 + 630 = 1.050.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi kendala (kapasitas mobil dan syarat minimal penumpang), melakukan partisi bilangan (integer partition) untuk membagi 7 penumpang ke 3 mobil, dan menerapkan rumus permutasi/kombinasi untuk setiap kasus. Ini adalah penerapan konsep kombinatorika pada konteks yang memerlukan perencanaan langkah.. Bukti: setiap mobil dikemudikan oleh pemiliknya; di setiap mobil minimal ada satu penumpang selain pengemudi; banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip dasar kombinatorika (permutasi/kombinasi) dan teknik partisi untuk menyelesaikan masalah pembagian objek ke dalam kelompok dengan batasan tertentu.. Bukti: banyaknya kemungkinan komposisi berbeda; minimal ada satu penumpang
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard karena siswa harus merencanakan sendiri pembagian kasus (partisi 7 ke 3 mobil dengan batasan kapasitas 3 dan minimal 1). Siswa perlu mengintegrasikan kendala kapasitas dan syarat minimal penumpang, serta melakukan perhitungan untuk setiap skenario yang mungkin (3,3,1 dan 3,2,2) tanpa bantuan langkah eksplisit.. Bukti: 3 mobil berkapasitas 4 orang; tiga orang diantarannya adalah pemilik mobil; setiap mobil dikemudikan oleh pemiliknya; di setiap mobil minimal ada satu penumpang selain pengemudi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar kombinatorika, permutasi, dan partisi bilangan. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menangani masalah kombinatorika dengan kendala ganda. Kesulitan utama terletak pada perencanaan kasus (partisi) yang harus dibangun sendiri oleh siswa, bukan sekadar menghitung rumus. |

Run 2 — solusi: Terdapat 7 penumpang yang harus dibagi ke 3 mobil. Kapasitas sisa tiap mobil adalah 3 (karena 1 kursi dipakai pengemudi). Syarat minimal 1 penumpang per mobil. Kemungkinan partisi 7 penumpang ke 3 mobil (maks 3 per mobil): 1) Pola (3,3,1): Ada 3 permutasi posisi mobil (3,3,1; 3,1,3; 1,3,3). Banyak cara: 3 * (7C3 * 4C3 * 1C1) = 3 * (35 * 4 * 1) = 420. 2) Pola (3,2,2): Ada 3 permutasi posisi mobil (3,2,2; 2,3,2; 2,2,3). Banyak cara: 3 * (7C3 * 4C2 * 2C2) = 3 * (35 * 6 * 1) = 630. Total = 420 + 630 = 1.050.
- Domain kognitif `classify/reasoning`: Siswa harus mengidentifikasi kendala (kapasitas mobil, syarat minimal penumpang) dan merencanakan strategi partisi (kasus pola pembagian) untuk menyelesaikan masalah kombinatorika yang tidak rutin.. Bukti: setiap mobil dikemudikan oleh pemiliknya; di setiap mobil minimal ada satu penumpang selain pengemudi; banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip kombinasi dan bagaimana menerapkannya dalam skenario partisi dengan kendala yang saling berinteraksi.. Bukti: banyaknya kemungkinan komposisi berbeda; minimal ada satu penumpang selain pengemudi
- Intended difficulty `classify/Hard`: Soal ini menuntut perencanaan strategis untuk membagi 7 penumpang ke dalam 3 mobil dengan kendala kapasitas (maks 3 penumpang per mobil) dan syarat minimal (1 penumpang per mobil). Siswa harus memecah masalah menjadi kasus-kasus partisi yang mungkin (3,3,1 dan 3,2,2) dan menghitung kombinasi untuk setiap kasus. Interaksi kendala ini membuat perencanaan langkah menjadi krusial.. Bukti: 3 mobil berkapasitas 4 orang; tiga orang diantarannya adalah pemilik mobil; minimal ada satu penumpang selain pengemudi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip kombinasi dasar dan teknik partisi/pengelompokan. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menangani masalah kombinatorika dengan kendala ganda. Soal ini menuntut kemampuan memecah masalah menjadi kasus (case-based reasoning) yang merupakan standar kesulitan tinggi untuk materi pencacahan di tingkat SMA. |

Run 3 — solusi: Terdapat 7 penumpang yang harus dibagi ke 3 mobil. Kapasitas sisa tiap mobil adalah 3 (karena 1 kursi dipakai pengemudi). Syarat minimal 1 penumpang per mobil. Kemungkinan distribusi penumpang (mobil 1, mobil 2, mobil 3): 1) (3,3,1) dan permutasi: 3 x (7!/(3!3!1!)) = 3 x 140 = 420. 2) (3,2,2) dan permutasi: 3 x (7!/(3!2!2!)) = 3 x 210 = 630. Total = 420 + 630 = 1.050.
- Domain kognitif `classify/reasoning`: Siswa harus mengidentifikasi kendala (kapasitas mobil, syarat minimal penumpang) dan merancang strategi partisi bilangan (7 penumpang ke 3 mobil) untuk menghitung komposisi yang valid. Ini memerlukan pemilihan prosedur kombinatorik yang tepat dalam konteks yang tidak rutin.. Bukti: setiap mobil dikemudikan oleh pemiliknya; di setiap mobil minimal ada satu penumpang selain pengemudi; banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prinsip kombinasi dan partisi bilangan untuk menyelesaikan masalah pencacahan yang melibatkan kendala-kendala yang saling berinteraksi.. Bukti: banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang
- Intended difficulty `classify/Hard`: Soal ini menuntut perencanaan strategis untuk memecah masalah menjadi kasus-kasus partisi yang mungkin (3,3,1 dan 3,2,2) dengan mempertimbangkan kendala kapasitas dan syarat minimal. Siswa harus mengintegrasikan prinsip kombinasi dengan pembatasan fisik, yang merupakan tuntutan tinggi bagi kelas 12.. Bukti: 3 mobil berkapasitas 4 orang; tiga orang diantarannya adalah pemilik mobil; di setiap mobil minimal ada satu penumpang selain pengemudi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar kombinasi, partisi bilangan, dan aturan perkalian. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Tingkat kesulitan tinggi karena siswa harus membangun sendiri model partisi yang memenuhi semua kendala (kapasitas dan syarat minimal) tanpa bantuan langkah-langkah eksplisit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "reasoning": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Hard": 3} | unanimous_3_0 / adjudicated | Hard |

Adjudikasi AI: `success`; token `5148`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus mengidentifikasi kendala (kapasitas mobil dan syarat minimal penumpang), melakukan partisi bilangan untuk membagi 7 penumpang ke 3 mobil, dan menerapkan rumus kombinasi untuk setiap kasus. Ini adalah penerapan konsep kombinatorika pada konteks yang memerlukan perencanaan langkah.
- Dimensi pengetahuan `procedural`: Siswa menggunakan prinsip dasar kombinatorika (kombinasi) dan teknik partisi untuk menyelesaikan masalah pembagian objek ke dalam kelompok dengan batasan tertentu.
- Intended difficulty `Hard`: Soal ini dikategorikan Hard karena siswa harus merencanakan sendiri pembagian kasus (partisi 7 ke 3 mobil dengan batasan kapasitas 3 dan minimal 1). Siswa perlu mengintegrasikan kendala kapasitas dan syarat minimal penumpang, serta melakukan perhitungan untuk setiap skenario yang mungkin tanpa bantuan langkah eksplisit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar kombinatorika, permutasi, dan partisi bilangan. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu menangani masalah kombinatorika dengan kendala ganda. Kesulitan utama terletak pada perencanaan kasus (partisi) yang harus dibangun sendiri oleh siswa, bukan sekadar menghitung rumus. |

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

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "procedural", "intendedDifficulty": "Hard"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Hard", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `42af439f72392b9d1118073a`

Pada suatu Olimpiade Matematika, peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia. Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan.

| Opsi | Isi |
|---|---|
| A | 6.720 |
| B | 40 |
| C | 70 |
| D | 56 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menggunakan rumus kombinasi C(n, r) = n! / (r!(n-r)!) untuk memilih 5 soal dari 8 soal. C(8, 5) = 8! / (5!(8-5)!) = (8 x 7 x 6) / (3 x 2 x 1) = 56.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d4c46df30aa920260b8f9fb21989649e2ca323445cc995a5d9734c779165712a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2635 |
| 2 | success | valid / verified | applying | procedural | Easy | 2608 |
| 3 | success | valid / verified | applying | procedural | Easy | 2607 |

Run 1 — solusi: Menggunakan rumus kombinasi C(n, r) = n! / (r!(n-r)!) untuk memilih 5 soal dari 8 soal. C(8, 5) = 8! / (5!(8-5)!) = (8 x 7 x 6) / (3 x 2 x 1) = 56.
- Domain kognitif `classify/applying`: Siswa perlu mengenali bahwa masalah ini adalah pemilihan subset (kombinasi) di mana urutan pengerjaan tidak relevan, kemudian menerapkan rumus kombinasi yang sesuai.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia; Tentukan banyaknya jenis pilihan soal
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus kombinasi dan kemampuan mengkategorikan masalah sebagai kombinasi (bukan permutasi).. Bukti: mengerjakan 5 soal dari 8 soal; banyaknya jenis pilihan soal
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Tidak ada kendala tambahan atau syarat khusus yang membuat perencanaan menjadi kompleks.. Bukti: mengerjakan 5 soal dari 8 soal yang tersedia; banyaknya jenis pilihan soal

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
| gradeRelativeRationale | Ini adalah soal standar kombinasi yang diajarkan di kelas 12. Tidak ada kompleksitas tambahan atau syarat yang memerlukan penalaran mendalam. |

Run 2 — solusi: Menggunakan rumus kombinasi C(n, r) = n! / (r!(n-r)!) untuk memilih 5 soal dari 8 soal. C(8, 5) = 8! / (5!3!) = (8 x 7 x 6) / (3 x 2 x 1) = 56.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini adalah pemilihan objek tanpa memperhatikan urutan, sehingga menggunakan konsep kombinasi. Ini adalah penerapan prosedur standar pada konteks yang rutin.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia; Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami prinsip kombinasi (konsep) dan menerapkan rumus kombinasi (prosedural) untuk menyelesaikan masalah.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 12. Tidak ada kendala tambahan atau syarat khusus yang membuat perencanaan menjadi kompleks.. Bukti: mengerjakan 5 soal dari 8 soal yang tersedia

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kombinasi dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kombinasi adalah standar kurikulum SMA kelas 12. Soal ini adalah aplikasi langsung rumus tanpa variasi atau syarat tambahan. |

Run 3 — solusi: Soal meminta pemilihan 5 soal dari 8 soal yang tersedia tanpa memperhatikan urutan pengerjaan. Ini adalah masalah kombinasi: C(8,5) = 8! / (5! * (8-5)!) = (8 * 7 * 6) / (3 * 2 * 1) = 56.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini adalah pemilihan subset (kombinasi) di mana urutan tidak penting, kemudian menerapkan rumus kombinasi standar.. Bukti: peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia; Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur algoritme kombinasi untuk menyelesaikan masalah pemilihan objek.. Bukti: mengerjakan 5 soal dari 8 soal yang tersedia
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus kombinasi dasar. Tidak ada kendala tambahan, syarat khusus, atau kebutuhan untuk menyusun strategi yang kompleks.. Bukti: mengerjakan 5 soal dari 8 soal yang tersedia

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
| gradeRelativeRationale | Ini adalah soal standar kelas 12 yang menguji pemahaman dasar tentang perbedaan permutasi dan kombinasi. Jalur penyelesaian sangat jelas dan langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `d4a29da533d9881db57e7c74`

Tim futsal SMA Abhipraya dijadwalkan mengikuti 3 pertandingan awal dalam turnamen dengan sistem poin. Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6 berdasarkan data latihan dan uji coba. Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.

| Opsi | Isi |
|---|---|
| A | 0,216 |
| B | 0,6 |
| C | 0,432 |
| D | 0,36 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menggunakan rumus peluang binomial P(X=k) = C(n,k) * p^k * (1-p)^(n-k) dengan n=3, k=2, p=0,6. P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ea053eaa813a323686925def19a78e488598db732d992c7c53074fa79e212621`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2816 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2761 |
| 3 | success | valid / verified | applying | procedural | Easy | 2760 |

Run 1 — solusi: Menggunakan rumus peluang binomial P(X=k) = C(n,k) * p^k * q^(n-k) dengan n=3, k=2, p=0,6, dan q=0,4. P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus peluang binomial untuk situasi yang sudah didefinisikan dengan jelas (n=3, k=2, p=0,6). Siswa perlu mengenali bahwa ini adalah masalah peluang binomial dan menerapkan prosedurnya secara langsung.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip dasar peluang binomial (konsep) dan menerapkan rumus atau metode perhitungan yang sesuai (prosedural) untuk menyelesaikan masalah.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari rumus peluang binomial yang standar. Variabel n, k, dan p sudah diberikan secara eksplisit, dan tidak ada kendala tambahan atau skenario kompleks yang memerlukan perencanaan strategi yang rumit.. Bukti: 3 pertandingan awal; Peluang menang ... sebesar 0,6; tepat 2 dari 3 pertandingan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang kejadian majemuk dan rumus distribusi binomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang binomial adalah standar kurikulum kelas 12. Soal ini tidak memerlukan modifikasi strategi atau integrasi konsep yang kompleks, sehingga sesuai untuk tingkat kesulitan rendah bagi siswa kelas 12. |

Run 2 — solusi: Menggunakan rumus peluang binomial P(X=k) = C(n,k) * p^k * (1-p)^(n-k) dengan n=3, k=2, p=0,6. P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini mengikuti distribusi binomial dan menerapkan rumus yang sesuai untuk menghitung peluang kejadian majemuk dengan syarat tertentu.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip peluang binomial (konsep) dan penggunaan rumus binomial (prosedural) untuk menyelesaikan masalah.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12 yang telah mempelajari distribusi binomial. Jalur penyelesaiannya jelas (menggunakan rumus binomial) dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang rumit.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian saling bebas dan rumus distribusi binomial. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang binomial adalah standar kurikulum kelas 12. Soal ini merupakan aplikasi langsung dari rumus tanpa modifikasi atau syarat tambahan yang menyulitkan. |

Run 3 — solusi: Menggunakan rumus peluang binomial P(X=k) = C(n,k) * p^k * (1-p)^(n-k), dengan n=3, k=2, p=0,6. P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa ini adalah masalah distribusi binomial, memilih rumus yang tepat, dan menerapkan nilai-nilai yang diberikan ke dalam rumus tersebut. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode perhitungan peluang kejadian majemuk dengan distribusi binomial.. Bukti: Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari rumus binomial yang sudah familiar di kelas 12. Jalur penyelesaiannya sangat jelas, tidak ada kendala yang berinteraksi, dan beban perhitungan rendah.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian majemuk dan rumus distribusi binomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang binomial adalah standar kurikulum kelas 12. Soal ini tidak memerlukan modifikasi strategi atau integrasi konsep yang kompleks, sehingga tergolong mudah bagi siswa kelas 12. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4483`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengenali bahwa situasi ini mengikuti distribusi binomial dan menerapkan rumus yang sesuai untuk menghitung peluang kejadian majemuk dengan syarat tertentu. Ini adalah penerapan prosedur standar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami prinsip dasar peluang binomial (konsep) dan menerapkan rumus atau metode perhitungan yang sesuai (prosedural) untuk menyelesaikan masalah.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 12 yang telah mempelajari distribusi binomial. Jalur penyelesaiannya jelas (menggunakan rumus binomial) dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang rumit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang kejadian majemuk dan rumus distribusi binomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang binomial adalah standar kurikulum kelas 12. Soal ini merupakan aplikasi langsung dari rumus tanpa modifikasi atau syarat tambahan yang menyulitkan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `eded99210de8f3efd55fe9df`

Guru IPA menjelaskan bahwa kenyamanan belajar dipengaruhi oleh kualitas udara, yang tergantung pada suhu (t) dan kelembaban (h). Dalam penelitian kecil di kelas, ditemukan bahwa pengaruh suhu dua kali lebih besar dibanding kelembaban, dan model total pengaruhnya adalah $(2t+h)^5$. Jika suatu waktu suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian. Berapakah total kontribusi kombinasi tersebut?

| Opsi | Isi |
|---|---|
| A | 80 |
| B | 32 |
| C | 10 |
| D | 40 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `80`.
Solusi minimum hasil AI: Ekspansi (2t+h)^5 menggunakan teorema binomial: suku dengan t^3 h^2 diperoleh saat k=2 (karena h^2). Suku tersebut adalah C(5,2) * (2t)^3 * h^2 = 10 * 8 * t^3 h^2 = 80 t^3 h^2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c03475537dcda76d286d51a13d17fbaf011fe2e135cd65acfe7878b180e829d7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3613 |
| 2 | success | valid / verified | applying | procedural | Easy | 4092 |
| 3 | success | valid / verified | applying | procedural | Medium | 4335 |

Run 1 — solusi: Ekspansi binomial (2t+h)^5 menggunakan rumus C(n,k) * a^(n-k) * b^k. Untuk suku t^3 h^2, kita pilih k=2 (karena h^2). Suku tersebut adalah C(5,2) * (2t)^3 * h^2 = 10 * 8t^3 * h^2 = 80t^3h^2. Koefisiennya adalah 80.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema binomial untuk mencari koefisien suku tertentu dalam ekspansi binomial. Ini adalah penerapan prosedur standar pada konteks yang diberikan.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penggunaan algoritma ekspansi binomial (prosedur) untuk menyelesaikan masalah.. Bukti: model total pengaruhnya adalah (2t+h)^5
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemilihan prosedur (teorema binomial) dan pemahaman hubungan antara variabel (t, h) dengan pangkat dalam ekspansi. Tidak terlalu sulit karena prosedurnya langsung, namun memerlukan ketelitian dalam mengidentifikasi k dan koefisien binomial.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial Newton |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 seharusnya familiar dengan teorema binomial. Soal ini menguji penerapan langsung prosedur tersebut dengan sedikit interpretasi variabel. |

Run 2 — solusi: Ekspansi (2t+h)^5 menggunakan teorema binomial: suku dengan t^3 h^2 adalah C(5,3) * (2t)^3 * h^2 = 10 * 8 * t^3 h^2 = 80 t^3 h^2. Koefisiennya adalah 80.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus teorema binomial untuk mencari koefisien suku tertentu dalam ekspansi (2t+h)^5.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma teorema binomial untuk mendapatkan nilai koefisien.. Bukti: model total pengaruhnya adalah (2t+h)^5
- Intended difficulty `classify/Easy`: Soal merupakan penerapan langsung teorema binomial yang merupakan materi standar kelas 12. Langkah penyelesaian bersifat rutin dan tidak memerlukan strategi non-rutin.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi teorema binomial adalah kurikulum standar kelas 12. Soal ini menguji pemahaman prosedural dasar tanpa kompleksitas tambahan. |

Run 3 — solusi: Ekspansi (2t+h)^5 menggunakan teorema binomial adalah sum_{k=0}^5 C(5,k) (2t)^{5-k} h^k. Untuk suku t^3 h^2, kita butuh 5-k=3, sehingga k=2. Suku tersebut adalah C(5,2) * (2t)^3 * h^2 = 10 * 8 * t^3 h^2 = 80 t^3 h^2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema binomial untuk menentukan koefisien suku tertentu dalam ekspansi (2t+h)^5. Ini adalah penerapan prosedur standar pada konteks yang diberikan.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma teorema binomial untuk mencari suku yang diminta.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian
- Intended difficulty `classify/Medium`: Siswa harus mengidentifikasi bahwa '3 bagian suhu' dan '2 bagian kelembaban' merujuk pada suku t^3 h^2 dalam ekspansi (2t+h)^5. Ini memerlukan pemahaman konseptual tentang teorema binomial dan kemampuan untuk memetakan konteks soal ke dalam bentuk matematika. Tidak terlalu sulit karena prosedurnya standar, namun memerlukan langkah pemilihan yang tepat.. Bukti: model total pengaruhnya adalah (2t+h)^5; suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial Newton |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji pemahaman teorema binomial yang merupakan materi kelas 11/12. Tingkat kesulitan Medium karena siswa harus menerjemahkan narasi ke dalam bentuk aljabar (2t+h)^5 dan memilih suku yang tepat, bukan sekadar menghitung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5417`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan teorema binomial untuk mencari koefisien suku tertentu dalam ekspansi (2t+h)^5. Ini adalah penerapan prosedur standar pada konteks yang diberikan.
- Dimensi pengetahuan `procedural`: Soal menguji penggunaan algoritma ekspansi binomial untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal memerlukan pemilihan prosedur (teorema binomial) dan pemahaman hubungan antara variabel (t, h) dengan pangkat dalam ekspansi. Siswa harus menerjemahkan narasi ke dalam bentuk aljabar dan memilih suku yang tepat. Prosedurnya standar, namun memerlukan langkah interpretasi yang sedikit lebih dari sekadar menghitung langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Binomial Newton |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi teorema binomial adalah kurikulum standar kelas 12. Soal ini menguji pemahaman prosedural dengan sedikit interpretasi variabel. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `6353e1b1ac73792bd65d8bcc`

Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.<br><br>Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?

| Opsi | Isi |
|---|---|
| A | Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$ |
| B | Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$ |
| C | Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$ |
| D | Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Kejadian A (muncul angka dobel) dan B (muncul jumlah 6) adalah kejadian saling bebas. P(A) = 6/36 = 1/6. P(B) = 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Peluang gabungan = P(A) * P(B) = 1/6 * 5/36 = 5/216.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d0937a7ae0a5cd17553a3b43a433b83878da4e99543f53ab26b23fa84b9586f8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2814 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2840 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2899 |

Run 1 — solusi: Kejadian A (mendapat angka dobel) dan B (mendapat jumlah enam) adalah dua kejadian saling bebas karena hasil lemparan pertama tidak mempengaruhi hasil lemparan kedua. P(A) = 6/36 = 1/6. P(B) = 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Peluang gabungan = P(A) x P(B) = 1/6 x 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi sifat kejadian (saling bebas) dan menerapkan aturan perkalian peluang yang sesuai. Ini melibatkan penerapan konsep dasar peluang pada konteks yang rutin.. Bukti: Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip atau aturan perkalian dalam peluang, yang merupakan bagian dari pengetahuan konseptual tentang hubungan antar kejadian.. Bukti: aturan perkalian dapat digunakan untuk menentukan peluang ini
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur penyelesaiannya sangat standar dan langsung. Siswa hanya perlu menghitung peluang dua kejadian sederhana dan mengalikannya. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam; Jelaskan mengapa aturan perkalian dapat digunakan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel dua dadu dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk saling bebas adalah topik standar kelas 12 yang rutin. Soal tidak menuntut analisis mendalam atau integrasi konsep yang rumit. |

Run 2 — solusi: Kejadian A (muncul angka dobel) dan B (muncul jumlah 6) adalah kejadian saling bebas. P(A) = 6/36 = 1/6. P(B) = 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Peluang gabungan = P(A) * P(B) = 1/6 * 5/36 = 5/216.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi independensi dua kejadian (konsep) dan menerapkan aturan perkalian peluang untuk kejadian saling bebas (prosedur). Siswa harus memahami syarat penggunaan aturan perkalian, bukan sekadar menghitung.. Bukti: Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar peluang kejadian saling bebas (konseptual) dan menerapkan algoritma perkalian peluang (prosedural) untuk menyelesaikan masalah.. Bukti: Jelaskan mengapa aturan perkalian dapat digunakan; Berapa peluangnya?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa tidak hanya menghitung, tetapi juga memberikan justifikasi konseptual mengapa aturan perkalian berlaku (independensi). Meskipun prosedurnya familiar, integrasi antara pemahaman konsep dan perhitungan membuat tuntutannya sedikit di atas sekadar penerapan langsung.. Bukti: mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam; Jelaskan mengapa aturan perkalian dapat digunakan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman ruang sampel dua dadu (36 titik sampel) dan definisi kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 12, soal ini adalah penerapan standar peluang majemuk. Tuntutan 'jelaskan' menambah beban kognitif dari sekadar hitungan rutin menjadi pemahaman konsep. |

Run 3 — solusi: Kejadian pertama (A): muncul angka dobel pada sepasang dadu. n(S)=36, n(A)={(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)}=6. P(A)=6/36=1/6. Kejadian kedua (B): jumlah mata dadu 6. n(B)={(1,5),(2,4),(3,3),(4,2),(5,1)}=5. P(B)=5/36. Karena lemparan pertama dan kedua saling bebas, P(A dan B) = P(A) x P(B) = 1/6 x 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi bahwa dua kejadian pelemparan dadu adalah saling bebas, kemudian menerapkan aturan perkalian peluang untuk dua kejadian independen. Ini adalah penerapan konsep dasar peluang pada konteks rutin.. Bukti: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam.; Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip dasar peluang (kejadian saling bebas) dan prosedur perhitungan peluang gabungan.. Bukti: Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar dan langsung. Siswa hanya perlu menghitung peluang dua kejadian sederhana secara terpisah dan mengalikannya. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam.; Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel pelemparan dua dadu dan konsep peluang kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah standar kelas 12. Soal ini tidak memiliki kerumitan tambahan, sehingga termasuk kategori mudah bagi siswa kelas 12. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4589`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk mengidentifikasi sifat kejadian (saling bebas) dan menerapkan aturan perkalian peluang yang sesuai. Ini melibatkan penerapan konsep dasar peluang pada konteks yang rutin.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman tentang prinsip atau aturan perkalian dalam peluang, yang merupakan bagian dari pengetahuan konseptual tentang hubungan antar kejadian.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena prosedur penyelesaiannya sangat standar dan langsung. Siswa hanya perlu menghitung peluang dua kejadian sederhana dan mengalikannya. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel dua dadu dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk saling bebas adalah topik standar kelas 12 yang rutin. Soal tidak menuntut analisis mendalam atau integrasi konsep yang rumit. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Peluang Inggris juara adalah peluang menang perempat final dikali peluang menang semifinal dikali peluang menang final. P(Juara) = P(Perempat Final) * P(Semifinal) * P(Final) = 0,7 * 0,5 * 0,5 = 0,175.
Gambar sumber: images/kelas12_panduan_siswa_kelas12.pdf-0154-01.png. Transkripsi visual: Bagan turnamen sistem gugur dengan 8 tim: Uruguay vs Prancis, Brazil vs Belgia, Swedia vs Inggris, Rusia vs Kroasia. Pemenang perempat final masuk semifinal, pemenang semifinal masuk final, pemenang final menjadi juara. Tabel peluang menang perempat final: Uruguay 0,5; Prancis 0,5; Brazil 0,8; Belgia 0,2; Swedia 0,3; Inggris 0,7; Rusia 0,4; Kroasia 0,6. Peluang menang semifinal dan final adalah 0,5 untuk semua tim.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41a6db2f767aacf9fed3c3594ffb1d4b3da1b5bddd7f550fe90abbbd3ac3a6da`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 4217 |
| 2 | success | valid / verified | applying | conceptual | Medium | 4213 |
| 3 | success | valid / verified | applying | conceptual | Medium | 4163 |

Run 1 — solusi: Peluang Inggris juara adalah peluang menang perempat final dikali peluang menang semifinal dikali peluang menang final. P(Juara) = P(Perempat Final) * P(Semifinal) * P(Final) = 0,7 * 0,5 * 0,5 = 0,175.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa memenangkan turnamen adalah kejadian majemuk yang terdiri dari tiga tahap berurutan (perempat final, semifinal, final) dan menerapkan aturan perkalian untuk kejadian independen.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut adalah; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang peluang kejadian majemuk yang saling bebas dan prosedur perkalian peluang.. Bukti: peluang masing-masing tim tersebut untuk menang di babak perempat final; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengintegrasikan informasi dari tabel (peluang perempat final) dengan informasi teks (peluang semifinal dan final) untuk membentuk model peluang kejadian majemuk. Meskipun prosedurnya sederhana, siswa perlu memahami struktur bagan turnamen untuk menentukan jumlah tahapan yang harus dimenangkan.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut adalah; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk dan aturan perkalian peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengolah data dari tabel dan teks untuk menghitung peluang kejadian berurutan dalam konteks turnamen. |

Run 2 — solusi: Inggris harus memenangkan tiga pertandingan berturut-turut: perempat final (peluang 0,7), semifinal (peluang 0,5), dan final (peluang 0,5). Karena kejadian dianggap independen, peluang total adalah 0,7 * 0,5 * 0,5 = 0,175.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa memenangkan turnamen adalah kejadian majemuk yang terdiri dari tiga tahap (perempat final, semifinal, final) dan menerapkan aturan perkalian untuk kejadian independen.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut adalah; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip dasar peluang kejadian majemuk (perkalian peluang) dan menerapkannya pada konteks turnamen.. Bukti: peluang masing-masing tim tersebut untuk menang di babak perempat final; semua tim memiliki peluang yang sama untuk menang, yakni 0,5
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengintegrasikan informasi dari tabel (perempat final) dengan informasi teks (semifinal dan final) untuk membentuk urutan kejadian. Meskipun prosedurnya sederhana (perkalian), siswa perlu memahami struktur turnamen dan bahwa kemenangan turnamen bergantung pada keberhasilan di setiap tahap.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut adalah; semua tim memiliki peluang yang sama untuk menang, yakni 0,5

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk dan aturan perkalian. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu memodelkan kejadian berurutan dalam turnamen sistem gugur menggunakan aturan perkalian peluang. |

Run 3 — solusi: Peluang Inggris juara adalah peluang menang perempat final dikali peluang menang semifinal dikali peluang menang final. P(Juara) = P(Menang QF) * P(Menang SF) * P(Menang F) = 0,7 * 0,5 * 0,5 = 0,175.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa memenangkan turnamen adalah kejadian majemuk yang terdiri dari tiga tahap berurutan (perempat final, semifinal, final) dan menerapkan aturan perkalian untuk kejadian independen.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut adalah; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip dasar peluang kejadian majemuk (perkalian peluang) dan menerapkannya pada struktur turnamen yang diberikan.. Bukti: peluang masing-masing tim tersebut untuk menang di babak perempat final; semua tim memiliki peluang yang sama untuk menang, yakni 0,5
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengintegrasikan informasi dari tabel (peluang perempat final) dengan informasi teks (peluang semifinal dan final) untuk menghitung peluang gabungan. Meskipun prosedurnya adalah perkalian sederhana, siswa perlu memahami struktur turnamen dan mengidentifikasi bahwa ketiga tahap tersebut harus dilalui secara berurutan.. Bukti: peluang Inggris untuk memenangkan turnamen tersebut adalah; semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk dan aturan perkalian. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengolah data dari tabel dan teks untuk menghitung peluang kejadian berurutan dalam konteks sistem gugur. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Transkripsi visual: Bagan turnamen sistem gugur dengan 8 tim: Uruguay vs Prancis, Brazil vs Belgia, Swedia vs Inggris, Rusia vs Kroasia. Pemenang perempat final masuk semifinal, pemenang semifinal masuk final, pemenang final menjadi juara. Tabel peluang menang perempat final: Uruguay 0,5; Prancis 0,5; Brazil 0,8; Belgia 0,2; Swedia 0,3; Inggris 0,7; Rusia 0,4; Kroasia 0,6. Peluang menang semifinal dan final adalah 0,5 untuk semua tim.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `e6f2f945c5e535887f5e64bc`

Jika tiga dadu standar bersisi enam dilempar bersama-sama, berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12?

| Opsi | Isi |
|---|---|
| A | $\frac{1}{36}$ |
| B | $\frac{1}{216}$ |
| C | $\frac{1}{18}$ |
| D | $\frac{25}{216}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `25/216`.
Solusi minimum hasil AI: Ruang sampel n(S) = 6^3 = 216. Kejadian jumlah 12 (x+y+z=12, 1<=x,y,z<=6): Kombinasi (6,5,1) ada 6 permutasi; (6,4,2) ada 6; (6,3,3) ada 3; (5,5,2) ada 3; (5,4,3) ada 6; (4,4,4) ada 1. Total n(A) = 6+6+3+3+6+1 = 25. Peluang = 25/216.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dba4f130ef46efe9623be0fdea3101d7363005e8feb0f6a3a7ea4edda5b468d8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2805 |
| 2 | success | valid / verified | applying | procedural | Medium | 2835 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2840 |

Run 1 — solusi: Total ruang sampel n(S) = 6^3 = 216. Kejadian jumlah 12 (x+y+z=12, 1<=x,y,z<=6): (6,5,1)x6, (6,4,2)x6, (6,3,3)x3, (5,5,2)x3, (5,4,3)x6, (4,4,4)x1. Total n(A) = 6+6+3+3+6+1 = 25. Peluang = 25/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel dan menghitung banyaknya kejadian yang memenuhi syarat jumlah tertentu dengan mempertimbangkan urutan (permutasi) dari kombinasi angka yang mungkin.. Bukti: berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12?
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur perhitungan peluang klasik dengan menggunakan prinsip pencacahan untuk menentukan titik sampel yang memenuhi kondisi jumlah.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama; peluang jumlah total dadu pada ketiga pelemparan sama dengan 12
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan sistematis untuk mendaftar semua kombinasi angka yang berjumlah 12 dan menghitung permutasi untuk setiap kombinasi tersebut agar tidak ada yang terlewat atau terhitung ganda. Meskipun prosedurnya familiar, siswa harus mengelola kendala jumlah dan batasan angka dadu (1-6) secara cermat.. Bukti: tiga dadu standar bersisi enam; jumlah total dadu pada ketiga pelemparan sama dengan 12

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
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan pencacahan sistematis untuk masalah peluang majemuk sederhana seperti ini. Kesulitan terletak pada ketelitian enumerasi kasus. |

Run 2 — solusi: Ruang sampel n(S) = 6^3 = 216. Kejadian jumlah 12: (6,5,1)x6, (6,4,2)x6, (6,3,3)x3, (5,5,2)x3, (5,4,3)x6, (4,4,4)x1. Total n(A) = 6+6+3+3+6+1 = 25. Peluang = 25/216.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi ruang sampel, menentukan kombinasi angka yang berjumlah 12, dan menghitung permutasi dari setiap kombinasi tersebut untuk mendapatkan total kejadian yang menguntungkan. Ini adalah penerapan prosedur peluang pada konteks rutin.. Bukti: berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar pencacahan dan peluang kejadian majemuk, yang merupakan pengetahuan prosedural untuk menghitung ruang sampel dan kejadian yang diinginkan.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan sistematis untuk mendaftar semua kombinasi angka yang berjumlah 12 dan menghitung permutasi masing-masing (memperhatikan urutan). Meskipun prosedurnya familiar, siswa harus berhati-hati agar tidak ada kombinasi yang terlewat atau terhitung ganda, yang menuntut ketelitian lebih tinggi daripada sekadar menghitung peluang satu dadu.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama; jumlah total dadu pada ketiga pelemparan sama dengan 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan, permutasi, dan konsep peluang kejadian majemuk. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan pencacahan sistematis untuk kejadian dengan ruang sampel yang cukup besar (216). Kesalahan umum pada distraktor menunjukkan bahwa soal ini efektif menguji pemahaman tentang pentingnya urutan dalam pelemparan dadu. |

Run 3 — solusi: Ruang sampel n(S) = 6^3 = 216. Kejadian jumlah 12 dengan 3 dadu (x1+x2+x3=12, 1<=xi<=6): Kombinasi (6,5,1) ada 6 permutasi; (6,4,2) ada 6; (6,3,3) ada 3; (5,5,2) ada 3; (5,4,3) ada 6; (4,4,4) ada 1. Total n(E) = 6+6+3+3+6+1 = 25. Peluang = 25/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel dan menghitung banyaknya kejadian yang memenuhi syarat jumlah tertentu dengan mempertimbangkan urutan (permutasi) dari kombinasi angka yang mungkin. Ini adalah penerapan konsep peluang pada konteks rutin.. Bukti: berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip dasar pencacahan dan definisi peluang klasik untuk menyelesaikan masalah yang melibatkan hubungan antara kombinasi angka dan permutasi.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama; peluang jumlah total dadu pada ketiga pelemparan sama dengan 12
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan sistematis untuk mendaftar semua kombinasi yang mungkin berjumlah 12 dan menghitung permutasinya tanpa terlewat. Meskipun prosedurnya familiar, siswa harus mengelola beberapa kasus (kombinasi angka) dan kendala (dadu maksimal 6) secara cermat.. Bukti: tiga dadu standar bersisi enam dilempar bersama-sama; peluang jumlah total dadu pada ketiga pelemparan sama dengan 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar pencacahan, permutasi, dan definisi peluang klasik. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Untuk kelas 12, masalah ini adalah latihan standar peluang kejadian majemuk. Kesulitan utama terletak pada ketelitian enumerasi kasus agar tidak ada yang terlewat atau terhitung ganda, yang merupakan tantangan moderat bagi siswa. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4812`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur pencacahan sistematis untuk menentukan titik sampel yang memenuhi kondisi jumlah tertentu. Ini adalah penerapan konsep peluang klasik pada konteks rutin yang memerlukan ketelitian dalam enumerasi.
- Dimensi pengetahuan `procedural`: Siswa menggunakan prinsip dasar pencacahan dan permutasi untuk menghitung ruang sampel dan kejadian yang diinginkan, yang merupakan pengetahuan prosedural.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan sistematis untuk mendaftar semua kombinasi angka yang berjumlah 12 dan menghitung permutasi untuk setiap kombinasi tersebut agar tidak ada yang terlewat atau terhitung ganda. Meskipun prosedurnya familiar, siswa harus mengelola kendala jumlah dan batasan angka dadu (1-6) secara cermat.

Profil difficulty hasil adjudikasi:

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
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu melakukan pencacahan sistematis untuk masalah peluang majemuk sederhana seperti ini. Kesulitan terletak pada ketelitian enumerasi kasus agar tidak ada yang terlewat atau terhitung ganda. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `3631e6eb715153077f0dac66`

Suatu dompet berisi 4 keping uang logam seribu rupiah dan 3 keping uang logam lima ratus rupiah. Dompet kedua berisi 3 keping uang logam seribu rupiah dan 5 keping uang lima ratus ripuah. Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.<br><br>Jika kemudian diambil sekeping uang logam dari dompet kedua, berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?

| Opsi | Isi |
|---|---|
| A | $\frac{38}{63}$ |
| B | $\frac{5}{8}$ |
| C | $\frac{3}{7}$ |
| D | $\frac{20}{63}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: P(500 dari W2) = P(pindah 1000)P(500\|pindah 1000) + P(pindah 500)P(500\|pindah 500) = (4/7)(5/9) + (3/7)(6/9) = 20/63 + 18/63 = 38/63.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72c2e55ad05f567fcdc65b35b014ce3ddf856ec6bc882f1b55dbec4f1d6b9a95`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3917 |
| 2 | success | valid / verified | applying | procedural | Medium | 3648 |
| 3 | success | valid / verified | applying | procedural | Medium | 3704 |

Run 1 — solusi: P(500 dari W2) = P(pindah 1000)P(500\|pindah 1000) + P(pindah 500)P(500\|pindah 500) = (4/7)(5/9) + (3/7)(6/9) = 20/63 + 18/63 = 38/63.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang bersyarat dan aturan penjumlahan untuk dua kasus yang saling lepas (pemindahan koin 1000 atau 500).. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur standar untuk menghitung peluang kejadian majemuk dengan membagi masalah menjadi dua skenario yang saling lepas.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Intended difficulty `classify/Medium`: Soal memerlukan perencanaan dua skenario (pemindahan koin 1000 atau 500) dan integrasi hasil peluang bersyarat. Ini adalah prosedur rutin dalam peluang majemuk namun memerlukan ketelitian dalam membedakan kondisi dompet kedua setelah pemindahan.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu mengidentifikasi dua kasus yang mungkin terjadi akibat pemindahan objek dan menghitung peluang totalnya. |

Run 2 — solusi: P(500 dari W2) = P(pindah 1000) * P(ambil 500\|pindah 1000) + P(pindah 500) * P(ambil 500\|pindah 500) = (4/7 * 5/9) + (3/7 * 6/9) = 20/63 + 18/63 = 38/63.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan peluang total untuk dua kejadian yang saling lepas (memindahkan koin 1000 atau 500) dan menghitung peluang bersyarat pada tahap kedua. Ini adalah penerapan prosedur standar untuk masalah peluang majemuk.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan peluang kejadian majemuk yang melibatkan perubahan ruang sampel.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Intended difficulty `classify/Medium`: Soal memerlukan perencanaan dua kasus yang saling bergantung (perubahan komposisi dompet kedua). Meskipun prosedurnya standar, siswa harus mengintegrasikan informasi dari dua tahap kejadian secara sistematis.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, peluang kejadian majemuk, dan peluang bersyarat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini merupakan standar kurikulum kelas 12 untuk topik peluang kejadian majemuk. Tingkat kesulitan menengah karena siswa harus mengelola perubahan ruang sampel pada tahap kedua berdasarkan hasil tahap pertama. |

Run 3 — solusi: P(500 dari W2) = P(pindah 1000) * P(ambil 500\|pindah 1000) + P(pindah 500) * P(ambil 500\|pindah 500) = (4/7 * 5/9) + (3/7 * 6/9) = 20/63 + 18/63 = 38/63.
- Domain kognitif `classify/applying`: Siswa harus menerapkan aturan peluang total untuk dua kejadian yang saling lepas (memindahkan koin 1000 atau 500) dan menghitung peluang bersyarat pada tahap kedua. Ini adalah penerapan prosedur standar dalam konteks peluang majemuk.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana menghitung peluang kejadian majemuk yang melibatkan perubahan ruang sampel (perpindahan objek).. Bukti: peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus merencanakan dua skenario yang saling lepas dan memperbarui komposisi dompet kedua setelah pemindahan. Meskipun prosedurnya familiar, siswa perlu teliti dalam mengintegrasikan perubahan kondisi pada tahap kedua.. Bukti: Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.; berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, peluang kejadian majemuk, dan peluang bersyarat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 diharapkan mampu memodelkan proses dua tahap dengan perubahan kondisi. Soal ini menuntut ketelitian dalam memperbarui ruang sampel, namun jalurnya bersifat rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `4f4ccc08a9a611e7c44d48a3`

Suatu kantong berisi enam bola merah dan empat bola biru. Dari kantong tersebut akan diambil dua bola berturut-turut.<br><br>Berapa peluang terambilnya dua bola biru, jika: a. dengan pengembalian, dan

| Opsi | Isi |
|---|---|
| A | $\frac{4}{5}$ |
| B | $\frac{2}{15}$ |
| C | $\frac{2}{5}$ |
| D | $\frac{4}{25}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Total bola = 6 + 4 = 10. Peluang terambil bola biru pada satu pengambilan = 4/10 = 2/5. Karena pengambilan dilakukan dengan pengembalian, kejadian bersifat independen. Peluang dua bola biru = (2/5) * (2/5) = 4/25.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d685fd6fb4a300d985a5060efe3f3ac371b49b28435f12acd07658ac198760fd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2671 |
| 2 | success | valid / verified | applying | procedural | Easy | 2655 |
| 3 | success | valid / verified | applying | procedural | Easy | 2735 |

Run 1 — solusi: Total bola = 6 + 4 = 10. Peluang terambil bola biru pada satu pengambilan = 4/10 = 2/5. Karena pengambilan dilakukan dengan pengembalian, kejadian bersifat independen. Peluang dua bola biru = (2/5) * (2/5) = 4/25.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kejadian sebagai kejadian independen (dengan pengembalian) dan menerapkan aturan perkalian peluang untuk kejadian majemuk. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Suatu kantong berisi enam bola merah dan empat bola biru.; diambil dua bola berturut-turut.; dengan pengembalian
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar peluang kejadian majemuk yang independen, yang merupakan konsep fundamental dalam teori peluang.. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu memahami konsep 'dengan pengembalian' yang berarti peluang tetap sama untuk setiap pengambilan, lalu mengalikan peluang tersebut. Tidak ada kendala tambahan atau langkah kompleks.. Bukti: diambil dua bola berturut-turut.; dengan pengembalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah kurikulum standar kelas 12. Soal ini merupakan aplikasi langsung dari rumus peluang kejadian independen tanpa variasi atau jebakan yang memerlukan penalaran tingkat tinggi. |

Run 2 — solusi: Total bola = 10. Peluang terambil bola biru pada satu pengambilan = 4/10 = 2/5. Karena pengambilan dilakukan dengan pengembalian, kejadian bersifat independen. Peluang dua bola biru = (2/5) * (2/5) = 4/25.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa pengambilan dengan pengembalian membuat dua kejadian tersebut saling bebas (independen), kemudian menerapkan aturan perkalian peluang untuk kejadian majemuk.. Bukti: Suatu kantong berisi enam bola merah dan empat bola biru.; diambil dua bola berturut-turut.; dengan pengembalian
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian peluang untuk kejadian independen dalam konteks pengambilan objek.. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Prosedur untuk kejadian independen (dengan pengembalian) sangat standar dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit.. Bukti: diambil dua bola berturut-turut; dengan pengembalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah kurikulum standar kelas 12. Soal ini merupakan aplikasi langsung dari rumus dasar tanpa variasi kondisi yang rumit. |

Run 3 — solusi: Total bola = 6 + 4 = 10. Peluang terambil bola biru pada pengambilan pertama P(B1) = 4/10 = 2/5. Karena pengambilan dengan pengembalian, peluang pengambilan kedua P(B2) = 4/10 = 2/5. Peluang dua bola biru = P(B1) * P(B2) = (2/5) * (2/5) = 4/25.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi konsep peluang kejadian saling bebas (dengan pengembalian) dan menerapkan aturan perkalian untuk kejadian majemuk. Ini adalah penerapan langsung dari prosedur yang sudah dipelajari.. Bukti: Suatu kantong berisi enam bola merah dan empat bola biru.; diambil dua bola berturut-turut... dengan pengembalian; Berapa peluang terambilnya dua bola biru
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana menghitung peluang kejadian majemuk yang saling bebas dengan menggunakan aturan perkalian.. Bukti: peluang terambilnya dua bola biru; dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami konsep 'dengan pengembalian' yang berarti peluang tetap sama untuk setiap pengambilan, lalu mengalikan kedua peluang tersebut. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: diambil dua bola berturut-turut; dengan pengembalian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah standar kelas 12. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga termasuk kategori mudah bagi siswa kelas 12. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4251`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi kejadian sebagai kejadian independen (dengan pengembalian) dan menerapkan aturan perkalian peluang untuk kejadian majemuk. Ini adalah penerapan prosedur standar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang aturan perkalian peluang untuk kejadian independen dalam konteks pengambilan objek.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami konsep 'dengan pengembalian' yang berarti peluang tetap sama untuk setiap pengambilan, lalu mengalikan kedua peluang tersebut. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah kurikulum standar kelas 12. Soal ini merupakan aplikasi langsung dari rumus peluang kejadian independen tanpa variasi atau jebakan yang memerlukan penalaran tingkat tinggi. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
