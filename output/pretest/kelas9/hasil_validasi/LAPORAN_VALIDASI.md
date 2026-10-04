# Validasi ulang soal kelas 9 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-smp9-key-verified`. Rubrik: `math-rubric-3x4x3-v8-smp9-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 9 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 9, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 22, "knowing": 17, "reasoning": 3}, "knowledgeDimension": {"conceptual": 20, "procedural": 21, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 30, "Medium": 12, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 21, "knowing": 15, "reasoning": 3}, "knowledgeDimension": {"conceptual": 18, "procedural": 20, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 28, "Medium": 11, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 39, "revision_required": 3}`.
Run awal sukses: 126/126; adjudikasi: 18; token sukses tercatat: 461,190.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 30 | 28 | [Easy.json](difficulty/Easy.json) |
| Medium | 12 | 11 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 9, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 9, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 9.

## 1. Soal `8af0a2ca82017a432c92902d`

Diketahui keliling sebuah segitiga sama kaki adalah 48 cm. Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.

| Opsi | Isi |
|---|---|
| A | $x + y = 48$ |
| B | $2x + y = 48$ |
| C | $x + 2y = 48$ |
| D | $2x + 2y = 48$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi berbeda (misal y). Keliling adalah jumlah ketiga sisi: x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `39d20e6d5685b89f46821fc6c55f2511f009c5135dd83bf8cba40c2f29a3388e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2693 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2682 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2691 |

Run 1 — solusi: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi berbeda (misal y). Keliling adalah jumlah ketiga sisi: x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi geometris (segitiga sama kaki) ke dalam bentuk aljabar (persamaan linear dua variabel). Ini melibatkan pemahaman konsep sifat segitiga dan representasi simbolik, yang merupakan penerapan konsep dalam konteks rutin.. Bukti: Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara sifat bangun datar (segitiga sama kaki) dan representasi aljabarnya (persamaan linear).. Bukti: segitiga sama kaki; model matematika yang menghubungkan antara keliling dan panjang sisi
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu menerjemahkan definisi segitiga sama kaki (dua sisi sama, satu sisi berbeda) ke dalam persamaan linear sederhana. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan beban kognitif rendah.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; model matematika yang menghubungkan antara keliling dan panjang sisi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling segitiga dan notasi aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan pemodelan matematika sederhana untuk bangun datar. Tidak ada tuntutan integrasi atau perencanaan yang kompleks. |

Run 2 — solusi: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi alas (misal y). Keliling adalah jumlah ketiga sisi tersebut, yaitu x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi geometris (segitiga sama kaki) ke dalam bentuk aljabar (model matematika). Ini memerlukan pemahaman konsep sifat segitiga sama kaki dan representasi variabel, yang merupakan penerapan konsep pada konteks rutin.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antara properti geometris (segitiga sama kaki) dan representasi simbolik aljabar (persamaan linear).. Bukti: model matematika yang menghubungkan antara keliling dan panjang sisi
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu memahami definisi segitiga sama kaki (dua sisi sama panjang) dan menerjemahkannya ke dalam persamaan linear sederhana. Tidak ada kendala yang berinteraksi atau perencanaan strategis yang kompleks.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; Tentukan model matematika

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling segitiga dan konsep variabel dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan pemodelan matematika sederhana dan sifat-sifat bangun datar dasar. |

Run 3 — solusi: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi alas (misal y). Keliling segitiga adalah jumlah ketiga sisinya, yaitu x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi geometri (segitiga sama kaki) ke dalam bentuk aljabar (model matematika). Ini memerlukan pemahaman konsep sifat segitiga sama kaki dan representasi variabel, yang termasuk dalam domain applying.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antara konsep geometri (sifat segitiga sama kaki) dan representasi simbolik aljabar (persamaan linear), yang merupakan pengetahuan konseptual.. Bukti: model matematika yang menghubungkan antara keliling dan panjang sisi
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu memahami definisi segitiga sama kaki (dua sisi sama panjang) dan menerjemahkannya ke dalam persamaan linear sederhana. Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang berinteraksi.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; Tentukan model matematika

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling segitiga dan konsep variabel dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah familiar dengan pemodelan matematika sederhana. Soal ini bersifat langsung dan tidak memerlukan perencanaan strategi yang rumit. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui keliling sebuah segitiga sama kaki adalah 48 cm. Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.
Pilihan: A. $x + y = 48$
B. $2x + y = 48$
C. $x + 2y = 48$
D. $2x + 2y = 48$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `e7003333bef697d763016f2e`

Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel.<br><br>Diketahui harga tiket film di suatu bioskop Rp35.000,00. y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual.

| Opsi | Isi |
|---|---|
| A | $y = \frac{x}{35.000}$ |
| B | $y = 35.000x$ |
| C | $x = 35.000y$ |
| D | $y = 35.000 + x$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pendapatan (y) adalah hasil kali harga tiket per unit (35.000) dengan jumlah tiket terjual (x). Maka, y = 35.000x.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d2a55c17dfc8b96a39009a1e9dae7becfb990f0973bc8526bc9c789ccdcb1abc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2543 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2553 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2608 |

Run 1 — solusi: Pendapatan (y) diperoleh dari harga per tiket dikalikan jumlah tiket (x). Maka, y = 35.000 * x.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi kontekstual ke dalam model matematika linear sederhana. Ini adalah proses mengenali hubungan antara variabel dan menyusunnya menjadi persamaan, yang merupakan penerapan langsung dari konsep dasar SPLDV.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana variabel-variabel dalam situasi nyata dapat direpresentasikan dalam bentuk persamaan linear.. Bukti: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu memahami hubungan perkalian sederhana antara harga satuan dan kuantitas untuk mendapatkan total pendapatan. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi perkalian dalam konteks aritmatika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal pengenalan model matematika yang sangat standar untuk kelas 9, di mana siswa diharapkan mampu memodelkan situasi linear sederhana. |

Run 2 — solusi: Pendapatan (y) diperoleh dari harga per tiket dikalikan jumlah tiket (x). Maka, y = 35.000 * x.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan situasi kontekstual ke dalam model matematika linear sederhana. Ini adalah proses mengenali hubungan proporsional dan menyatakannya dalam simbol, yang termasuk dalam domain knowing.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana variabel-variabel dalam situasi linear saling berhubungan (pendapatan sebagai fungsi dari jumlah barang).. Bukti: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi hubungan perkalian dasar antara harga satuan dan kuantitas untuk membentuk persamaan. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; harga tiket film di suatu bioskop Rp35.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep perkalian dan variabel dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah tugas dasar dalam pemodelan matematika untuk kelas 9, di mana siswa diharapkan mampu merumuskan persamaan linear sederhana dari konteks sehari-hari. |

Run 3 — solusi: Pendapatan (y) diperoleh dari harga per tiket dikalikan jumlah tiket (x). Maka, y = 35.000 * x.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan situasi kontekstual ke dalam model matematika linear sederhana. Ini adalah prosedur langsung untuk mengenali hubungan perkalian antara variabel.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana variabel dalam persamaan linear dua variabel merepresentasikan hubungan kuantitatif dalam situasi nyata.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengidentifikasi hubungan perkalian antara harga satuan dan jumlah barang untuk membentuk persamaan linear. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perkalian dan konsep variabel dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pengenalan awal terhadap pemodelan SPLDV yang sangat standar untuk kelas 9, sehingga dikategorikan mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4045`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta menerjemahkan hubungan proporsional sederhana dari konteks verbal ke dalam bentuk simbolik persamaan linear. Ini adalah prosedur langsung yang mengenali hubungan perkalian.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang bagaimana variabel dalam persamaan linear merepresentasikan hubungan kuantitatif dalam situasi nyata.
- Intended difficulty `Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengidentifikasi hubungan perkalian antara harga satuan dan jumlah barang untuk membentuk persamaan linear. Tidak ada langkah kompleks, kendala yang berinteraksi, atau kebutuhan perencanaan strategis.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perkalian dan konsep variabel dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah tugas dasar dalam pemodelan matematika untuk kelas 9, di mana siswa diharapkan mampu merumuskan persamaan linear sederhana dari konteks sehari-hari. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel.

Diketahui harga tiket film di suatu bioskop Rp35.000,00. y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual.
Pilihan: A. $y = \frac{x}{35.000}$
B. $y = 35.000x$
C. $x = 35.000y$
D. $y = 35.000 + x$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `0b4b98faa7f553833f0db971`

Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.<br><br>Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?

| Opsi | Isi |
|---|---|
| A | 27 kuas lukis jenis I dan 13 kuas lukis jenis II |
| B | 20 kuas lukis jenis I dan 20 kuas lukis jenis II |
| C | 13 kuas lukis jenis I dan 27 kuas lukis jenis II |
| D | 15 kuas lukis jenis I dan 25 kuas lukis jenis II |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Misal x = jumlah kuas I, y = jumlah kuas II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x + y = 40, maka x = 40 - y. Substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b87a6b3205cfa0b817151e4ef257a562b7268e2f9806ffd0b0fcf2b5e0b199c4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3104 |
| 2 | success | valid / verified | applying | procedural | Medium | 3112 |
| 3 | success | valid / verified | applying | procedural | Easy | 3124 |

Run 1 — solusi: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menerapkan prosedur penyelesaian (substitusi atau eliminasi) untuk menemukan nilai variabel yang tidak diketahui.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritme penyelesaian sistem persamaan linear dua variabel yang merupakan prosedur standar dalam kurikulum kelas 9.. Bukti: Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan rutin SPLDV. Siswa hanya perlu membuat dua persamaan linear sederhana dan menyelesaikannya. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan strategi non-rutin.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, persamaan linear, dan metode substitusi/eliminasi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi inti kelas 9. Soal ini menggunakan konteks belanja yang sangat umum dan familiar, dengan langkah penyelesaian yang langsung dan terstruktur. |

Run 2 — solusi: Misalkan x = jumlah kuas I, y = jumlah kuas II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menerapkan prosedur penyelesaian (substitusi atau eliminasi) untuk menemukan nilai variabel yang memenuhi kedua kendala.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang bagaimana menyusun dan menyelesaikan sistem persamaan linear dua variabel sebagai metode untuk memecahkan masalah aljabar.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemodelan matematika dari situasi nyata dan penyelesaian sistem persamaan linear dua variabel. Meskipun prosedurnya familiar, siswa harus melakukan langkah-langkah yang saling terkait (pemodelan, eliminasi/substitusi, verifikasi) tanpa bantuan langkah demi langkah.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar, sistem persamaan linear dua variabel, dan operasi aritmatika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9, di mana pemodelan SPLDV merupakan kompetensi inti. Tingkat kesulitan menengah karena menuntut ketelitian dalam perhitungan dan pemodelan tanpa bantuan eksplisit. |

Run 3 — solusi: Misal x = jumlah kuas I, y = jumlah kuas II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x + y = 40, maka x = 40 - y. Substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menerapkan prosedur penyelesaian (substitusi atau eliminasi) yang rutin untuk kelas 9.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara variabel dalam sistem persamaan linear dan penggunaan algoritma penyelesaian yang sistematis.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari SPLDV yang familiar bagi siswa kelas 9. Langkah-langkah penyelesaiannya jelas dan prosedural tanpa kendala yang saling berinteraksi secara kompleks.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, persamaan linear, dan metode eliminasi/substitusi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi inti kelas 9. Soal ini menggunakan konteks belanja yang standar dan tidak memerlukan strategi non-rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5475`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menerapkan prosedur penyelesaian (substitusi atau eliminasi) untuk menemukan nilai variabel yang tidak diketahui.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman siswa tentang algoritme penyelesaian sistem persamaan linear dua variabel yang merupakan prosedur standar dalam kurikulum kelas 9.
- Intended difficulty `Easy`: Soal ini adalah penerapan rutin SPLDV. Siswa hanya perlu membuat dua persamaan linear sederhana dan menyelesaikannya. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, persamaan linear, dan metode substitusi/eliminasi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi inti kelas 9. Soal ini menggunakan konteks belanja yang sangat umum dan familiar, dengan langkah penyelesaian yang langsung dan terstruktur. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.

Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
Pilihan: A. 27 kuas lukis jenis I dan 13 kuas lukis jenis II
B. 20 kuas lukis jenis I dan 20 kuas lukis jenis II
C. 13 kuas lukis jenis I dan 27 kuas lukis jenis II
D. 15 kuas lukis jenis I dan 25 kuas lukis jenis II
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `a4219a3c217e0979ca28b57e`

Wayan pergi ke toko kue tradisional untuk membeli kue basung (kue yang berasal dari Sumatera Barat) dan kue mendut (kue yang berasal dari Jawa Tengah). Dia membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00. Di toko yang sama, Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.<br><br>Berapa harga tiga kue mendut dan tujuh kue basung?

| Opsi | Isi |
|---|---|
| A | Rp42.000,00 |
| B | Rp34.500,00 |
| C | Rp37.500,00 |
| D | Rp40.500,00 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Sistem: b+3m=13500 dan 2b+5m=24000. Eliminasi b: 2(b+3m)=27000, kurangi dengan 2b+5m=24000 menghasilkan m=3000. Substitusi m ke b+3(3000)=13500 menghasilkan b=4500. Nilai 3m+7b = 3(3000)+7(4500) = 9000+31500 = 40500.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5a0a3e7cae6cfbb3ecf1c0af78c317160d6d4ad45886cb474ba94325565aafde`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3752 |
| 2 | success | valid / verified | applying | procedural | Medium | 3194 |
| 3 | success | valid / verified | applying | procedural | Medium | 3169 |

Run 1 — solusi: Sistem: b+3m=13500 dan 2b+5m=24000. Eliminasi b: 2(b+3m)=27000, kurangi dengan 2b+5m=24000 menghasilkan m=3000. Substitusi m ke b+3(3000)=13500 menghasilkan b=4500. Nilai 3m+7b = 3(3000)+7(4500) = 9000+31500 = 40500.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur sistem persamaan linear dua variabel (SPLDV) untuk menentukan harga satuan, kemudian menggunakan nilai tersebut untuk menghitung nilai ekspresi linear lainnya. Ini adalah penerapan rutin dari konsep SPLDV.. Bukti: Wayan pergi ke toko kue tradisional untuk membeli kue basung (kue yang berasal dari Sumatera Barat) dan kue mendut (kue yang berasal dari Jawa Tengah). Dia membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00.; Di toko yang sama, Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma penyelesaian SPLDV (eliminasi atau substitusi) yang merupakan prosedur standar dalam aljabar.. Bukti: Berapa harga tiga kue mendut dan tujuh kue basung?
- Intended difficulty `classify/Medium`: Soal dikategorikan Medium karena memerlukan perencanaan multi-langkah: menyusun model matematika, menyelesaikan sistem, dan menghitung nilai akhir. Meskipun prosedurnya familiar bagi siswa kelas 9, terdapat ketergantungan langkah yang jelas.. Bukti: satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar dan metode eliminasi/substitusi SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar SPLDV untuk kelas 9 yang menguji kemampuan menyelesaikan sistem dan melakukan substitusi nilai ke dalam bentuk linear lain. |

Run 2 — solusi: Misalkan b = harga kue basung, m = harga kue mendut. Sistem: b + 3m = 13.500 (1) dan 2b + 5m = 24.000 (2). Dari (1), b = 13.500 - 3m. Substitusi ke (2): 2(13.500 - 3m) + 5m = 24.000 => 27.000 - 6m + 5m = 24.000 => -m = -3.000 => m = 3.000. Maka b = 13.500 - 3(3.000) = 4.500. Harga 3m + 7b = 3(3.000) + 7(4.500) = 9.000 + 31.500 = 40.500.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika SPLDV, menyelesaikan sistem tersebut untuk menemukan harga satuan, dan menerapkan hasil tersebut untuk menghitung harga kombinasi baru. Ini adalah penerapan prosedur rutin dalam konteks.. Bukti: Wayan pergi ke toko kue tradisional untuk membeli kue basung... dan kue mendut... membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme penyelesaian SPLDV (substitusi atau eliminasi) yang merupakan prosedur standar dalam aljabar.. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: memodelkan, menyelesaikan sistem, dan menghitung nilai akhir. Meskipun prosedurnya familiar, siswa harus mengelola beberapa variabel dan melakukan perhitungan berjenjang tanpa bantuan langkah perantara.. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar dan metode penyelesaian SPLDV (eliminasi/substitusi). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menyelesaikan SPLDV dua variabel. Soal ini menuntut ketelitian dalam memodelkan dan menghitung, namun alurnya standar untuk materi tersebut. |

Run 3 — solusi: Misalkan b = harga kue basung dan m = harga kue mendut. Sistem persamaan: (1) b + 3m = 13.500 dan (2) 2b + 5m = 24.000. Dari (1), b = 13.500 - 3m. Substitusi ke (2): 2(13.500 - 3m) + 5m = 24.000 => 27.000 - 6m + 5m = 24.000 => -m = -3.000 => m = 3.000. Maka b = 13.500 - 3(3.000) = 4.500. Harga 3m + 7b = 3(3.000) + 7(4.500) = 9.000 + 31.500 = 40.500.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah cerita ke dalam model matematika SPLDV, menyelesaikan sistem tersebut untuk menemukan harga satuan, lalu menghitung nilai kombinasi baru. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Wayan pergi ke toko kue tradisional untuk membeli kue basung... membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00.; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.; Berapa harga tiga kue mendut dan tujuh kue basung?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian SPLDV (substitusi atau eliminasi) yang merupakan prosedur standar dalam aljabar.. Bukti: satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: memodelkan, menyelesaikan sistem, dan menghitung nilai akhir. Meskipun prosedurnya familiar bagi kelas 9, siswa harus melakukan perencanaan langkah yang berurutan tanpa bantuan eksplisit.. Bukti: satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan dasar aljabar, operasi aritmetika, dan pemahaman konsep SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar kurikulum kelas 9. Memerlukan integrasi antara pemodelan dan perhitungan, namun prosedurnya rutin. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Wayan pergi ke toko kue tradisional untuk membeli kue basung (kue yang berasal dari Sumatera Barat) dan kue mendut (kue yang berasal dari Jawa Tengah). Dia membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00. Di toko yang sama, Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.

Berapa harga tiga kue mendut dan tujuh kue basung?
Pilihan: A. Rp42.000,00
B. Rp34.500,00
C. Rp37.500,00
D. Rp40.500,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 9,45 kali pengangkutan |
| B | 10 kali pengangkutan |
| C | 9 kali pengangkutan |
| D | 11 kali pengangkutan |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Banyak pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `61ae3c8f5be0f920428c60ce7233ac238c73fe68eeb7cd678ed1c48d0f6db730`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2965 |
| 2 | success | valid / verified | applying | procedural | Medium | 2962 |
| 3 | success | valid / verified | applying | procedural | Medium | 2951 |

Run 1 — solusi: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Banyak pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pertidaksamaan/kapasitas untuk menentukan jumlah pengangkutan. Ini melibatkan pemilihan prosedur (pembagian dan pembulatan ke atas) dalam konteks masalah nyata, yang merupakan penerapan konsep.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika (pengurangan, pembagian) dan prinsip pembulatan ke atas (kontekstual) untuk menyelesaikan masalah kapasitas.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah terintegrasi: menghitung kapasitas bersih, menentukan kapasitas per angkut, dan melakukan pembulatan ke atas yang logis sesuai konteks (bukan sekadar pembulatan matematis biasa).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep kapasitas/pertidaksamaan sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu memodelkan masalah kapasitas sederhana dan memahami bahwa dalam konteks pengangkutan, hasil pecahan harus dibulatkan ke atas untuk memastikan semua barang terangkut. |

Run 2 — solusi: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Total pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pertidaksamaan/kapasitas angkut untuk menentukan jumlah pengangkutan. Siswa harus mengintegrasikan informasi berat total, berat pengemudi, dan berat per kotak untuk menentukan kapasitas per angkut, kemudian melakukan pembulatan ke atas (kontekstual) untuk menjawab masalah.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika dasar dan pemahaman konsep kapasitas (pertidaksamaan) untuk menyelesaikan masalah dunia nyata.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: menghitung kapasitas bersih, menghitung kapasitas per angkut, dan melakukan pembulatan ke atas yang tepat sesuai konteks masalah (bukan pembulatan matematis biasa).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar dan pemahaman konsep kapasitas/pertidaksamaan sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pemodelan sederhana terkait kapasitas dan memahami perlunya pembulatan ke atas dalam konteks pengangkutan barang. |

Run 3 — solusi: Kapasitas muatan barang = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Banyak pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kendala kapasitas (pengurangan berat pengemudi), menentukan kapasitas muatan per perjalanan, dan menerapkan pembulatan ke atas (ceiling function) dalam konteks dunia nyata untuk memastikan semua kotak terangkut.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika dasar dan konsep pertidaksamaan/pembagian untuk memecahkan masalah kapasitas angkut yang kontekstual.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah logis: menghitung kapasitas bersih (pengurangan berat pengemudi) dan menerapkan pembulatan ke atas (ceiling) yang sering menjadi jebakan bagi siswa, meskipun operasi dasarnya rutin.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep kapasitas/pertidaksamaan sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu memodelkan masalah kapasitas sederhana dan memahami implikasi pembulatan dalam konteks jumlah perjalanan/benda. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.

Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
Pilihan: A. 9,45 kali pengangkutan
B. 10 kali pengangkutan
C. 9 kali pengangkutan
D. 11 kali pengangkutan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `6d6cb72cedbdc46857aa2701`

Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....

| Opsi | Isi |
|---|---|
| A | 4x + 3y - 14 = 0 |
| B | 3x + 4y - 14 = 0 |
| C | 4x - 3y + 14 = 0 |
| D | 3x - 4y + 33 = 0 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S memiliki koordinat (6,-1) dan (2,2). Kemiringan (m) garis QS = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis: y - 2 = -3/4(x - 2) atau 4y - 8 = -3x + 6, yang disederhanakan menjadi 3x + 4y - 14 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4a9d31abca3ef846caf7f6bf020d8fc7b3339b7549e13c8650257ebd542f4237`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2868 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2900 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2885 |

Run 1 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S memiliki koordinat (6,-1) dan (2,2). Kemiringan (m) garis QS = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis: y - 2 = -3/4(x - 2) atau 4y - 8 = -3x + 6, yang disederhanakan menjadi 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat geometri persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S dari titik P dan R, kemudian menerapkan prosedur mencari persamaan garis melalui dua titik.. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara sifat geometri (persegi panjang sejajar sumbu) dengan representasi koordinat, serta prosedur aljabar untuk menentukan persamaan garis.. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan inferensi geometri (menentukan koordinat Q dan S) sebelum menerapkan prosedur standar persamaan garis. Langkah-langkahnya saling bergantung namun prosedurnya familiar bagi siswa kelas 9.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan; sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, sifat persegi panjang, dan rumus persamaan garis melalui dua titik. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghubungkan sifat geometri dengan koordinat. Menentukan titik Q dan S dari P dan R adalah langkah krusial yang memerlukan pemahaman konsep, bukan sekadar substitusi rumus. |

Run 2 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S memiliki koordinat (6,-1) dan (2,2). Kemiringan garis QS adalah m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4 adalah y - 2 = -3/4(x - 2), yang disederhanakan menjadi 4y - 8 = -3x + 6, atau 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat geometri persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S dari titik P dan R, kemudian menerapkan rumus kemiringan dan persamaan garis.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang hubungan koordinat titik pada persegi panjang yang sejajar sumbu dan prosedur aljabar untuk menyusun persamaan garis.. Bukti: titik sudut yang berhadapan; persamaan garis yang melalui titik Q dan S
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap integrasi: (1) deduksi koordinat titik Q dan S berdasarkan sifat persegi panjang yang sejajar sumbu, dan (2) perhitungan persamaan garis. Tidak ada bantuan langsung untuk koordinat Q dan S, sehingga siswa harus membangun pemahaman spasial tersebut sendiri.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, sifat persegi panjang, dan rumus persamaan garis (y-y1 = m(x-x1)). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghubungkan sifat geometri bangun datar dengan koordinat kartesius. Soal ini menuntut kemampuan deduksi koordinat yang menjadi prasyarat sebelum melakukan prosedur aljabar standar. |

Run 3 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S harus memiliki koordinat yang dibentuk dari kombinasi koordinat P(2,-1) dan R(6,2). Maka Q(6,-1) dan S(2,2). Kemiringan garis QS = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis: y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara titik sudut persegi panjang yang sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus kemiringan dan persamaan garis. Ini melibatkan penerapan konsep geometri koordinat pada konteks rutin.. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman prinsip geometri koordinat (sifat persegi panjang dengan sisi sejajar sumbu) dan prosedur aljabar untuk menyusun persamaan garis.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan; sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep bahwa sisi sejajar sumbu berarti koordinat x dan y titik sudut lainnya (Q dan S) adalah kombinasi dari koordinat P dan R. Setelah koordinat ditemukan, langkah selanjutnya adalah prosedur standar mencari persamaan garis. Tidak ada kendala yang berinteraksi secara kompleks.. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep koordinat kartesius, kemiringan garis, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengintegrasikan sifat bangun datar dengan koordinat kartesius. Menentukan titik Q dan S dari P dan R adalah langkah kunci yang memerlukan pemahaman konsep, namun prosedurnya standar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pengertian Kemiringan
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....
Pilihan: A. 4x + 3y - 14 = 0
B. 3x + 4y - 14 = 0
C. 4x - 3y + 14 = 0
D. 3x - 4y + 33 = 0
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d0b943d7f97005ee05dfe7b2`

Dapatkah kita membuat jaring-jaring bangun ruang bola?

| Opsi | Isi |
|---|---|
| A | Hanya kerucut dan tabung yang bisa dibuat jaring-jaringnya, bola tidak |
| B | Tidak, sama sekali tidak mungkin dibuat |
| C | Ya, tetapi hasilnya selalu berbentuk persegi panjang |
| D | Ya, jaring-jaring bangun ruang bola dapat dibuat |

Kunci sumber: `D`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Bola adalah permukaan non-developable. Secara matematis, bola tidak memiliki jaring-jaring karena permukaannya tidak dapat dibentangkan menjadi bidang datar tanpa distorsi atau pemotongan yang mengubah bentuk aslinya secara fundamental.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a7699d91cdc2bb8c87fed17a02495556854265c0fdaf887aec8a6b0ea940c598`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | knowing | conceptual | Easy | 3714 |
| 2 | success | concern / conflict | knowing | conceptual | Easy | 2725 |
| 3 | success | concern / conflict | knowing | conceptual | Easy | 3740 |

Run 1 — solusi: Secara matematis, bola tidak memiliki jaring-jaring karena permukaannya tidak dapat didatarkan tanpa distorsi. Kunci jawaban sumber (D) bertentangan dengan definisi geometri standar mengenai jaring-jaring bangun ruang.
- Domain kognitif `classify/knowing`: Soal menuntut pengenalan fakta atau definisi mengenai sifat bangun ruang.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep dasar mengenai sifat bangun ruang dan jaring-jaring.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Intended difficulty `classify/Easy`: Soal hanya menuntut ingatan atau pemahaman konsep dasar. Tidak ada langkah perhitungan atau integrasi.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang sisi lengkung. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pertanyaan bersifat teoretis dan tidak memerlukan prosedur kompleks. |

Run 2 — solusi: Bola tidak memiliki jaring-jaring dalam pengertian geometri bangun ruang karena permukaannya tidak dapat dibentangkan menjadi bidang datar tanpa distorsi atau pemotongan yang mengubah bentuk aslinya secara fundamental.
- Domain kognitif `classify/knowing`: Soal menuntut pemahaman konseptual tentang definisi jaring-jaring bangun ruang. Siswa perlu mengklasifikasikan apakah sifat permukaan bola memungkinkan representasi jaring-jaring.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pengetahuan faktual/konseptual mengenai definisi dan karakteristik jaring-jaring bangun ruang.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan menguji pemahaman definisi. Namun, karena kunci jawaban sumber secara matematis tidak akurat (konflik konten), tingkat kesulitan tidak dapat dinilai secara valid sebagai materi pembelajaran yang benar.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jaring-jaring bangun ruang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal hanya menanyakan definisi dasar, namun kontennya bermasalah secara matematis. |

Run 3 — solusi: Bola adalah permukaan non-developable. Bola tidak memiliki jaring-jaring karena tidak dapat dibentangkan pada bidang datar tanpa distorsi.
- Domain kognitif `classify/knowing`: Soal menanyakan pemahaman konsep dasar tentang jaring-jaring bangun ruang.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep jaring-jaring.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana (recall konsep), namun memiliki masalah validitas konten yang fatal.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jaring-jaring bangun ruang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal menanyakan konsep dasar. Namun, karena kunci jawaban salah secara matematis, soal ini bermasalah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3826`.
Konten: `concern`; kunci: `conflict`; masalah: Soal secara matematis tidak akurat. Bola adalah permukaan non-developable (tidak dapat didatarkan), sehingga secara definisi geometri standar, bola tidak memiliki jaring-jaring. Klaim bahwa jaring-jaring bola dapat dibuat adalah keliru secara konsep..
- Domain kognitif `knowing`: Soal menuntut pengenalan konsep dasar mengenai sifat bangun ruang dan definisi jaring-jaring.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual mengenai karakteristik bangun ruang sisi lengkung.
- Intended difficulty `Easy`: Soal bersifat teoretis dan menuntut pemahaman definisi dasar. Namun, karena kunci jawaban sumber secara matematis tidak akurat (konflik konten), tingkat kesulitan tidak dapat dinilai secara valid sebagai materi pembelajaran yang benar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jaring-jaring bangun ruang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pertanyaan bersifat teoretis dan tidak memerlukan prosedur kompleks, namun memiliki masalah validitas konten yang fatal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Klasifikasi Bangun Ruang dan Jaring-Jaring
Tipe soal: multiple_choice
Stimulus: -
Soal: Dapatkah kita membuat jaring-jaring bangun ruang bola?
Pilihan: A. Hanya kerucut dan tabung yang bisa dibuat jaring-jaringnya, bola tidak
B. Tidak, sama sekali tidak mungkin dibuat
C. Ya, tetapi hasilnya selalu berbentuk persegi panjang
D. Ya, jaring-jaring bangun ruang bola dapat dibuat
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal secara matematis tidak akurat. Bola adalah permukaan non-developable (tidak dapat didatarkan), sehingga secara definisi geometri standar, bola tidak memiliki jaring-jaring. Klaim bahwa jaring-jaring bola dapat dibuat adalah keliru secara konsep..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `394ec3b5c5b98c434a4cedde`

Apa yang dimaksud dengan jaring-jaring bangun ruang?

| Opsi | Isi |
|---|---|
| A | Kumpulan rusuk yang membentuk kerangka luar suatu bangun ruang |
| B | Bagian permukaan bangun ruang yang terlihat dari luar saja |
| C | Bentuk tiga dimensi yang menunjukkan besar ruang yang ditempati suatu bangun ruang |
| D | Bentuk dua dimensi yang dapat digambar, dipotong, dan dirangkai sedemikian rupa sehingga menjadi sebuah bangun tiga dimensi |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Jaring-jaring bangun ruang adalah bidang datar (dua dimensi) yang terdiri dari gabungan bangun datar yang jika dilipat atau dirangkai menurut garis-garis lipatannya akan membentuk bangun ruang tiga dimensi tertentu. Pilihan D adalah definisi yang tepat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `229924a8075a00e189a87546f44af21782626dd020bd2947ea5c430466f822b7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2586 |
| 2 | success | valid / verified | knowing | factual | Easy | 2584 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2573 |

Run 1 — solusi: Jaring-jaring bangun ruang adalah representasi dua dimensi dari sisi-sisi bangun ruang yang jika dilipat atau dirangkai akan membentuk bangun tiga dimensi tersebut. Pilihan D secara akurat mendeskripsikan proses ini.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali definisi konseptual dasar dari jaring-jaring bangun ruang. Siswa hanya perlu mengingat dan mengidentifikasi definisi yang benar di antara pilihan yang tersedia tanpa melakukan perhitungan atau analisis kompleks.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap terminologi dan konsep dasar geometri (jaring-jaring), yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Intended difficulty `classify/Easy`: Soal ini bersifat definisional dan sangat mendasar bagi siswa kelas 9. Tidak ada langkah perhitungan, perencanaan, atau integrasi konsep yang diperlukan. Siswa hanya perlu memahami istilah yang sudah dipelajari di jenjang sebelumnya.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang sisi datar dan sisi lengkung. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji pemahaman konsep dasar yang seharusnya sudah dikuasai siswa SMP kelas 9. Tidak ada tuntutan kognitif tinggi. |

Run 2 — solusi: Jaring-jaring bangun ruang adalah representasi dua dimensi dari permukaan bangun ruang yang jika dilipat atau dirangkai sesuai garis lipatannya akan membentuk bangun tiga dimensi tersebut. Pilihan D secara akurat mendeskripsikan proses ini.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali definisi konseptual dari jaring-jaring bangun ruang. Siswa hanya perlu mengingat dan mengidentifikasi fakta/definisi yang benar di antara pilihan yang tersedia.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap istilah dan definisi dasar dalam geometri bangun ruang, yang termasuk dalam kategori pengetahuan faktual/konseptual dasar.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Intended difficulty `classify/Easy`: Soal ini bersifat definisional dan sangat langsung. Tidak ada langkah perhitungan, analisis, atau integrasi konsep yang diperlukan. Siswa hanya perlu memahami terminologi dasar yang diajarkan di tingkat SMP.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan komponennya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Definisi jaring-jaring adalah materi dasar geometri yang sudah diperkenalkan sejak jenjang SD dan diperdalam di SMP. Soal ini tidak menuntut penalaran kompleks, hanya pengenalan konsep. |

Run 3 — solusi: Jaring-jaring bangun ruang adalah representasi dua dimensi dari permukaan bangun ruang yang jika dilipat atau dirangkai akan membentuk bangun tiga dimensi tersebut. Pilihan D secara akurat mendeskripsikan proses ini.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengenali definisi konseptual dari jaring-jaring bangun ruang. Siswa hanya perlu mengingat dan mengidentifikasi definisi yang benar di antara pilihan yang tersedia tanpa perlu melakukan perhitungan atau analisis mendalam.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap istilah dan definisi dasar dalam geometri, yang merupakan bagian dari pengetahuan konseptual.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar (definisi). Tidak ada langkah penyelesaian yang diperlukan selain mengingat konsep. Siswa kelas 9 seharusnya sudah sangat familiar dengan istilah ini sejak jenjang sebelumnya.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan jaring-jaringnya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini hanya menanyakan definisi teoretis yang sangat mendasar. Tidak ada tuntutan kognitif tinggi atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3974`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya meminta siswa untuk mengenali definisi konseptual dari jaring-jaring bangun ruang. Tidak ada proses analisis, perhitungan, atau pemecahan masalah yang diperlukan, sehingga masuk dalam domain knowing.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman siswa terhadap terminologi dan konsep dasar geometri, yang merupakan pengetahuan konseptual.
- Intended difficulty `Easy`: Soal ini bersifat definisional dan sangat mendasar. Tidak ada langkah perencanaan, integrasi konsep, atau perhitungan yang diperlukan. Siswa hanya perlu mengingat definisi yang sudah dipelajari.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan komponennya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Definisi jaring-jaring adalah materi dasar geometri yang sudah diperkenalkan sejak jenjang SD dan diperdalam di SMP. Soal ini tidak menuntut penalaran kompleks, hanya pengenalan konsep. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Klasifikasi Bangun Ruang dan Jaring-Jaring
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa yang dimaksud dengan jaring-jaring bangun ruang?
Pilihan: A. Kumpulan rusuk yang membentuk kerangka luar suatu bangun ruang
B. Bagian permukaan bangun ruang yang terlihat dari luar saja
C. Bentuk tiga dimensi yang menunjukkan besar ruang yang ditempati suatu bangun ruang
D. Bentuk dua dimensi yang dapat digambar, dipotong, dan dirangkai sedemikian rupa sehingga menjadi sebuah bangun tiga dimensi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `ee45c96e4346ffea193e7a99`

Sebuah kotak pensil terbuat dari logam dengan dimensi 20 cm × 10 cm × 3 cm. Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.

| Opsi | Isi |
|---|---|
| A | 580 cm² |
| B | 600 cm² |
| C | 520 cm² |
| D | 290 cm² |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Luas permukaan balok = 2 * (p*l + p*t + l*t) = 2 * (20*10 + 20*3 + 10*3) = 2 * (200 + 60 + 30) = 2 * 290 = 580 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `427157f9b23d6d9bbc1249772cfad63527d5e3b3f04bf756790fa32abb4fe3bf`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3396 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3254 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3400 |

Run 1 — solusi: Luas permukaan balok = 2 * (p*l + p*t + l*t) = 2 * (20*10 + 20*3 + 10*3) = 2 * (200 + 60 + 30) = 2 * 290 = 580 cm².
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan rumus luas permukaan balok secara langsung pada dimensi yang diberikan tanpa modifikasi atau penalaran tambahan.. Bukti: Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang rumus luas permukaan balok untuk menyelesaikan masalah.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan substitusi nilai ke dalam rumus luas permukaan balok tanpa kendala tambahan atau integrasi konsep yang kompleks.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan balok |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah familiar dengan rumus luas permukaan balok dan soal ini tidak menuntut langkah tambahan atau analisis mendalam. |

Run 2 — solusi: Luas permukaan balok = 2(pl + pt + lt) = 2(20*10 + 20*3 + 10*3) = 2(200 + 60 + 30) = 2(290) = 580 cm².
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan rumus luas permukaan balok secara langsung pada dimensi yang diberikan.. Bukti: Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep luas permukaan balok sebagai jumlah luas sisi-sisinya.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi dimensi dan menerapkan rumus luas permukaan balok tanpa kendala tambahan atau integrasi kompleks.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan balok dan operasi perkalian/penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah familiar dengan rumus luas permukaan bangun ruang sisi datar. Soal ini tidak memerlukan langkah perencanaan atau integrasi yang menantang. |

Run 3 — solusi: Luas permukaan balok = 2(pl + pt + lt) = 2(20*10 + 20*3 + 10*3) = 2(200 + 60 + 30) = 2(290) = 580 cm².
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan rumus luas permukaan balok secara langsung pada dimensi yang diberikan tanpa modifikasi.. Bukti: Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep luas permukaan balok sebagai jumlah luas sisi-sisinya.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan prosedur yang jelas. Siswa hanya perlu menerapkan rumus luas permukaan balok tanpa ada kendala tambahan atau integrasi konsep yang kompleks.. Bukti: dimensi 20 cm × 10 cm × 3 cm; Hitunglah berapa luas logam yang dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan balok dan operasi perkalian/penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas permukaan balok adalah standar kelas 9, dan soal ini merupakan penerapan langsung tanpa modifikasi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4077`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung rumus luas permukaan balok pada dimensi yang diberikan. Tidak ada modifikasi, analisis, atau penalaran non-rutin yang diperlukan.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep luas permukaan balok sebagai jumlah luas sisi-sisinya dan menerapkan prosedur perhitungan yang sesuai.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi dimensi dan menerapkan rumus luas permukaan balok tanpa kendala tambahan atau integrasi konsep yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan balok dan operasi aritmatika dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas permukaan balok adalah standar kelas 9, dan soal ini merupakan penerapan langsung tanpa modifikasi atau tuntutan perencanaan yang tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak pensil terbuat dari logam dengan dimensi 20 cm × 10 cm × 3 cm. Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.
Pilihan: A. 580 cm²
B. 600 cm²
C. 520 cm²
D. 290 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `27c5fab7664c58cab4d858b0`

Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

| Opsi | Isi |
|---|---|
| A | 0,0529 m² |
| B | 1,38 m² |
| C | 0,3174 m² |
| D | 0,012167 m² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, luas permukaan = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e73466940e6de1fbc5a0d60ffacfd0d1e7549592340d19335628d4896760ac59`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2652 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3295 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3352 |

Run 1 — solusi: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, luas permukaan = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus luas permukaan kubus. Siswa hanya perlu mengenali rumus dan melakukan perhitungan dasar.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang rumus luas permukaan kubus dan kemampuan melakukan operasi perkalian desimal.. Bukti: Temukan luas permukaan kubus
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu menerapkan rumus luas permukaan kubus (6s²) secara langsung. Tidak ada langkah perencanaan, integrasi, atau kendala yang kompleks.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan kubus dan operasi perkalian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan rumus standar yang diajarkan di tingkat SMP. Tidak ada tuntutan kognitif tinggi. |

Run 2 — solusi: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, Luas = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus luas permukaan kubus (6s²) dengan nilai yang sudah diberikan. Tidak ada langkah penalaran atau integrasi konsep yang diperlukan.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Dimensi pengetahuan `classify/procedural`: Siswa hanya perlu mengingat rumus luas permukaan kubus dan melakukan operasi perkalian desimal secara prosedural.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung rumus luas permukaan kubus. Siswa hanya perlu mensubstitusi nilai sisi ke dalam rumus 6s². Tidak ada kendala interaktif atau perencanaan strategi yang kompleks.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan kubus (6s²) dan operasi perkalian desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah familiar dengan rumus bangun ruang sisi datar. Soal ini bersifat rutin dan langsung. |

Run 3 — solusi: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, luas = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus luas permukaan kubus (6s²) dengan nilai yang sudah diketahui. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui rumus luas permukaan kubus dan melakukan operasi perkalian desimal yang bersifat prosedural.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu memasukkan nilai ke dalam rumus yang sudah familiar. Tidak ada kendala interaksi, perencanaan langkah, atau perpindahan representasi yang menantang.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan kubus (6s²) dan operasi perkalian desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 seharusnya sudah sangat familiar dengan rumus bangun ruang sisi datar sederhana. Soal ini hanya menguji ingatan rumus dan ketelitian hitung dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
Pilihan: A. 0,0529 m²
B. 1,38 m²
C. 0,3174 m²
D. 0,012167 m²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `aee8fd25cf246c58a370058e`

Sebuah balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7. Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.

| Opsi | Isi |
|---|---|
| A | 420 satuan kubik |
| B | 1.680 satuan kubik |
| C | 105 satuan kubik |
| D | 6.720 satuan kubik |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Volume awal balok adalah 5 x 3 x 7 = 105 satuan kubik. Jika ukuran balok diubah dengan skala k = 4, maka volume baru adalah V_baru = V_awal x k^3 = 105 x 4^3 = 105 x 64 = 6.720 satuan kubik.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6156e4c2dd33ca4a4b2099bfe84124b1f98b055cb9525fffcaadbb2ccf993dd6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2716 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2726 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2738 |

Run 1 — solusi: Volume awal balok adalah 5 x 3 x 7 = 105 satuan kubik. Jika ukuran balok diubah dengan skala k = 4, maka volume baru adalah V_baru = V_awal x k^3 = 105 x 4^3 = 105 x 64 = 6.720 satuan kubik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan volume bangun ruang akibat dilatasi (skala k), yaitu volume baru adalah volume awal dikali k pangkat tiga. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana perubahan dimensi linear (skala) mempengaruhi volume (tiga dimensi), yang merupakan prinsip dasar dalam geometri bangun ruang.. Bukti: diubah ukurannya dengan skala 4; tentukan volume balok setelah diubah
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat langsung dan familiar bagi siswa kelas 9. Siswa hanya perlu menghitung volume awal dan mengalikannya dengan faktor skala pangkat tiga (k^3). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: panjang 5, lebar 3, dan tinggi 7; skala 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep volume balok dan pemahaman dasar tentang dilatasi/skala. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi dan perubahan volume adalah standar kelas 9. Soal ini tidak menuntut integrasi kompleks, hanya penerapan rumus yang sudah dipelajari. |

Run 2 — solusi: Volume awal balok adalah 5 x 3 x 7 = 105 satuan kubik. Karena skala perubahan adalah 4, maka volume baru adalah 105 x (4^3) = 105 x 64 = 6.720 satuan kubik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan volume bangun ruang akibat dilatasi (skala k) dengan menggunakan faktor skala pangkat tiga (k^3). Ini adalah penerapan prosedur pada konteks yang rutin.. Bukti: Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana faktor skala mempengaruhi volume bangun ruang (hubungan k^3).. Bukti: diubah ukurannya dengan skala 4; tentukan volume balok setelah diubah
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari rumus volume dan konsep dilatasi bangun ruang yang umum di kelas 9. Langkah penyelesaiannya jelas dan tidak memerlukan integrasi kendala yang kompleks.. Bukti: balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7; diubah ukurannya dengan skala 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume balok dan konsep dilatasi/skala pada bangun ruang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi dan perubahan volume adalah standar kelas 9. Soal ini tidak menuntut penalaran non-rutin atau integrasi konsep yang sulit. |

Run 3 — solusi: Volume awal balok = 5 * 3 * 7 = 105. Jika skala perubahan adalah k=4, maka volume baru = V_awal * k^3 = 105 * 4^3 = 105 * 64 = 6.720.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan volume bangun ruang akibat dilatasi (skala k) dengan menggunakan faktor skala pangkat tiga (k^3). Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana faktor skala mempengaruhi volume bangun ruang (k^3), bukan sekadar menghitung volume awal.. Bukti: diubah ukurannya dengan skala 4; tentukan volume balok setelah diubah
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar bagi siswa kelas 9. Siswa hanya perlu menghitung volume awal dan mengalikannya dengan faktor skala pangkat tiga. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7; diubah ukurannya dengan skala 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume balok dan konsep dilatasi/skala pada bangun ruang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi dan perubahan volume adalah kurikulum standar kelas 9. Prosedur penyelesaian bersifat langsung dan rutin. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7. Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.
Pilihan: A. 420 satuan kubik
B. 1.680 satuan kubik
C. 105 satuan kubik
D. 6.720 satuan kubik
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `bc9eda46aa2fecb0da3798d8`

Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

| Opsi | Isi |
|---|---|
| A | Volume limas adalah setengah dari volume prisma |
| B | Volume limas adalah tiga kali volume prisma |
| C | Volume limas tersebut adalah sepertiga dari volume prisma |
| D | Volume limas sama dengan volume prisma |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Volume prisma dengan luas alas A dan tinggi t adalah V_prisma = A * t. Volume limas dengan luas alas A dan tinggi t adalah V_limas = 1/3 * A * t. Dengan membandingkan keduanya, V_limas = 1/3 * V_prisma.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7fdaded8b7eeff1bb5a34db0c0435b525abc129292e587d7966eb91c8cd48e48`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3135 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3260 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3211 |

Run 1 — solusi: Volume prisma dengan luas alas A dan tinggi t adalah V_prisma = A * t. Volume limas dengan luas alas A dan tinggi t adalah V_limas = 1/3 * A * t. Dengan membandingkan keduanya, V_limas = 1/3 * V_prisma.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat atau mengenali hubungan konseptual dasar antara volume limas dan prisma yang memiliki alas dan tinggi yang sama. Tidak ada prosedur kompleks atau penalaran non-rutin yang diperlukan.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Pertanyaan ini menguji pemahaman prinsip geometris mengenai hubungan antara dua bangun ruang, yang merupakan pengetahuan konseptual.. Bukti: Bagaimana kaitan antara volume limas dan prisma
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman definisi/teorema dasar yang diajarkan di kelas 9. Tidak ada langkah-langkah yang saling bergantung atau kendala yang harus diintegrasikan.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus volume prisma dan limas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pertanyaan ini adalah recall konsep dasar yang sangat familiar bagi siswa kelas 9. Tidak ada beban kognitif tinggi dalam perencanaan atau integrasi. |

Run 2 — solusi: Volume prisma = Luas alas x tinggi. Volume limas = 1/3 x Luas alas x tinggi. Jika alas dan tinggi sama, maka volume limas = 1/3 x volume prisma.
- Domain kognitif `classify/knowing`: Soal menanyakan pemahaman dasar mengenai hubungan rumus volume dua bangun ruang yang sudah menjadi standar kurikulum SMP.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau hubungan konseptual antara volume limas dan prisma.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (recall/pemahaman dasar) tanpa memerlukan perhitungan atau perencanaan langkah yang kompleks.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume prisma dan limas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi dasar geometri kelas 9 yang diajarkan secara eksplisit. |

Run 3 — solusi: Volume prisma = Luas alas x tinggi. Volume limas = 1/3 x Luas alas x tinggi. Jika alas dan tinggi sama, maka Volume limas = 1/3 x Volume prisma.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengingat atau memahami hubungan konseptual dasar antara volume limas dan prisma yang memiliki alas dan tinggi yang sama.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap prinsip atau rumus geometri dasar, yang merupakan pengetahuan konseptual.. Bukti: Bagaimana kaitan antara volume limas dan prisma
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung mengenai hubungan rumus volume. Tidak ada langkah perhitungan atau integrasi yang diperlukan.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume prisma dan limas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar geometri yang diajarkan di kelas 9. Soal hanya menanyakan hubungan rumus tanpa perlu perhitungan. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
Pilihan: A. Volume limas adalah setengah dari volume prisma
B. Volume limas adalah tiga kali volume prisma
C. Volume limas tersebut adalah sepertiga dari volume prisma
D. Volume limas sama dengan volume prisma
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `b0484eaccca405ba34c3f428`

Untuk tiap-tiap lingkaran yang diketahui r (panjang jari-jari) atau d (panjang diameter) berikut, tentukan keliling dan luasnya! ⓐ r = 12 cm

| Opsi | Isi |
|---|---|
| A | Keliling 75,36 cm dan luas 75,36 cm² |
| B | Keliling 452,16 cm dan luas 75,36 cm² |
| C | Keliling 75,36 cm dan luas 452,16 cm² |
| D | Keliling 37,68 cm dan luas 452,16 cm² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Keliling = 2 * 3,14 * 12 = 75,36 cm. Luas = 3,14 * 12^2 = 3,14 * 144 = 452,16 cm^2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `44822528fbf763c1afa91b60d60f4e79ec366cb5213cc31618b2c9fcc28f6968`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3353 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3424 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2616 |

Run 1 — solusi: Keliling = 2 * 3,14 * 12 = 75,36 cm. Luas = 3,14 * 12^2 = 3,14 * 144 = 452,16 cm^2.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus keliling dan luas lingkaran yang sudah diketahui. Tidak ada proses penalaran atau strategi non-rutin yang diperlukan.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Dimensi pengetahuan `classify/procedural`: Siswa hanya perlu menjalankan prosedur atau algoritma standar (rumus) untuk menghitung keliling dan luas lingkaran.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, menguji ingatan dan penerapan rumus dasar lingkaran yang merupakan materi prasyarat atau dasar di kelas 9.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus keliling (2πr) dan luas lingkaran (πr²) |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan dasar yang sangat familiar bagi siswa kelas 9. Tidak ada tuntutan integrasi konsep atau kendala yang kompleks. |

Run 2 — solusi: Keliling = 2 * 3,14 * 12 = 75,36 cm. Luas = 3,14 * 12^2 = 3,14 * 144 = 452,16 cm^2.
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan rumus keliling dan luas lingkaran secara langsung dengan nilai jari-jari yang sudah diketahui.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar mengenai rumus keliling dan luas lingkaran.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Intended difficulty `classify/Easy`: Soal ini sangat rutin, hanya memerlukan substitusi nilai ke dalam rumus yang sudah dikenal di kelas 9.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus keliling (2πr) dan luas (πr²) lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan rumus dasar lingkaran. Tidak ada integrasi konsep atau kendala yang kompleks. |

Run 3 — solusi: Diketahui r = 12 cm. Keliling (K) = 2πr = 2 × 3,14 × 12 = 75,36 cm. Luas (L) = πr² = 3,14 × 12² = 3,14 × 144 = 452,16 cm². Hasil yang sesuai adalah K = 75,36 cm dan L = 452,16 cm².
- Domain kognitif `classify/knowing`: Soal meminta siswa menerapkan rumus keliling dan luas lingkaran secara langsung dengan nilai jari-jari yang sudah diberikan. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui dan menerapkan rumus dasar keliling (2πr) dan luas (πr²) lingkaran.. Bukti: tentukan keliling dan luasnya
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan prosedur yang sangat jelas dan langsung. Siswa hanya perlu mensubstitusi nilai jari-jari ke dalam rumus yang sudah familiar di kelas 9.. Bukti: r = 12 cm; tentukan keliling dan luasnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus keliling dan luas lingkaran serta operasi perkalian desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar yang sangat umum di kelas 9, tidak memerlukan penalaran tingkat tinggi atau integrasi konsep. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk tiap-tiap lingkaran yang diketahui r (panjang jari-jari) atau d (panjang diameter) berikut, tentukan keliling dan luasnya! ⓐ r = 12 cm
Pilihan: A. Keliling 75,36 cm dan luas 75,36 cm²
B. Keliling 452,16 cm dan luas 75,36 cm²
C. Keliling 75,36 cm dan luas 452,16 cm²
D. Keliling 37,68 cm dan luas 452,16 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ce529c7a884ca9ebbfb36e54`

Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar ____.

| Opsi | Isi |
|---|---|
| A | 22 |
| B | 3,14 (atau 22/7) |
| C | 3,41 |
| D | 2 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Berdasarkan definisi konstanta pi (π), perbandingan antara keliling lingkaran (K) dan diameternya (d) adalah K/d = π. Nilai pendekatan untuk π adalah 3,14 atau 22/7.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a893f69afbb2b85a095a383b8ca338911676d72a71cad2e74902ac15c9ca2f7c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2552 |
| 2 | success | valid / verified | knowing | factual | Easy | 2542 |
| 3 | success | valid / verified | knowing | factual | Easy | 3532 |

Run 1 — solusi: Definisi konstanta pi (π) adalah perbandingan keliling (K) dengan diameter (d) lingkaran, yaitu K/d = π. Nilai pendekatan π adalah 3,14 atau 22/7.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali definisi dasar konstanta pi (π) sebagai rasio keliling terhadap diameter lingkaran. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi pi (π) sebagai hubungan tetap antara keliling dan diameter lingkaran.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan bersifat hafalan atau pemahaman konsep dasar yang diajarkan di awal materi lingkaran. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang unsur-unsur lingkaran (keliling, diameter) dan konstanta pi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pengetahuan faktual/konseptual dasar yang diharapkan dikuasai siswa kelas 9 saat mempelajari lingkaran. |

Run 2 — solusi: Definisi konstanta pi (π) adalah perbandingan keliling lingkaran (K) dengan diameternya (d), yaitu K/d = π. Nilai pendekatan π yang umum digunakan adalah 3,14 atau 22/7.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali definisi dasar konstanta pi (π) sebagai rasio keliling terhadap diameter lingkaran, yang merupakan pengetahuan faktual dasar dalam geometri.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap terminologi dan definisi dasar (fakta) mengenai konstanta lingkaran.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan ingatan terhadap definisi konstanta pi. Tidak ada langkah perhitungan atau integrasi konsep yang diperlukan.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar lingkaran dan konstanta pi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar yang diajarkan di tingkat SMP. Soal bersifat recall langsung tanpa memerlukan pemecahan masalah. |

Run 3 — solusi: Keliling lingkaran (K) dirumuskan sebagai K = π × d, sehingga perbandingan K/d = π. Nilai π adalah sekitar 3,14 atau 22/7.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat definisi konstanta pi sebagai perbandingan keliling terhadap diameter.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Dimensi pengetahuan `classify/factual`: Soal menanyakan pengetahuan dasar mengenai definisi konstanta pi.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Intended difficulty `classify/Easy`: Soal ini merupakan pengetahuan dasar yang diajarkan di awal materi lingkaran, tidak memerlukan langkah kompleks atau integrasi konsep.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi keliling dan diameter lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pengetahuan dasar yang diajarkan di awal materi lingkaran, tidak memerlukan langkah kompleks atau integrasi konsep. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3761`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menguji pengenalan langsung terhadap definisi konstanta pi (π) sebagai rasio keliling terhadap diameter. Tidak ada strategi atau integrasi yang diperlukan.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual mengenai definisi dan nilai konstanta lingkaran.
- Intended difficulty `Easy`: Soal ini sangat mendasar dan bersifat recall langsung. Tidak ada langkah perencanaan, integrasi, atau kendala yang harus dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang unsur-unsur lingkaran (keliling, diameter) dan konstanta pi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pengetahuan dasar yang diajarkan di awal materi lingkaran di SMP, sehingga dikategorikan sebagai Easy. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar ____.
Pilihan: A. 22
B. 3,14 (atau 22/7)
C. 3,41
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `487ffef7f793443d4d651476`

Untuk memperingati ulang tahun Gilang, ibunya membuat nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut dengan diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm. Jika nasi kerucut ini ingin ditutupi dengan daun pisang, berapa luas daun pisang yang akan dibutuhkan?

| Opsi | Isi |
|---|---|
| A | ≈1.456,96 cm² |
| B | ≈2.285,92 cm² |
| C | ≈1.142,96 cm² |
| D | ≈1.099 cm² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jari-jari (r) = 10 cm, tinggi (t) = 35 cm. Garis pelukis (s) = sqrt(r^2 + t^2) = sqrt(100 + 1225) = sqrt(1325) ≈ 36,40 cm. Luas selimut kerucut = πrs = 3,14 * 10 * 36,40 ≈ 1142,96 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `37e231a09728feb0da0d7e2aff728eca9ef33e5c7d9f447e1f2ae22033786548`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2903 |
| 2 | success | valid / verified | applying | procedural | Medium | 2895 |
| 3 | success | valid / verified | applying | procedural | Medium | 2925 |

Run 1 — solusi: Jari-jari (r) = 10 cm, tinggi (t) = 35 cm. Garis pelukis (s) = sqrt(r^2 + t^2) = sqrt(100 + 1225) = sqrt(1325) ≈ 36,40 cm. Luas selimut kerucut = πrs = 3,14 * 10 * 36,40 ≈ 1142,96 cm².
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa menutupi nasi tumpeng berarti menghitung luas selimut kerucut, bukan luas permukaan total. Ini memerlukan pemahaman konsep bangun ruang sisi lengkung dan pemilihan prosedur yang tepat.. Bukti: nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut; berapa luas daun pisang yang akan dibutuhkan
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur algoritme (Pythagoras untuk mencari garis pelukis dan rumus luas selimut) untuk menyelesaikan masalah kontekstual.. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas selimut kerucut = πrl
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dua langkah utama yang saling bergantung: menghitung garis pelukis menggunakan teorema Pythagoras sebelum menghitung luas selimut. Siswa juga harus memahami bahwa 'menutupi' tumpeng hanya melibatkan luas selimut, bukan luas alas.. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas daun pisang yang akan dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, rumus luas selimut kerucut, hubungan diameter dan jari-jari. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi kerucut adalah standar kelas 9. Menghitung garis pelukis dan luas selimut adalah prosedur rutin, namun memerlukan ketelitian dalam membedakan luas selimut dengan luas permukaan total. |

Run 2 — solusi: Jari-jari (r) = 10 cm. Garis pelukis (s) = sqrt(r^2 + t^2) = sqrt(10^2 + 35^2) = sqrt(100 + 1225) = sqrt(1325) ≈ 36,40 cm. Luas selimut kerucut = πrs = 3,14 * 10 * 36,40 ≈ 1.142,96 cm².
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa daun pisang hanya menutupi selimut kerucut, menghitung jari-jari dari diameter, menentukan garis pelukis menggunakan teorema Pythagoras, dan menerapkan rumus luas selimut kerucut.. Bukti: nasinya berbentuk kerucut dengan diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm.; berapa luas daun pisang yang akan dibutuhkan?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman prosedural tentang rumus luas selimut kerucut dan konsep konseptual mengenai bagian mana dari bangun ruang yang dihitung (selimut saja, bukan alas).. Bukti: luas daun pisang yang akan dibutuhkan; nasinya berbentuk kerucut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah utama yang saling terkait: menghitung garis pelukis menggunakan Pythagoras sebelum menghitung luas selimut. Siswa harus memahami bahwa tinggi kerucut berbeda dengan garis pelukis dan bahwa luas yang dicari hanya luas selimut.. Bukti: diameter 20 cm; Tinggi nasi... 35 cm; luas daun pisang yang akan dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, rumus luas selimut kerucut, hubungan diameter dan jari-jari. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengintegrasikan Pythagoras ke dalam perhitungan luas bangun ruang sisi lengkung. Soal ini menguji ketelitian dalam memilih komponen rumus yang tepat. |

Run 3 — solusi: Diketahui diameter d=20 cm, maka jari-jari r=10 cm. Tinggi kerucut t=35 cm. Garis pelukis l = √(r² + t²) = √(10² + 35²) = √(100 + 1225) = √1325 ≈ 36,40 cm. Luas selimut kerucut = πrl = 3,14 × 10 × 36,40 ≈ 1.142,96 cm².
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa menutupi tumpeng dengan daun pisang berarti menghitung luas selimut kerucut, bukan luas permukaan total. Ini memerlukan penerapan rumus luas selimut kerucut (πrl) dan pemahaman hubungan antara jari-jari, tinggi, dan garis pelukis.. Bukti: nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut; berapa luas daun pisang yang akan dibutuhkan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam menggunakan rumus luas selimut kerucut dan konsep konseptual mengenai hubungan Pythagoras pada kerucut untuk mencari garis pelukis.. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas selimut kerucut = πrl
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dua langkah utama: menghitung garis pelukis menggunakan teorema Pythagoras dan menerapkan rumus luas selimut kerucut. Meskipun prosedurnya familiar, terdapat integrasi konsep yang diperlukan untuk menentukan bagian mana dari bangun ruang yang harus dihitung (selimut saja).. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas daun pisang yang akan dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan rumus luas selimut kerucut. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung luas sisi lengkung dan menggunakan Pythagoras untuk mencari garis pelukis. Soal ini menguji ketelitian dalam memilih rumus yang tepat (selimut vs total) dan penggunaan variabel yang benar (jari-jari vs diameter). |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk memperingati ulang tahun Gilang, ibunya membuat nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut dengan diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm. Jika nasi kerucut ini ingin ditutupi dengan daun pisang, berapa luas daun pisang yang akan dibutuhkan?
Pilihan: A. ≈1.456,96 cm²
B. ≈2.285,92 cm²
C. ≈1.142,96 cm²
D. ≈1.099 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `efbc889b95676e6e2d913479`

Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

| Opsi | Isi |
|---|---|
| A | Luas permukaan bola sama dengan luas lingkaran yang memiliki jari-jari yang sama |
| B | Luas permukaan bola sama dengan dua kali luas lingkaran yang memiliki jari-jari yang sama |
| C | Luas permukaan bola sama dengan setengah luas lingkaran yang memiliki jari-jari yang sama |
| D | Luas permukaan bola sama dengan empat kali luas lingkaran yang memiliki jari-jari yang sama |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Luas permukaan bola adalah 4πr² dan luas lingkaran adalah πr². Perbandingan keduanya adalah (4πr²)/(πr²) = 4, sehingga luas permukaan bola adalah 4 kali luas lingkaran dengan jari-jari yang sama.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1a237670819eb07c684b12921d5266c37daf3cb5ccd61fc2c3571bccce96a301`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3266 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3395 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2621 |

Run 1 — solusi: Luas permukaan bola adalah 4πr² dan luas lingkaran adalah πr². Perbandingan keduanya adalah (4πr²)/(πr²) = 4, sehingga luas permukaan bola adalah 4 kali luas lingkaran dengan jari-jari yang sama.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat atau menerapkan rumus luas permukaan bola (4πr²) dan luas lingkaran (πr²) untuk menentukan hubungan keduanya secara langsung.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara rumus luas permukaan bola dan luas lingkaran.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct recall/application). Tidak ada langkah kompleks atau integrasi yang diperlukan.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan bola dan luas lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pengetahuan dasar geometri yang diajarkan di kelas 9, tidak memerlukan langkah penalaran yang rumit. |

Run 2 — solusi: Luas permukaan bola dirumuskan sebagai L_bola = 4πr² dan luas lingkaran sebagai L_lingkaran = πr². Dengan membandingkan kedua rumus tersebut, didapatkan L_bola = 4 × (πr²) = 4 × L_lingkaran. Maka, luas permukaan bola adalah empat kali luas lingkaran dengan jari-jari yang sama.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali hubungan matematis antara dua rumus dasar yang sudah dipelajari, yaitu luas permukaan bola dan luas lingkaran. Siswa hanya perlu membandingkan kedua rumus tersebut secara langsung.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep rumus luas permukaan bola dan luas lingkaran untuk menentukan hubungan perbandingannya.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman rumus dasar yang merupakan bagian dari kurikulum standar kelas 9. Tidak ada langkah kompleks, integrasi, atau kendala yang perlu dipecahkan.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan bola dan luas lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan sudah familiar dengan rumus-rumus bangun ruang sisi lengkung ini sebagai bagian dari kurikulum standar. |

Run 3 — solusi: Luas permukaan bola dirumuskan dengan L = 4πr². Luas lingkaran dengan jari-jari yang sama dirumuskan dengan A = πr². Maka, L = 4 × (πr²) = 4 × A. Jadi, luas permukaan bola adalah empat kali luas lingkaran dengan jari-jari yang sama.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menghubungkan rumus luas permukaan bola (4πr²) dengan rumus luas lingkaran (πr²). Siswa hanya perlu memahami hubungan matematis dasar antara kedua rumus tersebut.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual mengenai rumus bangun ruang sisi lengkung dan hubungan antar-rumus geometri dasar.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) karena hanya menanyakan hubungan rumus yang merupakan materi dasar geometri kelas 9. Tidak ada langkah perhitungan kompleks atau integrasi kendala.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan bola dan luas lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah mempelajari rumus luas permukaan bola. Menghubungkan 4πr² dengan πr² adalah prosedur rutin yang sangat dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
Pilihan: A. Luas permukaan bola sama dengan luas lingkaran yang memiliki jari-jari yang sama
B. Luas permukaan bola sama dengan dua kali luas lingkaran yang memiliki jari-jari yang sama
C. Luas permukaan bola sama dengan setengah luas lingkaran yang memiliki jari-jari yang sama
D. Luas permukaan bola sama dengan empat kali luas lingkaran yang memiliki jari-jari yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `1ef6efc5863938a14b737897`

Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar dengan diameter 2 meter dan panjang 12 meter?

| Opsi | Isi |
|---|---|
| A | 36.000 liter |
| B | 150.720 liter |
| C | 37.680 liter |
| D | 37,68 liter |

![Gambar sumber soal 17](<../../../images/kelas9_crop-s0011-truk-gas.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jari-jari (r) = diameter / 2 = 2 m / 2 = 1 m. Volume tabung = π × r² × t = 3,14 × 1² × 12 = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 liter/m³ = 37.680 liter.
Gambar sumber: images/kelas9_crop-s0011-truk-gas.png. Transkripsi visual: Sebuah truk tangki dengan tangki berbentuk silinder horizontal. Diameter tangki adalah 2 meter dan panjang tangki adalah 12 meter.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `240f83531640bcef9ab097ca45a685e57af39a6ec8b459ed4cc29aaabebdfd16`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3879 |
| 2 | success | valid / verified | applying | procedural | Medium | 3901 |
| 3 | success | valid / verified | applying | procedural | Medium | 3913 |

Run 1 — solusi: Diketahui diameter d=2 m, maka jari-jari r=1 m. Panjang silinder h=12 m. Volume V = πr²h = 3,14 × 1² × 12 = 37,68 m³. Karena 1 m³ = 1.000 liter, maka volume = 37,68 × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus volume silinder dan melakukan konversi satuan volume (m³ ke liter). Ini adalah penerapan prosedur rutin pada konteks yang familiar.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman konsep volume bangun ruang sisi lengkung dan prosedur konversi satuan yang merupakan pengetahuan prosedural.. Bukti: V=πr²h; 1 m³=1.000 liter
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan rumus volume yang standar dan familiar bagi siswa kelas 9. Langkah-langkah penyelesaiannya jelas: menentukan jari-jari dari diameter, menghitung volume, dan melakukan konversi satuan. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: diameter 2 meter; panjang 12 meter; Berapa liter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan konversi satuan volume. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah aplikasi langsung dari materi volume bangun ruang sisi lengkung yang merupakan standar kurikulum kelas 9. |

Run 2 — solusi: Jari-jari (r) = diameter / 2 = 2 m / 2 = 1 m. Volume tabung = π × r² × t = 3,14 × 1² × 12 = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 liter/m³ = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi rumus volume tabung, melakukan konversi dari diameter ke jari-jari, dan melakukan konversi satuan volume dari m³ ke liter. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang rumus volume bangun ruang sisi lengkung (konseptual) dan prosedur perhitungan serta konversi satuan (prosedural).. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: konversi diameter ke jari-jari, perhitungan volume, dan konversi satuan volume. Meskipun prosedurnya familiar, siswa harus teliti dalam setiap tahapan.. Bukti: diameter 2 meter; panjang 12 meter; Berapa liter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung, hubungan diameter dan jari-jari, konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung volume tabung dan melakukan konversi satuan. Soal ini menuntut ketelitian dalam langkah-langkah prosedural yang berurutan. |

Run 3 — solusi: Volume silinder = π × r² × h. Diketahui d = 2 m, maka r = 1 m. h = 12 m. V = 3,14 × 1² × 12 = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 liter/m³ = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi rumus volume tabung, melakukan konversi dari diameter ke jari-jari, dan melakukan konversi satuan volume dari m³ ke liter. Ini adalah penerapan prosedur rutin pada konteks yang familiar.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman konsep volume bangun ruang sisi lengkung dan prosedur konversi satuan yang merupakan pengetahuan prosedural standar.. Bukti: diameter 2 meter; V=πr²h; 1 m³=1.000 liter
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah prosedural yang saling terkait: menghitung volume dengan jari-jari (bukan diameter) dan melakukan konversi satuan volume. Meskipun prosedurnya familiar, siswa harus berhati-hati dengan langkah-langkah tersebut.. Bukti: diameter 2 meter; panjang 12 meter; Berapa liter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung, hubungan diameter dan jari-jari, konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung volume tabung dan melakukan konversi satuan. Kesalahan umum seperti menggunakan diameter sebagai jari-jari atau lupa konversi satuan diakomodasi dalam pilihan jawaban, menjadikannya soal yang menguji ketelitian prosedural. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5566`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan volume (m³ ke liter). Ini adalah penerapan prosedur rutin pada konteks yang familiar.
- Dimensi pengetahuan `procedural`: Soal memerlukan pemahaman konsep volume bangun ruang sisi lengkung dan prosedur konversi satuan yang merupakan pengetahuan prosedural.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: konversi diameter ke jari-jari, perhitungan volume, dan konversi satuan volume. Meskipun prosedurnya familiar, siswa harus teliti dalam setiap tahapan agar tidak terjebak pada distractor yang disediakan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung, hubungan diameter dan jari-jari, konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung volume tabung dan melakukan konversi satuan. Soal ini menuntut ketelitian dalam langkah-langkah prosedural yang berurutan, dengan distractor yang dirancang untuk menangkap kesalahan umum (seperti lupa membagi diameter atau lupa konversi satuan). |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar dengan diameter 2 meter dan panjang 12 meter?
Pilihan: A. 36.000 liter
B. 150.720 liter
C. 37.680 liter
D. 37,68 liter
Transkripsi visual: Sebuah truk tangki dengan tangki berbentuk silinder horizontal. Diameter tangki adalah 2 meter dan panjang tangki adalah 12 meter.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `a0c228d869728c3140dece74`

Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

| Opsi | Isi |
|---|---|
| A | Volume kerucut sama dengan sepertiga volume tabung |
| B | Volume kerucut adalah tiga kali volume tabung |
| C | Volume kerucut sama dengan volume tabung |
| D | Volume kerucut adalah setengah volume tabung |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rumus volume tabung adalah V_tabung = πr²t. Rumus volume kerucut adalah V_kerucut = 1/3 × πr²t. Dengan jari-jari (r) dan tinggi (t) yang sama, maka V_kerucut = 1/3 × V_tabung.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4cf6b7759e2e2e6573877390bd02fc075f941d020a6bd648f605c5d052878da7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2603 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2598 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2627 |

Run 1 — solusi: Rumus volume tabung adalah V_tabung = πr²t. Rumus volume kerucut adalah V_kerucut = 1/3 × πr²t. Dengan jari-jari (r) dan tinggi (t) yang sama, maka V_kerucut = 1/3 × V_tabung.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengingat dan menerapkan hubungan konseptual dasar antara rumus volume kerucut dan tabung. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai prinsip atau hubungan struktural antara dua bangun ruang sisi lengkung yang memiliki dimensi yang sama.. Bukti: hubungan antara volume kerucut dan tabung
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pengetahuan dasar yang diajarkan di kelas 9 mengenai hubungan volume bangun ruang. Tidak ada langkah-langkah kompleks atau kendala yang berinteraksi.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus volume tabung dan kerucut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan dasar tentang hubungan rumus volume yang merupakan materi standar kelas 9. |

Run 2 — solusi: Volume tabung (V_t) = πr²t. Volume kerucut (V_k) = 1/3 πr²t. Jika jari-jari (r) dan tinggi (t) sama, maka V_k = 1/3 V_t.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengingat dan menerapkan hubungan konseptual dasar antara rumus volume kerucut dan tabung. Siswa hanya perlu mengenali rumus yang sudah dipelajari.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap prinsip atau hubungan matematis antara dua bangun ruang yang berbeda namun memiliki variabel yang sama.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct recall) mengenai rumus dasar yang merupakan materi standar kelas 9. Tidak ada langkah perhitungan kompleks atau integrasi yang diperlukan.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan kerucut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan dasar tentang hubungan rumus volume yang dipelajari di kelas 9. Tidak menuntut penalaran tingkat tinggi. |

Run 3 — solusi: Rumus volume tabung adalah V_tabung = πr²t. Rumus volume kerucut adalah V_kerucut = 1/3 × πr²t. Jika jari-jari (r) dan tinggi (t) sama, maka V_kerucut = 1/3 × V_tabung.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengingat dan menerapkan hubungan konseptual dasar antara rumus volume kerucut dan tabung. Siswa hanya perlu mengenali fakta rumus atau hubungan proporsionalitas yang sudah dipelajari di kelas 9.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap hubungan antar konsep (rumus volume bangun ruang sisi lengkung) yang bersifat deklaratif/konseptual.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct recall) mengenai hubungan rumus volume yang merupakan materi dasar di kelas 9. Tidak ada langkah perhitungan atau integrasi yang kompleks.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus volume tabung dan kerucut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah pertanyaan dasar tentang hubungan rumus yang umum diajarkan di kelas 9, sehingga tingkat kesulitannya rendah. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
Pilihan: A. Volume kerucut sama dengan sepertiga volume tabung
B. Volume kerucut adalah tiga kali volume tabung
C. Volume kerucut sama dengan volume tabung
D. Volume kerucut adalah setengah volume tabung
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `4088b8d020de84282c07a2b3`

Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?

| Opsi | Isi |
|---|---|
| A | 1.250 liter 325 ml |
| B | 1.249 liter 675 ml |
| C | 1.249 liter 325 ml |
| D | 1.250 liter 675 ml |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 2.225 liter - 975 liter 325 ml = 2.224 liter 1.000 ml - 975 liter 325 ml = 1.249 liter 675 ml.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ca9bbff3e6fc42e022d55e224fba44d121a3c68e39e3c9edcf0161f0292a1c5c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3506 |
| 2 | success | valid / verified | applying | procedural | Easy | 2717 |
| 3 | success | valid / verified | applying | procedural | Easy | 3413 |

Run 1 — solusi: 2.225 liter - 975 liter 325 ml = 2.224 liter 1.000 ml - 975 liter 325 ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan konversi satuan volume (liter ke ml) yang familiar untuk menyelesaikan masalah.. Bukti: 2.225 liter - 975 liter 325 ml; 1.249 liter 675 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedur pengurangan bilangan dengan satuan campuran (liter dan ml) yang memerlukan teknik meminjam (regrouping).. Bukti: 2.225 liter - 975 liter 325 ml
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung prosedur pengurangan dengan konversi satuan sederhana. Tidak ada kendala kompleks atau integrasi konsep yang tinggi.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pengurangan bilangan bulat dan konversi satuan volume (1 liter = 1.000 ml). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini hanya memerlukan operasi pengurangan dasar dengan konversi satuan yang umum diajarkan, sehingga tingkat kesulitannya rendah untuk siswa kelas 9. |

Run 2 — solusi: 2.225 liter = 2.224 liter 1.000 ml. Pengurangan: (2.224 liter - 975 liter) + (1.000 ml - 325 ml) = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan konversi satuan volume (liter ke mililiter) untuk menyelesaikan masalah rutin.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan yang melibatkan konversi satuan volume.. Bukti: 2.225 liter - 975 liter 325 ml
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan satu prosedur konversi satuan (meminjam 1 liter menjadi 1.000 ml) dan pengurangan bilangan bulat. Tidak ada integrasi konsep yang kompleks atau kendala yang berinteraksi.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan volume (liter ke ml) dan pengurangan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 seharusnya sudah sangat familiar dengan operasi pengurangan satuan volume dasar. |

Run 3 — solusi: 2.225 liter - 975 liter 325 ml = (2.224 liter + 1.000 ml) - (975 liter + 325 ml) = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan pada satuan volume campuran (liter dan ml) dalam konteks rutin.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang konversi satuan (1 liter = 1000 ml) dan teknik pengurangan bersusun dengan meminjam.. Bukti: 2.225 liter - 975 liter 325 ml
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin pengurangan satuan volume. Tidak ada tuntutan perencanaan tinggi atau integrasi konsep yang kompleks.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan volume (1 liter = 1000 ml) dan pengurangan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan satuan campuran adalah materi dasar yang familiar bagi siswa kelas 9. Soal tidak memerlukan strategi non-rutin. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pengukuran Volume
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?
Pilihan: A. 1.250 liter 325 ml
B. 1.249 liter 675 ml
C. 1.249 liter 325 ml
D. 1.250 liter 675 ml
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `0d61de45054218c7d9af6710`

Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang. Bantulah beliau membuat gambar kerangka tersebut.<br><br>Manakah yang menghasilkan kerangka yang terluas?

| Opsi | Isi |
|---|---|
| A | Panjang 15 cm dan lebar 15 cm (luas 225 cm²) |
| B | Panjang 25 cm dan lebar 5 cm (luas 125 cm²) |
| C | Panjang 20 cm dan lebar 10 cm (luas 200 cm²) |
| D | Panjang 18 cm dan lebar 12 cm (luas 216 cm²) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Keliling persegi panjang adalah 2(p+l) = 60 cm, sehingga p+l = 30 cm. Luas L = p * l. Untuk keliling tetap, luas maksimum persegi panjang tercapai saat p = l (persegi). Maka p = l = 30/2 = 15 cm. Luas maksimum = 15 * 15 = 225 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dc7fd6fa24510c0d9cf4fdf9f928c320b4fac44b27b93d61e0e30d42478f6ff8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2825 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2812 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2805 |

Run 1 — solusi: Keliling persegi panjang adalah 2(p+l) = 60 cm, sehingga p+l = 30 cm. Luas L = p * l = p(30-p) = 30p - p². Fungsi kuadrat ini mencapai maksimum saat p = -b/(2a) = -30/(2*-1) = 15 cm. Jika p = 15, maka l = 30 - 15 = 15 cm. Luas maksimum = 15 * 15 = 225 cm².
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep keliling (sebagai kendala) dengan konsep luas untuk menemukan nilai maksimum. Ini melibatkan pemahaman hubungan antara dimensi dan luas, yang melampaui sekadar menghitung luas dari dimensi yang sudah ditentukan.. Bukti: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.; Manakah yang menghasilkan kerangka yang terluas?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang bagaimana perubahan dimensi persegi panjang dengan keliling tetap mempengaruhi luasnya, serta prinsip optimasi sederhana.. Bukti: Manakah yang menghasilkan kerangka yang terluas?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan eksplorasi atau pemahaman hubungan antara p+l=30 dan luas p*l. Meskipun bisa diselesaikan dengan mencoba opsi, pemahaman bahwa persegi adalah persegi panjang dengan luas maksimum memerlukan integrasi konsep yang lebih dari sekadar prosedur rutin.. Bukti: Bapak memiliki kawat sepanjang 60 cm.; Manakah yang menghasilkan kerangka yang terluas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep keliling dan luas persegi panjang, serta pemahaman dasar tentang variabel. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu memahami hubungan antara keliling dan luas. Soal ini menuntut pemilihan strategi (uji coba atau pemahaman sifat persegi) untuk menemukan luas maksimum. |

Run 2 — solusi: Keliling persegi panjang adalah 2(p+l) = 60 cm, sehingga p+l = 30 cm. Luas L = p * l = p(30-p) = 30p - p². Fungsi kuadrat ini mencapai maksimum saat p = -b/(2a) = -30/(2*-1) = 15 cm. Jika p = 15 cm, maka l = 30 - 15 = 15 cm. Luas maksimum = 15 * 15 = 225 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan keliling dan luas untuk mengoptimalkan luas persegi panjang dengan keliling tetap. Ini melibatkan pemahaman bahwa persegi adalah kasus khusus persegi panjang yang memberikan luas maksimum.. Bukti: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.; Manakah yang menghasilkan kerangka yang terluas?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara keliling dan luas bangun datar, serta prinsip optimasi sederhana pada persegi panjang.. Bukti: Manakah yang menghasilkan kerangka yang terluas?
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus memahami hubungan antara keliling dan luas, serta menyadari bahwa persegi adalah persegi panjang dengan luas maksimum untuk keliling tertentu. Meskipun prosedurnya bisa sederhana, siswa perlu melakukan eksplorasi atau pemahaman konsep optimasi yang melampaui sekadar menghitung luas dari angka yang diberikan.. Bukti: Bapak memiliki kawat sepanjang 60 cm.; Manakah yang menghasilkan kerangka yang terluas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep keliling dan luas persegi panjang, serta pemahaman dasar tentang optimasi luas. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghubungkan keliling tetap dengan variasi luas, dan mengenali properti persegi sebagai bentuk optimal. |

Run 3 — solusi: Keliling kawat 60 cm berarti 2(p+l) = 60, sehingga p+l = 30. Luas L = p x l = p(30-p) = 30p - p^2. Luas maksimum tercapai saat p = l = 15 cm (persegi), dengan luas 15 x 15 = 225 cm^2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan keliling dan luas persegi panjang untuk mengoptimalkan luas. Ini melibatkan pemahaman bahwa untuk keliling tetap, persegi adalah persegi panjang dengan luas maksimum.. Bukti: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.; Manakah yang menghasilkan kerangka yang terluas?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara keliling dan luas bangun datar, serta bagaimana perubahan dimensi mempengaruhi luas.. Bukti: Manakah yang menghasilkan kerangka yang terluas?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan eksplorasi atau pemahaman konsep optimasi sederhana (persegi sebagai kasus khusus persegi panjang dengan luas maksimal). Meskipun prosedurnya sederhana, siswa sering terjebak pada asumsi bahwa persegi panjang harus memiliki panjang dan lebar yang berbeda, sehingga memerlukan pemilihan strategi yang tepat.. Bukti: Bapak memiliki kawat sepanjang 60 cm.; Manakah yang menghasilkan kerangka yang terluas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep keliling dan luas persegi panjang, serta pemahaman dasar tentang optimasi luas. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu memahami hubungan antara keliling dan luas. Soal ini menuntut siswa untuk tidak sekadar menghitung, tetapi memilih konfigurasi yang memberikan hasil optimal di antara pilihan yang tersedia. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4598`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep hubungan keliling dan luas untuk mengoptimalkan luas persegi panjang. Meskipun bisa diselesaikan dengan mencoba opsi yang ada, pemahaman bahwa persegi adalah kasus khusus persegi panjang yang memberikan luas maksimum untuk keliling tertentu merupakan penerapan konsep yang rutin namun memerlukan pemilihan strategi.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara keliling dan luas bangun datar, serta prinsip optimasi sederhana pada persegi panjang.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus memahami hubungan antara keliling dan luas, serta menyadari bahwa persegi adalah persegi panjang dengan luas maksimum untuk keliling tertentu. Siswa perlu melakukan pemilihan strategi (uji coba atau pemahaman sifat persegi) untuk menemukan luas maksimum di antara pilihan yang tersedia.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep keliling dan luas persegi panjang, serta pemahaman dasar tentang optimasi luas. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghubungkan keliling tetap dengan variasi luas, dan mengenali properti persegi sebagai bentuk optimal. Soal ini menuntut siswa untuk tidak sekadar menghitung, tetapi memilih konfigurasi yang memberikan hasil optimal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Hubungan Keliling dan Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang. Bantulah beliau membuat gambar kerangka tersebut.

Manakah yang menghasilkan kerangka yang terluas?
Pilihan: A. Panjang 15 cm dan lebar 15 cm (luas 225 cm²)
B. Panjang 25 cm dan lebar 5 cm (luas 125 cm²)
C. Panjang 20 cm dan lebar 10 cm (luas 200 cm²)
D. Panjang 18 cm dan lebar 12 cm (luas 216 cm²)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `e81a665e38e1781b745677fd`

Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.<br><br>Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

| Opsi | Isi |
|---|---|
| A | 2 kali |
| B | 4 kali |
| C | 5 kali |
| D | 3 kali |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Posisi awal (F,1) ke posisi tujuan (D,2). Perubahan posisi horizontal: F ke D adalah 2 langkah (F->E->D). Perubahan posisi vertikal: 1 ke 2 adalah 1 langkah. Total rebahan = 2 + 1 = 3 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d3d4ea4ac07228fb2c43752391aa091fe84dc7f8a9f20a99e88f58d45df7b019`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2748 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2770 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2789 |

Run 1 — solusi: Posisi awal (F,1) ke posisi tujuan (D,2). Perubahan posisi horizontal: F ke D adalah 2 langkah (F->E->D). Perubahan posisi vertikal: 1 ke 2 adalah 1 langkah. Total rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami pemetaan koordinat pada sistem petak dan menerjemahkan perpindahan posisi menjadi jumlah langkah (rebahan) yang diperlukan, yang merupakan penerapan konsep lokasi dalam konteks rutin.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sistem koordinat dan bagaimana pergerakan objek (kubus) di atas grid berkorespondensi dengan jarak antar titik.. Bukti: Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena jalur penyelesaian sangat jelas (menghitung selisih koordinat horizontal dan vertikal). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin yang kompleks.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan sistem koordinat. Menghitung jarak antar titik pada grid adalah keterampilan dasar yang rutin. |

Run 2 — solusi: Posisi awal (F,1) ke posisi tujuan (D,2). Perubahan posisi horizontal: F ke D adalah 2 langkah (F->E->D). Perubahan posisi vertikal: 1 ke 2 adalah 1 langkah. Total langkah rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami pemetaan koordinat pada sistem petak dan menerjemahkan jarak antar koordinat menjadi jumlah langkah fisik (rebahan) kubus. Ini melibatkan penerapan konsep lokasi dalam konteks rutin.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang sistem koordinat dan hubungan spasial antara posisi objek pada grid untuk menentukan langkah.. Bukti: Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena jalur penyelesaiannya sangat jelas (menghitung selisih koordinat horizontal dan vertikal). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin yang kompleks. Siswa hanya perlu menghitung jarak absolut antar koordinat.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji kemampuan dasar spasial yang sesuai untuk kelas 9, dengan tingkat tuntutan kognitif yang rendah karena prosedur penyelesaiannya langsung dan tidak memerlukan integrasi konsep yang rumit. |

Run 3 — solusi: Posisi awal (F,1) ke posisi akhir (D,2). Perubahan posisi horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Perubahan posisi vertikal dari 1 ke 2 adalah 1 langkah. Total rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada sistem koordinat petak dan menerjemahkan jarak antar koordinat menjadi jumlah langkah (rebahan) yang diperlukan. Ini melibatkan penerapan konsep jarak pada grid ke dalam konteks pergerakan objek.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya.; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang sistem koordinat dan prosedur sederhana untuk menghitung selisih posisi (jarak) pada sumbu horizontal dan vertikal.. Bukti: jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak; Berapa kali kubus tersebut direbahkan
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena jalur penyelesaian sangat jelas: menghitung selisih koordinat horizontal dan vertikal lalu menjumlahkannya. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin yang kompleks.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan sistem koordinat. Menghitung jarak antar titik pada grid adalah keterampilan dasar yang rutin. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lokasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.

Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
Pilihan: A. 2 kali
B. 4 kali
C. 5 kali
D. 3 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `bba0d92faac1dbb90cd622ef`

Diketahui segitiga ABC dengan A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1). Tentukan translasinya serta koordinat titik B' dan C'.

| Opsi | Isi |
|---|---|
| A | Translasi $\binom{2}{-4}$, B'(4,-2), C'(6,1) |
| B | Translasi $\binom{-2}{4}$, B'(0,6), C'(2,9) |
| C | Translasi $\binom{4}{-2}$, B'(6,0), C'(8,3) |
| D | Translasi $\binom{-2}{4}$, B'(4,-2), C'(6,1) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Vektor translasi T = A' - A = (-2 - 0, 1 - (-3)) = (-2, 4). Maka B' = B + T = (2 + (-2), 2 + 4) = (0, 6) dan C' = C + T = (4 + (-2), 5 + 4) = (2, 9).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c1a0aaba3bb93f1baa1e94c518a6cbc33313e2833633396601ffbf97b4bc1981`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2770 |
| 2 | success | valid / verified | applying | procedural | Easy | 3601 |
| 3 | success | valid / verified | applying | procedural | Easy | 2781 |

Run 1 — solusi: Vektor translasi T = A' - A = (-2 - 0, 1 - (-3)) = (-2, 4). Maka B' = B + T = (2 + (-2), 2 + 4) = (0, 6) dan C' = C + T = (4 + (-2), 5 + 4) = (2, 9).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur translasi pada koordinat titik. Langkah-langkahnya rutin dan prosedural: menentukan vektor translasi dari pasangan titik yang diketahui, lalu menerapkannya pada titik lain.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1); Tentukan translasinya serta koordinat titik B' dan C'
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi translasi pada koordinat kartesius.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1)
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur translasi adalah materi dasar yang familiar. Siswa hanya perlu menghitung selisih koordinat untuk mendapatkan vektor translasi, lalu menjumlahkannya ke titik lain. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat serta konsep dasar koordinat kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi titik adalah materi standar kelas 9 yang prosedurnya sangat langsung dan tidak memerlukan integrasi konsep yang kompleks. |

Run 2 — solusi: Vektor translasi T = A' - A = (-2-0, 1-(-3)) = (-2, 4). Maka B' = B + T = (2-2, 2+4) = (0, 6) dan C' = C + T = (4-2, 5+4) = (2, 9).
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur standar translasi titik dengan menentukan vektor pergeseran terlebih dahulu, kemudian menerapkannya pada titik lain.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1); Tentukan translasinya serta koordinat titik B' dan C'
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang operasi translasi pada koordinat Kartesius.. Bukti: A(0,-3), B(2,2) dan C(4,5) ditranslasikan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menghitung selisih koordinat untuk mendapatkan vektor translasi, lalu menambahkannya ke titik lain. Tidak ada kendala interaktif atau kebutuhan strategi non-rutin.. Bukti: A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, konsep koordinat Kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi translasi adalah standar kelas 9. Prosedur yang digunakan sangat langsung dan familiar. |

Run 3 — solusi: Vektor translasi T = A' - A = (-2 - 0, 1 - (-3)) = (-2, 4). Maka B' = B + T = (2 + (-2), 2 + 4) = (0, 6) dan C' = C + T = (4 + (-2), 5 + 4) = (2, 9).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur translasi titik dengan menentukan vektor pergeseran terlebih dahulu dari pasangan titik yang diketahui, kemudian menerapkannya pada titik lain. Ini adalah penerapan prosedur rutin dalam konteks geometri.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1). Tentukan translasinya serta koordinat titik B' dan C'
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep translasi (pergeseran) sebagai operasi penjumlahan vektor pada koordinat kartesius.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1)
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur translasi adalah materi dasar yang familiar. Siswa hanya perlu menghitung selisih koordinat untuk mendapatkan vektor translasi, lalu menjumlahkannya ke titik lain. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, konsep koordinat kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi titik adalah materi standar kelas 9. Prosedur penentuan vektor translasi dan penerapannya pada titik lain bersifat langsung dan rutin. |

Histori retry: run 2 sebelumnya `failed` / `ValidationError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Translasi (Pergeseran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui segitiga ABC dengan A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1). Tentukan translasinya serta koordinat titik B' dan C'.
Pilihan: A. Translasi $\binom{2}{-4}$, B'(4,-2), C'(6,1)
B. Translasi $\binom{-2}{4}$, B'(0,6), C'(2,9)
C. Translasi $\binom{4}{-2}$, B'(6,0), C'(8,3)
D. Translasi $\binom{-2}{4}$, B'(4,-2), C'(6,1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `944be36e182518ad72be95aa`

Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah …

| Opsi | Isi |
|---|---|
| A | A'(-6,8) |
| B | A'(-6,-8) |
| C | A'(2,2) |
| D | A'(-2,8) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Translasi titik A(x, y) oleh vektor (a, b) menghasilkan bayangan A'(x+a, y+b). Untuk A(-2, 5) dan vektor (-4, 3), maka A' = (-2 + (-4), 5 + 3) = (-6, 8).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e734c1912c8d942c92737b44e7158ad7d45d55f730df80ea219e883409b2a021`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2622 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3508 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2627 |

Run 1 — solusi: Translasi titik A(x, y) oleh vektor (a, b) menghasilkan bayangan A'(x+a, y+b). Untuk A(-2, 5) dan vektor (-4, 3), maka A' = (-2 + (-4), 5 + 3) = (-6, 8).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi translasi titik pada koordinat Kartesius. Siswa hanya perlu melakukan operasi penjumlahan sederhana sesuai rumus translasi yang sudah dipelajari.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural mengenai algoritma translasi titik, yaitu menjumlahkan koordinat titik asal dengan komponen vektor translasi.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi. Siswa hanya perlu menerapkan rumus translasi dasar.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat Kartesius dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep translasi yang merupakan materi dasar kelas 9. Tidak ada tuntutan kognitif tinggi. |

Run 2 — solusi: Titik A(-2,5) ditranslasi oleh (-4,3) menghasilkan A'(-2+(-4), 5+3) = A'(-6,8).
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi translasi titik (x, y) oleh vektor (a, b) menjadi (x+a, y+b). Prosedur sangat langsung.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan prosedur penjumlahan koordinat dengan komponen translasi.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung rumus translasi yang merupakan materi dasar kelas 9. Tidak ada integrasi konsep atau langkah kompleks yang diperlukan.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat dan konsep dasar koordinat Kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah penerapan langsung rumus translasi yang merupakan materi dasar kelas 9. Tidak ada integrasi konsep atau langkah kompleks yang diperlukan. |

Run 3 — solusi: Translasi titik A(x, y) oleh vektor (a, b) menghasilkan A'(x+a, y+b). Untuk A(-2, 5) dan vektor (-4, 3), maka A' = (-2 + (-4), 5 + 3) = (-6, 8).
- Domain kognitif `classify/knowing`: Soal meminta siswa menerapkan prosedur translasi titik secara langsung menggunakan definisi penjumlahan vektor translasi pada koordinat titik. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Bayangan titik A(-2,5) oleh \binom{-4}{3} adalah
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritme atau prosedur penjumlahan koordinat dengan komponen translasi (prosedural) untuk mendapatkan hasil.. Bukti: Bayangan titik A(-2,5) oleh \binom{-4}{3}
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan rumus translasi dasar tanpa ada kendala tambahan, pemilihan strategi yang kompleks, atau integrasi konsep lain.. Bukti: Bayangan titik A(-2,5) oleh \binom{-4}{3}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat kartesius dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi titik adalah materi dasar kelas 9 yang prosedurnya sangat jelas. Soal ini tidak menuntut penalaran lebih lanjut selain eksekusi rumus. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Translasi (Pergeseran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah …
Pilihan: A. A'(-6,8)
B. A'(-6,-8)
C. A'(2,2)
D. A'(-2,8)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `34e4b41c04e7c9417acca5ce`

Titik (2,-3) direfleksikan terhadap garis y=x. Tentukan bayangannya.

| Opsi | Isi |
|---|---|
| A | (2,3) |
| B | (-3,2) |
| C | (3,-2) |
| D | (2,1) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), bayangannya adalah (-3, 2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b781501a3b25fa27d09e9e0826f931129f8c25468178e3c04984970c0ffac69`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2566 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2596 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2562 |

Run 1 — solusi: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), bayangannya adalah (-3, 2).
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan aturan transformasi geometri yang spesifik (refleksi terhadap garis y=x) secara langsung pada titik yang diberikan.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap prosedur atau aturan transformasi (refleksi) yang merupakan bagian dari pengetahuan prosedural dalam geometri.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan satu langkah pengerjaan menggunakan aturan yang umum diajarkan di kelas 9. Tidak ada integrasi konsep atau kendala yang kompleks.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat kartesius dan aturan transformasi refleksi terhadap garis y=x. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar yang menguji ingatan atau penerapan langsung rumus transformasi geometri yang merupakan materi dasar kelas 9. |

Run 2 — solusi: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), bayangannya adalah (-3, 2).
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat atau menerapkan aturan transformasi refleksi terhadap garis y=x secara langsung tanpa memerlukan strategi kompleks atau integrasi konsep.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman terhadap aturan atau rumus transformasi geometri (prosedur) yang bersifat faktual/konseptual dalam konteks koordinat kartesius.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (one-step problem) dengan aturan yang sudah umum dipelajari di kelas 9. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat kartesius dan aturan transformasi refleksi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar yang sangat rutin untuk materi transformasi geometri kelas 9, tidak menuntut penalaran tingkat tinggi. |

Run 3 — solusi: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), maka bayangannya adalah (-3, 2).
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat atau menerapkan aturan transformasi refleksi terhadap garis y=x secara langsung tanpa perlu strategi kompleks.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman terhadap aturan atau prosedur spesifik dalam transformasi geometri (refleksi).. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan rumus refleksi (x, y) -> (y, x) tanpa ada langkah tambahan atau kendala yang berinteraksi.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat kartesius dan aturan transformasi refleksi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi refleksi adalah standar kurikulum kelas 9. Soal ini adalah penerapan langsung rumus dasar tanpa modifikasi, sehingga tergolong mudah. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Refleksi (Pencerminan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik (2,-3) direfleksikan terhadap garis y=x. Tentukan bayangannya.
Pilihan: A. (2,3)
B. (-3,2)
C. (3,-2)
D. (2,1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `e23d76dc5ff2cda98f0f4ccc`

Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.

| Opsi | Isi |
|---|---|
| A | (2,3) |
| B | (-2,3) |
| C | (-2,-3) |
| D | (4,-3) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Aturan refleksi titik (x, y) terhadap sumbu x adalah (x, -y). Maka, bayangan dari titik (2, -3) adalah (2, -(-3)) = (2, 3).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `570c1b13fa0945b7900e3ca58f8e3e993c14064a5d27d6e1bd983d09213b1945`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3049 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2559 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2593 |

Run 1 — solusi: Aturan refleksi titik (x, y) terhadap sumbu x adalah (x, -y). Maka, bayangan dari titik (2, -3) adalah (2, -(-3)) = (2, 3).
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan aturan transformasi geometri dasar secara langsung tanpa perlu strategi atau penalaran kompleks.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menggunakan prosedur atau aturan algoritma spesifik untuk melakukan refleksi terhadap sumbu x.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan satu aturan transformasi tanpa ada kendala yang berinteraksi atau kebutuhan perencanaan langkah yang kompleks.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat Kartesius dan aturan dasar transformasi geometri. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 9 yang menguji ingatan terhadap aturan refleksi dasar. Tidak ada tuntutan integrasi atau analisis mendalam. |

Run 2 — solusi: Refleksi titik (x, y) terhadap sumbu x menghasilkan bayangan (x, -y). Untuk titik (2, -3), bayangannya adalah (2, -(-3)) = (2, 3).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung aturan transformasi geometri (refleksi terhadap sumbu x) yang merupakan prosedur standar dan sangat familiar bagi siswa kelas 9.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui aturan atau rumus refleksi terhadap sumbu x (prosedural) untuk menentukan bayangan titik tersebut.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (direct application) tanpa memerlukan perencanaan langkah yang kompleks atau integrasi konsep. Siswa hanya perlu mengingat atau menerapkan aturan refleksi dasar.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat Kartesius dan aturan refleksi terhadap sumbu x. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan dasar transformasi geometri yang sesuai dengan kurikulum kelas 9, tidak menuntut penalaran tingkat tinggi. |

Run 3 — solusi: Refleksi titik (x, y) terhadap sumbu x menghasilkan bayangan (x, -y). Untuk titik (2, -3), bayangannya adalah (2, -(-3)) = (2, 3).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung aturan transformasi geometri (refleksi terhadap sumbu x) yang merupakan prosedur standar dan sangat langsung bagi siswa kelas 9.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui aturan atau rumus refleksi terhadap sumbu x (fakta/prosedur dasar) untuk menyelesaikan soal ini.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (one-step) dengan prosedur yang familiar bagi siswa kelas 9. Tidak ada integrasi konsep atau perencanaan strategi yang kompleks.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan aturan dasar refleksi terhadap sumbu x. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan dasar transformasi geometri yang sesuai dengan kurikulum kelas 9, di mana siswa diharapkan sudah menguasai aturan refleksi dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Refleksi (Pencerminan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.
Pilihan: A. (2,3)
B. (-2,3)
C. (-2,-3)
D. (4,-3)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `078d6a87b40b143dc0e0683c`

Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0). Gambarkan segi empat KLMN beserta bayangannya pada bidang koordinat.

| Opsi | Isi |
|---|---|
| A | K'(-1,-2), L'(-6,-4), M'(-8,3), N'(-3,1) |
| B | K'(-2,1), L'(-4,6), M'(3,8), N'(1,3) |
| C | K'(1,-2), L'(6,-4), M'(8,3), N'(3,1) |
| D | K'(-1,2), L'(-6,4), M'(-8,-3), N'(-3,-1) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rotasi 180 derajat terhadap titik pusat O(0,0) memiliki aturan pemetaan (x, y) -> (-x, -y). Menerapkan aturan ini pada setiap titik: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), N(3,-1) -> N'(-3,1).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `af50b33a4fefb41321fe2da431f6ef2d8c2f20c51f0a5e9dc98203d2cd370d33`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2812 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2829 |
| 3 | success | valid / verified | applying | procedural | Easy | 2837 |

Run 1 — solusi: Rotasi 180° terhadap titik pusat O(0,0) memiliki aturan transformasi (x,y) -> (-x,-y). Menerapkan aturan ini pada setiap titik: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), N(3,-1) -> N'(-3,1).
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan aturan transformasi rotasi 180 derajat yang merupakan prosedur standar dan langsung dalam materi transformasi geometri kelas 9.. Bukti: Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap aturan atau rumus transformasi geometri (prosedural) untuk rotasi 180 derajat.. Bukti: rotasi 180º terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya meminta penerapan langsung rumus rotasi 180 derajat terhadap titik-titik yang diberikan. Tidak ada integrasi konsep yang kompleks atau kendala yang saling berinteraksi.. Bukti: Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan aturan transformasi rotasi 180 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah mempelajari transformasi geometri. Menerapkan rumus (x,y) -> (-x,-y) adalah tugas dasar yang familiar. |

Run 2 — solusi: Rotasi 180 derajat terhadap titik pusat (0,0) memiliki aturan pemetaan (x, y) -> (-x, -y). Menerapkan aturan ini pada setiap titik: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), N(3,-1) -> N'(-3,1). Hasil ini sesuai dengan pilihan A.
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan prosedur transformasi geometri (rotasi 180 derajat) yang merupakan materi standar kelas 9. Prosedur ini bersifat langsung dan rutin.. Bukti: Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan aturan transformasi geometri (rotasi) yang merupakan prosedur standar dalam kurikulum.. Bukti: rotasi 180º terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus rotasi 180 derajat (x,y) -> (-x,-y) pada setiap titik koordinat yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks.. Bukti: Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan aturan rotasi 180 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah materi dasar transformasi geometri kelas 9. Soal ini tidak memerlukan integrasi konsep atau perencanaan langkah yang rumit. |

Run 3 — solusi: Rotasi 180 derajat terhadap titik pusat O(0,0) memiliki aturan pemetaan (x, y) -> (-x, -y). Menerapkan aturan ini pada setiap titik: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), N(3,-1) -> N'(-3,1).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan transformasi rotasi 180 derajat yang merupakan prosedur standar dalam materi transformasi geometri kelas 9. Tidak diperlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap aturan atau rumus transformasi geometri (rotasi) yang merupakan bagian dari pengetahuan prosedural.. Bukti: rotasi 180º terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus rotasi 180 derajat (x,y) -> (-x,-y) secara langsung pada empat titik yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks.. Bukti: Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan aturan transformasi rotasi 180 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah materi dasar transformasi di kelas 9. Prosedur penyelesaian sangat langsung dan tidak memerlukan analisis mendalam. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4570`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta menerapkan prosedur transformasi geometri (rotasi 180 derajat) yang merupakan materi standar kelas 9. Prosedur ini bersifat langsung dan rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman dan penerapan aturan transformasi geometri (rotasi) yang merupakan prosedur standar dalam kurikulum.
- Intended difficulty `Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus rotasi 180 derajat (x,y) -> (-x,-y) pada setiap titik koordinat yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan aturan rotasi 180 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah materi dasar transformasi geometri kelas 9. Soal ini tidak memerlukan integrasi konsep atau perencanaan langkah yang rumit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Rotasi (Perputaran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0). Gambarkan segi empat KLMN beserta bayangannya pada bidang koordinat.
Pilihan: A. K'(-1,-2), L'(-6,-4), M'(-8,3), N'(-3,1)
B. K'(-2,1), L'(-4,6), M'(3,8), N'(1,3)
C. K'(1,-2), L'(6,-4), M'(8,3), N'(3,1)
D. K'(-1,2), L'(-6,4), M'(-8,-3), N'(-3,-1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `5cdb075f3e6376933323750c`

A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).

| Opsi | Isi |
|---|---|
| A | A'(-2,5), B'(-5,8), C'(-1,2) |
| B | A'(2,-5), B'(5,-8), C'(1,-2) |
| C | A'(-5,2), B'(-8,5), C'(-2,1) |
| D | A'(-5,-2), B'(-8,-5), C'(-2,-1) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rotasi 90 derajat berlawanan arah jarum jam terhadap pusat (0,0) menggunakan aturan (x, y) -> (-y, x). Untuk A(5,2) menjadi A'(-2,5), B(8,5) menjadi B'(-5,8), dan C(2,1) menjadi C'(-1,2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e6468022c57fbb293d6726c9b5ae84f67c0bead7c77501cc57b3c9c3628820a6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2841 |
| 2 | success | valid / verified | applying | procedural | Easy | 2802 |
| 3 | success | valid / verified | applying | procedural | Easy | 2847 |

Run 1 — solusi: Rotasi 90 derajat berlawanan arah jarum jam terhadap pusat (0,0) menggunakan aturan (x, y) -> (-y, x). Untuk A(5,2) menjadi A'(-2,5), B(8,5) menjadi B'(-5,8), dan C(2,1) menjadi C'(-1,2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan transformasi geometri yang spesifik (rotasi 90 derajat berlawanan arah jarum jam) pada titik-titik koordinat yang diberikan. Ini adalah penerapan prosedur standar dalam geometri transformasi.. Bukti: Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau aturan transformasi rotasi (prosedural) yang merupakan bagian dari materi geometri kelas 9.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9 yang telah mempelajari transformasi geometri. Aturan rotasi 90 derajat berlawanan arah jarum jam adalah konsep dasar yang sering dilatih. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sistem koordinat Kartesius dan aturan transformasi rotasi dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi titik terhadap pusat (0,0) adalah materi standar kelas 9. Siswa hanya perlu menerapkan rumus transformasi (x,y) -> (-y,x) secara langsung. |

Run 2 — solusi: Rotasi 90º berlawanan arah jarum jam terhadap pusat (0,0) memiliki aturan pemetaan (x, y) -> (-y, x). Menerapkan aturan ini pada titik-titik sudut: A(5,2) -> A'(-2,5), B(8,5) -> B'(-5,8), dan C(2,1) -> C'(-1,2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur transformasi geometri (rotasi) yang spesifik. Ini adalah penerapan langsung dari aturan rotasi yang sudah dipelajari di kelas 9.. Bukti: Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau aturan transformasi (rotasi) pada bidang koordinat.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena siswa hanya perlu menerapkan rumus transformasi yang sudah umum diajarkan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi kompleks.. Bukti: A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat kartesius dan aturan transformasi rotasi 90 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi titik adalah materi standar kelas 9. Soal ini langsung menanyakan penerapan rumus tanpa variasi atau integrasi konsep lain. |

Run 3 — solusi: Rotasi 90 derajat berlawanan arah jarum jam terhadap pusat O(0,0) memiliki aturan pemetaan (x, y) -> (-y, x). Untuk A(5,2) menjadi A'(-2,5), B(8,5) menjadi B'(-5,8), dan C(2,1) menjadi C'(-1,2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur transformasi geometri yang sudah dipelajari (rotasi 90 derajat) pada titik-titik yang diberikan. Ini adalah penerapan langsung dari rumus atau konsep rotasi.. Bukti: Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa mengenai algoritma atau aturan transformasi rotasi (prosedural) yang merupakan bagian dari materi geometri kelas 9.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9 karena hanya memerlukan penerapan rumus rotasi standar (x,y) -> (-y,x) pada titik-titik yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi kompleks.. Bukti: A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan aturan transformasi rotasi 90 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 90 derajat terhadap titik pusat adalah materi standar kelas 9 yang penyelesaiannya bersifat prosedural langsung. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Rotasi (Perputaran)
Tipe soal: multiple_choice
Stimulus: -
Soal: A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).
Pilihan: A. A'(-2,5), B'(-5,8), C'(-1,2)
B. A'(2,-5), B'(5,-8), C'(1,-2)
C. A'(-5,2), B'(-8,5), C'(-2,1)
D. A'(-5,-2), B'(-8,-5), C'(-2,-1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `f6516e65a41da50ae0f6a8b9`

Jika ΔMDN ≅ ΔKPG, maka MN = _____.

| Opsi | Isi |
|---|---|
| A | KP |
| B | KG |
| C | PG |
| D | DN |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Notasi ΔMDN ≅ ΔKPG menunjukkan korespondensi titik-titik: M ↔ K, D ↔ P, dan N ↔ G. Sisi MN menghubungkan titik pertama dan ketiga, sehingga bersesuaian dengan sisi KG yang menghubungkan titik pertama dan ketiga pada ΔKPG. Jadi, MN = KG.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `97bc5be9d872fbe699f56edde2424652072d6aaa69198426dddd9df683c4e7fb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3307 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3391 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3237 |

Run 1 — solusi: Berdasarkan notasi ΔMDN ≅ ΔKPG, titik-titik yang bersesuaian adalah M dengan K, D dengan P, dan N dengan G. Sisi MN menghubungkan titik pertama dan ketiga, sehingga bersesuaian dengan sisi KG yang menghubungkan titik pertama dan ketiga pada ΔKPG. Jadi, MN = KG.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman definisi dasar notasi kekongruenan segitiga. Siswa hanya perlu mengenali korespondensi titik-titik sudut berdasarkan urutan penulisan nama segitiga untuk menentukan sisi yang bersesuaian.. Bukti: ΔMDN ≅ ΔKPG; MN = _____
- Dimensi pengetahuan `classify/factual`: Soal ini berkaitan dengan pemahaman simbol dan notasi (fakta matematis) mengenai korespondensi dalam kekongruenan segitiga.. Bukti: ΔMDN ≅ ΔKPG
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari definisi kekongruenan. Tidak ada langkah integrasi atau perencanaan yang kompleks; siswa cukup memetakan urutan huruf.. Bukti: ΔMDN ≅ ΔKPG; MN = _____

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi kekongruenan segitiga dan korespondensi titik sudut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar mengenai notasi kekongruenan yang umum di kelas 9. Tidak ada tuntutan kognitif tinggi. |

Run 2 — solusi: Notasi ΔMDN ≅ ΔKPG menunjukkan korespondensi titik M↔K, D↔P, dan N↔G. Oleh karena itu, sisi MN bersesuaian dengan sisi KG.
- Domain kognitif `classify/knowing`: Soal hanya meminta identifikasi sisi yang bersesuaian berdasarkan notasi kekongruenan yang diberikan. Ini adalah prosedur langsung yang mengenali definisi kekongruenan.. Bukti: ΔMDN ≅ ΔKPG; MN = _____
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep korespondensi titik dalam notasi kekongruenan segitiga.. Bukti: ΔMDN ≅ ΔKPG
- Intended difficulty `classify/Easy`: Soal bersifat langsung dengan satu langkah identifikasi korespondensi titik. Tidak ada kendala atau integrasi yang diperlukan.. Bukti: ΔMDN ≅ ΔKPG; MN = _____

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi kekongruenan dan korespondensi titik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan dasar mengenai notasi kekongruenan yang umum di kelas 9. Tidak ada tuntutan kognitif tinggi. |

Run 3 — solusi: Notasi ΔMDN ≅ ΔKPG menunjukkan korespondensi titik-titik: M ↔ K, D ↔ P, dan N ↔ G. Oleh karena itu, sisi MN pada ΔMDN bersesuaian dengan sisi KG pada ΔKPG. Jadi, MN = KG.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengenali dan menerapkan definisi korespondensi titik pada dua segitiga yang kongruen secara langsung. Tidak ada langkah kompleks atau integrasi strategi.. Bukti: ΔMDN ≅ ΔKPG; MN = _____
- Dimensi pengetahuan `classify/conceptual`: Memahami hubungan korespondensi antara titik-titik pada dua bangun yang kongruen merupakan pemahaman konseptual dasar tentang kekongruenan.. Bukti: ΔMDN ≅ ΔKPG
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari definisi kekongruenan. Siswa hanya perlu mencocokkan urutan huruf pada notasi segitiga. Tidak ada langkah tambahan atau kendala yang perlu diintegrasikan.. Bukti: ΔMDN ≅ ΔKPG; MN = _____

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi kekongruenan segitiga dan korespondensi titik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar mengenai notasi kekongruenan yang umum di kelas 9. Tidak ada tuntutan perencanaan atau integrasi konsep yang tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4027`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menguji pemahaman definisi dasar notasi kekongruenan segitiga. Siswa hanya perlu mengenali korespondensi titik-titik sudut berdasarkan urutan penulisan nama segitiga untuk menentukan sisi yang bersesuaian secara langsung.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami prinsip korespondensi titik dalam notasi kekongruenan segitiga, yang merupakan pemahaman konseptual dasar tentang hubungan antar bangun yang kongruen.
- Intended difficulty `Easy`: Soal ini adalah penerapan langsung dari definisi kekongruenan. Tidak ada langkah integrasi atau perencanaan yang kompleks; siswa cukup memetakan urutan huruf untuk menemukan sisi yang bersesuaian.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi kekongruenan segitiga dan korespondensi titik sudut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar mengenai notasi kekongruenan yang umum di kelas 9. Tidak ada tuntutan kognitif tinggi atau langkah yang saling bergantung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kekongruenan
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika ΔMDN ≅ ΔKPG, maka MN = _____.
Pilihan: A. KP
B. KG
C. PG
D. DN
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `5494cb036f9f5ecded212fcf`

Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen. Pernyataan tersebut merupakan bunyi kriteria _____.

| Opsi | Isi |
|---|---|
| A | S-S-Sd |
| B | Sd-S-Sd |
| C | S-Sd-S |
| D | S-S-S |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Kriteria kekongruenan segitiga yang menyatakan dua sisi sama panjang dan sudut yang diapit oleh kedua sisi tersebut sama besar adalah kriteria Sisi-Sudut-Sisi (S-Sd-S).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b2d42a48fcd0857439582c7a115a7da1a3293adf551d8b9c00af987e622a061`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2621 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2678 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2642 |

Run 1 — solusi: Kriteria kekongruenan segitiga yang menyatakan dua sisi sama panjang dan sudut yang diapit oleh kedua sisi tersebut sama besar adalah kriteria Sisi-Sudut-Sisi (S-Sd-S).
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengenali dan mengklasifikasikan definisi kriteria kekongruenan segitiga berdasarkan deskripsi yang diberikan. Ini adalah proses mengingat kembali fakta atau definisi dasar.. Bukti: dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman terhadap istilah dan prinsip dasar dalam geometri, khususnya kriteria kekongruenan segitiga.. Bukti: kriteria Sisi-Sudut-Sisi (S-Sd-S)
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (recall) mengenai definisi kriteria kekongruenan. Tidak ada langkah perhitungan atau analisis kompleks yang diperlukan.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kriteria kekongruenan segitiga (S-Sd-S, Sd-S-Sd, S-S-S). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pengenalan konsep dasar kekongruenan yang diajarkan di kelas 9. Siswa hanya perlu mencocokkan deskripsi dengan istilah yang tepat. |

Run 2 — solusi: Kriteria kekongruenan segitiga yang menyatakan dua sisi sama panjang dan sudut yang diapit oleh kedua sisi tersebut sama besar adalah kriteria Sisi-Sudut-Sisi (S-Sd-S).
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali definisi atau kriteria dasar kekongruenan segitiga. Siswa hanya perlu mengingat dan mencocokkan deskripsi kriteria dengan istilah yang tepat (Sisi-Sudut-Sisi).. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual mengenai syarat kekongruenan segitiga, yaitu hubungan antara elemen-elemen segitiga (sisi dan sudut) yang membentuk kriteria kongruensi.. Bukti: Pernyataan tersebut merupakan bunyi kriteria _____
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (recall) mengenai definisi kriteria kekongruenan yang merupakan materi dasar kelas 9. Tidak ada langkah perhitungan atau analisis kompleks yang diperlukan.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kriteria kekongruenan segitiga (S-Sd-S, Sd-S-Sd, S-S-S). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah topik standar kelas 9. Soal ini hanya menanyakan definisi kriteria, sehingga tingkat kesulitannya rendah bagi siswa yang telah mempelajari materi tersebut. |

Run 3 — solusi: Kriteria kekongruenan segitiga yang menyatakan dua sisi sama panjang dan sudut yang diapit oleh kedua sisi tersebut sama besar adalah kriteria Sisi-Sudut-Sisi (S-Sd-S).
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi atau mengenali definisi/kriteria kekongruenan segitiga yang sudah dipelajari. Ini adalah proses mengingat kembali fakta atau definisi dasar.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap istilah dan definisi kriteria kekongruenan segitiga yang merupakan bagian dari pengetahuan konseptual.. Bukti: Pernyataan tersebut merupakan bunyi kriteria _____
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (recall) mengenai definisi kriteria kekongruenan segitiga. Tidak ada langkah perhitungan atau analisis kompleks yang diperlukan.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kriteria kekongruenan segitiga (S-Sd-S, Sd-S-Sd, S-S-S). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan dasar tentang definisi kekongruenan yang diajarkan di kelas 9. Siswa hanya perlu mencocokkan deskripsi dengan istilah yang tepat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4167`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengenali dan mengidentifikasi definisi kriteria kekongruenan segitiga yang sudah dipelajari. Ini adalah proses mengingat kembali fakta atau definisi dasar (knowing).
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual mengenai syarat kekongruenan segitiga, yaitu hubungan antara elemen-elemen segitiga (sisi dan sudut) yang membentuk kriteria kongruensi.
- Intended difficulty `Easy`: Soal ini bersifat langsung (recall) mengenai definisi kriteria kekongruenan yang merupakan materi dasar kelas 9. Tidak ada langkah perhitungan atau analisis kompleks yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kriteria kekongruenan segitiga (S-Sd-S, Sd-S-Sd, S-S-S). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah topik standar kelas 9. Soal ini hanya menanyakan definisi kriteria, sehingga tingkat kesulitannya rendah bagi siswa yang telah mempelajari materi tersebut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kekongruenan
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen. Pernyataan tersebut merupakan bunyi kriteria _____.
Pilihan: A. S-S-Sd
B. Sd-S-Sd
C. S-Sd-S
D. S-S-S
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `907f9e4697523a633ea0ac02`

Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…

| Opsi | Isi |
|---|---|
| A | 180 cm² |
| B | 1.620 cm² |
| C | 540 cm² |
| D | 60 cm² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Luas ΔABC = 0,5 × 8 × 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas menjadi k² × Luas awal. Maka, Luas ΔA'B'C' = 3² × 60 = 9 × 60 = 540 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fefcd23966a4c409b2f6b60572578ed54b97eeee09a72385cd9237e1f6427a51`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2762 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2724 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2690 |

Run 1 — solusi: Luas ΔABC = 0,5 × 8 × 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas menjadi k² × Luas awal. Maka, Luas ΔA'B'C' = 3² × 60 = 9 × 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep dilatasi pada bangun datar, khususnya memahami hubungan antara faktor skala (k) dengan perubahan luas (k²). Ini adalah penerapan konsep pada konteks rutin.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman prinsip geometris tentang bagaimana transformasi dilatasi mempengaruhi luas bangun datar (konsep k²).. Bukti: dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman hubungan antara faktor skala dan luas (k²), bukan sekadar mengalikan dengan k. Meskipun prosedurnya familiar, siswa harus memilih hubungan yang tepat (k²) dan menghindari jebakan umum (mengalikan dengan k atau k³).. Bukti: panjang AB=8 cm, BC=15 cm, dan AC=17 cm; dilatasi dari ΔABC dengan faktor skala 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Luas segitiga dan konsep dilatasi/skala. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami transformasi geometri. Kesalahan umum pada distractor (k vs k²) menunjukkan tuntutan konseptual yang sesuai untuk tingkat Medium. |

Run 2 — solusi: Luas ΔABC = 0,5 x 8 x 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas menjadi k² x Luas awal. Luas ΔA'B'C' = 3² x 60 = 9 x 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara faktor skala dilatasi (k) dengan perubahan luas bangun datar (k²). Ini adalah penerapan konsep pada konteks rutin.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman prinsip geometris mengenai bagaimana dilatasi mempengaruhi luas bangun datar, yang merupakan pengetahuan konseptual.. Bukti: hasil dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa memahami hubungan non-linear antara faktor skala dan luas (k²), bukan sekadar mengalikan dengan k. Meskipun prosedurnya familiar, siswa sering terjebak pada kesalahan umum mengalikan dengan k saja.. Bukti: luas ΔA'B'C' adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas segitiga dan konsep dasar dilatasi/skala. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami transformasi geometri. Kesalahan umum pada dilatasi luas (menggunakan k bukan k²) membuat soal ini memiliki tantangan konseptual yang sesuai untuk tingkat Medium. |

Run 3 — solusi: Luas ΔABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k²=9. Luas ΔA'B'C' = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara faktor skala dilatasi (k) dengan perubahan luas bangun datar (k²), bukan sekadar menghitung luas segitiga awal.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana transformasi dilatasi mempengaruhi properti luas bangun datar.. Bukti: dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus memahami prinsip bahwa dilatasi dengan faktor skala k mengubah luas sebesar k², bukan k. Meskipun prosedurnya familiar, siswa sering terjebak menggunakan k atau k³ (skala volume), sehingga memerlukan pemahaman konseptual yang tepat.. Bukti: faktor skala 3; luas ΔA'B'C' adalah

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
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami transformasi geometri. Kesalahan umum pada faktor skala luas (k²) menjadikannya tantangan yang sesuai untuk tingkat Medium. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Dilatasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…
Pilihan: A. 180 cm²
B. 1.620 cm²
C. 540 cm²
D. 60 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `61e70f2732214f09d97c2039`

Diketahui ΔABC dengan A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap $[O, \frac{1}{2}]$! Gambarkan segitiga tersebut beserta bayangannya pada bidang koordinat!

| Opsi | Isi |
|---|---|
| A | $A'(-\frac{3}{2},-2)$, $B'(3,4)$, $C'(\frac{1}{2},-2)$ |
| B | A'(-2.5,-1.5), B'(6.5,4.5), C'(1.5,-1.5) |
| C | A'(-6,-4), B'(12,8), C'(2,-4) |
| D | $A'(-\frac{3}{2},-1)$, $B'(3,2)$, $C'(\frac{1}{2},-1)$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3 * 1/2, -2 * 1/2) = (-1.5, -1); B' = (6 * 1/2, 4 * 1/2) = (3, 2); C' = (1 * 1/2, -2 * 1/2) = (0.5, -1).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `610e287b02d97cf30ea9334f3ab78d76b0dbaa22bb7b0f8ab659506e965462e0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2871 |
| 2 | success | valid / verified | applying | procedural | Easy | 2893 |
| 3 | success | valid / verified | applying | procedural | Easy | 2868 |

Run 1 — solusi: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3 * 1/2, -2 * 1/2) = (-1.5, -1); B' = (6 * 1/2, 4 * 1/2) = (3, 2); C' = (1 * 1/2, -2 * 1/2) = (0.5, -1).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus dilatasi terhadap titik pusat (0,0) dengan faktor skala k. Siswa hanya perlu mengalikan setiap koordinat dengan faktor skala yang diberikan.. Bukti: Tentukan bayangan ΔABC yang didilatasikan terhadap [O, 1/2]
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang transformasi geometri (dilatasi) dan penggunaan rumus koordinat bayangan.. Bukti: dilatasikan terhadap [O, 1/2]
- Intended difficulty `classify/Easy`: Soal bersifat rutin karena hanya memerlukan penerapan rumus dilatasi [O, k] secara langsung pada tiga titik yang diberikan. Tidak ada kendala tambahan atau integrasi konsep yang kompleks.. Bukti: A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap [O, 1/2]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan operasi perkalian bilangan pecahan/desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Dilatasi adalah materi standar kelas 9. Soal ini merupakan penerapan langsung definisi dilatasi tanpa modifikasi atau langkah tambahan yang rumit. |

Run 2 — solusi: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3*0.5, -2*0.5) = (-1.5, -1); B' = (6*0.5, 4*0.5) = (3, 2); C' = (1*0.5, -2*0.5) = (0.5, -1).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur dilatasi titik pada bidang koordinat dengan faktor skala tertentu. Ini adalah penerapan langsung dari rumus dilatasi yang sudah dipelajari di kelas 9.. Bukti: Tentukan bayangan ΔABC yang didilatasikan terhadap [O, 1/2]
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau prosedur dilatasi (transformasi geometri) yang merupakan bagian dari materi prosedural.. Bukti: dilatasikan terhadap [O, 1/2]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena siswa hanya perlu menerapkan rumus dilatasi [O, k] yaitu (x', y') = (kx, ky) secara langsung pada setiap titik. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi kompleks.. Bukti: Diketahui ΔABC dengan A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap [O, 1/2]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat kartesius dan konsep dilatasi dengan pusat O(0,0). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi adalah standar kurikulum kelas 9. Soal ini merupakan aplikasi langsung rumus tanpa modifikasi atau integrasi konsep lain. |

Run 3 — solusi: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3 * 0.5, -2 * 0.5) = (-1.5, -1); B' = (6 * 0.5, 4 * 0.5) = (3, 2); C' = (1 * 0.5, -2 * 0.5) = (0.5, -1).
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur dilatasi standar terhadap titik-titik koordinat yang diberikan. Ini adalah penerapan langsung dari rumus dilatasi [O, k] yaitu (kx, ky).. Bukti: Tentukan bayangan ΔABC yang didilatasikan terhadap [O, 1/2]
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep dilatasi dan aturan algoritmik perkalian koordinat dengan faktor skala untuk menentukan bayangan titik.. Bukti: dilatasikan terhadap [O, 1/2]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Prosedur dilatasi dengan pusat O(0,0) adalah materi standar yang langsung dapat diselesaikan dengan mengalikan koordinat dengan faktor skala. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Tentukan bayangan ΔABC yang didilatasikan terhadap [O, 1/2]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan operasi perkalian bilangan pecahan/desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Dilatasi dengan pusat O adalah materi dasar transformasi geometri kelas 9. Soal ini tidak menuntut integrasi konsep atau langkah yang saling bergantung. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Dilatasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui ΔABC dengan A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap $[O, \frac{1}{2}]$! Gambarkan segitiga tersebut beserta bayangannya pada bidang koordinat!
Pilihan: A. $A'(-\frac{3}{2},-2)$, $B'(3,4)$, $C'(\frac{1}{2},-2)$
B. A'(-2.5,-1.5), B'(6.5,4.5), C'(1.5,-1.5)
C. A'(-6,-4), B'(12,8), C'(2,-4)
D. $A'(-\frac{3}{2},-1)$, $B'(3,2)$, $C'(\frac{1}{2},-1)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br>Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = AE, karena ∠ACE = ∠AEC |
| B | AC = CE, karena ∠CAE = ∠AEC |
| C | AE = CE, karena ∠ACE = ∠CAE |
| D | AB = AC, karena AD garis bagi |

![Gambar sumber soal 32](<../../../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Karena CE \|\| AD, maka ∠AEC = ∠BAD (sehadap) dan ∠ACE = ∠DAC (berseberangan dalam). Karena AD adalah garis bagi, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Segitiga dengan dua sudut alas yang sama adalah segitiga sama kaki, sehingga AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Segitiga ABC dengan garis bagi AD yang membagi sudut A menjadi dua bagian sama besar. Titik D berada pada sisi BC. Terdapat konstruksi tambahan berupa garis melalui C yang sejajar dengan AD, memotong perpanjangan AB di titik E.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ed7ec5433c75ff54be8ab82aadc802bac2fade2bd82c17e9d1277d366bdcff60`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 3959 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 3932 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3994 |

Run 1 — solusi: Karena CE \|\| AD, maka ∠AEC = ∠BAD (sehadap) dan ∠ACE = ∠DAC (berseberangan dalam). Karena AD adalah garis bagi, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Segitiga dengan dua sudut alas yang sama adalah segitiga sama kaki, sehingga AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan penalaran deduktif untuk membuktikan sifat segitiga berdasarkan konstruksi yang diberikan. Siswa harus menghubungkan konsep garis sejajar (sudut sehadap dan berseberangan) dengan sifat garis bagi untuk menyimpulkan kesamaan sudut dan sisi.. Bukti: Beri alasan bahwa ΔACE sama kaki.; Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip-prinsip geometri (garis sejajar, sudut, dan sifat segitiga sama kaki) dan mengintegrasikannya untuk membangun argumen logis, yang merupakan pemahaman konseptual.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun petunjuk konstruksi diberikan, siswa harus melakukan integrasi konsep geometri (garis sejajar dan sudut) untuk membuktikan sifat segitiga. Ini bukan sekadar penerapan rumus langsung, melainkan penalaran langkah demi langkah yang saling bergantung.. Bukti: Beri alasan bahwa ΔACE sama kaki.; Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada dua garis sejajar yang dipotong garis transversal (sehadap, berseberangan) dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pembuktian geometri sederhana menggunakan sifat-sifat sudut dan kesebangunan. Soal ini menuntut pemahaman konsep yang lebih dalam daripada sekadar menghitung panjang sisi. |

Run 2 — solusi: Karena CE \|\| AD, maka ∠AEC = ∠BAD (sudut sehadap) dan ∠ACE = ∠DAC (sudut dalam berseberangan). Karena AD adalah garis bagi, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Dalam segitiga ACE, karena dua sudut alasnya sama, maka segitiga tersebut sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk melakukan pembuktian geometris sederhana menggunakan sifat sudut pada garis sejajar (sehadap dan berseberangan) untuk menunjukkan sifat segitiga sama kaki. Ini melibatkan penalaran logis untuk menghubungkan konsep garis bagi dengan sifat sudut.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; Beri alasan bahwa ΔACE sama kaki. Tuliskan sisi-sisi yang sama panjang.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara garis sejajar, sudut, dan sifat segitiga sama kaki, bukan sekadar menghafal rumus.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun pembuktiannya standar, siswa harus mengintegrasikan konsep garis sejajar dan sudut untuk menarik kesimpulan. Petunjuk konstruksi membantu siswa, namun siswa tetap harus memahami hubungan antar sudut secara mandiri.. Bukti: Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan) dan definisi segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pembuktian geometris sederhana. Soal ini menuntut pemahaman hubungan sudut, bukan sekadar komputasi. |

Run 3 — solusi: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, maka sudut BAD = sudut DAC. Akibatnya, sudut AEC = sudut ACE. Dalam segitiga ACE, karena dua sudut alasnya sama, maka segitiga tersebut sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan penalaran deduktif geometris dengan menggunakan konstruksi tambahan yang diberikan. Siswa harus mengintegrasikan sifat sudut pada garis sejajar (sudut sehadap dan berseberangan) dengan definisi garis bagi untuk menyimpulkan sifat segitiga sama kaki.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; Beri alasan bahwa ΔACE sama kaki. Tuliskan sisi-sisi yang sama panjang.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan konseptual antara garis sejajar, sudut-sudut yang terbentuk (sehadap, berseberangan), dan definisi segitiga sama kaki berdasarkan kesamaan sudut alas.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium. Meskipun prosedurnya melibatkan konsep geometri standar, siswa dituntut untuk melakukan perencanaan langkah deduktif (menghubungkan sudut sehadap dan berseberangan) untuk membuktikan sifat segitiga. Petunjuk konstruksi membantu, namun siswa tetap harus mengintegrasikan beberapa relasi sudut secara mandiri.. Bukti: Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada dua garis sejajar yang dipotong garis transversal (sudut sehadap, berseberangan dalam) dan definisi segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pembuktian geometris sederhana menggunakan sifat sudut. Soal ini menuntut kemampuan menghubungkan konstruksi dengan sifat sudut, yang merupakan standar menengah untuk jenjang SMP. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kesebangunan pada Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.

Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.
Pilihan: A. AC = AE, karena ∠ACE = ∠AEC
B. AC = CE, karena ∠CAE = ∠AEC
C. AE = CE, karena ∠ACE = ∠CAE
D. AB = AC, karena AD garis bagi
Transkripsi visual: Segitiga ABC dengan garis bagi AD yang membagi sudut A menjadi dua bagian sama besar. Titik D berada pada sisi BC. Terdapat konstruksi tambahan berupa garis melalui C yang sejajar dengan AD, memotong perpanjangan AB di titik E.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `49861bd79ef9562f45188055`

Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk oleh seorang guru dalam kelas yang terdiri dari 12 siswa laki-laki dan 18 siswa perempuan.

| Opsi | Isi |
|---|---|
| A | 30 (12 siswa laki-laki + 18 siswa perempuan) |
| B | 18 (hanya menghitung banyaknya siswa perempuan) |
| C | 12 (hanya menghitung banyaknya siswa laki-laki) |
| D | 2 (hanya menghitung banyaknya kategori jenis kelamin: laki-laki dan perempuan) |

Kunci sumber: `A`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal ambigu. Jika ruang sampel adalah himpunan siswa yang mungkin terpilih, n(S) = 12 + 18 = 30. Jika ruang sampel adalah himpunan hasil jenis kelamin yang mungkin, n(S) = 2 (Laki-laki atau Perempuan). Kunci jawaban A (30) tidak konsisten dengan frasa 'Jenis kelamin dari seorang siswa'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5c818ca1d27240b44d3683a0c6c21319fd503e0a53371e53b713c53cadf237b9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | knowing | conceptual | Easy | 2790 |
| 2 | success | concern / conflict | knowing | conceptual | Easy | 2793 |
| 3 | success | concern / conflict | knowing | conceptual | Easy | 2843 |

Run 1 — solusi: Jika ruang sampel didefinisikan sebagai himpunan siswa yang mungkin terpilih, maka n(S) = 12 + 18 = 30. Jika ruang sampel didefinisikan sebagai himpunan jenis kelamin yang mungkin muncul, maka n(S) = 2. Karena soal meminta 'banyaknya anggota ruang sampel' dari 'jenis kelamin', jawaban 2 secara matematis lebih tepat, namun kunci jawaban memilih 30 (mengasumsikan ruang sampel adalah individu).
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi ruang sampel dari sebuah percobaan sederhana. Ini melibatkan pemahaman konsep dasar ruang sampel.. Bukti: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut.; Jenis kelamin dari seorang siswa yang pertama kali ditunjuk
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap definisi ruang sampel (konsep dasar peluang).. Bukti: banyaknya anggota ruang sampel
- Intended difficulty `classify/Easy`: Soal ini secara teknis mudah karena hanya melibatkan penjumlahan sederhana, namun memiliki ambiguitas konseptual yang tinggi antara ruang sampel kejadian (individu) dan ruang sampel variabel acak (jenis kelamin).. Bukti: 12 siswa laki-laki dan 18 siswa perempuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar ruang sampel dan penjumlahan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kelas 9 mencakup ruang sampel. Soal ini sangat mendasar, namun kunci jawaban yang kontradiktif dengan definisi variabel 'jenis kelamin' membuatnya bermasalah secara konten. |

Run 2 — solusi: Soal ambigu. Jika ruang sampel adalah himpunan siswa yang mungkin terpilih, n(S) = 12 + 18 = 30. Jika ruang sampel adalah himpunan kemungkinan hasil jenis kelamin, n(S) = 2 (Laki-laki atau Perempuan). Kunci jawaban A mengasumsikan siswa sebagai anggota ruang sampel, namun redaksi soal menanyakan jenis kelamin.
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi dan menerapkan definisi ruang sampel pada konteks pemilihan individu dalam populasi.. Bukti: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa yang membentuk ruang sampel dalam sebuah percobaan acak.. Bukti: banyaknya anggota ruang sampel
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena hanya memerlukan pemahaman dasar tentang definisi ruang sampel dan operasi penjumlahan sederhana. Namun, terdapat masalah validitas konten pada redaksi soal.. Bukti: 12 siswa laki-laki dan 18 siswa perempuan; banyaknya anggota ruang sampel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar ruang sampel dan penjumlahan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar kelas 9. Kesulitan rendah karena hanya melibatkan identifikasi elemen ruang sampel. |

Run 3 — solusi: Soal ambigu. Jika ruang sampel didefinisikan sebagai himpunan siswa yang mungkin terpilih, n(S) = 12 + 18 = 30. Jika ruang sampel didefinisikan sebagai himpunan hasil jenis kelamin yang mungkin, n(S) = 2 (Laki-laki atau Perempuan). Kunci sumber (30) tidak konsisten dengan frasa 'Jenis kelamin dari seorang siswa'.
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi dan menghitung anggota ruang sampel berdasarkan deskripsi percobaan. Ini melibatkan pemahaman konsep dasar ruang sampel.. Bukti: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi ruang sampel sebagai elemen dasar dalam teori peluang.. Bukti: banyaknya anggota ruang sampel
- Intended difficulty `classify/Easy`: Soal ini secara prosedural sangat sederhana (penjumlahan 12+18), namun secara konseptual bermasalah karena ambiguitas antara ruang sampel 'siswa' dan 'jenis kelamin'. Jika diabaikan ambiguitasnya, ini adalah soal rutin.. Bukti: 12 siswa laki-laki dan 18 siswa perempuan; banyaknya anggota ruang sampel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel dan penjumlahan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ruang sampel adalah dasar peluang kelas 9. Kesulitan rendah karena hanya melibatkan penjumlahan sederhana, namun soal memiliki cacat logika pada definisi ruang sampel. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4233`.
Konten: `concern`; kunci: `conflict`; masalah: Soal memiliki ambiguitas konseptual yang fatal. Frasa 'Jenis kelamin dari seorang siswa' secara matematis merujuk pada variabel acak dengan ruang sampel {Laki-laki, Perempuan}, yang memiliki 2 anggota. Namun, kunci jawaban (30) mengasumsikan ruang sampel adalah himpunan siswa (individu).; Terdapat ketidaksesuaian antara pertanyaan (jenis kelamin) dan metode perhitungan yang diharapkan (jumlah siswa). Soal ini tidak valid secara matematis karena mencampuradukkan ruang sampel kejadian (individu) dengan ruang sampel variabel (kategori)..
- Domain kognitif `knowing`: Siswa diminta mengidentifikasi ruang sampel dari sebuah percobaan. Meskipun prosedurnya sederhana, terdapat kebingungan konseptual dalam mendefinisikan ruang sampel yang diminta.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman definisi ruang sampel, namun gagal dalam penerapan konseptual yang akurat.
- Intended difficulty `Easy`: Secara prosedural, soal ini sangat mudah (penjumlahan 12+18). Kesulitan utama bukan pada kompleksitas, melainkan pada cacat logika soal yang membingungkan siswa.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar ruang sampel dan penjumlahan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ruang sampel adalah dasar peluang kelas 9. Soal ini secara teknis mudah, namun memiliki masalah validitas konten yang serius. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk oleh seorang guru dalam kelas yang terdiri dari 12 siswa laki-laki dan 18 siswa perempuan.
Pilihan: A. 30 (12 siswa laki-laki + 18 siswa perempuan)
B. 18 (hanya menghitung banyaknya siswa perempuan)
C. 12 (hanya menghitung banyaknya siswa laki-laki)
D. 2 (hanya menghitung banyaknya kategori jenis kelamin: laki-laki dan perempuan)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal memiliki ambiguitas konseptual yang fatal. Frasa 'Jenis kelamin dari seorang siswa' secara matematis merujuk pada variabel acak dengan ruang sampel {Laki-laki, Perempuan}, yang memiliki 2 anggota. Namun, kunci jawaban (30) mengasumsikan ruang sampel adalah himpunan siswa (individu).; Terdapat ketidaksesuaian antara pertanyaan (jenis kelamin) dan metode perhitungan yang diharapkan (jumlah siswa). Soal ini tidak valid secara matematis karena mencampuradukkan ruang sampel kejadian (individu) dengan ruang sampel variabel (kategori)..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `47721424de374937d3a86de8`

Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase. ⓒ Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau. Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.

| Opsi | Isi |
|---|---|
| A | 1 (membandingkan bola bukan merah dengan sesamanya, bukan dengan total bola di kotak) |
| B | 1/6 (hanya menghitung peluang terambilnya bola kuning saja, lupa bola hijau) |
| C | 1/3 (hanya menghitung peluang terambilnya bola hijau saja, lupa bola kuning) |
| D | 1/2 (atau 0,5 atau 50%) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `1/2, 0,5, 50%`.
Solusi minimum hasil AI: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Bola bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal = 0,5. Dalam persentase = 50%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1b837f30343f2e8ea23a415d93862f9263dfa2c43c54483427fae0441bf1bafd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2805 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2809 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2789 |

Run 1 — solusi: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Bola bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal = 0,5. Dalam persentase = 50%.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kejadian komplemen (bukan merah) dari ruang sampel yang diberikan dan menerapkan rumus peluang dasar. Ini adalah penerapan konsep peluang pada konteks rutin.. Bukti: Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian yang diinginkan dibagi total ruang sampel) dan klasifikasi kejadian (bukan merah).. Bukti: Tentukan peluang tiap-tiap kejadian berikut ini; enam bola merah, dua bola kuning, dan empat bola hijau
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menjumlahkan total bola, mengidentifikasi jumlah bola yang memenuhi syarat (bukan merah), dan menghitung rasio. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: enam bola merah, dua bola kuning, dan empat bola hijau; kalian mendapatkan bola yang bukan merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, penjumlahan bilangan bulat, dan konversi pecahan ke desimal/persen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah standar kelas 9. Soal ini tidak menuntut integrasi konsep yang rumit atau perencanaan strategi, sehingga dikategorikan mudah. |

Run 2 — solusi: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Bola bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal = 0,5. Dalam persentase = 50%.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kejadian komplemen (bukan merah) dari ruang sampel yang diberikan dan menerapkan rumus peluang dasar. Ini adalah penerapan konsep peluang pada konteks rutin.. Bukti: Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip dasar peluang dan kemampuan mengonversi representasi bilangan (pecahan, desimal, persen).. Bukti: Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur penyelesaiannya sangat langsung (menghitung total, menghitung kejadian yang diinginkan, membagi). Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau.; kalian mendapatkan bola yang bukan merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (kejadian/ruang sampel) dan operasi pecahan/desimal/persen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah standar kelas 9. Soal ini tidak menuntut integrasi konsep yang rumit, hanya pemahaman definisi peluang dan konversi bentuk bilangan. |

Run 3 — solusi: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Bola bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal = 0,5. Dalam persentase = 50%.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel (total bola) dan kejadian yang diinginkan (bukan merah), lalu menerapkan rumus peluang dasar. Ini adalah penerapan konsep peluang pada konteks rutin.. Bukti: Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian/ruang sampel) dan konversi antar bentuk bilangan (pecahan, desimal, persen).. Bukti: Tentukan peluang tiap-tiap kejadian berikut ini
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menjumlahkan total bola dan menghitung jumlah bola yang memenuhi kriteria 'bukan merah'. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau.; kalian mendapatkan bola yang bukan merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan konsep peluang sederhana (P = n(A)/n(S)). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan konsep peluang dasar. Soal ini tidak memerlukan integrasi konsep yang rumit atau penalaran non-rutin. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase. ⓒ Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau. Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
Pilihan: A. 1 (membandingkan bola bukan merah dengan sesamanya, bukan dengan total bola di kotak)
B. 1/6 (hanya menghitung peluang terambilnya bola kuning saja, lupa bola hijau)
C. 1/3 (hanya menghitung peluang terambilnya bola hijau saja, lupa bola kuning)
D. 1/2 (atau 0,5 atau 50%)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `2fa02b235094086c5cc7be86`

Sebuah program komputer digunakan untuk menampilkan 12 bilangan 0–3 secara acak. Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3<br><br>Tentukan frekuensi relatif munculnya bilangan 0.

| Opsi | Isi |
|---|---|
| A | 2/4 (= 1/2) |
| B | 2/12 (= 1/6) |
| C | 3/12 (= 1/4) |
| D | 1/12 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Frekuensi munculnya angka 0 adalah 2 kali. Frekuensi relatif = (banyak kejadian) / (total percobaan) = 2/12 = 1/6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `17eb6d02ce63caa7bfb84ea255b0da2d9c1cc9f820324e6580f2fe029cdadfd6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2774 |
| 2 | success | valid / verified | applying | procedural | Easy | 2726 |
| 3 | success | valid / verified | applying | procedural | Easy | 2746 |

Run 1 — solusi: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Frekuensi munculnya angka 0 adalah 2. Frekuensi relatif = (frekuensi kejadian) / (total percobaan) = 2/12 = 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi frekuensi relatif (frekuensi kejadian dibagi total percobaan) pada data yang diberikan secara langsung.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.; Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep frekuensi relatif dan prosedur penghitungannya dari data empiris.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung kemunculan angka 0 dan membaginya dengan total data. Tidak ada kendala yang berinteraksi atau kebutuhan strategi kompleks.. Bukti: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3; Tentukan frekuensi relatif munculnya bilangan 0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif dan kemampuan menghitung data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang empiris adalah standar kelas 9. Soal ini merupakan penerapan langsung definisi tanpa modifikasi atau integrasi konsep yang menantang. |

Run 2 — solusi: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Frekuensi munculnya angka 0 adalah 2 kali. Frekuensi relatif = (banyak kejadian) / (total percobaan) = 2/12 = 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi frekuensi relatif (kejadian/total percobaan) pada data yang diberikan secara langsung. Ini adalah prosedur standar yang familiar.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang konsep frekuensi relatif dan kemampuan menerapkan algoritma penghitungan frekuensi pada data empiris.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menghitung kemunculan angka 0 dalam daftar data dan membaginya dengan total data. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: Sebuah program komputer digunakan untuk menampilkan 12 bilangan 0–3 secara acak.; Tentukan frekuensi relatif munculnya bilangan 0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang empiris dan konsep frekuensi relatif. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung definisi frekuensi relatif yang sesuai untuk kelas 9, dengan beban kognitif yang rendah. |

Run 3 — solusi: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Frekuensi munculnya angka 0 adalah 2 kali. Frekuensi relatif = (banyak kejadian) / (total percobaan) = 2/12 = 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi frekuensi relatif (kejadian/total percobaan) pada data yang diberikan secara langsung. Ini adalah penerapan prosedur standar.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau metode perhitungan frekuensi relatif dari data empiris.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menghitung frekuensi kemunculan angka 0 dalam daftar data yang diberikan dan membaginya dengan total data. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3; Tentukan frekuensi relatif munculnya bilangan 0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi dan konsep peluang empiris. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 9, hanya memerlukan penghitungan frekuensi sederhana dan pembagian dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4316`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan definisi frekuensi relatif (frekuensi kejadian dibagi total percobaan) pada data yang diberikan secara langsung. Ini adalah penerapan prosedur standar.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang algoritma atau metode perhitungan frekuensi relatif dari data empiris.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung kemunculan angka 0 dan membaginya dengan total data. Tidak ada kendala yang berinteraksi atau kebutuhan strategi kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif dan kemampuan menghitung data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang empiris adalah standar kelas 9. Soal ini merupakan penerapan langsung definisi tanpa modifikasi atau integrasi konsep yang menantang. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah program komputer digunakan untuk menampilkan 12 bilangan 0–3 secara acak. Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3

Tentukan frekuensi relatif munculnya bilangan 0.
Pilihan: A. 2/4 (= 1/2)
B. 2/12 (= 1/6)
C. 3/12 (= 1/4)
D. 1/12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `b09a24b57d973871a9f482c8`

Seperangkat kartu berisi 5 kartu yang masing-masing bergambar lingkaran atau bintang. Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20. 450 407 400 350 300 250 200 150 93 100 50 0 Lingkaran Bintang Gambar yang Muncul Frekuensi Gambar Frekuensi Munculnya Kartu Bergambar Lingkaran dan Bintang<br><br>Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.

| Opsi | Isi |
|---|---|
| A | 4 kartu lingkaran dan 1 kartu bintang |
| B | 5 kartu lingkaran dan 0 kartu bintang |
| C | 1 kartu lingkaran dan 4 kartu bintang |
| D | 3 kartu lingkaran dan 2 kartu bintang |

![Gambar sumber soal 36](<../../../images/kelas9_crop-s0012-gambar-muncul.png>)


Kunci sumber: `A`; status AI: `conflict`; jawaban diverifikasi AI: `1 kartu lingkaran dan 4 kartu bintang`.
Solusi minimum hasil AI: Frekuensi relatif Lingkaran = 93/500 = 0,186. Frekuensi relatif Bintang = 407/500 = 0,814. Estimasi jumlah kartu (total 5): Lingkaran = 0,186 * 5 = 0,93 (dibulatkan menjadi 1); Bintang = 0,814 * 5 = 4,07 (dibulatkan menjadi 4). Jadi, terdapat 1 kartu lingkaran dan 4 kartu bintang.
Gambar sumber: images/kelas9_crop-s0012-gambar-muncul.png. Transkripsi visual: Grafik batang menunjukkan dua kategori pada sumbu horizontal: 'Lingkaran' dan 'Bintang'. Sumbu vertikal 'Frekuensi' memiliki skala 0 hingga 450. Batang 'Lingkaran' memiliki tinggi 93. Batang 'Bintang' memiliki tinggi 407. Total percobaan adalah 500.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f49917af0dbbda683720d630082e45cd570a8866b856f04a9a12c945c54c3dec`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | applying | procedural | Medium | 4216 |
| 2 | success | concern / conflict | applying | procedural | Medium | 4192 |
| 3 | success | concern / conflict | applying | procedural | Medium | 4231 |

Run 1 — solusi: Berdasarkan data grafik: Lingkaran muncul 93 kali, Bintang 407 kali dari 500 percobaan. Frekuensi relatif Lingkaran = 93/500 = 0,186. Frekuensi relatif Bintang = 407/500 = 0,814. Estimasi jumlah kartu: Lingkaran = 0,186 * 5 = 0,93 (dibulatkan menjadi 1), Bintang = 0,814 * 5 = 4,07 (dibulatkan menjadi 4). Jadi, 1 kartu lingkaran dan 4 kartu bintang.
- Domain kognitif `classify/applying`: Siswa diminta menghubungkan data frekuensi empiris (hasil percobaan) dengan estimasi komposisi ruang sampel (jumlah kartu). Ini memerlukan penerapan konsep peluang empiris untuk mengestimasi probabilitas teoretis, yang kemudian dikonversi menjadi jumlah objek diskrit.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.; Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan frekuensi relatif dan mengaitkannya dengan prinsip dasar peluang untuk mengestimasi komposisi populasi (jumlah kartu).. Bukti: frekuensi relatif lingkaran = 407/500 = 0,814, dikalikan 5 kartu = 4,07 ≈ 4
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan dua tahap: menghitung frekuensi relatif dari data empiris dan mengonversinya menjadi estimasi jumlah kartu dalam populasi kecil (5 kartu). Meskipun prosedurnya rutin, siswa harus memahami hubungan antara peluang empiris dan komposisi populasi.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.; Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif dan pembulatan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menginterpretasi data statistik sederhana dan melakukan estimasi berdasarkan proporsi, yang merupakan bagian dari kurikulum peluang. |

Run 2 — solusi: Berdasarkan data grafik (Lingkaran=93, Bintang=407), frekuensi relatif Lingkaran adalah 93/500 = 0,186 dan Bintang adalah 407/500 = 0,814. Jika total kartu adalah 5, maka jumlah kartu Lingkaran = 0,186 * 5 = 0,93 (dibulatkan menjadi 1) dan Bintang = 0,814 * 5 = 4,07 (dibulatkan menjadi 4). Jadi, seharusnya 1 lingkaran dan 4 bintang.
- Domain kognitif `classify/applying`: Siswa diminta menghubungkan data frekuensi empiris (hasil percobaan) dengan estimasi komposisi populasi (jumlah kartu). Ini memerlukan penerapan konsep peluang empiris untuk mengestimasi proporsi, yang merupakan penerapan prosedur pada konteks rutin.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.; Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme frekuensi relatif dan teknik pembulatan untuk mengestimasi komposisi objek, yang merupakan pengetahuan prosedural.. Bukti: frekuensi relatif lingkaran = 407/500 = 0,814, dikalikan 5 kartu = 4,07 ≈ 4
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut integrasi antara data empiris (frekuensi) dengan konsep proporsi untuk mengestimasi populasi. Siswa harus memahami bahwa frekuensi relatif mendekati peluang teoretis. Meskipun prosedurnya rutin, terdapat kebutuhan untuk menginterpretasikan data grafik dan melakukan konversi ke jumlah kartu.. Bukti: Seperangkat kartu berisi 5 kartu; 500 percobaan; Tentukan banyaknya kartu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif dan perbandingan/proporsi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghubungkan data frekuensi empiris dengan estimasi proporsi populasi. Soal ini menguji kemampuan tersebut dengan langkah-langkah yang terstruktur. |

Run 3 — solusi: Data grafik: Lingkaran=93, Bintang=407. Total=500. Peluang empiris Lingkaran=93/500=0,186; Bintang=407/500=0,814. Estimasi jumlah kartu (total 5): Lingkaran=0,186*5=0,93 (dibulatkan 1); Bintang=0,814*5=4,07 (dibulatkan 4). Jawaban seharusnya 1 Lingkaran dan 4 Bintang. Kunci sumber salah karena tertukar.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep peluang empiris untuk mengestimasi komposisi populasi (jumlah kartu) dari data sampel yang diberikan, yang merupakan penerapan konsep pada konteks rutin.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan frekuensi relatif dan mengalikannya dengan total populasi untuk mendapatkan estimasi, yang merupakan pengetahuan prosedural.. Bukti: Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa untuk menghubungkan konsep peluang empiris dengan estimasi jumlah objek dalam populasi. Meskipun prosedurnya rutin, siswa harus melakukan interpretasi data grafik dan pembulatan yang tepat untuk mendapatkan jawaban logis (jumlah kartu harus bilangan bulat).. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang empiris (frekuensi relatif) dan operasi aritmatika dasar (perkalian dan pembulatan). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menginterpretasi data statistik sederhana dan melakukan estimasi proporsional. Kesulitan terletak pada ketelitian membaca grafik dan logika pembulatan hasil estimasi ke bilangan bulat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `6179`.
Konten: `concern`; kunci: `conflict`; masalah: Kunci jawaban pada sumber (A: 4 lingkaran, 1 bintang) bertentangan dengan data grafik yang menunjukkan frekuensi bintang jauh lebih tinggi (407) daripada lingkaran (93).; Berdasarkan perhitungan frekuensi relatif (Lingkaran: 93/500 = 0,186; Bintang: 407/500 = 0,814) dan dikalikan dengan total 5 kartu, estimasi yang benar adalah 1 lingkaran dan 4 bintang.; Pilihan C (1 lingkaran, 4 bintang) secara matematis benar berdasarkan data, namun kunci sumber menyatakan A, yang menunjukkan kesalahan fatal pada kunci jawaban atau pelabelan grafik..
- Domain kognitif `applying`: Siswa harus menerapkan konsep peluang empiris (frekuensi relatif) untuk mengestimasi komposisi populasi (jumlah kartu) dari data sampel. Ini adalah penerapan prosedur rutin pada konteks data statistik.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritme perhitungan frekuensi relatif dan teknik pembulatan untuk mengestimasi komposisi objek, yang merupakan pengetahuan prosedural.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena menuntut integrasi antara data empiris dengan konsep proporsi untuk mengestimasi populasi. Siswa harus memahami hubungan antara frekuensi relatif dan peluang teoretis, serta melakukan pembulatan yang logis untuk mendapatkan jumlah kartu yang bulat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif, perbandingan/proporsi, dan pembulatan bilangan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menginterpretasi data statistik sederhana dan melakukan estimasi proporsional. Kesulitan terletak pada ketelitian membaca grafik dan logika pembulatan hasil estimasi ke bilangan bulat. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Seperangkat kartu berisi 5 kartu yang masing-masing bergambar lingkaran atau bintang. Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20. 450 407 400 350 300 250 200 150 93 100 50 0 Lingkaran Bintang Gambar yang Muncul Frekuensi Gambar Frekuensi Munculnya Kartu Bergambar Lingkaran dan Bintang

Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.
Pilihan: A. 4 kartu lingkaran dan 1 kartu bintang
B. 5 kartu lingkaran dan 0 kartu bintang
C. 1 kartu lingkaran dan 4 kartu bintang
D. 3 kartu lingkaran dan 2 kartu bintang
Transkripsi visual: Grafik batang menunjukkan dua kategori pada sumbu horizontal: 'Lingkaran' dan 'Bintang'. Sumbu vertikal 'Frekuensi' memiliki skala 0 hingga 450. Batang 'Lingkaran' memiliki tinggi 93. Batang 'Bintang' memiliki tinggi 407. Total percobaan adalah 500.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Kunci jawaban pada sumber (A: 4 lingkaran, 1 bintang) bertentangan dengan data grafik yang menunjukkan frekuensi bintang jauh lebih tinggi (407) daripada lingkaran (93).; Berdasarkan perhitungan frekuensi relatif (Lingkaran: 93/500 = 0,186; Bintang: 407/500 = 0,814) dan dikalikan dengan total 5 kartu, estimasi yang benar adalah 1 lingkaran dan 4 bintang.; Pilihan C (1 lingkaran, 4 bintang) secara matematis benar berdasarkan data, namun kunci sumber menyatakan A, yang menunjukkan kesalahan fatal pada kunci jawaban atau pelabelan grafik..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `0292b36d9d04627c0f3ae4e8`

Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan. b. Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.

| Opsi | Isi |
|---|---|
| A | 48 |
| B | 25 |
| C | 13 |
| D | 75 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `75`.
Solusi minimum hasil AI: Jumlah kartu remi = 52. Jumlah kartu hati = 13. Jumlah kartu bukan hati = 52 - 13 = 39. Peluang bukan hati P(A) = 39/52 = 3/4. Frekuensi harapan = P(A) * n = 3/4 * 100 = 75.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `daa094333664231ddc3039d281ebd8ef6e81027c48cbfadc7522cefd7c99165b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2734 |
| 2 | success | valid / verified | applying | procedural | Easy | 2793 |
| 3 | success | valid / verified | applying | procedural | Easy | 2712 |

Run 1 — solusi: Jumlah kartu remi = 52. Jumlah kartu hati = 13. Jumlah kartu bukan hati = 52 - 13 = 39. Peluang bukan hati P(A) = 39/52 = 3/4. Frekuensi harapan = P(A) * n = 3/4 * 100 = 75.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus frekuensi harapan Fh = P(A) x n pada konteks peluang kejadian komplemen (bukan kartu hati). Ini adalah penerapan prosedur rutin pada konteks yang sudah dikenal.. Bukti: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan; Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang konsep peluang teoritis dan frekuensi harapan, serta prosedur perhitungan untuk kejadian komplemen.. Bukti: frekuensi harapan; pengambilan satu kartu secara acak dari seperangkat kartu remi
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat langsung dan familiar bagi siswa kelas 9. Siswa hanya perlu mengidentifikasi jumlah kartu, menentukan peluang komplemen, dan mengalikan dengan jumlah percobaan.. Bukti: 100 kali percobaan; tidak didapatkan kartu hati

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, peluang kejadian komplemen, dan frekuensi harapan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan dan peluang kartu remi adalah standar kurikulum kelas 9. Langkah penyelesaian bersifat linear dan tidak memerlukan integrasi konsep yang kompleks. |

Run 2 — solusi: Jumlah kartu remi = 52. Kartu hati = 13. Kartu bukan hati = 52 - 13 = 39. Peluang bukan hati P(A) = 39/52 = 3/4. Frekuensi harapan = P(A) * n = 3/4 * 100 = 75.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang teoritis dan frekuensi harapan pada konteks yang rutin (kartu remi). Langkah-langkahnya jelas: menentukan peluang komplemen, lalu mengalikan dengan jumlah percobaan.. Bukti: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan.; Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung frekuensi harapan dan konsep dasar peluang kejadian komplemen dalam set kartu remi.. Bukti: frekuensi harapan; pengambilan satu kartu secara acak dari seperangkat kartu remi
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan prosedur standar yang familiar bagi siswa kelas 9. Jalur penyelesaiannya linear: menghitung peluang kejadian komplemen (bukan hati) lalu mengalikan dengan total percobaan. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan.; Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, peluang kejadian komplemen, dan operasi perkalian pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari rumus frekuensi harapan yang diajarkan di kelas 9. Tidak ada kompleksitas tambahan dalam pemilihan strategi atau integrasi konsep. |

Run 3 — solusi: Jumlah kartu remi = 52. Jumlah kartu hati = 13. Jumlah kartu bukan hati = 52 - 13 = 39. Peluang bukan hati P(A) = 39/52 = 3/4. Frekuensi harapan = P(A) * n = 3/4 * 100 = 75.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang komplemen dan frekuensi harapan pada konteks yang sudah familiar (kartu remi). Ini adalah penerapan prosedur standar.. Bukti: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan.; Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma frekuensi harapan dan pengetahuan faktual mengenai komposisi kartu remi.. Bukti: frekuensi harapan; pengambilan satu kartu secara acak dari seperangkat kartu remi
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena prosedurnya langsung (menghitung peluang komplemen lalu dikalikan jumlah percobaan). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: 100 kali percobaan; tidak didapatkan kartu hati

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, peluang komplemen, dan frekuensi harapan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan sudah familiar dengan perhitungan frekuensi harapan dan komposisi kartu remi sebagai contoh standar ruang sampel. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan. b. Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.
Pilihan: A. 48
B. 25
C. 13
D. 75
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `dfd8cbd993b44696494b45c1`

Di sebuah kota, persentase penduduknya yang masuk Generasi Z adalah 28%. Jika kalian memilih 75 penduduk kota itu secara acak, tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z.

| Opsi | Isi |
|---|---|
| A | 28 |
| B | 47 |
| C | 75 |
| D | 21 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `21`.
Solusi minimum hasil AI: Frekuensi harapan (Fh) dihitung dengan rumus Fh = P(A) x n. Diketahui P(A) = 28% = 0,28 dan n = 75. Maka, Fh = 0,28 x 75 = 21.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a50a488b90d89bfcf0ffedefb2655315716b2001f7febb635cd88da9ba16afed`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2657 |
| 2 | success | valid / verified | applying | procedural | Easy | 2656 |
| 3 | success | valid / verified | applying | procedural | Easy | 2705 |

Run 1 — solusi: Frekuensi harapan (Fh) dihitung dengan rumus Fh = P(A) x n. Diketahui P(A) = 28% = 0,28 dan n = 75. Maka, Fh = 0,28 x 75 = 21.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus frekuensi harapan secara langsung dengan nilai yang sudah diberikan. Ini adalah prosedur standar yang familiar bagi siswa kelas 9.. Bukti: tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep frekuensi harapan sebagai hasil kali peluang kejadian dengan banyaknya percobaan.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan dua angka yang diberikan (persentase dan jumlah sampel). Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang dan perkalian bilangan desimal/persen. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung rumus frekuensi harapan yang merupakan materi dasar kelas 9. Tidak ada tuntutan integrasi atau penalaran non-rutin. |

Run 2 — solusi: Frekuensi harapan (Fh) dihitung dengan mengalikan peluang kejadian (P) dengan banyaknya percobaan (n). Diketahui P = 28% = 0,28 dan n = 75. Maka, Fh = 0,28 * 75 = 21.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus frekuensi harapan secara langsung dengan data yang sudah tersedia (persentase dan jumlah sampel). Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep frekuensi harapan sebagai hasil kali peluang dengan banyaknya percobaan, yang merupakan pengetahuan prosedural standar.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan dua angka yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan operasi perkalian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan adalah materi standar kelas 9. Soal ini merupakan penerapan langsung rumus tanpa modifikasi atau konteks yang membingungkan. |

Run 3 — solusi: Frekuensi harapan (Fh) dihitung dengan rumus Fh = P(A) x n, di mana P(A) adalah peluang kejadian dan n adalah banyaknya percobaan. Diketahui P(A) = 28% = 0,28 dan n = 75. Maka, Fh = 0,28 x 75 = 21.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus frekuensi harapan secara langsung dengan data yang sudah tersedia (peluang dan jumlah sampel). Ini adalah prosedur standar yang familiar bagi siswa kelas 9.. Bukti: tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep frekuensi harapan sebagai hasil kali antara peluang kejadian dengan banyaknya percobaan (prosedural) dan bagaimana menerjemahkan persentase ke dalam bentuk desimal/pecahan (konseptual).. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengalikan dua angka yang diberikan (28% dan 75). Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan operasi perkalian bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung rumus frekuensi harapan yang merupakan materi standar kelas 9. Tidak ada tuntutan kognitif tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4148`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal meminta penerapan langsung rumus frekuensi harapan (Fh = P x n) dengan nilai yang sudah tersedia secara eksplisit. Ini adalah prosedur standar yang rutin.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami konsep frekuensi harapan sebagai hasil kali peluang kejadian dengan banyaknya percobaan, yang merupakan pengetahuan prosedural standar.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan dua angka yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase dan operasi perkalian bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan adalah materi standar kelas 9. Soal ini merupakan penerapan langsung rumus tanpa modifikasi atau konteks yang membingungkan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah kota, persentase penduduknya yang masuk Generasi Z adalah 28%. Jika kalian memilih 75 penduduk kota itu secara acak, tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z.
Pilihan: A. 28
B. 47
C. 75
D. 21
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `4e77f956826bf22b33dbf58b`

Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.

| Opsi | Isi |
|---|---|
| A | 3/125 |
| B | 10/125 (atau 0,08) |
| C | 6/125 |
| D | 5/125 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 berarti jumlah ketiga angka < 6 (yaitu 3, 4, atau 5). Kombinasi yang memenuhi: jumlah 3 (1,1,1) ada 1 cara; jumlah 4 (1,1,2 dan permutasi) ada 3 cara; jumlah 5 (1,1,3 dan 1,2,2 serta permutasi) ada 3+3=6 cara. Total kejadian = 1+3+6 = 10. Peluang = 10/125.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `19125824549b8936abc699c3eb411a6ec18e2aa24236a6d16528c832d7e48716`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 2910 |
| 2 | success | valid / verified | reasoning | procedural | Medium | 4072 |
| 3 | success | valid / verified | reasoning | procedural | Medium | 3875 |

Run 1 — solusi: Total ruang sampel = 5^3 = 125. Rata-rata < 2 berarti jumlah ketiga angka < 6. Kemungkinan jumlah: (1,1,1) jumlah 3 (1 cara); (1,1,2), (1,2,1), (2,1,1) jumlah 4 (3 cara); (1,1,3), (1,3,1), (3,1,1), (1,2,2), (2,1,2), (2,2,1) jumlah 5 (6 cara). Total kejadian = 1 + 3 + 6 = 10. Peluang = 10/125.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep ruang sampel kejadian majemuk dengan syarat rata-rata, yang memerlukan perencanaan sistematis untuk mendaftar kombinasi angka yang memenuhi kondisi jumlah < 6.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang ruang sampel kejadian majemuk dan prosedur untuk menghitung peluang berdasarkan kondisi yang diberikan.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Hard`: Soal ini menuntut perencanaan langkah yang saling bergantung (menentukan total ruang sampel, menerjemahkan rata-rata ke jumlah, dan mendaftar kombinasi secara sistematis). Meskipun prosedurnya familiar, integrasi syarat jumlah < 6 dengan ruang sampel 125 memerlukan ketelitian tinggi.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk dan aturan perkalian dasar. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung peluang kejadian majemuk, namun mendaftar kombinasi untuk memenuhi syarat rata-rata tanpa melewatkan satu pun kasus adalah tugas yang menuntut ketelitian dan perencanaan tinggi. |

Run 2 — solusi: Total ruang sampel = 5^3 = 125. Rata-rata < 2 berarti jumlah 3 angka < 6 (yaitu 3, 4, atau 5). Kemungkinan: jumlah 3 (1,1,1) ada 1 cara; jumlah 4 (1,1,2; 1,2,1; 2,1,1) ada 3 cara; jumlah 5 (1,1,3; 1,3,1; 3,1,1; 1,2,2; 2,1,2; 2,2,1) ada 6 cara. Total cara = 1+3+6 = 10. Peluang = 10/125.
- Domain kognitif `classify/reasoning`: Siswa harus menerjemahkan kondisi rata-rata ke dalam batasan jumlah, lalu melakukan enumerasi sistematis untuk menghitung ruang sampel yang memenuhi syarat. Ini memerlukan integrasi konsep rata-rata dan peluang.. Bukti: rata-ratanya kurang dari 2; memutar roda tersebut sebanyak tiga kali
- Dimensi pengetahuan `classify/procedural`: Melibatkan penerapan prosedur sistematis untuk menghitung ruang sampel dan kejadian yang memenuhi syarat.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Soal memerlukan perencanaan enumerasi sistematis untuk jumlah 3, 4, dan 5. Meskipun prosedurnya familiar, siswa harus mengintegrasikan kondisi rata-rata ke jumlah total dan memastikan tidak ada kombinasi yang terlewat. Tidak terlalu sulit karena ruang sampel kecil dan kondisi terbatas.. Bukti: rata-ratanya kurang dari 2; memutar roda tersebut sebanyak tiga kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, rata-rata, dan teknik pencacahan sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pencacahan sistematis untuk masalah peluang sederhana. Soal ini menuntut ketelitian dalam enumerasi. |

Run 3 — solusi: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 berarti jumlah ketiga angka < 6 (yaitu 3, 4, atau 5). Kombinasi yang memenuhi: jumlah 3 (1,1,1) ada 1 cara; jumlah 4 (1,1,2 dan permutasi) ada 3 cara; jumlah 5 (1,1,3 dan 1,2,2 serta permutasi) ada 3+3=6 cara. Total kejadian = 1+3+6 = 10. Peluang = 10/125.
- Domain kognitif `classify/reasoning`: Siswa harus menerjemahkan syarat rata-rata ke dalam syarat jumlah, lalu melakukan pencacahan sistematis untuk setiap kemungkinan jumlah yang memenuhi syarat. Ini memerlukan integrasi konsep peluang dan strategi pencacahan.. Bukti: rata-ratanya kurang dari 2; memutar roda tersebut sebanyak tiga kali
- Dimensi pengetahuan `classify/procedural`: Melibatkan penerapan prosedur pencacahan sistematis untuk menentukan ruang sampel dan kejadian yang memenuhi syarat.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Soal memerlukan perencanaan langkah (mengubah rata-rata ke jumlah, lalu mencacah). Siswa harus teliti dalam permutasi agar tidak ada yang terlewat. Ini bukan sekadar penerapan rumus langsung, namun prosedurnya familiar bagi kelas 9.. Bukti: rata-ratanya kurang dari 2; memutar roda tersebut sebanyak tiga kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang dasar, aturan perkalian, dan rata-rata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pencacahan sistematis untuk ruang sampel kecil. Soal menguji ketelitian dalam permutasi dan pemahaman hubungan rata-rata dengan jumlah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Hard": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4659`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus menerjemahkan kondisi rata-rata ke dalam batasan jumlah, lalu melakukan enumerasi sistematis untuk menghitung ruang sampel yang memenuhi syarat. Ini memerlukan integrasi konsep rata-rata dan peluang.
- Dimensi pengetahuan `procedural`: Melibatkan penerapan prosedur sistematis untuk menghitung ruang sampel dan kejadian yang memenuhi syarat.
- Intended difficulty `Medium`: Soal memerlukan perencanaan enumerasi sistematis untuk jumlah 3, 4, dan 5. Meskipun prosedurnya familiar, siswa harus mengintegrasikan kondisi rata-rata ke jumlah total dan memastikan tidak ada kombinasi yang terlewat. Tidak terlalu sulit karena ruang sampel kecil dan kondisi terbatas.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, aturan perkalian, dan rata-rata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pencacahan sistematis untuk masalah peluang sederhana. Soal ini menuntut ketelitian dalam enumerasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.
Pilihan: A. 3/125
B. 10/125 (atau 0,08)
C. 6/125
D. 5/125
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `d57b84b818b2d3b772624d73`

Dhien adalah calon ketua OSIS. Dia ingin mengetahui persentase teman-teman di sekolahnya yang akan memilihnya.<br><br>Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa? ⓐ Dia bertanya kepada semua teman sekelasnya. ⓑ Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera. ⓒ Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya.

| Opsi | Isi |
|---|---|
| A | Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera |
| B | Dia menyurvei murid yang kebetulan lewat di depan kelasnya saat istirahat |
| C | Dia bertanya kepada semua teman sekelasnya |
| D | Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Metode A (menyurvei siswa urutan ke-3, 6, dan 9 di setiap barisan upacara) adalah metode sampling sistematis yang paling representatif. Metode ini mencakup seluruh populasi siswa di sekolah (semua barisan upacara), sehingga meminimalkan bias. Pilihan lain (bertanya ke teman sekelas atau media sosial) bersifat bias karena sampel hanya mewakili kelompok tertentu (bias populasi atau bias akses).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3c5cf78c70a2bb3c6226ded29a41c8617a791626f90a8b12f665620f6a3cd31c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / verified | reasoning | conceptual | Medium | 4336 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2800 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2775 |

Run 1 — solusi: Metode A (menyurvei siswa urutan ke-3, 6, 9 saat upacara) adalah yang terbaik karena menggunakan teknik sampling sistematis yang mencakup seluruh populasi siswa di sekolah, sehingga meminimalkan bias. Pilihan lain (teman sekelas, media sosial, atau siswa yang lewat) bersifat convenience sampling yang cenderung bias.
- Domain kognitif `classify/reasoning`: Siswa perlu mengevaluasi dan membandingkan tiga metode sampling untuk menentukan mana yang paling representatif dan minim bias, yang merupakan aktivitas penalaran (reasoning) untuk memilih strategi yang tepat.. Bukti: mana yang seharusnya dipilih Dhien?; Mengapa?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang prinsip-prinsip pemilihan sampel yang representatif dan sumber bias dalam statistika, bukan sekadar prosedur hitung.. Bukti: persentase teman-teman di sekolahnya; kemungkinan cara pemilihan sampel
- Intended difficulty `classify/Medium`: Soal menuntut siswa memahami konsep bias sampling. Siswa harus menganalisis tiga skenario berbeda dan memilih yang paling acak/sistematis. Ini adalah tugas Medium karena memerlukan pemahaman konseptual tentang representasi populasi, bukan sekadar prosedur hitung.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien?; Mengapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi, sampel, dan bias dalam statistika. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena menuntut pemahaman tentang pemilihan sampel yang valid, yang merupakan bagian dari kurikulum statistika SMP. |

Run 2 — solusi: Opsi A (menyurvei siswa urutan ke-3, 6, 9 di setiap barisan upacara) adalah metode sampling sistematis yang paling representatif karena mencakup seluruh populasi sekolah (semua barisan) dan mengurangi bias dibandingkan metode lain yang hanya mengambil sampel dari kelompok tertentu (teman sekelas) atau kelompok yang memiliki akses/kebiasaan tertentu (media sosial).
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk mengevaluasi dan memilih metode pengambilan sampel yang paling representatif, yang memerlukan pemahaman konseptual tentang bias sampling dan representasi populasi.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip-prinsip dasar sampling (konsep bias vs representasi) untuk menentukan metode mana yang paling valid secara statistik.. Bukti: mana yang seharusnya dipilih Dhien? Mengapa?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk membedakan berbagai metode sampling dan memahami konsep bias dalam konteks nyata. Meskipun prosedurnya tidak rumit secara matematis, siswa perlu melakukan analisis kritis terhadap setiap opsi untuk menentukan mana yang paling tidak bias, yang merupakan keterampilan berpikir tingkat tinggi untuk level SMP.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi, sampel, dan konsep bias dalam survei. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengevaluasi validitas metode pengumpulan data sederhana. Soal ini menguji kemampuan penalaran tentang representasi sampel tanpa memerlukan perhitungan kompleks. |

Run 3 — solusi: Sampel yang representatif harus mencakup seluruh populasi (siswa sekolah) secara acak. Opsi (a) bias karena hanya satu kelas. Opsi (c) bias karena hanya siswa aktif media sosial. Opsi (b) menggunakan sistematis sampling (setiap kelipatan 3) yang mencakup seluruh barisan upacara, sehingga lebih acak dan representatif.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengevaluasi dan memilih metode pengambilan sampel yang paling representatif (tidak bias) dari beberapa skenario, yang memerlukan pemahaman konsep dasar sampling.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar pemilihan sampel yang representatif (konsep statistik) untuk menentukan metode mana yang paling minim bias.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual namun prosedurnya sangat familiar dalam kurikulum SMP. Siswa hanya perlu mengidentifikasi sumber bias pada setiap opsi (bias kelas, bias media sosial, bias kenyamanan) dan memilih metode yang paling acak/sistematis. Tidak ada perhitungan kompleks atau integrasi langkah yang rumit.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi, sampel, dan bias dalam survei. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pemilihan sampel adalah bagian dari kurikulum SMP kelas 9. Soal ini menguji pemahaman dasar tentang representasi sampel tanpa menuntut analisis statistik yang mendalam. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 2, "applying": 1} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4416`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus mengevaluasi tiga metode sampling yang berbeda, mengidentifikasi potensi bias pada masing-masing metode, dan memilih metode yang paling representatif. Proses evaluasi dan perbandingan ini merupakan aktivitas penalaran (reasoning) untuk menentukan strategi pengambilan data yang valid.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang prinsip-prinsip dasar statistika, yaitu apa yang membuat sebuah sampel representatif dan bagaimana bias dapat muncul dalam pemilihan sampel.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk melakukan analisis kritis terhadap tiga skenario sampling yang berbeda. Siswa tidak hanya mengenali istilah, tetapi harus memahami hubungan antara metode pemilihan dan potensi bias yang dihasilkan. Meskipun tidak ada perhitungan numerik, tuntutan untuk mengintegrasikan pemahaman tentang representasi populasi dan bias sampling membuat soal ini melampaui sekadar penerapan prosedur langsung (Easy).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi, sampel, dan konsep bias dalam survei. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengevaluasi validitas metode pengumpulan data sederhana. Soal ini menguji kemampuan penalaran tentang representasi sampel tanpa memerlukan perhitungan kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dhien adalah calon ketua OSIS. Dia ingin mengetahui persentase teman-teman di sekolahnya yang akan memilihnya.

Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa? ⓐ Dia bertanya kepada semua teman sekelasnya. ⓑ Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera. ⓒ Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya.
Pilihan: A. Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera
B. Dia menyurvei murid yang kebetulan lewat di depan kelasnya saat istirahat
C. Dia bertanya kepada semua teman sekelasnya
D. Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `b0bcef02731ce1c1ec1f8a92`

Pilihan dadu<br><br>\|Pilihan 1\|Pilihan 2\|<br>\|---\|---\|<br>\|Dadu kubus dengan sisi sebagai\|Dadu piramida dengan sisi\|<br>\|berikut:\|sebagai berikut:\|<br>\|1, 2, 3, 4, 5, 6\|1, 2, 3, 4\|<br><br>Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!

| Opsi | Isi |
|---|---|
| A | Keduanya sama besar karena sama-sama punya satu angka 3 |
| B | Pilihan 1 (dadu kubus) |
| C | Pilihan 2 (dadu piramida) |
| D | Tidak bisa ditentukan karena bentuk dadunya berbeda |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Peluang muncul angka 3 pada dadu kubus (6 sisi) adalah 1/6. Peluang muncul angka 3 pada dadu piramida (4 sisi) adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menerapkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `86c95cfca3df133feb39c9d52c63a5018af97321ed0f185b6611694ca414de39`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2821 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2812 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2858 |

Run 1 — solusi: Peluang muncul angka 3 pada dadu kubus (6 sisi) adalah 1/6. Peluang muncul angka 3 pada dadu piramida (4 sisi) adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua peluang kejadian sederhana (1/6 vs 1/4) untuk menentukan mana yang lebih besar. Ini adalah penerapan konsep peluang dasar pada konteks perbandingan.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana jumlah ruang sampel (total sisi) memengaruhi peluang kejadian dengan jumlah titik sampel yang sama.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu menghitung dua nilai peluang dasar (1/6 dan 1/4) dan membandingkannya. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.; Syarat menangnya adalah mendapatkan angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (peluang = kejadian/ruang sampel) dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang adalah standar kelas 9. Membandingkan dua pecahan sederhana adalah tugas rutin yang sesuai dengan tingkat kemampuan siswa kelas 9. |

Run 2 — solusi: Peluang muncul angka 3 pada dadu kubus (6 sisi) adalah 1/6. Peluang muncul angka 3 pada dadu piramida (4 sisi) adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua peluang kejadian sederhana dengan menghitung rasio kejadian yang diinginkan terhadap total ruang sampel untuk masing-masing dadu, kemudian membandingkan kedua nilai pecahan tersebut.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi peluang klasik (kejadian yang diharapkan dibagi total ruang sampel) dan kemampuan membandingkan nilai pecahan.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu menerapkan rumus peluang dasar pada dua objek yang sudah didefinisikan ruang sampelnya secara eksplisit. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian sederhana dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang adalah standar kelas 9. Membandingkan dua peluang sederhana adalah tugas rutin yang tidak memerlukan integrasi konsep yang rumit. |

Run 3 — solusi: Peluang muncul angka 3 pada dadu kubus adalah 1/6. Peluang muncul angka 3 pada dadu piramida adalah 1/4. Karena 1/4 > 1/6, maka peluang menang lebih besar jika menggunakan dadu piramida (Pilihan 2).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang teoritis (rasio kejadian yang diinginkan terhadap total ruang sampel) pada dua objek yang berbeda dan membandingkan hasilnya untuk mengambil keputusan.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana ukuran ruang sampel mempengaruhi peluang suatu kejadian.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur perhitungannya sangat langsung (1/6 vs 1/4) dan konsep peluang dasar sudah familiar bagi siswa kelas 9. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Pilihan 1 (dadu kubus) ... 1, 2, 3, 4, 5, 6; Pilihan 2 (dadu piramida) ... 1, 2, 3, 4; Syarat menangnya adalah mendapatkan angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (peluang = kejadian/ruang sampel) dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung peluang sederhana dan membandingkan dua pecahan dengan penyebut berbeda tanpa kesulitan berarti. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Membandingkan Peluang Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Pilihan dadu

|Pilihan 1|Pilihan 2|
|---|---|
|Dadu kubus dengan sisi sebagai|Dadu piramida dengan sisi|
|berikut:|sebagai berikut:|
|1, 2, 3, 4, 5, 6|1, 2, 3, 4|

Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!
Pilihan: A. Keduanya sama besar karena sama-sama punya satu angka 3
B. Pilihan 1 (dadu kubus)
C. Pilihan 2 (dadu piramida)
D. Tidak bisa ditentukan karena bentuk dadunya berbeda
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| B | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| C | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Data terurut (n=14): 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Median (Q2) = (65+70)/2 = 67,5. Q1 (median 7 data pertama) = 65. Q3 (median 7 data terakhir) = 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * IQR = 7,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `35aed6ec6feb02db34db3fc591c46ccd28f230c4e20b78b1906b78fa92a7deb6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3192 |
| 2 | success | valid / verified | applying | procedural | Medium | 3180 |
| 3 | success | valid / verified | applying | procedural | Medium | 3229 |

Run 1 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 (median) = (65+70)/2 = 67,5. Data bawah (7 data): 50, 50, 60, 65, 65, 65, 65 -> Q1 = 65. Data atas (7 data): 70, 75, 80, 80, 85, 85, 90 -> Q3 = 80. Jangkauan kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menentukan statistik lima serangkai (kuartil) dari sekumpulan data. Ini adalah penerapan langsung dari algoritma yang dipelajari di kelas 9.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung statistik deskriptif (kuartil) dari data tunggal.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengurutkan data dan menerapkan rumus kuartil. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data dan menentukan median. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung kuartil adalah materi standar kelas 9. Prosedur pengurutan dan pembagian data menjadi dua bagian adalah langkah rutin yang familiar. |

Run 2 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 (median) = (65+70)/2 = 67,5. Q1 (median data ke-1 s.d ke-7) = 65. Q3 (median data ke-8 s.d ke-14) = 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar (menentukan kuartil dan simpangan kuartil) pada sekumpulan data yang diberikan. Ini adalah penerapan konsep yang rutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme dan metode statistik untuk mengolah data (kuartil, jangkauan, simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini termasuk kategori Medium karena memerlukan ketelitian dalam mengurutkan data (14 data) dan menerapkan prosedur kuartil yang berjenjang (Q1, Q2, Q3, lalu IQR dan simpangan kuartil). Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling bergantung dan potensi kesalahan hitung yang moderat.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan data dan menentukan median. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengolah data statistik dasar. Soal ini menuntut ketelitian dalam pengurutan dan perhitungan bertahap, namun metodenya sangat standar. |

Run 3 — solusi: Data terurut (n=14): 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Median (Q2) = (65+70)/2 = 67,5. Q1 (median 7 data pertama: 50, 50, 60, 65, 65, 65, 65) = 65. Q3 (median 7 data terakhir: 70, 75, 80, 80, 85, 85, 90) = 80. Jangkauan antar kuartil (H) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil (Qd) = 0,5 * H = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar untuk menentukan ukuran penyebaran data (kuartil, jangkauan, simpangan kuartil) pada sekumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman dan penerapan algoritme atau prosedur statistik untuk mengolah data menjadi ukuran penyebaran.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut ketelitian dalam mengurutkan data (14 data) dan menerapkan prosedur kuartil yang melibatkan pembagian data menjadi dua kelompok. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait (mengurutkan, mencari median, membagi data, menghitung selisih) yang meningkatkan beban kognitif dibandingkan soal satu langkah.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan data dan menentukan median. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengolah data statistik sederhana. Soal ini memerlukan ketelitian prosedural yang cukup untuk menghindari kesalahan pada langkah-langkah berurutan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5208`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur statistik standar untuk menentukan ukuran penyebaran data (kuartil, jangkauan, simpangan kuartil) dari sekumpulan data yang diberikan. Ini adalah penerapan algoritma yang rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang algoritme statistik untuk mengolah data tunggal menjadi ukuran penyebaran.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut ketelitian tinggi dalam mengurutkan 14 data dan melakukan langkah-langkah berjenjang (Q1, Q2, Q3, IQR, simpangan kuartil). Meskipun prosedurnya familiar, ketergantungan antar langkah dan potensi kesalahan hitung pada data yang cukup banyak meningkatkan beban kognitif.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data dan menentukan median. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengolah data statistik. Soal ini memerlukan ketelitian prosedural yang cukup untuk menghindari kesalahan pada langkah-langkah berurutan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Penyebaran Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65
Pilihan: A. Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
B. Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5
C. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
D. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
