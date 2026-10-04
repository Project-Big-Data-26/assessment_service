# Validasi ulang soal kelas 8 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-smp8-key-verified`. Rubrik: `math-rubric-3x4x3-v8-smp8-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 8 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 8, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 33, "knowing": 8, "reasoning": 1}, "knowledgeDimension": {"conceptual": 16, "procedural": 25, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 26, "Medium": 16, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 32, "knowing": 8, "reasoning": 1}, "knowledgeDimension": {"conceptual": 16, "procedural": 24, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 25, "Medium": 16, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 41, "revision_required": 1}`.
Run awal sukses: 126/126; adjudikasi: 14; token sukses tercatat: 450,813.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 26 | 25 | [Easy.json](difficulty/Easy.json) |
| Medium | 16 | 16 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 8, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 8, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 8.

## 1. Soal `93921cd412ef4ff1b28e79c7`

Dalam sebuah permainan kartu angka, 6 orang siswa mengambil satu kartu angka secara acak. Byoma mengambil kartu angka  6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi  mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3. Jika setiap siswa berpasangan dengan siswa yang lain,<br><br>Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?

| Opsi | Isi |
|---|---|
| A | Bathari |
| B | Lestari |
| C | Pranawa |
| D | Byoma |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rahagi memiliki angka 4. Pasangan yang mungkin adalah 3, 5, 6, 7, 8. Kita membandingkan hasil perpangkatan 4^x atau x^4. Pasangan dengan 8 menghasilkan 4^8 = 65.536 atau 8^4 = 4.096. Pasangan dengan 7 menghasilkan 4^7 = 16.384 atau 7^4 = 2.401. Pasangan dengan 6 menghasilkan 4^6 = 4.096 atau 6^4 = 1.296. Pasangan dengan 5 menghasilkan 4^5 = 1.024 atau 5^4 = 625. Pasangan dengan 3 menghasilkan 4^3 = 64 atau 3^4 = 81. Nilai terbesar adalah 65.536 (4^8), maka Rahagi harus berpasangan dengan Bathari (8).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `86d91c2e15b27aecf9da4839c3bf005ab04953907d48d161397ae676080586fa`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2864 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2838 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2759 |

Run 1 — solusi: Rahagi memiliki angka 4. Pasangan yang mungkin adalah 3, 5, 6, 7, 8. Kita perlu membandingkan hasil perpangkatan 4^x atau x^4. Pasangan dengan 8 menghasilkan 4^8 = 65.536 atau 8^4 = 4.096. Pasangan dengan 7 menghasilkan 4^7 = 16.384 atau 7^4 = 2.401. Pasangan dengan 6 menghasilkan 4^6 = 4.096 atau 6^4 = 1.296. Pasangan dengan 5 menghasilkan 4^5 = 1.024 atau 5^4 = 625. Pasangan dengan 3 menghasilkan 4^3 = 64 atau 3^4 = 81. Nilai terbesar adalah 65.536 (4^8), maka Rahagi harus berpasangan dengan Bathari (8).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perpangkatan bilangan bulat untuk membandingkan hasil dari berbagai kemungkinan pasangan. Ini melibatkan pemilihan prosedur (membandingkan hasil perpangkatan) untuk mencapai tujuan (nilai terbesar), yang masuk dalam kategori applying.. Bukti: Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi perpangkatan dan perbandingan nilai bilangan berpangkat.. Bukti: angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya langsung (membandingkan hasil perpangkatan dari pasangan yang tersedia). Siswa hanya perlu melakukan operasi hitung dasar dan membandingkan hasilnya. Tidak ada kendala yang saling berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perpangkatan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan operasi perpangkatan. Tugas membandingkan hasil perpangkatan dengan angka-angka kecil adalah tugas rutin yang sesuai dengan tingkat kemampuan kelas 8. |

Run 2 — solusi: Rahagi memiliki angka 4. Pasangan yang mungkin adalah 3, 5, 6, 7, 8. Nilai yang mungkin adalah 4^3=64, 3^4=81, 4^5=1024, 5^4=625, 4^6=4096, 6^4=1296, 4^7=16384, 7^4=2401, 4^8=65536, 8^4=4096. Nilai terbesar adalah 4^8 = 65536, sehingga Rahagi harus berpasangan dengan Bathari (8).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perpangkatan untuk membandingkan hasil dari berbagai kemungkinan pasangan (basis dan eksponen) guna menentukan nilai maksimum. Ini adalah penerapan konsep dalam konteks rutin.. Bukti: Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana basis dan eksponen memengaruhi hasil perpangkatan, serta prosedur perbandingan nilai.. Bukti: angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan operasi perpangkatan sederhana dan membandingkan hasilnya. Jalur penyelesaian sangat jelas (memeriksa pasangan yang ada) dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit.. Bukti: Byoma mengambil kartu angka 6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3.; menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perpangkatan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan operasi perpangkatan. Tugas membandingkan hasil perpangkatan dari pasangan angka yang tersedia adalah prosedur rutin yang sesuai dengan tingkat kemampuan kelas 8. |

Run 3 — solusi: Rahagi memiliki angka 4. Siswa lain memiliki angka 3, 5, 6, 7, 8. Rahagi harus berpasangan dengan siswa yang memiliki angka terbesar (8) agar hasil perpangkatan maksimal. Membandingkan 4^8 = 65.536 dengan kemungkinan lain (misal 8^4 = 4.096), 4^8 adalah yang terbesar.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep perpangkatan dan membandingkan hasil operasi untuk menentukan nilai terbesar. Ini adalah penerapan konsep dasar bilangan berpangkat dalam konteks perbandingan nilai.. Bukti: Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar jika angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat bilangan berpangkat (basis dan eksponen) dan bagaimana perubahan nilai pada basis atau eksponen memengaruhi hasil akhir.. Bukti: angka Rahagi dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengidentifikasi angka terbesar dari kumpulan data yang diberikan dan menerapkan operasi perpangkatan sederhana. Jalur penyelesaian sangat jelas, tidak ada kendala yang saling berinteraksi, dan beban perhitungan rendah.. Bukti: Byoma mengambil kartu angka 6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3.; Siapa yang harus diajak berpasangan oleh Rahagi agar kelompoknya menghasilkan angka terbesar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan berpangkat bulat positif. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan operasi perpangkatan. Soal ini hanya meminta perbandingan nilai sederhana tanpa kerumitan variabel atau kendala tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4845`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep perpangkatan untuk membandingkan hasil dari berbagai kemungkinan pasangan (basis dan eksponen) guna menentukan nilai maksimum. Ini adalah penerapan konsep dasar bilangan berpangkat dalam konteks perbandingan nilai.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana basis dan eksponen memengaruhi hasil perpangkatan, serta prosedur perbandingan nilai.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan operasi perpangkatan sederhana dan membandingkan hasilnya. Jalur penyelesaian sangat jelas (memeriksa pasangan yang ada) dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perpangkatan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan operasi perpangkatan. Tugas membandingkan hasil perpangkatan dari pasangan angka yang tersedia adalah prosedur rutin yang sesuai dengan tingkat kemampuan kelas 8. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `864dfc1e16dfcf65cd20bd5a`

Dalam sebuah permainan kartu angka, 6 orang siswa mengambil satu kartu angka secara acak. Byoma mengambil kartu angka  6, Pranawa mengambil angka 5, Lestari mengambil kartu angka 7, Rahagi  mengambil kartu angka 4, Bathari mengambil kartu angka 8, dan Dwi mengambil kartu angka 3. Jika setiap siswa berpasangan dengan siswa yang lain,<br><br>Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?

| Opsi | Isi |
|---|---|
| A | Rahagi |
| B | Pranawa |
| C | Dwi |
| D | Byoma |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Lestari memiliki angka 7. Pasangan yang mungkin adalah 3, 4, 5, 6, 8. Kita membandingkan hasil 7^x atau x^7 untuk setiap x. Pasangan dengan Dwi (3) menghasilkan 7^3 = 343 atau 3^7 = 2.187. Pasangan dengan Rahagi (4) menghasilkan 7^4 = 2.401 atau 4^7 = 16.384. Pasangan dengan Pranawa (5) menghasilkan 7^5 = 16.807 atau 5^7 = 78.125. Pasangan dengan Byoma (6) menghasilkan 7^6 = 117.649 atau 6^7 = 279.936. Pasangan dengan Bathari (8) menghasilkan 7^8 = 5.764.801 atau 8^7 = 2.097.152. Nilai terkecil dari semua kemungkinan adalah 343 (dari 7^3). Maka, pasangan yang menghasilkan nilai terkecil adalah Dwi (3).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aa10ef98dbf94c9b9159ab5547d470510ce31668e6afe3a74a0635a9caef4895`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2900 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2954 |
| 3 | success | concern / conflict | applying | conceptual | Medium | 4527 |

Run 1 — solusi: Lestari memiliki angka 7. Pasangan yang mungkin adalah Rahagi (4), Pranawa (5), Byoma (6), Bathari (8), dan Dwi (3). Kita membandingkan hasil perpangkatan: 7^3 = 343 atau 3^7 = 2.187; 7^4 = 2.401 atau 4^7 = 16.384; 7^5 = 16.807 atau 5^7 = 78.125; 7^6 = 117.649 atau 6^7 = 279.936; 7^8 = 5.764.801 atau 8^7 = 2.097.152. Nilai terkecil dari semua kemungkinan pasangan Lestari adalah 343 (dari 7^3). Maka, Lestari harus berpasangan dengan Dwi (3).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep perpangkatan dan membandingkan hasil dari berbagai kemungkinan pasangan untuk menentukan nilai terkecil. Ini melibatkan penerapan prosedur matematika pada konteks masalah yang diberikan.. Bukti: Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat perpangkatan bilangan bulat dan bagaimana basis serta eksponen memengaruhi hasil akhir.. Bukti: angka Lestari dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan perbandingan sistematis antara beberapa kemungkinan pasangan (7^x atau x^7). Meskipun prosedurnya familiar, terdapat beberapa langkah perhitungan yang saling terkait dan siswa harus mengevaluasi semua opsi untuk memastikan hasil terkecil.. Bukti: Lestari mengambil kartu angka 7; Byoma (6), Pranawa (5), Rahagi (4), Bathari (8), dan Dwi (3); menghasilkan angka terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perpangkatan bilangan bulat. |
| dependentSteps | 5 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi perpangkatan dan membandingkan nilai. Soal ini menuntut ketelitian dalam membandingkan hasil dari 5 pasangan yang berbeda, yang merupakan tantangan moderat bagi jenjang ini. |

Run 2 — solusi: Lestari memiliki angka 7. Pasangan yang mungkin adalah 3, 4, 5, 6, 8. Kita membandingkan hasil 7^x atau x^7 untuk setiap x. Pasangan dengan Dwi (3) menghasilkan 3^7 = 2.187 atau 7^3 = 343. Pasangan dengan Rahagi (4) menghasilkan 4^7 = 16.384 atau 7^4 = 2.401. Pasangan dengan Pranawa (5) menghasilkan 5^7 = 78.125 atau 7^5 = 16.807. Pasangan dengan Byoma (6) menghasilkan 6^7 = 279.936 atau 7^6 = 117.649. Pasangan dengan Bathari (8) menghasilkan 8^7 = 2.097.152 atau 7^8 = 5.764.801. Nilai terkecil dari semua kemungkinan hasil adalah 343 (dari 7^3). Maka, pasangan yang menghasilkan nilai terkecil adalah Dwi (3).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep perpangkatan dan membandingkan hasil operasi bilangan berpangkat untuk menentukan nilai terkecil dari berbagai kemungkinan pasangan. Ini melibatkan penerapan konsep pada situasi yang diberikan.. Bukti: Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil jika angka Lestari dipangkatkan dengan pasangannya atau sebaliknya?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip perpangkatan (konsep) untuk membandingkan hasil operasi bilangan berpangkat.. Bukti: Lestari mengambil kartu angka 7; angka Lestari dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Medium`: Soal ini memerlukan perbandingan beberapa hasil perpangkatan. Meskipun prosedurnya rutin, siswa harus melakukan perhitungan atau estimasi untuk beberapa pasangan (3, 4, 5, 6, 8) dengan dua kemungkinan operasi (a^b atau b^a), yang meningkatkan beban integrasi langkah.. Bukti: Lestari mengambil kartu angka 7; Byoma (6), Pranawa (5), Rahagi (4), Bathari (8), Dwi (3); angka Lestari dipangkatkan dengan pasangannya atau sebaliknya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan berpangkat bulat positif. |
| dependentSteps | 5 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi perpangkatan dan membandingkan nilai. Soal ini menuntut ketelitian dalam membandingkan banyak kemungkinan pasangan, yang sesuai untuk tingkat kesulitan menengah. |

Run 3 — solusi: Lestari=7. Pasangan dengan Dwi(3) menghasilkan 7^3=343 atau 3^7=2187. Pasangan lain menghasilkan nilai jauh lebih besar (misal 7^4=2401, 4^7=16384). Dwi adalah pasangan yang menghasilkan nilai terkecil.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perpangkatan untuk membandingkan hasil dari berbagai pasangan bilangan, yang merupakan penerapan prosedur dalam konteks rutin.. Bukti: Siapa yang harus diajak berpasangan oleh Lestari agar kelompoknya menghasilkan angka terkecil; Lestari mengambil kartu angka 7; Dwi mengambil kartu angka 3
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana nilai bilangan berpangkat berubah berdasarkan basis dan eksponennya.. Bukti: angka Lestari dipangkatkan dengan pasangannya atau sebaliknya
- Intended difficulty `classify/Medium`: Siswa harus melakukan beberapa perhitungan eksponen (atau estimasi) untuk membandingkan hasil dari 5 pasangan yang mungkin. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait dan perlu perbandingan nilai yang cermat.. Bukti: 6 orang siswa mengambil satu kartu angka secara acak; angka Lestari dipangkatkan dengan pasangannya atau sebaliknya

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menghitung dan membandingkan nilai perpangkatan sederhana. Beban kognitif terletak pada banyaknya perbandingan yang harus dilakukan untuk menentukan nilai terkecil. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4925`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep perpangkatan dan membandingkan hasil dari berbagai kemungkinan pasangan untuk menentukan nilai terkecil. Ini melibatkan penerapan prosedur matematika pada konteks masalah yang diberikan.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang sifat perpangkatan bilangan bulat dan bagaimana basis serta eksponen memengaruhi hasil akhir.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan perbandingan sistematis antara beberapa kemungkinan pasangan (7^x atau x^7). Meskipun prosedurnya familiar, terdapat beberapa langkah perhitungan yang saling terkait dan siswa harus mengevaluasi semua opsi untuk memastikan hasil terkecil.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perpangkatan bilangan bulat. |
| dependentSteps | 5 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi perpangkatan dan membandingkan nilai. Soal ini menuntut ketelitian dalam membandingkan hasil dari 5 pasangan yang berbeda, yang merupakan tantangan moderat bagi jenjang ini. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `9eeb60ca1e3ebdc6a02a1999`

Coba sederhanakan bentuk akar berikut. $3\sqrt{2} \times 6\sqrt{6}$

| Opsi | Isi |
|---|---|
| A | $2\sqrt{3}$ |
| B | $36\sqrt{3}$ |
| C | $18\sqrt{3}$ |
| D | $36\sqrt{2}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 3\sqrt{2} \times 6\sqrt{6} = (3 \times 6) \times \sqrt{2 \times 6} = 18 \times \sqrt{12} = 18 \times \sqrt{4 \times 3} = 18 \times 2\sqrt{3} = 36\sqrt{3}
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4987392ea896c7cfba5f64797e5899e18cec35df49e058c3ce881f92d3ae4ba7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2679 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3450 |
| 3 | success | valid / verified | applying | procedural | Easy | 2632 |

Run 1 — solusi: 3\sqrt{2} \times 6\sqrt{6} = (3 \times 6) \times \sqrt{2 \times 6} = 18 \times \sqrt{12} = 18 \times \sqrt{4 \times 3} = 18 \times 2\sqrt{3} = 36\sqrt{3}
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan operasi perkalian pada bentuk akar yang melibatkan koefisien dan bilangan di dalam akar. Siswa perlu menerapkan prosedur perkalian bentuk akar (a√b × c√d = ac√(bd)) dan menyederhanakan akar kuadrat, yang merupakan prosedur standar.. Bukti: Coba sederhanakan bentuk akar berikut. 3√2 × 6√6
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritme perkalian bentuk akar dan penyederhanaan bentuk akar, yang merupakan pengetahuan prosedural.. Bukti: 3√2 × 6√6
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Langkah-langkahnya jelas: mengalikan koefisien, mengalikan radikan, dan menyederhanakan hasil akar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 3√2 × 6√6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian bentuk akar dan penyederhanaan akar kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah dasar operasi bentuk akar yang diajarkan di kelas 8. Prosedur penyelesaiannya langsung dan tidak memerlukan perencanaan kompleks. |

Run 2 — solusi: 3√2 × 6√6 = (3 × 6) × √(2 × 6) = 18 × √12 = 18 × √(4 × 3) = 18 × 2√3 = 36√3.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi perkalian bentuk akar secara langsung menggunakan aturan (a√b) * (c√d) = (ac)√(bd) dan menyederhanakan hasilnya.. Bukti: 3\sqrt{2} \times 6\sqrt{6}
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritme perkalian bentuk akar dan penyederhanaan akar kuadrat.. Bukti: 3\sqrt{2} \times 6\sqrt{6}
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari prosedur perkalian bentuk akar yang familiar bagi siswa kelas 8. Tidak ada kendala kompleks atau langkah non-rutin.. Bukti: 3\sqrt{2} \times 6\sqrt{6}

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
| gradeRelativeRationale | Materi ini adalah dasar dari operasi bentuk akar di kelas 8, sehingga dikategorikan Easy karena prosedurnya langsung dan rutin. |

Run 3 — solusi: 3√2 × 6√6 = (3 × 6) × √(2 × 6) = 18 × √12 = 18 × √(4 × 3) = 18 × 2√3 = 36√3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur perkalian bentuk akar yang melibatkan koefisien dan bilangan di dalam akar secara langsung sesuai aturan operasi aljabar.. Bukti: 3√2 × 6√6
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang aturan perkalian bentuk akar (a√b × c√d = ac√(bd)) dan penyederhanaan bentuk akar.. Bukti: 3√2 × 6√6
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Langkah-langkah penyelesaiannya jelas: mengalikan koefisien, mengalikan radikan, dan menyederhanakan akar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: 3√2 × 6√6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian bentuk akar dan penyederhanaan akar kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan standar kurikulum kelas 8. Prosedur perkalian dan penyederhanaan akar adalah keterampilan dasar yang diajarkan secara eksplisit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4122`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur perkalian bentuk akar (a√b × c√d = ac√(bd)) dan menyederhanakan hasil akar kuadrat. Ini adalah penerapan langsung dari algoritme yang dipelajari.
- Dimensi pengetahuan `procedural`: Soal menguji penguasaan algoritme perkalian dan penyederhanaan bentuk akar, yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini adalah latihan rutin yang melibatkan langkah-langkah prosedural standar (perkalian koefisien, perkalian radikan, penyederhanaan akar). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian bentuk akar dan penyederhanaan akar kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan standar kurikulum kelas 8. Prosedur perkalian dan penyederhanaan akar adalah keterampilan dasar yang diajarkan secara eksplisit dan rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `8c189810bd620fa2b116eab9`

Coba buatlah dalam bentuk yang paling sederhana. $3\sqrt{2} + 5\sqrt{2}$

| Opsi | Isi |
|---|---|
| A | $8\sqrt{4}$ |
| B | $3\sqrt{2}$ |
| C | $15\sqrt{2}$ |
| D | $8\sqrt{2}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 3√2 + 5√2 = (3 + 5)√2 = 8√2
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f21ac2d9327d31a35088be755bb59b4f459582cfd7dc726ff017de55d2e882c4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2945 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3127 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2487 |

Run 1 — solusi: 3√2 + 5√2 = (3 + 5)√2 = 8√2
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk melakukan operasi penjumlahan pada bentuk akar yang sejenis. Ini adalah prosedur dasar yang langsung, tidak memerlukan strategi kompleks atau penalaran mendalam.. Bukti: 3√2 + 5√2
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan suku sejenis pada bentuk akar, yang merupakan pengetahuan prosedural.. Bukti: 3√2 + 5√2
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menjumlahkan koefisien dari bentuk akar yang sama. Tidak ada kendala yang berinteraksi atau perencanaan langkah yang kompleks.. Bukti: 3√2 + 5√2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan aljabar suku sejenis |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah pengenalan dasar operasi bentuk akar di kelas 8. Soal tidak menuntut lebih dari penerapan prosedur standar. |

Run 2 — solusi: Penjumlahan bentuk akar sejenis dilakukan dengan menjumlahkan koefisiennya: 3√2 + 5√2 = (3 + 5)√2 = 8√2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali bahwa ini adalah penjumlahan bentuk akar sejenis dan menerapkan prosedur penjumlahan koefisien secara langsung.. Bukti: 3√2 + 5√2
- Dimensi pengetahuan `classify/procedural`: Soal menguji penguasaan algoritma atau prosedur dasar dalam menjumlahkan bentuk akar yang sejenis.. Bukti: 3√2 + 5√2
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari aturan penjumlahan bentuk akar sejenis. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: 3√2 + 5√2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan bentuk akar sejenis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 sebagai latihan dasar operasi bentuk akar. |

Run 3 — solusi: Operasi penjumlahan bentuk akar sejenis dilakukan dengan menjumlahkan koefisiennya: 3√2 + 5√2 = (3 + 5)√2 = 8√2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali bahwa bentuk akar tersebut sejenis dan menerapkan prosedur penjumlahan koefisien yang sudah dipelajari.. Bukti: Coba buatlah dalam bentuk yang paling sederhana. 3√2 + 5√2
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan pada bentuk akar.. Bukti: 3√2 + 5√2
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan penerapan langsung dari aturan penjumlahan bentuk akar sejenis. Tidak ada langkah kompleks atau kendala yang perlu diintegrasikan.. Bukti: 3√2 + 5√2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan aljabar (variabel sejenis) dan sifat bentuk akar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin yang sangat standar untuk kelas 8 dalam topik bentuk akar, tidak memerlukan perencanaan atau strategi khusus. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `e97f2eaa7ee74e27d6bb517c`

Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

| Opsi | Isi |
|---|---|
| A | 3,4 × 10<sup>11</sup> |
| B | 3,4 × 10<sup>-10</sup> |
| C | 3,4 × 10<sup>10</sup> |
| D | 3,4 × 10<sup>9</sup> |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bilangan 34.000.000.000 memiliki 11 digit. Untuk mengubahnya ke bentuk baku (a x 10^n dengan 1 <= a < 10), kita letakkan koma setelah angka pertama (3,4). Pergeseran koma dari posisi awal ke posisi setelah angka 3 adalah 10 langkah ke kiri, sehingga n = 10. Hasilnya adalah 3,4 x 10^10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `479c9633e834834b7ee326a51dd6856d7e247e4e7416b05ce1473a6fbadcaa2f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2724 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2640 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2686 |

Run 1 — solusi: Bilangan 34.000.000.000 dapat ditulis sebagai 3,4 dikalikan dengan 10 pangkat n. Karena 34.000.000.000 = 3,4 x 10.000.000.000 dan 10.000.000.000 = 10^10, maka bentuk bakunya adalah 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengubah bilangan desimal besar ke dalam bentuk baku (notasi ilmiah). Siswa hanya perlu menerapkan prosedur standar penulisan bentuk baku (a x 10^n dengan 1 <= a < 10) secara langsung tanpa memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami definisi dan prosedur penulisan bentuk baku, yang merupakan algoritma atau metode standar dalam matematika untuk merepresentasikan bilangan besar.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung jumlah pergeseran koma desimal untuk menentukan eksponen. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategi yang kompleks.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan konsep perpangkatan bilangan 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penulisan bentuk baku adalah materi dasar kelas 8 yang diajarkan secara eksplisit. Soal ini menguji pemahaman prosedural dasar tanpa variasi atau jebakan yang memerlukan penalaran tingkat tinggi. |

Run 2 — solusi: Bilangan 34.000.000.000 dapat ditulis sebagai 3,4 dikalikan dengan 10 pangkat n. Karena terdapat 10 angka setelah angka 3, maka n = 10. Jadi, bentuk bakunya adalah 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengubah bilangan desimal besar ke dalam bentuk baku (notasi ilmiah). Ini adalah prosedur standar yang langsung, di mana siswa hanya perlu mengidentifikasi koefisien (1 <= a < 10) dan menghitung pergeseran koma desimal untuk menentukan eksponen.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap definisi dan aturan penulisan bentuk baku (notasi ilmiah), yang merupakan konsep dasar dalam materi bilangan berpangkat.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu menerapkan definisi bentuk baku dengan menghitung jumlah digit yang digeser. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang nilai tempat dan konsep dasar bilangan berpangkat positif. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bentuk baku adalah topik dasar kelas 8. Soal ini merupakan penerapan langsung definisi tanpa modifikasi atau konteks cerita yang rumit. |

Run 3 — solusi: Bilangan 34.000.000.000 dapat ditulis sebagai 3,4 dikalikan dengan 10 pangkat n. Karena terdapat 10 angka setelah angka 3, maka n = 10. Jadi, bentuk bakunya adalah 3,4 x 10^10.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengubah bilangan desimal besar ke dalam bentuk baku (notasi ilmiah). Ini adalah prosedur standar yang langsung, di mana siswa hanya perlu mengidentifikasi koefisien (1 <= a < 10) dan menghitung pergeseran desimal untuk menentukan eksponen.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap aturan penulisan bentuk baku (notasi ilmiah), yang merupakan bagian dari pengetahuan prosedural tentang bagaimana merepresentasikan bilangan besar.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan definisi bentuk baku (a x 10^n) tanpa ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks. Tingkat kesulitannya rendah bagi siswa kelas 8.. Bukti: Tulislah bilangan berikut dalam bentuk baku. 34.000.000.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang nilai tempat dan konsep dasar notasi ilmiah (bentuk baku). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bentuk baku adalah kurikulum standar kelas 8. Soal ini adalah penerapan langsung dari definisi tanpa variasi atau jebakan yang memerlukan penalaran tingkat tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4372`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung dari definisi bentuk baku (notasi ilmiah). Siswa hanya perlu mengenali prosedur standar untuk mengubah bilangan desimal besar menjadi bentuk a x 10^n, yang merupakan tugas knowing.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau metode standar untuk menuliskan bilangan dalam bentuk baku, yang termasuk dalam pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini adalah latihan rutin yang sangat mendasar bagi siswa kelas 8. Tidak ada kendala yang berinteraksi, tidak ada kebutuhan untuk strategi nonrutin, dan langkah penyelesaiannya sangat jelas (menghitung pergeseran desimal).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan konsep dasar notasi ilmiah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penulisan bentuk baku adalah materi kurikulum standar kelas 8. Soal ini merupakan penerapan langsung definisi tanpa variasi atau konteks yang rumit. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `f25d4029ecaafe78249ca72b`

Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10<sup>8</sup>

| Opsi | Isi |
|---|---|
| A | 2.500.000.000 |
| B | 25.000.000 |
| C | 0,000000025 |
| D | 250.000.000 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 2,5 x 10^8 = 2,5 x 100.000.000 = 250.000.000. Menggeser koma 8 posisi ke kanan dari 2,5 menghasilkan 250.000.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0710d7bb4e5acac7de4387edf0f0bac08db56a49d33f80d8671bab7e33018e8f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2619 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2589 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2613 |

Run 1 — solusi: 2,5 x 10^8 = 2,5 x 100.000.000 = 250.000.000. Menggeser koma 8 posisi ke kanan dari 2,5 menghasilkan 250.000.000.
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan prosedur langsung mengubah notasi ilmiah ke bentuk desimal biasa. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10^8
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan penulisan bentuk baku (notasi ilmiah) dan cara mengonversinya ke bentuk desimal.. Bukti: 2,5 × 10^8
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami definisi pangkat positif pada basis 10 untuk menggeser koma desimal. Tidak ada kendala atau langkah yang saling bergantung.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10^8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sistem bilangan desimal dan notasi ilmiah (pangkat bulat positif). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bentuk baku adalah kurikulum standar kelas 8. Soal ini adalah penerapan langsung definisi tanpa modifikasi atau konteks cerita yang rumit. |

Run 2 — solusi: 2,5 x 10^8 = 2,5 x 100.000.000 = 250.000.000. Menggeser koma 8 posisi ke kanan dari 2,5 menghasilkan 250.000.000.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan prosedur konversi standar dari notasi ilmiah ke bentuk desimal biasa dengan menggeser koma desimal sesuai pangkat sepuluh.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10^8
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan penulisan bentuk baku (notasi ilmiah) dan cara mengubahnya kembali ke bentuk desimal.. Bukti: 2,5 × 10^8
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu operasi pergeseran koma desimal berdasarkan eksponen yang diberikan tanpa ada kendala tambahan atau langkah yang saling bergantung.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10^8

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
| gradeRelativeRationale | Konversi notasi ilmiah adalah materi dasar kelas 8 yang prosedurnya sangat jelas dan familiar bagi siswa. |

Run 3 — solusi: 2,5 x 10^8 = 2,5 x 100.000.000 = 250.000.000. Menggeser koma 8 posisi ke kanan dari 2,5 menghasilkan 250.000.000.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan konversi langsung dari notasi ilmiah ke bentuk desimal biasa, yang merupakan prosedur standar dalam materi bentuk baku.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10^8
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami aturan penulisan bentuk baku (notasi ilmiah) dan bagaimana mengonversinya ke bentuk desimal biasa, yang merupakan pengetahuan prosedural.. Bukti: 2,5 × 10^8
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu menerapkan aturan pergeseran koma desimal berdasarkan eksponen 10. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Tulislah bilangan berikut dalam bentuk biasa. 2,5 × 10^8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sistem bilangan desimal dan operasi perkalian dengan perpangkatan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi notasi ilmiah ke bentuk biasa adalah materi dasar kelas 8 yang bersifat prosedural rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `ac7f560c796164a475dad657`

Indeks Massa Tubuh $= \dfrac{BB}{TB^2}$. BB: Berat badan (kg), TB: Tinggi badan (m).<br><br>**Tabel 2.12** Kategori Indeks Massa Tubuh<br><br>\|Kategori\|IMT\|<br>\|---\|---\|<br>\|Kekurangan berat badan tingkat berat\|Kurang dari 17,0\|<br>\|Kekurangan berat badan tingkat ringan\|17,0 sampai 18,4\|<br>\|Normal\|18,5 sampai 25,0\|<br>\|Kelebihan berat badan tingkat ringan\|25,1 sampai 27,0\|<br>\|Kelebihan berat badan tingkat berat\|Lebih dari 27,0\|<br><br>**Tabel 2.13** Data Berat dan Tinggi Badan<br><br>\|No\|Nama\|Berat Badan (kg)\|Tinggi Badan (m)\|<br>\|---\|---\|---\|---\|<br>\|1\|Pak Ananta\|80\|1,80\|<br>\|2\|Pak Bintoro\|50\|1,70\|<br>\|3\|Bu Citra\|65\|1,68\|<br>\|4\|Bu Dian\|60\|1,60\|<br>\|5\|Pak Erlangga\|75\|1,65\|<br><br>Pada Tabel 2.13, siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

| Opsi | Isi |
|---|---|
| A | Pak Bintoro, perlu menambah 3,465 kg |
| B | Pak Ananta, perlu menambah 3,465 kg |
| C | Pak Bintoro, perlu menambah 6,9375 kg |
| D | Pak Bintoro, perlu menambah 1,5 kg |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: IMT Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). Target berat untuk IMT 18,5 = 18,5 * 1,70^2 = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ee11c33224006c13175e500bab84e8a4f6d9a280d5ac69cab01cac6265f1538b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3084 |
| 2 | success | valid / verified | applying | procedural | Medium | 3120 |
| 3 | success | valid / verified | applying | procedural | Medium | 3113 |

Run 1 — solusi: IMT Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). Target berat untuk IMT 18,5 = 18,5 * 1,70^2 = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan untuk menghitung IMT setiap individu, mengklasifikasikannya berdasarkan tabel, lalu melakukan perhitungan aljabar untuk mencari selisih berat badan. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan rumus (prosedural) dan mengintegrasikannya dengan data dari tabel (konseptual) untuk menyelesaikan masalah.. Bukti: Indeks Massa Tubuh = BB/TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh; Tabel 2.13 Data Berat dan Tinggi Badan
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah (menghitung IMT, membandingkan dengan tabel, membalik rumus untuk mencari target berat, menghitung selisih), namun prosedurnya sangat rutin dan terstruktur. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal, pemahaman rumus aljabar sederhana, dan interpretasi tabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi hitung desimal dan manipulasi rumus sederhana. Langkah-langkahnya jelas dan terstruktur, namun memerlukan ketelitian dalam perhitungan bertahap. |

Run 2 — solusi: IMT Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 ≈ 17,30. Kategori 17,0-18,4 (Kekurangan berat badan tingkat ringan). Target berat untuk IMT 18,5: 18,5 * 1,70^2 = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan ke dalam data yang tersedia, mengidentifikasi kategori yang sesuai, dan melakukan manipulasi aljabar sederhana untuk mencari selisih berat badan. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Indeks Massa Tubuh = BB/TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang penggunaan rumus (prosedural) dan interpretasi data dalam tabel berdasarkan kriteria yang diberikan (konseptual).. Bukti: Indeks Massa Tubuh = BB/TB^2; Kategori 17,0 sampai 18,4
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap perhitungan yang saling terkait: menghitung IMT untuk identifikasi kategori, lalu membalik rumus untuk mencari target berat badan. Meskipun prosedurnya familiar, siswa harus merencanakan langkah-langkah tersebut secara berurutan tanpa bantuan eksplisit.. Bukti: Indeks Massa Tubuh = BB/TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal dan pemahaman rumus aljabar sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah terbiasa dengan operasi bilangan rasional dan substitusi nilai ke dalam rumus. Soal ini menuntut ketelitian dalam perhitungan desimal dan pemahaman konsep target berat badan. |

Run 3 — solusi: 1. Hitung IMT tiap orang: Pak Bintoro = 50 / (1,70^2) = 50 / 2,89 ≈ 17,30. Kategori 17,0-18,4 (kekurangan berat badan tingkat ringan) sesuai untuk Pak Bintoro. 2. Target berat untuk IMT 18,5: Berat = 18,5 * (1,70^2) = 18,5 * 2,89 = 53,465 kg. 3. Tambahan berat = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan ke dalam konteks data yang ada, melakukan perhitungan aritmatika, dan memanipulasi rumus untuk mencari nilai berat badan yang diperlukan. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Indeks Massa Tubuh = BB/TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma perhitungan (operasi bilangan rasional) dan memahami hubungan antara variabel (BB, TB, IMT) serta kategori yang diberikan.. Bukti: Indeks Massa Tubuh = BB/TB^2; Kategori Indeks Massa Tubuh; Data Berat dan Tinggi Badan
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah perhitungan (menghitung IMT, membandingkan dengan tabel, memanipulasi rumus untuk mencari berat target, dan mencari selisih). Meskipun prosedural, terdapat beberapa langkah yang saling terkait dan memerlukan ketelitian dalam operasi bilangan desimal.. Bukti: Indeks Massa Tubuh = BB/TB^2; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal dan pemahaman dasar aljabar (substitusi dan manipulasi rumus sederhana). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi hitung bilangan rasional dan memanipulasi rumus sederhana. Soal ini menuntut ketelitian dalam perhitungan berjenjang, namun prosedurnya bersifat rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `e997c38609f1bdf2dbf30b43`

Gambar berikut memperlihatkan tiang antena TV di atas genting. Tiang antena tersebut ditarik oleh kawat supaya kuat dan tidak goyang saat terkena angin. Biasanya kawat tersebut dipasang pada $\frac{3}{4}$ bagian dari tinggi tiang dari permukaan atas genting. Tiang antena tingginya 8 meter.<br><br>Tentukan panjang kawat jika jarak antara kawat dan tiang pada tanah adalah 8 meter.

| Opsi | Isi |
|---|---|
| A | 6 meter |
| B | 100 meter |
| C | 14 meter |
| D | 10 meter |

![Gambar sumber soal 8](<../../../images/kelas8_crop-p0040-antena-tv.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `10 meter`.
Solusi minimum hasil AI: Tinggi kawat pada tiang = 3/4 * 8 m = 6 m. Jarak kawat ke tiang di tanah = 8 m. Menggunakan teorema Pythagoras, panjang kawat = akar(6^2 + 8^2) = akar(36 + 64) = akar(100) = 10 m.
Gambar sumber: images/kelas8_crop-p0040-antena-tv.png. Transkripsi visual: Sebuah gambar menunjukkan tiang antena vertikal berwarna oranye dan sebuah kawat miring berwarna hitam yang menghubungkan tiang tersebut ke titik di tanah, membentuk segitiga siku-siku.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ac12080c747f3740201bb73ce35a0698fc77bde908f5d83d0d7c68ed95cbc582`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3875 |
| 2 | success | valid / verified | applying | procedural | Medium | 3875 |
| 3 | success | valid / verified | applying | procedural | Medium | 3812 |

Run 1 — solusi: Tinggi kawat pada tiang = 3/4 * 8 m = 6 m. Jarak kawat ke tiang di tanah = 8 m. Menggunakan teorema Pythagoras, panjang kawat = akar(6^2 + 8^2) = akar(36 + 64) = akar(100) = 10 m.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan informasi teks untuk menentukan panjang sisi tegak segitiga (3/4 dari 8m) dan sisi alas (8m), kemudian menerapkan prosedur teorema Pythagoras untuk mencari sisi miring. Ini adalah penerapan prosedur rutin pada konteks soal cerita.. Bukti: kawat tersebut dipasang pada 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter; Tentukan panjang kawat
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara panjang sisi-sisi segitiga siku-siku (konseptual) dan penerapan algoritma teorema Pythagoras (prosedural).. Bukti: 3/4 bagian dari tinggi tiang; panjang kawat = akar(6^2 + 8^2)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah berurutan: menghitung tinggi kawat (3/4 * 8) dan kemudian menerapkan teorema Pythagoras. Meskipun prosedurnya familiar, siswa harus mengintegrasikan informasi teks ke dalam model matematika segitiga siku-siku.. Bukti: kawat tersebut dipasang pada 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pecahan dasar dan Teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerjemahkan situasi nyata ke dalam model segitiga siku-siku dan melakukan perhitungan Pythagoras sederhana. |

Run 2 — solusi: Tinggi kawat pada tiang = (3/4) * 8 m = 6 m. Jarak kawat ke tiang di tanah = 8 m. Menggunakan Teorema Pythagoras, panjang kawat = akar(6^2 + 8^2) = akar(36 + 64) = akar(100) = 10 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang relevan (tinggi kawat dan jarak alas), melakukan operasi aritmatika dasar untuk menentukan tinggi segitiga, dan menerapkan prosedur Teorema Pythagoras yang rutin.. Bukti: Biasanya kawat tersebut dipasang pada 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter; Tentukan panjang kawat
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penerapan Teorema Pythagoras dalam konteks masalah nyata yang melibatkan perhitungan pecahan dan akar kuadrat.. Bukti: 3/4 bagian dari tinggi tiang; panjang kawat jika jarak antara kawat dan tiang pada tanah adalah 8 meter
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah berurutan: menghitung tinggi titik ikat kawat (3/4 * 8) dan kemudian menerapkan Teorema Pythagoras. Meskipun prosedurnya familiar, siswa harus mengintegrasikan informasi dari teks ke dalam model segitiga siku-siku.. Bukti: dipasang pada 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pecahan dasar dan Teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengonversi informasi teks menjadi model geometri dan menerapkan Pythagoras. Langkah-langkahnya jelas dan rutin. |

Run 3 — solusi: Tinggi kawat pada tiang = 3/4 * 8 m = 6 m. Jarak kawat ke tiang di tanah = 8 m. Panjang kawat = akar(6^2 + 8^2) = akar(36 + 64) = akar(100) = 10 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang relevan (tinggi kawat dan jarak alas), melakukan perhitungan aritmatika sederhana untuk menentukan tinggi segitiga, dan menerapkan teorema Pythagoras untuk mencari sisi miring. Ini adalah penerapan prosedur rutin pada konteks soal cerita.. Bukti: Biasanya kawat tersebut dipasang pada 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter; Tentukan panjang kawat
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menerapkan teorema Pythagoras setelah melakukan langkah awal berupa perhitungan pecahan sederhana.. Bukti: 3/4 bagian dari tinggi tiang; panjang kawat = akar(6^2 + 8^2)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah yang saling bergantung: menghitung tinggi kawat terlebih dahulu sebelum menerapkan teorema Pythagoras. Meskipun prosedurnya familiar, siswa harus mengintegrasikan informasi pecahan ke dalam model geometri.. Bukti: 3/4 bagian dari tinggi tiang; jarak antara kawat dan tiang pada tanah adalah 8 meter

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengaitkan konsep Pythagoras dengan situasi nyata sederhana yang memerlukan langkah antara (menghitung tinggi kawat). |

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
Transkripsi visual: Sebuah gambar menunjukkan tiang antena vertikal berwarna oranye dan sebuah kawat miring berwarna hitam yang menghubungkan tiang tersebut ke titik di tanah, membentuk segitiga siku-siku.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Panjang tangga adalah hipotenusa segitiga siku-siku dengan kaki 3 m dan 0,4 m. Menggunakan Teorema Pythagoras: c = akar(3^2 + 0,4^2) = akar(9 + 0,16) = akar(9,16) = 3,02 m.
Gambar sumber: images/kelas8_crop-p0041-aldo-naik-tangga.png. Transkripsi visual: Gambar menunjukkan seorang anak menaiki tangga yang bersandar pada tembok vertikal. Terdapat segitiga siku-siku yang terbentuk oleh tangga (sisi miring), tembok (sisi tegak), dan tanah (sisi alas). Tinggi tembok (sisi tegak) adalah 3 meter. Jarak alas tangga ke tembok (sisi alas) adalah 0,4 meter.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8c8a9154fc20f1bff92a6c2bb01ac76299e2b0a53382518e32e8eea2f4c15b97`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3794 |
| 2 | success | valid / verified | applying | procedural | Easy | 3811 |
| 3 | success | valid / verified | applying | procedural | Easy | 3802 |

Run 1 — solusi: Panjang tangga adalah hipotenusa segitiga siku-siku dengan kaki 3 m dan 0,4 m. Menggunakan Teorema Pythagoras: c = akar(3^2 + 0,4^2) = akar(9 + 0,16) = akar(9,16) = 3,02 m.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi situasi sebagai masalah Teorema Pythagoras dan menerapkan rumus c = akar(a^2 + b^2) secara langsung. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang penggunaan Teorema Pythagoras untuk mencari sisi miring segitiga siku-siku.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; 0.4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengenali model segitiga siku-siku dari gambar dan menerapkan rumus Pythagoras secara langsung. Tidak ada kendala kompleks atau perencanaan strategi yang diperlukan.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m

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
| gradeRelativeRationale | Soal ini adalah penerapan langsung Teorema Pythagoras yang merupakan materi standar kelas 8. Tingkat kesulitan rendah karena jalur penyelesaian sangat jelas dan tidak memerlukan manipulasi aljabar yang rumit. |

Run 2 — solusi: Panjang tangga adalah hipotenusa dari segitiga siku-siku dengan sisi tegak 3 m dan sisi alas 0,4 m. Menggunakan Teorema Pythagoras: c = akar(3^2 + 0,4^2) = akar(9 + 0,16) = akar(9,16) = 3,02 m.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi situasi sebagai masalah Teorema Pythagoras dan menerapkan rumus c = akar(a^2 + b^2) secara langsung. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan Teorema Pythagoras untuk mencari sisi miring segitiga.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi sisi-sisi segitiga dan menerapkan rumus Pythagoras. Tidak ada kendala kompleks atau langkah perencanaan yang rumit.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m

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
| gradeRelativeRationale | Soal ini adalah aplikasi standar Teorema Pythagoras yang umum diajarkan di kelas 8. Jalur penyelesaian sangat jelas dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Panjang tangga adalah sisi miring (c) dari segitiga siku-siku dengan sisi tegak a=3 m dan sisi alas b=0,4 m. Menggunakan Teorema Pythagoras: c = akar(a² + b²) = akar(3² + 0,4²) = akar(9 + 0,16) = akar(9,16) = 3,02 m.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi situasi sebagai masalah Teorema Pythagoras dan menerapkan rumus c = akar(a² + b²) secara langsung. Tidak ada langkah penalaran non-rutin atau integrasi konsep yang kompleks.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan Teorema Pythagoras untuk mencari sisi miring segitiga siku-siku.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; 0.4 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengenali model segitiga siku-siku dari konteks tangga dan menerapkan rumus Pythagoras secara langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukan panjang tangga yang digunakan Aldo.; tinggi tembok dari tumpuan tangga ke permukaan tanah adalah 3 meter. 0.4 m

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
| gradeRelativeRationale | Soal ini adalah aplikasi langsung dari Teorema Pythagoras yang merupakan materi standar kelas 8. Jalur penyelesaian sangat jelas dan familiar bagi siswa. |

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
Transkripsi visual: Gambar menunjukkan seorang anak menaiki tangga yang bersandar pada tembok vertikal. Terdapat segitiga siku-siku yang terbentuk oleh tangga (sisi miring), tembok (sisi tegak), dan tanah (sisi alas). Tinggi tembok (sisi tegak) adalah 3 meter. Jarak alas tangga ke tembok (sisi alas) adalah 0,4 meter.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `a75a3be4a28f98e263e644a4`

Seekor kucing berada di atas genting dan terlihat kebingungan karena tidak bisa turun. Aysha yang melihat kucing tersebut langsung mencari galah dan kemudian diikat dengan keranjang kecil pada ujung galah tersebut. Saat menolong kucing tersebut, Cintia melihat Aysha dan mencoba membantunya untuk mengarahkan galah yang telah diikat keranjang tepat pada titik lokasi kucing pada jarak 4 meter. Jika jarak pandangan Cintia terhadap kucing diperkirakan 5 meter.<br><br>Tentukan jarak atap yang ditempati kucing terhadap tanah tempat Aysha berdiri.

| Opsi | Isi |
|---|---|
| A | 9 meter |
| B | 5 meter |
| C | 1 meter |
| D | 3 meter |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misalkan t adalah jarak atap ke tanah (sisi tegak), 4 m adalah jarak horizontal (alas), dan 5 m adalah jarak pandang (hipotenusa). Berdasarkan Teorema Pythagoras: t² + 4² = 5². t² = 25 - 16 = 9. Maka t = √9 = 3 meter.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3adca218854500defb90c75674b0a1d97aafb4ed20e6b9defa9e775eb1abb911`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2718 |
| 2 | success | valid / verified | applying | procedural | Easy | 2720 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2670 |

Run 1 — solusi: Misalkan jarak atap ke tanah adalah t, jarak horizontal 4 m, dan jarak miring 5 m. Berdasarkan Teorema Pythagoras: t² + 4² = 5². t² = 25 - 16 = 9. Maka t = √9 = 3 meter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah segitiga siku-siku, memilih Teorema Pythagoras sebagai prosedur yang tepat, dan menerapkannya untuk mencari sisi tegak.. Bukti: jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip Teorema Pythagoras (konsep) dan menerapkan algoritma perhitungan (prosedural) untuk menyelesaikan masalah kontekstual.. Bukti: jarak 4 meter; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung Teorema Pythagoras dalam konteks sederhana. Siswa hanya perlu mengidentifikasi sisi-sisi segitiga (hipotenusa 5, alas 4) dan menghitung sisi tegak. Tidak ada kendala kompleks atau perencanaan strategi yang rumit.. Bukti: jarak 4 meter; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras (a² + b² = c²) dan operasi akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 8 karena menguji pemahaman dasar Teorema Pythagoras dengan angka yang membentuk tripel Pythagoras (3, 4, 5), yang merupakan materi standar. |

Run 2 — solusi: Jarak atap ke tanah (tinggi) adalah sisi tegak segitiga siku-siku. Dengan Teorema Pythagoras, tinggi = akar(sisi miring^2 - alas^2) = akar(5^2 - 4^2) = akar(25 - 16) = akar(9) = 3 meter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini membentuk segitiga siku-siku, di mana jarak pandang adalah sisi miring (hipotenusa) dan jarak horizontal adalah salah satu sisi tegak. Siswa menerapkan prosedur Teorema Pythagoras untuk mencari sisi tegak lainnya.. Bukti: jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip Teorema Pythagoras (konsep) dan menerapkan algoritma perhitungan akar kuadrat (prosedural) untuk menyelesaikan masalah geometri.. Bukti: jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari Teorema Pythagoras dengan angka yang familiar (tripel 3-4-5). Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan representasi masalah sederhana.. Bukti: jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; jarak 4 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah

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
| gradeRelativeRationale | Soal ini sesuai dengan standar kelas 8 untuk materi Teorema Pythagoras, di mana siswa diharapkan mampu membedakan sisi miring dan sisi tegak dalam konteks nyata sederhana. |

Run 3 — solusi: Misalkan jarak atap ke tanah adalah t, jarak horizontal 4 m, dan jarak pandang (sisi miring) 5 m. Berdasarkan Teorema Pythagoras: t² + 4² = 5². t² + 16 = 25. t² = 9. t = 3 meter.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah segitiga siku-siku, menentukan sisi-sisi yang diketahui (alas dan hipotenusa), dan menerapkan Teorema Pythagoras untuk mencari tinggi vertikal.. Bukti: jarak 4 meter; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip Teorema Pythagoras (konsep) untuk menyelesaikan masalah kontekstual.. Bukti: jarak atap yang ditempati kucing terhadap tanah; jarak 4 meter; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu memodelkan situasi ke dalam segitiga siku-siku dan menerapkan rumus Pythagoras secara langsung. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: jarak 4 meter; jarak pandangan Cintia terhadap kucing diperkirakan 5 meter; Tentukan jarak atap yang ditempati kucing terhadap tanah

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
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari Teorema Pythagoras yang merupakan materi standar kelas 8. Langkah penyelesaiannya jelas dan tidak memerlukan manipulasi aljabar yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4410`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi situasi sebagai masalah segitiga siku-siku, menentukan sisi-sisi yang diketahui (alas dan hipotenusa), dan menerapkan Teorema Pythagoras untuk mencari sisi tegak yang belum diketahui.
- Dimensi pengetahuan `procedural`: Siswa menerapkan algoritma Teorema Pythagoras (prosedural) untuk menyelesaikan masalah geometri yang diberikan dalam konteks cerita.
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung Teorema Pythagoras dengan angka yang membentuk tripel Pythagoras (3, 4, 5). Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan representasi masalah sederhana, sehingga dikategorikan Easy.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras (a² + b² = c²) dan operasi akar kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 8 karena menguji pemahaman dasar Teorema Pythagoras dengan angka yang membentuk tripel Pythagoras (3, 4, 5), yang merupakan materi standar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `7f0ea8ebdbf606480849cd78`

Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.

| Opsi | Isi |
|---|---|
| A | 9, 12, 16 |
| B | 7, 13, 11 |
| C | 6, 2,5, 6,5 |
| D | 24, 17, 25 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Tripel Pythagoras memenuhi a²+b²=c² dengan c sebagai sisi terpanjang. Opsi C: 2,5²+6² = 6,25+36 = 42,25. Karena 6,5² = 42,25, maka 2,5²+6²=6,5². Opsi lain tidak memenuhi: A (81+144=225≠256), B (49+121=170≠169), D (289+576=865≠625).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['membuktikan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `162f77d3a6b3bec5e6c37377b9289d095744ae2067e232923d09992013c691e7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2763 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2739 |
| 3 | success | valid / verified | applying | procedural | Easy | 2725 |

Run 1 — solusi: Sebuah kelompok tiga bilangan (a, b, c) dengan c sebagai bilangan terbesar adalah tripel Pythagoras jika memenuhi a² + b² = c². Untuk opsi C: 2,5² + 6² = 6,25 + 36 = 42,25. Karena 6,5² = 42,25, maka 2,5² + 6² = 6,5². Jadi, 2,5, 6, 6,5 adalah tripel Pythagoras.
- Domain kognitif `classify/applying`: Siswa diminta untuk menguji kebenaran hubungan Pythagoras pada beberapa kelompok bilangan. Ini melibatkan penerapan prosedur standar (menguadratkan dan menjumlahkan) untuk memverifikasi definisi tripel Pythagoras.. Bukti: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara sisi-sisi segitiga siku-siku (konsep) dan penggunaan algoritma perhitungan untuk memverifikasinya (prosedural).. Bukti: tripel Pythagoras; 2,5² + 6² = 6,25 + 36 = 42,25 = 6,5²
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena siswa hanya perlu melakukan verifikasi langsung menggunakan rumus Pythagoras pada setiap opsi. Tidak ada perencanaan langkah yang kompleks atau kendala yang saling berinteraksi. Prosedur yang digunakan adalah rutin dan familiar bagi siswa kelas 8.. Bukti: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.; A. 9, 12, 16; B. 7, 13, 11; C. 6, 2,5, 6,5

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar Teorema Pythagoras (a² + b² = c²). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan operasi kuadrat dan penjumlahan sederhana untuk memverifikasi tripel Pythagoras sebagai bagian dari materi dasar geometri. |

Run 2 — solusi: Tripel Pythagoras memenuhi a²+b²=c² dengan c sebagai sisi terpanjang. Untuk opsi C: 2,5²+6² = 6,25+36 = 42,25. Karena 6,5² = 42,25, maka 2,5²+6²=6,5². Opsi lain tidak memenuhi: A (81+144=225≠256), B (49+121=170≠169), D (289+576=865≠625).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengecekan teorema Pythagoras (a²+b²=c²) pada beberapa set bilangan untuk menentukan mana yang valid. Ini adalah penerapan prosedur rutin.. Bukti: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antar sisi dalam segitiga siku-siku (konsep tripel Pythagoras) dan penggunaan algoritma perhitungan kuadrat.. Bukti: tripel Pythagoras
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena siswa hanya perlu melakukan verifikasi aritmatika dasar (kuadrat dan penjumlahan) pada empat opsi yang diberikan. Prosedur pengecekan bersifat rutin dan langsung, tidak memerlukan perencanaan strategi kompleks atau integrasi kendala.. Bukti: 9, 12, 16; 7, 13, 11; 6, 2,5, 6,5; 24, 17, 25

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman teorema Pythagoras (a²+b²=c²) dan operasi hitung bilangan desimal/kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan teorema Pythagoras. Tugas ini hanya meminta verifikasi rutin tanpa manipulasi aljabar yang rumit. |

Run 3 — solusi: Uji setiap opsi dengan teorema Pythagoras a²+b²=c² (c adalah bilangan terbesar). A: 9²+12²=225≠16²=256. B: 7²+11²=170≠13²=169. C: 2,5²+6²=6,25+36=42,25=6,5². D: 17²+24²=865≠25²=625. Hanya C yang memenuhi.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur teorema Pythagoras untuk memverifikasi apakah kelompok bilangan membentuk tripel Pythagoras. Ini adalah penerapan prosedur standar.. Bukti: Buktikan bahwa diantara kelompok tiga bilangan berikut manakah yang merupakan tripel Pythagoras.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang hubungan antara sisi-sisi segitiga siku-siku (konsep tripel Pythagoras) dan penggunaan algoritmanya.. Bukti: tripel Pythagoras
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perhitungan kuadrat dan penjumlahan untuk empat opsi yang diberikan. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 9, 12, 16; 7, 13, 11; 6, 2,5, 6,5; 24, 17, 25

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras (a²+b²=c²) |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan teorema Pythagoras. Menghitung kuadrat bilangan desimal (2,5 dan 6,5) adalah beban komputasi yang wajar untuk tingkat ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4520`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur teorema Pythagoras (a²+b²=c²) untuk memverifikasi kebenaran hubungan pada beberapa set bilangan. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang hubungan antar sisi dalam segitiga siku-siku (konsep tripel Pythagoras) dan penggunaan algoritma perhitungan kuadrat.
- Intended difficulty `Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perhitungan kuadrat dan penjumlahan untuk empat opsi yang diberikan. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks. Beban komputasi desimal masih dalam batas wajar kelas 8.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras (a²+b²=c²) dan operasi hitung bilangan desimal/kuadrat. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan teorema Pythagoras. Menghitung kuadrat bilangan desimal (2,5 dan 6,5) adalah beban komputasi yang wajar untuk tingkat ini. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Pada segitiga ADC (siku-siku di D), sudut A = 60 derajat (karena sudut B=30 dan C=90). Dengan rasio 30-60-90, AD=8 cm, maka AC = 2*AD = 16 cm. Pada segitiga ABC besar, sudut B=30, sudut A=60, sudut C=90. AC=16 cm (sisi depan 30 derajat), maka AB = 2*AC = 32 cm dan BC = AC*√3 = 16√3 cm. Keliling = AB + BC + AC = 32 + 16√3 + 16 = (48 + 16√3) cm.
Gambar sumber: images/kelas8_crop-p0042-segitiga2.png. Transkripsi visual: Segitiga ABC dengan sudut siku-siku di C. Garis tinggi CD ditarik dari C ke sisi AB, membentuk sudut siku-siku di D. Diketahui panjang AD = 8 cm dan sudut B = 30 derajat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a34bd288ace0e974e2344bf5bed7b33df0dbcc78f572f70297ead0184f073b3c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3990 |
| 2 | success | valid / verified | applying | procedural | Medium | 3963 |
| 3 | success | valid / verified | applying | procedural | Medium | 4042 |

Run 1 — solusi: Pada segitiga ADC (siku-siku di D), sudut A = 60 derajat (karena sudut B=30 dan C=90). Dengan rasio 30-60-90, AD=8 cm, maka AC = 2*AD = 16 cm dan CD = 8√3 cm. Pada segitiga ABC besar, sudut B=30, sudut A=60, sudut C=90. AC=16 cm (sisi depan 30 derajat), maka AB = 2*AC = 32 cm dan BC = AC*√3 = 16√3 cm. Keliling = AB + BC + AC = 32 + 16√3 + 16 = (48 + 16√3) cm.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan konsep segitiga istimewa (30-60-90) pada dua segitiga yang saling terkait (ADC dan ABC) untuk menemukan panjang sisi-sisi yang belum diketahui sebelum menghitung keliling. Ini memerlukan penerapan konsep pada konteks rutin.. Bukti: Tentukan Keliling segitiga ABC.; segitiga siku-siku ABC; sudut B = 30 derajat; AD = 8 cm
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan rasio sisi-sisi pada segitiga istimewa (konseptual) dan menerapkan prosedur perhitungan panjang sisi tersebut (prosedural) untuk menyelesaikan masalah.. Bukti: segitiga siku-siku ABC; rasio 30-60-90
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap perhitungan yang saling bergantung (mencari sisi segitiga kecil ADC lalu menggunakan hasilnya untuk segitiga besar ABC). Siswa harus memilih prosedur yang tepat untuk rasio segitiga istimewa dan mengintegrasikan hasilnya.. Bukti: segitiga siku-siku ABC; AD = 8 cm; sudut B = 30 derajat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rasio sisi segitiga istimewa 30-60-90 dan sifat segitiga siku-siku. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan sesuai untuk kelas 8 karena melibatkan penerapan rutin konsep segitiga istimewa pada konfigurasi segitiga bertumpuk yang memerlukan ketelitian dalam langkah-langkah berurutan. |

Run 2 — solusi: Pada segitiga ADC (siku-siku di D), sudut A = 60 derajat (karena sudut B=30 dan C=90). Dengan rasio 30-60-90, AC = 2 * AD = 16 cm. Pada segitiga ABC (siku-siku di C), sudut A = 60 derajat, maka BC = AC * tan(60) = 16 * sqrt(3) cm dan AB = AC / cos(60) = 16 / 0.5 = 32 cm. Keliling = AC + BC + AB = 16 + 16sqrt(3) + 32 = (48 + 16sqrt(3)) cm.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan konsep segitiga istimewa (30-60-90) pada dua segitiga yang berbeda (ADC dan ABC) untuk menemukan panjang sisi-sisi segitiga ABC sebelum menghitung kelilingnya. Ini memerlukan penerapan konsep pada konteks rutin.. Bukti: Tentukan Keliling segitiga ABC.; segitiga siku-siku ABC; sudut B = 30 derajat; AD = 8 cm
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip segitiga istimewa dan prosedur perhitungan keliling segitiga.. Bukti: segitiga siku-siku ABC; sudut B = 30 derajat; AD = 8 cm
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang hubungan antar sisi pada segitiga istimewa dan kemampuan untuk mengidentifikasi dua segitiga yang saling terkait (ADC dan ABC). Siswa harus melakukan beberapa langkah perhitungan yang saling bergantung (mencari AC, lalu BC dan AB) sebelum menjumlahkan keliling. Ini adalah tugas rutin dengan beberapa langkah yang saling terkait.. Bukti: segitiga siku-siku ABC; sudut B = 30 derajat; AD = 8 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep segitiga istimewa 30-60-90 dan perbandingan trigonometri dasar atau rasio sisi segitiga istimewa. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan rasio sisi pada segitiga istimewa. Soal ini menuntut ketelitian dalam mengidentifikasi segitiga mana yang digunakan untuk mencari sisi tertentu, namun prosedurnya standar. |

Run 3 — solusi: Pada segitiga ADC (siku-siku di D), sudut A = 60 derajat (karena sudut B=30 dan C=90). Dengan rasio 30-60-90, jika AD=8, maka AC=16 dan CD=8√3. Pada segitiga BDC (siku-siku di D), dengan sudut B=30, maka BC = CD / sin(30) = 8√3 / 0.5 = 16√3. Sisi AB = AD + DB. DB = CD / tan(30) = 8√3 / (1/√3) = 24. Maka AB = 8 + 24 = 32. Keliling = AC + BC + AB = 16 + 16√3 + 32 = 48 + 16√3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perbandingan sisi pada segitiga istimewa (30-60-90) secara berulang untuk menemukan panjang sisi-sisi segitiga ABC (AC, BC, AB) sebelum menghitung keliling. Ini melibatkan pemilihan prosedur yang tepat dan integrasi beberapa langkah.. Bukti: Tentukan Keliling segitiga ABC; segitiga siku-siku ABC; sudut B = 30 derajat; AD = 8 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rasio sisi pada segitiga istimewa untuk menyelesaikan masalah geometri.. Bukti: segitiga siku-siku; sudut 30 derajat; rasio 30-60-90
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling bergantung (mencari sisi AC dan CD, lalu mencari sisi BC dan DB, kemudian menjumlahkan untuk keliling). Siswa harus mengidentifikasi dua segitiga siku-siku yang terbentuk oleh garis tinggi dan menerapkan rasio segitiga istimewa secara konsisten.. Bukti: Tentukan Keliling segitiga ABC; AD = 8 cm; sudut B = 30 derajat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep segitiga siku-siku, rasio sisi segitiga istimewa (30-60-90), dan definisi keliling. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menggunakan rasio segitiga istimewa. Soal ini menuntut ketelitian dalam menerapkan rasio tersebut pada dua segitiga yang berbeda namun saling berbagi sisi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `6087`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengintegrasikan konsep segitiga istimewa (30-60-90) pada dua segitiga yang saling terkait (ADC dan ABC) untuk menemukan panjang sisi-sisi yang belum diketahui sebelum menghitung keliling. Ini memerlukan penerapan konsep pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami hubungan rasio sisi-sisi pada segitiga istimewa (konseptual) dan menerapkan prosedur perhitungan panjang sisi tersebut (prosedural) untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap perhitungan yang saling bergantung (mencari sisi segitiga kecil ADC lalu menggunakan hasilnya untuk segitiga besar ABC). Siswa harus memilih prosedur yang tepat untuk rasio segitiga istimewa dan mengintegrasikan hasilnya.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rasio sisi segitiga istimewa 30-60-90 dan sifat segitiga siku-siku. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan sesuai untuk kelas 8 karena melibatkan penerapan rutin konsep segitiga istimewa pada konfigurasi segitiga bertumpuk yang memerlukan ketelitian dalam langkah-langkah berurutan. |

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
Transkripsi visual: Segitiga ABC dengan sudut siku-siku di C. Garis tinggi CD ditarik dari C ke sisi AB, membentuk sudut siku-siku di D. Diketahui panjang AD = 8 cm dan sudut B = 30 derajat.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `2ec551abe1f96d3c16146fb7`

Berikut ditunjukkan gambar rencana bangun rumah yang sedang dikerjakan oleh Amri sebagai seorang arsitek yang terlihat tampak depan. Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.<br><br>Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.

| Opsi | Isi |
|---|---|
| A | 6 meter |
| B | 8,4 meter |
| C | 3,2 meter |
| D | 5,075 meter |

![Gambar sumber soal 13](<../../../images/kelas8_crop-p0042-rencana-rumah.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `5,075 meter`.
Solusi minimum hasil AI: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Menggunakan Teorema Pythagoras: t² + 3,2² = 6². t² = 36 - 10,24 = 25,76. t = √25,76 ≈ 5,075 m.
Gambar sumber: images/kelas8_crop-p0042-rencana-rumah.png. Transkripsi visual: Gambar menunjukkan tampak depan sebuah rumah. Bagian atap berbentuk segitiga sama kaki dengan panjang sisi miring masing-masing 6 m. Lebar rumah adalah 6,4 m. Tinggi total bangunan dari dasar hingga batas bawah atap adalah 8,4 m, namun tinggi ini tidak relevan untuk menghitung tinggi atap saja.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `715156d2487a0ab9e4bc9cc22e504dad371a866241add41cc6b9c12201e1d07f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3855 |
| 2 | success | valid / verified | applying | procedural | Medium | 3842 |
| 3 | success | valid / verified | applying | procedural | Medium | 3822 |

Run 1 — solusi: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Menggunakan Teorema Pythagoras: t² + 3,2² = 6². t² = 36 - 10,24 = 25,76. t = √25,76 ≈ 5,075 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa tinggi atap membentuk segitiga siku-siku dengan setengah lebar rumah sebagai alas dan sisi miring atap sebagai hipotenusa. Ini adalah penerapan prosedur Pythagoras pada konteks geometri bangun datar.. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan geometris antara lebar rumah, sisi miring atap, dan tinggi atap (konseptual) serta menerapkan algoritma Pythagoras (prosedural).. Bukti: Tentukan tinggi atap rumah di atas; lebar rumah adalah 6.4 meter; sisi miring atap (6 m)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman untuk membagi lebar rumah menjadi dua (setengah alas segitiga) sebelum menerapkan Pythagoras. Meskipun prosedurnya rutin, terdapat langkah interpretasi visual yang diperlukan.. Bukti: lebar rumah adalah 6.4 meter; sisi miring atap (6 m); Tentukan tinggi atap rumah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan Pythagoras pada masalah geometri sederhana. Langkah membagi lebar rumah menjadi setengah adalah langkah krusial yang membedakan dari soal substitusi langsung. |

Run 2 — solusi: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Menggunakan Teorema Pythagoras: t² + 3,2² = 6². t² = 36 - 10,24 = 25,76. t = √25,76 ≈ 5,075 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa tinggi atap membentuk segitiga siku-siku dengan setengah lebar rumah sebagai alas dan sisi miring atap sebagai hipotenusa, kemudian menerapkan Teorema Pythagoras.. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman konsep Teorema Pythagoras dan prosedur perhitungan akar kuadrat untuk menyelesaikan masalah geometri.. Bukti: Tentukan tinggi atap rumah di atas; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan translasi dari konteks visual ke model matematika (segitiga siku-siku), menentukan panjang alas segitiga (setengah dari lebar rumah), dan menerapkan Teorema Pythagoras. Langkah-langkahnya rutin namun memerlukan pemahaman hubungan antar bagian bangunan.. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, konsep segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan Pythagoras pada situasi geometri sederhana. Soal memerlukan interpretasi gambar untuk menentukan panjang alas segitiga, yang merupakan langkah menengah. |

Run 3 — solusi: Atap membentuk segitiga sama kaki dengan alas 6,4 m dan sisi miring 6 m. Tinggi atap (t) membagi alas menjadi dua bagian sama panjang (3,2 m). Menggunakan Teorema Pythagoras: t² + 3,2² = 6². t² = 36 - 10,24 = 25,76. t = akar(25,76) = 5,075 m.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa tinggi atap membentuk segitiga siku-siku dengan setengah lebar rumah sebagai alas dan sisi miring atap sebagai hipotenusa, kemudian menerapkan Teorema Pythagoras.. Bukti: Tentukan tinggi atap rumah di atas, jika lebar rumah adalah 6.4 meter.; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman konsep Teorema Pythagoras dan prosedur perhitungan akar kuadrat untuk menyelesaikan masalah geometri.. Bukti: Tentukan tinggi atap rumah di atas; Kedua sisi atap rumah pada gambar masing-masing panjangnya 6 m.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan interpretasi visual (memahami bahwa tinggi atap membagi lebar rumah menjadi dua) dan menerapkan Teorema Pythagoras. Meskipun prosedurnya familiar, terdapat langkah perantara (membagi lebar rumah) yang harus dilakukan sebelum perhitungan.. Bukti: lebar rumah adalah 6.4 meter; sisi atap rumah pada gambar masing-masing panjangnya 6 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, konsep segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan Pythagoras pada konteks geometri sederhana. Langkah membagi lebar rumah menjadi setengahnya adalah langkah logis yang umum dalam geometri. |

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
Transkripsi visual: Gambar menunjukkan tampak depan sebuah rumah. Bagian atap berbentuk segitiga sama kaki dengan panjang sisi miring masing-masing 6 m. Lebar rumah adalah 6,4 m. Tinggi total bangunan dari dasar hingga batas bawah atap adalah 8,4 m, namun tinggi ini tidak relevan untuk menghitung tinggi atap saja.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `06779006c739d5de08849cb7`

Aldo dan Arjuna berdiri saling membelakangi untuk main tembak-tembakan pistol bambu. Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan. Pada saat yang sama, Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan. Pada titik terakhir, mereka berdua saling menembak.<br><br>Berapa langkah jarak kalian berdua saat mereka saling menembak?

| Opsi | Isi |
|---|---|
| A | 27 langkah |
| B | 45 langkah |
| C | 36 langkah |
| D | 63 langkah |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Misalkan posisi awal (0,0). Aldo bergerak ke depan (sumbu y) 20 langkah dan ke kanan (sumbu x) 15 langkah, posisi (15, 20). Arjuna bergerak membelakangi Aldo, ke depan (sumbu y negatif) 16 langkah dan ke kanan (sumbu x negatif) 12 langkah, posisi (-12, -16). Jarak = sqrt((15 - (-12))^2 + (20 - (-16))^2) = sqrt(27^2 + 36^2) = sqrt(729 + 1296) = sqrt(2025) = 45.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dc86e5845173329a4acc2a35c1be4eb841f87347dba5bd58a12c7e03d306fe91`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2804 |
| 2 | success | valid / verified | applying | procedural | Medium | 2826 |
| 3 | success | valid / verified | applying | procedural | Medium | 2795 |

Run 1 — solusi: Misalkan posisi awal (0,0). Aldo bergerak ke depan (sumbu y) 20 langkah dan ke kanan (sumbu x) 15 langkah, posisi (15, 20). Arjuna bergerak membelakangi Aldo, ke depan (sumbu y negatif) 16 langkah dan ke kanan (sumbu x negatif) 12 langkah, posisi (-12, -16). Jarak = sqrt((15 - (-12))^2 + (20 - (-16))^2) = sqrt(27^2 + 36^2) = sqrt(729 + 1296) = sqrt(2025) = 45.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan pergerakan dua orang dalam sistem koordinat kartesius, menentukan posisi akhir masing-masing, lalu menerapkan Teorema Pythagoras untuk mencari jarak antara dua titik tersebut. Ini melibatkan penerapan konsep pada konteks rutin.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.; Berapa langkah jarak kalian berdua saat mereka saling menembak?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma Teorema Pythagoras (prosedural) untuk menyelesaikan masalah jarak yang dimodelkan secara spasial.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang arah yang berlawanan (memodelkan posisi dalam koordinat) dan penerapan Pythagoras. Meskipun ada beberapa langkah, jalurnya cukup jelas dan familiar bagi siswa kelas 8.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, konsep koordinat kartesius dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari Pythagoras. Tantangan utama adalah memodelkan posisi 'saling membelakangi' ke dalam koordinat, yang merupakan langkah menengah. |

Run 2 — solusi: Aldo dan Arjuna berdiri saling membelakangi. Misalkan posisi awal (0,0). Aldo bergerak ke (20, 15). Arjuna bergerak ke arah berlawanan, yaitu (-16, -12). Jarak antara (20, 15) dan (-16, -12) adalah akar((20 - (-16))^2 + (15 - (-12))^2) = akar(36^2 + 27^2) = akar(1296 + 729) = akar(2025) = 45 langkah.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan posisi Aldo dan Arjuna dalam sistem koordinat kartesius, memahami konsep 'saling membelakangi' sebagai arah vektor yang berlawanan, lalu menerapkan Teorema Pythagoras untuk mencari jarak antar dua titik.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.; Berapa langkah jarak kalian berdua saat mereka saling menembak?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur Teorema Pythagoras untuk menyelesaikan masalah jarak dalam konteks geometri koordinat.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman bahwa 'saling membelakangi' berarti pergerakan mereka membentuk vektor yang berlawanan arah. Siswa harus menjumlahkan komponen pergerakan (depan-belakang dan kanan-kiri) sebelum menerapkan Pythagoras. Ini melibatkan beberapa langkah logis yang saling terkait.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.; Berapa langkah jarak kalian berdua saat mereka saling menembak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, konsep koordinat kartesius sederhana, dan penjumlahan vektor dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan Pythagoras pada situasi kontekstual. Tantangan utama adalah menginterpretasikan posisi 'saling membelakangi' untuk menentukan total selisih koordinat sebelum menghitung hipotenusa. |

Run 3 — solusi: Misalkan posisi awal (0,0). Aldo bergerak ke depan (sumbu y) 20 langkah dan ke kanan (sumbu x) 15 langkah, posisi (15, 20). Arjuna membelakangi Aldo, bergerak ke depan (sumbu y negatif) 16 langkah dan ke kanan (sumbu x negatif) 12 langkah, posisi (-12, -16). Jarak = sqrt((15 - (-12))^2 + (20 - (-16))^2) = sqrt(27^2 + 36^2) = sqrt(729 + 1296) = sqrt(2025) = 45.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan posisi kedua orang dalam koordinat kartesius, menentukan selisih posisi (jarak total horizontal dan vertikal), lalu menerapkan Teorema Pythagoras. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.; Berapa langkah jarak kalian berdua saat mereka saling menembak?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma Teorema Pythagoras (a^2 + b^2 = c^2) untuk menyelesaikan masalah jarak.. Bukti: Berapa langkah jarak kalian berdua saat mereka saling menembak?
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman arah (saling membelakangi) untuk menentukan koordinat relatif. Meskipun melibatkan beberapa langkah, prosedurnya familiar bagi kelas 8. Tidak ada kendala kompleks yang saling berinteraksi.. Bukti: Aldo berjalan 20 langkah ke depan kemudian 15 langkah ke kanan.; Arjuna juga berjalan 16 langkah ke depan kemudian 12 langkah ke kanan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan konsep koordinat kartesius dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari Pythagoras. Tantangan utama adalah memvisualisasikan posisi 'saling membelakangi' untuk menjumlahkan komponen jarak, yang merupakan langkah standar dalam pemodelan geometri. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi 12 - 5 = 7 kaki. Menggunakan Teorema Pythagoras: d = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 kaki < 30 kaki, wasit dapat mendengar atlet.
Gambar sumber: images/kelas8_crop-p0043-atlet-tenis.png. Transkripsi visual: Gambar menunjukkan seorang wasit duduk di kursi dengan tinggi 12 kaki dan seorang atlet tenis berdiri dengan tinggi 5 kaki. Jarak horizontal antara wasit dan atlet adalah 24 kaki. Ini membentuk segitiga siku-siku dengan alas 24 kaki dan tinggi vertikal 12 - 5 = 7 kaki.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ba46763973e0e9bcf94fb37d2b38767e83fc553b64c3545a098e946baf976b5f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3946 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3901 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3958 |

Run 1 — solusi: Jarak antara wasit dan atlet adalah hipotenusa dari segitiga siku-siku dengan alas 24 kaki dan tinggi 12 - 5 = 7 kaki. Menggunakan Teorema Pythagoras: d = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 kaki < 30 kaki, wasit dapat mendengar atlet.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini dapat dimodelkan sebagai segitiga siku-siku, menentukan panjang kaki-kakinya (termasuk menghitung selisih tinggi), dan menerapkan Teorema Pythagoras untuk mencari jarak miring, kemudian membandingkannya dengan ambang batas 30 kaki.. Bukti: Seorang atlet tenis mengajukan pertanyaan kepada wasit.; Berdasarkan posisi wasit dan atlet tenis pada gambar berikut.; dapatkah wasit mendengar suara sang atlet? Jelaskan jawaban kalian.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana Teorema Pythagoras diterapkan dalam situasi dunia nyata (pemodelan geometri) dan prosedur perhitungan yang terkait.. Bukti: Penerapan Teorema Pythagoras; jarak maksimum 30 kaki; selisih tinggi = 12-5=7 kaki; jarak = akar(24^2+7^2)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya sekadar memasukkan angka ke rumus, tetapi harus melakukan langkah tambahan untuk menentukan tinggi segitiga (12-5=7) sebelum menerapkan Pythagoras. Ini melibatkan pemodelan sederhana dari konteks visual.. Bukti: selisih tinggi = 12-5=7 kaki; jarak = akar(24^2+7^2) = akar(625) = 25 kaki; yang tidak melebihi 30 kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, operasi aritmatika dasar, pemahaman konsep jarak. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan situasi nyata ke dalam bentuk geometri sederhana dan melakukan perhitungan Pythagoras dasar. |

Run 2 — solusi: Jarak vertikal = 12 - 5 = 7 kaki. Jarak horizontal = 24 kaki. Jarak sebenarnya = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 < 30, wasit dapat mendengar atlet.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini membentuk segitiga siku-siku, menentukan panjang kaki-kakinya (termasuk melakukan pengurangan tinggi untuk mendapatkan tinggi segitiga), dan menerapkan Teorema Pythagoras untuk membandingkan hasilnya dengan batas jarak yang diberikan.. Bukti: Seorang atlet tenis mengajukan pertanyaan kepada wasit. Suara atlet mampu didengar wasit hanya pada jarak maksimum 30 kaki.; Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana menerapkan Teorema Pythagoras dalam konteks dunia nyata, yang memerlukan pemodelan situasi menjadi bentuk geometris.. Bukti: Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya sekadar memasukkan angka ke rumus, tetapi harus melakukan langkah tambahan yaitu menghitung selisih tinggi (12-5=7) untuk mendapatkan panjang sisi tegak segitiga sebelum menerapkan Teorema Pythagoras. Ini melibatkan perencanaan langkah yang saling bergantung.. Bukti: 12 kaki 12 kaki 5 kaki; 24 kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan operasi aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan situasi nyata ke dalam bentuk geometri dan menerapkan Pythagoras. Langkah pengurangan tinggi adalah tantangan utama yang membedakannya dari soal langsung. |

Run 3 — solusi: Jarak vertikal = 12 - 5 = 7 kaki. Jarak horizontal = 24 kaki. Jarak antara wasit dan atlet = akar(24^2 + 7^2) = akar(576 + 49) = akar(625) = 25 kaki. Karena 25 kaki < 30 kaki, maka wasit dapat mendengar suara atlet.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa situasi ini dapat dimodelkan sebagai segitiga siku-siku, menentukan panjang kaki-kaki segitiga (selisih tinggi dan jarak horizontal), dan menerapkan Teorema Pythagoras untuk membandingkan hasilnya dengan batas jarak yang diberikan.. Bukti: Seorang atlet tenis mengajukan pertanyaan kepada wasit. Suara atlet mampu didengar wasit hanya pada jarak maksimum 30 kaki.; Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet?
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan prinsip Teorema Pythagoras (konsep) untuk menyelesaikan masalah kontekstual yang melibatkan pemodelan geometri.. Bukti: Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemodelan situasi nyata ke dalam bentuk geometri (segitiga siku-siku). Siswa harus menyadari bahwa tinggi vertikal segitiga adalah selisih tinggi kedua objek (12-5=7), bukan menggunakan angka 12 atau 5 secara langsung. Meskipun prosedurnya familiar, langkah pemodelan ini merupakan langkah krusial yang membedakan dari soal yang hanya meminta substitusi langsung.. Bukti: Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet?; 24 kaki 12 kaki 5 kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, operasi aritmatika dasar, pemahaman konsep jarak dalam geometri. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menerapkan Teorema Pythagoras pada masalah kontekstual. Tantangan utama adalah menerjemahkan gambar ke model matematika yang tepat (menentukan kaki segitiga). |

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
Subtopik: Penerapan Teorema Pythagoras
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang atlet tenis mengajukan pertanyaan kepada wasit. Suara atlet mampu didengar wasit hanya pada jarak maksimum 30 kaki. Berdasarkan posisi wasit dan atlet tenis pada gambar berikut. 24 kaki 12 kaki 5 kaki

Berdasarkan posisi wasit dan atlet tenis pada gambar berikut, dapatkah wasit mendengar suara sang atlet? Jelaskan jawaban kalian.
Pilihan: A. Ya, karena jarak keduanya 25 kaki (kurang dari 30 kaki)
B. Tidak, karena jarak keduanya 36 kaki
C. Tidak, karena jarak keduanya 31 kaki (lebih dari 30 kaki)
D. Ya, karena jarak keduanya 24 kaki
Transkripsi visual: Gambar menunjukkan seorang wasit duduk di kursi dengan tinggi 12 kaki dan seorang atlet tenis berdiri dengan tinggi 5 kaki. Jarak horizontal antara wasit dan atlet adalah 24 kaki. Ini membentuk segitiga siku-siku dengan alas 24 kaki dan tinggi vertikal 12 - 5 = 7 kaki.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `e8e1147bfed27b5d98b29d8f`

Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.<br><br>Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, segitiga ABC siku-siku di C |
| B | Ya, segitiga ABC siku-siku di B |
| C | Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras |
| D | Tidak, karena AB² + BC² tidak sama dengan CA² |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `92005ccc8d7910717d7932442a0982c657ec7675ee51290ea1efa411452fd576`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2792 |
| 2 | success | valid / verified | applying | procedural | Medium | 2906 |
| 3 | success | valid / verified | applying | procedural | Medium | 2766 |

Run 1 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus jarak (atau kuadrat jarak) untuk ketiga sisi segitiga dan kemudian menggunakan kebalikan Teorema Pythagoras untuk memverifikasi sifat segitiga siku-siku. Ini adalah penerapan prosedur yang dipelajari pada konteks koordinat.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku? Jelaskan.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme (rumus jarak) dan kriteria (kebalikan Teorema Pythagoras) untuk menentukan sifat geometris segitiga.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: menghitung tiga jarak (atau kuadrat jarak) dan melakukan verifikasi hubungan Pythagoras. Meskipun prosedurnya rutin, siswa harus mengelola perhitungan koordinat negatif dan mengintegrasikan hasil untuk menarik kesimpulan.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku? Jelaskan.

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menghitung jarak antar titik dan menerapkan kebalikan Teorema Pythagoras. Beban kognitif berasal dari keharusan menghitung tiga sisi secara akurat dan membandingkannya, bukan dari konsep yang sangat abstrak. |

Run 2 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC adalah segitiga siku-siku di B.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus jarak (atau teorema Pythagoras) untuk menentukan sifat segitiga berdasarkan koordinat titik-titiknya. Ini memerlukan penerapan prosedur yang sudah dipelajari ke dalam konteks pembuktian sifat geometri.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku? Jelaskan.; AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68; karena AB²+BC²=50+18=68=CA²
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma rumus jarak dan kriteria segitiga siku-siku (kebalikan teorema Pythagoras).. Bukti: AB²=(4-(-1))²+(-2-3)²=50, BC²=(1-4)²+(-5-(-2))²=18, CA²=(-1-1)²+(3-(-5))²=68
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah sistematis: menghitung panjang ketiga sisi menggunakan rumus jarak, menguadratkannya, dan memverifikasi hubungan Pythagoras. Meskipun prosedurnya rutin, siswa harus melakukan perhitungan dengan teliti pada koordinat negatif dan mengintegrasikan hasil tersebut untuk menarik kesimpulan.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).; Apakah segitiga ABC merupakan segitiga siku-siku?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus jarak antara dua titik pada bidang koordinat dan Teorema Pythagoras. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menghitung jarak antar titik dan menerapkan teorema Pythagoras. Soal ini menuntut ketelitian dalam operasi bilangan bulat dan pemahaman konsep kebalikan teorema Pythagoras. |

Run 3 — solusi: Hitung kuadrat panjang sisi: AB² = (4 - (-1))² + (-2 - 3)² = 5² + (-5)² = 25 + 25 = 50. BC² = (1 - 4)² + (-5 - (-2))² = (-3)² + (-3)² = 9 + 9 = 18. AC² = (1 - (-1))² + (-5 - 3)² = 2² + (-8)² = 4 + 64 = 68. Karena AB² + BC² = 50 + 18 = 68 = AC², maka menurut kebalikan Teorema Pythagoras, segitiga ABC siku-siku di B.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus jarak untuk menghitung panjang sisi-sisi segitiga, lalu menggunakan kebalikan Teorema Pythagoras untuk menentukan jenis segitiga. Ini adalah penerapan prosedur yang sudah dipelajari pada konteks geometri koordinat.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku? Jelaskan.
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang rumus jarak (prosedural) dan prinsip Teorema Pythagoras (konseptual) untuk memverifikasi sifat segitiga.. Bukti: Diketahui ΔABC dengan titik-titik A(-1, 3), B(4, -2), dan C(1, -5).
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah sistematis: menghitung tiga panjang sisi menggunakan rumus jarak, menguadratkannya, dan memverifikasi hubungan Pythagoras. Meskipun prosedurnya rutin, siswa harus melakukan perhitungan dengan teliti dan mengintegrasikan hasil untuk menarik kesimpulan.. Bukti: Apakah segitiga ABC merupakan segitiga siku-siku? Jelaskan.

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menghitung jarak antar titik dan menerapkan Teorema Pythagoras. Langkah-langkahnya jelas namun memerlukan ketelitian dalam operasi bilangan negatif. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Substitusi koordinat A(-2,-1) dan B(3,11) ke rumus: AB = sqrt((3 - (-2))^2 + (11 - (-1))^2) = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13.
Gambar sumber: images/kelas8_crop-p0044-segitiga1.png. Transkripsi visual: Gambar menunjukkan segitiga siku-siku ABC pada bidang koordinat Kartesius. Titik A berada di (x1, y1), titik C di (x2, y1), dan titik B di (x2, y2). Sisi AC memiliki panjang (x2 - x1) dan sisi BC memiliki panjang (y2 - y1). Sudut siku-siku berada di titik C. Rumus jarak AB diberikan sebagai AB = akar((x2 - x1)^2 + (y2 - y1)^2).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `14dccce0bd68af91f6462a2f5ec42b0d7defdeac618a3f2b1b21cc926afe17a3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 4010 |
| 2 | success | valid / verified | applying | procedural | Easy | 3932 |
| 3 | success | valid / verified | applying | procedural | Easy | 3906 |

Run 1 — solusi: Substitusi koordinat A(-2,-1) dan B(3,11) ke rumus: AB = sqrt((3 - (-2))^2 + (11 - (-1))^2) = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus yang sudah disediakan secara eksplisit dalam teks soal. Siswa hanya perlu melakukan substitusi nilai koordinat ke dalam rumus dan melakukan operasi aritmatika dasar.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?; AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Dimensi pengetahuan `classify/procedural`: Soal menguji kemampuan siswa dalam menggunakan prosedur (rumus jarak) yang telah diberikan untuk menyelesaikan masalah numerik.. Bukti: AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena rumus sudah diberikan secara eksplisit. Siswa hanya perlu melakukan substitusi dan perhitungan aritmatika sederhana. Tidak ada perencanaan strategi yang kompleks atau kendala yang berinteraksi.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?; AB=sqrt((x2-x1)^2+(y2-y1)^2)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi bilangan bulat (termasuk pengurangan bilangan negatif) dan operasi akar kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan Teorema Pythagoras dan operasi bilangan bulat. Soal memberikan rumus secara langsung, sehingga mengurangi beban kognitif secara signifikan. |

Run 2 — solusi: Substitusi koordinat A(-2,-1) dan B(3,11) ke rumus: AB = sqrt((3 - (-2))^2 + (11 - (-1))^2) = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus jarak yang sudah diberikan secara eksplisit dalam soal ke dalam koordinat yang spesifik. Ini adalah penerapan prosedur langsung.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?; AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Dimensi pengetahuan `classify/procedural`: Siswa diminta menggunakan algoritma atau rumus yang sudah disediakan untuk menyelesaikan masalah numerik.. Bukti: AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Intended difficulty `classify/Easy`: Soal memberikan rumus secara eksplisit dan meminta substitusi langsung. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi. Tingkat kesulitan rendah karena jalur penyelesaian sangat jelas.. Bukti: AB=sqrt((x2-x1)^2+(y2-y1)^2); Diketahui titik A(-2,-1) dan B(3,11)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi bilangan bulat (termasuk pengurangan bilangan negatif) dan operasi akar kuadrat dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat terbantu dengan rumus yang sudah diberikan di stem soal, sehingga siswa hanya perlu melakukan substitusi dan aritmatika dasar. Ini sesuai dengan ekspektasi kemampuan kelas 8. |

Run 3 — solusi: AB = sqrt((3 - (-2))^2 + (11 - (-1))^2) = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan rumus jarak yang sudah diberikan secara eksplisit dalam soal ke dalam koordinat yang spesifik. Ini adalah penerapan prosedur langsung.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?; AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menggunakan algoritma (rumus jarak) untuk menyelesaikan masalah.. Bukti: AB=sqrt((x2-x1)^2+(y2-y1)^2)
- Intended difficulty `classify/Easy`: Soal memberikan rumus secara eksplisit dan meminta substitusi nilai. Langkah-langkahnya rutin dan terarah. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: Diketahui titik A(-2,-1) dan B(3,11). Bagaimana panjang AB?; AB=sqrt((x2-x1)^2+(y2-y1)^2)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi bilangan bulat (termasuk pengurangan bilangan negatif), kuadrat, dan akar kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat terbantu dengan rumus yang sudah disediakan di stem soal, sehingga siswa hanya perlu melakukan substitusi dan aritmatika dasar. Ini sesuai dengan tingkat kemudahan untuk kelas 8. |

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
Transkripsi visual: Gambar menunjukkan segitiga siku-siku ABC pada bidang koordinat Kartesius. Titik A berada di (x1, y1), titik C di (x2, y1), dan titik B di (x2, y2). Sisi AC memiliki panjang (x2 - x1) dan sisi BC memiliki panjang (y2 - y1). Sudut siku-siku berada di titik C. Rumus jarak AB diberikan sebagai AB = akar((x2 - x1)^2 + (y2 - y1)^2).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Misal CE \|\| AD. Maka ∠AEC = ∠BAD (sudut sehadap) dan ∠ACE = ∠DAC (sudut berseberangan dalam). Karena AD adalah garis bagi, maka ∠BAD = ∠DAC. Akibatnya, ∠AEC = ∠ACE. Karena dua sudut alas segitiga ACE sama besar, maka segitiga ACE adalah segitiga sama kaki dengan AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik B, D, C terletak pada satu garis lurus.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a22a01dd61d8d1b76ea0f664d1ab3912081214cf0f74c06e0dc90f8a774f22ed`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 3873 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 3873 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3836 |

Run 1 — solusi: AD \|\| CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka, sudut AEC = sudut ACE. Karena dua sudut alas segitiga ACE sama besar, maka segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan pembuktian geometris dengan bantuan konstruksi tambahan. Siswa harus mengintegrasikan sifat garis sejajar (sudut sehadap dan berseberangan) dengan definisi garis bagi untuk menyimpulkan sifat segitiga sama kaki. Ini melampaui sekadar prosedur rutin.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; Beri alasan bahwa ΔACE sama kaki.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara konsep garis sejajar, sudut-sudut yang terbentuk (sehadap, berseberangan), dan sifat segitiga sama kaki untuk membangun argumen logis.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard karena meskipun petunjuk konstruksi diberikan, siswa harus melakukan penalaran deduktif untuk menghubungkan sudut-sudut yang terbentuk oleh garis sejajar dengan sifat segitiga sama kaki. Ini memerlukan integrasi konsep geometri yang lebih dalam daripada sekadar penerapan rumus langsung.. Bukti: Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan dalam) dan sifat segitiga sama kaki. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi kesebangunan ada di kelas 8, pembuktian geometris seperti ini menuntut kemampuan penalaran yang tinggi bagi siswa kelas 8, terutama dalam mengaitkan konstruksi tambahan dengan sifat sudut. |

Run 2 — solusi: Misalkan AD \|\| CE. Sudut BAD = sudut AEC (sehadap) dan sudut DAC = sudut ACE (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka, sudut AEC = sudut ACE. Dalam segitiga ACE, karena sudut-sudut alasnya sama (sudut AEC = sudut ACE), maka segitiga ACE adalah segitiga sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana dengan mengikuti petunjuk konstruksi yang diberikan. Siswa perlu mengintegrasikan hubungan sudut (sehadap dan berseberangan dalam) untuk menyimpulkan sifat segitiga sama kaki.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; Beri alasan bahwa ΔACE sama kaki.
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip-prinsip geometri (garis sejajar, sudut, dan sifat segitiga sama kaki) dan menerapkannya dalam konteks pembuktian.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun petunjuk konstruksi diberikan, siswa harus menghubungkan beberapa konsep geometri (sudut sehadap, sudut berseberangan dalam, dan sifat segitiga sama kaki) untuk mencapai kesimpulan. Ini bukan sekadar penerapan rumus langsung, melainkan memerlukan penalaran logis langkah demi langkah.. Bukti: Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang garis sejajar, sudut sehadap, sudut berseberangan dalam, dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi kesebangunan diajarkan di kelas 8, pembuktian geometris dengan konstruksi tambahan menuntut kemampuan penalaran yang lebih tinggi daripada sekadar menghitung panjang sisi. |

Run 3 — solusi: Misal CE \|\| AD. ∠AEC = ∠BAD (sehadap) dan ∠ACE = ∠DAC (berseberangan dalam). Karena ∠BAD = ∠DAC (AD garis bagi), maka ∠AEC = ∠ACE. Segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk melakukan pembuktian geometris sederhana dengan mengikuti petunjuk konstruksi yang diberikan. Ini melibatkan penerapan konsep sudut pada garis sejajar dan sifat segitiga sama kaki, yang merupakan proses penalaran logis.. Bukti: Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan sudut-sudut pada garis sejajar dan sifat segitiga sama kaki, serta bagaimana mengintegrasikan konsep-konsep tersebut untuk membuktikan suatu pernyataan.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium. Meskipun petunjuk konstruksi diberikan, siswa harus mampu menghubungkan hubungan sudut (sehadap dan berseberangan) dengan sifat segitiga sama kaki secara mandiri. Ini memerlukan perencanaan langkah-langkah logis yang saling bergantung, namun prosedurnya cukup standar untuk materi geometri kelas 8.. Bukti: Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan dalam) dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari kesebangunan dan garis sejajar. Soal ini menuntut kemampuan deduktif yang sesuai dengan tingkat kognitif kelas 8, di mana petunjuk diberikan namun justifikasi tetap harus dibangun oleh siswa. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Hard": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5680`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini menuntut penalaran deduktif untuk menghubungkan konstruksi tambahan (garis sejajar) dengan sifat sudut (sehadap dan berseberangan) untuk menyimpulkan sifat segitiga sama kaki. Ini bukan sekadar prosedur rutin, melainkan proses pembuktian geometris.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami hubungan konseptual antara garis sejajar, sudut-sudut yang terbentuk, dan definisi segitiga sama kaki untuk membangun argumen logis.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium. Meskipun petunjuk konstruksi diberikan, siswa harus menghubungkan beberapa konsep geometri (sudut sehadap, sudut berseberangan dalam, dan sifat segitiga sama kaki) untuk mencapai kesimpulan. Ini memerlukan perencanaan langkah-langkah logis yang saling bergantung, namun prosedurnya cukup standar untuk materi geometri kelas 8.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan dalam) dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari kesebangunan dan garis sejajar. Soal ini menuntut kemampuan deduktif yang sesuai dengan tingkat kognitif kelas 8, di mana petunjuk diberikan namun justifikasi tetap harus dibangun oleh siswa. |

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
Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik B, D, C terletak pada satu garis lurus.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `51def5fab754abff1aeeed28`

Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.<br><br>Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.

| Opsi | Isi |
|---|---|
| A | 108.000 + y = 220.000 (y = uang Dhoni) |
| B | 108.000 - y = 220.000 (y = uang Dhoni) |
| C | 108.000 x y = 220.000 (y = uang Dhoni) |
| D | 220.000 + y = 108.000 (y = uang Dhoni) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Misalkan y adalah uang Dhoni. Diketahui uang Ahmad = 108.000 dan total uang = 220.000. Karena total uang adalah jumlah uang Ahmad dan Dhoni, maka persamaannya adalah 108.000 + y = 220.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0ed06f2f960cf73e94716cecd1b28c93948030c8853eaa8d84a0825c746ac777`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2692 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2683 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2713 |

Run 1 — solusi: Misalkan y adalah uang Dhoni. Diketahui uang Ahmad = 108.000 dan total uang = 220.000. Karena total uang adalah jumlah uang Ahmad dan Dhoni, maka persamaannya adalah 108.000 + y = 220.000.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi kontekstual ke dalam bentuk model matematika (persamaan linear satu variabel). Ini merupakan penerapan konsep dasar PLSV dalam konteks rutin.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana hubungan antar variabel dalam situasi nyata direpresentasikan ke dalam bentuk persamaan linear.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menerjemahkan pernyataan verbal langsung ke dalam bentuk persamaan linear satu variabel tanpa perlu melakukan manipulasi aljabar yang kompleks atau perencanaan strategi yang rumit.. Bukti: Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi penjumlahan dan konsep variabel dalam persamaan linear. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah terbiasa dengan pemodelan matematika sederhana untuk PLSV. Soal ini tidak memerlukan langkah-langkah yang saling bergantung atau perencanaan yang kompleks. |

Run 2 — solusi: Misalkan y adalah uang Dhoni. Total uang Ahmad dan Dhoni adalah 108.000 + y = 220.000.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan situasi kontekstual ke dalam bentuk persamaan linier satu variabel. Siswa perlu memahami hubungan penjumlahan antara dua variabel (uang Ahmad dan uang Dhoni) untuk membentuk persamaan yang tepat.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep dasar persamaan linier satu variabel dan bagaimana merepresentasikan hubungan kuantitatif dalam bentuk simbolik.. Bukti: 108.000 + y = 220.000 (y = uang Dhoni)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi komponen (bagian dan total) dan menyusunnya ke dalam operasi penjumlahan yang sesuai. Tidak ada kendala yang kompleks atau langkah perencanaan yang rumit.. Bukti: Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari. Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi penjumlahan dan konsep variabel dalam persamaan linier. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah terbiasa dengan pemodelan aljabar sederhana seperti ini. Soal tidak menuntut manipulasi aljabar yang kompleks, hanya pembentukan model. |

Run 3 — solusi: Misalkan y adalah uang Dhoni. Total uang Ahmad dan Dhoni adalah 220.000. Karena uang Ahmad 108.000, maka persamaannya adalah 108.000 + y = 220.000.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan situasi verbal ke dalam bentuk persamaan linier satu variabel. Ini adalah penerapan langsung dari konsep dasar PLSV, sehingga termasuk dalam domain applying.. Bukti: Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara komponen-komponen dalam masalah (uang Ahmad, uang Dhoni, total uang) dan bagaimana merepresentasikannya dalam bentuk persamaan matematis, yang merupakan pengetahuan konseptual.. Bukti: Ahmad dan Dhoni adalah teman dekat yang akan membeli buku dengan mengumpulkan uang saku selama beberapa hari.; Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu mengidentifikasi komponen yang diketahui dan menjumlahkannya untuk membentuk persamaan. Tidak ada langkah yang saling bergantung yang rumit atau kendala yang harus diintegrasikan.. Bukti: Uang Ahmad adalah Rp. 108.000,00. Total uang kaduannya Rp 220.000,00.; Berapa persamaan yang kalian gunakan untuk menentukan jumlah uang Dhoni.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi penjumlahan dan konsep variabel dalam persamaan linier. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 8, di mana siswa diharapkan sudah mampu memodelkan masalah sehari-hari ke dalam bentuk persamaan linier satu variabel sederhana. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `d490723c72a0d7e848c344b2`

Perhatikan beberapa kalimat berikut:<br>1. Bilangan prima terkecil adalah 3.<br>2. Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil.<br>3. Empat merupakan bilangan ganjil.<br>4. Jayapura merupakan ibu kota provinsi Papua.<br>5. Pegunungan Lantimojong berada di Sulawesi Utara.<br>Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?

| Opsi | Isi |
|---|---|
| A | Jika a adalah bilangan asli, maka 2a + 6 adalah bilangan ganjil. |
| B | Bilangan prima terkecil adalah 3. |
| C | Empat merupakan bilangan ganjil. |
| D | Jayapura merupakan ibu kota provinsi Papua. |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pernyataan 1 salah karena bilangan prima terkecil adalah 2. Pernyataan 2 salah karena 2a+6 selalu genap untuk a bilangan asli. Pernyataan 3 salah karena 4 adalah bilangan genap. Pernyataan 5 salah karena Pegunungan Lantimojong berada di Sulawesi Selatan. Pernyataan 4 benar karena Jayapura adalah ibu kota provinsi Papua.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe8a856bfd051b520bb188c02b3ebfde06abc6ae38d9b19d8fccee7cce8741bb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3933 |
| 2 | success | valid / verified | knowing | factual | Easy | 3524 |
| 3 | success | valid / verified | knowing | factual | Easy | 3535 |

Run 1 — solusi: Pernyataan 1 salah karena bilangan prima terkecil adalah 2. Pernyataan 2 salah karena 2a+6 selalu genap untuk a bilangan asli. Pernyataan 3 salah karena 4 adalah bilangan genap. Pernyataan 5 salah karena Pegunungan Lantimojong berada di Sulawesi Selatan. Pernyataan 4 benar karena Jayapura adalah ibu kota provinsi Papua.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi kebenaran dari beberapa pernyataan faktual secara langsung tanpa memerlukan prosedur matematis yang kompleks atau penalaran strategis.. Bukti: Bilangan prima terkecil adalah 3.; Empat merupakan bilangan ganjil.; Jayapura merupakan ibu kota provinsi Papua.
- Dimensi pengetahuan `classify/factual`: Tugas ini menguji pengetahuan faktual mengenai definisi bilangan prima, paritas bilangan, dan pengetahuan umum geografi.. Bukti: Bilangan prima terkecil adalah 3.; Empat merupakan bilangan ganjil.; Jayapura merupakan ibu kota provinsi Papua.
- Intended difficulty `classify/Easy`: Soal bersifat langsung dengan jalur penyelesaian yang jelas. Siswa hanya perlu mengevaluasi kebenaran setiap pernyataan secara terpisah.. Bukti: Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang bilangan prima, paritas bilangan, dan geografi dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas evaluasi kebenaran pernyataan faktual merupakan aktivitas rutin yang sesuai untuk tingkat kelas 8. |

Run 2 — solusi: Kalimat 1 salah karena bilangan prima terkecil adalah 2. Kalimat 2 salah karena 2a+6 selalu genap untuk a bilangan asli. Kalimat 3 salah karena 4 adalah bilangan genap. Kalimat 5 salah karena Pegunungan Latimojong berada di Sulawesi Selatan. Kalimat 4 benar karena Jayapura adalah ibu kota provinsi Papua.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menentukan nilai kebenaran dari beberapa kalimat. Proses ini melibatkan pengenalan fakta dasar dan prosedur aljabar sederhana untuk mengevaluasi pernyataan, yang termasuk dalam domain knowing.. Bukti: Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman siswa terhadap definisi bilangan (prima, genap/ganjil) dan fakta umum, yang merupakan pengetahuan faktual.. Bukti: Bilangan prima terkecil adalah 3.; Empat merupakan bilangan ganjil.; Jayapura merupakan ibu kota provinsi Papua.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct) dengan jalur penyelesaian yang jelas. Siswa hanya perlu mengevaluasi kebenaran setiap pernyataan satu per satu tanpa memerlukan perencanaan strategi yang kompleks atau integrasi antar konsep yang sulit.. Bukti: Perhatikan beberapa kalimat berikut:; Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?

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
| gradeRelativeRationale | Soal ini merupakan latihan standar untuk membedakan pernyataan dan kalimat terbuka dalam materi aljabar kelas 8, dengan tingkat tuntutan kognitif yang rendah. |

Run 3 — solusi: Evaluasi kebenaran setiap kalimat: (1) Salah, prima terkecil adalah 2. (2) Salah, 2a+6 selalu genap untuk a bilangan asli. (3) Salah, 4 adalah bilangan genap. (4) Benar, Jayapura adalah ibu kota Papua. (5) Salah, Pegunungan Latimojong berada di Sulawesi Selatan. Jadi, pernyataan yang benar adalah kalimat ke-4.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi kebenaran dari beberapa kalimat faktual dan matematis sederhana. Ini adalah tugas pengenalan konsep pernyataan dalam bab PLSV.. Bukti: Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui fakta dasar matematika (bilangan prima, paritas) dan pengetahuan umum untuk menentukan nilai kebenaran pernyataan.. Bukti: Bilangan prima terkecil adalah 3.; Empat merupakan bilangan ganjil.; Jayapura merupakan ibu kota provinsi Papua.
- Intended difficulty `classify/Easy`: Soal bersifat langsung dengan jalur penyelesaian yang jelas. Siswa hanya perlu mengevaluasi kebenaran masing-masing kalimat secara terpisah tanpa ada ketergantungan antar langkah atau kendala yang kompleks.. Bukti: Perhatikan beberapa kalimat berikut:; Berdasarkan beberapa kalimat di atas, manakah yang termasuk pernyataan yang benar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang bilangan prima, bilangan genap/ganjil, dan geografi dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas ini merupakan latihan dasar untuk membedakan pernyataan dan kalimat terbuka, yang merupakan prasyarat standar di kelas 8. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `d8ebb6f2c60e468be6bc868a`

x + 13 = 1<br><br>Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.

| Opsi | Isi |
|---|---|
| A | x = 12 |
| B | x = -12 |
| C | x = 14 |
| D | x = -14 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: x + 13 = 1. Kurangi kedua ruas dengan 13: x = 1 - 13. Maka, x = -12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7db890323ca4068b04efd581fc9029eadac02dc470b94748ab433769d87820e7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2449 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2454 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2483 |

Run 1 — solusi: x + 13 = 1. Kurangi kedua ruas dengan 13: x = 1 - 13. Maka, x = -12.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan prosedur aljabar dasar (mengurangi kedua ruas dengan konstanta yang sama) untuk mengisolasi variabel x. Ini adalah prosedur standar yang langsung.. Bukti: x + 13 = 1; Tentukan nilai x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme dasar penyelesaian persamaan linier satu variabel, yang merupakan prosedur rutin.. Bukti: x + 13 = 1
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu melakukan satu langkah operasi (pengurangan) untuk mendapatkan nilai x. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: x + 13 = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi bilangan bulat dan konsep persamaan linier satu variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal tingkat dasar untuk kelas 8 yang menguji kemampuan manipulasi aljabar satu langkah. |

Run 2 — solusi: x + 13 = 1. Kurangi kedua ruas dengan 13: x = 1 - 13. Maka x = -12.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan prosedur aljabar dasar (mengurangi kedua ruas dengan konstanta yang sama) untuk mengisolasi variabel x. Ini adalah prosedur rutin yang langsung.. Bukti: x + 13 = 1; Tentukan nilai x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma dasar penyelesaian persamaan linier satu variabel (prosedural).. Bukti: x + 13 = 1
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 8. Hanya memerlukan satu langkah penyelesaian (subtraksi) dengan angka yang sederhana. Tidak ada kendala atau perencanaan yang kompleks.. Bukti: x + 13 = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan bulat (penjumlahan dan pengurangan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Persamaan linier satu variabel adalah materi dasar kelas 7 dan 8. Soal ini merupakan bentuk paling sederhana dari persamaan tersebut. |

Run 3 — solusi: x + 13 = 1. Kurangi kedua ruas dengan 13: x = 1 - 13. Maka, x = -12.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur aljabar dasar untuk mengisolasi variabel x dengan operasi invers (pengurangan). Ini adalah penerapan langsung dari prosedur penyelesaian persamaan linier satu variabel.. Bukti: x + 13 = 1; Tentukan nilai x
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritme dasar dalam menyelesaikan persamaan linier satu variabel, yaitu prinsip kesetaraan (mengurangi kedua ruas dengan angka yang sama).. Bukti: x + 13 = 1
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 8. Hanya memerlukan satu langkah operasi (pengurangan) untuk mendapatkan nilai x. Tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: x + 13 = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi penjumlahan dan pengurangan bilangan bulat serta konsep persamaan linier satu variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar kompetensi dasar kelas 8 dalam menyelesaikan PLSV. Tingkat kesulitan rendah karena hanya melibatkan satu langkah operasional langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `117a580f4aab83cd83040024bbf64d9d9be204df57fab6dd429b95723a938f9d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2532 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2532 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2522 |

Run 1 — solusi: 3x + 5 = -10; 3x = -10 - 5; 3x = -15; x = -15 / 3; x = -5.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur aljabar standar untuk menyelesaikan persamaan linier satu variabel. Siswa hanya perlu menerapkan operasi invers (pengurangan dan pembagian) secara langsung.. Bukti: 3 x + 5 = -10; Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang langkah-langkah penyelesaian persamaan linier satu variabel (manipulasi aljabar dasar).. Bukti: 3 x + 5 = -10
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan dua langkah aljabar dasar (pengurangan dan pembagian) tanpa ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: 3 x + 5 = -10

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
| gradeRelativeRationale | Persamaan linier satu variabel adalah materi dasar kelas 8. Soal ini tidak memerlukan manipulasi kompleks, hanya operasi aritmatika dasar pada bilangan bulat negatif. |

Run 2 — solusi: 3x + 5 = -10; 3x = -10 - 5; 3x = -15; x = -15 / 3; x = -5.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur aljabar standar untuk menyelesaikan persamaan linier satu variabel. Siswa hanya perlu menerapkan operasi invers (pengurangan dan pembagian) secara langsung.. Bukti: 3 x + 5 = -10; Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang langkah-langkah penyelesaian persamaan linier satu variabel (manipulasi aljabar dasar).. Bukti: 3 x + 5 = -10
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari prosedur penyelesaian persamaan linier satu variabel yang sangat familiar bagi siswa kelas 8. Tidak ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.. Bukti: 3 x + 5 = -10

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
| gradeRelativeRationale | Persamaan linier satu variabel adalah materi dasar kelas 8. Soal ini tidak memerlukan manipulasi kompleks atau pemodelan, sehingga dikategorikan mudah. |

Run 3 — solusi: 3x + 5 = -10; 3x = -10 - 5; 3x = -15; x = -15 / 3; x = -5.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur aljabar standar untuk menyelesaikan persamaan linier satu variabel. Siswa hanya perlu menerapkan operasi invers (pengurangan dan pembagian) secara langsung.. Bukti: 3 x + 5 = -10; Tentukan nilai x yang menjadikan persamaan di atas bernilai benar.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma dasar dalam menyelesaikan persamaan linier satu variabel (prosedural).. Bukti: 3 x + 5 = -10
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari prosedur penyelesaian persamaan linier satu variabel yang sangat familiar bagi siswa kelas 8. Tidak ada langkah yang kompleks atau kendala yang berinteraksi.. Bukti: 3 x + 5 = -10

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
| gradeRelativeRationale | Persamaan linier satu variabel dengan koefisien dan konstanta bilangan bulat adalah materi dasar kelas 7 yang terus digunakan di kelas 8. Soal ini sangat rutin dan langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `69f14f018149ed7308b7751c`

Sekolah menyelenggarakan proyek penguatan proil pelajar Pancasila pada tema kearifan lokal untuk melakukan observasi menggunakan lima bus yang dapat mengangkut hanya 290 penumpang.<br><br>Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

| Opsi | Isi |
|---|---|
| A | 5x ≥ 290 (x = banyak penumpang per bus) |
| B | x ≤ 290 (x = banyak penumpang per bus) |
| C | 5x ≤ 290 (x = banyak penumpang per bus) |
| D | 5x < 290 (x = banyak penumpang per bus) |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Misalkan x adalah banyak penumpang per bus. Karena terdapat 5 bus dan total penumpang tidak boleh melebihi 290, maka 5 dikali x harus kurang dari atau sama dengan 290. Modelnya adalah 5x ≤ 290.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `844553068f524f1afc0d73e7f114136d076cccef74b6e1c974dcaf4be4ea0d2e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2659 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2623 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2662 |

Run 1 — solusi: Misalkan x adalah banyak penumpang per bus. Karena terdapat 5 bus dan total penumpang tidak boleh melebihi 290, maka 5 dikali x harus kurang dari atau sama dengan 290. Modelnya adalah 5x ≤ 290.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi kontekstual ke dalam model matematika berupa pertidaksamaan linier satu variabel. Ini melibatkan pemahaman konsep hubungan 'tidak lebih dari' sebagai simbol ≤ dan mengaitkan variabel dengan jumlah bus.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana menerjemahkan pernyataan verbal ke dalam notasi matematika pertidaksamaan linier.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu mengidentifikasi variabel (x), koefisien (5), dan relasi pertidaksamaan yang tepat ('hanya' berarti maksimal atau ≤). Tidak ada kendala yang berinteraksi atau langkah kompleks yang diperlukan.. Bukti: menggunakan lima bus yang dapat mengangkut hanya 290 penumpang.; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan simbol pertidaksamaan (≤, <, ≥, >). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemodelan pertidaksamaan linier satu variabel adalah materi standar kelas 8. Soal ini langsung menanyakan model tanpa perhitungan rumit, sehingga tergolong mudah. |

Run 2 — solusi: Misalkan x adalah banyak penumpang per bus. Karena terdapat 5 bus dan total penumpang maksimal 290, maka 5 dikali x tidak boleh melebihi 290. Pertidaksamaan yang sesuai adalah 5x ≤ 290.
- Domain kognitif `classify/applying`: Soal meminta siswa menerjemahkan situasi verbal ke dalam model matematika berupa pertidaksamaan linier satu variabel. Ini melibatkan pemahaman konsep hubungan 'maksimal' dengan simbol ≤.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar pertidaksamaan linier dan bagaimana menerjemahkan konteks 'hanya 290' (maksimal) ke dalam simbol matematika.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari konsep pertidaksamaan linier satu variabel. Siswa hanya perlu mengidentifikasi variabel, koefisien (jumlah bus), dan tanda pertidaksamaan yang tepat untuk situasi 'maksimal'.. Bukti: menggunakan lima bus yang dapat mengangkut hanya 290 penumpang; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan simbol pertidaksamaan (≤, ≥, <, >). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari pemodelan matematika sederhana. Soal ini tidak memerlukan langkah kompleks atau integrasi konsep yang sulit. |

Run 3 — solusi: Misalkan x adalah banyak penumpang per bus. Karena ada 5 bus dan kapasitas total maksimal 290 penumpang, maka total penumpang adalah 5x. Kata 'hanya' mengindikasikan batas atas (maksimal), sehingga 5x ≤ 290.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan situasi kontekstual ke dalam model matematika berupa pertidaksamaan. Ini melibatkan pemahaman hubungan antara variabel dan batasan (kapasitas maksimal), yang merupakan penerapan konsep dasar PtLSV.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang bagaimana merepresentasikan masalah dunia nyata ke dalam bentuk simbolik pertidaksamaan linier, yang merupakan aspek konseptual dari materi PtLSV.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu mengidentifikasi variabel, koefisien (jumlah bus), dan tanda pertidaksamaan yang sesuai dengan kata kunci 'hanya' (maksimal). Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: menggunakan lima bus yang dapat mengangkut hanya 290 penumpang; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan simbol pertidaksamaan (≤, ≥, <, >). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemodelan sederhana seperti ini adalah standar kompetensi kelas 8. Siswa diharapkan mampu menerjemahkan 'maksimal' menjadi simbol ≤ dengan cepat. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `4e77861a69e63696e5ee9f5e`

Pak Doni adalah seorang kuli bangunan kontrak yang sedang mengerjakan proyek pemerintah dengan penghasilan tidak lebih dari Rp. 3.600.000 setiap bulannya.<br><br>Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

| Opsi | Isi |
|---|---|
| A | x ≥ 3.600.000 (x = penghasilan Pak Doni per bulan) |
| B | x ≤ 3.600.000 (x = penghasilan Pak Doni per bulan) |
| C | x < 3.600.000 (x = penghasilan Pak Doni per bulan) |
| D | x = 3.600.000 (x = penghasilan Pak Doni per bulan) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Frasa 'tidak lebih dari' secara matematis berarti nilai tersebut adalah batas maksimum, sehingga mencakup nilai sama dengan. Jika x adalah penghasilan, maka x ≤ 3.600.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3b5005615f86ea8bd795be850a7a7bd37ee89f769128467dfd9ed083e6a36cfe`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2628 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2650 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2676 |

Run 1 — solusi: Frasa 'tidak lebih dari' secara matematis berarti nilai tersebut adalah batas maksimum, sehingga mencakup nilai sama dengan. Jika x adalah penghasilan, maka x ≤ 3.600.000.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan pernyataan verbal ke dalam model matematika (pertidaksamaan). Ini adalah penerapan konsep dasar pertidaksamaan pada konteks rutin.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang makna frasa verbal 'tidak lebih dari' dalam konteks pertidaksamaan.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menerjemahkan satu frasa kunci ke simbol matematika. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang simbol pertidaksamaan (≤, ≥, <, >) dan maknanya dalam kalimat sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan pemodelan matematika sederhana. Soal ini tidak memerlukan manipulasi aljabar, hanya pemahaman definisi pertidaksamaan. |

Run 2 — solusi: Frasa 'tidak lebih dari' secara matematis diterjemahkan sebagai 'kurang dari atau sama dengan' (≤). Jika x adalah penghasilan, maka modelnya adalah x ≤ 3.600.000.
- Domain kognitif `classify/applying`: Soal meminta siswa menerjemahkan pernyataan verbal ke dalam model matematika (pertidaksamaan). Ini adalah proses menerapkan konsep dasar pertidaksamaan pada konteks sederhana.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara frasa verbal 'tidak lebih dari' dengan simbol matematika '≤', yang merupakan bagian dari pemahaman konseptual tentang pertidaksamaan.. Bukti: tidak lebih dari Rp. 3.600.000
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menerjemahkan satu frasa kunci ke dalam simbol pertidaksamaan. Tidak ada langkah tambahan, kendala yang berinteraksi, atau perencanaan strategi yang kompleks.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang simbol pertidaksamaan (<, >, ≤, ≥) dan terjemahan kalimat verbal ke matematika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pertidaksamaan linier satu variabel adalah materi dasar kelas 8. Soal ini merupakan latihan standar untuk mengenali notasi pertidaksamaan dari konteks sehari-hari. |

Run 3 — solusi: Frasa 'tidak lebih dari' secara matematis berarti 'kurang dari atau sama dengan' (≤). Jika x adalah penghasilan Pak Doni, maka model pertidaksamaannya adalah x ≤ 3.600.000.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan pernyataan verbal ke dalam model matematika (pertidaksamaan). Ini adalah proses menerapkan konsep dasar pertidaksamaan pada konteks sederhana.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.; penghasilan tidak lebih dari Rp. 3.600.000
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap hubungan antara frasa verbal ('tidak lebih dari') dengan simbol matematika (≤), yang merupakan bagian dari pemahaman konsep pertidaksamaan.. Bukti: Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi kata kunci 'tidak lebih dari' dan memetakannya ke simbol pertidaksamaan yang tepat. Tidak ada langkah kompleks atau kendala yang saling berinteraksi.. Bukti: penghasilan tidak lebih dari Rp. 3.600.000; Modelkan permasalahan berikut menjadi bentuk pertidaksamaan linier satu variabel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang simbol pertidaksamaan (<, >, ≤, ≥) dan penerjemahan kalimat verbal ke model matematika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar dalam materi pertidaksamaan linier satu variabel di kelas 8, di mana siswa baru diperkenalkan dengan pemodelan matematika sederhana. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 11 kali pengangkutan |
| B | 9,45 kali pengangkutan |
| C | 10 kali pengangkutan |
| D | 9 kali pengangkutan |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Total pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4efe5399d75e8c8bc0458a2f8139d2646ff70bdd54c3b0dfa860fe67d0ae9e7f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2856 |
| 2 | success | valid / verified | applying | procedural | Medium | 2872 |
| 3 | success | valid / verified | applying | procedural | Medium | 2882 |

Run 1 — solusi: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Total pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kendala kapasitas (pengurangan), menentukan kapasitas angkut per perjalanan (pembagian), dan menerapkan penalaran pembulatan ke atas dalam konteks masalah nyata (banyak pengangkutan harus bilangan bulat). Ini adalah penerapan konsep pada masalah rutin.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika dasar (pengurangan, pembagian) dan memahami prinsip pembulatan dalam konteks masalah kehidupan sehari-hari.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perencanaan langkah (menghitung kapasitas bersih, menentukan kapasitas per angkut, lalu membagi total kotak) dan pemahaman bahwa hasil pembagian harus dibulatkan ke atas (konteks nyata), bukan sekadar operasi hitung langsung.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar (pengurangan dan pembagian) dan pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan situasi nyata ke dalam operasi matematika sederhana dan memahami implikasi pembulatan ke atas untuk masalah pengangkutan. |

Run 2 — solusi: Kapasitas muatan bersih = 2.000 kg - 150 kg = 1.850 kg. Kapasitas per angkut = 1.850 kg / 50 kg/kotak = 37 kotak. Total pengangkutan = 350 kotak / 37 kotak/angkut = 9,459... kali. Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep aritmatika dasar dan pemahaman konteks (pembulatan ke atas untuk masalah kapasitas) pada situasi nyata. Ini melibatkan pemilihan prosedur yang tepat untuk memodelkan masalah, yang masuk dalam kategori applying.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika (pengurangan, pembagian) dan prinsip konseptual tentang pembulatan dalam konteks masalah nyata (pembulatan ke atas karena sisa muatan tetap memerlukan satu perjalanan).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan perencanaan langkah (menghitung kapasitas bersih, menentukan kapasitas per angkut, lalu membagi total kotak) dan memahami kendala bahwa jumlah pengangkutan harus bilangan bulat (pembulatan ke atas).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar (pengurangan, pembagian) dan pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan masalah aritmatika sederhana dan membuat keputusan logis terkait pembulatan dalam konteks kapasitas, yang merupakan bagian dari materi pertidaksamaan/pemodelan aljabar. |

Run 3 — solusi: Kapasitas muatan kotak per angkut = (2000 - 150) / 50 = 1850 / 50 = 37 kotak. Total kotak = 350. Jumlah pengangkutan = 350 / 37 ≈ 9,459. Karena jumlah pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pertidaksamaan atau pembagian dengan pembulatan ke atas dalam konteks masalah nyata. Siswa harus mengidentifikasi kapasitas bersih, menghitung kapasitas per angkut, dan menentukan jumlah perjalanan yang diperlukan.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika dasar (pengurangan, pembagian) dan prinsip pembulatan dalam konteks masalah nyata (konseptual).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah terstruktur: menghitung kapasitas bersih, menentukan kapasitas per angkut, dan melakukan pembulatan ke atas yang logis (kontekstual). Meskipun prosedurnya familiar, siswa harus memahami bahwa hasil pembagian tidak bulat dan harus dibulatkan ke atas untuk memenuhi syarat 'semua kotak terangkut'.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep pembulatan dalam masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan masalah aritmatika sederhana dan memahami implikasi pembulatan ke atas dalam konteks transportasi/beban. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `b0ce9e96d828be7c94c0894c`

Humam memiliki uang Rp180.000,00 yang akan digunakan untuk membeli jeruk. Untuk harga 1 kg jeruk adalah Rp15.000,00.<br><br>Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.

| Opsi | Isi |
|---|---|
| A | x ≥ 12 (paling banyak 12 kg jeruk) |
| B | x ≤ 1.200 (paling banyak 1.200 kg jeruk) |
| C | x ≤ 15 (paling banyak 15 kg jeruk) |
| D | x ≤ 12 (paling banyak 12 kg jeruk) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misalkan x adalah berat jeruk dalam kg. Harga total jeruk adalah 15.000x. Karena uang Humam terbatas pada 180.000, maka 15.000x ≤ 180.000. Membagi kedua ruas dengan 15.000 menghasilkan x ≤ 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `29441cc653c38717333e04bc22bdb540b906e46bb42eb4f8e49aa0209bf6679c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2720 |
| 2 | success | valid / verified | applying | procedural | Easy | 2768 |
| 3 | success | valid / verified | applying | procedural | Easy | 2731 |

Run 1 — solusi: Misalkan x adalah berat jeruk dalam kg. Harga total jeruk adalah 15.000x. Karena uang Humam terbatas pada 180.000, maka 15.000x ≤ 180.000. Membagi kedua ruas dengan 15.000 menghasilkan x ≤ 12.
- Domain kognitif `classify/applying`: Siswa diminta untuk memodelkan situasi nyata ke dalam bentuk pertidaksamaan linier satu variabel dan menyelesaikannya. Ini melibatkan penerapan konsep pertidaksamaan pada konteks rutin.. Bukti: Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang prosedur aljabar untuk menyelesaikan pertidaksamaan linier satu variabel.. Bukti: 15.000x ≤ 180.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerjemahkan masalah ke dalam model matematika sederhana dan melakukan satu operasi pembagian. Tidak ada kendala yang saling berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Humam memiliki uang Rp180.000,00 yang akan digunakan untuk membeli jeruk. Untuk harga 1 kg jeruk adalah Rp15.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linier satu variabel dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan standar pertidaksamaan linier satu variabel yang sesuai dengan kurikulum kelas 8. Tingkat kesulitan rendah karena alur penyelesaian sangat jelas. |

Run 2 — solusi: Misalkan x adalah berat jeruk dalam kg. Harga total jeruk adalah 15.000x. Karena uang Humam terbatas (maksimal 180.000), maka berlaku pertidaksamaan 15.000x <= 180.000. Membagi kedua ruas dengan 15.000 menghasilkan x <= 12.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk memodelkan situasi nyata ke dalam bentuk pertidaksamaan linier satu variabel dan menyelesaikannya. Ini adalah penerapan langsung dari konsep pertidaksamaan pada konteks rutin.. Bukti: Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara harga satuan, jumlah barang, dan total uang yang tersedia untuk membentuk model matematika (konseptual) dan menerapkan prosedur aljabar untuk menyelesaikannya (prosedural).. Bukti: 15.000x <= 180.000
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari konsep pertidaksamaan linier satu variabel. Siswa hanya perlu menerjemahkan kalimat menjadi model matematika sederhana dan melakukan satu langkah pembagian. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Humam memiliki uang Rp180.000,00; harga 1 kg jeruk adalah Rp15.000,00; Buatlah penyelesaian dari pertidaksamaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linier satu variabel dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pertidaksamaan linier satu variabel adalah kurikulum standar kelas 8. Soal ini tidak menuntut penalaran tingkat tinggi, hanya pemodelan dasar dan penyelesaian rutin. |

Run 3 — solusi: Misalkan x adalah berat jeruk dalam kg. Biaya total adalah 15.000x. Karena uang yang dimiliki adalah Rp180.000, maka 15.000x ≤ 180.000. Membagi kedua ruas dengan 15.000 menghasilkan x ≤ 12.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi kontekstual ke dalam model matematika berupa pertidaksamaan linier satu variabel dan menyelesaikannya. Ini melibatkan penerapan prosedur yang sudah dipelajari dalam konteks rutin.. Bukti: Buatlah penyelesaian dari pertidaksamaan yang mengilustrasikan banyaknya jeruk yang dapat Humam beli.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara harga satuan, jumlah barang, dan batasan anggaran untuk membentuk pertidaksamaan, yang merupakan aspek prosedural dalam memodelkan masalah.. Bukti: 15.000x ≤ 180.000
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu memodelkan situasi menjadi pertidaksamaan linier satu variabel sederhana dan melakukan pembagian dasar. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Humam memiliki uang Rp180.000,00 yang akan digunakan untuk membeli jeruk. Untuk harga 1 kg jeruk adalah Rp15.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pertidaksamaan linier satu variabel dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari materi pertidaksamaan linier satu variabel yang merupakan standar kurikulum kelas 8. Langkah penyelesaiannya jelas dan tidak memerlukan perencanaan yang kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `bb5563c106a35bce8aef90f0`

Panitia OSIS menjual tiket untuk konser musik yang merupakan acara tahunan sekolah. Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani. a. Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik. b. Tulislah bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik. c. Jika ada 10 tiket yang tidak terjual, tulislah bentuk aljabar dari banyak tiket secara keseluruhan.<br><br>d. Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

| Opsi | Isi |
|---|---|
| A | 92 tiket |
| B | 76 tiket |
| C | 78 tiket |
| D | 88 tiket |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a + 6) + 10 = 6a + 16. Untuk a=12, total = 6(12) + 16 = 72 + 16 = 88.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0c7b6c5ca0fc3d65bec0ef262f00cad0f21f0fb068b7eb20700ecaa898cb1b81`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2867 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2887 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2905 |

Run 1 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a + 6) + 10 = 6a + 16. Untuk a=12, total = 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan situasi verbal ke dalam model aljabar (pemodelan) dan melakukan substitusi nilai ke dalam bentuk yang telah dibuat. Ini adalah penerapan konsep aljabar dalam konteks rutin.. Bukti: Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Tulislah bentuk aljabar dari total tiket yang terjual; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antar variabel dan prinsip penjumlahan bentuk aljabar (konseptual) serta melakukan operasi hitung aljabar (prosedural).. Bukti: Tulislah bentuk aljabar dari banyak tiket; total tiket yang terjual; Jika ada 10 tiket yang tidak terjual
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: memodelkan empat variabel berbeda, menjumlahkannya, menambahkan konstanta untuk tiket tidak terjual, dan melakukan substitusi. Meskipun prosedurnya familiar, integrasi beberapa informasi (variabel dan konstanta) memerlukan ketelitian.. Bukti: Bagas menjual 3 kali dari tiket yang dijual oleh Rani; Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani; Malik menjual 10 tiket lebih banyak dari Rani; Jika ada 10 tiket yang tidak terjual

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bentuk aljabar, substitusi nilai pada variabel. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu memodelkan situasi sehari-hari ke dalam bentuk aljabar linear satu variabel dan melakukan operasi penjumlahan suku sejenis. |

Run 2 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total tiket keseluruhan = (6a + 6) + 10 = 6a + 16. Jika a=12, maka 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi verbal ke dalam bentuk aljabar (pemodelan) dan melakukan operasi penjumlahan suku sejenis, yang merupakan penerapan konsep aljabar dasar dalam konteks rutin.. Bukti: Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Tulislah bentuk aljabar dari total tiket yang terjual; Jika ada 10 tiket yang tidak terjual, tulislah bentuk aljabar dari banyak tiket secara keseluruhan.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang bagaimana merepresentasikan hubungan kuantitatif menggunakan variabel dan operasi aljabar (konseptual) serta melakukan penyederhanaan bentuk aljabar (prosedural).. Bukti: Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Tulislah bentuk aljabar dari total tiket yang terjual
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: memodelkan empat variabel berbeda, menjumlahkannya, menambahkan konstanta untuk tiket tidak terjual, dan melakukan substitusi nilai. Meskipun prosedurnya familiar, integrasi antar langkah diperlukan.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar aljabar (penjumlahan suku sejenis) dan pemodelan matematika sederhana. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan pemodelan aljabar dasar yang merupakan kompetensi inti, dengan tingkat kompleksitas yang wajar melalui beberapa langkah berurutan. |

Run 3 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a + 6) + 10 = 6a + 16. Untuk a=12, total = 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam ekspresi aljabar (pemodelan) dan melakukan operasi penjumlahan suku sejenis, kemudian melakukan substitusi nilai untuk mendapatkan hasil akhir. Ini adalah penerapan konsep aljabar dalam konteks rutin.. Bukti: Tulislah bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Tulislah bentuk aljabar dari total tiket yang terjual; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang bagaimana variabel dan konstanta merepresentasikan situasi nyata serta prosedur manipulasi aljabar dasar (penjumlahan suku sejenis).. Bukti: Tulislah bentuk aljabar dari banyak tiket; total tiket yang terjual; Jika ada 10 tiket yang tidak terjual
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah terstruktur: memodelkan empat variabel berbeda, menjumlahkannya, menambahkan konstanta tambahan (tiket tidak terjual), dan melakukan substitusi. Meskipun prosedurnya familiar, siswa harus teliti dalam mengintegrasikan semua informasi (termasuk tiket Rani sendiri) agar tidak terjadi kesalahan perhitungan.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika ada 10 tiket yang tidak terjual; Jika tiket yang dijual oleh Rani sebanyak 12 tiket.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar variabel aljabar, operasi penjumlahan suku sejenis, dan substitusi nilai. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 8 karena melibatkan pemodelan aljabar dasar yang menjadi standar kurikulum, dengan tingkat kompleksitas yang menuntut ketelitian dalam mengelola beberapa variabel sekaligus. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `bc52760c552d361c6b1ad513`

Diketahui Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; dan relasi dari himpunan C ke D adalah "kurang dari". Nyatakan relasi tersebut dalam tiga cara berikut: a. Diagram panah b. Diagram Cartesius c. Himpunan pasangan berurutan<br><br>Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.

| Opsi | Isi |
|---|---|
| A | {(3, 4), (4, 5)} |
| B | {(4, 3), (5, 3), (5, 4)} |
| C | {(3, 3), (4, 4)} |
| D | {(3, 4), (3, 5), (4, 5)} |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Relasi 'kurang dari' dari C={3, 4} ke D={3, 4, 5} berarti mencari pasangan (c, d) dengan c < d. Untuk c=3, d yang memenuhi adalah 4 dan 5 (3<4, 3<5). Untuk c=4, d yang memenuhi adalah 5 (4<5). Himpunan pasangan berurutannya adalah {(3, 4), (3, 5), (4, 5)}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b0f7039a8e251853a0ea1d93395a51803046e13ddf7bf5eda3fce88b2d377f8d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2838 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2822 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2871 |

Run 1 — solusi: Relasi 'kurang dari' dari C={3, 4} ke D={3, 4, 5} berarti mencari pasangan (c, d) dengan c < d. Untuk c=3, d yang memenuhi adalah 4 dan 5 (3<4, 3<5). Untuk c=4, d yang memenuhi adalah 5 (4<5). Himpunan pasangan berurutannya adalah {(3, 4), (3, 5), (4, 5)}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi relasi 'kurang dari' dan menerapkannya pada elemen-elemen himpunan yang diberikan untuk membentuk pasangan berurutan. Ini adalah penerapan konsep relasi pada konteks yang rutin.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang relasi antara dua himpunan dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Himpunan C = {3, 4}; himpunan D = {3, 4, 5}
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu melakukan pengecekan sistematis terhadap pasangan elemen dari dua himpunan kecil. Tidak ada kendala yang kompleks atau perencanaan strategi yang rumit.. Bukti: Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; relasi dari himpunan C ke D adalah "kurang dari"

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep relasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi adalah topik standar kelas 8. Tugas ini merupakan latihan dasar dalam merepresentasikan relasi, yang sesuai dengan tingkat kemampuan siswa kelas 8. |

Run 2 — solusi: Relasi 'kurang dari' dari C={3, 4} ke D={3, 4, 5} berarti mencari pasangan (c, d) dengan c < d. Untuk c=3, d yang memenuhi adalah 4 dan 5 (pasangan: (3,4), (3,5)). Untuk c=4, d yang memenuhi adalah 5 (pasangan: (4,5)). Himpunan pasangan berurutan: {(3, 4), (3, 5), (4, 5)}.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi relasi 'kurang dari' pada dua himpunan yang diberikan untuk membentuk himpunan pasangan berurutan. Ini adalah penerapan prosedur standar dalam topik relasi.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang relasi matematika dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu memeriksa pasangan elemen dari dua himpunan kecil berdasarkan relasi sederhana. Tidak ada langkah perencanaan yang kompleks atau kendala yang saling berinteraksi.. Bukti: Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; relasi dari himpunan C ke D adalah "kurang dari"

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep relasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi adalah topik standar kelas 8. Tugas ini bersifat rutin dan langsung, tidak memerlukan penalaran tingkat tinggi. |

Run 3 — solusi: Relasi 'kurang dari' dari C={3, 4} ke D={3, 4, 5} berarti mencari pasangan (c, d) dengan c < d. Untuk c=3, d yang memenuhi adalah 4 dan 5 (pasangan: (3,4), (3,5)). Untuk c=4, d yang memenuhi adalah 5 (pasangan: (4,5)). Himpunan pasangan berurutan: {(3, 4), (3, 5), (4, 5)}.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi relasi 'kurang dari' pada dua himpunan yang diberikan untuk membentuk himpunan pasangan berurutan. Ini adalah penerapan prosedur standar dalam topik relasi.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang relasi matematika dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: relasi dari himpunan C ke D adalah "kurang dari"; Himpunan C = {3, 4}; himpunan D = {3, 4, 5}
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena himpunan yang diberikan sangat kecil, sehingga siswa dapat dengan mudah melakukan pengecekan satu per satu (exhaustive checking) untuk setiap elemen tanpa memerlukan strategi kompleks atau perencanaan langkah yang panjang.. Bukti: Himpunan C = {3, 4}; himpunan D = {3, 4, 5}; relasi dari himpunan C ke D adalah "kurang dari"

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep perbandingan bilangan (kurang dari). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi adalah topik dasar kelas 8. Soal ini hanya meminta penerapan definisi langsung pada himpunan beranggota sedikit, sehingga beban kognitifnya rendah. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `e044f1847d7a97d6815a581d`

Apabila relasi himpunan E ke F merupakan "akar dari" dengan diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}, maka nyatakan relasi tersebut dengan tiga cara berikut ini: a. himpunan pasangan berurutan. b. diagram panah; c. diagram Cartesius.<br><br>Nyatakan relasi tersebut dengan cara himpunan pasangan berurutan.

| Opsi | Isi |
|---|---|
| A | {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36)} |
| B | {(1, 1), (2, 4), (3, 9), (4, 16), (5, 20), (6, 36)} |
| C | {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)} |
| D | {(1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6)} |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Relasi 'akar dari' berarti untuk setiap x di E, pasangannya adalah y di F sedemikian sehingga x^2 = y. Dengan memeriksa setiap elemen E: 1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36. Semua hasil kuadrat tersebut ada di himpunan F. Maka himpunan pasangan berurutannya adalah {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1569cd7b4cdf0751e20f78a6d3d49eb313f139752866901aa69589fb2e2e2957`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3080 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3007 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3039 |

Run 1 — solusi: Relasi 'akar dari' berarti untuk setiap x di E, pasangannya adalah y di F sedemikian sehingga x^2 = y. Dengan memeriksa setiap elemen E: 1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36. Semua hasil kuadrat tersebut ada di himpunan F. Maka himpunan pasangan berurutannya adalah {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi relasi 'akar dari' untuk memetakan elemen dari himpunan E ke F. Ini adalah penerapan konsep relasi yang rutin dan langsung.. Bukti: Apabila relasi himpunan E ke F merupakan "akar dari" dengan diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang relasi dan bagaimana merepresentasikannya dalam bentuk pasangan berurutan.. Bukti: relasi himpunan E ke F merupakan "akar dari"
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan operasi kuadrat sederhana untuk setiap elemen di E dan mencocokkannya dengan elemen di F. Tidak ada kendala kompleks atau perencanaan strategi yang rumit.. Bukti: Apabila relasi himpunan E ke F merupakan "akar dari" dengan diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}

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
| gradeRelativeRationale | Siswa kelas 8 sudah familiar dengan konsep relasi dan pemetaan sederhana. Tugas ini adalah latihan standar yang tidak memerlukan integrasi konsep tingkat tinggi. |

Run 2 — solusi: Relasi 'akar dari' dari E ke F berarti untuk setiap e di E, f = e^2 harus ada di F. Pasangan (e, f) adalah: 1^2=1 (ada), 2^2=4 (ada), 3^2=9 (ada), 4^2=16 (ada), 5^2=25 (ada), 6^2=36 (ada). Himpunan pasangan berurutan: {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi relasi 'akar dari' untuk membentuk pasangan berurutan dari dua himpunan yang diberikan. Ini adalah penerapan konsep relasi yang rutin.. Bukti: Apabila relasi himpunan E ke F merupakan "akar dari"; nyatakan relasi tersebut dengan cara himpunan pasangan berurutan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang relasi dan representasi himpunan pasangan berurutan.. Bukti: relasi himpunan E ke F merupakan "akar dari"; himpunan pasangan berurutan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu menguji setiap elemen di E apakah kuadratnya ada di F. Tidak ada kendala yang saling berinteraksi atau perencanaan strategi yang kompleks.. Bukti: E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang relasi, kuadrat bilangan, dan himpunan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi relasi adalah topik standar kelas 8. Tugas mengidentifikasi pasangan berdasarkan aturan yang diberikan adalah latihan dasar yang familiar. |

Run 3 — solusi: Relasi 'akar dari' dari E ke F berarti untuk setiap elemen e di E, pasangannya f di F harus memenuhi e = akar(f) atau e^2 = f. Kita periksa setiap elemen E: 1^2=1 (ada di F), 2^2=4 (ada di F), 3^2=9 (ada di F), 4^2=16 (ada di F), 5^2=25 (ada di F), 6^2=36 (ada di F). Maka himpunan pasangan berurutannya adalah {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)}.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi relasi 'akar dari' untuk membentuk pasangan berurutan dari dua himpunan yang diberikan. Ini adalah penerapan konsep relasi yang rutin.. Bukti: Apabila relasi himpunan E ke F merupakan "akar dari"; nyatakan relasi tersebut dengan cara himpunan pasangan berurutan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang relasi dan pemetaan antara dua himpunan.. Bukti: relasi himpunan E ke F merupakan "akar dari"
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Prosedurnya jelas: mengkuadratkan elemen E dan memeriksa keberadaannya di F. Tidak ada kendala yang saling berinteraksi atau kebutuhan strategi nonrutin.. Bukti: diketahui himpunan E = {1, 2, 3, 4, 5, 6}, dan himpunan F = {1, 2, 4, 9, 12, 16, 20, 25, 36, 49}; nyatakan relasi tersebut dengan cara himpunan pasangan berurutan

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
| gradeRelativeRationale | Materi relasi adalah topik standar kelas 8. Tugas ini hanya memerlukan pengecekan elemen satu per satu secara langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `cc51dc6d0e0814ecda8e12e1`

Periksa apakah dua himpuan berikut ini termasuk fungsi atau bukan fungsi? Jelaskan. Diketahui bahwa himpunan R dan S memiliki anggota masing-masing adalah R = {3, 4, 6, 8, 9, 12, 14, 18} dan S = {1, 6, 9}. Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan,<br><br>Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?

| Opsi | Isi |
|---|---|
| A | Fungsi, karena setiap anggota R mempunyai tepat satu pasangan di S |
| B | Bukan fungsi, karena tidak semua anggota R memiliki pasangan di S |
| C | Bukan fungsi, karena S bukan himpunan bilangan bulat |
| D | Fungsi, karena semua anggota S mempunyai pasangan di R |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Relasi didefinisikan sebagai R = 1/3 * S, atau S = 3R. Untuk setiap r di R, harus ada tepat satu s di S. Uji anggota R: 3*3=9 (ada di S), 4*3=12 (tidak ada di S), 6*3=18 (tidak ada di S), dst. Karena hanya 3 yang memiliki pasangan di S, maka relasi ini bukan fungsi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cc673b184a194e84d21ae1a940757e294905e83a02a3534ee175717ba31efbeb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2813 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2825 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2867 |

Run 1 — solusi: Relasi didefinisikan sebagai R = 1/3 * S, atau S = 3R. Untuk setiap r di R, harus ada tepat satu s di S. Uji anggota R: 3*3=9 (ada di S), 4*3=12 (tidak ada di S), 6*3=18 (tidak ada di S), dst. Karena hanya 3 yang memiliki pasangan di S, maka relasi ini bukan fungsi.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi formal fungsi (setiap anggota domain harus memiliki tepat satu pasangan di kodomain) dan menerapkannya pada relasi yang diberikan untuk menentukan apakah syarat tersebut terpenuhi.. Bukti: Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi fungsi dan bagaimana relasi antar himpunan dapat dikategorikan sebagai fungsi atau bukan.. Bukti: Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan verifikasi sistematis terhadap setiap elemen himpunan R untuk memeriksa keberadaan pasangan di S. Meskipun prosedurnya rutin, siswa sering terjebak pada definisi fungsi (memeriksa arah relasi yang salah atau mengabaikan syarat 'setiap anggota domain').. Bukti: Periksa apakah dua himpuan berikut ini termasuk fungsi atau bukan fungsi?; Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi (domain, kodomain, syarat pemetaan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu membedakan relasi dan fungsi. Soal ini menuntut ketelitian dalam memeriksa syarat fungsi pada himpunan berhingga. |

Run 2 — solusi: Relasi didefinisikan sebagai r = 1/3 * s, atau s = 3r. Untuk setiap r di R, harus ada tepat satu s di S. Uji anggota R: jika r=3, s=9 (ada di S). Jika r=4, s=12 (tidak ada di S). Karena anggota lain di R tidak memiliki pasangan di S, maka relasi ini bukan fungsi.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi formal fungsi (setiap anggota domain harus memiliki tepat satu pasangan di kodomain) pada relasi yang diberikan untuk menentukan apakah relasi tersebut memenuhi syarat fungsi.. Bukti: Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?; Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi fungsi dan relasi, bukan sekadar menghafal fakta atau melakukan prosedur rutin tanpa pemahaman.. Bukti: Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan verifikasi sistematis terhadap setiap elemen domain (R) untuk melihat apakah mereka memiliki pasangan unik di kodomain (S). Meskipun prosedurnya familiar, siswa perlu berhati-hati dalam memeriksa setiap elemen dan memahami bahwa relasi bukan fungsi jika domain tidak terpetakan sepenuhnya.. Bukti: Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan; Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi (domain, kodomain, pemetaan satu-satu). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan memahami definisi fungsi. Soal ini menuntut ketelitian dalam memeriksa pemetaan elemen, yang merupakan standar kompetensi dasar fungsi. |

Run 3 — solusi: Relasi didefinisikan sebagai r = 1/3 s atau s = 3r. Untuk setiap r di R, harus ada tepat satu s di S. Uji anggota R: jika r=3, s=3(3)=9 (ada di S). Jika r=4, s=3(4)=12 (tidak ada di S). Karena anggota R lainnya (4, 6, 8, 9, 12, 14, 18) tidak memiliki pasangan di S, maka relasi ini bukan fungsi.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi formal fungsi (setiap anggota domain harus memiliki tepat satu pasangan di kodomain) pada relasi yang diberikan. Ini memerlukan pemahaman konseptual tentang syarat fungsi dan prosedur pengecekan elemen.. Bukti: Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?; Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar relasi dan fungsi, yang merupakan konsep fundamental dalam aljabar.. Bukti: Periksa apakah dua himpuan berikut ini termasuk fungsi atau bukan fungsi?; Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan pengecekan sistematis terhadap elemen-elemen himpunan R untuk memverifikasi syarat fungsi. Meskipun prosedurnya rutin, siswa sering terkecoh dengan definisi fungsi jika tidak teliti memeriksa domain (himpunan R).. Bukti: Apabila "Anggota R sepertiga kali anggota S" adalah relasi yang ditentukan; Dapatkah hubungan antara himpunan R dan S disebut sebagai fungsi atau bukan fungsi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi relasi dan fungsi, pemahaman himpunan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu membedakan relasi dan fungsi. Soal ini menuntut ketelitian dalam memeriksa syarat fungsi untuk setiap anggota domain. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `13db9a1e91c27f3f1a174ba0`

Perhatikan dengan cermat terhadap aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m.<br><br>Apa makna pesan dari kata sandi berikut ini: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

| Opsi | Isi |
|---|---|
| A | ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH |
| B | GURUKU ADALAH ORANG TUAKU KETIKA DI RUMAH |
| C | ORANG TUAKU BUKAN GURUKU KETIKA DI RUMAH |
| D | ORANG TUAKU ADALAH GURUKU KETIKA DI SEKOLAH |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Substitusi setiap huruf sandi berdasarkan aturan A->q, B->w, ..., Z->m. gkqfu=ORANG, zxqax=TUAKU, qrqsqi=ADALAH, uxkxax=GURUKU, atzoaq=KETIKA, ro=DI, kxdqi=RUMAH. Hasil: ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e913b9610ee5035f48df421b8bcff82da43005d2b26335fdd7e7e4ee3f0c3aeb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 4110 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2996 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2947 |

Run 1 — solusi: Substitusi setiap huruf sandi berdasarkan aturan A->q, B->w, ..., Z->m. gkqfu=ORANG, zxqax=TUAKU, qrqsqi=ADALAH, uxkxax=GURUKU, atzoaq=KETIKA, ro=DI, kxdqi=RUMAH. Hasil: ORANG TUAKU ADALAH GURUKU KETIKA DI RUMAH.
- Domain kognitif `classify/applying`: Siswa menerapkan aturan pemetaan (fungsi) satu-ke-satu yang diberikan untuk mendekode pesan. Ini adalah penerapan langsung dari konsep fungsi/korespondensi.. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m
- Dimensi pengetahuan `classify/conceptual`: Memahami konsep fungsi sebagai pemetaan atau korespondensi satu-satu antara dua himpunan (huruf asli dan huruf sandi).. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m
- Intended difficulty `classify/Easy`: Soal ini hanya memerlukan substitusi langsung berdasarkan tabel pemetaan yang sudah disediakan. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pemetaan atau korespondensi satu-satu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari fungsi dan korespondensi. Tugas ini adalah penerapan langsung dari konsep tersebut tanpa kompleksitas tambahan. |

Run 2 — solusi: Substitusi huruf sandi berdasarkan pemetaan: A->q, B->w, C->e, D->r, E->t, F->y, G->u, H->i, I->o, J->p, K->a, L->s, M->d, N->f, O->g, P->h, Q->j, R->k, S->l, T->z, U->x, V->c, W->v, X->b, Y->n, Z->m. Membalik pemetaan (q->A, w->B, dll), kata sandi 'gkqfu' menjadi 'ORANG', 'zxqax' menjadi 'TUAKU', 'qrqsqi' menjadi 'ADALAH', 'uxkxax' menjadi 'GURUKU', 'atzoaq' menjadi 'KETIKA', 'ro' menjadi 'DI', 'kxdqi' menjadi 'RUMAH'.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur substitusi sederhana berdasarkan aturan pemetaan (fungsi) yang diberikan secara eksplisit untuk mendekode pesan.. Bukti: Perhatikan dengan cermat terhadap aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep fungsi sebagai pemetaan satu-satu antara dua himpunan (huruf alfabet ke huruf sandi), yang merupakan konsep dasar relasi dan fungsi.. Bukti: aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan substitusi huruf satu per satu sesuai tabel yang diberikan. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks. Beban kognitif utama adalah ketelitian dalam substitusi.. Bukti: Apa makna pesan dari kata sandi berikut ini: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korespondensi satu-satu atau pemetaan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas ini adalah penerapan langsung dari konsep fungsi/pemetaan yang sesuai untuk kelas 8. Tidak memerlukan penalaran tingkat tinggi, hanya ketelitian dalam mengikuti aturan pemetaan yang sudah disediakan. |

Run 3 — solusi: Substitusi huruf berdasarkan pemetaan: A->q, B->w, C->e, D->r, E->t, F->y, G->u, H->i, I->o, J->p, K->a, L->s, M->d, N->f, O->g, P->h, Q->j, R->k, S->l, T->z, U->x, V->c, W->v, X->b, Y->n, Z->m. Membalik pemetaan (q->A, w->B, dll), kata 'gkqfu' menjadi 'ORANG', 'zxqax' menjadi 'TUAKU', 'qrqsqi' menjadi 'ADALAH', 'uxkxax' menjadi 'GURUKU', 'atzoaq' menjadi 'KETIKA', 'ro' menjadi 'DI', 'kxdqi' menjadi 'RUMAH'.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan pemetaan (fungsi) satu-ke-satu antara dua himpunan (huruf alfabet dan simbol sandi) untuk mendekode pesan. Ini adalah penerapan langsung dari konsep fungsi.. Bukti: Perhatikan dengan cermat terhadap aturan kata sandi berikut ini A B C D E F G H I J K L M N O P Q R S T U V W X Y Z q w e r t y u i o p a s d f g h j k l z x c v b n m.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep fungsi sebagai relasi yang memetakan setiap elemen domain ke tepat satu elemen kodomain, yang dalam hal ini adalah substitusi huruf.. Bukti: aturan kata sandi berikut ini
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena prosedurnya sangat langsung (substitusi satu-ke-satu). Siswa hanya perlu memetakan setiap huruf sandi kembali ke huruf alfabet sesuai aturan yang diberikan. Tidak ada kendala kompleks atau perencanaan strategi yang rumit.. Bukti: Apa makna pesan dari kata sandi berikut ini: gkqfu zxqax qrqsqi uxkxax atzoaq ro kxdqi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang relasi dan fungsi (pemetaan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas substitusi sederhana sesuai dengan kemampuan siswa kelas 8 dalam memahami konsep fungsi sebagai pemetaan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| B | 12 |
| C | 12! = 479.001.600 |
| D | 12 x 12 = 144 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f3719b263f16b4ade57f0a02fad1475ae7978266a65425527b4da46432e0f92a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2778 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2768 |
| 3 | success | valid / verified | applying | procedural | Easy | 2787 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial yang sudah dipelajari.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap prinsip dasar korespondensi satu-satu (bijeksi) antara dua himpunan berhingga, yang merupakan konsep matematis.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya menuntut penerapan rumus n! secara langsung. Tidak ada langkah perencanaan kompleks atau integrasi konsep yang saling bergantung. Meskipun angka 12! cukup besar, prosedur dasarnya sangat familiar bagi siswa yang mempelajari topik ini.. Bukti: n(A) = n(B) = 12

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
| gradeRelativeRationale | Meskipun topik ini sering dianggap pengayaan, soal ini hanya menuntut penerapan rumus langsung tanpa modifikasi atau penalaran tambahan, sehingga dikategorikan mudah untuk tingkat SMP. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n = 12, maka banyak korespondensi adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial yang sesuai.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang konsep korespondensi satu-satu dan prosedur perhitungan faktorial yang merupakan bagian dari materi himpunan/kombinatorika dasar.. Bukti: korespondensi satu-satu; n(A) = n(B) = 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Tidak ada langkah perencanaan kompleks atau integrasi antar konsep; siswa hanya perlu mengingat rumus n! dan menghitungnya.. Bukti: n(A) = n(B) = 12

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
| gradeRelativeRationale | Meskipun angka 12! cukup besar, prosedur faktorial adalah standar untuk topik ini. Soal tidak menuntut penalaran mendalam, hanya pengingatan rumus. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan rumus faktorial untuk menghitung banyaknya korespondensi satu-satu. Siswa perlu mengenali konsep korespondensi satu-satu dan menerapkan prosedur perhitungan faktorial yang sesuai.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami konsep korespondensi satu-satu antara dua himpunan dan mengetahui prosedur perhitungan faktorial (n!) untuk menentukan banyaknya pemetaan tersebut.. Bukti: korespondensi satu-satu; n(A) = n(B) = 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi pengayaan korespondensi satu-satu. Prosedur (n!) sudah jelas dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit.. Bukti: n(A) = n(B) = 12; ada berapa banyak korespondensi satu-satu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep korespondensi satu-satu (pengayaan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun melibatkan angka besar (12!), ini adalah prosedur standar untuk topik korespondensi satu-satu. Tidak ada langkah penalaran non-rutin yang diperlukan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4474`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan rumus faktorial (n!) untuk menentukan banyaknya korespondensi satu-satu. Ini adalah prosedur standar yang langsung, sehingga masuk dalam domain knowing.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami konsep korespondensi satu-satu (bijeksi) dan mengetahui prosedur perhitungan faktorial yang merupakan metode standar untuk menyelesaikan masalah ini.
- Intended difficulty `Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus n! secara langsung. Tidak ada langkah perencanaan kompleks, integrasi konsep, atau kendala yang saling berinteraksi. Meskipun angka 12! besar, prosedur dasarnya sangat familiar bagi siswa yang mempelajari topik ini.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Meskipun topik ini sering dianggap pengayaan, soal ini hanya menuntut penerapan rumus langsung tanpa modifikasi atau penalaran tambahan, sehingga dikategorikan mudah untuk tingkat SMP. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `bbdde7d74cc90e271efac7fa`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? b. n(A) = n(B) = 9<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 9?

| Opsi | Isi |
|---|---|
| A | 9 + 8 + 7 + ... + 2 + 1 = 45 |
| B | 9! = 362.880 |
| C | 9 |
| D | 9 x 9 = 81 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n(A) = n(B) = 9, maka banyak korespondensi satu-satu adalah 9! = 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 362.880.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d1f5724b21c43acc77a0eba1360825ce103df36e2c7fdbbfc035e9c74ce7d23b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2711 |
| 2 | success | valid / verified | applying | procedural | Medium | 2746 |
| 3 | success | valid / verified | applying | procedural | Easy | 2688 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n(A) = n(B) = 9, maka banyak korespondensi satu-satu adalah 9! = 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 362.880.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu. Meskipun konsep ini sering dianggap pengayaan, prosedurnya bersifat langsung (menerapkan n!) setelah konsep dipahami.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? b. n(A) = n(B) = 9
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar perhitungan (faktorial) dalam konteks korespondensi satu-satu.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya langsung (n!), konsep korespondensi satu-satu dan faktorial sering kali merupakan materi pengayaan atau perluasan yang memerlukan pemahaman konseptual di luar operasi aritmetika dasar.. Bukti: n(A) = n(B) = 9

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan prinsip perkalian (counting principle). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun prosedurnya sederhana (n!), konsep korespondensi satu-satu sering kali menjadi materi pengayaan di kelas 8, sehingga menuntut pemahaman konsep yang lebih dari sekadar operasi rutin. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n faktorial (n!). Untuk n(A) = n(B) = 9, maka banyaknya korespondensi adalah 9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362.880.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep korespondensi satu-satu dan menerapkan rumus faktorial untuk menghitung banyaknya pemetaan yang mungkin. Ini adalah penerapan prosedur yang dipelajari dalam materi relasi dan fungsi.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? b. n(A) = n(B) = 9
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar korespondensi satu-satu (konseptual) dan penerapan algoritma faktorial untuk menyelesaikannya (prosedural).. Bukti: korespondensi satu-satu; n(A) = n(B) = 9
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena meskipun prosedurnya spesifik (faktorial), siswa kelas 8 sering kali belum terbiasa dengan notasi faktorial atau konsep permutasi dasar dalam konteks korespondensi satu-satu, sehingga memerlukan pemilihan prosedur yang tepat di luar operasi aritmatika dasar.. Bukti: n(A) = n(B) = 9

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan konsep korespondensi satu-satu. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu adalah bagian dari kurikulum kelas 8. Menghitung faktorial untuk n=9 memerlukan ketelitian dan pemahaman rumus yang tepat, yang merupakan tantangan menengah bagi siswa di jenjang ini. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n(A) = n(B) = n adalah n!. Untuk n = 9, maka 9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362.880.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu. Ini adalah penerapan prosedur yang sudah dipelajari dalam materi korespondensi satu-satu.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? b. n(A) = n(B) = 9
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip dasar perhitungan (faktorial) dalam konteks korespondensi satu-satu, yang merupakan bagian dari pengetahuan prosedural.. Bukti: korespondensi satu-satu yang mungkin
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Prosedur (n!) langsung diterapkan tanpa perlu perencanaan strategi yang kompleks atau integrasi kendala.. Bukti: n(A) = n(B) = 9

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep korespondensi satu-satu dan operasi faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial sering dianggap materi lanjut, dalam kurikulum SMP kelas 8, ini adalah prosedur standar untuk topik korespondensi satu-satu. Soal tidak memerlukan penalaran tambahan selain mengingat rumus. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4403`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan rumus faktorial (n!) untuk menentukan banyaknya korespondensi satu-satu. Prosedur ini bersifat langsung dan rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu.
- Dimensi pengetahuan `procedural`: Soal ini menguji penerapan algoritma faktorial (prosedural) dalam konteks konsep korespondensi satu-satu.
- Intended difficulty `Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengingat atau menerapkan rumus n! untuk n=9. Tidak ada perencanaan strategi yang kompleks, kendala yang berinteraksi, atau kebutuhan untuk melakukan perpindahan representasi. Meskipun angka 9! cukup besar, beban kalkulasi masih dalam batas wajar untuk tingkat SMP.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep korespondensi satu-satu dan operasi faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial sering dianggap materi pengayaan, dalam konteks kurikulum SMP, ini adalah prosedur standar untuk topik korespondensi satu-satu. Soal tidak memerlukan penalaran tambahan selain menerapkan rumus. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `4facb7c0ab4ee644d3112751`

Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

| Opsi | Isi |
|---|---|
| A | $y^2 + x^2 = 25$ |
| B | $x^2 + 3y = 7$ |
| C | $x + 2y = 0$ |
| D | $\frac{y}{3x} + 3x = 9$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Persamaan garis lurus dalam dua variabel (x dan y) memiliki bentuk umum ax + by + c = 0, di mana variabel x dan y berpangkat satu. Opsi C (x + 2y = 0) memenuhi syarat ini. Opsi A dan B mengandung variabel berpangkat dua (lingkaran/parabola), dan opsi D mengandung variabel di penyebut (bukan linear).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f2f4db5d879c211bd0dfa28f16ffc7650a27d2be5e70dad93199243ce76a4d32`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2599 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2599 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2561 |

Run 1 — solusi: Persamaan garis lurus dalam dua variabel (x dan y) memiliki bentuk umum ax + by + c = 0, di mana variabel x dan y berpangkat satu. Opsi C (x + 2y = 0) memenuhi syarat ini. Opsi A dan B mengandung variabel berpangkat dua (lingkaran/parabola), dan opsi D mengandung variabel di penyebut (bukan linear).
- Domain kognitif `classify/knowing`: Siswa perlu mengenali karakteristik bentuk aljabar dari persamaan linear dua variabel (variabel berpangkat satu) dan membedakannya dari bentuk non-linear (pangkat dua atau variabel di penyebut). Ini adalah pengenalan konsep dasar.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi persamaan garis lurus dalam bentuk aljabar.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu memeriksa pangkat variabel pada setiap opsi untuk menentukan mana yang linear. Tidak ada langkah perhitungan kompleks atau perencanaan strategi yang diperlukan.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk aljabar linear (ax + by + c = 0) dan konsep pangkat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenali bentuk persamaan linear adalah materi dasar kelas 8 yang diajarkan secara eksplisit di awal bab persamaan garis lurus. |

Run 2 — solusi: Persamaan garis lurus dalam variabel x dan y memiliki bentuk umum ax + by + c = 0, di mana pangkat tertinggi variabel adalah 1. Opsi C, x + 2y = 0, memenuhi syarat ini (dapat ditulis y = -1/2 x). Opsi A dan B mengandung variabel berpangkat 2 (lingkaran/parabola), dan opsi D mengandung variabel di penyebut (bukan linear).
- Domain kognitif `classify/knowing`: Siswa perlu mengenali karakteristik bentuk persamaan linear (variabel berpangkat satu) dan membedakannya dari bentuk non-linear (kuadrat atau variabel di penyebut) untuk mengklasifikasikan persamaan yang diberikan.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi dan bentuk umum persamaan garis lurus (linear) dibandingkan dengan bentuk non-linear.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) karena hanya meminta identifikasi bentuk persamaan linear yang sudah dipelajari di kelas 8. Tidak ada langkah perhitungan kompleks atau perencanaan strategi yang diperlukan.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk umum persamaan linear ax + by + c = 0. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu membedakan persamaan linear dari non-linear sebagai dasar materi persamaan garis lurus. |

Run 3 — solusi: Persamaan garis lurus dalam variabel x dan y memiliki bentuk umum ax + by + c = 0, di mana pangkat tertinggi dari variabel adalah 1. Opsi C, x + 2y = 0, memenuhi syarat ini karena variabel x dan y berpangkat 1. Opsi A dan B mengandung variabel berpangkat 2 (kuadrat), sedangkan opsi D mengandung variabel di penyebut (non-linear).
- Domain kognitif `classify/knowing`: Siswa perlu mengenali karakteristik bentuk aljabar dari persamaan garis lurus (linear) dan membedakannya dari bentuk non-linear (kuadrat atau rasional). Ini adalah pengenalan konsep dasar.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi persamaan linear dua variabel sebagai representasi garis lurus.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman definisi dasar. Siswa hanya perlu mengidentifikasi pangkat variabel dalam persamaan linear.. Bukti: Manakah dari persamaan berikut yang dapat ditafsirkan sebagai persamaan garis lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk aljabar linear (variabel berpangkat satu). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenali bentuk persamaan linear adalah materi dasar kelas 8. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `0ca950fcf46ff904f0263642`

Hargai bahwa setiap titik pada garis harus memenuhi persamaan yang sesuai dan digunakan untuk menentukan nilai y dari nilai x, atau sebaliknya. Sehingga, apabila suatu garis lurus persamaannya adalah y = 2 x - 3.<br><br>Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.

| Opsi | Isi |
|---|---|
| A | x = 3,5 (atau 7/2) |
| B | x = 5 |
| C | x = 2 |
| D | x = 0,5 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Substitusikan y = 4 ke dalam persamaan y = 2x - 3, sehingga 4 = 2x - 3. Tambahkan 3 pada kedua ruas menjadi 7 = 2x. Bagi dengan 2, diperoleh x = 3,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0fac64c5de058693be1a6691aaf23af5e1d6fd8084684d5ba990113b1c6dac89`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2646 |
| 2 | success | valid / verified | applying | procedural | Easy | 2633 |
| 3 | success | valid / verified | applying | procedural | Easy | 2636 |

Run 1 — solusi: Substitusikan y = 4 ke dalam persamaan y = 2x - 3, sehingga 4 = 2x - 3. Tambahkan 3 pada kedua ruas menjadi 7 = 2x. Bagi dengan 2, diperoleh x = 3,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur substitusi nilai yang diketahui ke dalam persamaan linear yang diberikan untuk mencari variabel yang tidak diketahui. Ini adalah penerapan langsung dari konsep fungsi linear.. Bukti: Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menyelesaikan persamaan linear satu variabel setelah substitusi nilai koordinat.. Bukti: y = 2 x - 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Siswa hanya perlu melakukan substitusi dan manipulasi aljabar dasar (penjumlahan dan pembagian) untuk menyelesaikan persamaan linear satu variabel. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4, maka carilah koordinat x dari p.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan linear satu variabel dan substitusi nilai ke dalam persamaan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan standar untuk materi persamaan garis lurus di kelas 8, di mana siswa diharapkan mampu menghubungkan titik pada koordinat kartesius dengan persamaan aljabarnya. |

Run 2 — solusi: Substitusi y = 4 ke dalam persamaan y = 2x - 3, sehingga 4 = 2x - 3. Tambahkan 3 ke kedua sisi: 7 = 2x. Bagi dengan 2: x = 3,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur substitusi nilai yang diketahui ke dalam persamaan linear satu variabel yang diberikan untuk mencari nilai variabel lainnya. Ini adalah penerapan langsung dari konsep fungsi linear.. Bukti: Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menyelesaikan persamaan linear satu variabel setelah melakukan substitusi nilai ke dalam rumus fungsi yang diberikan.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan substitusi satu nilai dan menyelesaikan persamaan linear satu variabel sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan linear satu variabel dan substitusi nilai ke dalam persamaan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi persamaan garis lurus adalah standar kelas 8. Soal ini merupakan latihan dasar yang sering ditemui siswa untuk memahami hubungan antara titik dan persamaan garis. |

Run 3 — solusi: Substitusikan y = 4 ke dalam persamaan y = 2x - 3, sehingga 4 = 2x - 3. Tambahkan 3 pada kedua ruas menjadi 7 = 2x. Bagi dengan 2, diperoleh x = 3,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur substitusi nilai yang diketahui ke dalam persamaan linear yang diberikan untuk mencari variabel yang tidak diketahui. Ini adalah penerapan langsung dari konsep fungsi linear.. Bukti: Titik p terletak pada garis lurus tersebut dan koordinat y dari p adalah 4, maka carilah koordinat x dari p.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menyelesaikan persamaan linear satu variabel setelah melakukan substitusi nilai koordinat.. Bukti: y = 2 x - 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan substitusi satu nilai dan menyelesaikan persamaan linear satu variabel sederhana (dua langkah aljabar). Tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: y = 2 x - 3; koordinat y dari p adalah 4, maka carilah koordinat x dari p.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat kartesius dan penyelesaian persamaan linear satu variabel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi persamaan garis lurus adalah standar kelas 8. Soal ini menguji pemahaman dasar hubungan titik dan persamaan tanpa kerumitan tambahan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `6d6cb72cedbdc46857aa2701`

Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....

| Opsi | Isi |
|---|---|
| A | 3x + 4y - 14 = 0 |
| B | 4x - 3y + 14 = 0 |
| C | 3x - 4y + 33 = 0 |
| D | 4x + 3y - 14 = 0 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Karena sisi persegi panjang sejajar sumbu koordinat, titik P(2,-1) dan R(6,2) menentukan titik Q(6,-1) dan S(2,2). Gradien garis QS adalah m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4 adalah y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b9c308aeda23f1bf31e9c543e2199ea69610ec8c85c8b22318095f02d36be1dc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2778 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2835 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2815 |

Run 1 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S adalah (6,-1) dan (2,2). Kemiringan m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4: y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat persegi panjang dengan sisi sejajar sumbu untuk menentukan koordinat titik Q dan S, lalu menerapkan rumus kemiringan dan persamaan garis. Ini melibatkan penerapan konsep pada konteks geometri koordinat.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip geometri (sifat persegi panjang) dan prosedur aljabar (menentukan persamaan garis) untuk menyelesaikan masalah.. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep bahwa sisi sejajar sumbu berarti koordinat x dan y titik Q dan S dapat ditentukan dari P dan R. Langkah-langkahnya (menentukan titik, menghitung gradien, menyusun persamaan) saling terkait namun prosedural dan familiar bagi siswa kelas 8.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan; sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep koordinat kartesius, gradien garis, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari persamaan garis lurus dan koordinat. Menentukan titik Q dan S dari P dan R memerlukan pemahaman visual/konseptual tentang persegi panjang yang sejajar sumbu, yang merupakan tantangan menengah. |

Run 2 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik Q dan S adalah (6,-1) dan (2,2). Kemiringan m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4 adalah y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu mengonseptualisasikan sifat persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan prosedur mencari kemiringan dan persamaan garis. Ini adalah penerapan konsep dalam konteks rutin.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman hubungan antara sifat geometris (persegi panjang sejajar sumbu) dan representasi aljabar (persamaan garis), yang merupakan pengetahuan konseptual.. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah: menentukan koordinat Q dan S, menghitung gradien, dan menyusun persamaan garis. Meskipun prosedural, siswa harus memahami implikasi geometris dari 'sejajar sumbu' untuk mendapatkan titik yang tepat. Ini adalah tugas Medium karena melibatkan integrasi konsep geometri dan aljabar dengan jalur yang jelas namun memerlukan perencanaan langkah.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menghubungkan sifat geometri dengan koordinat. Langkah-langkahnya standar namun memerlukan ketelitian dalam menentukan titik Q dan S dari diagonal PR. |

Run 3 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik P(2,-1) dan R(6,2) menentukan titik Q(6,-1) dan S(2,2). Gradien garis QS adalah m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4 adalah y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat persegi panjang dengan sisi sejajar sumbu untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus gradien dan persamaan garis. Ini melibatkan pemilihan prosedur yang tepat (applying) untuk menyelesaikan masalah geometri koordinat.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara geometri (persegi panjang) dan aljabar (persamaan garis), yang merupakan pengetahuan konseptual.. Bukti: sisi sejajar sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah: menentukan koordinat Q dan S, menghitung gradien, dan menyusun persamaan garis. Meskipun prosedurnya familiar, integrasi antara properti geometri dan aljabar koordinat membuat tingkat kesulitannya menengah bagi siswa kelas 8.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, konsep gradien, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari persamaan garis lurus dan koordinat. Menentukan koordinat titik lain dari diagonal persegi panjang yang sejajar sumbu adalah tantangan menengah yang sesuai. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4763`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan pemahaman tentang sifat persegi panjang (sisi sejajar sumbu) untuk menentukan koordinat titik Q dan S, kemudian menerapkan prosedur mencari gradien dan persamaan garis. Ini adalah penerapan konsep geometri koordinat dalam konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman hubungan antara sifat geometris (persegi panjang sejajar sumbu) dan representasi aljabar (persamaan garis), yang merupakan pengetahuan konseptual.
- Intended difficulty `Medium`: Soal memerlukan beberapa langkah: menentukan koordinat Q dan S, menghitung gradien, dan menyusun persamaan garis. Meskipun prosedurnya familiar, integrasi antara properti geometri dan aljabar koordinat membuat tingkat kesulitannya menengah bagi siswa kelas 8.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, sifat persegi panjang, rumus gradien, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 sudah mempelajari persamaan garis lurus dan koordinat. Menentukan koordinat titik lain dari diagonal persegi panjang yang sejajar sumbu adalah tantangan menengah yang sesuai. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `170c704eff34e359339670a8db426fb25b69eca837283ef0d4580ce7f8472511`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3709 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3644 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3652 |

Run 1 — solusi: Tinggi setiap anak tangga = Total Height / jumlah anak tangga = 252 cm / 14 = 18 cm.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur pembagian sederhana untuk menentukan tinggi satu unit anak tangga berdasarkan total tinggi yang diberikan. Ini adalah penerapan langsung dari konsep pembagian dalam konteks rutin.. Bukti: Total Height 252 cm; 14 anak tangga; Total tinggi untuk setiap pijakan dari 14 pijakan adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana membagi total nilai menjadi bagian-bagian yang sama besar dalam konteks fisik.. Bukti: Total Height 252 cm; 14 anak tangga
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi informasi yang relevan (total tinggi dan jumlah anak tangga) dan melakukan satu operasi pembagian. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 14 anak tangga dengan tinggi 252 cm; Total tinggi untuk setiap pijakan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan aritmatika dasar yang sangat rutin untuk kelas 8, tidak memerlukan pemahaman mendalam tentang kemiringan (slope) meskipun subtopiknya adalah kemiringan. |

Run 2 — solusi: Tinggi setiap anak tangga = Total Height / jumlah anak tangga = 252 cm / 14 = 18 cm.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi informasi yang relevan (total tinggi dan jumlah anak tangga) dan menerapkan operasi pembagian sederhana untuk menemukan tinggi per anak tangga.. Bukti: Total Height 252 cm; 14 anak tangga; Total tinggi untuk setiap pijakan dari 14 pijakan adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang pembagian untuk mencari nilai satuan (tinggi per anak tangga) dari total yang diberikan.. Bukti: Total Height 252 cm; 14 anak tangga
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu melakukan satu operasi pembagian sederhana. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 14 anak tangga; Total Height 252 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu melakukan pembagian sederhana untuk menentukan nilai satuan dalam konteks nyata. |

Run 3 — solusi: Tinggi setiap anak tangga = Total Height / jumlah anak tangga = 252 cm / 14 = 18 cm.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi informasi yang relevan (total tinggi dan jumlah anak tangga) dan menerapkan prosedur pembagian sederhana untuk menemukan tinggi per anak tangga.. Bukti: 14 anak tangga dengan tinggi 252 cm; Total tinggi untuk setiap pijakan dari 14 pijakan adalah
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep pembagian rata (prosedural) untuk menentukan nilai per unit dari total yang diberikan.. Bukti: Total Height 252 cm; 14 anak tangga
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu melakukan satu operasi pembagian sederhana. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 14 anak tangga dengan tinggi 252 cm; Total Height 252 cm

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
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep pembagian dasar yang sudah dikuasai siswa kelas 8, dengan konteks visual yang sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4975`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta siswa untuk menerapkan prosedur pembagian sederhana untuk menentukan nilai satuan (tinggi per anak tangga) dari total yang diberikan. Ini adalah penerapan langsung dari konsep aritmatika dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Siswa perlu menggunakan prosedur pembagian bilangan bulat untuk memecahkan masalah nilai satuan, yang merupakan pengetahuan prosedural dasar.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi informasi yang relevan dan melakukan satu operasi pembagian. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan aritmatika dasar yang sangat rutin untuk kelas 8. Meskipun subtopiknya adalah kemiringan, soal ini hanya menguji pembagian sederhana. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `bc70cacaad85275414d879e3`

Rata-rata tinggi 12 anak adalah 166 cm. Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm. Berapa rata-rata tinggi 6 anak?

| Opsi | Isi |
|---|---|
| A | 169 cm |
| B | 166,5 cm |
| C | 84,5 cm |
| D | 167 cm |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total tinggi 12 anak = 12 * 166 = 1992. Total tinggi 18 anak = 18 * 167 = 3006. Total tinggi 6 anak tambahan = 3006 - 1992 = 1014. Rata-rata 6 anak = 1014 / 6 = 169 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fbc2df27e24d5f72ab51e05c0d9643ebb2243e3c74a15136e4961d5180f0152e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2797 |
| 2 | success | valid / verified | applying | procedural | Medium | 2783 |
| 3 | success | valid / verified | applying | procedural | Medium | 2771 |

Run 1 — solusi: Total tinggi 12 anak = 12 * 166 = 1992. Total tinggi 18 anak = 18 * 167 = 3006. Total tinggi 6 anak tambahan = 3006 - 1992 = 1014. Rata-rata 6 anak = 1014 / 6 = 169 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata gabungan dan memanipulasi rumus rata-rata untuk menemukan nilai rata-rata kelompok data yang baru ditambahkan. Ini melibatkan pemilihan prosedur yang tepat (menghitung total, selisih, lalu rata-rata baru) yang merupakan penerapan konsep dalam konteks rutin.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.; Berapa rata-rata tinggi 6 anak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana rata-rata dihitung dan bagaimana hubungan antara jumlah data, total nilai, dan rata-rata bekerja.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait (menghitung dua total yang berbeda, mencari selisih, lalu membagi). Meskipun prosedurnya familiar, siswa harus merencanakan langkah-langkah tersebut secara berurutan tanpa bantuan eksplisit.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.; Berapa rata-rata tinggi 6 anak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar rata-rata (mean) dan operasi aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengelola perhitungan rata-rata gabungan. Soal ini menuntut ketelitian dalam mengidentifikasi jumlah data yang berubah (12 menjadi 18) dan membagi selisih total dengan jumlah anak yang tepat (6). |

Run 2 — solusi: Total tinggi 12 anak = 12 * 166 = 1992. Total tinggi 18 anak = 18 * 167 = 3006. Total tinggi 6 anak tambahan = 3006 - 1992 = 1014. Rata-rata 6 anak = 1014 / 6 = 169 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata gabungan dan memanipulasi rumus rata-rata untuk menemukan nilai rata-rata kelompok data yang baru ditambahkan. Ini adalah penerapan prosedur yang rutin dalam konteks rata-rata.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm. Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm. Berapa rata-rata tinggi 6 anak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana rata-rata dihitung dan bagaimana memanipulasi total nilai (jumlah data) untuk mendapatkan informasi yang hilang.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah logis yang saling terkait (menghitung total awal, total akhir, selisih, lalu rata-rata baru) dan pemahaman bahwa rata-rata tidak bisa dijumlahkan secara langsung. Meskipun prosedurnya familiar, siswa harus merencanakan urutan operasi dengan benar.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar rata-rata (mean) dan operasi hitung dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengolah data rata-rata. Soal ini menuntut ketelitian dalam mengelola jumlah data yang berubah (12 menjadi 18) dan menghitung rata-rata kelompok parsial, yang merupakan standar kompetensi menengah. |

Run 3 — solusi: Total tinggi 12 anak = 12 * 166 = 1992 cm. Total tinggi 18 anak (12+6) = 18 * 167 = 3006 cm. Total tinggi 6 anak tambahan = 3006 - 1992 = 1014 cm. Rata-rata tinggi 6 anak = 1014 / 6 = 169 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep rata-rata gabungan dan melakukan manipulasi aljabar sederhana untuk mencari nilai rata-rata kelompok baru. Ini adalah penerapan prosedur rata-rata yang rutin.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.; Berapa rata-rata tinggi 6 anak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung rata-rata dari data yang digabungkan.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah perhitungan yang saling terkait (menghitung total awal, total akhir, selisih, dan rata-rata baru) serta pemahaman konsep rata-rata yang tidak sekadar menghitung rata-rata dari dua angka yang diberikan.. Bukti: Rata-rata tinggi 12 anak adalah 166 cm.; Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm.; Berapa rata-rata tinggi 6 anak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep rata-rata (mean) dan operasi hitung dasar. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengolah data rata-rata dengan jumlah anggota yang berbeda. Soal ini menuntut ketelitian dalam mengelola total nilai, yang merupakan standar kemampuan kelas 8. |

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
Soal: Rata-rata tinggi 12 anak adalah 166 cm. Setelah ditambah 6 anak, rata-rata tingginya menjadi 167 cm. Berapa rata-rata tinggi 6 anak?
Pilihan: A. 169 cm
B. 166,5 cm
C. 84,5 cm
D. 167 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `962364d9c3511c0598f13509`

Rata-rata berat badan 9 anak adalah 56 kg, jika berat badan Domi dimasukkan dalam hitungan tersebut, rata-ratanya menjadi 56,7. Tentukan berat badan Doni.

| Opsi | Isi |
|---|---|
| A | 7 kg |
| B | 63 kg |
| C | 56,7 kg |
| D | 6,3 kg |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak = 10 * 56,7 = 567 kg. Berat anak tambahan = 567 - 504 = 63 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6bb130b8d3e25ce0e8ac95ef31e831d7be027ac8af444275dedba683da1336ae`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / verified | applying | procedural | Easy | 2747 |
| 2 | success | valid / verified | applying | procedural | Easy | 2737 |
| 3 | success | concern / verified | applying | procedural | Easy | 2753 |

Run 1 — solusi: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak (setelah Domi masuk) = 10 * 56,7 = 567 kg. Berat Domi = 567 - 504 = 63 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata (mean) untuk mencari total nilai dari data yang ada, kemudian melakukan operasi pengurangan untuk menemukan nilai data yang baru ditambahkan. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7; Tentukan berat badan Doni
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana rata-rata dihitung dan bagaimana memanipulasi rumus rata-rata untuk menemukan nilai data yang hilang.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar dan familiar bagi siswa kelas 8. Siswa hanya perlu menghitung total awal, total akhir, dan selisihnya. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep rata-rata (mean) dan operasi hitung perkalian/pengurangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi rata-rata adalah kurikulum standar SMP kelas 8. Soal ini menggunakan prosedur langsung yang sering dilatih di kelas. |

Run 2 — solusi: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak = 10 * 56,7 = 567 kg. Berat anak tambahan = 567 - 504 = 63 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata (mean) untuk mencari total nilai dari rata-rata yang diketahui, kemudian mencari selisih antara dua kondisi (sebelum dan sesudah penambahan data). Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7; Tentukan berat badan Doni
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana rata-rata dihitung dan bagaimana memanipulasi rumus rata-rata untuk menemukan nilai data yang hilang.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan prosedur standar yang familiar bagi siswa kelas 8. Jalur penyelesaiannya langsung (menghitung total, lalu mencari selisih) tanpa memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang rumit.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rumus rata-rata (mean) dan operasi hitung bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi rata-rata adalah topik dasar di kelas 8. Soal ini tidak memiliki jebakan konseptual yang berat, hanya memerlukan ketelitian dalam operasi perkalian dan pengurangan. |

Run 3 — solusi: Total berat 9 anak = 9 * 56 = 504 kg. Total berat 10 anak (setelah Domi masuk) = 10 * 56,7 = 567 kg. Berat Domi = 567 - 504 = 63 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rata-rata (mean) untuk mencari total nilai dari rata-rata yang diketahui, kemudian mencari selisih antara dua kondisi (sebelum dan sesudah penambahan data). Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; jika berat badan Domi dimasukkan dalam hitungan tersebut, rata-ratanya menjadi 56,7; Tentukan berat badan Doni
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana rata-rata dihitung dan bagaimana memanipulasi rumus rata-rata untuk menemukan nilai data yang hilang.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan prosedur yang sangat familiar bagi siswa kelas 8 (mencari total dari rata-rata). Langkah penyelesaiannya linear dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi konsep yang sulit.. Bukti: Rata-rata berat badan 9 anak adalah 56 kg; rata-ratanya menjadi 56,7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar rata-rata (mean) dan operasi perkalian/pengurangan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi rata-rata adalah kurikulum standar kelas 8. Prosedur mencari nilai data baru dari perubahan rata-rata adalah latihan rutin yang umum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4411`.
Konten: `concern`; kunci: `verified`; masalah: Terdapat ketidakkonsistenan nama subjek dalam soal. Premis menyebutkan 'Domi', namun pertanyaan menanyakan berat badan 'Doni'. Meskipun secara matematis dapat diselesaikan, ini adalah kesalahan penulisan yang membingungkan..
- Domain kognitif `applying`: Siswa perlu menerapkan konsep rata-rata (mean) untuk mencari total nilai dari rata-rata yang diketahui, kemudian mencari selisih antara dua kondisi (sebelum dan sesudah penambahan data). Ini adalah penerapan prosedur standar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang bagaimana rata-rata dihitung dan bagaimana memanipulasi rumus rata-rata untuk menemukan nilai data yang hilang.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar dan familiar bagi siswa kelas 8. Siswa hanya perlu menghitung total awal, total akhir, dan selisihnya. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep rata-rata (mean) dan operasi hitung perkalian/pengurangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi rata-rata adalah kurikulum standar SMP kelas 8. Soal ini menggunakan prosedur langsung yang sering dilatih di kelas. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidakkonsistenan nama subjek dalam soal. Premis menyebutkan 'Domi', namun pertanyaan menanyakan berat badan 'Doni'. Meskipun secara matematis dapat diselesaikan, ini adalah kesalahan penulisan yang membingungkan..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |
| B | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| C | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 (median) = (65+70)/2 = 67,5. Q1 (median 7 data pertama: 50, 50, 60, 65, 65, 65, 65) = 65. Q3 (median 7 data terakhir: 70, 75, 80, 80, 85, 85, 90) = 80. Jangkauan kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0bca2179124122b4e4e9dea41da181b7fdb604b15cfab36197489aa0ad0d76ee`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3128 |
| 2 | success | valid / verified | applying | procedural | Medium | 3054 |
| 3 | success | valid / verified | applying | procedural | Medium | 3137 |

Run 1 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 (median) = (65+70)/2 = 67,5. Q1 (median 7 data pertama: 50, 50, 60, 65, 65, 65, 65) = 65. Q3 (median 7 data terakhir: 70, 75, 80, 80, 85, 85, 90) = 80. Jangkauan kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar (mengurutkan data, mencari median, Q1, Q3, dan menghitung jangkauan/simpangan kuartil) pada kumpulan data yang diberikan. Ini adalah penerapan prosedur rutin.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan algoritme atau metode statistik untuk menentukan ukuran penyebaran data.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data (14 data) dan perhitungan bertahap yang familiar bagi siswa kelas 8. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan, hanya ketelitian dalam prosedur.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan data dan menghitung median. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun prosedurnya rutin, jumlah data (14) dan perlunya ketelitian dalam mengurutkan serta membagi data menjadi dua kelompok untuk mencari kuartil membuat tingkat kesulitannya berada di level menengah bagi siswa kelas 8. |

Run 2 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q1 (kuartil bawah) adalah median dari 7 data pertama: 65. Q3 (kuartil atas) adalah median dari 7 data terakhir: 80. Jangkauan antar kuartil (H) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil (Qd) = 0,5 * H = 0,5 * 15 = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik deskriptif (mencari kuartil dan simpangan kuartil) pada sekumpulan data yang diberikan. Ini adalah penerapan langsung dari prosedur yang sudah dipelajari.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritme atau metode statistik untuk menentukan ukuran penyebaran data.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan pengurutan data (14 data) dan perhitungan bertahap (Q1, Q3, jangkauan, simpangan kuartil). Meskipun prosedurnya rutin, jumlah data yang cukup banyak meningkatkan beban kognitif dan risiko kesalahan hitung, namun jalur penyelesaiannya sangat jelas dan familiar bagi siswa kelas 8.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data, menentukan median, dan memahami definisi kuartil serta simpangan kuartil. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengolah data statistik sederhana. Tugas ini memerlukan ketelitian dalam mengurutkan data dan menerapkan rumus, yang sesuai dengan tingkat kesulitan menengah untuk jenjang tersebut. |

Run 3 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 (median) = (65+70)/2 = 67,5. Q1 (median 7 data pertama: 50, 50, 60, 65, 65, 65, 65) = 65. Q3 (median 7 data terakhir: 70, 75, 80, 80, 85, 85, 90) = 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik untuk menentukan kuartil dan simpangan kuartil dari sekumpulan data. Ini adalah penerapan langsung dari prosedur yang dipelajari di kelas 8.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme dan metode perhitungan statistik (kuartil, jangkauan, simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan ketelitian dalam mengurutkan data (14 data) dan menerapkan prosedur bertahap (mencari median, Q1, Q3, lalu menghitung jangkauan dan simpangan kuartil). Meskipun prosedurnya rutin, jumlah data yang cukup banyak meningkatkan beban kognitif dan risiko kesalahan hitung.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengolah data statistik dasar. Kompleksitas terletak pada ketelitian pengurutan dan penerapan rumus bertahap. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `2638edf211f383d8d9b95e05`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

| Opsi | Isi |
|---|---|
| A | Q1 = 7,5; Q2 = 6; Q3 = 4; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| B | Q1 = 4; Q2 = 5,83; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| C | Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 1,75 |
| D | Q1 = 4; Q2 = 6; Q3 = 7,5; jangkauan kuartil = 3,5; simpangan kuartil = 3,5 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9 (n=12). Q2 (median) = (6+6)/2 = 6. Q1 (median 6 data pertama: 3,4,4,4,5,6) = (4+4)/2 = 4. Q3 (median 6 data terakhir: 6,7,8,8,8,9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 1,75.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a5f4c9d7a50b3f2f62e8ec503e20395f9481ef105fe4e489ae6bdea12665f546`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3023 |
| 2 | success | valid / verified | applying | procedural | Easy | 3021 |
| 3 | success | valid / verified | applying | procedural | Medium | 3042 |

Run 1 — solusi: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9. n=12. Median (Q2) = (6+6)/2 = 6. Q1 (median 6 data pertama: 3,4,4,4,5,6) = (4+4)/2 = 4. Q3 (median 6 data terakhir: 6,7,8,8,8,9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 1,75.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik untuk menentukan nilai kuartil, jangkauan antar kuartil, dan simpangan kuartil dari sekumpulan data. Ini adalah penerapan prosedur rutin pada konteks data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penggunaan algoritme atau metode statistik untuk menghitung ukuran penyebaran data.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah berurutan yang saling terkait (mengurutkan data, membagi data menjadi dua bagian, menghitung median untuk Q1, Q2, Q3, lalu menghitung IQR dan simpangan kuartil). Meskipun prosedurnya rutin, siswa harus teliti dalam setiap langkah agar tidak terjadi kesalahan perhitungan.. Bukti: 3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang median, pengurutan data, dan definisi kuartil. |
| dependentSteps | 5 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 12 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengolah data statistik sederhana. Langkah-langkahnya jelas namun memerlukan ketelitian tinggi dalam pengurutan dan pembagian data. |

Run 2 — solusi: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9 (n=12). Median (Q2) = (6+6)/2 = 6. Q1 (median data bawah: 3, 4, 4, 4, 5, 6) = (4+4)/2 = 4. Q3 (median data atas: 6, 6, 7, 8, 8, 9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 0,5 * 3,5 = 1,75.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar untuk menentukan ukuran penyebaran data (kuartil, jangkauan antar kuartil, simpangan kuartil) pada sekumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritme atau metode statistik untuk menghitung nilai-nilai penyebaran data.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 8. Langkah-langkah penyelesaiannya jelas: mengurutkan data, membagi data menjadi dua bagian, menentukan median dari masing-masing bagian, dan melakukan operasi pengurangan/pembagian sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: 3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan data dan menentukan median. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 12 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kuartil dan simpangan kuartil adalah standar kurikulum kelas 8. Prosedur yang diperlukan bersifat langsung dan familiar. |

Run 3 — solusi: Data terurut: 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9. n=12. Median (Q2) = (6+6)/2 = 6. Q1 (median 6 data pertama: 3, 4, 4, 4, 5, 6) = (4+4)/2 = 4. Q3 (median 6 data terakhir: 6, 6, 7, 8, 8, 9) = (7+8)/2 = 7,5. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 7,5 - 4 = 3,5. Simpangan kuartil = 0,5 * IQR = 1,75.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik untuk menentukan kuartil, jangkauan antar kuartil, dan simpangan kuartil dari sekumpulan data. Ini adalah penerapan langsung dari prosedur yang dipelajari di kelas 8.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan metode perhitungan statistik deskriptif (kuartil dan simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah berurutan (mengurutkan data, mencari median, membagi data menjadi dua bagian, mencari median masing-masing bagian, lalu menghitung IQR dan simpangan kuartil). Meskipun prosedurnya rutin, terdapat beberapa langkah yang saling terkait yang harus dilakukan dengan teliti.. Bukti: 3, 6, 4, 4, 8, 7, 8, 9, 4, 5, 6, 6

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
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu menghitung statistik dasar ini. Tingkat kesulitan Medium diberikan karena jumlah langkah yang harus dilakukan secara berurutan dan potensi kesalahan pada setiap langkah (seperti pengurutan atau pembagian data). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5051`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur statistik rutin untuk mengolah data. Tidak ada strategi non-rutin yang diperlukan, hanya penerapan algoritma yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal menguji penguasaan algoritma dan metode perhitungan statistik deskriptif (kuartil, jangkauan, simpangan kuartil).
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya rutin, terdapat banyak langkah berurutan (mengurutkan, membagi data, menghitung median, menghitung IQR, menghitung simpangan) yang saling bergantung. Kesalahan pada satu langkah (terutama pengurutan atau pembagian data) akan berakibat fatal pada hasil akhir, sehingga menuntut ketelitian tinggi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data, menentukan median data genap, memahami definisi kuartil. |
| dependentSteps | 5 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 12 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 8 diharapkan mampu mengolah data statistik sederhana. Tingkat kesulitan Medium mencerminkan beban ketelitian yang diperlukan dalam mengurutkan 12 data dan melakukan serangkaian operasi statistik tanpa bantuan langkah. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `e8a6fabcd6f67b1be8f8ad7f`

Berikut data tingkat suku bunga deposito untuk jangka waktu 12 bulan di beberapa bank di Indonesia per tanggal 9 Maret 2022. Tingkat suku bunga selalu dinyatakan dalam persen.<br><br>Tabel 6.11 Tingkat Suku Bunga Deposito Jangka 12 Bulan<br><br>\| Nama Bank \| Tingkat Suku Bunga Deposito \|<br>\|---\|---\|<br>\| Bank Mandiri \| 2,50 % \|<br>\| BNI 1946 \| 2,50 % \|<br>\| BRI \| 2,50 % \|<br>\| BCA \| 1,90 % \|<br>\| Bank Maspion \| 4,75 % \|<br><br>Walaupun data di atas berbentuk persen, kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Mengapa demikian? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Karena suku bunga berupa bilangan desimal yang tidak dapat diubah menjadi sudut |
| B | Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan (jumlahnya tidak 100%) |
| C | Karena beberapa bank memiliki suku bunga yang sama sehingga juringnya bertumpuk |
| D | Karena banyaknya bank lebih dari 4 sehingga lingkaran tidak dapat dibagi |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Diagram lingkaran merepresentasikan bagian dari keseluruhan (proporsi) di mana total seluruh bagian harus 100%. Suku bunga deposito adalah nilai persentase masing-masing bank yang berdiri sendiri, bukan bagian dari satu kesatuan total (jumlahnya 2,5+2,5+2,5+1,9+4,75 = 14,15%, bukan 100%).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 8 / Matematika SMP Kelas 8. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a9d034acf455d34f108a35b845f34a5778b77a6a6275cb6eeb946f815d0cd810`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2721 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3762 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2769 |

Run 1 — solusi: Diagram lingkaran merepresentasikan bagian dari keseluruhan (proporsi) di mana total seluruh bagian harus 100%. Suku bunga deposito adalah nilai persentase masing-masing bank yang berdiri sendiri, bukan bagian dari satu kesatuan total (jumlahnya 2,5+2,5+2,5+1,9+4,75 = 14,15%, bukan 100%).
- Domain kognitif `classify/applying`: Siswa diminta untuk memahami prinsip dasar representasi data menggunakan diagram lingkaran, yaitu bahwa diagram tersebut menunjukkan proporsi bagian terhadap keseluruhan (total 100%). Ini memerlukan pemahaman konseptual tentang syarat penggunaan diagram lingkaran.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Mengapa demikian?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip atau aturan (konsep) kapan suatu jenis diagram statistik (diagram lingkaran) tepat digunakan.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menguji pemahaman dasar tentang syarat penggunaan diagram lingkaran yang merupakan materi standar kelas 8. Tidak ada perhitungan kompleks atau perencanaan strategi yang rumit; siswa hanya perlu mengenali bahwa data tersebut bukan merupakan bagian dari satu kesatuan (whole).. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram lingkaran sebagai representasi bagian dari keseluruhan (100%). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan memahami karakteristik diagram lingkaran. Soal ini langsung menanyakan konsep dasar tanpa memerlukan manipulasi data yang berat. |

Run 2 — solusi: Diagram lingkaran digunakan untuk menunjukkan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito adalah nilai independen, bukan bagian dari satu kesatuan, dan jumlahnya (14,15%) tidak mencapai 100%, sehingga tidak tepat disajikan dalam diagram lingkaran.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konseptual tentang syarat penggunaan diagram lingkaran (bagian dari keseluruhan) pada data yang diberikan.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas; Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual mengenai fungsi dan syarat penggunaan diagram lingkaran.. Bukti: diagram lingkaran untuk merepresentasikan data di atas; bukan bagian dari satu keseluruhan
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung. Siswa hanya perlu memahami definisi diagram lingkaran. Tidak ada perhitungan rumit atau perencanaan strategi yang kompleks.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas; Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran sebagai representasi bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pemilihan diagram adalah bagian dari kurikulum SMP kelas 8. Soal ini menguji pemahaman dasar tanpa beban komputasi. |

Run 3 — solusi: Diagram lingkaran (pie chart) digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito adalah nilai persentase masing-masing bank yang berdiri sendiri, bukan bagian dari satu kesatuan total 100%. Jumlah suku bunga bank-bank tersebut (2,5+2,5+2,5+1,9+4,75 = 14,15%) tidak sama dengan 100%, sehingga tidak dapat membentuk satu lingkaran utuh.
- Domain kognitif `classify/applying`: Siswa diminta untuk memahami prinsip dasar penggunaan diagram lingkaran, yaitu merepresentasikan bagian dari keseluruhan (part-to-whole). Ini memerlukan pemahaman konseptual tentang kapan diagram lingkaran tepat digunakan, bukan sekadar menghitung.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Mengapa demikian?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip atau aturan penggunaan representasi data (diagram lingkaran), yang merupakan pengetahuan konseptual.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menguji pemahaman dasar tentang syarat penggunaan diagram lingkaran. Siswa hanya perlu mengenali bahwa data tersebut bukan bagian dari satu kesatuan (part-to-whole) yang berjumlah 100%. Tidak ada perhitungan kompleks atau perencanaan strategi yang rumit.. Bukti: Walaupun data di atas berbentuk persen, kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran sebagai representasi bagian dari keseluruhan (proporsi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 8 diharapkan memahami karakteristik dasar diagram statistik. Membedakan data yang bersifat proporsional (bagian dari total) dengan data yang bersifat independen adalah konsep dasar dalam statistika tingkat SMP. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
