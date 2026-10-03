# Validasi ulang soal kelas 10 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v8-blind-sma10-key-verified`. Rubrik: `math-rubric-3x4x3-v6-sma10-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 10 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 10, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 46; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 41, "knowing": 4, "reasoning": 1}, "knowledgeDimension": {"conceptual": 17, "procedural": 28, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 29, "Medium": 17, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 41, "knowing": 4, "reasoning": 1}, "knowledgeDimension": {"conceptual": 17, "procedural": 28, "factual": 1}, "intendedDifficulty": {"Easy": 29, "Medium": 17}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 46}`.
Run awal sukses: 138/138; adjudikasi: 22; token sukses tercatat: 429,659.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 29 | 29 | [Easy.json](difficulty/Easy.json) |
| Medium | 17 | 17 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 10, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 10, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 10. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `20c03a0ebabbdc13efb66801`

Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.<br><br>\|Fase penyebaran\|1\|2\|3\|4\|5\|6\|7\|8\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Banyak orang yang menerima hoaks\|2\|4\|…\|….\|….\|….\|….\|….\|<br><br>Jika banyak fase adalah n, tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?

| Opsi | Isi |
|---|---|
| A | $2^{n-1}$ |
| B | $2n$ |
| C | $n^2$ |
| D | $2^n$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola penyebaran adalah 2, 4, 8, 16, ... untuk fase n=1, 2, 3, 4, .... Ini adalah barisan geometri dengan suku pertama a=2 dan rasio r=2. Rumus suku ke-n adalah U_n = a * r^(n-1) = 2 * 2^(n-1) = 2^n.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b9f1549230e21d3757488e159798e9504c123dc01810ea0dfdea4a9dff4dc65`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2237 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2216 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2246 |

Run 1 — solusi: Pola penyebaran adalah 2, 4, 8, 16, ... untuk fase n=1, 2, 3, 4, .... Ini adalah barisan geometri dengan suku pertama a=2 dan rasio r=2. Rumus suku ke-n adalah U_n = a * r^(n-1) = 2 * 2^(n-1) = 2^n.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola bilangan (2, 4, 8, ...) dan menggeneralisasikannya ke dalam bentuk rumus eksponensial. Ini melibatkan proses mengidentifikasi pola dan menerapkan konsep fungsi eksponensial sederhana.. Bukti: Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran; tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pertumbuhan eksponensial dan bagaimana merepresentasikannya dalam bentuk rumus fungsi.. Bukti: rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Pola pertumbuhan eksponensial (2^n) sangat mendasar dan sering ditemui dalam konteks pertumbuhan populasi atau penyebaran informasi. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya; Lengkapilah tabel di bawah ini; tentukan rumus sederhana

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah topik awal kelas 10. Soal ini menguji pemahaman dasar definisi eksponen melalui konteks yang sangat umum dan mudah dipahami. |

Run 2 — solusi: Pola penyebaran adalah 2, 4, 8, 16, ... yang merupakan barisan geometri dengan suku pertama a=2 dan rasio r=2. Pada fase ke-1 (n=1), banyak orang = 2^1 = 2. Pada fase ke-2 (n=2), banyak orang = 2^2 = 4. Maka, untuk fase ke-n, rumusnya adalah 2^n.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali pola bilangan dari konteks cerita, menggeneralisasi pola tersebut ke dalam bentuk rumus eksponensial, dan memverifikasinya dengan data yang diberikan.. Bukti: Lengkapilah tabel di bawah ini; tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pertumbuhan eksponensial dan bagaimana merepresentasikannya dalam bentuk rumus matematika.. Bukti: rumus sederhana untuk menghitung banyak orang; 2,4,8,16,...=2^1,2^2,2^3,2^4,...
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10 karena pola pertumbuhan eksponensial (2^n) merupakan materi dasar yang sering ditemui. Siswa hanya perlu mengidentifikasi pola dari urutan bilangan yang diberikan.. Bukti: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya; Lengkapilah tabel di bawah ini; tentukan rumus sederhana

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah topik standar kelas 10. Soal ini menggunakan konteks yang sangat umum dan prosedur yang langsung. |

Run 3 — solusi: Pola penyebaran adalah 2, 4, 8, 16, ... yang merupakan deret geometri dengan suku pertama a=2 dan rasio r=2. Pada fase ke-1, banyak orang = 2^1 = 2. Pada fase ke-2, banyak orang = 2^2 = 4. Maka, pada fase ke-n, banyak orang = 2^n.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali pola bilangan (2, 4, 8, ...) dan menggeneralisasikannya ke dalam bentuk rumus eksponensial. Ini melibatkan pemahaman konsep pertumbuhan eksponensial sederhana.. Bukti: Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.; tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana pertumbuhan eksponensial dimodelkan melalui pola bilangan.. Bukti: Banyak orang yang menerima hoaks\|2\|4\|…\|; rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10 karena pola pertumbuhan eksponensial dasar (basis 2) sangat umum dipelajari. Siswa hanya perlu mengidentifikasi pola dari data yang diberikan.. Bukti: 2, 4, 8, 16,...=2^1,2^2,2^3,2^4,...; rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah topik dasar kelas 10. Mengidentifikasi pola 2^n dari urutan 2, 4, 8 adalah prosedur standar yang familiar. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Solusi minimum hasil AI: Pola penyebaran mengikuti fungsi eksponensial f(n) = 2^n, dengan n adalah fase. Untuk fase ke-6, f(6) = 2^6 = 64.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fa4e42cb977cb70ed6814914e073000091788f89a62b1c619b9a0dd450874c70`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2174 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2186 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2143 |

Run 1 — solusi: Pola penyebaran mengikuti fungsi eksponensial f(n) = 2^n, dengan n adalah fase. Untuk fase ke-6, f(6) = 2^6 = 64.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan (2, 4, ...) dan menerapkan aturan eksponen untuk menentukan nilai pada fase ke-6. Ini adalah penerapan konsep dasar eksponen dalam situasi rutin.. Bukti: Lengkapilah tabel di bawah ini; Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pertumbuhan eksponensial dan kemampuan prosedural dalam menghitung nilai eksponen.. Bukti: pola bilangan tersebut; 2^6 = 64
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Siswa hanya perlu mengenali pola 2^n dan melakukan perhitungan sederhana. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya; hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pola bilangan dan eksponen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah dasar di kelas 10. Soal ini menggunakan konteks yang mudah dipahami dan prosedur yang sangat standar. |

Run 2 — solusi: Pola penyebaran mengikuti fungsi eksponensial f(n) = 2^n, di mana n adalah fase. Untuk fase ke-6, jumlah orang yang menerima hoaks adalah 2^6 = 64.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan dan menerapkan aturan tersebut untuk menentukan nilai pada fase tertentu. Ini adalah proses penerapan konsep eksponen dalam situasi rutin.. Bukti: Lengkapilah tabel di bawah ini; Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pertumbuhan eksponensial dan kemampuan prosedural dalam menghitung nilai berdasarkan pola yang ditemukan.. Bukti: pola bilangan tersebut; 2 orang temannya; 2^6 = 64
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena menggunakan konteks yang familiar (pertumbuhan dua kali lipat), prosedur yang langsung (pangkat bilangan bulat positif), dan hanya memerlukan satu langkah perhitungan rutin untuk mencapai jawaban.. Bukti: membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya; fase ke-8; hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang eksponen bilangan bulat positif. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah dasar kelas 10. Soal ini menguji pemahaman pola dasar tanpa kompleksitas tambahan, sehingga sesuai untuk tingkat kesulitan rendah. |

Run 3 — solusi: Pola penyebaran mengikuti fungsi eksponensial f(n) = 2^n, dengan n adalah fase penyebaran. Untuk fase ke-6, jumlah orang yang menerima hoaks adalah 2^6 = 64.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan dan menerapkan rumus eksponen untuk menentukan nilai pada fase tertentu.. Bukti: Pola penyebaran hoaks berlipat dua tiap fase sehingga mengikuti 2^fase
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pertumbuhan eksponensial dan kemampuan prosedural dalam menerapkan pola bilangan tersebut untuk memprediksi nilai.. Bukti: Lengkapilah tabel di bawah ini; Dengan memanfaatkan pola bilangan tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10 karena hanya memerlukan pengenalan pola eksponensial sederhana (basis 2) dan perhitungan langsung tanpa kendala kompleks.. Bukti: Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8; hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6

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
| gradeRelativeRationale | Materi eksponen adalah topik dasar kelas 10. Soal ini menggunakan konteks yang familiar dan prosedur yang langsung, sehingga tergolong mudah. |

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
Solusi minimum hasil AI: Persamaan: (3π)^p = 27π^3. Karena 27 = 3^3, maka 27π^3 = 3^3 * π^3 = (3π)^3. Sehingga (3π)^p = (3π)^3, yang berarti p = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `96059018f5b36ed527668f478a8d3fb9127ccd133f31bea450d076a5b7067d45`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2024 |
| 2 | success | valid / verified | applying | procedural | Easy | 2040 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2186 |

Run 1 — solusi: Persamaan: (3π)^p = 27π^3. Karena 27 = 3^3, maka 27π^3 = 3^3 * π^3 = (3π)^3. Sehingga (3π)^p = (3π)^3, yang berarti p = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat eksponen (a^n * b^n = (ab)^n) untuk menyamakan basis ruas kiri dan kanan sebelum menentukan nilai p.. Bukti: (3π)^p = 27π^3; 27π^3 = 3^3 * π^3 = (3π)^3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dan aturan operasi eksponen (sifat perpangkatan perkalian).. Bukti: (3π)^p = 27π^3
- Intended difficulty `classify/Easy`: Soal ini memerlukan satu langkah manipulasi aljabar rutin untuk mengubah bentuk 27π^3 menjadi (3π)^3 agar basisnya sama. Prosedur ini standar untuk kelas 10.. Bukti: (3π)^p = 27π^3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dasar (a^n * b^n = (ab)^n). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin penerapan sifat eksponen yang sesuai dengan kurikulum kelas 10, tidak memerlukan strategi kompleks. |

Run 2 — solusi: Persamaan: (3π)^p = 27π^3. Karena 27 = 3^3, maka 27π^3 = 3^3 * π^3 = (3π)^3. Sehingga (3π)^p = (3π)^3, yang berarti p = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat eksponen (a^n * b^n = (ab)^n) untuk menyamakan basis ruas kiri dan kanan. Ini adalah penerapan prosedur rutin dalam konteks eksponen.. Bukti: (3π)^p = 27π^3; 27π^3 = 3^3 * π^3 = (3π)^3
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang sifat-sifat eksponen dan manipulasi aljabar dasar untuk menyamakan bentuk basis.. Bukti: (3π)^p = 27π^3
- Intended difficulty `classify/Easy`: Soal ini memerlukan manipulasi aljabar sederhana untuk menyamakan basis. Prosedur ini familiar bagi siswa kelas 10 dan hanya melibatkan satu konsep utama (sifat eksponen).. Bukti: (3π)^p = 27π^3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dasar (a^n * b^n = (ab)^n) |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah kurikulum standar kelas 10. Soal ini menguji pemahaman dasar tanpa kompleksitas tinggi. |

Run 3 — solusi: Diketahui (3π)^p = 27π^3. Karena 27 = 3^3, maka persamaan menjadi (3π)^p = 3^3 · π^3. Berdasarkan sifat eksponen (ab)^n = a^n · b^n, maka 3^3 · π^3 = (3π)^3. Sehingga (3π)^p = (3π)^3, yang menghasilkan p = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat eksponen (ab)^n = a^n b^n untuk menyamakan basis ruas kanan dengan ruas kiri. Ini adalah penerapan prosedur rutin pada situasi yang sedikit dimodifikasi.. Bukti: (3π)^p = 27π^3; 27π^3 = 3^3·π^3 = (3π)^3
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara sifat-sifat eksponen dan manipulasi aljabar untuk menyamakan basis.. Bukti: (3π)^p = 27π^3
- Intended difficulty `classify/Easy`: Soal ini memerlukan satu langkah manipulasi aljabar (mengubah 27 menjadi 3^3) untuk menyamakan basis. Prosedur ini standar dan familiar bagi siswa kelas 10.. Bukti: (3π)^p = 27π^3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dasar (ab)^n = a^n b^n dan pemahaman bilangan berpangkat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah kurikulum standar kelas 10. Soal ini menguji pemahaman dasar sifat eksponen tanpa kompleksitas tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3579`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan sifat eksponen (a^n * b^n = (ab)^n) untuk menyamakan basis ruas kiri dan kanan sebelum menentukan nilai p. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang prinsip dan aturan operasi eksponen (sifat perpangkatan perkalian) untuk memanipulasi bentuk aljabar.
- Intended difficulty `Easy`: Soal ini memerlukan satu langkah manipulasi aljabar rutin untuk mengubah bentuk 27π^3 menjadi (3π)^3 agar basisnya sama. Prosedur ini standar untuk kelas 10.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dasar (a^n * b^n = (ab)^n). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin penerapan sifat eksponen yang sesuai dengan kurikulum kelas 10, tidak memerlukan strategi kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
| 1 | success | valid / verified | knowing | procedural | Easy | 1973 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1959 |
| 3 | success | valid / verified | applying | procedural | Easy | 1962 |

Run 1 — solusi: Menggunakan sifat eksponen (a^m)^n = a^(m*n), maka (3^4)^2 = 3^(4*2) = 3^8. Jadi, p = 8.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman langsung terhadap sifat dasar eksponen (a^m)^n = a^(m*n). Siswa hanya perlu menerapkan prosedur rutin tersebut tanpa memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: (3^4)^2 = 3^p
- Dimensi pengetahuan `classify/procedural`: Soal ini berfokus pada penguasaan algoritma atau aturan eksponen, yang merupakan bagian dari pengetahuan prosedural.. Bukti: (3^4)^2 = 3^p
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan satu langkah penerapan sifat eksponen. Tidak ada kendala tambahan atau kompleksitas yang berarti.. Bukti: (3^4)^2 = 3^p

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat dasar eksponen (perpangkatan bilangan berpangkat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah dasar yang dipelajari di awal kelas 10. Soal ini merupakan penerapan langsung sifat dasar tanpa modifikasi, sehingga dikategorikan mudah. |

Run 2 — solusi: Menggunakan sifat eksponen (a^m)^n = a^(m*n), maka (3^4)^2 = 3^(4*2) = 3^8. Jadi, p = 8.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman langsung terhadap sifat eksponen (a^m)^n = a^(m*n). Siswa hanya perlu menerapkan prosedur standar tanpa modifikasi strategi.. Bukti: (3^4)^2 = 3^p
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami aturan atau prinsip eksponen untuk menyelesaikan persamaan tersebut.. Bukti: (3^4)^2 = 3^p
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur satu langkah yang sangat mendasar dalam materi eksponen kelas 10. Tidak ada kompleksitas tambahan atau langkah ganda yang diperlukan.. Bukti: (3^4)^2 = 3^p

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat dasar eksponen (perpangkatan bilangan berpangkat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan fondasi awal eksponen di kelas 10. Soal ini bersifat rutin dan langsung menguji penguasaan sifat eksponen dasar. |

Run 3 — solusi: Menggunakan sifat eksponen (a^m)^n = a^(m*n), maka (3^4)^2 = 3^(4*2) = 3^8. Jadi, p = 8.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan sifat eksponen dasar (pangkat dipangkatkan) secara langsung. Ini adalah prosedur standar yang diajarkan di kelas 10.. Bukti: (3^4)^2 = 3^p
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menerapkan aturan atau algoritma eksponen (a^m)^n = a^(m*n).. Bukti: (3^4)^2 = 3^p
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung menguji pemahaman satu sifat eksponen tanpa langkah tambahan atau kompleksitas.. Bukti: (3^4)^2 = 3^p

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sifat-sifat eksponen. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah fondasi awal kelas 10. Soal ini hanya memerlukan satu langkah penerapan rumus, sehingga dikategorikan mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3275`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menguji pengenalan dan penerapan langsung sifat dasar eksponen (a^m)^n = a^(m*n). Siswa hanya perlu melakukan proses komputasi rutin tanpa strategi nonrutin.
- Dimensi pengetahuan `procedural`: Soal ini berfokus pada penerapan algoritma atau aturan eksponen yang spesifik, yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini adalah prosedur satu langkah yang sangat mendasar dalam materi eksponen kelas 10. Tidak ada kompleksitas tambahan atau langkah ganda yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat dasar eksponen (perpangkatan bilangan berpangkat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen adalah fondasi awal kelas 10. Soal ini bersifat rutin dan langsung menguji penguasaan sifat eksponen dasar. |

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
Solusi minimum hasil AI: Model pertumbuhan eksponensial: P(t) = P0(1+r)^t. Diketahui P0 = 36.000.000, r = 0,02, dan t = 2020 - 2015 = 5. Maka P(5) = 36.000.000 * (1,02)^5 = 36.000.000 * 1,1040808 = 39.746.908,8. Dibulatkan menjadi 39.746.909.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5da5e926e8df5a4456e1145f80d8c01c94706e8f14cfcdb28be5652bc4d92589`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2233 |
| 2 | success | valid / verified | applying | procedural | Medium | 3434 |
| 3 | success | valid / verified | applying | procedural | Medium | 2805 |

Run 1 — solusi: Model pertumbuhan eksponensial: f(x) = P0(1+r)^x. Diketahui P0 = 36.000.000, r = 0,02, dan x = 2020 - 2015 = 5. Maka f(5) = 36.000.000 * (1,02)^5 = 36.000.000 * 1,1040808 = 39.746.908,8. Dibulatkan menjadi 39.746.909.
- Domain kognitif `classify/applying`: Siswa perlu memilih model fungsi eksponensial yang tepat untuk pertumbuhan dan menerapkan prosedur substitusi nilai ke dalam rumus tersebut.. Bukti: peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun; berapa banyak kasus yang terjadi pada tahun 2020
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai prinsip pertumbuhan eksponensial dan penggunaan rumus pertumbuhan majemuk.. Bukti: bertambah secara eksponen pada peningkatan 2% setiap tahun
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan rutin dari rumus pertumbuhan eksponensial. Siswa hanya perlu mengidentifikasi nilai awal, laju pertumbuhan, dan selisih waktu (x=5), kemudian melakukan perhitungan.. Bukti: 36 juta jiwa; meningkat rata-rata 2% setiap tahun; tahun 2015... tahun 2020

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
| gradeRelativeRationale | Sesuai untuk kelas 10 karena merupakan aplikasi langsung dari materi fungsi eksponensial yang diajarkan di jenjang tersebut. |

Run 2 — solusi: Model pertumbuhan eksponensial: P(t) = P0(1+r)^t. Diketahui P0 = 36.000.000, r = 0,02, dan t = 2020 - 2015 = 5. Maka P(5) = 36.000.000 * (1,02)^5 ≈ 36.000.000 * 1,1040808 = 39.746.908,8. Dibulatkan menjadi 39.746.909.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model pertumbuhan eksponensial dan menerapkan rumus P(t) = P0(1+r)^t pada situasi nyata.. Bukti: peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan pertumbuhan eksponensial untuk menyelesaikan masalah.. Bukti: bertambah secara eksponen pada peningkatan 2% setiap tahun
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan model yang tepat (eksponensial vs linear) dan perhitungan langkah demi langkah yang rutin namun memerlukan ketelitian dalam menentukan selisih tahun.. Bukti: peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen; berapa banyak kasus yang terjadi pada tahun 2020

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep fungsi eksponensial dan pertumbuhan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman dasar fungsi eksponensial dalam konteks pertumbuhan. |

Run 3 — solusi: Model pertumbuhan eksponensial: P(t) = P0(1+r)^t. Diketahui P0 = 36.000.000, r = 0,02, dan t = 2020 - 2015 = 5. Maka P(5) = 36.000.000(1,02)^5 = 36.000.000(1,1040808) ≈ 39.746.909.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus pertumbuhan eksponensial yang sudah dipelajari untuk menyelesaikan masalah kontekstual.. Bukti: menggunakan model pertumbuhan eksponensial f(x)=36.000.000(1,02)^x; berapa banyak kasus yang terjadi pada tahun 2020
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau prosedur perhitungan pertumbuhan eksponensial untuk mendapatkan hasil.. Bukti: peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman model eksponensial dan penentuan variabel waktu yang tepat. Prosedur standar untuk kelas 10.. Bukti: 36 juta jiwa; meningkat rata-rata 2% setiap tahun; tahun 2020

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep fungsi eksponensial dan pertumbuhan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji kemampuan siswa dalam menerapkan model pertumbuhan eksponensial pada konteks nyata dengan langkah-langkah yang terstruktur. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3899`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi model pertumbuhan eksponensial yang tepat dan menerapkan prosedur substitusi nilai ke dalam rumus tersebut untuk menyelesaikan masalah kontekstual.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritma atau prosedur perhitungan pertumbuhan eksponensial untuk mendapatkan hasil.
- Intended difficulty `Easy`: Soal ini merupakan penerapan rutin dari rumus pertumbuhan eksponensial. Siswa perlu mengidentifikasi nilai awal, laju pertumbuhan, dan selisih waktu (x=5), kemudian melakukan perhitungan. Ini adalah prosedur standar yang familiar bagi siswa kelas 10.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Sesuai untuk kelas 10 karena merupakan aplikasi langsung dari materi fungsi eksponensial yang diajarkan di jenjang tersebut. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Model peluruhan eksponensial: M(t) = M0(1 - r)^t. Diketahui M0 = 0,3 kg, r = 0,15, t = 8. Maka M(8) = 0,3 * (1 - 0,15)^8 = 0,3 * (0,85)^8. (0,85)^8 ≈ 0,27249. M(8) = 0,3 * 0,27249 ≈ 0,081747 kg. Opsi D (0,08172 kg) adalah jawaban yang paling mendekati dengan pembulatan yang konsisten.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c85c8e9354aaeaf878d798bdccc7b5395bd890052c15c64d0b6f162fa709aae7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2221 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2197 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2234 |

Run 1 — solusi: Model peluruhan eksponensial: f(t) = M0 * (1 - r)^t. Diketahui M0 = 0,3 kg, r = 0,15, dan t = 8. Maka f(8) = 0,3 * (0,85)^8. (0,85)^8 ≈ 0,27243. f(8) = 0,3 * 0,27243 ≈ 0,081729 kg.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model peluruhan eksponensial dari narasi, menentukan basis peluruhan (1-r), dan menerapkan rumus f(t)=a(b)^t. Ini adalah penerapan konsep fungsi eksponensial pada situasi rutin.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip peluruhan eksponensial dan bagaimana variabel dalam fungsi tersebut merepresentasikan sisa massa.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; Fungsi f(x)=0,3(0,85)^x sudah menyatakan massa yang tersisa
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus menerjemahkan narasi menjadi model matematika f(t)=a(1-r)^t dan melakukan perhitungan eksponensial. Meskipun prosedural, terdapat pemilihan model yang tepat.. Bukti: Massa suatu zat radioaktif adalah 0,3 kg; Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; 8 jam kemudian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan persentase. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10, menguji pemahaman fungsi eksponensial dalam konteks peluruhan yang merupakan materi standar. |

Run 2 — solusi: Model peluruhan eksponensial adalah M(t) = M0(1 - r)^t. Dengan M0 = 0,3 kg, r = 0,15, dan t = 8, maka M(8) = 0,3 * (1 - 0,15)^8 = 0,3 * (0,85)^8. Hasil perhitungan 0,3 * 0,27249... ≈ 0,081747 kg. Opsi D (0,08172 kg) adalah jawaban yang paling mendekati dengan pembulatan yang konsisten.
- Domain kognitif `classify/applying`: Siswa perlu memilih model fungsi eksponensial yang tepat untuk situasi peluruhan (applying) dan menerapkan rumus M(t) = M0(1-r)^t untuk menyelesaikan masalah rutin.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep peluruhan eksponensial sebagai hubungan matematis antara waktu dan massa zat yang tersisa.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus peluruhan eksponensial. Siswa hanya perlu mengidentifikasi variabel (M0, r, t) dan melakukan perhitungan aritmetika sederhana.. Bukti: Massa suatu zat radioaktif adalah 0,3 kg; Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; 8 jam kemudian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi eksponensial adalah standar kelas 10. Soal ini bersifat rutin dan tidak memerlukan strategi kompleks. |

Run 3 — solusi: Model peluruhan eksponensial: M(t) = M0 * (1 - r)^t. Diketahui M0 = 0,3 kg, r = 0,15, dan t = 8. Maka M(8) = 0,3 * (1 - 0,15)^8 = 0,3 * (0,85)^8. Hasil perhitungan: 0,3 * 0,27249... ≈ 0,081747... kg. Pembulatan yang sesuai dengan opsi D adalah 0,08172 kg.
- Domain kognitif `classify/applying`: Siswa perlu memilih model fungsi eksponensial yang tepat untuk peluruhan (M = M0(1-r)^t) dan menerapkan nilai yang diberikan ke dalam rumus tersebut. Ini adalah penerapan prosedur rutin dalam konteks masalah nyata.. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep peluruhan eksponensial sebagai hubungan antara variabel waktu dan massa zat, serta bagaimana menerjemahkan persentase peluruhan menjadi faktor pengali (1-r).. Bukti: Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi model peluruhan yang tepat, mengubah persentase menjadi faktor peluruhan, dan melakukan perhitungan eksponensial. Meskipun prosedurnya rutin, terdapat potensi kesalahan dalam memahami bahwa fungsi sudah menyatakan sisa massa, bukan jumlah yang meluruh.. Bukti: Massa suatu zat radioaktif adalah 0,3 kg; Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam; 8 jam kemudian

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan pemodelan fungsi eksponensial sederhana yang merupakan standar kurikulum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4068`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi model peluruhan eksponensial dari narasi, menentukan basis peluruhan (1-r), dan menerapkan rumus f(t)=a(b)^t. Ini adalah penerapan konsep fungsi eksponensial pada situasi rutin.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami konsep peluruhan eksponensial sebagai hubungan matematis antara waktu dan massa zat yang tersisa, serta menerjemahkan persentase peluruhan menjadi faktor pengali.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus menerjemahkan narasi menjadi model matematika f(t)=a(1-r)^t dan melakukan perhitungan eksponensial. Meskipun prosedural, terdapat pemilihan model yang tepat dan potensi kesalahan dalam memahami bahwa fungsi sudah menyatakan sisa massa.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10, menguji pemahaman fungsi eksponensial dalam konteks peluruhan yang merupakan materi standar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Ubah bentuk akar ke eksponen pecahan: 5x^(5/2) * 3x^(1/3). Kalikan koefisien: 5 * 3 = 15. Jumlahkan eksponen: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c288a2c40c1296d6d66829d50d9622f6d882ca5540631440028d183c39dbbfb2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2061 |
| 2 | success | valid / verified | applying | procedural | Easy | 2057 |
| 3 | success | valid / verified | applying | procedural | Medium | 2054 |

Run 1 — solusi: (5x^(5/2)) * (3x^(1/3)) = (5 * 3) * x^(5/2 + 1/3) = 15 * x^(15/6 + 2/6) = 15x^(17/6)
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian eksponen dengan basis yang sama dan mengonversi bentuk akar ke eksponen pecahan. Ini adalah prosedur rutin yang melibatkan pemilihan aturan eksponen yang tepat.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik manipulasi aljabar (eksponen pecahan dan sifat perkalian eksponen).. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah rutin yang saling terkait: mengonversi akar ke eksponen pecahan dan menjumlahkan pecahan pangkat dengan penyebut berbeda. Ini bukan sekadar operasi satu langkah.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dan operasi penjumlahan pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan manipulasi aljabar dasar ini sebagai bagian dari materi eksponen dan bentuk akar. |

Run 2 — solusi: Ubah bentuk akar ke eksponen pecahan: 5x^(5/2) * 3x^(1/3). Kalikan koefisien: 5 * 3 = 15. Jumlahkan eksponen: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian eksponen dan mengubah bentuk akar menjadi eksponen pecahan. Ini adalah prosedur rutin yang dipelajari di kelas 10.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma operasi aljabar pada eksponen dan bentuk akar.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini memerlukan konversi bentuk akar ke eksponen pecahan dan penjumlahan pecahan, yang merupakan prosedur standar dan familiar bagi siswa kelas 10.. Bukti: (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dan operasi pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponen dan bentuk akar adalah kurikulum standar kelas 10. Prosedur yang diminta bersifat langsung tanpa jebakan konseptual yang rumit. |

Run 3 — solusi: Ubah bentuk akar ke eksponen pecahan: 5x^(5/2) * 3x^(1/3). Kalikan koefisien: 5 * 3 = 15. Jumlahkan eksponen: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian eksponen dengan basis yang sama dan mengubah bentuk akar menjadi eksponen pecahan. Ini adalah prosedur rutin dalam aljabar kelas 10.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang aturan eksponen dan konversi bentuk akar, yang merupakan pengetahuan prosedural.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah rutin: konversi akar ke eksponen dan penjumlahan pecahan pada eksponen. Tidak ada strategi non-rutin atau kendala kompleks.. Bukti: (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan eksponen dasar dan operasi penjumlahan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan manipulasi aljabar dasar yang merupakan standar kurikulum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3615`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan aturan perkalian eksponen dengan basis yang sama dan mengonversi bentuk akar ke eksponen pecahan. Ini adalah prosedur rutin yang melibatkan pemilihan aturan eksponen yang tepat.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik manipulasi aljabar (eksponen pecahan dan sifat perkalian eksponen).
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: mengonversi akar ke eksponen pecahan dan menjumlahkan pecahan pangkat dengan penyebut berbeda. Ini bukan sekadar operasi satu langkah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dan operasi penjumlahan pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan manipulasi aljabar dasar ini sebagai bagian dari materi eksponen dan bentuk akar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Rasionalkan dengan mengalikan pembilang dan penyebut dengan sekawan (√3 - √5): 2/(√3+√5) * (√3-√5)/(√3-√5) = 2(√3-√5) / (3-5) = 2(√3-√5) / -2 = -(√3-√5) = √5-√3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b87ce145a8f1f332623ce3cedb8b9c089fbb02b8dd8734e36c3cc18a29aaec0a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2027 |
| 2 | success | valid / verified | applying | procedural | Easy | 1981 |
| 3 | success | valid / verified | applying | procedural | Easy | 1998 |

Run 1 — solusi: Rasionalkan dengan mengalikan pembilang dan penyebut dengan sekawan (√3 - √5): 2/(√3+√5) * (√3-√5)/(√3-√5) = 2(√3-√5) / (3-5) = 2(√3-√5) / -2 = -(√3-√5) = √5-√3.
- Domain kognitif `classify/applying`: Soal ini meminta siswa menerapkan prosedur standar merasionalkan penyebut bentuk akar. Siswa perlu memilih sekawan yang tepat dan melakukan operasi aljabar dasar. Ini adalah penerapan prosedur rutin.. Bukti: Rasionalkan bentuk berikut ini.; 2/(√3+√5)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep sekawan bentuk akar (a+b)(a-b) = a^2-b^2 dan menerapkannya dalam algoritma merasionalkan penyebut.. Bukti: Rasionalkan bentuk berikut ini.; 2/(√3+√5)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Prosedur merasionalkan penyebut dengan sekawan adalah materi standar yang diajarkan secara eksplisit. Beban komputasi rendah dan langkah-langkahnya linear.. Bukti: 2/(√3+√5)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan sifat bentuk akar (sekawan). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Merasionalkan penyebut adalah keterampilan dasar dalam materi bentuk akar kelas 10 yang bersifat prosedural dan familiar. |

Run 2 — solusi: Rasionalkan dengan mengalikan pembilang dan penyebut dengan sekawan (√5-√3) atau (√3-√5). Menggunakan (√5-√3): 2(√5-√3) / (5-3) = 2(√5-√3) / 2 = √5-√3.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur rutin merasionalkan penyebut bentuk akar. Siswa perlu memilih faktor sekawan yang tepat dan melakukan operasi aljabar dasar.. Bukti: Rasionalkan bentuk berikut ini.; 2/(√3+√5)
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami prinsip merasionalkan penyebut (konsep) dan menerapkan algoritma perkalian sekawan (prosedural).. Bukti: Rasionalkan bentuk berikut ini.; 2/(√3+√5)
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang diajarkan di kelas 10. Langkah-langkahnya rutin (mengalikan sekawan, menyederhanakan pecahan) tanpa memerlukan strategi non-rutin.. Bukti: 2/(√3+√5)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar bentuk akar dan perkalian sekawan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Merasionalkan penyebut adalah materi dasar kelas 10 yang bersifat prosedural dan familiar. |

Run 3 — solusi: Rasionalkan dengan mengalikan pembilang dan penyebut dengan sekawan (√3 - √5): 2/(√3+√5) * (√3-√5)/(√3-√5) = 2(√3-√5) / (3-5) = 2(√3-√5) / -2 = -(√3-√5) = √5-√3.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur standar merasionalkan penyebut bentuk akar. Ini adalah tugas rutin yang memerlukan pemilihan prosedur (perkalian sekawan) dan eksekusi aljabar dasar.. Bukti: Rasionalkan bentuk berikut ini.; 2/(√3+√5)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip merasionalkan penyebut (konsep) dan menerapkan algoritma perkalian sekawan (prosedural).. Bukti: Rasionalkan bentuk berikut ini.; 2/(√3+√5)
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang diajarkan di kelas 10. Tidak ada strategi non-rutin atau kendala kompleks. Beban perhitungan rendah.. Bukti: Rasionalkan bentuk berikut ini.; 2/(√3+√5)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan sifat bentuk akar (sekawan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Merasionalkan penyebut adalah materi dasar kelas 10 yang bersifat prosedural rutin. |

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
Solusi minimum hasil AI: Bilangan 34.000.000.000 ditulis sebagai 3,4 dikali 10 pangkat n. Karena koma digeser 10 posisi ke kiri dari posisi awal (di belakang nol terakhir), maka n = 10. Hasilnya adalah 3,4 x 10^10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4cf449ed663d7de794416ee7c32821b0348110953aee87ba3539fa6ef38f6cbc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1943 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1918 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1907 |

Run 1 — solusi: Bilangan 34.000.000.000 memiliki 11 digit. Untuk mengubah ke bentuk baku a x 10^n dengan 1 <= a < 10, kita geser koma 10 kali ke kiri sehingga diperoleh 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan konversi langsung bilangan desimal besar ke notasi ilmiah (bentuk baku). Ini adalah prosedur standar yang diajarkan di kelas 10, tidak memerlukan strategi nonrutin.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma atau aturan penulisan bentuk baku (a x 10^n) untuk mengubah representasi bilangan.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah konversi yang familiar bagi siswa kelas 10. Tidak ada kendala kompleks atau integrasi konsep.. Bukti: 34.000.000.000

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
| gradeRelativeRationale | Konversi bilangan ke bentuk baku adalah materi dasar yang rutin di kelas 10, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Bilangan 34.000.000.000 memiliki 10 angka di belakang angka 3. Maka, 34.000.000.000 = 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi bentuk baku (notasi ilmiah) dengan menghitung jumlah pergeseran desimal, yang merupakan prosedur standar dan langsung.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang aturan penulisan notasi ilmiah (bentuk baku) yang merupakan konsep dasar dalam aljabar.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah konversi, tanpa kendala tambahan atau kompleksitas representasi.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep notasi ilmiah (bentuk baku) dan nilai tempat bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penulisan bentuk baku adalah materi dasar kelas 10 yang bersifat prosedural dan rutin. |

Run 3 — solusi: Bilangan 34.000.000.000 memiliki 10 angka di belakang angka pertama (3). Maka, 34.000.000.000 = 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Soal meminta siswa mengubah bilangan desimal besar ke bentuk notasi ilmiah (bentuk baku). Ini adalah prosedur standar yang langsung dan rutin.. Bukti: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami definisi bentuk baku (a x 10^n dengan 1 <= a < 10) dan menerapkan algoritma penghitungan pergeseran koma desimal.. Bukti: Buat bilangan berikut dalam bentuk baku
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung tanpa jebakan atau kompleksitas tambahan. Siswa hanya perlu menghitung jumlah digit untuk menentukan eksponen.. Bukti: 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi ilmiah dan sistem bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bentuk baku adalah materi dasar kelas 10 yang bersifat prosedural dan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3461`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung prosedur penulisan notasi ilmiah. Siswa hanya perlu mengenali definisi bentuk baku dan menghitung pergeseran desimal, yang merupakan proses rutin.
- Dimensi pengetahuan `procedural`: Siswa menerapkan algoritma atau aturan penulisan bentuk baku (a x 10^n) untuk mengubah representasi bilangan desimal besar.
- Intended difficulty `Easy`: Soal ini bersifat prosedural langsung dengan satu langkah konversi yang familiar bagi siswa kelas 10. Tidak ada kendala kompleks atau integrasi konsep.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Konversi bilangan ke bentuk baku adalah materi dasar yang rutin di kelas 10, sehingga tingkat kesulitannya rendah. |

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
| 1 | success | valid / verified | applying | procedural | Easy | 2079 |
| 2 | success | valid / verified | applying | procedural | Easy | 2112 |
| 3 | success | valid / verified | applying | procedural | Easy | 2112 |

Run 1 — solusi: Barisan aritmetika dengan suku pertama a=3 dan beda b=2. Rumus suku ke-n adalah Un = a + (n-1)b. Untuk n=10, U10 = 3 + (10-1)2 = 3 + 18 = 21.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola barisan aritmetika dari data yang diberikan dan menerapkan rumus suku ke-n untuk menentukan nilai pada posisi tertentu.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus barisan aritmetika untuk menyelesaikan masalah pola bilangan.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Prosedur penyelesaiannya langsung menggunakan rumus barisan aritmetika tanpa memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; hingga sepuluh temannya mendapat permen

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
| gradeRelativeRationale | Materi barisan aritmetika adalah topik standar kelas 10. Soal ini menguji kemampuan dasar dalam mengidentifikasi pola dan menerapkan rumus, yang merupakan kompetensi dasar. |

Run 2 — solusi: Barisan aritmetika dengan suku pertama a=3 dan beda b=2. Rumus suku ke-n adalah Un = a + (n-1)b. Untuk n=10, U10 = 3 + (10-1)2 = 3 + 18 = 21.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola barisan aritmetika dari data yang diberikan dan menerapkan rumus suku ke-n untuk menentukan nilai pada posisi tertentu. Ini adalah penerapan prosedur rutin.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma barisan aritmetika (prosedur) untuk menyelesaikan masalah.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang langsung dapat diselesaikan dengan rumus barisan aritmetika standar tanpa memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?

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
| gradeRelativeRationale | Materi barisan aritmetika adalah topik standar kelas 10. Soal ini menguji pemahaman langsung terhadap rumus tanpa modifikasi atau konteks yang membingungkan. |

Run 3 — solusi: Barisan aritmetika dengan suku pertama a=3 dan beda b=2. Rumus suku ke-n adalah Un = a + (n-1)b. Untuk teman kesepuluh (n=10), maka U10 = 3 + (10-1)2 = 3 + 18 = 21.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola barisan aritmetika dari data yang diberikan dan menerapkan rumus suku ke-n untuk menentukan nilai pada posisi tertentu. Ini adalah penerapan prosedur rutin.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma barisan aritmetika (prosedural) untuk menyelesaikan masalah yang terstruktur.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali pola aritmetika sederhana dan menerapkan rumus suku ke-n tanpa kendala tambahan atau strategi non-rutin.. Bukti: Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen.; Berapa permen yang didapat oleh teman kesepuluh?

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
| gradeRelativeRationale | Soal ini sangat standar untuk kelas 10, menguji pemahaman dasar barisan aritmetika yang merupakan materi prasyarat atau awal di jenjang ini. |

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
Solusi minimum hasil AI: Barisan aritmetika dengan suku pertama a=5 dan beda b=-2-5=-7. Suku ke-n dirumuskan Un = a + (n-1)b. Maka U50 = 5 + (50-1)(-7) = 5 + 49(-7) = 5 - 343 = -338.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c65e9fe8bb06dd8f59b85aabf2e8be32a2823efb62db7603e43476016ff121ff`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1935 |
| 2 | success | valid / verified | applying | procedural | Easy | 1955 |
| 3 | success | valid / verified | applying | procedural | Easy | 1934 |

Run 1 — solusi: Barisan aritmetika dengan suku pertama a=5 dan beda b=-2-5=-7. Suku ke-n dirumuskan Un = a + (n-1)b. Maka U50 = 5 + (50-1)(-7) = 5 + 49(-7) = 5 - 343 = -338.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus umum barisan aritmetika yang sudah dipelajari untuk menentukan suku ke-n. Proses ini bersifat rutin dan langsung menggunakan prosedur yang telah ditetapkan.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma atau urutan langkah (rumus suku ke-n) untuk menyelesaikan masalah barisan aritmetika.. Bukti: Un=a+(n-1)b
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam barisan aritmetika. Siswa hanya perlu mengidentifikasi suku pertama dan beda, lalu memasukkannya ke dalam rumus yang familiar.. Bukti: 5, –2, –9, –16, …; Tentukan suku ke-50

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
| gradeRelativeRationale | Materi barisan aritmetika adalah topik dasar kelas 10. Soal ini tidak memerlukan modifikasi strategi atau pemikiran kompleks, hanya aplikasi rumus langsung. |

Run 2 — solusi: Barisan aritmetika dengan suku pertama a = 5 dan beda b = -2 - 5 = -7. Rumus suku ke-n adalah Un = a + (n-1)b. Maka, U50 = 5 + (50-1)(-7) = 5 + 49(-7) = 5 - 343 = -338.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus suku ke-n barisan aritmetika yang sudah dipelajari di kelas 10. Siswa hanya perlu mengidentifikasi suku pertama dan beda, lalu mensubstitusikannya ke rumus.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman siswa terhadap algoritma atau prosedur standar untuk menentukan suku ke-n pada barisan aritmetika.. Bukti: Un=a+(n-1)b
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu prosedur standar (menentukan beda dan menggunakan rumus Un) tanpa memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: 5, –2, –9, –16, …; Tentukan suku ke-50

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep barisan aritmetika dan operasi bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi barisan aritmetika adalah materi dasar kelas 10. Soal ini tidak memiliki jebakan konseptual yang rumit, hanya menuntut ketelitian dalam operasi aritmetika dasar. |

Run 3 — solusi: Barisan aritmetika dengan suku pertama a = 5 dan beda b = -2 - 5 = -7. Rumus suku ke-n adalah Un = a + (n-1)b. Maka, U50 = 5 + (50-1)(-7) = 5 + 49(-7) = 5 - 343 = -338.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus umum barisan aritmetika untuk menentukan suku ke-n. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan urutan langkah dalam menentukan suku ke-n barisan aritmetika.. Bukti: 5, –2, –9, –16, …; Un=a+(n-1)b
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi suku pertama dan beda, lalu memasukkannya ke dalam rumus yang sudah dikenal.. Bukti: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …

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
| gradeRelativeRationale | Materi barisan aritmetika adalah standar kelas 10. Prosedur yang digunakan sangat mendasar dan tidak memerlukan strategi non-rutin. |

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
Soal: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
Pilihan: A. -338
B. 348
C. -345
D. -331
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Bilangan kelipatan 4 antara 10 dan 99 adalah 12, 16, ..., 96. Ini adalah deret aritmetika dengan a=12, b=4, dan Un=96. Mencari n: 96 = 12 + (n-1)4, maka 84 = (n-1)4, n-1 = 21, n = 22. Jumlah Sn = n/2(a + Un) = 22/2(12 + 96) = 11(108) = 1.188.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `63cee9a089d2ca6dafe44512844a56b6af81c700b0720018d8e52a21ddf411d9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2113 |
| 2 | success | valid / verified | applying | procedural | Easy | 2134 |
| 3 | success | valid / verified | applying | procedural | Medium | 2128 |

Run 1 — solusi: Bilangan kelipatan 4 antara 10 dan 99 adalah 12, 16, ..., 96. Ini adalah deret aritmetika dengan a=12, b=4, dan Un=96. Un = a + (n-1)b => 96 = 12 + (n-1)4 => 84 = (n-1)4 => 21 = n-1 => n=22. Jumlah Sn = n/2(a + Un) = 22/2(12 + 96) = 11(108) = 1.188.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola bilangan sebagai deret aritmetika, menentukan suku pertama dan terakhir yang memenuhi syarat, menghitung banyak suku, dan menerapkan rumus jumlah deret. Ini adalah penerapan prosedur rutin.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman konsep deret aritmetika dan prosedur perhitungan jumlah deret.. Bukti: jumlah bilangan kelipatan 4; di antara bilangan 10 dan 99
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang melibatkan identifikasi batas deret dan penggunaan rumus standar. Tidak ada kendala non-rutin atau integrasi representasi yang kompleks.. Bukti: jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar barisan dan deret aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi deret aritmetika adalah standar kelas 10. Soal ini menguji pemahaman dasar tentang batas interval dan rumus jumlah, yang merupakan prosedur standar. |

Run 2 — solusi: Bilangan kelipatan 4 antara 10 dan 99 membentuk deret aritmetika: 12, 16, ..., 96. Suku pertama (a) = 12, beda (b) = 4, suku terakhir (Un) = 96. Mencari banyak suku (n): 96 = 12 + (n-1)4 => 84 = (n-1)4 => 21 = n-1 => n = 22. Jumlah (Sn) = n/2 * (a + Un) = 22/2 * (12 + 96) = 11 * 108 = 1.188.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola bilangan sebagai deret aritmetika, menentukan suku pertama dan terakhir, menghitung banyak suku, dan menerapkan rumus jumlah deret. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami konsep deret aritmetika dan bagaimana menerjemahkan batasan 'di antara 10 dan 99' menjadi suku pertama dan terakhir yang tepat dalam deret.. Bukti: jumlah bilangan kelipatan 4; di antara bilangan 10 dan 99
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Memerlukan identifikasi suku pertama dan terakhir, perhitungan jumlah suku, dan penggunaan rumus jumlah deret aritmetika standar.. Bukti: jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar barisan dan deret aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi deret aritmetika adalah kurikulum standar kelas 10. Prosedur yang digunakan sangat langsung dan familiar. |

Run 3 — solusi: Bilangan kelipatan 4 antara 10 dan 99 adalah 12, 16, ..., 96. Ini adalah deret aritmetika dengan a=12, b=4, dan Un=96. Un = a + (n-1)b => 96 = 12 + (n-1)4 => 84 = (n-1)4 => 21 = n-1 => n=22. Jumlah (Sn) = n/2 * (a + Un) = 22/2 * (12 + 96) = 11 * 108 = 1.188.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola bilangan, menentukan suku pertama dan terakhir, menghitung banyaknya suku (n), dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur rutin.. Bukti: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang konsep barisan dan deret aritmetika serta kemampuan menerapkan algoritma penjumlahan deret.. Bukti: jumlah bilangan kelipatan 4; di antara bilangan 10 dan 99
- Intended difficulty `classify/Medium`: Soal ini merupakan masalah rutin yang melibatkan identifikasi suku pertama/terakhir, penentuan n, dan perhitungan jumlah. Prosedur ini standar untuk kelas 10.. Bukti: jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep barisan dan deret aritmetika, operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi deret aritmetika adalah kurikulum standar kelas 10. Soal ini menguji pemahaman batas interval dan rumus deret, yang merupakan tugas rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3870`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi pola bilangan sebagai deret aritmetika, menentukan suku pertama dan terakhir yang memenuhi syarat, menghitung banyak suku, dan menerapkan rumus jumlah deret. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal memerlukan pemahaman konsep deret aritmetika dan prosedur perhitungan jumlah deret.
- Intended difficulty `Easy`: Soal ini merupakan masalah rutin yang melibatkan identifikasi batas deret dan penggunaan rumus standar. Tidak ada kendala non-rutin atau integrasi representasi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar barisan dan deret aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi deret aritmetika adalah standar kelas 10. Soal ini menguji pemahaman dasar tentang batas interval dan rumus jumlah, yang merupakan prosedur standar. |

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

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Deret aritmetika dengan a=2, b=3, n=7. Suku ke-7 (U7) = 2 + (7-1)3 = 20. Jumlah 7 suku pertama (S7) = (n/2)(a + U7) = (7/2)(2 + 20) = 7/2 * 22 = 77.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a604cc5713e90151ec1f483ab1f4325a4f4e9d49cb8ee932a8392870beee7463`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2174 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2143 |
| 3 | success | valid / verified | applying | procedural | Easy | 2204 |

Run 1 — solusi: Ini adalah deret aritmetika dengan suku pertama a=2, beda b=3, dan n=7. Suku ke-7 (U7) = a + (n-1)b = 2 + 6(3) = 20. Jumlah 7 suku pertama (S7) = n/2 * (a + Un) = 7/2 * (2 + 20) = 7/2 * 22 = 7 * 11 = 77.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola sebagai deret aritmetika, menentukan parameter (a, b, n), dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang rumus deret aritmetika untuk menyelesaikan masalah.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang melibatkan identifikasi deret aritmetika dan penggunaan rumus jumlah suku. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Vina membagikan permen kepada tujuh temannya; Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya

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
| gradeRelativeRationale | Materi deret aritmetika adalah topik standar kelas 10. Soal ini menguji pemahaman langsung terhadap rumus jumlah deret tanpa variasi yang rumit. |

Run 2 — solusi: Ini adalah deret aritmetika dengan suku pertama a = 2, beda b = 3, dan jumlah suku n = 7. Rumus jumlah n suku pertama: Sn = n/2 * (2a + (n-1)b). S7 = 7/2 * (2(2) + (7-1)3) = 7/2 * (4 + 18) = 7/2 * 22 = 7 * 11 = 77.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola sebagai deret aritmetika, menentukan parameter (a, b, n), dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara pola bilangan dan konsep deret aritmetika untuk menyelesaikan masalah.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Intended difficulty `classify/Easy`: Soal ini memerlukan identifikasi pola aritmetika dan penggunaan rumus jumlah deret. Langkah-langkahnya rutin dan langsung, sesuai untuk tingkat kelas 10.. Bukti: Vina membagikan permen kepada tujuh temannya; Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.

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
| gradeRelativeRationale | Soal ini adalah aplikasi langsung dari rumus deret aritmetika yang merupakan materi standar kelas 10, dengan beban kognitif rendah. |

Run 3 — solusi: Ini adalah deret aritmetika dengan suku pertama a=2, beda b=3, dan jumlah suku n=7. Suku ke-7 (U7) = a + (n-1)b = 2 + 6(3) = 20. Jumlah 7 suku pertama (S7) = n/2 * (a + Un) = 7/2 * (2 + 20) = 7/2 * 22 = 7 * 11 = 77.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola sebagai deret aritmetika, menentukan parameter (a, b, n), dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antar suku dalam deret aritmetika dan penggunaan rumus jumlah deret (prosedural) untuk menyelesaikan masalah.. Bukti: setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya; Berapa permen yang harus Vina siapkan?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Prosedur yang diperlukan jelas (menghitung jumlah deret aritmetika) dengan beban kognitif rendah dan tidak ada jebakan konseptual yang kompleks.. Bukti: Vina membagikan permen kepada tujuh temannya; Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen.; setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya

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
| gradeRelativeRationale | Materi deret aritmetika adalah kurikulum standar kelas 10. Soal ini menggunakan konteks sederhana yang langsung mengarah pada penggunaan rumus deret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3983`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi pola sebagai deret aritmetika, menentukan parameter (a, b, n), dan menerapkan rumus jumlah deret aritmetika. Ini adalah penerapan prosedur rutin pada situasi kontekstual.
- Dimensi pengetahuan `procedural`: Siswa menggunakan pengetahuan prosedural tentang rumus deret aritmetika untuk menyelesaikan masalah.
- Intended difficulty `Easy`: Soal ini merupakan masalah rutin yang melibatkan identifikasi deret aritmetika dan penggunaan rumus jumlah suku. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Materi deret aritmetika adalah topik standar kelas 10. Soal ini menguji pemahaman langsung terhadap rumus jumlah deret tanpa variasi yang rumit. |

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
Solusi minimum hasil AI: Firman (bunga tunggal): 10.000.000 + (5 * 0,03 * 10.000.000) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1,03)^5 ≈ 11.592.741. Selisih: 11.592.741 - 11.500.000 = 92.741. Gigih memiliki uang lebih banyak.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `73f3351ee4d9f0b53cfb5097340e87933a59ef01911d9a977ad8a868ee7393ff`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2390 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2393 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2400 |

Run 1 — solusi: Firman (bunga tunggal): 10.000.000 + (5 * 0,03 * 10.000.000) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1,03)^5 ≈ 11.592.741. Selisih: 11.592.741 - 11.500.000 = 92.741. Gigih memiliki uang lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan konsep antara bunga tunggal dan bunga majemuk, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan untuk membandingkan hasil akhir.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga tunggal; Gigih... menambahkan bunganya ke dalam nilai depositonya... bunga majemuk; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bunga tunggal dan bunga majemuk bekerja serta prosedur perhitungan yang berbeda untuk keduanya.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus membedakan dua konsep bunga yang berbeda, menerapkan dua rumus yang berbeda, dan melakukan perhitungan yang melibatkan eksponen (untuk bunga majemuk) serta perbandingan nilai.. Bukti: Firman menyimpan uang sejumlah Rp10.000.000,00; bunga 3% per tahun; Setelah lima tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase, operasi aritmetika, dan konsep bunga tunggal vs majemuk. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena materi bunga majemuk dan tunggal merupakan bagian dari kurikulum matematika keuangan di jenjang ini. |

Run 2 — solusi: Firman (bunga tunggal): 10.000.000 * (1 + 5 * 0,03) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1,03)^5 = 11.592.740,74. Selisih: 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan konsep bunga tunggal dan bunga majemuk, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan untuk membandingkan hasilnya.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga tunggal; Gigih... menambahkan bunganya ke dalam nilai depositonya... bunga majemuk; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbedaan mekanisme bunga tunggal dan bunga majemuk, serta prosedur perhitungan yang sesuai untuk masing-masing.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua perhitungan rutin yang berbeda (bunga tunggal dan majemuk) dan perbandingan hasil. Ini adalah tugas standar untuk kelas 10.. Bukti: Firman menyimpan uang sejumlah Rp10.000.000,00; bunga 3% per tahun; Setelah lima tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase, bunga tunggal, dan bunga majemuk. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan dan menghitung bunga tunggal dan majemuk sebagai bagian dari materi keuangan. |

Run 3 — solusi: Firman (bunga tunggal): 10.000.000 * (1 + 5 * 0,03) = 11.500.000. Gigih (bunga majemuk): 10.000.000 * (1,03)^5 = 11.592.740,74. Selisih: 11.592.741 - 11.500.000 = 92.741.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan konsep bunga tunggal dan majemuk, memilih rumus yang tepat untuk masing-masing, dan melakukan perhitungan untuk membandingkan hasilnya.. Bukti: Firman menyimpan uang... bunga 3% per tahun... bunga tunggal; Gigih... menambahkan bunganya ke dalam nilai depositonya... bunga majemuk; Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bunga tunggal dan bunga majemuk bekerja serta prosedur perhitungan yang berbeda untuk keduanya.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua prosedur perhitungan yang berbeda (bunga tunggal dan majemuk) dan perbandingan hasil, yang merupakan langkah rutin namun membutuhkan ketelitian dalam pemilihan rumus.. Bukti: Firman menyimpan uang sejumlah Rp10.000.000,00; bunga 3% per tahun; Setelah lima tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persentase, operasi aritmetika, dan konsep bunga tunggal vs majemuk. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena membandingkan dua model pertumbuhan uang yang merupakan materi standar kurikulum. |

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
Solusi minimum hasil AI: Modal awal = Rp10.000.000,00. Bunga 1 tahun = 3% x 10.000.000 = Rp300.000,00. Total uang = Modal awal + Bunga = 10.000.000 + 300.000 = Rp10.300.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `116707bad64d19a7d9242bcace42094990bcac9d875fe9e8421a2d795b4319ef`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2136 |
| 2 | success | valid / verified | applying | procedural | Easy | 2065 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2132 |

Run 1 — solusi: Modal awal = Rp10.000.000,00. Bunga 1 tahun = 3% x 10.000.000 = Rp300.000,00. Total uang = Modal awal + Bunga = 10.000.000 + 300.000 = Rp10.300.000,00.
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan konsep dasar persentase bunga dan menambahkannya ke modal awal. Ini adalah prosedur rutin yang langsung.. Bukti: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun.; Berapa uang Gigih setelah satu tahun?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang perhitungan bunga sederhana/majemuk untuk periode satu tahun.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu operasi persentase dan satu operasi penjumlahan. Tidak ada kompleksitas tambahan.. Bukti: deposito sejumlah Rp10.000.000,00; bunga 3% per tahun; setelah satu tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan konsep persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai pengenalan atau pemanasan materi bunga/keuangan. |

Run 2 — solusi: Modal awal = 10.000.000. Bunga 1 tahun = 3% * 10.000.000 = 300.000. Total uang = 10.000.000 + 300.000 = 10.300.000.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep bunga sederhana/majemuk untuk menghitung nilai akhir setelah satu periode. Ini adalah prosedur rutin yang melibatkan pemahaman dasar tentang persentase dan penambahan nilai.. Bukti: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun.; Berapa uang Gigih setelah satu tahun?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana bunga dihitung dan ditambahkan ke modal awal.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dengan satu periode waktu dan satu operasi utama (persentase dan penjumlahan). Tidak ada kompleksitas tambahan.. Bukti: Rp10.000.000,00; bunga 3% per tahun; setelah satu tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar persentase dan operasi aritmetika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 10, hanya memerlukan satu langkah perhitungan bunga dan penambahan ke modal. |

Run 3 — solusi: Modal awal = Rp10.000.000,00. Bunga 1 tahun = 3% x 10.000.000 = Rp300.000,00. Total uang = 10.000.000 + 300.000 = Rp10.300.000,00.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep bunga sederhana/majemuk untuk menghitung total nilai setelah satu periode. Ini adalah prosedur rutin yang langsung.. Bukti: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun.; Berapa uang Gigih setelah satu tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip bunga dan bagaimana bunga ditambahkan ke modal awal.. Bukti: bunga 3% per tahun; menambahkan bunganya ke dalam nilai depositonya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu operasi perhitungan persentase dan penjumlahan. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: deposito sejumlah Rp10.000.000,00; bunga 3% per tahun; setelah satu tahun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai pengenalan atau pemanasan materi bunga, karena hanya melibatkan satu periode waktu. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3612`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep bunga untuk menghitung nilai akhir setelah satu periode. Ini adalah prosedur rutin yang langsung.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang perhitungan bunga dan penambahan ke modal awal.
- Intended difficulty `Easy`: Soal ini sangat mendasar, hanya melibatkan satu operasi perhitungan persentase dan penjumlahan. Tidak ada kendala kompleks atau strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman persentase. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai pengenalan atau pemanasan materi bunga, karena hanya melibatkan satu periode waktu. |

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
Solusi minimum hasil AI: Samakan rasio sirup per 1 liter air: (1) 2/3 liter sirup/liter air = 0,67. (2) Rasio air:sirup = 2:3, maka sirup/air = 3/2 = 1,5. (3) 2/3 campuran adalah air, maka 1/3 adalah sirup. Rasio sirup/air = (1/3)/(2/3) = 0,5. Campuran (2) memiliki rasio sirup tertinggi (1,5), sehingga paling manis.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6f37fe93441a0e97659392b476689468b41d151706de1077ec8606cb84e9e67d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2278 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2336 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2216 |

Run 1 — solusi: Samakan rasio sirup per 1 liter air: (1) 2/3 liter sirup/liter air = 0,67. (2) Rasio air:sirup = 2:3, maka sirup/air = 3/2 = 1,5. (3) 2/3 campuran adalah air, maka 1/3 adalah sirup. Rasio sirup/air = (1/3)/(2/3) = 0,5. Campuran (2) memiliki rasio sirup tertinggi (1,5), sehingga paling manis.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi berbagai bentuk representasi rasio (pecahan, perbandingan, bagian dari keseluruhan) ke dalam satu satuan standar (sirup per liter air) untuk membandingkan nilai. Ini adalah proses memilih dan menerapkan prosedur matematika pada situasi rutin.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang rasio dan proporsi, serta bagaimana hubungan bagian-keseluruhan dan bagian-bagian dapat dinyatakan dalam bentuk yang berbeda.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal memerlukan konversi tiga format rasio yang berbeda ke satu basis yang sama. Meskipun prosedurnya rutin, siswa harus berhati-hati dalam menafsirkan '2/3 dari campuran adalah air' (yang berarti sirup 1/3) agar tidak terjebak.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, proporsi, dan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, membandingkan rasio dalam berbagai format adalah keterampilan dasar yang diharapkan. Tingkat kesulitan Medium diberikan karena adanya kebutuhan untuk melakukan konversi representasi yang berbeda sebelum membandingkan. |

Run 2 — solusi: Samakan basis perbandingan (sirup per 1 liter air): (1) 2/3 liter sirup/liter air = 0,67. (2) Rasio air:sirup 2:3 berarti 3/2 liter sirup/liter air = 1,5. (3) 2/3 campuran adalah air, berarti 1/3 adalah sirup. Rasio sirup:air = 1:2, atau 1/2 liter sirup/liter air = 0,5. Campuran kedua memiliki konsentrasi sirup tertinggi (1,5 > 0,67 > 0,5).
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari tiga format representasi rasio yang berbeda (pecahan, rasio bagian-bagian, dan bagian-keseluruhan) untuk membandingkan konsentrasi sirup. Ini memerlukan pemilihan prosedur yang tepat untuk menormalisasi semua nilai ke basis yang sama (sirup per 1 liter air).. Bukti: Campuran mana yang paling manis?; Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang rasio dan proporsi, serta kemampuan mengubah berbagai bentuk representasi rasio ke dalam bentuk standar untuk perbandingan.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka yang diberikan. Mereka harus melakukan konversi representasi (dari rasio bagian-bagian atau bagian-keseluruhan ke rasio sirup/air) sebelum dapat membandingkan nilai secara akurat.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, proporsi, dan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengelola perbandingan rasio yang disajikan dalam format berbeda. Tingkat kesulitan Medium tepat karena adanya kebutuhan untuk menormalisasi data sebelum membandingkan. |

Run 3 — solusi: Samakan basis per 1 liter air: (1) 2/3 liter sirup per 1 liter air. (2) Rasio air:sirup 2:3 berarti 1 liter air : 1,5 liter sirup. (3) 2/3 campuran adalah air, berarti 1/3 adalah sirup. Rasio sirup:air = 1:2, jadi 1 liter air : 0,5 liter sirup. Campuran (2) memiliki sirup terbanyak per liter air (1,5 liter), sehingga paling manis.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi berbagai bentuk representasi rasio (pecahan, perbandingan, bagian dari keseluruhan) ke dalam satu basis yang sama (sirup per 1 liter air) untuk membandingkan tingkat kemanisan. Ini adalah proses applying.. Bukti: Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang rasio dan proporsi dalam berbagai bentuk penyajian, serta bagaimana mengaitkan konsep-konsep tersebut untuk memecahkan masalah perbandingan.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal memerlukan konversi tiga format rasio yang berbeda ke basis yang sama. Meskipun prosedurnya rutin, siswa harus berhati-hati dalam interpretasi (terutama campuran ketiga) dan melakukan perbandingan nilai pecahan/desimal.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, proporsi, dan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai soal aplikasi rasio yang memerlukan ketelitian interpretasi data. |

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

![Gambar sumber soal 17](<../images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Karena segitiga sebangun, rasio tinggi terhadap bayangan adalah konstan. Tinggi_anak / Bayangan_anak = Tinggi_dewasa / Bayangan_dewasa. 114 / 200 = h / 305. h = (114 * 305) / 200 = 173,85 cm.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png. Transkripsi visual: Terdapat tiga gambar segitiga siku-siku yang sebangun, masing-masing mewakili Anak Kecil, Remaja, dan Orang Dewasa. Untuk Anak Kecil, tinggi = 114 cm dan panjang bayangan = 200 cm. Untuk Remaja, tinggi = 148 cm. Untuk Orang Dewasa, panjang bayangan = 305 cm. Sudut elevasi theta (θ) sama untuk ketiga segitiga. Soal meminta mencari tinggi orang dewasa menggunakan perbandingan segitiga sebangun.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `46fa18ab76a26846be0ae26feef3976976c3be886cdba55de8135af7f109737f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3317 |
| 2 | success | valid / verified | applying | procedural | Easy | 3347 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3340 |

Run 1 — solusi: Karena segitiga sebangun, rasio tinggi terhadap bayangan adalah konstan. Tinggi anak/bayangan anak = Tinggi dewasa/bayangan dewasa. 114/200 = h/305. h = (114 * 305) / 200 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep kesebangunan segitiga (perbandingan senilai) untuk menyelesaikan masalah kontekstual. Ini adalah prosedur rutin yang melibatkan pemilihan rasio yang tepat.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip kesebangunan (konsep) dan penerapan algoritma perbandingan (prosedural) untuk mencari nilai yang tidak diketahui.. Bukti: perbandingan segitiga sebangun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi pasangan sisi yang bersesuaian dan melakukan operasi aritmetika dasar. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 114 cm 148 cm 200 cm 305 cm; Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.

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
| gradeRelativeRationale | Materi kesebangunan adalah materi dasar yang sudah dipelajari di jenjang SMP, sehingga untuk kelas 10 SMA, ini dikategorikan sebagai soal yang mudah (prosedural rutin). |

Run 2 — solusi: Karena segitiga sebangun, rasio tinggi terhadap bayangan adalah konstan: tinggi_anak/bayangan_anak = tinggi_dewasa/bayangan_dewasa. Maka, 114/200 = h/305. h = (114 * 305) / 200 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep kesebangunan segitiga untuk mencari nilai yang tidak diketahui. Ini adalah prosedur rutin yang melibatkan pemilihan rasio yang tepat.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang prinsip kesebangunan (konsep) dan penerapannya dalam perhitungan proporsi (prosedural).. Bukti: perbandingan segitiga sebangun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi rasio yang sesuai dari data yang diberikan dan melakukan perhitungan aritmatika dasar. Tidak ada strategi non-rutin atau kendala kompleks.. Bukti: 114 cm 148 cm 200 cm 305 cm; Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kesebangunan segitiga dan perbandingan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan dan perbandingan adalah materi dasar yang sudah dipelajari di jenjang SMP, sehingga untuk kelas 10 ini dikategorikan mudah. |

Run 3 — solusi: Karena segitiga sebangun, rasio tinggi terhadap alas adalah konstan: tinggi_anak/bayangan_anak = tinggi_dewasa/bayangan_dewasa. Maka, 114/200 = y/305. y = (114 * 305) / 200 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep kesebangunan segitiga (perbandingan senilai) untuk menyelesaikan masalah kontekstual yang rutin. Ini adalah penerapan prosedur matematika standar pada situasi yang diberikan.. Bukti: Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip kesebangunan (konsep) dan penggunaan rasio/proporsi (prosedural) untuk menemukan nilai yang tidak diketahui.. Bukti: perbandingan segitiga sebangun
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi hubungan proporsional antara dua segitiga sebangun dan melakukan operasi aritmetika dasar. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 114 cm / 200 cm = y / 305 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kesebangunan segitiga dan perbandingan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan dan perbandingan adalah dasar yang sudah dipelajari di jenjang SMP dan merupakan prasyarat rutin untuk kelas 10. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4871`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep kesebangunan segitiga (perbandingan senilai) untuk menyelesaikan masalah kontekstual. Ini adalah prosedur rutin yang melibatkan pemilihan rasio yang tepat.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang prinsip kesebangunan (konsep) dan penerapannya dalam perhitungan proporsi (prosedural).
- Intended difficulty `Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi rasio yang sesuai dari data yang diberikan dan melakukan perhitungan aritmatika dasar. Tidak ada strategi non-rutin atau kendala kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kesebangunan segitiga dan perbandingan senilai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan dan perbandingan adalah materi dasar yang sudah dipelajari di jenjang SMP, sehingga untuk kelas 10 ini dikategorikan mudah. |

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
Transkripsi visual: Terdapat tiga gambar segitiga siku-siku yang sebangun, masing-masing mewakili Anak Kecil, Remaja, dan Orang Dewasa. Untuk Anak Kecil, tinggi = 114 cm dan panjang bayangan = 200 cm. Untuk Remaja, tinggi = 148 cm. Untuk Orang Dewasa, panjang bayangan = 305 cm. Sudut elevasi theta (θ) sama untuk ketiga segitiga. Soal meminta mencari tinggi orang dewasa menggunakan perbandingan segitiga sebangun.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `c6e8b0f4419e6dcbc2ddc05d`

Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.<br><br>Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.

| Opsi | Isi |
|---|---|
| A | 173,85 cm |
| B | 114 cm |
| C | 152,50 cm |
| D | 535,09 cm |

![Gambar sumber soal 18](<../images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Diketahui tan theta = tinggi / bayangan. Dengan theta = 30 derajat, maka tan 30 derajat = tinggi_dewasa / 305 cm. Menggunakan nilai tan 30 derajat = 0,57, diperoleh tinggi_dewasa = 0,57 * 305 cm = 173,85 cm.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png. Transkripsi visual: Terdapat tiga ilustrasi segitiga siku-siku yang dibentuk oleh tinggi orang dan panjang bayangannya. 1. Anak Kecil: tinggi 114 cm, bayangan 200 cm. 2. Remaja: tinggi 148 cm. 3. Orang Dewasa: bayangan 305 cm. Sudut elevasi matahari (theta) sama untuk ketiga kasus. Soal meminta mencari tinggi orang dewasa menggunakan tan 30 derajat = 0,57.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2877db1eac5ce9fc01e62dc8a0e27c017288e93550f6461412e8d88dbede0f90`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3389 |
| 2 | success | valid / verified | applying | procedural | Easy | 3392 |
| 3 | success | valid / verified | applying | procedural | Easy | 3342 |

Run 1 — solusi: Diketahui tan theta = tinggi / bayangan. Dengan theta = 30 derajat, maka tan 30 derajat = tinggi_dewasa / 305 cm. Menggunakan nilai tan 30 derajat = 0,57, diperoleh tinggi_dewasa = 0,57 * 305 cm = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi perbandingan trigonometri (tangen) untuk menyelesaikan masalah kontekstual sederhana. Prosesnya melibatkan pemilihan rumus yang tepat dan substitusi nilai yang diberikan, yang merupakan karakteristik dari domain applying.. Bukti: Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.; tan 30 o = 0,57; bayangan 305 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau teknik perbandingan trigonometri (tangen) untuk menghitung panjang sisi segitiga, yang termasuk dalam pengetahuan prosedural.. Bukti: tan 30 o = 0,57; tan theta = depan/samping
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi variabel yang diketahui (bayangan sebagai sisi samping, tinggi sebagai sisi depan) dan menerapkan rumus tangen secara langsung. Tidak ada langkah kompleks atau strategi non-rutin yang diperlukan.. Bukti: tan 30 o = 0,57; bayangan 305 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri dasar (tangen) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, penggunaan perbandingan trigonometri dasar pada segitiga siku-siku adalah materi standar yang bersifat prosedural dan langsung. |

Run 2 — solusi: Diketahui tan theta = depan/samping. Dengan theta = 30 derajat, maka tan 30 derajat = tinggi_dewasa / panjang_bayangan_dewasa. Substitusi nilai: 0,57 = y / 305. Maka y = 0,57 * 305 = 173,85 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi perbandingan trigonometri (tangen) pada situasi yang diberikan untuk mencari nilai yang tidak diketahui. Ini adalah penerapan langsung dari rumus tan = depan/samping.. Bukti: Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.; tan 30 o = 0,57; panjang bayangan (sisi samping) = 305 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rasio trigonometri (tangen) untuk menyelesaikan masalah tinggi benda.. Bukti: tan 30 o = 0,57; tan theta = depan/samping
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi sisi depan dan samping pada segitiga siku-siku, lalu menerapkan rumus tangen yang sudah diberikan nilainya. Tidak ada langkah kompleks atau strategi non-rutin.. Bukti: tan 30 o = 0,57; panjang bayangan (sisi samping) = 305 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar perbandingan trigonometri (tangen) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini hanya memerlukan substitusi nilai ke dalam rumus yang sudah dipahami, sehingga tergolong mudah. |

Run 3 — solusi: Diketahui tan 30 derajat = sisi depan / sisi samping. Maka, tinggi orang dewasa = tan 30 derajat * panjang bayangan = 0,57 * 305 cm = 173,85 cm.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan definisi perbandingan trigonometri (tangen) pada situasi yang diberikan. Siswa perlu mengidentifikasi sisi depan dan samping dari gambar, lalu menerapkan rumus tan theta = depan/samping untuk menghitung tinggi.. Bukti: Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.; Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep perbandingan trigonometri (tangen) dan bagaimana menerapkannya dalam konteks geometri (segitiga siku-siku) untuk menyelesaikan masalah.. Bukti: tan 30 o = 0,57; memanfaatkan perbandingan trigonometri
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi variabel yang diketahui (panjang bayangan sebagai sisi samping) dan menerapkan rumus tangen yang sudah diberikan nilainya. Tidak ada strategi non-rutin atau integrasi kompleks yang diperlukan.. Bukti: Diketahui bahwa tan 30 o = 0,57; Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar perbandingan trigonometri (tangen) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat langsung (prosedural) untuk kelas 10, di mana siswa diharapkan sudah familiar dengan konsep dasar trigonometri. |

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
Subtopik: Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.

Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.
Pilihan: A. 173,85 cm
B. 114 cm
C. 152,50 cm
D. 535,09 cm
Transkripsi visual: Terdapat tiga ilustrasi segitiga siku-siku yang dibentuk oleh tinggi orang dan panjang bayangannya. 1. Anak Kecil: tinggi 114 cm, bayangan 200 cm. 2. Remaja: tinggi 148 cm. 3. Orang Dewasa: bayangan 305 cm. Sudut elevasi matahari (theta) sama untuk ketiga kasus. Soal meminta mencari tinggi orang dewasa menggunakan tan 30 derajat = 0,57.
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

![Gambar sumber soal 19](<../images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Perbandingan sisi QR terhadap QP adalah 4/5. Dalam segitiga PQR, QR adalah sisi samping sudut Q (36,8 derajat) dan QP adalah sisi miring. Maka, QR/QP = cos(Q) = cos(36,8 derajat) = 4/5.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png. Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sisi PR = 3, QR = 4, PQ = 5 (hipotenusa). Sudut P = 53,2 derajat, sudut Q = 36,8 derajat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8e0360737d4fa38165e8c4bb0f5d72937c9acc73dcb1690ebf045d794fa2e7cc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3268 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3302 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3247 |

Run 1 — solusi: Perbandingan sisi QR terhadap QP adalah 4/5. Dalam segitiga PQR, QR adalah sisi samping sudut Q (36,8 derajat) dan QP adalah sisi miring. Maka, QR/QP = cos(Q) = cos(36,8 derajat) = 4/5.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi posisi sisi (samping dan miring) relatif terhadap sudut Q untuk menentukan rasio trigonometri yang tepat. Ini adalah penerapan langsung dari definisi kosinus.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi perbandingan trigonometri (sinus, kosinus, tangen) dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali definisi kosinus berdasarkan gambar yang sudah lengkap dengan panjang sisi dan sudut.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

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
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini tidak memerlukan manipulasi aljabar atau strategi kompleks, hanya pengenalan rasio. |

Run 2 — solusi: Berdasarkan gambar, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring (hipotenusa). Rasio QR/QP = 4/5 = 0,8. Nilai cos 36,8° = sisi samping/sisi miring = QR/QP = 4/5 = 0,8. Jadi, QR/QP = cos 36,8°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi posisi sisi (samping dan miring) relatif terhadap sudut Q pada segitiga siku-siku untuk menentukan rasio trigonometri yang tepat. Ini adalah penerapan langsung dari definisi perbandingan trigonometri.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi perbandingan trigonometri (sinus, cosinus, tangen) dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali definisi cosinus sebagai perbandingan sisi samping terhadap sisi miring pada segitiga siku-siku yang sudah diberikan lengkap dengan nilai sisi-sisinya.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

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
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini tidak memerlukan manipulasi aljabar atau strategi kompleks, cukup pengenalan definisi. |

Run 3 — solusi: Perbandingan sisi QR terhadap QP adalah 4/5. Pada segitiga PQR, QR adalah sisi samping sudut Q (36,8 derajat) dan QP adalah sisi miring. Maka, QR/QP = cos(Q) = cos(36,8 derajat) = 4/5.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi rasio trigonometri yang tepat berdasarkan posisi sisi dalam segitiga siku-siku. Ini adalah penerapan langsung dari definisi perbandingan trigonometri (cosinus).. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi rasio trigonometri (samping/miring) dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi sisi samping dan miring terhadap sudut Q, lalu mencocokkannya dengan definisi cosinus.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

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
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kelas 10. Soal ini tidak memerlukan manipulasi aljabar atau strategi kompleks, hanya pengenalan rasio. |

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
Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sisi PR = 3, QR = 4, PQ = 5 (hipotenusa). Sudut P = 53,2 derajat, sudut Q = 36,8 derajat.
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

![Gambar sumber soal 20](<../images/kelas10_panduan_siswa_kelas10.pdf-0115-11.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Diketahui sisi depan (de) = 9,2 dan sudut θ = 30°. Maka: sin 30° = de/z => 0,5 = 9,2/z => z = 9,2 / 0,5 = 18,4. tan 30° = de/x => 1/√3 = 9,2/x => x = 9,2 * √3 ≈ 9,2 * 1,732 = 15,9344 ≈ 15,94.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0115-11.png. Transkripsi visual: Segitiga siku-siku dengan sudut 30 derajat di kanan bawah. Sisi vertikal di kiri memiliki panjang 9,2. Sisi horizontal di bawah adalah x. Sisi miring adalah z. Sudut 30 derajat berada di antara sisi x dan sisi miring z. Sisi 9,2 adalah sisi depan sudut 30 derajat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec76ac77affa22bfec8752a9b55f9a881e2c70652e0bc64ad64cdcc70e024b05`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3422 |
| 2 | success | valid / verified | applying | procedural | Easy | 3391 |
| 3 | success | valid / verified | applying | procedural | Easy | 3405 |

Run 1 — solusi: Diketahui sisi depan (de) = 9,2 dan sudut θ = 30°. Maka: sin 30° = de/z => 0,5 = 9,2/z => z = 9,2 / 0,5 = 18,4. tan 30° = de/x => 1/√3 = 9,2/x => x = 9,2 * √3 ≈ 9,2 * 1,732 = 15,9344 ≈ 15,94.
- Domain kognitif `classify/applying`: Siswa perlu memilih rasio trigonometri yang tepat (sinus dan tangen) berdasarkan posisi sisi yang diketahui (depan) terhadap sudut 30 derajat untuk mencari sisi miring dan sisi samping. Ini adalah penerapan prosedur rutin dalam konteks segitiga siku-siku.. Bukti: Cari panjang sisi x dan z.; sin 30° = de/z; tan 30° = de/x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi rasio trigonometri (sinus, tangen) dan kemampuan menerapkan algoritma tersebut untuk menyelesaikan panjang sisi yang tidak diketahui.. Bukti: sin 30° = de/z; tan 30° = de/x
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Siswa hanya perlu mengidentifikasi sisi depan, samping, dan miring, lalu menerapkan rumus perbandingan trigonometri dasar. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Cari panjang sisi x dan z.; 9,2 30º

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
| gradeRelativeRationale | Materi trigonometri dasar adalah standar kurikulum kelas 10. Soal ini langsung menguji pemahaman konsep dasar tanpa modifikasi konteks yang menyulitkan. |

Run 2 — solusi: Diketahui sisi depan (de) = 9,2 dan sudut = 30 derajat. Maka sin 30 = de/z -> 0,5 = 9,2/z -> z = 9,2 / 0,5 = 18,4. Kemudian tan 30 = de/x -> 1/sqrt(3) = 9,2/x -> x = 9,2 * sqrt(3) = 9,2 * 1,732 = 15,9344 (dibulatkan 15,94). Jadi x = 15,94 dan z = 18,4.
- Domain kognitif `classify/applying`: Siswa perlu memilih rasio trigonometri yang tepat (sinus dan tangen) berdasarkan posisi sisi yang diketahui (depan) terhadap sudut 30 derajat untuk mencari sisi miring dan sisi samping. Ini adalah penerapan prosedur rutin dalam situasi yang familiar.. Bukti: Cari panjang sisi x dan z.; sin 30 = de/z; tan 30 = de/x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi perbandingan trigonometri (sinus, tangen) dan kemampuan menerapkan algoritma perhitungan untuk mencari panjang sisi segitiga.. Bukti: sin 30 = de/z; tan 30 = de/x
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari definisi perbandingan trigonometri pada segitiga siku-siku dengan satu langkah pemilihan rumus yang jelas dan perhitungan dasar.. Bukti: Cari panjang sisi x dan z.; 9,2 30º

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
| gradeRelativeRationale | Siswa kelas 10 diharapkan sudah menguasai perbandingan trigonometri dasar pada segitiga siku-siku sebagai materi awal trigonometri. |

Run 3 — solusi: Diketahui sisi depan (de) = 9,2 dan sudut = 30 derajat. Maka sin 30 = de/z -> 0,5 = 9,2/z -> z = 9,2/0,5 = 18,4. Kemudian tan 30 = de/x -> 1/√3 = 9,2/x -> x = 9,2 * √3 ≈ 9,2 * 1,732 = 15,9344. Dibulatkan menjadi 15,94. Jadi x = 15,94 dan z = 18,4.
- Domain kognitif `classify/applying`: Siswa perlu memilih rasio trigonometri yang tepat (sinus dan tangen) berdasarkan posisi sisi yang diketahui (depan) terhadap sudut 30 derajat untuk mencari sisi miring dan sisi samping. Ini adalah penerapan prosedur rutin dalam konteks segitiga siku-siku.. Bukti: Cari panjang sisi x dan z.; sin 30 = de/z; tan 30 = de/x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi rasio trigonometri (sinus, tangen) dan kemampuan menerapkan algoritma tersebut untuk menyelesaikan panjang sisi yang tidak diketahui.. Bukti: sin 30 = de/z; tan 30 = de/x
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan aplikasi langsung dari definisi rasio trigonometri dasar pada segitiga siku-siku. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Cari panjang sisi x dan z.; 9,2 30º

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
| gradeRelativeRationale | Siswa kelas 10 SMA diharapkan sudah menguasai perbandingan trigonometri dasar sebagai materi standar kurikulum. |

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
Transkripsi visual: Segitiga siku-siku dengan sudut 30 derajat di kanan bawah. Sisi vertikal di kiri memiliki panjang 9,2. Sisi horizontal di bawah adalah x. Sisi miring adalah z. Sudut 30 derajat berada di antara sisi x dan sisi miring z. Sisi 9,2 adalah sisi depan sudut 30 derajat.
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
Solusi minimum hasil AI: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c38db0076998aa40dc1bbaae9a6a6a0c2f5468733866673ac3db5de59d1e2c1a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2344 |
| 2 | success | valid / verified | applying | procedural | Medium | 2261 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2238 |

Run 1 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak (atau kuadrat jarak) untuk menentukan panjang sisi-sisi segitiga dan kemudian menerapkan teorema Pythagoras untuk memverifikasi sifat siku-siku. Ini adalah penerapan prosedur rutin pada situasi geometri.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku?; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara koordinat titik, rumus jarak, dan prinsip teorema Pythagoras (konseptual) serta kemampuan melakukan perhitungan langkah demi langkah (prosedural).. Bukti: AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (menghitung tiga jarak, membandingkan kuadratnya) tanpa strategi non-rutin yang kompleks. Ini sesuai untuk tingkat menengah.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).; Apakah segitiga ABC merupakan segitiga siku-siku?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik pada koordinat Kartesius dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri koordinat adalah standar kelas 10. Soal ini menuntut ketelitian perhitungan aritmetika dasar dan penerapan teorema Pythagoras, yang merupakan ekspektasi rutin bagi siswa kelas 10. |

Run 2 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak untuk menghitung panjang sisi-sisi segitiga dan menggunakan teorema Pythagoras untuk memverifikasi sifat segitiga siku-siku. Ini melibatkan pemilihan prosedur yang tepat dan eksekusi langkah-langkah rutin.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku?; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan teknik prosedural (rumus jarak dan teorema Pythagoras) untuk menyelesaikan masalah geometri koordinat.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).; Apakah segitiga ABC merupakan segitiga siku-siku?
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin (menghitung tiga jarak, menguadratkan, menjumlahkan, dan membandingkan) tanpa strategi non-rutin atau kendala kompleks.. Bukti: A(-1, 3), B(4, -2), dan C(1, -5).; Apakah segitiga ABC merupakan segitiga siku-siku?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri koordinat dan teorema Pythagoras adalah standar kelas 10. Soal ini menuntut ketelitian perhitungan namun prosedurnya sangat standar. |

Run 3 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak (atau kuadrat jarak) untuk menentukan panjang sisi-sisi segitiga, kemudian menggunakan kebalikan Teorema Pythagoras untuk memverifikasi sifat siku-siku. Ini adalah penerapan prosedur rutin pada situasi geometri.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku? Jelaskan.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara koordinat titik, panjang sisi, dan sifat segitiga siku-siku melalui teorema Pythagoras, yang merupakan pengetahuan konseptual.. Bukti: Diketahui \triangle ABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin: menghitung kuadrat jarak ketiga sisi dan membandingkannya menggunakan teorema Pythagoras. Prosedurnya standar dan familiar bagi siswa kelas 10.. Bukti: Diketahui \triangle ABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).; Apakah segitiga ABC merupakan segitiga siku-siku?

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
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menghitung jarak antar titik dan menerapkan teorema Pythagoras untuk mengklasifikasikan segitiga. Langkah-langkahnya bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4367`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan rumus jarak untuk menghitung panjang sisi-sisi segitiga dan menggunakan kebalikan Teorema Pythagoras untuk memverifikasi sifat siku-siku. Ini adalah penerapan prosedur rutin pada situasi geometri.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang hubungan antara koordinat titik, rumus jarak, dan prinsip teorema Pythagoras (konseptual) serta kemampuan melakukan perhitungan langkah demi langkah (prosedural).
- Intended difficulty `Medium`: Soal memerlukan beberapa langkah rutin (menghitung tiga jarak, membandingkan kuadratnya) tanpa strategi non-rutin yang kompleks. Ini sesuai untuk tingkat menengah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik pada koordinat Kartesius dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri koordinat adalah standar kelas 10. Soal ini menuntut ketelitian perhitungan aritmetika dasar dan penerapan teorema Pythagoras, yang merupakan ekspektasi rutin bagi siswa kelas 10. |

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
Solusi minimum hasil AI: Misal k, h, b adalah panjang tongkat kasti, hoki, bisbol. Sistem: (1) 3k+2h+b=455, (2) k+3h+2b=545, (3) b=2k. Substitusi (3) ke (1): 3k+2h+2k=455 => 5k+2h=455. Substitusi (3) ke (2): k+3h+4k=545 => 5k+3h=545. Kurangi kedua persamaan: (5k+3h)-(5k+2h)=545-455 => h=90. Substitusi h=90 ke 5k+2(90)=455 => 5k=275 => k=55. Maka b=2(55)=110.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `994dbb41e2d8b4367968fd0e21ab332cb88e32bce926c92d926e445863d4feb6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2546 |
| 2 | success | valid / verified | applying | procedural | Medium | 2495 |
| 3 | success | valid / verified | applying | procedural | Medium | 2496 |

Run 1 — solusi: Misal k, h, b adalah panjang tongkat kasti, hoki, bisbol. Sistem: (1) 3k+2h+b=455, (2) k+3h+2b=545, (3) b=2k. Substitusi (3) ke (1): 3k+2h+2k=455 => 5k+2h=455. Substitusi (3) ke (2): k+3h+4k=545 => 5k+3h=545. Kurangi kedua persamaan: (5k+3h)-(5k+2h)=545-455 => h=90. Substitusi h=90 ke 5k+2(90)=455 => 5k=275 => k=55. Maka b=2(55)=110.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam sistem persamaan linear tiga variabel (SPLTV) dan memilih prosedur eliminasi atau substitusi untuk menyelesaikannya. Ini adalah penerapan prosedur matematika pada situasi kontekstual.. Bukti: Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm.; Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm.; 2 tongkat kasti sama panjang dengan tongkat bisbol.
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami struktur sistem persamaan linear dan hubungan antar variabel yang diberikan dalam soal cerita untuk menyusun model matematika yang tepat.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol
- Intended difficulty `classify/Medium`: Soal ini memerlukan pembentukan model matematika dari narasi dan penyelesaian sistem persamaan linear tiga variabel. Meskipun ada tiga variabel, hubungan b=2k menyederhanakan sistem menjadi dua variabel, menjadikannya tugas rutin bagi siswa kelas 10.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm.; Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm.; 2 tongkat kasti sama panjang dengan tongkat bisbol.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan kemampuan menerjemahkan soal cerita ke model matematika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLTV adalah materi standar kelas 10. Soal ini menuntut kemampuan translasi bahasa ke simbol dan manipulasi aljabar rutin. |

Run 2 — solusi: Misal k, h, b adalah panjang tongkat kasti, hoki, bisbol. Sistem: (1) 3k+2h+b=455, (2) k+3h+2b=545, (3) b=2k. Substitusi (3) ke (1): 3k+2h+2k=455 -> 5k+2h=455. Substitusi (3) ke (2): k+3h+4k=545 -> 5k+3h=545. Eliminasi: (5k+3h)-(5k+2h)=545-455 -> h=90. Substitusi h=90 ke 5k+2(90)=455 -> 5k=275 -> k=55. Maka b=2(55)=110.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi menjadi sistem persamaan linear tiga variabel (SPLTV) dan memilih prosedur eliminasi/substitusi untuk menyelesaikannya.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam memodelkan masalah nyata ke dalam sistem persamaan linear dan menerapkan teknik penyelesaian aljabar.. Bukti: 3k+2h+b=455; k+3h+2b=545; b=2k
- Intended difficulty `classify/Medium`: Soal ini memerlukan pembentukan model matematika dari narasi dan penyelesaian SPLTV dengan 3 variabel. Ini adalah prosedur rutin yang dipelajari di kelas 10.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua/tiga variabel dan substitusi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 10 mengenai sistem persamaan linear, di mana siswa diharapkan mampu memodelkan dan menyelesaikan masalah kontekstual. |

Run 3 — solusi: Misal k, h, b adalah panjang tongkat kasti, hoki, bisbol. Sistem: 3k+2h+b=455 (1), k+3h+2b=545 (2), b=2k (3). Substitusi (3) ke (1): 3k+2h+2k=455 -> 5k+2h=455. Substitusi (3) ke (2): k+3h+4k=545 -> 5k+3h=545. Eliminasi: (5k+3h)-(5k+2h)=545-455 -> h=90. Substitusi h=90 ke 5k+2(90)=455 -> 5k=275 -> k=55. Maka b=2(55)=110.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi menjadi model matematika (SPLTV) dan memilih prosedur eliminasi/substitusi untuk menyelesaikannya. Ini adalah penerapan prosedur rutin dalam konteks sistem persamaan.. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antar variabel dalam sistem persamaan linear dan penggunaan algoritma penyelesaian (substitusi/eliminasi).. Bukti: 3k+2h+b=455; k+3h+2b=545; b=2k
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pembentukan model matematika dari soal cerita dan penyelesaian sistem tiga variabel yang melibatkan beberapa langkah rutin (substitusi dan eliminasi).. Bukti: 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm; sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm; 2 tongkat kasti sama panjang dengan tongkat bisbol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar SPLDV dan substitusi variabel. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena SPLTV adalah materi standar yang menuntut ketelitian dalam manipulasi aljabar dan pemodelan. |

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
Solusi minimum hasil AI: Misalkan k=kecil, s=sedang, b=besar. Persamaan: (1) 3k+2s+3b=4700, (2) 3k+s+2b=3300, (3) 2s+2b=2800. Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) jika dibagi 2 juga menghasilkan s+b=1400. Karena persamaan (3) adalah kombinasi linear dari (1) dan (2), sistem ini memiliki tak hingga solusi (dependen linear).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5322e1d81ca4f13136b776a61c38382b540e73c9bb54fa33e7886e3b75d75bcb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2379 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2387 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2402 |

Run 1 — solusi: Misalkan k=kecil, s=sedang, b=besar. Persamaan: (1) 3k+2s+3b=4700, (2) 3k+s+2b=3300, (3) 2s+2b=2800. Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) jika dibagi 2 juga menghasilkan s+b=1400. Karena persamaan (3) adalah kombinasi linear dari (1) dan (2), sistem ini memiliki tak hingga solusi (dependen linear).
- Domain kognitif `classify/reasoning`: Siswa perlu menganalisis ketergantungan linear antar persamaan dalam sistem tiga variabel, bukan sekadar menghitung nilai variabel. Ini melibatkan pemahaman konseptual tentang sistem persamaan linear yang memiliki solusi tak hingga.. Bukti: 3k+2s+3b=4700; 3k+s+2b=3300; 2s+2b=2800; eliminasi (1) dan (2) identik dengan persamaan (3)
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang sifat sistem persamaan linear (dependensi linear) daripada sekadar prosedur penyelesaian aljabar.. Bukti: Berapakah volume tiap jenis kemasan? Ada berapa solusi yang ada?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan eliminasi sederhana untuk menyadari bahwa persamaan ketiga adalah redundan (dependen linear). Ini memerlukan langkah rutin (eliminasi) dan interpretasi hasil (banyak solusi) yang melampaui sekadar mencari nilai variabel tunggal.. Bukti: 3k+2s+3b=4700; 3k+s+2b=3300; 2s+2b=2800

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Dua Variabel (SPLDV) dan konsep dasar SPLTV. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengidentifikasi sistem yang tidak memiliki solusi tunggal melalui eliminasi sederhana. |

Run 2 — solusi: Misalkan k=kecil, s=sedang, b=besar. Persamaan: (1) 3k+2s+3b=4700, (2) 3k+s+2b=3300, (3) 2s+2b=2800. Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) jika dibagi 2 juga menghasilkan s+b=1400. Karena persamaan (3) adalah kombinasi linear dari (1) dan (2), sistem ini memiliki tak hingga solusi.
- Domain kognitif `classify/reasoning`: Siswa perlu menganalisis ketergantungan linear antar persamaan dalam sistem persamaan linear tiga variabel (SPLTV) untuk menentukan banyaknya solusi, yang merupakan proses reasoning.. Bukti: Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml.; Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml.; Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat sistem persamaan linear, khususnya mengenai sistem yang bergantung linear (dependent system) dan interpretasi banyaknya solusi.. Bukti: Banyak solusi (tak terhingga), karena eliminasi persamaan (1) dan (2) identik dengan persamaan (3).
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya sekadar menyelesaikan sistem, tetapi harus menyadari bahwa persamaan yang diberikan tidak independen (redundant), yang memerlukan pemahaman lebih dalam daripada sekadar prosedur eliminasi rutin.. Bukti: Ada berapa solusi yang ada? Jelaskan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua/tiga variabel dan konsep eliminasi. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengidentifikasi sistem yang memiliki solusi tak hingga melalui eliminasi sederhana, namun soal ini menuntut pemahaman konseptual di atas sekadar menghitung nilai variabel. |

Run 3 — solusi: Misalkan k, s, b adalah volume kemasan kecil, sedang, besar. Persamaan: (1) 3k+2s+3b=4700, (2) 3k+s+2b=3300, (3) 2s+2b=2800. Eliminasi (1)-(2) menghasilkan s+b=1400. Persamaan (3) jika dibagi 2 juga menghasilkan s+b=1400. Karena persamaan (3) adalah kombinasi linear dari (1) dan (2), sistem hanya memiliki 2 persamaan independen untuk 3 variabel, sehingga solusi tak hingga.
- Domain kognitif `classify/reasoning`: Siswa perlu menganalisis ketergantungan linear antar persamaan untuk menentukan banyaknya solusi, bukan sekadar menghitung nilai variabel.. Bukti: Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml.; Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml.; Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman.
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang sistem persamaan linear, khususnya mengenai sistem yang bergantung linear (dependent system) dan interpretasi jumlah solusi.. Bukti: Berapakah volume tiap jenis kemasan? Ada berapa solusi yang ada?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung menggunakan metode eliminasi/substitusi standar untuk mencari nilai tunggal. Siswa harus menyadari bahwa persamaan ketiga adalah kombinasi linear dari dua persamaan pertama, yang merupakan konsep penting dalam SPLTV.. Bukti: 3k+2s+3b=4700; 3k+s+2b=3300; 2s+2b=2800

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua dan tiga variabel, serta konsep eliminasi. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengidentifikasi sistem yang memiliki solusi tak hingga melalui manipulasi aljabar sederhana. |

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
Solusi minimum hasil AI: Substitusi x=0 dan y=0 ke dalam 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yaitu 0 < 10. Karena 0 < 10 adalah pernyataan yang benar, maka titik (0,0) merupakan bagian dari daerah hasil pertidaksamaan tersebut.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `936944d06fd1c1a3d136b7085a09beeaf3988113fc66beea1fd6b8977ad55b82`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2075 |
| 2 | success | valid / verified | applying | procedural | Easy | 2013 |
| 3 | success | valid / verified | applying | procedural | Easy | 2012 |

Run 1 — solusi: Substitusi x=0 dan y=0 ke dalam 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yaitu 0 < 10. Karena 0 < 10 adalah pernyataan yang benar, maka titik (0,0) merupakan bagian dari daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan prosedur substitusi langsung untuk memverifikasi apakah sebuah titik memenuhi pertidaksamaan linear. Ini adalah penerapan prosedur rutin.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep daerah penyelesaian pertidaksamaan linear dan menerapkan algoritma substitusi untuk menguji titik tersebut.. Bukti: 2 x + 5 y < 10; substitusi nilai x = 0 dan y = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan prosedural. Siswa hanya perlu melakukan substitusi nilai nol ke dalam variabel yang diberikan tanpa perlu manipulasi aljabar yang kompleks atau interpretasi grafik yang rumit.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linear dua variabel dan operasi substitusi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai pengenalan atau latihan dasar dalam menentukan daerah penyelesaian pertidaksamaan linear. |

Run 2 — solusi: Substitusi (0,0) ke 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yaitu 0 < 10. Karena 0 < 10 adalah pernyataan benar, maka (0,0) merupakan daerah hasil.
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan prosedur substitusi langsung untuk memverifikasi apakah suatu titik memenuhi pertidaksamaan linear. Ini adalah penerapan prosedur standar.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma substitusi nilai ke dalam bentuk pertidaksamaan linear untuk menentukan kebenaran pernyataan.. Bukti: 2 x + 5 y < 10; substitusi nilai x = 0 dan y = 0
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan satu langkah substitusi sederhana tanpa manipulasi aljabar yang kompleks atau interpretasi grafik yang rumit.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang substitusi variabel dan pertidaksamaan linear. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai pengenalan atau latihan dasar sistem pertidaksamaan linear. |

Run 3 — solusi: Substitusi (0,0) ke 2x + 5y < 10 menghasilkan 2(0) + 5(0) < 10, yaitu 0 < 10. Karena 0 < 10 adalah pernyataan benar, maka (0,0) merupakan daerah hasil.
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan prosedur substitusi langsung untuk memverifikasi apakah suatu titik memenuhi pertidaksamaan linear. Ini adalah penerapan prosedur rutin.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep daerah penyelesaian pertidaksamaan linear dan menerapkan algoritma substitusi untuk mengujinya.. Bukti: 2 x + 5 y < 10; substitusi nilai x = 0 dan y = 0
- Intended difficulty `classify/Easy`: Soal bersifat langsung, hanya memerlukan satu langkah substitusi sederhana tanpa manipulasi aljabar yang kompleks atau interpretasi grafik yang rumit.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan

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
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai pengenalan atau latihan dasar sistem pertidaksamaan linear. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, yang berarti 0 > 10. Karena 0 > 10 adalah pernyataan yang salah, maka titik (0,0) bukan merupakan daerah hasil pertidaksamaan tersebut.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e62c0e62e3bcd1b13d57622d5f4d9e5698588d3d5f82e8d23ebd683ebef84da7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2262 |
| 2 | success | valid / verified | applying | procedural | Easy | 2244 |
| 3 | success | valid / verified | applying | procedural | Easy | 2215 |

Run 1 — solusi: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, yang berarti 0 > 10. Karena 0 > 10 adalah pernyataan yang salah, maka titik (0,0) bukan merupakan daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk melakukan prosedur substitusi langsung dan mengevaluasi kebenaran pernyataan matematika yang dihasilkan. Ini adalah proses rutin yang menerapkan konsep dasar pertidaksamaan linear.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?; substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prosedur substitusi titik ke dalam pertidaksamaan linear untuk menentukan apakah titik tersebut memenuhi syarat atau tidak.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan langsung. Siswa hanya perlu melakukan substitusi nilai nol ke dalam variabel yang diberikan dan mengevaluasi ketidaksamaan sederhana. Tidak ada langkah kompleks atau interpretasi grafik yang rumit.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang substitusi variabel dan konsep pertidaksamaan linear. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, soal ini sangat mendasar karena hanya menguji pemahaman substitusi titik ke dalam pertidaksamaan linear tanpa perlu memodelkan sistem atau menggambar grafik. |

Run 2 — solusi: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, yang berarti 0 > 10. Karena 0 > 10 adalah pernyataan yang salah, maka titik (0,0) bukan merupakan daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerapkan prosedur substitusi titik ke dalam pertidaksamaan linear untuk menentukan apakah titik tersebut memenuhi syarat. Ini adalah proses rutin dalam materi sistem pertidaksamaan linear.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?; substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prosedur substitusi dan prinsip dasar pertidaksamaan linear untuk mengevaluasi kebenaran pernyataan matematika.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan prosedural. Siswa hanya perlu melakukan substitusi nilai nol ke dalam variabel yang diberikan dan membandingkan hasilnya dengan konstanta, yang merupakan prosedur dasar dalam topik pertidaksamaan linear.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan

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
| gradeRelativeRationale | Materi sistem pertidaksamaan linear adalah kurikulum standar kelas 10. Soal ini menguji pemahaman dasar tentang daerah penyelesaian melalui substitusi titik uji, yang merupakan langkah paling mendasar. |

Run 3 — solusi: Substitusi titik (0,0) ke dalam pertidaksamaan 6x + 2y > 10 menghasilkan 6(0) + 2(0) > 10, yang berarti 0 > 10. Karena 0 > 10 adalah pernyataan yang salah, maka titik (0,0) bukan merupakan daerah hasil pertidaksamaan tersebut.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk melakukan prosedur substitusi langsung ke dalam pertidaksamaan linear untuk menguji titik uji. Ini adalah proses rutin yang menerapkan konsep dasar pertidaksamaan linear dua variabel.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?; substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prosedur substitusi dan aturan pertidaksamaan linear untuk menentukan apakah suatu titik memenuhi daerah penyelesaian.. Bukti: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu melakukan substitusi nilai nol ke dalam persamaan linear sederhana. Tidak ada langkah kompleks atau interpretasi grafik yang rumit.. Bukti: Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10?

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
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai pengenalan atau penguatan konsep dasar daerah penyelesaian pertidaksamaan linear. |

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
Solusi minimum hasil AI: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `548aa9fb9eac8438c8d3ff9fd29285987a3576cf61cb552008a697ab6219159a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2368 |
| 2 | success | valid / verified | applying | procedural | Easy | 2342 |
| 3 | success | valid / verified | applying | procedural | Easy | 2318 |

Run 1 — solusi: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika SPLDV dan menyelesaikan sistem tersebut menggunakan metode substitusi atau eliminasi yang rutin.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam memodelkan situasi nyata ke dalam sistem persamaan linear dan menerapkan algoritma penyelesaian SPLDV.. Bukti: x+y=40 dan 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini adalah aplikasi standar SPLDV. Siswa hanya perlu membuat dua persamaan linear dan menyelesaikannya. Tidak ada kendala non-rutin atau integrasi representasi yang kompleks.. Bukti: 40 kuas lukis; Rp35.000,00; Rp24.000,00; Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, persamaan linear, dan metode eliminasi/substitusi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi dasar kelas 10. Soal ini menggunakan angka yang cukup besar namun prosedurnya sangat standar dan familiar bagi siswa. |

Run 2 — solusi: Misal x=jenis I, y=jenis II. Sistem: x+y=40 dan 35000x+24000y=1103000. Dari x=40-y, substitusi ke persamaan kedua: 35000(40-y)+24000y=1103000 -> 1400000-35000y+24000y=1103000 -> -11000y=-297000 -> y=27. Maka x=40-27=13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika berupa sistem persamaan linear dua variabel (SPLDV) dan menyelesaikannya menggunakan metode eliminasi atau substitusi.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam memodelkan situasi nyata ke dalam sistem persamaan linear dan menerapkan algoritma penyelesaian SPLDV.. Bukti: x+y=40; 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin SPLDV dengan dua variabel. Siswa hanya perlu melakukan pemodelan sederhana dan operasi aljabar dasar untuk mendapatkan solusi.. Bukti: 40 kuas lukis; Rp35.000,00; Rp24.000,00; Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan operasi aritmetika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi standar kelas 10. Soal ini menggunakan konteks belanja yang umum dan prosedur penyelesaian yang diajarkan secara eksplisit di kelas. |

Run 3 — solusi: Misal x=jenis I, y=jenis II. Sistem: x+y=40 dan 35000x+24000y=1103000. Dari x=40-y, substitusi ke persamaan kedua: 35000(40-y)+24000y=1103000 => 1400000-35000y+24000y=1103000 => -11000y=-297000 => y=27. Maka x=40-27=13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika SPLDV dan menyelesaikan sistem tersebut menggunakan metode substitusi atau eliminasi yang rutin.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur standar (SPLDV) untuk menyelesaikan masalah yang diberikan.. Bukti: x+y=40; 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari SPLDV dengan dua variabel dan dua persamaan linear. Prosedur penyelesaiannya standar dan familiar bagi siswa kelas 10.. Bukti: 40 kuas lukis; Rp35.000,00; Rp24.000,00; Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan operasi aritmetika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi standar kelas 10. Soal ini tidak memiliki kompleksitas tambahan, hanya menuntut ketelitian dalam perhitungan aritmetika. |

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
Solusi minimum hasil AI: Persamaan 2x^2 - 8x + 6 = 0 disederhanakan dengan membagi kedua ruas dengan 2 menjadi x^2 - 4x + 3 = 0. Faktorisasi dari x^2 - 4x + 3 adalah (x - 1)(x - 3) = 0. Maka, akar-akarnya adalah x = 1 atau x = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `365f1dd418672f134a220ef1cab937567680372e4d54db19e7b0332038f6c6f6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2088 |
| 2 | success | valid / verified | applying | procedural | Easy | 2075 |
| 3 | success | valid / verified | applying | procedural | Easy | 2091 |

Run 1 — solusi: Persamaan 2x^2 - 8x + 6 = 0 disederhanakan dengan membagi kedua ruas dengan 2 menjadi x^2 - 4x + 3 = 0. Faktorisasi dari x^2 - 4x + 3 adalah (x - 1)(x - 3) = 0. Maka, akar-akarnya adalah x = 1 atau x = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat (faktorisasi atau rumus ABC). Ini adalah tugas rutin yang memerlukan penerapan prosedur yang sudah dipelajari.. Bukti: Tentukan solusi atau akar-akar dari persamaan kuadrat 2x^2 - 8x + 6 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma faktorisasi persamaan kuadrat, yang merupakan bagian dari pengetahuan prosedural.. Bukti: 2x^2 - 8x + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu melakukan penyederhanaan (pembagian dengan 2) dan faktorisasi dasar. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 2x^2 - 8x + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan kuadrat dan faktorisasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi persamaan kuadrat adalah standar kelas 10. Soal ini adalah latihan dasar yang sangat umum dan tidak memerlukan langkah penalaran tingkat tinggi. |

Run 2 — solusi: Persamaan 2x^2 - 8x + 6 = 0 dibagi 2 menjadi x^2 - 4x + 3 = 0. Faktorkan menjadi (x - 1)(x - 3) = 0. Maka akar-akarnya adalah x = 1 atau x = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk mencari akar persamaan kuadrat (faktorisasi atau rumus ABC). Ini adalah tugas rutin yang memerlukan penerapan prosedur yang sudah dipelajari.. Bukti: Tentukan solusi atau akar-akar dari persamaan kuadrat 2x^2 - 8x + 6 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pemecahan persamaan kuadrat, yang merupakan pengetahuan prosedural.. Bukti: 2x^2 - 8x + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur standar yang familiar bagi siswa kelas 10. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 2x^2 - 8x + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang faktorisasi persamaan kuadrat atau penggunaan rumus kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Persamaan kuadrat adalah materi dasar kelas 10. Soal ini menggunakan koefisien sederhana yang mudah difaktorkan, sehingga tingkat kesulitannya rendah. |

Run 3 — solusi: Persamaan 2x^2 - 8x + 6 = 0 dibagi 2 menjadi x^2 - 4x + 3 = 0. Faktorkan menjadi (x - 1)(x - 3) = 0. Maka akar-akarnya adalah x = 1 atau x = 3.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur standar untuk mencari akar persamaan kuadrat. Ini adalah tugas rutin yang memerlukan penerapan algoritma pemfaktoran atau rumus kuadrat.. Bukti: Tentukan solusi atau akar-akar dari persamaan kuadrat 2x^2 - 8x + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma pemfaktoran atau penggunaan rumus kuadrat untuk menyelesaikan persamaan tersebut, yang merupakan pengetahuan prosedural.. Bukti: 2x^2 - 8x + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan penyederhanaan (membagi dengan 2) dan pemfaktoran sederhana. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 2x^2 - 8x + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan kuadrat, pembagian polinomial sederhana, dan teknik pemfaktoran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari akar persamaan kuadrat adalah materi dasar kelas 10. Soal ini menggunakan koefisien yang sederhana sehingga beban komputasi rendah. |

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
| 1 | success | valid / verified | applying | procedural | Easy | 2002 |
| 2 | success | valid / verified | applying | procedural | Easy | 2038 |
| 3 | success | valid / verified | applying | procedural | Easy | 1965 |

Run 1 — solusi: 2x^2 - 18 = 0 => 2x^2 = 18 => x^2 = 9 => x = ±√9 => x = 3 atau x = -3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat sederhana (memindahkan konstanta, membagi koefisien, dan menarik akar). Ini adalah penerapan prosedur rutin.. Bukti: Tentukan akar-akar dari persamaan kuadrat 2x^2 - 18 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian persamaan kuadrat bentuk ax^2 - c = 0.. Bukti: 2x^2 - 18 = 0
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan manipulasi aljabar satu langkah (pembagian) dan operasi akar kuadrat dasar. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: 2x^2 - 18 = 0

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
| gradeRelativeRationale | Ini adalah materi dasar persamaan kuadrat yang dipelajari di awal bab, sangat rutin untuk siswa kelas 10. |

Run 2 — solusi: 2x^2 - 18 = 0 dibagi 2 menjadi x^2 - 9 = 0. Faktorkan menjadi (x - 3)(x + 3) = 0, sehingga x = 3 atau x = -3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar pemfaktoran atau ekstraksi akar untuk menyelesaikan persamaan kuadrat sederhana. Ini adalah penerapan prosedur rutin.. Bukti: Tentukan akar-akar dari persamaan kuadrat 2x^2 - 18 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian persamaan kuadrat (prosedural) yang didasarkan pada prinsip aljabar (konseptual).. Bukti: 2x^2 - 18 = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan manipulasi aljabar dasar satu langkah (pembagian) diikuti pemfaktoran selisih dua kuadrat atau akar kuadrat. Tidak ada kendala kompleks.. Bukti: 2x^2 - 18 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan kuadrat dan operasi aljabar (pembagian, pemfaktoran). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Persamaan kuadrat adalah materi dasar kelas 10. Soal ini adalah bentuk paling sederhana dari persamaan kuadrat (tanpa suku linear), sehingga tergolong mudah. |

Run 3 — solusi: 2x^2 - 18 = 0 => 2x^2 = 18 => x^2 = 9 => x = ±√9 => x = 3 atau x = -3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk menyelesaikan persamaan kuadrat sederhana dengan memindahkan konstanta dan melakukan ekstraksi akar.. Bukti: Tentukan akar-akar dari persamaan kuadrat 2x^2 - 18 = 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian persamaan kuadrat (prosedural) dan konsep akar kuadrat.. Bukti: 2x^2 - 18 = 0
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin satu langkah (isolasi variabel) yang familiar bagi siswa kelas 10.. Bukti: 2x^2 - 18 = 0

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
| gradeRelativeRationale | Persamaan kuadrat bentuk ax^2 - c = 0 adalah materi dasar yang sudah dipelajari di jenjang sebelumnya dan diperkuat di kelas 10. |

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
Solusi minimum hasil AI: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan adanya titik maksimum, yang merupakan karakteristik fungsi kuadrat dengan koefisien a < 0, sehingga grafik terbuka ke bawah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dacd18c02778cc80c5466699f4e9625c54720bdbf7a63336e7733d1036378dbe`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2231 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2249 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2229 |

Run 1 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan nilai fungsi memiliki titik maksimum, yang secara geometris merepresentasikan parabola yang terbuka ke bawah (koefisien a < 0).
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menginterpretasikan pola data numerik dan menghubungkannya dengan karakteristik geometris fungsi kuadrat (arah bukaan parabola) tanpa perlu menggambar grafik. Ini memerlukan pemahaman konseptual tentang perilaku fungsi kuadrat.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara pola perubahan nilai dalam tabel (naik-turun) dengan sifat konseptual fungsi kuadrat (titik puncak dan arah bukaan).. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman dasar tentang perilaku fungsi kuadrat melalui data diskrit. Siswa hanya perlu mengenali pola simetris dan titik balik (maksimum) untuk menyimpulkan arah bukaan, yang merupakan prosedur rutin dalam analisis fungsi kuadrat.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan titik puncak fungsi kuadrat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menginterpretasikan data tabel untuk menentukan sifat fungsi kuadrat sederhana tanpa harus melakukan kalkulasi aljabar yang rumit. |

Run 2 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) ke 9 (t=3) lalu menurun kembali ke 0 (t=6). Pola naik-lalu-turun ini menunjukkan titik puncak (maksimum) pada t=3. Fungsi kuadrat dengan titik maksimum memiliki koefisien a < 0, sehingga grafik terbuka ke bawah.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan pola perubahan nilai dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan) tanpa bantuan visual grafik. Ini melibatkan pemahaman konseptual tentang hubungan antara titik puncak dan arah bukaan parabola.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat fungsi kuadrat (titik balik/maksimum) yang direpresentasikan melalui data numerik, bukan sekadar prosedur aljabar.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan penalaran untuk menghubungkan pola data numerik dengan sifat fungsi kuadrat tanpa bantuan visual langsung, yang memerlukan pemahaman lebih dalam daripada sekadar menghitung nilai.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi kuadrat, titik puncak, dan perilaku grafik parabola. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menganalisis perilaku fungsi kuadrat dari data tabel. Soal ini menuntut kemampuan berpikir analitis untuk mengaitkan pola data dengan karakteristik grafik tanpa harus menggambarnya secara eksplisit. |

Run 3 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak maksimum, yang merupakan karakteristik fungsi kuadrat dengan koefisien a < 0, sehingga grafik terbuka ke bawah.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan pola numerik dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan) tanpa bantuan visual grafik. Ini melibatkan pemahaman konseptual tentang perilaku fungsi kuadrat (titik puncak) yang diaplikasikan pada data diskrit.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pola perubahan nilai (naik-turun) dengan bentuk grafik fungsi kuadrat, bukan sekadar menghafal prosedur aljabar.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan kemampuan untuk mengabstraksi pola numerik menjadi sifat geometris fungsi tanpa bantuan visual langsung. Siswa harus memahami hubungan antara titik puncak dan arah bukaan parabola.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum fungsi kuadrat dan karakteristik grafik parabola (titik puncak). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman konseptual fungsi kuadrat di luar sekadar menghitung nilai fungsi, menuntut penalaran tentang perilaku data. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3996`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menginterpretasikan pola perubahan nilai dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan) tanpa bantuan visual grafik. Ini melibatkan pemahaman konseptual tentang perilaku fungsi kuadrat (titik puncak) yang diaplikasikan pada data diskrit.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pola perubahan nilai (naik-turun) dengan bentuk grafik fungsi kuadrat, bukan sekadar menghafal prosedur aljabar.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan kemampuan untuk mengabstraksi pola numerik menjadi sifat geometris fungsi tanpa bantuan visual langsung. Siswa harus memahami hubungan antara titik puncak dan arah bukaan parabola.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum fungsi kuadrat dan karakteristik grafik parabola (titik puncak). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman konseptual fungsi kuadrat di luar sekadar menghitung nilai fungsi, menuntut penalaran tentang perilaku data. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Titik puncak (2,8) memberikan bentuk y=a(x-2)^2+8. Substitusi titik awal (0,4): 4=a(0-2)^2+8 => 4=4a+8 => 4a=-4 => a=-1. Fungsi: y=-(x-2)^2+8 = -(x^2-4x+4)+8 = -x^2+4x+4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4fde9d455dab1f738cd6be8fab86dae33bf3d19a23e29d3f2acaea2160d5915b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2205 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2223 |
| 3 | success | valid / verified | applying | procedural | Medium | 2195 |

Run 1 — solusi: Titik puncak (2,8) memberikan bentuk y=a(x-2)^2+8. Substitusi titik awal (0,4): 4=a(0-2)^2+8 => 4=4a+8 => 4a=-4 => a=-1. Fungsi: y=-(x-2)^2+8 = -(x^2-4x+4)+8 = -x^2+4x+4.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi titik puncak dan titik potong sumbu y untuk menentukan parameter fungsi kuadrat. Ini melibatkan pemilihan prosedur (bentuk vertex ke bentuk umum) dan pemahaman konsep parabola.. Bukti: mencapai ketinggian maksimum 8 m setelah dua detik; ketinggian awal 4 m; Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara karakteristik geometris parabola (titik puncak) dengan representasi aljabar fungsi kuadrat.. Bukti: fungsi kuadrat; bentuk umum y = ax^2+bx+c; ketinggian maksimum 8 m setelah dua detik
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman bentuk vertex dan konversi ke bentuk umum. Siswa harus mengidentifikasi titik puncak (2,8) dan titik (0,4) untuk mencari nilai 'a'. Ini adalah prosedur rutin yang melibatkan beberapa langkah terhubung.. Bukti: ketinggian awal 4 m; mencapai ketinggian maksimum 8 m setelah dua detik; Nyatakan fungsi kuadrat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk vertex fungsi kuadrat y=a(x-h)^2+k dan substitusi titik. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman fungsi kuadrat dalam konteks masalah nyata (gerak parabola sederhana). |

Run 2 — solusi: Vertex form: y = a(x-2)^2 + 8. Substitute (0,4): 4 = a(0-2)^2 + 8 => 4 = 4a + 8 => 4a = -4 => a = -1. Expand: y = -1(x^2 - 4x + 4) + 8 = -x^2 + 4x - 4 + 8 = -x^2 + 4x + 4.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (bentuk vertex ke bentuk umum) dan menerapkan konsep fungsi kuadrat untuk menentukan parameter a, h, dan k berdasarkan informasi titik puncak dan titik potong sumbu y.. Bukti: mencapai ketinggian maksimum 8 m setelah dua detik; ketinggian awal 4 m; Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara titik puncak, titik potong, dan bentuk aljabar fungsi kuadrat untuk menyusun model matematika.. Bukti: bentuk umum y = ax^2+bx+c; titik puncak (2,8); ketinggian awal 4 m
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin: menentukan bentuk vertex, mencari nilai 'a' dengan substitusi titik, dan menjabarkan ke bentuk umum. Ini adalah prosedur standar untuk kelas 10.. Bukti: ketinggian awal 4 m; mencapai ketinggian maksimum 8 m setelah dua detik; Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk vertex fungsi kuadrat y=a(x-h)^2+k dan substitusi titik. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman mendalam tentang parameter fungsi kuadrat tanpa kompleksitas aljabar yang berlebihan. |

Run 3 — solusi: Titik puncak (h, k) = (2, 8), maka y = a(x-2)^2 + 8. Melalui (0, 4), maka 4 = a(0-2)^2 + 8 => 4 = 4a + 8 => 4a = -4 => a = -1. Fungsi: y = -1(x-2)^2 + 8 = -(x^2 - 4x + 4) + 8 = -x^2 + 4x - 4 + 8 = -x^2 + 4x + 4.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi titik puncak dan titik potong sumbu y untuk membentuk persamaan kuadrat, yang merupakan proses applying konsep fungsi kuadrat.. Bukti: mencapai ketinggian maksimum 8 m setelah dua detik; dilemparkan dari ketinggian awal 4 m
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara bentuk titik puncak (vertex form) dan bentuk umum (standard form) serta menerapkan prosedur aljabar untuk mengubahnya.. Bukti: Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum y = ax^2+bx+c
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang bentuk vertex dan substitusi titik untuk mencari koefisien a. Ini adalah prosedur rutin yang melibatkan beberapa langkah terstruktur.. Bukti: mencapai ketinggian maksimum 8 m setelah dua detik; dilemparkan dari ketinggian awal 4 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk vertex fungsi kuadrat y=a(x-h)^2+k dan substitusi titik. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman mendalam tentang parameter fungsi kuadrat dalam konteks masalah nyata. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3933`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengintegrasikan informasi titik puncak dan titik potong sumbu y untuk menentukan parameter fungsi kuadrat. Ini melibatkan pemilihan prosedur (bentuk vertex ke bentuk umum) dan penerapan konsep fungsi kuadrat pada situasi masalah nyata.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami hubungan antara karakteristik geometris parabola (titik puncak) dengan representasi aljabar fungsi kuadrat untuk menyusun model matematika.
- Intended difficulty `Medium`: Soal memerlukan beberapa langkah rutin: menentukan bentuk vertex, mencari nilai 'a' dengan substitusi titik, dan menjabarkan ke bentuk umum. Ini adalah prosedur standar untuk kelas 10.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk vertex fungsi kuadrat y=a(x-h)^2+k dan substitusi titik. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman fungsi kuadrat dalam konteks masalah nyata (gerak parabola sederhana). |

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
Solusi minimum hasil AI: Kapasitas muatan bersih = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Jumlah pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c5e6b68a8b88acf7f11fefa36609bfd344cdacfe912ac21d8eda975857241887`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2274 |
| 2 | success | valid / verified | applying | procedural | Medium | 2275 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2295 |

Run 1 — solusi: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Jumlah pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur aritmetika yang tepat untuk menentukan kapasitas efektif, menghitung jumlah kotak per angkut, dan menerapkan logika pembulatan ke atas (ceiling function) dalam konteks dunia nyata.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana memodelkan masalah kapasitas muatan ke dalam operasi aritmetika dan memahami batasan bilangan bulat dalam konteks praktis.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait (pengurangan kapasitas, pembagian, dan interpretasi hasil pembulatan) yang harus dilakukan secara berurutan untuk mencapai jawaban yang benar.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai aplikasi dasar dari pertidaksamaan linear atau aritmetika sosial sederhana. |

Run 2 — solusi: Kapasitas muatan bersih = 2000 kg - 150 kg = 1850 kg. Kapasitas kotak per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Jumlah pengangkutan = 350 kotak / 37 kotak/angkut ≈ 9,45. Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kendala (kapasitas bersih), memilih prosedur pembagian yang tepat, dan menerapkan penalaran logis untuk membulatkan hasil ke atas (konteks dunia nyata) agar semua kotak terangkut.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang operasi aritmetika dasar dan konsep pembulatan dalam konteks masalah optimasi sederhana.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; berapa kali pengangkutan kotak yang harus dilakukan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya melakukan operasi pembagian, tetapi harus menginterpretasikan sisa hasil bagi dalam konteks nyata (pembulatan ke atas) untuk memastikan semua muatan terangkut.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; 350 kotak; berapa kali pengangkutan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini sesuai untuk kelas 10 sebagai penerapan pertidaksamaan linear sederhana dalam kehidupan sehari-hari, menuntut ketelitian dalam interpretasi hasil. |

Run 3 — solusi: Kapasitas muatan per angkut = (2000 - 150) / 50 = 1850 / 50 = 37 kotak. Total kotak = 350. Banyak pengangkutan = 350 / 37 ≈ 9,459. Karena pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika sederhana (pertidaksamaan atau pembagian dengan pembulatan ke atas) untuk menentukan jumlah pengangkutan. Ini melibatkan pemilihan prosedur yang tepat untuk situasi rutin.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara kapasitas total, beban tetap, dan beban variabel, serta penerapan algoritma pembagian dan pembulatan dalam konteks nyata.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: menghitung kapasitas bersih, menentukan kapasitas per angkut, dan melakukan pembulatan ke atas yang logis sesuai konteks (bukan sekadar pembulatan matematis).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, konsep pembagian, dan pemahaman konteks masalah (pembulatan ke atas untuk kapasitas). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai aplikasi pertidaksamaan linear sederhana dalam kehidupan sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4218`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu memilih prosedur aritmetika yang tepat untuk menentukan kapasitas efektif, menghitung jumlah kotak per angkut, dan menerapkan logika pembulatan ke atas (ceiling function) dalam konteks dunia nyata.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana memodelkan masalah kapasitas muatan ke dalam operasi aritmetika dan memahami batasan bilangan bulat dalam konteks praktis.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait (pengurangan kapasitas, pembagian, dan interpretasi hasil pembulatan) yang harus dilakukan secara berurutan untuk mencapai jawaban yang benar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai aplikasi dasar dari pertidaksamaan linear atau aritmetika sosial sederhana. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `43deb443d803999ad9eb144ec855cfcf8c7419ffa883f31b6191b856bbf5281c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2217 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2269 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2260 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan dengan jumlah anggota yang sama.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar mengenai korespondensi satu-satu dan penggunaan rumus faktorial sebagai prosedur penyelesaiannya.. Bukti: korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Siswa hanya perlu mengenali rumus n! dan menerapkannya pada nilai n yang diberikan.. Bukti: n(A) = n(B) = 12

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
| gradeRelativeRationale | Meskipun angka 12! cukup besar, prosedur penyelesaiannya sangat langsung (n!) dan merupakan materi standar kelas 10. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Siswa perlu mengingat dan menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan dengan jumlah anggota yang sama.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep korespondensi satu-satu dan penggunaan prosedur faktorial.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Prosedur yang digunakan langsung (n!) tanpa memerlukan strategi nonrutin atau integrasi representasi yang kompleks.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korespondensi satu-satu dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! cukup besar, prosedur penyelesaiannya adalah standar untuk materi korespondensi satu-satu di kelas 10. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep korespondensi satu-satu dan prinsip perkalian (faktorial) yang mendasarinya.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung bagi siswa yang sudah mempelajari materi korespondensi satu-satu. Tidak ada strategi nonrutin atau integrasi kompleks yang diperlukan.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korespondensi satu-satu dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! cukup besar, prosedurnya sangat standar untuk materi korespondensi satu-satu di kelas 10. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `3b808934c13bf0822544d6d6`

1. Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998. Untuk dapat memahami diagram dengan lebih baik, kamu perlu memahami situasi dan konteks dari diagram.<br><br>Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

| Opsi | Isi |
|---|---|
| A | 6 pelari |
| B | 10 pelari |
| C | 4 pelari |
| D | 8 pelari |

![Gambar sumber soal 33](<../images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identifikasi batang dengan tinggi y > 30 dan y < 33. Batang tersebut adalah Estonia 2, Jepang, Kazakhstan, Latvia, Slovakia, Spain 1, Spain 2, dan Ukraine. Total terdapat 8 batang yang memenuhi kriteria interval 31:00-32:59.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png. Transkripsi visual: Diagram batang menunjukkan waktu tempuh (sumbu Y, 0-45 menit) untuk berbagai negara (sumbu X). Batang yang memiliki tinggi antara 31 dan 33 (mewakili interval 31:00-32:59) adalah: Estonia 2 (sedikit di atas 30), Jepang (sedikit di atas 30), Kazakhstan (sedikit di atas 30), Latvia (sedikit di atas 30), Slovakia (sedikit di atas 30), Spain 1 (sedikit di atas 30), Spain 2 (sedikit di atas 30), Ukraine (sedikit di atas 30). Total ada 8 batang.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `966bc164a10f51b7919aeab9d59f38d6941a76cc5c9af7e8175d12bc2fbff5f3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3333 |
| 2 | success | valid / verified | knowing | factual | Easy | 3339 |
| 3 | success | valid / verified | knowing | factual | Easy | 3459 |

Run 1 — solusi: Identifikasi batang dengan tinggi y > 30 dan y < 33. Batang tersebut adalah Estonia 2, Jepang, Kazakhstan, Latvia, Slovakia, Spain 1, Spain 2, dan Ukraine. Total terdapat 8 batang yang memenuhi kriteria interval 31:00-32:59.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram batang dan melakukan pencacahan sederhana berdasarkan kriteria interval yang diberikan. Ini adalah proses membaca dan menginterpretasi data visual secara langsung.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca diagram batang dan mengidentifikasi nilai data berdasarkan sumbu yang diberikan.. Bukti: Diagram batang menunjukkan waktu yang ditempuh oleh para atlet
- Intended difficulty `classify/Easy`: Tugas ini bersifat prosedural langsung: mengidentifikasi batang yang berada dalam rentang nilai tertentu pada sumbu Y. Tidak ada manipulasi data yang kompleks atau strategi non-rutin yang diperlukan.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca skala pada diagram batang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, membaca diagram batang adalah keterampilan dasar yang sudah dikuasai sejak jenjang sebelumnya. Soal ini tidak menuntut analisis statistik mendalam. |

Run 2 — solusi: Identifikasi batang pada diagram yang tingginya berada di antara garis 30 dan 35, tepatnya di atas 31 dan di bawah 33. Batang tersebut adalah: Estonia 2, Japan, Kazakhstan, Latvia, Slovakia, Spain 1, Spain 2, dan U.S 2. Terdapat 8 batang yang memenuhi kriteria.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari diagram batang dan melakukan pencacahan sederhana berdasarkan kriteria interval yang diberikan. Tidak ada strategi nonrutin atau integrasi kompleks yang diperlukan.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan informasi dari diagram batang.. Bukti: Perhatikan diagram batang berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct retrieval) dari representasi visual. Siswa hanya perlu mencocokkan tinggi batang dengan skala sumbu Y.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

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
| gradeRelativeRationale | Membaca diagram batang adalah keterampilan dasar yang sudah dikuasai sebelum kelas 10. Soal ini tidak menuntut analisis statistik mendalam. |

Run 3 — solusi: Berdasarkan visual, batang dengan tinggi antara 31 dan 33 menit adalah: Estonia 2, Kazakhstan, Slovakia, Spain 1, Ukraine. Total ada 5 atlet. Kunci D (8) tidak dapat diverifikasi dari diagram yang diberikan.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca nilai dari diagram batang dan membandingkannya dengan interval yang diberikan. Ini adalah proses membaca data langsung.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
- Dimensi pengetahuan `classify/factual`: Siswa menggunakan pengetahuan faktual tentang cara membaca diagram batang untuk mengidentifikasi nilai data.. Bukti: Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet
- Intended difficulty `classify/Easy`: Soal ini hanya memerlukan pembacaan grafik sederhana. Prosedurnya sangat langsung dan familiar bagi siswa kelas 10.. Bukti: Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca diagram batang adalah keterampilan dasar yang sudah dikuasai sebelum kelas 10. |

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
Transkripsi visual: Diagram batang menunjukkan waktu tempuh (sumbu Y, 0-45 menit) untuk berbagai negara (sumbu X). Batang yang memiliki tinggi antara 31 dan 33 (mewakili interval 31:00-32:59) adalah: Estonia 2 (sedikit di atas 30), Jepang (sedikit di atas 30), Kazakhstan (sedikit di atas 30), Latvia (sedikit di atas 30), Slovakia (sedikit di atas 30), Spain 1 (sedikit di atas 30), Spain 2 (sedikit di atas 30), Ukraine (sedikit di atas 30). Total ada 8 batang.
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

![Gambar sumber soal 34](<../images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung negara unik pada label sumbu horizontal. Negara yang muncul dua kali (Austria, Estonia, Norway, Spain, U.S) dihitung satu kali, ditambah 15 negara yang muncul sekali, total 20 negara.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png. Transkripsi visual: Diagram batang menunjukkan waktu tempuh atlet. Sumbu horizontal berisi label negara peserta: Austria 1, Austria 2, Canada, Czech Republic, Estonia 1, Estonia 2, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Norway 1, Norway 2, Russia, Slovakia, Spain 1, Spain 2, Ukraine, U.S 1, U.S 2. Terdapat 25 batang total. Negara yang muncul dua kali adalah Austria, Estonia, Norway, Spain, dan U.S. (5 negara). Negara yang muncul sekali: Canada, Czech Republic, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Russia, Slovakia, Ukraine (15 negara). Total negara unik = 5 + 15 = 20.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `21e59034e886afa94e1530e6fe973e5cec44e63b39fb5235d57c2271c3ca6267`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3367 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3349 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3372 |

Run 1 — solusi: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung negara unik pada label sumbu horizontal. Negara yang muncul dua kali (Austria, Estonia, Norway, Spain, U.S) dihitung satu kali, ditambah 15 negara yang muncul sekali, total 20 negara.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram batang (jumlah batang) dan melakukan proses klasifikasi/pengelompokan data (menghitung entitas unik dari label yang berulang) untuk menjawab pertanyaan.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data direpresentasikan dalam diagram batang, khususnya membedakan antara jumlah observasi (batang) dan kategori unik (negara).. Bukti: Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah rutin yang terkait: menghitung total batang (atlet) dan melakukan seleksi/pengelompokan data untuk menghitung kategori unik (negara) dengan memperhatikan label yang berulang.. Bukti: Dari Gambar 6.4, ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan memahami konsep data kategorikal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menginterpretasikan data statistik dasar dan membedakan antara frekuensi total dengan jumlah kategori unik dalam sebuah dataset. |

Run 2 — solusi: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung negara unik dengan mengabaikan duplikasi (Austria, Estonia, Norway, Spain, U.S muncul 2 kali). Total negara = 25 - 5 = 20.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan diagram batang untuk menghitung frekuensi total (atlet) dan mengidentifikasi kategori unik (negara) dengan memperhatikan label yang berulang. Ini adalah proses menerapkan pemahaman representasi data pada situasi yang memerlukan ketelitian.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data disajikan dalam diagram batang dan kemampuan untuk membedakan antara entitas individu (atlet) dan kategori (negara) dalam konteks statistik deskriptif.. Bukti: Diagram batang; negara yang muncul dua kali
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya sekadar membaca angka, tetapi harus melakukan langkah tambahan berupa identifikasi dan eliminasi duplikasi data (negara) untuk mendapatkan jawaban yang benar, yang memerlukan ketelitian lebih daripada sekadar membaca grafik langsung.. Bukti: Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet; beberapa negara (Austria, Estonia, Norway, Spain, U.S) muncul dua kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan memahami konsep data unik vs frekuensi. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu menganalisis data statistik sederhana. Soal ini menuntut ketelitian dalam membedakan antara jumlah data (atlet) dan kategori (negara) yang disajikan dalam diagram. |

Run 3 — solusi: Jumlah atlet adalah total batang pada diagram, yaitu 25. Untuk jumlah negara, hitung label unik pada sumbu horizontal. Negara yang muncul dua kali (Austria, Estonia, Norway, Spain, U.S) dihitung sebagai satu entitas negara. Total negara unik = 25 batang - 5 duplikasi = 20 negara.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan diagram batang untuk menghitung frekuensi total (jumlah atlet) dan mengidentifikasi kategori unik (jumlah negara) dengan memperhatikan label yang berulang. Ini adalah proses menerapkan pemahaman representasi data pada situasi yang sedikit menuntut ketelitian.. Bukti: ada berapa atlet yang berpartisipasi; Ada berapa negara yang berpartisipasi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data dikategorikan dan disajikan dalam diagram batang, khususnya membedakan antara jumlah observasi (batang) dan jumlah kategori unik (negara).. Bukti: Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah rutin yang terkait: menghitung total item (atlet) dan melakukan reduksi data untuk menghitung kategori unik (negara) dengan memperhatikan label yang berulang. Siswa tidak bisa hanya membaca angka langsung, tetapi harus memproses informasi visual.. Bukti: Dari Gambar 6.4, ada berapa atlet yang berpartisipasi dalam cabang lintas alam? Ada berapa negara yang berpartisipasi dalam cabang ini?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan memahami konsep data kategorikal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 10, tugas ini menuntut ketelitian dalam membedakan antara jumlah data (atlet) dan jumlah kategori (negara) yang disajikan dalam diagram, yang merupakan keterampilan dasar statistik deskriptif. |

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
Transkripsi visual: Diagram batang menunjukkan waktu tempuh atlet. Sumbu horizontal berisi label negara peserta: Austria 1, Austria 2, Canada, Czech Republic, Estonia 1, Estonia 2, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Norway 1, Norway 2, Russia, Slovakia, Spain 1, Spain 2, Ukraine, U.S 1, U.S 2. Terdapat 25 batang total. Negara yang muncul dua kali adalah Austria, Estonia, Norway, Spain, dan U.S. (5 negara). Negara yang muncul sekali: Canada, Czech Republic, Finland, France, Germany, Greece, Japan, Kazakhstan, Kenya, Latvia, Macedonia, Mongolia, Russia, Slovakia, Ukraine (15 negara). Total negara unik = 5 + 15 = 20.
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
Solusi minimum hasil AI: Total data N = 30. Modus: frekuensi tertinggi 7 pada ukuran 43 dan 44. Median: rata-rata data ke-15 dan ke-16. Kumulatif frekuensi: 38(1), 39(2), 40(4), 41(8), 42(13), 43(20). Data ke-15 dan ke-16 berada di ukuran 43. Mean: (38*1 + 39*1 + 40*2 + 41*4 + 42*5 + 43*7 + 44*7 + 45*2 + 46*1) / 30 = 1275 / 30 = 42,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cd9376f986bd2aba2484c384be9468f45cfbbd094a07f7b1f1d1a53a1fe5ade5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2424 |
| 2 | success | valid / verified | applying | procedural | Medium | 2445 |
| 3 | success | valid / verified | applying | procedural | Medium | 2332 |

Run 1 — solusi: Total data n = 1+1+2+4+5+7+7+2+1 = 30. Modus adalah nilai dengan frekuensi tertinggi (7), yaitu 43 dan 44. Median adalah rata-rata data ke-15 dan ke-16. Data ke-15 dan ke-16 berada pada ukuran 43. Mean = (38*1 + 39*1 + 40*2 + 41*4 + 42*5 + 43*7 + 44*7 + 45*2 + 46*1) / 30 = 1275 / 30 = 42,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar (menghitung mean, median, modus) pada data frekuensi tunggal yang sudah disediakan. Ini adalah penerapan rutin dari konsep statistik deskriptif.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan prosedur perhitungan statistik deskriptif (mean, median, modus) pada data berkelompok sederhana.. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perhitungan aritmetika dasar dan memahami definisi statistik dasar. Tidak ada strategi non-rutin atau integrasi kompleks yang diperlukan.. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A \| Ukuran: 38, 39, 40, 41, 42, 43, 44, 45, 46 \| Frekuensi: 1, 1, 2, 4, 5, 7, 7, 2, 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang mean, median, modus, dan tabel frekuensi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 9 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi statistik deskriptif adalah bagian dari kurikulum kelas 10. Perhitungan mean, median, dan modus pada tabel frekuensi adalah prosedur standar yang familiar bagi siswa. |

Run 2 — solusi: Total data N = 30. Modus: nilai dengan frekuensi tertinggi (7) adalah 43 dan 44. Median: rata-rata data ke-15 dan ke-16. Kumulatif frekuensi: 38(1), 39(2), 40(4), 41(8), 42(13), 43(20). Data ke-15 dan ke-16 berada di ukuran 43, jadi median = 43. Mean: (38*1 + 39*1 + 40*2 + 41*4 + 42*5 + 43*7 + 44*7 + 45*2 + 46*1) / 30 = 1275 / 30 = 42,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar (modus, median, mean) pada data frekuensi yang sudah terstruktur. Ini adalah penerapan rutin dari konsep statistik deskriptif.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perhitungan statistik (mean, median, modus) pada data berkelompok sederhana.. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait (menghitung total frekuensi, menentukan posisi median, dan menghitung rata-rata tertimbang) tanpa adanya jebakan konseptual yang rumit.. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A \| Ukuran: 38, 39, 40, 41, 42, 43, 44, 45, 46 \| Frekuensi: 1, 1, 2, 4, 5, 7, 7, 2, 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang mean, median, modus, dan tabel frekuensi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 9 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan pengolahan data statistik dasar yang merupakan materi standar kurikulum. |

Run 3 — solusi: Total data N = 30. Modus: frekuensi tertinggi 7 pada ukuran 43 dan 44. Median: rata-rata data ke-15 dan ke-16. Data ke-15 dan ke-16 berada pada ukuran 43 (kumulatif: 1+1+2+4+5=13, data ke-14 s.d. 20 adalah 43). Mean: (38*1 + 39*1 + 40*2 + 41*4 + 42*5 + 43*7 + 44*7 + 45*2 + 46*1) / 30 = 1275 / 30 = 42,5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik untuk data berkelompok/frekuensi (modus, median, mean) pada situasi rutin yang diberikan dalam bentuk tabel.. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman algoritma dan teknik perhitungan statistik dasar (mean, median, modus) pada data frekuensi.. Bukti: Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan rutin yang melibatkan beberapa langkah (menghitung total, menentukan posisi median, menghitung rata-rata tertimbang).. Bukti: Tentukanlah modus, median, dan mean dari kumpulan data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep mean, median, modus, dan cara membaca tabel frekuensi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 9 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan pengolahan data statistik dasar yang merupakan materi standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4268`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur statistik dasar (mean, median, modus) pada data frekuensi yang sudah terstruktur. Ini adalah penerapan rutin dari konsep statistik deskriptif.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang algoritma dan prosedur perhitungan statistik deskriptif pada data frekuensi.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait (menghitung total frekuensi, menentukan posisi median, dan menghitung rata-rata tertimbang) tanpa adanya jebakan konseptual yang rumit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang mean, median, modus, dan tabel frekuensi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 9 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan pengolahan data statistik dasar yang merupakan materi standar kurikulum. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Data terurut: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7 (n=16). Modus adalah nilai dengan frekuensi tertinggi, yaitu 0 (muncul 4 kali). Median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d412a47d6ed08aba9c84995b32c727b918c2f10009d28df1d4012a5d57ce97c6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2150 |
| 2 | success | valid / verified | applying | procedural | Easy | 2124 |
| 3 | success | valid / verified | applying | procedural | Easy | 2904 |

Run 1 — solusi: Data terurut: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7 (n=16). Modus adalah nilai dengan frekuensi tertinggi, yaitu 0 (muncul 4 kali). Median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar (mengurutkan data, mencari nilai tengah, dan frekuensi terbanyak) pada kumpulan data yang diberikan.. Bukti: Tentukanlah modus dan median dari data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma mencari modus dan median dari sekumpulan data.. Bukti: Data berikut menunjukkan jumlah kue yang dijual; Tentukanlah modus dan median
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengurutkan data (16 data) dan menerapkan definisi modus serta median. Tidak ada jebakan konseptual yang kompleks.. Bukti: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi modus dan median, kemampuan mengurutkan data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 16 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari modus dan median dari data tunggal adalah materi dasar statistik yang sangat familiar bagi siswa kelas 10. |

Run 2 — solusi: Data terurut: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7. Jumlah data (n) = 16. Modus adalah nilai dengan frekuensi tertinggi, yaitu 0 (muncul 4 kali). Median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik dasar untuk menentukan modus dan median dari sekumpulan data yang diberikan.. Bukti: Tentukanlah modus dan median dari data di atas.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma mencari modus dan median pada data tunggal.. Bukti: Data berikut menunjukkan jumlah kue yang dijual; Tentukanlah modus dan median
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin (mengurutkan data dan menghitung statistik dasar) dengan jumlah data yang kecil (16 data), sehingga beban kognitifnya rendah.. Bukti: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi modus dan median serta kemampuan mengurutkan data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 16 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (modus/median) merupakan materi dasar yang sudah diperkenalkan sebelum kelas 10, sehingga untuk kelas 10 ini dikategorikan mudah. |

Run 3 — solusi: Data terurut: 0, 0, 0, 0, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7. Frekuensi 0 adalah 4 (terbanyak), maka modus = 0. Median adalah rata-rata data ke-8 dan ke-9: (3+3)/2 = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik standar (mengurutkan data, menghitung frekuensi, mencari nilai tengah) pada situasi rutin.. Bukti: Data berikut menunjukkan jumlah kue yang dijual; Tentukanlah modus dan median dari data di atas
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritma statistik dasar untuk menentukan modus dan median dari sekumpulan data.. Bukti: Tentukanlah modus dan median dari data di atas
- Intended difficulty `classify/Easy`: Prosedur standar, data kecil, tidak ada jebakan konseptual yang kompleks.. Bukti: Data berikut menunjukkan jumlah kue yang dijual; Tentukanlah modus dan median dari data di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar modus dan median, kemampuan mengurutkan data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 16 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif dasar yang sesuai untuk kelas 10, prosedur langsung. |

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
Solusi minimum hasil AI: Urutkan data: 300, 305, 310, 310, 310, 315, 315, 320, 320, 750. Q1 (kuartil bawah) = 310. Q3 (kuartil atas) = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1,5 * IQR = 320 + 1,5(10) = 335. Karena 750 > 335, maka 750 adalah pencilan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4e82b53e736a11b850b973e7ea573df979144a4cfd1e7dcd1e89b9cf368d9cf1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2322 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2353 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2318 |

Run 1 — solusi: Urutkan data: 300, 305, 310, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1,5 * IQR = 320 + 1,5(10) = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik formal (menghitung kuartil, IQR, dan batas pencilan) untuk memvalidasi klaim, bukan sekadar observasi visual.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang algoritma deteksi pencilan menggunakan metode IQR (Interquartile Range).. Bukti: batas atas IQR (335 kWh); 750 kWh lebih besar dari batas atas IQR
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (mengurutkan, mencari kuartil, menghitung IQR, menghitung batas atas) dan pemilihan prosedur yang tepat untuk menentukan pencilan.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang statistik deskriptif dasar, kuartil, dan metode deteksi pencilan (IQR). |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan penerapan rumus statistik standar pada dataset kecil. |

Run 2 — solusi: Data terurut: 300, 305, 310, 310, 310, 315, 315, 320, 320, 750. Q1 (kuartil bawah) = 310. Q3 (kuartil atas) = 320. IQR = Q3 - Q1 = 10. Batas atas pencilan = Q3 + 1,5 * IQR = 320 + 1,5(10) = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur statistik standar untuk mendeteksi pencilan menggunakan aturan IQR (Interquartile Range), yang merupakan penerapan konsep statistik deskriptif.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara kuartil, IQR, dan kriteria pencilan (konseptual) serta melakukan perhitungan langkah demi langkah (prosedural) untuk memverifikasi pernyataan.. Bukti: batas atas IQR (335 kWh); 750 kWh lebih besar dari batas atas IQR
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin: mengurutkan data, menghitung Q1 dan Q3, menghitung IQR, dan menerapkan rumus batas atas. Meskipun prosedurnya standar, siswa harus melakukan serangkaian perhitungan yang saling terkait.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; Mengapa angka 750 kWh dapat dianggap sebagai pencilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang kuartil, IQR, dan definisi statistik pencilan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10, menguji pemahaman statistik deskriptif dasar yang diajarkan di kurikulum SMA. |

Run 3 — solusi: Urutkan data: 300, 305, 310, 310, 310, 315, 315, 320, 320, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1,5 * IQR = 320 + 15 = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik standar untuk menentukan pencilan (outlier) menggunakan metode IQR (Interquartile Range), bukan sekadar observasi visual.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi pencilan dalam statistik deskriptif dan prosedur perhitungan batas atas menggunakan IQR.. Bukti: batas atas IQR (335 kWh); 1,5 kali median data; batas bawah=295, batas atas=335
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data, penentuan kuartil, perhitungan IQR, dan penerapan rumus batas atas. Ini adalah prosedur rutin dalam statistik kelas 10.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; batas atas IQR (335 kWh)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang median, kuartil, dan konsep dasar pencilan (outlier) dalam statistik. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 10 mengenai statistika deskriptif, di mana siswa diharapkan mampu mengidentifikasi pencilan menggunakan metode IQR. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4207`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur statistik standar untuk mendeteksi pencilan menggunakan aturan IQR (Interquartile Range), yang merupakan penerapan konsep statistik deskriptif.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang algoritma deteksi pencilan menggunakan metode IQR (Interquartile Range).
- Intended difficulty `Medium`: Soal memerlukan beberapa langkah rutin (mengurutkan, mencari kuartil, menghitung IQR, menghitung batas atas) dan pemilihan prosedur yang tepat untuk menentukan pencilan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang statistik deskriptif dasar, kuartil, dan metode deteksi pencilan (IQR). |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan penerapan rumus statistik standar pada dataset kecil. |

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

![Gambar sumber soal 38](<../images/kelas10_panduan_siswa_kelas10.pdf-0228-02.png>)


![Gambar sumber soal 38](<../images/kelas10_panduan_siswa_kelas10.pdf-0228-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Membaca komponen box plot pada sumbu: ujung whisker kiri (minimum) = 68; tepi kiri kotak (Q1) = 71; garis tengah kotak (median/Q2) = 72; tepi kanan kotak (Q3) = 76; ujung whisker kanan (maksimum) = 77. Sesuai dengan opsi A.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0228-02.png, images/kelas10_panduan_siswa_kelas10.pdf-0228-03.png. Transkripsi visual: Gambar menunjukkan sebuah box plot dengan sumbu horizontal berlabel angka 68, 70, 72, 74, 76, 80. Ujung whisker kiri berada tepat di angka 68. Tepi kiri kotak (Q1) berada di 71 (tengah antara 70 dan 72). Garis tengah kotak (median/Q2) berada di 72. Tepi kanan kotak (Q3) berada di 76. Ujung whisker kanan berada di 77 (tengah antara 76 dan 78, namun dalam konteks pilihan A, ini merepresentasikan nilai 77).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f3c0aa8b0d7dbd2db9d517f435a773797c5dd3010c8697fa6631c6da6c79bd60`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 4513 |
| 2 | success | valid / verified | applying | conceptual | Easy | 4577 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 4622 |

Run 1 — solusi: Membaca komponen box plot: ujung whisker kiri (minimum) di 68, tepi kiri kotak (Q1) di 71, garis tengah kotak (median/Q2) di 72, tepi kanan kotak (Q3) di 76, dan ujung whisker kanan (maksimum) di 77.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca dan mengidentifikasi komponen statistik dari representasi visual (box plot). Ini adalah proses langsung dalam mengenali fakta dan komponen grafik.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur dan komponen box plot (konsep statistik) untuk dapat menginterpretasikan nilai-nilai yang diminta.. Bukti: Box Plot dari data waktu yang diperlukan
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung. Siswa hanya perlu memetakan posisi komponen box plot ke skala sumbu yang diberikan. Tidak ada perhitungan kompleks atau strategi non-rutin.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.

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
| gradeRelativeRationale | Membaca grafik box plot adalah materi dasar statistik yang sesuai untuk kelas 10. Tingkat kesulitan rendah karena hanya memerlukan pembacaan langsung tanpa manipulasi data. |

Run 2 — solusi: Membaca posisi komponen box plot pada sumbu horizontal: ujung whisker kiri (minimum) = 68; tepi kiri kotak (Q1) = 71; garis tengah kotak (Q2) = 72; tepi kanan kotak (Q3) = 76; ujung whisker kanan (maksimum) = 77.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk membaca dan menginterpretasikan komponen-komponen statistik dari representasi visual (box plot). Ini adalah proses langsung dalam menerapkan pemahaman tentang definisi komponen box plot ke data yang diberikan.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara struktur visual box plot (whisker, kotak, garis median) dengan konsep statistik lima serangkai (minimum, kuartil, maksimum).. Bukti: Perhatikan Box Plot dari data waktu yang diperlukan
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan langsung. Siswa hanya perlu mengidentifikasi posisi titik-titik kunci pada grafik terhadap skala sumbu yang tersedia. Tidak ada manipulasi data atau strategi non-rutin yang diperlukan.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen box plot (minimum, kuartil, median, maksimum). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca box plot adalah materi statistik dasar yang diajarkan di tingkat SMA kelas 10. Soal ini menguji kemampuan membaca grafik secara langsung tanpa komplikasi tambahan. |

Run 3 — solusi: Membaca komponen box plot: ujung whisker kiri (minimum) di 68, tepi kiri kotak (Q1) di 71, garis tengah kotak (median/Q2) di 72, tepi kanan kotak (Q3) di 76, dan ujung whisker kanan (maksimum) di 77. Sesuai dengan opsi A.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca dan menginterpretasikan komponen-komponen statistik dari representasi visual (box plot). Ini adalah proses langsung dalam mengenali dan membaca data dari grafik yang diberikan.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur box plot (apa yang diwakili oleh whisker dan kotak) serta kemampuan faktual dalam membaca nilai dari skala grafik.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung. Siswa hanya perlu mengidentifikasi posisi titik-titik kunci pada box plot terhadap sumbu yang tersedia. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.

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
| gradeRelativeRationale | Materi box plot adalah bagian dari kurikulum statistika kelas 10. Soal ini menguji kemampuan dasar membaca grafik yang merupakan prosedur standar dan familiar bagi siswa. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `6123`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk membaca dan mengidentifikasi komponen statistik dari representasi visual (box plot). Ini adalah proses langsung dalam mengenali fakta dan komponen grafik tanpa perlu melakukan perhitungan atau strategi non-rutin.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami struktur dan komponen box plot (konsep statistik) untuk dapat menginterpretasikan nilai-nilai yang diminta dari grafik.
- Intended difficulty `Easy`: Soal ini bersifat prosedural langsung. Siswa hanya perlu memetakan posisi komponen box plot ke skala sumbu yang diberikan. Tidak ada perhitungan kompleks atau strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen box plot (minimum, kuartil, median, maksimum). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca grafik box plot adalah materi dasar statistik yang sesuai untuk kelas 10. Tingkat kesulitan rendah karena hanya memerlukan pembacaan langsung tanpa manipulasi data. |

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
Transkripsi visual: Gambar menunjukkan sebuah box plot dengan sumbu horizontal berlabel angka 68, 70, 72, 74, 76, 80. Ujung whisker kiri berada tepat di angka 68. Tepi kiri kotak (Q1) berada di 71 (tengah antara 70 dan 72). Garis tengah kotak (median/Q2) berada di 72. Tepi kanan kotak (Q3) berada di 76. Ujung whisker kanan berada di 77 (tengah antara 76 dan 78, namun dalam konteks pilihan A, ini merepresentasikan nilai 77).
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
Solusi minimum hasil AI: Data terurut (n=14): 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Median (Q2) = (65+70)/2 = 67,5. Q1 (median dari 7 data pertama) = 65. Q3 (median dari 7 data terakhir) = 80. Jangkauan antar kuartil (H) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil (Qd) = 0,5 * H = 7,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6d4ed04551ea52d79437825c6daa06663375e0450da500d3f147faabb87206a1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2577 |
| 2 | success | valid / verified | applying | procedural | Easy | 2501 |
| 3 | success | valid / verified | applying | procedural | Medium | 2570 |

Run 1 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q1 (kuartil bawah) adalah median dari 7 data pertama (50, 50, 60, 65, 65, 65, 65) yaitu 65. Q3 (kuartil atas) adalah median dari 7 data terakhir (75, 80, 80, 85, 85, 90) yaitu 80. Jangkauan antar kuartil (H) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil (Qd) = 0,5 * H = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik deskriptif (menentukan kuartil dan simpangan kuartil) pada sekumpulan data yang diberikan. Ini adalah tugas rutin yang memerlukan pemilihan dan penerapan rumus yang tepat.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan teknik statistik untuk mengukur penyebaran data, yang merupakan pengetahuan prosedural.. Bukti: kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: mengurutkan data, membagi data menjadi kelompok, menentukan median untuk setiap kelompok (Q1, Q2, Q3), dan menghitung nilai simpangan kuartil. Meskipun prosedurnya standar, jumlah data yang cukup banyak (14) meningkatkan beban kognitif dan potensi kesalahan hitung.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang median dan pengurutan data. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai latihan rutin statistik deskriptif. |

Run 2 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q1 (kuartil bawah) adalah median dari 7 data pertama: 65. Q3 (kuartil atas) adalah median dari 7 data terakhir: 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar (mengurutkan data, menentukan median untuk kuartil, dan menghitung selisih) pada sekumpulan data yang diberikan. Ini adalah penerapan konsep rutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan urutan langkah untuk menghitung ukuran penyebaran data (kuartil dan simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengurutkan data dan menerapkan rumus kuartil. Tidak ada jebakan konseptual atau strategi non-rutin yang diperlukan.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang median dan pengurutan data. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (kuartil) adalah topik standar kelas 10. Prosedur yang diminta bersifat langsung dan familiar bagi siswa. |

Run 3 — solusi: Data terurut (n=14): 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Q1 (kuartil bawah) adalah median dari 7 data pertama (50, 50, 60, 65, 65, 65, 65) yaitu 65. Q3 (kuartil atas) adalah median dari 7 data terakhir (75, 80, 80, 85, 85, 90) yaitu 80. Jangkauan antar kuartil (H) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * H = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik deskriptif standar (menentukan kuartil dan jangkauan) pada sekumpulan data yang diberikan. Ini adalah penerapan algoritma rutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan urutan langkah untuk menghitung ukuran penyebaran data (kuartil, jangkauan, simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini bersifat rutin bagi siswa kelas 10. Prosedur pengurutan data dan perhitungan kuartil adalah materi dasar yang familiar. Beban perhitungan moderat karena jumlah data (14) cukup untuk melatih ketelitian tanpa memerlukan strategi kompleks.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

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
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 10 mengenai statistik deskriptif, di mana siswa diharapkan mampu menghitung ukuran penyebaran data secara mandiri. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4505`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur statistik deskriptif standar (mengurutkan data, menentukan median untuk kuartil, dan menghitung selisih) pada sekumpulan data yang diberikan. Ini adalah penerapan konsep rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang algoritma dan urutan langkah untuk menghitung ukuran penyebaran data (kuartil, jangkauan, simpangan kuartil).
- Intended difficulty `Medium`: Soal ini bersifat rutin bagi siswa kelas 10. Prosedur pengurutan data dan perhitungan kuartil adalah materi dasar yang familiar. Beban perhitungan moderat karena jumlah data (14) cukup untuk melatih ketelitian tanpa memerlukan strategi kompleks.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 10 mengenai statistik deskriptif, di mana siswa diharapkan mampu menghitung ukuran penyebaran data secara mandiri. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `581df18ab4eeb6c5cf613ab7`

Tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.<br><br>tentukan jumlah yang lebih besar daripada 3

| Opsi | Isi |
|---|---|
| A | $\frac{3}{36}$ |
| B | $\frac{33}{36}$ |
| C | $\frac{35}{36}$ |
| D | $\frac{34}{36}$ |

![Gambar sumber soal 40](<../images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: P(jumlah > 3) = 1 - P(jumlah <= 3). P(jumlah=2) = 1/36, P(jumlah=3) = 2/36. P(jumlah <= 3) = 1/36 + 2/36 = 3/36. Maka P(jumlah > 3) = 1 - 3/36 = 33/36.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png. Transkripsi visual: Tabel 7.2 menunjukkan kolom 'Jumlah' dengan nilai 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 dan kolom 'Peluang' yang kosong. Tabel ini merepresentasikan distribusi peluang jumlah dua dadu.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3fc1ef62a6301692b4942d9165b2a697bc9ea27c680e5a66e97b2c28617dd9a9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3233 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3160 |
| 3 | success | valid / verified | applying | procedural | Easy | 3244 |

Run 1 — solusi: P(jumlah > 3) = 1 - P(jumlah <= 3). P(jumlah=2) = 1/36, P(jumlah=3) = 2/36. P(jumlah <= 3) = 1/36 + 2/36 = 3/36. Maka P(jumlah > 3) = 1 - 3/36 = 33/36.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur komplemen untuk menyelesaikan masalah dengan efisien, yang merupakan penerapan konsep peluang pada situasi rutin.. Bukti: tentukan jumlah yang lebih besar daripada 3
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep peluang komplemen dan distribusi peluang diskrit.. Bukti: distribusi peluang; tentukan jumlah yang lebih besar daripada 3
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pemahaman dasar tentang peluang komplemen dan operasi aritmetika sederhana pada ruang sampel dua dadu yang standar.. Bukti: tentukan jumlah yang lebih besar daripada 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel dua dadu dan aturan peluang komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena melibatkan konsep dasar peluang yang merupakan materi standar. |

Run 2 — solusi: P(jumlah > 3) = 1 - P(jumlah <= 3). P(jumlah=2) = 1/36, P(jumlah=3) = 2/36. Maka P(jumlah <= 3) = 1/36 + 2/36 = 3/36. P(jumlah > 3) = 1 - 3/36 = 33/36.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur komplemen (1 - P(A^c)) untuk menyelesaikan masalah dengan efisien, yang merupakan penerapan konsep peluang pada situasi rutin.. Bukti: tentukan jumlah yang lebih besar daripada 3
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara kejadian komplemen dan total peluang (konsep) serta menerapkan algoritma perhitungan peluang (prosedural).. Bukti: Tabel 7.2 distribusi peluang; tentukan jumlah yang lebih besar daripada 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Memerlukan pemahaman konsep komplemen atau penjumlahan langsung, namun prosedurnya sangat standar.. Bukti: tentukan jumlah yang lebih besar daripada 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel dua dadu dan konsep peluang komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah kurikulum standar kelas 10. Soal ini menguji pemahaman konsep dasar tanpa kompleksitas tambahan. |

Run 3 — solusi: P(jumlah > 3) = 1 - P(jumlah <= 3). P(jumlah=2) = 1/36, P(jumlah=3) = 2/36. P(jumlah <= 3) = 1/36 + 2/36 = 3/36. Maka P(jumlah > 3) = 1 - 3/36 = 33/36.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang komplemen atau penjumlahan peluang untuk menyelesaikan masalah. Ini adalah penerapan prosedur rutin dalam konteks distribusi peluang.. Bukti: tentukan jumlah yang lebih besar daripada 3
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara kejadian dan ruang sampel serta menggunakan prinsip peluang komplemen (konseptual) untuk menghitung hasil (prosedural).. Bukti: Tabel 7.2 distribusi peluang; tentukan jumlah yang lebih besar daripada 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi kejadian yang tidak diinginkan (jumlah 2 dan 3) dan mengurangkannya dari total peluang (1). Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: tentukan jumlah yang lebih besar daripada 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel pelemparan dua dadu dan konsep peluang komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menggunakan konsep dasar peluang yang sudah diperkenalkan di jenjang sebelumnya dan diperdalam di kelas 10. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4600`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur rutin (peluang komplemen) untuk menyelesaikan masalah distribusi peluang yang standar.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konsep peluang komplemen dan distribusi peluang diskrit.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Memerlukan pemahaman konsep komplemen atau penjumlahan langsung, namun prosedurnya sangat standar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel dua dadu dan aturan peluang komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar adalah kurikulum standar kelas 10. Soal ini menguji pemahaman konsep dasar tanpa kompleksitas tambahan. |

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
Transkripsi visual: Tabel 7.2 menunjukkan kolom 'Jumlah' dengan nilai 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 dan kolom 'Peluang' yang kosong. Tabel ini merepresentasikan distribusi peluang jumlah dua dadu.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `cc90109177ce7d63bb1a90a7`

Coba kamu tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.<br><br>a. jumlah 2 atau 3

| Opsi | Isi |
|---|---|
| A | $\frac{1}{36}$ |
| B | $\frac{6}{36}$ |
| C | $\frac{3}{36}$ |
| D | $\frac{2}{36}$ |

![Gambar sumber soal 41](<../images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: P(jumlah 2) = 1/36. P(jumlah 3) = 2/36. Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png. Transkripsi visual: Tabel 7.2 menampilkan kolom 'Jumlah' dengan nilai 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 dan kolom kosong 'Peluang' di sebelahnya.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b5fc7df9324bb79a8a348b2f01c86ec09671ad3bed5b0402bf6f9490c49d32c2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3187 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3191 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3149 |

Run 1 — solusi: P(jumlah 2) = 1/36. P(jumlah 3) = 2/36. Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan penjumlahan untuk kejadian saling lepas pada distribusi peluang diskrit yang sudah dipahami konsepnya.. Bukti: tentukan peluang untuk kejadian berikut; jumlah 2 atau 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang aturan penjumlahan peluang untuk kejadian saling lepas dalam konteks distribusi peluang.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan pemahaman dasar tentang aturan penjumlahan peluang untuk kejadian saling lepas (P(A atau B) = P(A) + P(B)). Tidak ada langkah non-rutin atau kompleksitas tinggi.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang

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
| gradeRelativeRationale | Sesuai untuk kelas 10 karena merupakan penerapan langsung dari aturan penjumlahan peluang yang merupakan materi dasar distribusi peluang. |

Run 2 — solusi: Peluang jumlah 2 adalah 1/36 (pasangan (1,1)). Peluang jumlah 3 adalah 2/36 (pasangan (1,2), (2,1)). Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan penjumlahan untuk kejadian saling lepas dalam distribusi peluang diskrit. Ini adalah penerapan konsep dasar peluang pada situasi rutin.. Bukti: jumlah 2 atau 3; P(jumlah 2) = 1/36 dan P(jumlah 3) = 2/36, keduanya saling lepas sehingga dijumlahkan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar peluang (kejadian saling lepas) dan bagaimana mengoperasikannya dalam distribusi peluang.. Bukti: jumlah 2 atau 3; keduanya saling lepas sehingga dijumlahkan
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan langsung. Siswa hanya perlu mengidentifikasi dua kejadian yang saling lepas dan menjumlahkan peluangnya. Tidak ada strategi non-rutin atau kompleksitas tinggi.. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel dua dadu dan aturan penjumlahan peluang kejadian saling lepas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 sebagai latihan dasar distribusi peluang diskrit. |

Run 3 — solusi: P(jumlah 2) = 1/36. P(jumlah 3) = 2/36. Karena kejadian saling lepas, P(2 atau 3) = P(2) + P(3) = 1/36 + 2/36 = 3/36.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan penjumlahan untuk kejadian saling lepas pada distribusi peluang diskrit yang sederhana.. Bukti: jumlah 2 atau 3; P(jumlah 2) = 1/36 dan P(jumlah 3) = 2/36, keduanya saling lepas sehingga dijumlahkan menjadi 3/36
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang aturan penjumlahan peluang untuk kejadian saling lepas.. Bukti: jumlah 2 atau 3; keduanya saling lepas sehingga dijumlahkan
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu keputusan utama (menjumlahkan dua peluang kejadian saling lepas).. Bukti: jumlah 2 atau 3; Tabel 7.2 distribusi peluang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel dua dadu dan aturan penjumlahan peluang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena merupakan penerapan langsung aturan penjumlahan peluang pada ruang sampel yang sudah dikenal. |

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
Transkripsi visual: Tabel 7.2 menampilkan kolom 'Jumlah' dengan nilai 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 dan kolom kosong 'Peluang' di sebelahnya.
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

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `6/36`.
Solusi minimum hasil AI: Kejadian A (dobel): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 2): {(1,1)}, n(B)=1. Irisan A dan B: {(1,1)}, n(A∩B)=1. P(A∪B) = P(A) + P(B) - P(A∩B) = 6/36 + 1/36 - 1/36 = 6/36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `26779b72c79ecce9a5f34073512ddf0c736b7bb8b7d223d5f9004bf80885e969`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2126 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2157 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2149 |

Run 1 — solusi: Kejadian A (dobel): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 2): {(1,1)}, n(B)=1. Irisan A dan B: {(1,1)}, n(A∩B)=1. P(A∪B) = P(A) + P(B) - P(A∩B) = 6/36 + 1/36 - 1/36 = 6/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian yang tidak saling lepas, menentukan ruang sampel, dan menerapkan rumus peluang gabungan P(A∪B) = P(A) + P(B) - P(A∩B). Ini adalah penerapan prosedur rutin pada situasi probabilitas.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip aturan penjumlahan dalam probabilitas, termasuk konsep kejadian tidak saling lepas.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi bahwa kedua kejadian tidak saling lepas (irisan tidak kosong) dan menerapkan prinsip inklusi-eksklusi, bukan sekadar menjumlahkan peluang secara langsung.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan kejadian saling lepas dan tidak saling lepas dalam konteks peluang sederhana. |

Run 2 — solusi: Ruang sampel n(S)=36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 2): {(1,1)}, n(B)=1. Irisan A dan B: {(1,1)}, n(A∩B)=1. P(A∪B) = P(A) + P(B) - P(A∩B) = 6/36 + 1/36 - 1/36 = 6/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian yang tidak saling lepas, menentukan peluang masing-masing, dan menerapkan rumus aturan penjumlahan P(A atau B) = P(A) + P(B) - P(A dan B). Ini adalah penerapan prosedur rutin pada situasi probabilitas.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep kejadian tidak saling lepas dan penggunaan rumus aturan penjumlahan dalam probabilitas.. Bukti: Gunakan aturan penjumlahan; dua angka sama atau berjumlah 2
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus menyadari bahwa kejadian 'angka sama' dan 'jumlah 2' tidak saling lepas (ada irisan), sehingga memerlukan pemilihan prosedur yang tepat (pengurangan irisan) daripada sekadar menjumlahkan peluang.. Bukti: sepasang dadu yang dilempar; dua angka sama atau berjumlah 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, ruang sampel dua dadu, dan aturan penjumlahan peluang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu mengidentifikasi irisan antar kejadian dalam ruang sampel diskrit sederhana. |

Run 3 — solusi: Ruang sampel n(S)=36. Kejadian A (angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 2): {(1,1)}, n(B)=1. Irisan A dan B: {(1,1)}, n(A irisan B)=1. P(A atau B) = P(A) + P(B) - P(A irisan B) = 6/36 + 1/36 - 1/36 = 6/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian yang tidak saling lepas, menentukan peluang masing-masing, dan menerapkan rumus aturan penjumlahan P(A atau B) = P(A) + P(B) - P(A irisan B). Ini adalah penerapan prosedur rutin pada situasi peluang.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar aturan penjumlahan dalam peluang, yang merupakan konsep fundamental dalam statistika/peluang.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus menyadari bahwa kedua kejadian tidak saling lepas (ada irisan) dan melakukan operasi pengurangan irisan, bukan sekadar menjumlahkan peluang secara langsung.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman ruang sampel dua dadu dan konsep peluang kejadian majemuk. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu membedakan kejadian saling lepas dan tidak saling lepas dalam ruang sampel diskrit. |

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

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Kejadian A (dua angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B)=4. Karena A dan B saling lepas (tidak ada irisan), P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d929ba8e3996f7e8526e4a47851733fb3b61a5d5c832830013bc97b5f8e99335`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2121 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2051 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2132 |

Run 1 — solusi: Kejadian A (dua angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B)=4. Karena A dan B saling lepas (tidak ada irisan), P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian yang berbeda, menentukan ruang sampel masing-masing, memeriksa apakah kejadian tersebut saling lepas, dan menerapkan aturan penjumlahan peluang.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kejadian saling lepas dalam peluang dan penerapan prosedur aturan penjumlahan.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut; dua angka sama atau berjumlah 5
- Intended difficulty `classify/Medium`: Soal ini memerlukan identifikasi dua kejadian yang berbeda dan penerapan aturan penjumlahan dasar. Siswa harus memahami konsep 'saling lepas' untuk menghindari kesalahan perhitungan irisan.. Bukti: dua angka sama atau berjumlah 5; Gunakan aturan penjumlahan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar ruang sampel dua dadu dan definisi peluang kejadian sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang dasar adalah standar kelas 10. Soal ini menuntut ketelitian dalam mendaftar anggota ruang sampel dan memahami syarat kejadian saling lepas. |

Run 2 — solusi: Kejadian A (dua angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (jumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B)=4. Karena A dan B saling lepas (tidak ada irisan), P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian, memeriksa apakah saling lepas, dan menerapkan aturan penjumlahan peluang dasar.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep peluang kejadian saling lepas dan penerapan prosedur penjumlahan peluang.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 10 yang mempelajari peluang. Siswa hanya perlu mendaftar ruang sampel kejadian sederhana dan menjumlahkannya.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel dua dadu dan konsep peluang kejadian saling lepas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang dasar adalah standar kurikulum kelas 10. Soal ini tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Kejadian A (dua angka sama): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, n(A)=6. Kejadian B (berjumlah 5): {(1,4), (2,3), (3,2), (4,1)}, n(B)=4. Karena A dan B saling lepas (tidak ada irisan), P(A atau B) = P(A) + P(B) = 6/36 + 4/36 = 10/36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua kejadian yang berbeda, menentukan ruang sampel masing-masing, dan menerapkan aturan penjumlahan peluang untuk kejadian saling lepas.. Bukti: Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kejadian saling lepas dalam peluang dan penerapan prosedur penjumlahan peluang.. Bukti: Gunakan aturan penjumlahan untuk soal-soal berikut; dua angka sama atau berjumlah 5
- Intended difficulty `classify/Medium`: Soal ini memerlukan identifikasi dua himpunan kejadian yang berbeda dan verifikasi apakah kejadian tersebut saling lepas. Ini adalah prosedur rutin dalam materi peluang kelas 10.. Bukti: sepasang dadu yang dilempar; dua angka sama atau berjumlah 5

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar ruang sampel dua dadu dan definisi kejadian saling lepas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini standar untuk kelas 10, menguji pemahaman tentang aturan penjumlahan peluang tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3619`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi dua kejadian, menentukan ruang sampel masing-masing, memeriksa apakah kejadian tersebut saling lepas, dan menerapkan aturan penjumlahan peluang.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang kejadian saling lepas dalam peluang dan penerapan prosedur penjumlahan peluang.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 10. Siswa perlu mendaftar anggota ruang sampel untuk dua kejadian berbeda dan memastikan apakah kejadian tersebut saling lepas sebelum menjumlahkan peluangnya.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar ruang sampel dua dadu dan konsep peluang kejadian saling lepas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang dasar adalah standar kurikulum kelas 10. Soal ini tidak memerlukan strategi non-rutin atau integrasi kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: P(A) = peluang muncul angka dobel pada sepasang dadu = 6/36 = 1/6. P(B) = peluang jumlah mata dadu 6 pada sepasang dadu = {(1,5), (2,4), (3,3), (4,2), (5,1)} = 5/36. Karena lemparan pertama dan kedua adalah kejadian saling bebas, maka P(A dan B) = P(A) × P(B) = 1/6 × 5/36 = 5/216.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `abb72905b7b5356a372dfe76e46be58fc18bced9ffaeefd4003a069409393617`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2208 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2157 |
| 3 | success | valid / verified | applying | procedural | Medium | 2128 |

Run 1 — solusi: P(A) = peluang muncul angka dobel = 6/36 = 1/6. P(B) = peluang jumlah mata dadu 6 = {(1,5), (2,4), (3,3), (4,2), (5,1)} = 5/36. Karena dua lemparan dadu adalah kejadian saling bebas, maka P(A dan B) = P(A) × P(B) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep kejadian saling bebas dan menerapkan aturan perkalian peluang untuk dua kejadian yang berurutan, yang merupakan penerapan prosedur pada situasi rutin.. Bukti: Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; P(dobel) = 6/36 = 1/6 dan P(jumlah 6) = 5/36; karena saling bebas, 1/6 × 5/36 = 5/216
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar peluang (kejadian saling bebas) dan penggunaan algoritma perkalian peluang.. Bukti: Mengapa aturan perkalian dapat digunakan; karena saling bebas, 1/6 × 5/36 = 5/216
- Intended difficulty `classify/Medium`: Soal ini memerlukan identifikasi dua kejadian terpisah, menghitung peluang masing-masing, dan menerapkan aturan perkalian. Ini adalah prosedur standar untuk kelas 10.. Bukti: melemparkan sepasang dadu dan mendapatkan angka dobel; pada lemparan kedua mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian tunggal dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang kejadian saling bebas adalah standar kurikulum kelas 10. Soal ini menuntut pemahaman konsep dan perhitungan dasar tanpa kompleksitas tinggi. |

Run 2 — solusi: P(A) = peluang muncul angka dobel pada sepasang dadu = 6/36 = 1/6. P(B) = peluang jumlah mata dadu 6 pada sepasang dadu = {(1,5), (2,4), (3,3), (4,2), (5,1)} = 5/36. Karena kedua lemparan saling bebas, P(A dan B) = P(A) × P(B) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Soal menuntut siswa memahami syarat kejadian saling bebas untuk menerapkan aturan perkalian peluang, bukan sekadar menghitung, sehingga masuk kategori applying.. Bukti: Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar peluang kejadian saling bebas (konsep) dan menerapkan prosedur perkalian peluang (prosedural).. Bukti: aturan perkalian dapat digunakan; peluang ini dapat terjadi
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang ruang sampel sepasang dadu (36 titik sampel) dan identifikasi kejadian saling bebas. Ini adalah tugas rutin dalam materi peluang kelas 10.. Bukti: melemparkan sepasang dadu; mendapatkan angka dobel; mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman ruang sampel sepasang dadu dan konsep peluang kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang kejadian saling bebas adalah standar kelas 10. Soal ini memerlukan dua langkah perhitungan peluang terpisah sebelum dikalikan, yang sesuai untuk tingkat kesulitan menengah. |

Run 3 — solusi: P(A) = P(dobel) = 6/36 = 1/6. P(B) = P(jumlah 6) = 5/36. Karena lemparan pertama dan kedua adalah kejadian saling bebas, maka P(A dan B) = P(A) × P(B) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi syarat kejadian saling bebas (konseptual) dan menerapkan aturan perkalian peluang (prosedural) untuk dua kejadian yang berurutan.. Bukti: Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip kejadian saling bebas (konseptual) dan menerapkan algoritma perkalian peluang (prosedural) untuk menyelesaikan masalah.. Bukti: aturan perkalian dapat digunakan; peluang ini dapat terjadi
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang dua kejadian terpisah yang saling bebas. Siswa harus menghitung peluang masing-masing kejadian (dobel dan jumlah 6) lalu mengalikannya. Ini adalah prosedur rutin dalam materi peluang kelas 10.. Bukti: melemparkan sepasang dadu; mendapatkan angka dobel; mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian tunggal pada ruang sampel dua dadu (36 titik sampel). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang dua kejadian saling bebas adalah standar kurikulum kelas 10. Soal ini menguji pemahaman dasar tentang aturan perkalian tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3855`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas, kemudian menerapkan aturan perkalian peluang. Ini adalah penerapan prosedur standar pada situasi rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang prinsip kejadian saling bebas (konseptual) dan penggunaan algoritma perkalian peluang (prosedural).
- Intended difficulty `Medium`: Soal memerlukan pemahaman tentang ruang sampel sepasang dadu (36 titik sampel) dan identifikasi kejadian saling bebas. Ini adalah tugas rutin dalam materi peluang kelas 10.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian tunggal pada ruang sampel dua dadu dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang kejadian saling bebas adalah standar kurikulum kelas 10. Soal ini menuntut pemahaman konsep dan perhitungan dasar tanpa kompleksitas tinggi. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Peluang muncul angka genap pada satu lemparan dadu adalah 3/6 = 1/2. Karena dua lemparan dadu adalah kejadian saling bebas (independen), maka peluang muncul angka genap pada kedua lemparan adalah (1/2) * (1/2) = 1/4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `88d562a71a9ff85b2f171a909c059836df47e0af4e692b370907253e8be0f0f3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1990 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2046 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1998 |

Run 1 — solusi: Peluang muncul angka genap pada satu dadu adalah 3/6 = 1/2. Karena pelemparan dadu pertama dan kedua adalah kejadian saling bebas, maka peluang muncul angka genap pada kedua lemparan adalah (1/2) * (1/2) = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi peluang kejadian tunggal (angka genap) dan menerapkan aturan perkalian untuk kejadian saling bebas. Ini adalah penerapan prosedur rutin dalam konteks peluang.. Bukti: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan dua angka genap
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang aturan perkalian peluang (konsep) dan penggunaan algoritma perhitungan peluang kejadian saling bebas (prosedural).. Bukti: Hitung peluang untuk mendapatkan dua angka genap
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami peluang satu kejadian dan mengalikannya. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan dua angka genap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar dengan dua kejadian saling bebas adalah standar untuk kelas 10, prosedurnya sangat familiar dan langsung. |

Run 2 — solusi: Peluang muncul angka genap pada satu lemparan dadu adalah 3/6 = 1/2. Karena dua lemparan dadu adalah kejadian independen, peluang muncul angka genap pada kedua lemparan adalah (1/2) * (1/2) = 1/4.
- Domain kognitif `classify/applying`: Soal meminta penerapan aturan perkalian untuk kejadian independen (peluang dua kejadian terjadi bersamaan). Siswa perlu mengidentifikasi peluang kejadian tunggal dan mengalikannya, yang merupakan prosedur standar dalam materi peluang kelas 10.. Bukti: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan dua angka genap
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip dasar peluang kejadian independen dan bagaimana mengoperasikan peluang tersebut (aturan perkalian), yang merupakan pemahaman konseptual tentang hubungan antar kejadian.. Bukti: Hitung peluang untuk mendapatkan dua angka genap
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami konsep peluang kejadian independen dan melakukan satu operasi perkalian sederhana. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Sebuah dadu dilempar dua kali; dua angka genap

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
| gradeRelativeRationale | Materi peluang dasar dengan dua kejadian independen adalah standar kurikulum kelas 10. Soal ini tidak memerlukan analisis ruang sampel yang rumit karena dapat diselesaikan langsung dengan aturan perkalian. |

Run 3 — solusi: Peluang muncul angka genap pada satu lemparan dadu adalah 3/6 = 1/2. Karena dua lemparan dadu adalah kejadian independen, peluang keduanya genap adalah P(genap) × P(genap) = 1/2 × 1/2 = 1/4.
- Domain kognitif `classify/applying`: Soal meminta penerapan aturan perkalian untuk kejadian independen (dua lemparan dadu). Siswa perlu mengidentifikasi peluang kejadian tunggal dan mengalikannya, yang merupakan prosedur standar dalam materi peluang.. Bukti: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan dua angka genap
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip perkalian untuk kejadian independen dalam teori peluang, yang merupakan pemahaman konseptual tentang bagaimana kejadian-kejadian digabungkan.. Bukti: Hitung peluang untuk mendapatkan dua angka genap
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang melibatkan dua langkah sederhana: menentukan peluang satu kejadian dan mengalikan hasilnya. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Sebuah dadu dilempar dua kali; Hitung peluang untuk mendapatkan dua angka genap

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
| gradeRelativeRationale | Materi peluang dasar untuk dua kejadian independen adalah standar kurikulum kelas 10. Soal ini menguji pemahaman langsung tanpa jebakan atau kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3463`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi peluang kejadian tunggal (angka genap) dan menerapkan aturan perkalian untuk kejadian saling bebas. Ini adalah penerapan prosedur rutin dalam konteks peluang.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang aturan perkalian peluang (konsep) dan penggunaan algoritma perhitungan peluang kejadian saling bebas (prosedural).
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami peluang satu kejadian dan mengalikannya. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dasar dengan dua kejadian saling bebas adalah standar untuk kelas 10, prosedurnya sangat familiar dan langsung. |

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

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 ekuivalen dengan jumlah 3 angka < 6. Kemungkinan jumlah: 3 (1,1,1: 1 cara), 4 (1,1,2: 3 cara), 5 (1,1,3: 3 cara; 1,2,2: 3 cara). Total kejadian = 1 + 3 + 3 + 3 = 10. Peluang = 10/125.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b141c8a0f70431370f2a6edfeab69a82fb39f7a6f0ca0e2fd9ce8322f6527b7d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3069 |
| 2 | success | valid / verified | applying | procedural | Medium | 3043 |
| 3 | success | valid / verified | applying | procedural | Medium | 2257 |

Run 1 — solusi: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 ekuivalen dengan jumlah 3 angka < 6. Kemungkinan jumlah: 3 (1,1,1: 1 cara), 4 (1,1,2: 3 cara), 5 (1,1,3: 3 cara; 1,2,2: 3 cara). Total kejadian = 1 + 3 + 3 + 3 = 10. Peluang = 10/125.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prinsip pencacahan dan memahami hubungan antara rata-rata dan jumlah total untuk menentukan ruang sampel yang memenuhi syarat.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan penerapan algoritma pencacahan (permutasi dengan pengulangan) untuk menghitung kejadian yang memenuhi syarat.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Soal memerlukan translasi representasi (rata-rata ke jumlah) dan pencacahan sistematis, yang merupakan tugas rutin namun memerlukan ketelitian.. Bukti: rata-ratanya kurang dari 2; memutar roda tersebut sebanyak tiga kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan perkalian (prinsip dasar membilang) dan konsep dasar peluang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman peluang kejadian majemuk dengan ruang sampel yang terukur. |

Run 2 — solusi: Total ruang sampel = 5^3 = 125. Rata-rata < 2 berarti jumlah 3 angka < 6. Kemungkinan jumlah: 3 (1,1,1) ada 1 cara; 4 (1,1,2, permutasi 3) ada 3 cara; 5 (1,1,3, permutasi 3; 1,2,2, permutasi 3) ada 6 cara. Total kejadian = 1+3+6 = 10. Peluang = 10/125.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep ruang sampel dan menghitung kejadian yang memenuhi syarat (rata-rata < 2) melalui enumerasi sistematis.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan prosedur sistematis untuk menghitung ruang sampel dan kejadian yang memenuhi kondisi tertentu.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Memerlukan beberapa langkah rutin (menghitung total ruang sampel, menerjemahkan rata-rata ke jumlah, enumerasi kejadian) yang saling terkait.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, aturan perkalian, dan rata-rata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 10 karena menguji pemahaman peluang kejadian majemuk dengan enumerasi sederhana. |

Run 3 — solusi: Total ruang sampel = 5^3 = 125. Rata-rata < 2 berarti jumlah ketiga angka < 6. Kemungkinan jumlah: (1,1,1) -> jumlah 3 (1 cara); (1,1,2), (1,2,1), (2,1,1) -> jumlah 4 (3 cara); (1,1,3), (1,3,1), (3,1,1), (1,2,2), (2,1,2), (2,2,1) -> jumlah 5 (6 cara). Total kejadian = 1 + 3 + 6 = 10. Peluang = 10/125.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep ruang sampel dari kejadian majemuk dan menerjemahkan kondisi rata-rata ke dalam batasan jumlah (sum) untuk menghitung peluang kejadian yang memenuhi syarat.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prinsip dasar peluang dan aturan perkalian untuk menentukan ruang sampel serta menghitung kejadian yang memenuhi kondisi tertentu.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang ruang sampel (5^3) dan enumerasi sistematis untuk jumlah yang memenuhi kondisi (jumlah < 6). Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, aturan perkalian, dan rata-rata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 10 diharapkan mampu melakukan enumerasi sistematis untuk ruang sampel kecil dan memahami hubungan antara rata-rata dan jumlah total. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
