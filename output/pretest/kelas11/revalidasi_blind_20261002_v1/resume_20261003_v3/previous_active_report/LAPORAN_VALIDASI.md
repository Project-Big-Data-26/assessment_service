# Validasi ulang soal kelas 11 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 62/66 run awal sukses; 1 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v8-blind-sma11-key-verified`. Rubrik: `math-rubric-3x4x3-v6-sma11-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 11 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 11, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 22; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 18, "knowing": 2, "undecided": 2, "reasoning": 0}, "knowledgeDimension": {"conceptual": 10, "procedural": 9, "factual": 1, "undecided": 2, "metacognitive": 0}, "intendedDifficulty": {"Medium": 4, "Easy": 15, "Hard": 1, "undecided": 2}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 17, "knowing": 2, "reasoning": 0}, "knowledgeDimension": {"conceptual": 9, "procedural": 9, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Medium": 4, "Easy": 15, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 19, "revision_required": 1, "llm_retry_or_manual_review": 2}`.
Run awal sukses: 62/66; adjudikasi: 7; token sukses tercatat: 183,917.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 15 | 15 | [Easy.json](difficulty/Easy.json) |
| Medium | 4 | 4 | [Medium.json](difficulty/Medium.json) |
| Hard | 1 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 11, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 11, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 11. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `6e23a873d17dbf71c29d8901`

Berdasarkan data, pada tahun 2001 perusahaan A mampu menjual 9 laptop. Pada tahun 2002 dan 2003 perusahaan A mampu menjual masing-masing 27 dan 81 laptop. Apabila relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial, berapa penjualan laptop pada tahun 2007?

| Opsi | Isi |
|---|---|
| A | 6.561 laptop (3^8) |
| B | 2.187 (3^7) |
| C | 486 (9, 27, 81, ... ditambah 81 tiap tahun sampai 2007) |
| D | 19.683 (3^9) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pola penjualan mengikuti fungsi eksponensial f(t) = 3^(t-1999), di mana t adalah tahun. Untuk tahun 2001, f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6.561.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a0e65ad65d0e7cd197ea41c9dd0dcfd21403de9195aa1367a4c5de353557f988`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2244 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2282 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2193 |

Run 1 — solusi: Pola penjualan mengikuti fungsi eksponensial f(t) = 3^(t-1999), di mana t adalah tahun. Untuk tahun 2001, f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6.561.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan dan menerapkan model tersebut untuk memprediksi nilai pada tahun tertentu.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial; tahun 2001 perusahaan A mampu menjual 9 laptop. Pada tahun 2002 dan 2003 perusahaan A mampu menjual masing-masing 27 dan 81 laptop
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang fungsi eksponensial dan bagaimana menerjemahkan pola data ke dalam bentuk fungsi.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi basis dan eksponen yang tepat (bukan sekadar melanjutkan deret aritmatika) dan melakukan perhitungan perpangkatan yang memerlukan ketelitian.. Bukti: tahun 2001... 9 laptop. Pada tahun 2002 dan 2003... 27 dan 81 laptop; berapa penjualan laptop pada tahun 2007?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan pola bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 sebagai aplikasi fungsi eksponensial sederhana dalam konteks pertumbuhan. |

Run 2 — solusi: Pola penjualan mengikuti fungsi eksponensial f(t) = 3^(t-1999). Untuk tahun 2001, f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6.561.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola eksponensial dari data yang diberikan dan menerapkan rumus fungsi tersebut untuk memprediksi nilai pada tahun tertentu. Ini adalah penerapan konsep fungsi eksponensial pada situasi rutin.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial; tahun 2001 = 3^2 = 9, 2002 = 3^3 = 27, 2003 = 3^4 = 81
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep fungsi eksponensial dan bagaimana memodelkan pertumbuhan data ke dalam bentuk fungsi tersebut.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus menentukan basis dan eksponen yang tepat berdasarkan data yang diberikan (menemukan pola f(t) = 3^(t-1999)) sebelum melakukan perhitungan, bukan sekadar substitusi langsung tanpa analisis pola.. Bukti: tahun 2001 = 3^2 = 9, 2002 = 3^3 = 27, 2003 = 3^4 = 81; berapa penjualan laptop pada tahun 2007?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan pola bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu mengenali pola pertumbuhan eksponensial dari data diskrit dan mengekstrapolasinya. |

Run 3 — solusi: Pola penjualan adalah f(t) = 3^(t-1999). Untuk tahun 2001 (t=2001), f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6.561.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan dan menerapkan model tersebut untuk memprediksi nilai pada tahun tertentu.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang fungsi eksponensial dan kemampuan prosedural dalam memodelkan data ke dalam bentuk fungsi.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus menentukan basis dan eksponen yang tepat dari pola yang diberikan (bukan sekadar substitusi langsung) dan melakukan ekstrapolasi ke tahun 2007.. Bukti: 2001 mampu menjual 9 laptop; 2002 dan 2003 mampu menjual masing-masing 27 dan 81 laptop; berapa penjualan laptop pada tahun 2007

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan pola bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu mengenali pola pertumbuhan eksponensial sederhana dan melakukan perhitungan pangkat. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Berdasarkan data, pada tahun 2001 perusahaan A mampu menjual 9 laptop. Pada tahun 2002 dan 2003 perusahaan A mampu menjual masing-masing 27 dan 81 laptop. Apabila relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial, berapa penjualan laptop pada tahun 2007?
Pilihan: A. 6.561 laptop (3^8)
B. 2.187 (3^7)
C. 486 (9, 27, 81, ... ditambah 81 tiap tahun sampai 2007)
D. 19.683 (3^9)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `84e4a0b4e7fdc64998b248b3`

Satuan energi adalah Joule dan kalori dengan 1 J = 2,4 kal. Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, merupakan fungsi karena setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori |
| B | Tidak, karena rumus 1 J = 2,4 kal hanya berlaku untuk bilangan bulat |
| C | Tidak, karena satu nilai Joule dapat menghasilkan lebih dari satu nilai kalori |
| D | Ya, tetapi hanya berlaku jika satuannya diubah ke kalori terlebih dahulu |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Hubungan antara Joule (J) dan kalori (kal) dinyatakan dengan persamaan linear k = 2,4J. Untuk setiap nilai J (input), terdapat tepat satu nilai k (output) yang dihasilkan. Karena setiap elemen di domain (Joule) dipetakan ke tepat satu elemen di kodomain (kalori), maka relasi ini memenuhi definisi fungsi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cbab1d0acc0a783dfd63e0bc5d706b394b855493152a61dd4fecf633b091d272`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1928 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1914 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1955 |

Run 1 — solusi: Hubungan antara Joule (J) dan kalori (kal) dinyatakan dengan persamaan linear k = 2,4J. Untuk setiap nilai J (input), terdapat tepat satu nilai k (output) yang dihasilkan. Karena setiap elemen di domain (Joule) dipetakan ke tepat satu elemen di kodomain (kalori), maka relasi ini memenuhi definisi fungsi.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi apakah sebuah relasi konversi satuan memenuhi definisi formal fungsi. Ini memerlukan pemahaman konseptual tentang syarat pemetaan satu-ke-satu (fungsi).. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?; setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau definisi fungsi (konsep) dan menerapkannya pada konteks konversi satuan.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman definisi dasar fungsi. Tidak ada langkah perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: 1 J = 2,4 kal; Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi (relasi yang memetakan setiap anggota domain ke tepat satu anggota kodomain). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 sudah mempelajari fungsi sejak kelas 10. Mengidentifikasi fungsi dari relasi linear sederhana adalah tugas rutin. |

Run 2 — solusi: Hubungan antara Joule (J) dan kalori (kal) dinyatakan dengan persamaan linear f(x) = 2,4x, di mana x adalah nilai dalam Joule. Karena setiap input x (Joule) menghasilkan tepat satu output f(x) (kalori), maka relasi ini memenuhi definisi fungsi.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi apakah relasi konversi satuan memenuhi definisi formal fungsi (setiap input memiliki tepat satu output). Ini memerlukan pemahaman konseptual tentang definisi fungsi.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar atau definisi fungsi (konsep) untuk menentukan apakah relasi konversi satuan linear memenuhi kriteria tersebut.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural-konseptual yang sangat mendasar bagi siswa kelas 11. Tidak ada langkah perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: 1 J = 2,4 kal; Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar fungsi (relasi satu-ke-satu atau banyak-ke-satu). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi adalah topik awal kelas 11. Soal ini menguji pemahaman definisi fungsi melalui contoh konversi satuan yang sangat sederhana. |

Run 3 — solusi: Hubungan antara Joule (J) dan kalori (kal) dinyatakan dengan persamaan linear k = 2,4J. Untuk setiap nilai input J, terdapat tepat satu nilai output k yang unik. Karena setiap elemen di domain (Joule) dipetakan ke tepat satu elemen di kodomain (kalori), maka relasi ini memenuhi definisi fungsi.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi apakah suatu relasi konversi satuan memenuhi definisi formal fungsi. Ini memerlukan pemahaman konseptual tentang definisi fungsi (pemetaan satu-ke-satu atau banyak-ke-satu) dan menerapkannya pada konteks linear sederhana.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?; setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau definisi fungsi (konseptual) dan menerapkannya pada relasi linear yang diberikan.. Bukti: 1 J = 2,4 kal; setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dasar mengenai definisi fungsi. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: 1 J = 2,4 kal; Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar fungsi (domain, kodomain, dan aturan pemetaan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi merupakan dasar kelas 11. Soal ini menguji pemahaman definisi fungsi secara langsung tanpa komplikasi teknis, sehingga dikategorikan mudah. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Satuan energi adalah Joule dan kalori dengan 1 J = 2,4 kal. Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.
Pilihan: A. Ya, merupakan fungsi karena setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori
B. Tidak, karena rumus 1 J = 2,4 kal hanya berlaku untuk bilangan bulat
C. Tidak, karena satu nilai Joule dapat menghasilkan lebih dari satu nilai kalori
D. Ya, tetapi hanya berlaku jika satuannya diubah ke kalori terlebih dahulu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `f772da841c280f238b1bbb15`

Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3).

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 7 |
| C | 6 |
| D | 42 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: (f o g)(3) = f(g(3)). Diketahui g(3) = 6, maka f(g(3)) = f(6). Diketahui f(6) = 13. Jadi, (f o g)(3) = 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7cd201d9709f4fa0f023270d3c10591802b16f820840aec8a4bbcca08c95ed24`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2067 |
| 2 | success | valid / verified | applying | procedural | Easy | 2085 |
| 3 | success | valid / verified | applying | procedural | Easy | 2039 |

Run 1 — solusi: (f o g)(3) = f(g(3)). Diketahui g(3) = 6, maka f(g(3)) = f(6). Diketahui f(6) = 13. Jadi, (f o g)(3) = 13.
- Domain kognitif `classify/applying`: Soal meminta penerapan definisi komposisi fungsi f(g(x)) dengan nilai-nilai yang sudah diberikan secara eksplisit. Siswa hanya perlu melakukan substitusi berjenjang (dua langkah rutin).. Bukti: tentukan (f o g) (3)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana mengoperasikan komposisi fungsi menggunakan nilai-nilai yang diketahui.. Bukti: f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan prosedur yang familiar bagi siswa kelas 11. Tidak ada manipulasi aljabar yang kompleks atau konsep abstrak yang mendalam.. Bukti: f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi komposisi fungsi (f o g)(x) = f(g(x)) dan kemampuan membaca nilai fungsi dari data yang diberikan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi komposisi fungsi adalah topik dasar kelas 11. Soal ini hanya menguji pemahaman definisi dasar tanpa variasi atau tingkat kesulitan tambahan. |

Run 2 — solusi: (f o g)(3) = f(g(3)). Diketahui g(3) = 6, maka f(g(3)) = f(6). Diketahui f(6) = 13. Jadi, (f o g)(3) = 13.
- Domain kognitif `classify/applying`: Soal meminta penerapan definisi komposisi fungsi f(g(x)) secara langsung dengan nilai yang sudah diberikan. Siswa hanya perlu memahami notasi komposisi dan melakukan substitusi dua langkah sederhana.. Bukti: tentukan (f o g) (3); f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau prosedur komposisi fungsi, yaitu memasukkan output fungsi pertama sebagai input fungsi kedua.. Bukti: (f o g) (3)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung (straightforward). Siswa hanya perlu menerapkan definisi komposisi fungsi f(g(3)) = f(6) = 13. Tidak ada manipulasi aljabar yang kompleks atau variabel yang tidak diketahui.. Bukti: f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12; tentukan (f o g) (3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi komposisi fungsi f(g(x)) = f(g(x)). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi komposisi fungsi adalah standar kelas 11. Soal ini menguji pemahaman dasar definisi tanpa kerumitan tambahan, sehingga tergolong mudah. |

Run 3 — solusi: (f o g)(3) = f(g(3)). Diketahui g(3) = 6, maka f(g(3)) = f(6). Diketahui f(6) = 13. Jadi, (f o g)(3) = 13.
- Domain kognitif `classify/applying`: Soal meminta penerapan definisi komposisi fungsi f(g(x)) secara langsung menggunakan nilai-nilai yang sudah diberikan. Siswa hanya perlu melakukan substitusi berjenjang.. Bukti: tentukan (f o g) (3); f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana mengoperasikan komposisi fungsi dengan substitusi nilai.. Bukti: (f o g) (3)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami notasi komposisi dan melakukan dua langkah substitusi sederhana tanpa manipulasi aljabar yang kompleks.. Bukti: f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12; tentukan (f o g) (3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi fungsi dan komposisi fungsi dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi komposisi fungsi adalah dasar kelas 11. Soal ini tidak memerlukan manipulasi variabel, hanya evaluasi nilai, sehingga tergolong mudah. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Komposisi Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3).
Pilihan: A. 13
B. 7
C. 6
D. 42
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `f69622cd0a44a030d0eca055`

Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan<br><br>f (3) × g(3)

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 42 |
| C | 1 |
| D | 78 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `42`.
Solusi minimum hasil AI: Diketahui f(3) = 7 dan g(3) = 6. Maka f(3) × g(3) = 7 × 6 = 42.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fd6c0025bf73e34af53346a204e1498b28f9d6fc70353d7892b52b89208502e7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2025 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2024 |
| 3 | success | valid / verified | knowing | factual | Easy | 2724 |

Run 1 — solusi: f(3) = 7 dan g(3) = 6. Maka f(3) * g(3) = 7 * 6 = 42.
- Domain kognitif `classify/knowing`: Soal hanya meminta operasi perkalian sederhana dari nilai fungsi yang sudah diberikan secara eksplisit. Siswa hanya perlu mengenali nilai yang relevan dan melakukan operasi aritmatika dasar.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang notasi fungsi dan operasi aritmatika dasar pada nilai fungsi tersebut.. Bukti: f (3) = 7, g (3) = 6; f (3) × g(3)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan substitusi nilai yang sudah diketahui ke dalam operasi perkalian dasar tanpa langkah tambahan atau manipulasi aljabar.. Bukti: f (3) = 7, g (3) = 6; f (3) × g(3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi fungsi f(x) dan operasi perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini terlalu mendasar karena tidak melibatkan konsep komposisi fungsi yang sebenarnya, melainkan hanya operasi aritmatika pada nilai fungsi. |

Run 2 — solusi: f(3) = 7 dan g(3) = 6. Maka f(3) × g(3) = 7 × 6 = 42.
- Domain kognitif `classify/knowing`: Soal hanya meminta siswa untuk melakukan operasi perkalian sederhana berdasarkan nilai fungsi yang sudah diberikan secara eksplisit. Tidak ada proses komposisi fungsi yang sebenarnya terjadi, hanya substitusi nilai.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami notasi fungsi dan melakukan operasi aritmatika dasar (perkalian) pada nilai yang diberikan.. Bukti: f (3) = 7, g (3) = 6; f (3) × g(3)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung (direct). Siswa hanya perlu mengambil nilai yang sudah tersedia dan mengalikannya. Tidak ada langkah tambahan atau manipulasi aljabar.. Bukti: f (3) = 7, g (3) = 6; f (3) × g(3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar notasi fungsi f(x) dan operasi perkalian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini terlalu sederhana karena hanya melibatkan substitusi langsung tanpa konsep komposisi fungsi yang sebenarnya. |

Run 3 — solusi: Diketahui f(3) = 7 dan g(3) = 6. Maka f(3) × g(3) = 7 × 6 = 42.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi perkalian sederhana berdasarkan nilai fungsi yang sudah diberikan secara eksplisit.. Bukti: f(3) = 7, g(3) = 6; tentukan f(3) × g(3)
- Dimensi pengetahuan `classify/factual`: Melibatkan pemahaman dasar tentang notasi fungsi dan operasi aritmatika.. Bukti: f(3) = 7, g(3) = 6; f(3) × g(3)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan substitusi nilai yang diketahui ke dalam operasi perkalian dasar tanpa langkah tambahan.. Bukti: f(3) = 7, g(3) = 6; tentukan f(3) × g(3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi fungsi f(x) dan operasi perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini terlalu mendasar karena tidak melibatkan konsep komposisi fungsi yang sebenarnya, hanya evaluasi fungsi sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3505`.
Konten: `valid`; kunci: `verified`; masalah: Soal dikategorikan sebagai subtopik Komposisi Fungsi, namun soal ini sama sekali tidak melibatkan komposisi fungsi (f(g(x)) atau g(f(x))). Soal ini hanya menguji operasi aritmatika dasar pada nilai fungsi yang sudah diberikan secara eksplisit.; Tingkat kesulitan soal ini sangat rendah untuk jenjang kelas 11, karena hanya memerlukan substitusi nilai dan perkalian dasar..
- Domain kognitif `knowing`: Soal hanya meminta operasi perkalian sederhana dari nilai fungsi yang sudah diberikan secara eksplisit. Siswa hanya perlu mengenali nilai yang relevan dan melakukan operasi aritmatika dasar.
- Dimensi pengetahuan `factual`: Soal menguji pemahaman tentang notasi fungsi dan operasi aritmatika dasar pada nilai fungsi tersebut.
- Intended difficulty `Easy`: Soal ini sangat langsung, hanya memerlukan substitusi nilai yang sudah diketahui ke dalam operasi perkalian dasar tanpa langkah tambahan atau manipulasi aljabar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi fungsi f(x) dan operasi perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini terlalu mendasar karena tidak melibatkan konsep komposisi fungsi yang sebenarnya, melainkan hanya operasi aritmatika pada nilai fungsi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Komposisi Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan

f (3) × g(3)
Pilihan: A. 13
B. 42
C. 1
D. 78
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: Soal dikategorikan sebagai subtopik Komposisi Fungsi, namun soal ini sama sekali tidak melibatkan komposisi fungsi (f(g(x)) atau g(f(x))). Soal ini hanya menguji operasi aritmatika dasar pada nilai fungsi yang sudah diberikan secara eksplisit.; Tingkat kesulitan soal ini sangat rendah untuk jenjang kelas 11, karena hanya memerlukan substitusi nilai dan perkalian dasar..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `f2de3a4198c1c8c13c51a92a`

Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).

| Opsi | Isi |
|---|---|
| A | b = 3, f^-1(x) = (x - 3)/2 |
| B | b = 6, f^-1(x) = (x - 6)/2 |
| C | b = 2, f^-1(x) = (x + 2)/2 |
| D | b = 2, f^-1(x) = (x - 2)/2 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `b = 2, f^-1(x) = (x - 2)/2`.
Solusi minimum hasil AI: f(f(x)) = 2(2x+b)+b = 4x+3b. Diketahui f(f(x)) = 4x+6, maka 3b = 6, sehingga b = 2. Fungsi menjadi f(x) = 2x+2. Untuk invers, y = 2x+2 => 2x = y-2 => x = (y-2)/2. Jadi, f^-1(x) = (x-2)/2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0e67ec23a0ab263ec37f88402cfcf7b2566e443bc750f475b20adb46fa6e05ea`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2913 |
| 2 | success | valid / verified | applying | procedural | Easy | 2229 |
| 3 | success | valid / verified | applying | procedural | Medium | 2290 |

Run 1 — solusi: f(f(x)) = 2(2x+b)+b = 4x+3b. Diketahui 4x+3b = 4x+6, maka 3b=6 sehingga b=2. Fungsi menjadi f(x)=2x+2. Invers: y=2x+2, maka 2x=y-2, sehingga f^-1(x)=(x-2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur komposisi fungsi untuk mencari parameter b, kemudian menerapkan prosedur invers fungsi linear. Ini adalah penerapan konsep rutin.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6; Tentukan nilai b dan f-1 (x)
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma aljabar standar untuk komposisi dan invers fungsi.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah rutin yang saling terkait: menentukan parameter b melalui komposisi dan mencari invers. Beban kognitif rendah.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aljabar dasar, komposisi fungsi, dan invers fungsi linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin untuk kelas 11 terkait fungsi komposisi dan invers. Tidak ada strategi nonrutin yang diperlukan. |

Run 2 — solusi: f(f(x)) = 2(2x+b)+b = 4x+3b. Diketahui 4x+3b = 4x+6, maka 3b=6, sehingga b=2. Maka f(x)=2x+2. Untuk mencari invers, y=2x+2, maka 2x=y-2, sehingga f^-1(x)=(x-2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep komposisi fungsi f(f(x)) dan melakukan manipulasi aljabar untuk menentukan nilai konstanta b, kemudian menentukan invers fungsi linear. Ini adalah prosedur rutin yang memerlukan pemilihan langkah yang tepat.. Bukti: f(f(x)) = 2(2x+b)+b = 4x+3b; 4x+3b = 4x+6; f^-1(x)=(x-2)/2
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma komposisi fungsi dan teknik mencari invers fungsi linear.. Bukti: f(f(x)) = 2(2x+b)+b; f^-1(x)=(x-2)/2
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 11. Langkah-langkahnya rutin (substitusi komposisi, penyelesaian persamaan linear, dan invers fungsi) dengan beban kognitif rendah.. Bukti: f(f(x)) = 4x + 6; Tentukan nilai b dan f-1 (x)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep fungsi linear, komposisi fungsi, dan invers fungsi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi komposisi dan invers fungsi adalah kurikulum standar kelas 11. Soal ini tidak memerlukan strategi non-rutin atau integrasi konsep yang kompleks. |

Run 3 — solusi: f(f(x)) = 2(2x+b)+b = 4x+3b. Diketahui f(f(x)) = 4x+6, maka 3b = 6, sehingga b = 2. Fungsi menjadi f(x) = 2x+2. Untuk invers, y = 2x+2 => 2x = y-2 => x = (y-2)/2. Jadi, f^-1(x) = (x-2)/2.
- Domain kognitif `classify/applying`: Siswa perlu melakukan komposisi fungsi f(f(x)) dan menyamakan koefisien/konstanta untuk menemukan nilai b, kemudian menentukan invers fungsi linear. Ini adalah prosedur rutin yang memerlukan pemahaman konsep komposisi dan invers.. Bukti: f(f(x)) = 2(2x+b)+b = 4x+3b; disamakan dengan 4x+6 diperoleh 3b=6
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma komposisi fungsi dan teknik aljabar untuk mencari invers fungsi linear.. Bukti: f(f(x)) = 2(2x+b)+b = 4x+3b; f^-1(x)=(x-2)/2
- Intended difficulty `classify/Medium`: Soal ini melibatkan langkah-langkah rutin: komposisi fungsi, penyelesaian persamaan linear sederhana, dan penentuan invers. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar fungsi linear, komposisi fungsi, dan invers fungsi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi komposisi dan invers adalah standar kelas 11. Prosedur substitusi dan aljabar yang diminta bersifat rutin bagi siswa pada jenjang ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3939`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur komposisi fungsi untuk mencari parameter b, kemudian menerapkan prosedur invers fungsi linear. Ini adalah penerapan konsep rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritma aljabar standar untuk komposisi dan invers fungsi.
- Intended difficulty `Medium`: Soal memerlukan dua langkah rutin yang saling terkait: menentukan parameter b melalui komposisi dan mencari invers. Beban kognitif rendah dan prosedurnya familiar bagi siswa kelas 11.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aljabar dasar, komposisi fungsi, dan invers fungsi linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin untuk kelas 11 terkait fungsi komposisi dan invers. Tidak ada strategi nonrutin yang diperlukan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi Invers
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).
Pilihan: A. b = 3, f^-1(x) = (x - 3)/2
B. b = 6, f^-1(x) = (x - 6)/2
C. b = 2, f^-1(x) = (x + 2)/2
D. b = 2, f^-1(x) = (x - 2)/2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `7b396c45f8b99915cc10dc7b`

Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

| Opsi | Isi |
|---|---|
| A | f^-1(x) = x^2 - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |
| B | f^-1(x) = x^2 + 3, domain: semua bilangan riil, range: semua bilangan riil |
| C | f^-1(x) = x^2 + 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |
| D | f^-1(x) = akar(x) - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: y = sqrt(x - 3) => y^2 = x - 3 => x = y^2 + 3. Tukar variabel: f^-1(x) = x^2 + 3. Domain f(x) adalah x >= 3, maka range f^-1(x) adalah y >= 3. Range f(x) adalah y >= 0, maka domain f^-1(x) adalah x >= 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01117b082a4e9fb4b6eedf173f77fa5ba542c0ac83c79fed2c0703170ff1ac1c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2190 |
| 2 | success | valid / verified | applying | procedural | Medium | 2186 |
| 3 | success | valid / verified | applying | procedural | Medium | 2265 |

Run 1 — solusi: y = sqrt(x - 3) => y^2 = x - 3 => x = y^2 + 3. Tukar variabel: f^-1(x) = x^2 + 3. Domain f(x) adalah x >= 3, maka range f^-1(x) adalah y >= 3. Range f(x) adalah y >= 0, maka domain f^-1(x) adalah x >= 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep invers fungsi, melakukan manipulasi aljabar untuk mencari invers, serta menentukan domain dan range invers berdasarkan range dan domain fungsi asal.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural dalam mencari invers fungsi dan pemahaman konseptual mengenai hubungan domain dan range antara fungsi dan inversnya.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3)
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang pembatasan domain dan range pada fungsi akar kuadrat saat mencari inversnya, yang merupakan langkah rutin namun krusial bagi siswa kelas 11.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep fungsi, domain, range, dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menentukan invers fungsi sederhana dan memahami batasan domain/range yang muncul dari fungsi akar. |

Run 2 — solusi: y = sqrt(x - 3) => y^2 = x - 3 => x = y^2 + 3. Tukar variabel: f^-1(x) = x^2 + 3. Domain f^-1 adalah range f (y >= 0), range f^-1 adalah domain f (x >= 3). Jadi, f^-1(x) = x^2 + 3, domain x >= 0, range y >= 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aljabar untuk mencari invers dan memahami konsep bahwa domain invers adalah range fungsi asal dan sebaliknya.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman prosedural dalam memanipulasi aljabar dan pemahaman konseptual mengenai batasan domain dan range pada fungsi invers.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang pembatasan domain dan range yang sering terlewatkan, namun prosedurnya standar untuk kelas 11.. Bukti: f (x) = akar(x - 3); domain dan range-nya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi akar, aljabar invers, dan konsep domain/range. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menentukan invers fungsi irasional dan memperhatikan batasan domain/range yang muncul akibat sifat fungsi tersebut. |

Run 3 — solusi: f(x) = sqrt(x-3) memiliki domain x >= 3 dan range y >= 0. Untuk mencari invers, y = sqrt(x-3) -> y^2 = x-3 -> x = y^2 + 3. Menukar variabel, f^-1(x) = x^2 + 3. Domain f^-1 adalah range f (x >= 0), dan range f^-1 adalah domain f (y >= 3).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep invers fungsi, melakukan manipulasi aljabar untuk mencari invers, serta menentukan domain dan range invers berdasarkan sifat fungsi asalnya. Ini adalah prosedur standar dalam materi fungsi invers kelas 11.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang langkah-langkah mencari invers fungsi dan pemahaman konseptual tentang bagaimana domain dan range fungsi asal bertukar peran menjadi range dan domain fungsi invers.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang pembatasan domain dan range pada fungsi akar, yang merupakan langkah rutin namun krusial dalam materi fungsi invers kelas 11. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman fungsi akar, aljabar dasar, dan konsep dasar invers fungsi (domain/range). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini menguji pemahaman mendasar tentang invers fungsi akar yang merupakan materi standar kelas 11. Kesulitan 'Medium' diberikan karena siswa sering terjebak pada penentuan domain/range invers, bukan sekadar manipulasi aljabar. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi Invers
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
Pilihan: A. f^-1(x) = x^2 - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3
B. f^-1(x) = x^2 + 3, domain: semua bilangan riil, range: semua bilangan riil
C. f^-1(x) = x^2 + 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3
D. f^-1(x) = akar(x) - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d590344d18abe3ebd38fb8ed`

Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.<br><br>\|Waktu (Detik)\|0\|1\|2\|3\|4\|5\|6\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Jarak (m)\|0\|5\|8\|9\|8\|5\|0\|<br><br>Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.

| Opsi | Isi |
|---|---|
| A | Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi. |
| B | Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi. |
| C | Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi. |
| D | Tidak dapat ditentukan tanpa menggambar grafiknya. |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Data menunjukkan nilai jarak meningkat dari 0 (t=0) ke 9 (t=3) lalu menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak (maksimum), yang hanya terjadi pada fungsi kuadrat dengan koefisien a < 0 (terbuka ke bawah).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `011adaa34610e2de574587c527c57e5afeb7e952f0a2b53b147fa94a6153c589`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2205 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2215 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2228 |

Run 1 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) ke 9 (t=3) lalu menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak (maksimum), yang hanya terjadi pada fungsi kuadrat dengan koefisien a < 0 (terbuka ke bawah).
- Domain kognitif `classify/applying`: Soal meminta siswa menginterpretasikan pola numerik dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan). Ini memerlukan pemahaman konseptual tentang hubungan antara titik puncak dan koefisien fungsi kuadrat, bukan sekadar menghitung.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Siswa harus menghubungkan pola data (naik-turun) dengan struktur konseptual fungsi kuadrat (parabola dengan titik maksimum).. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural namun memerlukan pemahaman konseptual tentang perilaku fungsi kuadrat. Siswa tidak perlu melakukan perhitungan rumit, hanya mengenali pola simetris dan titik balik.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum fungsi kuadrat dan hubungan antara koefisien a dengan arah bukaan parabola. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengenali sifat fungsi kuadrat dari tabel data adalah keterampilan dasar yang diharapkan setelah mempelajari fungsi kuadrat di kelas 10. |

Run 2 — solusi: Data menunjukkan titik puncak (3,9) dengan nilai jarak yang simetris di sekitar t=3 (f(2)=f(4)=8, f(1)=f(5)=5, f(0)=f(6)=0). Karena nilai fungsi meningkat hingga mencapai maksimum (9) lalu menurun, grafik parabola harus terbuka ke bawah (koefisien a < 0).
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan pola perubahan nilai dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan parabola) tanpa bantuan visual grafik. Ini melibatkan pemahaman konseptual tentang hubungan antara nilai maksimum/minimum dengan arah bukaan parabola.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat fungsi kuadrat (parabola) dan bagaimana pola data numerik mencerminkan karakteristik fungsi tersebut.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena hanya memerlukan pengamatan pola sederhana (naik lalu turun) yang merupakan karakteristik dasar fungsi kuadrat dengan a < 0. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan hubungan antara nilai fungsi dengan arah bukaan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi arah bukaan parabola dari tabel data adalah prosedur rutin yang sangat mendasar. |

Run 3 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) ke 9 (t=3) lalu menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak (maksimum), yang secara matematis berarti koefisien a pada fungsi kuadrat f(t)=at^2+bt+c harus negatif. Oleh karena itu, grafik terbuka ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan pola data numerik dan menghubungkannya dengan sifat geometris fungsi kuadrat (arah bukaan parabola) tanpa harus menggambar grafik. Ini memerlukan pemahaman konseptual tentang hubungan antara titik puncak dan koefisien fungsi kuadrat.. Bukti: pola naik-lalu-turun ini khas parabola dengan koefisien a negatif, yaitu terbuka ke bawah
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang sifat-sifat fungsi kuadrat (arah bukaan) berdasarkan pola perubahan nilai, bukan sekadar prosedur menghitung nilai fungsi.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengenali pola naik-turun sederhana pada tabel untuk menentukan arah bukaan parabola. Tidak ada perhitungan kompleks atau manipulasi aljabar yang diperlukan.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum fungsi kuadrat dan hubungan antara koefisien a dengan arah bukaan parabola. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, mengidentifikasi arah bukaan parabola dari pola data tabel adalah tugas rutin yang sangat mendasar dalam materi fungsi kuadrat. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.

|Waktu (Detik)|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|Jarak (m)|0|5|8|9|8|5|0|

Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.
Pilihan: A. Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi.
B. Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi.
C. Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi.
D. Tidak dapat ditentukan tanpa menggambar grafiknya.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 x 12 = 144 |
| B | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| C | 12 |
| D | 12! = 479.001.600 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n=12, maka 12! = 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad1c706b06b5f9313d12e061c0d437a7c916d119fead7b81db0ba0c03af4347d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2202 |
| 2 | success | valid / verified | applying | procedural | Easy | 2310 |
| 3 | success | valid / verified | applying | procedural | Easy | 2218 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n=12, maka 12! = 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal meminta penerapan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga yang memiliki jumlah anggota sama. Siswa hanya perlu mengingat atau menerapkan prinsip dasar perhitungan (permutasi) untuk n objek.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang rumus faktorial dalam konteks korespondensi satu-satu.. Bukti: banyak korespondensi satu-satu yang mungkin adalah n! = 12! = 479.001.600
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Siswa hanya perlu menerapkan rumus n! secara langsung tanpa modifikasi strategi atau analisis kompleks.. Bukti: n(A) = n(B) = 12

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
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah materi standar kelas 11. Soal ini adalah penerapan langsung rumus tanpa variasi. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan kardinalitas yang sama. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang aturan perhitungan korespondensi satu-satu (bijeksi) pada himpunan berhingga.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari materi korespondensi satu-satu. Prosedurnya langsung (n!) tanpa memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan, kardinalitas himpunan, dan konsep faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah bagian standar kurikulum SMA kelas 11. Soal ini menguji ingatan prosedural dasar tanpa variasi yang menantang. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan dengan n anggota adalah n!. Untuk n = 12, maka 12! = 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal meminta penerapan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan dengan jumlah anggota yang sama.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prinsip dasar perhitungan (faktorial) untuk korespondensi satu-satu, yang merupakan konsep prosedural dalam kombinatorika.. Bukti: banyak korespondensi satu-satu yang mungkin adalah n! = 12! = 479.001.600
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena langsung menanyakan penerapan rumus faktorial untuk korespondensi satu-satu. Tidak ada langkah kompleks atau strategi non-rutin yang diperlukan.. Bukti: n(A) = n(B) = 12

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
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah materi standar kelas 11. Soal ini menguji ingatan akan rumus dasar tanpa modifikasi. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Korespondensi Satu-satu (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12

Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
Pilihan: A. 12 x 12 = 144
B. 12 + 11 + 10 + ... + 2 + 1 = 78
C. 12
D. 12! = 479.001.600
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `280f78ecf94b2c1b0d7d8f4a`

AB adalah diameter pada lingkaran berikut. Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm. Tentukan:<br><br>panjang BC

| Opsi | Isi |
|---|---|
| A | 9 cm |
| B | 18,8 cm |
| C | 17 cm |
| D | 15 cm |

![Gambar sumber soal 9](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0074-05.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: AB = 2 * r = 2 * 8,5 = 17 cm. Karena AB adalah diameter, maka ∠ACB = 90° (Teorema Thales). Dengan teorema Pythagoras pada ΔABC: BC = √(AB² - AC²) = √(17² - 8²) = √(289 - 64) = √225 = 15 cm.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0074-05.png. Transkripsi visual: Lingkaran dengan titik pusat di tengah diameter AB. Titik C berada pada keliling lingkaran. Segmen garis AB adalah diameter (berwarna biru). Segmen garis AC dan BC membentuk segitiga ABC (berwarna hijau).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `360e79c7fca1a88f085e2464ac669f5a8d2e5c9999eb4cc7a46f3fe5cff412cd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3309 |
| 2 | success | valid / verified | applying | procedural | Easy | 3367 |
| 3 | success | valid / verified | applying | procedural | Easy | 3325 |

Run 1 — solusi: AB adalah diameter, maka AB = 2 * r = 2 * 8,5 = 17 cm. Menurut Teorema Thales, sudut ACB = 90 derajat. Dengan teorema Pythagoras pada segitiga siku-siku ABC: BC = akar(AB^2 - AC^2) = akar(17^2 - 8^2) = akar(289 - 64) = akar(225) = 15 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengenali sifat diameter lingkaran (Teorema Thales) untuk menyimpulkan bahwa segitiga ABC adalah segitiga siku-siku, kemudian menerapkan teorema Pythagoras. Ini adalah prosedur rutin yang menghubungkan konsep geometri lingkaran dengan trigonometri/geometri dasar.. Bukti: AB adalah diameter pada lingkaran berikut.; Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm.; Tentukan: panjang BC
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara diameter dan sudut keliling (Teorema Thales) serta penerapan prosedural teorema Pythagoras.. Bukti: AB adalah diameter; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena menggunakan prosedur standar yang familiar bagi siswa kelas 11 (Teorema Pythagoras dan sifat diameter lingkaran). Tidak ada strategi non-rutin atau integrasi kompleks yang diperlukan.. Bukti: AB adalah diameter; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, sifat diameter lingkaran (sudut keliling yang menghadap diameter adalah 90 derajat). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan Pythagoras adalah dasar yang sudah dikuasai sebelum kelas 11, sehingga soal ini tergolong mudah untuk tingkat kelas 11. |

Run 2 — solusi: AB adalah diameter, maka AB = 2 * r = 2 * 8,5 = 17 cm. Sudut ACB adalah sudut keliling yang menghadap diameter, sehingga ∠ACB = 90° (Teorema Thales). Dengan teorema Pythagoras pada ΔABC: BC = √(AB² - AC²) = √(17² - 8²) = √(289 - 64) = √225 = 15 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat sudut keliling yang menghadap diameter (Teorema Thales) untuk membentuk segitiga siku-siku, kemudian menerapkan teorema Pythagoras. Ini adalah proses penerapan konsep geometri yang rutin.. Bukti: AB adalah diameter pada lingkaran berikut. Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm.; karena AB diameter, ∠ACB = 90° (Teorema Thales), sehingga BC = akar(AB² - AC²) = akar(17² - 8²) = akar(225) = 15 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan geometris (konseptual) dan penggunaan algoritma Pythagoras (prosedural) untuk menyelesaikan masalah.. Bukti: karena AB diameter, ∠ACB = 90° (Teorema Thales); BC = akar(AB² - AC²) = akar(17² - 8²) = akar(225) = 15 cm
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah-langkahnya jelas: menghitung diameter, mengenali sifat sudut siku-siku pada diameter, dan menghitung panjang sisi segitiga.. Bukti: Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm; AB adalah diameter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat sudut keliling lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan Pythagoras adalah materi dasar yang sudah dikuasai sebelum kelas 11. Prosedur penyelesaiannya langsung dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: AB = 2 * r = 2 * 8,5 = 17 cm. Karena AB adalah diameter, maka ∠ACB = 90° (Teorema Thales). Dengan teorema Pythagoras pada ΔABC: BC = √(AB² - AC²) = √(17² - 8²) = √(289 - 64) = √225 = 15 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat geometris lingkaran (diameter membentuk sudut siku-siku pada keliling) dan menerapkan teorema Pythagoras untuk mencari panjang sisi segitiga. Ini adalah penerapan konsep rutin pada situasi geometri.. Bukti: AB adalah diameter pada lingkaran berikut. Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm.; karena AB diameter, ∠ACB = 90° (Teorema Thales), sehingga BC = akar(AB² - AC²)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara diameter lingkaran dan sudut keliling (konseptual) serta penggunaan algoritma teorema Pythagoras (prosedural).. Bukti: karena AB diameter, ∠ACB = 90° (Teorema Thales); BC = akar(AB² - AC²)
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena melibatkan prosedur standar yang familiar bagi siswa kelas 11: menghitung diameter dari jari-jari, mengenali sifat sudut keliling yang menghadap diameter, dan menerapkan teorema Pythagoras.. Bukti: Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm; AB adalah diameter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi diameter, hubungan jari-jari dan diameter, teorema Pythagoras, sifat sudut keliling yang menghadap diameter. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan teorema Pythagoras adalah materi dasar yang sudah dikuasai sebelum kelas 11, namun tetap relevan sebagai prasyarat geometri di kelas 11. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5103`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi sifat geometris bahwa sudut keliling yang menghadap diameter adalah sudut siku-siku (Teorema Thales), kemudian menerapkan teorema Pythagoras untuk menghitung panjang sisi segitiga. Ini adalah penerapan prosedur rutin pada konteks geometri.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman konseptual tentang hubungan antara diameter dan sudut keliling, serta penggunaan algoritma teorema Pythagoras (prosedural) untuk menyelesaikan masalah.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena melibatkan prosedur standar yang familiar bagi siswa kelas 11: menghitung diameter dari jari-jari, mengenali sifat sudut keliling yang menghadap diameter, dan menerapkan teorema Pythagoras.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi diameter, hubungan jari-jari dan diameter, teorema Pythagoras, sifat sudut keliling yang menghadap diameter. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan teorema Pythagoras adalah materi dasar yang sudah dikuasai sebelum kelas 11, namun tetap relevan sebagai prasyarat geometri di kelas 11. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Busur Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: AB adalah diameter pada lingkaran berikut. Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm. Tentukan:

panjang BC
Pilihan: A. 9 cm
B. 18,8 cm
C. 17 cm
D. 15 cm
Transkripsi visual: Lingkaran dengan titik pusat di tengah diameter AB. Titik C berada pada keliling lingkaran. Segmen garis AB adalah diameter (berwarna biru). Segmen garis AC dan BC membentuk segitiga ABC (berwarna hijau).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `f6239979bb0b323db2b28a03`

Jika `∠` BOC = 90`◦` , berapakah besar `∠` BEC ?

| Opsi | Isi |
|---|---|
| A | 22,5° |
| B | 45° |
| C | 90° |
| D | 180° |

![Gambar sumber soal 10](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0074-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Sudut pusat ∠BOC = 90°. Sudut keliling ∠BEC menghadap busur yang sama dengan sudut pusat ∠BOC. Berdasarkan teorema sudut pusat dan sudut keliling, ∠BEC = 1/2 × ∠BOC = 1/2 × 90° = 45°.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0074-01.png. Transkripsi visual: Lingkaran dengan pusat O. Titik B, C, dan E terletak pada keliling lingkaran. Terdapat sudut pusat ∠BOC yang ditandai dengan simbol siku-siku (90 derajat). Titik E berada pada busur mayor BC. Garis EB dan EC membentuk sudut keliling ∠BEC.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `575e9b469f5dd3f18689123846f0b4901c1c33bb83148805f7247c3f833848d6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3191 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3148 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3184 |

Run 1 — solusi: Sudut pusat ∠BOC = 90°. Sudut keliling ∠BEC menghadap busur yang sama dengan sudut pusat ∠BOC. Berdasarkan teorema sudut pusat dan sudut keliling, ∠BEC = 1/2 × ∠BOC = 1/2 × 90° = 45°.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan teorema dasar hubungan antara sudut pusat dan sudut keliling yang menghadap busur yang sama. Ini adalah prosedur standar dalam geometri lingkaran.. Bukti: ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau hubungan konseptual antara sudut pusat dan sudut keliling untuk menyelesaikan masalah ini.. Bukti: ∠BEC = 1/2 × ∠BOC
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu mengenali konfigurasi sudut pusat dan keliling, lalu menerapkan rumus dasar. Tidak ada langkah tambahan atau strategi non-rutin yang diperlukan.. Bukti: Jika ∠BOC = 90° , berapakah besar ∠BEC ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema sudut pusat dan sudut keliling lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri lingkaran (sudut pusat/keliling) adalah topik standar kelas 11. Soal ini menguji pemahaman dasar yang bersifat prosedural dan rutin. |

Run 2 — solusi: Sudut pusat ∠BOC = 90°. Sudut keliling ∠BEC menghadap busur yang sama dengan sudut pusat ∠BOC. Berdasarkan teorema sudut pusat dan sudut keliling, ∠BEC = 1/2 × ∠BOC = 1/2 × 90° = 45°.
- Domain kognitif `classify/applying`: Soal ini menguji pemahaman konsep dasar hubungan antara sudut pusat dan sudut keliling yang menghadap busur yang sama. Siswa hanya perlu menerapkan teorema tersebut secara langsung.. Bukti: ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Dimensi pengetahuan `classify/conceptual`: Soal ini memerlukan pemahaman prinsip geometris tentang hubungan sudut pusat dan sudut keliling pada lingkaran.. Bukti: ∠BEC = 1/2 × ∠BOC
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah penerapan teorema yang sangat familiar bagi siswa SMA.. Bukti: Jika ∠ BOC = 90◦ , berapakah besar ∠ BEC ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema hubungan sudut pusat dan sudut keliling lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah topik standar. Soal ini hanya memerlukan pengenalan konfigurasi sudut pusat-keliling yang merupakan prosedur rutin. |

Run 3 — solusi: Sudut pusat ∠BOC = 90°. Sudut keliling ∠BEC menghadap busur yang sama dengan sudut pusat ∠BOC. Berdasarkan teorema sudut pusat dan sudut keliling, ∠BEC = 1/2 × ∠BOC = 1/2 × 90° = 45°.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan teorema hubungan antara sudut pusat dan sudut keliling yang menghadap busur yang sama. Ini adalah prosedur standar dalam geometri lingkaran.. Bukti: ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau hubungan konseptual antara sudut pusat dan sudut keliling untuk menyelesaikan masalah ini.. Bukti: ∠BEC = 1/2 × ∠BOC
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan teorema dasar geometri lingkaran yang sudah familiar bagi siswa kelas 11. Tidak ada langkah tambahan atau strategi non-rutin yang diperlukan.. Bukti: ∠BOC = 90°; ∠BEC = 1/2 × ∠BOC

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang sudut pusat dan sudut keliling lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran merupakan topik standar SMA kelas 11. Soal ini menguji penerapan langsung teorema dasar tanpa kompleksitas tambahan. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Busur Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika `∠` BOC = 90`◦` , berapakah besar `∠` BEC ?
Pilihan: A. 22,5°
B. 45°
C. 90°
D. 180°
Transkripsi visual: Lingkaran dengan pusat O. Titik B, C, dan E terletak pada keliling lingkaran. Terdapat sudut pusat ∠BOC yang ditandai dengan simbol siku-siku (90 derajat). Titik E berada pada busur mayor BC. Garis EB dan EC membentuk sudut keliling ∠BEC.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `838b526b72b79e514bd4fe62`

Pada gambar berikut, BD dan CD adalah garis singgung lingkaran A. Jika `∠` BAC = 147`◦` , tentukan besar `∠` BDC.

| Opsi | Isi |
|---|---|
| A | 33° |
| B | 57° |
| C | 147° |
| D | 90° |

![Gambar sumber soal 11](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0081-05.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, maka ∠ABD = 90° dan ∠ACD = 90°. Segiempat ABDC memiliki jumlah sudut 360°. ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0081-05.png. Transkripsi visual: Lingkaran berpusat di A. Titik B dan C berada pada lingkaran. Garis BD dan CD adalah garis singgung lingkaran yang bertemu di titik D di luar lingkaran. Segiempat ABDC terbentuk dari titik pusat A, titik singgung B dan C, serta titik potong garis singgung D.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `81afd686d8070297c4a1c4507761417eb90ecf6cc9d94b026341dd7fd8294657`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3298 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3261 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3307 |

Run 1 — solusi: Garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, maka ∠ABD = 90° dan ∠ACD = 90°. Segiempat ABDC memiliki jumlah sudut 360°. ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat geometris garis singgung (tegak lurus jari-jari) dan jumlah sudut segiempat untuk menyelesaikan masalah. Ini adalah penerapan prosedur rutin pada situasi geometris yang standar.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara garis singgung, jari-jari, dan sifat sudut dalam segiempat (konsep geometris).. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang mempelajari geometri lingkaran. Prosedurnya langsung (menggunakan sifat sudut segiempat dan garis singgung) tanpa memerlukan strategi non-rutin.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat garis singgung lingkaran (tegak lurus jari-jari) dan jumlah sudut dalam segiempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri lingkaran dan garis singgung adalah topik standar SMA kelas 11. Prosedur penyelesaiannya bersifat langsung dan familiar. |

Run 2 — solusi: Segiempat ABDC memiliki jumlah sudut 360°. Karena BD dan CD adalah garis singgung, maka ∠ABD = 90° dan ∠ACD = 90°. Maka, ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat garis singgung lingkaran (tegak lurus dengan jari-jari) dan sifat jumlah sudut segiempat untuk menyelesaikan masalah. Ini adalah penerapan prosedur rutin.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠BAC = 147°; tentukan besar ∠BDC
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat geometris garis singgung lingkaran dan segiempat.. Bukti: BD dan CD adalah garis singgung lingkaran A; jumlah sudutnya 360°
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang mempelajari geometri lingkaran. Prosedurnya langsung dan tidak memerlukan strategi non-rutin.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠BAC = 147°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat garis singgung lingkaran (tegak lurus jari-jari) dan jumlah sudut segiempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik standar SMA kelas 11. Soal ini menggunakan prosedur standar yang familiar. |

Run 3 — solusi: Pada segiempat ABDC, sudut ABD = 90° dan sudut ACD = 90° karena garis singgung tegak lurus jari-jari. Jumlah sudut segiempat adalah 360°. Maka, ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat geometris garis singgung (tegak lurus jari-jari) dan jumlah sudut dalam segiempat untuk menyelesaikan masalah. Ini adalah penerapan prosedur rutin pada situasi geometris.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep garis singgung lingkaran dan sifat-sifat segiempat yang terbentuk dari titik pusat dan titik singgung.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ABD = ∠ACD = 90°
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang sudah mempelajari geometri lingkaran. Prosedur penyelesaiannya langsung menggunakan sifat dasar garis singgung dan jumlah sudut segiempat.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat garis singgung lingkaran (tegak lurus jari-jari) dan jumlah sudut dalam segiempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik standar SMA kelas 11. Soal ini tidak memerlukan strategi non-rutin atau pembuktian kompleks. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Garis Singgung
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada gambar berikut, BD dan CD adalah garis singgung lingkaran A. Jika `∠` BAC = 147`◦` , tentukan besar `∠` BDC.
Pilihan: A. 33°
B. 57°
C. 147°
D. 90°
Transkripsi visual: Lingkaran berpusat di A. Titik B dan C berada pada lingkaran. Garis BD dan CD adalah garis singgung lingkaran yang bertemu di titik D di luar lingkaran. Segiempat ABDC terbentuk dari titik pusat A, titik singgung B dan C, serta titik potong garis singgung D.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `a0be320297e2f3ecca60fa01`

Jika jari-jari lingkaran A adalah 7 cm dan titik P berjarak 25 cm dari titik A, berapakah panjang garis singgung PB ?

| Opsi | Isi |
|---|---|
| A | 18 cm |
| B | 25 cm |
| C | 24 cm |
| D | 26 cm |

![Gambar sumber soal 12](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0081-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Garis singgung PB tegak lurus dengan jari-jari AB di titik B, membentuk segitiga siku-siku ABP dengan hipotenusa AP. Diketahui AB = 7 cm (jari-jari) dan AP = 25 cm (jarak titik ke pusat). Berdasarkan teorema Pythagoras: PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0081-03.png. Transkripsi visual: Gambar menunjukkan sebuah lingkaran dengan pusat A. Titik B terletak pada keliling lingkaran. Garis AB adalah jari-jari lingkaran. Titik P berada di luar lingkaran. Garis biru melewati titik B dan P, yang merupakan garis singgung lingkaran di titik B. Garis hitam menghubungkan pusat A ke titik P. Segitiga ABP terbentuk dengan sudut siku-siku di B karena sifat garis singgung yang tegak lurus dengan jari-jari.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7b0b78247827e52f4e8251f397ca5b50c10ac177a2a461c91cb054d0a6ddd429`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3309 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3318 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3291 |

Run 1 — solusi: Garis singgung PB tegak lurus dengan jari-jari AB di titik B, membentuk segitiga siku-siku ABP dengan hipotenusa AP. Diketahui AB = 7 cm (jari-jari) dan AP = 25 cm (jarak titik ke pusat). Berdasarkan teorema Pythagoras: PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengenali sifat geometris bahwa garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, kemudian menerapkan teorema Pythagoras untuk menghitung panjang sisi segitiga siku-siku.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B: PB = akar(PA^2 - AB^2)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara garis singgung dan jari-jari lingkaran (konseptual) serta penggunaan algoritma teorema Pythagoras (prosedural).. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; PB = akar(PA^2 - AB^2)
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari teorema Pythagoras pada konteks geometri lingkaran yang sudah sangat familiar bagi siswa kelas 11. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: jari-jari lingkaran A adalah 7 cm; titik P berjarak 25 cm dari titik A; panjang garis singgung PB

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat garis singgung lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah materi standar. Penggunaan Pythagoras pada segitiga siku-siku yang terbentuk adalah prosedur rutin. |

Run 2 — solusi: Garis singgung PB tegak lurus dengan jari-jari AB di titik B, membentuk segitiga siku-siku ABP dengan hipotenusa AP. Diketahui AB = 7 cm (jari-jari) dan AP = 25 cm (jarak titik ke pusat). Berdasarkan teorema Pythagoras: PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat geometris bahwa garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, kemudian menerapkan teorema Pythagoras untuk menyelesaikan masalah. Ini adalah penerapan prosedur rutin pada situasi geometris yang standar.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B: PB = akar(PA^2 - AB^2)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara garis singgung dan jari-jari lingkaran, serta penggunaan prosedur algoritma (Pythagoras) untuk menghitung panjang sisi.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali hubungan siku-siku antara garis singgung dan jari-jari, lalu menghitung menggunakan Pythagoras. Tidak ada langkah non-rutin atau integrasi kompleks.. Bukti: jari-jari lingkaran A adalah 7 cm; titik P berjarak 25 cm dari titik A; panjang garis singgung PB

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat dasar garis singgung lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik standar kelas 11. Soal ini menggunakan prosedur yang sangat familiar bagi siswa di jenjang ini. |

Run 3 — solusi: Garis singgung PB tegak lurus dengan jari-jari AB di titik B, membentuk segitiga siku-siku ABP dengan hipotenusa AP. Diketahui AB = 7 cm (jari-jari) dan AP = 25 cm (jarak titik ke pusat). Berdasarkan teorema Pythagoras: PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat geometris bahwa garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, kemudian menerapkan teorema Pythagoras pada segitiga siku-siku yang terbentuk. Ini adalah penerapan prosedur rutin.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B: PB = akar(PA^2 - AB^2)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara garis singgung dan jari-jari lingkaran, serta penggunaan prosedur algoritma teorema Pythagoras.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang sangat familiar bagi siswa kelas 11. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: jari-jari lingkaran A adalah 7 cm; titik P berjarak 25 cm dari titik A; panjang garis singgung PB

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat garis singgung lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik dasar geometri yang sudah dipelajari di jenjang sebelumnya dan diperkuat di kelas 11. Soal ini bersifat langsung (direct application). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5067`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengenali sifat geometris bahwa garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, kemudian menerapkan teorema Pythagoras untuk menghitung panjang sisi segitiga siku-siku.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang hubungan antara garis singgung dan jari-jari lingkaran (konseptual) serta penggunaan algoritma teorema Pythagoras (prosedural).
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung dari teorema Pythagoras pada konteks geometri lingkaran yang sudah sangat familiar bagi siswa kelas 11. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat garis singgung lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah materi standar. Penggunaan Pythagoras pada segitiga siku-siku yang terbentuk adalah prosedur rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Garis Singgung
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika jari-jari lingkaran A adalah 7 cm dan titik P berjarak 25 cm dari titik A, berapakah panjang garis singgung PB ?
Pilihan: A. 18 cm
B. 25 cm
C. 24 cm
D. 26 cm
Transkripsi visual: Gambar menunjukkan sebuah lingkaran dengan pusat A. Titik B terletak pada keliling lingkaran. Garis AB adalah jari-jari lingkaran. Titik P berada di luar lingkaran. Garis biru melewati titik B dan P, yang merupakan garis singgung lingkaran di titik B. Garis hitam menghubungkan pusat A ke titik P. Segitiga ABP terbentuk dengan sudut siku-siku di B karena sifat garis singgung yang tegak lurus dengan jari-jari.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `9d3b005f20ecd5dabca2aa9e`

Jika AD = 3 cm dan BE = AD, tentukan:<br><br>besar `∠` BAE

| Opsi | Isi |
|---|---|
| A | 90° |
| B | 60° |
| C | 45° |
| D | 120° |

![Gambar sumber soal 13](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0089-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm. Diketahui BE = AD = 3 cm. Karena AE = AB = BE = 3 cm, maka segitiga ABE adalah segitiga sama sisi. Oleh karena itu, ∠BAE = 60°.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0089-05.png. Transkripsi visual: Gambar menunjukkan lingkaran dengan pusat A. Titik D, E, dan B terletak pada keliling lingkaran. Ruas garis AD, AE, dan AB adalah jari-jari lingkaran. Ruas garis BE menghubungkan titik B dan E. Diketahui AD = 3 cm dan BE = AD = 3 cm. Karena A adalah pusat, maka AE = AB = AD = 3 cm. Segitiga ABE memiliki sisi AE = 3 cm, AB = 3 cm, dan BE = 3 cm.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4d52c9c72966c265d16c130d32b53e6b089bad1b2d051c205bcb7a2532db74c9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3250 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3206 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3189 |

Run 1 — solusi: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm. Diketahui BE = AD = 3 cm. Karena AE = AB = BE = 3 cm, maka segitiga ABE adalah segitiga sama sisi. Oleh karena itu, ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti jari-jari lingkaran untuk menentukan panjang sisi segitiga dan mengenali sifat segitiga sama sisi. Ini adalah penerapan konsep geometri dasar pada situasi rutin.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); karena BE=AD=3 cm juga, maka AE=AB=BE=3 cm dan segitiga ABE sama sisi
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi jari-jari lingkaran dan sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran; segitiga ABE sama sisi
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu menghubungkan informasi jari-jari dengan panjang sisi segitiga untuk menyimpulkan jenis segitiga. Tidak ada langkah non-rutin atau kompleksitas tinggi.. Bukti: AD = 3 cm dan BE = AD; A adalah pusat lingkaran

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari lingkaran dan sifat segitiga sama sisi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah topik standar kelas 11. Soal ini menguji pemahaman dasar geometri yang seharusnya sudah dikuasai siswa. |

Run 2 — solusi: A adalah pusat lingkaran, maka AD = AE = AB = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Segitiga ABE memiliki sisi-sisi AE = AB = BE = 3 cm, sehingga segitiga ABE adalah segitiga sama sisi. Maka, ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti lingkaran (jari-jari sama panjang) dan menerapkan konsep segitiga sama sisi untuk menentukan besar sudut. Ini adalah penerapan konsep geometri dasar pada situasi rutin.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); segitiga ABE sama sisi, sehingga ∠BAE=60°
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi jari-jari lingkaran dan sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); segitiga ABE sama sisi
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali bahwa jari-jari lingkaran sama panjang dan menggunakan informasi tersebut untuk mengidentifikasi segitiga sama sisi. Tidak ada langkah non-rutin atau kompleksitas tinggi.. Bukti: AD = 3 cm dan BE = AD; A adalah pusat lingkaran

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari lingkaran dan sifat segitiga sama sisi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan sifat segitiga adalah dasar geometri yang sudah dikuasai sebelum kelas 11. Soal ini sangat standar dan prosedural. |

Run 3 — solusi: A adalah pusat lingkaran, maka AB = AE = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Segitiga ABE memiliki sisi AB = AE = BE = 3 cm, sehingga merupakan segitiga sama sisi. Maka, besar ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti lingkaran (jari-jari) untuk menentukan panjang sisi segitiga dan menerapkan konsep segitiga sama sisi untuk menentukan sudutnya.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); segitiga ABE sama sisi, sehingga ∠BAE=60°
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara jari-jari lingkaran dan sifat segitiga yang dibentuk oleh jari-jari tersebut.. Bukti: A adalah pusat lingkaran; segitiga ABE sama sisi
- Intended difficulty `classify/Easy`: Soal ini memerlukan pemahaman dasar tentang jari-jari dan sifat segitiga sama sisi. Prosedur penyelesaiannya langsung dan familiar bagi siswa kelas 11.. Bukti: AD = 3 cm dan BE = AD; A adalah pusat lingkaran

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari lingkaran dan sifat segitiga sama sisi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah topik standar. Mengidentifikasi jari-jari dan sifat segitiga sama sisi adalah prosedur rutin yang sesuai untuk tingkat kesulitan rendah. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Tali Busur
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika AD = 3 cm dan BE = AD, tentukan:

besar `∠` BAE
Pilihan: A. 90°
B. 60°
C. 45°
D. 120°
Transkripsi visual: Gambar menunjukkan lingkaran dengan pusat A. Titik D, E, dan B terletak pada keliling lingkaran. Ruas garis AD, AE, dan AB adalah jari-jari lingkaran. Ruas garis BE menghubungkan titik B dan E. Diketahui AD = 3 cm dan BE = AD = 3 cm. Karena A adalah pusat, maka AE = AB = AD = 3 cm. Segitiga ABE memiliki sisi AE = 3 cm, AB = 3 cm, dan BE = 3 cm.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `b9acc681a7567cd1039ff751`

Lingkaran yang berpusat di titik O dan jari-jarinya 5 cm. Berapa panjang tali busurnya yang paling panjang?

| Opsi | Isi |
|---|---|
| A | 10 cm |
| B | 15 cm |
| C | 20 cm |
| D | 5 cm |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 * jari-jari = 2 * 5 cm = 10 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3522f2a5dcb71eb84d0633c81ba0fe930bc2258f66a229d3a96a353de52909fd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2450 |
| 2 | success | valid / verified | knowing | factual | Easy | 2602 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2464 |

Run 1 — solusi: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 * jari-jari = 2 * 5 cm = 10 cm.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat definisi bahwa diameter adalah tali busur terpanjang dan menerapkan rumus d = 2r.. Bukti: tali busurnya yang paling panjang; jari-jarinya 5 cm
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep dasar geometri tentang hubungan jari-jari dan diameter.. Bukti: tali busurnya yang paling panjang; jari-jarinya 5 cm
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pemahaman definisi diameter sebagai tali busur terpanjang.. Bukti: tali busurnya yang paling panjang; jari-jarinya 5 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari dan diameter lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini biasanya dipelajari di jenjang SMP, sehingga untuk kelas 11 ini sangat mudah (Easy). |

Run 2 — solusi: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 x jari-jari = 2 x 5 cm = 10 cm.
- Domain kognitif `classify/knowing`: Soal ini menuntut pemahaman definisi dasar bahwa tali busur terpanjang adalah diameter.. Bukti: tali busurnya yang paling panjang
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui fakta geometris bahwa diameter adalah tali busur terpanjang.. Bukti: jari-jarinya 5 cm; tali busurnya yang paling panjang
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan satu langkah perhitungan sederhana (2 x r) berdasarkan definisi.. Bukti: jari-jarinya 5 cm; tali busurnya yang paling panjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi diameter dan hubungan diameter dengan jari-jari lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah dasar geometri yang sudah dipelajari sejak SMP, sehingga untuk kelas 11 ini adalah soal yang sangat mudah. |

Run 3 — solusi: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 * jari-jari = 2 * 5 cm = 10 cm.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali definisi tali busur terpanjang sebagai diameter dan menerapkan rumus d=2r. Ini adalah proses langsung.. Bukti: tali busurnya yang paling panjang; jari-jarinya 5 cm
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep dasar geometri lingkaran mengenai hubungan antara jari-jari dan diameter.. Bukti: tali busurnya yang paling panjang; jari-jarinya 5 cm
- Intended difficulty `classify/Easy`: Soal sangat mendasar, hanya memerlukan satu langkah penerapan definisi diameter.. Bukti: jari-jarinya 5 cm; panjang tali busurnya yang paling panjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi diameter sebagai tali busur terpanjang dan hubungan d=2r. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dasar yang sudah dipelajari sejak SMP, sangat rutin untuk kelas 11. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3115`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal menuntut pengenalan fakta dasar bahwa tali busur terpanjang pada lingkaran adalah diameter, yang merupakan proses kognitif knowing.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konsep dasar geometri tentang hubungan antara jari-jari dan diameter.
- Intended difficulty `Easy`: Soal ini sangat mendasar dan rutin, hanya memerlukan satu langkah penerapan definisi diameter sebagai tali busur terpanjang.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari dan diameter lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan dasar geometri yang dipelajari di jenjang SMP, sehingga untuk kelas 11 soal ini dikategorikan sangat mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Tali Busur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lingkaran yang berpusat di titik O dan jari-jarinya 5 cm. Berapa panjang tali busurnya yang paling panjang?
Pilihan: A. 10 cm
B. 15 cm
C. 20 cm
D. 5 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `1ef6efc5863938a14b737897`

Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar 2.77 dengan diameter 2 meter dan panjang 12 meter?

| Opsi | Isi |
|---|---|
| A | 37,68 liter |
| B | 150.720 liter |
| C | 37.680 liter |
| D | 36.000 liter |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jari-jari (r) = diameter/2 = 2/2 = 1 m. Tinggi (h) = 12 m. Volume = π × r² × h = 3,14 × 1² × 12 = 37,68 m³. Karena 1 m³ = 1.000 liter, maka volume = 37,68 × 1.000 = 37.680 liter.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e2aa37e3757232adc6a1ceb7f584fde5c609cce4de0cef3f3df096fe00dd0efa`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2086 |
| 2 | success | valid / verified | applying | procedural | Easy | 2078 |
| 3 | success | valid / verified | applying | procedural | Easy | 2083 |

Run 1 — solusi: Jari-jari (r) = diameter/2 = 2/2 = 1 m. Tinggi (h) = 12 m. Volume = π × r² × h = 3,14 × 1² × 12 = 37,68 m³. Karena 1 m³ = 1.000 liter, maka volume = 37,68 × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan (m³ ke liter). Ini adalah prosedur rutin yang melibatkan pemilihan rumus dan aplikasi langsung, sehingga masuk dalam domain applying.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan volume bangun ruang (tabung) dan konversi satuan, yang merupakan pengetahuan prosedural.. Bukti: volume tabung; diameter 2 meter dan panjang 12 meter
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena melibatkan prosedur standar yang familiar bagi siswa kelas 11 (volume tabung) dengan beban komputasi rendah dan langkah-langkah yang jelas.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume tabung adalah materi dasar yang sudah dipelajari di jenjang sebelumnya, sehingga untuk kelas 11 ini merupakan prosedur yang sangat rutin. |

Run 2 — solusi: Jari-jari (r) = diameter/2 = 2/2 = 1 m. Tinggi (h) = 12 m. Volume = πr²h = 3,14 × 1² × 12 = 37,68 m³. Karena 1 m³ = 1.000 liter, maka volume = 37,68 × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan (m³ ke liter). Ini adalah prosedur standar yang rutin.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang rumus volume tabung dan hubungan antar satuan volume.. Bukti: Volume Bangun Ruang Sisi Lengkung; diameter 2 meter dan panjang 12 meter
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas: menentukan jari-jari, menghitung volume, dan mengonversi satuan. Tidak ada strategi non-rutin yang diperlukan.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume tabung adalah materi dasar yang sudah dipelajari di jenjang sebelumnya, sehingga bagi siswa kelas 11 ini merupakan prosedur yang sangat familiar. |

Run 3 — solusi: Jari-jari (r) = diameter/2 = 2/2 = 1 m. Volume tabung = πr²h = 3,14 × 1² × 12 = 37,68 m³. Karena 1 m³ = 1.000 liter, maka volume = 37,68 × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan (m³ ke liter). Ini adalah prosedur rutin yang melibatkan pemilihan rumus dan konversi unit yang umum dalam konteks geometri kelas 11.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang rumus volume tabung dan hubungan antar satuan volume, yang merupakan pengetahuan prosedural.. Bukti: tabung penyimpanan besar; diameter 2 meter dan panjang 12 meter
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menentukan jari-jari dari diameter, menghitung volume, dan melakukan konversi satuan. Tidak ada strategi non-rutin atau kendala kompleks.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung, hubungan diameter dan jari-jari, konversi satuan m³ ke liter. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume tabung adalah materi dasar geometri yang sudah dipelajari sebelum kelas 11, sehingga bagi siswa kelas 11 ini adalah prosedur yang sangat familiar. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar 2.77 dengan diameter 2 meter dan panjang 12 meter?
Pilihan: A. 37,68 liter
B. 150.720 liter
C. 37.680 liter
D. 36.000 liter
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `9bee88ce31163c95d6276272`

Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.<br><br>Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.

| Opsi | Isi |
|---|---|
| A | Semakin banyak kendaraan bermotor, semakin menurun tingkat polusi udara (korelasi negatif) |
| B | Semakin banyak kendaraan bermotor, semakin meningkat tingkat polusi udara (korelasi positif) |
| C | Tidak ada hubungan antara banyak kendaraan bermotor dan tingkat polusi udara |
| D | Hubungan keduanya tidak dapat ditentukan tanpa data numerik |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kendaraan bermotor menghasilkan emisi gas buang. Semakin banyak jumlah kendaraan, semakin besar volume emisi yang dihasilkan, sehingga tingkat polusi udara cenderung meningkat. Ini menunjukkan hubungan korelasi positif.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c7bb1fa33f2857c1bb9c0d9bb77224adcf85a0281a208b2a781d071923be216a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1981 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1991 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1988 |

Run 1 — solusi: Kendaraan bermotor menghasilkan emisi gas buang. Semakin banyak jumlah kendaraan, semakin besar volume emisi yang dihasilkan, sehingga tingkat polusi udara cenderung meningkat. Ini menunjukkan hubungan korelasi positif.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi arah hubungan (korelasi) antara dua variabel berdasarkan pemahaman kontekstual, bukan sekadar menghitung. Ini melibatkan penerapan konsep korelasi pada situasi nyata.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip hubungan antarvariabel (korelasi) dan menerapkannya pada konteks dunia nyata.. Bukti: korelasi positif; korelasi negatif
- Intended difficulty `classify/Easy`: Soal ini bersifat kualitatif dan menguji pemahaman dasar tentang arah korelasi. Tidak ada perhitungan numerik atau analisis data kompleks yang diperlukan, sehingga beban kognitifnya rendah.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep korelasi (positif/negatif) dan hubungan sebab-akibat sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi arah hubungan korelasi secara kualitatif adalah prosedur dasar sebelum masuk ke analisis regresi linear yang lebih formal. |

Run 2 — solusi: Kendaraan bermotor menghasilkan emisi gas buang. Semakin banyak jumlah kendaraan, semakin besar volume emisi yang dihasilkan, sehingga tingkat polusi udara meningkat. Ini menunjukkan hubungan korelasi positif.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi arah hubungan (korelasi) berdasarkan pemahaman kontekstual tentang sebab-akibat, bukan sekadar membaca data numerik.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep korelasi positif dalam konteks dunia nyata (hubungan sebab-akibat antara emisi kendaraan dan polusi).. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Intended difficulty `classify/Easy`: Soal ini bersifat kualitatif dan menguji pemahaman dasar tentang korelasi positif dalam konteks sehari-hari. Tidak ada perhitungan atau analisis data kompleks yang diperlukan.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi positif dan hubungan sebab-akibat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi arah korelasi dari konteks nyata adalah prosedur dasar dalam topik analisis data/diagram pencar. |

Run 3 — solusi: Kendaraan bermotor membakar bahan bakar yang menghasilkan emisi gas buang. Secara logis, peningkatan jumlah kendaraan akan meningkatkan total emisi gas buang di udara, sehingga terdapat korelasi positif antara jumlah kendaraan dan tingkat polusi udara.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi arah hubungan (korelasi) berdasarkan pemahaman kontekstual tentang sebab-akibat, bukan melakukan perhitungan statistik.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep korelasi positif dalam konteks dunia nyata (hubungan sebab-akibat antara emisi kendaraan dan polusi).. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Intended difficulty `classify/Easy`: Soal ini bersifat kualitatif dan menguji pemahaman dasar tentang arah korelasi dalam konteks sehari-hari yang sangat familiar, sehingga beban kognitifnya rendah.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi positif dan hubungan sebab-akibat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi arah korelasi dari konteks nyata adalah prosedur dasar sebelum masuk ke analisis data numerik yang lebih kompleks. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Diagram Pencar atau Diagram Scatter
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.

Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.
Pilihan: A. Semakin banyak kendaraan bermotor, semakin menurun tingkat polusi udara (korelasi negatif)
B. Semakin banyak kendaraan bermotor, semakin meningkat tingkat polusi udara (korelasi positif)
C. Tidak ada hubungan antara banyak kendaraan bermotor dan tingkat polusi udara
D. Hubungan keduanya tidak dapat ditentukan tanpa data numerik
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `954fcaa8282f462df30d7e71`

Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.<br><br>Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin? Berikan alasan kalian.

| Opsi | Isi |
|---|---|
| A | Tidak ada hubungan antara jarak tempuh dan volume bensin |
| B | Hubungan keduanya tidak dapat ditentukan tanpa data numerik |
| C | Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin berkurang volume bensin dalam tangki bensin (korelasi negatif) |
| D | Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin bertambah volume bensin dalam tangki bensin (korelasi positif) |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jarak tempuh dan volume bensin memiliki korelasi negatif. Semakin jauh motor bergerak, semakin banyak bensin yang dikonsumsi, sehingga volume bensin dalam tangki berkurang.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dfb0d88cb55bff7d8bff97c79a66f1aebae2c0c6332f67858052d4f9b9f114d5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2010 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2032 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2028 |

Run 1 — solusi: Jarak tempuh dan volume bensin memiliki korelasi negatif. Semakin jauh motor bergerak, semakin banyak bensin yang dikonsumsi, sehingga volume bensin dalam tangki berkurang.
- Domain kognitif `classify/applying`: Soal meminta siswa mengidentifikasi arah hubungan (korelasi) antara dua variabel berdasarkan pemahaman konsep dasar, bukan sekadar menghitung data.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip hubungan sebab-akibat antara konsumsi bahan bakar dan jarak tempuh (konsep korelasi negatif).. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung, tidak memerlukan perhitungan rumit atau strategi nonrutin, sehingga tergolong mudah bagi siswa kelas 11.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi negatif dan hubungan sebab-akibat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu mengidentifikasi korelasi kualitatif sederhana dalam konteks kehidupan sehari-hari. |

Run 2 — solusi: Jarak tempuh dan volume bensin memiliki korelasi negatif. Semakin jauh jarak yang ditempuh, semakin banyak bensin yang dikonsumsi mesin, sehingga volume bensin dalam tangki berkurang.
- Domain kognitif `classify/applying`: Soal meminta siswa mengidentifikasi arah hubungan (korelasi) antara dua variabel berdasarkan pemahaman konsep dasar, bukan sekadar menghitung atau mengingat fakta.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip korelasi negatif dalam konteks dunia nyata (hubungan sebab-akibat antara konsumsi bahan bakar dan jarak tempuh).. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung. Siswa hanya perlu memahami logika dasar konsumsi bahan bakar tanpa perlu melakukan perhitungan kompleks atau analisis data statistik yang mendalam.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi negatif dan hubungan sebab-akibat variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, memahami arah korelasi dari konteks sehari-hari adalah materi dasar dalam bab statistika/diagram pencar. |

Run 3 — solusi: Jarak tempuh dan volume bensin memiliki korelasi negatif. Semakin jauh jarak yang ditempuh motor, semakin banyak bensin yang terbakar sebagai energi, sehingga volume bensin dalam tangki semakin berkurang.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi dan menjelaskan arah hubungan (korelasi) antara dua variabel berdasarkan pemahaman konsep dunia nyata, bukan sekadar menghitung.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip hubungan sebab-akibat (konsumsi bahan bakar) untuk menentukan jenis korelasi (negatif) antara dua variabel.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Intended difficulty `classify/Easy`: Soal ini bersifat kualitatif dan menguji pemahaman dasar tentang korelasi variabel. Tidak memerlukan perhitungan atau strategi kompleks.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi variabel dan hubungan sebab-akibat dalam konteks sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi arah korelasi dari konteks nyata adalah tugas dasar dalam topik analisis data/diagram pencar. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Diagram Pencar atau Diagram Scatter
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.

Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin? Berikan alasan kalian.
Pilihan: A. Tidak ada hubungan antara jarak tempuh dan volume bensin
B. Hubungan keduanya tidak dapat ditentukan tanpa data numerik
C. Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin berkurang volume bensin dalam tangki bensin (korelasi negatif)
D. Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin bertambah volume bensin dalam tangki bensin (korelasi positif)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `cc594209724affd13041e475`

Pada saat kondisi mendadak, para pengendara mobil memerlukan waktu yang berbeda-beda untuk dapat bereaksi untuk menginjak rem mobil. Jarak yang diperlukan hingga terjadi reaksi menginjak rem disebut sebagai jarak reaksi. Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda. Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.<br><br>Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

| Opsi | Isi |
|---|---|
| A | 8,3 m |
| B | 7,2 m |
| C | 12,4 m |
| D | 11,34 m |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `7,2 m`.
Solusi minimum hasil AI: Persamaan regresi linear y = ax + b dapat diestimasi dari data. Menggunakan metode kuadrat terkecil, diperoleh persamaan y = 0,207x - 0,042. Untuk x = 35, y = 0,207(35) - 0,042 = 7,245 - 0,042 = 7,203. Dibulatkan menjadi 7,2 m.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1a372373f96828465177d9623bbd8e03e6ccff8d7e603a4a57706a7d38797c19`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2242 |
| 2 | success | valid / verified | applying | procedural | Medium | 2295 |
| 3 | success | valid / verified | applying | procedural | Medium | 2296 |

Run 1 — solusi: Persamaan regresi linear y = ax + b dapat diestimasi dari data. Menggunakan metode kuadrat terkecil, diperoleh persamaan y = 0,207x - 0,042. Untuk x = 35, y = 0,207(35) - 0,042 = 7,245 - 0,042 = 7,203. Dibulatkan menjadi 7,2 m.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan model regresi linear (prosedur) untuk melakukan interpolasi nilai di luar titik data yang diberikan, yang merupakan penerapan konsep statistik dalam situasi rutin.. Bukti: Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang bagaimana menggunakan model regresi linear untuk memprediksi nilai, yang merupakan bagian dari pengetahuan prosedural dalam statistika.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan prosedur regresi linear untuk melakukan interpolasi. Meskipun melibatkan perhitungan, langkah-langkahnya rutin dan terstruktur untuk siswa kelas 11.. Bukti: Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, persamaan garis lurus, dan substitusi nilai ke dalam persamaan. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu melakukan analisis regresi sederhana. Soal ini menuntut penerapan rumus regresi yang sudah dipelajari, bukan sekadar membaca tabel. |

Run 2 — solusi: Persamaan regresi linear y = a + bx dapat diestimasi dari data. Menggunakan metode kuadrat terkecil, diperoleh persamaan y = -0,042 + 0,207x. Untuk x = 35, y = -0,042 + 0,207(35) = -0,042 + 7,245 = 7,203, dibulatkan menjadi 7,2 m.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan model regresi linear (yang diberikan atau dihitung) untuk melakukan prediksi (interpolasi) pada nilai x yang tidak ada di tabel.. Bukti: Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Dimensi pengetahuan `classify/procedural`: Soal ini memerlukan pemahaman tentang konsep regresi linear sebagai model prediksi dan prosedur perhitungan menggunakan persamaan garis.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi; Hitunglah prediksi jarak reaksi
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa perlu memahami bahwa prediksi tidak bisa hanya membaca tabel (interpolasi sederhana), melainkan memerlukan model regresi. Meskipun persamaan diberikan dalam kunci, siswa kelas 11 diharapkan mampu mengkonstruksi atau menggunakan model linear untuk prediksi.. Bukti: Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang persamaan garis lurus dan konsep regresi linear sederhana. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 sudah mempelajari regresi linear. Soal ini menguji kemampuan menerapkan model untuk prediksi, yang merupakan standar kompetensi di jenjang tersebut. |

Run 3 — solusi: Persamaan regresi linear y = ax + b dapat ditentukan dari data. Dengan x = kecepatan dan y = jarak reaksi, diperoleh estimasi persamaan y = 0,207x - 0,042. Untuk x = 35, y = 0,207(35) - 0,042 = 7,245 - 0,042 = 7,203. Dibulatkan menjadi 7,2 m.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan model regresi linear untuk melakukan prediksi (interpolasi) pada nilai x yang tidak ada di tabel, yang merupakan penerapan prosedur statistik rutin.. Bukti: Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan linear antara dua variabel dan penggunaan model regresi untuk prediksi.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa perlu menentukan atau menggunakan model regresi linear dari data yang diberikan, bukan sekadar membaca tabel. Meskipun prosedurnya rutin, terdapat langkah pemilihan model dan perhitungan substitusi.. Bukti: Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, konsep variabel bebas dan terikat, serta kemampuan substitusi nilai ke dalam persamaan linear. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 karena regresi linear adalah materi standar. Tingkat kesulitan Medium karena menuntut siswa melakukan prediksi di luar data tabel (interpolasi) menggunakan model linear. |

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Regresi Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada saat kondisi mendadak, para pengendara mobil memerlukan waktu yang berbeda-beda untuk dapat bereaksi untuk menginjak rem mobil. Jarak yang diperlukan hingga terjadi reaksi menginjak rem disebut sebagai jarak reaksi. Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda. Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.

Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
Pilihan: A. 8,3 m
B. 7,2 m
C. 12,4 m
D. 11,34 m
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `cb666d7ac7a8bdfb36335e5a`

Tabel berikut menunjukkan banyak tempat duduk terhadap biaya per jam dari tiga model pesawat terbang yang digunakan oleh maskapai Garuda Indonesia.<br><br>\|Model Pesawat\|Banyak tempat duduk\|Biaya (rupiah/jam)\|<br>\|---\|---\|---\|<br>\|A\|50\|1.100.000,00\|<br>\|B\|100\|2.100.000,00\|<br>\|C\|150\|2.700.000,00\|<br><br>Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?

| Opsi | Isi |
|---|---|
| A | yˆ = 300000 + 16000x |
| B | yˆ = 367000 + 16000x |
| C | Tidak dapat ditentukan tanpa menggambar diagram pencarnya |
| D | Keduanya sama tepat karena mempunyai gradien (b) yang sama |

Kunci sumber: `B`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal memiliki cacat logika variabel. Jika x=biaya (dalam rupiah) dan y=tempat duduk, model y=367000+16000x menghasilkan nilai y yang tidak masuk akal (ratusan ribu). Jika x=biaya (dalam jutaan), model tetap tidak masuk akal. Karena model yang diberikan tidak sesuai dengan data (50, 100, 150), perhitungan residu yang diberikan sumber tidak dapat diverifikasi sebagai model regresi yang valid secara kontekstual.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e0810b5a763e3b67006264286ffd00404dbb23345415697961773a0a7b705204`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 2544 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 2519 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2363 |

Run 1 — solusi: Model regresi y = a + bx memprediksi y (tempat duduk) dari x (biaya). Untuk y = 367000 + 16000x, residu (y_i - y_hat_i)^2 dihitung: (50 - (367000+16000*1.1))^2 + ... (dst). Namun, soal meminta prediksi tempat duduk (y) terhadap biaya (x). Jika x=biaya, y=tempat duduk, maka y = 367000 + 16000x menghasilkan nilai y yang sangat besar (jutaan) untuk x=1.1 juta, yang tidak masuk akal secara fisik (jumlah kursi). Terdapat ambiguitas variabel dalam soal, namun berdasarkan perhitungan jumlah kuadrat residu yang diberikan sumber, opsi B adalah yang meminimalkan error.
- Domain kognitif `classify/reasoning`: Siswa diminta mengevaluasi ketepatan dua model regresi berdasarkan kriteria statistik (jumlah kuadrat residu), bukan sekadar menghitung regresi dari data.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang kriteria 'ketepatan' garis regresi (Least Squares Method) dan bagaimana residu digunakan untuk membandingkan model.. Bukti: jumlah kuadrat residu yˆ = 367000+16000x adalah 26.667.000.000
- Intended difficulty `classify/Hard`: Soal ini menuntut pemahaman mendalam tentang kriteria regresi linear (Least Squares). Siswa tidak hanya melakukan perhitungan rutin, tetapi harus memahami mengapa model dengan residu lebih kecil lebih tepat, yang merupakan konsep non-rutin dalam konteks SMA.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya; jumlah kuadrat residu yˆ = 367000+16000x adalah 26.667.000.000, lebih kecil dari jumlah kuadrat residu yˆ = 300000+16000x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar regresi linear, residu, dan metode kuadrat terkecil. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | high |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun regresi diajarkan di kelas 11, membandingkan dua model menggunakan jumlah kuadrat residu adalah tugas tingkat tinggi yang melampaui sekadar mencari persamaan garis. |

Run 2 — solusi: Misal x = biaya, y = tempat duduk. Model 1: y = 367000 + 16000x. Model 2: y = 300000 + 16000x. Karena x dalam jutaan, kita gunakan x_1=1.1, x_2=2.1, x_3=2.7. Prediksi Model 1: y1=384600, y2=400600, y3=410200. Prediksi Model 2: y1=317600, y2=333600, y3=343200. Namun, soal ini terbalik mendefinisikan variabel (x=biaya, y=tempat duduk). Jika x=biaya (dalam juta), y=tempat duduk, maka model y=a+bx tidak masuk akal secara skala (y=367000+16000x menghasilkan y > 300.000 untuk x=1.1). Terdapat kesalahan definisi variabel pada soal, namun secara matematis perbandingan jumlah kuadrat residu tetap dapat dihitung untuk menentukan model terbaik.
- Domain kognitif `classify/reasoning`: Siswa diminta mengevaluasi ketepatan dua model regresi berdasarkan kriteria statistik (jumlah kuadrat residu), bukan sekadar visual, sehingga memerlukan pemahaman konseptual tentang regresi.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip jumlah kuadrat residu sebagai ukuran ketepatan model regresi.. Bukti: jumlah kuadrat residu yˆ = 367000+16000x adalah 26.667.000.000
- Intended difficulty `classify/Hard`: Soal ini menuntut pemahaman mendalam tentang kriteria pemilihan model regresi (least squares) dan menuntut siswa untuk tidak terjebak pada visualisasi atau gradien saja.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep regresi linear, residu, dan jumlah kuadrat residu. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | high |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun topiknya ada di kelas 11, membandingkan dua model regresi menggunakan jumlah kuadrat residu adalah tugas non-rutin yang kompleks bagi siswa, terutama dengan angka yang besar dan potensi kebingungan variabel. |

Run 3 — solusi: Hitung jumlah kuadrat residu (SSE) untuk kedua model. Untuk y=300000+16000x: SSE = (50-(300000+16000*1.1))^2 + (100-(300000+16000*2.1))^2 + (150-(300000+16000*2.7))^2 = 40.000.000.000. Untuk y=367000+16000x: SSE = (50-(367000+16000*1.1))^2 + (100-(367000+16000*2.1))^2 + (150-(367000+16000*2.7))^2 = 26.667.000.000. Karena SSE B < SSE A, maka B lebih tepat.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (menghitung jumlah kuadrat residu) untuk membandingkan ketepatan dua model regresi yang diberikan, bukan sekadar membaca data.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang kriteria 'ketepatan' garis regresi (least squares) dan prosedur perhitungan residu.. Bukti: Persamaan garis regresi mana yang lebih tepat
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan residu untuk dua model berbeda. Ini melibatkan beberapa langkah rutin yang terkait dan pemilihan prosedur yang tepat untuk membandingkan model, yang sesuai untuk tingkat menengah.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear dan konsep residu. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu membandingkan model regresi menggunakan kriteria statistik dasar seperti jumlah kuadrat residu. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 2, "applying": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Hard": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Hard |

Adjudikasi AI: `success`; token `4750`.
Konten: `concern`; kunci: `conflict`; masalah: Terdapat kesalahan fatal dalam definisi variabel pada soal. Soal meminta memprediksi 'banyak tempat duduk' (y) terhadap 'biaya' (x). Namun, persamaan yang diberikan (y = 367000 + 16000x) menghasilkan nilai y dalam ratusan ribu untuk x dalam jutaan, yang secara fisik tidak masuk akal (jumlah kursi tidak mungkin ratusan ribu).; Terdapat ketidakkonsistenan skala. Jika x adalah biaya dalam rupiah (1.100.000), maka 16000x akan menghasilkan nilai yang sangat besar, jauh melampaui jumlah tempat duduk (50, 100, 150). Soal ini kemungkinan besar tertukar antara variabel bebas dan terikat atau memiliki kesalahan penulisan konstanta/koefisien yang sangat besar.; Meskipun secara matematis perbandingan jumlah kuadrat residu (SSE) dapat dihitung, soal ini cacat secara kontekstual karena model yang diberikan tidak merepresentasikan data dengan benar..
- Domain kognitif `applying`: Siswa diminta mengevaluasi ketepatan model berdasarkan kriteria statistik (jumlah kuadrat residu). Meskipun soal cacat, tuntutan kognitifnya adalah menerapkan prosedur perbandingan model.
- Dimensi pengetahuan `conceptual`: Memerlukan pemahaman konseptual tentang kriteria 'ketepatan' garis regresi (Least Squares Method) dan bagaimana residu digunakan untuk membandingkan model.
- Intended difficulty `Hard`: Soal ini menuntut pemahaman tentang kriteria pemilihan model regresi. Namun, karena soal memiliki cacat logika variabel yang sangat besar, tingkat kesulitan menjadi tidak relevan karena siswa tidak mungkin mendapatkan jawaban yang masuk akal secara kontekstual.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar regresi linear, residu, dan metode kuadrat terkecil. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | high |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Membandingkan dua model menggunakan jumlah kuadrat residu adalah tugas tingkat tinggi, namun soal ini cacat secara kontekstual. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Regresi Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel berikut menunjukkan banyak tempat duduk terhadap biaya per jam dari tiga model pesawat terbang yang digunakan oleh maskapai Garuda Indonesia.

|Model Pesawat|Banyak tempat duduk|Biaya (rupiah/jam)|
|---|---|---|
|A|50|1.100.000,00|
|B|100|2.100.000,00|
|C|150|2.700.000,00|

Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?
Pilihan: A. yˆ = 300000 + 16000x
B. yˆ = 367000 + 16000x
C. Tidak dapat ditentukan tanpa menggambar diagram pencarnya
D. Keduanya sama tepat karena mempunyai gradien (b) yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat kesalahan fatal dalam definisi variabel pada soal. Soal meminta memprediksi 'banyak tempat duduk' (y) terhadap 'biaya' (x). Namun, persamaan yang diberikan (y = 367000 + 16000x) menghasilkan nilai y dalam ratusan ribu untuk x dalam jutaan, yang secara fisik tidak masuk akal (jumlah kursi tidak mungkin ratusan ribu).; Terdapat ketidakkonsistenan skala. Jika x adalah biaya dalam rupiah (1.100.000), maka 16000x akan menghasilkan nilai yang sangat besar, jauh melampaui jumlah tempat duduk (50, 100, 150). Soal ini kemungkinan besar tertukar antara variabel bebas dan terikat atau memiliki kesalahan penulisan konstanta/koefisien yang sangat besar.; Meskipun secara matematis perbandingan jumlah kuadrat residu (SSE) dapat dihitung, soal ini cacat secara kontekstual karena model yang diberikan tidak merepresentasikan data dengan benar..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Hard", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `5a713d72bd575400bbc8e916`

Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.<br><br>Berapa persentase IQ yang diterangkan oleh lingkar kepala?

| Opsi | Isi |
|---|---|
| A | 13,8% |
| B | 0,19% |
| C | 98,1% |
| D | 1,9% |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Persentase variansi yang dijelaskan oleh variabel bebas ditentukan oleh koefisien determinasi (r^2). Diketahui r = 0,138, maka r^2 = (0,138)^2 = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044%, yang dibulatkan menjadi 1,9%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eb44baf2ba500410060c717e11419cb008f5494d3c82716d9dc17d338562d4a3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2173 |
| 2 | success | valid / verified | applying | procedural | Easy | 2125 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2164 |

Run 1 — solusi: Persentase variansi yang dijelaskan (koefisien determinasi) dihitung dengan mengkuadratkan koefisien korelasi (r). r = 0,138, maka r^2 = (0,138)^2 = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044% atau sekitar 1,9%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep koefisien determinasi (r^2) untuk menentukan persentase variansi yang dijelaskan oleh variabel bebas, yang merupakan prosedur standar dalam analisis korelasi.. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang hubungan antara koefisien korelasi (r) dan koefisien determinasi (r^2) dalam konteks statistika.. Bukti: Nilai koefisien korelasinya adalah 0,138; persentase IQ yang diterangkan oleh lingkar kepala
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena hanya memerlukan satu langkah prosedural langsung (mengkuadratkan nilai r) untuk mendapatkan jawaban. Tidak ada manipulasi data kompleks atau interpretasi non-rutin yang diperlukan.. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien korelasi dan koefisien determinasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi regresi dan korelasi adalah bagian dari kurikulum kelas 11. Mengubah r menjadi r^2 adalah prosedur rutin yang diajarkan. |

Run 2 — solusi: Persentase variansi IQ yang diterangkan oleh lingkar kepala ditentukan oleh koefisien determinasi (r²). Diketahui r = 0,138, maka r² = (0,138)² = 0,019044. Dalam bentuk persentase, 0,019044 ≈ 1,9%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep koefisien determinasi (r²) untuk menjelaskan persentase variansi variabel terikat yang dijelaskan oleh variabel bebas, yang merupakan prosedur standar dalam analisis korelasi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang hubungan antara koefisien korelasi (r) dan koefisien determinasi (r²) dalam konteks statistik.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan satu langkah perhitungan langsung (mengkuadratkan nilai r) tanpa manipulasi data yang kompleks atau interpretasi grafik yang mendalam.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien korelasi dan koefisien determinasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan memahami konsep dasar statistik deskriptif dan korelasi. Perhitungan r² adalah prosedur rutin. |

Run 3 — solusi: Persentase variansi variabel terikat yang dijelaskan oleh variabel bebas ditentukan oleh koefisien determinasi (r^2). Diketahui r = 0,138, maka r^2 = (0,138)^2 = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044%, yang dibulatkan menjadi 1,9%.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep koefisien determinasi (r^2) sebagai ukuran proporsi variansi yang dijelaskan oleh model regresi, bukan sekadar menggunakan nilai korelasi (r) secara langsung.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara koefisien korelasi dan koefisien determinasi dalam analisis regresi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus memilih prosedur yang tepat (mengkuadratkan r) dan memahami interpretasi statistik, bukan sekadar operasi hitung langsung.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi (r) dan koefisien determinasi (r^2). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi regresi dan korelasi merupakan bagian dari kurikulum kelas 11. Membedakan r dan r^2 adalah konsep kunci yang sering diuji. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3868`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep koefisien determinasi (r^2) untuk menentukan proporsi variansi yang dijelaskan, yang merupakan prosedur standar dalam analisis korelasi.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang hubungan antara koefisien korelasi (r) dan koefisien determinasi (r^2) dalam konteks statistika.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena hanya memerlukan satu langkah prosedural langsung (mengkuadratkan nilai r) untuk mendapatkan jawaban. Tidak ada manipulasi data kompleks atau interpretasi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien korelasi dan koefisien determinasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi regresi dan korelasi adalah bagian dari kurikulum kelas 11. Mengubah r menjadi r^2 adalah prosedur rutin yang diajarkan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Analisis Korelasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.

Berapa persentase IQ yang diterangkan oleh lingkar kepala?
Pilihan: A. 13,8%
B. 0,19%
C. 98,1%
D. 1,9%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `2071d19215ee9fcf4926b805`

Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.<br><br>Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

| Opsi | Isi |
|---|---|
| A | 0,981% |
| B | 99,1% |
| C | 98,1% |
| D | 1,9% |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Koefisien determinasi r^2 = (0,138)^2 = 0,019044 atau 1,9%. Persentase variansi yang diterangkan variabel lain = 100% - r^2 = 100% - 1,9% = 98,1%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6acdfba8fa2b949acd4e0e1877259ab08800430abcc10bc79e6834f53ce31009`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3081 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3091 |
| 3 | failed | — / — | — | — | — | 0 |

Run 1 — solusi: Koefisien determinasi r^2 = (0,138)^2 = 0,019044 atau 1,9%. Persentase variansi yang diterangkan variabel lain = 100% - r^2 = 100% - 1,9% = 98,1%.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep koefisien determinasi (r^2) sebagai proporsi variansi yang dijelaskan dan menghitung komplemennya (1 - r^2) untuk mencari variansi yang dijelaskan oleh faktor lain.. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara korelasi (r) dan koefisien determinasi (r^2) serta interpretasi statistik dalam regresi.. Bukti: Nilai koefisien korelasinya adalah 0,138; persentase IQ yang diterangkan oleh variabel-variabel lainnya
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep statistik (r^2) dan operasi aritmatika dasar. Ini adalah prosedur rutin dalam analisis regresi.. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep koefisien korelasi (r) dan koefisien determinasi (r^2). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 mempelajari regresi linear dan korelasi. Menghitung r^2 dan komplemennya adalah prosedur standar. |

Run 2 — solusi: Koefisien determinasi r^2 = (0,138)^2 = 0,019044 atau 1,9044%. Persentase variansi yang diterangkan oleh variabel lain adalah 100% - r^2 = 100% - 1,9044% = 98,0956%, dibulatkan menjadi 98,1%.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep koefisien determinasi (r^2) dan bagaimana menghitung variansi yang tidak dijelaskan oleh model (1 - r^2).. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang apa yang diwakili oleh koefisien korelasi dan koefisien determinasi dalam konteks regresi.. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep statistik (r^2) dan prosedur perhitungan sederhana. Tidak ada strategi non-rutin yang kompleks.. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang koefisien korelasi (r) dan koefisien determinasi (r^2) serta interpretasinya. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi regresi dan korelasi diajarkan di kelas 11. Soal ini menguji pemahaman konsep dasar koefisien determinasi. |

Run 3 gagal: `ClientError:429`; tidak dihitung sebagai suara.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2} | majority_2_of_3 / needs_adjudication | — |
| Dimensi pengetahuan | {"conceptual": 2} | majority_2_of_3 / needs_adjudication | — |
| Intended difficulty | {"Medium": 2} | majority_2_of_3 / needs_adjudication | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Analisis Korelasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.

Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
Pilihan: A. 0,981%
B. 99,1%
C. 98,1%
D. 1,9%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `d6d3b4c5f9819d69d4c859d0`

Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315<br><br>Mengapa angka 750 kWh dapat dianggap sebagai pencilan?

| Opsi | Isi |
|---|---|
| A | Karena 750 kWh lebih dari 1,5 kali median data (315 kWh) |
| B | Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit |
| C | Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh) |
| D | Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `31c1b2c091a427804603e51b0a82d319bd38f9ea744aec3ede748b23d5c1814d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Representasi Data Lanjutan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315

Mengapa angka 750 kWh dapat dianggap sebagai pencilan?
Pilihan: A. Karena 750 kWh lebih dari 1,5 kali median data (315 kWh)
B. Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit
C. Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh)
D. Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
