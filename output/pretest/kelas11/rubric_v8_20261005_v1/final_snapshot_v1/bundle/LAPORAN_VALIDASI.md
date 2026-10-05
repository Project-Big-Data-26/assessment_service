# Validasi ulang soal kelas 11 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-sma11-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sma11-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 11 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 11, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 22; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 17, "knowing": 5, "reasoning": 0}, "knowledgeDimension": {"conceptual": 14, "procedural": 6, "factual": 2, "metacognitive": 0}, "intendedDifficulty": {"Easy": 18, "Medium": 4, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 4, "applying": 16, "reasoning": 0}, "knowledgeDimension": {"conceptual": 13, "procedural": 5, "factual": 2, "metacognitive": 0}, "intendedDifficulty": {"Easy": 16, "Medium": 4, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"needs_ai_review": 2, "silver_ready": 20}`.
Run awal sukses: 66/66; adjudikasi: 11; token sukses tercatat: 265,692.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 18 | 16 | [Easy.json](difficulty/Easy.json) |
| Medium | 4 | 4 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 11, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 11, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 11.

## 1. Soal `6e23a873d17dbf71c29d8901`

Berdasarkan data, pada tahun 2001 perusahaan A mampu menjual 9 laptop. Pada tahun 2002 dan 2003 perusahaan A mampu menjual masing-masing 27 dan 81 laptop. Apabila relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial, berapa penjualan laptop pada tahun 2007?

| Opsi | Isi |
|---|---|
| A | 6.561 laptop (3^8) |
| B | 2.187 (3^7) |
| C | 486 (9, 27, 81, ... ditambah 81 tiap tahun sampai 2007) |
| D | 19.683 (3^9) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `6.561`.
Solusi minimum hasil AI: Pola penjualan adalah fungsi eksponensial f(t) = 3^(t-1999). Untuk tahun 2001 (t=2001), f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6.561.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `42c6974648d5ca3ec9970c56b81ce45e10092f433342b9cd913515599c6316b9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2873 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2944 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2925 |

Run 1 — solusi: Pola penjualan adalah fungsi eksponensial f(t) = 3^(t-1999). Untuk tahun 2001 (t=2001), f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6.561.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola eksponensial dari data yang diberikan (9, 27, 81) dan menerapkan model tersebut untuk memprediksi nilai pada tahun tertentu. Ini melibatkan pemilihan prosedur yang tepat (pemodelan eksponensial) dan menerapkannya pada konteks soal.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial; berapa penjualan laptop pada tahun 2007
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip fungsi eksponensial dan bagaimana menerapkannya untuk memodelkan pertumbuhan data.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena pola eksponensial (3^n) sangat jelas terlihat dari data yang diberikan. Siswa hanya perlu mengenali pola tersebut dan melanjutkan deretnya atau menggunakan rumus fungsi sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 9 laptop; 27 dan 81 laptop; fungsi eksponensial; tahun 2007

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi eksponensial dan pola bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengenali pola eksponensial sederhana dari data yang diberikan adalah tugas rutin yang sesuai dengan tingkat kemampuan dasar. |

Run 2 — solusi: Pola penjualan adalah fungsi eksponensial f(t) = 3^(t-1999). Untuk tahun 2001, f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2002, f(2002) = 3^3 = 27. Untuk tahun 2003, f(2003) = 3^4 = 81. Maka untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6561.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan dan menerapkan model tersebut untuk memprediksi nilai pada tahun tertentu. Ini melibatkan penerapan konsep fungsi eksponensial pada konteks rutin.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial; berapa penjualan laptop pada tahun 2007?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip fungsi eksponensial dan bagaimana memodelkan data ke dalam bentuk fungsi tersebut.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena pola eksponensial (basis 3) sangat jelas terlihat dari data yang diberikan (9, 27, 81). Siswa hanya perlu melanjutkan pola tersebut atau menentukan rumus fungsi sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: 2001 mampu menjual 9 laptop; 2002 dan 2003 mampu menjual masing-masing 27 dan 81 laptop; berapa penjualan laptop pada tahun 2007?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang barisan geometri atau fungsi eksponensial sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi eksponensial adalah bagian dari kurikulum kelas 11. Soal ini merupakan aplikasi langsung dari konsep tersebut dengan data yang sangat terstruktur, sehingga beban kognitifnya rendah bagi siswa kelas 11. |

Run 3 — solusi: Pola penjualan mengikuti fungsi eksponensial f(t) = 3^(t-1999). Untuk tahun 2001, f(2001) = 3^(2001-1999) = 3^2 = 9. Untuk tahun 2002, f(2002) = 3^3 = 27. Untuk tahun 2003, f(2003) = 3^4 = 81. Maka untuk tahun 2007, f(2007) = 3^(2007-1999) = 3^8 = 6.561.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola pertumbuhan eksponensial dari data yang diberikan (9, 27, 81) dan menerapkan model tersebut untuk memprediksi nilai pada tahun tertentu. Ini melibatkan pemilihan model yang tepat dan penerapan prosedur perhitungan eksponensial.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial; berapa penjualan laptop pada tahun 2007
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep fungsi eksponensial sebagai model pertumbuhan, yang merupakan bagian dari pengetahuan konseptual dalam matematika.. Bukti: relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena pola pertumbuhan eksponensial (basis 3) sangat jelas terlihat dari data yang diberikan. Siswa hanya perlu mengenali pola tersebut dan melanjutkan deret eksponensialnya. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi non-rutin.. Bukti: 2001 mampu menjual 9 laptop; 2002 dan 2003 mampu menjual masing-masing 27 dan 81 laptop; berapa penjualan laptop pada tahun 2007

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi eksponensial dan pola bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengenali pola eksponensial sederhana dari data diskrit adalah tugas rutin yang sesuai dengan tingkat kemampuan siswa. |

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
Soal: Berdasarkan data, pada tahun 2001 perusahaan A mampu menjual 9 laptop. Pada tahun 2002 dan 2003 perusahaan A mampu menjual masing-masing 27 dan 81 laptop. Apabila relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial, berapa penjualan laptop pada tahun 2007?
Pilihan: A. 6.561 laptop (3^8)
B. 2.187 (3^7)
C. 486 (9, 27, 81, ... ditambah 81 tiap tahun sampai 2007)
D. 19.683 (3^9)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `needs_ai_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `84e4a0b4e7fdc64998b248b3`

Satuan energi adalah Joule dan kalori dengan 1 J = 2,4 kal. Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, merupakan fungsi karena setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori |
| B | Tidak, karena rumus 1 J = 2,4 kal hanya berlaku untuk bilangan bulat |
| C | Tidak, karena satu nilai Joule dapat menghasilkan lebih dari satu nilai kalori |
| D | Ya, tetapi hanya berlaku jika satuannya diubah ke kalori terlebih dahulu |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Hubungan antara Joule (J) dan kalori (kal) dapat dinyatakan sebagai fungsi f(x) = 2,4x, di mana x adalah nilai dalam Joule. Karena setiap nilai x (Joule) memiliki tepat satu pasangan nilai f(x) (kalori), maka hubungan tersebut memenuhi definisi fungsi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `976c6fc30e70cd29ab687bb86aa47ea1f31cbd9d6b8b45e609dbbe9df42ce73a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2639 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2669 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2621 |

Run 1 — solusi: Hubungan antara Joule (J) dan kalori (kal) dapat dinyatakan sebagai fungsi f(x) = 2,4x, di mana x adalah nilai dalam Joule. Karena setiap nilai x (Joule) memiliki tepat satu pasangan nilai f(x) (kalori), maka hubungan tersebut memenuhi definisi fungsi.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi apakah relasi konversi satuan memenuhi definisi formal fungsi (setiap input memiliki tepat satu output). Ini memerlukan pemahaman konseptual tentang definisi fungsi.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dasar fungsi sebagai relasi yang memetakan setiap elemen domain ke tepat satu elemen kodomain.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menerapkan definisi fungsi pada relasi linear sederhana. Tidak ada langkah kompleks atau kendala yang saling berinteraksi.. Bukti: 1 J = 2,4 kal; Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi (relasi satu-ke-satu atau banyak-ke-satu). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 11, menguji pemahaman konsep fungsi yang seharusnya sudah dikuasai sejak kelas 10. |

Run 2 — solusi: Hubungan antara Joule (J) dan kalori (kal) dapat dinyatakan sebagai fungsi f(x) = 2,4x, di mana x adalah nilai dalam Joule. Karena setiap nilai x (Joule) menghasilkan tepat satu nilai y (kalori), maka hubungan ini memenuhi definisi fungsi.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerapkan definisi formal fungsi (setiap input memiliki tepat satu output) pada konteks konversi satuan linear. Ini memerlukan pemahaman konseptual tentang relasi fungsi.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar atau definisi fungsi sebagai relasi yang memetakan setiap elemen domain ke tepat satu elemen kodomain.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali bahwa konversi satuan linear (y = 2,4x) adalah fungsi karena setiap input memiliki output tunggal. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: 1 J = 2,4 kal; Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi (relasi satu-ke-satu atau banyak-ke-satu, bukan satu-ke-banyak). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep fungsi adalah materi dasar kelas 11. Soal ini menguji pemahaman definisi tanpa komplikasi tambahan, sehingga tergolong mudah bagi siswa SMA. |

Run 3 — solusi: Hubungan antara Joule (J) dan kalori (kal) dapat dinyatakan sebagai fungsi f(x) = 2,4x, di mana x adalah nilai dalam Joule. Karena setiap nilai x (Joule) menghasilkan tepat satu nilai f(x) (kalori), maka hubungan tersebut memenuhi definisi fungsi.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi apakah relasi konversi satuan memenuhi definisi formal fungsi. Ini memerlukan pemahaman konseptual tentang syarat pemetaan satu-ke-satu (setiap input memiliki tepat satu output).. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi konseptual fungsi sebagai relasi yang memetakan setiap elemen domain ke tepat satu elemen kodomain.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman dasar definisi fungsi tanpa memerlukan perhitungan kompleks atau perencanaan strategi yang rumit.. Bukti: Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar fungsi (pemetaan satu-ke-satu). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan sudah memahami definisi fungsi sebagai konsep dasar yang mendasari materi fungsi komposisi dan invers. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4076`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menguji pemahaman dasar tentang definisi fungsi. Siswa hanya perlu mengenali bahwa relasi konversi satuan linear memenuhi syarat pemetaan setiap elemen domain ke tepat satu elemen kodomain.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual mengenai definisi fungsi sebagai relasi yang memetakan setiap elemen domain ke tepat satu elemen kodomain.
- Intended difficulty `Easy`: Soal ini bersifat sangat langsung dan mendasar. Siswa hanya perlu menerapkan definisi fungsi pada relasi linear sederhana. Tidak ada langkah kompleks, kendala yang berinteraksi, atau kebutuhan untuk perencanaan strategi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar fungsi (pemetaan setiap input ke tepat satu output). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep fungsi adalah materi dasar yang sudah dipelajari di kelas 10 dan menjadi prasyarat untuk materi kelas 11. Soal ini tidak memiliki kompleksitas tambahan. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7cd201d9709f4fa0f023270d3c10591802b16f820840aec8a4bbcca08c95ed24`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2712 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2694 |
| 3 | success | valid / verified | applying | procedural | Easy | 2658 |

Run 1 — solusi: (f o g)(3) = f(g(3)). Diketahui g(3) = 6, maka f(g(3)) = f(6). Diketahui f(6) = 13. Jadi, (f o g)(3) = 13.
- Domain kognitif `classify/knowing`: Soal meminta siswa menerapkan definisi komposisi fungsi f(g(x)) dengan nilai-nilai yang sudah diberikan secara eksplisit. Siswa hanya perlu mengenali notasi komposisi dan melakukan substitusi berjenjang yang sangat langsung.. Bukti: tentukan (f o g) (3)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep komposisi fungsi sebagai prosedur operasional (f(g(x))) untuk menyelesaikan masalah ini.. Bukti: f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menerapkan definisi (f o g)(x) = f(g(x)) dan melakukan substitusi nilai yang sudah tersedia. Tidak ada langkah perencanaan, integrasi konsep yang kompleks, atau kendala yang harus dipecahkan.. Bukti: Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi komposisi fungsi f(g(x)) |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini merupakan penerapan dasar dari materi komposisi fungsi yang sangat rutin dan tidak memerlukan penalaran tingkat lanjut. |

Run 2 — solusi: (f o g)(3) = f(g(3)). Diketahui g(3) = 6, maka f(g(3)) = f(6). Diketahui f(6) = 13. Jadi, (f o g)(3) = 13.
- Domain kognitif `classify/knowing`: Soal meminta siswa menerapkan definisi komposisi fungsi f(g(x)) dengan nilai yang sudah diberikan secara eksplisit. Siswa hanya perlu mengenali notasi komposisi dan melakukan substitusi dua langkah yang sangat langsung.. Bukti: tentukan (f o g) (3)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep komposisi fungsi (f o g)(x) = f(g(x)) sebagai prosedur untuk menyelesaikan masalah ini.. Bukti: f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menerapkan definisi komposisi fungsi f(g(3)) = f(6) = 13. Tidak ada kendala, tidak ada manipulasi aljabar, dan semua informasi yang diperlukan tersedia secara eksplisit.. Bukti: Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3).

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
| gradeRelativeRationale | Untuk kelas 11, soal ini adalah penerapan dasar dari definisi komposisi fungsi yang sudah dipelajari. Tidak ada tuntutan kognitif tinggi. |

Run 3 — solusi: (f o g)(3) = f(g(3)). Diketahui g(3) = 6, maka f(g(3)) = f(6). Diketahui f(6) = 13. Jadi, (f o g)(3) = 13.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan definisi komposisi fungsi f(g(x)) dengan nilai yang sudah diberikan secara eksplisit. Ini adalah penerapan prosedur langsung.. Bukti: tentukan (f o g) (3)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami definisi komposisi fungsi sebagai prosedur untuk menyelesaikan masalah.. Bukti: f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12; (f o g) (3)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu memahami notasi komposisi f(g(x)) dan melakukan substitusi nilai yang sudah tersedia. Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang harus diintegrasikan.. Bukti: Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3).

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
| gradeRelativeRationale | Untuk kelas 11, ini adalah soal dasar mengenai komposisi fungsi yang tidak memerlukan manipulasi aljabar atau analisis domain/range. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4311`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal meminta siswa menerapkan definisi komposisi fungsi f(g(x)) dengan nilai-nilai yang sudah diberikan secara eksplisit. Siswa hanya perlu mengenali notasi komposisi dan melakukan substitusi berjenjang yang sangat langsung.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami konsep komposisi fungsi sebagai prosedur operasional (f(g(x))) untuk menyelesaikan masalah ini.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu menerapkan definisi (f o g)(x) = f(g(x)) dan melakukan substitusi nilai yang sudah tersedia. Tidak ada langkah perencanaan, integrasi konsep yang kompleks, atau kendala yang harus dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi komposisi fungsi f(g(x)) |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini merupakan penerapan dasar dari materi komposisi fungsi yang sangat rutin dan tidak memerlukan penalaran tingkat lanjut. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `f69622cd0a44a030d0eca055`

Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan<br><br>f (3) × g(3)

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 42 |
| C | 1 |
| D | 78 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Diketahui f(3) = 7 dan g(3) = 6. Maka f(3) × g(3) = 7 × 6 = 42.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6696b19f1f7abcaa62ebbd7a89c7fff5846a9143f44edc8e84699a566f8b89dd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3230 |
| 2 | success | valid / verified | knowing | factual | Easy | 2642 |
| 3 | success | valid / verified | knowing | factual | Easy | 3569 |

Run 1 — solusi: Diketahui f(3) = 7 dan g(3) = 6. Maka f(3) × g(3) = 7 × 6 = 42.
- Domain kognitif `classify/knowing`: Soal hanya meminta operasi perkalian langsung dari nilai fungsi yang sudah diberikan secara eksplisit. Tidak ada proses komposisi atau penalaran kompleks yang diperlukan.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)
- Dimensi pengetahuan `classify/factual`: Siswa hanya perlu mengenali nilai fungsi yang diberikan dan melakukan operasi aritmatika dasar.. Bukti: f (3) = 7, g (3) = 6
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengambil nilai yang sudah tersedia dan mengalikannya. Tidak ada langkah perantara atau strategi yang perlu dipilih.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian dasar dan pemahaman notasi fungsi f(x). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar substitusi nilai ke dalam operasi aritmatika, sangat mudah bagi siswa kelas 11. |

Run 2 — solusi: Diketahui f(3) = 7 dan g(3) = 6. Maka f(3) × g(3) = 7 × 6 = 42.
- Domain kognitif `classify/knowing`: Soal hanya meminta operasi perkalian sederhana dari nilai fungsi yang sudah diberikan secara eksplisit. Siswa hanya perlu mengenali nilai yang relevan dan melakukan operasi aritmatika dasar.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman faktual mengenai notasi fungsi dan operasi aritmatika dasar pada nilai fungsi tersebut.. Bukti: f (3) = 7, g (3) = 6; f (3) × g(3)
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengambil nilai yang diberikan dan mengalikannya. Tidak ada langkah perencanaan, integrasi konsep, atau kendala yang harus dipecahkan.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar notasi fungsi f(x) dan operasi perkalian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini terlalu sederhana karena hanya melibatkan substitusi langsung tanpa manipulasi aljabar atau pemahaman konsep fungsi yang mendalam. |

Run 3 — solusi: Diketahui f(3) = 7 dan g(3) = 6. Maka f(3) × g(3) = 7 × 6 = 42.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nilai fungsi yang diberikan dan melakukan operasi perkalian dasar tanpa perlu melakukan manipulasi aljabar atau penalaran kompleks.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman dasar tentang notasi fungsi dan penerapan operasi aritmatika pada nilai yang diketahui.. Bukti: f (3) = 7, g (3) = 6
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengambil nilai yang sudah tersedia dan mengalikannya. Tidak ada langkah perencanaan, integrasi konsep, atau kendala yang harus dipecahkan.. Bukti: f (3) = 7, g (3) = 6; tentukan f (3) × g(3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi fungsi f(x) dan operasi perkalian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini adalah prosedur yang sangat mendasar dan familiar, tidak memerlukan penalaran tingkat tinggi atau perencanaan strategi. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `f2de3a4198c1c8c13c51a92a`

Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).

| Opsi | Isi |
|---|---|
| A | b = 3, f^-1(x) = (x - 3)/2 |
| B | b = 6, f^-1(x) = (x - 6)/2 |
| C | b = 2, f^-1(x) = (x + 2)/2 |
| D | b = 2, f^-1(x) = (x - 2)/2 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `b = 2, f^-1(x) = (x - 2)/2`.
Solusi minimum hasil AI: f(f(x)) = 2(2x + b) + b = 4x + 3b. Diketahui 4x + 3b = 4x + 6, maka 3b = 6, sehingga b = 2. Fungsi menjadi f(x) = 2x + 2. Untuk invers, y = 2x + 2, maka 2x = y - 2, sehingga f^-1(x) = (x - 2)/2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b5931028b6d9767ddeeebb9bc3a95323b72b82be6b63ea88766db4e977537a24`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2889 |
| 2 | success | valid / verified | applying | procedural | Medium | 2919 |
| 3 | success | valid / verified | applying | procedural | Medium | 2916 |

Run 1 — solusi: f(f(x)) = 2(2x + b) + b = 4x + 3b. Diketahui 4x + 3b = 4x + 6, maka 3b = 6, sehingga b = 2. Fungsi menjadi f(x) = 2x + 2. Untuk invers, y = 2x + 2, maka 2x = y - 2, sehingga f^-1(x) = (x - 2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur komposisi fungsi dan invers secara berurutan. Langkah-langkahnya bersifat rutin dan terstruktur, tidak memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6; Tentukan nilai b dan f-1 (x)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara melakukan komposisi fungsi dan menentukan invers fungsi linear.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap yang saling bergantung: menentukan parameter b melalui komposisi fungsi, kemudian menentukan invers. Meskipun prosedurnya familiar, siswa harus melakukan substitusi dan penyelesaian persamaan linear dengan cermat.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar fungsi linear, komposisi fungsi, dan invers fungsi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu melakukan komposisi fungsi linear dan inversnya. Soal ini menuntut ketelitian dalam aljabar tanpa kerumitan konseptual yang tinggi. |

Run 2 — solusi: f(f(x)) = 2(2x + b) + b = 4x + 3b. Diketahui f(f(x)) = 4x + 6, maka 3b = 6, sehingga b = 2. Fungsi menjadi f(x) = 2x + 2. Untuk mencari invers, y = 2x + 2 => 2x = y - 2 => x = (y - 2)/2. Jadi, f^-1(x) = (x - 2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur komposisi fungsi dan invers secara berurutan. Langkah-langkahnya rutin namun memerlukan pemahaman konseptual tentang bagaimana parameter b berinteraksi dalam komposisi fungsi.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6; Tentukan nilai b dan f-1 (x)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang komposisi fungsi dan algoritma mencari invers fungsi linear.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua tahap yang saling bergantung: menentukan parameter b melalui komposisi fungsi, kemudian menentukan invers. Meskipun prosedurnya familiar, siswa harus mengintegrasikan dua konsep tersebut tanpa bantuan langkah perantara.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6; Tentukan nilai b dan f-1 (x)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep komposisi fungsi linear dan invers fungsi linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu melakukan komposisi fungsi dan invers. Soal ini menuntut ketelitian dalam aljabar komposisi (2b+b=3b) yang sering menjadi jebakan, namun secara konseptual masih dalam cakupan rutin. |

Run 3 — solusi: f(f(x)) = 2(2x+b)+b = 4x+3b. Diketahui f(f(x)) = 4x+6, maka 3b = 6, sehingga b = 2. Fungsi menjadi f(x) = 2x+2. Untuk mencari invers, y = 2x+2 => 2x = y-2 => x = (y-2)/2. Jadi, f^-1(x) = (x-2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur komposisi fungsi dan invers secara berurutan. Langkah-langkahnya bersifat rutin dan terstruktur, namun memerlukan pemahaman konseptual tentang bagaimana parameter 'b' berinteraksi dalam komposisi fungsi.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6; Tentukan nilai b dan f-1 (x)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritme komposisi fungsi dan teknik mencari invers fungsi linear.. Bukti: f (f (x)) = 4x + 6; f-1 (x)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah yang saling bergantung: menentukan parameter fungsi melalui komposisi, kemudian mencari invers. Siswa harus melakukan substitusi aljabar yang tepat dan memahami hubungan antara fungsi dan inversnya. Tidak ada langkah non-rutin, namun integrasi antara komposisi dan invers memerlukan ketelitian.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6; Tentukan nilai b dan f-1 (x)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar komposisi fungsi linear dan konsep fungsi invers. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 SMA karena menguji penguasaan materi fungsi komposisi dan invers yang merupakan standar kurikulum. |

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
Soal: Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).
Pilihan: A. b = 3, f^-1(x) = (x - 3)/2
B. b = 6, f^-1(x) = (x - 6)/2
C. b = 2, f^-1(x) = (x + 2)/2
D. b = 2, f^-1(x) = (x - 2)/2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `7b396c45f8b99915cc10dc7b`

Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

| Opsi | Isi |
|---|---|
| A | f^-1(x) = x^2 - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |
| B | f^-1(x) = x^2 + 3, domain: semua bilangan riil, range: semua bilangan riil |
| C | f^-1(x) = x^2 + 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |
| D | f^-1(x) = akar(x) - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: f(x) = sqrt(x-3). Domain f: x >= 3, Range f: y >= 0. Let y = sqrt(x-3). y^2 = x-3 => x = y^2 + 3. Swap variables: f^-1(x) = x^2 + 3. Domain f^-1 = Range f = {x \| x >= 0}. Range f^-1 = Domain f = {y \| y >= 3}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a0f6eb3f01ed28702acd209077ba3318a23260abfbc63f6547186fee68ce2113`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2893 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2874 |
| 3 | success | valid / verified | applying | procedural | Medium | 2825 |

Run 1 — solusi: f(x) = sqrt(x-3). Domain f: x >= 3, Range f: y >= 0. Let y = sqrt(x-3). y^2 = x-3 => x = y^2 + 3. Swap variables: f^-1(x) = x^2 + 3. Domain f^-1 = Range f = {x \| x >= 0}. Range f^-1 = Domain f = {y \| y >= 3}.
- Domain kognitif `classify/applying`: Siswa diminta menentukan invers fungsi akar dan menentukan domain serta range-nya. Ini memerlukan pemahaman konseptual tentang hubungan domain-range antara fungsi dan inversnya, serta prosedur aljabar untuk mencari invers.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman prosedural dalam mencari invers fungsi dan pemahaman konseptual tentang pembatasan domain dan range yang diperlukan agar fungsi invers terdefinisi dengan benar.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya familiar (mengubah y=f(x) menjadi x=f(y)), siswa harus secara eksplisit memperhatikan pembatasan domain dan range yang merupakan syarat mutlak fungsi invers, yang sering menjadi jebakan bagi siswa.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi, domain, range, dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu melakukan manipulasi aljabar dan memahami konsep invers. Kesulitan terletak pada ketelitian menentukan domain dan range, bukan pada kompleksitas aljabar. |

Run 2 — solusi: y = sqrt(x - 3) => y^2 = x - 3 => x = y^2 + 3. Tukar variabel: f^-1(x) = x^2 + 3. Domain f adalah [3, infinity), maka range f^-1 adalah [3, infinity). Range f adalah [0, infinity), maka domain f^-1 adalah [0, infinity). Jadi, f^-1(x) = x^2 + 3, domain x >= 0, range y >= 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aljabar untuk mencari invers fungsi dan memahami konsep hubungan domain-range antara fungsi asli dan inversnya. Ini adalah penerapan konsep rutin dalam konteks fungsi.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prosedur mencari invers fungsi dan hubungan konseptual antara domain dan range fungsi asli dengan inversnya.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya familiar, siswa harus melakukan integrasi antara manipulasi aljabar dan analisis batasan domain/range yang sering terlewatkan. Siswa tidak hanya mencari rumus invers, tetapi harus membatasi domain invers berdasarkan range fungsi asal.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi, domain, range, dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menentukan invers fungsi akar dan memahami pembatasan domain/range yang diperlukan. Kesalahan umum pada distractor menunjukkan tingkat kesulitan yang sesuai untuk menguji pemahaman konsep secara mendalam. |

Run 3 — solusi: y = sqrt(x - 3) => y^2 = x - 3 => x = y^2 + 3. Tukar variabel: f^-1(x) = x^2 + 3. Domain f(x) adalah [3, infinity), maka range f^-1(x) adalah [3, infinity). Range f(x) adalah [0, infinity), maka domain f^-1(x) adalah [0, infinity).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aljabar untuk mencari invers dan memahami konsep hubungan domain-range antara fungsi asli dan inversnya.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman prosedural dalam memanipulasi aljabar untuk invers dan pemahaman konseptual tentang batasan domain dan range.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya melakukan manipulasi aljabar rutin, tetapi juga harus secara sadar membatasi domain dan range invers berdasarkan fungsi aslinya, yang merupakan langkah krusial dalam fungsi invers.. Bukti: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar fungsi, domain, range, dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menentukan invers fungsi akar dan memahami pembatasan domain/range sebagai syarat fungsi invers. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5749`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur aljabar untuk mencari invers dan mengintegrasikan pemahaman tentang hubungan domain-range antara fungsi asli dan inversnya.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang pembatasan domain dan range yang diperlukan agar fungsi invers terdefinisi dengan benar, bukan sekadar manipulasi aljabar.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus memperhatikan pembatasan domain dan range yang merupakan syarat mutlak fungsi invers. Distraktor yang ada dirancang untuk menjebak siswa yang hanya melakukan manipulasi aljabar tanpa memperhatikan batasan domain/range.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi, domain, range, dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu melakukan manipulasi aljabar dan memahami konsep invers. Kesulitan terletak pada ketelitian menentukan domain dan range, bukan pada kompleksitas aljabar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d590344d18abe3ebd38fb8ed`

Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.<br><br>\|Waktu (Detik)\|0\|1\|2\|3\|4\|5\|6\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Jarak (m)\|0\|5\|8\|9\|8\|5\|0\|<br><br>Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.

| Opsi | Isi |
|---|---|
| A | Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi. |
| B | Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi. |
| C | Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi. |
| D | Tidak dapat ditentukan tanpa menggambar grafiknya. |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai maksimum 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak (maksimum) pada grafik fungsi kuadrat. Karena fungsi memiliki titik maksimum, maka parabola terbuka ke bawah (koefisien a < 0).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6adddb15508b0c5e605cddcf694390faba9301ea595e92526a743f7430a839b6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2826 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2821 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2808 |

Run 1 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai maksimum 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak (maksimum) pada grafik fungsi kuadrat. Karena fungsi memiliki titik maksimum, maka parabola terbuka ke bawah (koefisien a < 0).
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menafsirkan pola numerik dalam tabel dan menghubungkannya dengan sifat geometris fungsi kuadrat (arah bukaan parabola). Ini memerlukan pemahaman konseptual tentang hubungan antara titik puncak dan arah bukaan parabola, bukan sekadar menghitung.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.
- Dimensi pengetahuan `classify/conceptual`: Siswa harus menggunakan pengetahuan konseptual tentang bentuk parabola dan bagaimana titik balik (maksimum/minimum) menentukan arah bukaan fungsi kuadrat berdasarkan data yang diberikan.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengenali pola naik-turun sederhana dari data yang diberikan untuk menyimpulkan arah bukaan parabola. Tidak ada perhitungan kompleks atau manipulasi aljabar yang diperlukan; hanya pemahaman dasar tentang sifat fungsi kuadrat.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk grafik fungsi kuadrat dan hubungan titik puncak dengan arah bukaan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menginterpretasikan data tabel sederhana untuk fungsi kuadrat tanpa harus menggambar grafik secara manual. |

Run 2 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai maksimum 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak (maksimum) pada t=3. Fungsi kuadrat dengan titik puncak maksimum memiliki koefisien a < 0, sehingga grafik terbuka ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan pola numerik dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan). Ini memerlukan pemahaman konseptual tentang hubungan antara titik puncak dan arah bukaan parabola, bukan sekadar menghitung.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jarak (m)\|0\|5\|8\|9\|8\|5\|0
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana karakteristik fungsi kuadrat (arah bukaan) tercermin dalam data tabel.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengenali pola naik-turun sederhana dari data yang diberikan untuk menentukan arah bukaan parabola. Tidak ada perhitungan kompleks atau perencanaan strategi yang rumit; hubungan antara data dan sifat fungsi bersifat langsung.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jarak (m)\|0\|5\|8\|9\|8\|5\|0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan titik puncak fungsi kuadrat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menginterpretasikan data tabel fungsi kuadrat secara langsung tanpa perlu menggambar grafik. |

Run 3 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) ke 9 (t=3) lalu menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak maksimum, yang berarti parabola terbuka ke bawah (koefisien a < 0).
- Domain kognitif `classify/applying`: Siswa diminta menginterpretasikan pola numerik dari tabel untuk menentukan sifat geometris fungsi kuadrat (arah bukaan). Ini memerlukan pemahaman konseptual tentang hubungan antara titik puncak dan arah bukaan parabola, bukan sekadar menghitung.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jarak (m)\|0\|5\|8\|9\|8\|5\|0
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang karakteristik fungsi kuadrat (arah bukaan) berdasarkan pola data, bukan sekadar menghafal prosedur aljabar.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena pola data sangat jelas (simetris dengan puncak di tengah). Siswa hanya perlu mengenali pola naik-turun sebagai indikator titik maksimum, yang merupakan konsep dasar fungsi kuadrat.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.; Jarak (m)\|0\|5\|8\|9\|8\|5\|0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan titik puncak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menginterpretasikan tabel data sederhana untuk menentukan sifat fungsi kuadrat tanpa bantuan grafik. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 x 12 = 144 |
| B | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| C | 12 |
| D | 12! = 479.001.600 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `479.001.600`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a10cddff9d76f7cbcc2341920d6e619947c604c8b58b37535bbb0c98d90bacd3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2712 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2781 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2886 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus faktorial untuk korespondensi satu-satu. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang prinsip dasar korespondensi satu-satu dan penggunaan notasi faktorial sebagai prosedur standar.. Bukti: banyak korespondensi satu-satu yang mungkin adalah n! = 12! = 479.001.600
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena langsung menanyakan penerapan rumus faktorial untuk korespondensi satu-satu. Tidak ada langkah integrasi atau perencanaan yang kompleks.. Bukti: n(A) = n(B) = 12

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
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah materi dasar yang familiar bagi siswa kelas 11. Soal tidak menuntut analisis lebih lanjut. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu antara dua himpunan dengan jumlah anggota yang sama. Siswa hanya perlu mengenali konsep dasar korespondensi satu-satu dan menerapkan rumus n!.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap prinsip dasar korespondensi satu-satu (konsep) dan penggunaan rumus faktorial (prosedural) untuk menyelesaikan masalah kombinatorik sederhana.. Bukti: banyak korespondensi satu-satu yang mungkin adalah n! = 12! = 479.001.600
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengetahui rumus n! untuk korespondensi satu-satu. Tidak ada langkah integrasi yang kompleks atau kendala yang berinteraksi. Meskipun angka 12! cukup besar, prosedur penyelesaiannya sangat standar dan familiar bagi siswa kelas 11.. Bukti: n(A) = n(B) = 12

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
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah materi dasar yang familiar di kelas 11. Soal tidak menuntut penalaran mendalam, hanya pengingatan rumus. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × ... × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan rumus faktorial untuk menghitung banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama. Siswa hanya perlu mengenali konsep dasar korespondensi satu-satu dan menerapkan prosedur perhitungan faktorial.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar korespondensi satu-satu (bijeksi) dan prosedur faktorial sebagai metode penghitungan yang tepat untuk kasus tersebut.. Bukti: n(A) = n(B) = 12; banyak korespondensi satu-satu yang mungkin
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) karena hanya menanyakan penerapan rumus faktorial untuk n=12. Tidak ada langkah integrasi, kendala yang berinteraksi, atau perencanaan strategi yang kompleks. Siswa hanya perlu mengetahui bahwa korespondensi satu-satu untuk himpunan dengan n elemen adalah n!.. Bukti: n(A) = n(B) = 12; ada berapa banyak korespondensi satu-satu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar himpunan, korespondensi satu-satu, dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah materi dasar yang familiar bagi siswa kelas 11. Soal ini tidak memerlukan pemecahan masalah yang kompleks, hanya pengingatan rumus. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4623`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang prinsip dasar korespondensi satu-satu (konsep) dan penggunaan notasi faktorial sebagai prosedur standar untuk menghitung permutasi/bijeksi.
- Intended difficulty `Easy`: Soal bersifat rutin dan langsung. Siswa hanya perlu mengetahui rumus n! untuk korespondensi satu-satu. Tidak ada langkah integrasi yang kompleks atau kendala yang berinteraksi. Prosedur penyelesaiannya sangat standar dan familiar bagi siswa kelas 11.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Materi korespondensi satu-satu dan faktorial adalah materi dasar yang familiar di kelas 11. Soal tidak menuntut penalaran mendalam, hanya pengingatan rumus. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `needs_ai_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Diameter AB = 2 * jari-jari = 2 * 8,5 cm = 17 cm. Karena AB adalah diameter, maka ∠ACB = 90° (Teorema Thales). Dengan Teorema Pythagoras pada ΔABC: BC = √(AB² - AC²) = √(17² - 8²) = √(289 - 64) = √225 = 15 cm.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0074-05.png. Transkripsi visual: Sebuah lingkaran dengan titik pusat. Garis AB adalah diameter lingkaran yang melewati titik pusat. Titik C berada pada keliling lingkaran. Segitiga ABC terbentuk dengan sisi AC dan BC sebagai tali busur, dan AB sebagai diameter. Sudut ACB adalah sudut keliling yang menghadap diameter.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `657e3ba2efae1ac78ec28845e1b432212e4b06b47fc5e9bd6f6658fd9edb039e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3922 |
| 2 | success | valid / verified | applying | procedural | Easy | 3886 |
| 3 | success | valid / verified | applying | procedural | Easy | 3935 |

Run 1 — solusi: Diameter AB = 2 * jari-jari = 2 * 8,5 cm = 17 cm. Karena AB adalah diameter, segitiga ABC adalah segitiga siku-siku di C (Teorema Thales). Berdasarkan teorema Pythagoras: BC = akar(AB^2 - AC^2) = akar(17^2 - 8^2) = akar(289 - 64) = akar(225) = 15 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengenali sifat geometri lingkaran (diameter dan sudut keliling) untuk mengidentifikasi segitiga siku-siku, lalu menerapkan teorema Pythagoras. Ini adalah penerapan konsep rutin pada konteks geometri.. Bukti: AB adalah diameter pada lingkaran; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm; Tentukan: panjang BC
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara diameter lingkaran dan sudut keliling, serta prosedur algoritma Pythagoras.. Bukti: AB adalah diameter; Teorema Thales; teorema Pythagoras
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar dan familiar bagi siswa kelas 11. Siswa hanya perlu melakukan dua langkah rutin: menghitung diameter dari jari-jari dan menerapkan teorema Pythagoras pada segitiga siku-siku yang terbentuk.. Bukti: AB adalah diameter; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi diameter dan jari-jari, Teorema Thales (sudut keliling menghadap diameter adalah 90 derajat), dan Teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri lingkaran dan Pythagoras adalah prasyarat dasar yang sudah dikuasai siswa kelas 11. Tidak ada tuntutan integrasi kompleks atau strategi non-rutin. |

Run 2 — solusi: Diameter AB = 2 * r = 2 * 8,5 = 17 cm. Karena AB adalah diameter, sudut ACB = 90 derajat (Teorema Thales). Dengan teorema Pythagoras pada segitiga ABC: BC = akar(AB^2 - AC^2) = akar(17^2 - 8^2) = akar(289 - 64) = akar(225) = 15 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat geometris (sudut keliling menghadap diameter adalah 90 derajat) dan menerapkan teorema Pythagoras untuk menyelesaikan masalah. Ini adalah penerapan konsep rutin dalam konteks geometri.. Bukti: AB adalah diameter pada lingkaran berikut; Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm; Tentukan: panjang BC
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara diameter, sudut keliling, dan teorema Pythagoras (prosedur) serta konsep dasar lingkaran (konseptual).. Bukti: AB adalah diameter; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan prosedur standar (Teorema Thales dan Pythagoras) yang familiar bagi siswa kelas 11. Langkah-langkahnya jelas dan tidak memerlukan strategi non-rutin.. Bukti: AB adalah diameter; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat sudut keliling yang menghadap diameter. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan Pythagoras adalah prasyarat dasar yang sudah dikuasai siswa kelas 11. Soal ini merupakan penerapan langsung tanpa kompleksitas tambahan. |

Run 3 — solusi: Diameter AB = 2 * jari-jari = 2 * 8,5 = 17 cm. Karena AB adalah diameter, segitiga ABC adalah segitiga siku-siku di C (Teorema Thales). Dengan teorema Pythagoras, BC = akar(AB^2 - AC^2) = akar(17^2 - 8^2) = akar(289 - 64) = akar(225) = 15 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengenali sifat geometri lingkaran (diameter dan sudut keliling) untuk menentukan bahwa segitiga ABC adalah segitiga siku-siku, kemudian menerapkan teorema Pythagoras. Ini adalah penerapan konsep rutin pada konteks geometri.. Bukti: AB adalah diameter pada lingkaran; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm; Tentukan: panjang BC
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara diameter, sudut keliling, dan teorema Pythagoras (prosedur) dalam konteks geometri lingkaran (konseptual).. Bukti: AB adalah diameter; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm; panjang BC
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena jalur penyelesaiannya sangat jelas dan familiar bagi siswa kelas 11: menghitung diameter dari jari-jari, mengidentifikasi segitiga siku-siku, dan menggunakan teorema Pythagoras. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: AB adalah diameter; Jari-jari lingkaran 8,5 cm; panjang AC = 8 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat sudut keliling yang menghadap diameter. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan Pythagoras adalah prasyarat dasar yang sudah dikuasai siswa kelas 11. Langkah-langkah penyelesaian bersifat langsung dan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5673`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengintegrasikan sifat geometri lingkaran (sudut keliling menghadap diameter adalah 90 derajat) dengan prosedur aljabar (Teorema Pythagoras) untuk menyelesaikan masalah. Ini adalah penerapan konsep rutin dalam konteks geometri.
- Dimensi pengetahuan `conceptual`: Soal ini memerlukan pemahaman konseptual tentang sifat sudut keliling pada lingkaran dan prosedur algoritmik dari Teorema Pythagoras.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar dan familiar bagi siswa kelas 11. Siswa hanya perlu melakukan dua langkah rutin: menghitung diameter dari jari-jari dan menerapkan teorema Pythagoras pada segitiga siku-siku yang terbentuk.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi diameter dan jari-jari, Teorema Thales (sudut keliling menghadap diameter adalah 90 derajat), dan Teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri lingkaran dan Pythagoras adalah prasyarat dasar yang sudah dikuasai siswa kelas 11. Tidak ada tuntutan integrasi kompleks atau strategi non-rutin. |

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
Transkripsi visual: Sebuah lingkaran dengan titik pusat. Garis AB adalah diameter lingkaran yang melewati titik pusat. Titik C berada pada keliling lingkaran. Segitiga ABC terbentuk dengan sisi AC dan BC sebagai tali busur, dan AB sebagai diameter. Sudut ACB adalah sudut keliling yang menghadap diameter.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `f6239979bb0b323db2b28a03`

Jika `∠` BOC = 90`◦` , berapakah besar `∠` BEC ?

| Opsi | Isi |
|---|---|
| A | 22,5° |
| B | 45° |
| C | 90° |
| D | 180° |

![Gambar sumber soal 10](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0074-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `45°`.
Solusi minimum hasil AI: Sudut BOC adalah sudut pusat yang menghadap busur BC. Sudut BEC adalah sudut keliling yang menghadap busur BC yang sama. Berdasarkan teorema sudut pusat dan sudut keliling, besar sudut keliling adalah setengah dari sudut pusat: ∠BEC = 1/2 × ∠BOC = 1/2 × 90° = 45°.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0074-01.png. Transkripsi visual: A circle with center O. Points B, C, and E lie on the circumference. Line segments OB and OC are radii, forming a central angle ∠BOC = 90° (indicated by a right-angle symbol). Line segments EB and EC are chords, forming an inscribed angle ∠BEC.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0ba141e847c0f285ba9461d9dc43df2324dd816662fe9b1d89d13924473c7da3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3852 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3850 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3840 |

Run 1 — solusi: Sudut BOC adalah sudut pusat yang menghadap busur BC, dan sudut BEC adalah sudut keliling yang menghadap busur BC yang sama. Berdasarkan teorema sudut pusat dan sudut keliling, besar sudut keliling adalah setengah dari sudut pusat: ∠BEC = 1/2 × ∠BOC = 1/2 × 90° = 45°.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk mengenali hubungan antara sudut pusat dan sudut keliling yang menghadap busur yang sama. Ini adalah penerapan langsung dari teorema geometri lingkaran yang sudah dipelajari, sehingga masuk dalam domain applying.. Bukti: ∠BOC = 90◦; berapakah besar ∠BEC ?; ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau teorema geometri (hubungan sudut pusat dan sudut keliling), yang merupakan pengetahuan konseptual.. Bukti: ∠BEC = 1/2 × ∠BOC
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu mengidentifikasi hubungan sudut pusat dan keliling yang menghadap busur yang sama, lalu melakukan satu operasi pembagian sederhana. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: ∠BOC = 90◦; berapakah besar ∠BEC ?

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
| gradeRelativeRationale | Materi geometri lingkaran adalah materi standar SMA kelas 11. Soal ini merupakan penerapan langsung teorema dasar tanpa modifikasi, sehingga tergolong mudah bagi siswa kelas 11. |

Run 2 — solusi: Sudut pusat BOC = 90°. Sudut keliling BEC menghadap busur yang sama dengan sudut pusat BOC. Berdasarkan teorema sudut pusat dan sudut keliling, besar sudut keliling adalah setengah dari sudut pusat yang menghadap busur yang sama. Maka, ∠BEC = 1/2 * ∠BOC = 1/2 * 90° = 45°.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali hubungan geometris antara sudut pusat dan sudut keliling yang menghadap busur yang sama. Prosedur yang digunakan adalah penerapan langsung teorema dasar lingkaran, yang merupakan materi rutin.. Bukti: ∠BOC = 90°; berapakah besar ∠BEC; ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau hubungan konseptual antara sudut pusat dan sudut keliling dalam lingkaran untuk menyelesaikan masalah ini.. Bukti: ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman dasar tentang teorema sudut pusat dan sudut keliling. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Jika ∠ BOC = 90◦ , berapakah besar ∠ BEC ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut pusat dan sudut keliling lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran merupakan bagian dari kurikulum SMA kelas 11. Soal ini adalah penerapan langsung teorema dasar yang familiar bagi siswa pada jenjang ini. |

Run 3 — solusi: Sudut pusat BOC = 90°. Sudut keliling BEC menghadap busur BC yang sama dengan sudut pusat BOC. Berdasarkan teorema sudut pusat dan sudut keliling, besar sudut keliling adalah setengah dari sudut pusat: ∠BEC = 1/2 × ∠BOC = 1/2 × 90° = 45°.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk mengenali hubungan geometris antara sudut pusat dan sudut keliling yang menghadap busur yang sama, kemudian menerapkan teorema tersebut secara langsung. Ini adalah prosedur standar yang familiar.. Bukti: ∠BOC = 90°; berapakah besar ∠BEC ?; ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau teorema hubungan sudut pusat dan sudut keliling pada lingkaran.. Bukti: ∠BEC adalah sudut keliling dan ∠BOC adalah sudut pusat yang menghadap busur BC yang sama
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu mengidentifikasi hubungan sudut pusat dan keliling yang sudah umum dipelajari. Tidak ada langkah tambahan atau integrasi konsep yang rumit.. Bukti: Jika ∠ BOC = 90◦ , berapakah besar ∠ BEC ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut pusat dan sudut keliling pada lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah bagian dari kurikulum SMA kelas 11. Soal ini menguji penerapan teorema dasar yang merupakan rutinitas familiar bagi siswa pada jenjang ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5396`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta siswa untuk mengenali hubungan geometris antara sudut pusat dan sudut keliling yang menghadap busur yang sama, kemudian menerapkan teorema tersebut secara langsung. Ini adalah penerapan prosedur standar yang familiar.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami prinsip atau teorema hubungan sudut pusat dan sudut keliling pada lingkaran untuk menyelesaikan masalah ini.
- Intended difficulty `Easy`: Soal ini bersifat langsung (straightforward). Siswa hanya perlu mengidentifikasi hubungan sudut pusat dan keliling yang sudah umum dipelajari. Tidak ada langkah tambahan atau integrasi konsep yang rumit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut pusat dan sudut keliling pada lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah bagian dari kurikulum SMA kelas 11. Soal ini menguji penerapan teorema dasar yang merupakan rutinitas familiar bagi siswa pada jenjang ini. |

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
Transkripsi visual: A circle with center O. Points B, C, and E lie on the circumference. Line segments OB and OC are radii, forming a central angle ∠BOC = 90° (indicated by a right-angle symbol). Line segments EB and EC are chords, forming an inscribed angle ∠BEC.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `838b526b72b79e514bd4fe62`

Pada gambar berikut, BD dan CD adalah garis singgung lingkaran A. Jika `∠` BAC = 147`◦` , tentukan besar `∠` BDC.

| Opsi | Isi |
|---|---|
| A | 33° |
| B | 57° |
| C | 147° |
| D | 90° |

![Gambar sumber soal 11](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0081-05.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `33°`.
Solusi minimum hasil AI: Karena BD dan CD adalah garis singgung, maka ∠ABD = 90° dan ∠ACD = 90°. Pada segiempat ABDC, jumlah sudut dalam adalah 360°. Maka ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0081-05.png. Transkripsi visual: Lingkaran berpusat di A. Titik B dan C terletak pada lingkaran. Garis BD dan CD adalah garis singgung lingkaran yang bertemu di titik D di luar lingkaran. Segmen AB dan AC adalah jari-jari. Sudut BAC (sudut pusat) diberikan sebesar 147 derajat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cd1048a8c23e9997d83d988597187640ee335daa01ed67423153584c11dcf9b1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3931 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3939 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3935 |

Run 1 — solusi: Karena BD dan CD adalah garis singgung, maka ∠ABD = 90° dan ∠ACD = 90°. Pada segiempat ABDC, jumlah sudut dalam adalah 360°. Maka ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat garis singgung (tegak lurus jari-jari) dan menerapkan konsep jumlah sudut dalam segiempat untuk menyelesaikan masalah. Ini adalah penerapan prosedur standar pada konteks geometri.. Bukti: BD dan CD adalah garis singgung lingkaran; ∠ABD = ∠ACD = 90°; jumlah sudut dalam segiempat adalah 360°
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat garis singgung lingkaran dan hubungan sudut dalam segiempat.. Bukti: BD dan CD adalah garis singgung lingkaran; jumlah sudut dalam segiempat adalah 360°
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena melibatkan prosedur standar yang familiar bagi siswa kelas 11. Langkah-langkah penyelesaiannya langsung: mengidentifikasi dua sudut siku-siku dari sifat garis singgung dan menggunakan jumlah sudut segiempat.. Bukti: BD dan CD adalah garis singgung lingkaran; ∠BAC = 147°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat garis singgung lingkaran (tegak lurus jari-jari) dan jumlah sudut dalam segiempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik standar SMA kelas 11. Prosedur yang diperlukan sangat rutin dan tidak memerlukan perencanaan strategis yang kompleks. |

Run 2 — solusi: Garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, maka ∠ABD = 90° dan ∠ACD = 90°. Pada segiempat ABDC, jumlah sudut dalam adalah 360°. Maka, ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat geometris bahwa garis singgung tegak lurus dengan jari-jari (konsep) dan menggunakan jumlah sudut dalam segiempat (prosedur) untuk menyelesaikan masalah. Ini adalah penerapan konsep rutin pada konteks geometri.. Bukti: BD dan CD adalah garis singgung lingkaran; ∠BAC = 147°; tentukan besar ∠BDC
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara garis singgung dan jari-jari lingkaran, serta penggunaan sifat sudut pada segiempat.. Bukti: BD dan CD adalah garis singgung lingkaran; ∠ABD = ∠ACD = 90°
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena melibatkan penerapan langsung sifat garis singgung (tegak lurus jari-jari) dan jumlah sudut segiempat. Langkah penyelesaiannya jelas, tidak memerlukan strategi nonrutin atau integrasi yang kompleks.. Bukti: BD dan CD adalah garis singgung lingkaran; ∠BAC = 147°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat garis singgung lingkaran dan jumlah sudut dalam segiempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi geometri lingkaran adalah standar kelas 11. Soal ini adalah aplikasi langsung dari teorema dasar yang sudah dipelajari. |

Run 3 — solusi: Sifat garis singgung lingkaran menyatakan bahwa jari-jari yang ditarik ke titik singgung tegak lurus dengan garis singgung. Maka, ∠ABD = 90° dan ∠ACD = 90°. Pada segiempat ABDC, jumlah sudut dalam adalah 360°. ∠BDC = 360° - (∠BAC + ∠ABD + ∠ACD) = 360° - (147° + 90° + 90°) = 360° - 327° = 33°.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat geometris garis singgung (tegak lurus jari-jari) dan konsep jumlah sudut dalam segiempat untuk menyelesaikan masalah. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦; tentukan besar ∠ BDC
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip geometris (sifat garis singgung dan jumlah sudut segiempat) yang merupakan pengetahuan konseptual.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan sifat geometris yang sangat standar dan familiar bagi siswa kelas 11. Jalur penyelesaiannya langsung (jumlah sudut segiempat) tanpa memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit.. Bukti: BD dan CD adalah garis singgung lingkaran A; ∠ BAC = 147◦

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat garis singgung lingkaran (jari-jari tegak lurus garis singgung) dan jumlah sudut dalam segiempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung merupakan topik standar. Prosedur yang diperlukan sangat langsung dan tidak menuntut penalaran tingkat tinggi. |

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
Transkripsi visual: Lingkaran berpusat di A. Titik B dan C terletak pada lingkaran. Garis BD dan CD adalah garis singgung lingkaran yang bertemu di titik D di luar lingkaran. Segmen AB dan AC adalah jari-jari. Sudut BAC (sudut pusat) diberikan sebesar 147 derajat.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Garis singgung PB tegak lurus dengan jari-jari AB di titik B, sehingga segitiga ABP adalah segitiga siku-siku dengan hipotenusa AP. Berdasarkan teorema Pythagoras: PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0081-03.png. Transkripsi visual: Lingkaran dengan pusat A. Titik B berada pada keliling lingkaran. Garis AB adalah jari-jari (berwarna merah). Garis lurus melalui B dan P adalah garis singgung lingkaran di titik B. Titik P berada di luar lingkaran. Jarak dari A ke P adalah garis lurus yang menghubungkan pusat lingkaran ke titik P.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `82b23fb2b06b86bc2da8edc551390956a8cb847fbdf6fc01726d1f2a2374225b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3885 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3906 |
| 3 | success | valid / verified | applying | procedural | Easy | 3912 |

Run 1 — solusi: Garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, sehingga segitiga ABP adalah segitiga siku-siku di B. Dengan teorema Pythagoras, PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengenali properti geometris bahwa garis singgung tegak lurus dengan jari-jari di titik singgung untuk membentuk segitiga siku-siku, kemudian menerapkan teorema Pythagoras. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B: PB = akar(PA^2 - AB^2)
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman prinsip geometris (hubungan garis singgung dan jari-jari) dan penggunaan algoritma teorema Pythagoras.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari teorema Pythagoras pada konfigurasi geometris standar (garis singgung lingkaran). Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: jari-jari lingkaran A adalah 7 cm; titik P berjarak 25 cm dari titik A; panjang garis singgung PB

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat garis singgung lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi garis singgung lingkaran adalah topik standar kelas 11. Soal ini tidak menuntut penalaran non-rutin atau integrasi konsep yang kompleks. |

Run 2 — solusi: Garis singgung PB tegak lurus dengan jari-jari AB di titik B, sehingga segitiga ABP adalah segitiga siku-siku dengan hipotenusa AP. Berdasarkan teorema Pythagoras: PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengenali sifat geometris bahwa garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung untuk membentuk segitiga siku-siku, kemudian menerapkan teorema Pythagoras. Ini adalah penerapan konsep rutin.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B: PB = akar(PA^2 - AB^2)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip geometris (garis singgung tegak lurus jari-jari) dan prosedur algoritmis (teorema Pythagoras).. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi hubungan siku-siku antara jari-jari dan garis singgung, lalu menghitung panjang sisi segitiga siku-siku menggunakan teorema Pythagoras. Tidak ada langkah kompleks atau integrasi konsep yang sulit.. Bukti: jari-jari lingkaran A adalah 7 cm; titik P berjarak 25 cm dari titik A; panjang garis singgung PB

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
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik standar SMA kelas 11. Soal ini merupakan aplikasi langsung dari teorema Pythagoras dalam konteks geometri lingkaran yang sangat familiar. |

Run 3 — solusi: Garis singgung PB tegak lurus dengan jari-jari AB di titik B, membentuk segitiga siku-siku ABP dengan hipotenusa AP. Menggunakan teorema Pythagoras: PB = akar(AP^2 - AB^2) = akar(25^2 - 7^2) = akar(625 - 49) = akar(576) = 24 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengenali sifat geometris bahwa garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, kemudian menerapkan teorema Pythagoras untuk menghitung panjang sisi segitiga siku-siku. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B: PB = akar(PA^2 - AB^2)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip geometris (hubungan garis singgung dan jari-jari) dan penggunaan algoritma teorema Pythagoras.. Bukti: PB tegak lurus AB (radius) karena PB garis singgung; segitiga ABP siku-siku di B
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah penyelesaiannya jelas: mengidentifikasi segitiga siku-siku dan menerapkan teorema Pythagoras. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: jari-jari lingkaran A adalah 7 cm; titik P berjarak 25 cm dari titik A; panjang garis singgung PB

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat dasar garis singgung lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik standar yang familiar. Soal ini langsung menguji penerapan teorema Pythagoras tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5610`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengenali properti geometris bahwa garis singgung tegak lurus dengan jari-jari di titik singgung untuk membentuk segitiga siku-siku, kemudian menerapkan teorema Pythagoras. Ini adalah penerapan prosedur standar pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman prinsip geometris (hubungan garis singgung dan jari-jari) dan penggunaan algoritma teorema Pythagoras.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi hubungan siku-siku antara jari-jari dan garis singgung, lalu menghitung panjang sisi segitiga siku-siku menggunakan teorema Pythagoras. Tidak ada langkah kompleks atau integrasi konsep yang sulit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan sifat dasar garis singgung lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan garis singgung adalah topik standar SMA kelas 11. Soal ini merupakan aplikasi langsung dari teorema Pythagoras dalam konteks geometri lingkaran yang sangat familiar. |

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
Transkripsi visual: Lingkaran dengan pusat A. Titik B berada pada keliling lingkaran. Garis AB adalah jari-jari (berwarna merah). Garis lurus melalui B dan P adalah garis singgung lingkaran di titik B. Titik P berada di luar lingkaran. Jarak dari A ke P adalah garis lurus yang menghubungkan pusat lingkaran ke titik P.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Karena A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Maka segitiga ABE memiliki panjang sisi AE = AB = BE = 3 cm, yang berarti segitiga ABE adalah segitiga sama sisi. Oleh karena itu, besar ∠BAE = 60°.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0089-05.png. Transkripsi visual: Lingkaran berpusat di A. Titik D, E, dan B terletak pada keliling lingkaran. Ruas garis AD, AE, dan AB adalah jari-jari lingkaran. Diberikan AD = 3 cm, maka AE = AB = 3 cm. Diberikan BE = AD = 3 cm. Segitiga ABE memiliki sisi-sisi AE = AB = BE = 3 cm.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `730c2f35f7b09a6023456dcc23a1d83af23ecfd8cc547c0ff0cb2c40bd564014`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3883 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3841 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3819 |

Run 1 — solusi: Karena A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Maka segitiga ABE memiliki panjang sisi AE = AB = BE = 3 cm, yang berarti segitiga ABE adalah segitiga sama sisi. Oleh karena itu, besar ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti jari-jari lingkaran dari gambar (AE=AB=AD) dan menghubungkannya dengan informasi yang diberikan (BE=AD) untuk menyimpulkan sifat segitiga sama sisi. Ini adalah penerapan konsep geometri dasar pada konteks lingkaran.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); karena BE=AD=3 cm juga, maka AE=AB=BE=3 cm dan segitiga ABE sama sisi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi jari-jari lingkaran dan sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); segitiga ABE sama sisi
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengenali properti dasar lingkaran (jari-jari sama panjang) dan sifat segitiga sama sisi. Langkah penyelesaian sangat langsung dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: AD = 3 cm dan BE = AD; A adalah pusat lingkaran

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
| gradeRelativeRationale | Materi lingkaran dan sifat segitiga adalah pengetahuan dasar yang sudah dikuasai di jenjang sebelumnya, sehingga untuk kelas 11 ini adalah soal rutin yang sederhana. |

Run 2 — solusi: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Karena AE = AB = BE = 3 cm, segitiga ABE adalah segitiga sama sisi. Maka, ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti jari-jari lingkaran untuk menentukan panjang sisi segitiga dan menyimpulkan jenis segitiga tersebut untuk mendapatkan besar sudut.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); karena BE=AD=3 cm juga, maka AE=AB=BE=3 cm dan segitiga ABE sama sisi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat jari-jari lingkaran dan klasifikasi segitiga berdasarkan panjang sisinya.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); segitiga ABE sama sisi, sehingga ∠BAE=60°
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengenali definisi jari-jari lingkaran dan sifat segitiga sama sisi. Langkah penyelesaiannya langsung dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: AD = 3 cm dan BE = AD; A adalah pusat lingkaran

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
| gradeRelativeRationale | Materi lingkaran dan sifat segitiga adalah dasar yang sudah dikuasai di jenjang sebelumnya, sehingga untuk kelas 11 ini adalah penerapan rutin. |

Run 3 — solusi: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Karena AE = AB = BE = 3 cm, segitiga ABE adalah segitiga sama sisi. Maka, ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti jari-jari lingkaran dari gambar dan menghubungkannya dengan informasi panjang sisi yang diberikan untuk mengenali segitiga sama sisi.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); karena BE=AD=3 cm juga, maka AE=AB=BE=3 cm dan segitiga ABE sama sisi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi jari-jari lingkaran dan sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); segitiga ABE sama sisi
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengenali properti dasar lingkaran (jari-jari sama panjang) dan sifat segitiga sama sisi. Langkah penyelesaian sangat langsung dan familiar bagi siswa kelas 11.. Bukti: AD = 3 cm dan BE = AD; A adalah pusat lingkaran

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari lingkaran dan sifat segitiga sama sisi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah topik standar SMA. Mengidentifikasi jari-jari dan sifat segitiga sama sisi adalah prosedur rutin yang diharapkan dikuasai siswa kelas 11. |

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
Transkripsi visual: Lingkaran berpusat di A. Titik D, E, dan B terletak pada keliling lingkaran. Ruas garis AD, AE, dan AB adalah jari-jari lingkaran. Diberikan AD = 3 cm, maka AE = AB = 3 cm. Diberikan BE = AD = 3 cm. Segitiga ABE memiliki sisi-sisi AE = AB = BE = 3 cm.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `b9acc681a7567cd1039ff751`

Lingkaran yang berpusat di titik O dan jari-jarinya 5 cm. Berapa panjang tali busurnya yang paling panjang?

| Opsi | Isi |
|---|---|
| A | 10 cm |
| B | 15 cm |
| C | 20 cm |
| D | 5 cm |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 x jari-jari = 2 x 5 cm = 10 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `85890c4aedd374202e64b9c8411f1c6a373b61106fc22d888d59264e7342d37c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2591 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2570 |
| 3 | success | valid / verified | knowing | factual | Easy | 3157 |

Run 1 — solusi: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 x jari-jari = 2 x 5 cm = 10 cm.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali definisi tali busur terpanjang pada lingkaran, yaitu diameter, dan menerapkan prosedur perkalian sederhana (2 x jari-jari). Ini adalah pengenalan fakta geometris dasar.. Bukti: Berapa panjang tali busurnya yang paling panjang?; jari-jarinya 5 cm
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep dasar lingkaran, khususnya hubungan antara jari-jari dan diameter sebagai tali busur terpanjang.. Bukti: tali busurnya yang paling panjang; jari-jarinya 5 cm
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan menguji pengetahuan dasar yang sudah dipelajari jauh sebelum kelas 11. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Berapa panjang tali busurnya yang paling panjang?; jari-jarinya 5 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari dan diameter lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi lingkaran merupakan prasyarat dasar geometri yang sudah dikuasai siswa sebelum kelas 11. Soal ini tidak memiliki tuntutan kognitif yang sesuai dengan standar kelas 11. |

Run 2 — solusi: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 * jari-jari = 2 * 5 cm = 10 cm.
- Domain kognitif `classify/knowing`: Siswa perlu mengetahui definisi tali busur terpanjang pada lingkaran (diameter) dan hubungan antara diameter dengan jari-jari. Ini adalah penerapan langsung dari konsep dasar geometri lingkaran.. Bukti: Berapa panjang tali busurnya yang paling panjang?; jari-jarinya 5 cm
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap konsep dasar geometri lingkaran, yaitu hubungan antara jari-jari dan diameter sebagai tali busur terpanjang.. Bukti: tali busurnya yang paling panjang; jari-jarinya 5 cm
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung. Siswa hanya perlu mengingat bahwa diameter adalah tali busur terpanjang dan menghitung 2 kali jari-jari. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Berapa panjang tali busurnya yang paling panjang?; jari-jarinya 5 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari dan diameter lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi lingkaran adalah topik dasar yang sudah dipelajari sejak SMP. Untuk kelas 11, pertanyaan ini sangat sederhana dan tidak menuntut penalaran tingkat tinggi. |

Run 3 — solusi: Tali busur terpanjang pada lingkaran adalah diameter. Diameter = 2 * jari-jari = 2 * 5 cm = 10 cm.
- Domain kognitif `classify/knowing`: Soal hanya menanyakan definisi tali busur terpanjang (diameter) dan menerapkan rumus d = 2r secara langsung tanpa memerlukan penalaran kompleks.. Bukti: Berapa panjang tali busurnya yang paling panjang?; jari-jarinya 5 cm
- Dimensi pengetahuan `classify/factual`: Soal menguji pengetahuan faktual mengenai definisi diameter sebagai tali busur terpanjang pada lingkaran.. Bukti: tali busurnya yang paling panjang
- Intended difficulty `classify/Easy`: Siswa hanya perlu mengingat definisi diameter sebagai tali busur terpanjang dan melakukan satu operasi perkalian sederhana. Tidak ada langkah kompleks atau integrasi konsep.. Bukti: jari-jarinya 5 cm; panjang tali busurnya yang paling panjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi diameter dan jari-jari lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi dasar lingkaran yang sudah dipelajari sejak jenjang SMP, sehingga bagi siswa kelas 11 ini adalah soal yang sangat mendasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3898`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya meminta pengenalan fakta geometris dasar bahwa diameter adalah tali busur terpanjang pada lingkaran dan penerapan prosedur perkalian sederhana.
- Dimensi pengetahuan `factual`: Soal menguji pengetahuan faktual mengenai definisi diameter sebagai tali busur terpanjang pada lingkaran.
- Intended difficulty `Easy`: Soal ini sangat mendasar dan rutin. Tidak ada integrasi konsep atau perencanaan langkah yang diperlukan. Bagi siswa kelas 11, ini adalah materi prasyarat yang sangat sederhana.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jari-jari dan diameter lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi lingkaran adalah topik dasar yang sudah dipelajari sejak SMP. Untuk kelas 11, pertanyaan ini sangat sederhana dan tidak menuntut penalaran tingkat tinggi. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `1ef6efc5863938a14b737897`

Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar 2.77 dengan diameter 2 meter dan panjang 12 meter?

| Opsi | Isi |
|---|---|
| A | 37,68 liter |
| B | 150.720 liter |
| C | 37.680 liter |
| D | 36.000 liter |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Volume tabung V = πr²h. Diketahui d = 2 m, maka r = 1 m. Tinggi h = 12 m. V = 3,14 × (1)² × 12 = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 = 37.680 liter.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `717c8ba7d56c1b612825b59e4c4a3aa6f6279052d942849d1106b27425ed1cac`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2676 |
| 2 | success | valid / verified | applying | procedural | Easy | 2701 |
| 3 | success | valid / verified | applying | procedural | Easy | 2711 |

Run 1 — solusi: Volume tabung V = πr²h. Diketahui d = 2 m, maka r = 1 m. Tinggi h = 12 m. V = 3,14 × (1)² × 12 = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan volume dari m³ ke liter. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang rumus volume tabung (konseptual) dan prosedur konversi satuan (prosedural).. Bukti: volume tabung; konversi meter kubik ke liter
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan substitusi langsung ke rumus volume tabung dan konversi satuan dasar. Langkah-langkahnya linear dan familiar bagi siswa kelas 11.. Bukti: diameter 2 meter; panjang 12 meter; Berapa liter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan hubungan satuan m³ ke liter. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume tabung adalah materi dasar yang sudah dikuasai sebelum kelas 11, sehingga soal ini bersifat rutin dan langsung. |

Run 2 — solusi: Diketahui diameter d=2 m, maka jari-jari r=1 m. Panjang tabung h=12 m. Volume V = πr²h = 3,14 × 1² × 12 = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan volume (m³ ke liter). Ini adalah penerapan prosedur standar pada konteks geometri yang rutin.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang rumus volume tabung dan hubungan antar satuan volume, yang merupakan pengetahuan prosedural.. Bukti: tabung penyimpanan besar; diameter 2 meter dan panjang 12 meter
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan rumus geometri dasar yang familiar bagi siswa kelas 11. Langkah penyelesaiannya linear: menentukan jari-jari, menghitung volume, dan melakukan konversi satuan. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume tabung adalah materi dasar yang sudah dikuasai sebelum kelas 11. Soal ini hanya memerlukan aplikasi langsung rumus tanpa modifikasi kompleks. |

Run 3 — solusi: Jari-jari (r) = diameter/2 = 2/2 = 1 m. Volume tabung = πr²h = 3,14 × 1² × 12 = 37,68 m³. Karena 1 m³ = 1.000 liter, maka volume = 37,68 × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus volume tabung dan melakukan konversi satuan volume (m³ ke liter). Ini adalah penerapan prosedur standar pada konteks yang diberikan.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang rumus volume tabung dan hubungan antar satuan volume, yang merupakan pengetahuan prosedural.. Bukti: Volume Bangun Ruang Sisi Lengkung; V=πr²h
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menggunakan rumus standar yang familiar bagi siswa kelas 11. Langkah penyelesaiannya langsung (menentukan jari-jari, menghitung volume, mengonversi satuan) tanpa kendala yang saling berinteraksi atau kebutuhan strategi nonrutin.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume tabung adalah materi dasar yang sudah dikuasai sebelum kelas 11. Soal ini hanya memerlukan aplikasi rumus langsung tanpa kompleksitas tambahan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `9bee88ce31163c95d6276272`

Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.<br><br>Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.

| Opsi | Isi |
|---|---|
| A | Semakin banyak kendaraan bermotor, semakin menurun tingkat polusi udara (korelasi negatif) |
| B | Semakin banyak kendaraan bermotor, semakin meningkat tingkat polusi udara (korelasi positif) |
| C | Tidak ada hubungan antara banyak kendaraan bermotor dan tingkat polusi udara |
| D | Hubungan keduanya tidak dapat ditentukan tanpa data numerik |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Hubungan antara banyak kendaraan bermotor dan tingkat polusi udara adalah korelasi positif. Semakin banyak kendaraan bermotor, semakin banyak asap yang dihasilkan, sehingga tingkat polusi udara meningkat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `78dd5eebda64baf2439b35774b5ae8d700e418e4c9427681d6dec17dc20c963f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3878 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2629 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2629 |

Run 1 — solusi: Hubungan antara banyak kendaraan bermotor dan tingkat polusi udara adalah korelasi positif. Semakin banyak kendaraan bermotor, semakin banyak asap yang dihasilkan, sehingga tingkat polusi udara meningkat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep korelasi positif pada konteks dunia nyata yang umum untuk menentukan hubungan antar variabel.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep korelasi (positif) dalam konteks nyata, bukan sekadar hafalan fakta atau prosedur hitung.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Intended difficulty `classify/Easy`: Soal bersifat konseptual dasar. Hubungan antara kendaraan dan polusi sangat intuitif, tidak memerlukan perhitungan atau analisis data yang kompleks.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi positif dan negatif. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan konsep korelasi yang sangat mendasar dan intuitif bagi siswa kelas 11, tanpa beban komputasi atau analisis data yang rumit. |

Run 2 — solusi: Kendaraan bermotor menghasilkan emisi gas buang. Semakin banyak jumlah kendaraan, semakin besar volume emisi yang dihasilkan, sehingga tingkat polusi udara cenderung meningkat. Ini menunjukkan hubungan searah atau korelasi positif.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi arah hubungan (korelasi) antara dua variabel berdasarkan pemahaman konsep sebab-akibat dalam konteks nyata, bukan sekadar menghitung koefisien korelasi dari data.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar korelasi (positif vs negatif) dan menerapkannya pada fenomena dunia nyata (polusi udara).. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan kualitatif. Tidak ada perhitungan numerik yang diperlukan, dan hubungan sebab-akibat antara kendaraan dan polusi adalah pengetahuan umum yang rutin dalam konteks literasi data.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi positif dan negatif serta hubungan sebab-akibat sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi arah korelasi dari konteks nyata adalah tugas dasar dalam materi diagram pencar. Tidak ada tuntutan analisis data kompleks atau perhitungan statistik. |

Run 3 — solusi: Banyaknya kendaraan bermotor berbanding lurus dengan jumlah emisi gas buang yang dihasilkan. Semakin banyak kendaraan, semakin tinggi tingkat polusi udara. Hubungan ini menunjukkan korelasi positif.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi arah hubungan (korelasi) antara dua variabel berdasarkan pemahaman kontekstual, bukan sekadar menghitung data. Ini melibatkan penerapan konsep korelasi pada situasi nyata.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar korelasi (positif/negatif) dan menerapkannya pada hubungan sebab-akibat antara variabel yang diberikan.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan kualitatif. Siswa hanya perlu memahami hubungan sebab-akibat yang umum tanpa melakukan perhitungan atau analisis data statistik yang kompleks. Jalur penyelesaian sangat langsung.. Bukti: Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi positif dan negatif serta hubungan sebab-akibat sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi arah hubungan korelasi dari konteks sehari-hari adalah tugas dasar yang rutin dan tidak memerlukan analisis data mendalam. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `954fcaa8282f462df30d7e71`

Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.<br><br>Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin? Berikan alasan kalian.

| Opsi | Isi |
|---|---|
| A | Tidak ada hubungan antara jarak tempuh dan volume bensin |
| B | Hubungan keduanya tidak dapat ditentukan tanpa data numerik |
| C | Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin berkurang volume bensin dalam tangki bensin (korelasi negatif) |
| D | Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin bertambah volume bensin dalam tangki bensin (korelasi positif) |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Semakin jauh jarak yang ditempuh motor, semakin banyak bensin yang dikonsumsi untuk pembakaran mesin. Akibatnya, volume bensin dalam tangki akan berkurang seiring bertambahnya jarak. Ini menunjukkan hubungan korelasi negatif antara jarak tempuh dan volume bensin.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bf27679b9cef4b7376dfa9c0d147b6029505bbce548c7e17374a1538e4c44761`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2710 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2665 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3382 |

Run 1 — solusi: Semakin jauh jarak yang ditempuh motor, semakin banyak bensin yang dikonsumsi untuk pembakaran mesin. Akibatnya, volume bensin dalam tangki akan berkurang seiring bertambahnya jarak. Ini menunjukkan hubungan korelasi negatif antara jarak tempuh dan volume bensin.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk memahami konsep hubungan antarvariabel dalam konteks nyata (korelasi negatif) tanpa perlu melakukan perhitungan numerik. Siswa harus mengidentifikasi arah hubungan berdasarkan logika fungsional konsumsi bahan bakar.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip hubungan sebab-akibat (konsumsi bahan bakar) dan menerjemahkannya ke dalam konsep korelasi negatif, yang merupakan bagian dari pemahaman konseptual tentang diagram pencar.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Intended difficulty `classify/Easy`: Soal ini bersifat kualitatif dan menguji pemahaman dasar tentang korelasi. Tidak ada perhitungan kompleks atau langkah-langkah prosedural yang panjang. Siswa hanya perlu memahami logika hubungan variabel yang familiar dalam kehidupan sehari-hari.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi negatif dan hubungan sebab-akibat dalam konteks nyata. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 11 dalam topik analisis data/korelasi, karena hanya menuntut pemahaman konseptual kualitatif tanpa menuntut analisis data statistik yang mendalam. |

Run 2 — solusi: Jarak tempuh dan volume bensin memiliki korelasi negatif. Semakin jauh jarak yang ditempuh motor, semakin banyak bensin yang dikonsumsi, sehingga volume bensin dalam tangki akan semakin berkurang.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk memahami dan menjelaskan hubungan kualitatif antara dua variabel berdasarkan logika kontekstual, bukan sekadar menghitung atau menerapkan rumus.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin? Berikan alasan kalian.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip korelasi (konsep) dan menerapkannya pada situasi nyata (jarak vs volume bensin).. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung. Siswa hanya perlu mengidentifikasi arah hubungan (negatif) berdasarkan logika dasar penggunaan bahan bakar. Tidak ada perhitungan kompleks atau langkah-langkah yang saling bergantung.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin? Berikan alasan kalian.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi negatif dalam konteks kehidupan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, memahami korelasi negatif secara kualitatif adalah materi dasar dalam analisis data/statistik yang sangat mudah dipahami tanpa perlu data numerik. |

Run 3 — solusi: Semakin jauh jarak yang ditempuh motor, semakin banyak bensin yang dikonsumsi, sehingga volume bensin dalam tangki berkurang. Ini menunjukkan hubungan korelasi negatif antara jarak tempuh dan volume bensin.
- Domain kognitif `classify/applying`: Siswa diminta mengenali dan menginterpretasikan hubungan kualitatif antara dua variabel berdasarkan pemahaman konsep dasar korelasi negatif.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang hubungan antar variabel (korelasi) dalam situasi nyata.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu memahami logika hubungan sebab-akibat sederhana tanpa perhitungan atau analisis data kompleks. Tidak ada langkah yang saling bergantung atau kendala yang rumit.. Bukti: Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang hubungan antar variabel (korelasi negatif). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, mengidentifikasi korelasi negatif dari konteks sehari-hari adalah tugas yang sangat mendasar dan rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `cc594209724affd13041e475`

Pada saat kondisi mendadak, para pengendara mobil memerlukan waktu yang berbeda-beda untuk dapat bereaksi untuk menginjak rem mobil. Jarak yang diperlukan hingga terjadi reaksi menginjak rem disebut sebagai jarak reaksi. Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda. Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.<br><br>Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

| Opsi | Isi |
|---|---|
| A | 8,3 m |
| B | 7,2 m |
| C | 12,4 m |
| D | 11,34 m |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Persamaan regresi linear y = ax + b dapat ditentukan dari data. Dengan x = kecepatan dan y = jarak reaksi, diperoleh slope (a) sekitar 0,207 dan intersep (b) sekitar -0,042. Untuk x = 35, y = 0,207(35) - 0,042 = 7,245 - 0,042 = 7,203. Dibulatkan menjadi 7,2 m.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cd2835a012f78c01babae85a3d193f5c1fcaadbef8b6846d63cdd882eff60998`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2960 |
| 2 | success | valid / verified | applying | procedural | Medium | 2971 |
| 3 | success | valid / verified | applying | procedural | Medium | 2953 |

Run 1 — solusi: Persamaan regresi linear y = ax + b dapat ditentukan dari data. Dengan x = kecepatan dan y = jarak reaksi, diperoleh slope (a) sekitar 0,207 dan intersep (b) sekitar -0,042. Untuk x = 35, y = 0,207(35) - 0,042 = 7,245 - 0,042 = 7,203. Dibulatkan menjadi 7,2 m.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan model regresi linear untuk melakukan prediksi (interpolasi) pada nilai x yang tidak ada di tabel. Ini adalah penerapan prosedur statistik yang sudah dipelajari.. Bukti: Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menggunakan metode regresi linear (algoritme/teknik) untuk memprediksi nilai berdasarkan data yang diberikan.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan perhitungan regresi linear (menentukan persamaan garis) terlebih dahulu sebelum melakukan prediksi. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait (menghitung slope/intersep, lalu substitusi) yang memerlukan ketelitian.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, perhitungan slope dan intersep, serta substitusi nilai ke dalam persamaan linear. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, regresi linear adalah materi standar. Menghitung persamaan regresi dari data tabel adalah prosedur rutin, namun memerlukan beberapa langkah perhitungan yang berurutan, sehingga dikategorikan Medium. |

Run 2 — solusi: Persamaan regresi linear y = ax + b dapat ditentukan dari data. Dengan metode kuadrat terkecil, diperoleh persamaan y = 0,207x - 0,042. Untuk x = 35, y = 0,207(35) - 0,042 = 7,245 - 0,042 = 7,203. Dibulatkan menjadi 7,2 m.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan model regresi linear yang diperoleh dari data untuk melakukan prediksi (interpolasi) pada nilai x tertentu. Ini adalah penerapan prosedur statistik yang rutin dalam konteks regresi.. Bukti: Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan metode atau algoritme regresi linear untuk memprediksi nilai, yang merupakan bagian dari pengetahuan prosedural dalam statistika.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya familiar (regresi linear), siswa harus menentukan atau menggunakan persamaan regresi dari data yang diberikan sebelum melakukan substitusi. Terdapat beberapa langkah (menentukan model/persamaan, lalu substitusi) yang saling terkait.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, konsep variabel bebas dan terikat, serta kemampuan melakukan substitusi nilai ke dalam persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, regresi linear adalah materi standar. Soal ini menuntut siswa untuk tidak sekadar membaca tabel (seperti pengecoh A dan C), melainkan memahami bahwa prediksi harus dilakukan melalui model regresi, yang merupakan tuntutan kognitif yang sesuai untuk tingkat menengah. |

Run 3 — solusi: Persamaan regresi linear y = ax + b dapat ditentukan dari data. Dengan x = kecepatan dan y = jarak reaksi, diperoleh slope (a) ≈ 0,207 dan intersep (b) ≈ -0,042. Untuk x = 35, y = 0,207(35) - 0,042 = 7,245 - 0,042 = 7,203 ≈ 7,2 m.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan model regresi linear untuk memprediksi nilai di luar data yang diberikan (interpolasi). Ini memerlukan penerapan prosedur statistik yang telah dipelajari.. Bukti: Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang metode regresi linear sebagai teknik untuk memprediksi nilai berdasarkan tren data.. Bukti: Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya familiar (regresi linear), siswa perlu melakukan perhitungan statistik untuk menentukan persamaan garis terlebih dahulu sebelum melakukan prediksi, yang melibatkan beberapa langkah terstruktur.. Bukti: Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.; Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, perhitungan slope dan intersep, serta substitusi nilai ke dalam persamaan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu melakukan analisis regresi sederhana. Beban perhitungan moderat karena memerlukan penentuan persamaan garis dari data mentah sebelum prediksi. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `cb666d7ac7a8bdfb36335e5a`

Tabel berikut menunjukkan banyak tempat duduk terhadap biaya per jam dari tiga model pesawat terbang yang digunakan oleh maskapai Garuda Indonesia.<br><br>\|Model Pesawat\|Banyak tempat duduk\|Biaya (rupiah/jam)\|<br>\|---\|---\|---\|<br>\|A\|50\|1.100.000,00\|<br>\|B\|100\|2.100.000,00\|<br>\|C\|150\|2.700.000,00\|<br><br>Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?

| Opsi | Isi |
|---|---|
| A | yˆ = 300000 + 16000x |
| B | yˆ = 367000 + 16000x |
| C | Tidak dapat ditentukan tanpa menggambar diagram pencarnya |
| D | Keduanya sama tepat karena mempunyai gradien (b) yang sama |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Hitung jumlah kuadrat residu (SSE) untuk setiap model. Data (x, y): (50, 1.1jt), (100, 2.1jt), (150, 2.7jt). Model 1 (300rb + 16rb*x): ŷ1=1.1jt, ŷ2=1.9jt, ŷ3=2.7jt. SSE1 = (1.1-1.1)^2 + (2.1-1.9)^2 + (2.7-2.7)^2 = 0.04. Model 2 (367rb + 16rb*x): ŷ1=1.167jt, ŷ2=1.967jt, ŷ3=2.767jt. SSE2 = (1.1-1.167)^2 + (2.1-1.967)^2 + (2.7-2.767)^2 ≈ 0.0267. Karena SSE2 < SSE1, model B lebih tepat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f4ba0d5c31b22adef6ee9c9a0705371715511df71295dfde874cd1011db9a664`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3357 |
| 2 | success | valid / verified | applying | procedural | Medium | 3330 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 6112 |

Run 1 — solusi: Untuk menentukan garis regresi yang lebih tepat, hitung jumlah kuadrat residu (SSE = Σ(yi - ŷi)^2) untuk setiap model. Data: (50, 1.1jt), (100, 2.1jt), (150, 2.7jt). Model 1 (300rb + 16rb*x): ŷ1=1.1jt, ŷ2=1.9jt, ŷ3=2.7jt. SSE1 = (1.1-1.1)^2 + (2.1-1.9)^2 + (2.7-2.7)^2 = 0 + 0.04 + 0 = 0.04 (dalam triliun). Model 2 (367rb + 16rb*x): ŷ1=1.167jt, ŷ2=1.967jt, ŷ3=2.767jt. SSE2 = (1.1-1.167)^2 + (2.1-1.967)^2 + (2.7-2.767)^2 = 0.004489 + 0.017689 + 0.004489 = 0.026667. Karena SSE2 < SSE1, model B lebih tepat.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengevaluasi ketepatan dua model regresi menggunakan kriteria jumlah kuadrat residu (least squares). Ini memerlukan penerapan konsep statistik tentang bagaimana garis regresi 'terbaik' ditentukan, bukan sekadar menghafal rumus.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya; jumlah kuadrat residu yˆ = 367000+16000x adalah 26.667.000.000, lebih kecil dari jumlah kuadrat residu yˆ = 300000+16000x yaitu 40.000.000.000
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang kriteria 'ketepatan' garis regresi (minimasi jumlah kuadrat residu) dan kemampuan prosedural untuk menghitung atau membandingkan nilai residu tersebut.. Bukti: Persamaan garis regresi mana yang lebih tepat; jumlah kuadrat residu
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium. Siswa harus memahami kriteria pemilihan model regresi (SSE) dan melakukan perhitungan residu untuk dua model yang berbeda. Meskipun prosedurnya familiar, siswa perlu merencanakan langkah perhitungan untuk ketiga titik data dan membandingkan hasilnya, yang melibatkan beberapa langkah saling terkait.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, residu, dan perhitungan aritmatika. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu membandingkan model statistik sederhana. Soal menuntut pemilihan prosedur yang tepat (SSE) untuk memvalidasi model, yang merupakan standar kompetensi analisis data. |

Run 2 — solusi: Untuk menentukan garis regresi yang lebih tepat, hitung jumlah kuadrat residu (SSE) untuk setiap model. Data (x, y): (50, 1.100.000), (100, 2.100.000), (150, 2.700.000). Untuk y = 367.000 + 16.000x: SSE = (1.100.000 - 1.167.000)^2 + (2.100.000 - 1.967.000)^2 + (2.700.000 - 2.767.000)^2 = 26.667.000.000. Untuk y = 300.000 + 16.000x: SSE = (1.100.000 - 1.100.000)^2 + (2.100.000 - 1.900.000)^2 + (2.700.000 - 2.700.000)^2 = 40.000.000.000. Karena 26,67M < 40M, model pertama lebih tepat.
- Domain kognitif `classify/applying`: Siswa diminta mengevaluasi dua model regresi yang diberikan dengan kriteria ketepatan (jumlah kuadrat residu). Ini memerlukan penerapan konsep statistik tentang 'best fit' melalui perhitungan residu, bukan sekadar visualisasi.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya; jumlah kuadrat residu yˆ = 367000+16000x adalah 26.667.000.000, lebih kecil dari jumlah kuadrat residu yˆ = 300000+16000x yaitu 40.000.000.000
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang kriteria pemilihan garis regresi (konseptual) dan penerapan prosedur perhitungan jumlah kuadrat residu (prosedural).. Bukti: Persamaan garis regresi mana yang lebih tepat; jumlah kuadrat residu
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan perhitungan residu untuk dua model yang berbeda. Meskipun prosedurnya familiar, siswa harus melakukan perhitungan berulang untuk membandingkan kedua model, yang melibatkan beberapa langkah terstruktur dan ketelitian numerik.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, residu, dan perhitungan aritmatika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menghitung residu untuk membandingkan model regresi. Beban perhitungan moderat dan langkah-langkah yang jelas membuat soal ini berada di tingkat menengah. |

Run 3 — solusi: Hitung jumlah kuadrat residu (JKR) untuk kedua persamaan. Untuk y=300.000+16.000x: JKR = (1,1-1,1)^2 + (2,1-1,9)^2 + (2,7-2,7)^2 = 0 + 0,04 + 0 = 0,04 (dalam triliun). Untuk y=367.000+16.000x: JKR = (1,1-1,167)^2 + (2,1-1,967)^2 + (2,7-2,767)^2 = 0,004489 + 0,017689 + 0,004489 = 0,026667. Karena 0,026667 < 0,04, maka y=367.000+16.000x lebih tepat.
- Domain kognitif `classify/reasoning`: Siswa harus memahami kriteria 'ketepatan' garis regresi (jumlah kuadrat residu terkecil) dan menerapkan prosedur perhitungan residu untuk membandingkan dua model, yang merupakan proses penalaran konseptual.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang prinsip 'least squares' dalam regresi linear untuk menentukan model mana yang lebih baik, bukan sekadar menghafal rumus.. Bukti: Persamaan garis regresi mana yang lebih tepat
- Intended difficulty `classify/Hard`: Soal ini Hard karena siswa harus menentukan sendiri strategi (menghitung jumlah kuadrat residu) untuk membandingkan dua model. Tidak ada petunjuk eksplisit untuk menggunakan metode ini. Siswa harus melakukan perhitungan berulang dan membandingkan hasilnya, yang menuntut perencanaan langkah yang saling bergantung.. Bukti: Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep residu dan metode kuadrat terkecil (least squares) dalam regresi linear. |
| dependentSteps | 8 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan memahami regresi, namun memilih metode kuadrat terkecil untuk membandingkan dua model tanpa instruksi eksplisit merupakan tuntutan kognitif yang tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "reasoning": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Hard": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5743`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan kriteria statistik (jumlah kuadrat residu) untuk mengevaluasi dan membandingkan dua model regresi. Ini adalah penerapan prosedur statistik pada konteks yang diberikan.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang kriteria 'ketepatan' garis regresi (minimasi jumlah kuadrat residu) dan kemampuan prosedural untuk menghitung nilai tersebut.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium. Siswa perlu melakukan perhitungan residu untuk dua model yang berbeda. Meskipun prosedurnya familiar, siswa harus merencanakan langkah perhitungan untuk ketiga titik data dan membandingkan hasilnya, yang melibatkan beberapa langkah saling terkait dan ketelitian numerik.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang regresi linear, residu, dan perhitungan aritmatika. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu membandingkan model statistik sederhana. Soal menuntut pemilihan prosedur yang tepat (SSE) untuk memvalidasi model, yang merupakan standar kompetensi analisis data. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `5a713d72bd575400bbc8e916`

Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.<br><br>Berapa persentase IQ yang diterangkan oleh lingkar kepala?

| Opsi | Isi |
|---|---|
| A | 13,8% |
| B | 0,19% |
| C | 98,1% |
| D | 1,9% |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Persentase variansi yang dijelaskan oleh variabel bebas (koefisien determinasi) dihitung dengan menguadratkan koefisien korelasi (r). r = 0,138. r^2 = (0,138)^2 = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044% atau sekitar 1,9%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `848f2895258a98d11fd8943f6e3ba93823ab84a97523c8be2f32f5ec445f78d3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2761 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2769 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2780 |

Run 1 — solusi: Persentase variansi yang dijelaskan oleh variabel bebas (koefisien determinasi) dihitung dengan menguadratkan koefisien korelasi (r). r = 0,138. r^2 = (0,138)^2 = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044% atau sekitar 1,9%.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerapkan konsep koefisien determinasi (r^2) dari nilai koefisien korelasi (r) yang diberikan. Ini adalah penerapan langsung dari rumus statistik dasar yang dipelajari di kelas 11.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan konseptual antara koefisien korelasi dan koefisien determinasi (r^2) sebagai ukuran variansi yang dijelaskan.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan satu operasi aritmatika (pengkuadratan) dan konversi ke persen. Tidak ada langkah perencanaan kompleks atau kendala yang berinteraksi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

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
| gradeRelativeRationale | Siswa kelas 11 diharapkan memahami definisi koefisien determinasi sebagai r^2 dalam analisis regresi linear sederhana. |

Run 2 — solusi: Persentase variansi IQ yang diterangkan oleh lingkar kepala ditentukan oleh koefisien determinasi (r²). Diketahui r = 0,138, maka r² = (0,138)² = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044%, yang dibulatkan menjadi 1,9%.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerapkan konsep koefisien determinasi (r²) untuk menjelaskan variansi data. Ini adalah penerapan langsung dari definisi statistik yang dipelajari di kelas 11.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan konseptual antara koefisien korelasi (r) dan koefisien determinasi (r²) sebagai ukuran proporsi variansi yang dijelaskan.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang telah mempelajari analisis korelasi. Prosedurnya jelas (mengkuadratkan nilai r) dan tidak memerlukan perencanaan langkah yang kompleks atau integrasi kendala yang sulit.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien korelasi dan koefisien determinasi (r²). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu membedakan r dan r² dalam konteks analisis regresi linear sederhana. |

Run 3 — solusi: Persentase variansi IQ yang diterangkan oleh lingkar kepala ditentukan oleh koefisien determinasi (r²). Diketahui r = 0,138, maka r² = (0,138)² = 0,019044. Dalam bentuk persentase, 0,019044 ≈ 1,9%.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep koefisien determinasi (r²) sebagai ukuran proporsi variansi variabel terikat yang dijelaskan oleh variabel bebas. Ini adalah penerapan konsep statistik yang rutin dalam analisis korelasi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang hubungan antara koefisien korelasi (r) dan koefisien determinasi (r²) dalam konteks regresi/korelasi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena hanya memerlukan penerapan langsung rumus koefisien determinasi (r²) dari nilai r yang sudah diberikan. Tidak ada langkah perencanaan kompleks atau integrasi kendala yang sulit.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

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
| gradeRelativeRationale | Siswa kelas 11 yang mempelajari statistika deskriptif dan inferensial diharapkan memahami interpretasi r² sebagai persentase variansi yang dijelaskan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `2071d19215ee9fcf4926b805`

Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.<br><br>Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

| Opsi | Isi |
|---|---|
| A | 0,981% |
| B | 99,1% |
| C | 98,1% |
| D | 1,9% |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Koefisien determinasi (r²) = (0,138)² = 0,019044 atau 1,9%. Persentase variansi yang dijelaskan oleh variabel lain = 100% - r² = 100% - 1,9% = 98,1%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c7ffecd03a676a49cc5244782665586f73bc2f1348e7d64952c6ebef78b9c01a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3779 |
| 2 | success | valid / verified | applying | procedural | Medium | 3791 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3602 |

Run 1 — solusi: Koefisien determinasi r^2 = (0,138)^2 = 0,019044 atau 1,9%. Persentase variansi yang tidak dijelaskan oleh variabel lingkar kepala (diterangkan variabel lain) adalah 1 - r^2 = 1 - 0,019044 = 0,980956 atau 98,1%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep koefisien determinasi (r^2) dan konsep variansi yang tidak dijelaskan (1 - r^2) pada konteks statistik.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara koefisien korelasi, koefisien determinasi, dan interpretasi variansi dalam analisis regresi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep statistik yang spesifik (r^2 dan 1-r^2). Meskipun prosedurnya sederhana, siswa harus memahami interpretasi koefisien korelasi terhadap variansi, yang merupakan konsep menengah di kelas 11.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien korelasi (r) dan koefisien determinasi (r^2). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korelasi dan regresi adalah bagian dari kurikulum kelas 11. Konsep r^2 sebagai proporsi variansi yang dijelaskan adalah standar, namun seringkali membingungkan siswa, sehingga dikategorikan Medium. |

Run 2 — solusi: Koefisien determinasi (r²) = (0,138)² = 0,019044 atau 1,9%. Persentase variansi IQ yang dijelaskan oleh variabel lain = 100% - r² = 100% - 1,9% = 98,1%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep koefisien determinasi (r²) untuk menghitung variansi yang dijelaskan, lalu menggunakan komplemennya (1 - r²) untuk mencari variansi yang dijelaskan oleh variabel lain. Ini adalah penerapan prosedur statistik standar.. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode statistik untuk menghitung koefisien determinasi dan menginterpretasikannya dalam konteks variansi yang tidak dijelaskan oleh model regresi.. Bukti: Nilai koefisien korelasinya adalah 0,138; persentase IQ yang diterangkan oleh variabel-variabel lainnya
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep bahwa r² adalah variansi yang dijelaskan, dan siswa harus melakukan langkah tambahan (1 - r²) untuk menjawab 'variabel lain'. Ini melibatkan lebih dari satu langkah prosedural dan pemahaman konseptual tentang apa yang diwakili oleh r².. Bukti: Nilai koefisien korelasinya adalah 0,138; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang korelasi (r) dan koefisien determinasi (r²). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 diharapkan memahami interpretasi r² dalam analisis regresi. Soal ini menguji pemahaman tentang variansi yang dijelaskan vs tidak dijelaskan, yang merupakan bagian dari kurikulum statistik SMA. |

Run 3 — solusi: Koefisien determinasi (r²) = (0,138)² = 0,019044 atau 1,9%. Persentase variansi yang dijelaskan oleh variabel lain = 100% - r² = 100% - 1,9% = 98,1%.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung prosedur statistik untuk menghitung persentase variansi yang tidak dijelaskan oleh variabel bebas, menggunakan konsep koefisien determinasi (r²) yang sudah dipelajari di kelas 11.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan konseptual antara koefisien korelasi (r), koefisien determinasi (r²), dan proporsi variansi yang dijelaskan/tidak dijelaskan.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan rumus 1-r² untuk mendapatkan jawaban. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang koefisien korelasi (r) dan koefisien determinasi (r²). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi regresi dan korelasi adalah bagian dari kurikulum kelas 11. Prosedur menghitung persentase variansi yang tidak dijelaskan adalah aplikasi standar dari r². |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4593`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep koefisien determinasi (r²) untuk menghitung variansi yang dijelaskan oleh model, lalu menggunakan komplemennya (1 - r²) untuk menentukan variansi yang dijelaskan oleh variabel lain. Ini adalah penerapan prosedur statistik standar.
- Dimensi pengetahuan `conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara koefisien korelasi (r), koefisien determinasi (r²), dan interpretasi variansi dalam analisis regresi.
- Intended difficulty `Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan rumus 1-r² untuk mendapatkan jawaban. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks. Prosedur ini merupakan aplikasi langsung dari materi statistik kelas 11.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien korelasi (r) dan koefisien determinasi (r²). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi regresi dan korelasi adalah bagian dari kurikulum kelas 11. Prosedur menghitung persentase variansi yang tidak dijelaskan adalah aplikasi standar dari r² yang bersifat rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `d6d3b4c5f9819d69d4c859d0`

Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315<br><br>Mengapa angka 750 kWh dapat dianggap sebagai pencilan?

| Opsi | Isi |
|---|---|
| A | Karena 750 kWh lebih dari 1,5 kali median data (315 kWh) |
| B | Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit |
| C | Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh) |
| D | Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Urutkan data: 300, 305, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1.5 * IQR = 320 + 1.5(10) = 335. Karena 750 > 335, maka 750 adalah pencilan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e3bb25a294549a464cfb0e16cdcdee70ea28e37a6f241d828299959fb927e2cd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2987 |
| 2 | success | valid / verified | applying | procedural | Easy | 2965 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2972 |

Run 1 — solusi: Data terurut: 300, 305, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1.5 * IQR = 320 + 1.5(10) = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar untuk mendeteksi pencilan (outlier) menggunakan metode IQR (Interquartile Range). Ini melibatkan pemahaman konsep batas atas dan penerapan algoritma perhitungan yang rutin dalam statistika deskriptif.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dan kriteria statistik untuk menentukan pencilan, yang merupakan bagian dari prosedur standar dalam analisis data.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat standar dan familiar bagi siswa kelas 11. Langkah-langkahnya (mengurutkan data, mencari kuartil, menghitung IQR, dan membandingkan dengan batas atas) bersifat rutin dan tidak memerlukan integrasi konsep yang kompleks.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kuartil, jangkauan interkuartil (IQR), dan kriteria pencilan (outlier). |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistika deskriptif (ukuran penyebaran) adalah kurikulum standar kelas 11. Prosedur deteksi pencilan dengan 1.5*IQR adalah metode baku yang diajarkan secara eksplisit. |

Run 2 — solusi: Urutkan data: 300, 305, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1.5 * IQR = 320 + 15 = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi alasan statistik yang valid untuk menentukan pencilan, yang memerlukan pemahaman tentang konsep IQR dan batas pencilan.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang cara menghitung dan menerapkan kriteria statistik (IQR) untuk mendeteksi pencilan.. Bukti: Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur penentuan pencilan menggunakan IQR adalah materi standar kelas 11. Langkah-langkahnya rutin: mengurutkan data, mencari kuartil, menghitung IQR, dan membandingkan dengan batas atas. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kuartil, IQR, dan kriteria pencilan statistik. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (pencilan) adalah bagian dari kurikulum kelas 11. Prosedur yang diperlukan sangat standar dan familiar bagi siswa. |

Run 3 — solusi: Urutkan data: 300, 305, 310, 310, 310, 315, 315, 320, 320, 325, 750. Q1 = 310, Q3 = 320. IQR = Q3 - Q1 = 10. Batas atas = Q3 + 1.5 * IQR = 320 + 15 = 335. Karena 750 > 335, maka 750 adalah pencilan.
- Domain kognitif `classify/applying`: Soal meminta siswa mengidentifikasi alasan statistik yang tepat untuk mendefinisikan pencilan (outlier) menggunakan metode IQR, yang merupakan penerapan konsep statistik deskriptif.. Bukti: Mengapa angka 750 kWh dapat dianggap sebagai pencilan?; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip statistik tentang bagaimana pencilan ditentukan menggunakan kuartil dan rentang antarkuartil (IQR), yang merupakan pengetahuan konseptual.. Bukti: Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur penentuan pencilan dengan metode IQR adalah prosedur standar yang familiar di kelas 11. Langkah-langkahnya jelas (mengurutkan, mencari kuartil, menghitung batas), dan soal menyediakan pilihan yang menguji pemahaman konsep dasar tersebut.. Bukti: 300, 320, 310, 305, 315, 320, 750, 310, 325, 315; Karena 750 kWh lebih besar dari batas atas IQR (335 kWh)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang kuartil, IQR, dan definisi statistik pencilan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penentuan pencilan menggunakan IQR adalah materi standar statistik SMA kelas 11. Prosedur ini bersifat rutin dan tidak memerlukan integrasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4970`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur statistik standar untuk mendeteksi pencilan menggunakan metode IQR. Ini adalah penerapan langsung dari algoritma yang sudah dipelajari di kelas 11.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang cara menghitung dan menerapkan kriteria statistik (IQR) untuk mendeteksi pencilan.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena prosedur penentuan pencilan menggunakan IQR adalah materi standar kelas 11. Langkah-langkahnya rutin: mengurutkan data, mencari kuartil, menghitung IQR, dan membandingkan dengan batas atas. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kuartil, IQR, dan kriteria pencilan statistik. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 10 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi statistik deskriptif (pencilan) adalah bagian dari kurikulum kelas 11. Prosedur yang diperlukan sangat standar dan familiar bagi siswa. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
