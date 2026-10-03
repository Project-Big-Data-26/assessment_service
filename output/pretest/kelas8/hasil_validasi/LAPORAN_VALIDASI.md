# Validasi ulang soal kelas 8 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v6-blind-smp8-key-verified`. Rubrik: `math-rubric-3x4x3-v4-smp8-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 8 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 8, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 36, "knowing": 4, "reasoning": 2}, "knowledgeDimension": {"conceptual": 15, "procedural": 26, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 24, "Medium": 17, "Hard": 1}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 36, "knowing": 4, "reasoning": 2}, "knowledgeDimension": {"conceptual": 15, "procedural": 26, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 24, "Medium": 17, "Hard": 1}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 42}`.
Run awal sukses: 126/126; adjudikasi: 11; token sukses tercatat: 342,808.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 24 | 24 | [Easy.json](difficulty/Easy.json) |
| Medium | 17 | 17 | [Medium.json](difficulty/Medium.json) |
| Hard | 1 | 1 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 8, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 8, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 8. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMP.

## 1. Soal `93921cd412ef4ff1b28e79c7`

Dalam sebuah permainan kartu angka, 6 orang siswa mengambil satu kartu angka secara acak. Byoma mengambil kartu angka  6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi  mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3. Jika setiap siswa berpasangan dengan siswa yang lain,<br><br>Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?

| Opsi | Isi |
|---|---|
| A | Bathari |
| B | Lestari |
| C | Pranawa |
| D | Byoma |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rahagi memiliki angka 4. Pasangan yang mungkin adalah Byoma(6), Pranawa(5), Lestari(7), Bathari(8), Dwi(3). Kita membandingkan 4^x atau x^4 untuk setiap x. Pasangan dengan Bathari(8) menghasilkan 4^8 = 65.536 atau 8^4 = 4.096. Nilai terbesar adalah 65.536.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b68ac01fbd975dbfca731dd79898c950c504659fbce5cff0151b394052eb0eba`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2099 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2131 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2106 |

Run 1 — solusi: Rahagi memiliki angka 4. Pasangan yang mungkin adalah Byoma(6), Pranawa(5), Lestari(7), Bathari(8), Dwi(3). Kita membandingkan 4^x atau x^4 untuk setiap x. Pasangan dengan Bathari(8) menghasilkan 4^8 = 65.536 atau 8^4 = 4.096. Nilai terbesar adalah 65.536.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep perpangkatan dan membandingkan hasil operasi bilangan berpangkat untuk menentukan nilai terbesar, yang merupakan penerapan konsep dalam situasi rutin.. Bukti: Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip operasi perpangkatan (konseptual) untuk membandingkan hasil dari berbagai kemungkinan pasangan.. Bukti: angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Easy`: Soal ini memerlukan perbandingan nilai perpangkatan sederhana. Siswa hanya perlu mengidentifikasi pasangan yang menghasilkan nilai terbesar dengan membandingkan hasil operasi yang familiar.. Bukti: Rahagi mengambil angka 4; Bathari mengambil kartu angka 8; menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perpangkatan bilangan bulat positif. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah sangat familiar dengan operasi perpangkatan. Tugas ini hanya meminta perbandingan nilai sederhana tanpa kompleksitas aljabar yang tinggi. |

Run 2 — solusi: Rahagi memiliki angka 4. Pasangan yang mungkin adalah 3, 5, 6, 7, 8. Kita membandingkan 4^x atau x^4 untuk setiap x. Pasangan dengan Bathari (8) menghasilkan 4^8 = 65.536 atau 8^4 = 4.096. Nilai terbesar adalah 65.536. Pasangan lain: 4^7=16.384, 4^6=4.096, 4^5=1.024, 4^3=64. Maka, Bathari adalah pasangan yang tepat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perpangkatan untuk membandingkan hasil dari beberapa kemungkinan pasangan, yang merupakan penerapan konsep pada situasi rutin.. Bukti: Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip operasi perpangkatan (konsep) untuk menentukan nilai terbesar dari berbagai kombinasi.. Bukti: angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Easy`: Soal memerlukan perbandingan beberapa hasil perpangkatan sederhana. Prosedurnya rutin dan familiar bagi siswa kelas 8.. Bukti: Byoma mengambil kartu angka 6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi perpangkatan bilangan bulat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah terbiasa dengan operasi perpangkatan dan perbandingan nilai bilangan, sehingga soal ini termasuk kategori mudah. |

Run 3 — solusi: Rahagi memiliki angka 4. Pasangan yang mungkin adalah Byoma(6), Pranawa(5), Lestari(7), Bathari(8), Dwi(3). Kita bandingkan nilai terbesar dari pasangan (4,x) yaitu max(4^x, x^4): 4^6=4096, 4^5=1024, 4^7=16384, 4^8=65536, 4^3=64. Nilai terbesar adalah 65536 saat berpasangan dengan Bathari (8).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep perpangkatan dan membandingkan hasil operasi bilangan berpangkat untuk menentukan nilai terbesar, yang merupakan penerapan konsep dasar.. Bukti: Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip operasi bilangan berpangkat (konsep) untuk memecahkan masalah perbandingan nilai.. Bukti: angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Easy`: Soal ini melibatkan perbandingan beberapa hasil perpangkatan sederhana. Siswa hanya perlu melakukan perhitungan rutin dan membandingkan hasilnya untuk menemukan nilai maksimum.. Bukti: Rahagi (4) dengan siswa lain; 4^8 = 65.536 adalah nilai terbesar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perpangkatan bilangan bulat positif. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan operasi perpangkatan. Tugas membandingkan hasil perpangkatan adalah prosedur rutin yang sesuai untuk tingkat kesulitan rendah. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Bilangan Berpangkat Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam sebuah permainan kartu angka, 6 orang siswa mengambil satu kartu angka secara acak. Byoma mengambil kartu angka 6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3. Jika setiap siswa berpasangan dengan siswa yang lain,

Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?
Pilihan: A. Bathari
B. Lestari
C. Pranawa
D. Byoma
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `864dfc1e16dfcf65cd20bd5a`

Dalam sebuah permainan kartu angka, 6 orang siswa mengambil satu kartu angka secara acak. Byoma mengambil kartu angka  6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi  mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3. Jika setiap siswa berpasangan dengan siswa yang lain,<br><br>Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?

| Opsi | Isi |
|---|---|
| A | Rahagi |
| B | Pranawa |
| C | Dwi |
| D | Byoma |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Lestari memiliki angka 7. Siswa lain memiliki angka: Byoma(6), Pranawa(5), Rahagi(4), Bathari(8), Dwi(3). Kita membandingkan hasil perpangkatan: 7^x atau x^7. Pasangan dengan Dwi (3) menghasilkan 3^7 = 2.187 atau 7^3 = 343. Pasangan lain: 7^4=2.401, 7^5=16.807, 7^6=117.649, 7^8=5.764.801. Nilai terkecil dari semua kemungkinan pasangan Lestari adalah 343 (dari 7^3). Maka Dwi adalah pasangan yang tepat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ef24723a94268180ab78495e5f7f7b557315a01d07efeff77cd6d770423e29f5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2163 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2122 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2278 |

Run 1 — solusi: Lestari memiliki angka 7. Siswa lain memiliki angka: Byoma(6), Pranawa(5), Rahagi(4), Bathari(8), Dwi(3). Kita membandingkan hasil perpangkatan: 7^x atau x^7. Pasangan dengan Dwi (3) menghasilkan 3^7 = 2.187 atau 7^3 = 343. Pasangan lain: 7^4=2.401, 7^5=16.807, 7^6=117.649, 7^8=5.764.801. Nilai terkecil dari semua kemungkinan pasangan Lestari adalah 343 (dari 7^3). Maka Dwi adalah pasangan yang tepat.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan hasil operasi perpangkatan dari berbagai pasangan bilangan untuk menentukan nilai minimum. Ini melibatkan penerapan konsep perpangkatan dalam situasi perbandingan.. Bukti: Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip operasi perpangkatan (konsep) untuk memecahkan masalah perbandingan nilai.. Bukti: angka Lestari dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan perbandingan nilai perpangkatan dari beberapa pasangan bilangan. Prosedurnya rutin namun memerlukan ketelitian dalam membandingkan hasil.. Bukti: 6 orang siswa mengambil satu kartu angka secara acak; angka Lestari dipangkatkan dengan pasangannya atau sebaliknya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan berpangkat bulat positif dan perbandingan bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari bilangan berpangkat. Soal ini menuntut siswa melakukan komputasi perbandingan sederhana namun cukup banyak untuk menentukan nilai terkecil. |

Run 2 — solusi: Lestari memegang angka 7. Pasangan yang mungkin adalah: 7^6 (Byoma), 7^5 (Pranawa), 7^4 (Rahagi), 7^8 (Bathari), 7^3 (Dwi). Atau sebaliknya: 6^7, 5^7, 4^7, 8^7, 3^7. Membandingkan basis dan eksponen, nilai terkecil dihasilkan oleh 3^7 = 2.187. Pasangan Lestari (7) dengan Dwi (3) menghasilkan nilai terkecil.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep perpangkatan dan membandingkan nilai hasil perpangkatan untuk menentukan nilai terkecil dari beberapa kemungkinan pasangan.. Bukti: Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan prinsip operasi perpangkatan (konseptual) untuk membandingkan hasil dari berbagai kombinasi pasangan.. Bukti: angka Lestari dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Medium`: Soal memerlukan perbandingan nilai perpangkatan dengan basis dan eksponen yang berbeda. Siswa harus menguji beberapa kemungkinan pasangan untuk menemukan nilai terkecil.. Bukti: 6 orang siswa mengambil satu kartu angka secara acak; angka Lestari dipangkatkan dengan pasangannya atau sebaliknya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi perpangkatan bilangan bulat positif. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu membandingkan nilai bilangan berpangkat. Soal ini menuntut ketelitian dalam membandingkan hasil operasi tanpa harus menghitung semua nilai secara eksak. |

Run 3 — solusi: Lestari memiliki angka 7. Siswa lain memiliki angka: Byoma(6), Pranawa(5), Rahagi(4), Bathari(8), Dwi(3). Kita membandingkan hasil perpangkatan: 7^x atau x^7. Pasangan dengan Dwi (3) menghasilkan 3^7 = 2.187 atau 7^3 = 343. Pasangan dengan Rahagi (4) menghasilkan 4^7 = 16.384 atau 7^4 = 2.401. Pasangan dengan Pranawa (5) menghasilkan 5^7 = 78.125 atau 7^5 = 16.807. Pasangan dengan Byoma (6) menghasilkan 6^7 = 279.936 atau 7^6 = 117.649. Pasangan dengan Bathari (8) menghasilkan 8^7 = 2.097.152 atau 7^8 = 5.764.801. Nilai terkecil dari semua kemungkinan adalah 343 (dari 7^3). Maka, pasangan yang menghasilkan nilai terkecil adalah Dwi.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan hasil perpangkatan dari berbagai pasangan angka yang tersedia untuk menentukan nilai terkecil. Ini melibatkan penerapan konsep perpangkatan dalam situasi perbandingan.. Bukti: Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip perpangkatan (konsep) untuk membandingkan hasil operasi bilangan.. Bukti: angka Lestari dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Medium`: Soal memerlukan perbandingan beberapa hasil perpangkatan. Meskipun angkanya sederhana, siswa harus melakukan beberapa perhitungan rutin dan membandingkannya untuk menemukan nilai minimum.. Bukti: Byoma mengambil kartu angka 6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perpangkatan bilangan bulat. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi perpangkatan dan membandingkan nilai bilangan, namun soal ini menuntut ketelitian dalam membandingkan beberapa kemungkinan pasangan. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Bilangan Berpangkat Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam sebuah permainan kartu angka, 6 orang siswa mengambil satu kartu angka secara acak. Byoma mengambil kartu angka 6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3. Jika setiap siswa berpasangan dengan siswa yang lain,

Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?
Pilihan: A. Rahagi
B. Pranawa
C. Dwi
D. Byoma
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `9eeb60ca1e3ebdc6a02a1999`

Coba sederhanakan bentuk akar berikut. $3\sqrt{2} \times 6\sqrt{6}$

| Opsi | Isi |
|---|---|
| A | $2\sqrt{3}$ |
| B | $36\sqrt{3}$ |
| C | $18\sqrt{3}$ |
| D | $36\sqrt{2}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 3√2 × 6√6 = (3 × 6) × √(2 × 6) = 18√12 = 18 × 2√3 = 36√3
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5d3f88ef1d112202b7929146785f271dc0a2189e6ecf95513801f28a72519fb3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2543 |
| 2 | success | valid / verified | applying | procedural | Easy | 2939 |
| 3 | success | valid / verified | applying | procedural | Easy | 1983 |

Run 1 — solusi: 3√2 × 6√6 = (3 × 6) × √(2 × 6) = 18√12 = 18 × 2√3 = 36√3
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan perkalian bentuk akar (a√(b) × c√(d) = ac√(bd)) dan menyederhanakan hasilnya. Ini adalah penerapan prosedur standar.. Bukti: 3√2 × 6√6
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma perkalian bentuk akar dan penyederhanaan akar kuadrat.. Bukti: 3√2 × 6√6
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang langsung, melibatkan perkalian koefisien dan radikan, serta penyederhanaan akar kuadrat dasar yang umum di kelas 8.. Bukti: 3√2 × 6√6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian bentuk akar dan penyederhanaan akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi ini adalah standar kurikulum kelas 8 untuk materi bentuk akar, tidak memerlukan strategi non-rutin. |

Run 2 — solusi: 3√2 × 6√6 = (3 × 6) × √(2 × 6) = 18√12 = 18 × 2√3 = 36√3
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan perkalian bentuk akar (a√(b) × c√(d) = ac√(bd)) dan menyederhanakan hasil akar.. Bukti: 3√2 × 6√6
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perkalian pada bilangan bentuk akar.. Bukti: 3√2 × 6√6
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin perkalian bentuk akar yang langsung, tidak memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: 3√2 × 6√6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat perkalian bentuk akar dan penyederhanaan akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian bentuk akar adalah materi standar kelas 8 yang bersifat rutin. |

Run 3 — solusi: 3√2 × 6√6 = (3 × 6) × √(2 × 6) = 18 × √12 = 18 × √(4 × 3) = 18 × 2√3 = 36√3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan perkalian bentuk akar (a√b × c√d = ac√(bd)) dan menyederhanakan akar kuadrat. Ini adalah prosedur rutin yang dipelajari di kelas 8.. Bukti: 3√2 × 6√6
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian bentuk akar dan penyederhanaan bentuk akar.. Bukti: 3√2 × 6√6
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi rutin perkalian koefisien dan radikan, diikuti penyederhanaan akar. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: 3√2 × 6√6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian bilangan bentuk akar dan penyederhanaan akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 8 mengenai operasi bilangan bentuk akar. |

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Bilangan Bentuk Akar
Tipe soal: multiple_choice
Stimulus: -
Soal: Coba sederhanakan bentuk akar berikut. $3\sqrt{2} \times 6\sqrt{6}$
Pilihan: A. $2\sqrt{3}$
B. $36\sqrt{3}$
C. $18\sqrt{3}$
D. $36\sqrt{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `8c189810bd620fa2b116eab9`

Coba buatlah dalam bentuk yang paling sederhana. $3\sqrt{2} + 5\sqrt{2}$

| Opsi | Isi |
|---|---|
| A | $8\sqrt{4}$ |
| B | $3\sqrt{2}$ |
| C | $15\sqrt{2}$ |
| D | $8\sqrt{2}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Penjumlahan bentuk akar sejenis dilakukan dengan menjumlahkan koefisiennya saja: 3√2 + 5√2 = (3 + 5)√2 = 8√2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `51aad8f80d5196d8b0989315f15825a5f91a832c0ec968848d589203f2156f94`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1883 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1890 |
| 3 | success | valid / verified | applying | procedural | Easy | 1873 |

Run 1 — solusi: Penjumlahan bentuk akar sejenis dilakukan dengan menjumlahkan koefisiennya saja: 3√2 + 5√2 = (3 + 5)√2 = 8√2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan aturan penjumlahan bentuk akar sejenis (distributif), yang merupakan prosedur rutin dalam materi bentuk akar.. Bukti: 3√2 + 5√2
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau aturan penjumlahan pada bentuk akar (prosedural).. Bukti: 3√2 + 5√2
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya melibatkan satu langkah operasi penjumlahan koefisien pada bentuk akar yang sudah sejenis.. Bukti: 3√2 + 5√2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan aljabar (variabel sejenis) dan bentuk akar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari operasi bentuk akar. Soal ini adalah latihan dasar yang rutin. |

Run 2 — solusi: Operasi penjumlahan bentuk akar sejenis dilakukan dengan menjumlahkan koefisiennya: 3√2 + 5√2 = (3 + 5)√2 = 8√2.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan aturan penjumlahan pada bentuk akar sejenis secara langsung. Siswa hanya perlu menjumlahkan koefisien (3 dan 5) sementara bentuk akarnya tetap.. Bukti: 3√2 + 5√2
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip penjumlahan bentuk akar sejenis, yang merupakan bagian dari konsep dasar operasi aljabar pada bilangan irasional.. Bukti: 3√2 + 5√2
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dengan satu langkah operasi langsung tanpa variasi atau kendala tambahan.. Bukti: 3√2 + 5√2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan suku sejenis dalam aljabar dan sifat bentuk akar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari operasi bentuk akar sebagai bagian dari materi bilangan berpangkat dan akar. Soal ini adalah latihan rutin yang sangat mendasar. |

Run 3 — solusi: Penjumlahan bentuk akar sejenis dilakukan dengan menjumlahkan koefisiennya saja, sedangkan bagian akarnya tetap. Jadi, 3√2 + 5√2 = (3 + 5)√2 = 8√2.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan aturan penjumlahan bentuk akar yang sejenis. Ini adalah prosedur rutin yang langsung, sehingga masuk dalam domain applying.. Bukti: 3√2 + 5√2
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma atau aturan penjumlahan bentuk akar (prosedural) untuk menyelesaikan soal ini.. Bukti: 3√2 + 5√2
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya melibatkan satu langkah operasi penjumlahan koefisien, dan menggunakan representasi yang sangat familiar bagi siswa kelas 8.. Bukti: 3√2 + 5√2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan aljabar dan bentuk akar sejenis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar yang sesuai untuk kelas 8 dalam topik bentuk akar, tidak memerlukan strategi kompleks. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3076`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini merupakan penerapan langsung dari aturan penjumlahan bentuk akar sejenis (distributif). Siswa hanya perlu mengenali bahwa akar-akarnya sama dan menjumlahkan koefisiennya, yang merupakan proses rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau prosedur penjumlahan bentuk akar, yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini sangat mendasar, hanya melibatkan satu langkah operasi rutin tanpa kendala tambahan atau kompleksitas representasi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang penjumlahan suku sejenis dalam aljabar dan sifat distributif pada bentuk akar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal latihan dasar untuk materi bentuk akar di kelas 8, yang menguji pemahaman prosedural paling awal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Bilangan Bentuk Akar
Tipe soal: multiple_choice
Stimulus: -
Soal: Coba buatlah dalam bentuk yang paling sederhana. $3\sqrt{2} + 5\sqrt{2}$
Pilihan: A. $8\sqrt{4}$
B. $3\sqrt{2}$
C. $15\sqrt{2}$
D. $8\sqrt{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `e97f2eaa7ee74e27d6bb517c`

Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

| Opsi | Isi |
|---|---|
| A | 3,4 × 10<sup>11</sup> |
| B | 3,4 × 10<sup>-10</sup> |
| C | 3,4 × 10<sup>10</sup> |
| D | 3,4 × 10<sup>9</sup> |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bilangan 34.000.000.000 ditulis sebagai 3,4 dikali 10 pangkat n. Karena terdapat 10 angka setelah digit pertama (3), maka n = 10. Jadi, 34.000.000.000 = 3,4 x 10^10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9ca1520ccbeb8d43795f274d11d0ada0eec5c5c46bb036bdedbebd4ca1cffaa5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2016 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1982 |
| 3 | success | valid / verified | applying | procedural | Easy | 2018 |

Run 1 — solusi: Bilangan 34.000.000.000 memiliki 10 angka di belakang angka 3. Untuk mengubah ke bentuk baku (a x 10^n, dengan 1 <= a < 10), kita geser koma desimal ke kiri sebanyak 10 kali sehingga menjadi 3,4. Maka, 34.000.000.000 = 3,4 x 10^10.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar penulisan notasi ilmiah (bentuk baku) pada bilangan desimal besar. Ini adalah proses rutin yang langsung.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik penulisan bentuk baku (a x 10^n).. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah konversi yang familiar bagi siswa kelas 8. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan konsep dasar perpangkatan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penulisan bentuk baku adalah materi standar kelas 8 yang bersifat rutin dan langsung. |

Run 2 — solusi: Bilangan 34.000.000.000 dapat ditulis sebagai 3,4 dikalikan dengan 10 pangkat n. Karena terdapat 10 angka setelah digit pertama (3), maka n = 10. Jadi, 34.000.000.000 = 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi bentuk baku (a x 10^n, dengan 1 <= a < 10) secara langsung pada bilangan yang diberikan.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengubah bilangan desimal besar ke dalam notasi ilmiah (bentuk baku).. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu langkah konversi tanpa kendala tambahan atau strategi kompleks.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang nilai tempat dan notasi ilmiah dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena merupakan materi dasar dalam bab bilangan berpangkat/bentuk baku. |

Run 3 — solusi: Bilangan 34.000.000.000 memiliki 10 angka di belakang angka pertama (3). Maka, 34.000.000.000 = 3,4 x 10^10.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar penulisan notasi ilmiah (bentuk baku) pada bilangan desimal besar. Ini adalah proses penerapan algoritma yang sudah dipelajari.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang aturan penulisan bentuk baku (a x 10^n, di mana 1 <= a < 10) dan teknik mengubah bilangan desimal besar ke bentuk tersebut.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung pergeseran koma desimal untuk menentukan eksponen, yang merupakan prosedur standar di kelas 8.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan konsep dasar eksponen/perpangkatan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penulisan bentuk baku adalah materi dasar kelas 8. Soal ini tidak memiliki jebakan kompleks, hanya menguji ketelitian dalam menghitung jumlah nol/pergeseran desimal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3510`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur standar penulisan notasi ilmiah (bentuk baku) pada bilangan desimal besar. Ini adalah proses rutin yang langsung.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik penulisan bentuk baku (a x 10^n).
- Intended difficulty `Easy`: Soal ini bersifat prosedural langsung dengan satu langkah konversi yang familiar bagi siswa kelas 8. Tidak ada kendala kompleks atau strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan konsep dasar perpangkatan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penulisan bentuk baku adalah materi standar kelas 8 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Penulisan Bentuk Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
Pilihan: A. 3,4 × 10<sup>11</sup>
B. 3,4 × 10<sup>-10</sup>
C. 3,4 × 10<sup>10</sup>
D. 3,4 × 10<sup>9</sup>
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `f25d4029ecaafe78249ca72b`

Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10<sup>8</sup>

| Opsi | Isi |
|---|---|
| A | 2.500.000.000 |
| B | 25.000.000 |
| C | 0,000000025 |
| D | 250.000.000 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Bentuk baku 2,5 x 10^8 berarti menggeser koma desimal pada angka 2,5 sebanyak 8 posisi ke kanan. 2,5 x 10^8 = 250.000.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6a5667daa6a6cbb7a659e06201548bdb4bdb25b0203016064151007473e2d238`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1928 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1961 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1939 |

Run 1 — solusi: Bentuk baku 2,5 x 10^8 berarti menggeser koma desimal pada angka 2,5 sebanyak 8 posisi ke kanan. 2,5 x 10^8 = 250.000.000.
- Domain kognitif `classify/knowing`: Soal meminta konversi langsung dari notasi ilmiah ke bentuk desimal standar. Siswa hanya perlu menerapkan definisi pangkat positif pada basis 10, yang merupakan proses rutin.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10^8
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang cara mengubah notasi ilmiah menjadi bilangan biasa dengan menggeser tanda koma sesuai nilai eksponen.. Bukti: 2,5 × 10^8
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan rutin bagi siswa kelas 8. Tidak ada langkah kompleks atau jebakan konseptual yang signifikan.. Bukti: 2,5 × 10^8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang nilai tempat dan operasi perkalian dengan perpangkatan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi bentuk baku adalah materi dasar kelas 8 yang bersifat prosedural langsung. |

Run 2 — solusi: 2,5 x 10^8 = 2,5 x 100.000.000 = 250.000.000. Menggeser koma 8 posisi ke kanan dari 2,5 menghasilkan 250.000.000.
- Domain kognitif `classify/knowing`: Soal meminta konversi langsung dari notasi ilmiah ke bentuk desimal standar, yang merupakan proses rutin dalam materi bentuk baku.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 x 10^8
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami aturan notasi ilmiah (bentuk baku) dan bagaimana pangkat positif pada basis 10 memengaruhi pergeseran koma desimal.. Bukti: 2,5 x 10^8
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah operasi (pergeseran koma) tanpa kendala tambahan atau konteks yang kompleks.. Bukti: 2,5 x 10^8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat dan perkalian dengan kelipatan 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi bentuk baku ke bentuk biasa adalah materi dasar kelas 8 yang bersifat rutin. |

Run 3 — solusi: 2,5 x 10^8 = 2,5 x 100.000.000 = 250.000.000. Menggeser koma 8 posisi ke kanan dari 2,5 menghasilkan 250.000.000.
- Domain kognitif `classify/knowing`: Soal meminta konversi langsung dari notasi ilmiah ke bentuk biasa. Siswa hanya perlu menerapkan definisi pangkat positif pada basis 10, yang merupakan prosedur rutin.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 x 10^8
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami aturan penulisan bentuk baku (notasi ilmiah) dan bagaimana pangkat positif pada 10 memengaruhi pergeseran desimal.. Bukti: 2,5 x 10^8
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah operasi (pergeseran desimal). Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: 2,5 x 10^8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi ilmiah dan nilai tempat desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi bentuk baku adalah materi dasar kelas 8 yang bersifat rutin dan langsung. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Penulisan Bentuk Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10<sup>8</sup>
Pilihan: A. 2.500.000.000
B. 25.000.000
C. 0,000000025
D. 250.000.000
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `ac7f560c796164a475dad657`

Indeks Massa Tubuh $= \dfrac{BB}{TB^2}$. BB: Berat badan (kg), TB: Tinggi badan (m).<br><br>**Tabel 2.12** Kategori Indeks Massa Tubuh<br><br>\|Kategori\|IMT\|<br>\|---\|---\|<br>\|Kekurangan berat badan tingkat berat\|Kurang dari 17,0\|<br>\|Kekurangan berat badan tingkat ringan\|17,0 sampai 18,4\|<br>\|Normal\|18,5 sampai 25,0\|<br>\|Kelebihan berat badan tingkat ringan\|25,1 sampai 27,0\|<br>\|Kelebihan berat badan tingkat berat\|Lebih dari 27,0\|<br><br>**Tabel 2.13** Data Berat dan Tinggi Badan<br><br>\|No\|Nama\|Berat Badan (kg)\|Tinggi Badan (m)\|<br>\|---\|---\|---\|---\|<br>\|1\|Pak Ananta\|80\|1,80\|<br>\|2\|Pak Bintoro\|50\|1,70\|<br>\|3\|Bu Citra\|65\|1,68\|<br>\|4\|Bu Dian\|60\|1,60\|<br>\|5\|Pak Erlangga\|75\|1,65\|<br><br>Pada Tabel 2.13, siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

| Opsi | Isi |
|---|---|
| A | Pak Bintoro, perlu menambah 3,465 kg |
| B | Pak Ananta, perlu menambah 3,465 kg |
| C | Pak Bintoro, perlu menambah 6,9375 kg |
| D | Pak Bintoro, perlu menambah 1,5 kg |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: IMT Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 ≈ 17,30 (Kategori: 17,0-18,4). Target berat untuk IMT 18,5 = 18,5 * 1,70^2 = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `703c2d15a8ea95826df4bafabbbd11ee11173ddb68ff4cb0e31927ae09b80529`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2498 |
| 2 | success | valid / verified | applying | procedural | Medium | 2452 |
| 3 | success | valid / verified | applying | procedural | Medium | 2416 |

Run 1 — solusi: IMT Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 ≈ 17,30 (Kategori: 17,0-18,4). Target berat untuk IMT 18,5 = 18,5 * 1,70^2 = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan untuk menghitung IMT setiap individu, mengklasifikasikannya berdasarkan tabel, lalu melakukan operasi aljabar untuk mencari selisih berat badan agar mencapai target IMT tertentu.. Bukti: Indeks Massa Tubuh = BB / TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural dalam menggunakan rumus matematika (IMT) dan menerapkan prinsip kategori yang diberikan dalam tabel untuk menyelesaikan masalah kontekstual.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: menghitung IMT, membandingkan dengan tabel, dan memanipulasi rumus untuk mencari nilai variabel yang belum diketahui. Beban komputasi moderat.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.13 Data Berat dan Tinggi Badan; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal dan pemahaman rumus aljabar sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan operasi bilangan rasional (desimal) dan pemodelan aljabar sederhana dalam konteks nyata. |

Run 2 — solusi: IMT Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 ≈ 17,30 (Kategori: 17,0-18,4). Target berat untuk IMT 18,5: 18,5 * (1,70^2) = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan untuk menghitung IMT setiap individu, mengklasifikasikannya berdasarkan tabel, lalu melakukan operasi aljabar untuk mencari selisih berat badan. Ini adalah penerapan prosedur rutin dalam konteks nyata.. Bukti: Indeks Massa Tubuh = BB / TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang bagaimana menggunakan rumus (prosedural) dan menginterpretasikan hasil perhitungan berdasarkan kategori yang diberikan (konseptual).. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: menghitung IMT, membandingkan dengan tabel, dan memecahkan persamaan linear sederhana untuk target berat. Beban komputasi moderat karena melibatkan bilangan desimal.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.13 Data Berat dan Tinggi Badan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal dan pemahaman rumus aljabar sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena mengintegrasikan operasi bilangan rasional dengan pemodelan sederhana yang relevan dengan kehidupan sehari-hari. |

Run 3 — solusi: IMT Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 = 17,30 (Kategori: 17,0-18,4). Target BB untuk IMT 18,5 = 18,5 * 1,70^2 = 18,5 * 2,89 = 53,465 kg. Tambahan BB = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan pada data spesifik, mengklasifikasikan hasil ke dalam kategori tabel, dan melakukan operasi aljabar untuk mencari selisih berat badan. Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: Indeks Massa Tubuh = BB / TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan rumus (prosedural) dan menginterpretasikan data berdasarkan kategori yang diberikan (konseptual).. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan aritmatika dengan desimal dan pemahaman rumus, namun langkah-langkahnya bersifat rutin dan terstruktur.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.13 Data Berat dan Tinggi Badan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal dan pemahaman rumus aljabar sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah terbiasa dengan operasi hitung bilangan rasional dan substitusi nilai ke dalam rumus sederhana. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Operasi Hitung Bilangan Rasional
Tipe soal: multiple_choice
Stimulus: -
Soal: Indeks Massa Tubuh $= \dfrac{BB}{TB^2}$. BB: Berat badan (kg), TB: Tinggi badan (m).

**Tabel 2.12** Kategori Indeks Massa Tubuh

|Kategori|IMT|
|---|---|
|Kekurangan berat badan tingkat berat|Kurang dari 17,0|
|Kekurangan berat badan tingkat ringan|17,0 sampai 18,4|
|Normal|18,5 sampai 25,0|
|Kelebihan berat badan tingkat ringan|25,1 sampai 27,0|
|Kelebihan berat badan tingkat berat|Lebih dari 27,0|

**Tabel 2.13** Data Berat dan Tinggi Badan

|No|Nama|Berat Badan (kg)|Tinggi Badan (m)|
|---|---|---|---|
|1|Pak Ananta|80|1,80|
|2|Pak Bintoro|50|1,70|
|3|Bu Citra|65|1,68|
|4|Bu Dian|60|1,60|
|5|Pak Erlangga|75|1,65|

Pada Tabel 2.13, siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
Pilihan: A. Pak Bintoro, perlu menambah 3,465 kg
B. Pak Ananta, perlu menambah 3,465 kg
C. Pak Bintoro, perlu menambah 6,9375 kg
D. Pak Bintoro, perlu menambah 1,5 kg
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `e997c38609f1bdf2dbf30b43`

Gambar berikut memperlihatkan tiang antena TV di atas genting. Tiang antena tersebut ditarik oleh kawat supaya kuat dan tidak goyang saat terkena angin. Biasanya kawat tersebut dipasang pada $\frac{3}{4}$ bagian dari tinggi tiang dari permukaan atas genting. Tiang antena tingginya 8 meter.<br><br>Tentukan panjang kawat jika jarak antara kawat dan tiang pada tanah adalah 8 meter.

| Opsi | Isi |
|---|---|
| A | 6 meter |
| B | 100 meter |
| C | 14 meter |
| D | 10 meter |

![Gambar sumber soal 8](<../../../images/kelas8_crop-p0040-antena-tv.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Tinggi kawat pada tiang = 3/4 * 8 m = 6 m. Jarak kawat ke tiang di tanah = 8 m. Panjang kawat adalah sisi miring segitiga siku-siku dengan kaki 6 m dan 8 m. Menggunakan Teorema Pythagoras: c = akar(6^2 + 8^2) = akar(36 + 64) = akar(100) = 10 m.
Gambar sumber: images/kelas8_crop-p0040-antena-tv.png. Transkripsi visual: Gambar menunjukkan tiang vertikal (berwarna oranye) dan kawat penopang (berwarna hitam) yang membentuk segitiga siku-siku dengan tanah. Tiang antena memiliki tinggi total 8 meter. Kawat dipasang pada titik tertentu di tiang, membentuk sisi tegak segitiga, sementara jarak dari dasar tiang ke titik tambat kawat di tanah membentuk sisi alas segitiga.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4272e5098466b9d359413013c0896e13463c6a8b9f9de75bb40d38548899d0c6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3260 |
| 2 | success | valid / verified | applying | procedural | Medium | 3216 |
| 3 | success | valid / verified | applying | procedural | Medium | 3215 |

Run 1 — solusi: Tinggi kawat pada tiang = 3/4 * 8 m = 6 m. Jarak kawat ke tiang di tanah = 8 m. Panjang kawat adalah sisi miring segitiga siku-siku dengan kaki 6 m dan 8 m. Menggunakan Teorema Pythagoras: c = akar(6^2 + 8^2) = akar(36 + 64) = akar(100) = 10 m.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan teks untuk menentukan panjang kaki segitiga (3/4 dari 8m) dan menerapkan teorema Pythagoras untuk mencari sisi miring. Ini adalah penerapan prosedur rutin dalam konteks masalah.. Bukti: biasanya kawat tersebut dipasang pada 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter; Tentukan panjang kawat
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara bagian-bagian segitiga siku-siku dan menerapkan algoritma Pythagoras (prosedural) untuk menyelesaikan masalah.. Bukti: 3/4 bagian dari tinggi tiang; panjang kawat = akar(6^2 + 8^2)
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah rutin: menghitung tinggi titik tambat (3/4 * 8) dan menerapkan teorema Pythagoras. Beban kognitif rendah karena angka yang digunakan (6, 8, 10) adalah tripel Pythagoras standar.. Bukti: 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar pecahan dan Teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menggabungkan operasi pecahan sederhana dengan penerapan langsung teorema Pythagoras. |

Run 2 — solusi: Tinggi kawat pada tiang = 3/4 * 8 m = 6 m. Jarak kawat ke tiang di tanah = 8 m. Panjang kawat = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang relevan, menghitung tinggi titik ikat kawat, lalu menerapkan teorema Pythagoras untuk mencari sisi miring segitiga. Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: Biasanya kawat tersebut dipasang pada 3/4 bagian dari tinggi tiang; Tentukan panjang kawat jika jarak antara kawat dan tiang pada tanah adalah 8 meter
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang hubungan antara panjang sisi segitiga siku-siku (teorema Pythagoras) dan penggunaan operasi aritmatika dasar untuk menentukan panjang sisi.. Bukti: 3/4 bagian dari tinggi tiang; panjang kawat = akar(6^2 + 8^2)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah rutin yang saling terkait: menghitung tinggi titik ikat kawat terlebih dahulu, baru kemudian menerapkan teorema Pythagoras. Tidak cukup hanya satu langkah langsung.. Bukti: 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pecahan dasar dan teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menggabungkan pemahaman geometri dasar (Pythagoras) dengan konteks nyata yang memerlukan interpretasi teks menjadi model matematika. |

Run 3 — solusi: Tinggi kawat pada tiang = 3/4 * 8 meter = 6 meter. Jarak kawat ke tiang di tanah = 8 meter. Panjang kawat (hipotenusa) = akar(6^2 + 8^2) = akar(36 + 64) = akar(100) = 10 meter.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan teks menjadi model matematika (segitiga siku-siku), menghitung tinggi titik ikat kawat, lalu menerapkan teorema Pythagoras. Ini adalah penerapan prosedur rutin dalam konteks masalah.. Bukti: biasanya kawat tersebut dipasang pada 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter; Tentukan panjang kawat
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman prosedural tentang teorema Pythagoras dan operasi aritmatika dasar untuk menentukan panjang sisi segitiga.. Bukti: 3/4 bagian dari tinggi tiang; panjang kawat = akar(6^2 + 8^2)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah rutin yang saling terkait: menghitung tinggi titik ikat kawat terlebih dahulu, baru kemudian menerapkan teorema Pythagoras. Tidak ada strategi non-rutin yang kompleks.. Bukti: 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pecahan dasar dan teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8, menguji pemahaman konsep Pythagoras dalam situasi nyata sederhana. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menemukan Konsep Pythagoras
Tipe soal: multiple_choice
Stimulus: -
Soal: Gambar berikut memperlihatkan tiang antena TV di atas genting. Tiang antena tersebut ditarik oleh kawat supaya kuat dan tidak goyang saat terkena angin. Biasanya kawat tersebut dipasang pada $\frac{3}{4}$ bagian dari tinggi tiang dari permukaan atas genting. Tiang antena tingginya 8 meter.

Tentukan panjang kawat jika jarak antara kawat dan tiang pada tanah adalah 8 meter.
Pilihan: A. 6 meter
B. 100 meter
C. 14 meter
D. 10 meter
Transkripsi visual: Gambar menunjukkan tiang vertikal (berwarna oranye) dan kawat penopang (berwarna hitam) yang membentuk segitiga siku-siku dengan tanah. Tiang antena memiliki tinggi total 8 meter. Kawat dipasang pada titik tertentu di tiang, membentuk sisi tegak segitiga, sementara jarak dari dasar tiang ke titik tambat kawat di tanah membentuk sisi alas segitiga.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `d518d77ad2f2d4f8b0927b72`

Aldo akan menaiki tangga untuk memperbaiki jam dinding yang ditunjukkan seperti gambar di bawah ini. Jika tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m<br><br>Tentukan panjang tangga yang digunakan Aldo.

| Opsi | Isi |
|---|---|
| A | 3,4 meter |
| B | 3,02 meter |
| C | 9,16 meter |
| D | 3 meter |

![Gambar sumber soal 9](<../../../images/kelas8_crop-p0041-aldo-naik-tangga.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Menggunakan Teorema Pythagoras: c² = a² + b². Diketahui a = 3 m (tinggi) dan b = 0,4 m (alas). Maka c² = 3² + 0,4² = 9 + 0,16 = 9,16. Panjang tangga c = √9,16 ≈ 3,02 meter.
Gambar sumber: images/kelas8_crop-p0041-aldo-naik-tangga.png. Transkripsi visual: Gambar menunjukkan seorang anak menaiki tangga yang bersandar pada tembok vertikal. Terdapat segitiga siku-siku yang terbentuk oleh tembok, tanah, dan tangga. Tinggi tembok (sisi tegak) adalah 3 meter. Jarak dari dasar tangga ke tembok (sisi alas) adalah 0,4 meter. Tangga merupakan sisi miring (hipotenusa) dari segitiga tersebut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a6127f1a743bbe3c28f394d239d17b2ea81cfc633da91ac33abfe73487329471`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3219 |
| 2 | success | valid / verified | applying | procedural | Easy | 3203 |
| 3 | success | valid / verified | applying | procedural | Easy | 3193 |

Run 1 — solusi: Menggunakan Teorema Pythagoras: c² = a² + b². Diketahui a = 3 m (tinggi) dan b = 0,4 m (alas). Maka c² = 3² + 0,4² = 9 + 0,16 = 9,16. Panjang tangga c = √9,16 ≈ 3,02 meter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah Teorema Pythagoras, memilih rumus yang tepat (c² = a² + b²), dan melakukan perhitungan rutin. Ini adalah penerapan konsep pada situasi rutin.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan algoritma atau prosedur Teorema Pythagoras untuk menyelesaikan masalah geometri yang diberikan.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan konteks yang familiar (tangga bersandar). Siswa hanya perlu menerapkan rumus Pythagoras secara langsung tanpa langkah tambahan yang kompleks atau strategi non-rutin.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras dan operasi akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari Teorema Pythagoras yang merupakan materi standar kelas 8. Tidak ada jebakan atau kompleksitas tambahan. |

Run 2 — solusi: Panjang tangga adalah sisi miring (c) dari segitiga siku-siku dengan sisi tegak a=3 m dan sisi alas b=0,4 m. Menggunakan Teorema Pythagoras: c = akar(a^2 + b^2) = akar(3^2 + 0,4^2) = akar(9 + 0,16) = akar(9,16) = 3,0265... m. Dibulatkan menjadi 3,02 m.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan Teorema Pythagoras pada situasi kontekstual yang rutin. Siswa perlu mengidentifikasi sisi-sisi segitiga siku-siku dan memilih prosedur yang tepat untuk menghitung sisi miring.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus Pythagoras untuk menyelesaikan masalah geometri sederhana.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; akar(3^2 + 0,4^2)
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena merupakan aplikasi langsung dari rumus Pythagoras pada situasi yang sangat familiar (tangga bersandar). Tidak ada langkah non-rutin atau kendala kompleks.. Bukti: tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m; Tentukan panjang tangga yang digunakan Aldo.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras dan operasi akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 sebagai latihan penerapan langsung teorema Pythagoras. |

Run 3 — solusi: Panjang tangga adalah hipotenusa segitiga siku-siku dengan sisi tegak 3 m dan sisi alas 0,4 m. Menggunakan Teorema Pythagoras: c = akar(3^2 + 0,4^2) = akar(9 + 0,16) = akar(9,16) ≈ 3,02 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah Teorema Pythagoras, memilih rumus yang tepat (c^2 = a^2 + b^2), dan melakukan perhitungan rutin. Ini adalah penerapan konsep pada situasi rutin.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara sisi-sisi segitiga siku-siku (konsep Pythagoras) dan menerapkan prosedur perhitungan akar kuadrat.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; 0.4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi sisi-sisi segitiga dan menerapkan rumus Pythagoras secara langsung tanpa modifikasi strategi atau kendala yang kompleks.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras dan operasi akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi standar Teorema Pythagoras yang sesuai dengan kurikulum kelas 8. Tidak ada langkah non-rutin atau integrasi konsep yang sulit. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menemukan Konsep Pythagoras
Tipe soal: multiple_choice
Stimulus: -
Soal: Aldo akan menaiki tangga untuk memperbaiki jam dinding yang ditunjukkan seperti gambar di bawah ini. Jika tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m

Tentukan panjang tangga yang digunakan Aldo.
Pilihan: A. 3,4 meter
B. 3,02 meter
C. 9,16 meter
D. 3 meter
Transkripsi visual: Gambar menunjukkan seorang anak menaiki tangga yang bersandar pada tembok vertikal. Terdapat segitiga siku-siku yang terbentuk oleh tembok, tanah, dan tangga. Tinggi tembok (sisi tegak) adalah 3 meter. Jarak dari dasar tangga ke tembok (sisi alas) adalah 0,4 meter. Tangga merupakan sisi miring (hipotenusa) dari segitiga tersebut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `a75a3be4a28f98e263e644a4`

Seekor kucing berada di atas genting dan terlihat kebingungan karena tidak bisa turun. Aysha yang melihat kucing tersebut langsung mencari galah dan kemudian diikat dengan keranjang kecil pada ujung galah tersebut. Saat menolong kucing tersebut, Cintia melihat Aysha dan mencoba membantunya untuk mengarahkan galah yang telah diikat keranjang tepat pada titik lokasi kucing pada jarak 4 meter. Jika jarak pandangan Cintia terhadap kucing diperkirakan 5 meter.<br><br>Tentukan jarak atap yang ditempati kucing terhadap tanah tempat Aysha berdiri.

| Opsi | Isi |
|---|---|
| A | 9 meter |
| B | 5 meter |
| C | 1 meter |
| D | 3 meter |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misalkan jarak atap ke tanah adalah t, jarak horizontal 4 m, dan jarak miring 5 m. Berdasarkan Teorema Pythagoras: t² + 4² = 5². Maka t² = 25 - 16 = 9. Jadi, t = √9 = 3 meter.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d1f67c232621ce7427017e5976b973029f3a2473cbf24dfdc6dd584a7aef3b84`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2041 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2081 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2042 |

Run 1 — solusi: Misalkan jarak atap ke tanah adalah t, jarak horizontal 4 m, dan jarak miring 5 m. Berdasarkan Teorema Pythagoras: t² + 4² = 5². Maka t² = 25 - 16 = 9. Jadi, t = √9 = 3 meter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai segitiga siku-siku, menentukan sisi yang diketahui (alas dan hipotenusa), dan menerapkan Teorema Pythagoras untuk mencari tinggi.. Bukti: jarak atap yang ditempati kucing terhadap tanah; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip Teorema Pythagoras (konsep) untuk menyelesaikan masalah geometri yang diaplikasikan dalam konteks nyata.. Bukti: jarak atap yang ditempati kucing terhadap tanah; jarak 4 meter; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung Teorema Pythagoras dengan angka tripel dasar (3, 4, 5). Prosedurnya rutin dan familiar bagi siswa kelas 8.. Bukti: jarak 4 meter; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras dan operasi akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menggunakan tripel Pythagoras standar (3-4-5) yang sangat umum diajarkan di kelas 8, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Misalkan jarak atap ke tanah adalah t, jarak Aysha ke titik di bawah kucing adalah 4 m, dan jarak pandang (hipotenusa) adalah 5 m. Berdasarkan Teorema Pythagoras: t² + 4² = 5². Maka t² = 25 - 16 = 9. Jadi, t = √9 = 3 meter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai segitiga siku-siku, menentukan sisi mana yang merupakan hipotenusa (jarak pandang 5m) dan sisi tegak (jarak 4m), lalu menerapkan rumus Pythagoras untuk mencari sisi lainnya.. Bukti: jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak atap yang ditempati kucing terhadap tanah; jarak Aysha ke titik di bawah kucing adalah 4 meter
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan sisi-sisi pada segitiga siku-siku (Teorema Pythagoras) dan prosedur untuk menghitung panjang sisi yang tidak diketahui.. Bukti: jarak atap yang ditempati kucing terhadap tanah; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung Teorema Pythagoras pada konteks sehari-hari yang sederhana. Siswa hanya perlu mengidentifikasi komponen segitiga dan melakukan satu operasi Pythagoras.. Bukti: jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak atap yang ditempati kucing terhadap tanah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras (a² + b² = c²). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini standar untuk kelas 8, menggunakan angka tripel Pythagoras (3, 4, 5) yang sangat umum dan familiar bagi siswa. |

Run 3 — solusi: Misalkan jarak atap ke tanah adalah t, jarak horizontal 4 m, dan jarak pandang (hipotenusa) 5 m. Berdasarkan Teorema Pythagoras: t² + 4² = 5². t² + 16 = 25. t² = 9. t = √9 = 3 meter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah segitiga siku-siku, menentukan sisi mana yang merupakan hipotenusa, dan menerapkan Teorema Pythagoras untuk mencari panjang sisi tegak.. Bukti: jarak atap yang ditempati kucing terhadap tanah; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip Teorema Pythagoras (konsep) untuk menyelesaikan masalah kontekstual.. Bukti: jarak atap yang ditempati kucing terhadap tanah; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung Teorema Pythagoras dalam konteks sederhana. Siswa hanya perlu mengidentifikasi sisi-sisi segitiga dan melakukan perhitungan rutin.. Bukti: jarak atap yang ditempati kucing terhadap tanah; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras (a² + b² = c²). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 8 karena menguji pemahaman dasar Teorema Pythagoras dengan konteks yang mudah dipahami. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Tripel Pythagoras
Tipe soal: multiple_choice
Stimulus: -
Soal: Seekor kucing berada di atas genting dan terlihat kebingungan karena tidak bisa turun. Aysha yang melihat kucing tersebut langsung mencari galah dan kemudian diikat dengan keranjang kecil pada ujung galah tersebut. Saat menolong kucing tersebut, Cintia melihat Aysha dan mencoba membantunya untuk mengarahkan galah yang telah diikat keranjang tepat pada titik lokasi kucing pada jarak 4 meter. Jika jarak pandangan Cintia terhadap kucing diperkirakan 5 meter.

Tentukan jarak atap yang ditempati kucing terhadap tanah tempat Aysha berdiri.
Pilihan: A. 9 meter
B. 5 meter
C. 1 meter
D. 3 meter
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `7f0ea8ebdbf606480849cd78`

Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.

| Opsi | Isi |
|---|---|
| A | 9, 12, 16 |
| B | 7, 13, 11 |
| C | 6, 2,5, 6,5 |
| D | 24, 17, 25 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Sebuah kelompok bilangan (a, b, c) adalah tripel Pythagoras jika memenuhi a^2 + b^2 = c^2. Untuk opsi C: 2,5^2 + 6^2 = 6,25 + 36 = 42,25. Nilai 6,5^2 = 42,25. Karena 42,25 = 42,25, maka (2,5, 6, 6,5) adalah tripel Pythagoras.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['membuktikan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2bd296a529451ff625b3597c2e409740dcf6eccbf0f6ca117701ace4fa727c82`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2081 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2076 |
| 3 | success | valid / verified | applying | procedural | Easy | 2105 |

Run 1 — solusi: Tripel Pythagoras memenuhi a^2 + b^2 = c^2. Untuk opsi C: 2,5^2 + 6^2 = 6,25 + 36 = 42,25. Nilai 6,5^2 = 42,25. Karena 42,25 = 42,25, maka (2,5, 6, 6,5) adalah tripel Pythagoras.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi tripel Pythagoras (a^2 + b^2 = c^2) untuk menguji setiap opsi yang diberikan. Ini adalah proses penerapan konsep pada situasi rutin.. Bukti: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap prinsip atau hubungan matematis dalam teorema Pythagoras (konsep tripel).. Bukti: tripel Pythagoras
- Intended difficulty `classify/Medium`: Siswa harus melakukan perhitungan kuadrat dan penjumlahan untuk empat opsi yang berbeda. Meskipun prosedurnya rutin, siswa perlu melakukan verifikasi berulang (beberapa langkah rutin terkait) untuk menentukan jawaban yang benar.. Bukti: 9, 12, 16; 7, 13, 11; 6, 2,5, 6,5; 24, 17, 25

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman teorema Pythagoras dan operasi bilangan desimal. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menguji tripel Pythagoras. Beban perhitungan desimal pada opsi C meningkatkan sedikit kompleksitas dibandingkan angka bulat biasa. |

Run 2 — solusi: Sebuah kelompok bilangan (a, b, c) adalah tripel Pythagoras jika memenuhi a^2 + b^2 = c^2. Untuk opsi C: 2,5^2 + 6^2 = 6,25 + 36 = 42,25. Sedangkan 6,5^2 = 42,25. Karena 42,25 = 42,25, maka (2,5, 6, 6,5) adalah tripel Pythagoras.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi tripel Pythagoras (a^2 + b^2 = c^2) untuk menguji setiap opsi yang diberikan. Ini adalah proses penerapan konsep pada situasi rutin.. Bukti: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap prinsip atau hubungan matematis dalam Teorema Pythagoras (tripel Pythagoras).. Bukti: tripel Pythagoras
- Intended difficulty `classify/Easy`: Siswa hanya perlu melakukan perhitungan kuadrat sederhana untuk setiap opsi. Prosedurnya familiar dan rutin bagi siswa kelas 8.. Bukti: 9, 12, 16; 7, 13, 11; 6, 2,5, 6,5; 24, 17, 25

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman Teorema Pythagoras dan operasi hitung bilangan desimal. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin untuk memverifikasi tripel Pythagoras, sesuai dengan standar kompetensi kelas 8. |

Run 3 — solusi: Sebuah kelompok bilangan (a, b, c) dengan c sebagai bilangan terbesar adalah tripel Pythagoras jika memenuhi a² + b² = c². Untuk opsi C: 2,5² + 6² = 6,25 + 36 = 42,25. Sedangkan 6,5² = 42,25. Karena 42,25 = 42,25, maka (2,5, 6, 6,5) adalah tripel Pythagoras.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi tripel Pythagoras (a² + b² = c²) untuk menguji setiap opsi yang diberikan. Ini adalah proses penerapan prosedur standar pada situasi rutin.. Bukti: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan matematis dalam teorema Pythagoras (konsep) dan penggunaan algoritma perhitungan kuadrat untuk verifikasi (prosedural).. Bukti: tripel Pythagoras
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan perhitungan kuadrat dan penjumlahan untuk empat set angka yang berbeda. Ini adalah tugas rutin yang melibatkan beberapa langkah perhitungan, namun prosedurnya sangat familiar bagi siswa kelas 8.. Bukti: 9, 12, 16; 7, 13, 11; 6, 2,5, 6,5; 24, 17, 25

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman teorema Pythagoras (a² + b² = c²) dan operasi hitung bilangan desimal. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi kuadrat dan penjumlahan untuk memverifikasi tripel Pythagoras sebagai bagian dari materi standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3684`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan definisi tripel Pythagoras (a^2 + b^2 = c^2) untuk menguji setiap opsi. Ini adalah penerapan prosedur standar pada situasi rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang hubungan matematis dalam teorema Pythagoras (konsep) dan penggunaan algoritma perhitungan kuadrat untuk verifikasi (prosedural).
- Intended difficulty `Easy`: Siswa perlu melakukan perhitungan kuadrat dan penjumlahan untuk empat set angka. Meskipun melibatkan desimal, prosedurnya sangat rutin dan familiar bagi siswa kelas 8.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman teorema Pythagoras (a^2 + b^2 = c^2) dan operasi hitung bilangan desimal. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin untuk memverifikasi tripel Pythagoras, sesuai dengan standar kompetensi kelas 8. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Tripel Pythagoras
Tipe soal: multiple_choice
Stimulus: -
Soal: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.
Pilihan: A. 9, 12, 16
B. 7, 13, 11
C. 6, 2,5, 6,5
D. 24, 17, 25
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `0317e843f4ed4b4fe3c37612`

Perhatikan gambar segitiga siku-siku ABC di samping. C 30° A 8 cm D B<br><br>Tentukan Keliling segitiga ABC.

| Opsi | Isi |
|---|---|
| A | $(32+16\sqrt{3})$ cm |
| B | 64 cm |
| C | $48\sqrt{3}$ cm |
| D | $(48+16\sqrt{3})$ cm |

![Gambar sumber soal 12](<../../../images/kelas8_crop-p0042-segitiga2.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pada segitiga ADC (siku-siku di D, sudut A=60°), AD=8 cm, maka AC=16 cm dan CD=8√3 cm. Pada segitiga ABC (siku-siku di C, sudut B=30°), berlaku rasio sisi 1:√3:2. Sisi BC = AC * √3 = 16√3 cm. Sisi AB = AC * 2 = 32 cm. Keliling = AC + BC + AB = 16 + 16√3 + 32 = (48 + 16√3) cm.
Gambar sumber: images/kelas8_crop-p0042-segitiga2.png. Transkripsi visual: Segitiga ABC dengan sudut siku-siku di C. Garis tinggi CD ditarik dari C ke sisi AB, membentuk sudut siku-siku di D. Diketahui panjang AD = 8 cm dan sudut B = 30 derajat. Segitiga ADC adalah segitiga siku-siku di D dengan sudut A = 60 derajat (karena sudut B = 30 derajat dan sudut C = 90 derajat).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3d04e837145a0cabf4a9a769ce65527b61ae16668c2dc1cac4ebdd2112d60e7d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3326 |
| 2 | success | valid / verified | applying | procedural | Medium | 3348 |
| 3 | success | valid / verified | applying | procedural | Medium | 3380 |

Run 1 — solusi: Pada segitiga ADC (siku-siku di D, sudut A=60°), AD=8 cm, maka AC=16 cm dan CD=8√3 cm. Pada segitiga ABC (siku-siku di C, sudut B=30°), berlaku rasio sisi 1:√3:2. Sisi BC = AC * √3 = 16√3 cm. Sisi AB = AC * 2 = 32 cm. Keliling = AC + BC + AB = 16 + 16√3 + 32 = (48 + 16√3) cm.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan konsep segitiga istimewa (30-60-90) pada dua segitiga yang saling terkait (ADC dan ABC) untuk menentukan panjang sisi-sisi yang belum diketahui sebelum menghitung keliling.. Bukti: menggunakan rasio 30-60-90 pada segitiga ABC; sudut A=60° pada segitiga siku-siku ADC
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang penggunaan rasio panjang sisi pada segitiga istimewa dan konsep keliling segitiga.. Bukti: rasio 30-60-90; Keliling segitiga ABC
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang hubungan antar segitiga dalam satu gambar dan penerapan rasio segitiga istimewa secara bertahap.. Bukti: segitiga siku-siku ABC; garis tinggi CD; sudut B = 30 derajat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep segitiga siku-siku, rasio sisi segitiga istimewa (30-60-90), dan keliling segitiga. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengidentifikasi segitiga istimewa dan menerapkan rasionya, namun soal ini memerlukan dua tahap analisis segitiga yang saling terkait. |

Run 2 — solusi: Pada segitiga ADC (siku-siku di D), sudut A = 60 derajat (karena sudut B=30 dan C=90). Dengan rasio 30-60-90, AD=8 cm, maka AC=16 cm dan CD=8√3 cm. Pada segitiga BDC (siku-siku di D), sudut B=30 derajat, maka BC = CD / sin(30) = 8√3 / 0.5 = 16√3 cm. BD = CD * tan(60) = 8√3 * √3 = 24 cm. AB = AD + BD = 8 + 24 = 32 cm. Keliling = AC + BC + AB = 16 + 16√3 + 32 = 48 + 16√3 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan konsep segitiga istimewa (30-60-90) pada dua segitiga siku-siku yang berbeda (ADC dan BDC) untuk menemukan panjang sisi-sisi segitiga ABC sebelum menghitung kelilingnya.. Bukti: Tentukan Keliling segitiga ABC; segitiga siku-siku ABC; sudut B = 30 derajat; AD = 8 cm
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur algoritma segitiga istimewa dan rumus keliling segitiga.. Bukti: rasio 30-60-90; Keliling segitiga
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang hubungan antar sisi pada segitiga istimewa dan kemampuan memecah masalah menjadi beberapa langkah rutin (mencari sisi AC, CD, BD, lalu AB).. Bukti: segitiga siku-siku ABC; sudut B = 30 derajat; AD = 8 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rasio sisi segitiga istimewa 30-60-90 dan sifat segitiga siku-siku. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan rasio segitiga istimewa. Soal ini menuntut lebih dari satu langkah kalkulasi namun prosedurnya standar. |

Run 3 — solusi: Pada segitiga ADC (siku-siku di D), sudut A = 60 derajat, AD = 8 cm. Maka AC = AD / cos(60) = 8 / 0.5 = 16 cm. Pada segitiga ABC (siku-siku di C), sudut B = 30 derajat, maka sudut A = 60 derajat. AC adalah sisi di depan sudut 30 derajat (16 cm). Maka AB = 2 * AC = 32 cm dan BC = AC * akar(3) = 16 * akar(3) cm. Keliling = AC + BC + AB = 16 + 16*akar(3) + 32 = (48 + 16*akar(3)) cm.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan konsep segitiga istimewa (30-60-90) pada dua segitiga yang berbeda (ADC dan ABC) untuk menemukan panjang sisi-sisi segitiga ABC sebelum menghitung keliling.. Bukti: Tentukan Keliling segitiga ABC.; sudut B = 30 derajat. Panjang AD = 8 cm.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan prosedur algoritma segitiga istimewa (rasio sisi-sisi pada segitiga 30-60-90) untuk menyelesaikan masalah geometri.. Bukti: rasio 30-60-90 pada segitiga ABC
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang hubungan antar segitiga dalam satu bangun (segitiga di dalam segitiga) dan penerapan rasio segitiga istimewa secara bertahap. Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: segitiga siku-siku ABC; garis tinggi CD; sudut B = 30 derajat; AD = 8 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep segitiga siku-siku, perbandingan sisi pada segitiga istimewa (30-60-90), dan keliling segitiga. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari segitiga istimewa. Soal ini menuntut kemampuan mengorganisir langkah-langkah perhitungan untuk dua segitiga yang berbeda namun terhubung. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Segitiga Istimewa
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar segitiga siku-siku ABC di samping. C 30° A 8 cm D B

Tentukan Keliling segitiga ABC.
Pilihan: A. $(32+16\sqrt{3})$ cm
B. 64 cm
C. $48\sqrt{3}$ cm
D. $(48+16\sqrt{3})$ cm
Transkripsi visual: Segitiga ABC dengan sudut siku-siku di C. Garis tinggi CD ditarik dari C ke sisi AB, membentuk sudut siku-siku di D. Diketahui panjang AD = 8 cm dan sudut B = 30 derajat. Segitiga ADC adalah segitiga siku-siku di D dengan sudut A = 60 derajat (karena sudut B = 30 derajat dan sudut C = 90 derajat).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `2ec551abe1f96d3c16146fb7`

Berikut ditunjukkan gambar rencana bangun rumah yang sedang dikerjakan oleh Amri sebagai seorang arsitek yang terlihat tampak depan. Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.<br><br>Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.

| Opsi | Isi |
|---|---|
| A | 6 meter |
| B | 8,4 meter |
| C | 3,2 meter |
| D | 5,075 meter |

![Gambar sumber soal 13](<../../../images/kelas8_crop-p0042-rencana-rumah.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Menggunakan Teorema Pythagoras: t² + 3,2² = 6². t² = 36 - 10,24 = 25,76. t = √25,76 ≈ 5,075 m.
Gambar sumber: images/kelas8_crop-p0042-rencana-rumah.png. Transkripsi visual: Gambar menunjukkan tampak depan sebuah rumah. Atap rumah berbentuk segitiga sama kaki dengan panjang sisi miring masing-masing 6 m. Lebar rumah (alas segitiga) adalah 6,4 m. Tinggi total bangunan (dinding) adalah 8,4 m, namun ini tidak relevan untuk menghitung tinggi atap.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `743ed58c2cf41ef1395cb3ba446d25313c5edf0af9dcd55cd0c73c68eeb5b912`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3227 |
| 2 | success | valid / verified | applying | procedural | Medium | 3218 |
| 3 | success | valid / verified | applying | procedural | Medium | 4595 |

Run 1 — solusi: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Menggunakan Teorema Pythagoras: t² + 3,2² = 6². t² = 36 - 10,24 = 25,76. t = √25,76 ≈ 5,075 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa tinggi atap membentuk segitiga siku-siku dengan setengah lebar rumah sebagai alas dan sisi miring atap sebagai hipotenusa, kemudian menerapkan Teorema Pythagoras.. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Dimensi pengetahuan `classify/procedural`: Soal ini memerlukan pemahaman prosedural tentang penggunaan Teorema Pythagoras untuk menyelesaikan masalah geometri dalam konteks nyata.. Bukti: Tentukan tinggi atap rumah di atas; akar(6² - 3,2²) = akar(36-10,24) = akar(25,76) = 5,075 m
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah rutin: membagi lebar rumah menjadi dua, mengidentifikasi segitiga siku-siku yang relevan, dan menerapkan Teorema Pythagoras.. Bukti: lebar rumah adalah 6.4 meter; sisi miring atap (6 m); akar(6² - 3,2²)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan pemahaman geometri segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8, menguji pemahaman geometri dasar dan aplikasi Pythagoras pada situasi nyata. |

Run 2 — solusi: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Menggunakan Teorema Pythagoras: t² + 3,2² = 6². t² = 36 - 10,24 = 25,76. t = √25,76 ≈ 5,075 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa atap membentuk segitiga sama kaki, membagi alas menjadi dua untuk membentuk segitiga siku-siku, dan menerapkan Teorema Pythagoras untuk mencari tinggi.. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip Teorema Pythagoras (konsep) dan menerapkannya dalam konteks masalah geometri (prosedural).. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman geometri dasar (segitiga sama kaki) dan penerapan Pythagoras. Langkah-langkahnya rutin dan jelas bagi siswa kelas 8.. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menggabungkan pemahaman visual geometri dengan perhitungan Pythagoras yang merupakan materi inti. |

Run 3 — solusi: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Dengan Pythagoras: t² + 3,2² = 6² => t² = 36 - 10,24 = 25,76 => t = √25,76 ≈ 5,075 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi model segitiga sama kaki dari gambar, membagi alas menjadi dua, dan menerapkan teorema Pythagoras untuk mencari tinggi.. Bukti: Tentukan tinggi atap rumah; lebar rumah adalah 6.4 meter; sisi miring atap masing-masing 6 m
- Dimensi pengetahuan `classify/procedural`: Melibatkan penerapan algoritma teorema Pythagoras pada konteks geometri.. Bukti: Tentukan tinggi atap rumah; sisi miring atap masing-masing 6 m
- Intended difficulty `classify/Medium`: Memerlukan pemodelan geometri dari gambar dan penerapan Pythagoras. Tidak langsung karena siswa harus membagi lebar rumah menjadi dua terlebih dahulu.. Bukti: lebar rumah adalah 6.4 meter; sisi miring atap masing-masing 6 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menggabungkan pemahaman geometri dasar dengan penerapan Pythagoras. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Segitiga Istimewa
Tipe soal: multiple_choice
Stimulus: -
Soal: Berikut ditunjukkan gambar rencana bangun rumah yang sedang dikerjakan oleh Amri sebagai seorang arsitek yang terlihat tampak depan. Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.

Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.
Pilihan: A. 6 meter
B. 8,4 meter
C. 3,2 meter
D. 5,075 meter
Transkripsi visual: Gambar menunjukkan tampak depan sebuah rumah. Atap rumah berbentuk segitiga sama kaki dengan panjang sisi miring masing-masing 6 m. Lebar rumah (alas segitiga) adalah 6,4 m. Tinggi total bangunan (dinding) adalah 8,4 m, namun ini tidak relevan untuk menghitung tinggi atap.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `06779006c739d5de08849cb7`

Aldo dan Arjuna berdiri saling membelakangi untuk main tembak-tembakan pistol bambu. Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan. Pada saat yang sama, Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan. Pada titik terakhir, mereka berdua saling menembak.<br><br>Berapa langkah jarak kalian berdua saat mereka saling menembak?

| Opsi | Isi |
|---|---|
| A | 27 langkah |
| B | 45 langkah |
| C | 36 langkah |
| D | 63 langkah |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Aldo dan Arjuna bergerak saling membelakangi. Total jarak depan-belakang = 20 + 16 = 36 langkah. Total jarak kanan-kiri = 15 + 12 = 27 langkah. Jarak keduanya adalah hipotenusa dari segitiga siku-siku dengan kaki 36 dan 27. Jarak = sqrt(36^2 + 27^2) = sqrt(1296 + 729) = sqrt(2025) = 45 langkah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `52d8069a1851fb58d5acc85ade3876f4c12a20c130e6f34c1cc190f01b795c50`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2139 |
| 2 | success | valid / verified | applying | procedural | Medium | 2102 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2110 |

Run 1 — solusi: Aldo dan Arjuna bergerak saling membelakangi. Total jarak depan-belakang = 20 + 16 = 36 langkah. Total jarak kanan-kiri = 15 + 12 = 27 langkah. Jarak keduanya adalah hipotenusa dari segitiga siku-siku dengan kaki 36 dan 27. Jarak = sqrt(36^2 + 27^2) = sqrt(1296 + 729) = sqrt(2025) = 45 langkah.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi posisi dua orang yang bergerak ke arah berlawanan, menentukan total perpindahan pada dua sumbu tegak lurus, dan menerapkan teorema Pythagoras untuk mencari jarak.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan. Pada saat yang sama, Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.; Berapa langkah jarak kalian berdua saat mereka saling menembak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan teorema Pythagoras dalam konteks masalah nyata (pemodelan jarak).. Bukti: Penerapan Teorema Pythagoras
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman bahwa pergerakan saling membelakangi berarti menjumlahkan komponen jarak pada sumbu yang sama sebelum menerapkan Pythagoras. Ini adalah langkah rutin yang terkait.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.; jarak = akar(36²+27²) = akar(2025) = 45 langkah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan pergerakan dalam bidang koordinat dan menerapkan Pythagoras. Soal ini menuntut ketelitian dalam menjumlahkan komponen vektor jarak sebelum menghitung hipotenusa. |

Run 2 — solusi: Aldo dan Arjuna membelakangi, sehingga jarak total depan-belakang adalah 20+16=36 langkah dan jarak total kanan-kiri adalah 15+12=27 langkah. Jarak keduanya adalah hipotenusa dari segitiga siku-siku dengan kaki 36 dan 27. Jarak = sqrt(36^2 + 27^2) = sqrt(1296 + 729) = sqrt(2025) = 45 langkah.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi posisi dua orang yang membelakangi untuk menentukan komponen jarak horizontal dan vertikal, kemudian menerapkan teorema Pythagoras untuk mencari jarak diagonal.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan; Berapa langkah jarak kalian berdua saat mereka saling menembak?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur teorema Pythagoras untuk menyelesaikan masalah kontekstual.. Bukti: jarak = akar(36²+27²) = akar(2025) = 45 langkah
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep posisi relatif (membelakangi) dan penerapan teorema Pythagoras. Ini adalah prosedur standar yang melibatkan beberapa langkah rutin.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan; jarak = akar(36²+27²) = akar(2025) = 45 langkah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan operasi penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menggabungkan pemodelan situasi sederhana dengan teorema Pythagoras. |

Run 3 — solusi: Aldo's position relative to start: (20, 15). Arjuna's position relative to start (opposite direction): (-16, -12). Total displacement in forward/backward axis: 20 - (-16) = 36. Total displacement in right/left axis: 15 - (-12) = 27. Distance = sqrt(36^2 + 27^2) = sqrt(1296 + 729) = sqrt(2025) = 45 steps.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi posisi dua orang dalam sistem koordinat kartesius dan menerapkan Teorema Pythagoras untuk menghitung jarak antar titik.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan; Berapa langkah jarak kalian berdua saat mereka saling menembak?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara pergerakan dalam dua dimensi (x, y) dan bagaimana Teorema Pythagoras digunakan untuk mencari jarak diagonal (hipotenusa).. Bukti: Penerapan Teorema Pythagoras; jarak kalian berdua saat mereka saling menembak
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang sistem koordinat dan penerapan Pythagoras. Siswa harus menjumlahkan komponen vektor posisi (36 dan 27) sebelum menghitung hipotenusa.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, konsep koordinat kartesius sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini menuntut siswa untuk memodelkan situasi nyata ke dalam koordinat, yang merupakan standar kompetensi kelas 8. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3914`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengintegrasikan informasi posisi dua orang yang bergerak ke arah berlawanan, menentukan total perpindahan pada dua sumbu tegak lurus, dan menerapkan teorema Pythagoras untuk mencari jarak.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan teorema Pythagoras dalam konteks masalah nyata (pemodelan jarak).
- Intended difficulty `Medium`: Soal memerlukan pemahaman bahwa pergerakan saling membelakangi berarti menjumlahkan komponen jarak pada sumbu yang sama sebelum menerapkan Pythagoras. Ini adalah langkah rutin yang terkait.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan pergerakan dalam bidang koordinat dan menerapkan Pythagoras. Soal ini menuntut ketelitian dalam menjumlahkan komponen vektor jarak sebelum menghitung hipotenusa. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Penerapan Teorema Pythagoras
Tipe soal: multiple_choice
Stimulus: -
Soal: Aldo dan Arjuna berdiri saling membelakangi untuk main tembak-tembakan pistol bambu. Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan. Pada saat yang sama, Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan. Pada titik terakhir, mereka berdua saling menembak.

Berapa langkah jarak kalian berdua saat mereka saling menembak?
Pilihan: A. 27 langkah
B. 45 langkah
C. 36 langkah
D. 63 langkah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `595852bacf2288f5b8407683`

Seorang atlet tenis mengajukan pertanyaan kepada wasit. Suara atlet mampu didengar wasit hanya pada jarak maksimum 30 kaki. Berdasarkan posisi wasit dan atlet tenis pada gambar berikut. 24 kaki 12 kaki 5 kaki<br><br>Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet? Jelaskan jawaban kalian.

| Opsi | Isi |
|---|---|
| A | Ya, karena jarak keduanya 25 kaki (kurang dari 30 kaki) |
| B | Tidak, karena jarak keduanya 36 kaki |
| C | Tidak, karena jarak keduanya 31 kaki (lebih dari 30 kaki) |
| D | Ya, karena jarak keduanya 24 kaki |

![Gambar sumber soal 15](<../../../images/kelas8_crop-p0043-atlet-tenis.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi 12 - 5 = 7 kaki. Menggunakan Teorema Pythagoras: d = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 kaki < 30 kaki, maka wasit dapat mendengar suara atlet.
Gambar sumber: images/kelas8_crop-p0043-atlet-tenis.png. Transkripsi visual: Gambar menunjukkan seorang wasit duduk di kursi setinggi 12 kaki dan seorang atlet tenis berdiri dengan tinggi 5 kaki. Jarak horizontal antara wasit dan atlet adalah 24 kaki. Situasi ini membentuk segitiga siku-siku dengan alas 24 kaki dan tinggi tegak lurus (12 - 5) = 7 kaki.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a3eb6d0e390411a1aff5d9c29581ad81f9d55411cd220636f6084c4e500eba66`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3295 |
| 2 | success | valid / verified | applying | procedural | Medium | 3260 |
| 3 | success | valid / verified | applying | procedural | Medium | 3302 |

Run 1 — solusi: Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi 12 - 5 = 7 kaki. Menggunakan Teorema Pythagoras: d = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 kaki < 30 kaki, maka wasit dapat mendengar suara atlet.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini dapat dimodelkan sebagai segitiga siku-siku, menentukan panjang kaki-kakinya (24 dan 7), dan menerapkan Teorema Pythagoras untuk membandingkan hasilnya dengan batas jarak 30 kaki.. Bukti: Seorang atlet tenis mengajukan pertanyaan kepada wasit. Suara atlet mampu didengar wasit hanya pada jarak maksimum 30 kaki.; Berdasarkan posisi wasit dan atlet tenis pada gambar berikut.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip Teorema Pythagoras (konsep) untuk menyelesaikan masalah kontekstual yang memerlukan prosedur perhitungan rutin.. Bukti: Berdasarkan posisi wasit dan atlet tenis pada gambar berikut.; 24 kaki 12 kaki 5 kaki
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya sekadar memasukkan angka ke rumus, tetapi harus melakukan langkah tambahan untuk menentukan tinggi segitiga (12-5=7) sebelum menerapkan Teorema Pythagoras.. Bukti: 24 kaki 12 kaki 5 kaki; selisih tinggi = 12-5=7 kaki; jarak = akar(24^2+7^2) = akar(625) = 25 kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, operasi aritmatika dasar, pemahaman konsep jarak. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan situasi nyata ke dalam bentuk geometri dan menerapkan Pythagoras, termasuk melakukan pengurangan sederhana untuk mendapatkan panjang sisi segitiga. |

Run 2 — solusi: Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi 12-5=7 kaki. Menggunakan Teorema Pythagoras: d = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 kaki < 30 kaki, wasit dapat mendengar suara atlet.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini dapat dimodelkan sebagai segitiga siku-siku, menentukan panjang kaki-kakinya (24 dan 7), dan menerapkan Teorema Pythagoras untuk mencari hipotenusa.. Bukti: Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet?; Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi 12-5=7 kaki.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma Teorema Pythagoras untuk menyelesaikan masalah kontekstual.. Bukti: selisih tinggi = 12-5=7 kaki; jarak = akar(24²+7²)
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemodelan situasi nyata ke dalam bentuk geometri (segitiga siku-siku) dan melakukan perhitungan rutin. Ini adalah langkah standar untuk kelas 8.. Bukti: selisih tinggi = 12-5=7 kaki; jarak = akar(24²+7²)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, operasi aritmatika dasar, pemahaman konsep jarak. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan Teorema Pythagoras pada masalah kontekstual yang memerlukan sedikit interpretasi visual (menentukan selisih tinggi). |

Run 3 — solusi: Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi (12 - 5) = 7 kaki. Menggunakan Teorema Pythagoras: d = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 kaki < 30 kaki, wasit dapat mendengar suara atlet.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini dapat dimodelkan sebagai segitiga siku-siku, menentukan panjang kaki-kakinya (termasuk melakukan pengurangan tinggi), dan menerapkan Teorema Pythagoras untuk membandingkan hasilnya dengan batas jarak.. Bukti: Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet?; Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi (12 - 5) = 7 kaki.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma Teorema Pythagoras untuk menyelesaikan masalah kontekstual.. Bukti: Menggunakan Teorema Pythagoras: d = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya menerapkan rumus Pythagoras secara langsung, tetapi harus melakukan langkah tambahan untuk menentukan tinggi segitiga (selisih tinggi) dari informasi visual sebelum menghitung.. Bukti: selisih tinggi = 12-5=7 kaki; jarak = akar(24^2+7^2) = akar(625) = 25 kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, operasi aritmatika dasar, interpretasi gambar geometri. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8, menguji pemahaman konsep Pythagoras dalam konteks nyata yang memerlukan sedikit penalaran spasial. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Penerapan Teorema Pythagoras
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang atlet tenis mengajukan pertanyaan kepada wasit. Suara atlet mampu didengar wasit hanya pada jarak maksimum 30 kaki. Berdasarkan posisi wasit dan atlet tenis pada gambar berikut. 24 kaki 12 kaki 5 kaki

Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet? Jelaskan jawaban kalian.
Pilihan: A. Ya, karena jarak keduanya 25 kaki (kurang dari 30 kaki)
B. Tidak, karena jarak keduanya 36 kaki
C. Tidak, karena jarak keduanya 31 kaki (lebih dari 30 kaki)
D. Ya, karena jarak keduanya 24 kaki
Transkripsi visual: Gambar menunjukkan seorang wasit duduk di kursi setinggi 12 kaki dan seorang atlet tenis berdiri dengan tinggi 5 kaki. Jarak horizontal antara wasit dan atlet adalah 24 kaki. Situasi ini membentuk segitiga siku-siku dengan alas 24 kaki dan tinggi tegak lurus (12 - 5) = 7 kaki.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `e8e1147bfed27b5d98b29d8f`

Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.<br><br>Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, segitiga ABC siku-siku di C |
| B | Ya, segitiga ABC siku-siku di B |
| C | Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras |
| D | Tidak, karena AB² + BC² tidak sama dengan CA² |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `84e227b058758d77e245a5463bfd0fa94296993b5a55778e2c430ee6f6b69beb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2253 |
| 2 | success | valid / verified | applying | procedural | Medium | 2298 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2271 |

Run 1 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak untuk menghitung panjang sisi-sisi segitiga dan menggunakan kebalikan Teorema Pythagoras untuk menentukan jenis segitiga. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku?; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma (rumus jarak) dan prinsip (kebalikan Teorema Pythagoras) untuk menyelesaikan masalah.. Bukti: AB²=(4-(-1))²+(-2-3)²=50; karena AB²+BC²=50+18=68=CA², maka siku-siku di B
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan rutin menggunakan rumus jarak sebanyak tiga kali dan verifikasi menggunakan Teorema Pythagoras. Prosedur ini standar untuk kelas 8.. Bukti: A(-1, 3), B(4, -2), dan C(1, -5); AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68

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
| gradeRelativeRationale | Materi ini sesuai dengan kurikulum kelas 8 terkait koordinat dan Pythagoras. Perhitungan melibatkan bilangan negatif namun prosedurnya bersifat rutin. |

Run 2 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak untuk menghitung panjang sisi-sisi segitiga, lalu menggunakan prinsip kebalikan Teorema Pythagoras untuk menentukan jenis segitiga. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku?; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma (rumus jarak) dan prinsip konseptual (kebalikan Teorema Pythagoras) untuk memverifikasi properti segitiga.. Bukti: AB²=(4-(-1))²+(-2-3)²=50; karena AB²+BC²=50+18=68=CA², maka siku-siku di B
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan jarak untuk tiga sisi dan pengecekan hubungan Pythagoras. Ini melibatkan beberapa langkah rutin yang saling terkait namun prosedurnya sangat jelas dan familiar bagi siswa kelas 8.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik pada koordinat Kartesius dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini berada pada cakupan pengayaan kelas 8. Tingkat kesulitan Medium tepat karena siswa harus melakukan tiga perhitungan jarak yang berbeda dan melakukan verifikasi hubungan kuadrat sisi, yang merupakan langkah rutin namun membutuhkan ketelitian. |

Run 3 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak (atau kuadrat jarak) untuk menentukan panjang sisi-sisi segitiga, kemudian menggunakan kebalikan Teorema Pythagoras untuk memverifikasi sifat siku-siku. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku?; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara koordinat titik, panjang sisi, dan sifat segitiga siku-siku melalui Teorema Pythagoras.. Bukti: AB²=(4-(-1))²+(-2-3)²=50; karena AB²+BC²=50+18=68=CA², maka siku-siku di B
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (menghitung tiga jarak, membandingkan kuadratnya) yang saling terkait. Prosedurnya standar untuk kelas 8.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menghitung jarak antar titik dan menerapkan Teorema Pythagoras. Soal ini menguji ketelitian dalam operasi bilangan negatif dan penerapan teorema. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4450`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan rumus jarak untuk menghitung panjang sisi-sisi segitiga dan menggunakan kebalikan Teorema Pythagoras untuk menentukan jenis segitiga. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritma (rumus jarak) dan prinsip (kebalikan Teorema Pythagoras) untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal memerlukan perhitungan rutin menggunakan rumus jarak sebanyak tiga kali dan verifikasi menggunakan Teorema Pythagoras. Prosedur ini standar untuk kelas 8.

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
| gradeRelativeRationale | Materi ini sesuai dengan kurikulum kelas 8 terkait koordinat dan Pythagoras. Perhitungan melibatkan bilangan negatif namun prosedurnya bersifat rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Rumus Jarak (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.

Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.
Pilihan: A. Ya, segitiga ABC siku-siku di C
B. Ya, segitiga ABC siku-siku di B
C. Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras
D. Tidak, karena AB² + BC² tidak sama dengan CA²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `35a513e4d376af0fba4e3993`

Perhatikan gambar berikut. ABC merupakan segitiga siku-siku dengan koordinat A(x1,y1), B(x2,y2), dan C(x2,y1). AC = x2-x1 dan BC = y2-y1. Karena segitiga ABC siku-siku, berlaku Teorema Pythagoras: $AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$.<br><br>Diketahui titik $A(-2,-1)$ dan $B(3,11)$. Bagaimana panjang $AB$?

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 169 |
| C | 17 |
| D | 10,05 |

![Gambar sumber soal 17](<../../../images/kelas8_crop-p0044-segitiga1.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menggunakan rumus jarak AB = sqrt((x2-x1)^2 + (y2-y1)^2). Substitusi A(-2,-1) dan B(3,11): AB = sqrt((3 - (-2))^2 + (11 - (-1))^2) = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13.
Gambar sumber: images/kelas8_crop-p0044-segitiga1.png. Transkripsi visual: Gambar menunjukkan segitiga siku-siku ABC pada bidang Kartesius. Titik A berada di (x1, y1), titik C di (x2, y1), dan titik B di (x2, y2). Sisi AC memiliki panjang x2-x1 dan sisi BC memiliki panjang y2-y1. Sudut siku-siku terletak di titik C.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e60eca8310098ff7e7ba60adfa059a17a7e567f94f5a5f8cff2f036200e398fa`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3305 |
| 2 | success | valid / verified | applying | procedural | Easy | 3255 |
| 3 | success | valid / verified | applying | procedural | Easy | 3301 |

Run 1 — solusi: Menggunakan rumus jarak AB = sqrt((x2-x1)^2 + (y2-y1)^2). Substitusi A(-2,-1) dan B(3,11): AB = sqrt((3 - (-2))^2 + (11 - (-1))^2) = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus yang sudah diberikan secara eksplisit dalam stem soal. Ini adalah penerapan langsung dari prosedur yang sudah disediakan.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara teorema Pythagoras dan rumus jarak pada bidang koordinat, serta bagaimana mengoperasikan koordinat negatif.. Bukti: berlaku Teorema Pythagoras: AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena rumus diberikan langsung. Siswa hanya perlu melakukan substitusi dan operasi aritmatika dasar. Meskipun ada koordinat negatif, ini adalah prosedur standar kelas 8.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi bilangan bulat (termasuk pengurangan bilangan negatif) dan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah terbiasa dengan operasi bilangan bulat dan penggunaan rumus sederhana. Soal ini memberikan rumus secara eksplisit, sehingga mengurangi beban kognitif. |

Run 2 — solusi: Menggunakan rumus jarak AB = akar((x2-x1)^2 + (y2-y1)^2). Substitusi titik A(-2,-1) dan B(3,11): AB = akar((3 - (-2))^2 + (11 - (-1))^2) = akar(5^2 + 12^2) = akar(25 + 144) = akar(169) = 13.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus yang sudah diberikan secara eksplisit dalam stem soal. Ini adalah penerapan prosedur langsung pada situasi rutin.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menggunakan algoritma atau rumus jarak yang diberikan untuk menyelesaikan masalah.. Bukti: AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena rumus diberikan langsung di dalam soal. Siswa hanya perlu melakukan substitusi nilai dan operasi aritmatika dasar.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi bilangan bulat (pengurangan bilangan negatif) dan operasi akar kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun dilabeli pengayaan, soal ini hanya menuntut substitusi langsung ke rumus yang diberikan, sehingga tingkat kesulitannya rendah untuk kelas 8. |

Run 3 — solusi: Menggunakan rumus jarak AB = akar((x2-x1)^2 + (y2-y1)^2). Substitusi A(-2,-1) dan B(3,11): AB = akar((3 - (-2))^2 + (11 - (-1))^2) = akar(5^2 + 12^2) = akar(25 + 144) = akar(169) = 13.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus yang sudah diberikan dalam soal (substitusi nilai ke dalam rumus jarak) untuk menghitung panjang segmen garis. Ini adalah penerapan prosedur rutin.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penggunaan algoritma atau teknik perhitungan (rumus jarak) untuk menyelesaikan masalah koordinat.. Bukti: AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena rumus sudah disediakan di dalam teks soal. Siswa hanya perlu melakukan substitusi nilai dan operasi aritmatika dasar (pengurangan bilangan negatif, penguadratan, penjumlahan, dan akar kuadrat).. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi bilangan bulat (termasuk pengurangan bilangan negatif), konsep dasar akar kuadrat, dan substitusi variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun subtopik berlabel pengayaan, soal ini menyediakan rumus secara eksplisit, sehingga menurunkan tuntutan kognitif menjadi prosedur substitusi langsung yang sesuai untuk kelas 8. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Rumus Jarak (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut. ABC merupakan segitiga siku-siku dengan koordinat A(x1,y1), B(x2,y2), dan C(x2,y1). AC = x2-x1 dan BC = y2-y1. Karena segitiga ABC siku-siku, berlaku Teorema Pythagoras: $AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$.

Diketahui titik $A(-2,-1)$ dan $B(3,11)$. Bagaimana panjang $AB$?
Pilihan: A. 13
B. 169
C. 17
D. 10,05
Transkripsi visual: Gambar menunjukkan segitiga siku-siku ABC pada bidang Kartesius. Titik A berada di (x1, y1), titik C di (x2, y1), dan titik B di (x2, y2). Sisi AC memiliki panjang x2-x1 dan sisi BC memiliki panjang y2-y1. Sudut siku-siku terletak di titik C.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br>Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = CE, karena ∠CAE = ∠AEC |
| B | AE = CE, karena ∠ACE = ∠CAE |
| C | AC = AE, karena ∠ACE = ∠AEC |
| D | AB = AC, karena AD garis bagi |

![Gambar sumber soal 18](<../../../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: AD \|\| CE, maka ∠BAD = ∠AEC (sehadap) dan ∠DAC = ∠ACE (berseberangan dalam). Karena AD adalah garis bagi, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Karena sudut-sudut alas sama, maka ΔACE sama kaki dengan AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cd8100901ebe5f1e08ef886c0343ee68fc4fffc19c50c1744ce70ec5f97b9383`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 3164 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 3206 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 3180 |

Run 1 — solusi: AD \|\| CE, maka ∠BAD = ∠AEC (sehadap) dan ∠DAC = ∠ACE (berseberangan dalam). Karena AD adalah garis bagi, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Karena sudut-sudut alas sama, maka ΔACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan konstruksi mental atau fisik berdasarkan petunjuk, lalu menggunakan sifat sudut pada garis sejajar (sehadap dan berseberangan) untuk membuktikan kesamaan sudut, yang mengarah pada sifat segitiga sama kaki.. Bukti: Beri alasan bahwa ΔACE sama kaki; Gambarkan garis yang sejajar dengan AD dan melalui titik C
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan sudut-sudut pada garis sejajar dan sifat segitiga sama kaki, bukan sekadar menghafal rumus.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Hard`: Soal ini memerlukan kemampuan untuk mengintegrasikan konstruksi tambahan dengan teorema geometri dasar (garis sejajar dan segitiga). Ini bukan prosedur rutin bagi kebanyakan siswa kelas 8.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan) dan definisi segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materinya geometri dasar, pembuktian dengan konstruksi tambahan (garis bantu) merupakan tantangan kognitif yang signifikan bagi siswa kelas 8. |

Run 2 — solusi: AD \|\| CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD adalah garis bagi, maka sudut BAD = sudut DAC. Akibatnya, sudut AEC = sudut ACE. Dalam segitiga ACE, karena sudut alasnya sama, maka sisi di depan sudut tersebut sama panjang, yaitu AC = AE.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk melakukan pembuktian geometri sederhana menggunakan sifat sudut pada garis sejajar (sehadap dan berseberangan dalam) untuk menyimpulkan sifat segitiga sama kaki. Ini memerlukan integrasi konsep.. Bukti: Beri alasan bahwa ΔACE sama kaki.; Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan sudut-sudut pada garis sejajar dan sifat segitiga sama kaki, bukan sekadar menghafal rumus.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Intended difficulty `classify/Hard`: Soal ini memerlukan konstruksi tambahan (garis bantu) dan penalaran deduktif untuk menghubungkan sifat sudut pada garis sejajar dengan sifat segitiga sama kaki. Ini melampaui prosedur rutin.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut sehadap dan berseberangan dalam pada garis sejajar, sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materinya ada di kelas 8, melakukan pembuktian dengan konstruksi garis bantu adalah tantangan kognitif yang lebih tinggi daripada sekadar menghitung panjang sisi. |

Run 3 — solusi: AD \|\| CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD adalah garis bagi, maka sudut BAD = sudut DAC. Akibatnya, sudut AEC = sudut ACE. Karena dua sudut alas sama, maka segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Siswa perlu melakukan konstruksi geometris tambahan dan menggunakan sifat sudut pada garis sejajar (sehadap dan berseberangan) untuk membuktikan sifat segitiga sama kaki. Ini melibatkan integrasi konsep, bukan sekadar prosedur rutin.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa segitiga ACE sama kaki
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan sudut-sudut pada garis sejajar dan sifat segitiga sama kaki dalam konteks pembuktian teorema garis bagi.. Bukti: AD membagi sudut A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Hard`: Soal ini memerlukan konstruksi tambahan dan penalaran deduktif untuk menghubungkan sifat garis sejajar dengan sifat segitiga. Ini bukan prosedur rutin bagi siswa kelas 8.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa segitiga ACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan), sifat segitiga sama kaki, definisi garis bagi. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materinya ada di kelas 8, pembuktian geometris dengan konstruksi tambahan (garis bantu) merupakan tantangan kognitif yang signifikan bagi siswa pada jenjang ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Hard": 3} | unanimous_3_0 / unanimous | Hard |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Kesebangunan pada Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.

Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.
Pilihan: A. AC = CE, karena ∠CAE = ∠AEC
B. AE = CE, karena ∠ACE = ∠CAE
C. AC = AE, karena ∠ACE = ∠AEC
D. AB = AC, karena AD garis bagi
Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Hard", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `51def5fab754abff1aeeed28`

Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.<br><br>Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.

| Opsi | Isi |
|---|---|
| A | 108.000 + y = 220.000 (y = uang Dhoni) |
| B | 108.000 - y = 220.000 (y = uang Dhoni) |
| C | 108.000 x y = 220.000 (y = uang Dhoni) |
| D | 220.000 + y = 108.000 (y = uang Dhoni) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Misalkan y adalah uang Dhoni. Total uang Ahmad dan Dhoni adalah 220.000. Maka, uang Ahmad + uang Dhoni = 220.000. Substitusi uang Ahmad: 108.000 + y = 220.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0e685453337a49f505d5ac6a5c6c44fd7cb3e32bacd603311246b09b613ebcf4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2038 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2023 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2111 |

Run 1 — solusi: Misalkan y adalah uang Dhoni. Total uang Ahmad dan Dhoni adalah 220.000. Maka, uang Ahmad + uang Dhoni = 220.000. Substitusi uang Ahmad: 108.000 + y = 220.000.
- Domain kognitif `classify/applying`: Soal meminta siswa menerjemahkan situasi verbal ke dalam bentuk persamaan linier satu variabel sederhana. Ini adalah proses menerapkan konsep dasar PLSV pada situasi rutin.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara komponen (uang Ahmad, uang Dhoni) dan totalnya untuk membentuk persamaan, yang merupakan pemahaman konseptual.. Bukti: 108.000 + y = 220.000
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya meminta pembentukan model matematika dari kalimat sederhana tanpa perlu penyelesaian perhitungan yang rumit.. Bukti: Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi penjumlahan dan konsep variabel sebagai pengganti nilai yang belum diketahui. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 sebagai pengenalan atau latihan dasar pemodelan aljabar (PLSV). |

Run 2 — solusi: Misalkan y adalah uang Dhoni. Diketahui uang Ahmad = 108.000 dan total uang = 220.000. Maka, uang Ahmad + uang Dhoni = total uang, yaitu 108.000 + y = 220.000.
- Domain kognitif `classify/applying`: Soal meminta siswa menerjemahkan situasi kontekstual ke dalam bentuk persamaan linier satu variabel sederhana, yang merupakan proses applying konsep dasar.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antar variabel dan konstanta dalam konteks persamaan linier (konsep) untuk memilih model matematika yang tepat.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang penjumlahan untuk membentuk persamaan linier satu variabel.. Bukti: Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi penjumlahan dan konsep variabel sebagai representasi nilai yang belum diketahui. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan tingkat kelas 8 untuk materi awal PLSV, di mana siswa diharapkan mampu memodelkan situasi sehari-hari ke dalam bentuk persamaan. |

Run 3 — solusi: Misalkan y adalah uang Dhoni. Total uang Ahmad dan Dhoni adalah 220.000. Maka, uang Ahmad (108.000) ditambah uang Dhoni (y) sama dengan total uang (220.000). Persamaannya adalah 108.000 + y = 220.000.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan situasi kontekstual ke dalam bentuk model matematika (persamaan linier satu variabel). Ini adalah proses menerapkan konsep dasar aljabar pada situasi yang diberikan.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara komponen-komponen dalam soal (uang Ahmad, uang Dhoni, total uang) dan bagaimana hubungan tersebut direpresentasikan dalam bentuk persamaan linier.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya meminta pemodelan dasar dari situasi yang diberikan tanpa langkah perhitungan kompleks atau manipulasi aljabar yang rumit.. Bukti: Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan dan konsep variabel sebagai pengganti nilai yang belum diketahui. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 sebagai pengenalan atau latihan dasar pemodelan PLSV. Tidak memerlukan strategi non-rutin. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Memahami Konsep Persamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.

Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
Pilihan: A. 108.000 + y = 220.000 (y = uang Dhoni)
B. 108.000 - y = 220.000 (y = uang Dhoni)
C. 108.000 x y = 220.000 (y = uang Dhoni)
D. 220.000 + y = 108.000 (y = uang Dhoni)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `d490723c72a0d7e848c344b2`

Perhatikan beberapa kalimat berikut:<br>1. Bilangan prima terkecil adalah 3.<br>2. Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil.<br>3. Empat merupakan bilangan ganjil.<br>4. Jayapura merupakan ibu kota provinsi Papua.<br>5. Pegunungan Lantimojong berada di Sulawesi Utara.<br>Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?

| Opsi | Isi |
|---|---|
| A | Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil. |
| B | Bilangan prima terkecil adalah 3. |
| C | Empat merupakan bilangan ganjil. |
| D | Jayapura merupakan ibu kota provinsi Papua. |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Evaluasi kebenaran setiap pernyataan: (1) Salah, prima terkecil adalah 2. (2) Salah, 2a+6 selalu genap untuk a bilangan asli. (3) Salah, 4 adalah genap. (4) Benar, Jayapura adalah ibu kota Papua. (5) Salah, Pegunungan Latimojong berada di Sulawesi Selatan. Maka pernyataan yang benar adalah (4).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b09f9468c0a801e2e84b2a25ceaeb35eca45694a53a49ff4fce3e6ed0abbbd2f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2047 |
| 2 | success | valid / verified | knowing | factual | Easy | 2092 |
| 3 | success | valid / verified | knowing | factual | Easy | 2074 |

Run 1 — solusi: Evaluasi kebenaran setiap pernyataan: (1) Salah, prima terkecil adalah 2. (2) Salah, 2a+6 selalu genap untuk a bilangan asli. (3) Salah, 4 adalah genap. (4) Benar, Jayapura adalah ibu kota Papua. (5) Salah, Pegunungan Latimojong berada di Sulawesi Selatan. Maka pernyataan yang benar adalah (4).
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengevaluasi nilai kebenaran dari beberapa pernyataan faktual dan matematis. Proses ini melibatkan pengenalan fakta dasar dan konsep dasar bilangan, yang termasuk dalam domain knowing.. Bukti: Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?
- Dimensi pengetahuan `classify/factual`: Soal menguji pengetahuan tentang fakta-fakta spesifik (geografi, definisi bilangan prima, sifat bilangan genap/ganjil).. Bukti: Bilangan prima terkecil adalah 3.; Jayapura merupakan ibu kota provinsi Papua.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu memeriksa kebenaran setiap poin satu per satu tanpa memerlukan strategi kompleks atau langkah prosedural yang panjang.. Bukti: Perhatikan beberapa kalimat berikut; manakah yang termasuk pernyataan yang benar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang bilangan prima, sifat bilangan genap/ganjil, dan pengetahuan umum geografi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan rendah karena hanya memerlukan verifikasi kebenaran pernyataan dasar yang sudah dipelajari di tingkat sekolah dasar atau awal SMP. |

Run 2 — solusi: Evaluasi kebenaran setiap pernyataan: 1) Salah, prima terkecil adalah 2. 2) Salah, 2a+6 selalu genap untuk a bilangan asli. 3) Salah, 4 adalah bilangan genap. 4) Benar, Jayapura adalah ibu kota Papua. 5) Salah, Pegunungan Latimojong berada di Sulawesi Selatan. Maka pernyataan yang benar adalah 4.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengevaluasi nilai kebenaran dari beberapa pernyataan faktual dan matematis. Proses ini melibatkan pemanggilan pengetahuan dasar (knowing) tentang definisi bilangan prima, paritas bilangan, dan geografi.. Bukti: Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami definisi dan fakta dasar terkait bilangan (prima, genap/ganjil) serta pengetahuan umum untuk menentukan nilai kebenaran pernyataan.. Bukti: Bilangan prima terkecil adalah 3.; Empat merupakan bilangan ganjil.; Jayapura merupakan ibu kota provinsi Papua.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu memeriksa kebenaran setiap poin satu per satu tanpa memerlukan strategi kompleks atau langkah prosedural yang panjang.. Bukti: Perhatikan beberapa kalimat berikut:; Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan prima, bilangan genap/ganjil, dan pengetahuan umum geografi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pernyataan (kalimat terbuka/tertutup) adalah dasar logika matematika di kelas 8. Soal ini sangat standar dan tidak memerlukan manipulasi aljabar yang rumit. |

Run 3 — solusi: Analisis kebenaran kalimat: 1. Salah (prima terkecil adalah 2). 2. Salah (2a+6 selalu genap untuk a asli). 3. Salah (4 adalah genap). 4. Benar (Jayapura adalah ibu kota Papua). 5. Salah (Lantimojong di Sulawesi Selatan). Maka pernyataan yang benar adalah 4.
- Domain kognitif `classify/knowing`: Siswa perlu mengevaluasi nilai kebenaran dari setiap pernyataan yang diberikan (fakta geografis dan sifat bilangan). Ini adalah proses kognitif knowing karena hanya memerlukan pengenalan fakta dasar dan sifat bilangan tanpa manipulasi aljabar kompleks.. Bukti: Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman siswa terhadap definisi pernyataan (kalimat yang memiliki nilai kebenaran) dan pengetahuan faktual terkait bilangan prima serta geografi.. Bukti: Bilangan prima terkecil adalah 3.; Jayapura merupakan ibu kota provinsi Papua.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya meminta siswa memverifikasi kebenaran dari pernyataan-pernyataan sederhana yang bersifat faktual atau aritmatika dasar.. Bukti: Perhatikan beberapa kalimat berikut:; manakah yang termasuk pernyataan yang benar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang bilangan prima, sifat bilangan genap/ganjil, dan pengetahuan umum geografi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi logika dasar/pernyataan sering muncul di awal bab aljabar kelas 8 sebagai pengantar konsep variabel. Tingkat kesulitan rendah karena tidak melibatkan pemecahan persamaan. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Memahami Konsep Persamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan beberapa kalimat berikut:
1. Bilangan prima terkecil adalah 3.
2. Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil.
3. Empat merupakan bilangan ganjil.
4. Jayapura merupakan ibu kota provinsi Papua.
5. Pegunungan Lantimojong berada di Sulawesi Utara.
Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?
Pilihan: A. Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil.
B. Bilangan prima terkecil adalah 3.
C. Empat merupakan bilangan ganjil.
D. Jayapura merupakan ibu kota provinsi Papua.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `d8ebb6f2c60e468be6bc868a`

x + 13 = 1<br><br>Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.

| Opsi | Isi |
|---|---|
| A | x = 12 |
| B | x = -12 |
| C | x = 14 |
| D | x = -14 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: x + 13 = 1; x = 1 - 13; x = -12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `427eec6402e411462a6333deced3b2faceb330c8c85207a29550be193b73cf81`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1848 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1859 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1858 |

Run 1 — solusi: x + 13 = 1; x = 1 - 13; x = -12.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi aljabar dasar (pengurangan kedua ruas) untuk mengisolasi variabel. Ini adalah proses rutin yang langsung.. Bukti: x + 13 = 1
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma dasar penyelesaian persamaan linier satu variabel (prosedur) untuk menemukan nilai x.. Bukti: x + 13 = 1
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah operasi aritmatika (pengurangan) untuk menyelesaikan persamaan linier satu variabel.. Bukti: x + 13 = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi PLSV adalah dasar kelas 8. Soal ini adalah bentuk paling sederhana (satu langkah) tanpa kompleksitas tambahan. |

Run 2 — solusi: x + 13 = 1; x = 1 - 13; x = -12.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi aljabar dasar (pengurangan kedua ruas) untuk mengisolasi variabel. Ini adalah prosedur standar dalam menyelesaikan persamaan linier satu variabel.. Bukti: x + 13 = 1
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma atau teknik dasar untuk menyelesaikan persamaan linier satu variabel.. Bukti: x + 13 = 1
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah operasi (pengurangan) untuk mendapatkan nilai x. Beban kognitif sangat rendah.. Bukti: x + 13 = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi bilangan bulat (penjumlahan/pengurangan) dan konsep dasar persamaan linier. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 seharusnya sudah menguasai penyelesaian persamaan linier satu variabel sederhana ini sebagai prasyarat materi yang lebih kompleks. |

Run 3 — solusi: x + 13 = 1. Kurangi kedua ruas dengan 13: x = 1 - 13. Maka, x = -12.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan satu langkah operasi aljabar dasar (pengurangan) untuk mengisolasi variabel x. Ini adalah proses rutin yang langsung.. Bukti: x + 13 = 1
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menyelesaikan persamaan linear satu variabel dengan operasi invers.. Bukti: x + 13 = 1
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah operasi aritmatika sederhana untuk menyelesaikan persamaan linear satu variabel.. Bukti: x + 13 = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Persamaan linear satu variabel adalah materi dasar kelas 7 yang tetap relevan di kelas 8. Tingkat kesulitan ini sangat rendah karena hanya satu langkah operasi. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menyelesaikan Persamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: x + 13 = 1

Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.
Pilihan: A. x = 12
B. x = -12
C. x = 14
D. x = -14
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `6c4807ddb62ebe4c925c56fd`

3 x + 5 = -10<br><br>Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.

| Opsi | Isi |
|---|---|
| A | x = -5 |
| B | x = 5 |
| C | x = -5/3 |
| D | x = -15 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 3x + 5 = -10; 3x = -10 - 5; 3x = -15; x = -15 / 3; x = -5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `117a580f4aab83cd83040024bbf64d9d9be204df57fab6dd429b95723a938f9d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1880 |
| 2 | success | valid / verified | applying | procedural | Easy | 1883 |
| 3 | success | valid / verified | applying | procedural | Easy | 1851 |

Run 1 — solusi: 3x + 5 = -10; 3x = -10 - 5; 3x = -15; x = -15 / 3; x = -5.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur aljabar dasar untuk menyelesaikan persamaan linier satu variabel. Siswa hanya perlu melakukan operasi invers (pengurangan dan pembagian) secara langsung.. Bukti: 3 x + 5 = -10
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma atau urutan langkah sistematis (prosedural) dalam memindahkan konstanta dan mengisolasi variabel untuk menyelesaikan persamaan linier.. Bukti: 3 x + 5 = -10
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang sangat familiar bagi siswa kelas 8. Hanya melibatkan satu variabel dan operasi aritmatika dasar tanpa kendala kompleks.. Bukti: 3 x + 5 = -10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan bulat dan konsep dasar persamaan linier satu variabel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar PLSV yang sesuai dengan kurikulum kelas 8, di mana siswa diharapkan lancar melakukan manipulasi aljabar sederhana. |

Run 2 — solusi: 3x + 5 = -10; 3x = -10 - 5; 3x = -15; x = -15 / 3; x = -5.
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan operasi aljabar dasar untuk menyelesaikan persamaan linier satu variabel. Siswa hanya perlu menerapkan prosedur rutin (memindahkan konstanta dan membagi dengan koefisien) untuk mendapatkan nilai x.. Bukti: 3 x + 5 = -10
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau urutan langkah penyelesaian persamaan linier satu variabel (prosedural).. Bukti: 3 x + 5 = -10
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu variabel dan operasi dasar. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 3 x + 5 = -10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan bulat dan konsep dasar persamaan linier satu variabel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi PLSV adalah materi dasar kelas 8. Soal ini merupakan bentuk paling standar dan langsung dari penyelesaian PLSV. |

Run 3 — solusi: 3x + 5 = -10; 3x = -10 - 5; 3x = -15; x = -15 / 3; x = -5.
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan prosedur aljabar standar untuk menyelesaikan persamaan linier satu variabel. Ini adalah penerapan prosedur rutin.. Bukti: 3 x + 5 = -10
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penyelesaian persamaan linier (memindahkan konstanta, membagi dengan koefisien).. Bukti: 3 x + 5 = -10
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar satu variabel dengan operasi bilangan bulat sederhana. Tidak ada jebakan atau strategi non-rutin.. Bukti: 3 x + 5 = -10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar bilangan bulat dan konsep dasar persamaan linier satu variabel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 sebagai latihan dasar pemahaman persamaan linier satu variabel. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menyelesaikan Persamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: 3 x + 5 = -10

Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.
Pilihan: A. x = -5
B. x = 5
C. x = -5/3
D. x = -15
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `69f14f018149ed7308b7751c`

Sekolah menyelenggarakan proyek penguatan proil pelajar Pancasila pada tema kearifan lokal untuk melakukan observasi menggunakan lima bus yang dapat mengangkut hanya 290 penumpang.<br><br>Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

| Opsi | Isi |
|---|---|
| A | 5x ≥ 290 (x = banyak penumpang per bus) |
| B | x ≤ 290 (x = banyak penumpang per bus) |
| C | 5x ≤ 290 (x = banyak penumpang per bus) |
| D | 5x < 290 (x = banyak penumpang per bus) |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Misalkan x adalah banyak penumpang per bus. Karena terdapat 5 bus, maka total penumpang adalah 5x. Frasa 'dapat mengangkut hanya 290 penumpang' berarti kapasitas maksimal adalah 290, sehingga total penumpang tidak boleh melebihi 290. Pertidaksamaan yang tepat adalah 5x ≤ 290.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `da15f307b7450ed0d48ee4ad64a6b183d24ab12a08bdad1817fc57dbd8811cfc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2041 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2019 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2058 |

Run 1 — solusi: Misalkan x adalah banyak penumpang per bus. Karena terdapat 5 bus, maka total penumpang adalah 5x. Frasa 'dapat mengangkut hanya 290 penumpang' berarti kapasitas maksimal adalah 290, sehingga total penumpang tidak boleh melebihi 290. Pertidaksamaan yang tepat adalah 5x ≤ 290.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan situasi kontekstual ke dalam model matematika (pertidaksamaan). Ini melibatkan pemahaman konsep hubungan 'maksimal' dengan simbol pertidaksamaan, yang merupakan proses applying.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap prinsip pertidaksamaan linier satu variabel dan bagaimana menerjemahkan batasan kontekstual ke dalam struktur simbolik yang benar.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8 yang mempelajari PtLSV. Siswa hanya perlu mengidentifikasi variabel, koefisien, dan tanda pertidaksamaan yang sesuai dengan konteks 'maksimal'.. Bukti: menggunakan lima bus yang dapat mengangkut hanya 290 penumpang; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan simbol pertidaksamaan (≤, ≥, <, >). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan standar dalam pemodelan matematika sederhana untuk materi PtLSV di kelas 8. |

Run 2 — solusi: Misalkan x adalah banyak penumpang per bus. Karena terdapat 5 bus dan kapasitas total maksimal adalah 290 penumpang, maka total penumpang adalah 5x. Kata 'hanya' mengindikasikan batas atas (maksimal), sehingga 5x ≤ 290.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan situasi kontekstual ke dalam model matematika (pertidaksamaan). Ini melibatkan pemahaman konsep hubungan antara variabel dan batasan (kapasitas), yang termasuk dalam kategori applying.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap prinsip pertidaksamaan linier satu variabel sebagai model matematika untuk situasi dunia nyata.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu mengidentifikasi variabel, koefisien (jumlah bus), dan tanda pertidaksamaan yang tepat berdasarkan kata kunci 'hanya' (maksimal).. Bukti: lima bus yang dapat mengangkut hanya 290 penumpang; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan simbol pertidaksamaan (≤, ≥, <, >). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena memodelkan situasi nyata ke bentuk aljabar adalah kompetensi dasar pada materi PtLSV. |

Run 3 — solusi: Misalkan x adalah banyak penumpang per bus. Karena terdapat 5 bus, maka total penumpang adalah 5x. Kapasitas maksimal adalah 290 penumpang, yang berarti total penumpang tidak boleh melebihi 290. Maka, 5x ≤ 290.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan situasi kontekstual ke dalam model matematika berupa pertidaksamaan linier satu variabel. Ini memerlukan pemahaman konsep tentang hubungan antara variabel dan batasan (kapasitas maksimal).. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep pertidaksamaan linier dan bagaimana menerjemahkan frasa 'hanya 290' (maksimal) ke dalam simbol matematika yang tepat.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu mengidentifikasi variabel, koefisien, dan tanda pertidaksamaan yang sesuai dengan konteks 'maksimal'.. Bukti: menggunakan lima bus yang dapat mengangkut hanya 290 penumpang; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan simbol pertidaksamaan (≤, ≥, <, >). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari materi pertidaksamaan linier satu variabel yang diajarkan di kelas 8, dengan tingkat kesulitan yang rendah karena hanya memerlukan satu langkah pemodelan. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menemukan Konsep Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sekolah menyelenggarakan proyek penguatan proil pelajar Pancasila pada tema kearifan lokal untuk melakukan observasi menggunakan lima bus yang dapat mengangkut hanya 290 penumpang.

Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
Pilihan: A. 5x ≥ 290 (x = banyak penumpang per bus)
B. x ≤ 290 (x = banyak penumpang per bus)
C. 5x ≤ 290 (x = banyak penumpang per bus)
D. 5x < 290 (x = banyak penumpang per bus)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `4e77861a69e63696e5ee9f5e`

Pak Doni adalah seorang kuli bangunan kontrak yang sedang mengerjakan proyek pemerintah dengan penghasilan tidak lebih dari Rp. 3.600.000 setiap bulannya.<br><br>Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

| Opsi | Isi |
|---|---|
| A | x ≥ 3.600.000 (x = penghasilan Pak Doni per bulan) |
| B | x ≤ 3.600.000 (x = penghasilan Pak Doni per bulan) |
| C | x < 3.600.000 (x = penghasilan Pak Doni per bulan) |
| D | x = 3.600.000 (x = penghasilan Pak Doni per bulan) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Frasa 'tidak lebih dari' secara matematis diterjemahkan sebagai 'kurang dari atau sama dengan' (≤). Jika x adalah penghasilan Pak Doni, maka model pertidaksamaannya adalah x ≤ 3.600.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe36672215c4bcb910608af3563db7fe78d925c76802009af40d86f3163a3d0d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2070 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2064 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2035 |

Run 1 — solusi: Frasa 'tidak lebih dari' secara matematis diterjemahkan sebagai 'kurang dari atau sama dengan' (≤). Jika x adalah penghasilan Pak Doni, maka model pertidaksamaannya adalah x ≤ 3.600.000.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan pernyataan verbal ke dalam model matematika (pertidaksamaan). Ini adalah proses menerapkan konsep dasar pertidaksamaan pada situasi rutin.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara frasa verbal 'tidak lebih dari' dengan simbol pertidaksamaan (≤).. Bukti: penghasilan tidak lebih dari Rp. 3.600.000
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan satu langkah penerjemahan dari bahasa verbal ke simbol matematika tanpa perhitungan kompleks atau strategi nonrutin.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang simbol pertidaksamaan (≤, ≥, <, >) dan penerjemahan kalimat verbal ke model matematika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena merupakan pengenalan dasar pemodelan pertidaksamaan linier satu variabel. |

Run 2 — solusi: Frasa 'tidak lebih dari' secara matematis diterjemahkan sebagai 'kurang dari atau sama dengan' (≤). Jika x adalah penghasilan Pak Doni, maka model pertidaksamaannya adalah x ≤ 3.600.000.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan pernyataan verbal ke dalam model matematika (pertidaksamaan). Ini adalah proses menerapkan pemahaman konsep dasar pertidaksamaan pada situasi sederhana.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai hubungan antara frasa verbal ('tidak lebih dari') dengan simbol matematika (≤), yang merupakan bagian dari pengetahuan konseptual.. Bukti: tidak lebih dari; pertidaksamaan linier satu variabel
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan satu langkah penerjemahan dari bahasa verbal ke simbol matematika tanpa memerlukan strategi kompleks atau perhitungan.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang simbol pertidaksamaan (<, >, ≤, ≥) dan terjemahan frasa verbal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar dasar untuk materi pertidaksamaan linier satu variabel di kelas 8, di mana siswa diharapkan mampu memodelkan situasi nyata ke bentuk matematika sederhana. |

Run 3 — solusi: Frasa 'tidak lebih dari' secara matematis diterjemahkan sebagai 'kurang dari atau sama dengan' (≤). Jika x adalah penghasilan Pak Doni, maka model pertidaksamaannya adalah x ≤ 3.600.000.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan pernyataan verbal ke dalam model matematika (pertidaksamaan). Ini adalah proses menerapkan pemahaman konsep ke dalam situasi rutin.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara frasa verbal 'tidak lebih dari' dengan simbol pertidaksamaan (≤), yang merupakan pemahaman konseptual.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan satu keputusan utama yaitu menerjemahkan frasa verbal ke simbol matematika. Tidak ada langkah kompleks atau strategi non-rutin.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang simbol pertidaksamaan (<, >, ≤, ≥) dan penerjemahan kalimat verbal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 sebagai pengenalan atau latihan dasar pemodelan pertidaksamaan linier satu variabel. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menemukan Konsep Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Doni adalah seorang kuli bangunan kontrak yang sedang mengerjakan proyek pemerintah dengan penghasilan tidak lebih dari Rp. 3.600.000 setiap bulannya.

Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
Pilihan: A. x ≥ 3.600.000 (x = penghasilan Pak Doni per bulan)
B. x ≤ 3.600.000 (x = penghasilan Pak Doni per bulan)
C. x < 3.600.000 (x = penghasilan Pak Doni per bulan)
D. x = 3.600.000 (x = penghasilan Pak Doni per bulan)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 11 kali pengangkutan |
| B | 9,45 kali pengangkutan |
| C | 10 kali pengangkutan |
| D | 9 kali pengangkutan |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Kapasitas muatan kotak per trip = (2000 - 150) / 50 = 1850 / 50 = 37 kotak. Total trip = 350 / 37 = 9,459. Karena trip harus bilangan bulat dan semua kotak harus terangkut, maka diperlukan pembulatan ke atas menjadi 10 kali pengangkutan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2d1d76900284370d821d1963dd817781f90082d6f9b36215cd022cb5845021f4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3050 |
| 2 | success | valid / verified | applying | procedural | Medium | 2707 |
| 3 | success | valid / verified | applying | procedural | Medium | 3035 |

Run 1 — solusi: Kapasitas muatan kotak per trip = (2000 - 150) / 50 = 1850 / 50 = 37 kotak. Total trip = 350 / 37 = 9,459. Karena trip harus bilangan bulat dan semua kotak harus terangkut, maka diperlukan pembulatan ke atas menjadi 10 kali pengangkutan.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kapasitas efektif, memodelkan masalah ke dalam pembagian, dan menerapkan penalaran pembulatan ke atas dalam konteks dunia nyata.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Pengemudi dan kernek memiliki berat total 150 kg; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg; berapa kali pengangkutan kotak yang harus dilakukan
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika dan konsep pertidaksamaan/pembulatan untuk menyelesaikan masalah kontekstual.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; kotak yang berisi 50 kg; berapa kali pengangkutan kotak yang harus dilakukan
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang kapasitas bersih dan pembulatan ke atas (ceiling function) dalam konteks nyata. Ini adalah prosedur rutin yang melibatkan beberapa langkah logis.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg; Pengemudi dan kernek memiliki berat total 150 kg; 350 kotak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan pemodelan masalah nyata sederhana dengan pertidaksamaan/pembagian. |

Run 2 — solusi: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg = 37 kotak. Banyak pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena harus mengangkut semua kotak, maka dibulatkan ke atas menjadi 10 kali pengangkutan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep aritmatika dan pertidaksamaan dalam konteks dunia nyata, memilih prosedur pembagian dan pembulatan ke atas yang tepat untuk menyelesaikan masalah.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma pembagian dan pemahaman prosedural tentang bagaimana menginterpretasikan sisa hasil bagi dalam konteks masalah nyata (pembulatan ke atas).. Bukti: berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin yang saling terkait: menghitung kapasitas bersih, menentukan kapasitas per angkut, dan melakukan pembulatan yang logis sesuai konteks.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; 350 kotak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep pembagian dan pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Masalah ini adalah aplikasi standar pertidaksamaan linier satu variabel untuk kelas 8, menuntut ketelitian dalam interpretasi hasil pembagian. |

Run 3 — solusi: Kapasitas muatan kotak per trip = (2000 - 150) / 50 = 1850 / 50 = 37 kotak. Total trip = 350 / 37 ≈ 9,46. Karena harus mengangkut semua kotak, maka dibulatkan ke atas menjadi 10 kali pengangkutan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pertidaksamaan atau pembagian untuk menentukan kapasitas muatan per trip dan membulatkan hasil ke atas sesuai konteks masalah nyata.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan prosedur aritmatika bertahap (pengurangan, pembagian, dan pembulatan ke atas) untuk menyelesaikan masalah kontekstual.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (menghitung kapasitas bersih, membagi total beban, dan interpretasi pembulatan ke atas) yang saling terkait.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar (pengurangan, pembagian) dan pemahaman konteks pembulatan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menuntut siswa tidak hanya menghitung, tetapi memahami bahwa hasil pembagian harus dibulatkan ke atas karena sisa muatan tetap memerlukan satu perjalanan tambahan. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.

Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
Pilihan: A. 11 kali pengangkutan
B. 9,45 kali pengangkutan
C. 10 kali pengangkutan
D. 9 kali pengangkutan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `b0ce9e96d828be7c94c0894c`

Humam memiliki uang Rp180.000,00 yang akan digunakan untuk membeli jeruk. Untuk harga 1 kg jeruk adalah Rp15.000,00.<br><br>Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.

| Opsi | Isi |
|---|---|
| A | x ≥ 12 (paling banyak 12 kg jeruk) |
| B | x ≤ 1.200 (paling banyak 1.200 kg jeruk) |
| C | x ≤ 15 (paling banyak 15 kg jeruk) |
| D | x ≤ 12 (paling banyak 12 kg jeruk) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misalkan x adalah berat jeruk dalam kg. Biaya total adalah 15.000x. Karena uang Humam Rp180.000, maka 15.000x ≤ 180.000. Membagi kedua sisi dengan 15.000 menghasilkan x ≤ 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b968ece9e4860d21341000ef98bfedd2f315fe01ed74083e0345c17fa387c10b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2093 |
| 2 | success | valid / verified | applying | procedural | Easy | 2117 |
| 3 | success | valid / verified | applying | procedural | Easy | 2099 |

Run 1 — solusi: Misalkan x adalah berat jeruk dalam kg. Biaya total adalah 15.000x. Karena uang Humam Rp180.000, maka 15.000x ≤ 180.000. Membagi kedua sisi dengan 15.000 menghasilkan x ≤ 12.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika pertidaksamaan linier satu variabel dan menyelesaikannya. Ini termasuk dalam kategori applying karena menerapkan konsep pertidaksamaan pada situasi rutin.. Bukti: 15.000x ≤ 180.000; x ≤ 12
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur algoritma standar untuk menyelesaikan pertidaksamaan linier satu variabel.. Bukti: 15.000x ≤ 180.000; x ≤ 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah pemodelan dan satu langkah penyelesaian (pembagian), sesuai untuk tingkat kesulitan Easy.. Bukti: 15.000x ≤ 180.000; x ≤ 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar pertidaksamaan linier satu variabel dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari materi PtLSV kelas 8 yang melibatkan pemodelan sederhana dan operasi aritmatika dasar. |

Run 2 — solusi: Misalkan x adalah berat jeruk dalam kg. Biaya total adalah 15.000x. Karena uang Humam terbatas pada 180.000, maka 15.000x ≤ 180.000. Membagi kedua ruas dengan 15.000 menghasilkan x ≤ 12.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan situasi kontekstual ke dalam model matematika (pertidaksamaan) dan menyelesaikannya, yang merupakan penerapan prosedur pada situasi rutin.. Bukti: Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang hubungan antara variabel, harga satuan, dan batasan total, serta penggunaan algoritma penyelesaian pertidaksamaan linier.. Bukti: 15.000x ≤ 180.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu variabel dan satu ketidaksamaan linear sederhana. Siswa hanya perlu melakukan operasi pembagian dasar untuk mendapatkan nilai x.. Bukti: Humam memiliki uang Rp180.000,00; harga 1 kg jeruk adalah Rp15.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linier satu variabel dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 8 untuk materi pertidaksamaan linier satu variabel yang melibatkan pemodelan masalah kontekstual sederhana. |

Run 3 — solusi: Misalkan x adalah berat jeruk dalam kg. Harga total jeruk adalah 15.000x. Karena uang Humam terbatas (maksimal 180.000), maka 15.000x ≤ 180.000. Membagi kedua ruas dengan 15.000 menghasilkan x ≤ 12.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika pertidaksamaan linear satu variabel dan menyelesaikannya. Ini melibatkan penerapan prosedur standar pada situasi rutin.. Bukti: Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma penyelesaian pertidaksamaan linear satu variabel (prosedural) untuk menentukan batasan nilai variabel x.. Bukti: 15.000x ≤ 180.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Langkah penyelesaiannya langsung (satu langkah pembagian) dan konteksnya sangat familiar.. Bukti: Humam memiliki uang Rp180.000,00; harga 1 kg jeruk adalah Rp15.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linear satu variabel dan operasi pembagian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pertidaksamaan linear satu variabel adalah kurikulum standar kelas 8. Soal ini menguji pemahaman dasar tanpa kompleksitas tambahan. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Humam memiliki uang Rp180.000,00 yang akan digunakan untuk membeli jeruk. Untuk harga 1 kg jeruk adalah Rp15.000,00.

Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.
Pilihan: A. x ≥ 12 (paling banyak 12 kg jeruk)
B. x ≤ 1.200 (paling banyak 1.200 kg jeruk)
C. x ≤ 15 (paling banyak 15 kg jeruk)
D. x ≤ 12 (paling banyak 12 kg jeruk)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `bb5563c106a35bce8aef90f0`

Panitia OSIS menjual tiket untuk konser musik yang merupakan acara tahunan sekolah. Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani. a. Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik. b. Tulislah bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik. c. Jika ada 10 tiket yang tidak terjual, tulislah bentuk aljabar dari banyak tiket secara keseluruhan.<br><br>d. Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

| Opsi | Isi |
|---|---|
| A | 92 tiket |
| B | 76 tiket |
| C | 78 tiket |
| D | 88 tiket |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a + 6) + 10 = 6a + 16. Jika a=12, maka 6(12) + 16 = 72 + 16 = 88.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d5fde5db0c4f3516899f3dcb0e5f76194f5afbac0eb9a0dfcced09dda2787884`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2216 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2217 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2240 |

Run 1 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a + 6) + 10 = 6a + 16. Jika a=12, maka 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam ekspresi aljabar, menyederhanakan bentuk aljabar, dan melakukan substitusi nilai untuk mendapatkan hasil akhir. Ini adalah proses penerapan konsep aljabar pada situasi rutin.. Bukti: Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik; Tulislah bentuk aljabar dari total tiket yang terjual; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang variabel dan operasi aljabar untuk memodelkan situasi nyata.. Bukti: Tulislah bentuk aljabar dari banyak tiket; total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (pemodelan, penyederhanaan, substitusi) yang saling terkait namun prosedurnya familiar bagi siswa kelas 8.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika ada 10 tiket yang tidak terjual, tulislah bentuk aljabar dari banyak tiket secara keseluruhan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar (penjumlahan/pengurangan suku sejenis) dan substitusi nilai. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menggabungkan pemodelan aljabar sederhana dengan operasi aritmatika dasar. |

Run 2 — solusi: Rani=a, Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a + 6) + 10 = 6a + 16. Jika a=12, maka 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam ekspresi aljabar, menyederhanakan bentuk aljabar, dan melakukan substitusi nilai untuk mendapatkan hasil akhir.. Bukti: Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Tulislah bentuk aljabar dari total tiket yang terjual; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang variabel dan operasi aljabar dasar untuk memodelkan situasi nyata.. Bukti: Tulislah bentuk aljabar dari banyak tiket; Tulislah bentuk aljabar dari total tiket yang terjual
- Intended difficulty `classify/Medium`: Soal melibatkan beberapa langkah rutin (pemodelan, penyederhanaan, substitusi) yang saling terkait dalam satu konteks cerita, namun prosedurnya standar untuk kelas 8.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani.; Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani.; Malik menjual 10 tiket lebih banyak dari Rani.; Jika ada 10 tiket yang tidak terjual

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar (penjumlahan/pengurangan suku sejenis) dan substitusi nilai. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini merupakan aplikasi standar pemodelan aljabar di kelas 8, memerlukan ketelitian dalam menjumlahkan suku-suku aljabar dan konstanta. |

Run 3 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a+6) + 10 = 6a + 16. Jika a=12, maka 6(12)+16 = 72+16 = 88.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam ekspresi aljabar (pemodelan) dan melakukan operasi penjumlahan suku sejenis, yang merupakan penerapan konsep dasar aljabar dalam situasi rutin.. Bukti: Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Tulislah bentuk aljabar dari total tiket yang terjual; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana variabel dan konstanta merepresentasikan kuantitas dalam konteks masalah (konseptual) serta prosedur manipulasi aljabar untuk menyederhanakan bentuk (prosedural).. Bukti: Tulislah bentuk aljabar dari banyak tiket; total tiket yang terjual; 6a + 16
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (pemodelan tiap individu, penjumlahan total, penambahan konstanta tiket tidak terjual, substitusi nilai). Beban kognitif moderat karena memerlukan ketelitian dalam mengelola beberapa variabel dan konstanta.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani.; Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani.; Malik menjual 10 tiket lebih banyak dari Rani.; Jika ada 10 tiket yang tidak terjual

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar (penjumlahan/pengurangan suku sejenis) dan pemahaman variabel. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan pemodelan aljabar sederhana yang merupakan kompetensi dasar kurikulum. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Pemodelan dengan Bentuk Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Panitia OSIS menjual tiket untuk konser musik yang merupakan acara tahunan sekolah. Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani. a. Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik. b. Tulislah bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik. c. Jika ada 10 tiket yang tidak terjual, tulislah bentuk aljabar dari banyak tiket secara keseluruhan.

d. Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?
Pilihan: A. 92 tiket
B. 76 tiket
C. 78 tiket
D. 88 tiket
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `bc52760c552d361c6b1ad513`

Diketahui Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; dan relasi dari himpunan C ke D adalah "kurang dari". Nyatakan relasi tersebut dalam tiga cara berikut: a. Diagram panah b. Diagram Cartesius c. Himpunan pasangan berurutan<br><br>Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.

| Opsi | Isi |
|---|---|
| A | {(3, 4), (4, 5)} |
| B | {(4, 3), (5, 3), (5, 4)} |
| C | {(3, 3), (4, 4)} |
| D | {(3, 4), (3, 5), (4, 5)} |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Himpunan C = {3, 4}, D = {3, 4, 5}. Relasi 'kurang dari' dari C ke D berarti mencari pasangan (c, d) dengan c ∈ C dan d ∈ D sedemikian sehingga c < d. Untuk c=3: 3<4 dan 3<5 (pasangan: (3,4), (3,5)). Untuk c=4: 4<5 (pasangan: (4,5)). Himpunan pasangan berurutan: {(3, 4), (3, 5), (4, 5)}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2730334d6abd0061d8396a84da2122e2314c5f6a37f5fe5e13aec3472a07aded`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2220 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2245 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2174 |

Run 1 — solusi: Himpunan C = {3, 4}, D = {3, 4, 5}. Relasi 'kurang dari' dari C ke D berarti mencari pasangan (c, d) dengan c ∈ C dan d ∈ D sedemikian sehingga c < d. Untuk c=3: 3<4 dan 3<5 (pasangan: (3,4), (3,5)). Untuk c=4: 4<5 (pasangan: (4,5)). Himpunan pasangan berurutan: {(3, 4), (3, 5), (4, 5)}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi relasi dan menerapkan kondisi 'kurang dari' pada elemen-elemen himpunan yang diberikan. Ini adalah proses penerapan konsep relasi pada situasi rutin.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep relasi matematika dan bagaimana merepresentasikannya dalam bentuk himpunan pasangan berurutan.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Himpunan C = {3, 4}; himpunan D = {3, 4, 5}
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jumlah elemen yang sangat sedikit, sehingga beban kognitif rendah. Siswa hanya perlu melakukan pengecekan perbandingan sederhana.. Bukti: Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; relasi dari himpunan C ke D adalah "kurang dari"

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan perbandingan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi adalah topik standar kelas 8. Soal ini menggunakan angka kecil dan prosedur yang sangat langsung, cocok untuk tingkat kesulitan rendah. |

Run 2 — solusi: Relasi 'kurang dari' dari C={3, 4} ke D={3, 4, 5} mencari pasangan (c, d) dengan c < d. Untuk c=3, d yang memenuhi adalah 4 dan 5 (3<4, 3<5). Untuk c=4, d yang memenuhi adalah 5 (4<5). Himpunan pasangan berurutan: {(3, 4), (3, 5), (4, 5)}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi relasi 'kurang dari' dan menerapkannya pada elemen-elemen himpunan yang diberikan untuk membentuk pasangan berurutan yang memenuhi syarat.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang relasi antar himpunan dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; relasi dari himpunan C ke D adalah "kurang dari"
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk tingkat kelas 8. Siswa hanya perlu melakukan pengecekan perbandingan sederhana pada elemen himpunan yang terbatas (hanya 2 elemen di C dan 3 elemen di D).. Bukti: Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; relasi dari himpunan C ke D adalah "kurang dari"

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan perbandingan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi adalah topik dasar kelas 8. Prosedur pengecekan pasangan (c, d) dengan c < d sangat langsung dan tidak memerlukan strategi kompleks. |

Run 3 — solusi: Relasi 'kurang dari' dari C={3, 4} ke D={3, 4, 5} mencari pasangan (c, d) dengan c < d. Untuk c=3, d yang memenuhi adalah 4 dan 5 (3<4, 3<5). Untuk c=4, d yang memenuhi adalah 5 (4<5). Himpunan pasangan berurutan: {(3, 4), (3, 5), (4, 5)}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi relasi 'kurang dari' dan menerapkannya pada dua himpunan yang diberikan untuk membentuk pasangan berurutan yang memenuhi syarat.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang relasi antar himpunan dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu melakukan pengecekan sistematis terhadap elemen-elemen himpunan untuk memenuhi kondisi relasi yang diberikan.. Bukti: Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; relasi dari himpunan C ke D adalah "kurang dari"

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep relasi/pertidaksamaan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi adalah topik dasar kelas 8. Tugas ini hanya memerlukan pengecekan elemen satu per satu tanpa strategi kompleks. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Memahami Relasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; dan relasi dari himpunan C ke D adalah "kurang dari". Nyatakan relasi tersebut dalam tiga cara berikut: a. Diagram panah b. Diagram Cartesius c. Himpunan pasangan berurutan

Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.
Pilihan: A. {(3, 4), (4, 5)}
B. {(4, 3), (5, 3), (5, 4)}
C. {(3, 3), (4, 4)}
D. {(3, 4), (3, 5), (4, 5)}
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `e044f1847d7a97d6815a581d`

Apabila relasi himpunan E ke F merupakan "akar dari" dengan diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}, maka nyatakan relasi tersebut dengan tiga cara berikut ini: a. himpunan pasangan berurutan. b. diagram panah; c. diagram Cartesius.<br><br>Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.

| Opsi | Isi |
|---|---|
| A | {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36)} |
| B | {(1, 1), (2, 4), (3, 9), (4, 16), (5, 20), (6, 36)} |
| C | {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)} |
| D | {(1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6)} |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Relasi 'akar dari' dari E ke F berarti untuk setiap e di E, pasangan f di F harus memenuhi e = akar(f) atau e^2 = f. Untuk E={1, 2, 3, 4, 5, 6}: 1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36. Semua hasil kuadrat ada di F. Maka himpunan pasangan berurutannya adalah {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `04a1955761445761fe19b9091f2139decf6669c9c2cda8be9a888fa379d49458`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2480 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2490 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2437 |

Run 1 — solusi: Relasi 'akar dari' dari E ke F berarti untuk setiap e di E, pasangan f di F harus memenuhi e = akar(f) atau e^2 = f. Untuk E={1, 2, 3, 4, 5, 6}: 1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36. Semua hasil kuadrat ada di F. Maka himpunan pasangan berurutannya adalah {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi relasi 'akar dari' dan menerapkan prosedur pemetaan elemen himpunan E ke F berdasarkan aturan tersebut. Ini adalah penerapan konsep relasi yang rutin.. Bukti: Apabila relasi himpunan E ke F merupakan "akar dari"; E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang relasi matematika dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: relasi himpunan E ke F merupakan "akar dari"
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Prosedur yang diperlukan adalah mengkuadratkan setiap elemen E dan memeriksa keberadaannya di F. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang relasi, himpunan, dan operasi kuadrat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi dan fungsi adalah kurikulum standar kelas 8. Tugas ini hanya memerlukan pengecekan langsung terhadap definisi relasi yang diberikan. |

Run 2 — solusi: Relasi 'akar dari' dari E ke F berarti untuk setiap e di E, f = e^2 harus ada di F. Pasangan (e, f) adalah: 1^2=1 (1,1), 2^2=4 (2,4), 3^2=9 (3,9), 4^2=16 (4,16), 5^2=25 (5,25), 6^2=36 (6,36). Semua nilai f ada di F. Maka himpunan pasangan berurutannya adalah {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi relasi 'akar dari' dan menerapkannya untuk memetakan elemen dari himpunan E ke F. Ini adalah proses penerapan konsep relasi yang rutin.. Bukti: relasi himpunan E ke F merupakan "akar dari"; diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana relasi didefinisikan antara dua himpunan.. Bukti: relasi himpunan E ke F merupakan "akar dari"
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Prosedurnya jelas: mengkuadratkan setiap elemen di E dan memeriksa keberadaannya di F. Tidak ada strategi non-rutin atau kendala kompleks.. Bukti: relasi himpunan E ke F merupakan "akar dari"; himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan operasi kuadrat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 8 mengenai relasi dan fungsi. |

Run 3 — solusi: Relasi 'akar dari' dari E ke F berarti untuk setiap x di E, pasangannya y di F harus memenuhi x = akar(y) atau x^2 = y. Untuk E = {1, 2, 3, 4, 5, 6}, maka: 1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36. Semua hasil kuadrat ini ada di F. Maka himpunan pasangan berurutannya adalah {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi relasi 'akar dari' untuk membentuk pasangan berurutan dari dua himpunan yang diberikan. Ini adalah penerapan konsep relasi yang rutin.. Bukti: Apabila relasi himpunan E ke F merupakan "akar dari" dengan diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep relasi dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: relasi himpunan E ke F merupakan "akar dari"
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya meminta siswa memetakan elemen berdasarkan aturan yang jelas ('akar dari'). Tidak ada strategi non-rutin atau kendala kompleks.. Bukti: E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang relasi dan operasi kuadrat/akar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan konsep dasar relasi yang merupakan materi standar. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Memahami Relasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila relasi himpunan E ke F merupakan "akar dari" dengan diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}, maka nyatakan relasi tersebut dengan tiga cara berikut ini: a. himpunan pasangan berurutan. b. diagram panah; c. diagram Cartesius.

Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.
Pilihan: A. {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}
B. {(1, 1), (2, 4), (3, 9), (4, 16), (5, 20), (6, 36)}
C. {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}
D. {(1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6)}
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `cc51dc6d0e0814ecda8e12e1`

Periksa apakah dua himpuan berikut ini termasuk fungsi atau bukan fungsi? Jelaskan. Diketahui bahwa himpunan R dan S memiliki anggota masing-masing adalah R = {3, 4, 6, 8, 9, 12, 14, 18} dan S = {1, 6, 9}. Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan,<br><br>Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?

| Opsi | Isi |
|---|---|
| A | Fungsi, karena setiap anggota R mempunyai tepat satu pasangan di S |
| B | Bukan fungsi, karena tidak semua anggota R memiliki pasangan di S |
| C | Bukan fungsi, karena S bukan himpunan bilangan bulat |
| D | Fungsi, karena semua anggota S mempunyai pasangan di R |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Relasi didefinisikan sebagai r = 1/3 * s atau s = 3r. Untuk setiap r di R, harus ada tepat satu s di S. Uji anggota R: jika r=3, s=9 (ada di S). Jika r=4, s=12 (tidak ada di S). Jika r=6, s=18 (tidak ada di S), dan seterusnya. Karena banyak anggota R yang tidak memiliki pasangan di S, maka relasi ini bukan fungsi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a910339cc0e11c742e48787b3c9fe761170c43be72b8b093adcd7b93679fe735`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2238 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3110 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2244 |

Run 1 — solusi: Relasi didefinisikan sebagai r = 1/3 * s atau s = 3r. Untuk setiap r di R, harus ada tepat satu s di S. Uji anggota R: jika r=3, s=9 (ada di S). Jika r=4, s=12 (tidak ada di S). Jika r=6, s=18 (tidak ada di S), dan seterusnya. Karena banyak anggota R yang tidak memiliki pasangan di S, maka relasi ini bukan fungsi.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi formal fungsi (setiap anggota domain harus memiliki tepat satu pasangan di kodomain) pada relasi yang diberikan untuk menentukan apakah relasi tersebut memenuhi syarat fungsi.. Bukti: Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan; Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi fungsi, yaitu hubungan antara domain dan kodomain yang memenuhi syarat pemetaan.. Bukti: Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman definisi fungsi dan pengecekan sistematis terhadap elemen himpunan. Siswa harus menyadari bahwa fungsi memerlukan setiap elemen domain memiliki pasangan, yang tidak terpenuhi di sini.. Bukti: R = {3, 4, 6, 8, 9, 12, 14, 18} dan S = {1, 6, 9}; "Anggota R sepertiga kali anggota S"

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi (domain, kodomain, syarat pemetaan) dan operasi perkalian dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan memahami definisi fungsi. Soal ini menuntut ketelitian dalam memeriksa setiap elemen domain, yang merupakan langkah rutin namun memerlukan pemilihan prosedur yang tepat. |

Run 2 — solusi: Relasi didefinisikan sebagai s = 3r. Untuk r=3, s=9 (ada di S). Untuk r=4, s=12 (tidak ada di S). Karena tidak semua anggota domain R memiliki pasangan di kodomain S, maka relasi tersebut bukan fungsi.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi fungsi (setiap anggota domain harus memiliki tepat satu pasangan di kodomain) pada relasi yang diberikan.. Bukti: Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan; Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang syarat relasi dikatakan sebagai fungsi.. Bukti: Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?
- Intended difficulty `classify/Medium`: Siswa harus memeriksa pemetaan untuk setiap elemen domain R. Meskipun prosedurnya rutin, siswa perlu ketelitian dalam mengecek apakah setiap elemen memiliki pasangan di S.. Bukti: R = {3, 4, 6, 8, 9, 12, 14, 18} dan S = {1, 6, 9}; Anggota R sepertiga kali anggota S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi, relasi, dan operasi perkalian dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menguji pemahaman dasar fungsi dengan himpunan diskrit. |

Run 3 — solusi: Definisi fungsi dari R ke S mensyaratkan setiap anggota R memiliki tepat satu pasangan di S. Relasi yang diberikan adalah 'Anggota R sepertiga kali anggota S' atau s = 3r. Untuk r=3, s=9 (ada di S). Untuk r=4, s=12 (tidak ada di S). Karena anggota R lainnya (4, 6, 8, 9, 12, 14, 18) tidak memiliki pasangan di S, maka relasi ini bukan fungsi.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi formal fungsi (setiap anggota domain harus memiliki tepat satu pasangan di kodomain) pada relasi yang diberikan untuk menentukan apakah relasi tersebut memenuhi syarat fungsi.. Bukti: Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?; Apabila 'Anggota R sepertiga kali anggota S' adalah relasi yang ditentukan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi fungsi (relasi khusus di mana setiap anggota domain dipetakan ke tepat satu anggota kodomain).. Bukti: Periksa apakah dua himpuan berikut ini termasuk fungsi atau bukan fungsi?; Apabila 'Anggota R sepertiga kali anggota S' adalah relasi yang ditentukan
- Intended difficulty `classify/Medium`: Soal memerlukan pengecekan sistematis terhadap elemen domain untuk melihat apakah syarat fungsi terpenuhi. Ini adalah prosedur rutin dalam topik fungsi kelas 8.. Bukti: R = {3, 4, 6, 8, 9, 12, 14, 18} dan S = {1, 6, 9}; Apabila 'Anggota R sepertiga kali anggota S' adalah relasi yang ditentukan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi fungsi (domain, kodomain, relasi) dan operasi perkalian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena menguji pemahaman dasar tentang syarat fungsi menggunakan himpunan diskrit yang sederhana. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Memahami Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Periksa apakah dua himpuan berikut ini termasuk fungsi atau bukan fungsi? Jelaskan. Diketahui bahwa himpunan R dan S memiliki anggota masing-masing adalah R = {3, 4, 6, 8, 9, 12, 14, 18} dan S = {1, 6, 9}. Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan,

Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?
Pilihan: A. Fungsi, karena setiap anggota R mempunyai tepat satu pasangan di S
B. Bukan fungsi, karena tidak semua anggota R memiliki pasangan di S
C. Bukan fungsi, karena S bukan himpunan bilangan bulat
D. Fungsi, karena semua anggota S mempunyai pasangan di R
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `13db9a1e91c27f3f1a174ba0`

Perhatikan dengan cermat terhadap aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m.<br><br>Apa makna pesan dari kata sandi berikut ini: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

| Opsi | Isi |
|---|---|
| A | ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH |
| B | GURUKU ADALAH ORANG TUAKU KETIKA DI RUMAH |
| C | ORANG TUAKU BUKAN GURUKU KETIKA DI RUMAH |
| D | ORANG TUAKU ADALAH GURUKU KETIKA DI SEKOLAH |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Substitusi huruf berdasarkan pemetaan: g->O, k->R, q->A, f->N, u->G (gkqfu=ORANG); z->T, x->U, q->A, a->K, x->U (zxqax=TUAKU); q->A, r->D, q->A, s->L, q->A, i->H (qrqsqi=ADALAH); u->G, x->U, k->R, x->U, a->K, x->U (uxkxax=GURUKU); a->K, t->E, z->T, o->I, a->K, q->A (atzoaq=KETIKA); r->D, o->I (ro=DI); k->R, x->U, d->M, q->A, i->H (kxdqi=RUMAH). Hasil: ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d046cfa9413354bed511f299b0d5939fceb7669d35092250c1294f64374a9d80`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2486 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2307 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2357 |

Run 1 — solusi: Substitusi huruf berdasarkan pemetaan: A=q, B=w, C=e, D=r, E=t, F=y, G=u, H=i, I=o, J=p, K=a, L=s, M=d, N=f, O=g, P=h, Q=j, R=k, S=l, T=z, U=x, V=c, W=v, X=b, Y=n, Z=m. Kata 'gkqfu' -> g=O, k=R, q=A, f=N, u=G (ORANG). 'zxqax' -> z=T, x=U, q=A, a=K, x=U (TUAKU). 'qrqsqi' -> q=A, r=D, q=A, s=L, q=A, i=H (ADALAH). 'uxkxax' -> u=G, x=U, k=R, x=U, a=K, x=U (GURUKU). 'atzoaq' -> a=K, t=E, z=T, o=I, a=K, q=A (KETIKA). 'ro' -> r=D, o=I (DI). 'kxdqi' -> k=R, x=U, d=M, q=A, i=H (RUMAH). Hasil: ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pemetaan (fungsi) satu-satu antara domain (huruf asli) dan kodomain (huruf sandi) untuk mendekode pesan.. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam menerapkan aturan korespondensi satu-satu yang diberikan untuk melakukan dekripsi.. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan substitusi langsung berdasarkan tabel pemetaan yang sudah disediakan secara eksplisit. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korespondensi satu-satu/fungsi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 sebagai aplikasi langsung dari konsep fungsi/pemetaan. |

Run 2 — solusi: Substitusi huruf berdasarkan pemetaan: g->O, k->R, q->A, f->N, u->G (gkqfu=ORANG); z->T, x->U, q->A, a->K, x->U (zxqax=TUAKU); q->A, r->D, q->A, s->L, q->A, i->H (qrqsqi=ADALAH); u->G, x->U, k->R, x->U, a->K, x->U (uxkxax=GURUKU); a->K, t->E, z->T, o->I, a->K, q->A (atzoaq=KETIKA); r->D, o->I (ro=DI); k->R, x->U, d->M, q->A, i->H (kxdqi=RUMAH). Hasil: ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan pemetaan (fungsi) yang diberikan untuk mendekode pesan. Ini adalah proses menerapkan prosedur yang didefinisikan secara eksplisit dalam soal.. Bukti: substitusi huruf sesuai tabel sandi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep fungsi sebagai pemetaan satu-satu antara dua himpunan (huruf alfabet ke huruf sandi).. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m
- Intended difficulty `classify/Easy`: Tugas ini bersifat rutin dan mekanis. Siswa hanya perlu melakukan substitusi huruf demi huruf sesuai tabel yang diberikan. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pemetaan/fungsi (korespondensi satu-satu). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun panjang, proses dekode adalah algoritma sederhana yang sesuai untuk kelas 8 sebagai pengenalan fungsi. |

Run 3 — solusi: Substitusi balik berdasarkan pemetaan: g->O, k->R, q->A, f->N, u->G (gkqfu=ORANG); z->T, x->U, q->A, a->K, x->U (zxqax=TUAKU); q->A, r->D, q->A, s->L, q->A, i->H (qrqsqi=ADALAH); u->G, x->U, k->R, x->U, a->K, x->U (uxkxax=GURUKU); a->K, t->E, z->T, o->I, a->K, q->A (atzoaq=KETIKA); r->D, o->I (ro=DI); k->R, x->U, d->M, q->A, i->H (kxdqi=RUMAH). Hasil: ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep fungsi sebagai pemetaan satu-satu antara dua himpunan (huruf alfabet ke huruf sandi) dan menerapkan pemetaan tersebut secara terbalik untuk mendekode pesan.. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang fungsi/relasi sebagai pemetaan, di mana setiap elemen domain dipasangkan dengan tepat satu elemen kodomain.. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan substitusi langsung berdasarkan tabel pemetaan yang diberikan. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi/pemetaan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan sesuai untuk kelas 8 karena hanya melibatkan operasi substitusi sederhana yang merupakan aplikasi langsung dari konsep fungsi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4551`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan aturan pemetaan (fungsi) yang diberikan secara eksplisit untuk mendekode pesan. Ini adalah proses menerapkan prosedur yang didefinisikan dalam soal.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang fungsi sebagai pemetaan satu-satu antara dua himpunan (huruf alfabet ke huruf sandi).
- Intended difficulty `Easy`: Tugas ini bersifat rutin dan mekanis. Siswa hanya perlu melakukan substitusi huruf demi huruf sesuai tabel yang diberikan. Tidak ada strategi nonrutin atau kendala kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pemetaan/fungsi (korespondensi satu-satu). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun panjang, proses dekode adalah algoritma sederhana yang sesuai untuk kelas 8 sebagai pengenalan fungsi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Memahami Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan dengan cermat terhadap aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m.

Apa makna pesan dari kata sandi berikut ini: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi
Pilihan: A. ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH
B. GURUKU ADALAH ORANG TUAKU KETIKA DI RUMAH
C. ORANG TUAKU BUKAN GURUKU KETIKA DI RUMAH
D. ORANG TUAKU ADALAH GURUKU KETIKA DI SEKOLAH
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| B | 12 |
| C | 12! = 479.001.600 |
| D | 12 x 12 = 144 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n(A) = n(B) = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c1adca743952511d44cb6612ea9b787530f44b9d8b90ec0ef8798e935885a1c6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2162 |
| 2 | success | valid / verified | applying | procedural | Easy | 2142 |
| 3 | success | valid / verified | applying | procedural | Easy | 2170 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n(A) = n(B) = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus faktorial untuk menghitung korespondensi satu-satu. Meskipun ini adalah materi pengayaan, prosesnya adalah penerapan langsung dari rumus yang dipelajari.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep korespondensi satu-satu dan prinsip faktorial sebagai prosedur untuk menghitung banyaknya kemungkinan pemetaan.. Bukti: korespondensi satu-satu; n(A) = n(B) = 12
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena meskipun prosedurnya langsung (faktorial), siswa kelas 8 sering kali belum terbiasa dengan notasi faktorial atau perhitungan angka sebesar 12!, sehingga memerlukan pemilihan prosedur yang tepat.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep korespondensi satu-satu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | high |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu adalah materi pengayaan di kelas 8. Perhitungan 12! cukup menantang secara komputasi bagi siswa, namun secara konseptual merupakan penerapan rutin rumus. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi adalah 12! = 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 479.001.600.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus faktorial untuk menghitung banyaknya korespondensi satu-satu. Ini adalah penerapan prosedur yang sudah dipelajari dalam topik korespondensi satu-satu.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip perhitungan (faktorial) dalam konteks korespondensi satu-satu, yang merupakan pengetahuan prosedural.. Bukti: banyak korespondensi satu-satu yang mungkin adalah n! = 12! = 479.001.600
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Siswa hanya perlu mengingat dan menerapkan rumus n!.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korespondensi satu-satu dan konsep faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun melibatkan angka besar, prosedurnya sangat langsung (n!) dan merupakan standar materi pengayaan korespondensi satu-satu kelas 8. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan rumus faktorial untuk menghitung korespondensi satu-satu. Siswa perlu mengenali konsep korespondensi satu-satu dan menerapkan prosedur perhitungan faktorial yang sesuai.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip korespondensi satu-satu (konseptual) dan menerapkan algoritma faktorial (prosedural) untuk menyelesaikan masalah.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Prosedur yang digunakan adalah penerapan langsung rumus faktorial tanpa modifikasi strategi yang kompleks.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep korespondensi satu-satu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! cukup besar, konsep korespondensi satu-satu adalah materi standar kelas 8. Siswa hanya perlu menerapkan rumus n! secara langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3843`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan rumus faktorial (n!) untuk menghitung banyaknya korespondensi satu-satu. Ini adalah penerapan prosedur standar yang telah dipelajari dalam materi korespondensi satu-satu.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma faktorial sebagai prosedur untuk menyelesaikan masalah korespondensi satu-satu.
- Intended difficulty `Easy`: Soal ini bersifat rutin. Meskipun melibatkan angka besar, prosedurnya sangat langsung (n!) dan merupakan standar materi pengayaan korespondensi satu-satu kelas 8. Tidak ada strategi nonrutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep korespondensi satu-satu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! besar, konsep korespondensi satu-satu adalah materi standar kelas 8. Siswa hanya perlu menerapkan rumus n! secara langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Korespondensi Satu-satu (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12

Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
Pilihan: A. 12 + 11 + 10 + ... + 2 + 1 = 78
B. 12
C. 12! = 479.001.600
D. 12 x 12 = 144
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `bbdde7d74cc90e271efac7fa`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? b. n(A) = n(B) = 9<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 9?

| Opsi | Isi |
|---|---|
| A | 9 + 8 + 7 + ... + 2 + 1 = 45 |
| B | 9! = 362.880 |
| C | 9 |
| D | 9 x 9 = 81 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 9, maka banyak korespondensi adalah 9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362.880.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c9bb66f91efd31e2202f2b9d3c568e8d3b29344f56613ee64d4c377d5abc8d6b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2097 |
| 2 | success | valid / verified | applying | procedural | Medium | 2080 |
| 3 | success | valid / verified | applying | procedural | Medium | 2069 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 9, maka banyak korespondensi adalah 9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362.880.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep korespondensi satu-satu dan menerapkan rumus faktorial (n!) untuk menentukan banyaknya pemetaan yang mungkin. Ini adalah penerapan prosedur yang sudah dipelajari dalam materi fungsi/relasi.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 9
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang korespondensi satu-satu dan prosedur perhitungan faktorial yang terkait dengan materi himpunan dan fungsi.. Bukti: korespondensi satu-satu; n(A) = n(B) = 9
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus memahami konsep korespondensi satu-satu dan memilih prosedur faktorial yang tepat, bukan sekadar menjumlahkan atau mengalikan dua angka yang diberikan.. Bukti: n(A) = n(B) = 9

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan, fungsi, dan konsep korespondensi satu-satu. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu adalah bagian dari kurikulum kelas 8. Menghitung faktorial 9! memerlukan ketelitian namun prosedurnya standar bagi siswa yang memahami konsep pemetaan. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 9, maka 9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362.880.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep faktorial sebagai prosedur untuk menghitung banyaknya korespondensi satu-satu antara dua himpunan yang memiliki jumlah anggota yang sama.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 9?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus faktorial untuk menentukan banyaknya korespondensi satu-satu.. Bukti: korespondensi satu-satu; n(A) = n(B) = 9
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus memahami konsep korespondensi satu-satu dan memilih prosedur faktorial (n!) yang tepat, bukan sekadar operasi penjumlahan atau perkalian biasa.. Bukti: n(A) = n(B) = 9

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep korespondensi satu-satu. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu adalah bagian dari kurikulum kelas 8. Menghitung faktorial 9 adalah prosedur rutin namun memerlukan pemilihan rumus yang tepat agar tidak terjebak pada distractor penjumlahan atau perkalian sederhana. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 9, maka banyak korespondensi satu-satu adalah 9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362.880.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep faktorial untuk menghitung banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 9
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar korespondensi satu-satu dan prosedur perhitungan faktorial.. Bukti: korespondensi satu-satu; n(A) = n(B) = 9
- Intended difficulty `classify/Medium`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Prosedurnya langsung menggunakan rumus n!, namun memerlukan ketelitian dalam perhitungan faktorial.. Bukti: n(A) = n(B) = 9

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep korespondensi satu-satu dan operasi faktorial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu adalah bagian dari kurikulum SMP kelas 8. Menghitung 9! adalah prosedur rutin namun memiliki beban hitung yang cukup untuk tingkat SMP. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3713`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan rumus faktorial (n!) untuk menentukan banyaknya korespondensi satu-satu antara dua himpunan dengan jumlah anggota yang sama. Ini adalah penerapan prosedur standar dalam materi fungsi/relasi.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus faktorial untuk menghitung banyaknya korespondensi satu-satu.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena siswa harus memilih prosedur yang tepat (faktorial) di antara distractor yang masuk akal (penjumlahan atau perkalian sederhana). Meskipun prosedurnya rutin, beban perhitungan faktorial 9! cukup signifikan untuk tingkat SMP.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep korespondensi satu-satu dan operasi faktorial. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu adalah bagian dari kurikulum SMP kelas 8. Menghitung 9! adalah prosedur rutin namun memerlukan ketelitian dan pemilihan rumus yang tepat agar tidak terjebak pada distractor. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Korespondensi Satu-satu (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? b. n(A) = n(B) = 9

Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 9?
Pilihan: A. 9 + 8 + 7 + ... + 2 + 1 = 45
B. 9! = 362.880
C. 9
D. 9 x 9 = 81
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `4facb7c0ab4ee644d3112751`

Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

| Opsi | Isi |
|---|---|
| A | $y^2 + x^2 = 25$ |
| B | $x^2 + 3y = 7$ |
| C | $x + 2y = 0$ |
| D | $\frac{y}{3x} + 3x = 9$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Persamaan garis lurus (linear) dalam dua variabel x dan y memiliki bentuk umum ax + by + c = 0, di mana pangkat tertinggi dari variabel adalah 1. Opsi A memiliki x^2 dan y^2 (lingkaran), opsi B memiliki x^2 (parabola), dan opsi D memiliki variabel di penyebut (non-linear). Opsi C, x + 2y = 0, memenuhi bentuk linear ax + by + c = 0 dengan a=1, b=2, c=0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `417eb413f4b03d19e84cb9f2414689f8111440158003fcaff7d95da6f58cf6b0`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1995 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1986 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1970 |

Run 1 — solusi: Persamaan garis lurus (linear) dalam dua variabel x dan y memiliki bentuk umum ax + by + c = 0, di mana pangkat tertinggi dari variabel adalah 1. Opsi A memiliki x^2 dan y^2 (lingkaran), opsi B memiliki x^2 (parabola), dan opsi D memiliki variabel di penyebut (non-linear). Opsi C, x + 2y = 0, memenuhi bentuk linear ax + by + c = 0 dengan a=1, b=2, c=0.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali karakteristik bentuk persamaan linear dua variabel (pangkat variabel harus 1) dan membedakannya dari bentuk non-linear (kuadrat atau variabel di penyebut). Ini adalah proses pengenalan konsep dasar.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa mengenai definisi dan bentuk umum persamaan garis lurus (konsep linearitas).. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman dasar tentang definisi persamaan linear. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum persamaan linear dua variabel (ax + by + c = 0). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan dasar dari topik persamaan garis lurus di kelas 8. Siswa diharapkan mampu mengidentifikasi bentuk linear secara langsung. |

Run 2 — solusi: Persamaan garis lurus (linear) dalam dua variabel x dan y memiliki bentuk umum ax + by + c = 0, di mana pangkat tertinggi dari variabel adalah 1. Opsi A memiliki x^2 dan y^2 (lingkaran), opsi B memiliki x^2 (parabola), dan opsi D memiliki variabel di penyebut (non-linear). Opsi C, x + 2y = 0, memenuhi bentuk linear ax + by + c = 0 dengan a=1, b=2, c=0.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali karakteristik bentuk persamaan linear (pangkat variabel adalah 1) dan membedakannya dari bentuk non-linear (kuadrat atau variabel di penyebut). Ini adalah proses pengenalan konsep dasar.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap definisi atau prinsip dasar persamaan garis lurus dibandingkan dengan bentuk persamaan lainnya.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman dasar tentang definisi persamaan linear. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum persamaan linear ax + by + c = 0. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari persamaan garis lurus dan bentuk umumnya. Mengidentifikasi bentuk linear adalah kompetensi dasar. |

Run 3 — solusi: Persamaan garis lurus (linear) dalam dua variabel memiliki bentuk umum ax + by + c = 0, di mana variabel x dan y berpangkat satu. Opsi A memiliki pangkat dua (lingkaran), opsi B memiliki x pangkat dua (parabola), dan opsi D memiliki variabel di penyebut (non-linear). Opsi C, x + 2y = 0, memenuhi syarat linear dengan pangkat variabel adalah satu.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali karakteristik persamaan linear (variabel berpangkat satu) dan membedakannya dari bentuk non-linear (pangkat dua, variabel di penyebut). Ini adalah proses pengenalan konsep dasar.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan bentuk umum persamaan garis lurus (konsep linearitas).. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan identifikasi bentuk persamaan tanpa perhitungan kompleks.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum persamaan linear dua variabel (ax + by + c = 0). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 yang baru mempelajari persamaan garis lurus, di mana pengenalan bentuk persamaan adalah langkah awal yang rutin. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Grafik Persamaan Garis Lurus
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
Pilihan: A. $y^2 + x^2 = 25$
B. $x^2 + 3y = 7$
C. $x + 2y = 0$
D. $\frac{y}{3x} + 3x = 9$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `0ca950fcf46ff904f0263642`

Hargai bahwa setiap titik pada garis harus memenuhi persamaan yang sesuai dan digunakan untuk menentukan nilai y dari nilai x, atau sebaliknya. Sehingga, apabila suatu garis lurus persamaannya adalah y = 2 x - 3.<br><br>Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.

| Opsi | Isi |
|---|---|
| A | x = 3,5 (atau 7/2) |
| B | x = 5 |
| C | x = 2 |
| D | x = 0,5 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Substitusi y = 4 ke dalam persamaan y = 2x - 3 menghasilkan 4 = 2x - 3. Tambahkan 3 ke kedua sisi: 7 = 2x. Bagi dengan 2: x = 3,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f6e21f5f159a94c28beea460b2789b8e8014d88040c9befd7a9e1196765826c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2014 |
| 2 | success | valid / verified | applying | procedural | Easy | 1995 |
| 3 | success | valid / verified | applying | procedural | Easy | 1973 |

Run 1 — solusi: Substitusi y = 4 ke dalam persamaan y = 2x - 3 menghasilkan 4 = 2x - 3. Tambahkan 3 ke kedua sisi: 7 = 2x. Bagi dengan 2: x = 3,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur substitusi nilai yang diketahui ke dalam persamaan linear satu variabel untuk mencari nilai variabel lainnya. Ini adalah penerapan langsung dari konsep persamaan garis lurus.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4, maka carilah koordinat x dari p
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana koordinat titik (x, y) berinteraksi dengan persamaan linear, yang merupakan algoritma standar dalam aljabar.. Bukti: setiap titik pada garis harus memenuhi persamaan yang sesuai
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan substitusi satu variabel dan menyelesaikan persamaan linear satu variabel sederhana (dua langkah aljabar). Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang substitusi variabel dan penyelesaian persamaan linear satu variabel (PLSV). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi persamaan garis lurus adalah kurikulum standar kelas 8. Soal ini menguji kemampuan dasar manipulasi aljabar yang diharapkan sudah dikuasai. |

Run 2 — solusi: Substitusi y = 4 ke dalam persamaan y = 2x - 3 menghasilkan 4 = 2x - 3. Tambahkan 3 pada kedua ruas menjadi 7 = 2x, sehingga x = 7/2 atau 3,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur substitusi nilai yang diketahui ke dalam persamaan linear satu variabel untuk mencari nilai variabel lainnya. Ini adalah penerapan langsung dari konsep persamaan garis lurus.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4, maka carilah koordinat x dari p
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menyelesaikan persamaan linear satu variabel setelah melakukan substitusi nilai pada persamaan garis.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan substitusi dan operasi aljabar dasar (penjumlahan dan pembagian) untuk menemukan nilai x. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan linear satu variabel dan substitusi nilai ke dalam variabel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena merupakan aplikasi langsung dari materi persamaan garis lurus yang dipelajari pada jenjang tersebut. |

Run 3 — solusi: Substitusi y = 4 ke dalam persamaan y = 2x - 3 menghasilkan 4 = 2x - 3. Tambahkan 3 pada kedua sisi: 7 = 2x. Bagi dengan 2: x = 3,5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur substitusi nilai yang diketahui ke dalam persamaan linear satu variabel dan melakukan manipulasi aljabar dasar untuk menemukan nilai variabel lainnya.. Bukti: Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menyelesaikan persamaan linear satu variabel setelah melakukan substitusi nilai ke dalam rumus fungsi linear.. Bukti: y = 2 x - 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Hanya memerlukan satu langkah substitusi dan penyelesaian persamaan linear satu variabel sederhana tanpa kendala kompleks.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan linear satu variabel dan konsep substitusi nilai ke dalam persamaan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi persamaan garis lurus adalah kurikulum standar kelas 8. Prosedur yang diminta adalah operasi aljabar dasar yang sudah dipelajari. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Grafik Persamaan Garis Lurus
Tipe soal: multiple_choice
Stimulus: -
Soal: Hargai bahwa setiap titik pada garis harus memenuhi persamaan yang sesuai dan digunakan untuk menentukan nilai y dari nilai x, atau sebaliknya. Sehingga, apabila suatu garis lurus persamaannya adalah y = 2 x - 3.

Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.
Pilihan: A. x = 3,5 (atau 7/2)
B. x = 5
C. x = 2
D. x = 0,5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `6d6cb72cedbdc46857aa2701`

Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....

| Opsi | Isi |
|---|---|
| A | 3x + 4y - 14 = 0 |
| B | 4x - 3y + 14 = 0 |
| C | 3x - 4y + 33 = 0 |
| D | 4x + 3y - 14 = 0 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Karena sisi persegi panjang sejajar sumbu koordinat, titik P(2,-1) dan R(6,2) menentukan titik Q(6,-1) dan S(2,2). Gradien garis QS (m) = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4: y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2a00e663bb341428f40c1f4e9ea23103609a3e29680041d5ae09c17a3c94abf7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2159 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2144 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2169 |

Run 1 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik P(2,-1) dan R(6,2) menentukan titik Q(6,-1) dan S(2,2). Gradien garis QS (m) = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4: y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus gradien dan persamaan garis lurus.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang geometri koordinat (sifat persegi panjang) dan prosedur aljabar untuk menentukan persamaan garis.. Bukti: titik sudut yang berhadapan; sejajar dengan sumbu-sumbu koordinat; persamaan garis
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman geometri dasar untuk menentukan koordinat titik lain, diikuti oleh prosedur standar mencari persamaan garis. Ini adalah tugas rutin yang melibatkan beberapa langkah terkait.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan; sejajar dengan sumbu-sumbu koordinat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, sifat persegi panjang, rumus gradien, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8, mengintegrasikan konsep geometri koordinat yang dipelajari di bab persamaan garis lurus. |

Run 2 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S adalah (6,-1) dan (2,2). Kemiringan m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4: y - 2 = -3/4(x - 2) -> 4y - 8 = -3x + 6 -> 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat geometri persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus kemiringan dan persamaan garis.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara sifat geometri (persegi panjang sejajar sumbu) dengan koordinat kartesius, serta prosedur aljabar untuk menentukan persamaan garis.. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep geometri koordinat untuk menentukan koordinat titik Q dan S, diikuti oleh prosedur rutin mencari persamaan garis. Ini adalah langkah-langkah rutin yang saling terkait.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan; sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, konsep kemiringan garis, dan sifat persegi panjang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena mengintegrasikan geometri koordinat dan aljabar linear dasar. |

Run 3 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S adalah (6, -1) dan (2, 2). Kemiringan (m) garis QS = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2, 2) dengan m = -3/4: y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus kemiringan dan persamaan garis. Ini adalah penerapan prosedur rutin dalam geometri koordinat.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara sifat geometris persegi panjang (sisi sejajar sumbu) dengan koordinat titik, serta prosedur aljabar untuk menyusun persamaan garis.. Bukti: titik sudut yang berhadapan; sejajar dengan sumbu-sumbu koordinat; persamaan garis
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang properti persegi panjang untuk menentukan koordinat titik Q dan S (inferensi logis), diikuti oleh perhitungan kemiringan dan persamaan garis. Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: Titik P(2,-1) dan R(6,2); sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, konsep kemiringan garis, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena mengintegrasikan konsep geometri koordinat yang dipelajari pada bab persamaan garis lurus. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Pengertian Kemiringan
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....
Pilihan: A. 3x + 4y - 14 = 0
B. 4x - 3y + 14 = 0
C. 3x - 4y + 33 = 0
D. 4x + 3y - 14 = 0
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `d5711f5a3f145c11f3394792`

Diagram berikut menunjukkan suatu tangga pada rumah tertentu, terdapat 14 anak tangga dengan tinggi 252 cm. Total Height 252 cm. Total Depth 400 cm.<br><br>Total tinggi untuk setiap pijakan dari 14 pijakan adalah.....

| Opsi | Isi |
|---|---|
| A | 18 cm |
| B | 14 cm |
| C | 28 cm |
| D | 36 cm |

![Gambar sumber soal 37](<../../../images/kelas8_crop-p0045-persamaan-garis-lurus.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Tinggi setiap anak tangga = Total Height / jumlah anak tangga = 252 cm / 14 = 18 cm.
Gambar sumber: images/kelas8_crop-p0045-persamaan-garis-lurus.png. Transkripsi visual: Diagram menunjukkan profil samping tangga dengan 14 anak tangga. Terdapat label 'Total Height 252 cm' pada sisi vertikal kanan dan 'Total Depth 400 cm' pada sisi horizontal bawah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `170c704eff34e359339670a8db426fb25b69eca837283ef0d4580ce7f8472511`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3038 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3030 |
| 3 | success | valid / verified | applying | procedural | Easy | 3062 |

Run 1 — solusi: Tinggi setiap anak tangga = Total Height / jumlah anak tangga = 252 cm / 14 = 18 cm.
- Domain kognitif `classify/applying`: Siswa hanya perlu mengidentifikasi informasi yang relevan (total tinggi dan jumlah anak tangga) dan menerapkan operasi pembagian dasar untuk menemukan tinggi per anak tangga.. Bukti: Total Height 252 cm; 14 anak tangga; tinggi untuk setiap pijakan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang pembagian untuk menentukan nilai satuan (unit rate) dalam konteks fisik.. Bukti: tinggi untuk setiap pijakan dari 14 pijakan
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan satu operasi pembagian sederhana. Informasi 'Total Depth 400 cm' berfungsi sebagai distraktor yang tidak relevan untuk menghitung tinggi anak tangga.. Bukti: 14 anak tangga; Total Height 252 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan pembagian dasar dan memilah informasi yang relevan dari soal cerita sederhana. |

Run 2 — solusi: Tinggi setiap anak tangga = Total Height / jumlah anak tangga = 252 cm / 14 = 18 cm.
- Domain kognitif `classify/applying`: Siswa hanya perlu mengidentifikasi informasi yang relevan (total tinggi dan jumlah anak tangga) dan menerapkan operasi pembagian dasar untuk menemukan tinggi per pijakan.. Bukti: Total Height 252 cm; 14 anak tangga; tinggi untuk setiap pijakan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pembagian rata-rata tinggi total ke dalam jumlah langkah yang sama.. Bukti: Total Height 252 cm; 14 anak tangga
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu operasi pembagian sederhana tanpa perlu memproses informasi 'Total Depth' yang merupakan distraktor.. Bukti: 14 anak tangga; Total Height 252 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah sangat familiar dengan operasi aritmatika dasar dan interpretasi diagram sederhana. |

Run 3 — solusi: Tinggi setiap anak tangga = Total Height / Jumlah anak tangga = 252 cm / 14 = 18 cm.
- Domain kognitif `classify/applying`: Siswa hanya perlu mengidentifikasi informasi yang relevan (total tinggi dan jumlah anak tangga) dan menerapkan operasi pembagian dasar untuk menemukan tinggi per anak tangga.. Bukti: Total Height 252 cm; 14 anak tangga; tinggi untuk setiap pijakan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang pembagian untuk menentukan nilai satuan (unit rate) dalam konteks fisik.. Bukti: tinggi untuk setiap pijakan; 252 cm dibagi 14 anak tangga
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu memilih data yang relevan (tinggi total) dan membaginya dengan jumlah anak tangga. Informasi 'Total Depth' berfungsi sebagai distraktor.. Bukti: 14 anak tangga dengan tinggi 252 cm; Total Height 252 cm; Total Depth 400 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi aritmatika dasar dan memilih informasi yang relevan dari soal cerita sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4298`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi informasi yang relevan (total tinggi dan jumlah anak tangga) dan menerapkan operasi pembagian dasar untuk menemukan tinggi per anak tangga.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang pembagian untuk menentukan nilai satuan (unit rate) dalam konteks fisik.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu operasi pembagian sederhana tanpa perlu memproses informasi 'Total Depth' yang merupakan distraktor.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan pembagian dasar dan memilah informasi yang relevan dari soal cerita sederhana. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Pengertian Kemiringan
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram berikut menunjukkan suatu tangga pada rumah tertentu, terdapat 14 anak tangga dengan tinggi 252 cm. Total Height 252 cm. Total Depth 400 cm.

Total tinggi untuk setiap pijakan dari 14 pijakan adalah.....
Pilihan: A. 18 cm
B. 14 cm
C. 28 cm
D. 36 cm
Transkripsi visual: Diagram menunjukkan profil samping tangga dengan 14 anak tangga. Terdapat label 'Total Height 252 cm' pada sisi vertikal kanan dan 'Total Depth 400 cm' pada sisi horizontal bawah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `bc70cacaad85275414d879e3`

Rata-rata tinggi 12 anak adalah 166 cm. Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm. Berapa rata-rata tinggi 6 anak?

| Opsi | Isi |
|---|---|
| A | 169 cm |
| B | 166,5 cm |
| C | 84,5 cm |
| D | 167 cm |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total tinggi 12 anak = 12 * 166 = 1992. Total tinggi 18 anak = 18 * 167 = 3006. Total tinggi 6 anak baru = 3006 - 1992 = 1014. Rata-rata 6 anak baru = 1014 / 6 = 169 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2e31adfe41e140626bc7b31925a74f5c98327c7a90c9d6678d1a8492557bf9ed`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2110 |
| 2 | success | valid / verified | applying | procedural | Medium | 2126 |
| 3 | success | valid / verified | applying | procedural | Medium | 2122 |

Run 1 — solusi: Total tinggi 12 anak = 12 * 166 = 1992. Total tinggi 18 anak = 18 * 167 = 3006. Total tinggi 6 anak baru = 3006 - 1992 = 1014. Rata-rata 6 anak baru = 1014 / 6 = 169 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata gabungan dan melakukan manipulasi aljabar sederhana untuk menemukan nilai yang hilang. Ini adalah penerapan prosedur rata-rata pada situasi rutin.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm; Berapa rata-rata tinggi 6 anak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung rata-rata dari sekumpulan data yang dimodifikasi (penambahan data).. Bukti: Rata-rata tinggi 12 anak adalah 166 cm; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah rutin (menghitung total awal dan total akhir) dan satu operasi pembagian. Prosedur ini sangat familiar bagi siswa kelas 8.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar rata-rata (mean) dan operasi aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan standar untuk materi rata-rata di kelas 8, menggunakan angka yang dapat dihitung dengan prosedur rutin. |

Run 2 — solusi: Total tinggi 12 anak = 12 * 166 = 1992. Total tinggi 18 anak = 18 * 167 = 3006. Total tinggi 6 anak baru = 3006 - 1992 = 1014. Rata-rata 6 anak baru = 1014 / 6 = 169 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep rata-rata gabungan dan melakukan manipulasi aljabar sederhana untuk menemukan nilai yang hilang dari kelompok data baru. Ini adalah penerapan prosedur rata-rata pada situasi rutin.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.; Berapa rata-rata tinggi 6 anak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung rata-rata dari total data yang diberikan dalam dua kelompok.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.
- Intended difficulty `classify/Medium`: Soal ini melibatkan langkah-langkah rutin (perkalian dan pengurangan) untuk mencari selisih total, yang merupakan prosedur standar untuk masalah rata-rata gabungan di kelas 8.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep rata-rata (mean) dan operasi hitung dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah rata-rata gabungan adalah materi standar kelas 8. Tingkat kesulitan sedang karena memerlukan beberapa langkah perhitungan (total lama, total baru, selisih, rata-rata baru) namun prosedurnya sangat familiar. |

Run 3 — solusi: Total tinggi 12 anak = 12 * 166 = 1992 cm. Total tinggi 18 anak = 18 * 167 = 3006 cm. Total tinggi 6 anak tambahan = 3006 - 1992 = 1014 cm. Rata-rata 6 anak = 1014 / 6 = 169 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata gabungan dan melakukan manipulasi aljabar sederhana untuk menemukan nilai yang hilang dari kelompok data tambahan. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.; Berapa rata-rata tinggi 6 anak?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma perhitungan rata-rata (prosedural) untuk menyelesaikan masalah yang melibatkan hubungan antar kelompok data (konseptual).. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah rutin (menghitung total awal dan total akhir) dan satu operasi pembagian untuk mendapatkan hasil. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep rata-rata hitung dan operasi perkalian/pembagian dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan konsep rata-rata dan operasi hitung yang diperlukan. Soal ini menguji pemahaman tentang total data, bukan sekadar rata-rata langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3879`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep rata-rata gabungan dan melakukan manipulasi aljabar sederhana untuk menemukan nilai yang hilang dari kelompok data baru. Ini adalah penerapan prosedur rata-rata pada situasi rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung rata-rata dari total data yang diberikan dalam dua kelompok.
- Intended difficulty `Medium`: Soal ini melibatkan langkah-langkah rutin (perkalian dan pengurangan) untuk mencari selisih total, yang merupakan prosedur standar untuk masalah rata-rata gabungan di kelas 8.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep rata-rata (mean) dan operasi hitung dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah rata-rata gabungan adalah materi standar kelas 8. Tingkat kesulitan sedang karena memerlukan beberapa langkah perhitungan (total lama, total baru, selisih, rata-rata baru) namun prosedurnya sangat familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Pemusatan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Rata-rata tinggi 12 anak adalah 166 cm. Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm. Berapa rata-rata tinggi 6 anak?
Pilihan: A. 169 cm
B. 166,5 cm
C. 84,5 cm
D. 167 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `962364d9c3511c0598f13509`

Rata-rata berat badan 9 anak adalah 56 kg, jika berat badan Domi dimasukkan dalam hitungan tersebut, rata-ratanya menjadi 56,7. Tentukan berat badan Doni.

| Opsi | Isi |
|---|---|
| A | 7 kg |
| B | 63 kg |
| C | 56,7 kg |
| D | 6,3 kg |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak = 10 * 56,7 = 567 kg. Berat anak ke-10 = 567 - 504 = 63 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3d670c046d94fab01fe00e814329d7436a627e625c83ad500dc0835d1662fa20`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2097 |
| 2 | success | valid / verified | applying | procedural | Medium | 2105 |
| 3 | success | valid / verified | applying | procedural | Medium | 2087 |

Run 1 — solusi: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak = 10 * 56,7 = 567 kg. Berat anak ke-10 = 567 - 504 = 63 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata (mean) untuk mencari total nilai dari rata-rata yang diketahui, kemudian mencari selisih antara dua kondisi (sebelum dan sesudah penambahan data). Ini adalah penerapan prosedur rutin.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7; Tentukan berat badan Doni
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau prosedur standar untuk menghitung rata-rata dan mencari nilai data yang ditambahkan.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah rutin (menghitung total awal dan total akhir) dan satu operasi pengurangan. Prosedur ini sangat familiar bagi siswa kelas 8.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar rata-rata (mean) dan operasi hitung bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar kompetensi kelas 8 terkait pemusatan data. Tingkat kesulitan Medium diberikan karena melibatkan dua langkah perhitungan (total awal dan total akhir) yang saling terkait, bukan sekadar satu operasi langsung. |

Run 2 — solusi: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak = 10 * 56,7 = 567 kg. Berat anak tambahan = 567 - 504 = 63 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata untuk mencari total nilai dari data yang ada, kemudian menggunakan selisih total nilai untuk menemukan nilai data yang ditambahkan. Ini adalah prosedur standar dalam pemecahan masalah rata-rata.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7; Tentukan berat badan Doni
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma rata-rata (mean) untuk menyelesaikan masalah yang melibatkan perubahan jumlah data.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah rutin (menghitung total awal dan total baru) dan satu operasi pengurangan. Prosedur ini familiar bagi siswa kelas 8.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep rata-rata (mean) dan operasi perkalian/pengurangan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi standar dari konsep rata-rata yang diajarkan di kelas 8. Tingkat kesulitan Medium diberikan karena siswa harus melakukan dua perhitungan total yang saling terkait sebelum mendapatkan jawaban akhir. |

Run 3 — solusi: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak = 10 * 56,7 = 567 kg. Berat anak ke-10 = 567 - 504 = 63 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata (mean) untuk mencari total nilai dari rata-rata yang diketahui, kemudian mencari selisih antara dua kondisi (sebelum dan sesudah penambahan data). Ini adalah prosedur standar dalam pemusatan data.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; jika berat badan Domi dimasukkan dalam hitungan tersebut, rata-ratanya menjadi 56,7
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana rata-rata dihitung dan bagaimana memanipulasi rumus rata-rata untuk menemukan nilai data yang hilang.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7
- Intended difficulty `classify/Medium`: Soal ini melibatkan langkah rutin: menghitung total awal, menghitung total baru, dan mencari selisih. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar rata-rata (mean) dan operasi perkalian/pengurangan bilangan desimal. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan manipulasi rata-rata yang merupakan materi standar, dengan beban hitung yang wajar. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Pemusatan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Rata-rata berat badan 9 anak adalah 56 kg, jika berat badan Domi dimasukkan dalam hitungan tersebut, rata-ratanya menjadi 56,7. Tentukan berat badan Doni.
Pilihan: A. 7 kg
B. 63 kg
C. 56,7 kg
D. 6,3 kg
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: Terdapat ketidakkonsistenan penulisan nama antara 'Domi' pada kalimat soal dan 'Doni' pada pertanyaan akhir serta catatan opsi. Namun, hal ini tidak memengaruhi prosedur matematis penyelesaian.; Terdapat ketidakkonsistenan penulisan nama antara 'Domi' pada kalimat soal dan 'Doni' pada pertanyaan akhir dan catatan opsi. Namun, secara matematis hal ini tidak memengaruhi penyelesaian soal.; Terdapat ketidakkonsistenan nama subjek dalam soal (Domi vs Doni), namun tidak mengganggu pemahaman prosedur matematis..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |
| B | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| C | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Data terurut (n=14): 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Q1 (kuartil bawah) adalah median dari 7 data pertama (50, 50, 60, 65, 65, 65, 65), yaitu 65. Q3 (kuartil atas) adalah median dari 7 data terakhir (70, 75, 80, 80, 85, 85, 90), yaitu 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * IQR = 7,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe6dca80972658e481681f169b408b6e2fc90a5d0ba904e7354418f65e22d5fd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2421 |
| 2 | success | valid / verified | applying | procedural | Medium | 2434 |
| 3 | success | valid / verified | applying | procedural | Medium | 2488 |

Run 1 — solusi: Data terurut (n=14): 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Q1 (kuartil bawah) adalah median dari 7 data pertama (50, 50, 60, 65, 65, 65, 65), yaitu 65. Q3 (kuartil atas) adalah median dari 7 data terakhir (70, 75, 80, 80, 85, 85, 90), yaitu 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik untuk menentukan ukuran penyebaran data (kuartil dan simpangan kuartil) dari sekumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau langkah-langkah sistematis dalam menghitung statistik deskriptif (kuartil dan simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data (14 data) dan penerapan rumus kuartil yang rutin. Beban perhitungan moderat karena jumlah data cukup banyak, namun prosedurnya standar.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data, menentukan median, memahami definisi kuartil. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8, menguji ketelitian dalam pengurutan dan penerapan rumus statistik dasar. |

Run 2 — solusi: Data terurut (n=14): 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90. Q1 (median 7 data pertama) = 65. Q3 (median 7 data terakhir) = 80. Q2 (median data) = (65+70)/2 = 67,5. Jangkauan kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik untuk menentukan ukuran penyebaran data (kuartil, jangkauan, simpangan kuartil) pada sekumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan teknik statistik untuk menghitung ukuran penyebaran data.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data (14 data) dan penerapan rumus kuartil yang rutin. Beban kalkulasi moderat karena jumlah data cukup banyak namun angkanya sederhana.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data, menentukan median, memahami definisi kuartil dan jangkauan kuartil. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8, menguji ketelitian dalam mengurutkan data dan menerapkan rumus statistik dasar. |

Run 3 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q1 (kuartil bawah) adalah median dari 7 data pertama (50, 50, 60, 65, 65, 65, 65), yaitu 65. Q3 (kuartil atas) adalah median dari 7 data terakhir (70, 75, 80, 80, 85, 85, 90), yaitu 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * IQR = 0,5 * 15 = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar statistik (mengurutkan data, mencari median untuk kuartil, menghitung jangkauan dan simpangan kuartil) pada sekumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan teknik statistik untuk mengolah data, yang termasuk dalam dimensi pengetahuan prosedural.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data (14 data) dan penerapan rumus kuartil. Ini adalah tugas rutin yang melibatkan beberapa langkah berurutan namun tidak memerlukan strategi non-rutin.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

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
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan pengolahan data statistik dasar dengan jumlah data yang cukup untuk melatih ketelitian. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Penyebaran Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65
Pilihan: A. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15
B. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
C. Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
D. Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `2638edf211f383d8d9b95e05`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

| Opsi | Isi |
|---|---|
| A | Q1 = 7,5; Q2 = 6; Q3 = 4; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| B | Q1 = 4; Q2 = 5,83; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| C | Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| D | Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 3,5 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9 (n=12). Median (Q2) = (6+6)/2 = 6. Q1 (median 6 data pertama: 3, 4, 4, 4, 5, 6) = (4+4)/2 = 4. Q3 (median 6 data terakhir: 6, 7, 8, 8, 8, 9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 1,75.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `667a6240de4f388eb1d8987e5ec28998b6df2adcdffcf193124072c4e0ff03d2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2326 |
| 2 | success | valid / verified | applying | procedural | Medium | 2393 |
| 3 | success | valid / verified | applying | procedural | Medium | 2340 |

Run 1 — solusi: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9 (n=12). Median (Q2) = (6+6)/2 = 6. Q1 (median 6 data pertama: 3, 4, 4, 4, 5, 6) = (4+4)/2 = 4. Q3 (median 6 data terakhir: 6, 7, 8, 8, 8, 9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 1,75.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar (mencari kuartil dan simpangan kuartil) pada sekumpulan data yang diberikan. Ini adalah penerapan prosedur rutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan teknik statistik untuk mengolah data (kuartil, jangkauan, simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data dan penerapan rumus kuartil yang rutin. Tidak ada jebakan konseptual yang kompleks, hanya ketelitian dalam perhitungan.. Bukti: 3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan data dan menghitung median data genap. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 12 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 8, melibatkan pengolahan data statistik dasar dengan jumlah data yang cukup untuk melatih ketelitian. |

Run 2 — solusi: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9 (n=12). Median (Q2) = (6+6)/2 = 6. Q1 (median 6 data pertama: 3, 4, 4, 4, 5, 6) = (4+4)/2 = 4. Q3 (median 6 data terakhir: 6, 7, 8, 8, 8, 9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 1,75.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar (mengurutkan data, mencari median, Q1, Q3, dan menghitung simpangan kuartil) pada kumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan teknik perhitungan statistik deskriptif (kuartil dan simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data dan perhitungan berjenjang (Q1, Q2, Q3, IQR, simpangan kuartil). Ini adalah prosedur rutin yang melibatkan beberapa langkah terkait, sesuai untuk tingkat kesulitan menengah.. Bukti: 3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data, memahami konsep median, dan rumus kuartil. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 12 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengolah data statistik sederhana. Soal ini menguji ketelitian dalam langkah-langkah prosedural statistik. |

Run 3 — solusi: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9 (n=12). Median (Q2) = (6+6)/2 = 6. Q1 (median data bawah: 3, 4, 4, 4, 5, 6) = (4+4)/2 = 4. Q3 (median data atas: 6, 7, 8, 8, 8, 9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 1,75.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar untuk mencari kuartil dan simpangan kuartil pada data tunggal yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan prosedur perhitungan statistik deskriptif (kuartil dan simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data dan penerapan rumus kuartil yang rutin. Tidak ada jebakan konseptual yang kompleks, hanya ketelitian dalam perhitungan.. Bukti: 3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data, menentukan median data genap. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 12 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 8, melibatkan data tunggal dengan jumlah genap yang memerlukan rata-rata dua nilai tengah. |

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
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Penyebaran Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6
Pilihan: A. Q1 = 7,5; Q2 = 6; Q3 = 4; jangkauan kuartil = 3,5; simpangan kuartil = 1,75
B. Q1 = 4; Q2 = 5,83; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75
C. Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75
D. Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 3,5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `e8a6fabcd6f67b1be8f8ad7f`

Berikut data tingkat suku bunga deposito untuk jangka waktu 12 bulan di beberapa bank di Indonesia per tanggal 9 Maret 2022. Tingkat suku bunga selalu dinyatakan dalam persen.<br><br>Tabel 6.11 Tingkat Suku Bunga Deposito Jangka 12 Bulan<br><br>\| Nama Bank \| Tingkat Suku Bunga Deposito \|<br>\|---\|---\|<br>\| Bank Mandiri \| 2,50 % \|<br>\| BNI 1946 \| 2,50 % \|<br>\| BRI \| 2,50 % \|<br>\| BCA \| 1,90 % \|<br>\| Bank Maspion \| 4,75 % \|<br><br>Walaupun data di atas berbentuk persen, kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Mengapa demikian? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Karena suku bunga berupa bilangan desimal yang tidak dapat diubah menjadi sudut |
| B | Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan (jumlahnya tidak 100%) |
| C | Karena beberapa bank memiliki suku bunga yang sama sehingga juringnya bertumpuk |
| D | Karena banyaknya bank lebih dari 4 sehingga lingkaran tidak dapat dibagi |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Diagram lingkaran (pie chart) digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Data suku bunga deposito pada tabel adalah nilai persentase masing-masing bank yang berdiri sendiri, bukan bagian dari satu kesatuan total 100%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `19261af372960cd079eb1a3d8e72c111c50e2139e31309c7dffc21dd7a430a9b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2068 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2076 |
| 3 | success | valid / verified | reasoning | conceptual | Easy | 2031 |

Run 1 — solusi: Diagram lingkaran digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito pada tabel adalah nilai persentase individu per bank, bukan bagian dari satu kesatuan yang jika dijumlahkan bernilai 100%. Total suku bunga (2,5+2,5+2,5+1,9+4,75) = 14,15%, bukan 100%.
- Domain kognitif `classify/applying`: Soal menuntut pemahaman konseptual tentang syarat penggunaan diagram lingkaran (bagian dari keseluruhan 100%). Siswa harus menganalisis sifat data dan mencocokkannya dengan karakteristik diagram, yang termasuk dalam domain applying.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip atau aturan penggunaan representasi data (diagram lingkaran), yang merupakan pengetahuan konseptual.. Bukti: diagram lingkaran untuk merepresentasikan data
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menguji pemahaman dasar tentang syarat penggunaan diagram lingkaran yang merupakan materi standar kelas 8. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: Mengapa demikian? Jelaskan.; persen suku bunga tiap bank bukan bagian dari satu keseluruhan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram lingkaran dan konsep persentase sebagai bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan memahami kapan diagram lingkaran tepat digunakan. Soal ini menguji pemahaman konseptual dasar tanpa beban komputasi yang berat. |

Run 2 — solusi: Diagram lingkaran (pie chart) digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Data suku bunga deposito pada tabel adalah nilai persentase masing-masing bank yang berdiri sendiri, bukan bagian dari satu kesatuan total 100%. Oleh karena itu, diagram lingkaran tidak tepat digunakan.
- Domain kognitif `classify/reasoning`: Soal menuntut pemahaman konseptual tentang syarat penggunaan diagram lingkaran, yaitu data harus merupakan bagian dari satu keseluruhan (total 100%). Siswa perlu menganalisis sifat data untuk menentukan kesesuaian representasi.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman prinsip dasar (konsep) mengenai kapan suatu diagram statistik (diagram lingkaran) dapat digunakan, bukan sekadar menghitung atau mengingat fakta.. Bukti: diagram lingkaran untuk merepresentasikan data di atas
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut pemahaman konseptual tentang syarat representasi data, bukan sekadar prosedur rutin. Siswa harus membedakan antara data persentase sebagai nilai absolut dan data persentase sebagai bagian dari keseluruhan.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran dan konsep persentase sebagai bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memilih diagram yang tepat untuk data statistik. Soal ini menguji pemahaman mendalam tentang syarat penggunaan diagram lingkaran yang sering disalahpahami. |

Run 3 — solusi: Diagram lingkaran merepresentasikan bagian dari satu kesatuan utuh (total 100%). Data suku bunga deposito pada tabel adalah nilai persentase masing-masing bank yang berdiri sendiri, bukan proporsi bagian dari total suku bunga (jumlahnya tidak 100%).
- Domain kognitif `classify/reasoning`: Soal menuntut pemahaman konseptual tentang syarat penggunaan diagram lingkaran (proporsi bagian terhadap keseluruhan). Siswa harus mengevaluasi apakah data tersebut membentuk satu kesatuan utuh, bukan sekadar melakukan perhitungan.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar representasi data (konsep diagram lingkaran) untuk menentukan ketidaksesuaian antara jenis data dengan alat visualisasi yang dipilih.. Bukti: diagram lingkaran untuk merepresentasikan data di atas
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan tidak memerlukan perhitungan rumit. Siswa hanya perlu memahami syarat penggunaan diagram lingkaran, yang merupakan materi standar kelas 8.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran sebagai representasi bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pemilihan diagram adalah topik standar kelas 8. Soal ini menguji pemahaman konsep dasar tanpa beban komputasi, sehingga tergolong mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "reasoning": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3511`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal menuntut pemahaman konseptual tentang syarat penggunaan diagram lingkaran (proporsi bagian terhadap keseluruhan). Siswa harus mengevaluasi apakah data tersebut membentuk satu kesatuan utuh, yang merupakan proses penalaran konseptual.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman tentang prinsip atau aturan penggunaan representasi data (diagram lingkaran), yang merupakan pengetahuan konseptual.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena menguji pemahaman dasar tentang syarat penggunaan diagram lingkaran yang merupakan materi standar kelas 8. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran sebagai representasi bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pemilihan diagram adalah topik standar kelas 8. Soal ini menguji pemahaman konsep dasar tanpa beban komputasi, sehingga tergolong mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 8
Topik: Matematika SMP Kelas 8
Subtopik: Memilih Diagram yang Tepat
Tipe soal: multiple_choice
Stimulus: -
Soal: Berikut data tingkat suku bunga deposito untuk jangka waktu 12 bulan di beberapa bank di Indonesia per tanggal 9 Maret 2022. Tingkat suku bunga selalu dinyatakan dalam persen.

Tabel 6.11 Tingkat Suku Bunga Deposito Jangka 12 Bulan

| Nama Bank | Tingkat Suku Bunga Deposito |
|---|---|
| Bank Mandiri | 2,50 % |
| BNI 1946 | 2,50 % |
| BRI | 2,50 % |
| BCA | 1,90 % |
| Bank Maspion | 4,75 % |

Walaupun data di atas berbentuk persen, kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Mengapa demikian? Jelaskan.
Pilihan: A. Karena suku bunga berupa bilangan desimal yang tidak dapat diubah menjadi sudut
B. Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan (jumlahnya tidak 100%)
C. Karena beberapa bank memiliki suku bunga yang sama sehingga juringnya bertumpuk
D. Karena banyaknya bank lebih dari 4 sehingga lingkaran tidak dapat dibagi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
