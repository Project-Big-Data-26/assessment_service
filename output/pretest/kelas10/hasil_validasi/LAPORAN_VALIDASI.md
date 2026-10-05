# Validasi ulang soal kelas 10 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-sma10-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sma10-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 10 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 10, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 46; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 38, "knowing": 7, "reasoning": 1}, "knowledgeDimension": {"conceptual": 18, "procedural": 27, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 33, "Medium": 13, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 38, "knowing": 7, "reasoning": 1}, "knowledgeDimension": {"conceptual": 18, "procedural": 27, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 33, "Medium": 13, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 46}`.
Run awal sukses: 138/138; adjudikasi: 19; token sukses tercatat: 543,494.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 33 | 33 | [Easy.json](difficulty/Easy.json) |
| Medium | 13 | 13 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 10, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 10, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 10.

## 1. Soal `20c03a0ebabbdc13efb66801`

Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.<br><br>\|Fase penyebaran\|1\|2\|3\|4\|5\|6\|7\|8\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Banyak orang yang menerima hoaks\|2\|4\|…\|….\|….\|….\|….\|….\|<br><br>Jika banyak fase adalah n, tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?

| Opsi | Isi |
|---|---|
| A | $2^{n-1}$ |
| B | $2n$ |
| C | $n^2$ |
| D | $2^n$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola penyebaran adalah 2, 4, 8, 16, ... yang merupakan perpangkatan dari 2. Pada fase ke-1 (n=1), jumlah orang adalah 2^1 = 2. Pada fase ke-2 (n=2), jumlah orang adalah 2^2 = 4. Maka, untuk fase ke-n, rumusnya adalah 2^n.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7e2c62b696cf98f80bedf4eced5269b2a4e1aad18541c2a9756e262409f43cbd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2841 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2861 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2774 |

Run 1 — solusi: Pola penyebaran adalah 2, 4, 8, 16, ... yang merupakan perpangkatan dari 2. Pada fase ke-1 (n=1), jumlah orang adalah 2^1 = 2. Pada fase ke-2 (n=2), jumlah orang adalah 2^2 = 4. Maka, untuk fase ke-n, rumusnya adalah 2^n.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali pola bilangan (2, 4, 8, ...) dan menggeneralisasikannya ke dalam bentuk rumus eksponensial sederhana. Ini melibatkan penerapan konsep eksponen pada konteks pertumbuhan yang diberikan.. Bukti: Lengkapilah tabel di bawah ini; tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pertumbuhan eksponensial dan bagaimana merepresentasikannya dalam bentuk rumus matematika.. Bukti: tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena pola pertumbuhan eksponensial (2, 4, 8, ...) sangat eksplisit dan familiar bagi siswa kelas 10. Langkah penyelesaiannya langsung, tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit.. Bukti: Lengkapilah tabel di bawah ini; tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen (perpangkatan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola pertumbuhan eksponensial dasar seperti ini merupakan materi standar kelas 10 yang sering ditemui. Tidak ada tuntutan kognitif tinggi dalam menentukan rumus dari deret yang sudah jelas. |

Run 2 — solusi: Pola penyebaran adalah 2, 4, 8, 16, ... yang merupakan barisan geometri dengan suku pertama a=2 dan rasio r=2. Pada fase ke-n, banyak orang yang menerima adalah 2^1, 2^2, 2^3, ..., 2^n. Jadi, rumus untuk fase ke-n adalah 2^n.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pola dari data yang diberikan (2, 4, 8, ...) dan merumuskan fungsi eksponensial yang sesuai. Ini melibatkan pengenalan pola dan penerapan konsep eksponen dalam konteks pertumbuhan, yang masuk dalam domain applying.. Bukti: Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.; tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip pertumbuhan eksponensial dan bagaimana merepresentasikannya dalam bentuk rumus matematika (konsep), serta menerapkan prosedur untuk menentukan rumus umum dari pola yang ada.. Bukti: tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Pola pertumbuhan eksponensial (2, 4, 8, 16) sangat familiar dan langkah penyelesaiannya langsung (mengenali pola dan menuliskan rumus). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Lengkapilah tabel di bawah ini; tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari konsep eksponen yang dipelajari di kelas 10. Pola yang diberikan sangat jelas dan tidak memerlukan perencanaan langkah yang kompleks. |

Run 3 — solusi: Pola penyebaran adalah 2, 4, 8, 16, ... yang merupakan barisan geometri dengan suku pertama a=2 dan rasio r=2. Pada fase ke-n, banyak orang yang menerima hoaks adalah 2^n.
- Domain kognitif `classify/applying`: Siswa diminta mengenali pola pertumbuhan eksponensial dari data yang diberikan dan merumuskan fungsi umum. Ini melibatkan pemahaman konsep eksponen sebagai pertumbuhan berlipat, bukan sekadar menghitung.. Bukti: Tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara fase (n) dan jumlah penerima (hasil perpangkatan) untuk membangun model matematika (rumus) dari situasi nyata.. Bukti: Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Pola 2, 4, 8, 16 sangat familiar dan langsung mengarah pada 2^n. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah aplikasi langsung dari konsep eksponen yang merupakan materi dasar kelas 10. Siswa hanya perlu mengenali pola barisan geometri sederhana. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Definisi Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.

|Fase penyebaran|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|Banyak orang yang menerima hoaks|2|4|…|….|….|….|….|….|

Jika banyak fase adalah n, tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?
Pilihan: A. $2^{n-1}$
B. $2n$
C. $n^2$
D. $2^n$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `1a4524c9fb9888217a46bdf7`

Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Dengan asumsi setiap orang yang menerima pesan ini tidak mengetahui bahwa ini adalah hoaks, bayangkan betapa cepat hoaks ini akan tersebar. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.<br><br>\|Fase penyebaran\|1\|2\|3\|4\|5\|6\|7\|8\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Banyak orang yang menerima hoaks\|2\|4\|…\|….\|….\|….\|….\|….\|<br><br>Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?

| Opsi | Isi |
|---|---|
| A | 128 orang |
| B | 64 orang |
| C | 12 orang |
| D | 32 orang |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pola penyebaran mengikuti fungsi eksponensial f(n) = 2^n, di mana n adalah fase penyebaran. Untuk fase ke-6, jumlah orang yang menerima hoaks adalah 2^6 = 64.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe74bd635f9cf445ce2cb5f9a07916bdff55c1deef4a551f4708028ae97cc903`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2778 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2888 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2845 |

Run 1 — solusi: Pola penyebaran mengikuti fungsi eksponensial f(n) = 2^n, di mana n adalah fase penyebaran. Untuk fase ke-6, jumlah orang yang menerima hoaks adalah 2^6 = 64.
- Domain kognitif `classify/applying`: Siswa diminta mengenali pola pertumbuhan eksponensial dari data yang diberikan dan menerapkan rumus eksponen untuk menghitung nilai pada fase tertentu. Ini adalah penerapan prosedur yang familiar.. Bukti: Lengkapilah tabel di bawah ini; hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pertumbuhan eksponensial (pola berlipat dua) dan prosedur perhitungannya.. Bukti: memanfaatkan pola bilangan tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Pola pertumbuhan eksponensial (2^n) sangat jelas dari data fase 1 dan 2. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks; siswa hanya perlu mengenali pola dan melakukan perhitungan eksponen dasar.. Bukti: Lengkapilah tabel di bawah ini; hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang eksponen dan pola bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah materi dasar kelas 10. Soal ini memberikan konteks yang sangat jelas dan langsung mengarahkan siswa pada pola yang harus digunakan tanpa kerumitan tambahan. |

Run 2 — solusi: Pola penyebaran mengikuti fungsi eksponensial f(n) = 2^n, di mana n adalah fase penyebaran. Untuk fase ke-6, jumlah orang yang menerima hoaks adalah 2^6 = 64.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali pola pertumbuhan eksponensial dari konteks yang diberikan dan menerapkan rumus tersebut untuk menghitung nilai pada fase tertentu. Ini adalah penerapan prosedur yang langsung.. Bukti: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya.; Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.; Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep pertumbuhan eksponensial (konseptual) dan kemampuan menggunakan pola tersebut untuk menghitung nilai (prosedural).. Bukti: pola bilangan tersebut; 2 orang temannya; 2^n
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena pola pertumbuhan (2^n) sangat eksplisit dan familiar bagi siswa kelas 10. Langkah penyelesaiannya linear, tidak memerlukan integrasi kendala yang kompleks, dan tabel yang disediakan berfungsi sebagai perancah (scaffold) yang kuat untuk membantu siswa menemukan pola.. Bukti: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya.; Lengkapilah tabel di bawah ini; hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang eksponen dan pola bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 SMA sudah sangat familiar dengan pola pertumbuhan eksponensial sederhana. Soal memberikan tabel yang memandu siswa untuk melihat pola sebelum melakukan perhitungan, sehingga beban kognitif sangat rendah. |

Run 3 — solusi: Pola penyebaran hoaks mengikuti fungsi eksponensial f(n) = 2^n, dengan n adalah fase penyebaran. Untuk fase ke-6, jumlah orang yang menerima hoaks adalah 2^6 = 64.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan (2, 4, ...) dan menerapkan pola tersebut untuk menghitung nilai pada fase ke-6. Ini adalah penerapan konsep eksponen dalam konteks rutin.. Bukti: Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.; Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip pertumbuhan eksponensial (konsep) dan penggunaan aturan perpangkatan (prosedural) untuk memodelkan situasi nyata.. Bukti: Pola penyebaran hoaks berlipat dua tiap fase sehingga mengikuti 2^fase
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena pola pertumbuhan (2^n) sangat jelas dari data awal yang diberikan. Siswa hanya perlu mengenali pola bilangan berpangkat sederhana dan menghitung nilai 2^6. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Lengkapilah tabel di bawah ini; hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen (perpangkatan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, mengenali pola pertumbuhan eksponensial sederhana seperti 2^n adalah materi dasar yang familiar dan rutin. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Definisi Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Dengan asumsi setiap orang yang menerima pesan ini tidak mengetahui bahwa ini adalah hoaks, bayangkan betapa cepat hoaks ini akan tersebar. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.

|Fase penyebaran|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|Banyak orang yang menerima hoaks|2|4|…|….|….|….|….|….|

Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?
Pilihan: A. 128 orang
B. 64 orang
C. 12 orang
D. 32 orang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `d16acca83decc68e658d11d5`

Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.<br><br>$(3\pi)^p = 27\pi^3$

| Opsi | Isi |
|---|---|
| A | $p = 27$ |
| B | $p = 3$ |
| C | $p = 1$ |
| D | $p = 9$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: (3\pi)^p = 27\pi^3 \implies (3\pi)^p = 3^3 \cdot \pi^3 \implies (3\pi)^p = (3\pi)^3 \implies p = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ada381f85814e356c55d8bebce65e8319619b31a0c3c5b8c6545d81361e6f93a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3318 |
| 2 | success | valid / verified | applying | procedural | Easy | 3448 |
| 3 | success | valid / verified | applying | procedural | Easy | 3487 |

Run 1 — solusi: (3\pi)^p = 27\pi^3 \implies (3\pi)^p = 3^3 \cdot \pi^3 \implies (3\pi)^p = (3\pi)^3 \implies p = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat eksponen (ab)^n = a^n b^n untuk menyamakan basis ruas kanan dengan ruas kiri agar nilai p dapat ditentukan.. Bukti: (3\pi)^p = 27\pi^3; 27\pi^3 = 3^3 \cdot \pi^3 = (3\pi)^3
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan prosedur manipulasi aljabar menggunakan sifat-sifat eksponen untuk menyelesaikan persamaan.. Bukti: (3\pi)^p = 27\pi^3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Langkah penyelesaiannya langsung, yaitu mengubah bentuk 27\pi^3 menjadi (3\pi)^3 menggunakan sifat eksponen dasar. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: (3\pi)^p = 27\pi^3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dasar (ab)^n = a^n b^n. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar sifat eksponen yang sesuai dengan kurikulum kelas 10, tidak memerlukan langkah kompleks atau integrasi konsep yang sulit. |

Run 2 — solusi: (3π)^p = 27π^3. Karena 27 = 3^3, maka 27π^3 = 3^3 · π^3 = (3π)^3. Persamaan menjadi (3π)^p = (3π)^3, sehingga p = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat eksponen (a · b)^n = a^n · b^n untuk menyamakan basis ruas kiri dan kanan. Ini adalah penerapan prosedur familiar pada konteks rutin.. Bukti: (3π)^p = 27π^3; 27π^3 = 3^3 · π^3 = (3π)^3
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode penyelesaian persamaan eksponen dengan menyamakan basis.. Bukti: (3π)^p = 27π^3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengenali bahwa 27 adalah 3^3 dan menerapkan sifat eksponen dasar untuk menyamakan basis. Tidak ada kendala kompleks atau langkah yang saling bergantung secara rumit.. Bukti: (3π)^p = 27π^3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dasar (a^n · b^n = (ab)^n) |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 sudah familiar dengan sifat eksponen. Soal ini adalah latihan langsung tanpa jebakan atau integrasi konsep yang berat. |

Run 3 — solusi: Persamaan (3π)^p = 27π^3 dapat ditulis ulang sebagai (3π)^p = 3^3 · π^3. Karena 3^3 · π^3 = (3π)^3, maka (3π)^p = (3π)^3. Dengan menyamakan eksponen, diperoleh p = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat eksponen (a · b)^n = a^n · b^n untuk menyamakan basis ruas kanan dengan ruas kiri. Ini adalah penerapan prosedur familiar pada konteks yang sedikit dimodifikasi.. Bukti: (3π)^p = 27π^3; 27π^3 = 3^3 · π^3 = (3π)^3
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penggunaan algoritma sifat-sifat eksponen untuk menyelesaikan persamaan.. Bukti: (3π)^p = 27π^3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Langkah penyelesaiannya langsung: mengubah bentuk 27 menjadi 3^3 untuk menyamakan basis. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: (3π)^p = 27π^3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dasar (ab)^n = a^n b^n dan a^m · a^n = a^{m+n}. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah materi dasar kelas 10. Soal ini hanya memerlukan satu langkah manipulasi aljabar sederhana untuk menyamakan basis. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sifat-Sifat Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.

$(3\pi)^p = 27\pi^3$
Pilihan: A. $p = 27$
B. $p = 3$
C. $p = 1$
D. $p = 9$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `972c064ee62227036f9b40cd`

Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.<br><br>$(3^4)^2 = 3^p$

| Opsi | Isi |
|---|---|
| A | $p = 2$ |
| B | $p = 6$ |
| C | $p = 8$ |
| D | $p = 16$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menggunakan sifat eksponen (a^m)^n = a^(m*n), maka (3^4)^2 = 3^(4*2) = 3^8. Jadi, p = 8.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `58254e11c8199f973f4290c35c60706f693f8e5303faf10a578f5b170d3a1514`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2599 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2586 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2577 |

Run 1 — solusi: Menggunakan sifat eksponen (a^m)^n = a^(m*n), maka (3^4)^2 = 3^(4*2) = 3^8. Jadi, p = 8.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan sifat eksponen (a^m)^n = a^(m*n) secara langsung tanpa modifikasi atau integrasi konsep lain.. Bukti: (3^4)^2 = 3^p
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami aturan atau prosedur dasar dalam operasi eksponen (sifat pemangkatan bilangan berpangkat).. Bukti: (3^4)^2 = 3^p
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari satu sifat eksponen dasar. Tidak ada langkah tambahan, kendala yang berinteraksi, atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: (3^4)^2 = 3^p

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sifat eksponen (a^m)^n = a^(m*n). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah dasar kelas 10. Soal ini menguji pemahaman prosedural dasar tanpa kerumitan tambahan, sehingga dikategorikan mudah. |

Run 2 — solusi: Menggunakan sifat eksponen (a^m)^n = a^(m*n), maka (3^4)^2 = 3^(4*2) = 3^8. Jadi, p = 8.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan sifat eksponen (a^m)^n = a^(m*n) secara langsung. Tidak ada langkah kompleks atau strategi nonrutin yang diperlukan.. Bukti: (3^4)^2 = 3^p
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami aturan atau prinsip dasar eksponen (sifat pemangkatan bilangan berpangkat) untuk menyelesaikan persamaan ini.. Bukti: (3^4)^2 = 3^p
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari satu sifat eksponen dasar. Tidak ada langkah yang saling bergantung atau kendala yang berinteraksi. Siswa hanya perlu melakukan satu operasi perkalian sederhana pada eksponen.. Bukti: (3^4)^2 = 3^p

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sifat eksponen (a^m)^n = a^(m*n). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah dasar kelas 10. Soal ini menguji pemahaman langsung tanpa modifikasi atau integrasi konsep lain, sehingga sangat mudah bagi siswa kelas 10. |

Run 3 — solusi: Menggunakan sifat eksponen (a^m)^n = a^(m*n), maka (3^4)^2 = 3^(4*2) = 3^8. Jadi, p = 8.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan sifat eksponen dasar (pangkat dipangkatkan) secara langsung tanpa modifikasi atau integrasi konsep lain.. Bukti: (3^4)^2 = 3^p
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami aturan atau prosedur algoritme eksponen (a^m)^n = a^(m*n) untuk menyelesaikan persamaan.. Bukti: (3^4)^2 = 3^p
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan satu sifat eksponen dasar. Tidak ada langkah yang saling bergantung atau kendala yang berinteraksi.. Bukti: (3^4)^2 = 3^p

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sifat eksponen (pangkat dipangkatkan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah dasar kelas 10. Soal ini menguji pemahaman langsung terhadap satu sifat eksponen tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3926`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan sifat eksponen (a^m)^n = a^(m*n) secara langsung tanpa modifikasi atau integrasi konsep lain.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami aturan atau prosedur dasar dalam operasi eksponen (sifat pemangkatan bilangan berpangkat).
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung dari satu sifat eksponen dasar. Tidak ada langkah tambahan, kendala yang berinteraksi, atau kebutuhan untuk memilih strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sifat eksponen (a^m)^n = a^(m*n). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah dasar kelas 10. Soal ini menguji pemahaman prosedural dasar tanpa kerumitan tambahan, sehingga dikategorikan mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sifat-Sifat Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.

$(3^4)^2 = 3^p$
Pilihan: A. $p = 2$
B. $p = 6$
C. $p = 8$
D. $p = 16$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `d84e49739900804aa0aa6417`

Pada tahun 2015 kasus positif HIV-AIDS berjumlah sekitar 36 juta jiwa. Jumlah ini meningkat rata-rata 2% setiap tahun dari tahun 2010 hingga 2015. Jika peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun, berapa banyak kasus yang terjadi pada tahun 2020?

| Opsi | Isi |
|---|---|
| A | ≈39.746.909 jiwa |
| B | 38.203.488 jiwa |
| C | 39.600.000 jiwa |
| D | 40.541.832 jiwa |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Model pertumbuhan eksponensial: f(t) = P0(1 + r)^t. Diketahui P0 = 36.000.000, r = 0,02, dan t = 2020 - 2015 = 5. Maka, f(5) = 36.000.000 * (1,02)^5 = 36.000.000 * 1,1040808032 = 39.746.908,9152. Dibulatkan menjadi 39.746.909 jiwa.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `17eae62e40d4f4b2181a9b3dd1fa3a695bf958d48dc913d101d1e4db74c84b07`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2941 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2896 |
| 3 | success | valid / verified | applying | procedural | Medium | 2879 |

Run 1 — solusi: Model pertumbuhan eksponensial adalah f(t) = P0 * (1 + r)^t. Dengan P0 = 36.000.000, r = 0,02, dan t = 2020 - 2015 = 5, maka f(5) = 36.000.000 * (1,02)^5 = 36.000.000 * 1,1040808032 = 39.746.908,9152. Dibulatkan menjadi sekitar 39.746.909 jiwa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model pertumbuhan eksponensial yang sesuai dengan konteks soal, menentukan parameter (nilai awal, laju pertumbuhan, dan selisih waktu), serta menerapkan rumus tersebut untuk menghitung nilai akhir. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun; berapa banyak kasus yang terjadi pada tahun 2020?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip pertumbuhan eksponensial dan penggunaan rumus f(t) = P0(1+r)^t sebagai metode penyelesaian.. Bukti: bertambah secara eksponen pada peningkatan 2% setiap tahun
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus menentukan selisih waktu (t=5) dan menerapkan model eksponensial. Meskipun prosedurnya rutin, terdapat kebutuhan untuk menerjemahkan konteks tahun ke dalam variabel waktu yang tepat dan melakukan perhitungan eksponensial, yang merupakan langkah-langkah yang saling terkait.. Bukti: 36 juta jiwa; meningkat rata-rata 2% setiap tahun; tahun 2015... tahun 2020

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan konsep persentase pertumbuhan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu memodelkan pertumbuhan eksponensial sederhana. Soal ini memerlukan ketelitian dalam menentukan durasi waktu (5 tahun) dan menerapkan rumus, yang sesuai dengan tingkat kemampuan kelas 10. |

Run 2 — solusi: Model pertumbuhan eksponensial adalah f(x) = P(1 + r)^x. Diketahui P = 36.000.000, r = 0,02, dan x = 2020 - 2015 = 5. Maka, f(5) = 36.000.000 * (1,02)^5 = 36.000.000 * 1,1040808 = 39.746.908,8. Dibulatkan menjadi sekitar 39.746.909 jiwa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model pertumbuhan eksponensial yang sesuai, menentukan parameter (nilai awal, laju pertumbuhan, dan selisih waktu), serta menerapkan rumus tersebut untuk menghitung nilai akhir. Ini adalah penerapan prosedur rutin pada konteks yang diberikan.. Bukti: peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun; berapa banyak kasus yang terjadi pada tahun 2020?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai konsep fungsi eksponensial dan bagaimana menerapkannya dalam konteks pertumbuhan populasi.. Bukti: bertambah secara eksponen pada peningkatan 2% setiap tahun
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus menentukan selisih waktu (x=5) dan menerapkan rumus pertumbuhan eksponensial yang umum dipelajari di kelas 10. Tidak ada kendala yang saling berinteraksi secara kompleks, namun memerlukan ketelitian dalam menentukan variabel waktu dan melakukan perhitungan eksponensial.. Bukti: 36 juta jiwa; meningkat rata-rata 2% setiap tahun; tahun 2020

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi perpangkatan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 10 mengenai fungsi eksponensial. Langkah-langkahnya jelas dan prosedural. |

Run 3 — solusi: Model pertumbuhan eksponensial adalah f(t) = P(1+r)^t. Diketahui P = 36.000.000, r = 0,02, dan t = 2020 - 2015 = 5. Maka, f(5) = 36.000.000 * (1,02)^5 = 36.000.000 * 1,1040808 = 39.746.908,8. Dibulatkan menjadi ≈39.746.909.
- Domain kognitif `classify/applying`: Siswa perlu memilih model matematika yang tepat (pertumbuhan eksponensial) dan menerapkan prosedur perhitungan yang sesuai untuk konteks pertumbuhan tahunan. Ini adalah penerapan konsep pada situasi rutin.. Bukti: peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun; berapa banyak kasus yang terjadi pada tahun 2020?
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang prinsip pertumbuhan eksponensial dan kemampuan menggunakan rumus pertumbuhan eksponensial (prosedur) untuk menyelesaikan masalah.. Bukti: bertambah secara eksponen pada peningkatan 2% setiap tahun
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus mengidentifikasi parameter (P, r, t) dari narasi, menentukan model yang tepat, dan melakukan perhitungan eksponensial. Meskipun prosedurnya familiar, terdapat kebutuhan untuk menentukan selisih tahun (t=5) dengan benar dan menghindari jebakan model linear.. Bukti: 36 juta jiwa; meningkat rata-rata 2% setiap tahun; tahun 2015... tahun 2020

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi perpangkatan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10, menuntut ketelitian dalam menentukan durasi waktu dan pemilihan model pertumbuhan yang tepat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4855`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi model pertumbuhan eksponensial yang sesuai dengan konteks soal, menentukan parameter (nilai awal, laju pertumbuhan, dan selisih waktu), serta menerapkan rumus tersebut untuk menghitung nilai akhir. Ini adalah penerapan prosedur pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal menuntut pemahaman tentang prinsip pertumbuhan eksponensial dan penggunaan rumus f(t) = P0(1+r)^t sebagai metode penyelesaian.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena siswa harus menentukan selisih waktu (t=5) dan menerapkan model eksponensial. Meskipun prosedurnya rutin, terdapat kebutuhan untuk menerjemahkan konteks tahun ke dalam variabel waktu yang tepat dan melakukan perhitungan eksponensial, yang merupakan langkah-langkah yang saling terkait.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan konsep persentase pertumbuhan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu memodelkan pertumbuhan eksponensial sederhana. Soal ini memerlukan ketelitian dalam menentukan durasi waktu (5 tahun) dan menerapkan rumus, yang sesuai dengan tingkat kemampuan kelas 10. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Eksponensial
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada tahun 2015 kasus positif HIV-AIDS berjumlah sekitar 36 juta jiwa. Jumlah ini meningkat rata-rata 2% setiap tahun dari tahun 2010 hingga 2015. Jika peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun, berapa banyak kasus yang terjadi pada tahun 2020?
Pilihan: A. ≈39.746.909 jiwa
B. 38.203.488 jiwa
C. 39.600.000 jiwa
D. 40.541.832 jiwa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `6bd03dd3f29670f8050110d7`

Massa suatu zat radioaktif adalah 0,3 kg pada pukul 10 pagi. Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam. Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?

| Opsi | Isi |
|---|---|
| A | 0,21828 kg (218,28 gram) |
| B | 0,2724 kg (272,4 gram) |
| C | 0,255 kg (255 gram) |
| D | ≈0,08172 kg (81,72 gram) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Massa awal M0 = 0,3 kg. Laju peluruhan r = 15% = 0,15. Faktor sisa = 1 - 0,15 = 0,85. Fungsi massa tersisa f(t) = 0,3 * (0,85)^t. Untuk t = 8 jam, f(8) = 0,3 * (0,85)^8 ≈ 0,3 * 0,27249 = 0,081747 kg. Pembulatan yang sesuai dengan opsi D adalah 0,08172 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fd8808828d0266e4fd41c09ad549d882b8c28212aaf1697f72fe66a1f49f6c8d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2897 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2873 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3677 |

Run 1 — solusi: Massa awal M0 = 0,3 kg. Laju peluruhan r = 15% = 0,15. Faktor sisa = 1 - 0,15 = 0,85. Fungsi massa tersisa f(t) = 0,3 * (0,85)^t. Untuk t = 8 jam, f(8) = 0,3 * (0,85)^8 ≈ 0,3 * 0,27249 = 0,081747 kg. Pembulatan yang sesuai dengan opsi D adalah 0,08172 kg.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model peluruhan eksponensial dari narasi, menentukan parameter (massa awal, laju peluruhan, waktu), dan menerapkan rumus f(t) = M0(1-r)^t. Ini adalah penerapan prosedur rutin pada konteks yang familiar.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam.; Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip peluruhan eksponensial dan penggunaan rumus fungsi eksponensial untuk memodelkan situasi nyata.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu menerapkan rumus peluruhan eksponensial standar yang sudah dipelajari di kelas 10. Jalur penyelesaiannya linear, tidak ada kendala yang berinteraksi, dan variabel sudah tersedia secara eksplisit.. Bukti: Massa suatu zat radioaktif adalah 0,3 kg pada pukul 10 pagi.; Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam.; Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep fungsi eksponensial dan operasi bilangan berpangkat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 sudah terbiasa dengan model pertumbuhan dan peluruhan eksponensial sederhana. Soal ini tidak memerlukan modifikasi model atau penalaran tingkat lanjut. |

Run 2 — solusi: Model peluruhan eksponensial: f(x) = M0 * (1 - r)^x. Diketahui M0 = 0,3 kg, r = 0,15, dan x = 8 jam. Maka f(8) = 0,3 * (1 - 0,15)^8 = 0,3 * (0,85)^8. Hasil perhitungan: 0,3 * 0,27249 = 0,081747 kg, yang mendekati 0,08172 kg.
- Domain kognitif `classify/applying`: Siswa perlu memilih model fungsi eksponensial yang tepat untuk peluruhan (f(x) = M0(1-r)^x) dan menerapkan prosedur perhitungan untuk menentukan nilai fungsi pada x=8. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam.; Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip peluruhan eksponensial dan penggunaan rumus fungsi eksponensial sebagai metode penyelesaian.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengidentifikasi parameter (M0, r, x) dan memasukkannya ke dalam rumus peluruhan eksponensial yang sudah umum dipelajari di kelas 10. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Massa suatu zat radioaktif adalah 0,3 kg pada pukul 10 pagi.; Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam.; Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan konsep persentase peluruhan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 SMA sudah mempelajari fungsi eksponensial dan peluruhan sebagai materi standar. Soal ini bersifat langsung tanpa jebakan konseptual yang rumit. |

Run 3 — solusi: Model peluruhan eksponensial adalah f(t) = M0(1-r)^t. Dengan M0 = 0,3 kg, r = 0,15, dan t = 8, maka f(8) = 0,3(0,85)^8 ≈ 0,08172 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan model fungsi eksponensial untuk peluruhan pada konteks soal cerita yang rutin. Prosedur ini merupakan penerapan langsung dari konsep yang dipelajari.. Bukti: Massa suatu zat radioaktif adalah 0,3 kg; Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; jumlah zat radioaktif tersebut 8 jam kemudian
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep peluruhan eksponensial sebagai hubungan antara massa awal, laju peluruhan, dan waktu untuk menyusun model matematika yang tepat.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus peluruhan eksponensial. Siswa hanya perlu mengidentifikasi variabel yang diberikan dan melakukan perhitungan rutin. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merancang strategi non-rutin.. Bukti: Massa suatu zat radioaktif adalah 0,3 kg; Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; jumlah zat radioaktif tersebut 8 jam kemudian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep fungsi eksponensial dasar dan operasi persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini menguji pemahaman dasar fungsi eksponensial yang merupakan materi standar kelas 10. Tingkat kesulitan rendah karena alur penyelesaian sangat jelas dan tidak memerlukan integrasi konsep yang kompleks. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Eksponensial
Tipe soal: multiple_choice
Stimulus: -
Soal: Massa suatu zat radioaktif adalah 0,3 kg pada pukul 10 pagi. Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam. Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?
Pilihan: A. 0,21828 kg (218,28 gram)
B. 0,2724 kg (272,4 gram)
C. 0,255 kg (255 gram)
D. ≈0,08172 kg (81,72 gram)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `842ca4bb6c6ebd4208641b61`

Sederhanakan bentuk akar berikut ini.<br><br>$(5\sqrt{x^5})(3\sqrt[3]{x})$

| Opsi | Isi |
|---|---|
| A | $8x^{\frac{17}{6}}$ |
| B | $15x^{\frac{17}{6}}$ |
| C | $15x^{\frac{13}{6}}$ |
| D | $15x^{\frac{6}{17}}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Ubah bentuk akar ke eksponen pecahan: (5x^(5/2))(3x^(1/3)). Kalikan koefisien: 5 * 3 = 15. Jumlahkan eksponen: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2bccf9cfa4fd67622636578a48f111a290d25f99af03a4bf0d0b577e61b93e7c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2691 |
| 2 | success | valid / verified | applying | procedural | Easy | 2665 |
| 3 | success | valid / verified | applying | procedural | Easy | 2721 |

Run 1 — solusi: Ubah bentuk akar ke eksponen pecahan: (5x^(5/2))(3x^(1/3)). Kalikan koefisien: 5 * 3 = 15. Jumlahkan eksponen: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur rutin mengubah bentuk akar menjadi eksponen pecahan, mengalikan koefisien, dan menjumlahkan pecahan eksponen dengan penyebut berbeda. Ini adalah penerapan langsung dari aturan eksponen.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang aturan operasi aljabar pada eksponen dan bentuk akar (prosedural) serta hubungan antara bentuk akar dan eksponen pecahan (konseptual).. Bukti: (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Langkah-langkahnya jelas: konversi ke eksponen, operasi koefisien, dan penjumlahan pecahan. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan eksponen dasar dan penjumlahan pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan dasar aljabar kelas 10. Prosedur konversi dan operasi eksponen adalah standar dan familiar. |

Run 2 — solusi: Ubah bentuk akar ke eksponen pecahan: (5x^(5/2))(3x^(1/3)). Kalikan koefisien: 5 * 3 = 15. Jumlahkan pangkat: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur rutin mengubah bentuk akar menjadi eksponen pecahan dan menggunakan hukum eksponen (perkalian basis sama dengan menjumlahkan pangkat). Tidak ada strategi nonrutin yang diperlukan.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang aturan eksponen dan prosedur mengubah bentuk akar ke bentuk pangkat pecahan, yang merupakan pengetahuan prosedural.. Bukti: Sederhanakan bentuk akar berikut ini.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Langkah-langkahnya jelas: mengubah akar ke pecahan, mengalikan koefisien, dan menjumlahkan pecahan pangkat. Tidak ada kendala yang berinteraksi atau kebutuhan untuk membangun model yang kompleks.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar eksponen pecahan dan operasi pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen dan bentuk akar adalah kurikulum standar kelas 10. Prosedur yang diminta sangat langsung dan familiar. |

Run 3 — solusi: Ubah bentuk akar menjadi pangkat pecahan: 5x^(5/2) * 3x^(1/3). Kalikan koefisien: 5 * 3 = 15. Jumlahkan pangkat dengan menyamakan penyebut: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur rutin mengubah bentuk akar ke pangkat pecahan dan menggunakan sifat eksponen (perkalian bilangan berpangkat) untuk menyederhanakan ekspresi. Ini adalah penerapan langsung dari aturan eksponen.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme dan teknik manipulasi aljabar (eksponen dan bentuk akar) yang merupakan prosedur standar dalam kurikulum kelas 10.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah penyelesaian yang jelas (mengubah bentuk akar ke pecahan, mengalikan koefisien, menjumlahkan pangkat). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dan hubungan bentuk akar dengan pangkat pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah dasar aljabar kelas 10. Prosedur penyelesaian sangat standar dan familiar bagi siswa. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bentuk Akar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sederhanakan bentuk akar berikut ini.

$(5\sqrt{x^5})(3\sqrt[3]{x})$
Pilihan: A. $8x^{\frac{17}{6}}$
B. $15x^{\frac{17}{6}}$
C. $15x^{\frac{13}{6}}$
D. $15x^{\frac{6}{17}}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `7f717b29ae76a834f5c1363a`

Rasionalkan bentuk berikut ini.<br><br>$\dfrac{2}{\sqrt3+\sqrt5}$

| Opsi | Isi |
|---|---|
| A | $-1$ |
| B | $\sqrt5-\sqrt3$ |
| C | $\sqrt3-\sqrt5$ |
| D | $2(\sqrt3-\sqrt5)$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 2/(sqrt(3)+sqrt(5)) * (sqrt(3)-sqrt(5))/(sqrt(3)-sqrt(5)) = 2(sqrt(3)-sqrt(5))/(3-5) = 2(sqrt(3)-sqrt(5))/(-2) = -(sqrt(3)-sqrt(5)) = sqrt(5)-sqrt(3)
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fc1dbb27d73a1fc864ad499d4fed300f60b1eeadee275d2675440bee4343e7d8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3128 |
| 2 | success | valid / verified | applying | procedural | Easy | 3381 |
| 3 | success | valid / verified | applying | procedural | Easy | 3286 |

Run 1 — solusi: 2/(sqrt(3)+sqrt(5)) * (sqrt(3)-sqrt(5))/(sqrt(3)-sqrt(5)) = 2(sqrt(3)-sqrt(5))/(3-5) = 2(sqrt(3)-sqrt(5))/(-2) = -(sqrt(3)-sqrt(5)) = sqrt(5)-sqrt(3)
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar merasionalkan penyebut pecahan yang melibatkan bentuk akar. Ini adalah penerapan langsung dari algoritma perkalian dengan sekawan.. Bukti: Rasionalkan bentuk berikut ini.; 2/(sqrt(3)+sqrt(5))
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan prosedur atau algoritma matematika untuk merasionalkan penyebut.. Bukti: Rasionalkan bentuk berikut ini.
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin yang sangat standar dalam kurikulum kelas 10. Prosedur merasionalkan penyebut dengan mengalikan sekawan adalah materi dasar yang familiar. Tidak ada kendala kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Rasionalkan bentuk berikut ini.; 2/(sqrt(3)+sqrt(5))

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk akar dan operasi aljabar sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Merasionalkan penyebut adalah kompetensi dasar yang diajarkan secara eksplisit di kelas 10, sehingga soal ini dikategorikan mudah karena mengikuti pola rutin. |

Run 2 — solusi: 2/(sqrt(3)+sqrt(5)) * (sqrt(3)-sqrt(5))/(sqrt(3)-sqrt(5)) = 2(sqrt(3)-sqrt(5))/(3-5) = 2(sqrt(3)-sqrt(5))/(-2) = -(sqrt(3)-sqrt(5)) = sqrt(5)-sqrt(3).
- Domain kognitif `classify/applying`: Siswa perlu memilih dan menerapkan prosedur merasionalkan penyebut menggunakan sekawan, yang merupakan penerapan langsung dari konsep aljabar bentuk akar.. Bukti: Rasionalkan bentuk berikut ini.; 2/(sqrt3+sqrt5)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma atau metode standar untuk merasionalkan penyebut pecahan yang mengandung bentuk akar.. Bukti: Rasionalkan bentuk berikut ini.
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin yang standar untuk kelas 10. Langkah-langkah penyelesaiannya jelas, yaitu mengalikan dengan sekawan dan menyederhanakan, tanpa memerlukan perencanaan strategi yang kompleks.. Bukti: Rasionalkan bentuk berikut ini.; 2/(sqrt3+sqrt5)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar, sifat-sifat bentuk akar, dan perkalian sekawan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Merasionalkan penyebut adalah keterampilan dasar dalam kurikulum kelas 10. Soal ini tidak memiliki kendala yang berinteraksi atau tuntutan integrasi yang tinggi. |

Run 3 — solusi: 2/(sqrt(3)+sqrt(5)) * (sqrt(3)-sqrt(5))/(sqrt(3)-sqrt(5)) = 2(sqrt(3)-sqrt(5))/(3-5) = 2(sqrt(3)-sqrt(5))/(-2) = -(sqrt(3)-sqrt(5)) = sqrt(5)-sqrt(3)
- Domain kognitif `classify/applying`: Siswa perlu mengenali prosedur merasionalkan penyebut dengan mengalikan bentuk sekawan, yang merupakan penerapan langsung dari konsep aljabar bentuk akar.. Bukti: Rasionalkan bentuk berikut ini.; 2/(sqrt3+sqrt5)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma atau teknik standar dalam menyederhanakan bentuk akar.. Bukti: Rasionalkan bentuk berikut ini.
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang familiar bagi siswa kelas 10. Langkah-langkah penyelesaiannya jelas dan langsung, tidak memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Rasionalkan bentuk berikut ini.; 2/(sqrt3+sqrt5)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang bentuk akar dan perkalian sekawan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Merasionalkan penyebut adalah materi dasar kelas 10 yang bersifat prosedural dan rutin. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bentuk Akar
Tipe soal: multiple_choice
Stimulus: -
Soal: Rasionalkan bentuk berikut ini.

$\dfrac{2}{\sqrt3+\sqrt5}$
Pilihan: A. $-1$
B. $\sqrt5-\sqrt3$
C. $\sqrt3-\sqrt5$
D. $2(\sqrt3-\sqrt5)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `e97f2eaa7ee74e27d6bb517c`

Buat bilangan berikut dalam bentuk baku. 34.000.000.000

| Opsi | Isi |
|---|---|
| A | 3,4 × 10<sup>10</sup> |
| B | 3,4 × 10<sup>11</sup> |
| C | 3,4 × 10<sup>-10</sup> |
| D | 3,4 × 10<sup>9</sup> |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 34.000.000.000 = 3,4 x 10.000.000.000 = 3,4 x 10^10
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `83a6d9e8c1b4008503bfe9e0253e570060139183e0c7cfa29bb8469b0a1de593`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3519 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2715 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2725 |

Run 1 — solusi: 34.000.000.000 = 3,4 x 10.000.000.000 = 3,4 x 10^10
- Domain kognitif `classify/knowing`: Soal meminta konversi langsung bilangan desimal ke bentuk baku sesuai definisi a x 10^n, yang merupakan pengenalan fakta dan prosedur dasar.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur standar penulisan notasi ilmiah untuk mengubah representasi bilangan.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal merupakan tugas rutin yang langsung menguji pemahaman definisi bentuk baku tanpa memerlukan perencanaan strategi atau integrasi konsep yang kompleks.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan perpangkatan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bentuk baku adalah materi dasar yang familiar bagi siswa kelas 10, penyelesaiannya bersifat langsung. |

Run 2 — solusi: Bilangan 34.000.000.000 memiliki 11 digit. Untuk mengubah ke bentuk baku a x 10^n (dengan 1 <= a < 10), kita geser koma desimal ke kiri sebanyak 10 kali hingga menjadi 3,4. Maka, 34.000.000.000 = 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi bentuk baku (notasi ilmiah) secara langsung pada bilangan yang diberikan tanpa memerlukan strategi kompleks atau integrasi konsep.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang aturan penulisan notasi ilmiah (bentuk baku) sebagai prosedur standar.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah konversi langsung tanpa kendala yang berinteraksi atau perencanaan strategi.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat dan notasi eksponen. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bentuk baku adalah materi dasar yang sudah diperkenalkan di jenjang SMP dan merupakan prasyarat untuk kelas 10, sehingga soal ini tergolong sangat mudah bagi siswa kelas 10. |

Run 3 — solusi: Bilangan 34.000.000.000 memiliki 11 digit. Untuk mengubah ke bentuk baku a x 10^n (1 <= a < 10), kita geser koma desimal ke kiri sebanyak 10 kali hingga menjadi 3,4. Maka, 34.000.000.000 = 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan prosedur standar penulisan notasi ilmiah (bentuk baku) dengan menggeser koma desimal dan menghitung jumlah pergeseran sebagai eksponen basis 10.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur penulisan bilangan dalam bentuk baku (notasi ilmiah).. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah utama (menentukan posisi koma dan menghitung pangkat). Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat dan notasi ilmiah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bentuk baku adalah materi dasar yang sudah diajarkan di jenjang SMP dan merupakan prasyarat untuk kelas 10. Soal ini sangat rutin. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Penulisan Bentuk Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
Pilihan: A. 3,4 × 10<sup>10</sup>
B. 3,4 × 10<sup>11</sup>
C. 3,4 × 10<sup>-10</sup>
D. 3,4 × 10<sup>9</sup>
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `1704f944a606f647f17a0cc0`

Ivan membagikan permen kepada teman-temannya dengan cara tertentu. Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen. Dia melanjutkan pola ini hingga sepuluh temannya mendapat permen. Berapa permen yang didapat oleh teman kesepuluh?

| Opsi | Isi |
|---|---|
| A | 120 |
| B | 21 |
| C | 19 |
| D | 23 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Barisan aritmetika dengan suku pertama a=3 dan beda b=2. Rumus suku ke-n adalah Un = a + (n-1)b. Untuk n=10, U10 = 3 + (10-1)2 = 3 + 18 = 21.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `85585db028094b71fd4df07dbfb2bea1638f85f2c726523ce93cd049515409d6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2730 |
| 2 | success | valid / verified | applying | procedural | Easy | 2726 |
| 3 | success | valid / verified | applying | procedural | Easy | 2725 |

Run 1 — solusi: Barisan aritmetika dengan suku pertama a=3 dan beda b=2. Rumus suku ke-n adalah Un = a + (n-1)b. Untuk n=10, U10 = 3 + (10-1)2 = 3 + 18 = 21.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola bilangan sebagai barisan aritmetika dan menerapkan rumus suku ke-n secara langsung untuk menentukan nilai pada suku tertentu.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur standar barisan aritmetika untuk menyelesaikan masalah.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas. Siswa hanya perlu mengidentifikasi parameter barisan aritmetika (a=3, b=2) dan menerapkan rumus Un. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan barisan aritmetika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung rumus barisan aritmetika yang merupakan materi dasar kelas 10, tanpa kompleksitas tambahan. |

Run 2 — solusi: Barisan aritmetika dengan suku pertama a=3 dan beda b=2. Rumus suku ke-n adalah Un = a + (n-1)b. Untuk n=10, U10 = 3 + (10-1)2 = 3 + 18 = 21.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola barisan aritmetika dari data yang diberikan dan menerapkan rumus suku ke-n secara langsung untuk menentukan nilai pada posisi tertentu.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur standar barisan aritmetika untuk menyelesaikan masalah yang diberikan.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mengidentifikasi parameter barisan aritmetika dan menerapkan rumus suku ke-n. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang barisan aritmetika dan rumus suku ke-n. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep barisan aritmetika yang merupakan materi standar kelas 10. Tingkat kesulitan rendah karena siswa hanya perlu mengenali pola dan menghitung satu nilai. |

Run 3 — solusi: Barisan aritmetika dengan suku pertama a=3 dan beda b=2. Rumus suku ke-n adalah Un = a + (n-1)b. Untuk n=10, U10 = 3 + (10-1)2 = 3 + 18 = 21.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola bilangan sebagai barisan aritmetika dan menerapkan rumus suku ke-n untuk menentukan nilai pada posisi tertentu. Ini adalah penerapan prosedur standar.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritme barisan aritmetika (Un = a + (n-1)b) untuk menyelesaikan masalah.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi parameter barisan (a=3, b=2) dan menerapkan rumus suku ke-n. Tidak ada kendala kompleks atau integrasi konsep yang menantang.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar barisan aritmetika dan rumus suku ke-n. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar untuk kelas 10 mengenai barisan aritmetika. Prosedur penyelesaian sangat langsung dan familiar bagi siswa. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ivan membagikan permen kepada teman-temannya dengan cara tertentu. Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen. Dia melanjutkan pola ini hingga sepuluh temannya mendapat permen. Berapa permen yang didapat oleh teman kesepuluh?
Pilihan: A. 120
B. 21
C. 19
D. 23
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `b9a85ae0df70ee2053be254e`

Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …

| Opsi | Isi |
|---|---|
| A | -338 |
| B | 348 |
| C | -345 |
| D | -331 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Barisan aritmetika dengan suku pertama a = 5 dan beda b = -2 - 5 = -7. Rumus suku ke-n adalah Un = a + (n-1)b. Maka U50 = 5 + (50-1)(-7) = 5 + 49(-7) = 5 - 343 = -338.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bc0c07ff0c75b93ac053643e3f35535a1375de8ddb3c85c7bd502706e95950bc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2638 |
| 2 | success | valid / verified | applying | procedural | Easy | 2649 |
| 3 | success | valid / verified | applying | procedural | Easy | 2669 |

Run 1 — solusi: Barisan aritmetika dengan a = 5 dan b = -2 - 5 = -7. Suku ke-50 adalah U50 = a + (50-1)b = 5 + 49(-7) = 5 - 343 = -338.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi suku pertama dan beda, kemudian menerapkan rumus suku ke-n barisan aritmetika secara langsung.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus barisan aritmetika.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu menentukan beda dan memasukkannya ke rumus standar.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar barisan aritmetika dan operasi bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi barisan aritmetika adalah standar kelas 10. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep, sehingga tergolong mudah. |

Run 2 — solusi: Barisan aritmetika dengan a = 5 dan b = -7. Rumus suku ke-n adalah Un = a + (n-1)b. Maka U50 = 5 + (50-1)(-7) = 5 + 49(-7) = 5 - 343 = -338.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus suku ke-n barisan aritmetika secara langsung. Prosedur ini sangat rutin dan familiar bagi siswa kelas 10.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode standar untuk menentukan suku ke-n pada barisan aritmetika.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas. Siswa hanya perlu mengidentifikasi suku pertama dan beda, lalu memasukkannya ke rumus umum.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar barisan aritmetika dan rumus suku ke-n. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah aplikasi langsung dari rumus barisan aritmetika yang merupakan materi standar kelas 10, tanpa memerlukan modifikasi strategi atau integrasi konsep yang kompleks. |

Run 3 — solusi: Barisan aritmetika dengan suku pertama a = 5 dan beda b = -2 - 5 = -7. Suku ke-n dirumuskan Un = a + (n-1)b. Maka U50 = 5 + (50-1)(-7) = 5 + 49(-7) = 5 - 343 = -338.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus suku ke-n barisan aritmetika yang merupakan prosedur rutin dan familiar bagi siswa kelas 10.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode standar untuk mencari suku ke-n pada barisan aritmetika.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mengidentifikasi suku pertama dan beda, lalu memasukkannya ke rumus umum.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang barisan aritmetika dan rumus suku ke-n. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari suku ke-n barisan aritmetika adalah materi dasar kelas 10 yang bersifat prosedural langsung tanpa memerlukan penalaran kompleks atau integrasi konsep. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4196`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung rumus suku ke-n barisan aritmetika. Siswa hanya perlu mengidentifikasi suku pertama dan beda, lalu melakukan substitusi ke rumus yang sudah familiar.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang algoritma standar untuk menentukan suku ke-n pada barisan aritmetika.
- Intended difficulty `Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu menentukan beda dan memasukkannya ke rumus standar tanpa memerlukan perencanaan kompleks atau integrasi konsep.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar barisan aritmetika dan operasi bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi barisan aritmetika adalah standar kelas 10. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep, sehingga tergolong mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
Pilihan: A. -338
B. 348
C. -345
D. -331
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `c2fbd0a67c610e96b504751e`

Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.

| Opsi | Isi |
|---|---|
| A | 1.288 |
| B | 1.196 |
| C | 1.134 |
| D | 1.188 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `1.188`.
Solusi minimum hasil AI: Bilangan kelipatan 4 antara 10 dan 99 adalah 12, 16, ..., 96. Ini adalah barisan aritmetika dengan a=12, b=4, dan Un=96. Mencari n: 96 = 12 + (n-1)4 => 84 = (n-1)4 => 21 = n-1 => n=22. Jumlah: Sn = n/2(a + Un) = 22/2(12 + 96) = 11(108) = 1.188.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6b908624bf516ac21a8c47c3456852240ce59c7162783f89f744ed0a94ca88ea`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2761 |
| 2 | success | valid / verified | applying | procedural | Easy | 2787 |
| 3 | success | valid / verified | applying | procedural | Easy | 2777 |

Run 1 — solusi: Bilangan kelipatan 4 antara 10 dan 99 adalah 12, 16, ..., 96. Ini adalah barisan aritmetika dengan a=12, b=4, dan Un=96. Mencari n: 96 = 12 + (n-1)4 => 84 = (n-1)4 => 21 = n-1 => n=22. Jumlah: Sn = n/2(a + Un) = 22/2(12 + 96) = 11(108) = 1.188.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi barisan aritmetika dari deskripsi, menentukan suku pertama dan terakhir yang relevan, menghitung banyaknya suku (n), dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur rutin pada konteks yang diberikan.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme dan metode untuk menghitung jumlah deret aritmetika, yang merupakan pengetahuan prosedural.. Bukti: jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Langkah-langkahnya jelas: menentukan batas, mencari n, dan menghitung jumlah. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi nonrutin.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar barisan dan deret aritmetika, serta konsep kelipatan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi deret aritmetika adalah standar kelas 10. Soal ini adalah aplikasi langsung dari rumus deret tanpa modifikasi atau jebakan konseptual yang berat. |

Run 2 — solusi: Bilangan kelipatan 4 antara 10 dan 99 membentuk barisan aritmetika: 12, 16, ..., 96. Suku pertama (a) = 12, beda (b) = 4, suku terakhir (Un) = 96. Mencari n: 96 = 12 + (n-1)4 => 84 = (n-1)4 => 21 = n-1 => n = 22. Jumlah (Sn) = n/2 * (a + Un) = 22/2 * (12 + 96) = 11 * 108 = 1.188.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola bilangan (barisan aritmetika), menentukan suku pertama dan terakhir yang memenuhi syarat, menghitung banyaknya suku, dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme barisan dan deret aritmetika serta kriteria penggunaannya untuk menyelesaikan masalah penjumlahan bilangan dengan pola tertentu.. Bukti: jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Langkah-langkahnya jelas: menentukan batas barisan, mencari n, dan menghitung jumlah. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan strategi nonrutin.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep barisan dan deret aritmetika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi barisan dan deret adalah kurikulum standar kelas 10. Soal ini adalah aplikasi langsung dari rumus yang dipelajari tanpa modifikasi atau jebakan konseptual yang berat. |

Run 3 — solusi: Bilangan kelipatan 4 antara 10 dan 99 adalah 12, 16, ..., 96. Ini adalah barisan aritmetika dengan a=12, b=4, dan Un=96. Mencari n: 96 = 12 + (n-1)4 => 84 = (n-1)4 => 21 = n-1 => n=22. Jumlah: Sn = n/2(a + Un) = 22/2(12 + 96) = 11(108) = 1.188.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola bilangan (barisan aritmetika), menentukan suku pertama dan terakhir yang memenuhi syarat, menghitung banyaknya suku, dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur rutin pada konteks yang sudah familiar bagi siswa kelas 10.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep barisan dan deret aritmetika serta prosedur untuk menghitung jumlahnya.. Bukti: jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar (menentukan suku pertama, terakhir, n, dan jumlah deret). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin. Langkah-langkahnya jelas dan familiar bagi siswa kelas 10.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep barisan dan deret aritmetika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi deret aritmetika adalah kurikulum standar kelas 10. Soal ini tidak memerlukan modifikasi model atau penalaran kompleks, hanya aplikasi rumus langsung. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
Pilihan: A. 1.288
B. 1.196
C. 1.134
D. 1.188
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `24793dda0631231d4688920b`

Vina membagikan permen kepada tujuh temannya dengan cara tertentu. Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen. Dia melanjutkan pola ini, setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya, sampai semua temannya mendapat permen. Berapa permen yang harus Vina siapkan?

| Opsi | Isi |
|---|---|
| A | 57 |
| B | 100 |
| C | 20 |
| D | 77 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `77`.
Solusi minimum hasil AI: Ini adalah deret aritmetika dengan suku pertama a=2, beda b=3, dan n=7. Suku ke-7 (U7) = a + (n-1)b = 2 + 6(3) = 20. Jumlah 7 suku pertama (S7) = n/2 * (a + Un) = 7/2 * (2 + 20) = 7/2 * 22 = 7 * 11 = 77.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5adf8be553e607c1749110448b1300b20c0be0150e00114bae38d8f921e5f3e8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2746 |
| 2 | success | valid / verified | applying | procedural | Easy | 2766 |
| 3 | success | valid / verified | applying | procedural | Easy | 2741 |

Run 1 — solusi: Ini adalah deret aritmetika dengan suku pertama a=2, beda b=3, dan n=7. Suku ke-7 (U7) = a + (n-1)b = 2 + 6(3) = 20. Jumlah 7 suku pertama (S7) = n/2 * (a + Un) = 7/2 * (2 + 20) = 7/2 * 22 = 7 * 11 = 77.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola sebagai deret aritmetika, menentukan parameter (a, b, n), dan menerapkan rumus jumlah deret aritmetika untuk menyelesaikan masalah kontekstual.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur algoritme deret aritmetika (menghitung jumlah suku) untuk menyelesaikan masalah yang diberikan.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari rumus deret aritmetika yang familiar bagi siswa kelas 10. Jalur penyelesaian sangat jelas (identifikasi a, b, n, lalu hitung S7), tidak ada kendala yang berinteraksi, dan tidak memerlukan strategi nonrutin.. Bukti: Vina membagikan permen kepada tujuh temannya; Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang barisan dan deret aritmetika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi deret aritmetika adalah kurikulum standar kelas 10. Soal ini tidak memiliki kompleksitas tambahan, sehingga termasuk kategori mudah. |

Run 2 — solusi: Ini adalah deret aritmetika dengan suku pertama a=2, beda b=3, dan jumlah suku n=7. Suku ke-7 (U7) = a + (n-1)b = 2 + 6(3) = 20. Jumlah 7 suku pertama (S7) = n/2 * (a + Un) = 7/2 * (2 + 20) = 7/2 * 22 = 7 * 11 = 77.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola sebagai deret aritmetika, menentukan parameter (a, b, n), dan menerapkan rumus jumlah deret aritmetika untuk menyelesaikan masalah kontekstual.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pemahaman tentang struktur deret aritmetika (konsep) dan menerapkan algoritma penjumlahan deret (prosedural) untuk mendapatkan hasil.. Bukti: Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena jalur penyelesaiannya sangat jelas (deret aritmetika standar), parameter n, a, dan b diberikan secara eksplisit, dan tidak ada kendala yang saling berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: Vina membagikan permen kepada tujuh temannya; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang barisan dan deret aritmetika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari rumus deret aritmetika yang merupakan materi standar kelas 10. Tidak ada kompleksitas tambahan dalam pemodelan. |

Run 3 — solusi: Ini adalah deret aritmetika dengan suku pertama a = 2, beda b = 3, dan jumlah suku n = 7. Suku ke-7 (U7) = a + (n-1)b = 2 + 6(3) = 20. Jumlah 7 suku pertama (S7) = (n/2)(a + Un) = (7/2)(2 + 20) = (7/2)(22) = 7 * 11 = 77.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola sebagai deret aritmetika, menentukan parameter (a, b, n), dan menerapkan rumus jumlah deret aritmetika untuk menyelesaikan masalah kontekstual.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur standar (rumus jumlah deret aritmetika) untuk menyelesaikan masalah yang diberikan.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari rumus deret aritmetika. Jalur penyelesaian sangat jelas, parameter (a=2, b=3, n=7) diberikan secara eksplisit, dan tidak ada kendala kompleks atau integrasi konsep yang menuntut perencanaan tinggi.. Bukti: Vina membagikan permen kepada tujuh temannya; Teman pertama mendapat dua permen; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang barisan dan deret aritmetika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengidentifikasi dan menghitung jumlah deret aritmetika sederhana dengan parameter yang jelas. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Vina membagikan permen kepada tujuh temannya dengan cara tertentu. Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen. Dia melanjutkan pola ini, setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya, sampai semua temannya mendapat permen. Berapa permen yang harus Vina siapkan?
Pilihan: A. 57
B. 100
C. 20
D. 77
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `d215f8aa8bc3bed140f75b0b`

Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.<br><br>d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

| Opsi | Isi |
|---|---|
| A | Uang Gigih lebih banyak, selisihnya Rp92.741,00 |
| B | Uang Gigih lebih banyak, selisihnya Rp9.000,00 |
| C | Sama banyak, selisihnya Rp0,00 |
| D | Uang Firman lebih banyak, selisihnya Rp92.741,00 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Firman (bunga tunggal): M_t = M_0(1 + i*t) = 10.000.000(1 + 0,03*5) = 11.500.000. Gigih (bunga majemuk): M_t = M_0(1 + i)^t = 10.000.000(1,03)^5 = 10.000.000(1,1592741) = 11.592.741. Selisih = 11.592.741 - 11.500.000 = 92.741.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4e6d6d10234701e8ee69c309d1e159e9db9a140c36fbc7be382bb8b74637029b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3042 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3020 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3041 |

Run 1 — solusi: Firman (bunga tunggal): M_t = M_0(1 + i*t) = 10.000.000(1 + 0,03*5) = 11.500.000. Gigih (bunga majemuk): M_t = M_0(1 + i)^t = 10.000.000(1,03)^5 = 10.000.000(1,1592741) = 11.592.741. Selisih = 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan skema bunga tunggal dan majemuk dari deskripsi naratif, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan untuk membandingkan hasil akhir.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga ke rekening tabungan; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang bagaimana bunga tunggal dan majemuk bekerja (akumulasi bunga) serta penerapan prosedural rumus bunga untuk menghitung nilai akhir.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus membedakan dua konsep bunga yang berbeda (tunggal vs majemuk) berdasarkan deskripsi teks, merencanakan dua perhitungan terpisah, dan membandingkan hasilnya. Meskipun prosedurnya familiar, integrasi antara pemahaman konsep dan perhitungan membuat tuntutan kognitif lebih tinggi daripada sekadar menghitung satu nilai.. Bukti: Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar persentase, operasi aritmetika, dan konsep bunga tunggal/majemuk. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan bunga tunggal dan majemuk. Soal menuntut ketelitian dalam menerapkan rumus yang berbeda untuk dua skenario yang diberikan. |

Run 2 — solusi: Firman (bunga tunggal): M_n = M_0(1 + n*i) = 10.000.000(1 + 5*0,03) = 11.500.000. Gigih (bunga majemuk): M_n = M_0(1 + i)^n = 10.000.000(1,03)^5 ≈ 11.592.741. Selisih = 11.592.741 - 11.500.000 = 92.741. Uang Gigih lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model bunga yang berbeda (tunggal vs majemuk) dari deskripsi naratif, menerapkan rumus masing-masing, dan membandingkan hasilnya. Ini adalah penerapan konsep bunga dalam konteks rutin.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga tunggal; Gigih... menambahkan bunganya ke dalam nilai depositonya... bunga majemuk; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman prinsip bunga tunggal dan majemuk serta prosedur perhitungan yang sesuai untuk masing-masing model.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus memilih dua prosedur yang berbeda (bunga tunggal dan majemuk) berdasarkan deskripsi naratif, melakukan perhitungan untuk keduanya, dan membandingkan hasilnya. Meskipun prosedurnya familiar, terdapat beberapa langkah saling terkait yang harus dilakukan dengan benar.. Bukti: Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan bunga majemuk, serta operasi hitung eksponen. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan bunga tunggal dan majemuk. Soal menuntut ketelitian dalam menerapkan dua rumus berbeda dan membandingkan hasilnya, yang merupakan standar kemampuan menengah untuk topik ini. |

Run 3 — solusi: Firman (bunga tunggal): 10.000.000 + (5 * 0,03 * 10.000.000) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1,03)^5 = 11.592.740,74. Selisih: 11.592.740,74 - 11.500.000 = 92.740,74 (dibulatkan 92.741). Gigih memiliki uang lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan skema bunga tunggal dan majemuk, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan perbandingan untuk menentukan selisihnya. Ini melibatkan penerapan konsep bunga pada konteks perbandingan dua skema.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga ke rekening tabungan; Gigih... menambahkan bunganya ke dalam nilai depositonya; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip bunga tunggal dan bunga majemuk serta bagaimana bunga majemuk bekerja (akumulasi bunga ke modal awal) untuk memilih metode perhitungan yang benar.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemilihan dua prosedur yang berbeda (bunga tunggal dan majemuk) dan integrasi hasil perhitungan untuk menjawab perbandingan. Meskipun prosedurnya familiar, siswa harus mengelola dua alur perhitungan yang saling terkait untuk mendapatkan selisih akhir.. Bukti: Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar bunga tunggal dan bunga majemuk, operasi aritmetika dasar, dan penggunaan eksponen. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan bunga tunggal dan majemuk. Soal ini menuntut ketelitian dalam menghitung dua skema berbeda dan membandingkannya, yang merupakan standar kemampuan menengah untuk topik keuangan. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bunga
Tipe soal: multiple_choice
Stimulus: -
Soal: Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.

d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
Pilihan: A. Uang Gigih lebih banyak, selisihnya Rp92.741,00
B. Uang Gigih lebih banyak, selisihnya Rp9.000,00
C. Sama banyak, selisihnya Rp0,00
D. Uang Firman lebih banyak, selisihnya Rp92.741,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `2fbae8e5300a92a89c82f97e`

Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.<br><br>Berapa uang Gigih setelah satu tahun?

| Opsi | Isi |
|---|---|
| A | Rp300.000,00 |
| B | Rp10.300.000,00 |
| C | Rp10.030.000,00 |
| D | Rp10.609.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Modal akhir = Modal awal + (Persentase bunga * Modal awal) = 10.000.000 + (0,03 * 10.000.000) = 10.000.000 + 300.000 = 10.300.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e637bc664c17466614a97fbbac517eb4c7690bf9544e7c50cbfa83fae8a7875d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2704 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2692 |
| 3 | success | valid / verified | applying | procedural | Easy | 2650 |

Run 1 — solusi: Modal awal = 10.000.000. Bunga 3% per tahun = 0,03 * 10.000.000 = 300.000. Total uang setelah satu tahun = Modal awal + Bunga = 10.000.000 + 300.000 = 10.300.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep bunga sederhana/majemuk untuk menghitung nilai akhir setelah satu periode. Prosedur ini merupakan penerapan langsung dari definisi bunga dan penjumlahan dasar.. Bukti: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun.; Berapa uang Gigih setelah satu tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana bunga ditambahkan ke modal awal (bunga majemuk/akumulasi) dan prosedur perhitungan persentase dasar.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung 3% dari 10 juta dan menambahkannya ke modal awal. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Berapa uang Gigih setelah satu tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan konsep persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, perhitungan bunga satu periode adalah aplikasi dasar dari materi bunga majemuk/aritmetika sosial yang sudah dipelajari di jenjang sebelumnya. |

Run 2 — solusi: Uang setelah satu tahun = Modal awal + Bunga = 10.000.000 + (3% * 10.000.000) = 10.000.000 + 300.000 = 10.300.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep bunga sederhana/majemuk untuk menghitung nilai akhir setelah satu periode. Ini adalah penerapan langsung dari prosedur bunga yang sudah dipelajari di kelas 10.. Bukti: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun.; Berapa uang Gigih setelah satu tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bunga ditambahkan ke modal (bunga majemuk/akumulasi) dan prosedur perhitungan persentase dasar.. Bukti: Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung 3% dari 10 juta dan menambahkannya ke modal awal. Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang berinteraksi.. Bukti: Berapa uang Gigih setelah satu tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep persentase dan operasi aritmetika dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar untuk kelas 10 mengenai bunga. Prosedur perhitungan sangat langsung dan tidak memerlukan perencanaan strategi yang rumit. |

Run 3 — solusi: Uang setelah satu tahun = Modal awal + Bunga = 10.000.000 + (3% * 10.000.000) = 10.000.000 + 300.000 = 10.300.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep bunga sederhana/majemuk untuk menghitung nilai akhir setelah satu periode. Ini adalah penerapan langsung dari prosedur bunga.. Bukti: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun.; Berapa uang Gigih setelah satu tahun?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana bunga dihitung dan ditambahkan ke modal awal.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung 3% dari 10 juta dan menambahkannya ke modal awal. Tidak ada langkah kompleks atau integrasi kendala yang sulit.. Bukti: Berapa uang Gigih setelah satu tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan penjumlahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, perhitungan bunga satu periode adalah materi dasar yang sangat rutin dan tidak memerlukan perencanaan strategi yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4229`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur perhitungan bunga sederhana untuk menentukan nilai akhir setelah satu periode. Ini adalah penerapan langsung dari konsep bunga yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang bagaimana bunga dihitung dan diakumulasikan ke modal awal.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung 3% dari 10 juta dan menambahkannya ke modal awal. Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan operasi aritmetika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, perhitungan bunga satu periode adalah materi dasar yang sangat rutin dan tidak memerlukan perencanaan strategi yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bunga
Tipe soal: multiple_choice
Stimulus: -
Soal: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.

Berapa uang Gigih setelah satu tahun?
Pilihan: A. Rp300.000,00
B. Rp10.300.000,00
C. Rp10.030.000,00
D. Rp10.609.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `a1eac21e1913dacf28f160b7`

Perhatikan tiga komposisi sirup merah.<br>- Untuk satu liter air campurkan $\frac{2}{3}$ liter sirup merah<br>- Campurkan air dan sirup merah dengan perbandingan 2 : 3<br>- $\frac{2}{3}$ dari campuran sirup merah adalah air<br><br>Campuran mana yang paling manis?.

| Opsi | Isi |
|---|---|
| A | Campuran pertama, karena untuk 1 liter air ada $\frac{2}{3}$ liter sirup merah |
| B | Campuran kedua (air dan sirup merah 2 : 3), karena untuk 1 liter air ada $\frac{3}{2}$ liter sirup merah |
| C | Campuran ketiga, karena $\frac{2}{3}$ bagian campuran sudah ditentukan |
| D | Ketiga campuran sama manisnya, karena semuanya memuat angka 2 dan 3 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Samakan rasio sirup terhadap air untuk setiap campuran: (1) 2/3 liter sirup per 1 liter air = 0,67. (2) Rasio air:sirup 2:3 berarti sirup:air = 3:2 = 1,5. (3) Air 2/3 bagian, maka sirup 1/3 bagian, sehingga rasio sirup:air = (1/3)/(2/3) = 0,5. Karena 1,5 > 0,67 > 0,5, campuran kedua paling manis.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `287adc957fdf6aec55504cde5877427d4bd227432aad68e13120732981414520`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3756 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3491 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2944 |

Run 1 — solusi: Samakan rasio sirup terhadap air untuk setiap campuran: (1) 2/3 liter sirup per 1 liter air = 0,67. (2) Rasio air:sirup 2:3 berarti sirup:air = 3:2 = 1,5. (3) Air 2/3 bagian, maka sirup 1/3 bagian, sehingga rasio sirup:air = (1/3)/(2/3) = 0,5. Karena 1,5 > 0,67 > 0,5, campuran kedua paling manis.
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep rasio dan mengubah tiga representasi perbandingan yang berbeda (pecahan per satuan, rasio bagian-bagian, dan bagian-keseluruhan) ke dalam bentuk standar (rasio sirup terhadap air) untuk membandingkan tingkat kemanisan.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang rasio dan proporsi dalam konteks campuran, di mana siswa harus memahami hubungan antara komponen campuran dan bagaimana merepresentasikan hubungan tersebut secara konsisten agar dapat dibandingkan.. Bukti: Campuran mana yang paling manis?
- Intended difficulty `classify/Medium`: Siswa kelas 10 diharapkan mampu membandingkan rasio. Kesulitan terletak pada perlunya menstandarisasi tiga representasi yang berbeda ke dalam satu bentuk yang dapat dibandingkan. Ini memerlukan pemilihan strategi konversi yang tepat dan ketelitian dalam menginterpretasi data, bukan sekadar operasi hitung.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep rasio, perbandingan, dan operasi pecahan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena siswa harus melakukan konversi representasi yang berbeda untuk ketiga kasus sebelum bisa membandingkan nilai rasio secara valid. |

Run 2 — solusi: Samakan rasio sirup terhadap air untuk setiap campuran: (1) 2/3 liter sirup per 1 liter air = 0,67. (2) Rasio air:sirup 2:3 berarti 3/2 liter sirup per 1 liter air = 1,5. (3) 2/3 campuran adalah air, maka 1/3 adalah sirup; rasio sirup:air = (1/3):(2/3) = 1/2 = 0,5. Campuran kedua memiliki rasio sirup tertinggi (1,5), sehingga paling manis.
- Domain kognitif `classify/applying`: Siswa perlu memilih strategi untuk menormalisasi tiga representasi rasio yang berbeda (pecahan, perbandingan, dan bagian dari keseluruhan) ke dalam satu bentuk yang dapat dibandingkan (rasio sirup terhadap air).. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang rasio dan bagaimana berbagai format representasi (pecahan, perbandingan, proporsi) menyatakan hubungan yang sama.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal memerlukan konversi tiga representasi rasio yang berbeda ke bentuk standar untuk perbandingan. Siswa harus memahami hubungan antara bagian-bagian campuran, bukan sekadar menghitung angka yang ada.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, pecahan, dan perbandingan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengonversi berbagai bentuk rasio. Kesulitan terletak pada kebutuhan untuk menstandarisasi tiga format yang berbeda sebelum membandingkan. |

Run 3 — solusi: Samakan basis perbandingan (sirup per 1 liter air): Campuran 1: 2/3 liter sirup. Campuran 2: rasio air:sirup 2:3 berarti 1 liter air : 1,5 liter sirup. Campuran 3: 2/3 bagian campuran adalah air, berarti 1/3 bagian adalah sirup. Rasio sirup:air = 1:2, jadi 1 liter air : 0,5 liter sirup. Perbandingan sirup: 0,67 (C1), 1,5 (C2), 0,5 (C3). Campuran 2 paling manis.
- Domain kognitif `classify/applying`: Siswa harus mengonversi ketiga bentuk perbandingan ke dalam satuan yang sama (sirup per 1 liter air) untuk membandingkan konsentrasi. Ini adalah penerapan konsep rasio dalam konteks rutin.. Bukti: Campuran mana yang paling manis?; Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara bagian-bagian campuran (rasio) dan bagaimana merepresentasikannya dalam bentuk yang dapat dibandingkan (konseptual).. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal memerlukan konversi tiga bentuk rasio yang berbeda ke basis yang sama. Meskipun prosedurnya familiar, siswa harus teliti dalam menginterpretasikan '2/3 dari campuran adalah air' vs 'perbandingan 2:3'. Ini adalah tugas Medium karena melibatkan beberapa langkah saling terkait dan perpindahan representasi.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar rasio, pecahan, dan perbandingan senilai. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengonversi berbagai bentuk rasio. Kesulitan terletak pada ketelitian membaca informasi yang disajikan dalam format berbeda, bukan pada kompleksitas operasi hitung. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Laju Perubahan Satuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan tiga komposisi sirup merah.
- Untuk satu liter air campurkan $\frac{2}{3}$ liter sirup merah
- Campurkan air dan sirup merah dengan perbandingan 2 : 3
- $\frac{2}{3}$ dari campuran sirup merah adalah air

Campuran mana yang paling manis?.
Pilihan: A. Campuran pertama, karena untuk 1 liter air ada $\frac{2}{3}$ liter sirup merah
B. Campuran kedua (air dan sirup merah 2 : 3), karena untuk 1 liter air ada $\frac{3}{2}$ liter sirup merah
C. Campuran ketiga, karena $\frac{2}{3}$ bagian campuran sudah ditentukan
D. Ketiga campuran sama manisnya, karena semuanya memuat angka 2 dan 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `b7ee1480516d0d8e8f27caeb`

Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.<br><br>Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.

| Opsi | Isi |
|---|---|
| A | 173,85 cm |
| B | 219 cm |
| C | 148 cm |
| D | 535,09 cm |

![Gambar sumber soal 17](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Karena segitiga sebangun, rasio tinggi terhadap bayangan adalah konstan. (Tinggi Anak / Bayangan Anak) = (Tinggi Dewasa / Bayangan Dewasa). Maka, 114 / 200 = y / 305. y = (114 * 305) / 200 = 173,85 cm.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png. Transkripsi visual: Terdapat tiga gambar segitiga siku-siku yang sebangun. Gambar 1 (Anak Kecil): tinggi 114 cm, panjang bayangan 200 cm, sudut elevasi theta. Gambar 2 (Remaja): tinggi 148 cm, panjang bayangan tidak diketahui, sudut elevasi theta. Gambar 3 (Orang Dewasa): tinggi tidak diketahui (y), panjang bayangan 305 cm, sudut elevasi theta.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ab344a50847f885f26deb9acc9be793286f76f23e75c754f692932eeb16a7426`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3940 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3887 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3970 |

Run 1 — solusi: Karena segitiga sebangun, rasio tinggi terhadap bayangan adalah konstan. (Tinggi Anak / Bayangan Anak) = (Tinggi Dewasa / Bayangan Dewasa). Maka, 114 / 200 = y / 305. y = (114 * 305) / 200 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep kesebangunan segitiga yang sudah dipelajari untuk mencari nilai yang tidak diketahui dalam konteks masalah nyata (bayangan). Ini adalah penerapan prosedur rutin.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip kesebangunan (konsep) dan menerapkan algoritma perbandingan (prosedural) untuk menyelesaikan masalah.. Bukti: perbandingan segitiga sebangun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi rasio yang sesuai dari data yang diberikan secara eksplisit dalam gambar dan melakukan perhitungan dasar. Tidak ada kendala kompleks atau perencanaan strategi yang rumit.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep kesebangunan segitiga dan perbandingan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan adalah materi dasar yang familiar bagi siswa kelas 10. Soal memberikan informasi yang cukup dan langsung, sehingga tingkat kesulitan rendah. |

Run 2 — solusi: Karena segitiga sebangun, rasio tinggi terhadap bayangan adalah konstan: tinggi_anak/bayangan_anak = tinggi_dewasa/bayangan_dewasa. Maka, 114/200 = y/305. y = (114 * 305) / 200 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep kesebangunan segitiga untuk mencari nilai yang tidak diketahui. Prosedur ini bersifat rutin dan langsung.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip proporsionalitas dalam geometri (kesebangunan).. Bukti: perbandingan segitiga sebangun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi rasio yang sama dari data yang diberikan secara eksplisit dalam gambar. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar kesebangunan segitiga dan perbandingan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan adalah topik dasar yang familiar bagi siswa kelas 10. Soal memberikan informasi yang cukup dan jelas tanpa memerlukan manipulasi model yang rumit. |

Run 3 — solusi: Karena segitiga sebangun, rasio tinggi terhadap bayangan adalah konstan: (Tinggi Anak / Bayangan Anak) = (Tinggi Dewasa / Bayangan Dewasa). Maka, 114 / 200 = y / 305. y = (114 * 305) / 200 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep kesebangunan segitiga untuk mencari nilai yang tidak diketahui dalam konteks rutin. Prosedur perbandingan proporsional adalah standar untuk kelas 10.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.; 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip kesebangunan (konsep) dan penerapannya dalam perhitungan proporsi (prosedural).. Bukti: perbandingan segitiga sebangun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi pasangan sisi yang bersesuaian dari gambar dan menerapkan perbandingan senilai. Tidak ada kendala kompleks atau integrasi konsep yang menantang.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.; 114 cm 148 cm 200 cm 305 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep kesebangunan segitiga dan perbandingan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan adalah dasar yang sudah dikuasai di jenjang sebelumnya dan diaplikasikan langsung di kelas 10. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.

Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.
Pilihan: A. 173,85 cm
B. 219 cm
C. 148 cm
D. 535,09 cm
Transkripsi visual: Terdapat tiga gambar segitiga siku-siku yang sebangun. Gambar 1 (Anak Kecil): tinggi 114 cm, panjang bayangan 200 cm, sudut elevasi theta. Gambar 2 (Remaja): tinggi 148 cm, panjang bayangan tidak diketahui, sudut elevasi theta. Gambar 3 (Orang Dewasa): tinggi tidak diketahui (y), panjang bayangan 305 cm, sudut elevasi theta.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `c6e8b0f4419e6dcbc2ddc05d`

Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.<br><br>Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.

| Opsi | Isi |
|---|---|
| A | 173,85 cm |
| B | 114 cm |
| C | 152,50 cm |
| D | 535,09 cm |

![Gambar sumber soal 18](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Diketahui tan theta = depan/samping. Untuk orang dewasa, tinggi (depan) = tan 30 derajat * bayangan (samping). Maka, tinggi = 0,57 * 305 cm = 173,85 cm.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png. Transkripsi visual: Terdapat tiga ilustrasi segitiga siku-siku yang merepresentasikan bayangan tiga orang: Anak Kecil, Remaja, dan Orang Dewasa. Setiap ilustrasi menunjukkan sudut elevasi theta (sudut antara bayangan di tanah dan garis miring dari ujung bayangan ke puncak kepala). Untuk Orang Dewasa, panjang bayangan (sisi samping) adalah 305 cm, dan tinggi orang (sisi depan) adalah variabel yang dicari.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bc31c86ce593211d01e828c7ec2b153e314fd1c2a6e2b8edcb7ab90588ab9663`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3949 |
| 2 | success | valid / verified | applying | procedural | Easy | 4030 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3975 |

Run 1 — solusi: Diketahui tan theta = depan/samping. Dari soal, tan 30 derajat = 0,57. Untuk orang dewasa, sisi samping (bayangan) = 305 cm. Maka, tinggi orang dewasa = tan 30 derajat * 305 = 0,57 * 305 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi perbandingan trigonometri (tangen) pada konteks segitiga siku-siku yang diberikan. Prosedur ini bersifat langsung dan rutin bagi siswa kelas 10.. Bukti: Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.; Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang penggunaan rasio trigonometri (tangen) untuk menyelesaikan masalah tinggi benda.. Bukti: memanfaatkan perbandingan trigonometri; tan 30 o = 0,57
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena konsep yang digunakan (tan = depan/samping) diberikan secara eksplisit atau sangat familiar. Siswa hanya perlu mengidentifikasi variabel yang relevan dari gambar dan melakukan satu operasi perkalian sederhana.. Bukti: Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.; tan 30 o = 0,57

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar perbandingan trigonometri pada segitiga siku-siku. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari definisi tangen yang sudah dipelajari di kelas 10, dengan informasi yang sudah terstruktur jelas. |

Run 2 — solusi: Diketahui tan theta = depan/samping. Untuk orang dewasa, depan = tinggi (y) dan samping = 305 cm. Maka, y/305 = 0,57. Jadi, y = 0,57 * 305 = 173,85 cm.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan definisi perbandingan trigonometri (tangen) pada konteks yang diberikan secara eksplisit. Siswa hanya perlu mengidentifikasi sisi depan dan samping dari ilustrasi, lalu menerapkan rumus tan theta = depan/samping.. Bukti: Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.; Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.; tan 30 o = 0,57
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang definisi perbandingan trigonometri untuk menyelesaikan masalah yang sudah dimodelkan.. Bukti: tan 30 o = 0,57; tan theta = depan/samping
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hubungan antara variabel (tinggi, bayangan, sudut) sudah diberikan secara eksplisit melalui gambar dan nilai tangen. Siswa hanya perlu melakukan satu operasi perkalian sederhana. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.; tan 30 o = 0,57; bayangan 305 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri (tangen) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini hanya menuntut penerapan langsung rumus tanpa modifikasi atau integrasi konsep yang rumit. |

Run 3 — solusi: Diketahui tan theta = depan/samping = tinggi/bayangan. Maka, tinggi orang dewasa = tan theta * bayangan = 0,57 * 305 cm = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi perbandingan trigonometri (tangen) pada konteks geometri yang diberikan. Prosedur ini bersifat langsung dan rutin bagi siswa kelas 10.. Bukti: Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.; Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara rasio trigonometri (tangen) dengan panjang sisi pada segitiga siku-siku.. Bukti: memanfaatkan perbandingan trigonometri; tan 30 o = 0,57
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi variabel yang diketahui (bayangan sebagai sisi samping, tinggi sebagai sisi depan) dan menerapkan rumus tangen. Tidak ada kendala yang berinteraksi atau perencanaan langkah yang kompleks.. Bukti: tan 30 o = 0,57; Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri pada segitiga siku-siku (tangen). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini tidak memerlukan manipulasi aljabar atau pemodelan yang rumit, menjadikannya soal latihan rutin yang mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5512`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan definisi perbandingan trigonometri (tangen) pada konteks segitiga siku-siku yang diberikan. Prosedur ini bersifat langsung dan rutin bagi siswa kelas 10.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang penggunaan rasio trigonometri (tangen) untuk menyelesaikan masalah tinggi benda.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena konsep yang digunakan (tan = depan/samping) diberikan secara eksplisit. Siswa hanya perlu mengidentifikasi variabel yang relevan dari gambar dan melakukan satu operasi perkalian sederhana.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar perbandingan trigonometri pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari definisi tangen yang sudah dipelajari di kelas 10, dengan informasi yang sudah terstruktur jelas. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.

Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.
Pilihan: A. 173,85 cm
B. 114 cm
C. 152,50 cm
D. 535,09 cm
Transkripsi visual: Terdapat tiga ilustrasi segitiga siku-siku yang merepresentasikan bayangan tiga orang: Anak Kecil, Remaja, dan Orang Dewasa. Setiap ilustrasi menunjukkan sudut elevasi theta (sudut antara bayangan di tanah dan garis miring dari ujung bayangan ke puncak kepala). Untuk Orang Dewasa, panjang bayangan (sisi samping) adalah 305 cm, dan tinggi orang (sisi depan) adalah variabel yang dicari.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `899fad8c8260df6013a595be`

Sebuah segitiga siku-siku PQR, mempunyai besaran ∠P = 53,2o dan besaran ∠Q = 36,8o. Q 36,8º 5 4 53,2º P 3 R<br><br>Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.

| Opsi | Isi |
|---|---|
| A | tan 53,2° |
| B | cos 53,2° |
| C | cos 36,8° |
| D | tan 36,8° |

![Gambar sumber soal 19](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Berdasarkan gambar, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring. Perbandingan QR/QP = sisi samping/sisi miring = cos(Q) = cos(36,8°).
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png. Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sisi PR = 3, sisi QR = 4, dan sisi miring PQ = 5. Sudut P = 53,2 derajat dan sudut Q = 36,8 derajat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72d9132dcae634884412f7056c76cf5bf8a7ce8a2e6016364e17971acb8614cd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3915 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3849 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3924 |

Run 1 — solusi: Berdasarkan gambar, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring. Perbandingan QR/QP = sisi samping/sisi miring = cos(Q) = cos(36,8°).
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi perbandingan trigonometri dasar (cosinus) berdasarkan posisi sisi terhadap sudut tertentu dalam segitiga siku-siku. Ini adalah penerapan langsung dari definisi perbandingan trigonometri.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai; QR adalah sisi samping terhadap sudut Q dan QP adalah sisi miring
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi sinus, cosinus, dan tangen dalam segitiga siku-siku, serta kemampuan menghubungkan rasio sisi dengan fungsi trigonometri yang sesuai.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai; QR adalah sisi samping terhadap sudut Q dan QP adalah sisi miring
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi sisi samping dan sisi miring terhadap sudut Q, lalu mencocokkannya dengan definisi cosinus. Tidak ada langkah kompleks atau integrasi konsep yang berat.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri dasar (sin, cos, tan) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah dasar trigonometri kelas 10. Soal tidak menuntut manipulasi aljabar atau penalaran lanjut, hanya pengenalan rasio sisi. |

Run 2 — solusi: Pada segitiga PQR, QR adalah sisi samping sudut Q dan QP adalah sisi miring. Maka, perbandingan QR/QP = cos Q = cos 36,8°.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi perbandingan trigonometri yang sesuai dengan rasio sisi yang diberikan pada segitiga siku-siku. Ini adalah penerapan langsung dari definisi perbandingan trigonometri dasar.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi sinus, cosinus, dan tangen dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi sisi samping dan sisi miring terhadap sudut Q untuk menentukan rasio cosinus. Tidak ada langkah kompleks atau integrasi konsep yang sulit.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri (sin, cos, tan) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi dasar trigonometri kelas 10 yang sangat standar. Siswa diharapkan mampu mengenali rasio sisi terhadap sudut tanpa kesulitan berarti. |

Run 3 — solusi: Rasio QR/QP adalah perbandingan sisi samping terhadap sisi miring untuk sudut Q. Sisi samping sudut Q adalah QR = 4, dan sisi miring adalah PQ = 5. Maka, QR/QP = 4/5 = 0,8. Nilai cos 36,8 derajat juga 4/5 = 0,8. Jadi, QR/QP = cos 36,8 derajat.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi perbandingan trigonometri yang sesuai berdasarkan definisi sinus, cosinus, atau tangen pada segitiga siku-siku yang diberikan. Ini adalah penerapan langsung dari definisi perbandingan trigonometri.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi perbandingan trigonometri (sinus, cosinus, tangen) dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi sisi samping dan sisi miring terhadap sudut Q dari gambar yang sudah lengkap, lalu mencocokkannya dengan definisi cosinus. Tidak ada langkah kompleks atau integrasi konsep yang sulit.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri dasar (sin, cos, tan) pada segitiga siku-siku. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini tidak memerlukan manipulasi aljabar atau penalaran tingkat tinggi, cukup pengenalan sisi segitiga. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Pemanfaatan Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah segitiga siku-siku PQR, mempunyai besaran ∠P = 53,2o dan besaran ∠Q = 36,8o. Q 36,8º 5 4 53,2º P 3 R

Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.
Pilihan: A. tan 53,2°
B. cos 53,2°
C. cos 36,8°
D. tan 36,8°
Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sisi PR = 3, sisi QR = 4, dan sisi miring PQ = 5. Sudut P = 53,2 derajat dan sudut Q = 36,8 derajat.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `6392b9d64aaf026fd4ae54b2`

z 9,2 30º x<br><br>Cari panjang sisi x dan z.

| Opsi | Isi |
|---|---|
| A | x = 18,4 dan z = 15,94 |
| B | x = 5,31 dan z = 10,62 |
| C | x = 15,94 dan z = 18,4 |
| D | x = 9,2 dan z = 13,01 |

![Gambar sumber soal 20](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0115-11.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Diketahui sisi depan (de) = 9,2 dan sudut = 30 derajat. Untuk mencari sisi miring (z): sin 30 = de/z => 0,5 = 9,2/z => z = 9,2 / 0,5 = 18,4. Untuk mencari sisi samping (x): tan 30 = de/x => 1/sqrt(3) = 9,2/x => x = 9,2 * sqrt(3) ≈ 9,2 * 1,732 = 15,9344 (dibulatkan 15,94).
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0115-11.png. Transkripsi visual: Segitiga siku-siku dengan sudut 30 derajat. Sisi tegak (depan sudut 30 derajat) bernilai 9,2. Sisi mendatar (samping sudut 30 derajat) dilabeli x. Sisi miring dilabeli z.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5fbed0b06cdf31d0c7b98988c20438b78b07dbf2f72eb2beeddadfe3cef8b58f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 4034 |
| 2 | success | valid / verified | applying | procedural | Easy | 3997 |
| 3 | success | valid / verified | applying | procedural | Easy | 4018 |

Run 1 — solusi: Diketahui sisi depan (de) = 9,2 dan sudut = 30 derajat. Untuk mencari sisi miring (z): sin 30 = de/z => 0,5 = 9,2/z => z = 9,2 / 0,5 = 18,4. Untuk mencari sisi samping (x): tan 30 = de/x => 1/sqrt(3) = 9,2/x => x = 9,2 * sqrt(3) ≈ 9,2 * 1,732 = 15,9344 (dibulatkan 15,94).
- Domain kognitif `classify/applying`: Siswa diminta memilih dan menerapkan perbandingan trigonometri (sinus dan tangen) yang tepat untuk mencari panjang sisi segitiga siku-siku berdasarkan sudut dan satu sisi yang diketahui. Ini adalah penerapan prosedur rutin dalam konteks geometri.. Bukti: Cari panjang sisi x dan z.; sin 30 = de/z; tan 30 = de/x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi perbandingan trigonometri (sinus, tangen) dan prosedur aljabar untuk menyelesaikan variabel yang tidak diketahui.. Bukti: sin 30 = de/z; tan 30 = de/x
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi sisi depan, samping, dan miring, lalu memilih rasio trigonometri yang sesuai. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Cari panjang sisi x dan z.; 9,2 30º x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri dasar (sin, cos, tan) pada segitiga siku-siku. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini langsung menguji pemahaman konsep tanpa modifikasi atau integrasi materi lain. |

Run 2 — solusi: Diketahui sisi depan sudut 30 derajat adalah 9,2. Maka, sin 30 = 9,2/z => 0,5 = 9,2/z => z = 18,4. Tan 30 = 9,2/x => 1/akar(3) = 9,2/x => x = 9,2 * akar(3) = 9,2 * 1,732 = 15,9344, dibulatkan menjadi 15,94.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rasio trigonometri dasar (sinus dan tangen) untuk mencari panjang sisi segitiga yang belum diketahui berdasarkan sudut dan satu sisi yang diberikan. Ini adalah penerapan prosedur rutin.. Bukti: Cari panjang sisi x dan z.; sin 30 = 9,2/z; Tan 30 = 9,2/x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi rasio trigonometri (sinus, tangen) dan prosedur penggunaannya untuk menyelesaikan masalah geometri.. Bukti: Cari panjang sisi x dan z.; sin 30 = 9,2/z; Tan 30 = 9,2/x
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi sisi depan, samping, dan miring, lalu memilih rasio trigonometri yang tepat. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Cari panjang sisi x dan z.; 9,2 30º

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri dasar (sin, cos, tan) pada segitiga siku-siku. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini langsung menguji pemahaman definisi tanpa modifikasi atau konteks cerita yang rumit. |

Run 3 — solusi: Diketahui sisi depan (de) = 9,2 dan sudut = 30 derajat. Maka: sin 30 = de/z -> 0,5 = 9,2/z -> z = 9,2/0,5 = 18,4. tan 30 = de/x -> 1/sqrt(3) = 9,2/x -> x = 9,2 * sqrt(3) approx 9,2 * 1,732 = 15,934. Dibulatkan menjadi 15,94.
- Domain kognitif `classify/applying`: Siswa diminta memilih dan menerapkan rasio trigonometri yang tepat (sinus dan tangen) berdasarkan posisi sisi yang diketahui terhadap sudut acuan. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Cari panjang sisi x dan z.; sin 30 = de/z; tan 30 = de/x
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang hubungan antara sudut dan perbandingan sisi dalam segitiga siku-siku, yang merupakan pengetahuan konseptual dan prosedural.. Bukti: Cari panjang sisi x dan z.; sin 30 = de/z; tan 30 = de/x
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi sisi depan, samping, dan miring, lalu memilih rasio trigonometri yang sesuai. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Cari panjang sisi x dan z.; 9,2 30º x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri (sin, cos, tan) pada segitiga siku-siku. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah dasar trigonometri kelas 10. Soal tidak memerlukan manipulasi aljabar yang rumit atau pemodelan masalah dunia nyata, sehingga tingkat kesulitannya rendah. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Pemanfaatan Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: z 9,2 30º x

Cari panjang sisi x dan z.
Pilihan: A. x = 18,4 dan z = 15,94
B. x = 5,31 dan z = 10,62
C. x = 15,94 dan z = 18,4
D. x = 9,2 dan z = 13,01
Transkripsi visual: Segitiga siku-siku dengan sudut 30 derajat. Sisi tegak (depan sudut 30 derajat) bernilai 9,2. Sisi mendatar (samping sudut 30 derajat) dilabeli x. Sisi miring dilabeli z.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `e8e1147bfed27b5d98b29d8f`

Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.<br><br>Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, segitiga ABC siku-siku di B |
| B | Ya, segitiga ABC siku-siku di C |
| C | Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras |
| D | Tidak, karena AB² + BC² tidak sama dengan CA² |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka ΔABC siku-siku di B.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1a2cc90dd543ebfd14de64c5b72fdacd0319873dcc89465626b9c5630b4c366d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3758 |
| 2 | success | valid / verified | applying | procedural | Medium | 3827 |
| 3 | success | valid / verified | applying | procedural | Easy | 2852 |

Run 1 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka ΔABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak (atau kuadrat jarak) dan teorema Pythagoras untuk memverifikasi sifat segitiga. Ini adalah penerapan prosedur rutin dalam geometri koordinat.. Bukti: Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.; Apakah segitiga $ABC$ merupakan segitiga siku-siku?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut eksekusi algoritma standar (rumus jarak) dan pengecekan kondisi (teorema Pythagoras).. Bukti: Apakah segitiga $ABC$ merupakan segitiga siku-siku?
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan tiga sisi yang saling terkait dan perbandingan hasil untuk menentukan sifat segitiga. Tidak cukup sederhana untuk Easy karena melibatkan beberapa langkah perhitungan, namun tidak Hard karena prosedurnya sangat standar.. Bukti: Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.; Apakah segitiga $ABC$ merupakan segitiga siku-siku?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung jarak antar titik dan menerapkan teorema Pythagoras. Soal ini memerlukan beberapa langkah perhitungan yang saling terkait, sehingga dikategorikan Medium. |

Run 2 — solusi: Hitung kuadrat panjang sisi: AB² = (4-(-1))² + (-2-3)² = 50; BC² = (1-4)² + (-5-(-2))² = 18; AC² = (1-(-1))² + (-5-3)² = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka segitiga siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak untuk menentukan panjang sisi segitiga, kemudian menerapkan kebalikan Teorema Pythagoras untuk menguji sifat siku-siku. Ini adalah penerapan prosedur rutin pada konteks geometri koordinat.. Bukti: Diketahui \triangle ABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5); Apakah segitiga ABC merupakan segitiga siku-siku?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma rumus jarak dan teorema Pythagoras untuk memverifikasi sifat segitiga.. Bukti: Diketahui \triangle ABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5); Apakah segitiga ABC merupakan segitiga siku-siku?
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah (menghitung tiga panjang sisi, menjumlahkan dua sisi terpendek, membandingkan dengan sisi terpanjang). Meskipun prosedurnya familiar, siswa harus mengelola beberapa perhitungan dan menghubungkan hasil perhitungan dengan teorema Pythagoras.. Bukti: Diketahui \triangle ABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5); Apakah segitiga ABC merupakan segitiga siku-siku?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik pada koordinat Kartesius dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung jarak dua titik dan menerapkan Pythagoras. Soal ini memerlukan ketelitian dalam perhitungan koordinat dan kuadrat, namun prosedurnya standar. |

Run 3 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak (atau kuadrat jarak) untuk menentukan panjang sisi-sisi segitiga, kemudian menguji hubungan Pythagoras untuk menyimpulkan jenis segitiga. Ini adalah penerapan prosedur rutin pada konteks geometri koordinat.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku? Jelaskan.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan rumus jarak (prosedural) untuk menguji hubungan antar sisi (konseptual) dalam segitiga.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Prosedur menghitung jarak antar dua titik dan menguji Teorema Pythagoras adalah standar. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).; Apakah segitiga ABC merupakan segitiga siku-siku?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri koordinat dan Teorema Pythagoras adalah prasyarat dasar yang sudah dikuasai siswa kelas 10. Langkah penyelesaian bersifat langsung dan prosedural. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4719`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan rumus jarak (atau kuadrat jarak) dan teorema Pythagoras untuk memverifikasi sifat segitiga. Ini adalah penerapan prosedur rutin dalam geometri koordinat.
- Dimensi pengetahuan `procedural`: Soal menuntut eksekusi algoritma standar (rumus jarak) dan pengecekan kondisi (teorema Pythagoras).
- Intended difficulty `Medium`: Soal memerlukan perhitungan tiga sisi yang saling terkait dan perbandingan hasil untuk menentukan sifat segitiga. Tidak cukup sederhana untuk Easy karena melibatkan beberapa langkah perhitungan, namun tidak Hard karena prosedurnya sangat standar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung jarak antar titik dan menerapkan teorema Pythagoras. Soal ini memerlukan beberapa langkah perhitungan yang saling terkait, sehingga dikategorikan Medium. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Rumus Jarak (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.

Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.
Pilihan: A. Ya, segitiga ABC siku-siku di B
B. Ya, segitiga ABC siku-siku di C
C. Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras
D. Tidak, karena AB² + BC² tidak sama dengan CA²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `afeeb033a6caf863bee7e15a`

Asep memiliki beberapa jenis tongkat untuk olahraga: tongkat kasti, tongkat hoki, dan tongkat bisbol. Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm. Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm. Asep juga mengamati bahwa 2 tongkat kasti sama panjang dengan tongkat bisbol.<br><br>Berapakah panjang tiap jenis tongkat?

| Opsi | Isi |
|---|---|
| A | Tongkat kasti 55 cm, tongkat hoki 90 cm, dan tongkat bisbol 110 cm. |
| B | Tongkat kasti 90 cm, tongkat hoki 55 cm, dan tongkat bisbol 110 cm. |
| C | Tongkat kasti 110 cm, tongkat hoki 90 cm, dan tongkat bisbol 55 cm. |
| D | Tongkat kasti 55 cm, tongkat hoki 110 cm, dan tongkat bisbol 90 cm. |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Substitusi b=2k ke kedua persamaan: 3k+2h+2k=455 (5k+2h=455) dan k+3h+4k=545 (5k+3h=545). Kurangkan kedua persamaan: (5k+3h)-(5k+2h)=545-455, didapat h=90. Substitusi h=90 ke 5k+2(90)=455, 5k=275, k=55. Maka b=2(55)=110.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a193c157b1f58251ad007b9cea393f699aa5a50eb3de5f1a2ddcb8f47b8472fa`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3908 |
| 2 | success | valid / verified | applying | procedural | Medium | 3954 |
| 3 | success | valid / verified | applying | procedural | Medium | 4248 |

Run 1 — solusi: Substitusi b=2k ke kedua persamaan: 3k+2h+2k=455 (5k+2h=455) dan k+3h+4k=545 (5k+3h=545). Kurangkan kedua persamaan: (5k+3h)-(5k+2h)=545-455, didapat h=90. Substitusi h=90 ke 5k+2(90)=455, 5k=275, k=55. Maka b=2(55)=110.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan informasi tekstual menjadi model matematika (sistem persamaan linear) dan menerapkan prosedur aljabar (substitusi/eliminasi) untuk menemukan nilai variabel.. Bukti: Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm.; Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm.; Asep juga mengamati bahwa 2 tongkat kasti sama panjang dengan tongkat bisbol.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menggunakan algoritma penyelesaian sistem persamaan linear yang merupakan prosedur standar dalam aljabar.. Bukti: Berapakah panjang tiap jenis tongkat?
- Intended difficulty `classify/Medium`: Soal memerlukan translasi teks ke model matematika dan manipulasi aljabar multi-langkah. Tingkat kesulitan Medium karena meskipun melibatkan 3 variabel, substitusi b=2k menyederhanakan sistem menjadi SPLDV yang familiar bagi siswa kelas 10.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan manipulasi aljabar. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 sudah mempelajari SPLTV. Soal ini menuntut kemampuan memodelkan masalah dan menyelesaikan sistem, yang merupakan standar kompetensi kelas 10. |

Run 2 — solusi: Substitusi b=2k ke persamaan (1) 3k+2h+2k=455 -> 5k+2h=455 dan (2) k+3h+4k=545 -> 5k+3h=545. Kurangi kedua persamaan: (5k+3h)-(5k+2h)=545-455 -> h=90. Substitusi h=90 ke 5k+2(90)=455 -> 5k=275 -> k=55. Maka b=2(55)=110.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan informasi verbal menjadi sistem persamaan linear tiga variabel (SPLTV) dan menerapkan prosedur aljabar (substitusi/eliminasi) untuk menemukan nilai variabel. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm.; Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm.; Asep juga mengamati bahwa 2 tongkat kasti sama panjang dengan tongkat bisbol.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritme penyelesaian sistem persamaan linear, yang merupakan pengetahuan prosedural.. Bukti: Berapakah panjang tiap jenis tongkat?
- Intended difficulty `classify/Medium`: Soal memerlukan translasi verbal ke model matematika dan penyelesaian sistem linear. Meskipun prosedurnya familiar, siswa harus mengelola tiga variabel dan hubungan antar variabel, yang menuntut perencanaan langkah yang saling terkait.. Bukti: Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm.; Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm.; Asep juga mengamati bahwa 2 tongkat kasti sama panjang dengan tongkat bisbol.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar SPLDV dan kemampuan memodelkan masalah kontekstual ke dalam bentuk aljabar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 sudah mempelajari SPLTV. Soal ini berada pada tingkat kesulitan menengah karena menuntut pemodelan dari narasi ke sistem persamaan sebelum melakukan perhitungan rutin. |

Run 3 — solusi: Substitusi b=2k ke persamaan 3k+2h+b=455 dan k+3h+2b=545 menghasilkan 5k+2h=455 dan 5k+3h=545. Pengurangan kedua persamaan memberikan h=90. Substitusi h=90 ke 5k+2h=455 menghasilkan 5k=275, sehingga k=55. Maka b=2(55)=110.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam sistem persamaan linear tiga variabel dan menerapkan prosedur eliminasi atau substitusi untuk menyelesaikannya. Ini adalah penerapan rutin dari konsep SPLTV.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan metode aljabar (sistem persamaan) untuk menemukan nilai variabel yang tidak diketahui dari informasi yang diberikan.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol
- Intended difficulty `classify/Medium`: Soal memerlukan pembentukan model matematika dari narasi dan penyelesaian sistem 3 variabel. Meskipun prosedurnya standar, terdapat beberapa langkah saling terkait (substitusi b=2k, eliminasi h, lalu k) yang memerlukan ketelitian.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dan manipulasi aljabar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 SMA sudah mempelajari SPLTV. Soal ini adalah aplikasi standar yang memerlukan translasi bahasa ke model matematika dan penyelesaian sistem, yang sesuai dengan tingkat kesulitan menengah. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Persamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Asep memiliki beberapa jenis tongkat untuk olahraga: tongkat kasti, tongkat hoki, dan tongkat bisbol. Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm. Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm. Asep juga mengamati bahwa 2 tongkat kasti sama panjang dengan tongkat bisbol.

Berapakah panjang tiap jenis tongkat?
Pilihan: A. Tongkat kasti 55 cm, tongkat hoki 90 cm, dan tongkat bisbol 110 cm.
B. Tongkat kasti 90 cm, tongkat hoki 55 cm, dan tongkat bisbol 110 cm.
C. Tongkat kasti 110 cm, tongkat hoki 90 cm, dan tongkat bisbol 55 cm.
D. Tongkat kasti 55 cm, tongkat hoki 110 cm, dan tongkat bisbol 90 cm.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `873ea535dcce2925196e80f4`

Sebuah minuman dijual dalam tiga kemasan berbeda: kecil, sedang, dan besar. Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml. Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml. Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman. Berapakah volume tiap jenis kemasan?<br><br>Ada berapa solusi yang ada? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Banyak solusi (tak terhingga), karena eliminasi persamaan (1) dan (2) identik dengan persamaan (3). |
| B | Tidak dapat ditentukan tanpa menggambar grafik tiga dimensi. |
| C | Tidak ada solusi, karena hasil eliminasi menghasilkan pernyataan yang tidak mungkin benar. |
| D | Hanya satu solusi, karena ada tiga persamaan untuk tiga variabel. |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) adalah 2s+2b=2800, yang jika disederhanakan menjadi s+b=1400. Karena persamaan (3) adalah kombinasi linear dari (1) dan (2), sistem ini memiliki tak hingga solusi (dependen).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cb5695bbfd3d8e4e194357c0588a298bb930a20f83dfc68fce665825fd517f31`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 4174 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 4073 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 4288 |

Run 1 — solusi: Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) adalah 2s+2b=2800, yang jika disederhanakan menjadi s+b=1400. Karena persamaan (3) adalah kombinasi linear dari (1) dan (2), sistem ini memiliki tak hingga solusi (dependen).
- Domain kognitif `classify/reasoning`: Siswa harus menyadari bahwa sistem persamaan linear ini tidak memiliki solusi tunggal karena adanya ketergantungan linear antar persamaan. Siswa perlu melakukan eliminasi untuk membuktikan bahwa persamaan ketiga adalah redundan, yang menuntut penalaran tentang sifat sistem persamaan.. Bukti: Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml.; Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml.; Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang syarat sistem persamaan linear memiliki solusi tunggal, tak hingga, atau tidak ada solusi, bukan sekadar prosedur penyelesaian.. Bukti: Berapakah volume tiap jenis kemasan? Ada berapa solusi yang ada?
- Intended difficulty `classify/Medium`: Siswa perlu melakukan eliminasi sederhana untuk menemukan ketergantungan antar persamaan. Meskipun prosedurnya familiar, siswa harus membuat keputusan tentang sifat sistem (banyak solusi) alih-alih sekadar mencari nilai variabel, yang meningkatkan tuntutan kognitif di atas sekadar prosedur rutin.. Bukti: 3k + 2s + 3b = 4700; 3k + s + 2b = 3300; 2s + 2b = 2800

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Tiga Variabel (SPLTV) dan konsep eliminasi. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengidentifikasi sistem yang dependen. Soal ini menuntut pemahaman bahwa tidak semua sistem 3x3 memiliki solusi unik. |

Run 2 — solusi: Persamaan (1): 3k+2s+3b=4700. Persamaan (2): 3k+s+2b=3300. Persamaan (3): 2s+2b=2800. Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) jika dibagi 2 juga menghasilkan s+b=1400. Karena persamaan (3) adalah kombinasi linear dari (1) dan (2), sistem memiliki tak hingga solusi.
- Domain kognitif `classify/reasoning`: Siswa harus menganalisis ketergantungan linear antar persamaan untuk menentukan banyaknya solusi, bukan sekadar menghitung nilai variabel.. Bukti: Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml.; Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml.; Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman.
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang sistem persamaan linear yang bergantung (dependent system) dan syarat keberadaan solusi unik.. Bukti: Berapakah volume tiap jenis kemasan?; Ada berapa solusi yang ada?
- Intended difficulty `classify/Medium`: Siswa perlu mengidentifikasi bahwa sistem memiliki persamaan yang redundan. Ini adalah konsep standar SPLTV kelas 10, namun memerlukan langkah penalaran untuk menyadari ketergantungan linear, bukan sekadar substitusi rutin.. Bukti: 3k + 2s + 3b = 4700; 3k + s + 2b = 3300; 2s + 2b = 2800

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar SPLTV dan eliminasi. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diajarkan SPLTV. Menyadari bahwa persamaan ketiga adalah kombinasi linear dari dua persamaan lainnya adalah bagian dari kurikulum, namun menuntut penalaran lebih dari sekadar menghitung nilai. |

Run 3 — solusi: Persamaan 1: 3k+2s+3b=4700. Persamaan 2: 3k+s+2b=3300. Persamaan 3: 2s+2b=2800. Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) disederhanakan menjadi s+b=1400. Karena persamaan (3) ekuivalen dengan hasil eliminasi (1) dan (2), sistem memiliki tak hingga solusi.
- Domain kognitif `classify/reasoning`: Siswa harus melakukan eliminasi untuk menyadari bahwa persamaan ketiga adalah kombinasi linear dari dua persamaan pertama, yang menunjukkan ketergantungan linear. Ini memerlukan penalaran tentang sifat sistem persamaan, bukan sekadar prosedur rutin.. Bukti: 3k + 2s + 3b = 4700; 3k + 1s + 2b = 3300; 2s + 2b = 2800; Berapakah volume tiap jenis kemasan? Ada berapa solusi yang ada?
- Dimensi pengetahuan `classify/conceptual`: Memahami konsep sistem persamaan linear yang bergantung (dependent system) dan bagaimana hubungan antar persamaan menentukan jumlah solusi.. Bukti: 3k + 2s + 3b = 4700; 3k + 1s + 2b = 3300; 2s + 2b = 2800
- Intended difficulty `classify/Medium`: Soal ini memerlukan manipulasi aljabar sederhana namun menuntut pemahaman konseptual tentang sistem persamaan yang tidak memiliki solusi tunggal. Siswa tidak bisa langsung mencari nilai variabel, melainkan harus mengevaluasi ketergantungan antar persamaan.. Bukti: 3k + 2s + 3b = 4700; 3k + 1s + 2b = 3300; 2s + 2b = 2800

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Dua Variabel (SPLDV) dan konsep dasar eliminasi. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menyelesaikan SPLTV, namun soal ini menguji pemahaman mendalam tentang sistem yang bergantung, yang merupakan tantangan menengah. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Persamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah minuman dijual dalam tiga kemasan berbeda: kecil, sedang, dan besar. Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml. Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml. Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman. Berapakah volume tiap jenis kemasan?

Ada berapa solusi yang ada? Jelaskan.
Pilihan: A. Banyak solusi (tak terhingga), karena eliminasi persamaan (1) dan (2) identik dengan persamaan (3).
B. Tidak dapat ditentukan tanpa menggambar grafik tiga dimensi.
C. Tidak ada solusi, karena hasil eliminasi menghasilkan pernyataan yang tidak mungkin benar.
D. Hanya satu solusi, karena ada tiga persamaan untuk tiga variabel.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `55f4593490fe0eca29b58712`

Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).<br><br>Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

| Opsi | Isi |
|---|---|
| A | Tidak, karena 2(0) + 5(0) tidak sama dengan 10. |
| B | Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun. |
| C | Ya, karena 2(0) + 5(0) = 0 dan 0 < 10 (pertidaksamaan bernilai benar). |
| D | Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu. |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Substitusi x = 0 dan y = 0 ke dalam pertidaksamaan 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yang setara dengan 0 < 10. Karena 0 < 10 adalah pernyataan yang benar, maka titik (0,0) termasuk dalam daerah hasil pertidaksamaan tersebut.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3f643717774adab9b89262e1ea590ef70e9345afa944b4c9c0dff9c07f261e93`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3532 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3515 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2892 |

Run 1 — solusi: Substitusi x = 0 dan y = 0 ke dalam pertidaksamaan 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yang setara dengan 0 < 10. Karena 0 < 10 adalah pernyataan yang benar, maka titik (0,0) termasuk dalam daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan prosedur substitusi langsung yang sudah ditentukan langkah-langkahnya dalam petunjuk soal. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Siswa diminta untuk menerapkan algoritma substitusi nilai ke dalam variabel untuk memverifikasi kebenaran suatu pertidaksamaan.. Bukti: Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Intended difficulty `classify/Easy`: Soal bersifat sangat terbantu (scaffolded) dengan petunjuk eksplisit. Siswa hanya perlu melakukan operasi aritmetika dasar tanpa harus merencanakan langkah atau mengintegrasikan kendala.. Bukti: Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang substitusi nilai ke dalam variabel dan konsep pertidaksamaan linear. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan rendah karena soal memberikan panduan langkah demi langkah yang jelas, sehingga siswa kelas 10 dapat menyelesaikannya dengan prosedur rutin. |

Run 2 — solusi: Substitusi x=0 dan y=0 ke dalam pertidaksamaan 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yaitu 0 < 10. Karena 0 < 10 bernilai benar, maka titik (0,0) termasuk dalam daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/knowing`: Soal secara eksplisit memberikan petunjuk untuk melakukan substitusi nilai ke dalam pertidaksamaan. Siswa hanya perlu melakukan prosedur substitusi dan evaluasi kebenaran pernyataan matematika dasar.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang cara menentukan apakah suatu titik memenuhi pertidaksamaan linear dengan substitusi langsung.. Bukti: Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal memberikan petunjuk langkah demi langkah yang sangat jelas. Tidak ada perencanaan strategi yang kompleks atau kendala yang berinteraksi. Siswa hanya perlu melakukan substitusi sederhana dan membandingkan hasil.. Bukti: Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linear dan substitusi nilai variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat terbantu dengan petunjuk eksplisit yang diberikan, menjadikannya tugas prosedural yang sangat mendasar bagi siswa kelas 10. |

Run 3 — solusi: Substitusi x=0 dan y=0 ke dalam pertidaksamaan 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yaitu 0 < 10. Karena 0 < 10 adalah pernyataan yang benar, maka titik (0,0) termasuk dalam daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan prosedur substitusi nilai ke dalam pertidaksamaan linear yang sudah diberikan secara eksplisit. Ini adalah penerapan langsung dari prosedur dasar untuk menguji titik pada daerah penyelesaian pertidaksamaan.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prosedur substitusi dan aturan pertidaksamaan dasar untuk menentukan apakah suatu titik memenuhi syarat pertidaksamaan.. Bukti: 2 x + 5 y < 10; substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Prosedur substitusi diberikan sebagai petunjuk, dan operasi hitungnya sangat sederhana. Tidak ada perencanaan langkah yang kompleks atau kendala yang berinteraksi.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linear dan substitusi variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, menguji titik pada pertidaksamaan adalah prosedur dasar yang sangat familiar. Soal bahkan memberikan petunjuk langkah demi langkah, sehingga tidak ada tuntutan kognitif yang tinggi. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Pertidaksamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).

Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
Pilihan: A. Tidak, karena 2(0) + 5(0) tidak sama dengan 10.
B. Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun.
C. Ya, karena 2(0) + 5(0) = 0 dan 0 < 10 (pertidaksamaan bernilai benar).
D. Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `17d32fe57e7f77cdae983dc8`

Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).<br><br>Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

| Opsi | Isi |
|---|---|
| A | Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun. |
| B | Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu. |
| C | Ya, karena 6(0) + 2(0) = 0 sudah memenuhi pertidaksamaan tersebut. |
| D | Tidak, karena 6(0) + 2(0) = 0 dan 0 > 10 salah (pertidaksamaan tidak bernilai benar). |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, atau 0 > 10. Karena 0 > 10 adalah pernyataan yang salah, maka titik (0,0) bukan merupakan daerah hasil pertidaksamaan tersebut.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8c5c5896bb2998d43ec82c2bb021e506cb0f8bba74bcf46be815723900fe0b6e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2887 |
| 2 | success | valid / verified | applying | procedural | Easy | 2848 |
| 3 | success | valid / verified | applying | procedural | Easy | 2902 |

Run 1 — solusi: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, yang berarti 0 > 10. Karena 0 tidak lebih besar dari 10, maka pernyataan tersebut salah. Jadi, titik (0,0) bukan merupakan daerah hasil pertidaksamaan.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan prosedur substitusi langsung ke dalam pertidaksamaan yang sudah diberikan untuk menentukan kebenaran suatu titik. Ini adalah penerapan prosedur yang sangat langsung.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Siswa diminta untuk menjalankan algoritma substitusi untuk memverifikasi apakah titik memenuhi pertidaksamaan, yang merupakan prosedur standar dalam aljabar.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal memberikan petunjuk eksplisit tentang metode yang harus digunakan (substitusi). Tidak ada perencanaan langkah yang kompleks atau integrasi konsep yang menantang; siswa hanya perlu melakukan operasi aritmetika dasar dan membandingkan hasilnya.. Bukti: Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang substitusi variabel dan perbandingan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, tugas substitusi langsung ini sangat mendasar dan terbantu oleh petunjuk soal yang eksplisit, sehingga dikategorikan mudah. |

Run 2 — solusi: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, yang berarti 0 > 10. Karena 0 > 10 adalah pernyataan yang salah, maka titik (0,0) bukan merupakan daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur substitusi titik ke dalam pertidaksamaan linear untuk menentukan apakah titik tersebut memenuhi syarat pertidaksamaan. Ini adalah penerapan langsung dari konsep daerah penyelesaian pertidaksamaan linear.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana menguji titik pada pertidaksamaan linear.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal ini sangat terbimbing dengan petunjuk eksplisit untuk melakukan substitusi. Prosedur yang diperlukan sangat dasar dan familiar bagi siswa kelas 10.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linear dan substitusi variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini memberikan petunjuk langkah demi langkah yang sangat jelas, sehingga mengurangi beban kognitif siswa dalam merencanakan strategi penyelesaian. |

Run 3 — solusi: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, yang berarti 0 > 10. Karena 0 > 10 adalah pernyataan yang salah, maka titik (0,0) bukan merupakan daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerapkan prosedur substitusi titik ke dalam pertidaksamaan linear untuk menentukan apakah titik tersebut memenuhi syarat pertidaksamaan. Ini adalah penerapan langsung dari konsep daerah penyelesaian pertidaksamaan linear.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?; Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menggunakan prosedur substitusi untuk menguji titik pada pertidaksamaan, yang merupakan metode standar dalam aljabar.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal ini memberikan petunjuk eksplisit tentang metode penyelesaian (substitusi). Langkah-langkahnya sangat rutin dan tidak memerlukan perencanaan kompleks atau integrasi kendala yang sulit bagi siswa kelas 10.. Bukti: Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linear dua variabel dan substitusi titik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 10, dengan petunjuk langkah demi langkah yang memandu siswa, sehingga tingkat kesulitannya rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4543`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal secara eksplisit memberikan prosedur yang harus dilakukan (substitusi titik ke pertidaksamaan). Siswa hanya perlu menerapkan prosedur tersebut untuk memverifikasi kebenaran pernyataan, yang merupakan aktivitas penerapan konsep dasar.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman siswa tentang algoritma atau metode standar untuk menguji apakah suatu titik berada dalam daerah penyelesaian pertidaksamaan linear.
- Intended difficulty `Easy`: Soal ini sangat terbimbing (scaffolded) dengan petunjuk eksplisit tentang metode yang harus digunakan. Tidak ada perencanaan langkah yang kompleks atau integrasi konsep yang menantang; siswa hanya perlu melakukan operasi aritmetika dasar dan membandingkan hasilnya.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linear dua variabel dan substitusi variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, tugas substitusi langsung ini sangat mendasar dan terbantu oleh petunjuk soal yang eksplisit, sehingga dikategorikan mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Pertidaksamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).

Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
Pilihan: A. Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun.
B. Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu.
C. Ya, karena 6(0) + 2(0) = 0 sudah memenuhi pertidaksamaan tersebut.
D. Tidak, karena 6(0) + 2(0) = 0 dan 0 > 10 salah (pertidaksamaan tidak bernilai benar).
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `0b4b98faa7f553833f0db971`

Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.<br><br>Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?

| Opsi | Isi |
|---|---|
| A | 20 kuas lukis jenis I dan 20 kuas lukis jenis II |
| B | 15 kuas lukis jenis I dan 25 kuas lukis jenis II |
| C | 27 kuas lukis jenis I dan 13 kuas lukis jenis II |
| D | 13 kuas lukis jenis I dan 27 kuas lukis jenis II |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35x + 24y = 1103 (dalam ribuan). Substitusi x = 40 - y ke persamaan kedua: 35(40 - y) + 24y = 1103 => 1400 - 35y + 24y = 1103 => -11y = -297 => y = 27. Maka x = 40 - 27 = 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `477143305f930b62d551c771bb7acff094405800b413e93e5322eeb633318724`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3074 |
| 2 | success | valid / verified | applying | procedural | Easy | 3013 |
| 3 | success | valid / verified | applying | procedural | Easy | 2954 |

Run 1 — solusi: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika SPLDV dan menyelesaikan sistem tersebut menggunakan metode substitusi atau eliminasi yang sudah dipelajari.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam memodelkan situasi nyata ke dalam sistem persamaan linear dan menyelesaikannya.. Bukti: x+y=40 dan 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah utama: memodelkan masalah ke dalam SPLDV dan menyelesaikan sistem tersebut. Meskipun prosedurnya familiar, siswa harus mengelola angka yang cukup besar dan memastikan konsistensi antara dua kendala (jumlah barang dan total harga).. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

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
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai penerapan standar SPLDV dengan konteks ekonomi sederhana. |

Run 2 — solusi: Misal x=kuas I, y=kuas II. Sistem: x+y=40 dan 35x+24y=1103 (dalam ribuan). Dari x=40-y, substitusi ke 35(40-y)+24y=1103 -> 1400-35y+24y=1103 -> -11y=-297 -> y=27. Maka x=40-27=13. Jadi 13 kuas jenis I dan 27 kuas jenis II.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika SPLDV dan menyelesaikan sistem tersebut menggunakan metode substitusi atau eliminasi yang sudah dipelajari.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur standar (eliminasi/substitusi) untuk menyelesaikan sistem persamaan linear dua variabel.. Bukti: x+y=40; 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan rutin SPLDV. Siswa hanya perlu memodelkan dua persamaan linear sederhana dan menyelesaikannya. Tidak ada kendala kompleks atau kebutuhan strategi non-rutin.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan operasi aritmetika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar kompetensi kelas 10 untuk SPLDV. Tingkat kesulitan rendah karena prosedur penyelesaian sangat umum dan langsung. |

Run 3 — solusi: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan informasi tekstual ke dalam model matematika SPLDV dan menyelesaikan sistem tersebut menggunakan metode substitusi atau eliminasi yang sudah dipelajari.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam memodelkan masalah nyata ke dalam sistem persamaan linear dan menyelesaikannya.. Bukti: berapa banyak masing-masing jenis kuas lukis yang terjual
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan rutin SPLDV. Siswa hanya perlu membuat dua persamaan linear dan menyelesaikannya. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 40 kuas lukis; Rp35.000,00; Rp24.000,00; Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan operasi aritmetika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi SPLDV adalah standar kelas 10. Soal ini bersifat rutin dan langsung, tidak memerlukan penalaran tingkat tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5114`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika SPLDV dan menyelesaikan sistem tersebut menggunakan metode substitusi atau eliminasi yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dalam memodelkan situasi nyata ke dalam sistem persamaan linear dan menyelesaikannya.
- Intended difficulty `Easy`: Soal ini merupakan penerapan rutin SPLDV. Siswa hanya perlu membuat dua persamaan linear dan menyelesaikannya. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan. Prosedur penyelesaian sangat umum dan langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan operasi aritmetika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi SPLDV adalah standar kelas 10. Soal ini bersifat rutin dan langsung, tidak memerlukan penalaran tingkat tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.

Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
Pilihan: A. 20 kuas lukis jenis I dan 20 kuas lukis jenis II
B. 15 kuas lukis jenis I dan 25 kuas lukis jenis II
C. 27 kuas lukis jenis I dan 13 kuas lukis jenis II
D. 13 kuas lukis jenis I dan 27 kuas lukis jenis II
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `8fa35d360450878f96feeb48`

Tentukan solusi atau akar-akar dari persamaan kuadrat $2x^2 - 8x + 6 = 0$.

| Opsi | Isi |
|---|---|
| A | x = -1 atau x = 3 |
| B | x = -1 atau x = -3 |
| C | x = 2 atau x = 6 |
| D | x = 1 atau x = 3 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Persamaan 2x^2 - 8x + 6 = 0 dapat disederhanakan dengan membagi kedua ruas dengan 2 menjadi x^2 - 4x + 3 = 0. Faktorisasi dari persamaan tersebut adalah (x - 1)(x - 3) = 0, sehingga akar-akarnya adalah x = 1 atau x = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1acc10bd677b1f20a064af0265e2757a355fe58ff1b810c8644782683b50fd72`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2740 |
| 2 | success | valid / verified | applying | procedural | Easy | 3188 |
| 3 | success | valid / verified | applying | procedural | Easy | 2751 |

Run 1 — solusi: Persamaan 2x^2 - 8x + 6 = 0 dapat disederhanakan dengan membagi kedua ruas dengan 2 menjadi x^2 - 4x + 3 = 0. Faktorisasi dari persamaan tersebut adalah (x - 1)(x - 3) = 0, sehingga akar-akarnya adalah x = 1 atau x = 3.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur standar untuk mencari akar persamaan kuadrat. Siswa hanya perlu melakukan penyederhanaan (pembagian dengan konstanta) dan faktorisasi atau penggunaan rumus kuadrat, yang merupakan prosedur rutin.. Bukti: Tentukan solusi atau akar-akar dari persamaan kuadrat 2x^2 - 8x + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritme faktorisasi atau rumus kuadrat untuk menyelesaikan persamaan kuadrat, yang merupakan pengetahuan prosedural.. Bukti: 2x^2 - 8x + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa kelas 10 diharapkan sudah menguasai teknik faktorisasi persamaan kuadrat. Langkah penyelesaiannya jelas, tidak memerlukan integrasi konsep yang kompleks, dan tidak ada kendala yang saling berinteraksi.. Bukti: 2x^2 - 8x + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan kuadrat dan teknik faktorisasi atau rumus ABC. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari akar persamaan kuadrat adalah materi dasar kelas 10 yang bersifat prosedural dan rutin. |

Run 2 — solusi: 2x^2 - 8x + 6 = 0 dibagi 2 menjadi x^2 - 4x + 3 = 0. Faktorkan menjadi (x-1)(x-3) = 0, sehingga x = 1 atau x = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat, baik dengan pemfaktoran maupun rumus kuadrat.. Bukti: Tentukan solusi atau akar-akar dari persamaan kuadrat 2x^2 - 8x + 6 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma atau metode penyelesaian persamaan kuadrat.. Bukti: 2x^2 - 8x + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin yang sangat standar untuk kelas 10. Persamaan dapat disederhanakan dengan mudah dan faktor-faktornya jelas.. Bukti: 2x^2 - 8x + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar dan pemfaktoran persamaan kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menyelesaikan persamaan kuadrat adalah materi dasar kelas 10. Soal ini tidak memiliki kendala yang kompleks atau langkah yang saling bergantung secara rumit. |

Run 3 — solusi: Persamaan 2x^2 - 8x + 6 = 0 disederhanakan dengan membagi kedua ruas dengan 2 menjadi x^2 - 4x + 3 = 0. Faktorkan persamaan tersebut menjadi (x - 1)(x - 3) = 0. Maka, akar-akarnya adalah x = 1 atau x = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk mencari akar persamaan kuadrat. Tidak ada strategi non-rutin yang diperlukan; ini adalah penerapan langsung dari metode faktorisasi atau rumus kuadrat yang familiar bagi siswa kelas 10.. Bukti: Tentukan solusi atau akar-akar dari persamaan kuadrat 2x^2 - 8x + 6 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme penyelesaian persamaan kuadrat (faktorisasi), yang merupakan pengetahuan prosedural.. Bukti: Tentukan solusi atau akar-akar dari persamaan kuadrat 2x^2 - 8x + 6 = 0.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menyederhanakan persamaan dengan membagi koefisien dengan 2, lalu memfaktorkan bentuk kuadrat sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk membangun model kompleks.. Bukti: 2x^2 - 8x + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan kuadrat dan metode faktorisasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari akar persamaan kuadrat adalah materi dasar kelas 10. Soal ini tidak memerlukan langkah perencanaan yang rumit atau integrasi konsep yang mendalam. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Persamaan Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan solusi atau akar-akar dari persamaan kuadrat $2x^2 - 8x + 6 = 0$.
Pilihan: A. x = -1 atau x = 3
B. x = -1 atau x = -3
C. x = 2 atau x = 6
D. x = 1 atau x = 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `6d67a36d7ac3cfb4348b802b`

Tentukan akar-akar dari persamaan kuadrat $2x^2 - 18 = 0$.

| Opsi | Isi |
|---|---|
| A | x = 9 atau x = -9 |
| B | x = -3 (akar kembar) |
| C | x = 3 (hanya satu akar) |
| D | x = 3 atau x = -3 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 2x^2 - 18 = 0 => 2x^2 = 18 => x^2 = 9 => x = ±√9 => x = 3 atau x = -3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `397eed762c61765c5bc67a6150cdcfe6552c7d177974a55de09bad084db47699`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2642 |
| 2 | success | valid / verified | applying | procedural | Easy | 2644 |
| 3 | success | valid / verified | applying | procedural | Easy | 2643 |

Run 1 — solusi: 2x^2 - 18 = 0 => 2x^2 = 18 => x^2 = 9 => x = ±√9 => x = 3 atau x = -3.
- Domain kognitif `classify/knowing`: Soal meminta siswa menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat sederhana. Siswa hanya perlu melakukan manipulasi aljabar dasar (pindah ruas dan akar kuadrat) yang merupakan prosedur rutin.. Bukti: Tentukan akar-akar dari persamaan kuadrat 2x^2 - 18 = 0.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma penyelesaian persamaan kuadrat (prosedural) untuk menemukan nilai x yang memenuhi persamaan tersebut.. Bukti: 2x^2 - 18 = 0
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Persamaan kuadrat yang diberikan tidak memiliki suku linear (b=0), sehingga penyelesaiannya langsung melalui isolasi variabel. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: 2x^2 - 18 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan konsep akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi persamaan kuadrat adalah topik dasar kelas 10. Soal ini menguji pemahaman dasar tentang akar kuadrat tanpa kerumitan faktorisasi atau rumus ABC. |

Run 2 — solusi: 2x^2 - 18 = 0 => 2x^2 = 18 => x^2 = 9 => x = ±3. Jadi, x = 3 atau x = -3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat sederhana. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks yang diperlukan.. Bukti: Tentukan akar-akar dari persamaan kuadrat 2x^2 - 18 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian persamaan kuadrat (prosedural) dan konsep dasar akar persamaan.. Bukti: 2x^2 - 18 = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah penyelesaian yang sangat jelas dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk membangun model yang kompleks.. Bukti: Tentukan akar-akar dari persamaan kuadrat 2x^2 - 18 = 0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar, operasi pembagian, dan konsep akar kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Persamaan kuadrat bentuk ax^2 - c = 0 adalah materi dasar kelas 10 yang sangat familiar. Langkah penyelesaiannya langsung dan tidak memerlukan manipulasi aljabar yang rumit. |

Run 3 — solusi: 2x^2 - 18 = 0 => 2x^2 = 18 => x^2 = 9 => x = ±√9 => x = 3 atau x = -3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat sederhana. Tidak ada strategi non-rutin yang diperlukan; ini adalah penerapan langsung dari algoritma penyelesaian persamaan kuadrat.. Bukti: Tentukan akar-akar dari persamaan kuadrat 2x^2 - 18 = 0
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode penyelesaian persamaan kuadrat (prosedural) dan konsep akar-akar persamaan.. Bukti: 2x^2 - 18 = 0
- Intended difficulty `classify/Easy`: Soal ini sangat rutin dan langsung. Siswa hanya perlu melakukan manipulasi aljabar dasar (pindah ruas dan akar kuadrat). Tidak ada kendala yang berinteraksi atau kebutuhan untuk membangun model yang kompleks.. Bukti: 2x^2 - 18 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan konsep dasar persamaan kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Persamaan kuadrat bentuk x^2 - a = 0 adalah materi dasar kelas 10. Tingkat kesulitan rendah karena prosedur penyelesaian sangat standar dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4042`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta siswa menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat sederhana. Siswa hanya perlu melakukan manipulasi aljabar dasar (pindah ruas dan akar kuadrat) yang merupakan prosedur rutin.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritma penyelesaian persamaan kuadrat (prosedural) untuk menemukan nilai x yang memenuhi persamaan tersebut.
- Intended difficulty `Easy`: Soal ini sangat mendasar dan rutin. Persamaan kuadrat yang diberikan tidak memiliki suku linear (b=0), sehingga penyelesaiannya langsung melalui isolasi variabel. Tidak ada langkah kompleks atau kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan konsep akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi persamaan kuadrat adalah topik dasar kelas 10. Soal ini menguji pemahaman dasar tentang akar kuadrat tanpa kerumitan faktorisasi atau rumus ABC. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Persamaan Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan akar-akar dari persamaan kuadrat $2x^2 - 18 = 0$.
Pilihan: A. x = 9 atau x = -9
B. x = -3 (akar kembar)
C. x = 3 (hanya satu akar)
D. x = 3 atau x = -3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `d590344d18abe3ebd38fb8ed`

Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.<br><br>\|Waktu (Detik)\|0\|1\|2\|3\|4\|5\|6\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Jarak (m)\|0\|5\|8\|9\|8\|5\|0\|<br><br>Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan tanpa menggambar grafiknya. |
| B | Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi. |
| C | Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi. |
| D | Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi. |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Data menunjukkan nilai jarak meningkat dari 0 hingga mencapai maksimum 9 pada t=3, kemudian menurun kembali ke 0. Pola naik-lalu-turun ini menunjukkan titik puncak maksimum, yang berarti grafik fungsi kuadrat terbuka ke bawah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f6e74f3d98e95eaa80832fd045892894742a8e2afb6d62998b2dcc969df34c9a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2871 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2859 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2855 |

Run 1 — solusi: Data menunjukkan nilai jarak meningkat dari 0 ke 9 (puncak) lalu menurun kembali ke 0. Pola simetris naik-lalu-turun ini menunjukkan titik puncak maksimum. Fungsi kuadrat dengan titik puncak maksimum memiliki koefisien a < 0, sehingga grafik terbuka ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta menginterpretasikan pola numerik dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan) tanpa bantuan visual grafik. Ini memerlukan pemahaman konseptual tentang hubungan antara perilaku nilai fungsi (naik-turun) dengan karakteristik parabola.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip konseptual tentang bentuk parabola (titik balik maksimum vs minimum) untuk menganalisis data numerik yang diberikan.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk melakukan abstraksi dari data numerik ke sifat fungsi tanpa bantuan visual. Meskipun prosedurnya sederhana, siswa harus memahami hubungan antara pola data (naik-turun) dengan sifat koefisien fungsi kuadrat (a < 0) tanpa bantuan grafik yang biasanya menjadi scaffold utama.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jarak (m)\|0\|5\|8\|9\|8\|5\|0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan hubungan koefisien a dengan arah bukaan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengaitkan pola data dengan karakteristik fungsi kuadrat. Tantangan utamanya adalah melakukan analisis tanpa bantuan visual (grafik), yang menuntut pemahaman konseptual lebih dalam daripada sekadar menghitung. |

Run 2 — solusi: Data menunjukkan jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan nilai maksimum pada fungsi kuadrat, yang secara geometris berarti parabola terbuka ke bawah (koefisien a < 0).
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan pola data numerik (naik-turun) dan menghubungkannya dengan sifat geometris fungsi kuadrat (arah bukaan parabola) tanpa bantuan visual. Ini memerlukan pemahaman konseptual tentang hubungan antara perilaku fungsi dan bentuk grafiknya.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jelaskan alasanmu.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara data tabel (representasi diskrit) dan sifat fungsi kuadrat (konsep parabola), bukan sekadar menghafal rumus.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; pola naik-lalu-turun ini khas parabola dengan koefisien a negatif
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan penalaran konseptual untuk menghubungkan pola data (naik-turun) dengan sifat fungsi kuadrat tanpa bantuan visual. Meskipun prosedurnya tidak rumit, siswa perlu memahami hubungan antara titik puncak dan arah bukaan parabola secara mandiri.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jelaskan alasanmu.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi kuadrat dan bentuk parabola. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menginterpretasikan data tabel fungsi kuadrat. Tantangan utamanya adalah melakukan transfer representasi dari tabel ke sifat geometris tanpa menggambar, yang merupakan standar kemampuan menengah. |

Run 3 — solusi: Data menunjukkan jarak meningkat dari 0 (t=0) ke 9 (t=3) lalu menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak maksimum, yang merupakan karakteristik fungsi kuadrat dengan koefisien a negatif (terbuka ke bawah).
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan pola numerik dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan parabola) tanpa melakukan penggambaran. Ini memerlukan pemahaman konseptual tentang hubungan antara perilaku nilai fungsi (naik-maksimum-turun) dengan bentuk grafik.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jelaskan alasanmu.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana karakteristik fungsi kuadrat (koefisien a) tercermin dalam data tabel, bukan sekadar menghitung nilai.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; pola naik-lalu-turun ini khas parabola dengan koefisien a negatif
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena pola data sangat jelas (simetris dan memiliki titik balik maksimum yang eksplisit). Siswa tidak perlu melakukan perhitungan rumit atau manipulasi aljabar yang berat; cukup mengenali pola naik-turun sebagai indikator parabola terbuka ke bawah.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang grafik fungsi kuadrat dan hubungan antara titik puncak dengan arah bukaan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 sudah mempelajari fungsi kuadrat. Mengidentifikasi arah bukaan dari tabel data adalah aplikasi langsung dari konsep dasar fungsi kuadrat yang diharapkan sudah dikuasai. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5211`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan pemahaman konseptual tentang bentuk parabola (titik balik maksimum) untuk menginterpretasikan pola data numerik yang diberikan tanpa perlu melakukan perhitungan atau penggambaran.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang hubungan antara perilaku nilai fungsi (pola data) dan karakteristik geometris fungsi kuadrat (arah bukaan).
- Intended difficulty `Easy`: Soal ini tergolong Easy karena pola data sangat jelas, simetris, dan memiliki titik balik maksimum yang eksplisit. Siswa tidak perlu melakukan perhitungan rumit atau manipulasi aljabar; cukup mengenali pola naik-turun sebagai indikator parabola terbuka ke bawah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan hubungan titik puncak dengan arah bukaan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 sudah mempelajari fungsi kuadrat. Mengidentifikasi arah bukaan dari tabel data yang simetris dan memiliki titik balik jelas adalah aplikasi langsung dari konsep dasar yang diharapkan sudah dikuasai. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.

|Waktu (Detik)|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|Jarak (m)|0|5|8|9|8|5|0|

Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.
Pilihan: A. Tidak dapat ditentukan tanpa menggambar grafiknya.
B. Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi.
C. Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi.
D. Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `3fab45a2a8a53e25de52d0f6`

Sebuah bola dilemparkan dari ketinggian awal 4 m dan mencapai ketinggian maksimum 8 m setelah dua detik sejak dilempar.<br><br>Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum $y = ax^2+bx+c$.

| Opsi | Isi |
|---|---|
| A | $y = -x^2 - 4x + 4$ |
| B | $y = x^2 - 4x + 4$ |
| C | $y = -x^2 + 4x + 4$ |
| D | $y = -x^2 + 4x + 8$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Titik puncak (h, k) = (2, 8), maka y = a(x-2)^2 + 8. Melalui (0, 4), maka 4 = a(0-2)^2 + 8 => 4 = 4a + 8 => 4a = -4 => a = -1. Fungsi: y = -1(x-2)^2 + 8 = -(x^2 - 4x + 4) + 8 = -x^2 + 4x - 4 + 8 = -x^2 + 4x + 4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b59a70b59fbc85113632861e459563f16ab1dbc995218eac234cf202a8e9f580`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2888 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2871 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2865 |

Run 1 — solusi: Titik puncak (h, k) = (2, 8), maka y = a(x-2)^2 + 8. Melalui (0, 4), maka 4 = a(0-2)^2 + 8 => 4 = 4a + 8 => 4a = -4 => a = -1. Fungsi: y = -1(x-2)^2 + 8 = -(x^2 - 4x + 4) + 8 = -x^2 + 4x - 4 + 8 = -x^2 + 4x + 4.
- Domain kognitif `classify/applying`: Siswa perlu mengonstruksi model fungsi kuadrat dari informasi titik puncak dan titik potong sumbu y, kemudian melakukan manipulasi aljabar untuk mengubah bentuk vertex ke bentuk umum. Ini adalah penerapan konsep fungsi kuadrat pada konteks rutin.. Bukti: mencapai ketinggian maksimum 8 m setelah dua detik; dilemparkan dari ketinggian awal 4 m; Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang bentuk vertex fungsi kuadrat dan prosedur aljabar untuk menjabarkan persamaan.. Bukti: fungsi kuadrat tinggi bola; bentuk umum y = ax^2+bx+c
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah utama: menentukan parameter fungsi dari titik puncak dan titik bantu, serta melakukan ekspansi aljabar. Siswa harus memahami hubungan antara titik puncak (2,8) dan bentuk vertex, serta melakukan substitusi untuk mencari nilai 'a'.. Bukti: ketinggian awal 4 m; ketinggian maksimum 8 m setelah dua detik; Nyatakan fungsi kuadrat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk vertex fungsi kuadrat y=a(x-h)^2+k dan substitusi titik. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengonstruksi fungsi kuadrat dari titik puncak dan satu titik lain. Langkah-langkahnya terstruktur dan prosedural. |

Run 2 — solusi: Titik puncak (h, k) = (2, 8), maka y = a(x-2)^2 + 8. Melalui (0, 4), maka 4 = a(0-2)^2 + 8 => 4 = 4a + 8 => 4a = -4 => a = -1. Fungsi: y = -1(x-2)^2 + 8 = -(x^2 - 4x + 4) + 8 = -x^2 + 4x - 4 + 8 = -x^2 + 4x + 4.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan informasi titik puncak dan titik potong sumbu-y ke dalam bentuk vertex, lalu melakukan manipulasi aljabar untuk mengubahnya ke bentuk umum. Ini adalah penerapan konsep fungsi kuadrat yang rutin.. Bukti: mencapai ketinggian maksimum 8 m setelah dua detik; ketinggian awal 4 m; Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum y = ax^2+bx+c
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara titik puncak, titik potong, dan bentuk aljabar fungsi kuadrat.. Bukti: fungsi kuadrat tinggi bola; bentuk umum y = ax^2+bx+c
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah utama: menentukan persamaan dari titik puncak (vertex form) dan melakukan konversi aljabar ke bentuk umum. Siswa harus mengintegrasikan informasi titik puncak (2,8) dan titik awal (0,4) untuk menemukan parameter 'a'.. Bukti: ketinggian awal 4 m; ketinggian maksimum 8 m setelah dua detik; bentuk umum y = ax^2+bx+c

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk vertex fungsi kuadrat y=a(x-h)^2+k dan substitusi titik. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu memodelkan masalah kontekstual sederhana menggunakan fungsi kuadrat. Langkah-langkahnya standar namun memerlukan ketelitian dalam manipulasi aljabar. |

Run 3 — solusi: Titik puncak (h, k) = (2, 8), maka y = a(x-2)^2 + 8. Melalui (0, 4), maka 4 = a(0-2)^2 + 8 => 4 = 4a + 8 => 4a = -4 => a = -1. Fungsi: y = -1(x-2)^2 + 8 = -(x^2 - 4x + 4) + 8 = -x^2 + 4x - 4 + 8 = -x^2 + 4x + 4.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan informasi titik puncak dan titik potong sumbu-y ke dalam bentuk vertex, lalu melakukan manipulasi aljabar untuk mengubahnya ke bentuk umum. Ini adalah penerapan prosedur yang rutin namun memerlukan integrasi beberapa informasi.. Bukti: mencapai ketinggian maksimum 8 m setelah dua detik; ketinggian awal 4 m; Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara titik puncak parabola dengan bentuk vertex fungsi kuadrat dan bagaimana mengonversinya ke bentuk standar.. Bukti: bentuk umum y = ax^2+bx+c; ketinggian maksimum 8 m setelah dua detik
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah utama: menentukan persamaan dari titik puncak dan titik potong, serta melakukan ekspansi aljabar. Siswa harus mengintegrasikan dua informasi (titik puncak dan titik awal) untuk menemukan parameter 'a', yang merupakan proses standar namun membutuhkan ketelitian.. Bukti: ketinggian awal 4 m; mencapai ketinggian maksimum 8 m setelah dua detik; Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk vertex fungsi kuadrat y=a(x-h)^2+k dan substitusi titik. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu memodelkan situasi fisik sederhana ke dalam fungsi kuadrat. Langkah-langkahnya jelas dan prosedural. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah bola dilemparkan dari ketinggian awal 4 m dan mencapai ketinggian maksimum 8 m setelah dua detik sejak dilempar.

Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum $y = ax^2+bx+c$.
Pilihan: A. $y = -x^2 - 4x + 4$
B. $y = x^2 - 4x + 4$
C. $y = -x^2 + 4x + 4$
D. $y = -x^2 + 4x + 8$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 10 kali pengangkutan |
| B | 11 kali pengangkutan |
| C | 9,45 kali pengangkutan |
| D | 9 kali pengangkutan |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Kapasitas muatan bersih = 2000 kg - 150 kg = 1850 kg. Kapasitas kotak per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Jumlah pengangkutan = 350 kotak / 37 kotak/angkut ≈ 9,46. Karena harus mengangkut semua kotak, maka dibulatkan ke atas menjadi 10 kali pengangkutan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d7812094205b628af09852d40f2144ac56a7739fe935a4713555b3ab5f90cece`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3376 |
| 2 | success | valid / verified | applying | procedural | Medium | 3814 |
| 3 | success | valid / verified | applying | procedural | Medium | 4492 |

Run 1 — solusi: Kapasitas muatan bersih = 2000 kg - 150 kg = 1850 kg. Kapasitas kotak per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Jumlah pengangkutan = 350 kotak / 37 kotak/angkut ≈ 9,46. Karena harus mengangkut semua kotak, maka dibulatkan ke atas menjadi 10 kali pengangkutan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aritmetika dasar dan konsep pertidaksamaan dalam konteks dunia nyata untuk menentukan jumlah pengangkutan yang diperlukan.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menggunakan metode perhitungan standar (pengurangan, pembagian, dan pembulatan) untuk menyelesaikan masalah kontekstual.. Bukti: berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang melibatkan langkah-langkah aritmetika dasar yang saling terkait. Siswa hanya perlu memahami batasan kapasitas dan melakukan pembulatan ke atas, yang merupakan keterampilan standar kelas 10.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini adalah penerapan langsung dari pertidaksamaan linear satu variabel yang sering ditemui di kelas 10. Tidak ada tuntutan perencanaan yang kompleks atau integrasi konsep yang sulit. |

Run 2 — solusi: 1. Kapasitas muatan bersih = 2.000 kg - 150 kg = 1.850 kg. 2. Kapasitas kotak per angkut = 1.850 kg / 50 kg/kotak = 37 kotak. 3. Banyak pengangkutan = 350 kotak / 37 kotak/angkut ≈ 9,46. 4. Karena pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika (pembagian dengan pembulatan) dan menerapkan prosedur aritmetika untuk menentukan jumlah pengangkutan. Ini adalah penerapan konsep dalam konteks rutin.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Pengemudi dan kernek memiliki berat total 150 kg; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg; Jika mobil pick up harus membawa 350 kotak
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural (aritmetika dasar dan pembulatan ke atas dalam konteks masalah nyata) untuk menyelesaikan masalah.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Jika mobil pick up harus membawa 350 kotak
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah logis (menghitung sisa kapasitas, menentukan kapasitas per angkut, membagi total kotak, dan melakukan pembulatan ke atas yang logis). Siswa harus mengintegrasikan kendala berat pengemudi dan kapasitas muatan secara tepat.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Pengemudi dan kernek memiliki berat total 150 kg; Jika mobil pick up harus membawa 350 kotak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal memerlukan pemahaman tentang kendala fisik (kapasitas muatan) dan interpretasi hasil pembagian dalam konteks dunia nyata (pembulatan ke atas untuk sisa muatan), yang sesuai untuk kelas 10. |

Run 3 — solusi: Kapasitas muatan kotak per trip = (2000 - 150) / 50 = 37 kotak. Total trip = 350 / 37 = 9,459. Karena trip harus bilangan bulat, maka diperlukan 10 kali pengangkutan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pertidaksamaan linear satu variabel untuk menentukan kapasitas muatan per trip dan membagi total kotak dengan kapasitas tersebut, kemudian melakukan pembulatan ke atas sesuai konteks masalah.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Pengemudi dan kernek memiliki berat total 150 kg; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg; Jika mobil pick up harus membawa 350 kotak
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmetika dan pemahaman pertidaksamaan untuk memodelkan masalah nyata ke dalam bentuk matematika sederhana.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg; berapa kali pengangkutan kotak yang harus dilakukan
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konteks (pengurangan berat pengemudi) dan interpretasi hasil pembagian (pembulatan ke atas). Meskipun prosedurnya rutin, siswa harus membuat keputusan logis berdasarkan kendala fisik (kapasitas).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Pengemudi dan kernek memiliki berat total 150 kg; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg; berapa kali pengangkutan kotak yang harus dilakukan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman konsep pertidaksamaan linear satu variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu memodelkan masalah sehari-hari ke dalam pertidaksamaan linear. Langkah-langkahnya logis dan terstruktur, namun memerlukan ketelitian dalam interpretasi hasil akhir. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4815`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur aritmetika dasar dan konsep pertidaksamaan dalam konteks dunia nyata untuk menentukan jumlah pengangkutan yang diperlukan. Ini adalah penerapan konsep dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji kemampuan siswa dalam menggunakan metode perhitungan standar (pengurangan, pembagian, dan pembulatan) untuk menyelesaikan masalah kontekstual.
- Intended difficulty `Easy`: Soal ini merupakan masalah rutin yang melibatkan langkah-langkah aritmetika dasar yang saling terkait. Siswa hanya perlu memahami batasan kapasitas dan melakukan pembulatan ke atas, yang merupakan keterampilan standar kelas 10.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini adalah penerapan langsung dari pertidaksamaan linear satu variabel yang sering ditemui di kelas 10. Tidak ada tuntutan perencanaan yang kompleks atau integrasi konsep yang sulit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.

Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
Pilihan: A. 10 kali pengangkutan
B. 11 kali pengangkutan
C. 9,45 kali pengangkutan
D. 9 kali pengangkutan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| B | 12! = 479.001.600 |
| C | 12 |
| D | 12 x 12 = 144 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `094f3237ffb617f0f2ee0ff4debde74d587c330d368c67b9c97d592f241a4de6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2942 |
| 2 | success | valid / verified | applying | procedural | Easy | 2896 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2914 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan rumus faktorial (n!) untuk menentukan banyaknya korespondensi satu-satu antara dua himpunan dengan jumlah anggota yang sama. Siswa hanya perlu mengenali konsep dasar korespondensi satu-satu dan menerapkan prosedur perhitungan faktorial.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural mengenai rumus dasar korespondensi satu-satu (n!) pada himpunan berhingga.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari rumus faktorial untuk korespondensi satu-satu. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks; siswa hanya perlu mengetahui bahwa n(A)=n(B)=n berakibat banyaknya korespondensi adalah n!.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! cukup besar, konsep yang diuji adalah prosedur standar yang familiar bagi siswa kelas 10 yang mempelajari materi ini. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan dengan jumlah anggota yang sama. Ini adalah penerapan langsung dari konsep dasar korespondensi satu-satu.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip dasar korespondensi satu-satu dan bagaimana menghitungnya menggunakan faktorial, yang merupakan konsep prosedural dalam kombinatorika dasar.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks; siswa hanya perlu mengingat dan menerapkan rumus n!.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! cukup besar, konsep dasarnya adalah materi standar kelas 10. Soal tidak menuntut penalaran mendalam, hanya pengenalan rumus. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama. Siswa hanya perlu mengenali konsep dasar korespondensi satu-satu dan menerapkan prosedur perhitungan faktorial yang sudah dipelajari.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus faktorial untuk menghitung permutasi atau korespondensi satu-satu pada himpunan berhingga.. Bukti: n(A) = n(B) = 12; banyak korespondensi satu-satu yang mungkin
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari rumus faktorial (n!) untuk korespondensi satu-satu. Tidak ada langkah perencanaan yang kompleks, kendala yang berinteraksi, atau kebutuhan untuk membangun model. Siswa hanya perlu mengetahui bahwa untuk n=12, jawabannya adalah 12!.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar himpunan dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah materi standar kelas 10. Soal ini tidak memerlukan penalaran tingkat tinggi, hanya pengingatan rumus. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4686`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk menerapkan rumus faktorial (n!) untuk menentukan banyaknya korespondensi satu-satu antara dua himpunan dengan jumlah anggota yang sama. Siswa hanya perlu mengenali konsep dasar korespondensi satu-satu dan menerapkan prosedur perhitungan faktorial.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural mengenai rumus dasar korespondensi satu-satu (n!) pada himpunan berhingga.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari rumus faktorial untuk korespondensi satu-satu. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks; siswa hanya perlu mengetahui bahwa n(A)=n(B)=n berakibat banyaknya korespondensi adalah n!.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! cukup besar, konsep yang diuji adalah prosedur standar yang familiar bagi siswa kelas 10 yang mempelajari materi ini. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Korespondensi Satu-satu (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12

Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
Pilihan: A. 12 + 11 + 10 + ... + 2 + 1 = 78
B. 12! = 479.001.600
C. 12
D. 12 x 12 = 144
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `3b808934c13bf0822544d6d6`

1. Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998. Untuk dapat memahami diagram dengan lebih baik, kamu perlu memahami situasi dan konteks dari diagram.<br><br>Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

| Opsi | Isi |
|---|---|
| A | 6 pelari |
| B | 10 pelari |
| C | 4 pelari |
| D | 8 pelari |

![Gambar sumber soal 33](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identifikasi batang pada diagram yang tingginya berada di antara garis 30 dan 35 (mewakili interval 31:00-32:59). Batang tersebut adalah Estonia 2, Japan, Kazakhstan, Latvia, Slovakia, Spain 1, Spain 2, dan U.S 2. Total terdapat 8 batang.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png. Transkripsi visual: Diagram batang menunjukkan waktu tempuh (sumbu y, 0-45 menit) untuk berbagai negara (sumbu x). Batang yang memiliki tinggi antara 31 dan 33 (mewakili interval 31:00-32:59) adalah: Estonia 2 (sedikit di atas 30), Japan (tepat 30), Kazakhstan (sedikit di atas 30), Latvia (sedikit di atas 30), Slovakia (sedikit di atas 30), Spain 1 (tepat 30), Spain 2 (sedikit di atas 30), U.S 2 (tepat 30). Total ada 8 batang yang berada di rentang tersebut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0e0133ee8be345c897142f786d155fffcb4e092239ca9a973206ffd51381015d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3938 |
| 2 | success | valid / verified | knowing | factual | Easy | 4215 |
| 3 | success | valid / verified | knowing | factual | Easy | 3860 |

Run 1 — solusi: Identifikasi batang pada diagram yang tingginya berada di antara garis 30 dan 35 (mewakili interval 31:00-32:59). Batang tersebut adalah Estonia 2, Japan, Kazakhstan, Latvia, Slovakia, Spain 1, Spain 2, dan U.S 2. Total terdapat 8 batang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari diagram batang dan mencocokkan tinggi batang dengan interval yang diberikan. Ini adalah proses pengambilan informasi langsung.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan dasar dalam membaca dan menginterpretasikan representasi data visual (diagram batang).. Bukti: Perhatikan diagram batang berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu melakukan pencacahan sederhana berdasarkan kriteria visual yang jelas. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca diagram batang adalah keterampilan dasar yang sudah dikuasai siswa sebelum kelas 10. Soal ini tidak menuntut analisis data yang mendalam. |

Run 2 — solusi: Identifikasi batang pada diagram yang memiliki tinggi antara 31 dan 33 (mewakili interval 31:00-32:59). Batang tersebut adalah: Estonia 2, Japan, Latvia, Slovakia, Spain 1, Spain 2, Ukraine, dan U.S 2. Terdapat 8 batang yang memenuhi kriteria tersebut.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari diagram batang dan mencocokkan tinggi batang dengan interval yang diberikan. Ini adalah prosedur langsung.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan membaca dan menginterpretasikan data dari representasi visual (diagram batang), yang merupakan pengetahuan faktual tentang cara membaca grafik.. Bukti: Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (Easy). Siswa hanya perlu melakukan pencacahan visual sederhana pada diagram batang tanpa perlu melakukan perhitungan kompleks atau analisis mendalam.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membaca diagram batang adalah keterampilan dasar yang sudah dikuasai siswa kelas 10. |

Run 3 — solusi: Identifikasi batang dengan tinggi antara 30 dan 35 pada sumbu y. Batang tersebut adalah Estonia 2, Japan, Latvia, Slovakia, Spain 1, Spain 2, Ukraine, dan U.S. 2. Jumlahnya adalah 8.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram batang dan melakukan pencacahan sederhana berdasarkan kriteria interval yang diberikan. Ini adalah proses pengambilan informasi langsung.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan dasar dalam membaca dan menginterpretasikan representasi data visual (diagram batang).. Bukti: Perhatikan diagram batang berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi batang yang tingginya berada di antara 30 dan 35 pada sumbu y. Tidak ada manipulasi data atau langkah kompleks yang diperlukan.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca skala pada diagram batang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membaca diagram batang adalah keterampilan dasar yang sudah dikuasai siswa kelas 10. Soal tidak menuntut analisis statistik atau interpretasi mendalam. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data
Tipe soal: multiple_choice
Stimulus: -
Soal: 1. Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998. Untuk dapat memahami diagram dengan lebih baik, kamu perlu memahami situasi dan konteks dari diagram.

Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
Pilihan: A. 6 pelari
B. 10 pelari
C. 4 pelari
D. 8 pelari
Transkripsi visual: Diagram batang menunjukkan waktu tempuh (sumbu y, 0-45 menit) untuk berbagai negara (sumbu x). Batang yang memiliki tinggi antara 31 dan 33 (mewakili interval 31:00-32:59) adalah: Estonia 2 (sedikit di atas 30), Japan (tepat 30), Kazakhstan (sedikit di atas 30), Latvia (sedikit di atas 30), Slovakia (sedikit di atas 30), Spain 1 (tepat 30), Spain 2 (sedikit di atas 30), U.S 2 (tepat 30). Total ada 8 batang yang berada di rentang tersebut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `e9d27eefa537bb209c6d3b40`

Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998<br><br>Dari Gambar 6.4, ada berapa atlet yang berpartisipasi dalam cabang lintas alam? Ada berapa negara yang berpartisipasi dalam cabang ini?

| Opsi | Isi |
|---|---|
| A | 20 atlet; 25 negara |
| B | 25 atlet; 20 negara |
| C | 25 atlet; 25 negara |
| D | 24 atlet; 20 negara |

![Gambar sumber soal 34](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung negara unik dari label sumbu horizontal: Austria, Canada, Czech Republic, Estonia, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Norway, Russia, Slovakia, Spain, Ukraine, U.S. Total ada 20 negara unik.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png. Transkripsi visual: Diagram batang menunjukkan waktu tempuh peserta Lintas Alam Olimpiade 1998. Sumbu horizontal berisi label negara peserta: Austria 1, Austria 2, Canada, Czech Republic, Estonia 1, Estonia 2, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Norway 1, Norway 2, Russia, Slovakia, Spain 1, Spain 2, Ukraine, U.S 1, U.S 2. Terdapat 25 batang total. Negara yang muncul dua kali adalah Austria, Estonia, Norway, Spain, U.S (5 negara).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `259054e90d5fbb06bff3d915cf27c250e32578d11eaafa4fec966c1b6fe4ac78`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3961 |
| 2 | success | valid / verified | applying | conceptual | Medium | 4032 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3990 |

Run 1 — solusi: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung negara unik dari label sumbu horizontal: Austria, Canada, Czech Republic, Estonia, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Norway, Russia, Slovakia, Spain, Ukraine, U.S. Total ada 20 negara unik.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasi diagram batang untuk menghitung frekuensi total (jumlah batang) dan mengidentifikasi kategori unik (jumlah negara) dari label yang diberikan, yang merupakan penerapan konsep dasar membaca data.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data dikategorikan dan disajikan dalam diagram batang, serta kemampuan membedakan antara jumlah entri data dan jumlah kategori unik.. Bukti: Perhatikan diagram batang berikut; Ada berapa negara yang berpartisipasi
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut ketelitian dalam membedakan antara jumlah batang (atlet) dan jumlah kategori unik (negara). Siswa tidak bisa sekadar menghitung total batang, tetapi harus melakukan langkah tambahan untuk mengelompokkan label negara yang sama.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan memahami konsep kategori data. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan analisis data sederhana. Tantangan utama adalah ketelitian dalam mengidentifikasi negara yang muncul dua kali, yang memerlukan perhatian lebih daripada sekadar menghitung total batang. |

Run 2 — solusi: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung negara unik pada sumbu X. Negara yang muncul dua kali (Austria, Estonia, Norway, Spain, U.S) dihitung sebagai 1 negara per pasang. Total negara = 25 batang - 5 duplikasi = 20 negara.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan diagram batang untuk menghitung frekuensi total (jumlah atlet) dan mengidentifikasi kategori unik (jumlah negara) dengan memperhatikan label yang berulang.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data dikategorikan dalam diagram batang, khususnya membedakan antara jumlah entri data (atlet) dan jumlah kategori unik (negara).. Bukti: Perhatikan diagram batang berikut; Ada berapa negara yang berpartisipasi
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut ketelitian dalam membedakan antara jumlah batang (atlet) dan jumlah kategori unik (negara). Siswa harus melakukan dua langkah pemrosesan data yang berbeda dan tidak sekadar membaca angka langsung, namun prosedurnya tetap familiar.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan memahami konsep kategori data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menginterpretasikan data statistik dasar. Tantangan utama adalah ketelitian dalam mengidentifikasi duplikasi label negara, yang merupakan tugas analisis data rutin namun memerlukan perhatian pada detail. |

Run 3 — solusi: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung negara unik dengan mengabaikan duplikasi (Austria, Estonia, Norway, Spain, U.S masing-masing muncul 2 kali). Total negara = 25 - 5 = 20 negara. Jawaban: 25 atlet dan 20 negara.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menginterpretasikan diagram batang secara langsung. Siswa perlu menghitung jumlah batang (atlet) dan mengidentifikasi label unik pada sumbu horizontal (negara) untuk menentukan jumlah negara yang berpartisipasi. Ini adalah penerapan konsep membaca data.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pengetahuan konseptual tentang bagaimana data direpresentasikan dalam diagram batang dan bagaimana menginterpretasikan label pada sumbu untuk menghitung frekuensi unik.. Bukti: Perhatikan diagram batang berikut; Ada berapa negara yang berpartisipasi dalam cabang ini?
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut ketelitian dalam membedakan antara jumlah entitas (batang) dan jumlah kategori unik (negara). Siswa tidak bisa hanya menghitung jumlah label secara naif, tetapi harus mengenali duplikasi label pada sumbu horizontal.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan memahami konsep data unik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan Medium sesuai untuk kelas 10 karena menuntut ketelitian ekstra dalam memproses data visual (membedakan atlet vs negara) yang sering menjadi jebakan dalam interpretasi data. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998

Dari Gambar 6.4, ada berapa atlet yang berpartisipasi dalam cabang lintas alam? Ada berapa negara yang berpartisipasi dalam cabang ini?
Pilihan: A. 20 atlet; 25 negara
B. 25 atlet; 20 negara
C. 25 atlet; 25 negara
D. 24 atlet; 20 negara
Transkripsi visual: Diagram batang menunjukkan waktu tempuh peserta Lintas Alam Olimpiade 1998. Sumbu horizontal berisi label negara peserta: Austria 1, Austria 2, Canada, Czech Republic, Estonia 1, Estonia 2, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Norway 1, Norway 2, Russia, Slovakia, Spain 1, Spain 2, Ukraine, U.S 1, U.S 2. Terdapat 25 batang total. Negara yang muncul dua kali adalah Austria, Estonia, Norway, Spain, U.S (5 negara).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `ff85b5a87bfa58eb3957ceb3`

Jika data penjualan sepatu di toko A pada Tabel kita ubah menjadi tabel Frekuensi data tunggal sebagai berikut. Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A \| Ukuran: 38, 39, 40, 41, 42, 43, 44, 45, 46 \| Frekuensi: 1, 1, 2, 4, 5, 7, 7, 2, 1<br><br>Tentukanlah modus, median, dan mean dari kumpulan data di atas.

| Opsi | Isi |
|---|---|
| A | Modus = 43 dan 44, median = 42, mean = 42,5 |
| B | Modus = 43 dan 44, median = 43, mean = 42 |
| C | Modus = 7, median = 43, mean = 42,5 |
| D | Modus = 43 dan 44, median = 43, mean = 42,5 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Total data N = 30. Modus: nilai dengan frekuensi tertinggi (7) adalah 43 dan 44. Median: rata-rata data ke-15 dan ke-16. Data ke-15 dan ke-16 berada pada ukuran 43 (kumulatif frekuensi: 1+1+2+4+5=13, data ke-14 s.d. 20 adalah 43). Mean: (38*1 + 39*1 + 40*2 + 41*4 + 42*5 + 43*7 + 44*7 + 45*2 + 46*1) / 30 = 1275 / 30 = 42,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e272a655d565b84e90d270226e21e3de60457b1b21c78ffea13fe3522a1b7952`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3009 |
| 2 | success | valid / verified | applying | procedural | Easy | 2990 |
| 3 | success | valid / verified | applying | procedural | Easy | 2970 |

Run 1 — solusi: Total data N = 30. Modus: nilai dengan frekuensi tertinggi (7) adalah 43 dan 44. Median: rata-rata data ke-15 dan ke-16. Data ke-15 dan ke-16 berada pada ukuran 43 (kumulatif frekuensi: 1+1+2+4+5=13, data ke-14 s.d. 20 adalah 43). Mean: (38*1 + 39*1 + 40*2 + 41*4 + 42*5 + 43*7 + 44*7 + 45*2 + 46*1) / 30 = 1275 / 30 = 42,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar (menghitung mean, median, modus) pada data yang disajikan dalam tabel frekuensi. Ini adalah penerapan rutin dari konsep statistik deskriptif.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan metode perhitungan statistik deskriptif (mean, median, modus) pada data berkelompok sederhana.. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur perhitungan mean, median, dan modus pada tabel frekuensi adalah materi dasar yang familiar. Langkah-langkahnya jelas, tidak ada kendala yang berinteraksi secara kompleks, dan beban perhitungan moderat.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang mean, median, modus dan cara membaca tabel frekuensi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 9 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan sudah menguasai statistik deskriptif dasar ini. Soal tidak menuntut analisis mendalam atau integrasi konsep yang kompleks. |

Run 2 — solusi: Total data N = 30. Modus: nilai dengan frekuensi tertinggi (7) adalah 43 dan 44. Median: rata-rata data ke-15 dan ke-16. Data ke-15 ada di ukuran 43, data ke-16 ada di ukuran 43. Median = (43+43)/2 = 43. Mean: (38*1 + 39*1 + 40*2 + 41*4 + 42*5 + 43*7 + 44*7 + 45*2 + 46*1) / 30 = 1275 / 30 = 42,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar (mean, median, modus) pada data yang disajikan dalam tabel frekuensi. Ini adalah penerapan langsung dari definisi dan algoritma statistik.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perhitungan statistik (prosedural) dan konsep dasar ukuran pemusatan data (konseptual).. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengikuti prosedur standar untuk menghitung mean, median, dan modus dari tabel frekuensi. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang mean, median, modus, dan cara membaca tabel frekuensi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 9 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif adalah materi standar kelas 10. Perhitungan mean, median, dan modus dari tabel frekuensi adalah prosedur rutin yang diharapkan dikuasai siswa. |

Run 3 — solusi: Total data n = 1+1+2+4+5+7+7+2+1 = 30. Modus adalah ukuran dengan frekuensi tertinggi (7), yaitu 43 dan 44. Median adalah rata-rata data ke-15 dan ke-16. Data ke-15 dan ke-16 berada pada ukuran 43 (kumulatif frekuensi sampai 42 adalah 1+1+2+4+5=13, data ke-14 sampai ke-20 adalah 43). Mean = (38*1+39*1+40*2+41*4+42*5+43*7+44*7+45*2+46*1)/30 = 1275/30 = 42,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar (mean, median, modus) pada data yang disajikan dalam tabel frekuensi. Ini adalah penerapan rutin dari konsep statistik deskriptif.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan metode perhitungan statistik deskriptif (mean, median, modus) pada data berkelompok sederhana.. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengikuti prosedur standar untuk menghitung mean, median, dan modus dari tabel frekuensi. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang mean, median, modus, dan cara membaca tabel frekuensi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 9 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi statistik deskriptif adalah materi dasar kelas 10. Perhitungan mean, median, dan modus dari tabel frekuensi adalah prosedur standar yang familiar. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Statistik Deskriptif
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika data penjualan sepatu di toko A pada Tabel kita ubah menjadi tabel Frekuensi data tunggal sebagai berikut. Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A | Ukuran: 38, 39, 40, 41, 42, 43, 44, 45, 46 | Frekuensi: 1, 1, 2, 4, 5, 7, 7, 2, 1

Tentukanlah modus, median, dan mean dari kumpulan data di atas.
Pilihan: A. Modus = 43 dan 44, median = 42, mean = 42,5
B. Modus = 43 dan 44, median = 43, mean = 42
C. Modus = 7, median = 43, mean = 42,5
D. Modus = 43 dan 44, median = 43, mean = 42,5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `2de15d728d070fae8af5319c`

Data berikut menunjukkan jumlah kue yang dijual melalui situs online setiap harinya: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0<br><br>Tentukanlah modus dan median dari data di atas.

| Opsi | Isi |
|---|---|
| A | Modus = 4, median = 3 |
| B | Modus = 0, median = 3,5 |
| C | Modus = 0, median = 3 |
| D | Modus = 0, median = 2 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Data diurutkan: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7. Modus adalah nilai dengan frekuensi tertinggi, yaitu 0 (muncul 4 kali). Karena jumlah data n=16 (genap), median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a9dcf3803bb7d9fa123a15fb82d534fc4c3f597e248fbbfbf7f12975464fdba5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2814 |
| 2 | success | valid / verified | knowing | procedural | Easy | 4037 |
| 3 | success | valid / verified | applying | procedural | Easy | 2860 |

Run 1 — solusi: Data diurutkan: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7. Frekuensi 0 adalah 4 kali (terbanyak), maka modus = 0. Data berjumlah 16 (genap), median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menentukan modus dan median dari sekumpulan data yang diberikan. Ini adalah penerapan konsep statistik dasar yang rutin.. Bukti: Tentukanlah modus dan median dari data di atas.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan prosedur perhitungan modus serta median (konsep statistik deskriptif).. Bukti: Data berikut menunjukkan jumlah kue yang dijual melalui situs online setiap harinya: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengurutkan data dan menerapkan definisi modus serta median. Tidak ada kendala kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukanlah modus dan median dari data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang modus dan median, serta kemampuan mengurutkan data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 16 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (modus, median) adalah materi dasar yang sudah dipelajari sebelum kelas 10. Soal ini menguji prosedur dasar tanpa kerumitan tambahan. |

Run 2 — solusi: Data diurutkan: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7. Modus adalah nilai yang paling sering muncul, yaitu 0 (muncul 4 kali). Karena jumlah data (n=16) genap, median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan prosedur standar untuk menentukan modus dan median dari sekumpulan data kecil yang diberikan tanpa memerlukan strategi nonrutin.. Bukti: Tentukanlah modus dan median dari data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengurutkan data dan menghitung statistik deskriptif dasar.. Bukti: Tentukanlah modus dan median dari data di atas.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jumlah data yang kecil (16). Tidak ada kendala kompleks atau interpretasi yang sulit. Siswa hanya perlu mengurutkan data dan menerapkan rumus median untuk data genap.. Bukti: Data berikut menunjukkan jumlah kue yang dijual melalui situs online setiap harinya: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi modus dan median, serta cara mengurutkan data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 16 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif dasar (modus dan median) adalah materi standar kelas 10 yang bersifat prosedural dan rutin. |

Run 3 — solusi: Data diurutkan: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7. Modus adalah nilai yang paling sering muncul, yaitu 0 (muncul 4 kali). Karena jumlah data n=16 (genap), median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar untuk menentukan modus dan median dari sekumpulan data yang diberikan. Ini adalah penerapan langsung dari definisi dan prosedur statistik deskriptif.. Bukti: Tentukanlah modus dan median dari data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang konsep statistik (modus dan median) dan prosedur untuk menghitungnya dari data mentah.. Bukti: Data berikut menunjukkan jumlah kue yang dijual melalui situs online setiap harinya: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengurutkan data dan menerapkan rumus median untuk n genap serta mengidentifikasi frekuensi tertinggi untuk modus. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukanlah modus dan median dari data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pengurutan data, konsep modus, dan median untuk data genap. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 16 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (modus, median) adalah materi dasar yang sudah dipelajari di jenjang SMP dan merupakan bagian dari kurikulum kelas 10. Prosedur penyelesaian sangat standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4446`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur standar untuk menentukan modus dan median dari sekumpulan data yang diberikan. Ini adalah penerapan konsep statistik dasar yang rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang cara mengurutkan data dan menghitung statistik deskriptif dasar (modus dan median).
- Intended difficulty `Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengurutkan data dan menerapkan definisi modus serta median untuk data genap. Tidak ada kendala kompleks atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang modus dan median, serta kemampuan mengurutkan data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 16 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (modus, median) adalah materi dasar yang sudah dipelajari sebelum kelas 10. Soal ini menguji prosedur dasar tanpa kerumitan tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Statistik Deskriptif
Tipe soal: multiple_choice
Stimulus: -
Soal: Data berikut menunjukkan jumlah kue yang dijual melalui situs online setiap harinya: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0

Tentukanlah modus dan median dari data di atas.
Pilihan: A. Modus = 4, median = 3
B. Modus = 0, median = 3,5
C. Modus = 0, median = 3
D. Modus = 0, median = 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `d6d3b4c5f9819d69d4c859d0`

Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315<br><br>Mengapa angka 750 kWh dapat dianggap sebagai pencilan?

| Opsi | Isi |
|---|---|
| A | Karena 750 kWh lebih dari 1,5 kali median data (315 kWh) |
| B | Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh) |
| C | Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data |
| D | Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Urutkan data: 300, 305, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1,5 * IQR = 320 + 15 = 335. Karena 750 > 335, maka 750 adalah pencilan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2da83515669618c8c1a9e1a1959149b8b0eeb6f11df31152fe45471acc9a24af`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2947 |
| 2 | success | valid / verified | applying | procedural | Medium | 2950 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2982 |

Run 1 — solusi: Urutkan data: 300, 305, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1,5 * IQR = 320 + 15 = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik formal (menghitung kuartil dan batas pencilan) untuk memvalidasi klaim, bukan sekadar intuisi.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang cara menentukan pencilan menggunakan metode IQR yang merupakan standar statistik.. Bukti: batas atas IQR (335 kWh)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan serangkaian langkah prosedural (mengurutkan data, mencari Q1, Q3, IQR, dan batas atas) yang saling bergantung. Meskipun prosedurnya rutin, terdapat beberapa langkah yang harus dilakukan dengan teliti.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang kuartil, jangkauan interkuartil (IQR), dan kriteria pencilan statistik. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengolah data statistik deskriptif sederhana. Langkah-langkahnya terstruktur namun memerlukan ketelitian dalam perhitungan kuartil. |

Run 2 — solusi: Data terurut: 300, 305, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1,5 * IQR = 320 + 15 = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik standar untuk menentukan pencilan menggunakan aturan IQR (Q3 + 1,5*IQR). Ini adalah penerapan konsep statistik yang rutin dalam kurikulum kelas 10.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang prosedur statistik untuk mendeteksi pencilan (outlier) menggunakan kuartil dan IQR.. Bukti: Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah terstruktur: mengurutkan data, mencari kuartil, menghitung IQR, dan menerapkan rumus batas atas. Meskipun prosedurnya familiar, siswa harus melakukan perhitungan yang saling terkait secara akurat.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; Mengapa angka 750 kWh dapat dianggap sebagai pencilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang kuartil, IQR, dan definisi pencilan statistik. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengolah data statistik dasar. Langkah-langkahnya jelas namun memerlukan ketelitian dalam perhitungan kuartil dan batas pencilan. |

Run 3 — solusi: Data terurut: 300, 305, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = 320 - 310 = 10. Batas atas = Q3 + 1,5 * IQR = 320 + 15 = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik standar untuk mendeteksi pencilan (outlier) menggunakan aturan IQR (Interquartile Range). Ini melibatkan pengurutan data, penentuan kuartil, perhitungan IQR, dan penentuan batas atas, yang merupakan penerapan konsep statistik deskriptif.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip statistik mengenai definisi pencilan dan prosedur perhitungan batas atas menggunakan kuartil.. Bukti: Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah prosedural yang saling terkait (mengurutkan data, mencari Q1 dan Q3, menghitung IQR, menghitung batas atas, dan membandingkan). Meskipun prosedurnya rutin, siswa harus melakukan perhitungan berjenjang dengan cermat.. Bukti: data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang kuartil, IQR, dan kriteria pencilan statistik. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan analisis statistik deskriptif dasar termasuk deteksi pencilan menggunakan aturan 1,5 x IQR. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4905`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur statistik standar untuk mendeteksi pencilan menggunakan aturan IQR (Q3 + 1,5*IQR). Ini adalah penerapan konsep statistik yang rutin dalam kurikulum kelas 10.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang cara menentukan pencilan menggunakan metode IQR yang merupakan standar statistik.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan serangkaian langkah prosedural (mengurutkan data, mencari Q1, Q3, IQR, dan batas atas) yang saling bergantung. Meskipun prosedurnya rutin, terdapat beberapa langkah yang harus dilakukan dengan teliti.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang kuartil, jangkauan interkuartil (IQR), dan kriteria pencilan statistik. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengolah data statistik deskriptif sederhana. Langkah-langkahnya terstruktur namun memerlukan ketelitian dalam perhitungan kuartil. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data Lanjutan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315

Mengapa angka 750 kWh dapat dianggap sebagai pencilan?
Pilihan: A. Karena 750 kWh lebih dari 1,5 kali median data (315 kWh)
B. Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh)
C. Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
D. Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `8d43b2c9894a7ba29b09e984`

Perhatikan Box Plot dari data waktu yang diperlukan (dalam menit) untuk pengisian HP dari 0% sampai 100%. Gambar 6.17 Diagram Box-and-Whisker Kecepatan Pengisian HP dari 0 sampai 100%<br><br>Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.

| Opsi | Isi |
|---|---|
| A | Data minimum = 68, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 77 |
| B | Data minimum = 68, Q1 = 72, Q2 = 76, Q3 = 77, data maksimum = 80 |
| C | Data minimum = 68, Q1 = 72, Q2 = 74, Q3 = 76, data maksimum = 80 |
| D | Data minimum = 70, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 80 |

![Gambar sumber soal 38](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0228-02.png>)


![Gambar sumber soal 38](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0228-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Berdasarkan visualisasi box plot: ujung whisker kiri (minimum) berada di 68, tepi kiri kotak (Q1) di 71, garis tengah kotak (Q2/median) di 72, tepi kanan kotak (Q3) di 76, dan ujung whisker kanan (maksimum) di 77.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0228-02.png, images/kelas10_panduan_siswa_kelas10.pdf-0228-03.png. Transkripsi visual: The image shows a box-and-whisker plot aligned with a number line. The number line has markings at 68, 70, 72, 74, 76, and 80. The left whisker starts at 68. The left edge of the box (Q1) aligns with 71. The vertical line inside the box (Q2/median) aligns with 72. The right edge of the box (Q3) aligns with 76. The right whisker ends at 77.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `86e864bfd156f800099b530756a3deca9c1c045beea5f2c54c8f9d0ab050d876`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 5172 |
| 2 | success | valid / verified | knowing | factual | Easy | 6177 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 5146 |

Run 1 — solusi: Identify the five-number summary from the box plot: minimum at the left whisker end (68), first quartile Q1 at the left box edge (71), median Q2 at the internal box line (72), third quartile Q3 at the right box edge (76), and maximum at the right whisker end (77).
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca dan menginterpretasikan komponen statistik deskriptif langsung dari representasi visual (box plot). Tidak ada manipulasi data atau perhitungan kompleks yang diperlukan, hanya pengenalan komponen box plot.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang terminologi dan struktur elemen dasar dalam diagram box-and-whisker (fakta statistik).. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu memetakan posisi visual pada box plot ke skala sumbu yang tersedia. Tidak ada langkah perencanaan atau integrasi konsep yang diperlukan.. Bukti: Perhatikan Box Plot dari data waktu yang diperlukan; Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen box plot (minimum, kuartil, maksimum). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca box plot adalah keterampilan dasar statistik di kelas 10. Soal ini tidak menuntut analisis data, hanya pembacaan grafik. |

Run 2 — solusi: Berdasarkan pembacaan box plot: data minimum (ujung whisker kiri) = 68, Q1 (tepi kiri kotak) = 71, Q2 (median/garis tengah kotak) = 72, Q3 (tepi kanan kotak) = 76, dan data maksimum (ujung whisker kanan) = 77.
- Domain kognitif `classify/knowing`: Siswa hanya diminta untuk mengidentifikasi dan membaca nilai statistik lima serangkai langsung dari representasi visual box plot tanpa perlu melakukan perhitungan atau analisis lanjutan.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai terminologi dan komponen dasar dari diagram box plot.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (membaca grafik). Tidak ada langkah perencanaan, integrasi konsep, atau kendala yang harus dipecahkan. Siswa hanya perlu mengenali komponen box plot.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami definisi dan letak komponen box plot (min, Q1, Q2, Q3, max). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca box plot adalah keterampilan dasar statistik deskriptif yang sudah dipelajari di jenjang sebelumnya dan diperdalam di kelas 10. Soal ini tidak menuntut analisis lebih lanjut. |

Run 3 — solusi: Membaca komponen box plot: ujung whisker kiri (minimum) = 68, tepi kiri kotak (Q1) = 71, garis median (Q2) = 72, tepi kanan kotak (Q3) = 76, ujung whisker kanan (maksimum) = 77.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan membaca nilai statistik lima serangkai langsung dari representasi visual box plot. Tidak ada manipulasi data atau analisis mendalam yang diperlukan, hanya pemahaman definisi komponen box plot.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur dan komponen (konsep) dari diagram box-and-whisker untuk menentukan nilai-nilai yang diminta.. Bukti: Perhatikan Box Plot dari data waktu yang diperlukan; Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu memetakan posisi visual pada box plot ke skala sumbu yang tersedia. Tidak ada langkah kompleks atau integrasi antar konsep.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen box plot (minimum, kuartil, maksimum). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca box plot adalah keterampilan dasar statistik di kelas 10. Soal ini tidak menuntut analisis data, hanya pembacaan grafik. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `6761`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengidentifikasi komponen statistik lima serangkai langsung dari representasi visual box plot. Tidak ada manipulasi data atau analisis mendalam yang diperlukan, hanya pengenalan komponen box plot.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami struktur dan komponen (konsep) dari diagram box-and-whisker untuk menentukan nilai-nilai yang diminta.
- Intended difficulty `Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu memetakan posisi visual pada box plot ke skala sumbu yang tersedia. Tidak ada langkah kompleks atau integrasi antar konsep.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen box plot (minimum, kuartil, maksimum). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca box plot adalah keterampilan dasar statistik di kelas 10. Soal ini tidak menuntut analisis data, hanya pembacaan grafik. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data Lanjutan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan Box Plot dari data waktu yang diperlukan (dalam menit) untuk pengisian HP dari 0% sampai 100%. Gambar 6.17 Diagram Box-and-Whisker Kecepatan Pengisian HP dari 0 sampai 100%

Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
Pilihan: A. Data minimum = 68, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 77
B. Data minimum = 68, Q1 = 72, Q2 = 76, Q3 = 77, data maksimum = 80
C. Data minimum = 68, Q1 = 72, Q2 = 74, Q3 = 76, data maksimum = 80
D. Data minimum = 70, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 80
Transkripsi visual: The image shows a box-and-whisker plot aligned with a number line. The number line has markings at 68, 70, 72, 74, 76, and 80. The left whisker starts at 68. The left edge of the box (Q1) aligns with 71. The vertical line inside the box (Q2/median) aligns with 72. The right edge of the box (Q3) aligns with 76. The right whisker ends at 77.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| B | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |
| C | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 = (65+70)/2 = 67,5. Q1 = median 7 data pertama = 65. Q3 = median 7 data terakhir = 80. Jangkauan kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f549cb50e7cddd99dd052794827865dafae44f78cbb08da4931a28d9cb48693a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 4222 |
| 2 | success | valid / verified | applying | procedural | Easy | 4440 |
| 3 | success | valid / verified | applying | procedural | Easy | 3977 |

Run 1 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 = (65+70)/2 = 67,5. Q1 = median 7 data pertama = 65. Q3 = median 7 data terakhir = 80. Jangkauan kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar untuk menentukan kuartil dan ukuran penyebaran data. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma atau metode statistik untuk mengolah data.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas rutin yang familiar bagi siswa kelas 10. Langkah-langkah penyelesaiannya jelas (mengurutkan data, membagi data, menghitung median, dan menerapkan rumus). Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang median dan pengurutan data. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (kuartil) adalah topik standar kelas 10 yang penyelesaiannya bersifat prosedural langsung. |

Run 2 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q1 adalah median dari 7 data pertama (50, 50, 60, 65, 65, 65, 65) yaitu 65. Q3 adalah median dari 7 data terakhir (70, 75, 80, 80, 85, 85, 90) yaitu 80. Jangkauan antar kuartil = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 15 / 2 = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menentukan kuartil dan ukuran penyebaran data dari sekumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau langkah-langkah prosedural dalam menghitung statistik deskriptif (kuartil dan simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Intended difficulty `classify/Easy`: Soal bersifat rutin dengan langkah-langkah yang jelas dan familiar bagi siswa kelas 10. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang median dan pengurutan data. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas statistik standar yang sesuai dengan kurikulum kelas 10, hanya memerlukan pengurutan data dan penerapan rumus dasar. |

Run 3 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Q1 (median 7 data pertama) = 65. Q3 (median 7 data terakhir) = 80. Jangkauan antar kuartil = Q3 - Q1 = 15. Simpangan kuartil = 15/2 = 7,5.
- Domain kognitif `classify/applying`: Siswa perlu mengurutkan data, membagi data menjadi dua bagian, dan menerapkan prosedur standar untuk mencari kuartil serta simpangan kuartil. Ini adalah penerapan prosedur rutin pada data statistik.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau prosedur statistik untuk menentukan nilai kuartil dan simpangan kuartil dari sekumpulan data.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengurutkan data dan menerapkan rumus kuartil yang sudah dipelajari. Tidak ada kendala kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang median dan pengurutan data. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (kuartil) adalah materi standar kelas 10 yang bersifat prosedural dan rutin. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Penyebaran Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65
Pilihan: A. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
B. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15
C. Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5
D. Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `581df18ab4eeb6c5cf613ab7`

Tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.<br><br>tentukan jumlah yang lebih besar daripada 3

| Opsi | Isi |
|---|---|
| A | $\frac{3}{36}$ |
| B | $\frac{33}{36}$ |
| C | $\frac{35}{36}$ |
| D | $\frac{34}{36}$ |

![Gambar sumber soal 40](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: P(jumlah > 3) = 1 - P(jumlah <= 3). P(jumlah=2) = 1/36, P(jumlah=3) = 2/36. P(jumlah <= 3) = 1/36 + 2/36 = 3/36. Maka, P(jumlah > 3) = 1 - 3/36 = 33/36.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png. Transkripsi visual: Tabel 7.2 menampilkan dua kolom: 'Jumlah' (berisi angka 2 sampai 12) dan 'Peluang' (kosong). Tabel ini merepresentasikan distribusi peluang jumlah mata dadu dari pelemparan dua dadu.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `170f0c51e40c021e2272eb7034b2ba9d65c84b7cc4404775dc6e37d39037bf8f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3818 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3808 |
| 3 | success | valid / verified | applying | procedural | Easy | 3789 |

Run 1 — solusi: P(jumlah > 3) = 1 - P(jumlah <= 3) = 1 - (P(2) + P(3)). Diketahui P(2) = 1/36 dan P(3) = 2/36. Maka P(jumlah > 3) = 1 - (1/36 + 2/36) = 1 - 3/36 = 33/36.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep komplemen dalam peluang untuk menghitung kejadian 'lebih besar dari 3' dengan menggunakan distribusi peluang yang sudah dipahami (jumlah 2 dan 3). Ini adalah penerapan prosedur rutin.. Bukti: tentukan jumlah yang lebih besar daripada 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara kejadian komplemen dan distribusi peluang diskrit.. Bukti: Tabel 7.2 distribusi peluang; tentukan jumlah yang lebih besar daripada 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi kejadian komplemen (jumlah 2 atau 3) dan menguranginya dari total peluang 1. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: tentukan jumlah yang lebih besar daripada 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang kejadian komplemen dan distribusi peluang dua dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan sudah familiar dengan konsep peluang dasar dan penggunaan tabel distribusi peluang untuk menghitung kejadian sederhana. |

Run 2 — solusi: P(jumlah > 3) = 1 - P(jumlah <= 3) = 1 - (P(2) + P(3)). Diketahui P(2) = 1/36 dan P(3) = 2/36, maka P(jumlah <= 3) = 3/36. Jadi, P(jumlah > 3) = 1 - 3/36 = 33/36.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep peluang komplemen atau penjumlahan peluang untuk kejadian yang lebih besar dari 3. Ini adalah penerapan prosedur standar dalam distribusi peluang.. Bukti: tentukan jumlah yang lebih besar daripada 3
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar distribusi peluang (konsep komplemen) dan cara menggunakannya untuk menyelesaikan masalah.. Bukti: Tabel 7.2 distribusi peluang; tentukan jumlah yang lebih besar daripada 3
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas (menggunakan komplemen atau menjumlahkan peluang yang relevan). Tidak ada kendala yang berinteraksi secara kompleks.. Bukti: tentukan jumlah yang lebih besar daripada 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian majemuk dan komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung peluang kejadian sederhana atau komplemennya dengan cepat tanpa kesulitan berarti. |

Run 3 — solusi: P(jumlah > 3) = 1 - P(jumlah <= 3). P(jumlah=2) = 1/36, P(jumlah=3) = 2/36. P(jumlah <= 3) = 1/36 + 2/36 = 3/36. Maka, P(jumlah > 3) = 1 - 3/36 = 33/36.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep komplemen dalam peluang untuk menentukan kejadian 'lebih besar dari 3' dengan menggunakan distribusi peluang jumlah dua dadu yang sudah diketahui polanya.. Bukti: tentukan jumlah yang lebih besar daripada 3
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung peluang kejadian majemuk menggunakan aturan komplemen pada distribusi peluang diskrit.. Bukti: distribusi peluang; jumlah yang lebih besar daripada 3
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu menerapkan aturan komplemen dasar pada distribusi peluang yang sudah familiar (jumlah dua dadu). Langkah penyelesaiannya langsung dan tidak memerlukan integrasi kendala yang kompleks.. Bukti: tentukan jumlah yang lebih besar daripada 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang kejadian majemuk dan aturan komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung peluang kejadian sederhana dan komplemennya pada ruang sampel dua dadu yang merupakan materi standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5316`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep peluang komplemen untuk menghitung kejadian 'lebih besar dari 3' dengan menggunakan distribusi peluang dua dadu. Ini adalah penerapan prosedur rutin yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang cara menghitung peluang kejadian majemuk menggunakan aturan komplemen pada distribusi peluang diskrit.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena jalur penyelesaiannya sangat jelas (menggunakan komplemen). Siswa hanya perlu mengidentifikasi kejadian yang tidak diinginkan (jumlah 2 atau 3) dan menguranginya dari total peluang 1. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian majemuk dan aturan komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung peluang kejadian sederhana atau komplemennya dengan cepat tanpa kesulitan berarti. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Distribusi Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.

tentukan jumlah yang lebih besar daripada 3
Pilihan: A. $\frac{3}{36}$
B. $\frac{33}{36}$
C. $\frac{35}{36}$
D. $\frac{34}{36}$
Transkripsi visual: Tabel 7.2 menampilkan dua kolom: 'Jumlah' (berisi angka 2 sampai 12) dan 'Peluang' (kosong). Tabel ini merepresentasikan distribusi peluang jumlah mata dadu dari pelemparan dua dadu.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `cc90109177ce7d63bb1a90a7`

Coba kamu tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.<br><br>a. jumlah 2 atau 3

| Opsi | Isi |
|---|---|
| A | $\frac{1}{36}$ |
| B | $\frac{6}{36}$ |
| C | $\frac{3}{36}$ |
| D | $\frac{2}{36}$ |

![Gambar sumber soal 41](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: P(jumlah 2) = 1/36. P(jumlah 3) = 2/36. Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png. Transkripsi visual: Tabel 7.2 berjudul 'Jumlah' dan 'Peluang' dengan baris untuk jumlah 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. Kolom peluang kosong.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `19c6c88617600615dd578a63284f8515678d940e2fe550d51ea2d9d4c2bb9822`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3789 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3832 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3833 |

Run 1 — solusi: P(jumlah 2) = 1/36. P(jumlah 3) = 2/36. Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan penjumlahan untuk kejadian saling lepas pada distribusi peluang diskrit yang familiar (jumlah dua dadu).. Bukti: Coba kamu tentukan peluang untuk kejadian berikut.; jumlah 2 atau 3
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip dasar peluang (kejadian saling lepas) pada distribusi peluang yang diberikan.. Bukti: Tabel 7.2 distribusi peluang; jumlah 2 atau 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Siswa hanya perlu mengidentifikasi nilai peluang dari tabel (atau menghitungnya secara dasar) dan menjumlahkannya. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang kejadian saling lepas dan ruang sampel dua dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah standar kelas 10. Soal ini menguji pemahaman langsung tentang aturan penjumlahan peluang untuk kejadian saling lepas tanpa kerumitan tambahan. |

Run 2 — solusi: P(jumlah 2) = 1/36 (pasangan 1,1). P(jumlah 3) = 2/36 (pasangan 1,2 dan 2,1). Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan penjumlahan untuk kejadian saling lepas pada distribusi peluang yang sudah dipahami konsepnya. Ini adalah penerapan prosedur standar.. Bukti: Coba kamu tentukan peluang untuk kejadian berikut.; jumlah 2 atau 3
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar distribusi peluang dan aturan penjumlahan untuk kejadian saling lepas.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi dua nilai peluang dari distribusi yang diketahui dan menjumlahkannya. Tidak ada kendala kompleks atau perencanaan strategi yang rumit.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang kejadian saling lepas dan distribusi peluang dua dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan sudah menguasai konsep peluang dasar dan aturan penjumlahan untuk kejadian saling lepas. |

Run 3 — solusi: P(jumlah 2) = 1/36 (pasangan (1,1)). P(jumlah 3) = 2/36 (pasangan (1,2), (2,1)). Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan penjumlahan untuk kejadian saling lepas pada distribusi peluang yang sudah dipahami konsepnya. Ini adalah penerapan prosedur standar.. Bukti: Coba kamu tentukan peluang untuk kejadian berikut.; jumlah 2 atau 3
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar peluang (kejadian saling lepas) dan cara menggunakannya dalam konteks distribusi peluang.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi dua nilai peluang dari distribusi yang diketahui dan menjumlahkannya. Tidak ada kendala kompleks atau perencanaan strategi yang rumit.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang kejadian saling lepas dan pembacaan tabel distribusi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai latihan dasar penerapan aturan penjumlahan peluang. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Distribusi Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Coba kamu tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.

a. jumlah 2 atau 3
Pilihan: A. $\frac{1}{36}$
B. $\frac{6}{36}$
C. $\frac{3}{36}$
D. $\frac{2}{36}$
Transkripsi visual: Tabel 7.2 berjudul 'Jumlah' dan 'Peluang' dengan baris untuk jumlah 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. Kolom peluang kosong.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `4dc162c092a693bfc3a3ad55`

Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.<br><br>Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.

| Opsi | Isi |
|---|---|
| A | $\frac{7}{36}$ |
| B | $\frac{5}{36}$ |
| C | $\frac{6}{36}$ |
| D | $\frac{1}{36}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: P(A) = peluang angka sama = 6/36. P(B) = peluang jumlah 2 = 1/36. Irisan (A ∩ B) = (1,1) = 1/36. P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 6/36 + 1/36 - 1/36 = 6/36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1763ae80eaba5e49cb602209058827a70620e8bcef000d1584924f4e15dbde9c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3617 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2778 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2776 |

Run 1 — solusi: P(A) = peluang angka sama = 6/36. P(B) = peluang jumlah 2 = 1/36. Irisan (A ∩ B) = (1,1) = 1/36. P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 6/36 + 1/36 - 1/36 = 6/36.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus aturan penjumlahan peluang untuk dua kejadian yang tidak saling lepas dengan mengidentifikasi irisan kejadian.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konsep kejadian tidak saling lepas dan penerapan rumus P(A ∪ B) = P(A) + P(B) - P(A ∩ B).. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut; dua angka sama atau berjumlah 2
- Intended difficulty `classify/Medium`: Soal memerlukan identifikasi bahwa kejadian tidak saling lepas (irisan tidak kosong). Siswa harus mengidentifikasi irisan (1,1) dan mengurangkannya. Ini melibatkan beberapa langkah prosedural yang saling terkait.. Bukti: dua angka sama atau berjumlah 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan memahami aturan penjumlahan peluang. Soal ini menguji pemahaman tentang kejadian tidak saling lepas yang merupakan standar materi kelas 10. |

Run 2 — solusi: Ruang sampel n(S) = 36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 2): {(1,1)}, n(B)=1. Irisan A dan B: {(1,1)}, n(A∩B)=1. P(A∪B) = P(A) + P(B) - P(A∩B) = 6/36 + 1/36 - 1/36 = 6/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian, menghitung peluang masing-masing, dan menerapkan aturan penjumlahan untuk kejadian tidak saling lepas (mengurangi irisan). Ini adalah penerapan konsep peluang pada konteks rutin.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.; Gunakan aturan penjumlahan untuk soal-soal berikut
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip aturan penjumlahan dalam peluang, khususnya konsep kejadian tidak saling lepas.. Bukti: Gunakan aturan penjumlahan; dua angka sama atau berjumlah 2
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus menyadari bahwa kejadian 'angka sama' dan 'berjumlah 2' tidak saling lepas (memiliki irisan). Meskipun prosedurnya standar, siswa sering terjebak dengan menjumlahkan peluang tanpa mengurangkan irisannya, sehingga memerlukan ketelitian dalam mengidentifikasi hubungan antar kejadian.. Bukti: dua angka sama atau berjumlah 2; Gunakan aturan penjumlahan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang adalah standar kelas 10. Soal ini menguji pemahaman konseptual tentang irisan kejadian, yang merupakan jebakan umum namun prosedurnya familiar bagi siswa. |

Run 3 — solusi: Ruang sampel n(S) = 36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 2): {(1,1)}, n(B)=1. Irisan A dan B: {(1,1)}, n(A∩B)=1. P(A∪B) = P(A) + P(B) - P(A∩B) = 6/36 + 1/36 - 1/36 = 6/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian, menghitung peluang masing-masing, dan menerapkan aturan penjumlahan untuk kejadian tidak saling lepas (mengurangi irisan). Ini adalah penerapan prosedur yang sudah dipelajari.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2; Gunakan aturan penjumlahan
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip inklusi-eksklusi dalam peluang (aturan penjumlahan) dan bagaimana menerapkannya pada ruang sampel dadu.. Bukti: Gunakan aturan penjumlahan; dua angka sama atau berjumlah 2
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus menyadari bahwa kedua kejadian tidak saling lepas dan melakukan koreksi (pengurangan irisan). Meskipun prosedurnya standar, siswa sering terjebak dengan tidak mengurangkan irisan, sehingga memerlukan ketelitian dalam perencanaan langkah.. Bukti: dua angka sama atau berjumlah 2; Gunakan aturan penjumlahan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang adalah standar kelas 10. Soal ini menguji pemahaman konsep irisan dalam aturan penjumlahan yang merupakan bagian inti dari kurikulum, dengan pengecoh yang dirancang untuk menangkap kesalahan umum siswa. |

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.

Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.
Pilihan: A. $\frac{7}{36}$
B. $\frac{5}{36}$
C. $\frac{6}{36}$
D. $\frac{1}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `60d456804bca8ee0d55a4bb7`

Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.<br><br>Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.

| Opsi | Isi |
|---|---|
| A | $\frac{6}{36}$ |
| B | $\frac{4}{36}$ |
| C | $\frac{9}{36}$ |
| D | $\frac{10}{36}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `10/36`.
Solusi minimum hasil AI: Ruang sampel n(S) = 36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A) = 6. Kejadian B (jumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B) = 4. Karena A dan B saling lepas (angka sama selalu genap, jumlah 5 ganjil), P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec35f7bcc5b3e82d23ac74dd2224ecedae123a07f076e513d62bd407c72cd230`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2761 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2759 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2728 |

Run 1 — solusi: Ruang sampel n(S) = 36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A) = 6. Kejadian B (jumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B) = 4. Karena A dan B saling lepas (angka sama selalu genap, jumlah 5 ganjil), P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian, memeriksa apakah kejadian tersebut saling lepas, dan menerapkan aturan penjumlahan peluang yang sesuai.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konsep peluang kejadian saling lepas dan penerapan prosedur penjumlahan peluang.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut; Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus mengidentifikasi dua kejadian yang berbeda, memverifikasi sifat saling lepas (mutually exclusive) antara kedua kejadian tersebut, dan melakukan penjumlahan peluang. Meskipun prosedurnya familiar, terdapat kebutuhan untuk analisis hubungan antar kejadian sebelum menerapkan rumus.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan kejadian saling lepas dan tidak, serta menghitung peluang sederhana. Soal ini menguji pemahaman tersebut dengan pengecoh yang relevan. |

Run 2 — solusi: Ruang sampel n(S) = 36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A) = 6. Kejadian B (jumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B) = 4. Karena A dan B saling lepas (tidak ada irisan), P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian, memeriksa apakah kejadian tersebut saling lepas, dan menerapkan aturan penjumlahan peluang yang sesuai.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kejadian saling lepas dalam peluang dan penerapan prosedur aturan penjumlahan.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut; Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus mengidentifikasi dua kejadian yang berbeda, memverifikasi sifat saling lepas (tidak ada irisan), dan melakukan penjumlahan peluang. Meskipun prosedurnya standar, siswa perlu melakukan analisis mandiri terhadap ruang sampel untuk kedua kejadian tersebut.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengidentifikasi ruang sampel dua dadu dan menerapkan aturan penjumlahan. Kesulitan terletak pada ketelitian mengidentifikasi irisan (atau ketiadaannya) antara dua kejadian. |

Run 3 — solusi: Ruang sampel n(S) = 36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A) = 6. Kejadian B (jumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B) = 4. Karena A dan B saling lepas (angka sama selalu genap, jumlah 5 ganjil), maka P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian, memeriksa apakah keduanya saling lepas, dan menerapkan aturan penjumlahan peluang. Ini adalah penerapan konsep dasar peluang pada konteks rutin.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip aturan penjumlahan dalam peluang dan bagaimana menerapkannya pada kejadian saling lepas.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut; Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus mengidentifikasi dua kejadian yang berbeda, memverifikasi sifat saling lepas (mutually exclusive), dan melakukan operasi penjumlahan peluang. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan kejadian saling lepas dan tidak, serta menghitung peluang sederhana. Soal ini menuntut ketelitian dalam mengidentifikasi anggota ruang sampel untuk kedua kejadian. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.

Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
Pilihan: A. $\frac{6}{36}$
B. $\frac{4}{36}$
C. $\frac{9}{36}$
D. $\frac{10}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `6353e1b1ac73792bd65d8bcc`

Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.<br><br>Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?

| Opsi | Isi |
|---|---|
| A | Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$ |
| B | Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$ |
| C | Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$ |
| D | Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Peluang muncul angka dobel (E1) adalah 6/36 = 1/6. Peluang muncul jumlah mata dadu enam (E2) adalah {(1,5), (2,4), (3,3), (4,2), (5,1)}, yaitu 5/36. Karena lemparan pertama dan kedua adalah kejadian saling bebas, maka peluang keduanya terjadi adalah P(E1) x P(E2) = 1/6 x 5/36 = 5/216.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `66c6d1949c537de0fc280da652d0ab081476f09553a30bfbd13c319171f326c8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2833 |
| 2 | success | valid / verified | applying | procedural | Medium | 2821 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2810 |

Run 1 — solusi: Peluang mendapatkan angka dobel pada sepasang dadu adalah 6/36 = 1/6. Peluang mendapatkan jumlah enam pada sepasang dadu adalah 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Karena kedua lemparan dadu adalah kejadian saling bebas, peluang keduanya terjadi adalah P(A) × P(B) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas dan menerapkan aturan perkalian peluang untuk dua kejadian tersebut. Ini memerlukan pemahaman konsep dasar peluang kejadian majemuk.. Bukti: Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang syarat kejadian saling bebas dan penerapan prosedur aturan perkalian dalam peluang.. Bukti: aturan perkalian dapat digunakan; mendapatkan angka dobel; mendapatkan jumlah enam
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi dua kejadian yang berbeda (dobel dan jumlah enam), menghitung peluang masing-masing secara terpisah, dan memahami syarat kejadian saling bebas untuk menerapkan aturan perkalian. Meskipun prosedurnya standar, siswa perlu melakukan beberapa langkah integrasi.. Bukti: melemparkan sepasang dadu; mendapatkan angka dobel; mendapatkan jumlah enam; aturan perkalian dapat digunakan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian tunggal, ruang sampel dua dadu, dan definisi kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung peluang kejadian majemuk sederhana. Soal ini menuntut pemahaman tentang ruang sampel dua dadu dan aturan perkalian, yang merupakan materi standar namun memerlukan ketelitian dalam menentukan ruang sampel dan kejadian. |

Run 2 — solusi: Peluang muncul angka dobel (E1) adalah 6/36 = 1/6. Peluang jumlah mata dadu enam (E2) adalah {(1,5), (2,4), (3,3), (4,2), (5,1)}, yaitu 5/36. Karena lemparan pertama dan kedua adalah kejadian saling bebas, maka peluang keduanya terjadi adalah P(E1) x P(E2) = 1/6 x 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas (independen) dan menerapkan aturan perkalian peluang untuk kejadian tersebut. Ini melibatkan pemahaman konsep dasar peluang dan aturan perkalian, yang merupakan penerapan konsep pada konteks rutin.. Bukti: Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian saling bebas) dan prosedur perhitungan peluang gabungan, yang termasuk dalam kategori pengetahuan prosedural.. Bukti: aturan perkalian dapat digunakan; peluang ini dapat terjadi
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah perhitungan peluang terpisah (dobel dan jumlah enam) sebelum mengalikannya. Siswa harus memahami syarat kejadian saling bebas dan menghitung ruang sampel untuk masing-masing kejadian secara akurat.. Bukti: mendapatkan angka dobel; mendapatkan jumlah enam; aturan perkalian dapat digunakan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian tunggal, ruang sampel dua dadu, dan definisi kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 10 karena menguji pemahaman aturan perkalian pada kejadian saling bebas dengan konteks dadu yang standar. Tingkat kesulitan Medium diberikan karena siswa harus melakukan dua perhitungan peluang terpisah sebelum mengalikannya. |

Run 3 — solusi: Peluang muncul angka dobel pada sepasang dadu adalah 6/36 = 1/6. Peluang muncul jumlah enam pada sepasang dadu adalah 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Karena kedua lemparan adalah kejadian saling bebas, maka peluang keduanya terjadi adalah (1/6) * (5/36) = 5/216.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi sifat kejadian (saling bebas) sebagai syarat penggunaan aturan perkalian dan menerapkan prosedur perkalian peluang untuk dua kejadian tersebut. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip dasar peluang (kejadian saling bebas) dan metode perhitungannya, yang merupakan pengetahuan konseptual.. Bukti: Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi dua kejadian yang berbeda, menghitung peluang masing-masing secara terpisah (dobel dan jumlah enam), dan memahami syarat kejadian saling bebas untuk menerapkan aturan perkalian. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait.. Bukti: Kirana sedang memainkan sebuah permainan yang menggunakan dadu.; mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung peluang kejadian majemuk sederhana. Soal ini menuntut pemahaman konsep saling bebas dan perhitungan peluang dasar tanpa kompleksitas tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4557`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas dan menerapkan aturan perkalian peluang untuk dua kejadian tersebut. Ini memerlukan pemahaman konsep dasar peluang kejadian majemuk.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang syarat kejadian saling bebas dan penerapan prosedur aturan perkalian dalam peluang.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi dua kejadian yang berbeda, menghitung peluang masing-masing secara terpisah, dan memahami syarat kejadian saling bebas untuk menerapkan aturan perkalian. Meskipun prosedurnya standar, siswa perlu melakukan beberapa langkah integrasi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian tunggal, ruang sampel dua dadu, dan definisi kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung peluang kejadian majemuk sederhana. Soal ini menuntut pemahaman tentang ruang sampel dua dadu dan aturan perkalian, yang merupakan materi standar namun memerlukan ketelitian dalam menentukan ruang sampel dan kejadian. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Perkalian
Tipe soal: multiple_choice
Stimulus: -
Soal: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.

Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
Pilihan: A. Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$
B. Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$
C. Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$
D. Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `a870c7129a611f1645f3744f`

Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan<br><br>dua angka genap

| Opsi | Isi |
|---|---|
| A | $\frac{1}{2}$ |
| B | $\frac{1}{4}$ |
| C | $\frac{1}{36}$ |
| D | $\frac{1}{12}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Peluang muncul angka genap pada satu lemparan dadu adalah 3/6 = 1/2. Karena dua lemparan dadu adalah kejadian independen, peluang muncul angka genap pada kedua lemparan adalah (1/2) * (1/2) = 1/4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8afebc8bbef82980ed6f093e11338d9cea58d48910fa84ddad0612c1b58ed1ab`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2626 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2591 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2583 |

Run 1 — solusi: Peluang muncul angka genap pada satu dadu adalah 3/6 = 1/2. Karena pelemparan dadu pertama dan kedua adalah kejadian independen, peluang muncul dua angka genap adalah P(genap) × P(genap) = 1/2 × 1/2 = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian untuk kejadian independen (peluang dua kejadian terjadi bersamaan). Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan dua angka genap
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian independen) dan prosedur perhitungan peluang sederhana.. Bukti: peluang untuk mendapatkan dua angka genap
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Jalur penyelesaian sangat jelas (menghitung peluang satu kejadian lalu mengalikannya), tidak ada kendala yang berinteraksi, dan konsep peluang independen adalah materi dasar yang familiar.. Bukti: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan dua angka genap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah kurikulum standar kelas 10. Soal ini tidak memerlukan pemodelan kompleks atau integrasi konsep yang sulit. |

Run 2 — solusi: Peluang muncul angka genap pada satu lemparan dadu adalah 3/6 = 1/2. Karena dua lemparan dadu adalah kejadian independen, peluang muncul angka genap pada kedua lemparan adalah (1/2) * (1/2) = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian untuk kejadian independen (peluang dua kejadian terjadi bersamaan). Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks rutin.. Bukti: Hitung peluang untuk mendapatkan dua angka genap
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian independen) dan penggunaan aturan perkalian.. Bukti: Hitung peluang untuk mendapatkan dua angka genap
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Siswa hanya perlu mengidentifikasi peluang satu kejadian dan mengalikannya. Tidak ada kendala kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Sebuah dadu dilempar dua kali; Hitung peluang untuk mendapatkan dua angka genap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal dan aturan perkalian untuk kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar merupakan bagian standar kurikulum kelas 10. Soal ini tidak memerlukan integrasi konsep yang rumit. |

Run 3 — solusi: Peluang muncul angka genap pada satu lemparan dadu adalah 3/6 = 1/2. Karena dua lemparan dadu adalah kejadian independen, peluang mendapatkan dua angka genap adalah (1/2) * (1/2) = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian untuk kejadian independen (peluang dua lemparan dadu) setelah mengidentifikasi peluang kejadian tunggal.. Bukti: Hitung peluang untuk mendapatkan dua angka genap
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar peluang dan aturan perkalian untuk kejadian independen.. Bukti: Hitung peluang untuk mendapatkan dua angka genap
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Siswa hanya perlu memahami konsep peluang kejadian independen dan melakukan satu operasi perkalian sederhana. Tidak ada kendala kompleks atau kebutuhan untuk membangun model yang rumit.. Bukti: Sebuah dadu dilempar dua kali; Hitung peluang untuk mendapatkan dua angka genap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah kurikulum standar kelas 10. Soal ini tidak menuntut penalaran tingkat tinggi atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4023`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan aturan perkalian untuk kejadian independen (peluang dua kejadian terjadi bersamaan). Ini adalah penerapan prosedur standar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian independen) dan prosedur perhitungan peluang sederhana.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Jalur penyelesaian sangat jelas (menghitung peluang satu kejadian lalu mengalikannya), tidak ada kendala yang berinteraksi, dan konsep peluang independen adalah materi dasar yang familiar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah kurikulum standar kelas 10. Soal ini tidak memerlukan pemodelan kompleks atau integrasi konsep yang sulit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Perkalian
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan

dua angka genap
Pilihan: A. $\frac{1}{2}$
B. $\frac{1}{4}$
C. $\frac{1}{36}$
D. $\frac{1}{12}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `4e77f956826bf22b33dbf58b`

Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.

| Opsi | Isi |
|---|---|
| A | 6/125 |
| B | 5/125 |
| C | 10/125 (atau 0,08) |
| D | 3/125 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `10/125`.
Solusi minimum hasil AI: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 ekuivalen dengan jumlah 3 angka < 6. Kemungkinan jumlah: 3 (1,1,1: 1 cara), 4 (1,1,2: 3 cara), 5 (1,1,3: 3 cara; 1,2,2: 3 cara). Total kejadian = 1 + 3 + 6 = 10. Peluang = 10/125.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9e4d9a9eb6a7802e13471f4acfd8fdad35d7cf936c05d8342e10e408d87dc354`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3687 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3849 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3687 |

Run 1 — solusi: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 berarti jumlah 3 angka < 6. Kemungkinan jumlah: 3 (1,1,1: 1 cara), 4 (1,1,2: 3 cara), 5 (1,1,3: 3 cara; 1,2,2: 3 cara). Total cara = 1 + 3 + 6 = 10. Peluang = 10/125.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep ruang sampel dan peluang kejadian majemuk untuk menghitung rata-rata dari tiga kejadian independen dengan batasan tertentu.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan prosedur sistematis untuk menghitung ruang sampel dan mengidentifikasi kombinasi yang memenuhi syarat (jumlah < 6).. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Siswa harus menerjemahkan syarat rata-rata ke syarat jumlah, lalu melakukan enumerasi sistematis untuk setiap kemungkinan jumlah (3, 4, 5). Ini memerlukan perencanaan langkah yang saling terkait, bukan sekadar substitusi rumus langsung.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian independen dan ruang sampel. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena siswa perlu melakukan enumerasi sistematis untuk memenuhi kendala jumlah, yang melibatkan beberapa langkah logis yang saling bergantung. |

Run 2 — solusi: Total ruang sampel = 5^3 = 125. Rata-rata < 2 berarti jumlah 3 angka < 6. Kemungkinan jumlah: 3 (1,1,1) ada 1 cara; 4 (1,1,2; 1,2,1; 2,1,1) ada 3 cara; 5 (1,1,3; 1,3,1; 3,1,1; 1,2,2; 2,1,2; 2,2,1) ada 6 cara. Total cara = 1+3+6 = 10. Peluang = 10/125.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan kondisi rata-rata ke dalam syarat jumlah, lalu menghitung ruang sampel dan kejadian yang memenuhi syarat tersebut. Ini melibatkan penerapan konsep peluang pada konteks yang memerlukan ketelitian dalam pencacahan.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip dasar peluang (ruang sampel dan kejadian) dan menerapkannya pada masalah kombinatorik sederhana yang memerlukan pemahaman hubungan antar konsep.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Soal ini memerlukan perencanaan langkah (mengubah rata-rata ke jumlah, mendaftar kombinasi yang memenuhi syarat). Siswa harus teliti dalam mendaftar semua kemungkinan agar tidak ada yang terlewat, yang menuntut perencanaan lebih dari sekadar prosedur satu langkah.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, aturan perkalian, dan rata-rata. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan pencacahan sistematis untuk kejadian majemuk sederhana. Soal ini menuntut ketelitian dalam mendaftar kejadian yang memenuhi syarat jumlah < 6. |

Run 3 — solusi: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 ekuivalen dengan jumlah 3 angka < 6. Kemungkinan jumlah: 3 (1,1,1: 1 cara), 4 (1,1,2: 3 cara), 5 (1,1,3: 3 cara; 1,2,2: 3 cara). Total kejadian = 1 + 3 + 6 = 10. Peluang = 10/125.
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep peluang dan prinsip pencacahan pada konteks baru. Mereka perlu mengubah syarat rata-rata menjadi syarat jumlah, lalu menghitung ruang sampel dan kejadian yang memenuhi syarat secara sistematis.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara rata-rata dan jumlah dalam ruang sampel, serta bagaimana mengkategorikan hasil yang memenuhi syarat.. Bukti: rata-ratanya kurang dari 2; memilih sampel dengan memutar roda tersebut sebanyak tiga kali
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan langkah (mengubah rata-rata ke jumlah), integrasi konsep (ruang sampel 5^3), dan enumerasi sistematis tanpa bantuan langsung. Siswa harus mengelola kendala jumlah < 6 dan menghitung permutasi untuk setiap kombinasi angka.. Bukti: rata-ratanya kurang dari 2; memutar roda tersebut sebanyak tiga kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar peluang, permutasi sederhana, dan konsep rata-rata. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan enumerasi sistematis dan memahami ruang sampel untuk kejadian majemuk, namun soal ini menuntut ketelitian dalam mengaitkan rata-rata dengan jumlah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4685`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep peluang kejadian majemuk dan prinsip pencacahan. Mereka harus menerjemahkan syarat rata-rata ke dalam syarat jumlah, lalu menghitung ruang sampel dan kejadian yang memenuhi syarat tersebut secara sistematis.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara rata-rata dan jumlah dalam ruang sampel, serta bagaimana mengkategorikan hasil yang memenuhi syarat.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan langkah (mengubah rata-rata ke jumlah), integrasi konsep (ruang sampel 5^3), dan enumerasi sistematis tanpa bantuan langsung. Siswa harus mengelola kendala jumlah < 6 dan menghitung permutasi untuk setiap kombinasi angka.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Prinsip dasar peluang, aturan perkalian, dan konsep rata-rata. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan enumerasi sistematis dan memahami ruang sampel untuk kejadian majemuk, namun soal ini menuntut ketelitian dalam mengaitkan rata-rata dengan jumlah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.
Pilihan: A. 6/125
B. 5/125
C. 10/125 (atau 0,08)
D. 3/125
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
