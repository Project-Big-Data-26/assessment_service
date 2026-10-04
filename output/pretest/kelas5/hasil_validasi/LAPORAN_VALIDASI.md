# Validasi ulang soal kelas 5 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sd-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 5 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model dipakai sebagai diagnostik; tidak diberikan kembali ke Gemini.

Jumlah soal: 72; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 21, "applying": 43, "reasoning": 6, "undecided": 2}, "knowledgeDimension": {"conceptual": 28, "factual": 6, "procedural": 36, "undecided": 2, "metacognitive": 0}, "intendedDifficulty": {"Easy": 47, "Medium": 21, "undecided": 2, "Hard": 2}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 19, "applying": 42, "reasoning": 6}, "knowledgeDimension": {"conceptual": 27, "factual": 6, "procedural": 34, "metacognitive": 0}, "intendedDifficulty": {"Easy": 45, "Medium": 20, "Hard": 2}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 67, "revision_required": 4, "needs_ai_review": 1}`.
Run awal sukses: 216/216; adjudikasi: 39; token sukses tercatat: 819,575.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 47 | 45 | [Easy.json](difficulty/Easy.json) |
| Medium | 21 | 20 | [Medium.json](difficulty/Medium.json) |
| Hard | 2 | 2 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `467767b4f8454046da41a593`

Kecamatan Kayu Tanam terletak di Kabupaten Padang Pariaman, Provinsi Sumatra Barat. Pada tahun 2018, penduduk kecamatan ini berjumlah 26.932 jiwa yang terdiri atas 13.354 jiwa laki-laki dan tiga belas ribu lima ratus tujuh puluh delapan jiwa perempuan.<br><br>Berdasarkan bacaan tersebut, coba kerjakan beberapa hal berikut.<br><br>Tentukanj jumlah penduduk perempuan Kecamatan Kayu Tanam dan tentukan nilai tempatnya.

| Opsi | Isi |
|---|---|
| A | 13.354 (1 puluh ribuan, 3 ribuan, 3 ratusan, 5 puluhan, 4 satuan) |
| B | 13.587 (1 puluh ribuan, 3 ribuan, 5 ratusan, 8 puluhan, 7 satuan) |
| C | 130.578 (1 ratus ribuan, 3 puluh ribuan, 0 ribuan, 5 ratusan, 7 puluhan, 8 satuan) |
| D | 13.578 (1 puluh ribuan, 3 ribuan, 5 ratusan, 7 puluhan, 8 satuan) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Teks menyatakan jumlah penduduk perempuan adalah tiga belas ribu lima ratus tujuh puluh delapan, yang ditulis sebagai 13.578. Nilai tempatnya adalah 1 puluh ribuan, 3 ribuan, 5 ratusan, 7 puluhan, dan 8 satuan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4ecfab0ebdbd118f4d28eaa42b312e028a4f39c35cedfb64109fe69e0a025fea`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2521 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2538 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2521 |

Run 1 — solusi: Teks menyatakan jumlah penduduk perempuan adalah tiga belas ribu lima ratus tujuh puluh delapan, yang ditulis sebagai 13.578. Nilai tempatnya adalah 1 puluh ribuan, 3 ribuan, 5 ratusan, 7 puluhan, dan 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta menerjemahkan representasi verbal bilangan ke dalam bentuk angka dan mengidentifikasi nilai tempatnya. Ini adalah tugas langsung yang memerlukan pemahaman dasar tentang sistem bilangan cacah.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang simbol bilangan dan struktur nilai tempat (posisi angka dalam bilangan), yang merupakan pengetahuan konseptual dasar.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengubah bentuk verbal menjadi numerik dan menguraikan nilai tempatnya. Tidak ada langkah kompleks atau integrasi yang diperlukan.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman membaca dan menulis bilangan cacah sampai 100.000 serta nilai tempat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, membaca dan menulis bilangan serta menentukan nilai tempat adalah materi dasar yang sudah dikuasai. Soal ini tidak menuntut perencanaan atau integrasi langkah yang rumit. |

Run 2 — solusi: Teks menyatakan jumlah penduduk perempuan adalah 'tiga belas ribu lima ratus tujuh puluh delapan', yang ditulis sebagai 13.578. Nilai tempatnya adalah 1 puluh ribuan, 3 ribuan, 5 ratusan, 7 puluhan, dan 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan representasi verbal bilangan menjadi numerik dan mengidentifikasi nilai tempatnya. Ini adalah prosedur langsung yang tidak memerlukan strategi nonrutin atau integrasi kompleks.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan jiwa perempuan; tentukan nilai tempatnya
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang sistem penulisan bilangan (simbol) dan konsep nilai tempat (posisi angka), yang merupakan pengetahuan konseptual dasar.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengubah bentuk kata menjadi angka dan menguraikan nilai tempatnya. Tidak ada langkah yang saling bergantung atau kendala yang harus dipecahkan.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sistem nilai tempat bilangan cacah sampai 100.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, membaca bilangan dan menentukan nilai tempat adalah materi dasar yang sudah dikuasai. Soal ini tidak menuntut perencanaan atau integrasi langkah. |

Run 3 — solusi: Mengubah bilangan 'tiga belas ribu lima ratus tujuh puluh delapan' menjadi angka 13.578. Nilai tempat: 1 (puluh ribuan), 3 (ribuan), 5 (ratusan), 7 (puluhan), 8 (satuan).
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan representasi verbal bilangan menjadi angka dan mengidentifikasi nilai tempatnya. Ini adalah prosedur langsung yang melibatkan pengenalan simbol dan pemahaman sistem nilai tempat dasar.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang sistem penulisan bilangan (notasi) dan struktur nilai tempat yang merupakan pengetahuan konseptual dasar dalam matematika.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengubah teks menjadi angka dan memetakan digit ke nilai tempatnya. Tidak ada langkah perencanaan kompleks atau integrasi antar konsep yang diperlukan.. Bukti: tiga belas ribu lima ratus tujuh puluh delapan; tentukan nilai tempatnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sistem nilai tempat sampai puluhan ribu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca dan menulis bilangan sampai 100.000 adalah materi standar kelas 4-5. Tugas ini merupakan penerapan langsung dari konsep tersebut tanpa kerumitan tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 214/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000062; applying=0.999938; reasoning=0.000000 | applying | 0.999938 | 0.000607 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004800; conceptual=0.954657; procedural=0.040543; metacognitive=0.000000 | conceptual | 0.954657 | 0.144186 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.704270; Medium=0.285973; Hard=0.009757 | Easy | 0.704270 | 0.591732 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999938; −Σp ln(p) = 0.000667; H = 0.000667/ln(3) = 0.000607; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.954657; −Σp ln(p) = 0.199884; H = 0.199884/ln(4) = 0.144186; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.704270; −Σp ln(p) = 0.650084; H = 0.650084/ln(3) = 0.591732; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membaca dan Menulis Bilangan Cacah Sampai 100.000 dan Menentukan Nilai Tempatnya
Tipe soal: multiple_choice
Stimulus: -
Soal: Kecamatan Kayu Tanam terletak di Kabupaten Padang Pariaman, Provinsi Sumatra Barat. Pada tahun 2018, penduduk kecamatan ini berjumlah 26.932 jiwa yang terdiri atas 13.354 jiwa laki-laki dan tiga belas ribu lima ratus tujuh puluh delapan jiwa perempuan.

Berdasarkan bacaan tersebut, coba kerjakan beberapa hal berikut.

Tentukanj jumlah penduduk perempuan Kecamatan Kayu Tanam dan tentukan nilai tempatnya.
Pilihan: A. 13.354 (1 puluh ribuan, 3 ribuan, 3 ratusan, 5 puluhan, 4 satuan)
B. 13.587 (1 puluh ribuan, 3 ribuan, 5 ratusan, 8 puluhan, 7 satuan)
C. 130.578 (1 ratus ribuan, 3 puluh ribuan, 0 ribuan, 5 ratusan, 7 puluhan, 8 satuan)
D. 13.578 (1 puluh ribuan, 3 ribuan, 5 ratusan, 7 puluhan, 8 satuan)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `a58707d1174175358f6a4012`

Bacalah bilangan berikut.<br><br>b. Jarak kota Sibolga ke kota New York adalah 15.229 km.

| Opsi | Isi |
|---|---|
| A | lima belas ribu dua ratus dua puluh sembilan |
| B | lima belas ribu sembilan ratus dua puluh dua |
| C | lima belas ribu dua ratus sembilan puluh dua |
| D | lima puluh ribu dua ratus dua puluh sembilan |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bilangan 15.229 terdiri dari 15 ribu, 2 ratus, 2 puluh, dan 9 satuan. Dibaca: lima belas ribu dua ratus dua puluh sembilan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6fc56eac306c0dd04e1e7d7e30adae2d318331a5f71f56556f8edf6bf420fcad`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2302 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3776 |
| 3 | success | valid / verified | knowing | factual | Easy | 2311 |

Run 1 — solusi: Bilangan 15.229 terdiri dari 15 ribu, 2 ratus, 2 puluh, dan 9 satuan. Dibaca: lima belas ribu dua ratus dua puluh sembilan.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca atau melafalkan bilangan cacah sesuai dengan nilai tempatnya. Ini adalah prosedur langsung yang sudah dipelajari di kelas 5.. Bukti: Bacalah bilangan berikut. b. Jarak kota Sibolga ke kota New York adalah 15.229 km.
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang simbol bilangan dan cara membacanya, yang merupakan pengetahuan faktual mengenai sistem penamaan bilangan.. Bukti: 15.229
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah perencanaan atau integrasi yang diperlukan, hanya pengenalan simbol bilangan.. Bukti: Bacalah bilangan berikut. b. Jarak kota Sibolga ke kota New York adalah 15.229 km.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 100.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan adalah materi dasar kelas 5 yang bersifat rutin dan langsung. |

Run 2 — solusi: Bilangan 15.229 terdiri dari 15 ribu, 2 ratus, 2 puluh, dan 9 satuan, sehingga dibaca lima belas ribu dua ratus dua puluh sembilan.
- Domain kognitif `classify/knowing`: Siswa diminta membaca bilangan cacah 15.229. Ini adalah prosedur langsung untuk menerjemahkan simbol angka ke dalam bentuk kata sesuai aturan nilai tempat.. Bukti: Bacalah bilangan berikut; 15.229
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang struktur nilai tempat bilangan cacah hingga 100.000.. Bukti: 15.229
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: 15.229

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan cacah sampai 100.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan adalah keterampilan dasar kelas 5. Soal tidak memerlukan langkah tambahan atau penalaran kompleks. |

Run 3 — solusi: Bilangan 15.229 terdiri dari 15 ribu, 2 ratus, 2 puluh, dan 9 satuan. Dibaca: lima belas ribu dua ratus dua puluh sembilan.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca atau melafalkan bilangan cacah sesuai dengan nilai tempatnya. Ini adalah tugas pengenalan dan pembacaan simbol bilangan yang bersifat langsung.. Bukti: Bacalah bilangan berikut.; Jarak kota Sibolga ke kota New York adalah 15.229 km.
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang sistem penamaan bilangan (fakta) dan nilai tempat dalam bilangan cacah sampai 100.000.. Bukti: 15.229 km
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 5. Membaca bilangan adalah keterampilan rutin yang diajarkan jauh sebelum kelas 5. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Bacalah bilangan berikut.; 15.229

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca bilangan cacah hingga puluhan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan adalah materi dasar yang sudah dikuasai siswa kelas 5. Soal ini tidak menuntut penalaran atau perencanaan, hanya pengenalan simbol bilangan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3587`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal meminta siswa untuk membaca bilangan cacah sesuai dengan nilai tempatnya. Ini adalah tugas pengenalan dan pembacaan simbol bilangan yang bersifat langsung (knowing).
- Dimensi pengetahuan `factual`: Soal menguji pemahaman tentang sistem penamaan bilangan dan nilai tempat, yang merupakan pengetahuan faktual mengenai sistem bilangan.
- Intended difficulty `Easy`: Soal ini sangat mendasar bagi siswa kelas 5. Membaca bilangan adalah keterampilan rutin yang sudah dikuasai. Tidak ada langkah kompleks, perencanaan, atau integrasi konsep yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca bilangan cacah hingga puluhan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan adalah materi dasar yang sudah dikuasai siswa kelas 5. Soal ini tidak menuntut penalaran atau perencanaan, hanya pengenalan simbol bilangan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 105/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.010106; applying=0.989894; reasoning=0.000000 | applying | 0.989894 | 0.051419 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.500689; conceptual=0.482053; procedural=0.017258; metacognitive=0.000000 | factual | 0.500689 | 0.554120 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.920914; Medium=0.077378; Hard=0.001709 | Easy | 0.920914 | 0.259213 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.989894; −Σp ln(p) = 0.056490; H = 0.056490/ln(3) = 0.051419; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.500689; −Σp ln(p) = 0.768174; H = 0.768174/ln(4) = 0.554120; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.920914; −Σp ln(p) = 0.284775; H = 0.284775/ln(3) = 0.259213; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membaca dan Menulis Bilangan Cacah Sampai 100.000 dan Menentukan Nilai Tempatnya
Tipe soal: multiple_choice
Stimulus: -
Soal: Bacalah bilangan berikut.

b. Jarak kota Sibolga ke kota New York adalah 15.229 km.
Pilihan: A. lima belas ribu dua ratus dua puluh sembilan
B. lima belas ribu sembilan ratus dua puluh dua
C. lima belas ribu dua ratus sembilan puluh dua
D. lima puluh ribu dua ratus dua puluh sembilan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `cb199d3a879b430da365173e`

Isilah titik-titik dengan bilangan-bilangan yang sesuai.<br><br>b. ....   50.000   70.000   ....

| Opsi | Isi |
|---|---|
| A | 30.000 dan 90.000 |
| B | 40.000 dan 80.000 |
| C | 60.000 dan 80.000 |
| D | 30.000 dan 80.000 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Selisih antara 70.000 dan 50.000 adalah 20.000. Bilangan pertama adalah 50.000 - 20.000 = 30.000. Bilangan terakhir adalah 70.000 + 20.000 = 90.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ffed5478f58b77a6638a41e0971657b67adc277415bbecc96a1d4fb03824125a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2436 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2420 |
| 3 | success | valid / verified | applying | procedural | Easy | 2375 |

Run 1 — solusi: Pola bilangan adalah urutan naik dengan selisih 20.000. Bilangan pertama sebelum 50.000 adalah 50.000 - 20.000 = 30.000. Bilangan terakhir setelah 70.000 adalah 70.000 + 20.000 = 90.000. Jadi, jawabannya 30.000 dan 90.000.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi pola bilangan sederhana (penambahan konstan) dan melengkapinya. Ini adalah penerapan prosedur familiar dalam konteks rutin.. Bukti: b. ....   50.000   70.000   ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang urutan bilangan dan pola aritmetika sederhana, yang merupakan bagian dari pengetahuan konseptual tentang sistem bilangan.. Bukti: b. ....   50.000   70.000   ....
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menentukan selisih antara dua bilangan yang diketahui (50.000 dan 70.000) dan menerapkan selisih tersebut untuk menemukan bilangan yang hilang. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: b. ....   50.000   70.000   ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi pengurangan/penjumlahan bilangan cacah hingga 100.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi pola bilangan dengan selisih konstan adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Pola bilangan adalah penambahan 20.000. Bilangan sebelum 50.000 adalah 50.000 - 20.000 = 30.000. Bilangan setelah 70.000 adalah 70.000 + 20.000 = 90.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan (selisih) antara dua bilangan yang diketahui (50.000 dan 70.000) dan menerapkan pola tersebut untuk menentukan bilangan yang hilang. Ini adalah penerapan prosedur familiar dalam konteks rutin.. Bukti: Isilah titik-titik dengan bilangan-bilangan yang sesuai.; b. .... 50.000 70.000 ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang urutan bilangan dan pola aritmetika sederhana, yang merupakan pengetahuan konseptual tentang hubungan antar bilangan.. Bukti: 50.000 70.000
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena pola penambahan 20.000 sangat jelas dari dua angka yang berdekatan. Siswa hanya perlu melakukan satu operasi pengurangan dan satu operasi penjumlahan sederhana.. Bukti: b. .... 50.000 70.000 ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi penjumlahan/pengurangan bilangan cacah sampai 100.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi pola bilangan dengan selisih tetap adalah keterampilan dasar yang sudah sering dilatih. |

Run 3 — solusi: Pola bilangan adalah penambahan 20.000 secara konstan. Bilangan sebelum 50.000 adalah 50.000 - 20.000 = 30.000. Bilangan setelah 70.000 adalah 70.000 + 20.000 = 90.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan konstan (20.000) dari dua bilangan yang diberikan, lalu menerapkan pola tersebut untuk menentukan bilangan sebelum dan sesudah. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: 50.000 70.000
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode atau algoritme untuk menentukan selisih antar bilangan dan menerapkannya untuk melengkapi urutan.. Bukti: 50.000 70.000
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengenali pola aritmetika sederhana. Jalur penyelesaian sangat jelas, hanya memerlukan satu operasi pengurangan dan satu operasi penjumlahan dengan selisih yang konsisten.. Bukti: 50.000 70.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 100.000 dan operasi penjumlahan/pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menentukan pola bilangan dengan selisih konstan adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5018`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi pola penambahan konstan (20.000) dari dua bilangan yang diberikan, lalu menerapkan pola tersebut untuk menentukan bilangan yang hilang. Ini adalah penerapan prosedur familiar dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Siswa menggunakan metode atau algoritme (menentukan selisih dan menerapkannya) untuk melengkapi urutan bilangan.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu menentukan selisih antara dua bilangan yang diketahui dan menerapkan selisih tersebut untuk menemukan bilangan yang hilang. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi pengurangan/penjumlahan bilangan cacah hingga 100.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi pola bilangan dengan selisih konstan adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 107/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.135439; applying=0.864561; reasoning=0.000000 | applying | 0.864561 | 0.360997 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.594681; conceptual=0.377596; procedural=0.027723; metacognitive=0.000000 | factual | 0.594681 | 0.559929 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.912188; Medium=0.085388; Hard=0.002425 | Easy | 0.912188 | 0.280847 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.864561; −Σp ln(p) = 0.396596; H = 0.396596/ln(3) = 0.360997; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.594681; −Σp ln(p) = 0.776226; H = 0.776226/ln(4) = 0.559929; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.912188; −Σp ln(p) = 0.308542; H = 0.308542/ln(3) = 0.280847; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan dan Mengurutkan Bilangan Cacah Sampai 100.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik dengan bilangan-bilangan yang sesuai.

b. .... 50.000 70.000 ....
Pilihan: A. 30.000 dan 90.000
B. 40.000 dan 80.000
C. 60.000 dan 80.000
D. 30.000 dan 80.000
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `6b5ab982a459198c7d3f10b6`

Isilah titik-titik dengan bilangan-bilangan yang sesuai.<br><br>c. 85.350   ....   85.450   ....   85.550

| Opsi | Isi |
|---|---|
| A | 85.450 dan 85.550 |
| B | 85.360 dan 85.460 |
| C | 86.350 dan 86.450 |
| D | 85.400 dan 85.500 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola bilangan adalah penambahan 50 pada setiap langkah. Selisih antara 85.350 dan 85.450 adalah 100, sehingga titik di antaranya adalah 85.350 + 50 = 85.400. Demikian pula, titik antara 85.450 dan 85.550 adalah 85.450 + 50 = 85.500. Urutan lengkapnya: 85.350, 85.400, 85.450, 85.500, 85.550.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4ebe9806034912f06083cc45afcc484ff0d9d734f69a21fda8b27645c49a30ac`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2505 |
| 2 | success | valid / verified | applying | procedural | Easy | 2521 |
| 3 | success | valid / verified | applying | procedural | Easy | 2417 |

Run 1 — solusi: Pola bilangan adalah penambahan 100 pada setiap langkah (85.350 + 100 = 85.450; 85.450 + 100 = 85.550). Namun, soal meminta mengisi titik-titik di antara bilangan tersebut. Selisih antara 85.350 dan 85.450 adalah 100. Titik tengahnya adalah 85.350 + 50 = 85.400. Titik tengah antara 85.450 dan 85.550 adalah 85.450 + 50 = 85.500. Jadi, jawabannya 85.400 dan 85.500.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan bilangan cacah dengan menentukan selisih antara dua bilangan yang diketahui dan membaginya untuk mengisi titik-titik di antaranya. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: 85.350 .... 85.450 .... 85.550
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman tentang nilai tempat dan urutan bilangan cacah untuk menentukan pola penambahan yang konsisten.. Bukti: 85.350 .... 85.450 .... 85.550
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengenali pola bilangan sederhana. Langkah penyelesaiannya jelas (menentukan selisih dan membagi dua) dan familiar bagi siswa kelas 5.. Bukti: 85.350 .... 85.450 .... 85.550

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 100.000 dan operasi penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan dan melengkapi pola bilangan cacah adalah materi standar kelas 5. Soal ini tidak memerlukan perencanaan kompleks. |

Run 2 — solusi: Pola bilangan adalah penambahan 100 pada setiap langkah (85.350 + 100 = 85.450; 85.450 + 100 = 85.550). Namun, soal meminta mengisi dua titik-titik di antara bilangan tersebut. Jarak antara 85.350 dan 85.450 adalah 100. Jika diisi satu bilangan di tengah, maka penambahannya adalah 50. Jadi: 85.350 + 50 = 85.400; 85.450 + 50 = 85.500. Urutan: 85.350, 85.400, 85.450, 85.500, 85.550.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan bilangan cacah untuk mengisi titik-titik yang kosong. Ini melibatkan penerapan prosedur aritmatika dasar dalam konteks urutan bilangan yang rutin.. Bukti: 85.350 .... 85.450 .... 85.550
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang urutan bilangan dan pola penambahan (prosedur) yang merupakan bagian dari pengetahuan prosedural dalam matematika.. Bukti: Isilah titik-titik dengan bilangan-bilangan yang sesuai.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menentukan selisih antara bilangan yang diketahui dan menerapkan pola tersebut. Langkah-langkahnya jelas dan rutin bagi siswa kelas 5.. Bukti: 85.350 .... 85.450 .... 85.550

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 100.000 dan operasi penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan pola bilangan adalah materi standar kelas 5. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep yang sulit. |

Run 3 — solusi: Pola bilangan adalah penambahan 50. 85.350 + 50 = 85.400. 85.450 + 50 = 85.500. Jadi, bilangan yang tepat adalah 85.400 dan 85.500.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan konstan pada deret bilangan cacah. Ini adalah penerapan prosedur aritmatika dasar dalam konteks rutin.. Bukti: 85.350 .... 85.450 .... 85.550
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang urutan bilangan dan nilai tempat, yang merupakan pengetahuan prosedural dalam menentukan selisih antar bilangan.. Bukti: 85.350 .... 85.450 .... 85.550
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menentukan selisih antara 85.350 dan 85.450 (yaitu 100), lalu membagi dua untuk menemukan langkah tengah (50). Tidak ada kendala kompleks.. Bukti: 85.350 .... 85.450 .... 85.550

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 100.000 dan operasi penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi pola bilangan dengan selisih konstan adalah tugas yang sangat familiar dan mendasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4315`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi pola penambahan konstan pada deret bilangan cacah dengan menentukan selisih antara dua bilangan yang diketahui dan membaginya untuk mengisi titik-titik di antaranya. Ini adalah penerapan prosedur aritmatika dasar dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang urutan bilangan dan pola penambahan (algoritme/metode) yang merupakan bagian dari pengetahuan prosedural dalam matematika.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menentukan selisih antara 85.350 dan 85.450 (yaitu 100), lalu membagi dua untuk menemukan langkah tengah (50). Tidak ada kendala kompleks atau perencanaan yang sulit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 100.000 dan operasi penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan dan melengkapi pola bilangan cacah adalah materi standar kelas 5. Soal ini tidak memerlukan perencanaan kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 111/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.151006; applying=0.848994; reasoning=0.000000 | applying | 0.848994 | 0.386352 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.728262; conceptual=0.251327; procedural=0.020411; metacognitive=0.000000 | factual | 0.728262 | 0.474245 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.925403; Medium=0.072403; Hard=0.002194 | Easy | 0.925403 | 0.250563 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.848994; −Σp ln(p) = 0.424451; H = 0.424451/ln(3) = 0.386352; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.728262; −Σp ln(p) = 0.657443; H = 0.657443/ln(4) = 0.474245; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.925403; −Σp ln(p) = 0.275272; H = 0.275272/ln(3) = 0.250563; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan dan Mengurutkan Bilangan Cacah Sampai 100.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik dengan bilangan-bilangan yang sesuai.

c. 85.350 .... 85.450 .... 85.550
Pilihan: A. 85.450 dan 85.550
B. 85.360 dan 85.460
C. 86.350 dan 86.450
D. 85.400 dan 85.500
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `e05bf2067c83ab344656d352`

Ibu Saga berbelanja di pasar sebesar Rp59.000,00. Jika di dompet Ibu Saga ada 2 lembar uang Rp20.000,00; 3 lembar uang Rp10.000,00; 2 lembar uang Rp5.000,00; dan 5 lembar uang Rp2.000,00; berapa komposisi cara membayar yang mungkin dilakukan?

| Opsi | Isi |
|---|---|
| A | 4 cara |
| B | 1 cara |
| C | 3 cara |
| D | 2 cara |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Target Rp59.000. Wajib menggunakan 1x5.000 dan 2x2.000 untuk mendapatkan Rp9.000 (karena denominasi lain kelipatan 10.000). Sisa Rp50.000 harus dibentuk dari 2x20.000 dan 3x10.000. Kombinasi yang mungkin: (1) 2x20.000 + 1x10.000 + 1x5.000 + 2x2.000 = 59.000. (2) 1x20.000 + 3x10.000 + 1x5.000 + 2x2.000 = 59.000. Total 2 cara.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `238272f167e548ab7bc7fbb2242fa5fc94a00c9c5b17d73b6c0bae936ddefc72`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2636 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 4336 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 2534 |

Run 1 — solusi: Total belanja Rp59.000. Tersedia: 2x20rb, 3x10rb, 2x5rb, 5x2rb. Kombinasi yang mungkin: (1) 2x20rb + 1x10rb + 1x5rb + 2x2rb = 40+10+5+4 = 59rb. (2) 1x20rb + 3x10rb + 1x5rb + 2x2rb = 20+30+5+4 = 59rb. Tidak ada kombinasi lain yang memenuhi batasan jumlah lembar uang yang tersedia.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi kombinasi nilai uang yang tepat untuk mencapai target Rp59.000 dengan batasan jumlah lembar uang yang tersedia. Ini memerlukan pemilihan dan penerapan strategi sistematis untuk menemukan semua kemungkinan kombinasi yang valid.. Bukti: berapa komposisi cara membayar yang mungkin dilakukan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang komposisi dan dekomposisi bilangan (nilai uang) dalam konteks pemecahan masalah, yang merupakan pengetahuan konseptual tentang bagaimana angka dapat dibentuk dari bagian-bagiannya.. Bukti: komposisi cara membayar yang mungkin dilakukan
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan pencarian sistematis (trial and error yang terarah) dengan batasan (constraint) jumlah lembar uang yang tersedia. Siswa harus mengelola beberapa variabel secara bersamaan untuk memastikan totalnya tepat Rp59.000. Ini melampaui sekadar operasi hitung rutin karena memerlukan perencanaan langkah untuk mengecek kombinasi yang valid.. Bukti: berapa komposisi cara membayar yang mungkin dilakukan?; 2 lembar uang Rp20.000,00; 3 lembar uang Rp10.000,00; 2 lembar uang Rp5.000,00; dan 5 lembar uang Rp2.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100.000 dan pemahaman nilai tempat/mata uang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 4 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu melakukan operasi hitung dasar, namun mengelola batasan jumlah lembar uang (constraint) untuk menemukan semua kombinasi yang mungkin memerlukan ketelitian dan perencanaan yang lebih dari sekadar soal rutin satu langkah. |

Run 2 — solusi: Target 59.000. Wajib menggunakan 1x5.000 dan 2x2.000 untuk mendapatkan 9.000. Sisa 50.000 dapat dibentuk dari (2x20.000 + 1x10.000) atau (1x20.000 + 3x10.000). Total 2 cara.
- Domain kognitif `classify/reasoning`: Siswa harus melakukan analisis sistematis untuk menemukan kombinasi yang mungkin dengan kendala jumlah uang yang tersedia, bukan sekadar menghitung.. Bukti: berapa komposisi cara membayar yang mungkin dilakukan
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman tentang konsep komposisi dan dekomposisi bilangan dalam konteks nilai mata uang.. Bukti: komposisi cara membayar
- Intended difficulty `classify/Medium`: Siswa perlu merencanakan langkah (memisahkan 9.000) dan menguji kombinasi dengan kendala jumlah uang. Ini melibatkan beberapa langkah saling terkait namun masih dalam batas kemampuan kelas 5.. Bukti: berapa komposisi cara membayar yang mungkin dilakukan; 2 lembar uang Rp20.000,00; 3 lembar uang Rp10.000,00; 2 lembar uang Rp5.000,00; dan 5 lembar uang Rp2.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan sampai 100.000, konsep nilai mata uang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas ini menuntut penalaran kombinatorik sederhana yang sesuai untuk kelas 5, di mana siswa harus mengelola kendala jumlah uang yang tersedia. |

Run 3 — solusi: Total belanja Rp59.000. Tersedia: 2x20rb, 3x10rb, 2x5rb, 5x2rb. Kombinasi yang mungkin: (1) 2x20rb + 1x10rb + 1x5rb + 2x2rb = 40+10+5+4 = 59rb. (2) 1x20rb + 3x10rb + 1x5rb + 2x2rb = 20+30+5+4 = 59rb. Tidak ada kombinasi lain yang memenuhi batasan jumlah lembar uang.
- Domain kognitif `classify/reasoning`: Siswa harus menguji kombinasi nilai uang yang tersedia untuk mencapai target jumlah tertentu (Rp59.000) dengan batasan jumlah lembar uang yang ada. Ini memerlukan penalaran sistematis untuk menemukan semua kemungkinan yang valid.. Bukti: berapa komposisi cara membayar yang mungkin dilakukan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang dekomposisi bilangan (nilai uang) ke dalam bagian-bagian yang lebih kecil dengan batasan kuantitas tertentu.. Bukti: komposisi cara membayar yang mungkin dilakukan
- Intended difficulty `classify/Hard`: Soal ini menuntut siswa melakukan pencarian sistematis (trial and error yang terstruktur) untuk menemukan kombinasi yang memenuhi target jumlah dan batasan ketersediaan uang. Siswa harus mengelola beberapa kendala sekaligus (jumlah total dan jumlah lembar per denominasi), yang cukup menantang untuk kelas 5.. Bukti: berapa komposisi cara membayar yang mungkin dilakukan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan perkalian bilangan cacah dasar, pemahaman nilai tempat/mata uang. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 4 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi dasarnya sederhana, kebutuhan untuk menguji kombinasi secara sistematis tanpa bantuan langkah-langkah membuat soal ini memiliki tuntutan kognitif yang tinggi bagi siswa kelas 5. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "reasoning": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Hard": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4507`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus mengintegrasikan batasan ketersediaan lembar uang dengan target jumlah belanja. Ini bukan sekadar menghitung, melainkan menentukan strategi untuk menguji kombinasi yang valid secara sistematis.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang dekomposisi bilangan (nilai uang) ke dalam bagian-bagian yang lebih kecil dengan batasan kuantitas tertentu.
- Intended difficulty `Medium`: Soal ini menuntut perencanaan langkah yang saling bergantung. Siswa harus menyadari bahwa Rp9.000 harus dibentuk dari pecahan Rp5.000 dan Rp2.000, lalu mengelola sisa Rp50.000 dengan batasan lembar uang yang ada. Meskipun prosedurnya familiar, kebutuhan untuk membangun strategi pengujian kombinasi tanpa bantuan langkah membuat ini memiliki tuntutan kognitif yang cukup tinggi bagi kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan perkalian bilangan cacah, pemahaman nilai mata uang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 4 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas ini menuntut penalaran kombinatorik sederhana yang sesuai untuk kelas 5, di mana siswa harus mengelola kendala jumlah uang yang tersedia secara sistematis. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 126/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.216964; conceptual=0.769815; procedural=0.013221; metacognitive=0.000000 | conceptual | 0.769815 | 0.425671 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.839911; Medium=0.155162; Hard=0.004927 | Easy | 0.839911 | 0.420366 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.769815; −Σp ln(p) = 0.590105; H = 0.590105/ln(4) = 0.425671; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.839911; −Σp ln(p) = 0.461819; H = 0.461819/ln(3) = 0.420366; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Komposisi dan Dekomposisi Bilangan Sampai 100.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Saga berbelanja di pasar sebesar Rp59.000,00. Jika di dompet Ibu Saga ada 2 lembar uang Rp20.000,00; 3 lembar uang Rp10.000,00; 2 lembar uang Rp5.000,00; dan 5 lembar uang Rp2.000,00; berapa komposisi cara membayar yang mungkin dilakukan?
Pilihan: A. 4 cara
B. 1 cara
C. 3 cara
D. 2 cara
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `48a418e26c40fb4de2a1783c`

Tuliskan bilangan berikut angka dan bacalah.<br><br>c. Bilangan yang merupakan jumlah dari 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan.

| Opsi | Isi |
|---|---|
| A | 97.005, dibaca sembilan puluh tujuh ribu lima |
| B | 79.500, dibaca tujuh puluh sembilan ribu lima ratus |
| C | 97.050, dibaca sembilan puluh tujuh ribu lima puluh |
| D | 97.500, dibaca sembilan puluh tujuh ribu lima ratus |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 9 x 10.000 + 7 x 1.000 + 5 x 100 = 90.000 + 7.000 + 500 = 97.500. Dibaca: sembilan puluh tujuh ribu lima ratus.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6e0c0471f21f53207c1a70fbf5e3e1d525b687ae28db0bc14e01894ea84f7a8e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2407 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2395 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2401 |

Run 1 — solusi: 9 x 10.000 + 7 x 1.000 + 5 x 100 = 90.000 + 7.000 + 500 = 97.500. Dibaca: sembilan puluh tujuh ribu lima ratus.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menyusun bilangan berdasarkan nilai tempat yang diberikan secara eksplisit. Ini adalah prosedur langsung untuk mengonversi bentuk penjumlahan nilai tempat menjadi notasi standar.. Bukti: jumlah dari 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang sistem nilai tempat (place value) dan bagaimana angka disusun dari komponen-komponen penyusunnya.. Bukti: 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan nilai tempat dengan jumlah lembar/keping yang diberikan dan menjumlahkannya. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai 100.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menyusun bilangan dari nilai tempat adalah materi dasar yang sudah dikuasai. Soal tidak memiliki jebakan atau kompleksitas tambahan. |

Run 2 — solusi: 9 lembar sepuluh ribuan = 90.000; 7 lembar seribuan = 7.000; 5 keping seratusan = 500. Jumlahkan: 90.000 + 7.000 + 500 = 97.500.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan komposisi bilangan berdasarkan nilai tempat yang diberikan secara eksplisit. Ini adalah prosedur langsung yang sudah dipelajari di kelas 5.. Bukti: jumlah dari 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang sistem nilai tempat (place value) dan bagaimana angka disusun dari komponen-komponennya.. Bukti: 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan nilai tempat dengan jumlah lembar/keping yang diberikan dan menjumlahkannya. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat sampai puluhan ribu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, komposisi bilangan sampai 100.000 adalah materi dasar yang rutin. Soal ini tidak memerlukan perencanaan kompleks. |

Run 3 — solusi: 9 lembar sepuluh ribuan = 90.000; 7 lembar seribuan = 7.000; 5 keping seratusan = 500. Jumlah = 90.000 + 7.000 + 500 = 97.500.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan komposisi bilangan berdasarkan nilai tempat yang diberikan secara eksplisit. Ini adalah prosedur langsung yang familiar bagi siswa kelas 5.. Bukti: Bilangan yang merupakan jumlah dari 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang struktur nilai tempat (ribuan, puluh ribuan, ratusan) dan bagaimana elemen-elemen tersebut dikomposisikan menjadi satu bilangan utuh.. Bukti: 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menjumlahkan nilai tempat yang diberikan tanpa ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.. Bukti: 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai 100.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, komposisi bilangan berdasarkan nilai tempat adalah materi dasar yang sudah sering dilatih. Tidak ada kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 123/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001310; applying=0.998690; reasoning=0.000000 | applying | 0.998690 | 0.009108 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.332942; conceptual=0.656143; procedural=0.010915; metacognitive=0.000000 | conceptual | 0.656143 | 0.499143 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.883831; Medium=0.112769; Hard=0.003400 | Easy | 0.883831 | 0.340956 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998690; −Σp ln(p) = 0.010006; H = 0.010006/ln(3) = 0.009108; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.656143; −Σp ln(p) = 0.691960; H = 0.691960/ln(4) = 0.499143; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.883831; −Σp ln(p) = 0.374579; H = 0.374579/ln(3) = 0.340956; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Komposisi dan Dekomposisi Bilangan Sampai 100.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Tuliskan bilangan berikut angka dan bacalah.

c. Bilangan yang merupakan jumlah dari 9 lembar sepuluh ribuan, 7 lembar seribuan, dan 5 keping seratusan.
Pilihan: A. 97.005, dibaca sembilan puluh tujuh ribu lima
B. 79.500, dibaca tujuh puluh sembilan ribu lima ratus
C. 97.050, dibaca sembilan puluh tujuh ribu lima puluh
D. 97.500, dibaca sembilan puluh tujuh ribu lima ratus
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `0540aa26f4da9da27f7785db`

Toko Zafran menjual beberapa jenis buah, di antaranya mangga, alpukat, jeruk, buah naga, dan kelengkeng. Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00; harga satu bungkus kelengkeng Rp34.000,00; harga satu bungkus buah naga Rp15.000,00; dan harga satu bungkus alpukat Rp32.000,00.<br><br>Yohana membeli dua bungkus mangga dan satu bungkus jeruk. Berapa uang yang harus ia bayarkan?

| Opsi | Isi |
|---|---|
| A | Rp40.500,00 |
| B | Rp81.000,00 |
| C | Rp64.000,00 |
| D | Rp63.000,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Total = (2 x 23.500) + 17.000 = 47.000 + 17.000 = 64.000
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe02f2f076f8aab24fa908213160d27c5bb686891f40e5be624f335d3b649674`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2490 |
| 2 | success | valid / verified | applying | procedural | Easy | 2518 |
| 3 | success | valid / verified | applying | procedural | Easy | 2544 |

Run 1 — solusi: Total = (2 x 23.500) + 17.000 = 47.000 + 17.000 = 64.000
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi perkalian dan penjumlahan bilangan cacah pada konteks rutin (belanja). Prosedur penyelesaiannya langsung dan sudah umum dipelajari.. Bukti: Yohana membeli dua bungkus mangga dan satu bungkus jeruk. Berapa uang yang harus ia bayarkan?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian dan penjumlahan bilangan cacah dalam konteks harga barang.. Bukti: Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas dan rutin bagi siswa kelas 5. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Yohana membeli dua bungkus mangga dan satu bungkus jeruk.; Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian dan penjumlahan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan operasi hitung campuran sederhana dalam konteks kehidupan sehari-hari seperti transaksi jual beli. |

Run 2 — solusi: Total = (2 * 23.500) + 17.000 = 47.000 + 17.000 = 64.000
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi perkalian dan penjumlahan bilangan cacah pada konteks rutin (belanja). Prosedur penyelesaian bersifat langsung dan familiar bagi siswa kelas 5.. Bukti: Yohana membeli dua bungkus mangga dan satu bungkus jeruk. Berapa uang yang harus ia bayarkan?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian dan penjumlahan bilangan cacah untuk menyelesaikan masalah kontekstual.. Bukti: Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00; Yohana membeli dua bungkus mangga dan satu bungkus jeruk.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaian sangat jelas, hanya melibatkan dua operasi dasar (perkalian dan penjumlahan) dengan data yang eksplisit. Tidak ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi nonrutin.. Bukti: Yohana membeli dua bungkus mangga dan satu bungkus jeruk.; Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung perkalian dan penjumlahan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan operasi hitung bilangan cacah hingga puluhan ribu dan penerapan dalam soal cerita sederhana. |

Run 3 — solusi: Total = (2 x 23.500) + 17.000 = 47.000 + 17.000 = 64.000
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi perkalian dan penjumlahan bilangan cacah dalam konteks rutin (transaksi belanja). Prosedur penyelesaian bersifat langsung dan familiar bagi siswa kelas 5.. Bukti: Yohana membeli dua bungkus mangga dan satu bungkus jeruk. Berapa uang yang harus ia bayarkan?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian dan penjumlahan bilangan cacah yang sudah dipelajari sebagai metode standar untuk menyelesaikan masalah harga.. Bukti: Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00; Yohana membeli dua bungkus mangga dan satu bungkus jeruk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaian sangat jelas, hanya melibatkan dua operasi dasar (perkalian dan penjumlahan) dengan data yang eksplisit. Tidak ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.. Bukti: Yohana membeli dua bungkus mangga dan satu bungkus jeruk.; Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian dan penjumlahan bilangan cacah sampai 100.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan soal cerita transaksi belanja yang melibatkan operasi hitung dasar. Langkah-langkah penyelesaian bersifat linear dan tidak memerlukan perencanaan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 177/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.005287; conceptual=0.993407; procedural=0.001305; metacognitive=0.000000 | conceptual | 0.993407 | 0.030988 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.757163; Medium=0.230706; Hard=0.012132 | Easy | 0.757163 | 0.548423 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.993407; −Σp ln(p) = 0.042958; H = 0.042958/ln(4) = 0.030988; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.757163; −Σp ln(p) = 0.602505; H = 0.602505/ln(3) = 0.548423; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Operasi Hitung pada Bilangan Cacah Sampai 100.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Toko Zafran menjual beberapa jenis buah, di antaranya mangga, alpukat, jeruk, buah naga, dan kelengkeng. Harga satu bungkus mangga Rp23.500,00; harga satu bungkus jeruk Rp17.000,00; harga satu bungkus kelengkeng Rp34.000,00; harga satu bungkus buah naga Rp15.000,00; dan harga satu bungkus alpukat Rp32.000,00.

Yohana membeli dua bungkus mangga dan satu bungkus jeruk. Berapa uang yang harus ia bayarkan?
Pilihan: A. Rp40.500,00
B. Rp81.000,00
C. Rp64.000,00
D. Rp63.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `620215ae8a2b079133b0233a`

Tentukan hasil dan nilai tempat dari operasi bilangan berikut.<br><br>b. 67.987 – 13.453 =

| Opsi | Isi |
|---|---|
| A | 53.534 |
| B | 54.434 |
| C | 54.534 |
| D | 81.440 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 67.987 - 13.453 = 54.534
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6864b8dd3f540e6b4904c168ba9d10cb58a179d6da57fef82248f53042dd2392`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2231 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2290 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2305 |

Run 1 — solusi: 67.987 - 13.453 = 54.534
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan bilangan cacah sampai 100.000 secara langsung. Ini adalah prosedur rutin yang sudah dipelajari di kelas 5.. Bukti: 67.987 – 13.453 =
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan algoritma pengurangan bersusun standar untuk menyelesaikan operasi bilangan cacah.. Bukti: 67.987 – 13.453 =
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan bilangan cacah standar tanpa teknik meminjam yang kompleks atau kendala tambahan. Jalur penyelesaian sangat jelas dan familiar bagi siswa kelas 5.. Bukti: 67.987 – 13.453 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan algoritma pengurangan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan bilangan lima angka adalah materi dasar kelas 5. Soal tidak memiliki jebakan atau tuntutan penalaran tambahan. |

Run 2 — solusi: 67.987 - 13.453 = 54.534. Pengurangan dilakukan per nilai tempat: 7-3=4 (satuan), 8-5=3 (puluhan), 9-4=5 (ratusan), 7-3=4 (ribuan), 6-1=5 (puluh ribuan). Hasilnya 54.534.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan bilangan cacah sampai 100.000 secara langsung. Ini adalah prosedur standar yang sudah dipelajari di kelas 5.. Bukti: 67.987 – 13.453 =
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan algoritma pengurangan bersusun untuk menyelesaikan operasi hitung bilangan cacah.. Bukti: 67.987 – 13.453 =
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan bilangan cacah yang rutin dan langsung. Tidak ada langkah tambahan atau kendala yang perlu diintegrasikan.. Bukti: 67.987 – 13.453 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan algoritma pengurangan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan bilangan cacah sampai 100.000 adalah materi dasar kelas 5 yang bersifat rutin. |

Run 3 — solusi: 67.987 - 13.453 = 54.534. Pengurangan dilakukan per nilai tempat: 7-3=4 (satuan), 8-5=3 (puluhan), 9-4=5 (ratusan), 7-3=4 (ribuan), 6-1=5 (puluh ribuan). Hasilnya 54.534.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan bilangan cacah lima angka secara langsung. Ini adalah prosedur rutin yang sudah dipelajari di kelas sebelumnya dan diperkuat di kelas 5.. Bukti: 67.987 – 13.453 =
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan algoritma pengurangan standar (prosedural) untuk menyelesaikan operasi hitung bilangan cacah.. Bukti: 67.987 – 13.453 =
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan langsung tanpa teknik meminjam yang rumit atau kendala tambahan. Jalur penyelesaian sangat jelas dan familiar bagi siswa kelas 5.. Bukti: 67.987 – 13.453 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi pengurangan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan bilangan lima angka adalah materi dasar yang sudah dikuasai siswa kelas 5. Tidak ada tuntutan perencanaan atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.994065; applying=0.005935; reasoning=0.000000 | knowing | 0.994065 | 0.033084 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.845697; conceptual=0.114128; procedural=0.040175; metacognitive=0.000000 | factual | 0.845697 | 0.374080 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.927412; Medium=0.070471; Hard=0.002117 | Easy | 0.927412 | 0.245628 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.994065; −Σp ln(p) = 0.036347; H = 0.036347/ln(3) = 0.033084; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.845697; −Σp ln(p) = 0.518584; H = 0.518584/ln(4) = 0.374080; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.927412; −Σp ln(p) = 0.269850; H = 0.269850/ln(3) = 0.245628; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Operasi Hitung pada Bilangan Cacah Sampai 100.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan hasil dan nilai tempat dari operasi bilangan berikut.

b. 67.987 – 13.453 =
Pilihan: A. 53.534
B. 54.434
C. 54.534
D. 81.440
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `bc95fc44d6c120fad4812c7c`

Slamet membantu ibu membagikan beras kepada masyarakat kurang mampu. Total beras yang dibagikan oleh Ibu Slamet 10 kg. Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama. Bantulah ibu Slamet untuk membagikan beras tersebut. Tuliskan kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?

| Opsi | Isi |
|---|---|
| A | 10 orang, 20 orang, 30 orang, atau 40 orang |
| B | 1 orang, 2 orang, 5 orang, atau 10 orang |
| C | 2 orang, 3 orang, 4 orang, atau 5 orang |
| D | 1 orang, 2 orang, 3 orang, 5 orang, atau 10 orang |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Total beras 10 kg dibagi sama rata ke n orang, maka n harus merupakan faktor dari 10. Faktor dari 10 adalah 1, 2, 5, dan 10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4afe3650401c5a1d8582e4c675cec6fcbea275d6b16886fca90e427a3be2b882`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2386 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2370 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2425 |

Run 1 — solusi: Total beras 10 kg dibagi sama rata ke n orang, maka n harus merupakan faktor dari 10. Faktor dari 10 adalah 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep faktor sebagai pembagi yang menghasilkan sisa nol dalam konteks pembagian sama rata. Ini melibatkan penerapan konsep faktor pada situasi nyata.. Bukti: Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama.; Tuliskan kemungkinan banyaknya orang yang akan mendapat pembagian beras
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pembagian bilangan bulat dan faktor bilangan.. Bukti: kemungkinan banyaknya orang yang akan mendapat pembagian beras; berat yang sama
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengidentifikasi faktor dari 10. Tidak ada kendala yang berinteraksi atau langkah yang kompleks.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg.; membagikan semua beras ke beberapa orang dengan berat yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari faktor bilangan. Menentukan faktor dari 10 adalah tugas rutin yang sesuai dengan tingkat kelas. |

Run 2 — solusi: Total beras 10 kg harus dibagi sama rata, artinya jumlah orang harus merupakan faktor dari 10. Faktor dari 10 adalah bilangan yang dapat membagi habis 10, yaitu 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep faktor sebagai pembagi yang menghasilkan sisa nol dalam konteks pembagian beras. Ini melibatkan penerapan konsep faktor pada situasi rutin.. Bukti: membagikan semua beras ke beberapa orang dengan berat yang sama; kemungkinan banyaknya orang yang akan mendapat pembagian beras
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pembagian dan faktor bilangan.. Bukti: membagikan semua beras ke beberapa orang dengan berat yang sama
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengidentifikasi faktor dari 10. Jalur penyelesaiannya langsung dan familiar bagi siswa kelas 5.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg; membagikan semua beras ke beberapa orang dengan berat yang sama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor dari bilangan kecil (10) adalah materi standar kelas 5 yang bersifat rutin. |

Run 3 — solusi: Mencari faktor dari 10. Bilangan yang dapat membagi habis 10 adalah 1, 2, 5, dan 10. Maka, kemungkinan banyaknya orang adalah 1, 2, 5, atau 10 orang.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pembagian rata (tanpa sisa) yang berkaitan dengan konsep faktor bilangan. Siswa menerapkan pemahaman faktor untuk menentukan kemungkinan jumlah orang yang dapat menerima beras secara merata.. Bukti: Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama.; Tuliskan kemungkinan banyaknya orang yang akan mendapat pembagian beras
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang faktor bilangan dalam konteks pembagian yang adil.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg.; membagikan semua beras ke beberapa orang dengan berat yang sama
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengidentifikasi faktor dari bilangan 10 yang merupakan konsep dasar kelas 5. Jalur penyelesaian langsung dan tidak memerlukan perencanaan langkah yang kompleks.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg.; membagikan semua beras ke beberapa orang dengan berat yang sama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan faktor dari bilangan kecil (10) adalah materi standar kelas 5 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 150/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.006632; conceptual=0.957933; procedural=0.035435; metacognitive=0.000000 | conceptual | 0.957933 | 0.139069 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.753520; Medium=0.240010; Hard=0.006470 | Easy | 0.753520 | 0.535558 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.957933; −Σp ln(p) = 0.192791; H = 0.192791/ln(4) = 0.139069; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.753520; −Σp ln(p) = 0.588370; H = 0.588370/ln(3) = 0.535558; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Faktor dan Kelipatan
Tipe soal: multiple_choice
Stimulus: -
Soal: Slamet membantu ibu membagikan beras kepada masyarakat kurang mampu. Total beras yang dibagikan oleh Ibu Slamet 10 kg. Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama. Bantulah ibu Slamet untuk membagikan beras tersebut. Tuliskan kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
Pilihan: A. 10 orang, 20 orang, 30 orang, atau 40 orang
B. 1 orang, 2 orang, 5 orang, atau 10 orang
C. 2 orang, 3 orang, 4 orang, atau 5 orang
D. 1 orang, 2 orang, 3 orang, 5 orang, atau 10 orang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `a2afbcfa3b4617cdf0f3a8f2`

Manakah yang termasuk 5 bilangan kelipatan 6.

| Opsi | Isi |
|---|---|
| A | 6, 11, 16, 21, 26 |
| B | 6, 12, 18, 24, 30 |
| C | 1, 2, 3, 6, 12 |
| D | 6, 12, 18, 24, 32 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kelipatan 6 adalah hasil perkalian 6 dengan bilangan asli (1, 2, 3, 4, 5). Maka: 6x1=6, 6x2=12, 6x3=18, 6x4=24, 6x5=30. Deret yang benar adalah 6, 12, 18, 24, 30.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `84bbf3a926c6e24236e69edae3414e8e4393aa6144c6a0639d378ee8d7db1883`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2310 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2335 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2327 |

Run 1 — solusi: Kelipatan 6 diperoleh dengan mengalikan 6 dengan bilangan asli berurutan (1, 2, 3, 4, 5). Hasilnya adalah 6x1=6, 6x2=12, 6x3=18, 6x4=24, 6x5=30.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat definisi kelipatan dan melakukan operasi perkalian dasar atau penjumlahan berulang untuk mengidentifikasi deret yang benar.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 6.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep dasar kelipatan bilangan.. Bukti: 5 bilangan kelipatan 6
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala yang kompleks. Siswa hanya perlu mengenali deret kelipatan 6 yang benar.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 6.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kelipatan adalah topik dasar kelas 4-5. Soal ini tidak menuntut perencanaan atau integrasi konsep yang rumit. |

Run 2 — solusi: Kelipatan 6 diperoleh dengan mengalikan 6 dengan bilangan asli berurutan (1, 2, 3, 4, 5). Hasilnya adalah 6x1=6, 6x2=12, 6x3=18, 6x4=24, 6x5=30.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi deret bilangan yang merupakan kelipatan dari 6. Ini adalah prosedur langsung yang melibatkan pengenalan pola perkalian dasar yang sudah dipelajari di kelas 5.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 6.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep kelipatan sebagai hasil perkalian bilangan dengan bilangan asli, yang merupakan pengetahuan konseptual dasar.. Bukti: 5 bilangan kelipatan 6
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan perkalian dasar atau penjumlahan berulang untuk memverifikasi opsi. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 6.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dasar dan konsep kelipatan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, konsep kelipatan adalah materi dasar yang sudah dikuasai. Soal ini tidak menuntut perencanaan atau integrasi konsep yang rumit. |

Run 3 — solusi: Kelipatan 6 diperoleh dengan mengalikan 6 dengan bilangan asli berurutan (1, 2, 3, 4, 5). Hasilnya adalah 6x1=6, 6x2=12, 6x3=18, 6x4=24, 6x5=30. Jadi, 6, 12, 18, 24, 30.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menjalankan prosedur dasar menentukan kelipatan suatu bilangan dengan perkalian berurutan.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 6.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghasilkan kelipatan bilangan.. Bukti: 5 bilangan kelipatan 6
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu melakukan perkalian dasar atau penjumlahan berulang untuk mengidentifikasi deret kelipatan 6. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 6.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kelipatan adalah dasar di kelas 5. Soal ini meminta identifikasi langsung tanpa manipulasi tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3742`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengingat definisi kelipatan dan melakukan operasi perkalian dasar atau penjumlahan berulang untuk mengidentifikasi deret yang benar. Ini adalah prosedur langsung.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep dasar kelipatan bilangan sebagai hasil perkalian.
- Intended difficulty `Easy`: Soal ini sangat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala yang kompleks. Siswa hanya perlu mengenali deret kelipatan 6 yang benar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kelipatan adalah topik dasar kelas 4-5. Soal ini tidak menuntut perencanaan atau integrasi konsep yang rumit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 85/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.783856; applying=0.216144; reasoning=0.000000 | knowing | 0.783856 | 0.475130 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.485040; conceptual=0.483915; procedural=0.031045; metacognitive=0.000000 | factual | 0.485040 | 0.584280 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873165; Medium=0.124450; Hard=0.002385 | Easy | 0.873165 | 0.356963 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.783856; −Σp ln(p) = 0.521984; H = 0.521984/ln(3) = 0.475130; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.485040; −Σp ln(p) = 0.809984; H = 0.809984/ln(4) = 0.584280; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873165; −Σp ln(p) = 0.392164; H = 0.392164/ln(3) = 0.356963; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Kelipatan
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah yang termasuk 5 bilangan kelipatan 6.
Pilihan: A. 6, 11, 16, 21, 26
B. 6, 12, 18, 24, 30
C. 1, 2, 3, 6, 12
D. 6, 12, 18, 24, 32
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `832752421f3344f9b02244e9`

Manakah yang termasuk 5 bilangan kelipatan 8.

| Opsi | Isi |
|---|---|
| A | 4, 8, 12, 16, 20 |
| B | 1, 2, 4, 8 |
| C | 8, 16, 24, 32, 40 |
| D | 8, 18, 28, 38, 48 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Kelipatan 8 adalah hasil perkalian 8 dengan bilangan asli (1, 2, 3, 4, 5). 8x1=8, 8x2=16, 8x3=24, 8x4=32, 8x5=40. Jadi, 5 bilangan kelipatan 8 yang pertama adalah 8, 16, 24, 32, 40.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4faad05f39584e1c7e33b6b4a46030e7c61f35cebef34223a3abff43aee4ee11`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2317 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2313 |
| 3 | success | valid / verified | knowing | factual | Easy | 2941 |

Run 1 — solusi: Kelipatan 8 diperoleh dengan mengalikan 8 dengan bilangan asli berurutan (1, 2, 3, 4, 5). 8x1=8, 8x2=16, 8x3=24, 8x4=32, 8x5=40. Jadi, 8, 16, 24, 32, 40.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi deret bilangan yang merupakan kelipatan dari 8. Ini adalah prosedur langsung yang melibatkan pengenalan konsep kelipatan dasar.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi atau konsep kelipatan bilangan, yang merupakan pengetahuan konseptual dasar dalam matematika.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala kompleks. Siswa hanya perlu mengenali deret kelipatan 8.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kelipatan adalah materi dasar kelas 4/5. Soal ini tidak memerlukan perencanaan atau integrasi langkah, sehingga dikategorikan mudah. |

Run 2 — solusi: Kelipatan 8 diperoleh dengan mengalikan 8 dengan bilangan asli berurutan (1, 2, 3, 4, 5). Hasilnya adalah 8x1=8, 8x2=16, 8x3=24, 8x4=32, dan 8x5=40.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat definisi kelipatan dan melakukan perkalian dasar atau penjumlahan berulang untuk mengidentifikasi deret yang benar.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang kelipatan bilangan.. Bukti: 5 bilangan kelipatan 8
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan kelipatan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kelipatan adalah materi dasar kelas 4/5. Soal ini meminta identifikasi langsung tanpa manipulasi tambahan. |

Run 3 — solusi: Kelipatan 8 diperoleh dengan mengalikan 8 dengan bilangan asli berurutan (1, 2, 3, 4, 5), yaitu 8x1=8, 8x2=16, 8x3=24, 8x4=32, 8x5=40.
- Domain kognitif `classify/knowing`: Soal hanya meminta identifikasi langsung dari definisi kelipatan suatu bilangan, yang merupakan prosedur dasar dan sangat langsung bagi siswa kelas 5.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar mengenai kelipatan bilangan, yaitu hasil perkalian bilangan tersebut dengan bilangan asli.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu mengenali deret kelipatan 8 yang benar. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Manakah yang termasuk 5 bilangan kelipatan 8.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perkalian dan konsep kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kelipatan adalah materi dasar kelas 4/5. Soal ini tidak menuntut perencanaan atau integrasi, hanya pengenalan pola kelipatan sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3736`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan prosedur rutin yaitu mengalikan 8 dengan bilangan asli berurutan atau menjumlahkan 8 secara berulang untuk mengidentifikasi deret yang benar. Tidak ada penalaran non-rutin yang diperlukan.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang definisi kelipatan, yang merupakan konsep dasar dalam aritmetika.
- Intended difficulty `Easy`: Soal ini sangat rutin dan langsung. Siswa hanya perlu menerapkan definisi kelipatan. Tidak ada langkah yang saling bergantung, kendala yang berinteraksi, atau kebutuhan untuk merencanakan strategi. Beban kognitif sangat rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kelipatan adalah materi dasar kelas 4/5. Soal ini tidak memerlukan perencanaan atau integrasi langkah, sehingga dikategorikan mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 83/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.842054; applying=0.157946; reasoning=0.000000 | knowing | 0.842054 | 0.397091 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.540879; conceptual=0.431375; procedural=0.027746; metacognitive=0.000000 | factual | 0.540879 | 0.573150 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.874725; Medium=0.122991; Hard=0.002284 | Easy | 0.874725 | 0.353825 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.842054; −Σp ln(p) = 0.436249; H = 0.436249/ln(3) = 0.397091; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.540879; −Σp ln(p) = 0.794554; H = 0.794554/ln(4) = 0.573150; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.874725; −Σp ln(p) = 0.388716; H = 0.388716/ln(3) = 0.353825; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Kelipatan
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah yang termasuk 5 bilangan kelipatan 8.
Pilihan: A. 4, 8, 12, 16, 20
B. 1, 2, 4, 8
C. 8, 16, 24, 32, 40
D. 8, 18, 28, 38, 48
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `b0a4a7a0fbc116f18ee73c8b`

Asep dan Lukas juga ikut kelas berenang. Mereka berlatih renang di tempat yang sama. Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari. Pada tanggal 20 Agustus mereka berlatih bersama-sama. Kapan waktu paling dekat mereka akan berlatih bersama lagi?

| Opsi | Isi |
|---|---|
| A | 5 September |
| B | 28 Agustus |
| C | 4 September |
| D | 30 Agustus |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: KPK dari 3 dan 5 adalah 15. Mereka akan berlatih bersama lagi 15 hari setelah 20 Agustus. Agustus memiliki 31 hari. Sisa hari di bulan Agustus adalah 31 - 20 = 11 hari. Sisa hari yang dibutuhkan adalah 15 - 11 = 4 hari. Jadi, mereka berlatih bersama lagi pada 4 September.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `689242f727577dfa8e3bd4672f6d2566004cba582969b4a4047cbd49bb2d8b76`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2420 |
| 2 | success | valid / verified | applying | procedural | Medium | 2275 |
| 3 | success | valid / verified | applying | procedural | Medium | 2408 |

Run 1 — solusi: KPK dari 3 dan 5 adalah 15. Mereka akan berlatih bersama lagi 15 hari setelah 20 Agustus. Agustus memiliki 31 hari. Sisa hari di bulan Agustus adalah 31 - 20 = 11 hari. Sisa hari yang dibutuhkan adalah 15 - 11 = 4 hari. Jadi, mereka berlatih bersama lagi pada 4 September.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian kelipatan persekutuan terkecil (KPK) dari dua bilangan prima (3 dan 5) untuk menentukan interval waktu pertemuan berikutnya, kemudian menerapkan konsep tersebut ke dalam konteks kalender.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; Pada tanggal 20 Agustus mereka berlatih bersama-sama. Kapan waktu paling dekat mereka akan berlatih bersama lagi?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur rutin untuk mencari KPK dan menerapkannya pada situasi nyata (penambahan tanggal pada kalender).. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; Kapan waktu paling dekat mereka akan berlatih bersama lagi?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa memahami konsep KPK dan menerapkannya pada konteks kalender. Meskipun prosedurnya standar, siswa harus memperhatikan jumlah hari dalam bulan Agustus (31 hari) untuk menentukan tanggal yang tepat, yang merupakan langkah integrasi sederhana namun penting.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; Pada tanggal 20 Agustus mereka berlatih bersama-sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman KPK bilangan kecil dan pengetahuan jumlah hari dalam bulan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari KPK dan penggunaan kalender. Tantangan utama adalah transisi bulan yang memerlukan ketelitian, namun prosedurnya sangat rutin. |

Run 2 — solusi: KPK dari 3 dan 5 adalah 15. Mereka akan berlatih bersama lagi 15 hari setelah 20 Agustus. Agustus memiliki 31 hari, maka 20 + 15 = 35. 35 - 31 = 4. Jadi, tanggal 4 September.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini berkaitan dengan kelipatan persekutuan terkecil (KPK) untuk menentukan waktu pertemuan berikutnya. Ini adalah penerapan konsep KPK dalam konteks rutin.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; Pada tanggal 20 Agustus mereka berlatih bersama-sama. Kapan waktu paling dekat mereka akan berlatih bersama lagi?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur algoritma KPK untuk menyelesaikan masalah jadwal rutin.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; KPK 3 dan 5 = 15
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman KPK dan perhitungan kalender (transisi bulan). Meskipun prosedurnya standar, siswa harus mengintegrasikan pengetahuan jumlah hari dalam bulan Agustus (31 hari) untuk mendapatkan jawaban yang tepat, yang merupakan langkah tambahan yang wajar untuk kelas 5.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; Pada tanggal 20 Agustus mereka berlatih bersama-sama.; Agustus 31 hari

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman KPK dua bilangan prima dan jumlah hari dalam bulan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari KPK dan kalender. Menghitung hari melewati batas bulan adalah tantangan yang sesuai untuk tingkat kesulitan menengah. |

Run 3 — solusi: KPK dari 3 dan 5 adalah 15. Mereka akan berlatih bersama lagi 15 hari setelah 20 Agustus. Agustus memiliki 31 hari. 20 + 15 = 35. 35 - 31 = 4. Jadi, tanggal 4 September.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian kelipatan persekutuan terkecil (KPK) dari dua bilangan prima untuk menentukan interval pertemuan berikutnya, kemudian menerapkan hasil tersebut pada konteks kalender.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; Pada tanggal 20 Agustus mereka berlatih bersama-sama. Kapan waktu paling dekat mereka akan berlatih bersama lagi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mencari KPK dan menerapkannya dalam situasi nyata yang melibatkan penambahan tanggal.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; KPK 3 dan 5 = 15
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dua langkah yang saling terkait: menghitung KPK (15) dan melakukan konversi tanggal dengan memperhatikan jumlah hari dalam bulan Agustus (31 hari), yang merupakan kendala tambahan.. Bukti: Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari.; Pada tanggal 20 Agustus mereka berlatih bersama-sama.; Agustus 31 hari

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep KPK dan pengetahuan jumlah hari dalam bulan Agustus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah mempelajari KPK dan penggunaan kalender. Tantangan terletak pada integrasi perhitungan KPK dengan penambahan tanggal yang melintasi pergantian bulan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 98/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.387747; conceptual=0.577346; procedural=0.034908; metacognitive=0.000000 | conceptual | 0.577346 | 0.578242 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.763640; Medium=0.231093; Hard=0.005266 | Easy | 0.763640 | 0.520737 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.577346; −Σp ln(p) = 0.801613; H = 0.801613/ln(4) = 0.578242; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.763640; −Σp ln(p) = 0.572088; H = 0.572088/ln(3) = 0.520737; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Kelipatan Persekutuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Asep dan Lukas juga ikut kelas berenang. Mereka berlatih renang di tempat yang sama. Asep berlatih setiap 3 hari dan Lukas berlatih setiap 5 hari. Pada tanggal 20 Agustus mereka berlatih bersama-sama. Kapan waktu paling dekat mereka akan berlatih bersama lagi?
Pilihan: A. 5 September
B. 28 Agustus
C. 4 September
D. 30 Agustus
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `47584cde140924518d08fe5d`

Tentukan KPK dari kelompok bilangan berikut.<br><br>b. 6 dan 8

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 24 |
| C | 48 |
| D | 14 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kelipatan 6 adalah 6, 12, 18, 24, 30, ... Kelipatan 8 adalah 8, 16, 24, 32, ... Kelipatan persekutuan terkecil (KPK) dari 6 dan 8 adalah 24.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8205ecbef3381a46fea6438e141fad1f1160d39bb23a6b1ab0403ee4d5818321`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2270 |
| 2 | success | valid / verified | applying | procedural | Easy | 2258 |
| 3 | success | valid / verified | applying | procedural | Easy | 2257 |

Run 1 — solusi: Kelipatan 6 adalah 6, 12, 18, 24, 30, ... Kelipatan 8 adalah 8, 16, 24, 32, ... Kelipatan persekutuan terkecil (KPK) dari 6 dan 8 adalah 24.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk mencari KPK dari dua bilangan kecil. Ini adalah tugas rutin yang melibatkan penerapan algoritma atau metode daftar kelipatan yang sudah dipelajari di kelas 5.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode untuk menentukan kelipatan persekutuan terkecil, yang merupakan pengetahuan prosedural.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mencari kelipatan dari dua bilangan kecil atau menggunakan faktorisasi prima sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep kelipatan dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK dari dua bilangan satu digit adalah materi dasar kelas 5 yang sangat familiar dan prosedural. |

Run 2 — solusi: Kelipatan 6 adalah 6, 12, 18, 24, 30, ... Kelipatan 8 adalah 8, 16, 24, 32, ... Kelipatan persekutuan terkecil (KPK) adalah 24.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk mencari KPK dari dua bilangan kecil. Ini adalah tugas rutin yang menguji pemahaman konsep kelipatan persekutuan.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode untuk menentukan KPK (kelipatan persekutuan terkecil) dari dua bilangan.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa kelas 5 diharapkan sudah familiar dengan konsep kelipatan dan cara mencari KPK untuk bilangan kecil. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep kelipatan dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK dari dua bilangan satu digit adalah materi dasar kelas 5 yang penyelesaiannya bersifat prosedural langsung tanpa memerlukan langkah tambahan yang rumit. |

Run 3 — solusi: Kelipatan 6 adalah 6, 12, 18, 24, 30, ... Kelipatan 8 adalah 8, 16, 24, 32, ... Kelipatan persekutuan terkecil (KPK) dari 6 dan 8 adalah 24.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk mencari KPK dari dua bilangan kecil. Ini adalah tugas rutin yang langsung menguji pemahaman konsep KPK.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode untuk menentukan kelipatan persekutuan terkecil (KPK) dari dua bilangan.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mendaftar kelipatan atau menggunakan faktorisasi prima untuk bilangan kecil yang familiar. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: Tentukan KPK dari kelompok bilangan berikut. b. 6 dan 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep kelipatan dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK dari dua bilangan satu digit adalah materi dasar kelas 5 yang sangat rutin dan tidak menuntut integrasi langkah yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 58/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999979; applying=0.000021; reasoning=0.000000 | knowing | 0.999979 | 0.000227 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.669265; conceptual=0.308200; procedural=0.022536; metacognitive=0.000000 | factual | 0.669265 | 0.517194 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.901555; Medium=0.096271; Hard=0.002174 | Easy | 0.901555 | 0.302284 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999979; −Σp ln(p) = 0.000249; H = 0.000249/ln(3) = 0.000227; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.669265; −Σp ln(p) = 0.716984; H = 0.716984/ln(4) = 0.517194; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.901555; −Σp ln(p) = 0.332093; H = 0.332093/ln(3) = 0.302284; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Kelipatan Persekutuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan KPK dari kelompok bilangan berikut.

b. 6 dan 8
Pilihan: A. 2
B. 24
C. 48
D. 14
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `5b8b2bc7a8297541cdb45654`

tentukan faktor-faktor dari bilangan 72

| Opsi | Isi |
|---|---|
| A | 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36 |
| B | 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 72 |
| C | 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72 |
| D | 1, 2, 3, 4, 6, 8, 12, 18, 24, 36, 72 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Faktor dari 72 adalah bilangan yang membagi habis 72. Pasangan faktor: 1x72, 2x36, 3x24, 4x18, 6x12, 8x9. Himpunan faktor: {1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7d7285a34f35fbee0bb389bdfa6a36d8c28168430ca68f54035a3d372cbd0a14`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2473 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3017 |
| 3 | success | valid / verified | applying | procedural | Easy | 2397 |

Run 1 — solusi: Faktor dari 72 adalah bilangan yang membagi habis 72. Pasangan faktor: 1x72, 2x36, 3x24, 4x18, 6x12, 8x9. Himpunan faktor: {1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72}.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur rutin untuk mencari faktor dari bilangan yang diberikan. Ini adalah tugas prosedural standar yang sudah dipelajari di kelas 5.. Bukti: tentukan faktor-faktor dari bilangan 72
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep faktor dan kemampuan menerapkan algoritma pembagian atau perkalian untuk menemukan semua faktor dari suatu bilangan.. Bukti: tentukan faktor-faktor dari bilangan 72
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 5. Siswa hanya perlu melakukan pembagian atau perkalian dasar untuk menemukan pasangan faktor. Tidak ada kendala kompleks atau kebutuhan strategi non-rutin.. Bukti: tentukan faktor-faktor dari bilangan 72

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan faktor bilangan adalah materi dasar kelas 5. Prosedur pencarian faktor secara sistematis (pasangan faktor) adalah rutin. |

Run 2 — solusi: Faktor dari 72 adalah bilangan yang membagi habis 72. Pasangan faktor: 1x72, 2x36, 3x24, 4x18, 6x12, 8x9. Himpunan faktor: {1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72}.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi faktor dan melakukan pembagian atau perkalian dasar untuk menemukan pasangan faktor. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: tentukan faktor-faktor dari bilangan 72
- Dimensi pengetahuan `classify/procedural`: Soal meminta penerapan prosedur rutin untuk mencari faktor suatu bilangan.. Bukti: tentukan faktor-faktor dari bilangan 72
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas rutin yang langsung menguji pemahaman konsep faktor. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: tentukan faktor-faktor dari bilangan 72

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan adalah materi standar kelas 5. Prosedur pencarian faktor adalah rutin dan langsung, tidak memerlukan perencanaan langkah yang kompleks. |

Run 3 — solusi: Faktor dari 72 adalah bilangan yang membagi habis 72. Pasangan faktor: 1x72, 2x36, 3x24, 4x18, 6x12, 8x9. Himpunan faktor: {1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72}.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur rutin mencari faktor dari suatu bilangan. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks yang diperlukan.. Bukti: tentukan faktor-faktor dari bilangan 72
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode mencari faktor (prosedural) berdasarkan definisi faktor (konseptual).. Bukti: faktor-faktor dari bilangan 72
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 5. Jalur penyelesaian sangat jelas (mencari pasangan pengali), tidak ada kendala yang berinteraksi, dan beban kalkulasi rendah.. Bukti: tentukan faktor-faktor dari bilangan 72

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan adalah materi standar kelas 5 yang bersifat prosedural langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3861`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur rutin untuk mencari faktor dari bilangan yang diberikan. Ini adalah tugas prosedural standar yang sudah dipelajari di kelas 5.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang konsep faktor dan kemampuan menerapkan algoritma pembagian atau perkalian untuk menemukan semua faktor dari suatu bilangan.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 5. Siswa hanya perlu melakukan pembagian atau perkalian dasar untuk menemukan pasangan faktor. Tidak ada kendala kompleks atau kebutuhan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan faktor bilangan adalah materi dasar kelas 5. Prosedur pencarian faktor secara sistematis (pasangan faktor) adalah rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 138/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.870602; applying=0.129398; reasoning=0.000000 | knowing | 0.870602 | 0.350662 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.097878; conceptual=0.884619; procedural=0.017503; metacognitive=0.000000 | conceptual | 0.884619 | 0.293394 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.771643; Medium=0.223126; Hard=0.005231 | Easy | 0.771643 | 0.511742 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.870602; −Σp ln(p) = 0.385242; H = 0.385242/ln(3) = 0.350662; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.884619; −Σp ln(p) = 0.406730; H = 0.406730/ln(4) = 0.293394; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.771643; −Σp ln(p) = 0.562206; H = 0.562206/ln(3) = 0.511742; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Faktor
Tipe soal: multiple_choice
Stimulus: -
Soal: tentukan faktor-faktor dari bilangan 72
Pilihan: A. 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36
B. 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 72
C. 1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72
D. 1, 2, 3, 4, 6, 8, 12, 18, 24, 36, 72
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `5d06ae960e3abd045c974c60`

Tentukan faktor-faktor dari bilangan berikut 24

| Opsi | Isi |
|---|---|
| A | 1, 2, 3, 4, 6, 8, 12, 24 |
| B | 24, 48, 72, 96 |
| C | 1, 2, 3, 4, 6, 8, 12, 16, 24 |
| D | 2, 3, 4, 6, 8, 12 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Faktor dari 24 adalah semua bilangan yang membagi habis 24. Pasangan faktornya adalah: 1x24, 2x12, 3x8, 4x6. Jadi, faktor-faktor dari 24 adalah 1, 2, 3, 4, 6, 8, 12, 24.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a55aa5f22d5dcbb98b36c18a6e0bc6e81ad03ff8304b36ecb782dce7a1c7ed7e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2324 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2320 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2302 |

Run 1 — solusi: Faktor dari 24 adalah bilangan yang membagi habis 24. Pasangan faktornya: 1x24, 2x12, 3x8, 4x6. Maka faktornya adalah 1, 2, 3, 4, 6, 8, 12, 24.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi faktor dari bilangan 24. Ini adalah prosedur langsung yang sudah dipelajari di kelas 5, yaitu mencari pasangan bilangan yang hasil kalinya adalah 24.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami definisi faktor (konsep) dan menerapkan metode pembagian atau perkalian untuk menemukan semua faktor (prosedural).. Bukti: Tentukan faktor-faktor dari bilangan berikut 24
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari definisi faktor. Siswa hanya perlu melakukan pembagian atau perkalian dasar untuk menemukan faktor-faktor dari 24. Tidak ada langkah kompleks atau integrasi konsep yang sulit.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan adalah materi standar kelas 5 yang bersifat rutin dan langsung. |

Run 2 — solusi: Faktor dari 24 adalah bilangan yang membagi habis 24. Pasangan faktor: 1x24, 2x12, 3x8, 4x6. Maka faktornya adalah 1, 2, 3, 4, 6, 8, 12, 24.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk menentukan faktor dari bilangan 24, yang merupakan prosedur standar dan langsung dalam materi kelas 5. Siswa hanya perlu mengingat definisi faktor dan melakukan pembagian atau perkalian dasar untuk menemukan pasangan faktor.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep faktor, yaitu bilangan yang membagi habis bilangan lain. Ini adalah pengetahuan konseptual dasar tentang pembagian.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa kelas 5 sudah terbiasa dengan konsep faktor. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan faktor bilangan adalah materi dasar kelas 5 yang bersifat rutin dan tidak memerlukan perencanaan langkah yang kompleks. |

Run 3 — solusi: Faktor dari 24 adalah bilangan yang membagi habis 24. Pasangan faktor: 1x24, 2x12, 3x8, 4x6. Jadi faktornya adalah 1, 2, 3, 4, 6, 8, 12, 24.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi faktor dari bilangan 24, yang merupakan prosedur langsung dan rutin dalam materi kelas 5.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi faktor dan kemampuan menerapkan prosedur untuk mencari pembagi bilangan.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan pembagian atau perkalian dasar untuk menemukan pasangan faktor. Tidak ada langkah yang saling bergantung atau kendala kompleks.. Bukti: Tentukan faktor-faktor dari bilangan berikut 24

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan adalah materi dasar kelas 5 yang diajarkan secara rutin. Soal ini tidak menuntut penalaran kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3735`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengidentifikasi faktor dari bilangan 24. Ini adalah prosedur langsung yang sudah dipelajari di kelas 5, yaitu mencari pasangan bilangan yang hasil kalinya adalah 24.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami definisi faktor (konsep) dan menerapkan metode pembagian atau perkalian untuk menemukan semua faktor (prosedural).
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung dari definisi faktor. Siswa hanya perlu melakukan pembagian atau perkalian dasar untuk menemukan faktor-faktor dari 24. Tidak ada langkah kompleks atau integrasi konsep yang sulit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan adalah materi standar kelas 5 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 99/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.948768; applying=0.051232; reasoning=0.000000 | knowing | 0.948768 | 0.183983 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.470912; conceptual=0.514524; procedural=0.014563; metacognitive=0.000000 | conceptual | 0.514524 | 0.546880 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.889939; Medium=0.107517; Hard=0.002544 | Easy | 0.889939 | 0.326541 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.948768; −Σp ln(p) = 0.202126; H = 0.202126/ln(3) = 0.183983; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.514524; −Σp ln(p) = 0.758137; H = 0.758137/ln(4) = 0.546880; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.889939; −Σp ln(p) = 0.358742; H = 0.358742/ln(3) = 0.326541; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Faktor
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan faktor-faktor dari bilangan berikut 24
Pilihan: A. 1, 2, 3, 4, 6, 8, 12, 24
B. 24, 48, 72, 96
C. 1, 2, 3, 4, 6, 8, 12, 16, 24
D. 2, 3, 4, 6, 8, 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `ced0037808c936917602ebcb`

Dania akan merayakan ulang tahun. Ia berencana membuat bingkisan untuk teman-temannya yang hadir di pesta. Setiap paket berisi susu kotak, permen lolipop, dan biskuit. Banyaknya jenis barang pada setiap paket sama. Ia memiliki 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit. Berapa paket paling banyak yang dapat dibuat?

| Opsi | Isi |
|---|---|
| A | 144 paket |
| B | 6 paket |
| C | 24 paket |
| D | 12 paket |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mencari FPB dari 36, 48, dan 24. Faktorisasi prima: 36 = 2^2 x 3^2; 48 = 2^4 x 3; 24 = 2^3 x 3. FPB = 2^2 x 3 = 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `64592a9b1cca87fd60e5f538522469cb65fad9e5b124ca334cccaaa72ab6cea6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2409 |
| 2 | success | valid / verified | applying | procedural | Medium | 2391 |
| 3 | success | valid / verified | applying | procedural | Easy | 2383 |

Run 1 — solusi: Mencari FPB dari 36, 48, dan 24. Faktorisasi prima: 36 = 2^2 x 3^2; 48 = 2^4 x 3; 24 = 2^3 x 3. FPB = 2^2 x 3 = 4 x 3 = 12. Jadi, paling banyak 12 paket.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian faktor persekutuan terbesar (FPB) dari tiga bilangan (36, 48, 24) untuk menentukan jumlah paket maksimal yang dapat dibuat dengan pembagian rata.. Bukti: Berapa paket paling banyak yang dapat dibuat?
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur algoritma FPB (faktorisasi prima atau pembagian berulang) untuk menyelesaikan masalah kontekstual.. Bukti: 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit; Berapa paket paling banyak yang dapat dibuat?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk mengenali situasi FPB dari konteks cerita dan melakukan prosedur FPB pada tiga bilangan. Meskipun prosedurnya rutin, siswa harus menghubungkan konsep pembagian rata dengan FPB tanpa bantuan langkah-langkah eksplisit.. Bukti: 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit; Berapa paket paling banyak yang dapat dibuat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep faktor, kelipatan, dan FPB dua atau tiga bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi FPB adalah standar kelas 5. Soal menuntut pemilihan prosedur yang tepat untuk masalah pembagian kelompok, yang merupakan aplikasi standar namun memerlukan pemahaman konsep FPB yang baik. |

Run 2 — solusi: Mencari FPB dari 36, 48, dan 24. Faktorisasi prima: 36 = 2^2 x 3^2, 48 = 2^4 x 3, 24 = 2^3 x 3. FPB = 2^2 x 3 = 4 x 3 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian faktor persekutuan terbesar (FPB) dari tiga bilangan untuk menentukan jumlah paket maksimal yang dapat dibuat dengan pembagian rata.. Bukti: Berapa paket paling banyak yang dapat dibuat?
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur algoritme FPB (faktorisasi prima atau pembagian berulang) untuk menyelesaikan masalah kontekstual.. Bukti: 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk mengenali bahwa masalah pembagian rata dengan jumlah maksimal memerlukan konsep FPB. Meskipun prosedurnya rutin, siswa harus menghubungkan konteks cerita dengan konsep FPB dari tiga bilangan, yang merupakan langkah integrasi standar untuk kelas 5.. Bukti: 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit; Berapa paket paling banyak yang dapat dibuat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep faktor, kelipatan, dan FPB dari dua atau tiga bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari FPB dari tiga bilangan adalah materi standar kelas 5. Tingkat kesulitan Medium tepat karena siswa harus mengidentifikasi kebutuhan FPB tanpa bantuan langkah-langkah eksplisit. |

Run 3 — solusi: Mencari FPB dari 36, 48, dan 24. Faktorisasi prima: 36 = 2^2 x 3^2, 48 = 2^4 x 3, 24 = 2^3 x 3. FPB = 2^2 x 3 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian faktor persekutuan terbesar (FPB) dari tiga bilangan untuk menentukan jumlah paket maksimal. Ini adalah penerapan prosedur FPB dalam konteks soal cerita rutin.. Bukti: Berapa paket paling banyak yang dapat dibuat?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode atau algoritme FPB (prosedural) untuk menyelesaikan masalah pembagian barang ke dalam paket dengan jumlah yang sama.. Bukti: 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan rutin FPB. Siswa kelas 5 sudah mempelajari konsep faktor dan FPB. Jalur penyelesaiannya jelas (mencari FPB dari tiga angka), tidak ada kendala yang saling berinteraksi secara kompleks, dan tidak memerlukan strategi nonrutin.. Bukti: 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit; Berapa paket paling banyak yang dapat dibuat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang faktor bilangan dan FPB. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari FPB dari tiga bilangan adalah standar kompetensi kelas 5. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga termasuk kategori mudah bagi siswa kelas 5. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4052`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus mengidentifikasi bahwa masalah pembagian barang ke dalam paket dengan jumlah yang sama dan maksimal menuntut penggunaan konsep FPB. Ini adalah penerapan prosedur matematika dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Siswa menerapkan algoritma atau metode faktorisasi untuk mencari FPB dari tiga bilangan.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya rutin, siswa harus melakukan pemilihan strategi (FPB) berdasarkan konteks cerita. Terdapat tiga bilangan yang harus diolah, yang meningkatkan beban kognitif dibandingkan FPB dua bilangan, namun jalur penyelesaiannya tetap jelas dan familiar bagi siswa kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep faktor, kelipatan, dan FPB. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari FPB dari tiga bilangan adalah standar kelas 5. Soal menuntut pemilihan prosedur yang tepat untuk masalah pembagian kelompok, yang merupakan aplikasi standar namun memerlukan pemahaman konsep FPB yang baik. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 116/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.128132; conceptual=0.848146; procedural=0.023723; metacognitive=0.000000 | conceptual | 0.848146 | 0.354699 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.795663; Medium=0.198865; Hard=0.005472 | Easy | 0.795663 | 0.483848 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.848146; −Σp ln(p) = 0.491718; H = 0.491718/ln(4) = 0.354699; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.795663; −Σp ln(p) = 0.531562; H = 0.531562/ln(3) = 0.483848; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Faktor Persekutuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dania akan merayakan ulang tahun. Ia berencana membuat bingkisan untuk teman-temannya yang hadir di pesta. Setiap paket berisi susu kotak, permen lolipop, dan biskuit. Banyaknya jenis barang pada setiap paket sama. Ia memiliki 36 susu kotak, 48 permen lolipop, dan 24 bungkus biskuit. Berapa paket paling banyak yang dapat dibuat?
Pilihan: A. 144 paket
B. 6 paket
C. 24 paket
D. 12 paket
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `4971c1d138b152cf3a247dc0`

Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 6 |
| C | 3 |
| D | 84 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Faktor dari 12 adalah {1, 2, 3, 4, 6, 12}. Faktor dari 42 adalah {1, 2, 3, 6, 7, 14, 21, 42}. Faktor persekutuan adalah {1, 2, 3, 6}. FPB adalah 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d840dfa4e37eab786c1ba0d4d901e22eac4d38e297a790cbdbb65f7a59493378`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2914 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2858 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2267 |

Run 1 — solusi: Faktor dari 12 adalah {1, 2, 3, 4, 6, 12}. Faktor dari 42 adalah {1, 2, 3, 6, 7, 14, 21, 42}. Faktor persekutuan adalah {1, 2, 3, 6}. FPB adalah 6.
- Domain kognitif `classify/knowing`: Siswa diminta menjalankan prosedur standar untuk mencari FPB dari dua bilangan yang relatif kecil. Ini adalah prosedur langsung yang sudah dipelajari di kelas 5.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode mencari faktor persekutuan terbesar, yang merupakan pengetahuan prosedural.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mendaftar faktor atau menggunakan pohon faktor untuk menemukan FPB. Tidak ada kendala yang berinteraksi atau langkah yang kompleks.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang faktor bilangan dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari FPB dua bilangan adalah materi standar kelas 5 yang bersifat rutin dan langsung. |

Run 2 — solusi: Faktor dari 12 adalah 1, 2, 3, 4, 6, 12. Faktor dari 42 adalah 1, 2, 3, 6, 7, 14, 21, 42. Faktor persekutuan adalah 1, 2, 3, 6. FPB adalah 6.
- Domain kognitif `classify/knowing`: Siswa diminta menjalankan prosedur standar untuk mencari FPB dari dua bilangan kecil. Ini adalah prosedur rutin yang diajarkan di kelas 5.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang konsep faktor dan prosedur mencari FPB.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mendaftar faktor atau menggunakan pohon faktor untuk menemukan FPB. Tidak ada kendala kompleks atau langkah yang saling bergantung.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep faktor bilangan dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari FPB dari dua bilangan kecil adalah materi standar kelas 5 yang bersifat rutin dan langsung. |

Run 3 — solusi: Faktor dari 12 adalah 1, 2, 3, 4, 6, 12. Faktor dari 42 adalah 1, 2, 3, 6, 7, 14, 21, 42. Faktor persekutuan adalah 1, 2, 3, 6. Nilai terbesar (FPB) adalah 6.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menjalankan prosedur standar (mencari FPB) yang sudah dipelajari di kelas 5. Tidak ada konteks baru atau strategi nonrutin yang diperlukan.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mencari FPB dari dua bilangan.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari prosedur mencari FPB yang sangat familiar bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang faktor bilangan dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari FPB adalah materi standar kelas 5. Soal ini bersifat langsung tanpa memerlukan perencanaan atau integrasi konsep yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 59/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.998830; applying=0.001170; reasoning=0.000000 | knowing | 0.998830 | 0.008257 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.200607; conceptual=0.712001; procedural=0.087392; metacognitive=0.000000 | conceptual | 0.712001 | 0.560567 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.879030; Medium=0.118153; Hard=0.002817 | Easy | 0.879030 | 0.347921 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998830; −Σp ln(p) = 0.009071; H = 0.009071/ln(3) = 0.008257; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.712001; −Σp ln(p) = 0.777112; H = 0.777112/ln(4) = 0.560567; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.879030; −Σp ln(p) = 0.382230; H = 0.382230/ln(3) = 0.347921; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Faktor Persekutuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan faktor persekutuan terbesar (FPB) dari 12 dan 42.
Pilihan: A. 12
B. 6
C. 3
D. 84
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `91cfdc7e234e38ad8f34ec21`

Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima dan cara pembagian berulang.<br><br>d. 7, 18, 33

| Opsi | Isi |
|---|---|
| A | KPK = 1.386, FPB = 1 |
| B | KPK = 462, FPB = 1 |
| C | KPK = 1.386, FPB = 3 |
| D | KPK = 4.158, FPB = 1 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor persekutuan terbesar yang membagi ketiganya. Karena tidak ada faktor prima yang sama untuk ketiganya, maka FPB = 1. KPK adalah kelipatan persekutuan terkecil, diambil dari semua faktor prima dengan pangkat tertinggi: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.386.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c70998257aeb94571ec13056debb7a3fb8b193406f31f4e05a4baaa4b98b1e2f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2446 |
| 2 | success | valid / verified | applying | procedural | Easy | 2366 |
| 3 | success | valid / verified | applying | procedural | Medium | 2395 |

Run 1 — solusi: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor persekutuan terbesar yang membagi ketiganya, karena tidak ada faktor prima yang sama, maka FPB = 1. KPK adalah kelipatan persekutuan terkecil, diambil dari semua faktor prima dengan pangkat tertinggi: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.386.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur faktorisasi prima untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan prosedur standar yang sudah dipelajari di kelas 5.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode faktorisasi prima untuk menyelesaikan masalah KPK dan FPB.. Bukti: menggunakan cara faktorisasi prima dan cara pembagian berulang
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan tiga bilangan sekaligus (7, 18, 33) yang memerlukan ketelitian dalam faktorisasi prima dan penggabungan faktor untuk KPK. Meskipun prosedurnya rutin, mengelola tiga bilangan dengan faktor yang berbeda (terutama angka 7 dan 11 yang prima) meningkatkan beban kognitif dibandingkan hanya dua bilangan.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman faktorisasi prima, konsep KPK dan FPB, serta perkalian bilangan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menentukan KPK dan FPB dari tiga bilangan adalah standar, namun menuntut ketelitian lebih tinggi dalam faktorisasi dan pemilihan faktor prima dibandingkan dua bilangan. |

Run 2 — solusi: Faktorisasi prima: 7 = 7; 18 = 2 x 3^2; 33 = 3 x 11. KPK = 2 x 3^2 x 7 x 11 = 1.386. FPB = 1 karena tidak ada faktor prima yang sama untuk ketiga bilangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur faktorisasi prima yang sudah dipelajari untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan konsep rutin.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme faktorisasi prima untuk menyelesaikan masalah KPK dan FPB.. Bukti: menggunakan cara faktorisasi prima
- Intended difficulty `classify/Easy`: Soal melibatkan tiga bilangan dengan faktorisasi yang cukup sederhana (7 prima, 18=2x3^2, 33=3x11). Prosedur KPK dan FPB adalah rutin bagi kelas 5. Tidak ada kendala kompleks yang saling berinteraksi.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman faktorisasi prima dan konsep KPK/FPB dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK dan FPB dari tiga bilangan adalah materi standar kelas 5. Prosedur faktorisasi prima sudah diajarkan dan merupakan rutinitas. |

Run 3 — solusi: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. KPK = 2 x 3^2 x 7 x 11 = 1.386. FPB = 1 (tidak ada faktor prima persekutuan untuk ketiganya).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur faktorisasi prima yang sudah dipelajari untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan konsep rutin.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme faktorisasi prima untuk menyelesaikan masalah KPK dan FPB.. Bukti: menggunakan cara faktorisasi prima dan cara pembagian berulang
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan tiga bilangan dengan faktorisasi yang berbeda (7 prima, 18 komposit, 33 komposit). Siswa harus mengelola faktorisasi untuk tiga angka sekaligus dan memahami bahwa FPB adalah 1 karena tidak ada faktor persekutuan untuk ketiganya, yang merupakan langkah integrasi konsep dasar.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman faktorisasi prima, konsep KPK dan FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mencari KPK dan FPB dari tiga bilangan adalah standar, namun menuntut ketelitian dalam faktorisasi dan pemilihan faktor prima untuk KPK serta identifikasi FPB yang bernilai 1. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4004`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur faktorisasi prima yang sudah dipelajari untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan prosedur standar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritme atau metode faktorisasi prima untuk menyelesaikan masalah KPK dan FPB.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena melibatkan tiga bilangan sekaligus yang memerlukan ketelitian dalam faktorisasi dan penggabungan faktor untuk KPK. Meskipun prosedurnya rutin, mengelola tiga bilangan dengan faktor yang berbeda (terutama angka 7 dan 11 yang prima) meningkatkan beban kognitif dibandingkan hanya dua bilangan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman faktorisasi prima, konsep KPK dan FPB, serta perkalian bilangan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menentukan KPK dan FPB dari tiga bilangan adalah standar, namun menuntut ketelitian lebih tinggi dalam faktorisasi dan pemilihan faktor prima dibandingkan dua bilangan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 118/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001149; applying=0.998851; reasoning=0.000000 | applying | 0.998851 | 0.008125 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.106352; conceptual=0.832488; procedural=0.061160; metacognitive=0.000000 | conceptual | 0.832488 | 0.405294 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.840389; Medium=0.156138; Hard=0.003473 | Easy | 0.840389 | 0.414845 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998851; −Σp ln(p) = 0.008926; H = 0.008926/ln(3) = 0.008125; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.832488; −Σp ln(p) = 0.561857; H = 0.561857/ln(4) = 0.405294; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.840389; −Σp ln(p) = 0.455754; H = 0.455754/ln(3) = 0.414845; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Menentukan KPK dan FPB dengan Menggunakan Faktor Prima
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima dan cara pembagian berulang.

d. 7, 18, 33
Pilihan: A. KPK = 1.386, FPB = 1
B. KPK = 462, FPB = 1
C. KPK = 1.386, FPB = 3
D. KPK = 4.158, FPB = 1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `98de773bdad80e3ec2e81668`

Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor.<br><br>a. 60

| Opsi | Isi |
|---|---|
| A | 2 × 3 × 10 |
| B | 2 × 2 × 15 |
| C | 2 × 3 × 5 |
| D | 2 × 2 × 3 × 5 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 60 = 2 x 30 = 2 x 2 x 15 = 2 x 2 x 3 x 5. Semua faktor (2, 2, 3, 5) adalah bilangan prima.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `005bdf83b8686c103740df7253cf915947d8f9ee1d15e3f3a273cd900127e3b9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2911 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2917 |
| 3 | success | valid / verified | applying | procedural | Easy | 2911 |

Run 1 — solusi: Faktorisasi prima dari 60 adalah 60 = 2 x 30 = 2 x 2 x 15 = 2 x 2 x 3 x 5. Semua faktor (2, 2, 3, 5) adalah bilangan prima.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan prosedur standar faktorisasi prima yang merupakan keterampilan dasar dan langsung dalam kurikulum matematika kelas 5.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor. a. 60
- Dimensi pengetahuan `classify/procedural`: Tugas ini memerlukan penerapan algoritma faktorisasi (pohon faktor) untuk menguraikan bilangan komposit menjadi faktor-faktor primanya.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor. a. 60
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin. Prosedur faktorisasi prima adalah materi standar yang familiar bagi siswa kelas 5.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor. a. 60

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang bilangan prima dan pembagian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Faktorisasi prima adalah materi standar kelas 5. Soal ini meminta prosedur langsung tanpa langkah tambahan atau integrasi konsep yang kompleks. |

Run 2 — solusi: 60 = 2 x 30 = 2 x 2 x 15 = 2 x 2 x 3 x 5
- Domain kognitif `classify/knowing`: Siswa diminta melakukan prosedur faktorisasi prima yang merupakan prosedur standar dan langsung.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan algoritma faktorisasi prima.. Bukti: faktorisasi prima
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin faktorisasi prima untuk bilangan kecil. Tidak ada kendala kompleks atau kebutuhan strategi non-rutin.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor. a. 60

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bilangan prima dan pembagian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Faktorisasi prima adalah materi standar kelas 5. Prosedur ini bersifat rutin dan langsung. |

Run 3 — solusi: 60 = 2 x 30 = 2 x 2 x 15 = 2 x 2 x 3 x 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar faktorisasi prima untuk bilangan 60. Ini adalah penerapan langsung dari algoritma yang sudah dipelajari di kelas 5.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor. a. 60
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma faktorisasi prima (pohon faktor) dan kriteria bilangan prima.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor. a. 60
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin yang sangat familiar bagi siswa kelas 5. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor. a. 60

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang bilangan prima dan pembagian dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Faktorisasi prima bilangan dua digit adalah materi dasar kelas 5 yang diselesaikan dengan prosedur rutin tanpa tuntutan integrasi tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3582`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta melakukan prosedur standar faktorisasi prima menggunakan pohon faktor. Ini adalah tugas rutin yang memerlukan ingatan dan penerapan algoritma dasar.
- Dimensi pengetahuan `procedural`: Soal menguji penguasaan algoritma faktorisasi prima (pohon faktor) dan kriteria bilangan prima.
- Intended difficulty `Easy`: Soal ini merupakan latihan rutin faktorisasi prima untuk bilangan dua digit. Tidak ada kendala kompleks, integrasi konsep, atau kebutuhan strategi non-rutin. Prosedur ini sangat familiar bagi siswa kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang bilangan prima dan pembagian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Faktorisasi prima adalah materi standar kelas 5. Soal ini meminta prosedur langsung tanpa langkah tambahan atau integrasi konsep yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.830157; applying=0.169843; reasoning=0.000000 | knowing | 0.830157 | 0.414739 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.762405; conceptual=0.113553; procedural=0.124042; metacognitive=0.000000 | factual | 0.762405 | 0.514140 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.899836; Medium=0.097318; Hard=0.002845 | Easy | 0.899836 | 0.308007 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.830157; −Σp ln(p) = 0.455638; H = 0.455638/ln(3) = 0.414739; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.762405; −Σp ln(p) = 0.712749; H = 0.712749/ln(4) = 0.514140; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.899836; −Σp ln(p) = 0.338380; H = 0.338380/ln(3) = 0.308007; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Menentukan KPK dan FPB dengan Menggunakan Faktor Prima
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan faktorisasi prima dari bilangan-bilangan berikut dengan menggunakan pohon faktor.

a. 60
Pilihan: A. 2 × 3 × 10
B. 2 × 2 × 15
C. 2 × 3 × 5
D. 2 × 2 × 3 × 5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `b3d9b778a4f7d0b7eb930ba1`

Bandingkan kedua gambar berikut ini, kemudian pilihlah tanda <, =, atau > untuk mengisi titik-titik. . . .

| Opsi | Isi |
|---|---|
| A | $\frac{3}{4} = \frac{9}{16}$ |
| B | $\frac{3}{4} > \frac{9}{16}$ |
| C | $\frac{1}{4} > \frac{7}{16}$ |
| D | $\frac{3}{4} < \frac{9}{16}$ |

![Gambar sumber soal 20](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0091-00.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: The problem text (3/4 vs 9/16) is inconsistent with the visual representation (which shows different fractions). Assuming the text is the intended problem: 3/4 = 12/16. Since 12/16 > 9/16, the correct sign is >.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0091-00.png. Transkripsi visual: The image shows three rows of comparison problems labeled b, c, and d. Row 'd' contains two rectangles. The left rectangle is a 2x3 grid (6 total cells) with 3 cells shaded orange, representing 3/6 or 1/2. The right rectangle is a 1x6 grid (6 total cells) with 2 cells shaded orange, representing 2/6 or 1/3. However, the problem text and options refer to 3/4 and 9/16. The provided image does not match the problem text (3/4 vs 9/16). The problem text is inconsistent with the visual evidence provided in the image.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8d2da60b813cc8ea7466cfef427a8950fa52cd9d36bb1e5670a3d1d72d4f9005`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3623 |
| 2 | success | valid / verified | applying | procedural | Medium | 3598 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3579 |

Run 1 — solusi: Gambar kiri merepresentasikan 3/4 atau 12/16. Gambar kanan merepresentasikan 9/16. Karena 12/16 > 9/16, maka 3/4 > 9/16.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan representasi visual pecahan, mengubahnya ke bentuk numerik (3/4 dan 9/16), lalu menerapkan prosedur perbandingan pecahan dengan menyamakan penyebut. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Bandingkan kedua gambar berikut ini; pilihlah tanda <, =, atau >
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang pecahan sebagai bagian dari keseluruhan dan prosedur untuk membandingkan pecahan (menyamakan penyebut atau membandingkan nilai).. Bukti: Bandingkan kedua gambar berikut ini; pilihlah tanda <, =, atau >
- Intended difficulty `classify/Easy`: Soal ini memerlukan interpretasi visual dan konversi ke pecahan, diikuti dengan perbandingan. Langkah-langkahnya rutin dan jelas bagi siswa kelas 5.. Bukti: Bandingkan kedua gambar berikut ini; pilihlah tanda <, =, atau >

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar pecahan sebagai bagian dari keseluruhan dan cara membandingkan pecahan dengan penyebut berbeda. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan representasi visual pecahan dan perbandingan pecahan sederhana. Tugas ini adalah latihan rutin. |

Run 2 — solusi: Mengubah pecahan ke penyebut yang sama: 3/4 = 12/16. Karena 12/16 > 9/16, maka 3/4 > 9/16.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai pecahan dari representasi visual (gambar d), kemudian melakukan perbandingan nilai pecahan dengan menyamakan penyebut atau membandingkan secara proporsional. Ini adalah penerapan prosedur standar pada konteks visual.. Bukti: Bandingkan kedua gambar berikut ini; 3/4 > 9/16
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau metode untuk membandingkan pecahan (menyamakan penyebut) yang merupakan prosedur matematis standar.. Bukti: 3/4 = 12/16; 3/4 > 9/16
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus melakukan dua langkah: (1) menginterpretasi representasi visual menjadi pecahan, dan (2) melakukan operasi perbandingan pecahan. Meskipun prosedurnya rutin, terdapat perpindahan representasi dari gambar ke simbol numerik yang memerlukan ketelitian.. Bukti: Bandingkan kedua gambar berikut ini; 3/4 > 9/16

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan sebagai bagian dari keseluruhan dan kemampuan menyamakan penyebut. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu membandingkan pecahan dengan penyebut berbeda menggunakan visualisasi atau konversi penyebut. |

Run 3 — solusi: Gambar kiri merepresentasikan 3/4 atau 12/16. Gambar kanan merepresentasikan 9/16. Karena 12/16 > 9/16, maka 3/4 > 9/16.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan representasi visual pecahan, mengubahnya ke bentuk numerik, dan membandingkan nilainya. Ini adalah penerapan prosedur standar untuk membandingkan pecahan.. Bukti: Bandingkan kedua gambar berikut ini; pilihlah tanda <, =, atau >
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep pecahan sebagai bagian dari keseluruhan dan menerapkan prosedur perbandingan (menyamakan penyebut atau membandingkan nilai) untuk menentukan hubungan antara dua pecahan.. Bukti: Bandingkan kedua gambar berikut ini; pilihlah tanda <, =, atau >
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 5. Siswa hanya perlu mengidentifikasi nilai pecahan dari gambar dan membandingkannya. Tidak ada kendala kompleks atau langkah yang saling bergantung yang tinggi.. Bukti: Bandingkan kedua gambar berikut ini; pilihlah tanda <, =, atau >

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar pecahan sebagai bagian dari keseluruhan dan cara membandingkan pecahan dengan penyebut berbeda. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan pecahan adalah materi standar kelas 5. Mengubah representasi visual ke numerik dan membandingkannya adalah tugas rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5022`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur perbandingan pecahan (menyamakan penyebut atau membandingkan nilai) pada konteks yang diberikan. Ini adalah penerapan konsep rutin.
- Dimensi pengetahuan `procedural`: Siswa menggunakan prosedur matematis standar untuk membandingkan pecahan dengan penyebut berbeda.
- Intended difficulty `Easy`: Soal ini rutin bagi kelas 5. Siswa hanya perlu melakukan konversi pecahan sederhana ke penyebut yang sama (atau membandingkan secara visual jika gambar akurat) dan memilih tanda yang tepat. Tidak ada kendala kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan pecahan adalah materi standar kelas 5. Prosedur menyamakan penyebut adalah metode rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 317/256; truncation: `True`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006196; applying=0.993804; reasoning=0.000000 | applying | 0.993804 | 0.034293 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000723; conceptual=0.944194; procedural=0.055083; metacognitive=0.000000 | conceptual | 0.944194 | 0.158069 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.574229; Medium=0.411342; Hard=0.014429 | Easy | 0.574229 | 0.678226 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993804; −Σp ln(p) = 0.037675; H = 0.037675/ln(3) = 0.034293; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.944194; −Σp ln(p) = 0.219130; H = 0.219130/ln(4) = 0.158069; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.574229; −Σp ln(p) = 0.745107; H = 0.745107/ln(3) = 0.678226; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan dan Mengurutkan Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Bandingkan kedua gambar berikut ini, kemudian pilihlah tanda <, =, atau > untuk mengisi titik-titik. . . .
Pilihan: A. $\frac{3}{4} = \frac{9}{16}$
B. $\frac{3}{4} > \frac{9}{16}$
C. $\frac{1}{4} > \frac{7}{16}$
D. $\frac{3}{4} < \frac{9}{16}$
Transkripsi visual: The image shows three rows of comparison problems labeled b, c, and d. Row 'd' contains two rectangles. The left rectangle is a 2x3 grid (6 total cells) with 3 cells shaded orange, representing 3/6 or 1/2. The right rectangle is a 1x6 grid (6 total cells) with 2 cells shaded orange, representing 2/6 or 1/3. However, the problem text and options refer to 3/4 and 9/16. The provided image does not match the problem text (3/4 vs 9/16). The problem text is inconsistent with the visual evidence provided in the image.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `0a7f58a69ba9ec033899af2c`

Bandingkan kedua gambar berikut ini, kemudian isilah titik-titik dengan tanda <, =, atau >.<br><br>d. ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{6} < \frac{4}{6}$ |
| B | $\frac{3}{6} < \frac{2}{6}$ |
| C | $\frac{3}{6} > \frac{2}{6}$ |
| D | $\frac{3}{6} = \frac{2}{6}$ |

![Gambar sumber soal 21](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0091-00.png>)


Kunci sumber: `C`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal tidak valid karena representasi visual pada gambar kanan (2/5) tidak sesuai dengan pecahan 2/6 yang digunakan dalam pilihan jawaban.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0091-00.png. Transkripsi visual: Gambar d menunjukkan dua persegi panjang. Persegi panjang kiri dibagi menjadi grid 3x2 (6 kotak), dengan 3 kotak diarsir (3/6). Persegi panjang kanan dibagi menjadi 5 kolom vertikal, dengan 2 kolom diarsir (2/5).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `68834eb76228748650ef598cfaa9a7875fcb9da0cac36bee0cbd0149049735e1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | — | — | — | 3287 |
| 2 | success | concern / conflict | applying | conceptual | Easy | 3542 |
| 3 | success | concern / verified | applying | conceptual | Easy | 3665 |

Run 1 — solusi: Soal tidak valid karena representasi visual tidak sesuai dengan pecahan dalam pilihan jawaban.
- Domain kognitif `abstain/None`: Soal tidak dapat diklasifikasikan karena terdapat ketidaksesuaian antara representasi visual (gambar d) dengan pilihan jawaban yang tersedia. Gambar tidak merepresentasikan pecahan 3/6 dan 2/6 seperti yang tertulis di pilihan jawaban.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Soal tidak dapat diklasifikasikan karena terdapat ketidaksesuaian antara representasi visual (gambar d) dengan pilihan jawaban yang tersedia.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak dapat diklasifikasikan karena terdapat ketidaksesuaian antara representasi visual (gambar d) dengan pilihan jawaban yang tersedia.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 2 — solusi: Tidak dapat diverifikasi karena ketidaksesuaian antara gambar dan pilihan jawaban.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan representasi visual pecahan dan membandingkan nilainya. Ini adalah tugas applying karena melibatkan pemilihan prosedur perbandingan pecahan yang sudah dipelajari.. Bukti: Bandingkan kedua gambar berikut ini; isilah titik-titik dengan tanda <, =, atau >
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep pecahan sebagai bagian dari keseluruhan dan hubungan antara representasi visual dengan simbol numerik.. Bukti: Bandingkan kedua gambar berikut ini
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena tugas utamanya adalah membandingkan dua pecahan sederhana yang penyebutnya sama (jika mengabaikan kesalahan gambar). Langkah penyelesaiannya langsung dan rutin bagi siswa kelas 5.. Bukti: Bandingkan kedua gambar berikut ini; isilah titik-titik dengan tanda <, =, atau >

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar pecahan sebagai bagian dari keseluruhan dan perbandingan pecahan berpenyebut sama. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan pecahan dengan penyebut sama adalah materi standar kelas 5 yang bersifat rutin. |

Run 3 — solusi: Gambar kiri merepresentasikan 3/6. Gambar kanan merepresentasikan 2/6. Karena penyebut sama (6), bandingkan pembilang: 3 > 2. Jadi, 3/6 > 2/6.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi nilai pecahan dari representasi visual (gambar) dan membandingkan kedua nilai tersebut. Ini adalah penerapan langsung dari konsep pecahan yang sudah dipelajari.. Bukti: Bandingkan kedua gambar berikut ini; isilah titik-titik dengan tanda <, =, atau >
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai pecahan yang direpresentasikan secara visual dan prosedur membandingkan dua pecahan dengan penyebut yang sama.. Bukti: Bandingkan kedua gambar berikut ini
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menghitung bagian yang diarsir dari gambar yang sudah terbagi secara jelas dan membandingkan dua pecahan dengan penyebut yang sama. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: Bandingkan kedua gambar berikut ini; isilah titik-titik dengan tanda <, =, atau >

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan cara membandingkan pecahan berpenyebut sama. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan representasi visual pecahan dan perbandingan pecahan sederhana. Tugas ini adalah latihan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2} | majority_2_of_3 / abstained | — |
| Dimensi pengetahuan | {"conceptual": 2} | majority_2_of_3 / abstained | — |
| Intended difficulty | {"Easy": 2} | majority_2_of_3 / abstained | — |

Adjudikasi AI: `success`; token `4538`.
Konten: `concern`; kunci: `conflict`; masalah: Terdapat ketidaksesuaian antara representasi visual pada gambar 'd' dengan pecahan yang tertulis di pilihan jawaban. Gambar kiri pada 'd' adalah persegi panjang 3x2 dengan 3 dari 6 bagian diarsir (3/6). Gambar kanan pada 'd' adalah persegi panjang yang dibagi menjadi 5 kolom vertikal dengan 2 kolom diarsir (2/5). Pilihan jawaban menggunakan pecahan 3/6 dan 2/6, yang tidak sesuai dengan gambar kanan (2/5)..
- Domain kognitif `None`: Soal tidak dapat diklasifikasikan secara akurat karena terdapat kesalahan fatal pada representasi visual (gambar kanan menunjukkan 2/5, bukan 2/6). Siswa tidak dapat melakukan perbandingan yang valid berdasarkan data yang diberikan.
- Dimensi pengetahuan `None`: Soal tidak dapat diklasifikasikan karena ketidaksesuaian data visual membuat tugas kognitif menjadi ambigu.
- Intended difficulty `None`: Soal tidak dapat dinilai tingkat kesulitannya karena data soal cacat (gambar tidak sesuai dengan pilihan jawaban).

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 207/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan dan Mengurutkan Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Bandingkan kedua gambar berikut ini, kemudian isilah titik-titik dengan tanda <, =, atau >.

d. ....
Pilihan: A. $\frac{3}{6} < \frac{4}{6}$
B. $\frac{3}{6} < \frac{2}{6}$
C. $\frac{3}{6} > \frac{2}{6}$
D. $\frac{3}{6} = \frac{2}{6}$
Transkripsi visual: Gambar d menunjukkan dua persegi panjang. Persegi panjang kiri dibagi menjadi grid 3x2 (6 kotak), dengan 3 kotak diarsir (3/6). Persegi panjang kanan dibagi menjadi 5 kolom vertikal, dengan 2 kolom diarsir (2/5).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidaksesuaian antara representasi visual pada gambar 'd' dengan pecahan yang tertulis di pilihan jawaban. Gambar kiri pada 'd' adalah persegi panjang 3x2 dengan 3 dari 6 bagian diarsir (3/6). Gambar kanan pada 'd' adalah persegi panjang yang dibagi menjadi 5 kolom vertikal dengan 2 kolom diarsir (2/5). Pilihan jawaban menggunakan pecahan 3/6 dan 2/6, yang tidak sesuai dengan gambar kanan (2/5)..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `ab3c3fc2501910ff7987e2df`

Populasi suku Batak di Indonesia $\frac{1}{20}$ dari penduduk Indonesia. Populasi suku Jawa di Indonesia $\frac{1}{6}$ dari penduduk Indonesia. Berapa jumlah populasi suku Batak dan suku Jawa dari seluruh penduduk Indonesia?

| Opsi | Isi |
|---|---|
| A | $\frac{7}{60}$ |
| B | $\frac{13}{60}$ |
| C | $\frac{2}{60}$ |
| D | $\frac{2}{26}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Samakan penyebut 1/20 dan 1/6 dengan KPK yaitu 60. 1/20 = 3/60 dan 1/6 = 10/60. Jumlahkan pembilangnya: 3/60 + 10/60 = 13/60.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c1811ce5e07bcaa4f178c95dc52411a677c6515d2c3013dcaec456ec9d294105`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2400 |
| 2 | success | valid / verified | applying | procedural | Medium | 2405 |
| 3 | success | valid / verified | applying | procedural | Easy | 2338 |

Run 1 — solusi: Menjumlahkan 1/20 dan 1/6 memerlukan penyamaan penyebut ke KPK yaitu 60. 1/20 menjadi 3/60 dan 1/6 menjadi 10/60. Hasil penjumlahannya adalah 3/60 + 10/60 = 13/60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan pecahan dengan penyebut berbeda yang sudah dipelajari di kelas 5. Soal bersifat rutin karena siswa hanya perlu melakukan konversi pecahan ke penyebut yang sama dan menjumlahkannya.. Bukti: Berapa jumlah populasi suku Batak dan suku Jawa dari seluruh penduduk Indonesia?
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma penjumlahan pecahan yang melibatkan penyamaan penyebut (KPK), yang merupakan prosedur standar dalam materi pecahan.. Bukti: 1/20 dari penduduk Indonesia; 1/6 dari penduduk Indonesia
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium bagi kelas 5. Meskipun prosedurnya rutin, siswa harus melakukan dua langkah terpisah: mencari KPK dari 20 dan 6, lalu melakukan konversi pecahan sebelum menjumlahkan. Ini melibatkan beberapa langkah saling terkait yang menuntut ketelitian lebih daripada sekadar penjumlahan pecahan berpenyebut sama.. Bukti: 1/20; 1/6; Berapa jumlah populasi suku Batak dan suku Jawa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan KPK. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan pecahan dengan penyebut berbeda adalah materi inti kelas 5. Tingkat kesulitan Medium tepat karena siswa harus mengintegrasikan konsep KPK ke dalam prosedur penjumlahan. |

Run 2 — solusi: Menjumlahkan 1/20 dan 1/6 memerlukan penyamaan penyebut ke KPK yaitu 60. 1/20 menjadi 3/60 dan 1/6 menjadi 10/60. Hasil penjumlahan 3/60 + 10/60 = 13/60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan pecahan dengan penyebut berbeda yang merupakan materi rutin di kelas 5. Soal ini menguji kemampuan siswa dalam memilih dan menerapkan algoritma penjumlahan pecahan.. Bukti: Berapa jumlah populasi suku Batak dan suku Jawa dari seluruh penduduk Indonesia?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang algoritma penjumlahan pecahan, termasuk mencari KPK untuk menyamakan penyebut, yang merupakan pengetahuan prosedural.. Bukti: Populasi suku Batak di Indonesia 1/20 dari penduduk Indonesia. Populasi suku Jawa di Indonesia 1/6 dari penduduk Indonesia.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dua langkah prosedural yang saling terkait: menentukan KPK dari penyebut (20 dan 6) dan melakukan konversi pecahan sebelum menjumlahkan. Meskipun prosedurnya familiar, terdapat beberapa langkah yang harus dikelola secara berurutan.. Bukti: 1/20 dari penduduk Indonesia; 1/6 dari penduduk Indonesia; Berapa jumlah populasi suku Batak dan suku Jawa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan penjumlahan pecahan dengan penyebut berbeda. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan pecahan dengan penyebut berbeda adalah standar kompetensi kelas 5. Soal ini menuntut ketelitian dalam konversi pecahan, namun jalurnya sangat jelas dan rutin. |

Run 3 — solusi: Samakan penyebut 1/20 dan 1/6 menjadi per 60. 1/20 = 3/60 dan 1/6 = 10/60. Jumlahkan pembilangnya: 3/60 + 10/60 = 13/60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan pecahan dengan penyebut berbeda yang sudah dipelajari di kelas 5. Soal ini merupakan penerapan rutin dari konsep penjumlahan pecahan.. Bukti: Berapa jumlah populasi suku Batak dan suku Jawa dari seluruh penduduk Indonesia?
- Dimensi pengetahuan `classify/procedural`: Siswa harus menggunakan algoritma atau metode untuk menyamakan penyebut (KPK) sebelum menjumlahkan pecahan, yang merupakan pengetahuan prosedural.. Bukti: 1/20 dari penduduk Indonesia; 1/6 dari penduduk Indonesia
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari prosedur penjumlahan pecahan dengan penyebut berbeda yang merupakan materi standar kelas 5. Jalur penyelesaian sangat jelas (menentukan KPK, mengubah pecahan, menjumlahkan).. Bukti: 1/20; 1/6; Berapa jumlah populasi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan senilai dan penjumlahan pecahan dengan penyebut berbeda. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan pecahan dengan penyebut berbeda adalah materi inti kelas 5. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga tingkat kesulitannya rendah bagi siswa kelas 5. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3942`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur penjumlahan pecahan dengan penyebut berbeda yang sudah dipelajari di kelas 5. Soal bersifat rutin karena siswa hanya perlu melakukan konversi pecahan ke penyebut yang sama dan menjumlahkannya.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang algoritma penjumlahan pecahan yang melibatkan penyamaan penyebut (KPK), yang merupakan prosedur standar dalam materi pecahan.
- Intended difficulty `Medium`: Soal ini tergolong Medium bagi kelas 5. Meskipun prosedurnya rutin, siswa harus melakukan dua langkah terpisah: mencari KPK dari 20 dan 6, lalu melakukan konversi pecahan sebelum menjumlahkan. Ini melibatkan beberapa langkah saling terkait yang menuntut ketelitian lebih daripada sekadar penjumlahan pecahan berpenyebut sama.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan KPK. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan pecahan dengan penyebut berbeda adalah materi inti kelas 5. Tingkat kesulitan Medium tepat karena siswa harus mengintegrasikan konsep KPK ke dalam prosedur penjumlahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 140/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000035; applying=0.999965; reasoning=0.000000 | applying | 0.999965 | 0.000360 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.001363; conceptual=0.964023; procedural=0.034613; metacognitive=0.000000 | conceptual | 0.964023 | 0.115949 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.670667; Medium=0.324235; Hard=0.005099 | Easy | 0.670667 | 0.600773 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999965; −Σp ln(p) = 0.000395; H = 0.000395/ln(3) = 0.000360; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.964023; −Σp ln(p) = 0.160739; H = 0.160739/ln(4) = 0.115949; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.670667; −Σp ln(p) = 0.660017; H = 0.660017/ln(3) = 0.600773; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Penjumlahan Bilangan Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Populasi suku Batak di Indonesia $\frac{1}{20}$ dari penduduk Indonesia. Populasi suku Jawa di Indonesia $\frac{1}{6}$ dari penduduk Indonesia. Berapa jumlah populasi suku Batak dan suku Jawa dari seluruh penduduk Indonesia?
Pilihan: A. $\frac{7}{60}$
B. $\frac{13}{60}$
C. $\frac{2}{60}$
D. $\frac{2}{26}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `fc9fe265c2c5380ee0471dba`

Populasi penduduk dari Kabupaten Sleman adalah $\frac{2}{5}$ dari penduduk Provinsi D.I. Yogyakarta. Adapun populasi penduduk Kabupaten Kulonprogo $\frac{1}{5}$ dari penduduk Provinsi D.I. Yogyakarta. Berapa jumlah populasi penduduk dari Kabupaten Sleman dan Kulonprogo?

| Opsi | Isi |
|---|---|
| A | $\frac{2}{25}$ |
| B | $\frac{3}{10}$ |
| C | $\frac{3}{5}$ |
| D | $\frac{1}{5}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jumlah populasi = (2/5) + (1/5) = (2+1)/5 = 3/5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `255bb3424de4d4a431692ea3b2d13add61bbf6038e52361855d142c29c25f44d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2308 |
| 2 | success | valid / verified | applying | procedural | Easy | 2241 |
| 3 | success | valid / verified | applying | procedural | Easy | 2283 |

Run 1 — solusi: Jumlah populasi = (2/5) + (1/5) = (2+1)/5 = 3/5.
- Domain kognitif `classify/applying`: Siswa diminta untuk menjumlahkan dua pecahan dengan penyebut yang sama. Ini adalah prosedur standar yang diajarkan di kelas 5, sehingga termasuk dalam domain applying.. Bukti: Populasi penduduk dari Kabupaten Sleman adalah 2/5 dari penduduk Provinsi D.I. Yogyakarta.; populasi penduduk Kabupaten Kulonprogo 1/5 dari penduduk Provinsi D.I. Yogyakarta.; Berapa jumlah populasi penduduk dari Kabupaten Sleman dan Kulonprogo?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma penjumlahan pecahan dengan penyebut yang sama, yang merupakan bagian dari pengetahuan prosedural.. Bukti: Berapa jumlah populasi penduduk dari Kabupaten Sleman dan Kulonprogo?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menjumlahkan dua pecahan dengan penyebut yang sama. Tidak ada langkah tambahan atau kendala yang kompleks.. Bukti: Populasi penduduk dari Kabupaten Sleman adalah 2/5 dari penduduk Provinsi D.I. Yogyakarta.; populasi penduduk Kabupaten Kulonprogo 1/5 dari penduduk Provinsi D.I. Yogyakarta.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan pecahan dengan penyebut sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan pecahan dengan penyebut sama adalah materi dasar kelas 5. Soal tidak memiliki jebakan atau langkah yang saling bergantung. |

Run 2 — solusi: Jumlah populasi = (2/5) + (1/5) = (2+1)/5 = 3/5.
- Domain kognitif `classify/applying`: Siswa diminta untuk menjumlahkan dua pecahan dengan penyebut yang sama. Ini adalah prosedur standar yang diajarkan di kelas 5, sehingga termasuk dalam domain applying.. Bukti: Berapa jumlah populasi penduduk dari Kabupaten Sleman dan Kulonprogo?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan pecahan dengan penyebut yang sama, yang merupakan bagian dari pengetahuan prosedural.. Bukti: Populasi penduduk dari Kabupaten Sleman adalah 2/5 ... populasi penduduk Kabupaten Kulonprogo 1/5
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah penyelesaian yang sangat jelas (penjumlahan langsung). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Berapa jumlah populasi penduduk dari Kabupaten Sleman dan Kulonprogo?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan pecahan dengan penyebut sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan operasi penjumlahan pecahan sederhana. Soal ini tidak menuntut pemahaman mendalam atau perencanaan langkah yang kompleks. |

Run 3 — solusi: Jumlah populasi = (2/5) + (1/5) = (2+1)/5 = 3/5.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menjumlahkan dua pecahan dengan penyebut yang sama. Ini adalah prosedur rutin yang langsung, sehingga masuk dalam domain applying.. Bukti: Berapa jumlah populasi penduduk dari Kabupaten Sleman dan Kulonprogo?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep penjumlahan pecahan dengan penyebut yang sama, yang merupakan bagian dari pengetahuan prosedural dalam operasi pecahan.. Bukti: Populasi penduduk dari Kabupaten Sleman adalah 2/5 dari penduduk Provinsi D.I. Yogyakarta.; populasi penduduk Kabupaten Kulonprogo 1/5 dari penduduk Provinsi D.I. Yogyakarta.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena penyebut pecahan sudah sama, sehingga tidak memerlukan konversi atau langkah tambahan yang kompleks. Siswa hanya perlu menjumlahkan pembilang.. Bukti: Populasi penduduk dari Kabupaten Sleman adalah 2/5 dari penduduk Provinsi D.I. Yogyakarta.; populasi penduduk Kabupaten Kulonprogo 1/5 dari penduduk Provinsi D.I. Yogyakarta.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan pecahan dengan penyebut sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan pecahan dengan penyebut sama adalah materi dasar kelas 5 yang sangat familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 152/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000014 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000560; conceptual=0.948159; procedural=0.051280; metacognitive=0.000000 | conceptual | 0.948159 | 0.149314 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.683066; Medium=0.311968; Hard=0.004966 | Easy | 0.683066 | 0.591749 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000016; H = 0.000016/ln(3) = 0.000014; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.948159; −Σp ln(p) = 0.206994; H = 0.206994/ln(4) = 0.149314; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.683066; −Σp ln(p) = 0.650103; H = 0.650103/ln(3) = 0.591749; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Penjumlahan Bilangan Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Populasi penduduk dari Kabupaten Sleman adalah $\frac{2}{5}$ dari penduduk Provinsi D.I. Yogyakarta. Adapun populasi penduduk Kabupaten Kulonprogo $\frac{1}{5}$ dari penduduk Provinsi D.I. Yogyakarta. Berapa jumlah populasi penduduk dari Kabupaten Sleman dan Kulonprogo?
Pilihan: A. $\frac{2}{25}$
B. $\frac{3}{10}$
C. $\frac{3}{5}$
D. $\frac{1}{5}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `3c69165f4b4cdf66760b5fe1`

Di daerah Nusa Tenggara Timur terdapat beberapa macam bahasa yang digunakan sehari-hari. Penggunaan bahasa Indonesia $\frac{1}{8}$ bagian. Penggunaan bahasa daerah $\frac{3}{10}$ bagian. Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?

| Opsi | Isi |
|---|---|
| A | $\frac{17}{40}$ |
| B | $\frac{2}{18}$ |
| C | $\frac{2}{40}$ |
| D | $\frac{7}{40}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Samakan penyebut 8 dan 10 menjadi 40. 3/10 = 12/40 dan 1/8 = 5/40. Selisih = 12/40 - 5/40 = 7/40.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `99ec7dd7c9ff0238e403842ee8a167f97f5c375299133849bdac9b045f684fcc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2356 |
| 2 | success | valid / verified | applying | procedural | Medium | 2334 |
| 3 | success | valid / verified | applying | procedural | Medium | 2366 |

Run 1 — solusi: Samakan penyebut dari 1/8 dan 3/10 menjadi per 40. 1/8 = 5/40 dan 3/10 = 12/40. Selisihnya adalah 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan pecahan dengan penyebut berbeda dalam konteks soal cerita sederhana. Ini adalah penerapan konsep yang sudah dipelajari di kelas 5.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode standar untuk pengurangan pecahan (menyamakan penyebut, lalu mengurangkan pembilang).. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari prosedur pengurangan pecahan dengan penyebut berbeda yang merupakan materi standar kelas 5. Jalur penyelesaiannya jelas (menyamakan penyebut ke KPK, lalu kurangi), tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan KPK untuk menyamakan penyebut. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan operasi hitung pecahan. Soal ini adalah latihan rutin tanpa jebakan atau kompleksitas tambahan. |

Run 2 — solusi: Samakan penyebut 8 dan 10 menjadi 40. 3/10 = 12/40 dan 1/8 = 5/40. Selisih = 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan pecahan dengan penyebut berbeda yang sudah dipelajari di kelas 5. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme standar untuk menyamakan penyebut dan melakukan pengurangan pecahan.. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan dua langkah prosedural yang saling terkait: mencari KPK dari penyebut (8 dan 10) dan melakukan pengurangan pecahan. Meskipun prosedurnya familiar, siswa harus melakukan konversi pecahan secara mandiri tanpa bantuan langkah antara.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan pecahan dengan penyebut berbeda, KPK. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengoperasikan pecahan dengan penyebut berbeda. Langkah-langkahnya jelas namun memerlukan ketelitian dalam konversi pecahan. |

Run 3 — solusi: Samakan penyebut 8 dan 10 menjadi 40. 3/10 = 12/40 dan 1/8 = 5/40. Selisihnya adalah 12/40 - 5/40 = 7/40.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan pecahan dengan penyebut berbeda dalam konteks soal cerita sederhana. Ini adalah penerapan konsep yang sudah dipelajari di kelas 5.. Bukti: Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode standar untuk menyamakan penyebut dan melakukan pengurangan pecahan.. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan dua langkah prosedural yang saling terkait: mencari KPK dari penyebut (8 dan 10) untuk menyamakan penyebut, lalu melakukan pengurangan. Meskipun prosedurnya rutin, siswa harus melakukan konversi pecahan secara mandiri tanpa bantuan langkah antara.. Bukti: Penggunaan bahasa Indonesia 1/8 bagian. Penggunaan bahasa daerah 3/10 bagian.; Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai, KPK, dan operasi pengurangan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah menguasai operasi pecahan dengan penyebut berbeda. Soal ini menguji kemampuan prosedural standar tanpa jebakan konseptual yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3891`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pengurangan pecahan dengan penyebut berbeda dalam konteks soal cerita sederhana. Ini adalah penerapan konsep yang sudah dipelajari di kelas 5.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritme standar untuk menyamakan penyebut dan melakukan pengurangan pecahan.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan dua langkah prosedural yang saling terkait: mencari KPK dari penyebut (8 dan 10) untuk menyamakan penyebut, lalu melakukan pengurangan. Meskipun prosedurnya rutin, siswa harus melakukan konversi pecahan secara mandiri tanpa bantuan langkah antara.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai, KPK, dan operasi pengurangan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah menguasai operasi pecahan dengan penyebut berbeda. Soal ini menguji kemampuan prosedural standar tanpa jebakan konseptual yang rumit, namun memerlukan ketelitian dalam konversi pecahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 149/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000024; applying=0.999976; reasoning=0.000000 | applying | 0.999976 | 0.000255 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000276; conceptual=0.972462; procedural=0.027262; metacognitive=0.000000 | conceptual | 0.972462 | 0.092060 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.693532; Medium=0.300466; Hard=0.006002 | Easy | 0.693532 | 0.587826 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999976; −Σp ln(p) = 0.000280; H = 0.000280/ln(3) = 0.000255; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.972462; −Σp ln(p) = 0.127623; H = 0.127623/ln(4) = 0.092060; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.693532; −Σp ln(p) = 0.645793; H = 0.645793/ln(3) = 0.587826; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Pengurangan Bilangan Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di daerah Nusa Tenggara Timur terdapat beberapa macam bahasa yang digunakan sehari-hari. Penggunaan bahasa Indonesia $\frac{1}{8}$ bagian. Penggunaan bahasa daerah $\frac{3}{10}$ bagian. Berapa bagian selisih penggunaan bahasa indonesia dan bahasa daerah dalam percakapan sehari-hari?
Pilihan: A. $\frac{17}{40}$
B. $\frac{2}{18}$
C. $\frac{2}{40}$
D. $\frac{7}{40}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `72d2df56927428ed8ca5cade`

Beni memiliki $1\frac{1}{8}$ bagian bika Ambon. Sebanyak $\frac{1}{8}$ bagian bika Ambon diberikan kepada neneknya. Berapa bagian sisa bika Ambon yang masih dimiliki Beni?

| Opsi | Isi |
|---|---|
| A | 1 |
| B | $1\frac{2}{8}$ |
| C | $\frac{7}{8}$ |
| D | $\frac{1}{8}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 1 1/8 - 1/8 = 1 + (1/8 - 1/8) = 1 + 0 = 1
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3f2b61b244e11949c4410a76a208a50de5f26ac08cb9bea0707b30b49a08ef9c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2255 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2320 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2296 |

Run 1 — solusi: Sisa bika Ambon = 1 1/8 - 1/8 = (9/8) - (1/8) = 8/8 = 1.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan pecahan campuran dengan penyebut yang sama. Prosedur ini merupakan materi rutin yang dipelajari di kelas 5.. Bukti: Beni memiliki 1 1/8 bagian bika Ambon. Sebanyak 1/8 bagian bika Ambon diberikan kepada neneknya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan pecahan campuran, yang termasuk dalam kategori prosedural.. Bukti: 1 1/8 - 1/8
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu melakukan satu operasi pengurangan pecahan dengan penyebut yang sama. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 1 1/8 - 1/8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan campuran dan operasi pengurangan pecahan dengan penyebut sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan pecahan dengan penyebut sama adalah kompetensi dasar kelas 5 yang bersifat langsung. |

Run 2 — solusi: 1 1/8 - 1/8 = (1 + 1/8) - 1/8 = 1 + (1/8 - 1/8) = 1 + 0 = 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi pengurangan pecahan campuran dengan penyebut yang sama. Prosedur ini sangat langsung dan merupakan aplikasi rutin dari konsep pengurangan pecahan yang sudah dipelajari di kelas 5.. Bukti: Beni memiliki 1 1/8 bagian bika Ambon.; Sebanyak 1/8 bagian bika Ambon diberikan kepada neneknya.; Berapa bagian sisa bika Ambon yang masih dimiliki Beni?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara melakukan pengurangan pada bilangan pecahan campuran dengan penyebut yang sama.. Bukti: 1 1/8 - 1/8
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengurangkan bagian pecahan dari pecahan campuran tersebut. Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang berinteraksi.. Bukti: 1 1/8 - 1/8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan campuran dan operasi pengurangan pecahan dengan penyebut sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan pecahan dengan penyebut sama adalah materi dasar kelas 5. Soal ini tidak memerlukan konversi bentuk atau langkah tambahan yang rumit. |

Run 3 — solusi: 1 1/8 - 1/8 = (1 + 1/8) - 1/8 = 1 + (1/8 - 1/8) = 1 + 0 = 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi pengurangan pecahan campuran dengan penyebut yang sama. Prosedur ini bersifat langsung dan rutin bagi siswa kelas 5.. Bukti: Beni memiliki 1 1/8 bagian bika Ambon. Sebanyak 1/8 bagian bika Ambon diberikan kepada neneknya. Berapa bagian sisa bika Ambon yang masih dimiliki Beni?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang pengurangan pecahan campuran dengan penyebut yang sama.. Bukti: 1 1/8 - 1/8
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep pengurangan pecahan dengan penyebut sama. Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang berinteraksi.. Bukti: 1 1/8 - 1/8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan campuran dan operasi pengurangan pecahan dengan penyebut sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari operasi hitung pecahan dengan penyebut sama. Soal ini tidak memerlukan konversi bentuk atau langkah tambahan yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3633`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk melakukan operasi pengurangan pecahan campuran dengan penyebut yang sama. Prosedur ini sangat langsung dan merupakan penerapan rutin dari konsep yang sudah dipelajari di kelas 5.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang algoritma pengurangan pecahan campuran dengan penyebut yang sama.
- Intended difficulty `Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu melakukan satu operasi pengurangan pecahan dengan penyebut yang sama. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan campuran dan operasi pengurangan pecahan dengan penyebut sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan pecahan dengan penyebut sama adalah kompetensi dasar kelas 5 yang bersifat langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 130/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000020; applying=0.999980; reasoning=0.000000 | applying | 0.999980 | 0.000211 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004097; conceptual=0.956733; procedural=0.039170; metacognitive=0.000000 | conceptual | 0.956733 | 0.138313 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.763015; Medium=0.231912; Hard=0.005072 | Easy | 0.763015 | 0.520744 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999980; −Σp ln(p) = 0.000232; H = 0.000232/ln(3) = 0.000211; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.956733; −Σp ln(p) = 0.191743; H = 0.191743/ln(4) = 0.138313; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.763015; −Σp ln(p) = 0.572096; H = 0.572096/ln(3) = 0.520744; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Pengurangan Bilangan Pecahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Beni memiliki $1\frac{1}{8}$ bagian bika Ambon. Sebanyak $\frac{1}{8}$ bagian bika Ambon diberikan kepada neneknya. Berapa bagian sisa bika Ambon yang masih dimiliki Beni?
Pilihan: A. 1
B. $1\frac{2}{8}$
C. $\frac{7}{8}$
D. $\frac{1}{8}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `f01f2f8c93ea076e4331abae`

Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut !

| Opsi | Isi |
|---|---|
| A | 6% |
| B | 60% |
| C | 0,6% |
| D | 40% |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Mengubah pecahan 6/10 menjadi per seratus dengan mengalikan pembilang dan penyebut dengan 10, sehingga 6/10 = 60/100 = 60%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ca4aa16f10e4ec3893f4fdbe371b14ce0f641cff34f190b3b84d5dd269ff78da`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2259 |
| 2 | success | valid / verified | applying | procedural | Easy | 2265 |
| 3 | success | valid / verified | applying | procedural | Easy | 2306 |

Run 1 — solusi: Mengubah pecahan 6/10 menjadi per seratus dengan mengalikan pembilang dan penyebut dengan 10, sehingga 6/10 = 60/100 = 60%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur mengubah pecahan biasa ke bentuk persen. Prosedur ini merupakan standar yang dipelajari di kelas 5, sehingga termasuk kategori applying.. Bukti: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode konversi pecahan ke persen, yang merupakan pengetahuan prosedural.. Bukti: Tentukan berapa persen soal yang dijawab benar tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu langkah konversi pecahan ke persen (6/10 = 60/100). Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 6 pertanyaan dari 10 soal; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan konsep dasar persen sebagai per seratus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi pecahan ke persen adalah materi dasar kelas 5. Soal ini tidak memerlukan langkah tambahan atau penalaran tingkat tinggi. |

Run 2 — solusi: Siswa perlu mengubah pecahan 6/10 menjadi per seratus agar menjadi persen. 6/10 = (6 x 10) / (10 x 10) = 60/100 = 60%.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur mengubah pecahan biasa ke bentuk persen. Ini adalah penerapan konsep pecahan dan persen yang sudah dipelajari di kelas 5.. Bukti: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau metode mengubah penyebut pecahan menjadi 100 untuk menentukan nilai persen.. Bukti: Tentukan berapa persen soal yang dijawab benar tersebut
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan prosedur standar yang familiar bagi siswa kelas 5. Langkah penyelesaiannya langsung dan tidak memerlukan perencanaan kompleks.. Bukti: 6 pertanyaan dari 10 soal; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan konsep dasar persen sebagai per seratus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengubah pecahan 6/10 menjadi 60/100 adalah materi dasar kelas 5. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin. |

Run 3 — solusi: Siswa perlu mengubah pecahan 6/10 menjadi bentuk per seratus agar menjadi persen. 6/10 = (6 x 10) / (10 x 10) = 60/100 = 60%.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur mengubah pecahan biasa ke bentuk persen. Prosedur ini merupakan standar yang dipelajari di kelas 5, sehingga siswa hanya perlu menerapkan konsep yang sudah familiar.. Bukti: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau metode konversi pecahan ke persen (mengubah penyebut menjadi 100 atau mengalikan dengan 100%).. Bukti: Tentukan berapa persen soal yang dijawab benar tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 5. Langkah penyelesaiannya jelas (mengubah pecahan ke persen), tidak ada kendala yang berinteraksi, dan beban kalkulasi sangat rendah.. Bukti: 6 pertanyaan dari 10 soal; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pecahan sebagai bagian dari keseluruhan dan ekuivalensi pecahan dengan penyebut 100. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengubah pecahan 6/10 menjadi persen adalah materi dasar kelas 5. Siswa hanya perlu melakukan satu kali konversi sederhana tanpa langkah perencanaan yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 84/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.103739; applying=0.896261; reasoning=0.000000 | applying | 0.896261 | 0.303311 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.140868; conceptual=0.829238; procedural=0.029894; metacognitive=0.000000 | conceptual | 0.829238 | 0.386856 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.843078; Medium=0.154434; Hard=0.002488 | Easy | 0.843078 | 0.407160 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.896261; −Σp ln(p) = 0.333221; H = 0.333221/ln(3) = 0.303311; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.829238; −Σp ln(p) = 0.536296; H = 0.536296/ln(4) = 0.386856; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.843078; −Σp ln(p) = 0.447311; H = 0.447311/ln(3) = 0.407160; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Menghubungkan Pecahan Desimal Perseratusan dengan Konsep Persen
Tipe soal: multiple_choice
Stimulus: -
Soal: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut !
Pilihan: A. 6%
B. 60%
C. 0,6%
D. 40%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `a9e11957b4596092e41bbc15`

Aku berlari mengelilingi tepian lapangan bola. Perhatikan kembali lintasan berlari Asep di lapangan sepak bola. Lapangan sepak bola dapat kita lihat sebagai bangun datar.<br>50 m<br>100 m<br><br>Bagaimana menentukan panjang lintasan berlarinya?

| Opsi | Isi |
|---|---|
| A | 100 × 50 = 5.000 m |
| B | 4 × 100 = 400 m |
| C | 100 + 50 + 100 + 50 = 300 m |
| D | 100 + 50 = 150 m |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Keliling lapangan adalah jumlah seluruh sisi tepinya. Lapangan berbentuk persegi panjang dengan panjang 100 m dan lebar 50 m. Keliling = 100 + 50 + 100 + 50 = 300 m.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5cc340b71e66414dce5bb5567e789f9d491bce83c3fdc77ace8589dfc368a277`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3006 |
| 2 | success | valid / verified | applying | procedural | Easy | 2398 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2319 |

Run 1 — solusi: Keliling lapangan adalah jumlah panjang seluruh sisinya: 100 m + 50 m + 100 m + 50 m = 300 m.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep keliling bangun datar (jumlah seluruh sisi) ke dalam konteks nyata (berlari mengelilingi lapangan). Ini adalah penerapan konsep dasar.. Bukti: Aku berlari mengelilingi tepian lapangan bola; Bagaimana menentukan panjang lintasan berlarinya?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa mengenai konsep keliling sebagai penjumlahan panjang sisi-sisi bangun datar.. Bukti: Bagaimana menentukan panjang lintasan berlarinya?; 100 + 50 + 100 + 50 = 300 m
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung konsep keliling untuk bangun datar sederhana (persegi panjang). Jalur penyelesaian sangat jelas dan tidak memerlukan perencanaan kompleks.. Bukti: 50 m; 100 m; Bagaimana menentukan panjang lintasan berlarinya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan dan konsep sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung keliling persegi panjang dengan menjumlahkan keempat sisinya adalah materi standar kelas 5 yang bersifat rutin. |

Run 2 — solusi: Keliling lapangan berbentuk persegi panjang adalah jumlah seluruh sisinya: 100 m + 50 m + 100 m + 50 m = 300 m.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan konsep keliling bangun datar (persegi panjang) pada konteks nyata (lapangan bola). Ini adalah penerapan prosedur yang sudah dipelajari.. Bukti: Bagaimana menentukan panjang lintasan berlarinya?; 100 + 50 + 100 + 50 = 300 m
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur menghitung keliling bangun datar dengan menjumlahkan panjang sisi-sisinya.. Bukti: Bagaimana menentukan panjang lintasan berlarinya?; 100 + 50 + 100 + 50 = 300 m
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami konsep keliling sebagai jumlah seluruh sisi luar bangun datar. Tidak ada kendala yang berinteraksi atau perencanaan kompleks yang diperlukan.. Bukti: Aku berlari mengelilingi tepian lapangan bola.; 100 + 50 + 100 + 50 = 300 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep keliling bangun datar dan penjumlahan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling persegi panjang dengan menjumlahkan sisi-sisinya adalah materi dasar yang rutin dan familiar. |

Run 3 — solusi: Keliling lapangan adalah jumlah seluruh sisi tepinya. Lapangan berbentuk persegi panjang dengan panjang 100 m dan lebar 50 m. Keliling = 100 + 50 + 100 + 50 = 300 m.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep keliling bangun datar (persegi panjang) pada konteks nyata yang rutin. Siswa perlu mengenali bahwa mengelilingi lapangan berarti menjumlahkan seluruh panjang sisi-sisinya.. Bukti: Bagaimana menentukan panjang lintasan berlarinya?; Aku berlari mengelilingi tepian lapangan bola.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa itu keliling (jumlah sisi-sisi) dibandingkan dengan luas atau setengah keliling.. Bukti: Lapangan sepak bola dapat kita lihat sebagai bangun datar.; 100 + 50 + 100 + 50 = 300 m
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena konsep keliling adalah materi dasar kelas 5. Jalur penyelesaian sangat jelas (menjumlahkan keempat sisi) dan tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: 100 m; 50 m; 100 + 50 + 100 + 50 = 300 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan bilangan dan konsep keliling sebagai jumlah panjang sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan konsep keliling bangun datar sederhana. Soal ini hanya meminta penerapan langsung definisi keliling tanpa modifikasi atau langkah tambahan yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3912`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep keliling bangun datar (persegi panjang) pada konteks nyata. Siswa perlu mengenali bahwa mengelilingi lapangan berarti menjumlahkan seluruh panjang sisi-sisinya, yang merupakan penerapan prosedur rutin.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang keliling sebagai jumlah sisi-sisi bangun datar, membedakannya dari konsep luas atau setengah keliling.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena konsep keliling adalah materi dasar kelas 5. Jalur penyelesaian sangat jelas (menjumlahkan keempat sisi) dan tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan bilangan dan konsep keliling sebagai jumlah panjang sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan konsep keliling bangun datar sederhana. Soal ini hanya meminta penerapan langsung definisi keliling tanpa modifikasi atau langkah tambahan yang rumit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 114/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001028; applying=0.998972; reasoning=0.000000 | applying | 0.998972 | 0.007372 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.690649; conceptual=0.271514; procedural=0.037838; metacognitive=0.000000 | factual | 0.690649 | 0.529114 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.868100; Medium=0.129409; Hard=0.002491 | Easy | 0.868100 | 0.366223 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998972; −Σp ln(p) = 0.008099; H = 0.008099/ln(3) = 0.007372; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.690649; −Σp ln(p) = 0.733508; H = 0.733508/ln(4) = 0.529114; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.868100; −Σp ln(p) = 0.402337; H = 0.402337/ln(3) = 0.366223; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Apakah Keliling Bangun Datar Itu?
Tipe soal: multiple_choice
Stimulus: -
Soal: Aku berlari mengelilingi tepian lapangan bola. Perhatikan kembali lintasan berlari Asep di lapangan sepak bola. Lapangan sepak bola dapat kita lihat sebagai bangun datar.
50 m
100 m

Bagaimana menentukan panjang lintasan berlarinya?
Pilihan: A. 100 × 50 = 5.000 m
B. 4 × 100 = 400 m
C. 100 + 50 + 100 + 50 = 300 m
D. 100 + 50 = 150 m
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `cc5fd01ffa204b51f2db5c54`

Sekarang, perhatikan gambar-gambar berikut. Tentukan berapa kelilingnya?.

| Opsi | Isi |
|---|---|
| A | Keliling = 4 × 4 = 16 cm |
| B | Keliling = 4 + 5 + 5 = 14 cm |
| C | Keliling = 4 × 5 = 20 cm |
| D | Keliling = 4 + 5 + 5 + 5 = 19 cm |

![Gambar sumber soal 28](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0130-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Keliling adalah jumlah panjang seluruh sisi luar bangun datar. Untuk bangun kedua (trapesium), keliling = 4 cm + 5 cm + 5 cm + 5 cm = 19 cm.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0130-06.png. Transkripsi visual: Terdapat dua bangun datar. Bangun pertama adalah persegi (atau belah ketupat) dengan keempat sisinya masing-masing berukuran 4 cm. Bangun kedua adalah trapesium dengan sisi atas 4 cm, sisi bawah 5 cm, dan dua sisi miring masing-masing 5 cm. Terdapat tanda panah yang menunjukkan arah penelusuran keliling pada setiap sisi.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bfe1a12ceac25002cb668bb11354c8b600d46022d9e722ea969587fa894bd44b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3519 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3465 |
| 3 | success | valid / conflict | applying | procedural | Easy | 3469 |

Run 1 — solusi: Keliling adalah jumlah seluruh sisi luar bangun datar. Untuk bangun kedua (trapesium), keliling = 4 cm + 5 cm + 5 cm + 5 cm = 19 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi keliling sebagai jumlah panjang sisi-sisi bangun datar pada bangun trapesium yang sisi-sisinya sudah diketahui.. Bukti: Tentukan berapa kelilingnya?; Keliling = 4 + 5 + 5 + 5 = 19 cm
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur penjumlahan panjang sisi untuk menentukan keliling bangun datar.. Bukti: Tentukan berapa kelilingnya?; Keliling = 4 + 5 + 5 + 5 = 19 cm
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menjumlahkan angka-angka yang sudah tertera pada gambar. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Tentukan berapa kelilingnya?; 4 + 5 + 5 + 5 = 19 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep keliling sebagai jumlah panjang sisi-sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menjumlahkan sisi-sisi bangun datar adalah prosedur yang sangat dasar dan familiar. |

Run 2 — solusi: Keliling bangun kedua (trapesium) adalah jumlah dari panjang keempat sisinya: 4 cm + 5 cm + 5 cm + 5 cm = 19 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep keliling sebagai jumlah panjang sisi-sisi bangun datar pada bangun trapesium yang diberikan. Ini adalah penerapan langsung dari definisi keliling.. Bukti: Tentukan berapa kelilingnya?; Keliling = 4 + 5 + 5 + 5 = 19 cm
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang keliling sebagai jumlah panjang sisi-sisi bangun datar.. Bukti: Tentukan berapa kelilingnya?; Keliling = 4 + 5 + 5 + 5 = 19 cm
- Intended difficulty `classify/Easy`: Soal ini meminta siswa menjumlahkan panjang sisi-sisi bangun datar. Prosedurnya sangat rutin dan langsung, dengan beban kognitif yang rendah bagi siswa kelas 5.. Bukti: Tentukan berapa kelilingnya?; Keliling = 4 + 5 + 5 + 5 = 19 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling sebagai jumlah panjang sisi-sisi bangun datar dan kemampuan penjumlahan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat familiar dengan konsep keliling bangun datar sederhana dan penjumlahan bilangan satu digit. |

Run 3 — solusi: Keliling trapesium adalah jumlah semua sisinya: 4 cm + 5 cm + 5 cm + 5 cm = 19 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep keliling sebagai jumlah panjang sisi-sisi bangun datar pada bangun trapesium yang sisi-sisinya sudah diketahui.. Bukti: Tentukan berapa kelilingnya?
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang cara menghitung keliling bangun datar dengan menjumlahkan panjang sisi-sisinya.. Bukti: Tentukan berapa kelilingnya?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menjumlahkan panjang sisi-sisi yang sudah tertera secara eksplisit pada gambar. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Tentukan berapa kelilingnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling sebagai jumlah panjang sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat familiar dengan konsep keliling bangun datar sederhana dan operasi penjumlahan bilangan bulat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4843`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan definisi keliling sebagai jumlah panjang sisi-sisi bangun datar pada bangun trapesium yang sisi-sisinya sudah diketahui secara eksplisit.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung keliling bangun datar dengan menjumlahkan panjang sisi-sisinya.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menjumlahkan angka-angka yang sudah tertera pada gambar. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep keliling sebagai jumlah panjang sisi-sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menjumlahkan sisi-sisi bangun datar adalah prosedur yang sangat dasar dan familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 159/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.063586; applying=0.936414; reasoning=0.000000 | applying | 0.936414 | 0.215473 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.205827; conceptual=0.774001; procedural=0.020172; metacognitive=0.000000 | conceptual | 0.774001 | 0.434526 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.815073; Medium=0.181699; Hard=0.003229 | Easy | 0.815073 | 0.450616 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.936414; −Σp ln(p) = 0.236721; H = 0.236721/ln(3) = 0.215473; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.774001; −Σp ln(p) = 0.602382; H = 0.602382/ln(4) = 0.434526; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.815073; −Σp ln(p) = 0.495053; H = 0.495053/ln(3) = 0.450616; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Apakah Keliling Bangun Datar Itu?
Tipe soal: multiple_choice
Stimulus: -
Soal: Sekarang, perhatikan gambar-gambar berikut. Tentukan berapa kelilingnya?.
Pilihan: A. Keliling = 4 × 4 = 16 cm
B. Keliling = 4 + 5 + 5 = 14 cm
C. Keliling = 4 × 5 = 20 cm
D. Keliling = 4 + 5 + 5 + 5 = 19 cm
Transkripsi visual: Terdapat dua bangun datar. Bangun pertama adalah persegi (atau belah ketupat) dengan keempat sisinya masing-masing berukuran 4 cm. Bangun kedua adalah trapesium dengan sisi atas 4 cm, sisi bawah 5 cm, dan dua sisi miring masing-masing 5 cm. Terdapat tanda panah yang menunjukkan arah penelusuran keliling pada setiap sisi.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `c234ac355c404df57cd80cef`

Bagaimana cara menghitung keliling bangun datar tersebut?

| Opsi | Isi |
|---|---|
| A | Keliling = 6 × 4 = 24 cm |
| B | Keliling = 3 × 6 = 18 cm |
| C | Keliling = 6 + 4 = 10 cm |
| D | Keliling = 6 + 6 + 4 = 16 cm |

![Gambar sumber soal 29](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0133-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Keliling segitiga adalah jumlah panjang ketiga sisinya. Berdasarkan gambar, sisi-sisinya adalah 6 cm, 6 cm, dan 4 cm. Maka, keliling = 6 + 6 + 4 = 16 cm.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0133-06.png. Transkripsi visual: Gambar menunjukkan sebuah segitiga dengan panjang sisi 6 cm, 6 cm, dan 4 cm. Terdapat tanda garis pada dua sisi yang panjangnya 6 cm, menunjukkan bahwa kedua sisi tersebut sama panjang. Seorang karakter kartun bertanya 'Apakah ada sisi-sisi yang sama panjang?'

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e08dafa8e74c98edde0a49f35a49a7eb51787189c2cf7eb37237320f58ecc585`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3428 |
| 2 | success | valid / verified | applying | procedural | Easy | 3435 |
| 3 | success | valid / verified | applying | procedural | Easy | 3442 |

Run 1 — solusi: Keliling segitiga adalah jumlah panjang ketiga sisinya. Berdasarkan gambar, sisi-sisinya adalah 6 cm, 6 cm, dan 4 cm. Maka, keliling = 6 + 6 + 4 = 16 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur dasar menghitung keliling (penjumlahan panjang sisi) pada bangun segitiga yang diberikan. Ini adalah penerapan konsep rutin.. Bukti: Bagaimana cara menghitung keliling bangun datar tersebut?; 6 + 6 + 4 = 16 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung keliling bangun datar dengan menjumlahkan panjang sisi-sisinya.. Bukti: Keliling = 6 + 6 + 4 = 16 cm
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi panjang ketiga sisi dari gambar (yang sudah diberi label) dan menjumlahkannya. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: 6 cm, 6 cm, dan 4 cm; Keliling = 6 + 6 + 4 = 16 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep keliling sebagai jumlah panjang sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling segitiga dengan panjang sisi yang sudah diketahui adalah tugas rutin yang sangat mendasar. |

Run 2 — solusi: Keliling segitiga adalah jumlah panjang ketiga sisinya. Berdasarkan gambar, sisi-sisinya adalah 6 cm, 6 cm, dan 4 cm. Maka, keliling = 6 + 6 + 4 = 16 cm.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan definisi keliling (penjumlahan semua sisi) pada bangun segitiga yang diberikan. Ini adalah penerapan prosedur rutin pada konteks yang sudah jelas.. Bukti: Bagaimana cara menghitung keliling bangun datar tersebut?; 6 + 6 + 4 = 16 cm
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menggunakan prosedur penjumlahan untuk menghitung keliling, yang merupakan metode standar dalam geometri dasar.. Bukti: Keliling = 6 + 6 + 4 = 16 cm
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi kelas 5. Siswa hanya perlu mengidentifikasi panjang ketiga sisi dari gambar dan menjumlahkannya. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: Bagaimana cara menghitung keliling bangun datar tersebut?; 6 cm, 6 cm, dan 4 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah panjang sisi dan kemampuan penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi keliling segitiga adalah topik dasar kelas 4/5. Soal ini langsung menanyakan prosedur standar tanpa modifikasi atau tuntutan penalaran tambahan. |

Run 3 — solusi: Keliling segitiga adalah jumlah panjang ketiga sisinya. Berdasarkan gambar, sisi-sisinya adalah 6 cm, 6 cm, dan 4 cm. Maka, keliling = 6 + 6 + 4 = 16 cm.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur dasar menghitung keliling segitiga dengan menjumlahkan panjang ketiga sisinya. Soal ini bersifat rutin dan langsung.. Bukti: Bagaimana cara menghitung keliling bangun datar tersebut?; 6 + 6 + 4 = 16 cm
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep keliling sebagai jumlah sisi-sisi bangun datar dan menerapkan prosedur penjumlahan untuk menyelesaikannya.. Bukti: Keliling = 6 + 6 + 4 = 16 cm
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 5. Prosedur penjumlahan sisi untuk mencari keliling adalah rutin, jalur penyelesaiannya sangat jelas, dan tidak ada kendala yang kompleks.. Bukti: Bagaimana cara menghitung keliling bangun datar tersebut?; 6 + 6 + 4 = 16 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah sisi dan kemampuan penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari keliling segitiga dengan menjumlahkan sisi-sisinya adalah materi dasar yang sudah dikuasai di kelas 5. Tidak ada tuntutan perencanaan atau integrasi yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 134/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.430206; applying=0.569794; reasoning=0.000000 | applying | 0.569794 | 0.622033 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.082327; conceptual=0.909954; procedural=0.007719; metacognitive=0.000000 | conceptual | 0.909954 | 0.237312 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.787554; Medium=0.208337; Hard=0.004110 | Easy | 0.787554 | 0.489221 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.569794; −Σp ln(p) = 0.683373; H = 0.683373/ln(3) = 0.622033; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.909954; −Σp ln(p) = 0.328984; H = 0.328984/ln(4) = 0.237312; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.787554; −Σp ln(p) = 0.537464; H = 0.537464/ln(3) = 0.489221; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Bagaimana cara menghitung keliling bangun datar tersebut?
Pilihan: A. Keliling = 6 × 4 = 24 cm
B. Keliling = 3 × 6 = 18 cm
C. Keliling = 6 + 4 = 10 cm
D. Keliling = 6 + 6 + 4 = 16 cm
Transkripsi visual: Gambar menunjukkan sebuah segitiga dengan panjang sisi 6 cm, 6 cm, dan 4 cm. Terdapat tanda garis pada dua sisi yang panjangnya 6 cm, menunjukkan bahwa kedua sisi tersebut sama panjang. Seorang karakter kartun bertanya 'Apakah ada sisi-sisi yang sama panjang?'
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `b1b0e3eb7042a38fd736f941`

Apakah nama bangun datar berikut?

| Opsi | Isi |
|---|---|
| A | Segitiga sembarang |
| B | Segitiga siku-siku |
| C | Segitiga sama sisi |
| D | Segitiga sama kaki |

![Gambar sumber soal 30](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0133-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Segitiga memiliki tiga sisi dengan panjang 6 cm, 6 cm, dan 4 cm. Karena terdapat dua sisi yang sama panjang (6 cm dan 6 cm), maka segitiga tersebut diklasifikasikan sebagai segitiga sama kaki.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0133-06.png. Transkripsi visual: Gambar menunjukkan sebuah segitiga dengan panjang sisi 6 cm, 6 cm, dan 4 cm. Dua sisi yang masing-masing berukuran 6 cm ditandai dengan simbol garis kecil (tanda centang atau coretan) yang identik, menunjukkan bahwa kedua sisi tersebut sama panjang. Terdapat ilustrasi seorang siswa yang bertanya 'Apakah ada sisi-sisi yang sama panjang?'

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4a1c7e5520d58bdaae8a96987c5b1b92f31dff4931378a8e6bb226c57e69b037`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3408 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3459 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3386 |

Run 1 — solusi: Segitiga memiliki tiga sisi dengan panjang 6 cm, 6 cm, dan 4 cm. Karena terdapat dua sisi yang sama panjang (6 cm dan 6 cm), maka segitiga tersebut diklasifikasikan sebagai segitiga sama kaki.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi jenis segitiga berdasarkan properti panjang sisi yang diberikan secara eksplisit pada gambar. Ini adalah tugas pengenalan sifat bangun datar yang langsung.. Bukti: Apakah nama bangun datar berikut?; dua sisi yang masing-masing berukuran 6 cm ditandai dengan simbol garis kecil
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman definisi segitiga sama kaki (konsep) berdasarkan atribut panjang sisi yang diberikan.. Bukti: Apakah nama bangun datar berikut?; dua sisi yang masing-masing berukuran 6 cm ditandai dengan simbol garis kecil
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengamati tanda pada gambar dan menerapkan definisi segitiga sama kaki. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: Apakah nama bangun datar berikut?; dua sisi yang masing-masing berukuran 6 cm ditandai dengan simbol garis kecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama kaki dan kemampuan membaca tanda kesamaan panjang sisi pada gambar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi jenis segitiga berdasarkan panjang sisi adalah materi dasar yang rutin dan tidak memerlukan penalaran tingkat tinggi. |

Run 2 — solusi: Segitiga memiliki tiga sisi dengan panjang 6 cm, 6 cm, dan 4 cm. Karena terdapat dua sisi yang sama panjang (6 cm dan 6 cm), maka segitiga tersebut diklasifikasikan sebagai segitiga sama kaki.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi jenis segitiga berdasarkan properti panjang sisi yang diberikan secara eksplisit pada gambar. Ini adalah tugas pengenalan sifat bangun datar dasar.. Bukti: Apakah nama bangun datar berikut?; panjang sisi-sisinya 6 cm, 6 cm, dan 4 cm; dua sisi yang panjangnya 6 cm ditandai dengan simbol garis kecil
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman definisi dan klasifikasi segitiga berdasarkan panjang sisinya, yang merupakan konsep dasar geometri.. Bukti: Apakah nama bangun datar berikut?; panjang sisi-sisinya 6 cm, 6 cm, dan 4 cm
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengamati label angka dan tanda pada gambar untuk menyimpulkan bahwa dua sisi sama panjang. Tidak ada langkah perhitungan atau perencanaan yang diperlukan.. Bukti: panjang sisi-sisinya 6 cm, 6 cm, dan 4 cm; dua sisi yang panjangnya 6 cm ditandai dengan simbol garis kecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama kaki (memiliki dua sisi sama panjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi jenis segitiga berdasarkan panjang sisi adalah materi dasar yang rutin dan tidak memerlukan penalaran kompleks. |

Run 3 — solusi: Segitiga tersebut memiliki dua sisi dengan panjang yang sama, yaitu 6 cm dan 6 cm, sementara sisi ketiga panjangnya 4 cm. Berdasarkan definisi, segitiga dengan tepat dua sisi sama panjang disebut segitiga sama kaki.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi jenis segitiga berdasarkan properti panjang sisinya yang diberikan secara eksplisit. Ini adalah tugas pengenalan konsep dasar.. Bukti: Apakah nama bangun datar berikut?; segitiga dengan panjang sisi 6 cm, 6 cm, dan 4 cm
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman definisi klasifikasi segitiga berdasarkan panjang sisi (konseptual).. Bukti: segitiga sama kaki; dua sisinya sama panjang (6 cm dan 6 cm)
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membandingkan panjang sisi yang diberikan dan mencocokkannya dengan definisi segitiga sama kaki. Tidak ada langkah perantara atau integrasi yang kompleks.. Bukti: Apakah nama bangun datar berikut?; 6 cm, 6 cm, dan 4 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama kaki, sama sisi, dan sembarang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi jenis segitiga berdasarkan panjang sisi adalah materi dasar yang sangat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 124/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001598; applying=0.998402; reasoning=0.000000 | applying | 0.998402 | 0.010822 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.173313; conceptual=0.811826; procedural=0.014861; metacognitive=0.000000 | conceptual | 0.811826 | 0.386318 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.842950; Medium=0.154188; Hard=0.002862 | Easy | 0.842950 | 0.408738 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998402; −Σp ln(p) = 0.011889; H = 0.011889/ln(3) = 0.010822; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.811826; −Σp ln(p) = 0.535550; H = 0.535550/ln(4) = 0.386318; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.842950; −Σp ln(p) = 0.449045; H = 0.449045/ln(3) = 0.408738; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Apakah nama bangun datar berikut?
Pilihan: A. Segitiga sembarang
B. Segitiga siku-siku
C. Segitiga sama sisi
D. Segitiga sama kaki
Transkripsi visual: Gambar menunjukkan sebuah segitiga dengan panjang sisi 6 cm, 6 cm, dan 4 cm. Dua sisi yang masing-masing berukuran 6 cm ditandai dengan simbol garis kecil (tanda centang atau coretan) yang identik, menunjukkan bahwa kedua sisi tersebut sama panjang. Terdapat ilustrasi seorang siswa yang bertanya 'Apakah ada sisi-sisi yang sama panjang?'
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `1227c8e81090cfbb43cbc1c3`

Bagaimana cara menghitung keliling bangun datar berikut?

| Opsi | Isi |
|---|---|
| A | Keliling = 5 × 3 = 15 cm |
| B | Keliling = 5 + 3 = 8 cm |
| C | Keliling = (2 × 5) + (2 × 3) = 16 cm |
| D | Keliling = 4 × 5 = 20 cm |

![Gambar sumber soal 31](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0135-05.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Keliling jajar genjang adalah jumlah keempat sisinya: 5 cm + 3 cm + 5 cm + 3 cm = 16 cm, atau (2 x 5 cm) + (2 x 3 cm) = 16 cm.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0135-05.png. Transkripsi visual: Gambar a menampilkan jajar genjang dengan panjang sisi sejajar 5 cm dan 3 cm. Gambar b menampilkan layang-layang dengan label sisi 2 cm dan 4 cm, disertai pertanyaan 'Apakah ada sisi-sisi yang sama panjang?'. Soal utama merujuk pada cara menghitung keliling bangun datar (jajar genjang pada gambar a).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f87d3c8933c212edb2d35ae58f32f924609ec04a553a7d34c6e29775c9b9a4d0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3524 |
| 2 | success | valid / verified | applying | procedural | Easy | 3578 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3532 |

Run 1 — solusi: Keliling jajar genjang adalah jumlah keempat sisinya: 5 cm + 3 cm + 5 cm + 3 cm = 16 cm, atau (2 x 5 cm) + (2 x 3 cm) = 10 cm + 6 cm = 16 cm.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerapkan rumus keliling jajar genjang yang sudah dipelajari. Siswa hanya perlu mengidentifikasi panjang sisi-sisi yang diketahui dan menerapkan prosedur penjumlahan sisi atau rumus keliling yang umum.. Bukti: Bagaimana cara menghitung keliling bangun datar berikut?; Keliling = (2 × 5) + (2 × 3) = 16 cm
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur rutin untuk menghitung keliling bangun datar berdasarkan panjang sisi yang diberikan.. Bukti: Keliling = (2 × 5) + (2 × 3) = 16 cm
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali sifat jajar genjang (sisi berhadapan sama panjang) dan menjumlahkan keempat sisinya. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Bagaimana cara menghitung keliling bangun datar berikut?; 5 cm; 3 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah panjang sisi-sisi bangun datar dan sifat jajar genjang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling jajar genjang dengan panjang sisi yang sudah tertera secara eksplisit adalah tugas yang sangat mendasar dan familiar. |

Run 2 — solusi: Keliling jajar genjang adalah jumlah seluruh sisinya: 5 cm + 3 cm + 5 cm + 3 cm = 16 cm, atau (2 x 5 cm) + (2 x 3 cm) = 10 cm + 6 cm = 16 cm.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus keliling bangun datar (jajar genjang) yang sudah dipelajari. Soal ini bersifat rutin karena hanya memerlukan pemahaman konsep keliling sebagai jumlah panjang sisi-sisi bangun datar.. Bukti: Bagaimana cara menghitung keliling bangun datar berikut?; Gambar a menunjukkan bangun datar jajar genjang dengan panjang sisi atas dan bawah masing-masing 5 cm, serta panjang sisi kiri dan kanan masing-masing 3 cm.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung keliling bangun datar dengan menjumlahkan panjang sisi-sisinya.. Bukti: Bagaimana cara menghitung keliling bangun datar berikut?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengidentifikasi panjang sisi-sisi jajar genjang dan menerapkan rumus keliling dasar. Tidak ada kendala yang berinteraksi atau langkah yang kompleks.. Bukti: Bagaimana cara menghitung keliling bangun datar berikut?; Gambar a menunjukkan bangun datar jajar genjang dengan panjang sisi atas dan bawah masing-masing 5 cm, serta panjang sisi kiri dan kanan masing-masing 3 cm.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling bangun datar sebagai jumlah panjang sisi-sisinya. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa menghitung keliling bangun datar sederhana. Soal ini merupakan penerapan langsung dari definisi keliling. |

Run 3 — solusi: Keliling jajar genjang adalah jumlah keempat sisinya: 5 cm + 3 cm + 5 cm + 3 cm = 16 cm, atau (2 x 5 cm) + (2 x 3 cm) = 16 cm.
- Domain kognitif `classify/applying`: Soal meminta siswa mengidentifikasi rumus atau prosedur yang tepat untuk menghitung keliling jajar genjang berdasarkan panjang sisi yang diketahui. Ini adalah penerapan langsung dari konsep keliling (penjumlahan semua sisi) pada bangun datar yang familiar.. Bukti: Bagaimana cara menghitung keliling bangun datar berikut?; (2 × 5) + (2 × 3) = 16 cm
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip keliling sebagai jumlah panjang sisi-sisi bangun datar dan menerapkan prosedur perhitungan yang sesuai untuk jajar genjang.. Bukti: Keliling = (2 × 5) + (2 × 3) = 16 cm
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali bangun datar, mengidentifikasi panjang sisi yang diberikan, dan memilih operasi penjumlahan atau perkalian yang benar untuk keliling. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Bagaimana cara menghitung keliling bangun datar berikut?; Pilihan C. Keliling = (2 × 5) + (2 × 3) = 16 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling bangun datar sebagai jumlah panjang sisi-sisinya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling jajar genjang dengan panjang sisi yang sudah diketahui secara eksplisit adalah tugas yang sangat mendasar dan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5130`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur rutin untuk menghitung keliling bangun datar (jajar genjang) berdasarkan panjang sisi yang sudah diketahui. Ini adalah penerapan langsung dari konsep keliling sebagai jumlah panjang sisi-sisi.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang cara menghitung keliling bangun datar dengan menggunakan rumus atau penjumlahan sisi-sisi.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi panjang sisi-sisi jajar genjang dan menerapkan rumus keliling dasar. Tidak ada kendala yang berinteraksi atau langkah perencanaan yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah panjang sisi-sisi bangun datar dan sifat jajar genjang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling jajar genjang dengan panjang sisi yang sudah tertera secara eksplisit adalah tugas yang sangat mendasar dan familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 155/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000080; applying=0.999920; reasoning=0.000000 | applying | 0.999920 | 0.000758 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.045716; conceptual=0.943575; procedural=0.010709; metacognitive=0.000000 | conceptual | 0.943575 | 0.176321 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.745934; Medium=0.250234; Hard=0.003833 | Easy | 0.745934 | 0.533980 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999920; −Σp ln(p) = 0.000833; H = 0.000833/ln(3) = 0.000758; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.943575; −Σp ln(p) = 0.244433; H = 0.244433/ln(4) = 0.176321; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.745934; −Σp ln(p) = 0.586637; H = 0.586637/ln(3) = 0.533980; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Segi Empat
Tipe soal: multiple_choice
Stimulus: -
Soal: Bagaimana cara menghitung keliling bangun datar berikut?
Pilihan: A. Keliling = 5 × 3 = 15 cm
B. Keliling = 5 + 3 = 8 cm
C. Keliling = (2 × 5) + (2 × 3) = 16 cm
D. Keliling = 4 × 5 = 20 cm
Transkripsi visual: Gambar a menampilkan jajar genjang dengan panjang sisi sejajar 5 cm dan 3 cm. Gambar b menampilkan layang-layang dengan label sisi 2 cm dan 4 cm, disertai pertanyaan 'Apakah ada sisi-sisi yang sama panjang?'. Soal utama merujuk pada cara menghitung keliling bangun datar (jajar genjang pada gambar a).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `f1bf25d82612cb22f80e24e7`

Apakah nama bangun datar berikut?

| Opsi | Isi |
|---|---|
| A | Belah ketupat |
| B | Layang-layang |
| C | Jajargenjang |
| D | Trapesium |

![Gambar sumber soal 32](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0135-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bangun pada gambar b memiliki dua pasang sisi yang berdekatan sama panjang (CD=CB=2 cm dan AD=AB=4 cm). Sifat ini adalah definisi dari layang-layang.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0135-05.png. Transkripsi visual: Gambar b menunjukkan bangun datar dengan empat sisi. Sisi CD dan CB memiliki tanda garis ganda (sama panjang, 2 cm). Sisi AD dan AB memiliki tanda garis tunggal (sama panjang, 4 cm). Bangun ini memiliki dua pasang sisi berdekatan yang sama panjang.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f303e5de887e56bc0274111dd76cb187866e9350c3ad8b57ceef19ba38b1c605`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3456 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3491 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3488 |

Run 1 — solusi: Bangun pada gambar b memiliki dua pasang sisi yang berdekatan sama panjang (CD=CB=2 cm dan AD=AB=4 cm). Sifat ini adalah definisi dari layang-layang.
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi bangun datar berdasarkan sifat geometris yang diberikan (dua pasang sisi berdekatan sama panjang). Ini adalah proses mengenali dan mengklasifikasikan objek berdasarkan definisi yang sudah dipelajari.. Bukti: Apakah nama bangun datar berikut?; dua pasang sisi yang berdekatan sama panjang
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap definisi dan sifat-sifat dasar (konsep) dari bangun datar segi empat.. Bukti: Apakah nama bangun datar berikut?; dua pasang sisi yang berdekatan sama panjang
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mencocokkan properti visual yang diberikan (dua pasang sisi sama panjang) dengan definisi layang-layang yang sudah dipelajari di kelas 5. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: Apakah nama bangun datar berikut?; dua pasang sisi yang berdekatan sama panjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sifat-sifat bangun datar segi empat (layang-layang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi bangun datar berdasarkan sifat sisinya adalah materi standar kelas 5. Soal ini tidak menuntut analisis mendalam, hanya pengenalan bentuk. |

Run 2 — solusi: Bangun (b) memiliki dua pasang sisi yang berdekatan sama panjang, yaitu pasangan sisi atas (2 cm) dan pasangan sisi bawah (4 cm). Sifat ini merupakan definisi dari layang-layang.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali bangun datar berdasarkan properti geometris yang diberikan (panjang sisi dan tanda kesamaan sisi). Ini adalah tugas pengenalan sifat dasar bangun datar.. Bukti: Apakah nama bangun datar berikut?; dua pasang sisi yang berdekatan sama panjang (2 cm dan 4 cm), jadi layang-layang
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan sifat-sifat bangun datar (layang-layang) untuk mengklasifikasikan gambar tersebut.. Bukti: dua pasang sisi yang berdekatan sama panjang (2 cm dan 4 cm), jadi layang-layang
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi ciri khas layang-layang yang sudah terlihat jelas pada gambar (dua pasang sisi berdekatan sama panjang). Tidak ada langkah perencanaan atau integrasi yang rumit.. Bukti: Apakah nama bangun datar berikut?; dua pasang sisi yang berdekatan sama panjang (2 cm dan 4 cm)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang sifat-sifat bangun datar segi empat (layang-layang, jajargenjang, dll). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenali bangun datar berdasarkan sifat sisinya adalah materi standar kelas 5. Soal tidak menuntut perhitungan atau analisis mendalam. |

Run 3 — solusi: Bangun pada gambar b memiliki dua pasang sisi yang berdekatan sama panjang (2 cm dan 4 cm), yang merupakan ciri khas bangun layang-layang.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nama bangun datar berdasarkan properti sisi yang diberikan pada gambar. Ini adalah tugas pengenalan sifat bangun datar yang langsung.. Bukti: Apakah nama bangun datar berikut?; Gambar b menunjukkan bangun datar dengan empat sisi. Sisi CD dan CB memiliki tanda garis ganda yang menunjukkan panjang sama (2 cm). Sisi AD dan AB memiliki tanda garis tunggal yang menunjukkan panjang sama (4 cm).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap definisi dan sifat-sifat geometris dari bangun datar (layang-layang).. Bukti: Apakah nama bangun datar berikut?; dua pasang sisi yang berdekatan sama panjang
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali properti yang sudah divisualisasikan secara eksplisit pada gambar (dua pasang sisi berdekatan sama panjang) dan mencocokkannya dengan nama bangun yang sudah dipelajari.. Bukti: Apakah nama bangun datar berikut?; Gambar b menunjukkan bangun datar dengan empat sisi. Sisi CD dan CB memiliki tanda garis ganda yang menunjukkan panjang sama (2 cm). Sisi AD dan AB memiliki tanda garis tunggal yang menunjukkan panjang sama (4 cm).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sifat-sifat bangun datar segi empat (layang-layang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah mengenal sifat-sifat bangun datar sederhana. Soal ini tidak memerlukan perhitungan kompleks atau penalaran bertingkat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 111/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001020; applying=0.998980; reasoning=0.000000 | applying | 0.998980 | 0.007324 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.384055; conceptual=0.605361; procedural=0.010584; metacognitive=0.000000 | conceptual | 0.605361 | 0.519022 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.865004; Medium=0.132446; Hard=0.002550 | Easy | 0.865004 | 0.371762 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998980; −Σp ln(p) = 0.008046; H = 0.008046/ln(3) = 0.007324; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.605361; −Σp ln(p) = 0.719517; H = 0.719517/ln(4) = 0.519022; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.865004; −Σp ln(p) = 0.408423; H = 0.408423/ln(3) = 0.371762; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Segi Empat
Tipe soal: multiple_choice
Stimulus: -
Soal: Apakah nama bangun datar berikut?
Pilihan: A. Belah ketupat
B. Layang-layang
C. Jajargenjang
D. Trapesium
Transkripsi visual: Gambar b menunjukkan bangun datar dengan empat sisi. Sisi CD dan CB memiliki tanda garis ganda (sama panjang, 2 cm). Sisi AD dan AB memiliki tanda garis tunggal (sama panjang, 4 cm). Bangun ini memiliki dua pasang sisi berdekatan yang sama panjang.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `6a24acac84ee1e57911309bc`

Bagaimana cara mencari keliling bangun tersebut?

| Opsi | Isi |
|---|---|
| A | Keliling = 4 × 3 = 12 cm |
| B | Keliling = 6 × 3 = 18 cm |
| C | Keliling = 5 × 3 = 15 cm |
| D | Keliling = 3 × 3 = 9 cm |

![Gambar sumber soal 33](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0138-06.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bangun tersebut adalah segi lima beraturan dengan 5 sisi yang sama panjang, masing-masing 3 cm. Keliling adalah jumlah panjang seluruh sisi, yaitu 5 x 3 cm = 15 cm.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0138-06.png. Transkripsi visual: Gambar menunjukkan sebuah bangun datar segi lima beraturan. Setiap sisi bangun tersebut diberi label panjang '3 cm'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe65a03ddb67fb541e32001c9de766de0b106e383bcc52e15e2fbe2ff0cc059d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3426 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3413 |
| 3 | success | valid / verified | applying | procedural | Easy | 3444 |

Run 1 — solusi: Bangun tersebut adalah segi lima beraturan dengan panjang setiap sisi 3 cm. Keliling adalah jumlah panjang seluruh sisi, yaitu 5 sisi × 3 cm/sisi = 15 cm.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi konsep keliling pada bangun datar sederhana (segi lima) dan menerapkan prosedur penjumlahan berulang atau perkalian sederhana. Ini adalah penerapan langsung dari konsep keliling pada konteks rutin.. Bukti: Bagaimana cara mencari keliling bangun tersebut?; segi lima beraturan punya 5 sisi 3 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung keliling poligon dengan menjumlahkan panjang sisi-sisinya atau menggunakan perkalian untuk poligon beraturan.. Bukti: Keliling = 5 × 3 = 15 cm
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu mengenali bangun sebagai segi lima dan melakukan satu operasi perkalian sederhana (5x3). Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: Bagaimana cara mencari keliling bangun tersebut?; segi lima beraturan punya 5 sisi 3 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling sebagai jumlah panjang sisi-sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling bangun datar sederhana dengan panjang sisi yang sudah diketahui adalah tugas rutin yang sangat mendasar. |

Run 2 — solusi: Bangun tersebut adalah segi lima beraturan dengan panjang setiap sisi 3 cm. Keliling adalah jumlah panjang seluruh sisinya, yaitu 5 sisi × 3 cm = 15 cm.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi prosedur dasar menghitung keliling bangun datar dengan menjumlahkan panjang sisi-sisinya. Ini adalah penerapan langsung dari definisi keliling.. Bukti: Bagaimana cara mencari keliling bangun tersebut?; segi lima beraturan punya 5 sisi 3 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung keliling poligon dengan menjumlahkan panjang sisi-sisinya.. Bukti: Keliling = 5 × 3 = 15 cm
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu mengenali bentuk sebagai segi lima dan melakukan perkalian sederhana (5 x 3). Tidak ada langkah kompleks atau kendala yang harus dipecahkan.. Bukti: Bagaimana cara mencari keliling bangun tersebut?; segi lima beraturan punya 5 sisi 3 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep keliling sebagai jumlah panjang sisi-sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling bangun datar sederhana adalah materi dasar yang rutin dan tidak memerlukan perencanaan tinggi. |

Run 3 — solusi: Bangun tersebut adalah segi lima beraturan dengan panjang setiap sisi 3 cm. Keliling = jumlah panjang semua sisi = 5 x 3 cm = 15 cm.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi jumlah sisi pada bangun datar yang diberikan dan menerapkan prosedur dasar keliling (penjumlahan sisi atau perkalian sisi dengan banyaknya sisi). Ini adalah penerapan langsung dari konsep keliling pada konteks rutin.. Bukti: Bagaimana cara mencari keliling bangun tersebut?; segi lima beraturan punya 5 sisi 3 cm
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami prosedur menghitung keliling bangun datar (konsep) dan menerapkan algoritma perkalian atau penjumlahan berulang (prosedural) untuk mendapatkan hasil.. Bukti: Keliling = 5 × 3 = 15 cm
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menghitung jumlah sisi (5) dan mengalikannya dengan panjang sisi (3 cm). Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Bagaimana cara mencari keliling bangun tersebut?; segi lima beraturan punya 5 sisi 3 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling sebagai jumlah panjang sisi dan kemampuan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling bangun datar sederhana adalah materi dasar yang rutin. Soal tidak menuntut perencanaan atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4849`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi bangun datar sebagai segi lima (memiliki 5 sisi) dan menerapkan prosedur keliling (penjumlahan sisi atau perkalian sisi dengan banyaknya sisi). Ini adalah penerapan konsep keliling pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung keliling poligon dengan menggunakan algoritma perkalian sederhana.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu mengenali jumlah sisi pada bangun (5) dan mengalikannya dengan panjang sisi (3 cm). Tidak ada langkah yang saling bergantung atau kendala yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling sebagai jumlah panjang sisi-sisi bangun datar dan kemampuan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling bangun datar sederhana dengan panjang sisi yang sudah diketahui adalah tugas rutin yang sangat mendasar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 102/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.094908; applying=0.905092; reasoning=0.000000 | applying | 0.905092 | 0.285587 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.715233; conceptual=0.253411; procedural=0.031356; metacognitive=0.000000 | factual | 0.715233 | 0.502160 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.905245; Medium=0.091701; Hard=0.003053 | Easy | 0.905245 | 0.297553 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.905092; −Σp ln(p) = 0.313749; H = 0.313749/ln(3) = 0.285587; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.715233; −Σp ln(p) = 0.696141; H = 0.696141/ln(4) = 0.502160; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.905245; −Σp ln(p) = 0.326895; H = 0.326895/ln(3) = 0.297553; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Segi Banyak
Tipe soal: multiple_choice
Stimulus: -
Soal: Bagaimana cara mencari keliling bangun tersebut?
Pilihan: A. Keliling = 4 × 3 = 12 cm
B. Keliling = 6 × 3 = 18 cm
C. Keliling = 5 × 3 = 15 cm
D. Keliling = 3 × 3 = 9 cm
Transkripsi visual: Gambar menunjukkan sebuah bangun datar segi lima beraturan. Setiap sisi bangun tersebut diberi label panjang '3 cm'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `15decc9f68f755794c576412`

Tentukan keliling bangun berikut.

| Opsi | Isi |
|---|---|
| A | 80 cm |
| B | 60 cm |
| C | 100 cm |
| D | 40 cm |

![Gambar sumber soal 34](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0146-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Mengasumsikan soal merujuk pada bangun nomor 3 (segi delapan beraturan). Keliling = 8 × panjang sisi = 8 × 10 cm = 80 cm.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0146-03.png. Transkripsi visual: Gambar menampilkan lima bangun datar bernomor 1 sampai 5. Bangun 1 adalah segitiga sama sisi dengan satu sisi 8 cm. Bangun 2 adalah layang-layang dengan sisi 4 cm dan 6 cm. Bangun 3 adalah segi delapan beraturan dengan satu sisi 10 cm. Bangun 4 adalah bangun datar tidak beraturan dengan sisi 12 cm, 12 cm, 20 cm, dan 16 cm. Bangun 5 adalah bangun datar berbentuk L dengan beberapa ukuran sisi.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8061c77387d5d144472c46eee2a17d3d6ead0778cc6146f11865135222b7cd6f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3485 |
| 2 | success | valid / unverifiable | applying | conceptual | Easy | 3410 |
| 3 | success | concern / verified | knowing | procedural | Easy | 3485 |

Run 1 — solusi: Bangun nomor 3 adalah segi delapan beraturan dengan panjang sisi 10 cm. Keliling = 8 × 10 cm = 80 cm.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerapkan rumus keliling bangun datar (segi delapan beraturan) yang merupakan prosedur rutin dan langsung.. Bukti: Tentukan keliling bangun berikut.; segi delapan beraturan dengan sisi 10 cm
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep keliling sebagai jumlah panjang sisi-sisi bangun datar dan menerapkan prosedur perkalian untuk bangun beraturan.. Bukti: segi delapan beraturan; keliling = 8 × 10 = 80 cm
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengidentifikasi jumlah sisi pada bangun segi delapan dan mengalikannya dengan panjang sisi yang sudah diketahui. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: Tentukan keliling bangun berikut.; segi delapan beraturan dengan sisi 10 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah sisi dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling bangun beraturan adalah materi dasar yang rutin dan langsung. |

Run 2 — solusi: Soal ambigu karena tidak menentukan bangun mana yang dimaksud. Jika merujuk pada bangun nomor 3 (segi delapan beraturan), kelilingnya adalah 8 sisi x 10 cm = 80 cm.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur menghitung keliling bangun datar (segi delapan beraturan) yang merupakan prosedur rutin.. Bukti: Tentukan keliling bangun berikut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep keliling sebagai jumlah panjang sisi-sisi bangun datar.. Bukti: Tentukan keliling bangun berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin jika bangun yang dimaksud jelas. Mengingat ambiguitas soal, tingkat kesulitan sulit ditentukan secara objektif, namun secara prosedural ini adalah tugas standar kelas 5.. Bukti: Tentukan keliling bangun berikut.; segi delapan beraturan dengan panjang sisi 10 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah panjang sisi dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung keliling bangun beraturan adalah materi dasar kelas 5. Soal ini hanya memerlukan satu operasi perkalian sederhana. |

Run 3 — solusi: Bangun nomor 3 adalah segi delapan beraturan. Keliling = 8 × panjang sisi = 8 × 10 cm = 80 cm.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali bangun sebagai segi delapan beraturan dan menerapkan rumus keliling (jumlah seluruh sisi atau 8 kali panjang sisi). Ini adalah prosedur langsung.. Bukti: Tentukan keliling bangun berikut.; segi delapan beraturan: keliling = 8 × 10 = 80 cm
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang cara menghitung keliling bangun datar beraturan.. Bukti: segi delapan beraturan; keliling = 8 × 10 = 80 cm
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta penerapan rumus keliling pada bangun beraturan yang sudah diketahui panjang sisinya.. Bukti: segi delapan beraturan; 10 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah panjang sisi-sisi bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa menghitung keliling bangun datar sederhana. Soal ini tidak memerlukan perencanaan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4825`.
Konten: `concern`; kunci: `verified`; masalah: Soal bersifat ambigu karena meminta 'keliling bangun berikut' tanpa spesifikasi bangun mana yang dimaksud dari lima bangun yang tersedia di gambar.; Meskipun kunci jawaban merujuk pada bangun nomor 3 (segi delapan), instruksi soal tidak eksplisit mengarahkan siswa ke bangun tersebut..
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi bangun dan menerapkan rumus keliling yang merupakan prosedur rutin.
- Dimensi pengetahuan `procedural`: Siswa menggunakan pengetahuan prosedural tentang cara menghitung keliling bangun datar beraturan.
- Intended difficulty `Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengidentifikasi jumlah sisi pada bangun segi delapan dan mengalikannya dengan panjang sisi yang sudah diketahui. Tidak ada langkah kompleks atau kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling sebagai jumlah sisi dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung keliling bangun beraturan adalah materi dasar yang rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 137/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Segi Banyak
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan keliling bangun berikut.
Pilihan: A. 80 cm
B. 60 cm
C. 100 cm
D. 40 cm
Transkripsi visual: Gambar menampilkan lima bangun datar bernomor 1 sampai 5. Bangun 1 adalah segitiga sama sisi dengan satu sisi 8 cm. Bangun 2 adalah layang-layang dengan sisi 4 cm dan 6 cm. Bangun 3 adalah segi delapan beraturan dengan satu sisi 10 cm. Bangun 4 adalah bangun datar tidak beraturan dengan sisi 12 cm, 12 cm, 20 cm, dan 16 cm. Bangun 5 adalah bangun datar berbentuk L dengan beberapa ukuran sisi.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal bersifat ambigu karena meminta 'keliling bangun berikut' tanpa spesifikasi bangun mana yang dimaksud dari lima bangun yang tersedia di gambar.; Meskipun kunci jawaban merujuk pada bangun nomor 3 (segi delapan), instruksi soal tidak eksplisit mengarahkan siswa ke bangun tersebut..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `4b98e16cdb2f561fb46c8068`

Tentukan keliling bangun berikut.

| Opsi | Isi |
|---|---|
| A | 72 cm |
| B | 56 cm |
| C | 88 cm |
| D | 60 cm |

![Gambar sumber soal 35](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0146-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Keliling adalah jumlah seluruh sisi luar bangun. Sisi-sisinya adalah 12 cm, 16 cm, 12 cm, 12 cm, dan 20 cm. Keliling = 12 + 16 + 12 + 12 + 20 = 72 cm. Garis putus-putus 16 cm berada di dalam bangun, sehingga tidak dihitung dalam keliling.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0146-03.png. Transkripsi visual: Gambar 4 menunjukkan bangun datar gabungan yang terdiri dari dua bagian. Sisi-sisi luar bangun tersebut memiliki panjang: 12 cm (kiri), 16 cm (atas), 12 cm (kanan atas), 12 cm (kanan bawah), dan 20 cm (bawah). Terdapat garis putus-putus horizontal sepanjang 16 cm di bagian dalam bangun yang menghubungkan sisi kiri dengan titik pertemuan sisi kanan atas dan kanan bawah. Tanda siku-siku ada pada pertemuan garis putus-putus dengan sisi kanan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `74e0b3ae1c5a6ce679804e7ac4e6a2baf72d85a7249d283cad7fbc3116d7d463`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3629 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3740 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3682 |

Run 1 — solusi: Keliling adalah jumlah seluruh sisi luar bangun. Sisi-sisinya adalah 12 cm, 16 cm, 12 cm, 12 cm, dan 20 cm. Keliling = 12 + 16 + 12 + 12 + 20 = 72 cm. Garis putus-putus 16 cm berada di dalam bangun, sehingga tidak dihitung dalam keliling.
- Domain kognitif `classify/applying`: Siswa diminta untuk menghitung keliling bangun datar gabungan. Siswa harus mengidentifikasi sisi mana yang merupakan batas luar bangun (keliling) dan membedakannya dari garis bantu (garis putus-putus) yang ada di dalam bangun. Ini adalah penerapan konsep keliling pada konteks bangun gabungan yang rutin.. Bukti: Tentukan keliling bangun berikut.; Gambar 4 menunjukkan bangun datar gabungan
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep keliling sebagai jumlah panjang sisi-sisi luar suatu bangun datar dan menerapkan prosedur penjumlahan panjang sisi-sisi tersebut.. Bukti: Tentukan keliling bangun berikut.; Gambar 4
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan seleksi informasi (membedakan sisi luar dengan garis bantu internal) dan menjumlahkan panjang sisi-sisi tersebut. Meskipun prosedurnya rutin, terdapat sedikit tuntutan untuk mengenali struktur bangun gabungan agar tidak salah menjumlahkan garis internal.. Bukti: Gambar 4; 12 cm, 16 cm, 12 cm, 12 cm, 20 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling bangun datar dan penjumlahan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung keliling bangun datar gabungan sederhana. Kesalahan umum (seperti menjumlahkan garis internal) adalah pengecoh yang wajar untuk tingkat ini. |

Run 2 — solusi: Keliling adalah jumlah seluruh sisi terluar bangun. Berdasarkan gambar 4, sisi-sisinya adalah 12 cm, 12 cm, 12 cm, 12 cm, dan 20 cm. Total keliling = 12 + 12 + 12 + 12 + 20 = 68 cm. Kunci jawaban A (72 cm) tidak sesuai dengan perhitungan geometri dasar dari gambar yang diberikan.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi sisi-sisi terluar dari bangun gabungan dan menjumlahkannya. Ini adalah prosedur standar untuk mencari keliling bangun datar.. Bukti: Tentukan keliling bangun berikut.; Gambar 4
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep keliling sebagai jumlah panjang sisi-sisi terluar suatu bangun datar.. Bukti: Tentukan keliling bangun berikut.
- Intended difficulty `classify/Medium`: Soal ini meminta siswa menghitung keliling bangun gabungan. Meskipun ada garis putus-putus (distraktor), siswa kelas 5 yang sudah memahami konsep keliling seharusnya dapat membedakan sisi luar dan dalam. Namun, karena terdapat ketidaksesuaian antara visual dan kunci jawaban, tingkat kesulitan menjadi ambigu.. Bukti: Tentukan keliling bangun berikut.; Gambar 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling bangun datar dan penjumlahan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung keliling bangun gabungan adalah materi standar kelas 5. Kesulitan terletak pada kemampuan membedakan sisi luar dan garis bantu. |

Run 3 — solusi: Keliling adalah jumlah seluruh sisi luar bangun. Sisi-sisinya adalah 12 cm, 12 cm, 12 cm, 20 cm, dan sisi atas yang panjangnya sama dengan garis putus-putus horizontal yaitu 16 cm. Keliling = 12 + 12 + 12 + 20 + 16 = 72 cm.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi sisi-sisi luar bangun gabungan dan menjumlahkannya. Ini adalah penerapan prosedur standar menghitung keliling pada konteks bangun gabungan yang rutin.. Bukti: Tentukan keliling bangun berikut.; sisi luar 12 + 16 + 12 + 12 + 20 = 72 cm
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep keliling sebagai jumlah sisi luar dan membedakannya dengan garis bantu internal (garis putus-putus), yang merupakan pemahaman konseptual.. Bukti: Tentukan keliling bangun berikut.; garis putus-putus bukan bagian keliling
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi sisi yang tidak tertulis secara eksplisit (sisi atas 16 cm) berdasarkan informasi garis putus-putus dan membedakannya dari garis internal yang tidak dihitung. Ini memerlukan sedikit perencanaan dan pemahaman hubungan antar bagian bangun.. Bukti: Tentukan keliling bangun berikut.; sisi luar 12 + 16 + 12 + 12 + 20 = 72 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling bangun datar dan penjumlahan bilangan cacah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung keliling bangun gabungan. Kesulitan menengah muncul dari keharusan mengidentifikasi sisi yang tidak diberi label angka secara langsung (sisi atas 16 cm) dan mengabaikan garis internal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 151/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.011067; applying=0.988933; reasoning=0.000000 | applying | 0.988933 | 0.055388 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.026193; conceptual=0.969303; procedural=0.004504; metacognitive=0.000000 | conceptual | 0.969303 | 0.108169 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.784609; Medium=0.210904; Hard=0.004487 | Easy | 0.784609 | 0.494097 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.988933; −Σp ln(p) = 0.060850; H = 0.060850/ln(3) = 0.055388; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.969303; −Σp ln(p) = 0.149955; H = 0.149955/ln(4) = 0.108169; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.784609; −Σp ln(p) = 0.542821; H = 0.542821/ln(3) = 0.494097; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Bangun Gabungan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan keliling bangun berikut.
Pilihan: A. 72 cm
B. 56 cm
C. 88 cm
D. 60 cm
Transkripsi visual: Gambar 4 menunjukkan bangun datar gabungan yang terdiri dari dua bagian. Sisi-sisi luar bangun tersebut memiliki panjang: 12 cm (kiri), 16 cm (atas), 12 cm (kanan atas), 12 cm (kanan bawah), dan 20 cm (bawah). Terdapat garis putus-putus horizontal sepanjang 16 cm di bagian dalam bangun yang menghubungkan sisi kiri dengan titik pertemuan sisi kanan atas dan kanan bawah. Tanda siku-siku ada pada pertemuan garis putus-putus dengan sisi kanan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Soal tidak secara eksplisit merujuk pada gambar nomor berapa yang dimaksud, namun berdasarkan konteks pilihan jawaban (angka 12, 16, 20), soal ini merujuk pada bangun nomor 4.; Soal tidak secara eksplisit merujuk pada gambar nomor berapa yang dimaksud, namun berdasarkan konteks pilihan jawaban dan catatan ekstraksi, soal merujuk pada gambar nomor 4..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `4d698768a13668ccb860a20d`

Tentukan keliling bangun berikut.

| Opsi | Isi |
|---|---|
| A | 23 cm |
| B | 33 cm |
| C | 40 cm |
| D | 46 cm |

![Gambar sumber soal 36](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0146-03.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Keliling bangun L dapat dihitung dengan menjumlahkan semua sisi luarnya. Sisi-sisi tersebut adalah 12 cm, 8 cm, 3 cm, 3 cm, (12-3)=9 cm, dan (8+3)=11 cm. Keliling = 12 + 8 + 3 + 3 + 9 + 11 = 46 cm. Alternatif: Keliling bangun L sama dengan keliling persegi panjang dengan panjang 12 cm dan lebar (8+3) = 11 cm, yaitu 2 x (12 + 11) = 46 cm.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0146-03.png. Transkripsi visual: Gambar 5 menunjukkan bangun datar berbentuk huruf L yang tidak beraturan. Sisi-sisi yang diketahui panjangnya adalah: sisi vertikal paling kiri 12 cm, sisi horizontal paling atas 8 cm, sisi vertikal yang menjorok ke dalam 3 cm, dan sisi horizontal yang menjorok ke dalam 7 cm. Terdapat garis putus-putus merah yang membentuk persegi panjang pembungkus di sekeliling bangun tersebut, menunjukkan bahwa lebar total adalah 8 cm + 3 cm = 11 cm dan tinggi total adalah 12 cm.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `532fa76ce1263b2a686e382702d00f16bb596d8b8770fe6adea28e8b6f772a4a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3718 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3635 |
| 3 | success | valid / verified | applying | procedural | Medium | 3734 |

Run 1 — solusi: Keliling bangun dapat dihitung dengan menjumlahkan semua sisi luar. Sisi horizontal total adalah 8 + 3 = 11 cm. Sisi vertikal total adalah 12 cm. Karena ini adalah bangun L yang sisi-sisinya sejajar dengan sumbu, kelilingnya sama dengan keliling persegi panjang dengan panjang 12 cm dan lebar 11 cm, yaitu 2 x (12 + 11) = 46 cm.
- Domain kognitif `classify/applying`: Siswa diminta untuk menentukan keliling bangun datar gabungan. Ini memerlukan pemahaman konseptual tentang keliling sebagai jumlah panjang sisi-sisi luar dan kemampuan untuk mengidentifikasi atau menghitung panjang sisi yang tidak tertulis secara eksplisit dengan memanfaatkan sifat geometri bangun tersebut.. Bukti: Tentukan keliling bangun berikut.; bangun berbentuk huruf L yang tidak beraturan
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan prinsip keliling pada bangun gabungan yang memerlukan pemahaman hubungan antar sisi (konseptual) dan prosedur penjumlahan sisi-sisi tersebut.. Bukti: Tentukan keliling bangun berikut.; bangun berbentuk huruf L
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus memahami bahwa keliling bangun L ini ekuivalen dengan keliling persegi panjang yang membungkusnya. Meskipun prosedurnya familiar, siswa perlu melakukan inferensi visual atau deduksi logis untuk menyimpulkan panjang sisi yang tidak tertulis (seperti sisi horizontal bawah) atau menggunakan sifat translasi sisi untuk menyederhanakan perhitungan. Ini melibatkan lebih dari sekadar menjumlahkan angka yang ada.. Bukti: bangun berbentuk huruf L yang tidak beraturan; sisi-sisi luar bersesuaian dengan persegi panjang 12 cm x (8 + 3) cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling bangun datar dan sifat-sifat persegi panjang. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung keliling bangun gabungan. Soal ini menuntut kemampuan untuk melihat hubungan antara sisi-sisi bangun L dengan persegi panjang, yang merupakan langkah penalaran yang sesuai untuk tingkat kesulitan menengah di kelas 5. |

Run 2 — solusi: Keliling bangun L ini sama dengan keliling persegi panjang dengan panjang 12 cm dan lebar (8+3) = 11 cm. Keliling = 2 x (12 + 11) = 2 x 23 = 46 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa keliling bangun L yang tidak beraturan ini dapat dihitung dengan memproyeksikan sisi-sisinya menjadi keliling persegi panjang yang lebih besar. Ini melibatkan penerapan konsep keliling pada konteks bangun gabungan yang rutin.. Bukti: Tentukan keliling bangun berikut.; sisi-sisi luar bersesuaian dengan persegi panjang 12 cm × (8 + 3) cm
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip keliling bangun datar dan menerapkannya pada struktur bangun gabungan yang memerlukan pemahaman hubungan antar sisi.. Bukti: Tentukan keliling bangun berikut.; sisi-sisi luar bersesuaian dengan persegi panjang 12 cm × (8 + 3) cm
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus memahami bahwa sisi-sisi yang tidak diketahui dapat diproyeksikan ke sisi luar untuk membentuk persegi panjang. Meskipun prosedurnya familiar, siswa perlu melakukan langkah integrasi visual untuk menentukan lebar total (8+3) sebelum menghitung keliling.. Bukti: Tentukan keliling bangun berikut.; sisi-sisi luar bersesuaian dengan persegi panjang 12 cm × (8 + 3) cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar keliling bangun datar dan penjumlahan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu memahami konsep keliling dan melakukan manipulasi visual sederhana pada bangun datar gabungan. |

Run 3 — solusi: Keliling bangun dapat dihitung dengan menjumlahkan semua sisi luar. Sisi vertikal kiri = 12 cm. Sisi horizontal atas = 8 cm. Sisi vertikal lekukan = 3 cm. Sisi horizontal lekukan = 3 cm. Sisi vertikal kanan = 12 - 3 = 9 cm. Sisi horizontal bawah = 8 + 3 = 11 cm. Keliling = 12 + 8 + 3 + 3 + 9 + 11 = 46 cm. Alternatif: Keliling bangun L ini sama dengan keliling persegi panjang dengan panjang 12 cm dan lebar (8+3) = 11 cm, yaitu 2 x (12 + 11) = 46 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep keliling pada bangun datar gabungan yang tidak beraturan. Mereka harus memahami bahwa keliling adalah jumlah seluruh sisi luar dan mampu mengidentifikasi atau menghitung panjang sisi yang tidak tertulis secara eksplisit (seperti sisi vertikal kanan dan horizontal bawah) berdasarkan hubungan geometris dengan sisi lainnya.. Bukti: Tentukan keliling bangun berikut.; Gambar 5 menunjukkan bangun datar berbentuk huruf L
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip keliling (konseptual) dan menerapkan prosedur penjumlahan sisi atau metode transformasi keliling bangun (prosedural) untuk menyelesaikan masalah.. Bukti: Tentukan keliling bangun berikut.; Gambar 5
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan penalaran untuk menentukan panjang sisi yang tidak diketahui (sisi vertikal kanan dan horizontal bawah) atau memahami prinsip transformasi keliling bangun L ke persegi panjang. Ini melibatkan lebih dari satu langkah logis dan integrasi informasi visual, namun prosedurnya familiar bagi siswa kelas 5.. Bukti: Gambar 5 menunjukkan bangun datar berbentuk huruf L; 12 cm; 8 cm; 3 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling bangun datar dan operasi penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung keliling bangun datar. Menghitung keliling bangun gabungan dengan sisi yang tidak tertulis memerlukan perencanaan langkah tambahan, yang sesuai dengan tingkat kesulitan menengah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5496`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep keliling pada bangun gabungan. Siswa perlu mengidentifikasi hubungan antar sisi atau melakukan transformasi visual untuk menentukan panjang sisi yang tidak tertulis secara eksplisit, yang merupakan penerapan konsep dalam konteks rutin.
- Dimensi pengetahuan `conceptual`: Siswa menggunakan prinsip keliling (konseptual) dan menerapkan prosedur penjumlahan sisi atau metode transformasi keliling bangun (prosedural) untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan penalaran untuk menentukan panjang sisi yang tidak diketahui atau memahami prinsip transformasi keliling bangun L ke persegi panjang. Ini melibatkan lebih dari satu langkah logis dan integrasi informasi visual, namun prosedurnya familiar bagi siswa kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling bangun datar dan operasi penjumlahan bilangan cacah. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung keliling bangun datar. Menghitung keliling bangun gabungan dengan sisi yang tidak tertulis memerlukan perencanaan langkah tambahan, yang sesuai dengan tingkat kesulitan menengah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 146/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.582258; applying=0.417742; reasoning=0.000000 | knowing | 0.582258 | 0.618555 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.180004; conceptual=0.810262; procedural=0.009734; metacognitive=0.000000 | conceptual | 0.810262 | 0.378154 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.841015; Medium=0.155339; Hard=0.003646 | Easy | 0.841015 | 0.414480 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.582258; −Σp ln(p) = 0.679553; H = 0.679553/ln(3) = 0.618555; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.810262; −Σp ln(p) = 0.524233; H = 0.524233/ln(4) = 0.378154; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.841015; −Σp ln(p) = 0.455353; H = 0.455353/ln(3) = 0.414480; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Keliling Bangun Gabungan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan keliling bangun berikut.
Pilihan: A. 23 cm
B. 33 cm
C. 40 cm
D. 46 cm
Transkripsi visual: Gambar 5 menunjukkan bangun datar berbentuk huruf L yang tidak beraturan. Sisi-sisi yang diketahui panjangnya adalah: sisi vertikal paling kiri 12 cm, sisi horizontal paling atas 8 cm, sisi vertikal yang menjorok ke dalam 3 cm, dan sisi horizontal yang menjorok ke dalam 7 cm. Terdapat garis putus-putus merah yang membentuk persegi panjang pembungkus di sekeliling bangun tersebut, menunjukkan bahwa lebar total adalah 8 cm + 3 cm = 11 cm dan tinggi total adalah 12 cm.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `8fe432cf4c0a120aab6def21`

\|**No**\|**Nama Bangun Datar**\|**Gambar**\|**Banyaknya**\|<br>\|---\|---\|---\|---\|<br>\|1<br>2\|Segitiga<br>...\|...\|...<br>...\|<br><br>Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :

| Opsi | Isi |
|---|---|
| A | Segitiga 5, trapesium 1, persegi 1 |
| B | Segitiga 5, jajargenjang 1, persegi 1 |
| C | Segitiga 4, jajargenjang 1, persegi 1 |
| D | Segitiga 6, persegi 1 |

![Gambar sumber soal 37](<../../../images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Mengidentifikasi kepingan tangram pada gambar: terdapat 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Pilihan B sesuai dengan jumlah dan jenis bangun datar tersebut.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png. Transkripsi visual: Gambar menunjukkan sebuah perahu yang tersusun dari 7 keping tangram. Keping-keping tersebut terdiri dari: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua sedang, 1 persegi hijau muda, 1 segitiga oranye kecil, 1 jajargenjang kuning, dan 1 segitiga merah muda. Total keping: 5 segitiga (berbagai ukuran), 1 persegi, 1 jajargenjang.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aeeff929c552f8b52d561eec6b8507f71f4111b68bf42c8694e318412a9351e4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3630 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3557 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3558 |

Run 1 — solusi: Mengidentifikasi kepingan tangram pada gambar: terdapat 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Pilihan B sesuai dengan jumlah dan jenis bangun datar tersebut.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (dekomposisi) dari gambar yang diberikan. Ini adalah tugas mengenali dan mengklasifikasikan bentuk geometri dasar, yang termasuk dalam domain knowing.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut; Pilihan B. Segitiga 5, jajargenjang 1, persegi 1
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang sifat-sifat bangun datar (segitiga, persegi, jajargenjang) dan kemampuan mengenali bentuk-bentuk tersebut dalam komposisi yang lebih kompleks.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah kepingan berdasarkan bentuknya. Tidak ada langkah perencanaan yang rumit atau integrasi konsep yang mendalam. Tugas ini rutin bagi siswa kelas 5 yang sudah mengenal bentuk geometri dasar.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi bentuk dasar dari tangram adalah materi yang sangat familiar dan sesuai untuk kelas 5, dengan beban kognitif yang rendah. |

Run 2 — solusi: Mengidentifikasi kepingan tangram pada gambar: terdapat 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Totalnya adalah 5 segitiga, 1 persegi, dan 1 jajargenjang.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (dekomposisi) dari sebuah gambar yang sudah diberikan. Ini adalah tugas mengenali dan mengklasifikasikan bentuk geometri dasar, yang termasuk dalam domain knowing.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang sifat-sifat bangun datar (segitiga, persegi, jajargenjang) dan kemampuan mengenali bentuk-bentuk tersebut dalam komposisi yang lebih kompleks.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengamati gambar dan menghitung jumlah masing-masing bentuk geometri yang sudah dikenal. Tidak ada langkah perhitungan rumit atau perencanaan strategi yang diperlukan.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar geometri (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi bentuk geometri dasar dalam tangram adalah tugas yang rutin dan sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Mengidentifikasi kepingan pada gambar: terdapat 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Pilihan yang sesuai adalah B.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (dekomposisi) dari gambar yang diberikan. Ini adalah tugas pengenalan bentuk dasar yang langsung.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu mengenali sifat-sifat geometris dari bentuk-bentuk dasar (segitiga, persegi, jajargenjang) untuk mengklasifikasikannya dengan benar.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah kepingan berdasarkan bentuknya. Tidak ada langkah rumit atau integrasi konsep yang berat.. Bukti: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi bentuk dasar adalah materi standar kelas 5. Soal tidak menuntut analisis kompleks, hanya observasi visual langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 246/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.004027; applying=0.995973; reasoning=0.000000 | applying | 0.995973 | 0.023870 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.014475; conceptual=0.965944; procedural=0.019581; metacognitive=0.000000 | conceptual | 0.965944 | 0.123921 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.660569; Medium=0.326719; Hard=0.012712 | Easy | 0.660569 | 0.632511 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.995973; −Σp ln(p) = 0.026224; H = 0.026224/ln(3) = 0.023870; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.965944; −Σp ln(p) = 0.171792; H = 0.171792/ln(4) = 0.123921; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.660569; −Σp ln(p) = 0.694884; H = 0.694884/ln(3) = 0.632511; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Komposisi dan Dekomposisi Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: |**No**|**Nama Bangun Datar**|**Gambar**|**Banyaknya**|
|---|---|---|---|
|1<br>2|Segitiga<br>...|...|...<br>...|

Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :
Pilihan: A. Segitiga 5, trapesium 1, persegi 1
B. Segitiga 5, jajargenjang 1, persegi 1
C. Segitiga 4, jajargenjang 1, persegi 1
D. Segitiga 6, persegi 1
Transkripsi visual: Gambar menunjukkan sebuah perahu yang tersusun dari 7 keping tangram. Keping-keping tersebut terdiri dari: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua sedang, 1 persegi hijau muda, 1 segitiga oranye kecil, 1 jajargenjang kuning, dan 1 segitiga merah muda. Total keping: 5 segitiga (berbagai ukuran), 1 persegi, 1 jajargenjang.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `b1d67520342a7317015c9a90`

Perhatikan bangun-bangun datar berikut.<br><br>Hitunglah luas daerah bangun-bangun datar tersebut.

| Opsi | Isi |
|---|---|
| A | 5 satuan luas |
| B | 18 satuan luas |
| C | 12 satuan luas |
| D | 9 satuan luas |

![Gambar sumber soal 38](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0158-07.png>)


Kunci sumber: `D`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal tidak dapat diselesaikan karena instruksi ambigu. Kunci D (9) hanya sesuai untuk luas bangun E (segitiga dengan alas 6 dan tinggi 3), namun soal tidak meminta luas bangun E secara spesifik.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0158-07.png. Transkripsi visual: Terdapat 7 bangun datar pada kertas berpetak: A (persegi 3x3), B (persegi panjang 2x6), C (persegi panjang 3x5), D (bangun L), E (segitiga siku-siku alas 6 tinggi 3), F (jajar genjang), G (bangun tidak beraturan). Soal meminta menghitung luas bangun-bangun tersebut, namun hanya ada satu jawaban (9) yang sesuai dengan luas bangun E (1/2 x 6 x 3 = 9).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3af3fd8d62b169ae95b47d7dad530dc6bd74fa9f43c3aabcddb0329371a61e3d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | applying | conceptual | Medium | 3580 |
| 2 | success | concern / unverifiable | — | — | — | 3250 |
| 3 | success | concern / conflict | — | — | — | 3265 |

Run 1 — solusi: Soal tidak dapat diselesaikan karena instruksi tidak spesifik bangun mana yang dimaksud. Jika diasumsikan bangun E (segitiga dengan alas 6 dan tinggi 3), luasnya adalah 0.5 * 6 * 3 = 9 satuan luas. Namun, soal tidak menyebutkan bangun E.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep luas pada bangun datar yang diberikan. Jika instruksi jelas, ini adalah aktivitas applying karena menggunakan rumus atau membilang satuan luas pada konteks rutin.. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep luas (konseptual) dan menerapkan prosedur perhitungan atau pembilangan (prosedural).. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.
- Intended difficulty `classify/Medium`: Meskipun soal memiliki masalah konten (ambiguitas), jika diasumsikan siswa diminta menghitung luas salah satu bangun (misal segitiga E), prosedurnya adalah rutin (menggunakan rumus atau menghitung kotak).. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas sebagai jumlah satuan luas atau penggunaan rumus luas bangun datar sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung luas pada kertas berpetak adalah materi standar kelas 5. Kesulitan utama terletak pada ambiguitas instruksi, bukan pada kompleksitas matematisnya. |

Run 2 — solusi: Soal tidak dapat diselesaikan karena instruksi ambigu. Jika diasumsikan yang dimaksud adalah bangun E (segitiga), luasnya adalah 1/2 x alas x tinggi = 1/2 x 6 x 3 = 9 satuan luas.
- Domain kognitif `abstain/None`: Soal tidak memiliki instruksi yang jelas mengenai bangun mana yang harus dihitung luasnya di antara tujuh bangun yang tersedia. Ambiguitas ini membuat klasifikasi domain kognitif tidak mungkin dilakukan secara valid.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Karena soal tidak spesifik dan instruksinya ambigu, tidak mungkin menentukan dimensi pengetahuan yang diuji.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak dapat dinilai tingkat kesulitannya karena instruksi yang diberikan tidak lengkap atau ambigu (tidak jelas bangun mana yang dimaksud).. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 3 — solusi: Soal tidak dapat diselesaikan karena instruksi tidak spesifik mengenai bangun mana yang harus dihitung luasnya dari tujuh bangun yang tersedia.
- Domain kognitif `abstain/None`: Soal tidak memiliki instruksi yang jelas mengenai bangun mana yang harus dihitung luasnya, sehingga tidak mungkin menentukan domain kognitif yang diperlukan untuk menyelesaikan masalah ini.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Karena soal tidak dapat diidentifikasi sebagai masalah yang valid (ambigu), dimensi pengetahuan tidak dapat diklasifikasikan.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak dapat diklasifikasikan tingkat kesulitannya karena instruksi yang ambigu membuat masalah tidak dapat diselesaikan.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1} | no_consensus / abstained | — |
| Dimensi pengetahuan | {"conceptual": 1} | no_consensus / abstained | — |
| Intended difficulty | {"Medium": 1} | no_consensus / abstained | — |

Adjudikasi AI: `success`; token `5389`.
Konten: `concern`; kunci: `conflict`; masalah: Soal meminta menghitung luas 'bangun-bangun datar tersebut' (jamak), namun hanya menyediakan satu jawaban yang hanya cocok untuk satu bangun (E).; Tidak ada instruksi spesifik bangun mana yang dimaksud, sehingga soal tidak dapat diselesaikan secara valid..
- Domain kognitif `None`: Soal tidak memiliki instruksi yang jelas mengenai bangun mana yang harus dihitung luasnya, sehingga tidak mungkin menentukan domain kognitif yang diperlukan untuk menyelesaikan masalah ini.
- Dimensi pengetahuan `None`: Karena soal tidak spesifik dan instruksinya ambigu, tidak mungkin menentukan dimensi pengetahuan yang diuji.
- Intended difficulty `None`: Soal tidak dapat dinilai tingkat kesulitannya karena instruksi yang diberikan tidak lengkap atau ambigu (tidak jelas bangun mana yang dimaksud).

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 176/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Konsep Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bangun-bangun datar berikut.

Hitunglah luas daerah bangun-bangun datar tersebut.
Pilihan: A. 5 satuan luas
B. 18 satuan luas
C. 12 satuan luas
D. 9 satuan luas
Transkripsi visual: Terdapat 7 bangun datar pada kertas berpetak: A (persegi 3x3), B (persegi panjang 2x6), C (persegi panjang 3x5), D (bangun L), E (segitiga siku-siku alas 6 tinggi 3), F (jajar genjang), G (bangun tidak beraturan). Soal meminta menghitung luas bangun-bangun tersebut, namun hanya ada satu jawaban (9) yang sesuai dengan luas bangun E (1/2 x 6 x 3 = 9).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal meminta menghitung luas 'bangun-bangun datar tersebut' (jamak), namun hanya menyediakan satu jawaban yang hanya cocok untuk satu bangun (E).; Tidak ada instruksi spesifik bangun mana yang dimaksud, sehingga soal tidak dapat diselesaikan secara valid..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `d7e4c01422c15450739e2b0a`

Perhatikan bangun-bangun datar berikut.<br><br>Hitunglah luas daerah bangun-bangun datar tersebut.

| Opsi | Isi |
|---|---|
| A | 24 satuan luas |
| B | 12 satuan luas |
| C | 16 satuan luas |
| D | 4 satuan luas |

![Gambar sumber soal 39](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0158-07.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bangun D terdiri dari dua bagian persegi panjang: bagian atas berukuran 2x2 (4 satuan) dan bagian bawah berukuran 6x2 (12 satuan). Total luas = 4 + 12 = 16 satuan luas.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0158-07.png. Transkripsi visual: Terdapat 7 bangun datar pada kertas berpetak yang diberi label A sampai G. Bangun D adalah bangun komposit berbentuk huruf L terbalik. Bagian atas bangun D memiliki lebar 2 kotak dan tinggi 2 kotak (luas 4 satuan). Bagian bawah bangun D memiliki lebar 6 kotak dan tinggi 2 kotak (luas 12 satuan). Total luas bangun D adalah 4 + 12 = 16 satuan luas.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d12e1a9e9c44752cb49bec72c6cdc2f21b8cded9d5d0e0f3fa25a5c71c84d0b4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | — | — | — | 3234 |
| 2 | success | concern / unverifiable | applying | procedural | Easy | 3526 |
| 3 | success | concern / conflict | applying | procedural | Easy | 3541 |

Run 1 — solusi: Soal tidak dapat diselesaikan karena instruksi tidak spesifik menunjuk bangun mana yang harus dihitung luasnya di antara 7 bangun yang ada.
- Domain kognitif `abstain/None`: Soal tidak memiliki instruksi yang jelas mengenai bangun mana yang harus dihitung luasnya. Tanpa kejelasan ini, tidak mungkin menentukan domain kognitif yang diperlukan untuk menjawab soal.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Karena soal ambigu dan tidak dapat diselesaikan, dimensi pengetahuan tidak dapat ditentukan.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak dapat diklasifikasikan tingkat kesulitannya karena instruksi soal tidak lengkap dan ambigu.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 2 — solusi: Soal ambigu karena tidak menentukan bangun mana yang harus dihitung luasnya. Jika diasumsikan merujuk pada bangun D, luasnya adalah (2x2) + (6x2) = 4 + 12 = 16 satuan luas.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur menghitung luas bangun datar komposit pada kertas berpetak. Ini adalah penerapan konsep luas yang rutin.. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode penjumlahan luas bagian-bagian bangun (dekomposisi) untuk menentukan luas total.. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena hanya memerlukan penghitungan luas bangun komposit sederhana dengan metode petak satuan. Namun, terdapat masalah konten yang signifikan terkait ambiguitas instruksi.. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas sebagai jumlah satuan luas (petak) dan kemampuan menjumlahkan luas bagian-bagian bangun. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa menghitung luas bangun datar sederhana pada kertas berpetak. Tugas ini adalah prosedur rutin. |

Run 3 — solusi: Soal tidak dapat diselesaikan secara definitif karena instruksi tidak spesifik merujuk pada bangun mana yang harus dihitung luasnya. Jika diasumsikan merujuk pada bangun D, luasnya adalah 16 satuan luas (4 + 12).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep luas dengan menghitung jumlah kotak satuan pada bangun datar. Ini adalah prosedur rutin dalam konteks geometri dasar.. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode penghitungan kotak satuan (algoritme dasar) untuk menentukan luas bangun datar.. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.
- Intended difficulty `classify/Easy`: Tugas ini sebenarnya sederhana (menghitung kotak), namun karena instruksi soal tidak spesifik (ambigu), tingkat kesulitan menjadi tidak terukur dengan baik. Jika instruksi jelas, ini termasuk kategori Easy.. Bukti: Hitunglah luas daerah bangun-bangun datar tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang luas sebagai jumlah satuan luas (kotak). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung luas dengan kotak satuan adalah materi dasar kelas 5. Kesulitan utama bukan pada konsep, melainkan pada ketidakjelasan instruksi soal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4721`.
Konten: `valid`; kunci: `verified`; masalah: Instruksi soal 'Hitunglah luas daerah bangun-bangun datar tersebut' bersifat ambigu karena terdapat 7 bangun (A-G) namun hanya ada satu jawaban yang tersedia. Berdasarkan kunci jawaban (16 satuan luas), soal ini secara implisit merujuk pada bangun D yang terdiri dari 16 kotak satuan (4 kotak di bagian atas dan 12 kotak di bagian bawah). Meskipun instruksi kurang spesifik, konteks visual dan pilihan jawaban memungkinkan identifikasi target bangun yang dimaksud..
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur menghitung luas bangun komposit dengan menjumlahkan luas bagian-bagiannya (dekomposisi) pada kertas berpetak. Ini adalah penerapan konsep luas yang rutin.
- Dimensi pengetahuan `procedural`: Siswa menggunakan metode penghitungan kotak satuan atau dekomposisi bangun datar, yang merupakan prosedur standar dalam geometri dasar.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena tugas utamanya adalah menghitung luas bangun komposit sederhana dengan metode petak satuan. Meskipun instruksi kurang spesifik, prosedur penyelesaiannya sangat rutin bagi siswa kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas sebagai jumlah satuan luas (petak) dan kemampuan menjumlahkan luas bagian-bagian bangun. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung luas dengan kotak satuan adalah materi dasar kelas 5. Kesulitan utama bukan pada konsep, melainkan pada ketidakjelasan instruksi soal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 148/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.079866; applying=0.920134; reasoning=0.000000 | applying | 0.920134 | 0.253450 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.027153; conceptual=0.954892; procedural=0.017955; metacognitive=0.000000 | conceptual | 0.954892 | 0.154493 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.714195; Medium=0.281202; Hard=0.004604 | Easy | 0.714195 | 0.566101 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.920134; −Σp ln(p) = 0.278443; H = 0.278443/ln(3) = 0.253450; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.954892; −Σp ln(p) = 0.214172; H = 0.214172/ln(4) = 0.154493; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.714195; −Σp ln(p) = 0.621926; H = 0.621926/ln(3) = 0.566101; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Konsep Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bangun-bangun datar berikut.

Hitunglah luas daerah bangun-bangun datar tersebut.
Pilihan: A. 24 satuan luas
B. 12 satuan luas
C. 16 satuan luas
D. 4 satuan luas
Transkripsi visual: Terdapat 7 bangun datar pada kertas berpetak yang diberi label A sampai G. Bangun D adalah bangun komposit berbentuk huruf L terbalik. Bagian atas bangun D memiliki lebar 2 kotak dan tinggi 2 kotak (luas 4 satuan). Bagian bawah bangun D memiliki lebar 6 kotak dan tinggi 2 kotak (luas 12 satuan). Total luas bangun D adalah 4 + 12 = 16 satuan luas.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Instruksi soal 'Hitunglah luas daerah bangun-bangun datar tersebut' bersifat ambigu karena terdapat 7 bangun (A-G) namun hanya ada satu jawaban yang tersedia. Berdasarkan kunci jawaban (16 satuan luas), soal ini secara implisit merujuk pada bangun D yang terdiri dari 16 kotak satuan (4 kotak di bagian atas dan 12 kotak di bagian bawah). Meskipun instruksi kurang spesifik, konteks visual dan pilihan jawaban memungkinkan identifikasi target bangun yang dimaksud..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `dacf45a93c564182ea5cb7dc`

Perhatikan bangun-bangun persegi panjang berikut. Temukan cara menghitung luas daerahnya.<br><br>\|**Bangun**\|**Panjang**\|**Lebar**\|**Luas Daerah**\|**Hitungan**\|<br>\|---\|---\|---\|---\|---\|<br>\|A\|2 satuan\|1 satuan\|2 satuan luas\|2 × 1 = 2\|<br>\|B\|5 satuan\|2 satuan\|… satuan luas\|5 × 2 = …\|<br>\|C\|… satuan\|… satuan\|… satuan luas\|… × … = …\|<br>\|D\|… satuan\|… satuan\|… satuan luas\|… × … = …\|<br><br>Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas.

| Opsi | Isi |
|---|---|
| A | Panjang 4 satuan, lebar 3 satuan, luas 14 satuan luas |
| B | Panjang 4 satuan, lebar 3 satuan, luas 7 satuan luas |
| C | Panjang 4 satuan, lebar 3 satuan, luas 12 satuan luas |
| D | Panjang 5 satuan, lebar 4 satuan, luas 20 satuan luas |

![Gambar sumber soal 40](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0160-06.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bangun C memiliki panjang 4 satuan dan lebar 3 satuan. Luas = panjang x lebar = 4 x 3 = 12 satuan luas.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0160-06.png. Transkripsi visual: Gambar menampilkan empat persegi panjang (A, B, C, D) pada kertas berpetak. Bangun A berukuran 2x1 petak. Bangun B berukuran 5x2 petak. Bangun C berukuran 4x3 petak. Bangun D berukuran 2x3 petak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `75c83b0680356ff5503a0f802b703c8aad41708a0aae0fb10858e06b06bcf9f9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3626 |
| 2 | success | valid / verified | applying | procedural | Easy | 3628 |
| 3 | success | valid / verified | applying | procedural | Easy | 3601 |

Run 1 — solusi: Bangun C memiliki panjang 4 satuan dan lebar 3 satuan. Luas = panjang x lebar = 4 x 3 = 12 satuan luas.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus luas persegi panjang (panjang x lebar) pada bangun yang diberikan dalam bentuk grid. Ini adalah penerapan prosedur rutin pada konteks visual yang familiar.. Bukti: Temukan cara menghitung luas daerahnya; Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau metode menghitung luas persegi panjang dengan menggunakan data yang diekstraksi dari representasi visual (grid).. Bukti: 2 × 1 = 2; 5 × 2 = …
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu membaca dimensi dari grid dan menerapkan rumus luas yang sudah dipelajari. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Perhatikan bangun-bangun persegi panjang berikut; Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas sebagai hasil kali panjang dan lebar, serta kemampuan membaca satuan pada grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung luas persegi panjang dari grid adalah materi dasar yang sangat familiar dan prosedural. |

Run 2 — solusi: Bangun C memiliki panjang 4 satuan dan lebar 3 satuan. Luas = panjang x lebar = 4 x 3 = 12 satuan luas.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dimensi (panjang dan lebar) dari bangun pada grid dan menerapkan rumus luas persegi panjang (p x l). Ini adalah penerapan prosedur rutin pada konteks visual yang familiar.. Bukti: Temukan cara menghitung luas daerahnya.; Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau metode perhitungan luas persegi panjang (p x l) dan bagaimana menerapkannya pada representasi grid.. Bukti: 2 × 1 = 2; Luas Daerah = panjang x lebar
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menghitung jumlah petak untuk panjang dan lebar, lalu mengalikannya. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Perhatikan bangun-bangun persegi panjang berikut.; Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep luas sebagai jumlah satuan petak dan perkalian bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat familiar dengan konsep luas persegi panjang menggunakan grid dan operasi perkalian dasar. |

Run 3 — solusi: Bangun C memiliki panjang 4 satuan dan lebar 3 satuan. Luas = panjang x lebar = 4 x 3 = 12 satuan luas.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur perkalian panjang dan lebar untuk menghitung luas persegi panjang berdasarkan representasi visual (grid). Ini adalah penerapan konsep luas yang rutin.. Bukti: Temukan cara menghitung luas daerahnya.; Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau metode menghitung luas persegi panjang (panjang x lebar) yang merupakan pengetahuan prosedural.. Bukti: Luas Daerah; 2 × 1 = 2
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membaca ukuran dari grid dan menerapkan rumus luas yang sudah familiar. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: Perhatikan bangun-bangun persegi panjang berikut.; Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep luas sebagai jumlah satuan petak dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung luas persegi panjang dari grid adalah tugas dasar yang rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 299/256; truncation: `True`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999076; applying=0.000924; reasoning=0.000000 | knowing | 0.999076 | 0.006718 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.007676; conceptual=0.689561; procedural=0.302762; metacognitive=0.000000 | conceptual | 0.689561 | 0.472794 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.457657; Medium=0.532470; Hard=0.009873 | Medium | 0.532470 | 0.672569 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999076; −Σp ln(p) = 0.007381; H = 0.007381/ln(3) = 0.006718; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.689561; −Σp ln(p) = 0.655432; H = 0.655432/ln(4) = 0.472794; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.532470; −Σp ln(p) = 0.738892; H = 0.738892/ln(3) = 0.672569; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bangun-bangun persegi panjang berikut. Temukan cara menghitung luas daerahnya.

|**Bangun**|**Panjang**|**Lebar**|**Luas Daerah**|**Hitungan**|
|---|---|---|---|---|
|A|2 satuan|1 satuan|2 satuan luas|2 × 1 = 2|
|B|5 satuan|2 satuan|… satuan luas|5 × 2 = …|
|C|… satuan|… satuan|… satuan luas|… × … = …|
|D|… satuan|… satuan|… satuan luas|… × … = …|

Hitunglah panjang, lebar, dan luas daerah setiap kotak di atas.
Pilihan: A. Panjang 4 satuan, lebar 3 satuan, luas 14 satuan luas
B. Panjang 4 satuan, lebar 3 satuan, luas 7 satuan luas
C. Panjang 4 satuan, lebar 3 satuan, luas 12 satuan luas
D. Panjang 5 satuan, lebar 4 satuan, luas 20 satuan luas
Transkripsi visual: Gambar menampilkan empat persegi panjang (A, B, C, D) pada kertas berpetak. Bangun A berukuran 2x1 petak. Bangun B berukuran 5x2 petak. Bangun C berukuran 4x3 petak. Bangun D berukuran 2x3 petak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Medium", "blindLabel": "Easy", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `ee75e145108e35883906fd59`

Hitung luas daerah bangun gabungan berikut.<br><br>1

| Opsi | Isi |
|---|---|
| A | 216 cm² |
| B | 84 cm² |
| C | 42 cm² |
| D | 432 cm² |

![Gambar sumber soal 41](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0178-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `216 cm²`.
Solusi minimum hasil AI: Luas layang-layang = 1/2 x d1 x d2 = 1/2 x 18 cm x 24 cm = 9 cm x 24 cm = 216 cm².
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0178-03.png. Transkripsi visual: Gambar 1 menunjukkan sebuah bangun datar layang-layang dengan dua diagonal yang saling tegak lurus. Panjang diagonal pertama adalah 18 cm dan panjang diagonal kedua adalah 24 cm.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f64894d8f2c002b27b753da4e1c112e36a059652f8da6a6c1f535eb3215a0378`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3501 |
| 2 | success | valid / verified | applying | procedural | Easy | 3448 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3537 |

Run 1 — solusi: Luas layang-layang = 1/2 x d1 x d2 = 1/2 x 18 cm x 24 cm = 9 cm x 24 cm = 216 cm².
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan rumus luas layang-layang yang sudah dipelajari secara langsung pada data yang diberikan dalam gambar. Tidak ada langkah penalaran kompleks atau strategi nonrutin yang diperlukan.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 1 menunjukkan sebuah layang-layang dengan dua diagonal yang saling tegak lurus. Panjang diagonal pertama adalah 18 cm dan panjang diagonal kedua adalah 24 cm.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap rumus (prosedur) untuk menghitung luas bangun datar tertentu (layang-layang).. Bukti: Hitung luas daerah bangun gabungan berikut.; luas layang-layang = 1/2 x 24 x 18 = 216 cm²
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi bangun datar, memilih rumus yang tepat, dan melakukan perhitungan dasar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan langkah-langkah yang kompleks.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 1 menunjukkan sebuah layang-layang dengan dua diagonal yang saling tegak lurus. Panjang diagonal pertama adalah 18 cm dan panjang diagonal kedua adalah 24 cm.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas bangun datar dan rumus luas layang-layang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung luas bangun datar sederhana dengan rumus yang sudah diketahui adalah tugas standar yang bersifat rutin. |

Run 2 — solusi: Luas layang-layang = 1/2 x d1 x d2 = 1/2 x 18 cm x 24 cm = 9 x 24 cm² = 216 cm².
- Domain kognitif `classify/applying`: Siswa diminta untuk menghitung luas bangun datar (layang-layang) dengan menggunakan rumus yang sudah umum dipelajari. Ini adalah penerapan langsung dari prosedur yang sudah diketahui.. Bukti: Hitung luas daerah bangun gabungan berikut. 1; luas layang-layang = 1/2 x 24 x 18 = 216 cm²
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau rumus luas bangun datar layang-layang.. Bukti: luas layang-layang = 1/2 x 24 x 18
- Intended difficulty `classify/Easy`: Soal ini termasuk kategori mudah karena siswa hanya perlu mengidentifikasi bangun datar sebagai layang-layang dan menerapkan rumus luas yang sudah familiar secara langsung tanpa langkah tambahan atau integrasi yang kompleks.. Bukti: Hitung luas daerah bangun gabungan berikut. 1; 18 cm; 24 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus luas layang-layang dan operasi perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari luas bangun datar. Soal ini adalah latihan rutin yang tidak memerlukan perencanaan strategi atau integrasi konsep yang rumit. |

Run 3 — solusi: Luas layang-layang = 1/2 x d1 x d2 = 1/2 x 18 cm x 24 cm = 9 x 24 cm² = 216 cm².
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerapkan rumus luas bangun datar (layang-layang) yang sudah diketahui secara langsung pada data yang diberikan. Tidak ada langkah penalaran kompleks atau strategi nonrutin yang diperlukan.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 1 menunjukkan sebuah bangun datar layang-layang dengan dua diagonal yang saling tegak lurus. Panjang diagonal pertama adalah 18 cm dan panjang diagonal kedua adalah 24 cm.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural siswa dalam menggunakan rumus luas layang-layang (1/2 x d1 x d2) untuk menyelesaikan masalah perhitungan sederhana.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 1 menunjukkan sebuah bangun datar layang-layang dengan dua diagonal yang saling tegak lurus. Panjang diagonal pertama adalah 18 cm dan panjang diagonal kedua adalah 24 cm.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu mengidentifikasi bangun, memilih rumus yang tepat, dan melakukan operasi hitung dasar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan langkah yang kompleks.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 1 menunjukkan sebuah bangun datar layang-layang dengan dua diagonal yang saling tegak lurus. Panjang diagonal pertama adalah 18 cm dan panjang diagonal kedua adalah 24 cm.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus luas layang-layang dan operasi perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung luas bangun datar sederhana dengan rumus yang sudah dipelajari adalah tugas rutin yang sesuai dengan tingkat kemampuan dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5155`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk menerapkan rumus luas layang-layang yang sudah dipelajari secara langsung pada data yang diberikan dalam gambar. Tidak ada langkah penalaran kompleks atau strategi nonrutin yang diperlukan.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman siswa terhadap rumus (prosedur) untuk menghitung luas bangun datar tertentu (layang-layang).
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi bangun datar, memilih rumus yang tepat, dan melakukan perhitungan dasar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan langkah-langkah yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas bangun datar dan rumus luas layang-layang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung luas bangun datar sederhana dengan rumus yang sudah diketahui adalah tugas standar yang bersifat rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 91/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.988969; applying=0.011031; reasoning=0.000000 | knowing | 0.988969 | 0.055239 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.895707; conceptual=0.087744; procedural=0.016549; metacognitive=0.000000 | factual | 0.895707 | 0.274141 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.924536; Medium=0.072166; Hard=0.003298 | Easy | 0.924536 | 0.255866 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.988969; −Σp ln(p) = 0.060686; H = 0.060686/ln(3) = 0.055239; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.895707; −Σp ln(p) = 0.380040; H = 0.380040/ln(4) = 0.274141; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.924536; −Σp ln(p) = 0.281097; H = 0.281097/ln(3) = 0.255866; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitung luas daerah bangun gabungan berikut.

1
Pilihan: A. 216 cm²
B. 84 cm²
C. 42 cm²
D. 432 cm²
Transkripsi visual: Gambar 1 menunjukkan sebuah bangun datar layang-layang dengan dua diagonal yang saling tegak lurus. Panjang diagonal pertama adalah 18 cm dan panjang diagonal kedua adalah 24 cm.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `e4a5a859b3d314d36c30b33a`

Hitung luas daerah bangun gabungan berikut.<br><br>3

| Opsi | Isi |
|---|---|
| A | 22 satuan luas |
| B | 20 satuan luas |
| C | 28 satuan luas |
| D | 16 satuan luas |

![Gambar sumber soal 42](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0178-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bangun A terdiri dari persegi panjang 4x4 (luas 16) ditambah dua segitiga dengan luas masing-masing 4 dan 2, sehingga total luas adalah 16 + 4 + 2 = 22 satuan luas.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0178-03.png. Transkripsi visual: Gambar 3 menampilkan bangun datar A pada kertas berpetak. Bangun tersebut dapat didekomposisi menjadi persegi panjang 4x4 dan dua segitiga tambahan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a6a16fe557774a7c803eb191003d0098c8896f88123c78fa4e83d59cc0223249`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3601 |
| 2 | success | concern / unverifiable | — | — | — | 3327 |
| 3 | success | valid / verified | applying | procedural | Medium | 3572 |

Run 1 — solusi: Bangun A terdiri dari persegi panjang 4x4 (luas 16), segitiga kiri (alas 1, tinggi 4, luas 0.5*1*4=2), dan segitiga kanan (alas 2, tinggi 4, luas 0.5*2*4=4). Total luas = 16 + 2 + 4 = 22 satuan luas.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bangun-bangun penyusun (persegi panjang dan segitiga) dari gambar gabungan pada kertas berpetak, lalu menerapkan rumus luas masing-masing bangun dan menjumlahkannya. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar nomor 3 (label A) pada kertas berpetak.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritme atau metode standar untuk menghitung luas bangun datar (persegi panjang dan segitiga) dan menjumlahkannya untuk mendapatkan luas total.. Bukti: Hitung luas daerah bangun gabungan berikut.
- Intended difficulty `classify/Easy`: Soal ini meminta dekomposisi bangun gabungan sederhana pada grid. Jalur penyelesaian jelas (memecah menjadi persegi panjang dan segitiga), langkah-langkahnya rutin, dan beban kognitif rendah bagi siswa kelas 5.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar nomor 3 (label A) pada kertas berpetak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman luas persegi panjang dan segitiga, serta konsep luas sebagai penjumlahan daerah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa menghitung luas bangun datar sederhana dan gabungan pada kertas berpetak. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan. |

Run 2 — solusi: Tidak dapat ditentukan karena ketidakjelasan referensi bangun dalam soal dan ketidaksesuaian kunci dengan visual.
- Domain kognitif `abstain/None`: Soal tidak dapat diklasifikasikan karena ambiguitas referensi visual (tidak jelas bangun mana yang harus dihitung) dan ketidaksesuaian antara kunci jawaban dengan gambar yang tersedia.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Soal tidak dapat diklasifikasikan karena ambiguitas referensi visual dan ketidaksesuaian kunci jawaban.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak dapat diklasifikasikan karena ambiguitas referensi visual dan ketidaksesuaian kunci jawaban.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 3 — solusi: Bangun dapat dipecah menjadi persegi panjang 4x4 (luas 16), segitiga siku-siku di kiri (alas 1, tinggi 4, luas 0.5*1*4=2), dan segitiga di kanan atas (alas 2, tinggi 4, luas 0.5*2*4=4). Total luas = 16 + 2 + 4 = 22 satuan luas.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur menghitung luas bangun datar gabungan dengan cara mendekomposisi bangun tersebut menjadi bangun-bangun sederhana (persegi panjang dan segitiga) yang luasnya sudah dipelajari.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar nomor 3 menunjukkan poligon pada kertas berpetak
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritme atau metode standar untuk menghitung luas bangun datar gabungan melalui dekomposisi.. Bukti: Hitung luas daerah bangun gabungan berikut.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa perlu melakukan dekomposisi bangun gabungan menjadi beberapa bagian (persegi panjang dan segitiga) secara mandiri, yang melibatkan beberapa langkah terkait, meskipun prosedurnya familiar.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar nomor 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas persegi panjang dan segitiga, serta kemampuan dekomposisi bangun datar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung luas bangun datar gabungan dengan memecahnya menjadi bangun sederhana. Tugas ini memerlukan perencanaan dekomposisi yang tepat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 1} | no_consensus / adjudicated | Easy |

Adjudikasi AI: `success`; token `6662`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur menghitung luas bangun datar gabungan dengan mendekomposisi bangun menjadi persegi panjang dan segitiga pada kertas berpetak.
- Dimensi pengetahuan `procedural`: Siswa menggunakan metode dekomposisi untuk menghitung luas bangun gabungan, yang merupakan prosedur standar dalam geometri dasar.
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung konsep luas bangun datar pada kertas berpetak. Jalur penyelesaian (dekomposisi) jelas dan rutin bagi siswa kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman luas persegi panjang dan segitiga, serta konsep luas sebagai penjumlahan daerah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa menghitung luas bangun datar sederhana dan gabungan pada kertas berpetak. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 91/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.996936; applying=0.003064; reasoning=0.000000 | knowing | 0.996936 | 0.018929 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.290892; conceptual=0.690489; procedural=0.018619; metacognitive=0.000000 | conceptual | 0.690489 | 0.497075 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.901748; Medium=0.095102; Hard=0.003150 | Easy | 0.901748 | 0.305075 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996936; −Σp ln(p) = 0.020796; H = 0.020796/ln(3) = 0.018929; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.690489; −Σp ln(p) = 0.689092; H = 0.689092/ln(4) = 0.497075; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.901748; −Σp ln(p) = 0.335159; H = 0.335159/ln(3) = 0.305075; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Luas Daerah Bangun Gabungan
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitung luas daerah bangun gabungan berikut.

3
Pilihan: A. 22 satuan luas
B. 20 satuan luas
C. 28 satuan luas
D. 16 satuan luas
Transkripsi visual: Gambar 3 menampilkan bangun datar A pada kertas berpetak. Bangun tersebut dapat didekomposisi menjadi persegi panjang 4x4 dan dua segitiga tambahan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `201997c9ac57959886dabd86`

Hitung luas daerah bangun gabungan berikut.<br><br>2

| Opsi | Isi |
|---|---|
| A | 224 cm² |
| B | 128 cm² |
| C | 320 cm² |
| D | 160 cm² |

![Gambar sumber soal 43](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0178-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Luas = Luas jajargenjang + Luas segitiga = (alas x tinggi) + (1/2 x alas x tinggi) = (16 x 8) + (1/2 x 16 x 12) = 128 + 96 = 224 cm².
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0178-03.png. Transkripsi visual: Gambar 2 menunjukkan sebuah bangun gabungan yang terdiri dari jajargenjang di bagian atas dan segitiga di bagian bawah. Jajargenjang memiliki alas 16 cm dan tinggi 8 cm. Segitiga memiliki alas 16 cm (berhimpit dengan alas jajargenjang) dan tinggi 12 cm.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5eaf02adea54abef59a3610330a0b4616d786d10fdfc20c319f797e78673f9e5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3576 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3566 |
| 3 | success | valid / verified | applying | procedural | Medium | 3506 |

Run 1 — solusi: Luas = Luas jajargenjang + Luas segitiga = (alas x tinggi) + (1/2 x alas x tinggi) = (16 x 8) + (1/2 x 16 x 12) = 128 + 96 = 224 cm².
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dua bangun datar penyusun (jajargenjang dan segitiga) dan menerapkan rumus luas masing-masing untuk kemudian dijumlahkan. Ini adalah penerapan prosedur rutin pada konteks bangun gabungan.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 2 menunjukkan bangun gabungan yang terdiri dari jajargenjang di bagian atas dan segitiga di bagian bawah.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara bangun gabungan dan bangun-bangun penyusunnya (konseptual) serta menerapkan rumus luas yang relevan (prosedural).. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 2 menunjukkan bangun gabungan yang terdiri dari jajargenjang di bagian atas dan segitiga di bagian bawah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dekomposisi bangun gabungan menjadi dua bangun sederhana (jajargenjang dan segitiga) dan melakukan dua perhitungan luas yang berbeda sebelum menjumlahkannya. Meskipun rumusnya familiar, terdapat beberapa langkah yang saling terkait yang harus direncanakan oleh siswa.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 2 menunjukkan bangun gabungan yang terdiri dari jajargenjang di bagian atas dan segitiga di bagian bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus luas jajargenjang dan segitiga, serta konsep penjumlahan luas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah mampu menghitung luas bangun datar sederhana. Soal ini menuntut kemampuan dekomposisi bangun gabungan yang merupakan standar kompetensi kelas 5. |

Run 2 — solusi: Luas bangun = Luas jajar genjang + Luas segitiga = (alas x tinggi) + (1/2 x alas x tinggi) = (16 x 8) + (1/2 x 16 x 12) = 128 + 96 = 224 cm².
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi komponen bangun gabungan (jajar genjang dan segitiga) dan menerapkan rumus luas masing-masing bangun yang sudah dipelajari di kelas 5, kemudian menjumlahkannya. Ini adalah penerapan prosedur rutin.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 2 menunjukkan sebuah bangun gabungan yang terdiri dari jajar genjang di bagian atas dan segitiga di bagian bawah.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara bangun gabungan dan komponen-komponen penyusunnya (jajar genjang dan segitiga) serta menerapkan rumus luas yang relevan.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 2 menunjukkan sebuah bangun gabungan yang terdiri dari jajar genjang di bagian atas dan segitiga di bagian bawah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah perhitungan luas bangun datar yang berbeda (jajar genjang dan segitiga) dan satu langkah penjumlahan. Meskipun prosedurnya rutin, siswa harus mampu membedah bangun gabungan menjadi komponen yang dikenal dan menerapkan rumus yang tepat untuk masing-masing bagian.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar 2 menunjukkan sebuah bangun gabungan yang terdiri dari jajar genjang di bagian atas dan segitiga di bagian bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus luas jajar genjang dan segitiga. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari luas bangun datar. Soal ini menuntut penggabungan dua rumus dasar yang merupakan standar kompetensi kelas 5. |

Run 3 — solusi: Luas = Luas jajargenjang + Luas segitiga = (alas x tinggi) + (1/2 x alas x tinggi) = (16 x 8) + (1/2 x 16 x 12) = 128 + 96 = 224 cm².
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dua bangun datar penyusun (jajargenjang dan segitiga) dan menerapkan rumus luas masing-masing untuk kemudian dijumlahkan. Ini adalah penerapan prosedur rutin pada konteks bangun gabungan.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar nomor 2 menunjukkan bangun gabungan yang terdiri dari jajargenjang di bagian atas dan segitiga di bagian bawah.
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang rumus luas bangun datar (konseptual) dan kemampuan melakukan perhitungan algoritma (prosedural) untuk mendapatkan hasil akhir.. Bukti: Luas jajargenjang; Luas segitiga
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dekomposisi bangun gabungan menjadi dua bangun sederhana (jajargenjang dan segitiga) dan melakukan dua perhitungan luas yang berbeda sebelum menjumlahkannya. Meskipun rumusnya familiar, terdapat beberapa langkah yang saling terkait.. Bukti: Hitung luas daerah bangun gabungan berikut.; Gambar nomor 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas jajargenjang dan segitiga. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung luas bangun gabungan dengan memecahnya menjadi bangun-bangun dasar yang sudah dipelajari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5273`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi dua bangun datar penyusun (jajargenjang dan segitiga) dari gambar gabungan, memilih rumus yang tepat untuk masing-masing, dan melakukan operasi penjumlahan. Ini adalah penerapan prosedur rutin pada konteks bangun gabungan.
- Dimensi pengetahuan `procedural`: Siswa harus menggunakan pengetahuan prosedural tentang rumus luas bangun datar (jajargenjang dan segitiga) dan menerapkannya secara berurutan untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dekomposisi bangun gabungan menjadi dua bangun sederhana dan melakukan dua perhitungan luas yang berbeda sebelum menjumlahkannya. Meskipun rumusnya familiar, terdapat beberapa langkah yang saling terkait yang harus direncanakan oleh siswa.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus luas jajargenjang dan segitiga, serta konsep penjumlahan luas. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah mampu menghitung luas bangun datar sederhana. Soal ini menuntut kemampuan dekomposisi bangun gabungan yang merupakan standar kompetensi kelas 5. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 115/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006805; applying=0.993195; reasoning=0.000000 | applying | 0.993195 | 0.037081 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.699067; conceptual=0.266513; procedural=0.034420; metacognitive=0.000000 | factual | 0.699067 | 0.518400 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.910287; Medium=0.086725; Hard=0.002988 | Easy | 0.910287 | 0.286703 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993195; −Σp ln(p) = 0.040737; H = 0.040737/ln(3) = 0.037081; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.699067; −Σp ln(p) = 0.718655; H = 0.718655/ln(4) = 0.518400; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.910287; −Σp ln(p) = 0.314975; H = 0.314975/ln(3) = 0.286703; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Luas Daerah Bangun Gabungan
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitung luas daerah bangun gabungan berikut.

2
Pilihan: A. 224 cm²
B. 128 cm²
C. 320 cm²
D. 160 cm²
Transkripsi visual: Gambar 2 menunjukkan sebuah bangun gabungan yang terdiri dari jajargenjang di bagian atas dan segitiga di bagian bawah. Jajargenjang memiliki alas 16 cm dan tinggi 8 cm. Segitiga memiliki alas 16 cm (berhimpit dengan alas jajargenjang) dan tinggi 12 cm.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `0d61de45054218c7d9af6710`

Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.<br><br>Manakah yang menghasilkan kerangka yang terluas?

| Opsi | Isi |
|---|---|
| A | Panjang 25 cm dan lebar 5 cm (luas 125 cm²) |
| B | Panjang 15 cm dan lebar 15 cm (luas 225 cm²) |
| C | Panjang 20 cm dan lebar 10 cm (luas 200 cm²) |
| D | Panjang 18 cm dan lebar 12 cm (luas 216 cm²) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Keliling persegi panjang adalah 2 x (p + l) = 60 cm, maka p + l = 30 cm. Luas = p x l. Untuk keliling tetap, luas maksimum persegi panjang tercapai saat p = l (persegi). Maka p = l = 15 cm. Luas = 15 x 15 = 225 cm². Pilihan B adalah yang terbesar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `199b62ad1de10475a843f6e0481eb901e8abe23394fb0a61547936e587c3db23`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2512 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2539 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2477 |

Run 1 — solusi: Keliling persegi panjang adalah 2 x (p + l) = 60 cm, maka p + l = 30 cm. Luas = p x l. Untuk keliling tetap, luas maksimum persegi panjang tercapai saat p = l (persegi). Maka p = l = 15 cm. Luas = 15 x 15 = 225 cm². Pilihan B adalah yang terbesar.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara keliling tetap dan luas maksimum pada persegi panjang. Ini melibatkan pemilihan strategi untuk menguji opsi atau menerapkan prinsip bahwa persegi memiliki luas terbesar untuk keliling tertentu, yang merupakan penerapan konsep pada konteks rutin.. Bukti: Manakah yang menghasilkan kerangka yang terluas?; Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara keliling dan luas (konsep) serta prosedur menghitung luas dari dimensi yang diberikan.. Bukti: Manakah yang menghasilkan kerangka yang terluas?; Bapak memiliki kawat sepanjang 60 cm
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah perhitungan (menghitung luas untuk setiap opsi) dan membandingkannya untuk menentukan nilai maksimum. Meskipun konsepnya mendasar, siswa perlu melakukan verifikasi sistematis terhadap pilihan yang ada.. Bukti: Manakah yang menghasilkan kerangka yang terluas?; Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus keliling dan luas persegi panjang, serta operasi perkalian dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu menghitung luas persegi panjang. Menentukan luas maksimum dari beberapa opsi dengan keliling tetap memerlukan ketelitian dalam perhitungan dan perbandingan, yang sesuai dengan tingkat kesulitan menengah untuk jenjang ini. |

Run 2 — solusi: Keliling persegi panjang adalah 2(p+l) = 60 cm, sehingga p+l = 30 cm. Luas = p x l. Untuk p+l tetap, luas maksimum tercapai saat p=l (persegi). Maka p=l=15 cm, luas = 15x15 = 225 cm². Pilihan B adalah 15x15=225 cm², yang merupakan luas terbesar di antara pilihan yang ada.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara keliling tetap dan luas persegi panjang, serta menguji atau menyimpulkan bahwa bentuk persegi (kasus khusus persegi panjang) memberikan luas maksimum. Ini melibatkan penerapan konsep luas dan keliling dalam konteks pemilihan nilai optimal.. Bukti: Manakah yang menghasilkan kerangka yang terluas?; Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip hubungan keliling dan luas (konseptual) untuk mengevaluasi pilihan jawaban yang diberikan (prosedural).. Bukti: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.; Manakah yang menghasilkan kerangka yang terluas?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memahami bahwa persegi panjang dengan keliling tetap memiliki luas yang berbeda-beda. Siswa harus menghitung atau membandingkan luas dari setiap opsi. Meskipun konsep luas maksimum adalah materi lanjut, untuk kelas 5, siswa dapat menyelesaikannya dengan menghitung luas setiap opsi yang tersedia (prosedur rutin).. Bukti: Bapak memiliki kawat sepanjang 60 cm.; Manakah yang menghasilkan kerangka yang terluas?; A. Panjang 25 cm dan lebar 5 cm; B. Panjang 15 cm dan lebar 15 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus keliling dan luas persegi panjang, serta operasi perkalian dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari luas dan keliling. Menghitung luas dari setiap opsi adalah prosedur yang dapat diakses, namun menuntut ketelitian dalam membandingkan hasil untuk menentukan yang terbesar. |

Run 3 — solusi: Keliling = 2(p+l) = 60, maka p+l = 30. Luas = p x l. Untuk p+l tetap, luas maksimum dicapai saat p=l (persegi). Maka p=l=15, luas = 15x15 = 225 cm².
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara keliling dan luas persegi panjang, serta menguji atau menyimpulkan bahwa untuk keliling tetap, persegi memiliki luas terbesar. Ini melibatkan pemilihan strategi untuk membandingkan luas dari berbagai kemungkinan dimensi yang memenuhi syarat keliling.. Bukti: Manakah yang menghasilkan kerangka yang terluas?; Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana dimensi (panjang dan lebar) memengaruhi luas ketika kelilingnya tetap.. Bukti: Hubungan Keliling dan Luas Daerah Bangun Datar
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya menghitung luas, tetapi harus membandingkan beberapa opsi untuk menemukan nilai maksimum. Meskipun prosedurnya familiar, siswa perlu melakukan beberapa langkah perhitungan (luas) untuk setiap opsi dan memahami bahwa persegi adalah kasus khusus persegi panjang yang memberikan luas maksimal.. Bukti: Manakah yang menghasilkan kerangka yang terluas?; Panjang 25 cm dan lebar 5 cm; Panjang 15 cm dan lebar 15 cm; Panjang 20 cm dan lebar 10 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus keliling dan luas persegi panjang, serta operasi perkalian dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari luas dan keliling. Menghitung luas dari beberapa opsi dan membandingkannya adalah tugas yang sesuai, namun memerlukan ketelitian dalam perhitungan dan pemahaman konsep optimasi sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 123/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.010410; applying=0.989590; reasoning=0.000000 | applying | 0.989590 | 0.052684 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.546288; conceptual=0.429900; procedural=0.023812; metacognitive=0.000000 | factual | 0.546288 | 0.564247 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.914447; Medium=0.083056; Hard=0.002497 | Easy | 0.914447 | 0.276177 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.989590; −Σp ln(p) = 0.057879; H = 0.057879/ln(3) = 0.052684; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.546288; −Σp ln(p) = 0.782212; H = 0.782212/ln(4) = 0.564247; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.914447; −Σp ln(p) = 0.303411; H = 0.303411/ln(3) = 0.276177; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Hubungan Keliling dan Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.

Manakah yang menghasilkan kerangka yang terluas?
Pilihan: A. Panjang 25 cm dan lebar 5 cm (luas 125 cm²)
B. Panjang 15 cm dan lebar 15 cm (luas 225 cm²)
C. Panjang 20 cm dan lebar 10 cm (luas 200 cm²)
D. Panjang 18 cm dan lebar 12 cm (luas 216 cm²)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `fbc3163f1b8a4e5fbfc4eaae`

Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.<br><br>Berapa ukuran-ukuran yang mungkin dibuat. Jika panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?

| Opsi | Isi |
|---|---|
| A | Lebar 42 cm, luas 756 cm² |
| B | Lebar 12 cm, luas 60 cm² |
| C | Lebar 12 cm, luas 30 cm² |
| D | Lebar 12 cm, luas 216 cm² |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Keliling = 2 x (p + l) = 60 cm, maka p + l = 30 cm. Jika p = 18 cm, maka l = 30 - 18 = 12 cm. Luas = p x l = 18 cm x 12 cm = 216 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fd8253696d902c37f77899511c55838f53e55c2ba1cf867bcf7ace6f4021de39`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2425 |
| 2 | success | valid / verified | applying | procedural | Easy | 2401 |
| 3 | success | valid / verified | applying | procedural | Medium | 2365 |

Run 1 — solusi: Keliling = 2 x (panjang + lebar). 60 = 2 x (18 + lebar). 30 = 18 + lebar. Lebar = 30 - 18 = 12 cm. Luas = panjang x lebar = 18 cm x 12 cm = 216 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep keliling persegi panjang untuk mencari lebar, kemudian menerapkan rumus luas persegi panjang. Ini adalah penerapan prosedur rutin pada konteks yang sudah familiar bagi kelas 5.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Jika panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode standar (rumus keliling dan luas) untuk menyelesaikan masalah.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Jika panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan dua langkah yang saling bergantung: pertama mencari lebar dari keliling, kemudian menghitung luas. Meskipun prosedurnya rutin, siswa harus memahami hubungan antara keliling dan setengah keliling (panjang + lebar) sebelum menghitung luas.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Jika panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus keliling dan luas persegi panjang, serta operasi dasar aritmatika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari hubungan keliling dan luas. Soal ini menuntut pemahaman bahwa keliling kawat adalah total panjang sisi, yang memerlukan pemahaman konsep dasar geometri tanpa tingkat abstraksi tinggi. |

Run 2 — solusi: Keliling = 2 x (p + l) = 60 cm. Maka p + l = 30 cm. Jika p = 18 cm, maka l = 30 - 18 = 12 cm. Luas = p x l = 18 cm x 12 cm = 216 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep keliling persegi panjang untuk mencari lebar, kemudian menerapkan rumus luas persegi panjang. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Jika panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara keliling dan luas, serta penggunaan rumus-rumus dasar tersebut secara prosedural.. Bukti: keliling = 2 x (p + l); luas = p x l
- Intended difficulty `classify/Easy`: Soal ini meminta dua langkah berurutan yang familiar bagi siswa kelas 5: mencari lebar dari keliling yang diketahui, lalu menghitung luas. Jalur penyelesaian sangat jelas dan tidak memerlukan strategi nonrutin.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Jika panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep keliling dan luas persegi panjang, serta operasi hitung dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari hubungan keliling dan luas persegi panjang. Soal ini adalah aplikasi langsung dari rumus tersebut tanpa jebakan atau kompleksitas tambahan. |

Run 3 — solusi: Keliling = 2 x (p + l) = 60 cm. Maka p + l = 30 cm. Jika p = 18 cm, maka l = 30 - 18 = 12 cm. Luas = p x l = 18 cm x 12 cm = 216 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep keliling persegi panjang untuk mencari lebar, kemudian menerapkan rumus luas. Ini adalah penerapan prosedur familiar pada konteks rutin.. Bukti: Bapak memiliki kawat sepanjang 60 cm; panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme atau metode perhitungan keliling dan luas yang sudah dipelajari.. Bukti: keliling = 2 x (p + l); luas = p x l
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah berurutan: mencari lebar dari keliling, lalu menghitung luas. Jalur penyelesaian jelas dan prosedural.. Bukti: Bapak memiliki kawat sepanjang 60 cm; panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus keliling dan luas persegi panjang, serta operasi hitung dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan hubungan keliling dan luas. Soal ini menuntut dua langkah perhitungan yang saling terkait namun prosedurnya standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3997`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan konsep keliling persegi panjang untuk menentukan lebar, kemudian menerapkan rumus luas. Ini adalah penerapan prosedur rutin pada konteks yang sudah familiar bagi kelas 5.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritma atau metode standar (rumus keliling dan luas) untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena menuntut dua langkah yang saling bergantung: mencari lebar dari keliling, kemudian menghitung luas. Meskipun prosedurnya rutin, siswa harus memahami hubungan antara keliling dan setengah keliling (panjang + lebar) sebelum menghitung luas.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus keliling dan luas persegi panjang, serta operasi dasar aritmatika. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari hubungan keliling dan luas. Soal ini menuntut pemahaman bahwa keliling kawat adalah total panjang sisi, yang memerlukan pemahaman konsep dasar geometri tanpa tingkat abstraksi tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 117/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.388981; applying=0.611019; reasoning=0.000000 | applying | 0.611019 | 0.608304 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.585788; conceptual=0.384481; procedural=0.029731; metacognitive=0.000000 | factual | 0.585788 | 0.566480 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.915089; Medium=0.082117; Hard=0.002794 | Easy | 0.915089 | 0.275701 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.611019; −Σp ln(p) = 0.668290; H = 0.668290/ln(3) = 0.608304; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.585788; −Σp ln(p) = 0.785308; H = 0.785308/ln(4) = 0.566480; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.915089; −Σp ln(p) = 0.302888; H = 0.302888/ln(3) = 0.275701; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Hubungan Keliling dan Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.

Berapa ukuran-ukuran yang mungkin dibuat. Jika panjang kerangka 18 cm, berapa lebar dan luas kerangka tersebut?
Pilihan: A. Lebar 42 cm, luas 756 cm²
B. Lebar 12 cm, luas 60 cm²
C. Lebar 12 cm, luas 30 cm²
D. Lebar 12 cm, luas 216 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `4088b8d020de84282c07a2b3`

Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?

| Opsi | Isi |
|---|---|
| A | 1.249 liter 325 ml |
| B | 1.250 liter 675 ml |
| C | 1.249 liter 675 ml |
| D | 1.250 liter 325 ml |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 2.225 liter = 2.224 liter 1.000 ml. Pengurangan: (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `60ea68bbb8208ab912d8c9df694db3424a76b327bd2bd0d92c5763b90a72f8e0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2443 |
| 2 | success | valid / verified | applying | procedural | Medium | 2493 |
| 3 | success | valid / verified | applying | procedural | Medium | 2498 |

Run 1 — solusi: 2.225 liter = 2.224 liter 1.000 ml. Pengurangan: (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan satuan campuran (liter dan mililiter) yang memerlukan teknik meminjam (regrouping) antar satuan volume.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma pengurangan dengan satuan yang berbeda dan konversi antar satuan volume (1 liter = 1.000 ml).. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan langkah konversi satuan (meminjam 1 liter menjadi 1.000 ml) sebelum melakukan pengurangan, yang merupakan tantangan prosedural standar bagi kelas 5.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan volume (liter ke ml) dan pengurangan bersusun. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu melakukan operasi hitung dengan satuan campuran. Tantangan utama adalah melakukan regrouping 1 liter menjadi 1.000 ml agar pengurangan mililiter dapat dilakukan. |

Run 2 — solusi: 2.225 liter = 2.224 liter 1.000 ml. Pengurangan: (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan satuan campuran (liter dan mililiter) yang memerlukan teknik meminjam antar satuan (konversi 1 liter menjadi 1.000 ml). Ini adalah penerapan prosedur rutin dalam konteks pengukuran.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antar satuan volume (liter ke mililiter) dan prosedur pengurangan yang melibatkan konversi satuan tersebut.. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan langkah konversi satuan (meminjam 1 liter menjadi 1.000 ml) sebelum melakukan pengurangan. Meskipun prosedurnya familiar, siswa harus melakukan dua langkah terintegrasi (konversi dan pengurangan) untuk mendapatkan hasil yang benar, yang merupakan tuntutan sedang bagi kelas 5.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan volume (1 liter = 1.000 ml) dan operasi pengurangan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu melakukan operasi hitung dengan satuan campuran. Tantangan terletak pada ketelitian saat melakukan konversi satuan (meminjam) agar tidak terjebak pada kesalahan umum seperti yang ditunjukkan oleh opsi pengecoh. |

Run 3 — solusi: 2.225 liter = 2.224 liter 1.000 ml. Pengurangan: (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan satuan campuran (liter dan mililiter) yang memerlukan teknik meminjam antar satuan (konversi 1 liter menjadi 1.000 ml). Ini adalah penerapan prosedur rutin dalam konteks pengukuran.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme pengurangan dengan satuan yang berbeda dan hubungan konversi antar satuan volume (liter ke mililiter).. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah terkait: konversi satuan (meminjam 1 liter menjadi 1.000 ml) dan pengurangan bilangan desimal/campuran. Meskipun prosedurnya rutin, siswa kelas 5 sering melakukan kesalahan pada proses 'meminjam' antar satuan yang berbeda, sehingga tuntutan kognitifnya lebih tinggi daripada pengurangan bilangan bulat biasa.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan volume (1 liter = 1.000 ml) dan pengurangan bersusun. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari satuan volume dan operasi hitung campuran. Tantangan utama adalah ketelitian dalam melakukan konversi satuan saat pengurangan, yang merupakan keterampilan standar namun menuntut ketelitian pada level ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 103/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.020880; applying=0.979120; reasoning=0.000000 | applying | 0.979120 | 0.092338 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.784812; conceptual=0.194082; procedural=0.021106; metacognitive=0.000000 | factual | 0.784812 | 0.425446 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.880745; Medium=0.115963; Hard=0.003292 | Easy | 0.880745 | 0.346349 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.979120; −Σp ln(p) = 0.101444; H = 0.101444/ln(3) = 0.092338; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.784812; −Σp ln(p) = 0.589793; H = 0.589793/ln(4) = 0.425446; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.880745; −Σp ln(p) = 0.380503; H = 0.380503/ln(3) = 0.346349; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Pengukuran Volume
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?
Pilihan: A. 1.249 liter 325 ml
B. 1.250 liter 675 ml
C. 1.249 liter 675 ml
D. 1.250 liter 325 ml
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `5b39909f145e4cc23b6e544c`

Perhatikan bangun datar berikut. Temukan banyaknya sudut siku-siku pada setiap bangun berikut.<br><br>Bangun 5

| Opsi | Isi |
|---|---|
| A | 0 |
| B | 4 |
| C | 3 |
| D | 2 |

![Gambar sumber soal 47](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0185-10.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bangun nomor 5 adalah persegi. Persegi memiliki empat sudut siku-siku, terlepas dari orientasi rotasinya. Oleh karena itu, terdapat 4 sudut siku-siku.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0185-10.png. Transkripsi visual: Terdapat enam bangun datar yang diberi nomor 1 sampai 6. Bangun nomor 5 adalah sebuah persegi yang diputar 45 derajat, memiliki empat sisi yang sama panjang dan empat sudut yang semuanya merupakan sudut siku-siku.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `135805ffa51dcab8464e1797ea9e1e541afca5e30ebd0a3364e854492a046742`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3402 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3387 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3374 |

Run 1 — solusi: Bangun nomor 5 adalah persegi. Persegi memiliki empat sudut siku-siku, terlepas dari orientasi rotasinya. Oleh karena itu, terdapat 4 sudut siku-siku.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi properti sudut siku-siku pada bangun datar yang posisinya diputar. Ini memerlukan pengenalan konsep sudut siku-siku yang tidak bergantung pada orientasi bangun (rotasi), yang merupakan penerapan konsep dasar pada konteks visual yang sedikit dimodifikasi.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut. Bangun 5
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi sudut siku-siku dan sifat-sifat bangun datar (persegi) yang tetap konstan meskipun orientasinya berubah.. Bukti: Temukan banyaknya sudut siku-siku
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengenalan visual langsung terhadap sifat dasar bangun datar (persegi). Meskipun bangun diputar, sifat sudut siku-siku tetap jelas bagi siswa kelas 5.. Bukti: Bangun 5; Temukan banyaknya sudut siku-siku

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku dan pengenalan bentuk bangun datar (persegi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah mampu mengenali sudut siku-siku pada berbagai orientasi bangun datar sederhana. |

Run 2 — solusi: Bangun nomor 5 adalah persegi. Persegi memiliki empat sudut yang masing-masing besarnya 90 derajat (sudut siku-siku). Meskipun bangun tersebut diputar, sifat sudutnya tidak berubah.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah sudut siku-siku pada bangun datar yang diberikan. Ini adalah penerapan langsung dari konsep sudut siku-siku pada bentuk geometri yang sudah dikenal, meskipun orientasinya berubah.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut. Bangun 5
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat sudut siku-siku pada bangun datar (persegi) terlepas dari orientasi rotasinya.. Bukti: Temukan banyaknya sudut siku-siku
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengenali sifat dasar bangun datar (persegi) dan sudut siku-siku. Rotasi bangun mungkin sedikit mengecoh bagi siswa yang belum memahami invarian bentuk, namun prosedurnya tetap langsung.. Bukti: Bangun 5

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku dan bentuk bangun datar (persegi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi sudut siku-siku pada bangun datar adalah materi dasar. Tantangan rotasi adalah bagian dari pengembangan pemahaman spasial yang wajar di tingkat ini. |

Run 3 — solusi: Bangun nomor 5 adalah persegi yang diputar. Persegi memiliki empat sudut siku-siku. Oleh karena itu, bangun nomor 5 memiliki 4 sudut siku-siku.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah sudut siku-siku pada bangun yang diberikan. Ini adalah penerapan langsung dari definisi sudut siku-siku pada bentuk geometri yang sudah dikenal, meskipun orientasinya diputar.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut. Bangun 5
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat sudut siku-siku pada bangun datar, terlepas dari orientasi atau posisi bangun tersebut.. Bukti: Temukan banyaknya sudut siku-siku
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya meminta identifikasi sifat dasar bangun datar. Meskipun bangun diputar, ini adalah variasi rutin untuk menguji pemahaman konsep sudut siku-siku yang sebenarnya, bukan sekadar pengenalan visual berdasarkan orientasi.. Bukti: Bangun 5; Temukan banyaknya sudut siku-siku

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku dan bentuk persegi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi sudut siku-siku pada bangun datar adalah materi dasar yang sudah dikuasai. Tantangan kecil berupa rotasi bangun masih dalam batas kemampuan rutin siswa. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 104/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.018743; applying=0.981257; reasoning=0.000000 | applying | 0.981257 | 0.084749 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.076950; conceptual=0.904913; procedural=0.018137; metacognitive=0.000000 | conceptual | 0.904913 | 0.260037 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.848011; Medium=0.148653; Hard=0.003336 | Easy | 0.848011 | 0.402493 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.981257; −Σp ln(p) = 0.093106; H = 0.093106/ln(3) = 0.084749; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.904913; −Σp ln(p) = 0.360488; H = 0.360488/ln(4) = 0.260037; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.848011; −Σp ln(p) = 0.442184; H = 0.442184/ln(3) = 0.402493; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Sudut Siku-Siku
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bangun datar berikut. Temukan banyaknya sudut siku-siku pada setiap bangun berikut.

Bangun 5
Pilihan: A. 0
B. 4
C. 3
D. 2
Transkripsi visual: Terdapat enam bangun datar yang diberi nomor 1 sampai 6. Bangun nomor 5 adalah sebuah persegi yang diputar 45 derajat, memiliki empat sisi yang sama panjang dan empat sudut yang semuanya merupakan sudut siku-siku.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `ff6d8a6a3950529913ba071e`

Perhatikan bangun datar berikut. Temukan banyaknya sudut siku-siku pada setiap bangun berikut.<br><br>Bangun 1

| Opsi | Isi |
|---|---|
| A | 0 |
| B | 4 |
| C | 2 |
| D | 3 |

![Gambar sumber soal 48](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0185-09.png>)


Kunci sumber: `B`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal tidak dapat dijawab dengan pasti karena instruksi meminta jumlah sudut untuk 'setiap bangun' namun pilihan jawaban hanya satu angka. Jika hanya untuk bangun 1 (persegi panjang), jawabannya adalah 4.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0185-09.png. Transkripsi visual: Terdapat tiga bangun datar. Bangun 1 adalah persegi panjang. Bangun 2 adalah trapesium siku-siku (memiliki dua sudut siku-siku di bagian bawah). Bangun 3 adalah belah ketupat (tidak memiliki sudut siku-siku).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e8cf5ffe545c8a3b3a73bc73adbbb2f75937ed72e4be18446bbb32a77d5d31b3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | knowing | conceptual | Easy | 3422 |
| 2 | success | concern / conflict | knowing | factual | Easy | 3532 |
| 3 | success | concern / conflict | knowing | conceptual | Easy | 3462 |

Run 1 — solusi: Bangun pertama adalah persegi panjang yang memiliki 4 sudut siku-siku. Namun, soal tidak memberikan opsi jawaban untuk bangun kedua dan ketiga, sehingga soal tidak lengkap.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung sudut siku-siku pada bangun datar yang diberikan. Ini adalah tugas pengenalan sifat geometri dasar.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi sudut siku-siku (konsep) dan menerapkannya untuk mengidentifikasi sudut tersebut pada bangun datar (prosedural).. Bukti: Temukan banyaknya sudut siku-siku
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar bagi siswa kelas 5. Mengidentifikasi sudut siku-siku pada persegi panjang adalah prosedur rutin yang familiar.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku dan bentuk bangun datar sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi sudut siku-siku pada bangun datar sederhana adalah materi yang sudah dikuasai sejak kelas rendah, sehingga bagi kelas 5 ini adalah tugas yang sangat mudah. |

Run 2 — solusi: Bangun pertama (persegi panjang) memiliki 4 sudut siku-siku. Bangun kedua (trapesium) memiliki 2 sudut siku-siku di bagian bawah. Bangun ketiga (belah ketupat) memiliki 0 sudut siku-siku. Soal tidak menyediakan format jawaban yang mengakomodasi ketiga bangun tersebut.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung sudut siku-siku pada bangun datar yang diberikan. Ini adalah prosedur langsung untuk mengenali properti sudut pada bentuk geometris dasar.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang definisi dan pengenalan visual sudut siku-siku sebagai elemen dasar geometri.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar bagi siswa kelas 5. Mengidentifikasi sudut siku-siku pada bangun datar sederhana adalah keterampilan rutin. Namun, karena soal tidak terstruktur dengan baik (instruksi jamak vs pilihan tunggal), tingkat kesulitan teknis menjadi tidak relevan.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku dan bentuk bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Mengidentifikasi sudut siku-siku pada bangun datar adalah materi yang sudah dikuasai sejak kelas rendah/awal kelas 4. |

Run 3 — solusi: Bangun 1 (persegi panjang) memiliki 4 sudut siku-siku. Bangun 2 (trapesium) memiliki 2 sudut siku-siku di bagian bawah. Bangun 3 (belah ketupat) memiliki 0 sudut siku-siku. Soal tidak memberikan format jawaban yang mengakomodasi ketiga bangun tersebut.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung sudut siku-siku pada bangun datar yang diberikan. Ini adalah tugas pengenalan sifat geometri dasar.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi sudut siku-siku (konsep) dan menerapkannya pada bentuk-bentuk geometri yang diberikan.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar bagi siswa kelas 5. Mengidentifikasi sudut siku-siku pada persegi panjang adalah prosedur yang sangat familiar dan rutin.. Bukti: Temukan banyaknya sudut siku-siku pada setiap bangun berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku dan bentuk bangun datar sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Mengenali sudut siku-siku pada bangun datar adalah materi dasar geometri yang sudah dipelajari jauh sebelum kelas 5. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5922`.
Konten: `concern`; kunci: `conflict`; masalah: Soal meminta mencari banyaknya sudut siku-siku pada 'setiap bangun', namun pilihan jawaban hanya menyediakan satu angka, yang mengindikasikan ketidaksesuaian antara instruksi dan format soal.; Instruksi soal ambigu karena menggunakan kata 'setiap bangun' tetapi hanya menyediakan satu set pilihan jawaban yang kemungkinan besar hanya ditujukan untuk bangun pertama..
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi dan menghitung sudut siku-siku pada bangun datar. Ini adalah tugas pengenalan sifat geometri dasar.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami definisi sudut siku-siku (konsep) dan menerapkannya untuk mengidentifikasi sudut tersebut pada bangun datar.
- Intended difficulty `Easy`: Tugas mengidentifikasi sudut siku-siku pada bangun datar sederhana adalah prosedur rutin yang sangat familiar bagi siswa kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku dan bentuk bangun datar sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi sudut siku-siku pada bangun datar sederhana adalah materi yang sudah dikuasai sejak kelas rendah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 110/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Sudut Siku-Siku
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bangun datar berikut. Temukan banyaknya sudut siku-siku pada setiap bangun berikut.

Bangun 1
Pilihan: A. 0
B. 4
C. 2
D. 3
Transkripsi visual: Terdapat tiga bangun datar. Bangun 1 adalah persegi panjang. Bangun 2 adalah trapesium siku-siku (memiliki dua sudut siku-siku di bagian bawah). Bangun 3 adalah belah ketupat (tidak memiliki sudut siku-siku).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal meminta mencari banyaknya sudut siku-siku pada 'setiap bangun', namun pilihan jawaban hanya menyediakan satu angka, yang mengindikasikan ketidaksesuaian antara instruksi dan format soal.; Instruksi soal ambigu karena menggunakan kata 'setiap bangun' tetapi hanya menyediakan satu set pilihan jawaban yang kemungkinan besar hanya ditujukan untuk bangun pertama..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `fd335c551b48bcf09d6a8482`

Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.

| Opsi | Isi |
|---|---|
| A | Tumpul |
| B | Lurus |
| C | Siku-siku |
| D | Lancip |

![Gambar sumber soal 49](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0188-07.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pada pukul 08.00, jarum panjang di angka 12 dan jarum pendek di angka 8. Sudut yang terbentuk mencakup 4 bagian jam (dari 8 ke 12). Karena 1 bagian jam adalah 30 derajat (360/12), maka sudutnya adalah 4 x 30 = 120 derajat. Sudut 120 derajat lebih besar dari 90 derajat (siku-siku) dan kurang dari 180 derajat (lurus), sehingga dikategorikan sebagai sudut tumpul.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0188-07.png. Transkripsi visual: Gambar menunjukkan jam analog dengan jarum panjang menunjuk ke angka 12 dan jarum pendek menunjuk ke angka 8. Terdapat busur merah yang menghubungkan kedua jarum tersebut, menunjukkan sudut yang terbentuk di bagian dalam (sudut tumpul).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2dcf2bba5757129f5f40dc58d2fc9977147817ba325b1d7ae1eade593aadbc17`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3484 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3516 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3440 |

Run 1 — solusi: Pada pukul 08.00, jarum panjang di angka 12 dan jarum pendek di angka 8. Sudut yang terbentuk mencakup 4 bagian jam (dari 8 ke 12). Karena 1 bagian jam adalah 30 derajat (360/12), maka sudutnya adalah 4 x 30 = 120 derajat. Sudut 120 derajat lebih besar dari 90 derajat (siku-siku) dan kurang dari 180 derajat (lurus), sehingga dikategorikan sebagai sudut tumpul.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi jenis sudut berdasarkan posisi jarum jam. Ini adalah penerapan konsep dasar sudut (tumpul, siku-siku, lancip) pada konteks yang familiar (jam analog).. Bukti: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang klasifikasi sudut berdasarkan besarannya (tumpul vs siku-siku vs lancip) dalam konteks visual.. Bukti: Sudut apakah yang terbentuk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengenali visual sudut tumpul yang jelas pada jam analog. Tidak diperlukan perhitungan derajat yang rumit, cukup pemahaman visual dasar tentang sudut yang lebih besar dari siku-siku.. Bukti: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (lancip, siku-siku, tumpul) dan cara membaca jam analog. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, mengidentifikasi jenis sudut pada jam analog adalah materi standar yang rutin dan tidak memerlukan perencanaan kompleks. |

Run 2 — solusi: Pada pukul 08.00, jarum panjang menunjuk ke angka 12 dan jarum pendek ke angka 8. Sudut yang terbentuk mencakup 4 bagian (dari 8 ke 12). Karena satu bagian jam adalah 30 derajat (360/12), maka sudutnya adalah 4 x 30 = 120 derajat. Sudut 120 derajat lebih besar dari 90 derajat (siku-siku) dan kurang dari 180 derajat (lurus), sehingga diklasifikasikan sebagai sudut tumpul.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi jenis sudut berdasarkan representasi visual jam. Ini adalah penerapan konsep klasifikasi sudut (lancip, siku-siku, tumpul) pada konteks yang familiar (jam analog). Tidak diperlukan strategi nonrutin atau integrasi kompleks.. Bukti: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi jenis-jenis sudut (tumpul, siku-siku, lancip) dan bagaimana menerapkannya pada objek nyata (jam).. Bukti: Sudut apakah yang terbentuk; pukul 08.00
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengenali visual sudut yang lebih besar dari siku-siku. Tidak ada perhitungan rumit atau kendala yang berinteraksi.. Bukti: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis sudut (lancip, siku-siku, tumpul) dan cara membaca jam analog. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari klasifikasi sudut dan jam analog sebagai alat bantu visual yang umum. Soal ini bersifat langsung tanpa memerlukan langkah perencanaan yang panjang. |

Run 3 — solusi: Pada pukul 08.00, jarum panjang berada di angka 12 dan jarum pendek di angka 8. Sudut yang terbentuk mencakup 4 bagian jam (dari 12 ke 8). Karena 90 derajat adalah 3 bagian jam, maka sudut ini lebih besar dari 90 derajat tetapi kurang dari 180 derajat, sehingga dikategorikan sebagai sudut tumpul.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi jenis sudut berdasarkan representasi visual jam. Ini adalah penerapan konsep dasar klasifikasi sudut (lancip, siku-siku, tumpul) pada konteks yang familiar.. Bukti: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi sudut tumpul dibandingkan dengan sudut siku-siku dan lancip.. Bukti: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengenali visual sudut tumpul yang jelas pada jam analog. Tidak ada perhitungan kompleks atau perencanaan strategi yang diperlukan.. Bukti: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (lancip, siku-siku, tumpul) dan cara membaca jam analog. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari klasifikasi sudut. Soal ini merupakan penerapan langsung dari konsep tersebut pada objek sehari-hari (jam). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 105/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.333573; applying=0.666427; reasoning=0.000000 | applying | 0.666427 | 0.579531 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.308218; conceptual=0.678349; procedural=0.013433; metacognitive=0.000000 | conceptual | 0.678349 | 0.493341 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.872183; Medium=0.124842; Hard=0.002976 | Easy | 0.872183 | 0.360770 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.666427; −Σp ln(p) = 0.636680; H = 0.636680/ln(3) = 0.579531; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.678349; −Σp ln(p) = 0.683916; H = 0.683916/ln(4) = 0.493341; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.872183; −Σp ln(p) = 0.396346; H = 0.396346/ln(3) = 0.360770; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Pengertian Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Sudut apakah yang terbentuk oleh jarum pendek dan panjang saat jam menunjukkan pukul 08.00.
Pilihan: A. Tumpul
B. Lurus
C. Siku-siku
D. Lancip
Transkripsi visual: Gambar menunjukkan jam analog dengan jarum panjang menunjuk ke angka 12 dan jarum pendek menunjuk ke angka 8. Terdapat busur merah yang menghubungkan kedua jarum tersebut, menunjukkan sudut yang terbentuk di bagian dalam (sudut tumpul).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 50. Soal `2b5db81c155e3ca6e5058b47`

Apa jenis sudut pada pojokan jendela.

| Opsi | Isi |
|---|---|
| A | Siku-siku |
| B | Lancip |
| C | Lurus |
| D | Tumpul |

![Gambar sumber soal 50](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0189-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jendela berbentuk persegi panjang. Sudut pada pojok persegi panjang adalah sudut siku-siku (90 derajat).
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0189-01.png. Transkripsi visual: Gambar menunjukkan tabel dengan beberapa baris. Baris terakhir (f) menampilkan gambar jendela persegi panjang dengan tanda sudut siku-siku yang jelas di setiap pojoknya. Teks di samping gambar berbunyi 'Sudut pada pojokan jendela.' dengan pilihan jawaban: Lancip, Siku-siku, Tumpul.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `321ce5f5256679e270b52a2947c970249db41c3eeeb9ad3056936047750487c6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3313 |
| 2 | success | valid / verified | knowing | factual | Easy | 3312 |
| 3 | success | valid / verified | knowing | factual | Easy | 3324 |

Run 1 — solusi: Jendela berbentuk persegi panjang. Sudut pada persegi panjang adalah sudut siku-siku (90 derajat).
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali karakteristik sudut pada bentuk geometris yang umum (persegi panjang) dan mengklasifikasikannya ke dalam kategori sudut yang sudah dipelajari.. Bukti: Apa jenis sudut pada pojokan jendela.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan klasifikasi jenis sudut (faktual/konseptual) pada objek nyata.. Bukti: Apa jenis sudut pada pojokan jendela.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, mengenali properti sudut pada bentuk yang sangat familiar (jendela persegi panjang). Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Apa jenis sudut pada pojokan jendela.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (siku-siku, lancip, tumpul). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Mengenali sudut siku-siku pada benda di sekitar adalah materi dasar kelas 4/5 yang sangat rutin. |

Run 2 — solusi: Pojok jendela berbentuk persegi panjang, yang secara definisi memiliki sudut siku-siku (90 derajat).
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi jenis sudut berdasarkan pengamatan visual pada objek geometris yang familiar (jendela). Ini adalah tugas pengenalan langsung.. Bukti: Apa jenis sudut pada pojokan jendela.
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang istilah dan definisi dasar jenis-jenis sudut (siku-siku, lancip, tumpul).. Bukti: Apa jenis sudut pada pojokan jendela.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengenali bentuk sudut siku-siku pada objek nyata yang umum. Tidak ada langkah perhitungan atau perencanaan yang diperlukan.. Bukti: Apa jenis sudut pada pojokan jendela.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (siku-siku, lancip, tumpul). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pengenalan sudut siku-siku pada benda di sekitar adalah materi dasar kelas 4/5 yang bersifat rutin dan langsung. |

Run 3 — solusi: Pojok jendela berbentuk persegi panjang, yang secara definisi memiliki sudut siku-siku (90 derajat).
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi jenis sudut berdasarkan pengamatan visual objek geometris yang umum (jendela persegi panjang). Ini adalah tugas pengenalan langsung.. Bukti: Apa jenis sudut pada pojokan jendela.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang definisi dan klasifikasi jenis-jenis sudut (siku-siku, lancip, tumpul) pada objek nyata.. Bukti: Apa jenis sudut pada pojokan jendela.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengenali bentuk sudut siku-siku pada objek sehari-hari yang familiar. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Apa jenis sudut pada pojokan jendela.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (siku-siku, lancip, tumpul). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pengenalan sudut siku-siku pada benda konkret adalah materi dasar kelas 4-5. Soal ini tidak menuntut analisis kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4552`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali karakteristik sudut pada bentuk geometris yang umum (persegi panjang) dan mengklasifikasikannya ke dalam kategori sudut yang sudah dipelajari. Ini adalah tugas pengenalan langsung.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual tentang definisi dan klasifikasi jenis-jenis sudut (siku-siku, lancip, tumpul) pada objek nyata.
- Intended difficulty `Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengenali bentuk sudut siku-siku pada objek sehari-hari yang familiar. Tidak ada langkah perencanaan atau integrasi yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (siku-siku, lancip, tumpul). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pengenalan sudut siku-siku pada benda konkret adalah materi dasar kelas 4-5. Soal ini tidak menuntut analisis kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.111913; applying=0.888087; reasoning=0.000000 | applying | 0.888087 | 0.319036 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.044344; conceptual=0.945000; procedural=0.010656; metacognitive=0.000000 | conceptual | 0.945000 | 0.173138 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.858224; Medium=0.138427; Hard=0.003349 | Easy | 0.858224 | 0.385967 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.888087; −Σp ln(p) = 0.350496; H = 0.350496/ln(3) = 0.319036; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.945000; −Σp ln(p) = 0.240020; H = 0.240020/ln(4) = 0.173138; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.858224; −Σp ln(p) = 0.424028; H = 0.424028/ln(3) = 0.385967; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Pengertian Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa jenis sudut pada pojokan jendela.
Pilihan: A. Siku-siku
B. Lancip
C. Lurus
D. Tumpul
Transkripsi visual: Gambar menunjukkan tabel dengan beberapa baris. Baris terakhir (f) menampilkan gambar jendela persegi panjang dengan tanda sudut siku-siku yang jelas di setiap pojoknya. Teks di samping gambar berbunyi 'Sudut pada pojokan jendela.' dengan pilihan jawaban: Lancip, Siku-siku, Tumpul.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 51. Soal `08c456eda435cd6d336fd7d0`

Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang pada gambar berikut.<br><br>d. Pukul ....<br>Besar sudut adalah ... $^\circ$

| Opsi | Isi |
|---|---|
| A | Pukul 01.30, $150^\circ$ |
| B | Pukul 01.30, $225^\circ$ |
| C | Pukul 02.30, $105^\circ$ |
| D | Pukul 01.30, $135^\circ$ |

![Gambar sumber soal 51](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0198-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `Pukul 01.30, 135 derajat`.
Solusi minimum hasil AI: Satu putaran penuh jam adalah 360 derajat, sehingga setiap angka mewakili 30 derajat (360/12). Pukul 01.30 berarti jarum panjang di angka 6 (180 derajat dari angka 12). Jarum pendek bergerak dari angka 1 ke arah 2 sebanyak setengah perjalanan (30 derajat / 2 = 15 derajat dari angka 1). Posisi jarum pendek adalah 30 + 15 = 45 derajat dari angka 12. Sudut antara jarum panjang (180 derajat) dan jarum pendek (45 derajat) adalah 180 - 45 = 135 derajat.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0198-04.png. Transkripsi visual: Gambar d menunjukkan jam analog dengan jarum pendek berada di antara angka 1 dan 2 (tepat di tengah), dan jarum panjang berada tepat di angka 6. Sudut yang ditandai adalah sudut terkecil antara kedua jarum tersebut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `392d737b59adac96c30df86bd4b8816472deb54d11e4bf3baf592b7ddb7e911a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3665 |
| 2 | success | valid / verified | applying | procedural | Medium | 3804 |
| 3 | success | valid / verified | applying | procedural | Medium | 3655 |

Run 1 — solusi: Satu putaran penuh jam adalah 360 derajat, sehingga setiap angka mewakili 30 derajat (360/12). Pukul 01.30 berarti jarum panjang di angka 6 (180 derajat dari angka 12). Jarum pendek bergerak dari angka 1 ke arah 2 sebanyak setengah perjalanan (30 derajat / 2 = 15 derajat dari angka 1). Posisi jarum pendek adalah 30 + 15 = 45 derajat dari angka 12. Sudut antara jarum panjang (180 derajat) dan jarum pendek (45 derajat) adalah 180 - 45 = 135 derajat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep sudut pada jam analog, memahami pergerakan jarum pendek, dan melakukan perhitungan sudut. Ini melibatkan penerapan prosedur pada konteks rutin.. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang pada gambar berikut.; Pukul 01.30, 135 derajat
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau metode untuk menghitung sudut berdasarkan posisi jarum jam, yang merupakan prosedur standar dalam topik geometri sudut.. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman bahwa jarum pendek tidak diam di angka 1 pada pukul 01.30, melainkan bergeser. Ini adalah langkah tambahan yang krusial dibandingkan soal jam sederhana (misal pukul 03.00).. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang pada gambar berikut.; Pukul 01.30

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sudut (lingkaran = 360 derajat), pembagian jam menjadi 12 bagian, dan konsep pergerakan jarum jam. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengukur sudut dan memahami konsep jam. Kesulitan menengah muncul karena siswa harus memperhitungkan pergeseran jarum pendek, bukan sekadar membaca posisi angka bulat. |

Run 2 — solusi: Satu putaran penuh jam adalah 360 derajat, tiap angka mewakili 30 derajat. Pukul 01.30: jarum panjang di angka 6 (180 derajat dari angka 12). Jarum pendek di antara 1 dan 2. Posisi jarum pendek = (1 x 30) + (30/60 x 30) = 30 + 15 = 45 derajat dari angka 12. Sudut terkecil = 180 - 45 = 135 derajat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep sudut pada jam (360 derajat per putaran, 30 derajat per angka) dan melakukan perhitungan untuk menentukan posisi jarum yang tidak tepat di angka, kemudian menghitung selisih sudutnya. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang pada gambar berikut.; Pukul 01.30: jarum pendek di 45 derajat, jarum panjang di 180 derajat; 180 - 45 = 135 derajat
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode atau algoritma untuk menghitung besar sudut berdasarkan posisi jarum jam yang diketahui.. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah saling terkait: menentukan posisi jarum panjang, menentukan posisi jarum pendek yang bergeser (memerlukan pemahaman pecahan/proporsi waktu), dan menghitung selisih sudut. Ini melampaui sekadar membaca sudut yang tepat di angka.. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang; Pukul 01.30

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jam analog, konsep sudut 360 derajat, dan pembagian sudut per angka (30 derajat). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengukur sudut dan memahami hubungan waktu dengan posisi jarum jam. Menghitung pergeseran jarum pendek (setengah jam = setengah jarak antar angka) adalah tantangan standar untuk tingkat ini. |

Run 3 — solusi: Satu putaran penuh jam adalah 360 derajat, sehingga tiap angka mewakili 30 derajat (360/12). Pukul 01.30 berarti jarum panjang di angka 6 (180 derajat dari angka 12) dan jarum pendek di antara 1 dan 2. Posisi jarum pendek adalah 1 * 30 + 0.5 * 30 = 45 derajat dari angka 12. Sudut terkecil = 180 - 45 = 135 derajat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep sudut pada jam (30 derajat per angka) dan melakukan perhitungan untuk menentukan posisi jarum yang tidak tepat di angka, kemudian menghitung selisih sudutnya. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang pada gambar berikut.; jarum panjang menunjuk tepat ke angka 6 dan jarum pendek berada di antara angka 1 dan 2
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau metode untuk menghitung sudut berdasarkan posisi jarum jam (konsep sudut pada lingkaran jam).. Bukti: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman bahwa jarum pendek bergerak (tidak statis di angka) dan melibatkan perhitungan posisi jarum yang berada di antara angka. Siswa harus mengintegrasikan dua langkah: menentukan posisi jarum pendek dalam derajat dan menghitung selisihnya dengan posisi jarum panjang.. Bukti: jarum pendek berada di antara angka 1 dan 2, tepat di tengah-tengah; Ukurlah sudut terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sudut satu putaran penuh (360 derajat) dan pembagiannya pada jam analog (30 derajat per jam). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menghitung sudut jarum jam yang tidak tepat di angka memerlukan ketelitian lebih tinggi daripada sekadar membaca sudut jam tepat (misal pukul 03.00), sehingga tingkat kesulitannya menengah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 162/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.005765; applying=0.994235; reasoning=0.000000 | applying | 0.994235 | 0.032287 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000538; conceptual=0.995986; procedural=0.003475; metacognitive=0.000000 | conceptual | 0.995986 | 0.020007 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.572422; Medium=0.422073; Hard=0.005505 | Easy | 0.572422 | 0.648135 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.994235; −Σp ln(p) = 0.035470; H = 0.035470/ln(3) = 0.032287; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.995986; −Σp ln(p) = 0.027735; H = 0.027735/ln(4) = 0.020007; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.572422; −Σp ln(p) = 0.712049; H = 0.712049/ln(3) = 0.648135; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Mengukur dan Membandingkan Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Ukurlah sudut terkecil yang dibentuk oleh jarum jam pendek dan panjang pada gambar berikut.

d. Pukul ....
Besar sudut adalah ... $^\circ$
Pilihan: A. Pukul 01.30, $150^\circ$
B. Pukul 01.30, $225^\circ$
C. Pukul 02.30, $105^\circ$
D. Pukul 01.30, $135^\circ$
Transkripsi visual: Gambar d menunjukkan jam analog dengan jarum pendek berada di antara angka 1 dan 2 (tepat di tengah), dan jarum panjang berada tepat di angka 6. Sudut yang ditandai adalah sudut terkecil antara kedua jarum tersebut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `needs_ai_review`.
Status konten: `valid`. Catatan konten: Soal meminta pengukuran sudut pada gambar 'd', namun gambar 'd' menunjukkan jarum panjang di angka 6 dan jarum pendek di antara angka 1 dan 2 (pukul 01.30). Kunci jawaban D menyatakan 135 derajat. Perhitungan: jarum panjang di 180 derajat (angka 6). Jarum pendek bergerak dari angka 1 (30 derajat) sebanyak 15 derajat (setengah dari 30 derajat untuk 30 menit), total 45 derajat. Sudut = 180 - 45 = 135 derajat. Soal valid secara matematis..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 52. Soal `7ee9b555983c0c876d5f3e5c`

Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00

| Opsi | Isi |
|---|---|
| A | $210^\circ$ |
| B | $120^\circ$ |
| C | $150^\circ$ |
| D | $70^\circ$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Pada pukul 07.00, jarum panjang menunjuk angka 12 dan jarum pendek menunjuk angka 7. Jarak terpendek antara angka 12 dan 7 adalah 5 satuan jam. Karena satu putaran penuh (360 derajat) dibagi 12 angka, maka setiap satuan jam bernilai 30 derajat. Sudut terkecil = 5 x 30 derajat = 150 derajat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cfef8b2ab925d5e9615bec87897f659641d2ca8f591897c6bdbf7f2ca01d686e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2440 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2367 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2412 |

Run 1 — solusi: Pada pukul 07.00, jarum panjang menunjuk angka 12 dan jarum pendek menunjuk angka 7. Jarak antara angka 12 ke 7 melalui angka 6, 5, 4, 3, 2, 1 adalah 5 satuan jam (arah berlawanan jarum jam). Karena satu putaran penuh 360 derajat dibagi 12 angka, maka setiap angka bernilai 30 derajat. Sudut terkecil = 5 x 30 derajat = 150 derajat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep sudut pada jam (satu putaran 360 derajat dibagi 12 angka = 30 derajat per angka) untuk menghitung sudut terkecil antara dua jarum jam pada posisi spesifik. Ini adalah penerapan prosedur rutin pada konteks geometri jam.. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang cara menghitung sudut pada jam (mengalikan jumlah selisih angka dengan 30 derajat) untuk menyelesaikan masalah.. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari konsep sudut jam yang familiar bagi siswa kelas 5. Jalur penyelesaiannya jelas (menghitung selisih angka lalu dikali 30 derajat), tidak ada kendala yang berinteraksi, dan beban kalkulasinya rendah.. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang lingkaran, pembagian 360 derajat, dan konsep jam analog. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi sudut pada jam adalah topik standar kelas 5. Soal ini tidak memerlukan penalaran kompleks atau langkah-langkah yang saling bergantung, sehingga cukup mudah bagi siswa pada level ini. |

Run 2 — solusi: Pada pukul 07.00, jarum panjang menunjuk angka 12 dan jarum pendek menunjuk angka 7. Selisih angka adalah 5 unit. Karena satu putaran penuh (360 derajat) dibagi 12 angka, maka setiap satu angka bernilai 30 derajat. Sudut terkecil = 5 x 30 derajat = 150 derajat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pengukuran sudut pada jam (konsep 360 derajat dibagi 12 angka) untuk menentukan besar sudut. Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks rutin.. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara posisi jarum jam dan besar sudut (konseptual) serta penggunaan metode perhitungan sudut (prosedural).. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus memahami representasi jam sebagai lingkaran 360 derajat dan melakukan perhitungan langkah demi langkah (menentukan selisih angka, mengalikan dengan 30 derajat).. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang lingkaran, pembagian 360 derajat, dan membaca jam. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu memahami konsep sudut pada jam. Soal memerlukan dua langkah logis: menentukan selisih angka dan mengonversinya ke derajat, yang merupakan tuntutan sedang. |

Run 3 — solusi: Pada pukul 07.00, jarum panjang menunjuk angka 12 dan jarum pendek menunjuk angka 7. Jarak antara angka 12 ke 7 melalui angka 6, 5, 4, 3, 2, 1 adalah 5 satuan jam (arah berlawanan jarum jam). Setiap satuan jam bernilai 360 derajat / 12 = 30 derajat. Sudut terkecil = 5 x 30 derajat = 150 derajat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep sudut pada jam (setiap jam bernilai 30 derajat) dan memilih jalur terpendek antara dua jarum jam. Ini adalah penerapan prosedur rutin pada konteks jam.. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip hubungan antara posisi jarum jam dan besar sudut (konseptual) serta melakukan perhitungan perkalian sederhana (prosedural).. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus memahami bahwa satu putaran penuh adalah 360 derajat, membaginya menjadi 12 bagian (30 derajat per jam), dan menentukan jarak terpendek antara angka 7 dan 12. Meskipun prosedurnya rutin, siswa perlu melakukan integrasi konsep sudut dan representasi jam.. Bukti: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut, lingkaran, dan pembagian jam menjadi 12 bagian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari sudut dan jam. Menentukan sudut pada jam adalah aplikasi standar yang memerlukan pemahaman hubungan antara angka pada jam dan derajat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4227`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur rutin (menghitung selisih angka dan mengalikannya dengan 30 derajat) untuk menyelesaikan masalah sudut pada jam. Ini adalah penerapan konsep geometri dasar dalam konteks yang sudah dikenal.
- Dimensi pengetahuan `procedural`: Siswa menggunakan pengetahuan prosedural tentang cara menghitung sudut pada jam (mengalikan jumlah selisih angka dengan 30 derajat) yang didasarkan pada pemahaman konseptual tentang lingkaran 360 derajat.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari prosedur yang familiar bagi siswa kelas 5. Jalur penyelesaiannya sangat jelas (menghitung selisih angka lalu dikali 30 derajat), tidak ada kendala yang berinteraksi, dan beban kalkulasinya rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang lingkaran, pembagian 360 derajat, dan konsep jam analog. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi sudut pada jam adalah topik standar kelas 5. Soal ini tidak memerlukan penalaran kompleks atau langkah-langkah yang saling bergantung, sehingga cukup mudah bagi siswa pada level ini. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.085369; applying=0.914631; reasoning=0.000000 | applying | 0.914631 | 0.265508 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.033330; conceptual=0.941817; procedural=0.024854; metacognitive=0.000000 | conceptual | 0.941817 | 0.188740 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.832381; Medium=0.165261; Hard=0.002358 | Easy | 0.832381 | 0.422793 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.914631; −Σp ln(p) = 0.291690; H = 0.291690/ln(3) = 0.265508; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.941817; −Σp ln(p) = 0.261649; H = 0.261649/ln(4) = 0.188740; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.832381; −Σp ln(p) = 0.464486; H = 0.464486/ln(3) = 0.422793; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Mengukur dan Membandingkan Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan besar sudut terkecil yang dibentuk oleh jarum pendek dan jarum panjang pada jam saat menunjukkan pukul 07.00
Pilihan: A. $210^\circ$
B. $120^\circ$
C. $150^\circ$
D. $70^\circ$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 53. Soal `aacaa86c1fc9990161672c5c`

Memasang Keramik<br><br>Seorang tukang keramik memasang keramik dengan menggunakan pola berikut.<br><br>Pak Tukang akan memotong keramik untuk mengisi bagian kosong yang diberi tanda panah. Bantulah Pak Tukang untuk membuat potongan yang tepat. Berapa besar sudut potongan keramik untuk Pola 1? (Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.)

| Opsi | Isi |
|---|---|
| A | $36^\circ$ |
| B | $144^\circ$ |
| C | $72^\circ$ |
| D | $54^\circ$ |

![Gambar sumber soal 53](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Sudut dalam segi lima beraturan adalah 108 derajat. Sudut persegi adalah 90 derajat. Pada titik pertemuan, sudut total adalah 360 derajat. Sudut celah = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png. Transkripsi visual: Terdapat dua pola keramik. Pola 1 menunjukkan sebuah persegi biru di tengah yang dikelilingi oleh empat segi lima beraturan merah. Terdapat celah di antara dua segi lima yang bersebelahan dan sudut persegi biru. Pola 2 menunjukkan dua segi lima beraturan yang bersentuhan, dengan celah di bawahnya. Soal menanyakan besar sudut potongan untuk mengisi celah pada Pola 1.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f314d45a91c15e8c33a9ad8c7bca934f68c7c0698cc82edb405c91df9182ae90`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 3634 |
| 2 | success | valid / verified | applying | conceptual | Hard | 3697 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 3619 |

Run 1 — solusi: Sudut dalam segi lima beraturan adalah 108 derajat. Sudut persegi adalah 90 derajat. Sudut satu putaran penuh adalah 360 derajat. Sudut celah = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan pengetahuan tentang sudut dalam bangun datar (segi lima dan persegi) dan konsep sudut satu putaran penuh (360 derajat) untuk memecahkan masalah geometri yang tidak rutin bagi mereka.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang sifat-sifat sudut pada bangun datar dan bagaimana mereka berinteraksi dalam sebuah pola (sudut di sekitar titik pusat).. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.; Berapa besar sudut potongan keramik untuk Pola 1?
- Intended difficulty `classify/Hard`: Soal ini menuntut siswa untuk mengidentifikasi hubungan sudut di sekitar titik pusat, menghitung sudut dalam segi lima (108 derajat), dan mengurangkannya dari 360 derajat. Ini melibatkan perencanaan langkah-langkah yang saling bergantung.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sudut dalam segi lima beraturan dan persegi, serta konsep sudut satu putaran penuh. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 5 jarang diminta untuk mengintegrasikan properti sudut bangun datar dalam pola mosaik seperti ini tanpa bantuan visual atau langkah terpandu. |

Run 2 — solusi: Sudut dalam segi lima beraturan adalah 108 derajat. Sudut persegi adalah 90 derajat. Sudut satu putaran penuh adalah 360 derajat. Sudut celah = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti sudut bangun datar (segi lima dan persegi) dan menerapkan konsep sudut satu putaran penuh (360 derajat) untuk menemukan sudut yang hilang. Ini melibatkan penerapan konsep geometri pada situasi yang diberikan.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar sudut dalam bangun datar (konseptual) dan penggunaan prosedur perhitungan sudut untuk menyelesaikan masalah.. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.; Berapa besar sudut potongan keramik untuk Pola 1?
- Intended difficulty `classify/Hard`: Soal ini memerlukan integrasi pengetahuan tentang sudut dalam poligon (segi lima dan persegi) dan sudut satu putaran penuh. Siswa harus merencanakan langkah: menentukan sudut segi lima (108), sudut persegi (90), dan mengurangkannya dari 360. Ini adalah tugas yang menuntut bagi kelas 5 karena melibatkan integrasi beberapa konsep geometri.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang sudut dalam segi lima beraturan (108 derajat) dan persegi (90 derajat), serta konsep sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 5 jarang diminta mengintegrasikan properti sudut poligon yang berbeda dalam satu titik pertemuan. Mengharuskan siswa mengingat/menghitung sudut segi lima dan mengintegrasikannya dengan sudut persegi dalam konteks 360 derajat adalah tuntutan yang cukup tinggi. |

Run 3 — solusi: Sudut dalam segi lima beraturan adalah 108 derajat. Sudut persegi adalah 90 derajat. Pada titik pertemuan, sudut total adalah 360 derajat. Sudut celah = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan pengetahuan tentang sudut dalam bangun datar (segi lima dan persegi) dan memahami hubungan sudut pada satu titik (360 derajat) untuk memecahkan masalah yang tidak rutin bagi mereka.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Siswa harus menerapkan prinsip geometri tentang jumlah sudut dalam bangun datar dan sudut satu putaran penuh untuk menyelesaikan masalah.. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Intended difficulty `classify/Hard`: Soal ini menuntut perencanaan langkah yang saling bergantung: menentukan sudut dalam segi lima, sudut persegi, dan mengintegrasikannya dengan konsep sudut satu putaran penuh (360 derajat). Siswa harus membangun sendiri hubungan antar bangun tersebut.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; 360 - 108 - 108 - 90 = 54 derajat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sudut dalam bangun datar (segi lima dan persegi) dan sudut satu putaran penuh. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 5 jarang diminta mengintegrasikan properti sudut dari dua bangun berbeda untuk mencari sudut celah pada pola kompleks tanpa bantuan visual eksplisit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 2, "applying": 1} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Hard": 3} | unanimous_3_0 / adjudicated | Hard |

Adjudikasi AI: `success`; token `5471`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus mengintegrasikan pengetahuan tentang besar sudut dalam bangun datar (segi lima dan persegi) dengan konsep sudut satu putaran penuh (360 derajat) untuk menentukan sudut yang tidak diketahui. Ini memerlukan penalaran geometris untuk menghubungkan properti bangun dengan konfigurasi titik pertemuan.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat sudut pada bangun datar (segi lima dan persegi) dan bagaimana sudut-sudut tersebut berinteraksi dalam sebuah pola mosaik di sekitar satu titik.
- Intended difficulty `Hard`: Soal ini menuntut perencanaan langkah yang saling bergantung: menentukan sudut dalam segi lima (108 derajat), sudut persegi (90 derajat), dan mengintegrasikannya dengan konsep sudut satu putaran penuh (360 derajat). Siswa harus membangun sendiri hubungan antar bangun tersebut tanpa bantuan langkah-langkah eksplisit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sudut dalam segi lima beraturan (108 derajat) dan persegi (90 derajat), serta konsep sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 5 jarang diminta untuk mengintegrasikan properti sudut dari dua bangun berbeda untuk mencari sudut celah pada pola kompleks tanpa bantuan visual eksplisit atau panduan langkah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 187/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000746; conceptual=0.989352; procedural=0.009903; metacognitive=0.000000 | conceptual | 0.989352 | 0.044480 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.655547; Medium=0.335846; Hard=0.008607 | Easy | 0.655547 | 0.622783 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.989352; −Σp ln(p) = 0.061662; H = 0.061662/ln(4) = 0.044480; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.655547; −Σp ln(p) = 0.684197; H = 0.684197/ln(3) = 0.622783; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Melukis Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Memasang Keramik

Seorang tukang keramik memasang keramik dengan menggunakan pola berikut.

Pak Tukang akan memotong keramik untuk mengisi bagian kosong yang diberi tanda panah. Bantulah Pak Tukang untuk membuat potongan yang tepat. Berapa besar sudut potongan keramik untuk Pola 1? (Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.)
Pilihan: A. $36^\circ$
B. $144^\circ$
C. $72^\circ$
D. $54^\circ$
Transkripsi visual: Terdapat dua pola keramik. Pola 1 menunjukkan sebuah persegi biru di tengah yang dikelilingi oleh empat segi lima beraturan merah. Terdapat celah di antara dua segi lima yang bersebelahan dan sudut persegi biru. Pola 2 menunjukkan dua segi lima beraturan yang bersentuhan, dengan celah di bawahnya. Soal menanyakan besar sudut potongan untuk mengisi celah pada Pola 1.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Hard", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 54. Soal `0340747e52966376a7c4bd21`

Memasang Keramik<br><br>Seorang tukang keramik memasang keramik dengan menggunakan pola berikut.<br><br>Pak Tukang akan memotong keramik untuk mengisi bagian kosong yang diberi tanda panah. Bantulah Pak Tukang untuk membuat potongan yang tepat. Berapa besar sudut potongan keramik untuk Pola 2? (Keramik merah berbentuk segi lima beraturan.)

| Opsi | Isi |
|---|---|
| A | $54^\circ$ |
| B | $36^\circ$ |
| C | $108^\circ$ |
| D | $72^\circ$ |

![Gambar sumber soal 54](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Pada Pola 2, tiga sudut segi lima bertemu di satu titik. Total sudut satu putaran penuh adalah 360 derajat. Maka, besar sudut celah adalah 360 - (3 x 108) = 360 - 324 = 36 derajat.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png. Transkripsi visual: Gambar menunjukkan dua pola keramik. Pola 1 terdiri dari empat segi lima beraturan yang mengelilingi satu persegi biru di tengah. Pola 2 terdiri dari tiga segi lima beraturan yang bertemu pada satu titik pusat, menyisakan celah kosong yang ditunjuk oleh tanda panah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b62050a5b296d15b0baba1cb795717aa178bafff003bcda413928d4f4c080dfb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 3678 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 3673 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 3638 |

Run 1 — solusi: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Pada Pola 2, tiga sudut segi lima bertemu di satu titik. Total sudut satu putaran penuh adalah 360 derajat. Maka, besar sudut celah adalah 360 - (3 x 108) = 360 - 324 = 36 derajat.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan pengetahuan tentang besar sudut dalam segi lima beraturan dan konsep sudut satu putaran penuh (360 derajat) untuk menentukan besar sudut celah. Ini melibatkan penalaran untuk menghubungkan geometri poligon dengan sudut pusat.. Bukti: Berapa besar sudut potongan keramik untuk Pola 2?; tiga sudut segi lima beraturan bertemu: 360 - 3 x 108 = 36 derajat
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang sifat sudut poligon beraturan dan hubungan sudut-sudut yang bertemu pada satu titik (sudut satu putaran).. Bukti: Keramik merah berbentuk segi lima beraturan; 360 - 3 x 108 = 36 derajat
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard untuk kelas 5 karena siswa harus membangun sendiri hubungan antara sudut dalam segi lima (108 derajat) dan sudut satu putaran (360 derajat) tanpa bantuan langkah-langkah eksplisit. Siswa harus menyadari bahwa tiga sudut segi lima bertemu di titik tersebut dan menghitung selisihnya. Ini memerlukan perencanaan langkah yang saling bergantung dan integrasi konsep geometri yang cukup kompleks bagi tingkat kelas 5.. Bukti: Berapa besar sudut potongan keramik untuk Pola 2?; tiga sudut segi lima beraturan bertemu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut dalam poligon beraturan dan sudut satu putaran. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, kemampuan untuk mengabstraksi situasi geometris menjadi perhitungan sudut memerlukan penalaran yang melampaui prosedur rutin standar kelas 5. |

Run 2 — solusi: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Pada Pola 2, tiga sudut segi lima bertemu pada satu titik. Total sudut satu putaran penuh adalah 360 derajat. Maka, besar sudut celah adalah 360 - (3 x 108) = 360 - 324 = 36 derajat.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan pengetahuan tentang besar sudut dalam segi lima beraturan dan konsep sudut satu putaran penuh (360 derajat) untuk menentukan besar sudut celah. Ini melibatkan penalaran untuk menghubungkan properti bangun datar dengan geometri sudut di sekitar titik pertemuan.. Bukti: Berapa besar sudut potongan keramik untuk Pola 2?; Keramik merah berbentuk segi lima beraturan.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang sifat sudut dalam poligon beraturan dan bagaimana sudut-sudut tersebut berinteraksi saat disusun (tessellation sederhana).. Bukti: Keramik merah berbentuk segi lima beraturan.; Berapa besar sudut potongan keramik untuk Pola 2?
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard untuk kelas 5 karena menuntut perencanaan langkah yang saling bergantung: menghitung sudut dalam segi lima (108 derajat), memahami bahwa tiga sudut bertemu di satu titik, dan mengurangkannya dari 360 derajat. Siswa harus membangun sendiri hubungan antar-sudut tanpa bantuan langkah-langkah eksplisit.. Bukti: Berapa besar sudut potongan keramik untuk Pola 2?; Keramik merah berbentuk segi lima beraturan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang besar sudut dalam poligon beraturan dan sudut satu putaran penuh. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 5 jarang diminta untuk melakukan deduksi sudut pada pola keramik yang kompleks secara mandiri tanpa panduan langkah demi langkah. |

Run 3 — solusi: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Pada Pola 2, tiga sudut segi lima bertemu pada satu titik. Total sudut satu putaran penuh adalah 360 derajat. Besar sudut celah adalah 360 - (3 x 108) = 360 - 324 = 36 derajat.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan pengetahuan tentang besar sudut dalam segi lima beraturan (konsep) dan menerapkan pemahaman sudut satu putaran penuh (360 derajat) untuk memecahkan masalah geometri yang tidak rutin bagi mereka.. Bukti: Berapa besar sudut potongan keramik untuk Pola 2?; Keramik merah berbentuk segi lima beraturan.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman hubungan antara sudut-sudut poligon yang bertemu pada satu titik dan prinsip sudut satu putaran penuh, yang merupakan pemahaman konseptual geometri.. Bukti: Keramik merah berbentuk segi lima beraturan.; Berapa besar sudut potongan keramik untuk Pola 2?
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard untuk kelas 5 karena siswa harus membangun sendiri strategi penyelesaian: menentukan sudut dalam segi lima (108 derajat), memahami bahwa tiga sudut bertemu di satu titik, dan mengurangkannya dari 360 derajat. Tidak ada langkah bantuan eksplisit.. Bukti: Berapa besar sudut potongan keramik untuk Pola 2?; Keramik merah berbentuk segi lima beraturan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sudut satu putaran penuh (360 derajat) dan cara menghitung besar sudut dalam poligon beraturan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 5 jarang diminta mengintegrasikan properti poligon dengan sudut satu putaran penuh untuk mencari sudut celah tanpa bantuan diagram atau langkah terpandu. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Hard": 3} | unanimous_3_0 / unanimous | Hard |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 165/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000844; conceptual=0.988839; procedural=0.010317; metacognitive=0.000000 | conceptual | 0.988839 | 0.046353 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.660495; Medium=0.333544; Hard=0.005962 | Easy | 0.660495 | 0.610509 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.988839; −Σp ln(p) = 0.064259; H = 0.064259/ln(4) = 0.046353; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.660495; −Σp ln(p) = 0.670713; H = 0.670713/ln(3) = 0.610509; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Melukis Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Memasang Keramik

Seorang tukang keramik memasang keramik dengan menggunakan pola berikut.

Pak Tukang akan memotong keramik untuk mengisi bagian kosong yang diberi tanda panah. Bantulah Pak Tukang untuk membuat potongan yang tepat. Berapa besar sudut potongan keramik untuk Pola 2? (Keramik merah berbentuk segi lima beraturan.)
Pilihan: A. $54^\circ$
B. $36^\circ$
C. $108^\circ$
D. $72^\circ$
Transkripsi visual: Gambar menunjukkan dua pola keramik. Pola 1 terdiri dari empat segi lima beraturan yang mengelilingi satu persegi biru di tengah. Pola 2 terdiri dari tiga segi lima beraturan yang bertemu pada satu titik pusat, menyisakan celah kosong yang ditunjuk oleh tanda panah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Hard", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 55. Soal `f311bf91df38724a90b35b69`

Perhatikan huruf-huruf berikut ini.<br><br>Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

| Opsi | Isi |
|---|---|
| A | Huruf E |
| B | Tidak ada |
| C | Huruf M |
| D | Huruf T |

![Gambar sumber soal 55](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Analisis geometri huruf: E memiliki 3 pasang garis sejajar (horizontal) dan 3 pasang garis tegak lurus. M memiliki 1 pasang garis sejajar (vertikal) dan 0 garis tegak lurus. T memiliki 0 pasang garis sejajar dan 1 pasang garis tegak lurus. Tidak ada huruf yang memenuhi syarat tepat 1 pasang garis sejajar dan 2 pasang garis tegak lurus. Jawaban: Tidak ada.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png. Transkripsi visual: Gambar menunjukkan kata 'MATEMATIKA' yang ditulis menggunakan garis lurus di atas kertas berpetak. Huruf-huruf tersebut adalah M, A, T, E, M, A, T, I, K, A. Huruf E memiliki tiga garis horizontal sejajar dan satu garis vertikal tegak lurus terhadap ketiganya. Huruf M memiliki dua garis miring yang tidak sejajar dan dua garis vertikal yang sejajar. Huruf T memiliki satu garis horizontal dan satu garis vertikal yang saling tegak lurus. Huruf A memiliki dua garis miring dan satu garis horizontal.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `664bf9c201292fbe705ad53fc05696d5f14d38aefb1e3681d52d52937762ae93`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3715 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3648 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3620 |

Run 1 — solusi: Analisis geometri huruf: E memiliki 3 pasang garis sejajar (horizontal) dan 3 pasang garis tegak lurus. M memiliki 1 pasang garis sejajar (vertikal) dan 0 garis tegak lurus. T memiliki 0 pasang garis sejajar dan 1 pasang garis tegak lurus. Tidak ada huruf yang memenuhi syarat tepat 1 pasang garis sejajar dan 2 pasang garis tegak lurus. Jawaban: Tidak ada.
- Domain kognitif `classify/applying`: Siswa diminta untuk menganalisis properti geometris (garis sejajar dan tegak lurus) dari bentuk huruf yang diberikan. Ini memerlukan penerapan konsep garis pada konteks visual yang familiar, sehingga masuk dalam domain applying.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; E memang punya garis sejajar dan tegak lurus, tetapi garis sejajarnya tiga; M punya sepasang garis sejajar tetapi tanpa tegak lurus; T punya tegak lurus tanpa sejajar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan geometris antara garis (sejajar dan tegak lurus) yang merupakan konsep dasar dalam geometri bidang.. Bukti: garis sejajar dan dua pasang garis tegak lurus
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa setiap huruf secara sistematis terhadap dua kriteria yang berinteraksi (jumlah pasangan garis sejajar dan tegak lurus). Meskipun konsepnya dasar, siswa harus melakukan verifikasi visual yang cermat untuk setiap pilihan, yang meningkatkan beban kognitif.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi garis sejajar dan tegak lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengidentifikasi sifat garis pada bentuk sederhana. Menuntut ketelitian dalam menghitung pasangan garis pada setiap huruf membuat soal ini berada di tingkat menengah. |

Run 2 — solusi: Analisis huruf: E memiliki 3 pasang garis sejajar (horizontal) dan 2 pasang garis tegak lurus (vertikal dengan horizontal). M memiliki 0 pasang garis sejajar dan 0 pasang garis tegak lurus (diagonal). T memiliki 0 pasang garis sejajar dan 1 pasang garis tegak lurus. Tidak ada huruf yang memenuhi syarat tepat 1 pasang sejajar dan 2 pasang tegak lurus.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan menghitung jumlah pasangan garis sejajar dan tegak lurus pada setiap huruf yang diberikan, yang merupakan penerapan konsep geometri dasar pada konteks visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi garis sejajar dan tegak lurus serta kemampuan untuk mengklasifikasikan properti geometris pada objek visual.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal menuntut siswa untuk memeriksa properti geometris setiap huruf secara sistematis. Meskipun prosedurnya familiar, siswa harus melakukan analisis pada beberapa objek (M, A, T, E) dan memverifikasi kondisi ganda (sejajar dan tegak lurus) secara bersamaan, yang memerlukan ketelitian.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi garis sejajar dan tegak lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengidentifikasi sifat garis pada bentuk geometris sederhana. Tingkat kesulitan Medium diberikan karena siswa harus mengevaluasi beberapa huruf dan kondisi secara simultan tanpa bantuan langkah-langkah. |

Run 3 — solusi: Analisis properti geometris huruf: E memiliki 3 garis sejajar dan 3 garis tegak lurus. M memiliki 1 pasang garis sejajar (vertikal) tetapi tidak ada garis tegak lurus. T memiliki 1 pasang garis tegak lurus tetapi tidak ada garis sejajar. Tidak ada huruf yang memiliki tepat 1 pasang garis sejajar dan 2 pasang garis tegak lurus.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan memverifikasi properti geometris (sejajar dan tegak lurus) pada setiap huruf yang diberikan, yang merupakan penerapan konsep pada konteks visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar garis (sejajar dan tegak lurus) dalam bentuk huruf.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa properti geometris dari beberapa objek (huruf) secara sistematis. Meskipun prosedurnya rutin, siswa harus melakukan analisis pada setiap pilihan jawaban untuk memverifikasi kondisi yang diberikan, yang memerlukan ketelitian.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengidentifikasi garis sejajar dan tegak lurus. Tugas ini memerlukan pemeriksaan sistematis terhadap setiap opsi, yang sedikit lebih kompleks daripada sekadar identifikasi satu objek. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 180/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000693; applying=0.999307; reasoning=0.000000 | applying | 0.999307 | 0.005222 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004915; conceptual=0.962207; procedural=0.032878; metacognitive=0.000000 | conceptual | 0.962207 | 0.126578 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.679566; Medium=0.314660; Hard=0.005774 | Easy | 0.679566 | 0.597214 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999307; −Σp ln(p) = 0.005738; H = 0.005738/ln(3) = 0.005222; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.962207; −Σp ln(p) = 0.175474; H = 0.175474/ln(4) = 0.126578; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.679566; −Σp ln(p) = 0.656107; H = 0.656107/ln(3) = 0.597214; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan huruf-huruf berikut ini.

Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
Pilihan: A. Huruf E
B. Tidak ada
C. Huruf M
D. Huruf T
Transkripsi visual: Gambar menunjukkan kata 'MATEMATIKA' yang ditulis menggunakan garis lurus di atas kertas berpetak. Huruf-huruf tersebut adalah M, A, T, E, M, A, T, I, K, A. Huruf E memiliki tiga garis horizontal sejajar dan satu garis vertikal tegak lurus terhadap ketiganya. Huruf M memiliki dua garis miring yang tidak sejajar dan dua garis vertikal yang sejajar. Huruf T memiliki satu garis horizontal dan satu garis vertikal yang saling tegak lurus. Huruf A memiliki dua garis miring dan satu garis horizontal.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 56. Soal `4182b10b0d1d91b16f5a2f4c`

Perhatikan tabel berikut.<br>\|No.\|Sedotan (cm) a\|b\|c\|Membentuk Segitiga?\|b+c\|a+c\|a+b\|<br>\|1\|5\|6\|7\|Bisa\|13\|12\|11\|<br>\|2\|4\|6\|6\|…\|…\|…\|…\|<br>\|3\|5\|4\|12\|…\|…\|…\|…\|<br>\|4\|10\|5\|15\|…\|…\|…\|…\|<br>\|5\|5\|12\|13\|…\|…\|…\|…\|<br><br>Perhatikan jumlah panjang sisi-sisinya di kolom sebelah kanan.<br><br>Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?

| Opsi | Isi |
|---|---|
| A | Pada kelompok yang dapat dibuat segitiga, ada jumlah panjang dua sisi yang kurang dari sisi ketiga |
| B | Pada kelompok yang tidak dapat dibuat segitiga, jumlah panjang ketiga sisinya lebih dari 20 cm |
| C | Pada kelompok yang tidak dapat dibuat segitiga, ada dua sedotan yang sama panjang |
| D | Pada kelompok yang tidak dapat dibuat segitiga, ada jumlah panjang dua sisi yang tidak lebih dari sisi ketiga |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Syarat pembentukan segitiga adalah jumlah panjang dua sisi harus lebih besar dari sisi ketiga (a+b>c, a+c>b, b+c>a). Pada baris 2 (4,6,6), 4+6>6 (10>6), 4+6>6 (10>6), 6+6>4 (12>4) -> Bisa. Pada baris 3 (5,4,12), 5+4=9 < 12 -> Tidak bisa. Pada baris 4 (10,5,15), 10+5=15 = 15 -> Tidak bisa. Pada baris 5 (5,12,13), 5+12=17 > 13 -> Bisa. Kelompok yang tidak bisa membentuk segitiga memiliki jumlah dua sisi yang tidak lebih dari (kurang dari atau sama dengan) sisi ketiga.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7017dc11cee0e13bd74ff4513a99d10a77d5a6aab7ff18b382e9902a22a0eb6f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2703 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2628 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2553 |

Run 1 — solusi: Syarat pembentukan segitiga adalah jumlah panjang dua sisi harus lebih besar dari sisi ketiga (a+b>c, a+c>b, b+c>a). Pada baris 2 (4,6,6), 4+6>6 (10>6), 4+6>6 (10>6), 6+6>4 (12>4) -> Bisa. Pada baris 3 (5,4,12), 5+4=9 < 12 -> Tidak bisa. Pada baris 4 (10,5,15), 10+5=15 = 15 -> Tidak bisa. Pada baris 5 (5,12,13), 5+12=17 > 13 -> Bisa. Kelompok yang tidak bisa membentuk segitiga memiliki jumlah dua sisi yang tidak lebih dari (kurang dari atau sama dengan) sisi ketiga.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk menyimpulkan aturan atau prinsip (ketaksamaan segitiga) berdasarkan data yang diberikan dalam tabel. Ini melampaui sekadar mengingat fakta atau menerapkan prosedur rutin, karena siswa harus menganalisis hubungan antar sisi untuk menemukan pola umum.. Bukti: Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip atau aturan geometris (ketaksamaan segitiga) yang menghubungkan panjang sisi-sisi segitiga, yang merupakan pengetahuan konseptual.. Bukti: Perhatikan jumlah panjang sisi-sisinya di kolom sebelah kanan.; Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk mengintegrasikan informasi dari tabel dan menguji hipotesis terhadap pilihan jawaban. Meskipun konsepnya mendasar, siswa harus melakukan analisis perbandingan untuk setiap kasus (atau setidaknya memahami pola dari data yang ada) untuk membedakan kondisi yang valid dan tidak valid. Ini memerlukan perencanaan langkah berpikir yang lebih dari sekadar penerapan rumus langsung.. Bukti: Perhatikan tabel berikut.; Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang panjang sisi dan operasi penjumlahan sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengenali pola dari data tabel. Menentukan aturan ketaksamaan segitiga dari data yang diberikan memerlukan penalaran tingkat menengah karena siswa harus menguji hubungan antara jumlah dua sisi dengan sisi ketiga secara konsisten. |

Run 2 — solusi: Syarat pembentukan segitiga adalah jumlah dua sisi harus lebih besar dari sisi ketiga (a+b>c, a+c>b, b+c>a). Pada baris 2 (4,6,6), 4+6>6 (10>6), 4+6>6 (10>6), 6+6>4 (12>4). Pada baris 3 (5,4,12), 5+4=9 < 12 (tidak membentuk segitiga). Pada baris 4 (10,5,15), 10+5=15 (tidak membentuk segitiga). Pilihan D menyatakan syarat ketidaksamaan segitiga dengan benar (jumlah dua sisi tidak lebih dari sisi ketiga berarti tidak membentuk segitiga).
- Domain kognitif `classify/reasoning`: Siswa diminta untuk menyimpulkan aturan atau prinsip matematis (ketidaksamaan segitiga) berdasarkan pola yang ada pada tabel. Ini memerlukan pemahaman hubungan antar konsep, bukan sekadar prosedur rutin.. Bukti: Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip atau aturan (ketidaksamaan segitiga) yang mendasari pembentukan bangun datar, yang merupakan pengetahuan konseptual.. Bukti: Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan analisis pola pada tabel untuk menggeneralisasi aturan ketidaksamaan segitiga. Meskipun prosedurnya sederhana, siswa perlu mengintegrasikan informasi dari beberapa baris untuk membedakan kondisi yang memenuhi syarat dan yang tidak.. Bukti: Perhatikan jumlah panjang sisi-sisinya di kolom sebelah kanan.; Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang panjang sisi segitiga dan operasi penjumlahan sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengidentifikasi pola dari data yang disajikan. Soal ini menuntut kemampuan penalaran untuk menyimpulkan aturan geometris dari data numerik yang diberikan. |

Run 3 — solusi: Syarat pembentukan segitiga adalah jumlah panjang dua sisi harus lebih besar dari sisi ketiga (a+b > c, a+c > b, b+c > a). Jika ada jumlah dua sisi yang kurang dari atau sama dengan sisi ketiga, segitiga tidak terbentuk. Pilihan D menyatakan kondisi ini dengan benar.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk menyimpulkan aturan (teorema ketaksamaan segitiga) berdasarkan pola yang diamati pada tabel. Ini memerlukan penalaran untuk menggeneralisasi hubungan antara panjang sisi-sisi segitiga.. Bukti: Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang prinsip atau aturan geometris (teorema ketaksamaan segitiga) yang mendasari pembentukan segitiga.. Bukti: Perhatikan jumlah panjang sisi-sisinya di kolom sebelah kanan.; Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengintegrasikan data dari tabel untuk menemukan pola/aturan umum. Meskipun prosedurnya sederhana (membandingkan jumlah sisi), siswa perlu melakukan abstraksi dari contoh-contoh yang diberikan untuk menentukan kondisi yang benar, yang merupakan langkah kognitif di atas sekadar menghitung.. Bukti: Perhatikan tabel berikut.; Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan bilangan dan konsep panjang sisi segitiga. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengamati pola dan menarik kesimpulan sederhana dari tabel. Tugas ini menuntut kemampuan penalaran untuk menggeneralisasi aturan segitiga dari data yang tersedia. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 257/256; truncation: `True`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000037; applying=0.999963; reasoning=0.000000 | applying | 0.999963 | 0.000376 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000939; conceptual=0.903168; procedural=0.095894; metacognitive=0.000000 | conceptual | 0.903168 | 0.233249 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.591575; Medium=0.397482; Hard=0.010943 | Easy | 0.591575 | 0.661459 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999963; −Σp ln(p) = 0.000413; H = 0.000413/ln(3) = 0.000376; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.903168; −Σp ln(p) = 0.323352; H = 0.323352/ln(4) = 0.233249; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.591575; −Σp ln(p) = 0.726687; H = 0.726687/ln(3) = 0.661459; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan Ciri-Ciri Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan tabel berikut.
|No.|Sedotan (cm) a|b|c|Membentuk Segitiga?|b+c|a+c|a+b|
|1|5|6|7|Bisa|13|12|11|
|2|4|6|6|…|…|…|…|
|3|5|4|12|…|…|…|…|
|4|10|5|15|…|…|…|…|
|5|5|12|13|…|…|…|…|

Perhatikan jumlah panjang sisi-sisinya di kolom sebelah kanan.

Apakah perbedaan antara kelompok yang dapat dibuat segitiga dan kelompok yang tidak dapat dibuat segitiga?
Pilihan: A. Pada kelompok yang dapat dibuat segitiga, ada jumlah panjang dua sisi yang kurang dari sisi ketiga
B. Pada kelompok yang tidak dapat dibuat segitiga, jumlah panjang ketiga sisinya lebih dari 20 cm
C. Pada kelompok yang tidak dapat dibuat segitiga, ada dua sedotan yang sama panjang
D. Pada kelompok yang tidak dapat dibuat segitiga, ada jumlah panjang dua sisi yang tidak lebih dari sisi ketiga
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 57. Soal `30f40c729a52410a063b5714`

Komang dan Nisa berbeda pendapat tentang bentuk bangunan Candi Sewu.<br><br>Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?

| Opsi | Isi |
|---|---|
| A | Tidak boleh, karena sudut-sudut segitiga sama sisi tidak ada yang sama besar |
| B | Tidak boleh, karena segitiga sama kaki hanya boleh memiliki tepat 2 sisi sama panjang |
| C | Boleh, karena segitiga sama sisi memiliki setidaknya 2 sisi yang sama panjang |
| D | Boleh, karena semua segitiga dapat disebut segitiga sama kaki |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Segitiga sama kaki didefinisikan sebagai segitiga yang memiliki setidaknya dua sisi sama panjang. Segitiga sama sisi memiliki tiga sisi sama panjang, sehingga memenuhi syarat minimal memiliki dua sisi sama panjang. Oleh karena itu, segitiga sama sisi adalah jenis khusus dari segitiga sama kaki.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9cfa5db229e2d2c610bde9c46a654f694481bc5ce12a3c1d8800f1412c71b1f3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3553 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2382 |
| 3 | success | valid / verified | reasoning | conceptual | Easy | 2357 |

Run 1 — solusi: Segitiga sama kaki didefinisikan sebagai segitiga yang memiliki setidaknya dua sisi sama panjang. Segitiga sama sisi memiliki tiga sisi sama panjang, sehingga memenuhi syarat tersebut.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi segitiga sama kaki (setidaknya dua sisi sama panjang) pada properti segitiga sama sisi untuk menentukan kebenaran pernyataan.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman hubungan hierarkis antara kategori bangun datar (segitiga sama sisi sebagai bagian dari segitiga sama kaki).. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman konsep dasar geometri. Tidak ada perhitungan atau langkah kompleks yang diperlukan, hanya pemahaman definisi.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama sisi dan segitiga sama kaki. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan memahami klasifikasi bangun datar. Soal ini menguji pemahaman konsep dasar definisi segitiga tanpa perhitungan rumit. |

Run 2 — solusi: Segitiga sama kaki didefinisikan sebagai segitiga yang memiliki setidaknya dua sisi sama panjang. Segitiga sama sisi memiliki tiga sisi sama panjang, sehingga memenuhi syarat memiliki setidaknya dua sisi sama panjang. Oleh karena itu, segitiga sama sisi adalah jenis khusus dari segitiga sama kaki.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk memahami hubungan hierarkis antara dua jenis segitiga (klasifikasi inklusif). Ini memerlukan pemahaman konseptual tentang definisi sifat-sifat segitiga, bukan sekadar menghafal.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan hubungan antar konsep geometri (segitiga sama sisi dan sama kaki), yang merupakan pengetahuan konseptual.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman definisi yang tepat dan kemampuan untuk melihat hubungan inklusif antar bentuk geometri. Siswa sering terjebak pada definisi eksklusif (hanya 2 sisi), sehingga memerlukan penalaran untuk menyimpulkan bahwa 'setidaknya 2 sisi' mencakup kasus 3 sisi sama panjang.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama sisi dan segitiga sama kaki. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari sifat-sifat bangun datar. Memahami hierarki klasifikasi (bahwa segitiga sama sisi adalah subset dari segitiga sama kaki) adalah tantangan konseptual yang sesuai untuk tingkat ini. |

Run 3 — solusi: Segitiga sama kaki didefinisikan sebagai segitiga yang memiliki setidaknya dua sisi sama panjang. Segitiga sama sisi memiliki tiga sisi sama panjang, sehingga memenuhi syarat minimal memiliki dua sisi sama panjang. Oleh karena itu, segitiga sama sisi adalah jenis khusus dari segitiga sama kaki.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk memahami hubungan hierarkis antara dua kategori bangun datar (segitiga sama sisi dan sama kaki) berdasarkan definisi sifat-sifatnya. Ini memerlukan pemahaman konsep, bukan sekadar ingatan prosedur.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan klasifikasi bangun datar (segitiga), yang merupakan pengetahuan konseptual.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman konseptual tentang klasifikasi segitiga. Siswa harus memahami bahwa definisi segitiga sama kaki (setidaknya dua sisi sama panjang) mencakup segitiga sama sisi (tiga sisi sama panjang). Ini adalah konsep dasar geometri yang diajarkan di kelas 5, sehingga tingkat kesulitannya rendah.. Bukti: Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama sisi dan segitiga sama kaki. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memahami klasifikasi bangun datar adalah materi standar kelas 5. Soal ini menguji pemahaman definisi tanpa memerlukan perhitungan atau langkah kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "reasoning": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3838`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa perlu melakukan penalaran untuk memahami hubungan inklusif antara dua kategori bangun datar (segitiga sama sisi sebagai subset dari segitiga sama kaki) berdasarkan definisi sifat-sifatnya, bukan sekadar mengingat fakta.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman tentang definisi, klasifikasi, dan hubungan hierarkis antar konsep geometri, yang merupakan pengetahuan konseptual.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena meskipun konsepnya dasar, siswa sering terjebak pada definisi eksklusif (hanya 2 sisi). Memahami inklusi kelas (segitiga sama sisi adalah sama kaki) memerlukan penalaran konseptual yang melampaui hafalan definisi sederhana, yang merupakan tantangan kognitif yang sesuai untuk kelas 5.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama sisi dan segitiga sama kaki. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Memahami hierarki klasifikasi bangun datar adalah materi standar kelas 5. Tantangan utamanya adalah mengatasi miskonsepsi umum bahwa 'sama kaki' harus memiliki 'tepat' dua sisi sama panjang. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 120/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000008; applying=0.999992; reasoning=0.000000 | applying | 0.999992 | 0.000088 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.109912; conceptual=0.871456; procedural=0.018632; metacognitive=0.000000 | conceptual | 0.871456 | 0.315090 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.890183; Medium=0.106697; Hard=0.003121 | Easy | 0.890183 | 0.327978 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000097; H = 0.000097/ln(3) = 0.000088; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.871456; −Σp ln(p) = 0.436807; H = 0.436807/ln(4) = 0.315090; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.890183; −Σp ln(p) = 0.360321; H = 0.360321/ln(3) = 0.327978; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan Ciri-Ciri Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Komang dan Nisa berbeda pendapat tentang bentuk bangunan Candi Sewu.

Bolehkah segitiga sama sisi juga disebut segitiga sama kaki?
Pilihan: A. Tidak boleh, karena sudut-sudut segitiga sama sisi tidak ada yang sama besar
B. Tidak boleh, karena segitiga sama kaki hanya boleh memiliki tepat 2 sisi sama panjang
C. Boleh, karena segitiga sama sisi memiliki setidaknya 2 sisi yang sama panjang
D. Boleh, karena semua segitiga dapat disebut segitiga sama kaki
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 58. Soal `4857ed456bf6383ee84ff085`

Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

| Opsi | Isi |
|---|---|
| A | Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang |
| B | Ya, karena sisi-sisi yang berhadapan pada jajargenjang sejajar |
| C | Ya, karena belah ketupat boleh disebut jajargenjang, maka sebaliknya juga boleh |
| D | Tidak, karena jajargenjang tidak memiliki sisi-sisi yang sejajar |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Belah ketupat adalah jajargenjang dengan keempat sisi sama panjang. Jajargenjang umum tidak harus memiliki keempat sisi sama panjang. Oleh karena itu, tidak semua jajargenjang adalah belah ketupat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e1d0b7620d082fe10c7f906fbe07e4610221a6737435b37dd9455b633fa3cb49`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2321 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2385 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2328 |

Run 1 — solusi: Belah ketupat adalah jajargenjang dengan keempat sisi sama panjang. Jajargenjang umum tidak harus memiliki keempat sisi sama panjang. Oleh karena itu, tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk mengevaluasi hubungan hierarkis antara dua bangun datar (belah ketupat dan jajargenjang). Ini memerlukan pemahaman tentang sifat-sifat bangun tersebut dan kemampuan untuk menyimpulkan bahwa hubungan inklusi tidak berlaku dua arah.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?; Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan hubungan hierarkis antar kategori bangun datar (konsep), bukan sekadar menghafal fakta atau melakukan prosedur hitung.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; apakah sembarang jajargenjang boleh disebut belah ketupat?
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman konseptual yang mendalam tentang klasifikasi bangun datar. Siswa harus menolak logika 'bolak-balik' yang umum terjadi pada pemula. Meskipun langkahnya singkat, tuntutan untuk membedakan sifat esensial (sisi sama panjang) dalam konteks hierarki geometri cukup menantang bagi siswa kelas 5.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sering mengalami kesulitan dengan logika inklusi bangun datar. Soal ini menguji pemahaman konsep yang melampaui sekadar identifikasi visual, sehingga dikategorikan Medium. |

Run 2 — solusi: Belah ketupat adalah jajargenjang dengan empat sisi sama panjang. Jajargenjang umum tidak harus memiliki empat sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk mengevaluasi hubungan hierarkis antara dua bangun datar (belah ketupat dan jajargenjang). Ini memerlukan pemahaman konsep sifat-sifat bangun datar dan kemampuan untuk menyimpulkan bahwa hubungan inklusi tidak berlaku dua arah.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?; Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan, kategori, dan struktur konsep dalam geometri (klasifikasi bangun datar).. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; apakah sembarang jajargenjang boleh disebut belah ketupat?
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman konseptual tentang hierarki bangun datar. Meskipun prosedurnya sederhana (memilih jawaban), siswa harus menalar hubungan inklusi antar bangun datar tanpa bantuan visual, yang merupakan tantangan konseptual bagi kelas 5.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memahami klasifikasi bangun datar adalah materi kelas 5. Menentukan hubungan inklusi (apakah semua A adalah B) memerlukan penalaran logis yang melampaui sekadar menghafal definisi, sehingga dikategorikan Medium. |

Run 3 — solusi: Belah ketupat adalah jajargenjang dengan keempat sisi sama panjang. Jajargenjang umum tidak harus memiliki empat sisi sama panjang. Oleh karena itu, jajargenjang tidak selalu merupakan belah ketupat.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk mengevaluasi hubungan hierarkis antara dua bangun datar (belah ketupat dan jajargenjang). Ini memerlukan pemahaman konsep tentang sifat-sifat bangun datar dan hubungan inklusi antar himpunan bangun tersebut, yang melampaui sekadar mengingat definisi.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan, kategori, dan struktur konsep dalam klasifikasi bangun datar (hierarki bangun segi empat).. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; apakah sembarang jajargenjang boleh disebut belah ketupat?
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman konseptual yang mendalam tentang sifat bangun datar. Siswa harus mampu membedakan antara sifat yang dimiliki oleh semua anggota kelas (jajargenjang) dan sifat khusus yang membatasi sub-kelas (belah ketupat). Ini adalah tugas klasifikasi yang memerlukan penalaran logis tentang hubungan inklusi, bukan sekadar prosedur rutin.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?; jajargenjang tidak harus memiliki empat sisi yang sama panjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi dan sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, memahami hierarki bangun datar adalah materi standar. Soal ini menantang siswa untuk tidak terjebak pada logika terbalik (konvers) yang sering terjadi dalam klasifikasi geometri. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 128/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000010; applying=0.999990; reasoning=0.000000 | applying | 0.999990 | 0.000112 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.027005; conceptual=0.961706; procedural=0.011289; metacognitive=0.000000 | conceptual | 0.961706 | 0.133959 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.787356; Medium=0.206814; Hard=0.005830 | Easy | 0.787356 | 0.495311 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999990; −Σp ln(p) = 0.000123; H = 0.000123/ln(3) = 0.000112; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.961706; −Σp ln(p) = 0.185706; H = 0.185706/ln(4) = 0.133959; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.787356; −Σp ln(p) = 0.544155; H = 0.544155/ln(3) = 0.495311; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan Ciri-Ciri Segi Empat
Tipe soal: multiple_choice
Stimulus: -
Soal: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?
Pilihan: A. Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang
B. Ya, karena sisi-sisi yang berhadapan pada jajargenjang sejajar
C. Ya, karena belah ketupat boleh disebut jajargenjang, maka sebaliknya juga boleh
D. Tidak, karena jajargenjang tidak memiliki sisi-sisi yang sejajar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 59. Soal `125e1947badecc1a26459e6e`

Guru kalian akan menyediakan 2 pasang sedotan yang sama panjang dan seutas tali. Rangkailah keempat sedotan tersebut sehingga membentuk jajargenjang.<br><br>Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?<br><br>Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?

| Opsi | Isi |
|---|---|
| A | Persegi panjang |
| B | Belah ketupat |
| C | Layang-layang |
| D | Trapesium siku-siku |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jajargenjang memiliki sifat sudut berdekatan berjumlah 180 derajat. Jika satu sudut diubah menjadi 90 derajat, maka sudut yang berdekatan dengannya juga menjadi 90 derajat (180 - 90 = 90). Karena sisi-sisi berhadapan sejajar dan sama panjang, maka keempat sudutnya menjadi 90 derajat, yang membentuk persegi panjang.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `64f9d8f234344d3c5645d99b5e795a76767141b5a80b7b4e2fc08d90885d7a2b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2480 |
| 2 | success | valid / verified | applying | conceptual | Medium | 4048 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2474 |

Run 1 — solusi: Jajargenjang memiliki sisi berhadapan sejajar dan sama panjang. Jika satu sudut diubah menjadi siku-siku (90 derajat), maka sudut yang berhadapan dengannya juga menjadi 90 derajat (karena sama besar). Sudut yang berdekatan dengan sudut siku-siku tersebut juga harus menjadi 90 derajat agar jumlah sudut berdekatan dalam jajargenjang adalah 180 derajat. Karena keempat sudutnya menjadi siku-siku, bangun tersebut adalah persegi panjang.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk menganalisis sifat geometris jajargenjang dan bagaimana perubahan satu sudut mempengaruhi sudut lainnya serta klasifikasi bangun datar yang dihasilkan. Ini memerlukan pemahaman hubungan antar sudut dalam jajargenjang.. Bukti: Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?; Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat bangun datar (jajargenjang dan persegi panjang) serta hubungan antar sudut di dalamnya.. Bukti: Rangkailah keempat sedotan tersebut sehingga membentuk jajargenjang.; Jika satu saja sudut jajargenjang diubah menjadi siku-siku
- Intended difficulty `classify/Medium`: Soal menuntut pemahaman sifat jajargenjang. Siswa harus menyimpulkan bahwa jika satu sudut 90 derajat, maka sudut berdekatan dan berhadapan juga 90 derajat. Ini adalah langkah penalaran logis yang melampaui sekadar mengingat definisi.. Bukti: Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?; Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat jajargenjang (sudut berhadapan sama besar, sudut berdekatan berjumlah 180 derajat). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan sudah mengenal sifat-sifat bangun datar. Menghubungkan perubahan sudut pada jajargenjang menjadi persegi panjang adalah tugas standar untuk tingkat ini, namun memerlukan penalaran lebih dari sekadar hafalan. |

Run 2 — solusi: Jajargenjang memiliki sifat sudut berdekatan yang berjumlah 180 derajat. Jika satu sudut diubah menjadi 90 derajat, maka sudut yang berdekatan dengannya juga menjadi 90 derajat (180 - 90 = 90). Karena sisi-sisi berhadapan sama panjang dan keempat sudutnya menjadi 90 derajat, maka bangun tersebut adalah persegi panjang.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang sifat sudut pada jajargenjang (sudut berdekatan berjumlah 180 derajat) untuk menyimpulkan perubahan pada sudut lainnya dan mengidentifikasi bangun baru yang terbentuk.. Bukti: Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?; Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antar sifat bangun datar (jajargenjang dan persegi panjang) dan bagaimana perubahan satu properti memengaruhi properti lainnya.. Bukti: Rangkailah keempat sedotan tersebut sehingga membentuk jajargenjang.; Jika satu saja sudut jajargenjang diubah menjadi siku-siku
- Intended difficulty `classify/Medium`: Soal menuntut pemahaman relasional tentang sifat bangun datar. Siswa tidak hanya menghafal nama bangun, tetapi harus menalar konsekuensi perubahan sudut pada jajargenjang. Ini melibatkan beberapa langkah logis (sudut berdekatan, sifat persegi panjang).. Bukti: Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?; Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat jajargenjang (sisi sejajar, sudut berdekatan berjumlah 180 derajat) dan definisi persegi panjang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari sifat bangun datar. Menghubungkan perubahan sudut pada jajargenjang menjadi persegi panjang adalah tantangan yang sesuai untuk tingkat menengah karena memerlukan penalaran logis sederhana. |

Run 3 — solusi: Jajargenjang memiliki sifat sudut berhadapan sama besar dan sudut berdekatan berjumlah 180 derajat. Jika satu sudut diubah menjadi 90 derajat (siku-siku), maka sudut berhadapannya juga menjadi 90 derajat. Sudut berdekatan yang semula bukan 90 derajat juga akan menjadi 90 derajat karena 180 - 90 = 90. Bangun dengan sisi berhadapan sejajar dan keempat sudut siku-siku adalah persegi panjang.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat-sifat geometri jajargenjang dan bagaimana perubahan sudut memengaruhi klasifikasi bangun tersebut. Ini melibatkan penerapan konsep sifat sudut pada jajargenjang untuk menyimpulkan bentuk baru.. Bukti: Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?; Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar bangun datar (jajargenjang ke persegi panjang) berdasarkan sifat sudut dan sisi.. Bukti: Rangkailah keempat sedotan tersebut sehingga membentuk jajargenjang.; Jika satu saja sudut jajargenjang diubah menjadi siku-siku
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman sifat geometri yang mendalam. Siswa harus memvisualisasikan atau menalar perubahan sudut pada jajargenjang (sudut berdekatan berjumlah 180 derajat) untuk menyimpulkan bahwa semua sudut menjadi siku-siku. Ini melampaui sekadar hafalan definisi.. Bukti: Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?; Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat jajargenjang (sudut berhadapan sama besar, sudut berdekatan berjumlah 180 derajat) dan definisi persegi panjang. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mengenal sifat bangun datar. Menghubungkan perubahan sudut pada jajargenjang menjadi persegi panjang memerlukan penalaran logis tentang sifat sudut, yang merupakan tantangan menengah bagi level ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4396`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pemahaman sifat sudut pada jajargenjang (sudut berdekatan berjumlah 180 derajat) untuk menyimpulkan perubahan pada sudut lainnya dan mengidentifikasi bangun baru yang terbentuk. Ini adalah penerapan konsep pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang hubungan antar sifat bangun datar (jajargenjang dan persegi panjang) dan bagaimana perubahan satu properti memengaruhi properti lainnya.
- Intended difficulty `Medium`: Soal menuntut pemahaman relasional tentang sifat bangun datar. Siswa tidak hanya menghafal nama bangun, tetapi harus menalar konsekuensi perubahan sudut pada jajargenjang. Ini melibatkan beberapa langkah logis (sudut berdekatan, sifat persegi panjang) yang sesuai untuk tingkat menengah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat jajargenjang (sisi sejajar, sudut berdekatan berjumlah 180 derajat) dan definisi persegi panjang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah mempelajari sifat bangun datar. Menghubungkan perubahan sudut pada jajargenjang menjadi persegi panjang adalah tantangan yang sesuai untuk tingkat menengah karena memerlukan penalaran logis sederhana. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 120/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000545; applying=0.999455; reasoning=0.000000 | applying | 0.999455 | 0.004224 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.075873; conceptual=0.915752; procedural=0.008374; metacognitive=0.000000 | conceptual | 0.915752 | 0.228162 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.848315; Medium=0.148504; Hard=0.003181 | Easy | 0.848315 | 0.401471 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999455; −Σp ln(p) = 0.004640; H = 0.004640/ln(3) = 0.004224; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.915752; −Σp ln(p) = 0.316300; H = 0.316300/ln(4) = 0.228162; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.848315; −Σp ln(p) = 0.441061; H = 0.441061/ln(3) = 0.401471; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membandingkan Ciri-Ciri Segi Empat
Tipe soal: multiple_choice
Stimulus: -
Soal: Guru kalian akan menyediakan 2 pasang sedotan yang sama panjang dan seutas tali. Rangkailah keempat sedotan tersebut sehingga membentuk jajargenjang.

Jika satu saja sudut jajargenjang diubah menjadi siku-siku, bagaimana dengan sudut-sudut yang lain?

Setelah menjadi sudut siku-siku, bangun apa yang diperoleh?
Pilihan: A. Persegi panjang
B. Belah ketupat
C. Layang-layang
D. Trapesium siku-siku
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 60. Soal `55b83913e74d5fc1fd6b66d8`

Data berikut menunjukkan hasil ulangan Matematika siswa kelas V SD Mekarsari.<br><br>Jika siswa dengan nilai kurang dari 70 harus mengikuti remedi, ada berapa siswa yang mengikuti remedi?

| Opsi | Isi |
|---|---|
| A | 3 siswa |
| B | 8 siswa |
| C | 5 siswa |
| D | 14 siswa |

![Gambar sumber soal 60](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0263-03.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `8 siswa`.
Solusi minimum hasil AI: Identifikasi nilai kurang dari 70: nilai 40 (ada 2), nilai 50 (ada 1), nilai 60 (ada 5). Total siswa remedi = 2 + 1 + 5 = 8 siswa.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0263-03.png. Transkripsi visual: Data nilai ulangan Matematika siswa kelas V SD Mekarsari disajikan dalam bentuk daftar angka: Baris 1: 80, 40, 80, 70, 40, 50, 80, 90, 60, 60. Baris 2: 70, 70, 80, 70, 100, 60, 80, 90, 70, 80. Baris 3: 60, 70, 60, 90, 80.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `af94d799867fe024c6f92be616402a8abdf4483720f1fa0dc26564665824bdf7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3523 |
| 2 | success | valid / verified | applying | procedural | Easy | 3524 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3461 |

Run 1 — solusi: Identifikasi nilai < 70: 40 (ada 2), 50 (ada 1), 60 (ada 5). Total = 2 + 1 + 5 = 8 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengklasifikasikan data mentah berdasarkan kriteria yang diberikan (nilai < 70) dan melakukan penghitungan frekuensi. Ini adalah penerapan prosedur pengolahan data sederhana yang rutin.. Bukti: Jika siswa dengan nilai kurang dari 70 harus mengikuti remedi; Data berikut menunjukkan hasil ulangan Matematika
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep pengumpulan dan pengolahan data sederhana (frekuensi nilai), yang merupakan pengetahuan prosedural dalam statistika dasar.. Bukti: Data berikut menunjukkan hasil ulangan Matematika
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan pemindaian data (scanning) dan penghitungan frekuensi sederhana. Tidak ada langkah yang saling bergantung secara kompleks atau kebutuhan untuk membangun strategi non-rutin.. Bukti: Jika siswa dengan nilai kurang dari 70 harus mengikuti remedi; Data berikut menunjukkan hasil ulangan Matematika

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan dan menghitung frekuensi data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa mengolah data sederhana dalam bentuk daftar nilai. Tugas ini adalah prosedur rutin yang sesuai dengan tingkat kelas. |

Run 2 — solusi: Identifikasi nilai kurang dari 70: nilai 40 (ada 2), nilai 50 (ada 1), nilai 60 (ada 5). Total siswa remedi = 2 + 1 + 5 = 8 siswa.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengklasifikasikan data mentah ke dalam kategori (kurang dari 70) dan menghitung frekuensinya. Ini adalah penerapan prosedur pengolahan data sederhana yang rutin.. Bukti: Jika siswa dengan nilai kurang dari 70 harus mengikuti remedi; ada berapa siswa yang mengikuti remedi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang bagaimana mengorganisir dan menghitung frekuensi dari sekumpulan data mentah, yang merupakan pengetahuan prosedural dalam statistika dasar.. Bukti: Data berikut menunjukkan hasil ulangan Matematika
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan pencacahan data (tallying) sederhana berdasarkan kriteria yang jelas. Tidak ada langkah yang saling bergantung atau kendala kompleks.. Bukti: kurang dari 70; ada berapa siswa yang mengikuti remedi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca data dan membandingkan bilangan (kurang dari). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa mengolah data sederhana. Tugas ini hanya memerlukan ketelitian dalam menyortir data, yang sesuai dengan tingkat kemampuan kelas 5. |

Run 3 — solusi: Identifikasi nilai kurang dari 70: nilai 40 (ada 2), 50 (ada 1), dan 60 (ada 5). Jumlah siswa = 2 + 1 + 5 = 8 siswa.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengklasifikasikan dan menghitung frekuensi data yang memenuhi kriteria tertentu (kurang dari 70). Ini adalah penerapan prosedur pengolahan data sederhana yang rutin.. Bukti: Jika siswa dengan nilai kurang dari 70 harus mengikuti remedi; Data berikut menunjukkan hasil ulangan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pengumpulan dan pengolahan data sederhana (frekuensi) serta kemampuan menerapkan kriteria perbandingan (kurang dari).. Bukti: Data berikut menunjukkan hasil ulangan; kurang dari 70
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan pemindaian data (scanning) dan penghitungan frekuensi sederhana. Tidak ada langkah yang saling bergantung secara kompleks atau kendala yang berinteraksi.. Bukti: kurang dari 70; Data berikut menunjukkan hasil ulangan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca data acak dan membandingkan bilangan (kurang dari). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan pengolahan data sederhana seperti menghitung frekuensi dari daftar nilai. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4948`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur pengolahan data sederhana (menghitung frekuensi) berdasarkan kriteria yang diberikan (nilai < 70). Ini adalah tugas rutin dalam statistika dasar.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang prosedur pengumpulan dan pengolahan data sederhana (frekuensi nilai), yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan pemindaian data (scanning) dan penghitungan frekuensi sederhana. Tidak ada langkah yang saling bergantung secara kompleks atau kebutuhan untuk membangun strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan dan menghitung frekuensi data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa mengolah data sederhana dalam bentuk daftar nilai. Tugas ini adalah prosedur rutin yang sesuai dengan tingkat kelas. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 155/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000131; applying=0.999869; reasoning=0.000000 | applying | 0.999869 | 0.001182 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.017449; conceptual=0.976439; procedural=0.006112; metacognitive=0.000000 | conceptual | 0.976439 | 0.090226 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.772235; Medium=0.221909; Hard=0.005856 | Easy | 0.772235 | 0.513173 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999869; −Σp ln(p) = 0.001299; H = 0.001299/ln(3) = 0.001182; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.976439; −Σp ln(p) = 0.125080; H = 0.125080/ln(4) = 0.090226; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.772235; −Σp ln(p) = 0.563779; H = 0.563779/ln(3) = 0.513173; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Mengumpulkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Data berikut menunjukkan hasil ulangan Matematika siswa kelas V SD Mekarsari.

Jika siswa dengan nilai kurang dari 70 harus mengikuti remedi, ada berapa siswa yang mengikuti remedi?
Pilihan: A. 3 siswa
B. 8 siswa
C. 5 siswa
D. 14 siswa
Transkripsi visual: Data nilai ulangan Matematika siswa kelas V SD Mekarsari disajikan dalam bentuk daftar angka: Baris 1: 80, 40, 80, 70, 40, 50, 80, 90, 60, 60. Baris 2: 70, 70, 80, 70, 100, 60, 80, 90, 70, 80. Baris 3: 60, 70, 60, 90, 80.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 61. Soal `e796428d8e43335b955f16db`

Data berikut menunjukkan hasil ulangan Matematika siswa kelas V SD Mekarsari.<br><br>Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?

| Opsi | Isi |
|---|---|
| A | 100 |
| B | 80 |
| C | 90 |
| D | 40 |

![Gambar sumber soal 61](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0263-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Memindai seluruh 25 data yang diberikan untuk mencari nilai maksimum. Nilai-nilai yang ada adalah 40, 50, 60, 70, 80, 90, 100. Nilai tertinggi adalah 100.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0263-03.png. Transkripsi visual: Terdapat sekumpulan data nilai ulangan matematika yang terdiri dari 25 angka: 80, 40, 80, 70, 40, 50, 80, 90, 60, 60, 70, 70, 80, 70, 100, 60, 80, 90, 70, 80, 60, 70, 60, 90, 80.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `772b417b59490c3eee2cd6fa701b2a7e9e4946bab48a04c01f8ce22f0680ef2a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3407 |
| 2 | success | valid / verified | knowing | factual | Easy | 3455 |
| 3 | success | valid / verified | knowing | factual | Easy | 3399 |

Run 1 — solusi: Memindai seluruh 25 data yang diberikan untuk mencari nilai maksimum. Nilai-nilai yang ada adalah 40, 50, 60, 70, 80, 90, 100. Nilai tertinggi adalah 100.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan identifikasi nilai maksimum dari sekumpulan data yang diberikan. Ini adalah prosedur langsung untuk mengenali elemen terbesar dalam himpunan data.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang konsep dasar statistik deskriptif yaitu nilai maksimum (rentang data), yang merupakan pengetahuan faktual tentang data.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pemindaian visual sederhana untuk menemukan nilai terbesar. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah dan membaca data. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa mengurutkan atau mencari nilai ekstrem dari sekumpulan data sederhana. |

Run 2 — solusi: Memeriksa seluruh 25 data yang diberikan untuk mencari nilai maksimum. Nilai-nilai yang ada adalah 40, 50, 60, 70, 80, 90, dan 100. Nilai tertinggi adalah 100.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan pemindaian (scanning) terhadap sekumpulan data untuk mengidentifikasi nilai maksimum. Ini adalah prosedur langsung yang tidak memerlukan analisis mendalam atau strategi kompleks.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang konsep nilai tertinggi dalam sebuah kumpulan data sederhana.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?
- Intended difficulty `classify/Easy`: Soal ini termasuk kategori Easy karena tugasnya sangat langsung: mencari nilai maksimum dari daftar data yang tersedia. Tidak ada langkah-langkah yang saling bergantung, tidak ada kendala yang berinteraksi, dan tidak ada kebutuhan untuk memilih strategi khusus. Siswa hanya perlu ketelitian dalam membaca data.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?; Data berikut menunjukkan hasil ulangan Matematika siswa kelas V SD Mekarsari.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca bilangan dan membandingkan nilai bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 5, mengidentifikasi nilai tertinggi dari sekumpulan data adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Memeriksa seluruh 25 data yang diberikan untuk mencari nilai maksimum. Nilai-nilai yang ada adalah 40, 50, 60, 70, 80, 90, dan 100. Nilai tertinggi di antara data tersebut adalah 100.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan pemindaian (scanning) terhadap sekumpulan data untuk mengidentifikasi nilai maksimum. Ini adalah prosedur langsung yang tidak memerlukan analisis mendalam atau strategi kompleks.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang konsep nilai tertinggi dalam sebuah kumpulan data sederhana.. Bukti: Data berikut menunjukkan hasil ulangan Matematika
- Intended difficulty `classify/Easy`: Tugas ini sangat rutin dan langsung. Siswa hanya perlu membandingkan angka-angka yang diberikan untuk menemukan nilai terbesar. Tidak ada langkah yang saling bergantung atau kendala yang perlu diintegrasikan.. Bukti: Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah dan membaca data sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 5, mengidentifikasi nilai maksimum dari daftar data adalah tugas dasar yang sudah sering dilatih. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 129/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000019 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.035595; conceptual=0.959158; procedural=0.005247; metacognitive=0.000000 | conceptual | 0.959158 | 0.134367 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.855906; Medium=0.141029; Hard=0.003064 | Easy | 0.855906 | 0.388814 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000021; H = 0.000021/ln(3) = 0.000019; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.959158; −Σp ln(p) = 0.186272; H = 0.186272/ln(4) = 0.134367; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.855906; −Σp ln(p) = 0.427156; H = 0.427156/ln(3) = 0.388814; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Mengumpulkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Data berikut menunjukkan hasil ulangan Matematika siswa kelas V SD Mekarsari.

Berapa nilai tertinggi pada hasil ulangan Matematika tersebut?
Pilihan: A. 100
B. 80
C. 90
D. 40
Transkripsi visual: Terdapat sekumpulan data nilai ulangan matematika yang terdiri dari 25 angka: 80, 40, 80, 70, 40, 50, 80, 90, 60, 60, 70, 70, 80, 70, 100, 60, 80, 90, 70, 80, 60, 70, 60, 90, 80.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 62. Soal `03ce645d3a0216321e3e95e0`

Tabel berikut adalah hasil penjualan kue apem selama seminggu yang dicatat Anggi.<br><br>Tabel 8.6 Hasil Penjualan Kue Apem<br><br>\|Hari\|Banyaknya Penjualan Kue Apem\|<br>\|---\|---\|<br>\|Senin\|40\|<br>\|Selasa\|35\|<br>\|Rabu\|30\|<br>\|Kamis\|37\|<br>\|Jumat\|27\|<br>\|Sabtu\|29\|<br><br>Satu kue apem dibeli ibunya Anggi seharga Rp1.200,00 dan dijual dengan harga Rp1.500,00. Tentukan keuntungan yang diperoleh ibunya Anggi dari hasil penjualan kue apem tersebut.

| Opsi | Isi |
|---|---|
| A | Rp5.940,00 |
| B | Rp237.600,00 |
| C | Rp59.400,00 |
| D | Rp297.000,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Total kue = 40 + 35 + 30 + 37 + 27 + 29 = 198. Keuntungan per kue = Rp1.500 - Rp1.200 = Rp300. Total keuntungan = 198 x Rp300 = Rp59.400.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d72884f617d6e9f85799bc03362d5be7dd04bc29b715140f42d5cf92935c6913`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3770 |
| 2 | success | valid / verified | applying | procedural | Medium | 4008 |
| 3 | success | valid / verified | applying | procedural | Medium | 3953 |

Run 1 — solusi: Total kue = 40 + 35 + 30 + 37 + 27 + 29 = 198. Keuntungan per kue = Rp1.500 - Rp1.200 = Rp300. Total keuntungan = 198 x Rp300 = Rp59.400.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aritmetika (penjumlahan data tabel dan perhitungan laba) dalam konteks rutin penjualan.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Tentukan keuntungan yang diperoleh ibunya Anggi
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme penjumlahan dan perkalian untuk menyelesaikan masalah keuntungan.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Satu kue apem dibeli ibunya Anggi seharga Rp1.200,00 dan dijual dengan harga Rp1.500,00
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah (menjumlahkan data tabel, menghitung selisih harga, mengalikan total). Meskipun prosedurnya rutin, ketergantungan langkah (total kue harus dihitung dulu) menempatkannya di tingkat Medium.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Tentukan keuntungan yang diperoleh ibunya Anggi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan operasi dasar aritmetika (pengurangan dan perkalian). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan tabel dan operasi hitung campuran. Soal ini menuntut ketelitian dalam tiga tahap perhitungan yang saling bergantung. |

Run 2 — solusi: Total kue = 40+35+30+37+27+29 = 198. Keuntungan per kue = 1500 - 1200 = 300. Total keuntungan = 198 x 300 = 59.400.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aritmetika (penjumlahan dan perkalian) pada data yang disajikan dalam tabel untuk menyelesaikan masalah keuntungan.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Tentukan keuntungan yang diperoleh ibunya Anggi
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma penjumlahan dan perkalian yang berurutan untuk mencapai solusi.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Tentukan keuntungan yang diperoleh ibunya Anggi
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah berurutan (menjumlahkan data tabel, menghitung selisih harga, mengalikan total) yang saling bergantung. Beban kalkulasi moderat.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Tentukan keuntungan yang diperoleh ibunya Anggi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan perkalian bilangan cacah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu melakukan operasi hitung campuran dan membaca data tabel sederhana. |

Run 3 — solusi: Total penjualan = 40+35+30+37+27+29 = 198 kue. Keuntungan per kue = Rp1.500 - Rp1.200 = Rp300. Total keuntungan = 198 x Rp300 = Rp59.400.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan data dari tabel (penjumlahan) dan menerapkan konsep keuntungan (selisih harga jual-beli) untuk menyelesaikan masalah rutin.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Satu kue apem dibeli ibunya Anggi seharga Rp1.200,00 dan dijual dengan harga Rp1.500,00; Tentukan keuntungan yang diperoleh ibunya Anggi
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma aritmetika dasar (penjumlahan dan perkalian) untuk memecahkan masalah kontekstual.. Bukti: Tabel berikut adalah hasil penjualan kue apem; Tentukan keuntungan yang diperoleh ibunya Anggi
- Intended difficulty `classify/Medium`: Siswa harus melakukan tiga langkah berurutan: menjumlahkan data tabel, menghitung selisih harga, dan mengalikan hasilnya. Meskipun prosedurnya rutin, beban kognitif menengah muncul dari perlunya mengelola beberapa informasi numerik secara berurutan.. Bukti: Tabel berikut adalah hasil penjualan kue apem selama seminggu; Satu kue apem dibeli ibunya Anggi seharga Rp1.200,00 dan dijual dengan harga Rp1.500,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan konsep dasar untung-rugi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena siswa harus mengelola data dari tabel dan melakukan operasi aritmetika bertahap tanpa bantuan langkah perantara. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 180/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.001763; conceptual=0.986245; procedural=0.011992; metacognitive=0.000000 | conceptual | 0.986245 | 0.056183 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.786866; Medium=0.200415; Hard=0.012718 | Easy | 0.786866 | 0.515434 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.986245; −Σp ln(p) = 0.077886; H = 0.077886/ln(4) = 0.056183; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.786866; −Σp ln(p) = 0.566262; H = 0.566262/ln(3) = 0.515434; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Piktogram
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel berikut adalah hasil penjualan kue apem selama seminggu yang dicatat Anggi.

Tabel 8.6 Hasil Penjualan Kue Apem

|Hari|Banyaknya Penjualan Kue Apem|
|---|---|
|Senin|40|
|Selasa|35|
|Rabu|30|
|Kamis|37|
|Jumat|27|
|Sabtu|29|

Satu kue apem dibeli ibunya Anggi seharga Rp1.200,00 dan dijual dengan harga Rp1.500,00. Tentukan keuntungan yang diperoleh ibunya Anggi dari hasil penjualan kue apem tersebut.
Pilihan: A. Rp5.940,00
B. Rp237.600,00
C. Rp59.400,00
D. Rp297.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Soal menyebutkan 'Piktogram' pada subtopik, namun data disajikan dalam tabel frekuensi biasa, bukan piktogram..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 63. Soal `52f23c67babf5a81e9ba7e79`

Sejak kecil, Nisa diajari orang tuanya untuk menabung. Ia sudah terbiasa menabung dari menyisihkan uang saku jika ingin membeli sesuatu. Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.<br><br>Jumlah Tabungan Nisa<br><br>Keterangan mewakili Rp4.000,00<br><br>Pada minggu berapa Nisa menabung paling banyak?

| Opsi | Isi |
|---|---|
| A | Minggu ke-5 |
| B | Minggu ke-2 |
| C | Minggu ke-3 |
| D | Minggu ke-1 |

![Gambar sumber soal 63](<../../../images/kelas5_crop-p0286-piktogram.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan jumlah simbol lingkaran pada setiap baris minggu. Minggu 1: 4,25 lingkaran; Minggu 2: 6 lingkaran; Minggu 3: 5,25 lingkaran; Minggu 4: 4,5 lingkaran; Minggu 5: 5,25 lingkaran. Jumlah terbanyak adalah 6 lingkaran pada Minggu ke-2.
Gambar sumber: images/kelas5_crop-p0286-piktogram.png. Transkripsi visual: Piktogram berjudul 'Jumlah Tabungan Nisa' dengan sumbu vertikal 'Minggu Ke-' (1 sampai 5) dan sumbu horizontal 'Jumlah Tabungan'. Keterangan: satu lingkaran penuh mewakili Rp4.000,00. Data per minggu: Minggu 1 memiliki 4 lingkaran penuh dan 1/4 lingkaran. Minggu 2 memiliki 6 lingkaran penuh. Minggu 3 memiliki 5 lingkaran penuh dan 1/4 lingkaran. Minggu 4 memiliki 4 lingkaran penuh dan 1/2 lingkaran. Minggu 5 memiliki 5 lingkaran penuh dan 1/4 lingkaran.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe367ee2f99fc6414fe1bf8d0e97eee575b6371eca8b5644af82aa725e402f1b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3553 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3601 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3622 |

Run 1 — solusi: Menghitung jumlah lingkaran pada setiap minggu: Minggu 1 (4,25 lingkaran), Minggu 2 (6 lingkaran), Minggu 3 (5,25 lingkaran), Minggu 4 (4,5 lingkaran), Minggu 5 (5,25 lingkaran). Minggu dengan jumlah lingkaran terbanyak adalah Minggu ke-2.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari piktogram dan membandingkan jumlah simbol untuk menentukan nilai maksimum. Ini adalah tugas membaca dan membandingkan data visual secara langsung.. Bukti: Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.; Pada minggu berapa Nisa menabung paling banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang representasi data dalam bentuk piktogram, yang merupakan konsep dasar dalam statistika.. Bukti: Keterangan mewakili Rp4.000,00
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan jumlah simbol pada setiap baris tanpa perlu melakukan perhitungan konversi nilai uang yang rumit, karena jumlah simbol sudah merepresentasikan jumlah tabungan secara proporsional.. Bukti: Pada minggu berapa Nisa menabung paling banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana dan membandingkan kuantitas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa membaca piktogram sederhana. Tugas ini hanya memerlukan perbandingan visual langsung. |

Run 2 — solusi: Menghitung jumlah lingkaran pada setiap baris: Minggu 1 (4,25 lingkaran), Minggu 2 (6 lingkaran), Minggu 3 (5,25 lingkaran), Minggu 4 (4,5 lingkaran), Minggu 5 (5,25 lingkaran). Minggu ke-2 memiliki jumlah lingkaran terbanyak, sehingga tabungan paling banyak terjadi pada minggu ke-2.
- Domain kognitif `classify/applying`: Siswa hanya perlu membandingkan jumlah simbol (lingkaran) pada setiap baris untuk menentukan nilai terbesar. Ini adalah penerapan langsung dari kemampuan membaca data piktogram.. Bukti: Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.; Pada minggu berapa Nisa menabung paling banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data dalam bentuk piktogram, yang merupakan konsep dasar dalam statistika.. Bukti: Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu melakukan inspeksi visual sederhana untuk membandingkan panjang baris (jumlah lingkaran) tanpa perlu melakukan perhitungan nilai uang yang kompleks.. Bukti: Pada minggu berapa Nisa menabung paling banyak?; Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca piktogram sederhana dan membandingkan jumlah objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat familiar dengan membaca grafik batang atau piktogram sederhana. Tugas membandingkan jumlah visual adalah tugas rutin yang tidak memerlukan perencanaan kompleks. |

Run 3 — solusi: Hitung jumlah lingkaran pada setiap minggu: Minggu 1 (4,25 lingkaran), Minggu 2 (6 lingkaran), Minggu 3 (5,25 lingkaran), Minggu 4 (4,5 lingkaran), Minggu 5 (5,25 lingkaran). Minggu dengan jumlah lingkaran terbanyak adalah Minggu ke-2.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari piktogram dan membandingkan jumlah simbol untuk menentukan nilai terbesar. Ini adalah tugas membaca dan membandingkan data secara langsung.. Bukti: Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.; Pada minggu berapa Nisa menabung paling banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk piktogram, yang merupakan konsep dasar dalam statistika.. Bukti: Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.; Keterangan mewakili Rp4.000,00
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan jumlah simbol lingkaran pada setiap baris untuk menentukan baris mana yang memiliki jumlah terbanyak. Tidak diperlukan perhitungan nilai uang yang kompleks karena perbandingan visual sudah cukup.. Bukti: Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.; Pada minggu berapa Nisa menabung paling banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana dan membandingkan jumlah benda. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa membaca piktogram sederhana. Tugas ini hanya memerlukan perbandingan visual langsung tanpa langkah perantara yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5081`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan inspeksi visual dan membandingkan kuantitas simbol (lingkaran) antar baris untuk menentukan nilai maksimum. Tidak diperlukan perhitungan nilai uang atau prosedur kompleks.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman dasar tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk piktogram.
- Intended difficulty `Easy`: Soal ini sangat mudah karena siswa hanya perlu membandingkan jumlah simbol secara visual. Tidak ada perhitungan yang diperlukan karena perbandingan langsung pada simbol sudah cukup untuk menjawab.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca piktogram sederhana dan membandingkan jumlah objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat familiar dengan membaca piktogram. Tugas ini adalah tugas rutin yang tidak memerlukan perencanaan atau integrasi konsep yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 217/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000012; applying=0.999988; reasoning=0.000000 | applying | 0.999988 | 0.000132 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.028772; conceptual=0.851996; procedural=0.119232; metacognitive=0.000000 | conceptual | 0.851996 | 0.354996 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.644500; Medium=0.343101; Hard=0.012399 | Easy | 0.644500 | 0.641332 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999988; −Σp ln(p) = 0.000145; H = 0.000145/ln(3) = 0.000132; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.851996; −Σp ln(p) = 0.492130; H = 0.492130/ln(4) = 0.354996; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.644500; −Σp ln(p) = 0.704575; H = 0.704575/ln(3) = 0.641332; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Piktogram
Tipe soal: multiple_choice
Stimulus: -
Soal: Sejak kecil, Nisa diajari orang tuanya untuk menabung. Ia sudah terbiasa menabung dari menyisihkan uang saku jika ingin membeli sesuatu. Piktogram pada Gambar 8.11 menunjukkan tabungan Nisa selama 5 minggu.

Jumlah Tabungan Nisa

Keterangan mewakili Rp4.000,00

Pada minggu berapa Nisa menabung paling banyak?
Pilihan: A. Minggu ke-5
B. Minggu ke-2
C. Minggu ke-3
D. Minggu ke-1
Transkripsi visual: Piktogram berjudul 'Jumlah Tabungan Nisa' dengan sumbu vertikal 'Minggu Ke-' (1 sampai 5) dan sumbu horizontal 'Jumlah Tabungan'. Keterangan: satu lingkaran penuh mewakili Rp4.000,00. Data per minggu: Minggu 1 memiliki 4 lingkaran penuh dan 1/4 lingkaran. Minggu 2 memiliki 6 lingkaran penuh. Minggu 3 memiliki 5 lingkaran penuh dan 1/4 lingkaran. Minggu 4 memiliki 4 lingkaran penuh dan 1/2 lingkaran. Minggu 5 memiliki 5 lingkaran penuh dan 1/4 lingkaran.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 64. Soal `1312d88be889daa8b0ab7ee7`

Perhatikan diagram batang berikut.<br><br>Kandungan Kalori Per 100 Gram Makanan<br><br>Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan. Kalori dihitung untuk setiap 100 gram makanan. Kalori adalah satuan energi. Kalori dalam makanan itulah yang digunakan tubuh sebagai sumber energi untuk dapat melaksanakan fungsinya dengan baik.<br><br>Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki. Dalam satu hari, Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau. Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal per bungkus. Apakah makanan yang dimakan Lukas kalorinya berlebihan? Mengapa demikian?

| Opsi | Isi |
|---|---|
| A | Tidak, karena totalnya 1.620 kkal, di bawah kebutuhan 2.100 kkal |
| B | Ya, karena totalnya 1.620 kkal, di atas kebutuhan 1.500 kkal |
| C | Ya, karena totalnya 2.270 kkal, di atas kebutuhan 2.100 kkal |
| D | Tidak, karena totalnya 970 kkal, di bawah kebutuhan 2.100 kkal |

![Gambar sumber soal 64](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0282-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Kalori Lukas: (3x130) + (2x260) + (1x60) + 300 + 350 = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Karena 1.620 < 2.100 (kebutuhan anak laki-laki), maka tidak berlebihan.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0282-04.png. Transkripsi visual: Diagram batang horizontal menunjukkan kandungan kalori per 100 gram makanan. Sumbu horizontal (Kalori kkal) memiliki garis grid setiap 50 unit (0, 50, 100, 150, 200, 250, 300). Nilai kalori per 100g: Nasi putih = 130, Nasi jagung = 150, Daging Sapi = 290, Daging Ayam = 260, Tahu goreng = 270, Tempe goreng = 240, Sayuran hijau = 60.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8c3a130b26a9968703440195dd182e06416600eb8b6649e872f901caf434d7d0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3986 |
| 2 | success | valid / verified | applying | procedural | Medium | 3975 |
| 3 | success | valid / verified | applying | procedural | Medium | 3949 |

Run 1 — solusi: Kalori Lukas: (3x130) + (2x260) + (1x60) + 300 + 350 = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Karena 1.620 < 2.100 (kebutuhan anak laki-laki), maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram, melakukan perkalian untuk menyesuaikan porsi (per 100g), menjumlahkan semua komponen kalori, dan membandingkannya dengan ambang batas yang diberikan. Ini adalah penerapan prosedur matematika dalam konteks rutin.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal; Apakah makanan yang dimakan Lukas kalorinya berlebihan?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma penjumlahan dan perkalian untuk memproses data yang disajikan dalam bentuk diagram batang.. Bukti: Diagram batang di atas menunjukkan kandungan kalori; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: membaca diagram, mengalikan nilai per 100g dengan jumlah porsi, menjumlahkan total, dan membandingkan dengan ambang batas. Meskipun prosedurnya rutin, siswa harus mengelola banyak informasi dan melakukan konversi porsi dengan cermat.. Bukti: 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal; Apakah makanan yang dimakan Lukas kalorinya berlebihan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membaca diagram batang, perkalian dasar, penjumlahan bilangan ribuan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu membaca data dan melakukan operasi hitung campuran. Soal ini menuntut ketelitian dalam mengolah data dari diagram dan teks secara bersamaan. |

Run 2 — solusi: Kalori Lukas: (3 x 130) + (2 x 260) + (1 x 60) + 300 + 350 = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Karena 1.620 < 2.100, maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram, melakukan perkalian untuk menyesuaikan porsi (per 100g), menjumlahkan total kalori, dan membandingkannya dengan ambang batas yang diberikan. Ini adalah penerapan prosedur matematika dalam konteks rutin.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal; Apakah makanan yang dimakan Lukas kalorinya berlebihan?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika (perkalian dan penjumlahan) untuk memproses data yang disajikan dalam bentuk diagram batang.. Bukti: Diagram batang di atas menunjukkan kandungan kalori; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait (membaca grafik, mengalikan porsi, menjumlahkan total, membandingkan). Meskipun prosedurnya rutin, siswa harus mengelola beberapa informasi sekaligus tanpa bantuan langkah demi langkah.. Bukti: 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membaca diagram batang, perkalian bilangan cacah, penjumlahan bilangan cacah. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu mengolah data dari tabel/grafik dan melakukan operasi hitung campuran. Soal ini menuntut ketelitian dalam mengintegrasikan data grafik dengan informasi teks. |

Run 3 — solusi: Nasi putih: 3 x 130 = 390. Daging ayam: 2 x 260 = 520. Sayuran hijau: 1 x 60 = 60. Makanan ringan: 300. Mi instan: 350. Total: 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Lukas (laki-laki) butuh 2.100 kkal. 1.620 < 2.100, jadi tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram batang, melakukan perkalian berdasarkan porsi (per 100g), menjumlahkan berbagai sumber kalori, dan membandingkan hasilnya dengan ambang batas yang diberikan. Ini adalah penerapan prosedur matematika dalam konteks rutin.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan; Apakah makanan yang dimakan Lukas kalorinya berlebihan?
- Dimensi pengetahuan `classify/procedural`: Siswa harus menggunakan prosedur perkalian dan penjumlahan untuk mengolah data yang diekstraksi dari diagram batang.. Bukti: Diagram batang di atas menunjukkan kandungan kalori; Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah yang saling terkait: membaca diagram, mengalikan dengan porsi, menjumlahkan total, dan membandingkan dengan kriteria. Meskipun prosedurnya familiar, siswa harus mengelola banyak informasi (5 sumber kalori) tanpa bantuan langkah per langkah.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membaca diagram batang, perkalian bilangan cacah, penjumlahan bilangan cacah. |
| dependentSteps | 5 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu melakukan operasi hitung campuran dan membaca data. Beban kognitif berasal dari banyaknya item yang harus dijumlahkan dan perlunya ketelitian dalam mengalikan porsi dengan nilai per 100g. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 336/256; truncation: `True`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000018; applying=0.999982; reasoning=0.000000 | applying | 0.999982 | 0.000192 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.032997; conceptual=0.629087; procedural=0.337916; metacognitive=0.000000 | conceptual | 0.629087 | 0.555986 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.708771; Medium=0.278518; Hard=0.012710 | Easy | 0.708771 | 0.596645 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999982; −Σp ln(p) = 0.000211; H = 0.000211/ln(3) = 0.000192; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.629087; −Σp ln(p) = 0.770761; H = 0.770761/ln(4) = 0.555986; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.708771; −Σp ln(p) = 0.655481; H = 0.655481/ln(3) = 0.596645; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan diagram batang berikut.

Kandungan Kalori Per 100 Gram Makanan

Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan. Kalori dihitung untuk setiap 100 gram makanan. Kalori adalah satuan energi. Kalori dalam makanan itulah yang digunakan tubuh sebagai sumber energi untuk dapat melaksanakan fungsinya dengan baik.

Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki. Dalam satu hari, Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau. Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal per bungkus. Apakah makanan yang dimakan Lukas kalorinya berlebihan? Mengapa demikian?
Pilihan: A. Tidak, karena totalnya 1.620 kkal, di bawah kebutuhan 2.100 kkal
B. Ya, karena totalnya 1.620 kkal, di atas kebutuhan 1.500 kkal
C. Ya, karena totalnya 2.270 kkal, di atas kebutuhan 2.100 kkal
D. Tidak, karena totalnya 970 kkal, di bawah kebutuhan 2.100 kkal
Transkripsi visual: Diagram batang horizontal menunjukkan kandungan kalori per 100 gram makanan. Sumbu horizontal (Kalori kkal) memiliki garis grid setiap 50 unit (0, 50, 100, 150, 200, 250, 300). Nilai kalori per 100g: Nasi putih = 130, Nasi jagung = 150, Daging Sapi = 290, Daging Ayam = 260, Tahu goreng = 270, Tempe goreng = 240, Sayuran hijau = 60.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 65. Soal `690a0d172f3a4c63acbfca28`

Tabel 8.13 Data Pengunjung Perpustakaan SD Pancasila<br><br>\|Hari\|Banyaknya Pengunjung\|<br>\|---\|---\|<br>\|Senin\|42\|<br>\|Selasa\|60\|<br>\|Rabu\|50\|<br>\|Kamis\|36\|<br>\|Jumat\|24\|<br>\|Sabtu\|48\|<br><br>Kapan perpustakaan tersebut menerima pengunjung paling sedikit?

| Opsi | Isi |
|---|---|
| A | Hari Sabtu |
| B | Hari Kamis |
| C | Hari Jumat |
| D | Hari Selasa |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Membandingkan nilai pada kolom 'Banyaknya Pengunjung' untuk setiap hari: 42, 60, 50, 36, 24, 48. Nilai terkecil adalah 24, yang terjadi pada hari Jumat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0cb74526f4496009c1d6c66d11381d613f6ce4d6d685ea2f4035e973c6bd68e0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2143 |
| 2 | success | valid / verified | knowing | factual | Easy | 2138 |
| 3 | success | valid / verified | knowing | factual | Easy | 2140 |

Run 1 — solusi: Membandingkan nilai pada kolom 'Banyaknya Pengunjung' untuk setiap hari: 42, 60, 50, 36, 24, 48. Nilai terkecil adalah 24, yang terjadi pada hari Jumat.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari tabel dan melakukan perbandingan nilai sederhana untuk menentukan nilai minimum. Ini adalah prosedur langsung.. Bukti: Kapan perpustakaan tersebut menerima pengunjung paling sedikit?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk tabel.. Bukti: Tabel 8.13 Data Pengunjung Perpustakaan SD Pancasila
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pemindaian data tabel untuk mencari nilai terkecil tanpa ada langkah tambahan atau kendala yang kompleks.. Bukti: Kapan perpustakaan tersebut menerima pengunjung paling sedikit?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel dan membandingkan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat familiar dengan membaca tabel sederhana dan membandingkan angka, sehingga soal ini tidak memberikan tantangan kognitif yang berarti. |

Run 2 — solusi: Membandingkan nilai pada kolom 'Banyaknya Pengunjung' untuk setiap hari: 42, 60, 50, 36, 24, 48. Nilai terkecil adalah 24, yang terjadi pada hari Jumat.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari tabel dan melakukan perbandingan nilai sederhana untuk menentukan nilai minimum. Ini adalah prosedur langsung.. Bukti: Kapan perpustakaan tersebut menerima pengunjung paling sedikit?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk tabel sederhana.. Bukti: Tabel 8.13 Data Pengunjung Perpustakaan SD Pancasila
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pembandingan nilai numerik sederhana tanpa langkah tambahan atau kendala yang kompleks.. Bukti: Kapan perpustakaan tersebut menerima pengunjung paling sedikit?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel dan membandingkan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat terbiasa membaca tabel dan membandingkan data sederhana, sehingga soal ini tidak menuntut kemampuan kognitif tinggi. |

Run 3 — solusi: Membandingkan nilai pada kolom 'Banyaknya Pengunjung' (42, 60, 50, 36, 24, 48) untuk mencari nilai terkecil. Nilai terkecil adalah 24, yang terjadi pada hari Jumat.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari tabel dan melakukan perbandingan sederhana untuk mengidentifikasi nilai minimum. Ini adalah prosedur langsung.. Bukti: Kapan perpustakaan tersebut menerima pengunjung paling sedikit?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk tabel sederhana.. Bukti: Tabel 8.13 Data Pengunjung Perpustakaan SD Pancasila
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pembacaan data langsung dari tabel tanpa langkah tambahan atau manipulasi data.. Bukti: Kapan perpustakaan tersebut menerima pengunjung paling sedikit?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel dan membandingkan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah sangat familiar dengan tabel data sederhana dan perbandingan nilai, sehingga soal ini tidak menuntut perencanaan atau integrasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000019 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.033662; conceptual=0.913139; procedural=0.053199; metacognitive=0.000000 | conceptual | 0.913139 | 0.254784 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.884295; Medium=0.111994; Hard=0.003711 | Easy | 0.884295 | 0.341063 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000021; H = 0.000021/ln(3) = 0.000019; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.913139; −Σp ln(p) = 0.353206; H = 0.353206/ln(4) = 0.254784; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.884295; −Σp ln(p) = 0.374696; H = 0.374696/ln(3) = 0.341063; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel 8.13 Data Pengunjung Perpustakaan SD Pancasila

|Hari|Banyaknya Pengunjung|
|---|---|
|Senin|42|
|Selasa|60|
|Rabu|50|
|Kamis|36|
|Jumat|24|
|Sabtu|48|

Kapan perpustakaan tersebut menerima pengunjung paling sedikit?
Pilihan: A. Hari Sabtu
B. Hari Kamis
C. Hari Jumat
D. Hari Selasa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 66. Soal `177f5534f5d559f72a66d033`

Diagram batang berikut menunjukan banyak siswa di SD Permata.<br><br>Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan:<br><br>Banyak siswa kelas 2 SD Permata?

| Opsi | Isi |
|---|---|
| A | 292 siswa |
| B | 54 siswa |
| C | 154 siswa |
| D | 0 siswa |

![Gambar sumber soal 66](<../../../images/kelas4_panduan_guru_kelas4.pdf-0244-06.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Jumlahkan siswa kelas 1, 3, 4, 5, dan 6: 57 + 58 + 56 + 62 + 59 = 292. Kurangi total siswa dengan jumlah tersebut: 346 - 292 = 54.
Gambar sumber: images/kelas4_panduan_guru_kelas4.pdf-0244-06.png. Transkripsi visual: Diagram batang menunjukkan jumlah siswa di SD Permata. Sumbu horizontal: Kelas 1, 2, 3, 4, 5, 6. Sumbu vertikal: 0-70. Batang Kelas 1=57, Kelas 2=kosong, Kelas 3=58, Kelas 4=56, Kelas 5=62, Kelas 6=59.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c657ed0fba7de062f3cc6be16f2c50c6ffe66196f0808f804b4a0ca54e5c7b73`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3653 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3603 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3722 |

Run 1 — solusi: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 adalah total siswa dikurangi jumlah siswa kelas lainnya: 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi data dari diagram batang, menjumlahkan nilai-nilai tersebut, dan melakukan pengurangan untuk menemukan nilai yang hilang. Ini adalah penerapan prosedur matematika rutin dalam konteks data.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?; Diagram batang berikut menunjukan banyak siswa di SD Permata.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang bagaimana data disajikan dalam diagram batang dan penggunaan operasi aritmatika dasar (penjumlahan dan pengurangan) untuk memecahkan masalah terkait data tersebut.. Bukti: Diagram batang berikut menunjukan banyak siswa di SD Permata.; Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: membaca data dari grafik, menjumlahkan lima nilai, dan melakukan pengurangan dari total. Meskipun prosedurnya rutin, siswa harus merencanakan langkah-langkah tersebut secara berurutan.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa.; 57 + 58 + 56 + 62 + 59 = 292, jadi kelas 2 = 346 - 292 = 54 siswa.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana dan melakukan operasi penjumlahan serta pengurangan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menjumlahkan lima bilangan dua digit dan melakukan pengurangan dengan total 346 adalah tugas yang sesuai dengan tingkat kemampuan, menuntut ketelitian dalam langkah-langkah berurutan. |

Run 2 — solusi: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 adalah total seluruh siswa dikurangi jumlah siswa kelas lainnya: 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat (penjumlahan data yang ada dan pengurangan dari total) untuk menyelesaikan masalah dalam konteks rutin diagram batang.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana data disajikan dalam diagram batang dan bagaimana menggunakan informasi tersebut untuk melakukan perhitungan.. Bukti: Diagram batang berikut menunjukan banyak siswa di SD Permata.
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah rutin: menjumlahkan nilai dari batang yang ada dan melakukan pengurangan dari total. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pengurangan bilangan cacah, serta kemampuan membaca data dari diagram batang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu melakukan operasi hitung dasar dan menginterpretasikan data sederhana. Soal ini menuntut ketelitian dalam menjumlahkan data yang tersedia sebelum melakukan pengurangan. |

Run 3 — solusi: Jumlahkan siswa kelas 1, 3, 4, 5, dan 6: 57 + 58 + 56 + 62 + 59 = 292. Kurangi total seluruh siswa dengan jumlah tersebut: 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi data yang tersedia, melakukan operasi penjumlahan untuk mencari total siswa yang diketahui, dan melakukan operasi pengurangan untuk mencari nilai yang hilang (missing value). Ini adalah penerapan prosedur matematika pada konteks data yang rutin.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?; 57 + 58 + 56 + 62 + 59 = 292, jadi kelas 2 = 346 - 292 = 54 siswa.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca data dari diagram batang dan menggunakan hubungan bagian-keseluruhan (part-whole) untuk menyelesaikan masalah, yang merupakan pengetahuan konseptual.. Bukti: Diagram batang berikut menunjukan banyak siswa di SD Permata.; Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap operasi (penjumlahan data yang ada, lalu pengurangan dari total) dan pemahaman bahwa data yang hilang dapat dicari melalui selisih total. Meskipun prosedurnya rutin, siswa harus merencanakan langkah-langkah tersebut secara berurutan.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa.; 57 + 58 + 56 + 62 + 59 = 292, jadi kelas 2 = 346 - 292 = 54 siswa.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman dasar diagram batang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan diagram batang dan operasi hitung dasar. Tantangan utama adalah mengintegrasikan data dari diagram ke dalam perhitungan dua langkah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `6551`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur penjumlahan dan pengurangan untuk menyelesaikan masalah data yang hilang. Ini adalah penerapan rutin dalam konteks diagram batang.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman hubungan bagian-keseluruhan (part-whole) di mana total adalah jumlah dari semua bagian, termasuk bagian yang tidak terlihat di diagram.
- Intended difficulty `Medium`: Soal memerlukan dua langkah rutin: menjumlahkan lima nilai dan melakukan pengurangan. Meskipun prosedurnya rutin, siswa harus merencanakan langkah-langkah tersebut secara berurutan dan teliti.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan cacah, serta kemampuan membaca diagram batang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 diharapkan mampu melakukan operasi hitung dasar dan menginterpretasikan data sederhana. Soal ini menuntut ketelitian dalam menjumlahkan data yang tersedia sebelum melakukan pengurangan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 144/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.013174; conceptual=0.976854; procedural=0.009971; metacognitive=0.000000 | conceptual | 0.976854 | 0.090790 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.614896; Medium=0.376349; Hard=0.008755 | Easy | 0.614896 | 0.644712 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.976854; −Σp ln(p) = 0.125862; H = 0.125862/ln(4) = 0.090790; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.614896; −Σp ln(p) = 0.708289; H = 0.708289/ln(3) = 0.644712; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram batang berikut menunjukan banyak siswa di SD Permata.

Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan:

Banyak siswa kelas 2 SD Permata?
Pilihan: A. 292 siswa
B. 54 siswa
C. 154 siswa
D. 0 siswa
Transkripsi visual: Diagram batang menunjukkan jumlah siswa di SD Permata. Sumbu horizontal: Kelas 1, 2, 3, 4, 5, 6. Sumbu vertikal: 0-70. Batang Kelas 1=57, Kelas 2=kosong, Kelas 3=58, Kelas 4=56, Kelas 5=62, Kelas 6=59.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 67. Soal `a1af57352d757d10ac9304b8`

Nyatakan bilangan berikut dalam bentuk angka.<br><br> Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.

| Opsi | Isi |
|---|---|
| A | 933.403 |
| B | 903.403 |
| C | 930.403 |
| D | 933.430 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Sembilan ratus ribu (900.000) ditambah tiga puluh tiga ribu (33.000) ditambah empat ratus tiga (403) sama dengan 933.403.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `655434819e28044a5c36403bb5d351671a1510db571f4a516c38eee71d2d28b2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2281 |
| 2 | success | valid / verified | knowing | factual | Easy | 2315 |
| 3 | success | valid / verified | knowing | factual | Easy | 2298 |

Run 1 — solusi: Sembilan ratus ribu (900.000) ditambah tiga puluh tiga ribu (33.000) ditambah empat ratus tiga (403) sama dengan 933.403.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerjemahkan representasi verbal bilangan ke dalam bentuk angka standar sesuai dengan nilai tempat yang disebutkan. Ini adalah prosedur langsung yang sudah dipelajari di kelas rendah.. Bukti: Nyatakan bilangan berikut dalam bentuk angka. Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang sistem penamaan bilangan (istilah dan simbol) yang merupakan pengetahuan faktual dasar dalam matematika.. Bukti: Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala yang kompleks. Siswa hanya perlu menuliskan angka berdasarkan kata-kata yang diberikan.. Bukti: Nyatakan bilangan berikut dalam bentuk angka. Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai ratusan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menuliskan bilangan dari nama bilangan adalah keterampilan dasar yang sudah dikuasai sejak kelas 3-4. Tidak ada tuntutan kognitif tinggi. |

Run 2 — solusi: Sembilan ratus ribu (900.000) ditambah tiga puluh tiga ribu (33.000) ditambah empat ratus tiga (403) menghasilkan 933.403.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan representasi verbal bilangan ke dalam bentuk angka (notasi posisional). Ini adalah tugas langsung yang melibatkan pengenalan nilai tempat dan penulisan angka sesuai dengan standar yang dipelajari di kelas 5.. Bukti: Nyatakan bilangan berikut dalam bentuk angka. Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap sistem penulisan bilangan cacah (fakta/simbol) dan bagaimana nilai tempat disusun dalam notasi desimal.. Bukti: Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala yang kompleks; siswa hanya perlu memetakan kata-kata ke dalam posisi digit yang sesuai.. Bukti: Nyatakan bilangan berikut dalam bentuk angka. Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai ratusan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menuliskan bilangan dari nama bilangan adalah keterampilan dasar kelas 5 yang sudah sering dilatih. |

Run 3 — solusi: Sembilan ratus ribu (900.000) ditambah tiga puluh tiga ribu (33.000) ditambah empat ratus tiga (403) menghasilkan 933.403.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan representasi verbal bilangan ke dalam bentuk angka (notasi posisional). Ini adalah tugas langsung yang melibatkan pengenalan nilai tempat dan penulisan simbol angka.. Bukti: Nyatakan bilangan berikut dalam bentuk angka. Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap sistem penamaan bilangan (fakta/istilah) dan aturan penulisan angka berdasarkan nilai tempat.. Bukti: Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau kendala yang kompleks; siswa hanya perlu mengonversi kata-kata menjadi angka.. Bukti: Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengonversi nama bilangan ke angka adalah keterampilan dasar yang diharapkan sudah dikuasai siswa kelas 5. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 93/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.171817; applying=0.828183; reasoning=0.000000 | applying | 0.828183 | 0.417578 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.612873; conceptual=0.371886; procedural=0.015242; metacognitive=0.000000 | factual | 0.612873 | 0.527801 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.918325; Medium=0.079598; Hard=0.002076 | Easy | 0.918325 | 0.266259 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.828183; −Σp ln(p) = 0.458756; H = 0.458756/ln(3) = 0.417578; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.612873; −Σp ln(p) = 0.731687; H = 0.731687/ln(4) = 0.527801; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.918325; −Σp ln(p) = 0.292515; H = 0.292515/ln(3) = 0.266259; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membaca dan Menulis Bilangan Cacah Sampai 1.000.000 dan Menentukan Nilai Tempatnya
Tipe soal: multiple_choice
Stimulus: -
Soal: Nyatakan bilangan berikut dalam bentuk angka.

 Sembilan ratus ribu tiga puluh tiga ribu empat ratus tiga.
Pilihan: A. 933.403
B. 903.403
C. 930.403
D. 933.430
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 68. Soal `ad1de3f95f757ac7d08e4e4d`

Komang mempunyai uang lima ratus enam puluh tujuh ribu rupiah. Bagaimana menulisnya dalam bentuk bilangan?

| Opsi | Isi |
|---|---|
| A | Rp500.067.000,00 |
| B | Rp567.000,00 |
| C | Rp576.000,00 |
| D | Rp56.700,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Lima ratus enam puluh tujuh ribu ditulis sebagai 567.000. Penulisan dalam format mata uang rupiah adalah Rp567.000,00.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6efd8a0c8df3626bc095dcd792bb7cb67d08265e6ae80ddbf14c064b86e3b7c1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2278 |
| 2 | success | valid / verified | knowing | factual | Easy | 2214 |
| 3 | success | valid / verified | knowing | factual | Easy | 2220 |

Run 1 — solusi: Lima ratus enam puluh tujuh ribu ditulis sebagai 567.000. Penulisan dalam format mata uang rupiah adalah Rp567.000,00.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerjemahkan representasi verbal bilangan ke dalam representasi numerik standar. Ini adalah tugas langsung yang melibatkan pengenalan nilai tempat dan simbol bilangan, sehingga masuk dalam domain knowing.. Bukti: Komang mempunyai uang lima ratus enam puluh tujuh ribu rupiah. Bagaimana menulisnya dalam bentuk bilangan?
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami konvensi penulisan bilangan cacah dan simbol mata uang, yang merupakan pengetahuan faktual tentang sistem bilangan.. Bukti: lima ratus enam puluh tujuh ribu
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan rutin bagi siswa kelas 5. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: lima ratus enam puluh tujuh ribu; Rp567.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai ratusan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menuliskan bilangan dari nama bilangan adalah keterampilan dasar yang sudah dikuasai di kelas 5. Tidak ada jebakan atau kompleksitas tambahan. |

Run 2 — solusi: Lima ratus enam puluh tujuh ribu ditulis sebagai 567.000.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk menerjemahkan representasi verbal bilangan ke dalam bentuk angka standar. Ini adalah prosedur langsung yang sudah dipelajari di kelas 5.. Bukti: lima ratus enam puluh tujuh ribu rupiah. Bagaimana menulisnya dalam bentuk bilangan?
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami sistem nilai tempat dan cara penulisan bilangan cacah (fakta/istilah dasar dalam matematika).. Bukti: lima ratus enam puluh tujuh ribu rupiah
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengubah representasi verbal menjadi numerik tanpa langkah tambahan atau integrasi konsep yang kompleks.. Bukti: lima ratus enam puluh tujuh ribu rupiah. Bagaimana menulisnya dalam bentuk bilangan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai ratusan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penulisan bilangan cacah adalah materi dasar kelas 5. Soal tidak menuntut perencanaan atau integrasi, hanya pemahaman langsung terhadap simbol bilangan. |

Run 3 — solusi: Lima ratus enam puluh tujuh ribu ditulis sebagai 567.000.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk menerjemahkan representasi verbal (nama bilangan) ke dalam representasi simbolik (angka). Ini adalah prosedur langsung yang sudah dipelajari di kelas 5.. Bukti: Komang mempunyai uang lima ratus enam puluh tujuh ribu rupiah. Bagaimana menulisnya dalam bentuk bilangan?
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami sistem nilai tempat dan konvensi penulisan angka untuk bilangan cacah sampai 1.000.000.. Bukti: lima ratus enam puluh tujuh ribu
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas rutin yang sangat mendasar bagi siswa kelas 5. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: lima ratus enam puluh tujuh ribu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menuliskan bilangan dari nama bilangan adalah keterampilan dasar yang diharapkan sudah dikuasai sepenuhnya di kelas 5. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 104/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000099; applying=0.999901; reasoning=0.000000 | applying | 0.999901 | 0.000925 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.605761; conceptual=0.380127; procedural=0.014112; metacognitive=0.000000 | factual | 0.605761 | 0.527634 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.917686; Medium=0.079777; Hard=0.002538 | Easy | 0.917686 | 0.269169 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999901; −Σp ln(p) = 0.001016; H = 0.001016/ln(3) = 0.000925; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.605761; −Σp ln(p) = 0.731456; H = 0.731456/ln(4) = 0.527634; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.917686; −Σp ln(p) = 0.295712; H = 0.295712/ln(3) = 0.269169; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Membaca dan Menulis Bilangan Cacah Sampai 1.000.000 dan Menentukan Nilai Tempatnya
Tipe soal: multiple_choice
Stimulus: -
Soal: Komang mempunyai uang lima ratus enam puluh tujuh ribu rupiah. Bagaimana menulisnya dalam bentuk bilangan?
Pilihan: A. Rp500.067.000,00
B. Rp567.000,00
C. Rp576.000,00
D. Rp56.700,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 69. Soal `e7bc3c7cab3ea665b16281b4`

Isilah .... dengan bilangan-bilangan yang urutannya sesuai.<br><br> ....   500.000   700.000   ....   ....

| Opsi | Isi |
|---|---|
| A | 300.000, 900.000, dan 1.000.000 |
| B | 100.000, 900.000, dan 1.100.000 |
| C | 400.000, 800.000, dan 900.000 |
| D | 300.000, 900.000, dan 1.100.000 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola bilangan adalah penambahan 200.000. Bilangan sebelum 500.000 adalah 500.000 - 200.000 = 300.000. Bilangan setelah 700.000 adalah 700.000 + 200.000 = 900.000, dan 900.000 + 200.000 = 1.100.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c4bf2614c88568278c2aea4cd7a2d408a0f0938f10bb22f25f16fb97c47cfc37`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2527 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2545 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2558 |

Run 1 — solusi: Pola bilangan adalah penambahan 200.000. Bilangan sebelum 500.000 adalah 500.000 - 200.000 = 300.000. Bilangan setelah 700.000 adalah 700.000 + 200.000 = 900.000, dan 900.000 + 200.000 = 1.100.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan konstan (200.000) dari dua bilangan yang berurutan, lalu menerapkan pola tersebut untuk mengisi titik-titik. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: 500.000 700.000
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip urutan bilangan dan pola aritmetika sederhana.. Bukti: urutannya sesuai
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola penambahan 200.000 sangat jelas dari dua angka yang diberikan. Siswa hanya perlu melakukan operasi penjumlahan/pengurangan dasar secara berulang tanpa kendala yang rumit.. Bukti: .... 500.000 700.000 .... ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi penjumlahan/pengurangan bilangan cacah sampai 1.000.000. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi pola bilangan adalah materi standar kelas 5. Langkah penyelesaian bersifat linear dan langsung. |

Run 2 — solusi: Pola bilangan memiliki selisih tetap sebesar 200.000 (700.000 - 500.000 = 200.000). Maka, bilangan sebelum 500.000 adalah 500.000 - 200.000 = 300.000. Bilangan setelah 700.000 adalah 700.000 + 200.000 = 900.000, dan berikutnya 900.000 + 200.000 = 1.100.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan tetap (aritmetika sederhana) dari dua angka yang berurutan dan menerapkannya untuk melengkapi urutan tersebut.. Bukti: 500.000 700.000
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep urutan bilangan dan pola bilangan (konseptual) serta prosedur untuk menentukan selisih dan melanjutkan urutan.. Bukti: urutannya sesuai
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola penambahan (selisih 200.000) sangat jelas dari dua angka yang diberikan. Siswa hanya perlu melakukan operasi penjumlahan dan pengurangan dasar secara berulang.. Bukti: .... 500.000 700.000 .... ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan cacah sampai 1.000.000. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menentukan pola bilangan dengan selisih tetap adalah materi dasar yang rutin dan tidak memerlukan perencanaan kompleks. |

Run 3 — solusi: Pola bilangan adalah penambahan 200.000 (700.000 - 500.000 = 200.000). Maka, bilangan sebelum 500.000 adalah 500.000 - 200.000 = 300.000. Bilangan setelah 700.000 adalah 700.000 + 200.000 = 900.000, dan berikutnya 900.000 + 200.000 = 1.100.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pola penambahan konstan dari dua angka yang berurutan (500.000 dan 700.000) untuk menentukan angka lainnya. Ini adalah penerapan prosedur aritmatika dasar dalam konteks pola bilangan.. Bukti: 500.000 700.000
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep urutan bilangan dan pola penambahan (konseptual) yang diimplementasikan melalui prosedur pengurangan dan penjumlahan (prosedural).. Bukti: urutannya sesuai
- Intended difficulty `classify/Easy`: Siswa hanya perlu menentukan selisih antara dua angka yang diketahui (200.000) dan menerapkannya secara konsisten. Jalur penyelesaian sangat jelas dan rutin bagi siswa kelas 5.. Bukti: .... 500.000 700.000 .... ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi pengurangan/penjumlahan bilangan cacah besar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan pola bilangan dengan selisih konstan adalah materi standar kelas 5 yang bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 138/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.004773; applying=0.995227; reasoning=0.000000 | applying | 0.995227 | 0.027553 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.079923; conceptual=0.886649; procedural=0.033428; metacognitive=0.000000 | conceptual | 0.886649 | 0.304560 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.798876; Medium=0.196607; Hard=0.004517 | Easy | 0.798876 | 0.476572 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.995227; −Σp ln(p) = 0.030270; H = 0.030270/ln(3) = 0.027553; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.886649; −Σp ln(p) = 0.422210; H = 0.422210/ln(4) = 0.304560; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.798876; −Σp ln(p) = 0.523568; H = 0.523568/ln(3) = 0.476572; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Mengurutkan dan Membandingkan Bilangan Sampai 1.000.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah .... dengan bilangan-bilangan yang urutannya sesuai.

 .... 500.000 700.000 .... ....
Pilihan: A. 300.000, 900.000, dan 1.000.000
B. 100.000, 900.000, dan 1.100.000
C. 400.000, 800.000, dan 900.000
D. 300.000, 900.000, dan 1.100.000
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 70. Soal `2af433502475b5d052206497`

Sekolah mengadakan kegiatan pengumpulan dana untuk melakukan aksi sosial ke panti asuhan. Kelompok Yohana mengumpulkan Rp345.600,00. Kelompok Komang berhasil mengumpulkan Rp354.500,00. Berapakah dana yang lebih banyak terkumpul?

| Opsi | Isi |
|---|---|
| A | Rp345.600,00 |
| B | Rp700.100,00 |
| C | Rp354.500,00 |
| D | Rp8.900,00 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Membandingkan nilai tempat puluh ribuan dari kedua bilangan: 354.500 memiliki angka 5 pada posisi puluh ribuan, sedangkan 345.600 memiliki angka 4. Karena 5 > 4, maka 354.500 > 345.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `56ddbda6ccff9493a2a1b29a09ca64c895bb8e7902779efb95cbf1a3185e9de3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2441 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3216 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3255 |

Run 1 — solusi: Membandingkan nilai tempat puluh ribuan dari kedua bilangan: 354.500 memiliki angka 5 pada posisi puluh ribuan, sedangkan 345.600 memiliki angka 4. Karena 5 > 4, maka 354.500 > 345.600.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan dua bilangan bulat yang sudah diberikan untuk menentukan mana yang lebih besar. Ini adalah penerapan langsung dari konsep perbandingan bilangan yang sudah dipelajari di kelas 5.. Bukti: Berapakah dana yang lebih banyak terkumpul?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat (place value) dalam bilangan cacah besar, yang merupakan pengetahuan konseptual dasar untuk membandingkan besaran.. Bukti: Rp345.600,00; Rp354.500,00
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan dua angka yang sudah tersedia tanpa perlu melakukan operasi hitung tambahan atau perencanaan langkah yang kompleks. Pilihan pengecoh (distraktor) cukup jelas untuk menguji pemahaman konsep nilai tempat dibandingkan dengan operasi aritmatika lainnya.. Bukti: Kelompok Yohana mengumpulkan Rp345.600,00. Kelompok Komang berhasil mengumpulkan Rp354.500,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai ratusan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan dua bilangan adalah materi dasar kelas 5 yang rutin. Tidak ada kendala atau langkah tambahan yang diperlukan. |

Run 2 — solusi: Membandingkan nilai tempat kedua bilangan: 354.500 memiliki angka 5 pada posisi puluh ribuan, sedangkan 345.600 memiliki angka 4. Karena 5 > 4, maka 354.500 > 345.600.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman nilai tempat untuk membandingkan dua bilangan dalam konteks uang.. Bukti: Berapakah dana yang lebih banyak terkumpul?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konsep nilai tempat (ratus ribuan, puluh ribuan) untuk menentukan besaran bilangan.. Bukti: Kelompok Yohana mengumpulkan Rp345.600,00. Kelompok Komang berhasil mengumpulkan Rp354.500,00.
- Intended difficulty `classify/Easy`: Soal ini adalah tugas rutin membandingkan dua bilangan. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: Berapakah dana yang lebih banyak terkumpul?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai 1.000.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan dua bilangan adalah keterampilan dasar kelas 5 yang langsung dan tidak memerlukan perencanaan tinggi. |

Run 3 — solusi: Membandingkan nilai tempat kedua bilangan: 354.500 > 345.600. Maka, dana yang lebih banyak adalah Rp354.500,00.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perbandingan nilai tempat bilangan cacah untuk menentukan mana yang lebih besar antara dua nilai yang diberikan.. Bukti: Berapakah dana yang lebih banyak terkumpul?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman tentang nilai tempat (ratus ribuan, puluh ribuan, dst) untuk membandingkan besaran dua bilangan.. Bukti: Rp345.600,00; Rp354.500,00
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan dua bilangan yang diberikan tanpa langkah tambahan atau kendala yang kompleks.. Bukti: Kelompok Yohana mengumpulkan Rp345.600,00.; Kelompok Komang berhasil mengumpulkan Rp354.500,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai 1.000.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan dua bilangan adalah kompetensi dasar kelas 5 yang sangat familiar dan tidak memerlukan perencanaan strategi yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 122/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.190398; conceptual=0.784786; procedural=0.024816; metacognitive=0.000000 | conceptual | 0.784786 | 0.431160 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873684; Medium=0.122568; Hard=0.003748 | Easy | 0.873684 | 0.360637 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.784786; −Σp ln(p) = 0.597715; H = 0.597715/ln(4) = 0.431160; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873684; −Σp ln(p) = 0.396200; H = 0.396200/ln(3) = 0.360637; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Mengurutkan dan Membandingkan Bilangan Sampai 1.000.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Sekolah mengadakan kegiatan pengumpulan dana untuk melakukan aksi sosial ke panti asuhan. Kelompok Yohana mengumpulkan Rp345.600,00. Kelompok Komang berhasil mengumpulkan Rp354.500,00. Berapakah dana yang lebih banyak terkumpul?
Pilihan: A. Rp345.600,00
B. Rp700.100,00
C. Rp354.500,00
D. Rp8.900,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 71. Soal `96994f5adee1bd93453d2335`

Ibu akan membeli seragam sekolah seharga Rp450.000,00. Ternyata Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan. Berapakah kurangnya uang ibu?

| Opsi | Isi |
|---|---|
| A | Rp7.000,00 |
| B | Rp47.000,00 |
| C | Rp43.000,00 |
| D | Rp10.000,00 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8de16af05e0fc1a321ca3f46200373b83d4af43c3eea82dca669b00842fe50cb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2504 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2520 |
| 3 | success | valid / verified | applying | procedural | Easy | 2496 |

Run 1 — solusi: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai dari komposisi uang yang dimiliki (dekomposisi bilangan) dan melakukan operasi pengurangan untuk mencari selisih. Ini adalah penerapan konsep nilai tempat dan operasi dasar pada konteks rutin.. Bukti: Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan; Berapakah kurangnya uang ibu?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang komposisi bilangan (nilai tempat) dan prosedur operasi hitung dasar (penjumlahan dan pengurangan).. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas dan rutin bagi siswa kelas 5. Siswa hanya perlu menghitung total uang yang dimiliki lalu menguranginya dari harga barang.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00; 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai ratusan ribu dan operasi hitung dasar (penjumlahan dan pengurangan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi komposisi bilangan dan operasi hitung dasar adalah standar kompetensi kelas 5. Tidak ada kendala kompleks atau langkah yang saling bergantung yang sulit. |

Run 2 — solusi: Uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi nilai nominal uang (komposisi bilangan) dan melakukan pengurangan untuk menemukan selisih. Ini adalah penerapan konsep nilai tempat dan operasi dasar pada konteks rutin.. Bukti: Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan; Berapakah kurangnya uang ibu?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang sistem nilai tempat dan dekomposisi bilangan dalam konteks uang, yang merupakan pengetahuan konseptual.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena melibatkan prosedur rutin yang familiar bagi siswa kelas 5. Langkah-langkahnya jelas: menghitung total uang yang dimiliki, lalu mengurangkannya dari harga barang. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00; 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan cacah sampai 1.000.000 serta pemahaman nilai tempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan operasi hitung uang dan nilai tempat. Soal ini adalah aplikasi langsung dari materi tersebut tanpa kerumitan tambahan. |

Run 3 — solusi: Uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai dari komposisi uang yang diberikan (dekomposisi bilangan) dan melakukan operasi pengurangan untuk mencari selisih. Ini adalah penerapan konsep nilai tempat dan operasi dasar dalam konteks rutin.. Bukti: Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan; Berapakah kurangnya uang ibu?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang komposisi bilangan (nilai tempat) dan prosedur aritmatika dasar untuk menyelesaikan masalah sehari-hari.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena melibatkan prosedur aritmatika dasar yang familiar (perkalian sederhana dan pengurangan) dengan jalur penyelesaian yang sangat jelas dan langsung.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00; 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai ratusan ribu dan operasi hitung dasar (penjumlahan dan pengurangan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 5 sudah terbiasa dengan operasi hitung uang dan nilai tempat. Langkah-langkahnya bersifat rutin dan tidak memerlukan perencanaan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4375`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi nilai dari komposisi uang yang dimiliki (dekomposisi bilangan) dan melakukan operasi pengurangan untuk mencari selisih. Ini adalah penerapan konsep nilai tempat dan operasi dasar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang komposisi bilangan (nilai tempat) dan prosedur operasi hitung dasar (penjumlahan dan pengurangan).
- Intended difficulty `Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas dan rutin bagi siswa kelas 5. Siswa hanya perlu menghitung total uang yang dimiliki lalu menguranginya dari harga barang.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai ratusan ribu dan operasi hitung dasar (penjumlahan dan pengurangan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi komposisi bilangan dan operasi hitung dasar adalah standar kompetensi kelas 5. Tidak ada kendala kompleks atau langkah yang saling bergantung yang sulit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 114/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000002; applying=0.999998; reasoning=0.000000 | applying | 0.999998 | 0.000020 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.469580; conceptual=0.516896; procedural=0.013524; metacognitive=0.000000 | conceptual | 0.516896 | 0.544088 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.911002; Medium=0.083985; Hard=0.005013 | Easy | 0.911002 | 0.290824 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999998; −Σp ln(p) = 0.000022; H = 0.000022/ln(3) = 0.000020; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.516896; −Σp ln(p) = 0.754266; H = 0.754266/ln(4) = 0.544088; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.911002; −Σp ln(p) = 0.319503; H = 0.319503/ln(3) = 0.290824; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Komposisi dan Dekomposisi Bilangan Sampai 1.000.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu akan membeli seragam sekolah seharga Rp450.000,00. Ternyata Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan. Berapakah kurangnya uang ibu?
Pilihan: A. Rp7.000,00
B. Rp47.000,00
C. Rp43.000,00
D. Rp10.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 72. Soal `14407bf745406032cd70e58f`

Tuliskan bilangan berikut dalam bentuk angka, kemudian bacalah.<br><br>c. Bilangan yang merupakan jumlah dari 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan.

| Opsi | Isi |
|---|---|
| A | 857.529, dibaca delapan ratus lima puluh tujuh ribu lima ratus dua puluh sembilan |
| B | 857.295, dibaca delapan ratus lima puluh tujuh ribu dua ratus sembilan puluh lima |
| C | 875.259, dibaca delapan ratus tujuh puluh lima ribu dua ratus lima puluh sembilan |
| D | 857.259, dibaca delapan ratus lima puluh tujuh ribu dua ratus lima puluh sembilan |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 800.000 + 50.000 + 7.000 + 200 + 50 + 9 = 857.259. Dibaca: delapan ratus lima puluh tujuh ribu dua ratus lima puluh sembilan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 5 / Matematika SD Kelas 5. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `16acb6b414cca59ba34930f95b3637b722a8000884ec6a151abd8cc2ff63b0d2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3450 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2504 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2425 |

Run 1 — solusi: 8 ratus ribuan (800.000) + 5 puluh ribuan (50.000) + 7 ribuan (7.000) + 2 ratusan (200) + 5 puluhan (50) + 9 satuan (9) = 857.259.
- Domain kognitif `classify/applying`: Siswa menerapkan pemahaman nilai tempat untuk menyusun bilangan dari komponen-komponen yang diberikan.. Bukti: 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman prinsip nilai tempat (place value) dalam sistem bilangan desimal.. Bukti: 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan
- Intended difficulty `classify/Easy`: Soal bersifat langsung dengan satu langkah penyelesaian. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat sampai ratus ribuan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 5, tugas komposisi bilangan adalah prosedur rutin. |

Run 2 — solusi: Menyusun nilai tempat: 800.000 + 50.000 + 7.000 + 200 + 50 + 9 = 857.259. Dibaca: delapan ratus lima puluh tujuh ribu dua ratus lima puluh sembilan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan prosedur langsung yaitu menyusun angka berdasarkan nilai tempat yang telah diberikan secara eksplisit dalam soal. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Bilangan yang merupakan jumlah dari 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa mengenai sistem nilai tempat (place value) sebagai konsep dasar dalam bilangan cacah.. Bukti: 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan jalur penyelesaian yang jelas. Siswa hanya perlu memetakan setiap nilai tempat ke posisi digit yang sesuai. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan langkah yang kompleks.. Bukti: Tuliskan bilangan berikut dalam bentuk angka, kemudian bacalah.; 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan sampai ratusan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat sampai 1.000.000 adalah standar kurikulum kelas 5. Soal ini adalah latihan rutin yang tidak menuntut penalaran lebih lanjut selain pemahaman notasi angka. |

Run 3 — solusi: Menyusun nilai tempat: 800.000 + 50.000 + 7.000 + 200 + 50 + 9 = 857.259. Dibaca: delapan ratus lima puluh tujuh ribu dua ratus lima puluh sembilan.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan pemahaman nilai tempat (place value) untuk menyusun angka dari bentuk panjang yang diberikan. Ini adalah prosedur rutin yang langsung.. Bukti: Bilangan yang merupakan jumlah dari 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang struktur sistem bilangan desimal dan bagaimana nilai tempat membentuk sebuah bilangan.. Bukti: 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu memetakan setiap nilai tempat ke posisi digit yang sesuai. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat hingga ratusan ribu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 5, menyusun bilangan berdasarkan nilai tempat adalah tugas dasar yang sudah dipelajari sebelumnya. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3964`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa hanya perlu menerapkan prosedur rutin menyusun angka berdasarkan nilai tempat yang diberikan secara eksplisit. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman prinsip nilai tempat (place value) dalam sistem bilangan desimal.
- Intended difficulty `Easy`: Soal bersifat langsung dengan jalur penyelesaian yang jelas. Siswa hanya perlu memetakan setiap nilai tempat ke posisi digit yang sesuai. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan langkah yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat sampai ratus ribuan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas komposisi bilangan berdasarkan nilai tempat adalah materi standar dan rutin untuk kelas 5. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 162/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000002; applying=0.999998; reasoning=0.000000 | applying | 0.999998 | 0.000021 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.021704; conceptual=0.951287; procedural=0.027010; metacognitive=0.000000 | conceptual | 0.951287 | 0.164601 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.808135; Medium=0.184468; Hard=0.007397 | Easy | 0.808135 | 0.473553 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999998; −Σp ln(p) = 0.000023; H = 0.000023/ln(3) = 0.000021; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.951287; −Σp ln(p) = 0.228185; H = 0.228185/ln(4) = 0.164601; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.808135; −Σp ln(p) = 0.520251; H = 0.520251/ln(3) = 0.473553; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 5
Topik: Matematika SD Kelas 5
Subtopik: Komposisi dan Dekomposisi Bilangan Sampai 1.000.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Tuliskan bilangan berikut dalam bentuk angka, kemudian bacalah.

c. Bilangan yang merupakan jumlah dari 8 ratus ribuan, 5 puluh ribuan, 7 ribuan, 2 ratusan, 5 puluhan, dan 9 satuan.
Pilihan: A. 857.529, dibaca delapan ratus lima puluh tujuh ribu lima ratus dua puluh sembilan
B. 857.295, dibaca delapan ratus lima puluh tujuh ribu dua ratus sembilan puluh lima
C. 875.259, dibaca delapan ratus tujuh puluh lima ribu dua ratus lima puluh sembilan
D. 857.259, dibaca delapan ratus lima puluh tujuh ribu dua ratus lima puluh sembilan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
