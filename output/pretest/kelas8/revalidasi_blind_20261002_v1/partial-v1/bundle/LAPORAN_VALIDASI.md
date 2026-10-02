# Validasi ulang soal kelas 8 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 8/126 run awal sukses; 1 item masih memerlukan adjudikasi atau kelengkapan run. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v6-blind-smp8-key-verified`. Rubrik: `math-rubric-3x4x3-v4-smp8-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 8 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 8, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 2, "undecided": 40, "knowing": 0, "reasoning": 0}, "knowledgeDimension": {"conceptual": 2, "undecided": 40, "factual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 1, "Medium": 1, "undecided": 40, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 2, "knowing": 0, "reasoning": 0}, "knowledgeDimension": {"conceptual": 2, "factual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 1, "Medium": 1, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 2, "llm_retry_or_manual_review": 40}`.
Run awal sukses: 8/126; adjudikasi: 0; token sukses tercatat: 18,381.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 1 | 1 | [Easy.json](difficulty/Easy.json) |
| Medium | 1 | 1 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

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
| 3 | failed | — / — | — | — | — | 0 |

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

Run 3 gagal: `ClientError:429`; tidak dihitung sebagai suara.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2} | majority_2_of_3 / needs_adjudication | — |
| Dimensi pengetahuan | {"procedural": 2} | majority_2_of_3 / needs_adjudication | — |
| Intended difficulty | {"Easy": 2} | majority_2_of_3 / needs_adjudication | — |

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `8c189810bd620fa2b116eab9`

Coba buatlah dalam bentuk yang paling sederhana. $3\sqrt{2} + 5\sqrt{2}$

| Opsi | Isi |
|---|---|
| A | $8\sqrt{4}$ |
| B | $3\sqrt{2}$ |
| C | $15\sqrt{2}$ |
| D | $8\sqrt{2}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a3f4dbe76e3c578ca32c783e3386470dbbb435e8f038e52e81711d180f9f5bb8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `e97f2eaa7ee74e27d6bb517c`

Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

| Opsi | Isi |
|---|---|
| A | 3,4 × 10<sup>11</sup> |
| B | 3,4 × 10<sup>-10</sup> |
| C | 3,4 × 10<sup>10</sup> |
| D | 3,4 × 10<sup>9</sup> |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cc42bda9beef9c0e694a477ac215e38b33697d6f6861ac3551479a3af2c4414c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `f25d4029ecaafe78249ca72b`

Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10<sup>8</sup>

| Opsi | Isi |
|---|---|
| A | 2.500.000.000 |
| B | 25.000.000 |
| C | 0,000000025 |
| D | 250.000.000 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5c6a23bc41f795d6e4cde5f18558d2728db3712a8fdb576418be61937f51c06f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `ac7f560c796164a475dad657`

Indeks Massa Tubuh $= \dfrac{BB}{TB^2}$. BB: Berat badan (kg), TB: Tinggi badan (m).<br><br>**Tabel 2.12** Kategori Indeks Massa Tubuh<br><br>\|Kategori\|IMT\|<br>\|---\|---\|<br>\|Kekurangan berat badan tingkat berat\|Kurang dari 17,0\|<br>\|Kekurangan berat badan tingkat ringan\|17,0 sampai 18,4\|<br>\|Normal\|18,5 sampai 25,0\|<br>\|Kelebihan berat badan tingkat ringan\|25,1 sampai 27,0\|<br>\|Kelebihan berat badan tingkat berat\|Lebih dari 27,0\|<br><br>**Tabel 2.13** Data Berat dan Tinggi Badan<br><br>\|No\|Nama\|Berat Badan (kg)\|Tinggi Badan (m)\|<br>\|---\|---\|---\|---\|<br>\|1\|Pak Ananta\|80\|1,80\|<br>\|2\|Pak Bintoro\|50\|1,70\|<br>\|3\|Bu Citra\|65\|1,68\|<br>\|4\|Bu Dian\|60\|1,60\|<br>\|5\|Pak Erlangga\|75\|1,65\|<br><br>Pada Tabel 2.13, siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

| Opsi | Isi |
|---|---|
| A | Pak Bintoro, perlu menambah 3,465 kg |
| B | Pak Ananta, perlu menambah 3,465 kg |
| C | Pak Bintoro, perlu menambah 6,9375 kg |
| D | Pak Bintoro, perlu menambah 1,5 kg |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bca5d686cee12ebe401041bc440ce73843226a20f03c924e2a47212ae7ecad11`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas8_crop-p0040-antena-tv.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8eaaf0ce23c5071bd32702db58863e7cda28853a273b737cb65744562e8583ee`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas8_crop-p0041-aldo-naik-tangga.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b6bfcc36b352cb4bf53db1f558d4136116d261895618877803aecc096fb402cd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `a75a3be4a28f98e263e644a4`

Seekor kucing berada di atas genting dan terlihat kebingungan karena tidak bisa turun. Aysha yang melihat kucing tersebut langsung mencari galah dan kemudian diikat dengan keranjang kecil pada ujung galah tersebut. Saat menolong kucing tersebut, Cintia melihat Aysha dan mencoba membantunya untuk mengarahkan galah yang telah diikat keranjang tepat pada titik lokasi kucing pada jarak 4 meter. Jika jarak pandangan Cintia terhadap kucing diperkirakan 5 meter.<br><br>Tentukan jarak atap yang ditempati kucing terhadap tanah tempat Aysha berdiri.

| Opsi | Isi |
|---|---|
| A | 9 meter |
| B | 5 meter |
| C | 1 meter |
| D | 3 meter |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e9ec90a7631978b3657c3a322f0167a27dc0a77ea7ba6841682fb48bf42fa81e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `7f0ea8ebdbf606480849cd78`

Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.

| Opsi | Isi |
|---|---|
| A | 9, 12, 16 |
| B | 7, 13, 11 |
| C | 6, 2,5, 6,5 |
| D | 24, 17, 25 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['membuktikan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2ba1ddf2bd615a3ab2f4f5665efd4be07bc226ece2d3e2515296d99677f4ccf7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas8_crop-p0042-segitiga2.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3673b14104e8e2a0de802d6da3c57fa45c960b2ad24359de4161c342b7e5cb58`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas8_crop-p0042-rencana-rumah.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `848eb67358446c6d0a5c6998b32de2eed428a2c78b23acc65d1561248113f67a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `06779006c739d5de08849cb7`

Aldo dan Arjuna berdiri saling membelakangi untuk main tembak-tembakan pistol bambu. Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan. Pada saat yang sama, Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan. Pada titik terakhir, mereka berdua saling menembak.<br><br>Berapa langkah jarak kalian berdua saat mereka saling menembak?

| Opsi | Isi |
|---|---|
| A | 27 langkah |
| B | 45 langkah |
| C | 36 langkah |
| D | 63 langkah |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `446f71f50fd78952d891b428b9ae660b8e32df4923dbe119a46735736f0c1c7e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas8_crop-p0043-atlet-tenis.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41084c2b3774fa5055653fbac0150af48e402ac279632db9daea49be2cc5c05f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `e8e1147bfed27b5d98b29d8f`

Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.<br><br>Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, segitiga ABC siku-siku di C |
| B | Ya, segitiga ABC siku-siku di B |
| C | Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras |
| D | Tidak, karena AB² + BC² tidak sama dengan CA² |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f388a3d981ccd1cf52ca93bd2c96916ed3c11a2bc686d942c0806f63698207a6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas8_crop-p0044-segitiga1.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9a75baddb78f0f0f5eab8f29709020aca0391408f1f1a37514fe00a59d4ac673`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2928442f1b592d7ec569ffd93f49f1630d5c959ab94dfc2ab8a10f1183130272`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `51def5fab754abff1aeeed28`

Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.<br><br>Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.

| Opsi | Isi |
|---|---|
| A | 108.000 + y = 220.000 (y = uang Dhoni) |
| B | 108.000 - y = 220.000 (y = uang Dhoni) |
| C | 108.000 x y = 220.000 (y = uang Dhoni) |
| D | 220.000 + y = 108.000 (y = uang Dhoni) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7121801e86cfa0a7b4cb9859a787fa6bdcd12ecef7b1d3ddc91721a3ae8d13fc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `d490723c72a0d7e848c344b2`

Perhatikan beberapa kalimat berikut:<br>1. Bilangan prima terkecil adalah 3.<br>2. Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil.<br>3. Empat merupakan bilangan ganjil.<br>4. Jayapura merupakan ibu kota provinsi Papua.<br>5. Pegunungan Lantimojong berada di Sulawesi Utara.<br>Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?

| Opsi | Isi |
|---|---|
| A | Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil. |
| B | Bilangan prima terkecil adalah 3. |
| C | Empat merupakan bilangan ganjil. |
| D | Jayapura merupakan ibu kota provinsi Papua. |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bad499c0bb1221676e6fd1686d6d55cd7ac2d53cb005fac7b05092d2119abc51`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `d8ebb6f2c60e468be6bc868a`

x + 13 = 1<br><br>Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.

| Opsi | Isi |
|---|---|
| A | x = 12 |
| B | x = -12 |
| C | x = 14 |
| D | x = -14 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d04725e15751303982500ec8bff7c12510efa1ccffb54ab1ed0b84a09b077135`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `6c4807ddb62ebe4c925c56fd`

3 x + 5 = -10<br><br>Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.

| Opsi | Isi |
|---|---|
| A | x = -5 |
| B | x = 5 |
| C | x = -5/3 |
| D | x = -15 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `530225bfc438195c3fd8fbb8877c2db4eeb894b71908735e52b9a2caa3a35bce`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `69f14f018149ed7308b7751c`

Sekolah menyelenggarakan proyek penguatan proil pelajar Pancasila pada tema kearifan lokal untuk melakukan observasi menggunakan lima bus yang dapat mengangkut hanya 290 penumpang.<br><br>Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

| Opsi | Isi |
|---|---|
| A | 5x ≥ 290 (x = banyak penumpang per bus) |
| B | x ≤ 290 (x = banyak penumpang per bus) |
| C | 5x ≤ 290 (x = banyak penumpang per bus) |
| D | 5x < 290 (x = banyak penumpang per bus) |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `555a9d79c59a4a347e78323ee282534e0c5b3100265319c619185daa5736f6c4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `4e77861a69e63696e5ee9f5e`

Pak Doni adalah seorang kuli bangunan kontrak yang sedang mengerjakan proyek pemerintah dengan penghasilan tidak lebih dari Rp. 3.600.000 setiap bulannya.<br><br>Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

| Opsi | Isi |
|---|---|
| A | x ≥ 3.600.000 (x = penghasilan Pak Doni per bulan) |
| B | x ≤ 3.600.000 (x = penghasilan Pak Doni per bulan) |
| C | x < 3.600.000 (x = penghasilan Pak Doni per bulan) |
| D | x = 3.600.000 (x = penghasilan Pak Doni per bulan) |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `029f3cb890069277adbca54176156f96fc6d22d61a0b2b9b3a88beb2fef15a75`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 11 kali pengangkutan |
| B | 9,45 kali pengangkutan |
| C | 10 kali pengangkutan |
| D | 9 kali pengangkutan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c657fee617f8cd51514489f9a6c2641fab013b7f747c14e368966401a6ae9a20`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `b0ce9e96d828be7c94c0894c`

Humam memiliki uang Rp180.000,00 yang akan digunakan untuk membeli jeruk. Untuk harga 1 kg jeruk adalah Rp15.000,00.<br><br>Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.

| Opsi | Isi |
|---|---|
| A | x ≥ 12 (paling banyak 12 kg jeruk) |
| B | x ≤ 1.200 (paling banyak 1.200 kg jeruk) |
| C | x ≤ 15 (paling banyak 15 kg jeruk) |
| D | x ≤ 12 (paling banyak 12 kg jeruk) |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f8e4701a0a6e49c0bba078866c7dd8e21b9a3366c4e1e38228be471a685ef288`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `bb5563c106a35bce8aef90f0`

Panitia OSIS menjual tiket untuk konser musik yang merupakan acara tahunan sekolah. Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani. a. Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik. b. Tulislah bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik. c. Jika ada 10 tiket yang tidak terjual, tulislah bentuk aljabar dari banyak tiket secara keseluruhan.<br><br>d. Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

| Opsi | Isi |
|---|---|
| A | 92 tiket |
| B | 76 tiket |
| C | 78 tiket |
| D | 88 tiket |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `91e15667430da0f4b01af4c5fa579bff4125938e03e992d8b2f1368f8f69b910`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `bc52760c552d361c6b1ad513`

Diketahui Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; dan relasi dari himpunan C ke D adalah "kurang dari". Nyatakan relasi tersebut dalam tiga cara berikut: a. Diagram panah b. Diagram Cartesius c. Himpunan pasangan berurutan<br><br>Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.

| Opsi | Isi |
|---|---|
| A | {(3, 4), (4, 5)} |
| B | {(4, 3), (5, 3), (5, 4)} |
| C | {(3, 3), (4, 4)} |
| D | {(3, 4), (3, 5), (4, 5)} |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7526c4ab41cc3cabe86c93dffd410a60468d500992c259d240942894d6ff9dee`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `e044f1847d7a97d6815a581d`

Apabila relasi himpunan E ke F merupakan "akar dari" dengan diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}, maka nyatakan relasi tersebut dengan tiga cara berikut ini: a. himpunan pasangan berurutan. b. diagram panah; c. diagram Cartesius.<br><br>Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.

| Opsi | Isi |
|---|---|
| A | {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36)} |
| B | {(1, 1), (2, 4), (3, 9), (4, 16), (5, 20), (6, 36)} |
| C | {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)} |
| D | {(1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6)} |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6d05553ee32834f9e1685b07f1b3a5851bf2c9cb4082764b58224156aa6b00ba`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `cc51dc6d0e0814ecda8e12e1`

Periksa apakah dua himpuan berikut ini termasuk fungsi atau bukan fungsi? Jelaskan. Diketahui bahwa himpunan R dan S memiliki anggota masing-masing adalah R = {3, 4, 6, 8, 9, 12, 14, 18} dan S = {1, 6, 9}. Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan,<br><br>Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?

| Opsi | Isi |
|---|---|
| A | Fungsi, karena setiap anggota R mempunyai tepat satu pasangan di S |
| B | Bukan fungsi, karena tidak semua anggota R memiliki pasangan di S |
| C | Bukan fungsi, karena S bukan himpunan bilangan bulat |
| D | Fungsi, karena semua anggota S mempunyai pasangan di R |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b53cca83b1c9f9320a81dc509a6f95fdab670d0e56d88c42c110b74d203d0ac3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `13db9a1e91c27f3f1a174ba0`

Perhatikan dengan cermat terhadap aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m.<br><br>Apa makna pesan dari kata sandi berikut ini: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

| Opsi | Isi |
|---|---|
| A | ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH |
| B | GURUKU ADALAH ORANG TUAKU KETIKA DI RUMAH |
| C | ORANG TUAKU BUKAN GURUKU KETIKA DI RUMAH |
| D | ORANG TUAKU ADALAH GURUKU KETIKA DI SEKOLAH |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5fbaa9c0b18ff38dc40d4b7bca23c5e980c9e1ef6116de80ed9b106bdb382ad2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| B | 12 |
| C | 12! = 479.001.600 |
| D | 12 x 12 = 144 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7918e1fcf08e6b34c2bd59d63f4f25f51f1cf7036841435762c561cf1a02ec4d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `bbdde7d74cc90e271efac7fa`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? b. n(A) = n(B) = 9<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 9?

| Opsi | Isi |
|---|---|
| A | 9 + 8 + 7 + ... + 2 + 1 = 45 |
| B | 9! = 362.880 |
| C | 9 |
| D | 9 x 9 = 81 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `27f1096426a8168829c556215de2b7927e5078e6ba69e4f5dc2aaa34e2ef8eaf`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `4facb7c0ab4ee644d3112751`

Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

| Opsi | Isi |
|---|---|
| A | $y^2 + x^2 = 25$ |
| B | $x^2 + 3y = 7$ |
| C | $x + 2y = 0$ |
| D | $\frac{y}{3x} + 3x = 9$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e3829b1746f9559c7407e2d600e437929d89e43a21087fdb8056e601390d96aa`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `0ca950fcf46ff904f0263642`

Hargai bahwa setiap titik pada garis harus memenuhi persamaan yang sesuai dan digunakan untuk menentukan nilai y dari nilai x, atau sebaliknya. Sehingga, apabila suatu garis lurus persamaannya adalah y = 2 x - 3.<br><br>Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.

| Opsi | Isi |
|---|---|
| A | x = 3,5 (atau 7/2) |
| B | x = 5 |
| C | x = 2 |
| D | x = 0,5 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `230f7b215bfd1ad2d3117c9d14885b0adcbfb5c34dbef5534627a48d1db7397e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `6d6cb72cedbdc46857aa2701`

Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....

| Opsi | Isi |
|---|---|
| A | 3x + 4y - 14 = 0 |
| B | 4x - 3y + 14 = 0 |
| C | 3x - 4y + 33 = 0 |
| D | 4x + 3y - 14 = 0 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a936b383ca054fdad27b857df63846a02109ea76ff407e0eba08f793c3648714`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
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


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas8_crop-p0045-persamaan-garis-lurus.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a2d9bffe251b83a2c62958a548e6a19afbf05f1afe62033d68878a3f7faf0a0d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `bc70cacaad85275414d879e3`

Rata-rata tinggi 12 anak adalah 166 cm. Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm. Berapa rata-rata tinggi 6 anak?

| Opsi | Isi |
|---|---|
| A | 169 cm |
| B | 166,5 cm |
| C | 84,5 cm |
| D | 167 cm |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `127f4c930d4fad48166d5330bf7f2c5fa0fff28c870295591fb98905f8fea640`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `962364d9c3511c0598f13509`

Rata-rata berat badan 9 anak adalah 56 kg, jika berat badan Domi dimasukkan dalam hitungan tersebut, rata-ratanya menjadi 56,7. Tentukan berat badan Doni.

| Opsi | Isi |
|---|---|
| A | 7 kg |
| B | 63 kg |
| C | 56,7 kg |
| D | 6,3 kg |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f6fe7e04485ee29766123b7f8a1440ec4558fbc57706c96f4c626b67e9e2b40d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |
| B | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| C | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b413732f5b2b8281a2a1c1f3b463c1de9de0f3a0bfd884475ea7fca02a4e3502`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `2638edf211f383d8d9b95e05`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

| Opsi | Isi |
|---|---|
| A | Q1 = 7,5; Q2 = 6; Q3 = 4; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| B | Q1 = 4; Q2 = 5,83; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| C | Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| D | Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 3,5 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `df26d01c1bcb7ab7860b7885def498d87a08e0b6e865849f13896f3118fbc895`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `e8a6fabcd6f67b1be8f8ad7f`

Berikut data tingkat suku bunga deposito untuk jangka waktu 12 bulan di beberapa bank di Indonesia per tanggal 9 Maret 2022. Tingkat suku bunga selalu dinyatakan dalam persen.<br><br>Tabel 6.11 Tingkat Suku Bunga Deposito Jangka 12 Bulan<br><br>\| Nama Bank \| Tingkat Suku Bunga Deposito \|<br>\|---\|---\|<br>\| Bank Mandiri \| 2,50 % \|<br>\| BNI 1946 \| 2,50 % \|<br>\| BRI \| 2,50 % \|<br>\| BCA \| 1,90 % \|<br>\| Bank Maspion \| 4,75 % \|<br><br>Walaupun data di atas berbentuk persen, kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Mengapa demikian? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Karena suku bunga berupa bilangan desimal yang tidak dapat diubah menjadi sudut |
| B | Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan (jumlahnya tidak 100%) |
| C | Karena beberapa bank memiliki suku bunga yang sama sehingga juringnya bertumpuk |
| D | Karena banyaknya bank lebih dari 4 sehingga lingkaran tidak dapat dibagi |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `924fae6f2a84b7005e0fd1c3d5bd9a965eb3b9923f64e66b662f62f32acc4051`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
