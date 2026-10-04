# Validasi ulang soal kelas 2 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sd-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 2 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model dipakai sebagai diagnostik; tidak diberikan kembali ke Gemini.

Jumlah soal: 44; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 24, "reasoning": 1, "applying": 19}, "knowledgeDimension": {"factual": 10, "conceptual": 25, "procedural": 9, "metacognitive": 0}, "intendedDifficulty": {"Easy": 38, "Hard": 1, "Medium": 5}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 23, "reasoning": 1, "applying": 19}, "knowledgeDimension": {"factual": 10, "conceptual": 24, "procedural": 9, "metacognitive": 0}, "intendedDifficulty": {"Easy": 37, "Hard": 1, "Medium": 5}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 43, "revision_required": 1}`.
Run awal sukses: 132/132; adjudikasi: 13; token sukses tercatat: 452,791.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 38 | 37 | [Easy.json](difficulty/Easy.json) |
| Medium | 5 | 5 | [Medium.json](difficulty/Medium.json) |
| Hard | 1 | 1 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `2bf12b3f27f51d2f775ff81f`

Lengkapi urutan bilangan di bawah ini.<br><br>28 ... 30 ... ...

| Opsi | Isi |
|---|---|
| A | 27, 31, 32 |
| B | 29, 30, 31 |
| C | 29, 31, 32 |
| D | 29, 31, 33 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Urutan bilangan adalah 28, 29, 30, 31, 32. Titik-titik yang kosong harus diisi dengan bilangan yang berurutan setelah 28 dan setelah 30, yaitu 29, 31, dan 32.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9677e699a5ffb0ca2d0cba7e47916de77a2fd949c87e625105831929fe73a745`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2313 |
| 2 | success | valid / verified | knowing | factual | Easy | 2317 |
| 3 | success | valid / verified | knowing | factual | Easy | 2300 |

Run 1 — solusi: Urutan bilangan adalah 28, 29, 30, 31, 32. Titik-titik yang kosong harus diisi dengan bilangan yang berurutan setelah 28 dan setelah 30, yaitu 29, 31, dan 32.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali pola urutan bilangan cacah sederhana dan mengisi bagian yang hilang, yang merupakan prosedur langsung dalam pemahaman bilangan kelas 2.. Bukti: Lengkapi urutan bilangan di bawah ini. 28 ... 30 ... ...
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang urutan bilangan cacah dan konsep dasar berhitung maju.. Bukti: 28 ... 30 ... ...
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2. Tidak ada kendala yang berinteraksi atau perencanaan kompleks; siswa hanya perlu melanjutkan urutan bilangan 28, 29, 30, 31, 32.. Bukti: 28 ... 30 ... ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan berhitung maju dan mengenal urutan bilangan cacah hingga 50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengisi urutan bilangan adalah materi standar kelas 2 yang bersifat rutin dan tidak memerlukan penalaran tingkat tinggi. |

Run 2 — solusi: Urutan bilangan adalah 28, 29, 30, 31, 32. Titik-titik yang kosong diisi dengan 29, 31, dan 32.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali pola urutan bilangan cacah sederhana (bertambah 1) dan melengkapi bagian yang hilang. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Lengkapi urutan bilangan di bawah ini. 28 ... 30 ... ...
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar matematika) dalam rentang sampai 50.. Bukti: 28 ... 30 ... ...
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2. Pola urutan bilangan 28, 29, 30, 31, 32 adalah materi rutin yang familiar. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: 28 ... 30 ... ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang dan mengurutkan bilangan 1-50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan adalah kompetensi dasar kelas 2. Soal ini tidak menuntut penalaran lebih lanjut selain melanjutkan urutan yang sudah jelas. |

Run 3 — solusi: Urutan bilangan adalah 28, 29, 30, 31, 32. Titik-titik yang kosong diisi dengan 29, 31, dan 32.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali pola urutan bilangan cacah sederhana (bertambah satu) dan melengkapinya. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Lengkapi urutan bilangan di bawah ini. 28 ... 30 ... ...
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar matematika) dalam rentang sampai 50.. Bukti: 28 ... 30 ... ...
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2. Pola urutan bilangan (n+1) adalah materi rutin yang familiar. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: 28 ... 30 ... ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang urutan bilangan cacah sampai 50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan adalah kompetensi dasar kelas 2. Soal ini tidak menuntut penalaran lebih lanjut selain melanjutkan urutan yang sudah jelas. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.998333; applying=0.001667; reasoning=0.000000 | knowing | 0.998333 | 0.011221 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.589570; conceptual=0.385386; procedural=0.025044; metacognitive=0.000000 | factual | 0.589570 | 0.556386 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.871177; Medium=0.126290; Hard=0.002533 | Easy | 0.871177 | 0.361004 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998333; −Σp ln(p) = 0.012328; H = 0.012328/ln(3) = 0.011221; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.589570; −Σp ln(p) = 0.771315; H = 0.771315/ln(4) = 0.556386; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.871177; −Σp ln(p) = 0.396604; H = 0.396604/ln(3) = 0.361004; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Menghitung, Membaca, dan Menulis Bilangan sampai dengan 50
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi urutan bilangan di bawah ini.

28 ... 30 ... ...
Pilihan: A. 27, 31, 32
B. 29, 30, 31
C. 29, 31, 32
D. 29, 31, 33
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `bffdfbd5e63e7fbc426dd6b7`

35 dibaca ....

| Opsi | Isi |
|---|---|
| A | lima puluh tiga |
| B | empat puluh lima |
| C | tiga puluh lima |
| D | tiga puluh enam |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Angka 35 terdiri dari 3 puluhan dan 5 satuan, sehingga dibaca tiga puluh lima.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d2f538700945bada8a01683db66eb3ab7bf8ef12c2d5e40a4aa8b3ca2af47e15`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2839 |
| 2 | success | valid / verified | knowing | factual | Easy | 2155 |
| 3 | success | valid / verified | knowing | factual | Easy | 2160 |

Run 1 — solusi: Angka 35 terdiri dari 3 puluhan dan 5 satuan, sehingga dibaca tiga puluh lima.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bilangan dari simbol angka yang diberikan tanpa memerlukan prosedur atau penalaran tambahan.. Bukti: 35 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai nama bilangan dalam sistem numerasi.. Bukti: 35 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas pengenalan langsung nama bilangan yang merupakan materi dasar kelas 2. Tidak ada langkah kompleks atau perencanaan yang diperlukan.. Bukti: 35 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan sampai 50 adalah kompetensi dasar kelas 2 yang bersifat rutin. |

Run 2 — solusi: Angka 35 terdiri dari angka 3 di posisi puluhan dan 5 di posisi satuan, sehingga dibaca 'tiga puluh lima'.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk membaca atau menyebutkan nama bilangan berdasarkan simbol angka yang diberikan. Ini adalah tugas pengenalan langsung terhadap simbol bilangan.. Bukti: 35 dibaca ....
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui fakta tentang bagaimana simbol angka (35) dipetakan ke dalam nama bilangan dalam bahasa Indonesia.. Bukti: 35 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau strategi yang perlu dipilih. Ini adalah pengenalan langsung.. Bukti: 35 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan dan nama bilangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan dua digit adalah kompetensi dasar yang diharapkan sudah dikuasai di kelas 2. |

Run 3 — solusi: Angka 35 terdiri dari angka 3 di posisi puluhan (tiga puluh) dan angka 5 di posisi satuan (lima), sehingga dibaca tiga puluh lima.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali simbol angka dan menyebutkan nama bilangannya sesuai dengan sistem nilai tempat yang sudah dipelajari di kelas 2.. Bukti: 35 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai nama bilangan dan simbol angka.. Bukti: 35 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan pengenalan langsung terhadap simbol angka yang sudah dipelajari di kelas 2.. Bukti: 35 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan 1-50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan dua digit adalah kompetensi dasar kelas 2 yang bersifat rutin dan tidak memerlukan langkah penyelesaian kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 68/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.985305; applying=0.014695; reasoning=0.000000 | knowing | 0.985305 | 0.069726 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.815266; conceptual=0.166377; procedural=0.018357; metacognitive=0.000000 | factual | 0.815266 | 0.388297 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.902393; Medium=0.095432; Hard=0.002175 | Easy | 0.902393 | 0.300576 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.985305; −Σp ln(p) = 0.076602; H = 0.076602/ln(3) = 0.069726; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.815266; −Σp ln(p) = 0.538294; H = 0.538294/ln(4) = 0.388297; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.902393; −Σp ln(p) = 0.330216; H = 0.330216/ln(3) = 0.300576; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Menghitung, Membaca, dan Menulis Bilangan sampai dengan 50
Tipe soal: multiple_choice
Stimulus: -
Soal: 35 dibaca ....
Pilihan: A. lima puluh tiga
B. empat puluh lima
C. tiga puluh lima
D. tiga puluh enam
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `84fcc60564bf4fa76e2051cf`

Isilah titik-titik berikut dengan bilangan yang tepat.<br><br>24 = ... puluhan + ... satuan

| Opsi | Isi |
|---|---|
| A | 4 puluhan + 2 satuan |
| B | 2 puluhan + 4 satuan |
| C | 2 puluhan + 40 satuan |
| D | 20 puluhan + 4 satuan |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bilangan 24 terdiri dari angka 2 di tempat puluhan dan angka 4 di tempat satuan. Jadi, 24 = 2 puluhan + 4 satuan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `00b4c0f8771d77ea72b415086ca707711f88d164729dfcd6ff2126c967862989`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2238 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2234 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2216 |

Run 1 — solusi: Bilangan 24 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 4 di tempat satuan (bernilai 4). Maka, 24 = 2 puluhan + 4 satuan.
- Domain kognitif `classify/applying`: Siswa diminta untuk menguraikan bilangan dua angka berdasarkan nilai tempatnya. Ini adalah penerapan langsung dari konsep nilai tempat yang sudah dipelajari di kelas 2.. Bukti: 24 = ... puluhan + ... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) pada bilangan dua angka, yang merupakan konsep dasar dalam aritmatika.. Bukti: 24 = ... puluhan + ... satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi digit puluhan dan satuan dari bilangan 24 tanpa langkah tambahan atau integrasi yang kompleks.. Bukti: 24 = ... puluhan + ... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat bilangan dua angka (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, menguraikan bilangan dua angka menjadi puluhan dan satuan adalah materi standar yang bersifat rutin dan tidak memerlukan perencanaan langkah yang rumit. |

Run 2 — solusi: Bilangan 24 terdiri dari angka 2 di posisi puluhan (bernilai 20) dan angka 4 di posisi satuan (bernilai 4). Maka, 24 = 2 puluhan + 4 satuan.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi nilai tempat dari angka-angka dalam bilangan dua digit (24). Ini adalah prosedur langsung yang sudah dipelajari di kelas 2 mengenai dekomposisi bilangan berdasarkan nilai tempat.. Bukti: 24 = ... puluhan + ... satuan
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) sebagai struktur dasar bilangan dua digit.. Bukti: 24 = ... puluhan + ... satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau kendala yang kompleks; siswa hanya perlu mengenali posisi digit.. Bukti: 24 = ... puluhan + ... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat adalah kurikulum standar kelas 2. Soal ini menguji pemahaman dasar tanpa memerlukan perencanaan atau integrasi langkah yang rumit. |

Run 3 — solusi: Bilangan 24 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 4 di tempat satuan (bernilai 4). Maka, 24 = 2 puluhan + 4 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menguraikan bilangan dua angka berdasarkan nilai tempatnya. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: 24 = ... puluhan + ... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep nilai tempat (puluhan dan satuan) sebagai elemen dasar dalam sistem bilangan.. Bukti: 24 = ... puluhan + ... satuan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2. Siswa hanya perlu mengidentifikasi digit puluhan dan satuan dari bilangan 24 tanpa langkah tambahan atau kendala yang kompleks.. Bukti: 24 = ... puluhan + ... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat bilangan dua angka (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menguraikan bilangan dua angka menjadi puluhan dan satuan adalah materi standar kelas 2 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3532`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengidentifikasi dan menempatkan digit bilangan ke dalam kategori nilai tempat yang sesuai. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat (puluhan dan satuan) sebagai struktur dasar bilangan dua angka.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan sangat mendasar bagi siswa kelas 2. Tidak ada langkah yang saling bergantung, kendala yang kompleks, atau kebutuhan untuk merencanakan strategi. Siswa hanya perlu mengenali posisi digit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat bilangan dua angka (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menguraikan bilangan dua angka menjadi puluhan dan satuan adalah materi standar kelas 2 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 84/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.942816; applying=0.057184; reasoning=0.000000 | knowing | 0.942816 | 0.199477 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.458244; conceptual=0.502316; procedural=0.039440; metacognitive=0.000000 | conceptual | 0.502316 | 0.599410 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.905282; Medium=0.092917; Hard=0.001800 | Easy | 0.905282 | 0.293313 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.942816; −Σp ln(p) = 0.219148; H = 0.219148/ln(3) = 0.199477; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.502316; −Σp ln(p) = 0.830959; H = 0.830959/ln(4) = 0.599410; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.905282; −Σp ln(p) = 0.322237; H = 0.322237/ln(3) = 0.293313; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Nilai Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik berikut dengan bilangan yang tepat.

24 = ... puluhan + ... satuan
Pilihan: A. 4 puluhan + 2 satuan
B. 2 puluhan + 4 satuan
C. 2 puluhan + 40 satuan
D. 20 puluhan + 4 satuan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `120f51a1f7135cf30273aba8`

Isilah dengan bilangan yang tepat.<br><br>28 =    puluhan +    satuan

| Opsi | Isi |
|---|---|
| A | 20 puluhan + 8 satuan |
| B | 2 puluhan + 8 satuan |
| C | 2 puluhan + 80 satuan |
| D | 8 puluhan + 2 satuan |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bilangan 28 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 8 di tempat satuan (bernilai 8). Maka, 28 = 2 puluhan + 8 satuan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `49b1f49d43bbde036ae2f749cd0569466e0f6c3fb4e9080a934dfeee4a5653a8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2208 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2215 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2206 |

Run 1 — solusi: Bilangan 28 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 8 di tempat satuan (bernilai 8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menguraikan bilangan dua digit berdasarkan nilai tempatnya. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2, sehingga termasuk dalam domain knowing.. Bukti: 28 =    puluhan +    satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) yang merupakan konsep dasar dalam sistem bilangan.. Bukti: 28 =    puluhan +    satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: 28 =    puluhan +    satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menguraikan bilangan 28 menjadi puluhan dan satuan adalah materi standar kelas 2 yang bersifat prosedural dan familiar. |

Run 2 — solusi: Bilangan 28 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 8 di tempat satuan (bernilai 8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menguraikan bilangan dua digit berdasarkan nilai tempatnya. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2, sehingga termasuk dalam domain knowing.. Bukti: 28 =    puluhan +    satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar dalam sistem bilangan desimal.. Bukti: 28 =    puluhan +    satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau strategi kompleks yang harus dipilih.. Bukti: 28 =    puluhan +    satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menguraikan bilangan 28 menjadi 2 puluhan dan 8 satuan adalah materi standar kelas 2 yang bersifat prosedural dan familiar. |

Run 3 — solusi: Bilangan 28 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 8 di tempat satuan (bernilai 8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menguraikan bilangan dua digit berdasarkan nilai tempatnya. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2, sehingga termasuk dalam domain knowing.. Bukti: 28 =    puluhan +    satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar dalam sistem bilangan.. Bukti: 28 =    puluhan +    satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: 28 =    puluhan +    satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menguraikan bilangan dua digit menjadi puluhan dan satuan adalah materi standar kelas 2 yang bersifat prosedural dan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 74/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.985933; applying=0.014067; reasoning=0.000000 | knowing | 0.985933 | 0.067312 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.708407; conceptual=0.253895; procedural=0.037698; metacognitive=0.000000 | factual | 0.708407 | 0.516370 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.919194; Medium=0.079072; Hard=0.001734 | Easy | 0.919194 | 0.263160 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.985933; −Σp ln(p) = 0.073949; H = 0.073949/ln(3) = 0.067312; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.708407; −Σp ln(p) = 0.715841; H = 0.715841/ln(4) = 0.516370; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.919194; −Σp ln(p) = 0.289111; H = 0.289111/ln(3) = 0.263160; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Nilai Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah dengan bilangan yang tepat.

28 = puluhan + satuan
Pilihan: A. 20 puluhan + 8 satuan
B. 2 puluhan + 8 satuan
C. 2 puluhan + 80 satuan
D. 8 puluhan + 2 satuan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `ed47e9294466e94e73d2b69c`

Malosi, Kira, dan Lili sedang memegang kartu bilangan. Bilangan Malosi 3 lebihnya dari bilangan Lili. Bilangan Lili 2 kurangnya dari bilangan Kira. Kira memegang kartu bilangan 34.<br><br>Urutkan bilangan mereka dari nilai terkecil ke terbesar.

| Opsi | Isi |
|---|---|
| A | Lili 36, Kira 34, Malosi 39 |
| B | Lili 32, Malosi 34, Kira 35 |
| C | Lili 32, Kira 34, Malosi 35 |
| D | Kira 32, Lili 34, Malosi 35 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Kira = 34. Lili = 34 - 2 = 32. Malosi = 32 + 3 = 35. Urutan dari terkecil ke terbesar: Lili (32), Kira (34), Malosi (35).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6812b878c72c527a6bbfae1e2f2f74c2c3ac47d4da7d985b5f62bcff227ad4ff`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2500 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 2500 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 2458 |

Run 1 — solusi: Kira = 34. Lili = 34 - 2 = 32. Malosi = 32 + 3 = 35. Urutan dari terkecil ke terbesar: Lili (32), Kira (34), Malosi (35).
- Domain kognitif `classify/applying`: Siswa perlu mengolah informasi relasional untuk menentukan nilai setiap anak sebelum mengurutkannya. Ini melibatkan penerapan konsep operasi dasar (penjumlahan/pengurangan) dalam konteks rutin, sehingga masuk dalam domain applying.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.; Urutkan bilangan mereka dari nilai terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antarbilangan (lebih dari/kurang dari) dan menerjemahkannya ke dalam operasi aritmatika, yang merupakan pemahaman konseptual.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa melakukan dua langkah perhitungan berantai (menentukan Lili, lalu Malosi) dan mengurutkan hasilnya. Meskipun prosedurnya rutin, ketergantungan langkah (nilai Malosi bergantung pada nilai Lili yang harus dihitung terlebih dahulu) memberikan tuntutan sedang bagi kelas 2.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.; Urutkan bilangan mereka dari nilai terkecil ke terbesar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan dua angka, pemahaman konsep 'lebih dari' dan 'kurang dari'. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah belajar membandingkan dan mengurutkan bilangan, namun melakukan perhitungan berantai untuk menentukan nilai sebelum mengurutkan meningkatkan beban kognitif ke tingkat menengah. |

Run 2 — solusi: Kira = 34. Lili = 34 - 2 = 32. Malosi = 32 + 3 = 35. Urutan dari terkecil ke terbesar: Lili (32), Kira (34), Malosi (35).
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi relasional antarbilangan untuk menentukan nilai masing-masing sebelum mengurutkannya. Ini melampaui sekadar mengingat fakta atau prosedur rutin satu langkah, karena melibatkan penalaran logis untuk menghubungkan tiga variabel.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.; Urutkan bilangan mereka dari nilai terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan 'lebih dari' dan 'kurang dari' serta bagaimana hubungan tersebut membentuk nilai bilangan dalam konteks perbandingan.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.
- Intended difficulty `classify/Hard`: Soal ini menuntut perencanaan langkah yang saling bergantung (menentukan Lili dulu, baru Malosi) dan integrasi informasi. Bagi siswa kelas 2, mengelola tiga variabel dengan relasi yang berbeda dan mengurutkannya adalah tugas yang menantang.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan dasar (hingga 50), pemahaman konsep urutan bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 2 harus membangun sendiri urutan langkah penyelesaian (Kira -> Lili -> Malosi) dan mengintegrasikan relasi yang diberikan tanpa bantuan langkah perantara. |

Run 3 — solusi: Kira=34. Lili=34-2=32. Malosi=32+3=35. Urutan terkecil ke terbesar: Lili(32), Kira(34), Malosi(35).
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi yang saling bergantung untuk menentukan nilai setiap anak sebelum mengurutkannya. Ini melampaui sekadar membaca atau menjalankan prosedur langsung, karena siswa harus membangun hubungan antarbilangan secara berurutan.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang hubungan antarbilangan (lebih dari/kurang dari) dan prinsip pengurutan bilangan, yang merupakan konsep relasional dalam matematika.. Bukti: Urutkan bilangan mereka dari nilai terkecil ke terbesar.
- Intended difficulty `classify/Hard`: Soal ini menuntut perencanaan langkah yang saling bergantung (menentukan Lili dulu, baru Malosi) dan integrasi informasi sebelum melakukan pengurutan. Bagi siswa kelas 2, ini memerlukan penalaran yang lebih dari sekadar prosedur rutin satu langkah.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan dua digit, pemahaman konsep perbandingan (lebih dari/kurang dari). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 2 harus mengelola ketergantungan antarvariabel (Lili bergantung pada Kira, Malosi bergantung pada Lili) dan melakukan pengurutan akhir. Ini adalah tuntutan kognitif yang tinggi untuk tingkat kelas 2. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "reasoning": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 1, "Hard": 2} | majority_2_of_3 / adjudicated | Hard |

Adjudikasi AI: `success`; token `4252`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa harus mengintegrasikan informasi relasional yang diberikan untuk menentukan nilai setiap anak secara berurutan sebelum melakukan pengurutan. Proses ini memerlukan penalaran untuk menghubungkan variabel-variabel yang saling bergantung, bukan sekadar menjalankan prosedur rutin satu langkah.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan 'lebih dari' dan 'kurang dari' serta bagaimana hubungan tersebut membentuk nilai bilangan dalam konteks perbandingan dan pengurutan.
- Intended difficulty `Hard`: Meskipun operasi hitungnya sederhana, siswa kelas 2 harus merencanakan langkah yang saling bergantung (Kira -> Lili -> Malosi) dan mengintegrasikan relasi tanpa bantuan langkah perantara. Mengelola tiga variabel dengan relasi yang berbeda dan mengurutkannya adalah tugas yang menantang bagi tingkat kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan dasar (hingga 50), pemahaman konsep urutan bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 harus membangun sendiri urutan langkah penyelesaian dan mengintegrasikan relasi yang diberikan. Ketergantungan antarvariabel (Lili bergantung pada Kira, Malosi bergantung pada Lili) membuat soal ini memiliki tuntutan perencanaan yang tinggi untuk kelas 2. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 127/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.028879; conceptual=0.933265; procedural=0.037856; metacognitive=0.000000 | conceptual | 0.933265 | 0.209741 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.666447; Medium=0.326729; Hard=0.006825 | Easy | 0.666447 | 0.609827 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.933265; −Σp ln(p) = 0.290762; H = 0.290762/ln(4) = 0.209741; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.666447; −Σp ln(p) = 0.669963; H = 0.669963/ln(3) = 0.609827; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Membandingkan Dua Bilangan atau Lebih
Tipe soal: multiple_choice
Stimulus: -
Soal: Malosi, Kira, dan Lili sedang memegang kartu bilangan. Bilangan Malosi 3 lebihnya dari bilangan Lili. Bilangan Lili 2 kurangnya dari bilangan Kira. Kira memegang kartu bilangan 34.

Urutkan bilangan mereka dari nilai terkecil ke terbesar.
Pilihan: A. Lili 36, Kira 34, Malosi 39
B. Lili 32, Malosi 34, Kira 35
C. Lili 32, Kira 34, Malosi 35
D. Kira 32, Lili 34, Malosi 35
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Hard", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `f8b50899e6f07b82441104f3`

Perhatikan keempat bilangan berikut. 25 12 35 21<br><br>Bilangan mana yang paling besar?

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 35 |
| C | 25 |
| D | 21 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan nilai tempat puluhan dari bilangan 25, 12, 35, dan 21. Bilangan 35 memiliki angka puluhan 3, yang merupakan nilai terbesar dibandingkan angka puluhan 2, 1, dan 2 dari bilangan lainnya.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `554f9762d1d2359d244e0954b6163dc201d7ad343fca69302379839e4a42df3e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2282 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2326 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2267 |

Run 1 — solusi: Membandingkan nilai tempat puluhan dari bilangan 25, 12, 35, dan 21. Bilangan 35 memiliki angka puluhan 3, yang merupakan nilai terbesar dibandingkan angka puluhan 2, 1, dan 2 dari bilangan lainnya.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membandingkan nilai tempat puluhan dari sekumpulan bilangan untuk menentukan mana yang terbesar. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Bilangan mana yang paling besar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat (puluhan dan satuan) sebagai konsep dasar untuk membandingkan besaran bilangan.. Bukti: 25 12 35 21
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan nilai puluhan dari empat bilangan yang diberikan. Tidak ada langkah tersembunyi atau kendala yang berinteraksi.. Bukti: Perhatikan keempat bilangan berikut. 25 12 35 21; Bilangan mana yang paling besar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan untuk bilangan dua angka. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan dua angka adalah materi standar kelas 2. Soal ini tidak menuntut perencanaan kompleks, hanya pengenalan langsung terhadap nilai tempat. |

Run 2 — solusi: Membandingkan nilai tempat puluhan dari bilangan 25, 12, 35, dan 21. Bilangan 35 memiliki angka puluhan 3, yang merupakan nilai terbesar dibandingkan 2 (pada 25 dan 21) dan 1 (pada 12). Maka, 35 adalah bilangan terbesar.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membandingkan nilai tempat puluhan dari sekumpulan bilangan dua digit untuk menentukan mana yang terbesar. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Perhatikan keempat bilangan berikut. 25 12 35 21; Bilangan mana yang paling besar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat (puluhan dan satuan) sebagai konsep dasar untuk membandingkan besaran bilangan.. Bukti: 25 12 35 21; Bilangan mana yang paling besar?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan angka puluhan dari empat bilangan yang diberikan. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: 25 12 35 21; Bilangan mana yang paling besar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan dua digit adalah materi standar kelas 2. Tugas ini merupakan penerapan langsung dari konsep nilai tempat tanpa memerlukan perencanaan langkah tambahan. |

Run 3 — solusi: Membandingkan nilai tempat puluhan dari bilangan 25, 12, 35, dan 21. Angka puluhan adalah 2, 1, 3, dan 2. Nilai puluhan terbesar adalah 3, sehingga 35 adalah bilangan terbesar.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi bilangan terbesar dari sekumpulan bilangan dua digit. Ini adalah prosedur langsung membandingkan nilai tempat puluhan, yang merupakan tugas rutin bagi siswa kelas 2.. Bukti: Bilangan mana yang paling besar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat (puluhan dan satuan) untuk membandingkan besaran bilangan.. Bukti: 25 12 35 21
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu membandingkan nilai puluhan dari empat bilangan yang diberikan. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: 25 12 35 21; Bilangan mana yang paling besar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan dua digit adalah materi standar kelas 2. Tugas ini tidak memerlukan perencanaan langkah atau integrasi konsep yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999565; applying=0.000435; reasoning=0.000000 | knowing | 0.999565 | 0.003459 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.430637; conceptual=0.532735; procedural=0.036628; metacognitive=0.000000 | conceptual | 0.532735 | 0.591081 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.901656; Medium=0.096328; Hard=0.002016 | Easy | 0.901656 | 0.301528 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999565; −Σp ln(p) = 0.003800; H = 0.003800/ln(3) = 0.003459; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.532735; −Σp ln(p) = 0.819413; H = 0.819413/ln(4) = 0.591081; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.901656; −Σp ln(p) = 0.331262; H = 0.331262/ln(3) = 0.301528; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Membandingkan Dua Bilangan atau Lebih
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan keempat bilangan berikut. 25 12 35 21

Bilangan mana yang paling besar?
Pilihan: A. 12
B. 35
C. 25
D. 21
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `76bd2315ce21573dfa2ea8d7`

Perhatikan bilangan berikut. 13 11 18<br><br>Urutan mulai dari bilangan terkecil: .... , .... , ....

| Opsi | Isi |
|---|---|
| A | 18, 13, 11 |
| B | 11, 13, 18 |
| C | 13, 11, 18 |
| D | 11, 18, 13 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan nilai tempat puluhan dan satuan dari 13, 11, 18. Ketiganya memiliki puluhan yang sama (1). Membandingkan angka satuan: 1, 3, 8. Urutan dari terkecil ke terbesar adalah 1, 3, 8. Maka urutan bilangan adalah 11, 13, 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c93e31b8b449b410e75bd2906351b0fc0a2c7f40bc9ad1ec9b099286724e63f8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2199 |
| 2 | success | valid / verified | applying | procedural | Easy | 2368 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2350 |

Run 1 — solusi: Membandingkan nilai tempat puluhan (semua 1) dan satuan (3, 1, 8). Urutan dari terkecil: 1 (dari 11), 3 (dari 13), 8 (dari 18). Jadi, 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur membandingkan dan mengurutkan bilangan cacah dua angka yang sudah dipelajari di kelas 2. Ini adalah penerapan langsung dari konsep nilai tempat.. Bukti: Urutan mulai dari bilangan terkecil: .... , .... , ....; 13 11 18
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma pengurutan bilangan berdasarkan nilai tempat.. Bukti: Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan tiga bilangan dua angka yang sederhana dan mengurutkannya. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan cacah sampai 20 dan membandingkan dua bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah standar kompetensi kelas 2 yang bersifat rutin dan langsung. |

Run 2 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 (1 puluhan, 1 satuan), 13 (1 puluhan, 3 satuan), 18 (1 puluhan, 8 satuan). Karena puluhan sama, urutkan berdasarkan satuan: 1 < 3 < 8. Maka urutan terkecil ke terbesar adalah 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan tiga bilangan dua angka yang diberikan. Tugas ini merupakan penerapan langsung dari konsep perbandingan bilangan yang sudah dipelajari di kelas 2, sehingga termasuk domain applying.. Bukti: Urutan mulai dari bilangan terkecil: .... , .... , ....; 13 11 18
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip urutan bilangan (konseptual) dan prosedur membandingkan nilai tempat untuk menentukan urutan (prosedural). Karena fokus utamanya adalah menerapkan prosedur pengurutan, ini diklasifikasikan sebagai procedural.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan tiga bilangan dua angka yang sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan dua angka dan perbandingan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah tugas standar kelas 2. Tidak ada kompleksitas tambahan. |

Run 3 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 (1 puluhan, 1 satuan), 13 (1 puluhan, 3 satuan), 18 (1 puluhan, 8 satuan). Karena puluhan sama, urutkan berdasarkan satuan: 1 < 3 < 8. Maka urutan terkecil adalah 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan tiga bilangan dua angka yang diberikan. Tugas ini merupakan penerapan langsung dari konsep perbandingan bilangan yang sudah dipelajari di kelas 2, yaitu membandingkan nilai tempat puluhan dan satuan untuk menentukan urutan.. Bukti: Urutan mulai dari bilangan terkecil: .... , .... , ....; 13 11 18
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan bilangan (konsep lebih kecil/lebih besar) dan prosedur membandingkan bilangan dua angka.. Bukti: Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini termasuk kategori mudah karena siswa hanya perlu membandingkan tiga bilangan dua angka yang sederhana. Prosedurnya rutin dan tidak memerlukan perencanaan langkah yang kompleks.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan dua angka (puluhan dan satuan) dan konsep perbandingan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, mengurutkan tiga bilangan dua angka adalah tugas standar yang rutin dan langsung, tidak memerlukan penalaran tingkat tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3867`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur perbandingan bilangan yang sudah dipelajari untuk mengurutkan tiga bilangan dua angka. Ini adalah penerapan langsung dari konsep nilai tempat.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang algoritma pengurutan bilangan berdasarkan nilai tempat.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan tiga bilangan dua angka yang sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan dua angka dan perbandingan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah tugas standar kelas 2 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 89/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.997263; applying=0.002737; reasoning=0.000000 | knowing | 0.997263 | 0.017191 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.281102; conceptual=0.696463; procedural=0.022434; metacognitive=0.000000 | conceptual | 0.696463 | 0.500511 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.871596; Medium=0.125710; Hard=0.002694 | Easy | 0.871596 | 0.360836 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997263; −Σp ln(p) = 0.018887; H = 0.018887/ln(3) = 0.017191; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.696463; −Σp ln(p) = 0.693855; H = 0.693855/ln(4) = 0.500511; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.871596; −Σp ln(p) = 0.396418; H = 0.396418/ln(3) = 0.360836; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bilangan berikut. 13 11 18

Urutan mulai dari bilangan terkecil: .... , .... , ....
Pilihan: A. 18, 13, 11
B. 11, 13, 18
C. 13, 11, 18
D. 11, 18, 13
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `5bde2df393a963ef6574cd85`

Hitunglah operasi penjumlahan berikut dengan menghitung maju.<br><br>11 + 9 = .…

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 19 |
| C | 21 |
| D | 20 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mulai dari 11, hitung maju 9 langkah: 12, 13, 14, 15, 16, 17, 18, 19, 20.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ea87c510906035a7f15c41c53a858137e00aa8ce33724a7b108fd5bfbed33776`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3157 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2229 |
| 3 | success | valid / verified | applying | procedural | Easy | 2253 |

Run 1 — solusi: Mulai dari 11, hitung maju 9 langkah: 12, 13, 14, 15, 16, 17, 18, 19, 20.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur penjumlahan dasar dengan metode menghitung maju yang sudah dipelajari, sehingga masuk kategori knowing.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju.
- Dimensi pengetahuan `classify/procedural`: Soal menguji penerapan algoritma atau metode menghitung maju untuk menyelesaikan penjumlahan.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju.
- Intended difficulty `classify/Easy`: Soal adalah penerapan langsung prosedur penjumlahan dasar. Tidak ada kendala kompleks atau perencanaan strategi yang diperlukan.. Bukti: 11 + 9 = .…

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan kemampuan berhitung maju. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dengan metode hitung maju adalah materi standar kelas 2 yang bersifat rutin dan langsung. |

Run 2 — solusi: Menghitung maju 9 langkah dari 11: 12, 13, 14, 15, 16, 17, 18, 19, 20.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur penjumlahan sederhana dengan metode spesifik (menghitung maju) yang merupakan prosedur rutin di kelas 2.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 11 + 9 = .…
- Dimensi pengetahuan `classify/procedural`: Siswa diminta menerapkan algoritma atau metode penghitungan (menghitung maju) untuk menyelesaikan operasi penjumlahan.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 11 + 9 = .…
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari prosedur menghitung maju yang familiar bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau kendala kompleks.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 11 + 9 = .…

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan berhitung maju dari bilangan dua digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 11 + 9 dengan metode menghitung maju adalah materi standar kelas 2 yang bersifat rutin dan langsung. |

Run 3 — solusi: Menghitung maju 9 langkah dari 11: 12, 13, 14, 15, 16, 17, 18, 19, 20. Hasilnya adalah 20.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan sederhana menggunakan strategi menghitung maju yang sudah dipelajari di kelas 2.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 11 + 9 = .…
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma atau metode penjumlahan (menghitung maju) sebagai teknik dasar.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju.
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari prosedur penjumlahan dasar yang familiar bagi siswa kelas 2. Jalur penyelesaiannya tunggal dan jelas tanpa kendala yang saling berinteraksi.. Bukti: 11 + 9 = .…

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan kemampuan membilang maju. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dengan hasil di bawah 30 adalah materi standar kelas 2. Strategi menghitung maju adalah prosedur rutin yang diajarkan di tingkat ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3442`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal meminta siswa menjalankan prosedur penjumlahan dasar dengan metode spesifik (menghitung maju) yang sudah dipelajari, sehingga masuk kategori knowing.
- Dimensi pengetahuan `procedural`: Soal menguji penerapan algoritma atau metode menghitung maju untuk menyelesaikan penjumlahan.
- Intended difficulty `Easy`: Soal adalah penerapan langsung prosedur penjumlahan dasar. Tidak ada kendala kompleks atau perencanaan strategi yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan kemampuan berhitung maju. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dengan metode hitung maju adalah materi standar kelas 2 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 63/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999642; applying=0.000358; reasoning=0.000000 | knowing | 0.999642 | 0.002911 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.842605; conceptual=0.059367; procedural=0.098028; metacognitive=0.000000 | factual | 0.842605 | 0.389258 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.917613; Medium=0.079839; Hard=0.002548 | Easy | 0.917613 | 0.269363 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999642; −Σp ln(p) = 0.003198; H = 0.003198/ln(3) = 0.002911; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.842605; −Σp ln(p) = 0.539626; H = 0.539626/ln(4) = 0.389258; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.917613; −Σp ln(p) = 0.295925; H = 0.295925/ln(3) = 0.269363; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Berbagai Cara Melakukan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi penjumlahan berikut dengan menghitung maju.

11 + 9 = .…
Pilihan: A. 2
B. 19
C. 21
D. 20
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `dee5237101a9a4d500e44455`

Hitunglah operasi penjumlahan berikut dengan menghitung maju.<br><br>10 + 7 = ....

| Opsi | Isi |
|---|---|
| A | 17 |
| B | 18 |
| C | 3 |
| D | 16 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menghitung maju dari 10 sebanyak 7 langkah: 11, 12, 13, 14, 15, 16, 17. Hasilnya adalah 17.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3a1c35753bf25eba99295631b2ee53b2aaf4eae53d0a47885e9a8c6c7124a614`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2201 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2206 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2237 |

Run 1 — solusi: Menghitung maju dari 10 sebanyak 7 langkah: 11, 12, 13, 14, 15, 16, 17. Hasilnya adalah 17.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur penjumlahan dasar dengan strategi spesifik (menghitung maju) yang sudah diajarkan di kelas 2. Ini adalah penerapan prosedur langsung.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 10 + 7 = ....
- Dimensi pengetahuan `classify/procedural`: Soal menguji penguasaan algoritma atau teknik penjumlahan dasar (menghitung maju) yang merupakan prosedur standar.. Bukti: 10 + 7 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2. Prosedur menghitung maju dari 10 adalah strategi yang sangat familiar dan rutin. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: 10 + 7 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan sampai 20 dan kemampuan menghitung maju. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dasar dengan angka 10 (bilangan dasar) sangat sesuai dengan kurikulum kelas 2 awal. Tidak ada tuntutan kognitif tambahan selain melakukan prosedur yang diminta. |

Run 2 — solusi: Menghitung maju 7 langkah dari 10: 11, 12, 13, 14, 15, 16, 17.
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan strategi 'menghitung maju' (counting on) yang merupakan prosedur dasar untuk menyelesaikan penjumlahan sederhana. Tidak ada tuntutan untuk merancang strategi baru atau melakukan penalaran kompleks.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 10 + 7 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap prosedur penjumlahan dasar dan penggunaan strategi menghitung maju sebagai metode komputasi.. Bukti: 10 + 7 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2. Strategi menghitung maju adalah prosedur rutin yang diajarkan di awal kelas. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk perencanaan langkah yang kompleks.. Bukti: 10 + 7 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan 1-20 dan kemampuan menghitung maju. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Penjumlahan 10 + 7 adalah operasi dasar yang diharapkan sudah dikuasai siswa kelas 2 dengan strategi menghitung maju. |

Run 3 — solusi: Mulai dari 10, hitung maju sebanyak 7 langkah: 11, 12, 13, 14, 15, 16, 17. Hasilnya adalah 17.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur penjumlahan dasar menggunakan strategi 'menghitung maju' yang merupakan prosedur standar yang diajarkan di kelas 2. Tidak ada tuntutan untuk merancang strategi baru atau memecahkan masalah non-rutin.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 10 + 7 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi penjumlahan dasar dan penggunaan strategi menghitung maju sebagai metode untuk menyelesaikannya.. Bukti: 10 + 7 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, menggunakan angka yang familiar (puluhan dan satuan), dan meminta prosedur yang sudah diajarkan secara eksplisit. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan langkah yang kompleks.. Bukti: 10 + 7 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menghitung maju. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Penjumlahan 10 + 7 adalah operasi dasar yang sesuai dengan kurikulum kelas 2. Siswa diharapkan sudah lancar melakukan penjumlahan sederhana dengan strategi menghitung maju. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999809; applying=0.000191; reasoning=0.000000 | knowing | 0.999809 | 0.001662 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.637010; conceptual=0.288788; procedural=0.074202; metacognitive=0.000000 | factual | 0.637010 | 0.605183 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.896133; Medium=0.101756; Hard=0.002111 | Easy | 0.896133 | 0.312951 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999809; −Σp ln(p) = 0.001826; H = 0.001826/ln(3) = 0.001662; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.637010; −Σp ln(p) = 0.838962; H = 0.838962/ln(4) = 0.605183; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.896133; −Σp ln(p) = 0.343812; H = 0.343812/ln(3) = 0.312951; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Berbagai Cara Melakukan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi penjumlahan berikut dengan menghitung maju.

10 + 7 = ....
Pilihan: A. 17
B. 18
C. 3
D. 16
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `c9d5c58f9bea9fbc5724dae7`

Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan.<br><br>17 – 12 = ....

| Opsi | Isi |
|---|---|
| A | 29 |
| B | 6 |
| C | 5 |
| D | 4 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 17 = 10 + 7; 12 = 10 + 2. (10 - 10) + (7 - 2) = 0 + 5 = 5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cf5ecdb6a29ae095d029f868a5aebc581ba492bd3113a8e7ea7d402f9dae1408`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3007 |
| 2 | success | valid / verified | applying | procedural | Easy | 3032 |
| 3 | success | valid / verified | applying | procedural | Easy | 2256 |

Run 1 — solusi: 17 = 10 + 7; 12 = 10 + 2. (10 - 10) + (7 - 2) = 0 + 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan metode dekomposisi (pasangan bilangan) untuk menyelesaikan pengurangan dua bilangan dua digit. Ini adalah penerapan prosedur yang sudah dipelajari.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan; 17 – 12 = ....
- Dimensi pengetahuan `classify/procedural`: Soal secara eksplisit meminta penggunaan metode atau teknik tertentu (pasangan bilangan/dekomposisi) untuk menyelesaikan operasi pengurangan.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan
- Intended difficulty `classify/Easy`: Soal meminta penerapan langsung metode dekomposisi yang familiar bagi kelas 2. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan beban kognitif rendah.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan; 17 – 12 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Metode dekomposisi adalah materi standar kelas 2. Tidak ada langkah kompleks atau kendala yang harus diintegrasikan. |

Run 2 — solusi: 17 = 10 + 7; 12 = 10 + 2. (10 - 10) + (7 - 2) = 0 + 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan metode dekomposisi (pasangan bilangan) untuk menyelesaikan pengurangan dua digit. Ini adalah penerapan prosedur yang sudah dipelajari di kelas 2.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan.; 17 – 12 = ....
- Dimensi pengetahuan `classify/procedural`: Soal secara eksplisit meminta penggunaan metode atau teknik 'pasangan bilangan' (dekomposisi) untuk melakukan pengurangan.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan.
- Intended difficulty `classify/Easy`: Soal ini adalah latihan rutin pengurangan dua digit dengan metode dekomposisi yang umum diajarkan di kelas 2. Langkah-langkahnya langsung dan tidak memerlukan perencanaan kompleks.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan.; 17 – 12 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar 1-digit. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari metode dekomposisi yang sudah dipelajari siswa kelas 2. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi baru. |

Run 3 — solusi: 17 = 10 + 7; 12 = 10 + 2. (10 - 10) + (7 - 2) = 0 + 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan dengan metode dekomposisi (pasangan bilangan) yang merupakan metode standar untuk kelas 2. Ini adalah penerapan prosedur yang sudah dipelajari.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan. 17 – 12 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritme pengurangan melalui dekomposisi nilai tempat (pasangan bilangan), yang merupakan pengetahuan prosedural.. Bukti: menggunakan pasangan bilangan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 2. Prosedur dekomposisi (17=10+7, 12=10+2) adalah metode familiar. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: 17 – 12 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dua digit dengan dekomposisi adalah materi standar kelas 2. Langkah-langkahnya langsung dan familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999872; applying=0.000128; reasoning=0.000000 | knowing | 0.999872 | 0.001162 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.777049; conceptual=0.108749; procedural=0.114202; metacognitive=0.000000 | factual | 0.777049 | 0.494187 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.926823; Medium=0.070286; Hard=0.002891 | Easy | 0.926823 | 0.249365 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999872; −Σp ln(p) = 0.001277; H = 0.001277/ln(3) = 0.001162; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.777049; −Σp ln(p) = 0.685089; H = 0.685089/ln(4) = 0.494187; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.926823; −Σp ln(p) = 0.273955; H = 0.273955/ln(3) = 0.249365; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Berbagai Cara Melakukan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan.

17 – 12 = ....
Pilihan: A. 29
B. 6
C. 5
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `2e68e85a51ce02c29adaaa88`

Hitunglah operasi pengurangan berikut dengan menghitung mundur.<br><br>15 – 4 = ....

| Opsi | Isi |
|---|---|
| A | 11 |
| B | 10 |
| C | 19 |
| D | 12 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menghitung mundur 4 langkah dari 15: 14 (1), 13 (2), 12 (3), 11 (4). Hasilnya adalah 11.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eb3fe0fc2b586e0652cd229910a9fcbcb3caf00ca5008f3e21259c71f1302d0d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2198 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2218 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2239 |

Run 1 — solusi: Menghitung mundur 4 langkah dari 15: 14 (1), 13 (2), 12 (3), 11 (4). Hasilnya adalah 11.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan prosedur pengurangan sederhana dengan metode spesifik (menghitung mundur) yang merupakan prosedur langsung yang diajarkan di kelas 2.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur. 15 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma atau metode pengurangan (menghitung mundur) yang merupakan prosedur standar.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur.
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari metode pengurangan yang familiar bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari bilangan 15. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dasar dalam rentang 20 adalah materi standar kelas 2. Metode menghitung mundur adalah prosedur rutin yang diajarkan. |

Run 2 — solusi: Menghitung mundur 4 langkah dari 15: 14 (1), 13 (2), 12 (3), 11 (4). Hasilnya adalah 11.
- Domain kognitif `classify/knowing`: Siswa diminta menjalankan prosedur pengurangan spesifik (menghitung mundur) yang sudah dipelajari sebagai metode dasar untuk memahami pengurangan.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur. 15 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan prosedur atau algoritma pengurangan sederhana melalui metode menghitung mundur.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur.
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari prosedur menghitung mundur yang familiar bagi siswa kelas 2. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari bilangan 15. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dalam lingkup 20 dengan metode hitung mundur adalah materi standar kelas 2. Soal bersifat langsung tanpa jebakan atau integrasi konsep. |

Run 3 — solusi: Menghitung mundur 4 langkah dari 15: 14, 13, 12, 11.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan prosedur pengurangan sederhana (15-4) menggunakan strategi spesifik yang diarahkan oleh soal, yaitu menghitung mundur. Ini adalah penerapan langsung dari prosedur yang sudah dipelajari.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur. 15 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan algoritma atau metode pengurangan dasar (menghitung mundur) yang merupakan bagian dari keterampilan prosedural matematika dasar.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2. Strategi (menghitung mundur) ditentukan secara eksplisit, langkah penyelesaiannya tunggal dan langsung, serta tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi sendiri.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan berhitung mundur dari angka 15. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dalam lingkup 20 dengan strategi yang diarahkan adalah materi standar kelas 2. Tidak ada kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999818; applying=0.000182; reasoning=0.000000 | knowing | 0.999818 | 0.001595 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.724610; conceptual=0.114049; procedural=0.161341; metacognitive=0.000000 | factual | 0.724610 | 0.559298 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.916902; Medium=0.080296; Hard=0.002802 | Easy | 0.916902 | 0.271728 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999818; −Σp ln(p) = 0.001752; H = 0.001752/ln(3) = 0.001595; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.724610; −Σp ln(p) = 0.775352; H = 0.775352/ln(4) = 0.559298; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.916902; −Σp ln(p) = 0.298523; H = 0.298523/ln(3) = 0.271728; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Berbagai Cara Melakukan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi pengurangan berikut dengan menghitung mundur.

15 – 4 = ....
Pilihan: A. 11
B. 10
C. 19
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `86ef303fdabf175f3223919d`

Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.<br><br>Berapa jumlah semua kupu-kupu?

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 11 |
| C | 18 |
| D | 12 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5dd8f8fb6b3be35853d640aac5e085b1ae92a0e9cba2334bdac56130ab11adb3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2349 |
| 2 | success | valid / verified | applying | procedural | Medium | 2373 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2400 |

Run 1 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan setelah menentukan nilai yang belum diketahui (kuning) melalui operasi sederhana. Ini adalah penerapan konsep penjumlahan pada konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma penjumlahan dasar dan pemahaman hubungan 'lebih dari' untuk menyelesaikan masalah.. Bukti: Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah: menentukan jumlah kupu-kupu kuning, lalu menjumlahkan ketiganya. Ini adalah tugas rutin bagi kelas 2.. Bukti: Ada 5 kupu-kupu merah.; Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar hingga 20 dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan soal cerita penjumlahan bertahap. Soal ini menuntut ketelitian dalam mengidentifikasi semua variabel sebelum menjumlahkan. |

Run 2 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan dasar setelah menentukan nilai yang belum diketahui (kuning) melalui operasi sederhana. Ini adalah penerapan konsep penjumlahan dalam konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritme penjumlahan dasar dan pemahaman relasi 'lebihnya dari' untuk menyelesaikan masalah.. Bukti: Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah: mencari jumlah kupu-kupu kuning, lalu menjumlahkan ketiganya. Langkah-langkahnya jelas dan familiar bagi siswa kelas 2.. Bukti: Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar sampai 20 dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan soal cerita penjumlahan bertahap. Meskipun ada dua langkah, alurnya sangat linear dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang diberikan, melakukan satu operasi hitung sederhana untuk menentukan jumlah kupu-kupu kuning, lalu menjumlahkan ketiga kelompok tersebut. Ini adalah penerapan prosedur penjumlahan pada konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar kuantitas (konsep 'lebih dari') dan penggunaan algoritme penjumlahan dasar.. Bukti: Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah sederhana: menentukan jumlah kupu-kupu kuning (5+2) dan menjumlahkan total (5+6+7). Langkah-langkahnya berurutan dan jelas, tidak memerlukan perencanaan strategi yang kompleks bagi siswa kelas 2.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar sampai 20 dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun hanya penjumlahan, siswa harus melakukan langkah perantara (mencari jumlah kuning) sebelum menjumlahkan total, yang sedikit lebih menuntut daripada soal satu langkah langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3972`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur penjumlahan setelah menentukan nilai yang belum diketahui (kuning) melalui operasi sederhana. Ini adalah penerapan konsep penjumlahan pada konteks rutin.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritme penjumlahan dasar dan pemahaman relasi 'lebih dari' untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal memerlukan dua langkah: menentukan jumlah kupu-kupu kuning, lalu menjumlahkan ketiganya. Meskipun prosedurnya rutin, siswa harus mengelola dua langkah yang saling bergantung, yang sedikit lebih menuntut daripada soal satu langkah langsung bagi kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar hingga 20 dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan soal cerita penjumlahan bertahap. Soal ini menuntut ketelitian dalam mengidentifikasi semua variabel sebelum menjumlahkan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000254; applying=0.999746; reasoning=0.000000 | applying | 0.999746 | 0.002144 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.260301; conceptual=0.724991; procedural=0.014708; metacognitive=0.000000 | conceptual | 0.724991 | 0.465670 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.858381; Medium=0.138570; Hard=0.003049 | Easy | 0.858381 | 0.384676 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999746; −Σp ln(p) = 0.002355; H = 0.002355/ln(3) = 0.002144; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.724991; −Σp ln(p) = 0.645556; H = 0.645556/ln(4) = 0.465670; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.858381; −Σp ln(p) = 0.422610; H = 0.422610/ln(3) = 0.384676; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Soal Cerita Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Berapa jumlah semua kupu-kupu?
Pilihan: A. 13
B. 11
C. 18
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `c0bf29e80c730eba9378deaf`

Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.<br><br>Berapa banyak kupu-kupu kuning?

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 3 |
| C | 8 |
| D | 6 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Kupu-kupu kuning = kupu-kupu merah + 2 = 5 + 2 = 7.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `876bfada9ec83c93933d5842eaf055714547b7db488e7de9780a9de15330fff2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2229 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2256 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2226 |

Run 1 — solusi: Kupu-kupu kuning = kupu-kupu merah + 2 = 5 + 2 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan kalimat '2 lebihnya dari' menjadi operasi penjumlahan sederhana (5 + 2). Ini adalah penerapan konsep penjumlahan pada konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang hubungan 'lebih dari' untuk menentukan operasi yang diperlukan.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi nilai merah (5) dan menerapkan operasi penambahan (2) sesuai instruksi. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Ada 5 kupu-kupu merah.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar bilangan cacah sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, soal cerita satu langkah dengan operasi penjumlahan dasar adalah materi standar yang rutin. |

Run 2 — solusi: Banyak kupu-kupu kuning adalah 2 lebihnya dari kupu-kupu merah. Diketahui kupu-kupu merah = 5. Maka, kupu-kupu kuning = 5 + 2 = 7.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep penjumlahan dasar untuk menentukan jumlah objek berdasarkan informasi perbandingan yang diberikan secara eksplisit. Ini adalah penerapan prosedur penjumlahan dalam konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan 'lebih dari' sebagai operasi penjumlahan.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi nilai dasar (5) dan menerapkan operasi penjumlahan (5+2) berdasarkan kata kunci 'lebihnya'. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Ada 5 kupu-kupu merah.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman penjumlahan dasar dan konsep 'lebih dari'. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, soal ini adalah penerapan langsung dari operasi penjumlahan dasar dengan satu langkah penyelesaian yang jelas. |

Run 3 — solusi: Kupu-kupu kuning = 5 (merah) + 2 = 7.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep penjumlahan dasar untuk menentukan jumlah objek berdasarkan informasi perbandingan yang diberikan secara eksplisit.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan 'lebih dari' dalam konteks penjumlahan sederhana.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi nilai dasar (5) dan menerapkan operasi penjumlahan (5+2) sesuai instruksi '2 lebihnya'. Tidak ada langkah yang saling bergantung atau kendala kompleks.. Bukti: Ada 5 kupu-kupu merah.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar sampai 10 dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, soal ini adalah penerapan langsung dari operasi penjumlahan dasar dalam konteks cerita sederhana yang familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000277; applying=0.999723; reasoning=0.000000 | applying | 0.999723 | 0.002319 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.423088; conceptual=0.563686; procedural=0.013226; metacognitive=0.000000 | conceptual | 0.563686 | 0.536882 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.858811; Medium=0.138373; Hard=0.002816 | Easy | 0.858811 | 0.383143 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999723; −Σp ln(p) = 0.002547; H = 0.002547/ln(3) = 0.002319; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.563686; −Σp ln(p) = 0.744277; H = 0.744277/ln(4) = 0.536882; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.858811; −Σp ln(p) = 0.420925; H = 0.420925/ln(3) = 0.383143; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Soal Cerita Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Berapa banyak kupu-kupu kuning?
Pilihan: A. 7
B. 3
C. 8
D. 6
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `54e65cf97cc65f3ef126daef`

Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.<br><br>Berapakah sisa bolu kukus Ibu sekarang?

| Opsi | Isi |
|---|---|
| A | 11 |
| B | 12 |
| C | 15 |
| D | 10 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Ibu memiliki 13 bolu, dimakan 2. Sisa bolu = 13 - 2 = 11.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4fda78da588c41f8e418bb3a3ae6b68e1b06841cb5470444a286fffacb7d2304`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2255 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2267 |
| 3 | success | valid / verified | applying | procedural | Easy | 2250 |

Run 1 — solusi: Ibu membeli 13 bolu, dimakan 2. Sisa bolu = 13 - 2 = 11.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi pengurangan dasar (13 - 2) yang merupakan prosedur rutin dan langsung dalam konteks kehidupan sehari-hari yang familiar bagi siswa kelas 2.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi pengurangan untuk menyelesaikan masalah kontekstual sederhana.. Bukti: 13 bolu kukus; memakan 2 bolu kukus
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dengan satu langkah penyelesaian (pengurangan). Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan di bawah 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 13-2 adalah standar kompetensi kelas 2. Soal disajikan secara eksplisit tanpa jebakan atau langkah tambahan yang rumit. |

Run 2 — solusi: Ibu memiliki 13 bolu, dimakan 2, maka sisa bolu adalah 13 - 2 = 11.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar (13-2) yang merupakan prosedur rutin dan langsung dalam konteks kehidupan sehari-hari yang sudah dipelajari di kelas 2.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma pengurangan dasar untuk menyelesaikan masalah yang melibatkan fakta numerik dan operasi hitung sederhana.. Bukti: 13 bolu kukus; memakan 2 bolu kukus
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep pengurangan dasar. Tidak ada langkah yang saling bergantung atau kendala yang kompleks. Siswa hanya perlu melakukan satu operasi hitung sederhana.. Bukti: 13 bolu kukus; memakan 2 bolu kukus; Berapakah sisa bolu kukus Ibu sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung mundur atau pengurangan bilangan cacah di bawah 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, pengurangan bilangan di bawah 20 adalah materi dasar yang rutin. Soal tidak memiliki jebakan atau kompleksitas tambahan. |

Run 3 — solusi: Ibu membeli 13 bolu, dimakan 2. Sisa bolu = 13 - 2 = 11.
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi pengurangan dasar (13 - 2) dalam konteks cerita sederhana. Ini adalah penerapan langsung dari prosedur pengurangan yang sudah dipelajari di kelas 2.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan dasar untuk menyelesaikan masalah sehari-hari.. Bukti: 13 bolu kukus; memakan 2 bolu kukus
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah pengurangan satu langkah yang sangat rutin bagi siswa kelas 2. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 13 bolu kukus; memakan 2 bolu kukus; Berapakah sisa bolu kukus Ibu sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan di bawah 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 13-2 adalah standar kurikulum kelas 2. Soal disajikan secara langsung tanpa jebakan atau kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3698`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta siswa untuk melakukan operasi pengurangan dasar (13 - 2) dalam konteks cerita sederhana. Ini adalah penerapan langsung dari prosedur pengurangan yang sudah dipelajari di kelas 2.
- Dimensi pengetahuan `procedural`: Siswa perlu menerapkan algoritma pengurangan dasar untuk menyelesaikan masalah yang melibatkan fakta numerik dan operasi hitung sederhana.
- Intended difficulty `Easy`: Soal ini merupakan masalah pengurangan satu langkah yang sangat rutin bagi siswa kelas 2. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan di bawah 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 13-2 adalah standar kurikulum kelas 2. Soal disajikan secara langsung tanpa jebakan atau kompleksitas tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000219; applying=0.999781; reasoning=0.000000 | applying | 0.999781 | 0.001880 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.388760; conceptual=0.560413; procedural=0.050828; metacognitive=0.000000 | conceptual | 0.560413 | 0.608279 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.899044; Medium=0.096268; Hard=0.004688 | Easy | 0.899044 | 0.315076 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999781; −Σp ln(p) = 0.002065; H = 0.002065/ln(3) = 0.001880; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.560413; −Σp ln(p) = 0.843254; H = 0.843254/ln(4) = 0.608279; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.899044; −Σp ln(p) = 0.346147; H = 0.346147/ln(3) = 0.315076; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Pengurangan yang Hasilnya Kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.

Berapakah sisa bolu kukus Ibu sekarang?
Pilihan: A. 11
B. 12
C. 15
D. 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `c1065f5b900e24e5013bfcc9`

Tulislah nama bangun datar berikut.

| Opsi | Isi |
|---|---|
| A | Segitiga |
| B | Segi empat |
| C | Lingkaran |
| D | Segi lima |

![Gambar sumber soal 15](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0089-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bangun datar tersebut memiliki 3 sisi lurus dan 3 sudut, yang merupakan definisi dari segitiga.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0089-03.png. Transkripsi visual: Sebuah gambar bangun datar berwarna merah muda berbentuk segitiga sama kaki dengan tiga sisi lurus dan tiga sudut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f4e9a728d53c66ce859ca218e426009cd075d62808fde8e2861ef3e317693f13`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3315 |
| 2 | success | valid / verified | knowing | factual | Easy | 3298 |
| 3 | success | valid / verified | knowing | factual | Easy | 3321 |

Run 1 — solusi: Bangun datar tersebut memiliki 3 sisi lurus dan 3 sudut, yang merupakan definisi dari segitiga.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengenali dan menamai bangun datar berdasarkan karakteristik visualnya (jumlah sisi). Ini adalah proses pengenalan langsung terhadap objek geometris dasar yang sudah dipelajari.. Bukti: Tulislah nama bangun datar berikut.; gambar bangun datar berwarna merah muda berbentuk segitiga
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui fakta tentang nama-nama bangun datar dan karakteristik dasarnya (jumlah sisi) untuk mengidentifikasi gambar tersebut.. Bukti: nama bangun datar; bangun datar berwarna merah muda berbentuk segitiga
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan, hanya pengenalan bentuk dasar.. Bukti: Tulislah nama bangun datar berikut.; gambar bangun datar berwarna merah muda berbentuk segitiga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama-nama bangun datar sederhana (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan untuk mengidentifikasi bangun datar berdasarkan jumlah sisi. Soal ini adalah penerapan langsung dari pengetahuan tersebut. |

Run 2 — solusi: Bangun datar tersebut memiliki 3 sisi garis lurus. Bangun dengan 3 sisi disebut segitiga.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nama bangun datar berdasarkan pengamatan visual langsung terhadap jumlah sisi. Ini adalah tugas pengenalan bentuk dasar yang sudah dipelajari di kelas 2.. Bukti: Tulislah nama bangun datar berikut.; bangun dibatasi oleh 3 sisi garis lurus
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun datar dasar (segitiga, segi empat, lingkaran) berdasarkan ciri visualnya.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana dan langsung. Siswa hanya perlu mengenali bentuk visual yang sangat umum (segitiga) tanpa perlu melakukan perhitungan atau perencanaan langkah yang kompleks.. Bukti: Tulislah nama bangun datar berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk dasar geometri (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pengenalan bentuk dasar adalah materi standar kelas 2. Soal ini tidak memerlukan analisis mendalam, hanya pengenalan visual langsung. |

Run 3 — solusi: Bangun datar tersebut memiliki 3 sisi lurus dan 3 sudut, yang merupakan ciri khas dari segitiga.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi nama bangun datar berdasarkan pengamatan visual langsung terhadap ciri-ciri geometris dasar (jumlah sisi). Ini adalah proses pengenalan bentuk yang sudah dipelajari.. Bukti: Tulislah nama bangun datar berikut.; Gambar menunjukkan sebuah bangun datar berwarna merah muda berbentuk segitiga
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui fakta tentang nama-nama bangun datar dasar dan ciri-cirinya (jumlah sisi) untuk menjawab soal ini.. Bukti: Tulislah nama bangun datar berikut.; Gambar menunjukkan sebuah bangun datar berwarna merah muda berbentuk segitiga
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan merupakan pengenalan bentuk dasar yang umum di kelas 2. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Tulislah nama bangun datar berikut.; Gambar menunjukkan sebuah bangun datar berwarna merah muda berbentuk segitiga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk dasar (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan sudah mampu mengidentifikasi bangun datar sederhana seperti segitiga secara visual tanpa kesulitan berarti. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 73/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999835; applying=0.000165; reasoning=0.000000 | knowing | 0.999835 | 0.001460 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.879416; conceptual=0.115268; procedural=0.005316; metacognitive=0.000000 | factual | 0.879416 | 0.281238 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.903546; Medium=0.093249; Hard=0.003205 | Easy | 0.903546 | 0.301549 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999835; −Σp ln(p) = 0.001604; H = 0.001604/ln(3) = 0.001460; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.879416; −Σp ln(p) = 0.389878; H = 0.389878/ln(4) = 0.281238; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.903546; −Σp ln(p) = 0.331285; H = 0.331285/ln(3) = 0.301549; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Tulislah nama bangun datar berikut.
Pilihan: A. Segitiga
B. Segi empat
C. Lingkaran
D. Segi lima
Transkripsi visual: Sebuah gambar bangun datar berwarna merah muda berbentuk segitiga sama kaki dengan tiga sisi lurus dan tiga sudut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `13edcfffbf7fe9b6f346ad87`

Tulislah nama bangun datar berikut.

| Opsi | Isi |
|---|---|
| A | Segi lima |
| B | Lingkaran |
| C | Segi enam |
| D | Segitiga |

![Gambar sumber soal 16](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0089-06.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bangun datar tersebut memiliki satu sisi lengkung yang tertutup dan tidak memiliki sudut, yang merupakan ciri khas dari lingkaran.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0089-06.png. Transkripsi visual: Sebuah gambar bangun datar berwarna ungu berbentuk lingkaran sempurna.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `58793b30aeda7bd130cfb5f9fe91113bce1c2d95b8aa558e5310a98dda7f478b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3266 |
| 2 | success | valid / verified | knowing | factual | Easy | 3353 |
| 3 | success | valid / verified | knowing | factual | Easy | 3251 |

Run 1 — solusi: Bangun datar tersebut memiliki satu sisi lengkung yang tertutup dan tidak memiliki sudut, yang merupakan ciri khas dari lingkaran.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menamai bangun datar berdasarkan ciri visual yang sangat mendasar dan familiar.. Bukti: Tulislah nama bangun datar berikut.; gambar bangun datar berwarna ungu berbentuk lingkaran
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai nama dan bentuk dasar bangun datar.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta identifikasi visual langsung dari bentuk dasar yang sudah dipelajari di kelas 2.. Bukti: Tulislah nama bangun datar berikut.; gambar bangun datar berwarna ungu berbentuk lingkaran

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk dasar geometri (lingkaran, segitiga, segiempat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 2 sudah sangat familiar dengan bentuk lingkaran sebagai bentuk dasar geometri. |

Run 2 — solusi: Gambar tersebut adalah bentuk geometri yang dibatasi oleh satu garis lengkung tertutup yang jaraknya sama dari titik pusat, yang dikenal sebagai lingkaran.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menamai bangun datar berdasarkan pengenalan visual langsung. Ini adalah proses pengenalan bentuk dasar yang sudah dipelajari.. Bukti: Tulislah nama bangun datar berikut.; Gambar tersebut adalah bentuk geometri yang dibatasi oleh satu garis lengkung
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui fakta tentang nama-nama bangun datar dasar (lingkaran, segitiga, dll) untuk menjawab soal ini.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana dan langsung. Siswa hanya perlu mengenali bentuk visual yang sangat familiar (lingkaran) dan memilih opsi yang sesuai. Tidak ada langkah kompleks atau penalaran yang diperlukan.. Bukti: Tulislah nama bangun datar berikut.; Gambar tersebut adalah bentuk geometri yang dibatasi oleh satu garis lengkung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk geometri dasar seperti lingkaran, segitiga, dan segiempat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 2, mengenali bentuk dasar seperti lingkaran adalah materi awal yang sangat mendasar dan rutin. |

Run 3 — solusi: Gambar tersebut adalah lingkaran karena memiliki satu sisi lengkung yang tertutup dan tidak memiliki sudut.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun datar berdasarkan pengamatan visual langsung.. Bukti: Tulislah nama bangun datar berikut.; Gambar tersebut adalah lingkaran
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai nama-nama bangun datar dasar.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengenalan visual terhadap bentuk dasar yang sudah sangat familiar bagi siswa kelas 2.. Bukti: Tulislah nama bangun datar berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun datar dasar (lingkaran, segitiga, segiempat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pengenalan bentuk lingkaran adalah materi dasar kelas 1 dan 2. Tidak ada langkah kompleks atau penalaran yang diperlukan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999999; applying=0.000001; reasoning=0.000000 | knowing | 0.999999 | 0.000010 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.780643; conceptual=0.212101; procedural=0.007256; metacognitive=0.000000 | factual | 0.780643 | 0.402484 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.907099; Medium=0.090105; Hard=0.002796 | Easy | 0.907099 | 0.292866 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000011; H = 0.000011/ln(3) = 0.000010; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.780643; −Σp ln(p) = 0.557961; H = 0.557961/ln(4) = 0.402484; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.907099; −Σp ln(p) = 0.321746; H = 0.321746/ln(3) = 0.292866; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Tulislah nama bangun datar berikut.
Pilihan: A. Segi lima
B. Lingkaran
C. Segi enam
D. Segitiga
Transkripsi visual: Sebuah gambar bangun datar berwarna ungu berbentuk lingkaran sempurna.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `7b1097bedb274e0d05e2f483`

Susun bangun datar berikut menjadi satu bentuk. Bentuk apa hasil susunannya?

| Opsi | Isi |
|---|---|
| A | Berbentuk seperti anak panah dua arah (kiri dan kanan) |
| B | Berbentuk persegi (kotak) |
| C | Berbentuk seperti anak panah tunggal |
| D | Berbentuk seperti tangga (undakan) |

![Gambar sumber soal 17](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0097-12.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menyusun persegi panjang dan segitiga dengan menempelkan sisi tegak segitiga pada salah satu sisi pendek persegi panjang akan membentuk bangun gabungan yang menyerupai anak panah (panah tunggal).
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0097-12.png. Transkripsi visual: Terdapat dua bangun datar yang terpisah: sebuah persegi panjang di sebelah kiri dan sebuah segitiga sama sisi di sebelah kanan. Jika persegi panjang ditempelkan pada sisi tegak segitiga, akan terbentuk bangun menyerupai anak panah yang menunjuk ke kanan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f06857818cddb7144213e9111d74b67efaf73ed7188524dc10e3f949deeb84ff`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3419 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3395 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3376 |

Run 1 — solusi: Menyusun persegi panjang dan segitiga dengan menempelkan sisi tegak segitiga pada salah satu sisi pendek persegi panjang akan membentuk bangun gabungan yang menyerupai anak panah (panah tunggal).
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan visualisasi mental atau manipulasi spasial sederhana untuk menggabungkan dua bangun datar yang sudah dikenal (persegi panjang dan segitiga) menjadi bentuk baru yang familiar. Ini adalah penerapan konsep komposisi bangun datar.. Bukti: Susun bangun datar berikut menjadi satu bentuk; Bentuk apa hasil susunannya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bangun datar dapat disusun atau dikomposisikan untuk membentuk bangun baru yang lebih kompleks.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan dua bangun dasar yang sangat umum. Visualisasi penggabungan keduanya menjadi bentuk panah adalah tugas rutin dalam kurikulum geometri kelas 2.. Bukti: Susun bangun datar berikut menjadi satu bentuk; Bentuk apa hasil susunannya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (persegi panjang, segitiga) dan konsep penggabungan bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan aktivitas menyusun bangun datar (tangram atau puzzle sederhana). Tugas ini tidak memerlukan perencanaan kompleks, hanya pengenalan visual langsung. |

Run 2 — solusi: Menempelkan sisi tegak segitiga ke salah satu sisi lebar persegi panjang akan membentuk bangun gabungan yang menyerupai anak panah (panah ke kanan).
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan visualisasi mental atau manipulasi spasial sederhana untuk menggabungkan dua bangun datar (persegi panjang dan segitiga) menjadi satu bentuk baru yang familiar. Ini adalah proses menerapkan pemahaman konsep komposisi bangun datar.. Bukti: Susun bangun datar berikut menjadi satu bentuk; Bentuk apa hasil susunannya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bentuk-bentuk dasar dapat disusun atau dikomposisikan untuk membentuk bentuk yang lebih kompleks.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan penggabungan dua bangun sederhana yang secara visual jelas membentuk pola anak panah. Tidak ada kendala rumit atau langkah bertingkat yang diperlukan.. Bukti: Susun bangun datar berikut menjadi satu bentuk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar (persegi panjang dan segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, tugas menyusun bangun datar sederhana adalah materi standar yang rutin. Visualisasi penggabungan dua bentuk dasar ini tidak menuntut perencanaan kompleks. |

Run 3 — solusi: Menempelkan sisi tegak segitiga ke sisi kanan persegi panjang menghasilkan bentuk yang menyerupai anak panah tunggal yang menunjuk ke kanan.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan visualisasi mental atau manipulasi spasial sederhana untuk menggabungkan dua bangun datar menjadi satu bentuk baru. Ini adalah penerapan konsep komposisi bangun datar yang rutin.. Bukti: Susun bangun datar berikut menjadi satu bentuk; Bentuk apa hasil susunannya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bentuk-bentuk dasar dapat disusun atau dikomposisikan untuk membentuk bentuk yang lebih kompleks.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan penggabungan dua bangun datar sederhana yang familiar. Tidak ada kendala yang rumit atau langkah-langkah yang saling bergantung yang kompleks.. Bukti: Susun bangun datar berikut menjadi satu bentuk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bangun datar dasar (persegi panjang dan segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, tugas menyusun dua bangun datar sederhana adalah aktivitas rutin dalam geometri dasar yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 128/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.141558; applying=0.858442; reasoning=0.000000 | applying | 0.858442 | 0.371178 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.156347; conceptual=0.832845; procedural=0.010808; metacognitive=0.000000 | conceptual | 0.832845 | 0.354468 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.796196; Medium=0.199347; Hard=0.004457 | Easy | 0.796196 | 0.479767 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.858442; −Σp ln(p) = 0.407781; H = 0.407781/ln(3) = 0.371178; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.832845; −Σp ln(p) = 0.491397; H = 0.491397/ln(4) = 0.354468; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.796196; −Σp ln(p) = 0.527078; H = 0.527078/ln(3) = 0.479767; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Mengurai dan Menyusun Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Susun bangun datar berikut menjadi satu bentuk. Bentuk apa hasil susunannya?
Pilihan: A. Berbentuk seperti anak panah dua arah (kiri dan kanan)
B. Berbentuk persegi (kotak)
C. Berbentuk seperti anak panah tunggal
D. Berbentuk seperti tangga (undakan)
Transkripsi visual: Terdapat dua bangun datar yang terpisah: sebuah persegi panjang di sebelah kiri dan sebuah segitiga sama sisi di sebelah kanan. Jika persegi panjang ditempelkan pada sisi tegak segitiga, akan terbentuk bangun menyerupai anak panah yang menunjuk ke kanan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `2188dcf71c96bfe0666fa262`

Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?

| Opsi | Isi |
|---|---|
| A | Menjadi 2 persegi sama besar |
| B | Menjadi 2 segitiga dan 1 persegi panjang |
| C | Menjadi 2 persegi panjang berbeda ukuran |
| D | Menjadi 2 segitiga |

![Gambar sumber soal 18](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0098-09.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bangun huruf T dapat dipotong menjadi dua bagian persegi panjang: satu persegi panjang horizontal (batang atas) dan satu persegi panjang vertikal (batang bawah). Keduanya memiliki dimensi yang berbeda, sehingga membentuk 2 persegi panjang berbeda ukuran.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0098-09.png. Transkripsi visual: Gambar menunjukkan sebuah bangun datar berbentuk huruf T kapital. Bangun ini memiliki bagian horizontal di atas dan bagian vertikal di bawah yang menyatu. Secara visual, bangun ini dapat diurai menjadi dua persegi panjang: satu persegi panjang horizontal yang lebih lebar di bagian atas dan satu persegi panjang vertikal yang lebih panjang di bagian bawah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6626c7f4981d75583d9a8a5a8aff038b719fba465dfaabed2780848838127ecb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3453 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3430 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3408 |

Run 1 — solusi: Bangun huruf T dapat dipotong menjadi dua bagian persegi panjang: satu persegi panjang horizontal (batang atas) dan satu persegi panjang vertikal (batang bawah). Keduanya memiliki dimensi yang berbeda, sehingga membentuk 2 persegi panjang berbeda ukuran.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali komponen penyusun bangun datar kompleks (huruf T) dengan melakukan dekomposisi visual. Ini adalah penerapan konsep dasar bangun datar yang sudah dipelajari di kelas 2.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?; bangun huruf T terdiri dari batang mendatar dan batang tegak berupa 2 persegi panjang berbeda ukuran
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bangun datar dapat dibentuk dari gabungan bangun datar yang lebih sederhana.. Bukti: Mengurai dan Menyusun Bangun Datar; bentuk apa hasilnya?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan visualisasi sederhana untuk membagi bentuk T menjadi dua persegi panjang. Tidak ada perhitungan rumit atau kendala yang saling berinteraksi.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian; bangun huruf T

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (persegi panjang) dan konsep bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan pengenalan bentuk dasar. Membagi bangun T menjadi dua persegi panjang adalah tugas visual langsung yang sesuai dengan tingkat perkembangan kognitif kelas 2. |

Run 2 — solusi: Bangun huruf T dapat dipotong menjadi dua bagian persegi panjang: satu bagian horizontal di atas dan satu bagian vertikal di bawah. Kedua persegi panjang ini memiliki ukuran yang berbeda (panjang dan lebar berbeda), sehingga sesuai dengan opsi C.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan dekomposisi visual pada bangun datar komposit menjadi bentuk-bentuk dasar yang lebih sederhana (persegi panjang). Ini melibatkan pengenalan bentuk dan pemahaman spasial, yang merupakan penerapan konsep dasar geometri.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?; Gambar menunjukkan sebuah bangun datar berbentuk huruf T kapital.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bangun datar yang lebih kompleks dapat dibentuk dari atau diurai menjadi bangun datar yang lebih sederhana (persegi panjang).. Bukti: Mengurai dan Menyusun Bangun Datar
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena hanya memerlukan pengenalan visual sederhana terhadap bentuk dasar. Tidak ada perhitungan kompleks atau kendala yang saling berinteraksi. Siswa kelas 2 sudah familiar dengan bentuk persegi panjang.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar seperti persegi dan persegi panjang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mengurai bangun datar sederhana menjadi komponen dasarnya adalah materi standar kelas 2 yang bersifat langsung dan visual. |

Run 3 — solusi: Bangun huruf T dapat dipotong secara horizontal atau vertikal menjadi dua bagian persegi panjang. Misalnya, memotong bagian batang tegak dari bagian mendatar akan menghasilkan dua persegi panjang dengan ukuran yang berbeda.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan dekomposisi visual pada bangun datar komposit menjadi bentuk-bentuk dasar (persegi panjang). Ini melibatkan pengenalan sifat bangun dan kemampuan memvisualisasikan pemotongan, yang merupakan penerapan konsep dasar geometri.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?; Gambar menunjukkan sebuah bangun datar berbentuk huruf T
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bangun datar yang lebih kompleks dapat disusun dari atau diurai menjadi bangun datar yang lebih sederhana (persegi panjang).. Bukti: Mengurai dan Menyusun Bangun Datar
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena tugas dekomposisi bangun T menjadi dua persegi panjang adalah prosedur visual yang sangat standar dan familiar dalam kurikulum geometri kelas 2. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar seperti persegi dan persegi panjang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Dekomposisi bangun datar sederhana adalah materi dasar kelas 2. Visualisasi pemotongan bangun T menjadi dua persegi panjang adalah tugas rutin yang tidak menuntut perencanaan tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 142/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.031986; applying=0.968014; reasoning=0.000000 | applying | 0.968014 | 0.128871 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.092057; conceptual=0.883263; procedural=0.024681; metacognitive=0.000000 | conceptual | 0.883263 | 0.303392 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.769411; Medium=0.223679; Hard=0.006911 | Easy | 0.769411 | 0.519777 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.968014; −Σp ln(p) = 0.141579; H = 0.141579/ln(3) = 0.128871; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.883263; −Σp ln(p) = 0.420590; H = 0.420590/ln(4) = 0.303392; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.769411; −Σp ln(p) = 0.571033; H = 0.571033/ln(3) = 0.519777; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Mengurai dan Menyusun Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?
Pilihan: A. Menjadi 2 persegi sama besar
B. Menjadi 2 segitiga dan 1 persegi panjang
C. Menjadi 2 persegi panjang berbeda ukuran
D. Menjadi 2 segitiga
Transkripsi visual: Gambar menunjukkan sebuah bangun datar berbentuk huruf T kapital. Bangun ini memiliki bagian horizontal di atas dan bagian vertikal di bawah yang menyatu. Secara visual, bangun ini dapat diurai menjadi dua persegi panjang: satu persegi panjang horizontal yang lebih lebar di bagian atas dan satu persegi panjang vertikal yang lebih panjang di bagian bawah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `087423442be49795c5b1bf93`

Toni sedang menyusun mainan balok.<br><br>Ada berapa banyak balok satuan pada mainan yang Toni susun?

| Opsi | Isi |
|---|---|
| A | 8 |
| B | 14 |
| C | 7 |
| D | 6 |

![Gambar sumber soal 19](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menghitung jumlah balok: baris depan bawah (3) + baris depan atas (2) + baris belakang bawah (3) = 8 balok.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png. Transkripsi visual: Gambar menunjukkan susunan balok satuan. Baris depan terdiri dari 3 balok di bawah dan 2 balok di atasnya (total 5 balok terlihat di depan). Baris belakang memiliki 3 balok yang menopang balok-balok di atasnya. Secara total, terdapat 8 balok satuan yang membentuk struktur tersebut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `57caa0f275a8737386fef56dbb68295374fd013bf231500595aeb8a089958405`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3472 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3502 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3468 |

Run 1 — solusi: Menghitung jumlah balok: baris depan bawah (3) + baris depan atas (2) + baris belakang bawah (3) = 8 balok.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan menghitung objek 3D yang sebagian tersembunyi. Ini memerlukan penerapan pemahaman spasial dasar untuk membayangkan bagian yang tidak terlihat, yang merupakan penerapan konsep bangun ruang.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur bangun ruang yang disusun dari balok-balok satuan.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 2 harus melakukan penalaran spasial untuk menghitung balok yang tidak terlihat sepenuhnya (tersembunyi di belakang). Meskipun prosedurnya sederhana (menghitung), tuntutan untuk membayangkan struktur 3D dari gambar 2D meningkatkan kompleksitas bagi siswa kelas 2.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan kemampuan membilang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 umumnya sudah mengenal balok, namun visualisasi objek 3D yang memiliki bagian tersembunyi memerlukan kemampuan spasial yang sedikit lebih tinggi dari sekadar menghitung objek yang terlihat utuh. |

Run 2 — solusi: Menghitung balok: baris depan bawah ada 4 balok. Di atasnya ada 2 balok. Di belakang baris depan bawah, terdapat 2 balok yang menopang balok tingkat kedua. Total = 4 + 2 + 2 = 8.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali dan menghitung objek dalam susunan 3D. Ini memerlukan pemahaman spasial dasar untuk mengidentifikasi balok yang tidak terlihat secara langsung, yang merupakan penerapan konsep volume/susunan bangun ruang sederhana.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur bangun ruang yang tersusun dari satuan-satuan kubus, bukan sekadar menghitung benda 2D.. Bukti: Ada berapa banyak balok satuan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 2 harus melakukan penalaran spasial untuk membayangkan balok yang tersembunyi di balik struktur yang terlihat. Meskipun prosedurnya sederhana (menghitung), integrasi antara apa yang terlihat dan apa yang tersirat memerlukan ketelitian lebih daripada sekadar menghitung objek yang tampak sepenuhnya.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan kemampuan menghitung objek. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membayangkan objek 3D yang tersembunyi adalah tantangan kognitif yang sesuai untuk tingkat Medium, karena memerlukan visualisasi mental di luar apa yang tampak langsung di gambar. |

Run 3 — solusi: Menghitung jumlah balok: baris depan bawah (3) + baris depan atas (2) + baris belakang bawah (3) = 8 balok.
- Domain kognitif `classify/applying`: Siswa diminta untuk menghitung objek 3D yang sebagian tersembunyi. Ini memerlukan penerapan konsep visualisasi spasial untuk mengenali balok yang tidak terlihat langsung, yang merupakan penerapan konsep dasar geometri.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur bangun ruang yang tersusun dari unit-unit dasar (balok satuan).. Bukti: Ada berapa banyak balok satuan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk melakukan visualisasi spasial guna mengidentifikasi balok yang tersembunyi di balik struktur yang terlihat. Meskipun prosedurnya sederhana (menghitung), siswa harus memahami struktur 3D secara utuh, bukan sekadar menghitung apa yang tampak di permukaan.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang objek 3D dan kemampuan menghitung benda konkret. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membayangkan objek tersembunyi dalam susunan balok merupakan tantangan kognitif yang sesuai untuk tingkat Medium, karena memerlukan penalaran spasial melampaui pengamatan visual langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 115/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000010 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.334359; conceptual=0.657006; procedural=0.008635; metacognitive=0.000000 | conceptual | 0.657006 | 0.492912 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.822750; Medium=0.174020; Hard=0.003230 | Easy | 0.822750 | 0.439952 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000011; H = 0.000011/ln(3) = 0.000010; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.657006; −Σp ln(p) = 0.683321; H = 0.683321/ln(4) = 0.492912; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.822750; −Σp ln(p) = 0.483336; H = 0.483336/ln(3) = 0.439952; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Bangun Ruang
Tipe soal: multiple_choice
Stimulus: -
Soal: Toni sedang menyusun mainan balok.

Ada berapa banyak balok satuan pada mainan yang Toni susun?
Pilihan: A. 8
B. 14
C. 7
D. 6
Transkripsi visual: Gambar menunjukkan susunan balok satuan. Baris depan terdiri dari 3 balok di bawah dan 2 balok di atasnya (total 5 balok terlihat di depan). Baris belakang memiliki 3 balok yang menopang balok-balok di atasnya. Secara total, terdapat 8 balok satuan yang membentuk struktur tersebut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `b752c451c1f2a955262fabf4`

Berilah nama pada bangun ruang berikut.

| Opsi | Isi |
|---|---|
| A | Bola |
| B | Balok |
| C | Kerucut |
| D | Tabung |

![Gambar sumber soal 20](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0110-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Gambar tersebut adalah bangun ruang yang memiliki alas dan tutup berbentuk lingkaran serta selimut melengkung, yang secara geometris disebut tabung.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0110-04.png. Transkripsi visual: Gambar menunjukkan sebuah bangun ruang berbentuk silinder (tabung) dengan dua sisi datar berbentuk lingkaran di bagian atas dan bawah serta satu sisi lengkung yang menyelimuti. Terdapat kotak teks di bawah gambar dengan tulisan 'Nama = ___'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3126b3e3e3c1614a4442c4b07a19f074f7f2cf10e33745db9c2a1959679b526c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3337 |
| 2 | success | valid / verified | knowing | factual | Easy | 3338 |
| 3 | success | valid / verified | knowing | factual | Easy | 3344 |

Run 1 — solusi: Gambar tersebut adalah bangun ruang yang memiliki alas dan tutup berbentuk lingkaran serta selimut melengkung, yang secara geometris disebut tabung.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun ruang berdasarkan ciri visual yang terlihat langsung. Tidak ada proses analisis atau penerapan prosedur kompleks.. Bukti: Berilah nama pada bangun ruang berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai nama-nama bangun ruang dasar yang dipelajari di kelas 2.. Bukti: Berilah nama pada bangun ruang berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan pengenalan visual terhadap bangun ruang dasar yang umum diajarkan di kelas 2.. Bukti: Berilah nama pada bangun ruang berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun ruang dasar (bola, tabung, kerucut, balok, kubus). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengenalan bangun ruang adalah materi standar kelas 2. Soal ini tidak memerlukan langkah tambahan selain identifikasi visual langsung. |

Run 2 — solusi: Gambar tersebut adalah tabung karena memiliki dua sisi berbentuk lingkaran dan satu sisi lengkung yang menyelimutinya. Pilihan D adalah tabung.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menamai bangun ruang berdasarkan representasi visualnya. Ini adalah proses pengenalan langsung terhadap objek geometri yang sudah dipelajari.. Bukti: Berilah nama pada bangun ruang berikut.; Gambar menunjukkan sebuah bangun ruang berbentuk silinder
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun ruang dasar.. Bukti: Berilah nama pada bangun ruang berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Siswa hanya perlu mengenali bentuk visual dan mencocokkannya dengan istilah yang tepat.. Bukti: Berilah nama pada bangun ruang berikut.; Gambar menunjukkan sebuah bangun ruang berbentuk silinder

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama dan ciri dasar bangun ruang (tabung, bola, balok, kerucut). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengenalan bangun ruang dasar adalah materi standar kelas 2. Tidak ada langkah kompleks atau penalaran yang diperlukan, hanya pengenalan visual langsung. |

Run 3 — solusi: Bangun ruang tersebut memiliki dua sisi berbentuk lingkaran yang sejajar dan satu sisi lengkung, yang merupakan ciri khas dari bangun ruang tabung.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menamai bangun ruang berdasarkan representasi visualnya. Ini adalah proses pengenalan langsung terhadap objek geometri yang sudah dipelajari.. Bukti: Berilah nama pada bangun ruang berikut.; Gambar menunjukkan sebuah bangun ruang berbentuk silinder
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual siswa mengenai nama-nama bangun ruang dasar.. Bukti: Berilah nama pada bangun ruang berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan pengenalan visual terhadap bangun ruang yang umum dipelajari di kelas 2. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Berilah nama pada bangun ruang berikut.; Gambar menunjukkan sebuah bangun ruang berbentuk silinder

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun ruang dasar (bola, tabung, kerucut, balok, kubus). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan sudah mampu membedakan bangun ruang dasar secara visual. Soal ini adalah tugas pengenalan langsung tanpa manipulasi atau analisis tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 96/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000153; applying=0.999847; reasoning=0.000000 | applying | 0.999847 | 0.001361 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.124364; conceptual=0.862539; procedural=0.013097; metacognitive=0.000000 | conceptual | 0.862539 | 0.319968 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.811252; Medium=0.185430; Hard=0.003318 | Easy | 0.811252 | 0.456121 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999847; −Σp ln(p) = 0.001496; H = 0.001496/ln(3) = 0.001361; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.862539; −Σp ln(p) = 0.443569; H = 0.443569/ln(4) = 0.319968; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.811252; −Σp ln(p) = 0.501100; H = 0.501100/ln(3) = 0.456121; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Bangun Ruang
Tipe soal: multiple_choice
Stimulus: -
Soal: Berilah nama pada bangun ruang berikut.
Pilihan: A. Bola
B. Balok
C. Kerucut
D. Tabung
Transkripsi visual: Gambar menunjukkan sebuah bangun ruang berbentuk silinder (tabung) dengan dua sisi datar berbentuk lingkaran di bagian atas dan bawah serta satu sisi lengkung yang menyelimuti. Terdapat kotak teks di bawah gambar dengan tulisan 'Nama = ___'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `aaf396a280df35704272b0d3`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 8 |
| C | 4 |
| D | 5 |

![Gambar sumber soal 21](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengidentifikasi dan menghitung bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada tubuh (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk lengkung yang terlihat adalah: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah pada tubuh anjing. Total ada 5 bentuk lengkung.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `83ef434ce391437dcc0532fc3700c652daf7e0cd27669fe40a99f5504e3b7367`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3443 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3463 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3455 |

Run 1 — solusi: Mengidentifikasi dan menghitung bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada tubuh (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik tertentu (lengkung) dari sebuah gambar komposit. Ini adalah prosedur langsung untuk mengenali dan menghitung bentuk.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep bentuk dasar (lingkaran/oval vs bangun datar bersudut) dan kemampuan untuk mengkategorikan elemen visual ke dalam konsep tersebut.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini memerlukan ketelitian visual untuk membedakan bentuk lengkung dari bentuk bersudut (persegi/persegi panjang). Tidak ada langkah perencanaan yang kompleks atau integrasi konsep yang sulit bagi siswa kelas 2.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran, persegi, segitiga) dan kemampuan berhitung dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa mengidentifikasi bentuk geometri dasar. Tugas ini hanya memerlukan pengamatan visual langsung dan penghitungan sederhana. |

Run 2 — solusi: Mengidentifikasi dan menghitung bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik tertentu (lengkung) dari sebuah gambar komposit. Ini adalah prosedur langsung untuk mengenali dan menghitung elemen visual.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap konsep bentuk geometri dasar (lengkung vs tidak lengkung) dan kemampuan untuk mengklasifikasikan objek berdasarkan atribut tersebut.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini sederhana bagi siswa kelas 2. Siswa hanya perlu membedakan bentuk lengkung dari bentuk bersudut (persegi/persegi panjang) dan menghitungnya. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk geometri dasar (lingkaran/oval vs persegi/persegi panjang) dan kemampuan berhitung dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas visual counting sederhana sesuai dengan kurikulum kelas 2 untuk mengidentifikasi atribut bangun datar. |

Run 3 — solusi: Mengidentifikasi dan menghitung objek dengan sisi lengkung: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak di badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik tertentu (lengkung) dari sebuah gambar komposit. Ini adalah tugas pengenalan dan penghitungan langsung, yang termasuk dalam domain knowing.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap konsep bentuk geometri (lengkung vs tidak lengkung), yang merupakan pengetahuan konseptual dasar.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena tugasnya bersifat langsung: mengidentifikasi dan menghitung objek visual yang jelas. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk geometri dasar (lingkaran/oval vs poligon). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa mengklasifikasikan bentuk geometri sederhana. Tugas menghitung objek visual yang terpisah adalah aktivitas rutin yang sesuai dengan tingkat kelas. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006760; applying=0.993240; reasoning=0.000000 | applying | 0.993240 | 0.036876 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.324906; conceptual=0.635282; procedural=0.039812; metacognitive=0.000000 | conceptual | 0.635282 | 0.563966 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.870266; Medium=0.126742; Hard=0.002993 | Easy | 0.870266 | 0.364205 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993240; −Σp ln(p) = 0.040513; H = 0.040513/ln(3) = 0.036876; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.635282; −Σp ln(p) = 0.781822; H = 0.781822/ln(4) = 0.563966; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.870266; −Σp ln(p) = 0.400120; H = 0.400120/ln(3) = 0.364205; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Menyusun dan Mengurai Bentuk Bangun
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
Pilihan: A. 6
B. 8
C. 4
D. 5
Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk lengkung yang terlihat adalah: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah pada tubuh anjing. Total ada 5 bentuk lengkung.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `801ce06c2a691e98bf7478c5`

Amati gambar berikut. Temukan benda-benda yang posisinya sebagai berikut.<br><br>Di bawah tempat tidur ada ....

| Opsi | Isi |
|---|---|
| A | tas ransel dan penggaris segitiga |
| B | sandal dan mainan mobil-mobilan |
| C | kotak penyimpanan berwarna biru |
| D | boneka beruang di atas kursi |

![Gambar sumber soal 22](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0121-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Mengamati area di bawah tempat tidur pada gambar, ditemukan sepasang sandal dan mainan mobil-mobilan. Pilihan B sesuai dengan pengamatan ini.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0121-01.png. Transkripsi visual: Gambar menunjukkan suasana kamar tidur. Terdapat tempat tidur dengan sprei biru muda dan bantal hijau. Di kolong (bawah) tempat tidur, terlihat sepasang sandal hijau dan sebuah mainan mobil-mobilan. Di area lain terdapat meja belajar, kursi dengan boneka beruang, kotak penyimpanan biru, dan seorang anak perempuan yang sedang bermain dengan kotak kardus.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7c2955dc1e20dade59bdd3be478521923b643afbd4b1ab563a609817e44daf98`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3408 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3423 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3408 |

Run 1 — solusi: Mengamati area di bawah tempat tidur pada gambar, ditemukan sepasang sandal dan mainan mobil-mobilan. Pilihan B sesuai dengan pengamatan ini.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi posisi benda berdasarkan gambar. Ini adalah tugas membaca representasi visual dan mengenali hubungan spasial dasar, yang termasuk dalam domain knowing.. Bukti: Temukan benda-benda yang posisinya sebagai berikut.; Di bawah tempat tidur ada ....
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep posisi (spasial) dasar, yaitu 'di bawah'. Ini adalah pengetahuan konseptual mengenai hubungan spasial.. Bukti: Di bawah tempat tidur ada ....
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu melakukan observasi visual sederhana untuk mencocokkan deskripsi posisi dengan objek yang terlihat. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: Di bawah tempat tidur ada ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali objek dan memahami konsep posisi dasar (di atas, di bawah, di samping). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mengidentifikasi posisi benda dalam gambar adalah materi standar kelas 2 yang bersifat observasional langsung tanpa beban kognitif tinggi. |

Run 2 — solusi: Mengamati area di bawah tempat tidur pada gambar, ditemukan sepasang sandal dan mainan mobil-mobilan. Pilihan B sesuai dengan pengamatan ini.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi lokasi spasial benda berdasarkan gambar. Ini adalah tugas mengenali dan membaca informasi visual yang langsung, yang termasuk dalam domain knowing.. Bukti: Temukan benda-benda yang posisinya sebagai berikut.; Di bawah tempat tidur ada ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep posisi atau letak benda (spasial), yang merupakan pengetahuan konseptual dasar.. Bukti: Di bawah tempat tidur ada ....
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Siswa hanya perlu melakukan observasi visual sederhana untuk mencocokkan posisi benda dengan deskripsi yang diberikan. Tidak ada langkah kompleks atau perencanaan yang diperlukan.. Bukti: Di bawah tempat tidur ada ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali konsep posisi (di atas, di bawah, di samping) dan kemampuan mengamati gambar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi posisi benda adalah materi standar kelas 2 yang sangat mendasar dan familiar. |

Run 3 — solusi: Mengamati posisi benda pada gambar, di bawah tempat tidur terdapat sandal dan mainan mobil-mobilan. Pilihan B sesuai dengan pengamatan ini.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi posisi benda berdasarkan gambar. Ini adalah tugas mengenali dan membaca informasi spasial yang disajikan secara visual, yang termasuk dalam domain knowing.. Bukti: Temukan benda-benda yang posisinya sebagai berikut.; Di bawah tempat tidur ada ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep posisi (spasial) seperti 'di bawah', yang merupakan pengetahuan konseptual dasar tentang hubungan antar objek dalam ruang.. Bukti: Temukan benda-benda yang posisinya sebagai berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan observasi visual langsung untuk mencocokkan deskripsi posisi dengan objek yang terlihat. Tidak ada langkah kompleks atau penalaran yang diperlukan.. Bukti: Di bawah tempat tidur ada ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali objek dan memahami konsep posisi dasar (di atas, di bawah, di samping). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mengidentifikasi posisi benda adalah materi dasar kelas 2. Soal ini bersifat langsung dan tidak menuntut perencanaan atau integrasi konsep. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 149/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000017; applying=0.999983; reasoning=0.000000 | applying | 0.999983 | 0.000188 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.129822; conceptual=0.869043; procedural=0.001135; metacognitive=0.000000 | conceptual | 0.869043 | 0.284729 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.778413; Medium=0.215116; Hard=0.006471 | Easy | 0.778413 | 0.508051 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999983; −Σp ln(p) = 0.000207; H = 0.000207/ln(3) = 0.000188; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.869043; −Σp ln(p) = 0.394718; H = 0.394718/ln(4) = 0.284729; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.778413; −Σp ln(p) = 0.558151; H = 0.558151/ln(3) = 0.508051; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Posisi Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati gambar berikut. Temukan benda-benda yang posisinya sebagai berikut.

Di bawah tempat tidur ada ....
Pilihan: A. tas ransel dan penggaris segitiga
B. sandal dan mainan mobil-mobilan
C. kotak penyimpanan berwarna biru
D. boneka beruang di atas kursi
Transkripsi visual: Gambar menunjukkan suasana kamar tidur. Terdapat tempat tidur dengan sprei biru muda dan bantal hijau. Di kolong (bawah) tempat tidur, terlihat sepasang sandal hijau dan sebuah mainan mobil-mobilan. Di area lain terdapat meja belajar, kursi dengan boneka beruang, kotak penyimpanan biru, dan seorang anak perempuan yang sedang bermain dengan kotak kardus.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `44d1998fb7727977ef848256`

Perhatikan posisi kucing berikut. Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.<br><br>Kucing duduk di .... meja.

| Opsi | Isi |
|---|---|
| A | belakang |
| B | bawah |
| C | kanan |
| D | atas |

![Gambar sumber soal 23](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0119-12.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Berdasarkan pengamatan visual, kucing berada di permukaan atas meja, sehingga kata yang tepat untuk melengkapi kalimat adalah 'atas'.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0119-12.png. Transkripsi visual: Gambar menunjukkan seekor kucing berwarna oranye sedang duduk di atas permukaan sebuah meja kayu berwarna cokelat. Terdapat teks di bawah gambar: 'Kucing duduk di ____ meja.'

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b1a43b35c618ef2f31c67c441b01565087e2993854950b7b615d8b67a427b93a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3374 |
| 2 | success | valid / verified | knowing | factual | Easy | 3383 |
| 3 | success | valid / verified | knowing | factual | Easy | 3344 |

Run 1 — solusi: Berdasarkan pengamatan visual, kucing berada di permukaan atas meja, sehingga kata yang tepat untuk melengkapi kalimat adalah 'atas'.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi posisi spasial objek (kucing) relatif terhadap objek lain (meja) berdasarkan representasi visual. Ini adalah tugas pengenalan langsung terhadap konsep posisi, yang termasuk dalam domain knowing.. Bukti: Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.; Kucing duduk di .... meja.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang istilah posisi (atas, bawah, dll.), yang merupakan pengetahuan konseptual dasar mengenai hubungan spasial.. Bukti: Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana dan langsung. Siswa hanya perlu mengamati gambar dan memilih istilah posisi yang paling tepat dari pilihan yang tersedia. Tidak ada langkah kompleks atau perencanaan yang diperlukan.. Bukti: Kucing duduk di .... meja.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kosakata posisi spasial (atas, bawah, depan, belakang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 2, mengidentifikasi posisi benda berdasarkan gambar adalah tugas yang sangat mendasar dan rutin. |

Run 2 — solusi: Berdasarkan pengamatan visual, kucing berada di permukaan meja, sehingga posisi yang tepat adalah 'atas'.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi posisi spasial objek (kucing) relatif terhadap objek lain (meja) berdasarkan representasi visual. Ini adalah tugas pengenalan langsung terhadap konsep posisi, yang termasuk dalam domain knowing.. Bukti: Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.; Kucing duduk di .... meja.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang istilah posisi (atas, bawah, dll.), yang merupakan elemen dasar atau fakta dalam geometri spasial.. Bukti: Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pengamatan visual langsung dan pemilihan kata posisi yang paling sesuai dengan gambar. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Kucing duduk di .... meja.; Pilihan: A. belakang, B. bawah, C. kanan, D. atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kosakata posisi spasial (atas, bawah, depan, belakang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, mengidentifikasi posisi benda berdasarkan gambar adalah tugas yang sangat mendasar dan rutin. |

Run 3 — solusi: Berdasarkan pengamatan visual, kucing berada di atas permukaan meja, sehingga kata yang tepat untuk melengkapi kalimat adalah 'atas'.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi posisi spasial objek (kucing) relatif terhadap objek lain (meja). Ini adalah tugas pengenalan langsung terhadap konsep posisi yang sudah dipelajari, sehingga termasuk dalam domain knowing.. Bukti: Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.; Kucing duduk di .... meja.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang istilah posisi (atas, bawah, belakang, kanan) yang merupakan elemen dasar dalam geometri spasial.. Bukti: Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung dan pemilihan istilah posisi yang tepat. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Kucing duduk di .... meja.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang istilah posisi (atas, bawah, samping). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, mengidentifikasi posisi benda di atas meja adalah tugas yang sangat mendasar dan familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4654`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengidentifikasi posisi spasial objek (kucing) relatif terhadap objek lain (meja) berdasarkan representasi visual. Ini adalah tugas pengenalan langsung terhadap konsep posisi, yang termasuk dalam domain knowing.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman tentang istilah posisi (atas, bawah, dll.), yang merupakan elemen dasar atau fakta dalam geometri spasial.
- Intended difficulty `Easy`: Soal ini sangat mudah karena hanya memerlukan pengamatan visual langsung dan pemilihan kata posisi yang paling sesuai dengan gambar. Tidak ada langkah perencanaan atau integrasi yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kosakata posisi spasial (atas, bawah, depan, belakang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, mengidentifikasi posisi benda berdasarkan gambar adalah tugas yang sangat mendasar dan rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 104/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000193; applying=0.999807; reasoning=0.000000 | applying | 0.999807 | 0.001680 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.352794; conceptual=0.586027; procedural=0.061179; metacognitive=0.000000 | conceptual | 0.586027 | 0.614345 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.879714; Medium=0.116283; Hard=0.004003 | Easy | 0.879714 | 0.350490 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999807; −Σp ln(p) = 0.001846; H = 0.001846/ln(3) = 0.001680; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.586027; −Σp ln(p) = 0.851663; H = 0.851663/ln(4) = 0.614345; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.879714; −Σp ln(p) = 0.385052; H = 0.385052/ln(3) = 0.350490; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Posisi Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan posisi kucing berikut. Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.

Kucing duduk di .... meja.
Pilihan: A. belakang
B. bawah
C. kanan
D. atas
Transkripsi visual: Gambar menunjukkan seekor kucing berwarna oranye sedang duduk di atas permukaan sebuah meja kayu berwarna cokelat. Terdapat teks di bawah gambar: 'Kucing duduk di ____ meja.'
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `c5e424e9914591b1d5286ef0`

Amati pola berikut. Tentukan pola gambar berikutnya.

| Opsi | Isi |
|---|---|
| A | kelinci |
| B | kupu-kupu |
| C | bunga |
| D | heksagon |

![Gambar sumber soal 24](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah gambar kupu-kupu terakhir, gambar berikutnya dalam urutan adalah kelinci.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Terdapat baris gambar dengan pola berulang: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Di akhir baris terdapat garis kosong untuk diisi.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `50eefa2f2a9a07c4227b58621944c6f66a86ba9b8b5bfc4a8bc0df2549799638`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3406 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3430 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3514 |

Run 1 — solusi: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah gambar kupu-kupu terakhir, gambar berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi unit pengulangan dalam pola visual dan menerapkan aturan pengulangan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan prosedur pengenalan pola yang rutin.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating pattern), yang merupakan struktur konseptual dasar dalam matematika awal.. Bukti: Amati pola berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali unit pengulangan (kupu-kupu, kelinci, kelinci) dan melanjutkan urutan tersebut. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali objek visual dan urutan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, mengenali dan melanjutkan pola berulang sederhana adalah tugas yang familiar dan sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Pola yang diberikan adalah pengulangan unit (kupu-kupu, kelinci, kelinci). Setelah gambar kupu-kupu terakhir, elemen berikutnya dalam urutan pengulangan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengulangan dalam pola visual sederhana dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan prosedur pengenalan pola yang rutin.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan struktur konseptual dasar dalam matematika awal.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali unit pengulangan (kupu-kupu, kelinci, kelinci) dan melanjutkan urutan tersebut. Tidak ada kendala yang berinteraksi atau perencanaan kompleks yang diperlukan.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan dan pengulangan gambar sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, mengenali dan melanjutkan pola berulang adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah gambar kupu-kupu terakhir, gambar berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi unit pengulangan dalam pola visual dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan konsep pola yang sudah dipelajari di kelas 2.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan pengetahuan konseptual dasar dalam matematika awal.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 2. Pola yang diberikan jelas dan berulang secara konsisten. Siswa hanya perlu mengenali unit pengulangan (kupu-kupu, kelinci, kelinci) dan melanjutkan urutan tersebut. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan dan pengulangan objek visual sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenali dan melanjutkan pola berulang adalah materi standar kelas 2. Soal ini menyajikan pola yang sangat jelas tanpa jebakan atau kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 100/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.013709; applying=0.986291; reasoning=0.000000 | applying | 0.986291 | 0.065920 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.124466; conceptual=0.868129; procedural=0.007405; metacognitive=0.000000 | conceptual | 0.868129 | 0.301844 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.851400; Medium=0.143925; Hard=0.004675 | Easy | 0.851400 | 0.401456 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.986291; −Σp ln(p) = 0.072421; H = 0.072421/ln(3) = 0.065920; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.868129; −Σp ln(p) = 0.418445; H = 0.418445/ln(4) = 0.301844; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.851400; −Σp ln(p) = 0.441044; H = 0.441044/ln(3) = 0.401456; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Pola
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati pola berikut. Tentukan pola gambar berikutnya.
Pilihan: A. kelinci
B. kupu-kupu
C. bunga
D. heksagon
Transkripsi visual: Terdapat baris gambar dengan pola berulang: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Di akhir baris terdapat garis kosong untuk diisi.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `66d36724cd73e571bae49422`

Amati pola warna berikut. Warna apa yang benar untuk melanjutkan polanya.

| Opsi | Isi |
|---|---|
| A | hijau |
| B | merah muda |
| C | biru |
| D | oranye |

![Gambar sumber soal 25](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0131-02.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pola berulang oranye-hijau. Setelah oranye, warna berikutnya adalah hijau.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-02.png. Transkripsi visual: Terdapat baris pola yang terdiri dari lingkaran berwarna oranye, hijau, oranye, hijau, oranye, dan satu lingkaran kosong di akhir.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dc3da4b3e93bf6337405cfbd86c2e31066418d87a0ee6effbb81a69e84d5143c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3308 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3337 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3329 |

Run 1 — solusi: Pola berulang oranye-hijau. Setelah oranye, warna berikutnya adalah hijau.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali aturan pola berulang sederhana (oranye-hijau) dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah prosedur langsung.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang sederhana, yang merupakan struktur konseptual dasar dalam matematika awal.. Bukti: Amati pola warna berikut
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 2 karena pola yang disajikan sangat sederhana (AB-AB) dan hanya memerlukan satu langkah identifikasi untuk menentukan elemen berikutnya.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan warna atau objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola berulang sederhana adalah materi dasar kelas 2 yang sudah sangat familiar. |

Run 2 — solusi: Pola warna adalah oranye-hijau yang berulang. Setelah lingkaran oranye terakhir, warna berikutnya dalam urutan adalah hijau.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi aturan pola sederhana (AB-AB) dan menerapkannya untuk menentukan elemen berikutnya. Ini adalah tugas pengenalan dan penerapan prosedur langsung.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (konseptual) yang merupakan materi dasar kelas 2.. Bukti: Amati pola warna berikut
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena pola yang disajikan adalah pola berulang sederhana (AB-AB) dengan elemen yang sangat jelas. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali warna dan urutan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola berulang adalah materi standar kelas 2. Soal ini tidak menuntut perencanaan atau integrasi langkah, sehingga dikategorikan mudah. |

Run 3 — solusi: Pola yang diberikan adalah pengulangan dua warna: oranye dan hijau. Karena lingkaran terakhir yang terlihat adalah oranye, maka warna berikutnya dalam pola tersebut adalah hijau.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali aturan pengulangan sederhana (AB-AB) dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah prosedur langsung yang familiar bagi siswa kelas 2.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola sederhana, yaitu pengulangan elemen secara teratur.. Bukti: Amati pola warna berikut
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena pola yang diberikan adalah pola pengulangan dua elemen yang sangat sederhana dan langsung terlihat.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali warna dan urutan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola pengulangan dua warna adalah materi dasar yang sesuai untuk kelas 2, dengan tingkat kesulitan rendah karena tidak memerlukan perencanaan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 84/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.096437; applying=0.903563; reasoning=0.000000 | applying | 0.903563 | 0.288712 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.189361; conceptual=0.805040; procedural=0.005599; metacognitive=0.000000 | conceptual | 0.805040 | 0.374187 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.857362; Medium=0.138687; Hard=0.003951 | Easy | 0.857362 | 0.389389 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.903563; −Σp ln(p) = 0.317183; H = 0.317183/ln(3) = 0.288712; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.805040; −Σp ln(p) = 0.518733; H = 0.518733/ln(4) = 0.374187; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.857362; −Σp ln(p) = 0.427788; H = 0.427788/ln(3) = 0.389389; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Pola
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati pola warna berikut. Warna apa yang benar untuk melanjutkan polanya.
Pilihan: A. hijau
B. merah muda
C. biru
D. oranye
Transkripsi visual: Terdapat baris pola yang terdiri dari lingkaran berwarna oranye, hijau, oranye, hijau, oranye, dan satu lingkaran kosong di akhir.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `81440a329d7562b80ba3a0a1`

Perhatikan gambar berikut. Manakah yang bukan setengah?

| Opsi | Isi |
|---|---|
| A | C (lingkaran biru-putih, dibagi garis mendatar sama besar) |
| B | G (persegi panjang cokelat-putih, dibagi garis tegak sama besar) |
| C | B (segitiga hijau-putih, dibagi garis tegak tidak sama besar) |
| D | F (segi enam ungu-putih, dibagi garis mendatar sama besar) |

![Gambar sumber soal 26](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0146-06.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Konsep setengah (1/2) memerlukan pembagian benda menjadi dua bagian yang sama besar. Gambar B (segitiga) dibagi menjadi dua bagian yang tidak sama besar (sisi kiri lebih besar dari sisi kanan), sehingga tidak merepresentasikan setengah.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0146-06.png. Transkripsi visual: Terdapat tujuh gambar bentuk geometri yang diberi label A sampai G. Gambar A adalah persegi panjang dibagi dua sama besar. Gambar B adalah segitiga yang dibagi garis tegak menjadi dua bagian yang tidak sama besar (bagian kiri lebih luas daripada bagian kanan). Gambar C adalah lingkaran dibagi dua sama besar secara horizontal. Gambar D adalah bentuk hati dibagi dua sama besar. Gambar E adalah bintang utuh tanpa pembagian. Gambar F adalah segi enam dibagi dua sama besar secara horizontal. Gambar G adalah persegi panjang dibagi dua sama besar secara vertikal. Soal meminta untuk mengidentifikasi gambar yang bukan merupakan setengah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9817af3dc9a7a1a47cef0cd0f48747c02206ae6587d588ca833a108a83f7158a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3537 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3521 |
| 3 | success | valid / verified | applying | conceptual | Easy | 4430 |

Run 1 — solusi: Konsep setengah (1/2) memerlukan pembagian benda menjadi dua bagian yang sama besar. Gambar B (segitiga) dibagi menjadi dua bagian yang tidak sama besar (sisi kiri lebih besar dari sisi kanan), sehingga tidak merepresentasikan setengah.
- Domain kognitif `classify/applying`: Siswa perlu mengenali definisi konsep 'setengah' sebagai pembagian menjadi dua bagian yang sama besar dan menerapkan pemahaman ini untuk mengevaluasi setiap opsi visual. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Manakah yang bukan setengah?; gambar B (segitiga hijau-putih, dibagi garis tegak tidak sama besar)
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa tentang prinsip dasar pecahan (setengah) sebagai hubungan antara bagian dan keseluruhan yang sama besar.. Bukti: Manakah yang bukan setengah?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa membedakan antara representasi yang benar dan salah dari konsep setengah. Siswa harus memeriksa setiap opsi secara visual. Tugas ini bersifat rutin bagi kelas 2 karena hanya memerlukan pengenalan visual sederhana terhadap konsep pembagian sama besar.. Bukti: Manakah yang bukan setengah?; gambar B (segitiga hijau-putih, dibagi garis tegak tidak sama besar)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah sebagai dua bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah mempelajari konsep pecahan sederhana (setengah) melalui representasi visual. Membedakan pembagian sama besar dan tidak sama besar adalah tugas standar yang familiar. |

Run 2 — solusi: Konsep setengah memerlukan pembagian benda menjadi dua bagian yang sama besar. Gambar B (segitiga) dibagi menjadi dua bagian yang ukurannya jelas tidak sama (satu bagian lebih besar dari yang lain), sehingga bukan merupakan setengah.
- Domain kognitif `classify/applying`: Siswa perlu mengenali definisi konsep 'setengah' (dua bagian yang sama besar) dan menerapkannya untuk mengevaluasi setiap pilihan gambar. Ini adalah penerapan konsep pada konteks visual rutin.. Bukti: Manakah yang bukan setengah?; gambar B dibagi menjadi dua bagian yang tidak sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai pembagian menjadi dua bagian yang sama besar.. Bukti: Manakah yang bukan setengah?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan inspeksi visual sederhana untuk membandingkan ukuran dua bagian pada setiap bangun. Tidak ada perhitungan kompleks atau perencanaan langkah yang rumit.. Bukti: Manakah yang bukan setengah?; gambar B (segitiga hijau-putih, dibagi garis tegak tidak sama besar)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah sebagai dua bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pembagian sama besar dan tidak sama besar adalah materi standar yang rutin dan langsung. |

Run 3 — solusi: Setengah didefinisikan sebagai dua bagian yang sama besar. Gambar B menunjukkan segitiga yang dibagi menjadi dua bagian dengan ukuran berbeda, sehingga bukan setengah.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep setengah (dua bagian sama besar) dan menerapkannya untuk mengidentifikasi gambar yang tidak memenuhi kriteria tersebut.. Bukti: Manakah yang bukan setengah?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai pembagian benda menjadi dua bagian yang sama besar.. Bukti: Manakah yang bukan setengah?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa membedakan antara representasi setengah yang benar dan salah. Ini adalah tugas rutin untuk kelas 2.. Bukti: Manakah yang bukan setengah?; gambar B dibagi menjadi dua bagian yang tidak sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk dan konsep pembagian dua bagian sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah mempelajari konsep pecahan sederhana (setengah) melalui representasi visual. Mengidentifikasi ketidaksamaan ukuran bagian adalah tugas langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 219/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001360; applying=0.998640; reasoning=0.000000 | applying | 0.998640 | 0.009410 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.002647; conceptual=0.990331; procedural=0.007022; metacognitive=0.000000 | conceptual | 0.990331 | 0.043391 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.701610; Medium=0.290872; Hard=0.007518 | Easy | 0.701610 | 0.586732 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998640; −Σp ln(p) = 0.010338; H = 0.010338/ln(3) = 0.009410; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.990331; −Σp ln(p) = 0.060153; H = 0.060153/ln(4) = 0.043391; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.701610; −Σp ln(p) = 0.644591; H = 0.644591/ln(3) = 0.586732; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut. Manakah yang bukan setengah?
Pilihan: A. C (lingkaran biru-putih, dibagi garis mendatar sama besar)
B. G (persegi panjang cokelat-putih, dibagi garis tegak sama besar)
C. B (segitiga hijau-putih, dibagi garis tegak tidak sama besar)
D. F (segi enam ungu-putih, dibagi garis mendatar sama besar)
Transkripsi visual: Terdapat tujuh gambar bentuk geometri yang diberi label A sampai G. Gambar A adalah persegi panjang dibagi dua sama besar. Gambar B adalah segitiga yang dibagi garis tegak menjadi dua bagian yang tidak sama besar (bagian kiri lebih luas daripada bagian kanan). Gambar C adalah lingkaran dibagi dua sama besar secara horizontal. Gambar D adalah bentuk hati dibagi dua sama besar. Gambar E adalah bintang utuh tanpa pembagian. Gambar F adalah segi enam dibagi dua sama besar secara horizontal. Gambar G adalah persegi panjang dibagi dua sama besar secara vertikal. Soal meminta untuk mengidentifikasi gambar yang bukan merupakan setengah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `90c3bb9928fdd60f115a0d85`

Perhatikan gambar berikut. Manakah yang setengah?

| Opsi | Isi |
|---|---|
| A | Tidak ada gambar yang menunjukkan setengah |
| B | Gambar kanan (dibagi oleh garis diagonal) |
| C | Gambar kiri (dibagi rata oleh garis tegak di tengah) |
| D | Kedua gambar menunjukkan setengah |

![Gambar sumber soal 27](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0145-02.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Definisi setengah adalah membagi benda menjadi dua bagian yang sama besar. Gambar kiri menunjukkan pembagian simetris dengan dua bagian identik, sedangkan gambar kanan menunjukkan pembagian tidak merata.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0145-02.png. Transkripsi visual: Terdapat dua gambar hati. Gambar kiri dibagi oleh garis vertikal tepat di tengah, menghasilkan dua bagian (merah dan toska) yang tampak sama besar. Gambar kanan dibagi oleh garis diagonal yang tidak melalui pusat simetri, menghasilkan bagian merah yang lebih kecil daripada bagian toska.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `71ce6deee7d67d281fbd377da552700cdc8ef1fc804421c453c8090d106750c6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3365 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3384 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3390 |

Run 1 — solusi: Definisi setengah adalah membagi benda menjadi dua bagian yang sama besar. Gambar kiri menunjukkan pembagian simetris dengan dua bagian identik, sedangkan gambar kanan menunjukkan pembagian tidak merata.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali representasi visual dari konsep pecahan sederhana (setengah) dengan membandingkan dua gambar. Ini adalah pengenalan konsep dasar pecahan.. Bukti: Manakah yang setengah?; Gambar kiri (dibagi rata oleh garis tegak di tengah)
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa arti 'setengah' (bagian yang sama besar) dalam bentuk visual.. Bukti: Setengah dari Benda Utuh
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi gambar mana yang terbagi menjadi dua bagian sama besar. Tidak ada langkah perhitungan atau perencanaan yang kompleks.. Bukti: Manakah yang setengah?; Perhatikan gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman visual tentang kesamaan ukuran dan konsep dasar pecahan setengah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pembagian yang sama besar dan tidak sama besar adalah materi dasar yang familiar. |

Run 2 — solusi: Konsep setengah (1/2) memerlukan pembagian benda menjadi dua bagian yang sama besar. Gambar kiri menunjukkan pembagian simetris yang menghasilkan dua bagian identik, sedangkan gambar kanan tidak.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali representasi visual dari konsep pecahan sederhana (setengah). Ini adalah pengenalan langsung terhadap definisi 'setengah' sebagai dua bagian yang sama besar.. Bukti: Manakah yang setengah?; Gambar kiri (dibagi rata oleh garis tegak di tengah)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang dimaksud dengan 'setengah' (bagian yang sama besar), bukan sekadar menghafal fakta atau prosedur algoritmik.. Bukti: Manakah yang setengah?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan dua representasi visual sederhana untuk mengidentifikasi mana yang memenuhi kriteria 'sama besar'. Tidak ada langkah kompleks atau integrasi yang diperlukan.. Bukti: Manakah yang setengah?; Perhatikan gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 'sama besar' atau 'setengah' sebagai dua bagian yang identik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pembagian yang sama besar dan tidak sama besar adalah tugas rutin yang sesuai dengan kurikulum awal pengenalan pecahan. |

Run 3 — solusi: Setengah didefinisikan sebagai dua bagian yang sama besar. Gambar kiri menunjukkan hati yang dibagi oleh garis vertikal tepat di tengah, sehingga luas bagian merah sama dengan luas bagian toska. Gambar kanan tidak sama besar.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali representasi visual dari konsep pecahan 'setengah' dengan membandingkan dua gambar. Ini adalah tugas pengenalan konsep dasar yang sudah dipelajari.. Bukti: Manakah yang setengah?; gambar kiri dipotong oleh garis tegak tepat di tengah sehingga menghasilkan dua bagian sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang dimaksud dengan 'setengah' (dua bagian yang sama besar) melalui representasi visual.. Bukti: Manakah yang setengah?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi gambar mana yang terbagi menjadi dua bagian yang sama besar. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: Manakah yang setengah?; gambar kiri dipotong oleh garis tegak tepat di tengah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 'sama besar' atau 'setengah' (pecahan sederhana). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pembagian yang sama besar dan tidak sama besar adalah materi dasar yang rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 133/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001468; applying=0.998532; reasoning=0.000000 | applying | 0.998532 | 0.010050 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.010234; conceptual=0.982245; procedural=0.007521; metacognitive=0.000000 | conceptual | 0.982245 | 0.073049 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.736788; Medium=0.258702; Hard=0.004510 | Easy | 0.736788 | 0.545418 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998532; −Σp ln(p) = 0.011041; H = 0.011041/ln(3) = 0.010050; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.982245; −Σp ln(p) = 0.101267; H = 0.101267/ln(4) = 0.073049; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.736788; −Σp ln(p) = 0.599203; H = 0.599203/ln(3) = 0.545418; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut. Manakah yang setengah?
Pilihan: A. Tidak ada gambar yang menunjukkan setengah
B. Gambar kanan (dibagi oleh garis diagonal)
C. Gambar kiri (dibagi rata oleh garis tegak di tengah)
D. Kedua gambar menunjukkan setengah
Transkripsi visual: Terdapat dua gambar hati. Gambar kiri dibagi oleh garis vertikal tepat di tengah, menghasilkan dua bagian (merah dan toska) yang tampak sama besar. Gambar kanan dibagi oleh garis diagonal yang tidak melalui pusat simetri, menghasilkan bagian merah yang lebih kecil daripada bagian toska.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `5eacf4162dd820a1d51e8bdc`

Perhatikan gambar berikut.<br><br>Kelompok mana yang menunjukkan setengah.

| Opsi | Isi |
|---|---|
| A | Kedua baris menunjukkan setengah |
| B | Tidak ada baris yang menunjukkan setengah |
| C | Baris pertama (2 monyet dan 2 monyet) |
| D | Baris kedua (1 monyet dan 3 monyet) |

![Gambar sumber soal 28](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0150-12.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Setengah berarti membagi kumpulan benda menjadi dua kelompok yang sama banyak. Baris pertama membagi 4 monyet menjadi dua kelompok berisi 2 monyet dan 2 monyet (sama banyak). Baris kedua membagi 4 monyet menjadi 1 dan 3 (tidak sama banyak). Jadi, baris pertama menunjukkan setengah.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0150-12.png. Transkripsi visual: Gambar menunjukkan 4 monyet di baris paling atas. Di bawahnya terdapat dua baris kotak. Baris pertama berisi dua kotak, masing-masing berisi 2 monyet (total 4 monyet). Baris kedua berisi dua kotak, kotak kiri berisi 1 monyet dan kotak kanan berisi 3 monyet (total 4 monyet).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d0373d2c496d96f88593d848e9f2bb4e159a4554eca917f12ba98dcbad386eed`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3462 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3464 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3468 |

Run 1 — solusi: Setengah berarti membagi kumpulan benda menjadi dua kelompok yang sama banyak. Baris pertama membagi 4 monyet menjadi dua kelompok berisi 2 monyet dan 2 monyet (sama banyak). Baris kedua membagi 4 monyet menjadi 1 dan 3 (tidak sama banyak). Jadi, baris pertama menunjukkan setengah.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali representasi visual dari konsep 'setengah' (pembagian menjadi dua bagian yang sama). Ini adalah penerapan langsung dari konsep dasar pecahan/pembagian sederhana yang sudah dipelajari di kelas 2.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet); Baris kedua (1 monyet dan 3 monyet)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'setengah' sebagai pembagian dua kelompok dengan jumlah anggota yang sama.. Bukti: Kelompok mana yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membandingkan jumlah benda dalam dua kelompok yang disajikan secara visual. Tidak ada langkah perhitungan kompleks atau perencanaan strategi yang diperlukan.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet); Baris kedua (1 monyet dan 3 monyet)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jumlah benda dan konsep membagi dua kelompok sama banyak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah familiar dengan konsep membagi benda menjadi dua bagian sama besar secara visual. |

Run 2 — solusi: Setengah berarti membagi jumlah benda menjadi dua kelompok yang sama banyak. Baris pertama membagi 4 monyet menjadi dua kelompok berisi 2 monyet (2 = 2), yang menunjukkan setengah. Baris kedua membagi 4 monyet menjadi kelompok berisi 1 dan 3, yang tidak sama banyak.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi representasi visual dari konsep 'setengah' (pembagian menjadi dua bagian sama besar). Ini adalah penerapan langsung dari konsep dasar pecahan/pembagian sederhana pada konteks rutin.. Bukti: Kelompok mana yang menunjukkan setengah.; Baris pertama (2 monyet dan 2 monyet); Baris kedua (1 monyet dan 3 monyet)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'setengah' sebagai pembagian benda menjadi dua kelompok yang sama banyak.. Bukti: Kelompok mana yang menunjukkan setengah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan jumlah benda dalam dua kelompok yang disajikan secara visual. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Kelompok mana yang menunjukkan setengah.; Baris pertama (2 monyet dan 2 monyet); Baris kedua (1 monyet dan 3 monyet)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jumlah benda dan konsep membagi dua kelompok sama banyak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, konsep setengah sebagai pembagian dua kelompok sama banyak adalah materi standar yang familiar. Tugas visual ini tidak memerlukan perhitungan rumit. |

Run 3 — solusi: Setengah berarti membagi jumlah total (4 monyet) menjadi dua kelompok yang sama banyak. Baris pertama menunjukkan 2 monyet dan 2 monyet (sama banyak), sehingga ini adalah setengah. Baris kedua menunjukkan 1 monyet dan 3 monyet (tidak sama banyak). Maka, baris pertama adalah jawaban yang benar.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi representasi visual dari konsep 'setengah' (pembagian menjadi dua bagian yang sama). Ini adalah penerapan langsung dari konsep dasar pecahan/pembagian sederhana ke dalam konteks visual yang rutin.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'setengah' sebagai pembagian objek menjadi dua kelompok yang sama besar.. Bukti: Kelompok mana yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membandingkan jumlah objek dalam dua kelompok yang disajikan secara visual. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet); Baris kedua (1 monyet dan 3 monyet)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jumlah benda dan konsep membagi sama rata (setengah). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, membedakan kelompok yang sama banyak (setengah) dari yang tidak sama banyak adalah tugas rutin yang sesuai dengan kurikulum dasar. |

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
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000006 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003371; conceptual=0.992623; procedural=0.004007; metacognitive=0.000000 | conceptual | 0.992623 | 0.035096 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.621945; Medium=0.371331; Hard=0.006724 | Easy | 0.621945 | 0.634311 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000006; H = 0.000006/ln(3) = 0.000006; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.992623; −Σp ln(p) = 0.048654; H = 0.048654/ln(4) = 0.035096; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.621945; −Σp ln(p) = 0.696862; H = 0.696862/ln(3) = 0.634311; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Kumpulan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut.

Kelompok mana yang menunjukkan setengah.
Pilihan: A. Kedua baris menunjukkan setengah
B. Tidak ada baris yang menunjukkan setengah
C. Baris pertama (2 monyet dan 2 monyet)
D. Baris kedua (1 monyet dan 3 monyet)
Transkripsi visual: Gambar menunjukkan 4 monyet di baris paling atas. Di bawahnya terdapat dua baris kotak. Baris pertama berisi dua kotak, masing-masing berisi 2 monyet (total 4 monyet). Baris kedua berisi dua kotak, kotak kiri berisi 1 monyet dan kotak kanan berisi 3 monyet (total 4 monyet).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `2550e20d6fe8dd73c9128673`

Perhatikan gambar berikut.<br><br>Kelompok mana yang menunjukkan setengah.

| Opsi | Isi |
|---|---|
| A | Baris kedua (4 kelinci dan 4 kelinci) |
| B | Tidak ada baris yang menunjukkan setengah |
| C | Baris pertama (3 kelinci dan 5 kelinci) |
| D | Kedua baris menunjukkan setengah |

![Gambar sumber soal 29](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0151-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Setengah berarti membagi sekumpulan benda menjadi dua kelompok yang sama banyak. Baris ketiga memiliki dua kotak dengan masing-masing 4 kelinci (4 sama dengan 4), sehingga ini menunjukkan setengah. Baris kedua memiliki 3 dan 5 kelinci (tidak sama). Maka, baris ketiga adalah yang benar.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0151-01.png. Transkripsi visual: Gambar terdiri dari tiga baris kelinci. Baris pertama berisi 8 kelinci tanpa pembagian kelompok. Baris kedua berisi dua kotak: kotak kiri berisi 3 kelinci, kotak kanan berisi 5 kelinci. Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9b7cd783e6bc99e7ff7fd46ee4f6f4f6c73ff5a7dfdb632c8f542980686dffdc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3495 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3446 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3509 |

Run 1 — solusi: Setengah berarti membagi sekumpulan benda menjadi dua kelompok yang sama banyak. Baris ketiga memiliki dua kotak dengan masing-masing 4 kelinci (4 sama dengan 4), sehingga ini menunjukkan setengah. Baris kedua memiliki 3 dan 5 kelinci (tidak sama). Maka, baris ketiga adalah yang benar.
- Domain kognitif `classify/applying`: Siswa diminta mengenali representasi visual dari konsep 'setengah' (pembagian dua kelompok sama banyak). Ini adalah penerapan langsung dari konsep dasar pecahan/pembagian sederhana yang sudah dipelajari di kelas 2.. Bukti: Kelompok mana yang menunjukkan setengah; Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa arti 'setengah' dalam konteks kumpulan benda, bukan sekadar menghafal fakta atau prosedur algoritmik.. Bukti: Kelompok mana yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan jumlah benda dalam dua kelompok pada setiap baris untuk melihat mana yang sama banyak. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Kelompok mana yang menunjukkan setengah; Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah dan kemampuan menghitung benda hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan kelompok yang sama banyak adalah tugas rutin yang sesuai dengan kurikulum awal tentang pecahan sederhana. |

Run 2 — solusi: Setengah berarti membagi sekumpulan benda menjadi dua bagian yang sama banyak. Baris ketiga memiliki dua kotak dengan jumlah kelinci yang sama, yaitu 4 kelinci di kotak kiri dan 4 kelinci di kotak kanan. Jadi, baris ketiga menunjukkan setengah.
- Domain kognitif `classify/applying`: Siswa diminta mengenali representasi visual dari konsep 'setengah' (pembagian menjadi dua bagian sama banyak). Ini adalah penerapan langsung dari konsep dasar pecahan/pembagian sederhana yang sudah dipelajari di kelas 2.. Bukti: Kelompok mana yang menunjukkan setengah.; Baris kedua (4 kelinci dan 4 kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang arti 'setengah' sebagai pembagian dua kelompok yang sama banyak.. Bukti: Kelompok mana yang menunjukkan setengah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah benda dalam kelompok yang tersedia dan membandingkan apakah jumlahnya sama. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Kelompok mana yang menunjukkan setengah.; Baris kedua (4 kelinci dan 4 kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang dan membandingkan jumlah benda sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan konsep setengah sebagai membagi dua sama banyak. Tugas ini hanya memerlukan observasi visual dan hitung sederhana. |

Run 3 — solusi: Setengah dari kumpulan benda berarti membagi kumpulan tersebut menjadi dua kelompok dengan jumlah yang sama banyak. Baris ketiga memiliki dua kelompok yang masing-masing berisi 4 kelinci (4+4=8), sehingga ini menunjukkan setengah. Baris kedua memiliki 3 dan 5 kelinci (tidak sama). Maka, baris ketiga adalah jawaban yang benar.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi representasi visual dari konsep 'setengah' (pembagian dua kelompok sama banyak). Ini adalah penerapan langsung dari konsep dasar pecahan/pembagian sederhana yang sudah dipelajari di kelas 2.. Bukti: Kelompok mana yang menunjukkan setengah.; Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'setengah' dalam konteks kumpulan benda, yaitu hubungan kesamaan jumlah antara dua bagian.. Bukti: Kelompok mana yang menunjukkan setengah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah benda dalam kelompok yang tersedia dan membandingkannya untuk melihat mana yang memiliki jumlah sama. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Kelompok mana yang menunjukkan setengah.; Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang sampai 10 dan memahami konsep jumlah yang sama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan konsep membagi benda menjadi dua bagian sama besar. Soal ini adalah penerapan langsung dari konsep tersebut tanpa kerumitan tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 133/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000007; applying=0.999993; reasoning=0.000000 | applying | 0.999993 | 0.000083 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.006244; conceptual=0.991681; procedural=0.002076; metacognitive=0.000000 | conceptual | 0.991681 | 0.038087 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.708260; Medium=0.286541; Hard=0.005199 | Easy | 0.708260 | 0.573264 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999993; −Σp ln(p) = 0.000091; H = 0.000091/ln(3) = 0.000083; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.991681; −Σp ln(p) = 0.052800; H = 0.052800/ln(4) = 0.038087; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.708260; −Σp ln(p) = 0.629795; H = 0.629795/ln(3) = 0.573264; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Kumpulan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut.

Kelompok mana yang menunjukkan setengah.
Pilihan: A. Baris kedua (4 kelinci dan 4 kelinci)
B. Tidak ada baris yang menunjukkan setengah
C. Baris pertama (3 kelinci dan 5 kelinci)
D. Kedua baris menunjukkan setengah
Transkripsi visual: Gambar terdiri dari tiga baris kelinci. Baris pertama berisi 8 kelinci tanpa pembagian kelompok. Baris kedua berisi dua kotak: kotak kiri berisi 3 kelinci, kotak kanan berisi 5 kelinci. Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `764036b9759f6277bc4dca51`

Perhatikan gambar yang diwarnai berikut.<br><br>Gambar mana yang menunjukkan seperempat?

| Opsi | Isi |
|---|---|
| A | Gambar 3 (bentuk anak panah) |
| B | Gambar 1 (segitiga) |
| C | Gambar 4 (kotak berpetak) |
| D | Gambar 2 (segi enam memanjang) |

![Gambar sumber soal 30](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Konsep seperempat (1/4) memerlukan pembagian benda utuh menjadi empat bagian yang sama besar. Hanya Gambar 2 yang memiliki empat bagian dengan luas yang sama besar karena dibagi oleh garis simetri vertikal dan horizontal tepat di tengah.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png. Transkripsi visual: Terdapat empat gambar bangun datar yang masing-masing dibagi menjadi empat bagian. Gambar 1 adalah segitiga yang dibagi menjadi empat bagian tidak sama besar. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis vertikal dan horizontal tepat di tengah, menghasilkan empat bagian yang sama besar. Gambar 3 adalah bentuk anak panah yang dibagi menjadi empat bagian tidak sama besar. Gambar 4 adalah kotak berpetak yang dibagi menjadi empat bagian tidak sama besar (kolom kiri lebih lebar).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e2f7e3951699fbbd8e6d990915fd00eacdaee428f07e5dfbaa15d9cbe45061cd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3580 |
| 2 | success | valid / verified | applying | conceptual | Medium | 4527 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3556 |

Run 1 — solusi: Konsep seperempat (1/4) memerlukan pembagian benda utuh menjadi empat bagian yang sama besar. Gambar 2 adalah satu-satunya bangun yang dibagi oleh garis simetri vertikal dan horizontal tepat di tengah, sehingga keempat bagiannya memiliki luas yang sama.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konseptual tentang pecahan sederhana (seperempat) untuk mengidentifikasi representasi visual yang tepat di antara beberapa pilihan. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Gambar mana yang menunjukkan seperempat?; segi enam memanjang dibagi oleh garis tegak dan garis mendatar yang tepat di tengah sehingga menghasilkan 4 bagian sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa yang dimaksud dengan 'seperempat' (pembagian menjadi empat bagian yang sama besar), bukan sekadar menghafal fakta atau menjalankan algoritme prosedural.. Bukti: seperempat dari benda utuh
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan observasi visual sederhana untuk membandingkan luas bagian-bagian bangun datar. Tidak ada langkah perhitungan atau perencanaan yang kompleks. Siswa cukup mengenali prinsip 'sama besar' sebagai syarat pecahan.. Bukti: Gambar mana yang menunjukkan seperempat?; Gambar 1 (segitiga); Gambar 2 (segi enam memanjang); Gambar 3 (bentuk anak panah)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep 'sama besar'. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pembagian yang sama besar dan tidak sama besar adalah materi standar yang rutin. Tidak ada tuntutan perencanaan atau integrasi yang tinggi. |

Run 2 — solusi: Seperempat (1/4) berarti satu bagian dari empat bagian yang sama besar. Hanya gambar kedua (segi enam) yang memiliki empat bagian dengan luas yang sama.
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep pecahan (seperempat) untuk mengidentifikasi gambar mana yang terbagi menjadi empat bagian sama besar, bukan sekadar terbagi menjadi empat bagian.. Bukti: Gambar mana yang menunjukkan seperempat?; segi enam memanjang dibagi oleh garis tegak dan garis mendatar yang tepat di tengah
- Dimensi pengetahuan `classify/conceptual`: Memahami konsep pecahan sebagai bagian dari keseluruhan yang sama besar.. Bukti: seperempat dari Benda Utuh; Gambar mana yang menunjukkan seperempat?
- Intended difficulty `classify/Medium`: Siswa perlu membedakan antara pembagian menjadi 4 bagian secara umum dengan pembagian menjadi 4 bagian yang sama besar (syarat pecahan). Ini memerlukan ketelitian visual dan pemahaman konsep dasar pecahan.. Bukti: Gambar mana yang menunjukkan seperempat?; bentuk anak panah; segi enam memanjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 2 sudah belajar pecahan sederhana. Soal ini menuntut kemampuan membedakan 'dibagi 4' dengan 'dibagi 4 sama besar', yang merupakan konsep krusial namun sering membingungkan. |

Run 3 — solusi: Seperempat (1/4) berarti satu bagian dari empat bagian yang sama besar. Gambar 2 adalah satu-satunya bangun yang dibagi menjadi empat bagian dengan luas yang sama besar oleh garis simetri vertikal dan horizontal.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep pecahan seperempat sebagai bagian dari keseluruhan yang dibagi menjadi empat bagian sama besar. Ini melibatkan penerapan konsep dasar pecahan pada representasi visual.. Bukti: Gambar mana yang menunjukkan seperempat?; Gambar 2 (segi enam memanjang) \| catatan sumber: Benar: segi enam memanjang dibagi oleh garis tegak dan garis mendatar yang tepat di tengah sehingga menghasilkan 4 bagian sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang dimaksud dengan 'seperempat' (bagian yang sama besar) dalam konteks geometri.. Bukti: Gambar mana yang menunjukkan seperempat?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya sekadar menghitung jumlah bagian (semua opsi dibagi menjadi 4), tetapi harus mengevaluasi apakah bagian-bagian tersebut sama besar. Ini memerlukan diskriminasi visual yang lebih teliti daripada sekadar menghitung.. Bukti: Gambar mana yang menunjukkan seperempat?; Gambar 2 (segi enam memanjang) \| catatan sumber: Benar: segi enam memanjang dibagi oleh garis tegak dan garis mendatar yang tepat di tengah sehingga menghasilkan 4 bagian sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep 'sama besar'. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan antara pembagian yang sama besar dan tidak sama besar adalah tantangan konseptual yang sesuai untuk tingkat kesulitan menengah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5090`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pemahaman konseptual tentang pecahan (seperempat) untuk mengidentifikasi representasi visual yang tepat di antara beberapa pilihan. Ini adalah penerapan konsep pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang apa yang dimaksud dengan 'seperempat' (pembagian menjadi empat bagian yang sama besar), bukan sekadar menghafal fakta atau menjalankan algoritme prosedural.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena siswa tidak hanya sekadar menghitung jumlah bagian (semua opsi dibagi menjadi 4), tetapi harus mengevaluasi apakah bagian-bagian tersebut sama besar. Ini memerlukan diskriminasi visual yang lebih teliti daripada sekadar menghitung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep 'sama besar'. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan antara pembagian yang sama besar dan tidak sama besar adalah tantangan konseptual yang sesuai untuk tingkat kesulitan menengah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 168/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000045; applying=0.999955; reasoning=0.000000 | applying | 0.999955 | 0.000448 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003141; conceptual=0.991190; procedural=0.005669; metacognitive=0.000000 | conceptual | 0.991190 | 0.040539 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.668901; Medium=0.323970; Hard=0.007128 | Easy | 0.668901 | 0.609283 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999955; −Σp ln(p) = 0.000492; H = 0.000492/ln(3) = 0.000448; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.991190; −Σp ln(p) = 0.056199; H = 0.056199/ln(4) = 0.040539; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.668901; −Σp ln(p) = 0.669366; H = 0.669366/ln(3) = 0.609283; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Seperempat dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar yang diwarnai berikut.

Gambar mana yang menunjukkan seperempat?
Pilihan: A. Gambar 3 (bentuk anak panah)
B. Gambar 1 (segitiga)
C. Gambar 4 (kotak berpetak)
D. Gambar 2 (segi enam memanjang)
Transkripsi visual: Terdapat empat gambar bangun datar yang masing-masing dibagi menjadi empat bagian. Gambar 1 adalah segitiga yang dibagi menjadi empat bagian tidak sama besar. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis vertikal dan horizontal tepat di tengah, menghasilkan empat bagian yang sama besar. Gambar 3 adalah bentuk anak panah yang dibagi menjadi empat bagian tidak sama besar. Gambar 4 adalah kotak berpetak yang dibagi menjadi empat bagian tidak sama besar (kolom kiri lebih lebar).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `bdbd4e9367baef3f90950f22`

Perhatikan bagian yang diwarnai pada gambar berikut.<br><br>Manakah yang menunjukkan seperempat?

| Opsi | Isi |
|---|---|
| A | D |
| B | E |
| C | A |
| D | C |

![Gambar sumber soal 31](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0160-01.png>)


Kunci sumber: `A`; status AI: `conflict`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Seperempat (1/4) didefinisikan sebagai satu bagian dari empat bagian yang sama besar. Gambar D menunjukkan sebuah persegi yang dibagi menjadi empat bagian yang kongruen (sama besar) dengan tepat satu bagian diarsir. Oleh karena itu, D adalah representasi visual yang benar untuk seperempat.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0160-01.png. Transkripsi visual: Terdapat 8 gambar bangun datar yang diberi label A sampai H. Gambar A: segitiga utuh. Gambar B: jajar genjang dibagi 4 bagian sama besar, 1 bagian diarsir. Gambar C: persegi panjang dibagi 4 bagian sama besar, 2 bagian diarsir (setengah). Gambar D: persegi dibagi 4 bagian sama besar, 1 bagian diarsir. Gambar E: bintang dengan satu ujung kecil diarsir. Gambar F: pentagon dibagi 2 bagian sama besar, 1 bagian diarsir. Gambar G: lingkaran dibagi 4 bagian sama besar, 2 bagian diarsir. Gambar H: persegi dibagi 4 bagian sama besar, 1 bagian diarsir (namun bentuknya persegi panjang vertikal).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `68a6db24c7cad608360009d86197efd8c27e938ed9bdf06c7f893a09a4f6db16`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | knowing | conceptual | Easy | 3556 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 5027 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 4973 |

Run 1 — solusi: Seperempat berarti satu bagian dari empat bagian yang sama besar. Gambar D menunjukkan sebuah bangun yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir, sehingga D adalah jawaban yang benar.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali representasi visual dari pecahan sederhana (seperempat). Ini adalah tugas pengenalan konsep dasar yang sudah dipelajari di kelas 2.. Bukti: Manakah yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sebagai bagian dari keseluruhan yang dibagi sama besar.. Bukti: Manakah yang menunjukkan seperempat?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya meminta identifikasi visual langsung dari konsep pecahan yang sudah umum. Tidak ada langkah kompleks atau perencanaan yang diperlukan.. Bukti: Manakah yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian benda menjadi bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu mengenali pecahan sederhana melalui representasi visual. |

Run 2 — solusi: Gambar D menunjukkan sebuah persegi yang dibagi menjadi 4 bagian sama besar dengan 1 bagian diarsir, yang merepresentasikan seperempat (1/4).
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali representasi visual pecahan seperempat yang sudah dipelajari.. Bukti: Manakah yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Memahami konsep pecahan sebagai bagian dari keseluruhan yang dibagi sama besar.. Bukti: Manakah yang menunjukkan seperempat?
- Intended difficulty `classify/Easy`: Tugas pengenalan visual langsung untuk konsep dasar pecahan.. Bukti: Manakah yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu mengenali representasi visual pecahan sederhana. |

Run 3 — solusi: Gambar D menunjukkan sebuah bangun datar (persegi) yang dibagi menjadi 4 bagian sama besar dengan 1 bagian diarsir, yang merepresentasikan seperempat (1/4).
- Domain kognitif `classify/knowing`: Siswa diminta mengenali representasi visual dari pecahan seperempat.. Bukti: Manakah yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Memahami konsep bagian dari keseluruhan (pecahan) secara visual.. Bukti: Manakah yang menunjukkan seperempat?
- Intended difficulty `classify/Easy`: Tugas ini adalah pengenalan konsep dasar pecahan melalui representasi visual yang umum di kelas 2.. Bukti: Manakah yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian benda menjadi bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenali pecahan dari gambar adalah materi standar kelas 2. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4614`.
Konten: `valid`; kunci: `conflict`; masalah: Kunci jawaban pada sumber (A) salah. Gambar A adalah segitiga utuh yang tidak dibagi. Gambar D adalah persegi yang dibagi menjadi 4 bagian sama besar dengan 1 bagian diarsir, yang secara tepat merepresentasikan seperempat (1/4)..
- Domain kognitif `knowing`: Siswa diminta untuk mengenali representasi visual dari konsep pecahan sederhana (seperempat). Ini adalah tugas pengenalan konsep dasar yang sudah dipelajari di kelas 2.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sebagai bagian dari keseluruhan yang dibagi menjadi bagian-bagian yang sama besar.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya meminta identifikasi visual langsung dari konsep pecahan yang sudah umum. Tidak ada langkah kompleks atau perencanaan yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian benda menjadi bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu mengenali pecahan sederhana melalui representasi visual. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 194/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Seperempat dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bagian yang diwarnai pada gambar berikut.

Manakah yang menunjukkan seperempat?
Pilihan: A. D
B. E
C. A
D. C
Transkripsi visual: Terdapat 8 gambar bangun datar yang diberi label A sampai H. Gambar A: segitiga utuh. Gambar B: jajar genjang dibagi 4 bagian sama besar, 1 bagian diarsir. Gambar C: persegi panjang dibagi 4 bagian sama besar, 2 bagian diarsir (setengah). Gambar D: persegi dibagi 4 bagian sama besar, 1 bagian diarsir. Gambar E: bintang dengan satu ujung kecil diarsir. Gambar F: pentagon dibagi 2 bagian sama besar, 1 bagian diarsir. Gambar G: lingkaran dibagi 4 bagian sama besar, 2 bagian diarsir. Gambar H: persegi dibagi 4 bagian sama besar, 1 bagian diarsir (namun bentuknya persegi panjang vertikal).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `valid`. Catatan konten: Kunci jawaban pada sumber (A) salah. Gambar A adalah segitiga utuh yang tidak dibagi. Gambar D adalah persegi yang dibagi menjadi 4 bagian sama besar dengan 1 bagian diarsir, yang secara tepat merepresentasikan seperempat (1/4)..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `1622e07bf377db746a052549`

Amati setiap gambar berikut.<br><br>Berat 1 pepaya adalah .... manggis.

| Opsi | Isi |
|---|---|
| A | 3 manggis |
| B | 2 manggis |
| C | 8 manggis |
| D | 4 manggis |

![Gambar sumber soal 32](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0188-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Dari gambar, 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 2 mangga = 2 x 2 manggis = 4 manggis. Jadi, 1 pepaya = 4 manggis.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0188-04.png. Transkripsi visual: Terdapat dua timbangan. Timbangan pertama menunjukkan 2 mangga setara dengan 1 pepaya. Timbangan kedua menunjukkan 1 mangga setara dengan 2 manggis. Pertanyaan meminta untuk menentukan berat 1 pepaya dalam satuan manggis.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `210205c6c138d7ffe755dc8796200c623f189e978a0e09f1614d93dc36f9d95f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3514 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3507 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3475 |

Run 1 — solusi: Dari gambar, 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 2 mangga = 2 x 2 manggis = 4 manggis. Jadi, 1 pepaya = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu menghubungkan dua informasi (dua timbangan) untuk menyelesaikan masalah. Ini melibatkan penerapan konsep kesetaraan berat dalam konteks rutin, yang dikategorikan sebagai applying.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis; Berat 1 pepaya adalah .... manggis
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan kesetaraan (konsep) dan penggunaan prosedur substitusi sederhana untuk menemukan nilai yang tidak diketahui.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah penyelesaian (substitusi nilai) yang saling bergantung. Siswa harus memahami hubungan antara pepaya-mangga dan mangga-manggis untuk mendapatkan jawaban akhir. Ini adalah tuntutan yang sesuai untuk kelas 2 namun memerlukan perencanaan langkah yang lebih dari sekadar satu operasi langsung.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kesetaraan berat dan perkalian sederhana (2x2). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah belajar tentang kesetaraan dan perkalian dasar. Soal ini menuntut integrasi dua informasi visual, yang merupakan tantangan sedang bagi tingkat kelas tersebut. |

Run 2 — solusi: Dari gambar, 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 2 mangga = 2 x 2 manggis = 4 manggis. Jadi, 1 pepaya = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu menghubungkan dua informasi terpisah (dua timbangan) untuk menyimpulkan nilai pepaya dalam satuan manggis. Ini melibatkan penerapan konsep kesetaraan dalam konteks rutin.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis; Berat 1 pepaya adalah .... manggis
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip kesetaraan (transitivitas sederhana) untuk menyelesaikan masalah pengukuran.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah logis: mengidentifikasi hubungan 1 pepaya dengan mangga, lalu mengganti mangga dengan manggis. Ini adalah tugas rutin bagi kelas 2 yang sudah belajar perkalian dasar atau penjumlahan berulang.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis; Berat 1 pepaya adalah .... manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kesetaraan timbangan dan konsep perkalian/penjumlahan berulang sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu melakukan substitusi sederhana dalam konteks visual. Memerlukan dua langkah (mengganti 2 mangga dengan 2x2 manggis) yang saling terkait. |

Run 3 — solusi: Dari gambar, 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 2 mangga = 2 x 2 manggis = 4 manggis. Jadi, 1 pepaya = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu menghubungkan dua informasi (dua timbangan) untuk menyelesaikan masalah. Ini melibatkan penerapan konsep kesetaraan dalam konteks rutin, yang masuk dalam kategori applying.. Bukti: 2 mangga = 1 pepaya; 1 mangga = 2 manggis; Berat 1 pepaya adalah .... manggis
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip kesetaraan dan substitusi sederhana antar objek, yang merupakan pengetahuan konseptual.. Bukti: 2 mangga = 1 pepaya; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah: mengidentifikasi hubungan 1 pepaya dengan mangga, lalu mengonversi mangga ke manggis. Bagi kelas 2, ini adalah tugas Medium karena memerlukan integrasi dua informasi yang saling terkait (transitif) meskipun prosedurnya sederhana.. Bukti: 2 mangga = 1 pepaya; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kesetaraan berat dan perkalian sederhana (2x2). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah belajar tentang perbandingan berat sederhana. Soal ini menuntut integrasi dua langkah kesetaraan yang merupakan tantangan sedang untuk tingkat kelas tersebut. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 98/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000012; applying=0.999988; reasoning=0.000000 | applying | 0.999988 | 0.000137 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.019042; conceptual=0.965753; procedural=0.015205; metacognitive=0.000000 | conceptual | 0.965753 | 0.124601 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.828640; Medium=0.167167; Hard=0.004193 | Easy | 0.828640 | 0.434852 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999988; −Σp ln(p) = 0.000151; H = 0.000151/ln(3) = 0.000137; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.965753; −Σp ln(p) = 0.172733; H = 0.172733/ln(4) = 0.124601; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.828640; −Σp ln(p) = 0.477733; H = 0.477733/ln(3) = 0.434852; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati setiap gambar berikut.

Berat 1 pepaya adalah .... manggis.
Pilihan: A. 3 manggis
B. 2 manggis
C. 8 manggis
D. 4 manggis
Transkripsi visual: Terdapat dua timbangan. Timbangan pertama menunjukkan 2 mangga setara dengan 1 pepaya. Timbangan kedua menunjukkan 1 mangga setara dengan 2 manggis. Pertanyaan meminta untuk menentukan berat 1 pepaya dalam satuan manggis.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `4cba291cad9e7ab23945d506`

Perhatikan gambar di bawah ini.<br><br>Berat 1 buah jeruk sama dengan .... stroberi.

| Opsi | Isi |
|---|---|
| A | 4 stroberi |
| B | 2 stroberi |
| C | 1 stroberi |
| D | 3 stroberi |

![Gambar sumber soal 33](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0200-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Berdasarkan gambar pertama, 1 buah jeruk seimbang dengan 2 buah stroberi. Jadi, berat 1 buah jeruk sama dengan 2 stroberi.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0200-01.png. Transkripsi visual: Terdapat dua gambar timbangan yang seimbang. Gambar pertama (kiri) menunjukkan 1 buah jeruk di piring kiri dan 2 buah stroberi di piring kanan. Gambar kedua (kanan) menunjukkan 2 buah jeruk di piring kiri dan 4 buah stroberi di piring kanan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d0afee982c64386feaf868f72b13159ec0811686efb147c34788d276287f9a8b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3384 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3361 |
| 3 | success | valid / verified | knowing | factual | Easy | 3377 |

Run 1 — solusi: Berdasarkan gambar pertama, 1 buah jeruk berada pada satu sisi timbangan yang seimbang dengan 2 buah stroberi di sisi lainnya. Jadi, berat 1 buah jeruk sama dengan 2 stroberi.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca informasi dari representasi visual (timbangan) dan melakukan pencocokan langsung antara objek di satu sisi dengan objek di sisi lainnya. Ini adalah tugas membaca data visual sederhana.. Bukti: Perhatikan gambar di bawah ini.; Berat 1 buah jeruk sama dengan .... stroberi.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang konsep kesetaraan berat melalui representasi visual timbangan sederhana.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu mengamati gambar pertama yang secara eksplisit menunjukkan kesetaraan 1 jeruk dengan 2 stroberi. Tidak ada langkah tambahan atau manipulasi yang diperlukan.. Bukti: Perhatikan gambar di bawah ini.; Berat 1 buah jeruk sama dengan .... stroberi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca gambar timbangan sederhana dan menghitung jumlah objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, membaca timbangan sederhana adalah materi dasar yang familiar. Soal ini tidak menuntut perencanaan atau integrasi langkah, sehingga dikategorikan Easy. |

Run 2 — solusi: Berdasarkan gambar kiri, 1 jeruk seimbang dengan 2 stroberi. Maka, berat 1 jeruk sama dengan 2 stroberi.
- Domain kognitif `classify/knowing`: Siswa diminta membaca informasi dari representasi visual (timbangan) untuk menentukan kesetaraan berat. Ini adalah prosedur langsung membaca data dari gambar yang diberikan.. Bukti: Perhatikan gambar di bawah ini.; Berat 1 buah jeruk sama dengan .... stroberi.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep dasar pengukuran berat melalui perbandingan visual (kesetaraan).. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu mengamati gambar kiri secara langsung tanpa perlu melakukan perhitungan atau manipulasi data. Informasi yang dibutuhkan tersedia secara eksplisit.. Bukti: Perhatikan gambar di bawah ini.; Berat 1 buah jeruk sama dengan .... stroberi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep dasar timbangan/kesetaraan berat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan konsep perbandingan sederhana melalui gambar. Soal tidak menuntut operasi hitung atau penalaran kompleks. |

Run 3 — solusi: Berdasarkan gambar pertama, 1 jeruk seimbang dengan 2 stroberi. Maka, berat 1 jeruk sama dengan 2 stroberi.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca informasi visual secara langsung dari gambar pertama yang menunjukkan kesetaraan berat antara 1 jeruk dan 2 stroberi. Tidak ada prosedur kompleks atau penalaran yang diperlukan.. Bukti: Perhatikan gambar di bawah ini.; Berat 1 buah jeruk sama dengan .... stroberi.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang konsep dasar pengukuran berat menggunakan timbangan sederhana (kesetaraan berat).. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu mengamati gambar pertama secara langsung untuk mendapatkan jawaban. Tidak ada langkah tambahan atau manipulasi yang diperlukan.. Bukti: Perhatikan gambar di bawah ini.; Berat 1 buah jeruk sama dengan .... stroberi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca representasi visual timbangan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 2, membaca timbangan sederhana adalah materi dasar yang familiar. Soal ini tidak menuntut perencanaan atau integrasi, hanya observasi langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4679`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu membaca informasi visual secara langsung dari gambar pertama yang menunjukkan kesetaraan berat antara 1 jeruk dan 2 stroberi. Tidak ada prosedur kompleks atau penalaran yang diperlukan.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman faktual tentang konsep kesetaraan berat melalui representasi visual timbangan sederhana.
- Intended difficulty `Easy`: Soal ini sangat mudah karena siswa hanya perlu mengamati gambar pertama yang secara eksplisit menunjukkan kesetaraan 1 jeruk dengan 2 stroberi. Tidak ada langkah tambahan atau manipulasi yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca gambar timbangan sederhana dan menghitung jumlah objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, membaca timbangan sederhana adalah materi dasar yang familiar. Soal ini tidak menuntut perencanaan atau integrasi langkah, sehingga dikategorikan Easy. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 113/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001883; applying=0.998117; reasoning=0.000000 | applying | 0.998117 | 0.012467 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.043232; conceptual=0.951362; procedural=0.005406; metacognitive=0.000000 | conceptual | 0.951362 | 0.152534 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.826967; Medium=0.168293; Hard=0.004741 | Easy | 0.826967 | 0.439093 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998117; −Σp ln(p) = 0.013697; H = 0.013697/ln(3) = 0.012467; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.951362; −Σp ln(p) = 0.211457; H = 0.211457/ln(4) = 0.152534; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.826967; −Σp ln(p) = 0.482393; H = 0.482393/ln(3) = 0.439093; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar di bawah ini.

Berat 1 buah jeruk sama dengan .... stroberi.
Pilihan: A. 4 stroberi
B. 2 stroberi
C. 1 stroberi
D. 3 stroberi
Transkripsi visual: Terdapat dua gambar timbangan yang seimbang. Gambar pertama (kiri) menunjukkan 1 buah jeruk di piring kiri dan 2 buah stroberi di piring kanan. Gambar kedua (kanan) menunjukkan 2 buah jeruk di piring kiri dan 4 buah stroberi di piring kanan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `dd3cb9360df4fe034e2f2480`

Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

| Opsi | Isi |
|---|---|
| A | menyikat gigi, bangun tidur, makan siang, bermain bola |
| B | bangun tidur, menyikat gigi, makan siang, bermain bola |
| C | bermain bola, makan siang, menyikat gigi, bangun tidur |
| D | bangun tidur, makan siang, menyikat gigi, bermain bola |

![Gambar sumber soal 34](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Mengurutkan waktu pada jam: 06.00 (bangun tidur) -> 08.00 (menyikat gigi) -> 12.00 (makan siang) -> 16.00 (bermain bola). Urutan yang benar adalah C, D, B, A.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png. Transkripsi visual: Terdapat empat gambar kegiatan dengan jam analog: Gambar C (bangun tidur, jam 6:00), Gambar D (menyikat gigi, jam 8:00), Gambar B (makan siang, jam 12:00), dan Gambar A (bermain bola, jam 4:00). Urutan waktu yang logis dari pagi ke sore/malam adalah 6:00, 8:00, 12:00, lalu 4:00.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e82a95d774f7b5989c9b2a5d95a893966d49ac498ca6b853dd4adb080cf052d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3511 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3639 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3490 |

Run 1 — solusi: Mengurutkan waktu pada jam: 06.00 (bangun tidur) -> 08.00 (menyikat gigi) -> 12.00 (makan siang) -> 16.00 (bermain bola). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi waktu pada jam analog dan mengurutkan kegiatan berdasarkan kronologi waktu yang familiar. Ini adalah penerapan prosedur membaca jam dan pemahaman urutan waktu dalam konteks rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam sehari dan kemampuan membaca jam analog sebagai alat bantu.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena siswa hanya perlu membaca waktu pada jam analog yang menunjukkan angka bulat dan mengurutkannya berdasarkan rutinitas harian yang sangat umum.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog (angka bulat) dan memahami urutan waktu harian (pagi, siang, sore). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah mempelajari pembacaan jam analog sederhana dan urutan kegiatan sehari-hari. Tugas mengurutkan empat gambar berdasarkan waktu adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Mengurutkan kegiatan berdasarkan waktu yang ditunjukkan jam: bangun tidur (06.00) -> menyikat gigi (08.00) -> makan siang (12.00) -> bermain bola (16.00). Urutan ini sesuai dengan pilihan B.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi waktu pada jam analog dan mengurutkan kegiatan berdasarkan urutan kronologis harian yang umum. Ini adalah penerapan prosedur membaca jam dan pemahaman urutan waktu yang rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).; jam analog: Gambar C (anak bangun tidur, jam 6:00), Gambar D (anak menyikat gigi, jam 8:00), Gambar B (anak makan siang, jam 12:00), dan Gambar A (anak bermain bola, jam 4:00)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam sehari dan kemampuan membaca jam analog sebagai alat bantu.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 2. Siswa hanya perlu membaca waktu pada empat jam analog yang sederhana dan mengurutkannya. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).; jam analog: Gambar C (anak bangun tidur, jam 6:00), Gambar D (anak menyikat gigi, jam 8:00), Gambar B (anak makan siang, jam 12:00), dan Gambar A (anak bermain bola, jam 4:00)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog (jam tepat) dan pemahaman urutan kegiatan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca jam dan mengurutkan kegiatan adalah materi standar kelas 2. Tugas ini langsung dan tidak memerlukan perencanaan kompleks. |

Run 3 — solusi: Mengurutkan kegiatan berdasarkan waktu pada jam: bangun tidur (06.00) -> menyikat gigi (08.00) -> makan siang (12.00) -> bermain bola (16.00). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan kejadian berdasarkan waktu yang ditunjukkan pada jam analog. Ini adalah penerapan prosedur membaca jam dan memahami urutan waktu dalam konteks rutin sehari-hari.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu (pagi ke malam) dan kemampuan membaca jam analog sebagai representasi waktu.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 2. Siswa hanya perlu membaca waktu pada empat jam analog dan mengurutkannya secara kronologis. Tidak ada kendala yang berinteraksi atau perencanaan kompleks yang diperlukan.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog (pukul tepat) dan memahami urutan waktu sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan kegiatan berdasarkan waktu adalah materi standar kelas 2. Tugas ini langsung dan tidak memerlukan penalaran tingkat tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 188/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000325; applying=0.999675; reasoning=0.000000 | applying | 0.999675 | 0.002672 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.024618; conceptual=0.972893; procedural=0.002488; metacognitive=0.000000 | conceptual | 0.972893 | 0.095831 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.647396; Medium=0.344327; Hard=0.008277 | Easy | 0.647396 | 0.626496 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999675; −Σp ln(p) = 0.002936; H = 0.002936/ln(3) = 0.002672; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.972893; −Σp ln(p) = 0.132849; H = 0.132849/ln(4) = 0.095831; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.647396; −Σp ln(p) = 0.688276; H = 0.688276/ln(3) = 0.626496; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Waktu
Tipe soal: multiple_choice
Stimulus: -
Soal: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
Pilihan: A. menyikat gigi, bangun tidur, makan siang, bermain bola
B. bangun tidur, menyikat gigi, makan siang, bermain bola
C. bermain bola, makan siang, menyikat gigi, bangun tidur
D. bangun tidur, makan siang, menyikat gigi, bermain bola
Transkripsi visual: Terdapat empat gambar kegiatan dengan jam analog: Gambar C (bangun tidur, jam 6:00), Gambar D (menyikat gigi, jam 8:00), Gambar B (makan siang, jam 12:00), dan Gambar A (bermain bola, jam 4:00). Urutan waktu yang logis dari pagi ke sore/malam adalah 6:00, 8:00, 12:00, lalu 4:00.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `c0080230ef4ab5e5b0a07c55`

Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

| Opsi | Isi |
|---|---|
| A | Bermain bola |
| B | Mencuci tangan |
| C | Sarapan |
| D | Menyisir rambut |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Membandingkan durasi dua kegiatan: mencuci tangan (beberapa detik/menit) dan bermain bola (biasanya lebih lama). Bermain bola lebih lama.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e1c401e36c872a0bb939bb04093c62bd16aded2c86cf2104f7f7612ff7a92293`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2176 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2181 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2181 |

Run 1 — solusi: Membandingkan durasi dua kegiatan: mencuci tangan (beberapa detik/menit) dan bermain bola (biasanya lebih lama). Bermain bola lebih lama.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan durasi dua kegiatan sehari-hari yang familiar. Ini adalah penerapan konsep durasi waktu pada konteks rutin.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang durasi waktu (lebih lama/lebih singkat) dalam konteks kegiatan sehari-hari.. Bukti: Kegiatan manakah yang lebih lama
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana bagi siswa kelas 2. Perbandingan durasi antara kegiatan yang sangat singkat (mencuci tangan) dan kegiatan yang relatif lama (bermain bola) adalah pengetahuan umum yang rutin dan langsung.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep waktu dan durasi kegiatan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Membandingkan durasi kegiatan adalah materi dasar kelas 2. Tidak ada langkah kompleks atau kendala yang harus dipecahkan. |

Run 2 — solusi: Bermain bola membutuhkan waktu yang lebih lama (bisa hitungan menit atau jam) dibandingkan mencuci tangan yang hanya membutuhkan waktu beberapa detik.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan durasi dua kegiatan sehari-hari yang sudah familiar. Ini adalah penerapan konsep durasi waktu pada konteks rutin.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang durasi waktu (lama vs sebentar) dalam konteks aktivitas sehari-hari.. Bukti: Kegiatan manakah yang lebih lama
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana bagi siswa kelas 2. Perbandingan durasi antara dua aktivitas yang sangat kontras (detik vs menit/jam) adalah pengetahuan umum yang sudah dipelajari di tingkat dasar. Tidak ada langkah rumit atau kendala yang saling berinteraksi.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep waktu (lama dan sebentar) dalam kehidupan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Membandingkan durasi dua kegiatan yang sangat berbeda durasinya adalah materi yang sangat mendasar dan familiar bagi siswa kelas 2. |

Run 3 — solusi: Membandingkan durasi dua kegiatan: mencuci tangan (sebentar) dan bermain bola (lama). Bermain bola membutuhkan waktu lebih lama.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan durasi dua kegiatan yang sudah dikenal dalam kehidupan sehari-hari. Ini adalah penerapan konsep durasi waktu yang sederhana.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang durasi waktu (lama vs sebentar) melalui perbandingan dua aktivitas rutin.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana bagi siswa kelas 2 karena membandingkan dua aktivitas dengan perbedaan durasi yang sangat kontras dan familiar.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep waktu (lama dan sebentar) dalam kehidupan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan durasi aktivitas sehari-hari. Membandingkan 'mencuci tangan' dan 'bermain bola' adalah tugas kognitif yang sangat mendasar dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.130316; applying=0.869684; reasoning=0.000000 | applying | 0.869684 | 0.352251 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.869526; conceptual=0.117139; procedural=0.013336; metacognitive=0.000000 | factual | 0.869526 | 0.310419 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.871058; Medium=0.126094; Hard=0.002848 | Easy | 0.871058 | 0.362318 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.869684; −Σp ln(p) = 0.386988; H = 0.386988/ln(3) = 0.352251; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.869526; −Σp ln(p) = 0.430332; H = 0.430332/ln(4) = 0.310419; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.871058; −Σp ln(p) = 0.398047; H = 0.398047/ln(3) = 0.362318; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Waktu
Tipe soal: multiple_choice
Stimulus: -
Soal: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
Pilihan: A. Bermain bola
B. Mencuci tangan
C. Sarapan
D. Menyisir rambut
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `5202d6bd8064acc3f5637504`

Hitunglah banyak benda berikut. Contoh: 5 puluhan = 50 Jadi, ada 50 buah rambutan. Lakukan seperti contoh.<br><br> .... puluhan = .... Jadi, ada .... buah jeruk.

| Opsi | Isi |
|---|---|
| A | 7 puluhan = 70 (70 buah jeruk) |
| B | 6 puluhan = 60 (60 buah jeruk) |
| C | 6 satuan = 6 (6 buah jeruk) |
| D | 5 puluhan = 50 (50 buah jeruk) |

![Gambar sumber soal 36](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0215-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Terdapat 6 keranjang jeruk. Setiap keranjang mewakili 1 puluhan. Jadi, 6 puluhan = 60. Total ada 60 buah jeruk.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0215-04.png. Transkripsi visual: The image displays 6 baskets, each containing a group of oranges. The text below the image asks the student to complete the sentence: '____ puluhan = ____. Jadi, ada ____ buah jeruk.' based on the provided example.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `110c7d275e455d182b8ad2065a0c3ae5756cbd7677f46116720599a519753820`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3497 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3454 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3467 |

Run 1 — solusi: Terdapat 6 keranjang, masing-masing mewakili 1 puluhan. Jadi, 6 puluhan = 60. Total ada 60 buah jeruk.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penghitungan kelompok puluhan yang sudah dicontohkan dalam soal ke dalam konteks visual yang baru. Ini adalah penerapan langsung dari konsep nilai tempat (puluhan) yang sudah dipelajari.. Bukti: Lakukan seperti contoh.; 6 puluhan = 60 (60 buah jeruk)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana mengelompokkan benda ke dalam satuan puluhan dan mengonversinya menjadi angka.. Bukti: 5 puluhan = 50; 6 puluhan = 60
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu menghitung jumlah keranjang (objek) dan mengalikan dengan nilai puluhan sesuai contoh yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Hitunglah banyak benda berikut.; Lakukan seperti contoh.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep puluhan dan kemampuan membilang benda. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, menghitung kelompok puluhan adalah materi dasar yang rutin. Soal memberikan contoh eksplisit yang memandu siswa langkah demi langkah, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Menghitung jumlah keranjang yang ada, yaitu 6 keranjang. Karena setiap keranjang mewakili 1 puluhan, maka 6 keranjang = 6 puluhan = 60 buah jeruk.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menghitung jumlah kelompok benda (keranjang) dan mengonversinya ke nilai puluhan sesuai dengan contoh yang diberikan. Ini adalah prosedur langsung yang sudah dipelajari.. Bukti: Hitunglah banyak benda berikut.; 6 puluhan = 60
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat puluhan dan representasi visual kelompok benda (keranjang sebagai satuan puluhan).. Bukti: 5 puluhan = 50; 6 puluhan = 60
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu menghitung jumlah objek yang terlihat dan mengikuti pola contoh yang sudah diberikan secara eksplisit.. Bukti: Hitunglah banyak benda berikut.; Lakukan seperti contoh.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda sampai 100 dan memahami konsep puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan konsep puluhan dan membilang benda. Soal memberikan contoh yang jelas dan langkah penyelesaiannya bersifat rutin. |

Run 3 — solusi: Terdapat 6 keranjang, di mana setiap keranjang mewakili 1 puluhan. Jadi, 6 puluhan = 60. Total ada 60 buah jeruk.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur yang sudah dicontohkan (menghitung kelompok puluhan) pada objek yang diberikan. Ini adalah penerapan langsung dari konsep nilai tempat puluhan yang sudah dipelajari.. Bukti: Lakukan seperti contoh.; 6 puluhan = 60
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat (puluhan) dan bagaimana merepresentasikannya dalam bentuk angka.. Bukti: 5 puluhan = 50; 6 puluhan = 60
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu menghitung jumlah keranjang (objek) dan mengalikannya dengan 10 sesuai contoh yang diberikan. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: Lakukan seperti contoh.; 6 puluhan = 60

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda dan memahami konsep puluhan (kelompok sepuluh). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan konsep puluhan dan satuan. Soal ini adalah latihan rutin yang mengikuti pola contoh yang diberikan secara eksplisit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4892`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur penghitungan kelompok puluhan yang sudah dicontohkan dalam soal ke dalam konteks visual yang baru. Ini adalah penerapan langsung dari konsep nilai tempat (puluhan) yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana mengelompokkan benda ke dalam satuan puluhan dan mengonversinya menjadi angka.
- Intended difficulty `Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu menghitung jumlah keranjang (objek) dan mengalikan dengan nilai puluhan sesuai contoh yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep puluhan dan kemampuan membilang benda. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, menghitung kelompok puluhan adalah materi dasar yang rutin. Soal memberikan contoh eksplisit yang memandu siswa langkah demi langkah, sehingga tingkat kesulitannya rendah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 196/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000019; applying=0.999981; reasoning=0.000000 | applying | 0.999981 | 0.000207 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003461; conceptual=0.990157; procedural=0.006382; metacognitive=0.000000 | conceptual | 0.990157 | 0.044479 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.696550; Medium=0.294227; Hard=0.009223 | Easy | 0.696550 | 0.596261 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999981; −Σp ln(p) = 0.000227; H = 0.000227/ln(3) = 0.000207; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.990157; −Σp ln(p) = 0.061662; H = 0.061662/ln(4) = 0.044479; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.696550; −Σp ln(p) = 0.655060; H = 0.655060/ln(3) = 0.596261; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Menghitung, Membaca, dan Menulis Bilangan sampai dengan 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah banyak benda berikut. Contoh: 5 puluhan = 50 Jadi, ada 50 buah rambutan. Lakukan seperti contoh.

 .... puluhan = .... Jadi, ada .... buah jeruk.
Pilihan: A. 7 puluhan = 70 (70 buah jeruk)
B. 6 puluhan = 60 (60 buah jeruk)
C. 6 satuan = 6 (6 buah jeruk)
D. 5 puluhan = 50 (50 buah jeruk)
Transkripsi visual: The image displays 6 baskets, each containing a group of oranges. The text below the image asks the student to complete the sentence: '____ puluhan = ____. Jadi, ada ____ buah jeruk.' based on the provided example.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `98cb95b9467c6a458263f9f1`

Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan .....

| Opsi | Isi |
|---|---|
| A | 780 |
| B | 87 |
| C | 70 |
| D | 78 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Nama bilangan 'tujuh puluh delapan' terdiri dari 7 puluhan dan 8 satuan, sehingga lambang bilangannya adalah 78.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `645022234a233af7463cfa00e81a7d60150e6dab5322af9a77045c6c00dd4ffd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2098 |
| 2 | success | valid / verified | knowing | factual | Easy | 2199 |
| 3 | success | valid / verified | knowing | factual | Easy | 2583 |

Run 1 — solusi: Nama bilangan 'tujuh puluh delapan' terdiri dari 7 puluhan dan 8 satuan, sehingga lambang bilangannya adalah 78.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan representasi verbal (nama bilangan) ke dalam representasi simbolik (lambang bilangan). Ini adalah tugas pengenalan langsung terhadap sistem nilai tempat dasar yang sudah dipelajari di kelas 2.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap simbol dan istilah dasar dalam sistem bilangan sampai 100.. Bukti: Tujuh puluh delapan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 2. Tidak ada langkah tambahan atau kendala yang perlu dipecahkan selain memahami nama bilangan tersebut.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan serta penulisan lambang bilangan 1-100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menulis lambang bilangan dari nama bilangan adalah materi dasar kelas 2 yang sangat rutin dan tidak memerlukan perencanaan kompleks. |

Run 2 — solusi: Tujuh puluh delapan berarti 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nama bilangan dan mengubahnya menjadi lambang bilangan (simbol numerik) yang sesuai. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol numerik (lambang bilangan) yang merepresentasikan nama bilangan tertentu.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2. Tidak ada langkah kompleks atau perencanaan yang diperlukan.. Bukti: Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan serta penulisan lambang bilangan 1-100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menuliskan lambang bilangan dari nama bilangan adalah keterampilan dasar yang diharapkan sudah dikuasai siswa kelas 2. |

Run 3 — solusi: Tujuh puluh delapan terdiri dari 7 puluhan dan 8 satuan, sehingga lambang bilangannya adalah 78.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menuliskan lambang bilangan dari nama bilangan yang diberikan. Ini adalah tugas dasar yang bersifat langsung (knowing) tanpa memerlukan strategi kompleks.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Pengetahuan yang diuji adalah pemahaman tentang simbol angka dan sistem penamaan bilangan, yang termasuk dalam kategori pengetahuan faktual.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan merupakan materi dasar kelas 2. Siswa hanya perlu menerjemahkan nama bilangan ke dalam bentuk angka.. Bukti: Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep nilai tempat puluhan dan satuan serta lambang bilangan sampai 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas ini adalah standar kompetensi kelas 2 untuk membaca dan menulis bilangan. Tidak ada langkah perencanaan atau integrasi yang diperlukan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 73/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999922; applying=0.000078; reasoning=0.000000 | knowing | 0.999922 | 0.000741 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.737571; conceptual=0.245177; procedural=0.017252; metacognitive=0.000000 | factual | 0.737571 | 0.461096 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.898726; Medium=0.099252; Hard=0.002022 | Easy | 0.898726 | 0.307470 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999922; −Σp ln(p) = 0.000814; H = 0.000814/ln(3) = 0.000741; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.737571; −Σp ln(p) = 0.639215; H = 0.639215/ln(4) = 0.461096; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.898726; −Σp ln(p) = 0.337790; H = 0.337790/ln(3) = 0.307470; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Menghitung, Membaca, dan Menulis Bilangan sampai dengan 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan .....
Pilihan: A. 780
B. 87
C. 70
D. 78
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `f366f15007b61b27653bdf58`

Kira menuliskan satu bilangan.<br><br>Kira berkata, 'Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.' Berapa bilangan yang ditulis Kira?

| Opsi | Isi |
|---|---|
| A | 92 |
| B | 29 |
| C | 12 |
| D | 81 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bilangan awal = 55 - 40 - 3 = 15 - 3 = 12. Atau, 55 memiliki 5 puluhan dan 5 satuan. Kurangi 4 dari puluhan (5-4=1) dan 3 dari satuan (5-3=2), sehingga bilangan tersebut adalah 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c6eafe92d12dac05284b3af09012156dcdee2a74ed4fdf1d285c25b378d002fc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2368 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2329 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2362 |

Run 1 — solusi: Bilangan awal = 55 - 40 - 3 = 15 - 3 = 12. Atau, 55 memiliki 5 puluhan dan 5 satuan. Kurangi 4 dari puluhan (5-4=1) dan 3 dari satuan (5-3=2), sehingga bilangan tersebut adalah 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) dan melakukan operasi kebalikan (invers) untuk menemukan bilangan awal. Ini melibatkan penerapan konsep nilai tempat dalam konteks pemecahan masalah rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur bilangan (puluhan dan satuan) dan bagaimana operasi aritmatika mempengaruhi nilai tempat tersebut.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa melakukan operasi invers (pengurangan) pada nilai tempat yang spesifik. Meskipun prosedurnya familiar, siswa harus memisahkan puluhan dan satuan dari hasil akhir untuk mendapatkan bilangan awal, yang merupakan langkah integrasi sedang bagi kelas 2.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah belajar nilai tempat dan pengurangan. Menentukan bilangan awal dari hasil akhir dengan operasi invers pada masing-masing nilai tempat adalah tantangan yang sesuai untuk tingkat menengah di kelas 2. |

Run 2 — solusi: Bilangan Kira adalah N. Diketahui N + (40 + 3) = 55. Maka N = 55 - 43 = 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) dan melakukan operasi kebalikan (pengurangan) untuk menemukan bilangan awal. Ini melibatkan penerapan konsep nilai tempat pada konteks rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana angka disusun berdasarkan nilai tempat (puluhan dan satuan) dan bagaimana operasi aritmatika mempengaruhi posisi tersebut.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa melakukan operasi kebalikan (invers) dari penambahan nilai tempat. Meskipun prosedurnya familiar, siswa harus memahami struktur bilangan dua digit dan melakukan pengurangan pada posisi yang tepat (puluhan dengan puluhan, satuan dengan satuan). Ini adalah tugas rutin bagi kelas 2 namun memerlukan pemahaman konsep nilai tempat yang baik.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua digit (puluhan dan satuan) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah belajar nilai tempat dan penjumlahan/pengurangan bilangan dua digit. Soal ini menuntut pembalikan logika (invers) yang merupakan langkah menengah dalam pemahaman konsep nilai tempat. |

Run 3 — solusi: Bilangan awal memiliki puluhan dan satuan. Hasil akhir 55 berarti 5 puluhan dan 5 satuan. Operasi invers dari 'tambah 4 pada puluhan' adalah 'kurang 4 dari puluhan' (5-4=1). Operasi invers dari 'tambah 3 pada satuan' adalah 'kurang 3 dari satuan' (5-3=2). Jadi, bilangan awal adalah 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) dan melakukan operasi invers untuk menemukan bilangan awal. Ini melibatkan penerapan konsep nilai tempat pada konteks rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman tentang struktur bilangan (puluhan dan satuan) untuk memecahkan masalah, yang merupakan pengetahuan konseptual.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman invers operasi pada nilai tempat. Meskipun prosedurnya familiar, siswa harus membalikkan dua operasi secara terpisah (puluhan dan satuan) untuk mendapatkan jawaban. Ini adalah tugas rutin dengan beberapa langkah yang saling terkait.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah mempelajari nilai tempat. Soal ini menuntut pembalikan operasi yang memerlukan ketelitian pada dua posisi nilai tempat yang berbeda, sehingga tingkat kesulitannya menengah bagi siswa kelas 2. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 77/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.991164; applying=0.008836; reasoning=0.000000 | knowing | 0.991164 | 0.046041 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.103234; conceptual=0.841834; procedural=0.054932; metacognitive=0.000000 | conceptual | 0.841834 | 0.388629 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.754643; Medium=0.242162; Hard=0.003195 | Easy | 0.754643 | 0.522678 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.991164; −Σp ln(p) = 0.050581; H = 0.050581/ln(3) = 0.046041; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.841834; −Σp ln(p) = 0.538754; H = 0.538754/ln(4) = 0.388629; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.754643; −Σp ln(p) = 0.574221; H = 0.574221/ln(3) = 0.522678; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira menuliskan satu bilangan.

Kira berkata, 'Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.' Berapa bilangan yang ditulis Kira?
Pilihan: A. 92
B. 29
C. 12
D. 81
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `4a38b766ecd4b82494e8afb8`

Aku adalah bilangan. Aku 1 kurangnya dari bilangan 67. Bilangan berapakah aku?

| Opsi | Isi |
|---|---|
| A | 67 |
| B | 66 |
| C | 68 |
| D | 57 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bilangan yang dimaksud adalah 67 - 1 = 66.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a23232d5cb5b77d04ed6637d11d357873f74c323e8fb957c16bf8e7468651183`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2168 |
| 2 | success | valid / verified | knowing | factual | Easy | 2163 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2174 |

Run 1 — solusi: Bilangan yang dimaksud adalah 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi pengurangan dasar (67 - 1) untuk menemukan bilangan yang dimaksud. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Aku 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang urutan bilangan dan konsep 'kurang dari' yang merupakan pengetahuan prosedural dasar dalam aritmatika.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan satu langkah operasi pengurangan sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Aku 1 kurangnya dari bilangan 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan cacah sampai 100 dan operasi pengurangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan konsep 'kurang dari' dan pengurangan satu satuan dari bilangan dua angka. |

Run 2 — solusi: Bilangan yang dimaksud adalah 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi pengurangan dasar (67 - 1) untuk menentukan bilangan yang dimaksud. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Aku 1 kurangnya dari bilangan 67.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dan operasi pengurangan dasar (fakta numerik).. Bukti: Aku 1 kurangnya dari bilangan 67.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan satu langkah operasi pengurangan sederhana. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: Aku 1 kurangnya dari bilangan 67.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan cacah sampai 100 dan konsep pengurangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, menentukan bilangan '1 kurangnya' dari bilangan dua digit adalah tugas rutin yang sangat mendasar. |

Run 3 — solusi: Bilangan yang dimaksud adalah 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar (67 - 1) untuk menemukan bilangan yang dimaksud. Ini adalah prosedur langsung yang sudah dipelajari di kelas 2.. Bukti: Aku 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang urutan bilangan dan konsep 'kurang dari' yang merupakan pengetahuan prosedural dasar dalam aritmatika.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan satu langkah pengurangan sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks.. Bukti: Aku 1 kurangnya dari bilangan 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan cacah sampai 100 dan operasi pengurangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, pengurangan satu satuan dari bilangan dua digit adalah tugas rutin yang sangat mendasar dan tidak menuntut perencanaan tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3351`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan operasi pengurangan satu satuan (67 - 1) yang merupakan prosedur langsung dan rutin bagi siswa kelas 2.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang urutan bilangan dan operasi pengurangan dasar, yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini sangat langsung, hanya memerlukan satu langkah pengurangan sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan cacah sampai 100 dan operasi pengurangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, pengurangan satu satuan dari bilangan dua digit adalah tugas rutin yang sangat mendasar dan tidak menuntut perencanaan tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999925; applying=0.000075; reasoning=0.000000 | knowing | 0.999925 | 0.000718 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.550557; conceptual=0.398305; procedural=0.051138; metacognitive=0.000000 | factual | 0.550557 | 0.611188 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.819093; Medium=0.178258; Hard=0.002648 | Easy | 0.819093 | 0.442905 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999925; −Σp ln(p) = 0.000788; H = 0.000788/ln(3) = 0.000718; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.550557; −Σp ln(p) = 0.847286; H = 0.847286/ln(4) = 0.611188; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.819093; −Σp ln(p) = 0.486581; H = 0.486581/ln(3) = 0.442905; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Aku adalah bilangan. Aku 1 kurangnya dari bilangan 67. Bilangan berapakah aku?
Pilihan: A. 67
B. 66
C. 68
D. 57
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `874e86479e51d283015833cd`

Kira sedang mendata mainan kesukaan teman-temannya.<br><br>Berapa banyak mainan mobil-mobilan pada gambar tersebut?

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 6 |
| C | 4 |
| D | 2 |

![Gambar sumber soal 40](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0246-03.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah mainan mobil-mobilan yang terlihat pada gambar. Terdapat 1 mobil merah dan 1 mobil ungu. Total = 2.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0246-03.png. Transkripsi visual: Gambar menunjukkan seorang anak perempuan memegang kotak berisi boneka beruang. Di lantai terdapat mainan: 2 mobil-mobilan (satu merah, satu ungu), 3 boneka beruang (satu ungu, satu merah muda, satu kuning-biru), 6 balok mainan (berbagai warna), dan 5 kelereng.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `669f9f6c2e9ad5c28809242ebc6adf93a0362813011e83a246f5f0338cedc793`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3401 |
| 2 | success | valid / verified | knowing | factual | Easy | 3408 |
| 3 | success | valid / verified | knowing | factual | Easy | 3404 |

Run 1 — solusi: Menghitung jumlah mainan mobil-mobilan yang terlihat pada gambar. Terdapat 1 mobil merah dan 1 mobil ungu. Total = 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan identifikasi visual dan menghitung objek yang terlihat secara langsung. Tidak ada prosedur kompleks atau penalaran yang diperlukan.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan dasar dalam mengenali objek dan menghitung jumlahnya (fakta dasar).. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung dan penghitungan objek yang jumlahnya sedikit. Tidak ada langkah yang saling bergantung atau strategi yang perlu dipilih.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 2, menghitung objek dalam gambar adalah tugas rutin yang sangat mendasar dan sesuai dengan tingkat perkembangan mereka. |

Run 2 — solusi: Mengamati gambar dan menghitung jumlah mobil-mobilan secara langsung. Terdapat 1 mobil merah dan 1 mobil ungu. Total = 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan identifikasi visual dan menghitung objek yang terlihat secara langsung tanpa perlu manipulasi data atau inferensi lebih lanjut.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan mengenali objek (fakta) dalam konteks visual sederhana.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung terhadap objek yang jelas. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, menghitung objek dalam gambar adalah tugas dasar yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Mengamati gambar secara langsung, terdapat 1 mobil-mobilan berwarna merah dan 1 mobil-mobilan berwarna ungu. Total mobil-mobilan = 1 + 1 = 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan identifikasi visual dan menghitung objek yang terlihat secara langsung (counting) tanpa perlu manipulasi data atau inferensi lebih lanjut.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan mengenali objek (fakta) dalam sebuah gambar untuk kemudian dihitung jumlahnya.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung dan penghitungan dasar. Tidak ada langkah kompleks atau kendala yang harus dipecahkan.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, menghitung objek dalam gambar adalah tugas rutin yang sangat mendasar dan sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 126/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000007 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.254197; conceptual=0.744589; procedural=0.001214; metacognitive=0.000000 | conceptual | 0.744589 | 0.415430 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.839130; Medium=0.157282; Hard=0.003588 | Easy | 0.839130 | 0.417166 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000007; H = 0.000007/ln(3) = 0.000007; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.744589; −Σp ln(p) = 0.575908; H = 0.575908/ln(4) = 0.415430; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.839130; −Σp ln(p) = 0.458303; H = 0.458303/ln(3) = 0.417166; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Turus
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira sedang mendata mainan kesukaan teman-temannya.

Berapa banyak mainan mobil-mobilan pada gambar tersebut?
Pilihan: A. 7
B. 6
C. 4
D. 2
Transkripsi visual: Gambar menunjukkan seorang anak perempuan memegang kotak berisi boneka beruang. Di lantai terdapat mainan: 2 mobil-mobilan (satu merah, satu ungu), 3 boneka beruang (satu ungu, satu merah muda, satu kuning-biru), 6 balok mainan (berbagai warna), dan 5 kelereng.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `a425d49d4fa1757682ab7805`

Perhatikan gambar di bawah ini. Malosi sedang mendata banyaknya buah yang dibeli Ibu di pasar.<br><br>Berapa banyak buah semangka yang dibeli ibu?

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 3 |
| C | 7 |
| D | 1 |

![Gambar sumber soal 41](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0258-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengamati gambar dan menghitung jumlah buah semangka yang ada di atas meja. Hanya terdapat 1 buah semangka.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0258-04.png. Transkripsi visual: Gambar menunjukkan seorang anak laki-laki di belakang meja yang berisi berbagai buah. Terdapat 1 buah semangka besar, 3 buah apel merah, 3 buah alpukat hijau, dan 6 buah jeruk kecil.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dfd245f0b2ff89bc47bdf0ea9075c27acb7d2a95db17153b634b47b926e2635d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3242 |
| 2 | success | valid / verified | knowing | factual | Easy | 3203 |
| 3 | success | valid / verified | knowing | factual | Easy | 3242 |

Run 1 — solusi: Mengamati gambar dan menghitung jumlah buah semangka yang ada di atas meja. Hanya terdapat 1 buah semangka.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan identifikasi visual langsung dan menghitung objek yang terlihat (counting) untuk menjawab pertanyaan.. Bukti: Berapa banyak buah semangka yang dibeli ibu?; hanya terlihat 1 semangka
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan siswa dalam mengenali objek (buah semangka) dan menghitung jumlahnya sebagai elemen dasar data.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta penghitungan satu jenis objek yang terlihat jelas. Tidak ada langkah kompleks atau integrasi data.. Bukti: Berapa banyak buah semangka yang dibeli ibu?; hanya terlihat 1 semangka

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa melakukan penghitungan objek sederhana dari gambar. Tugas ini adalah tugas dasar pengumpulan data visual. |

Run 2 — solusi: Mengamati gambar dan menghitung jumlah buah semangka yang ada di atas meja. Hanya terdapat 1 buah semangka.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan identifikasi visual langsung dan menghitung objek yang terlihat (counting) untuk menjawab pertanyaan.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan siswa dalam mengenali objek (fakta) dan melakukan penghitungan dasar.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Intended difficulty `classify/Easy`: Tugas ini sangat sederhana, hanya memerlukan pengamatan visual langsung tanpa langkah perencanaan atau integrasi konsep yang kompleks.. Bukti: Berapa banyak buah semangka yang dibeli ibu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, menghitung jumlah objek dalam gambar adalah tugas rutin yang sangat mendasar. |

Run 3 — solusi: Mengamati gambar dan menghitung jumlah buah semangka yang ada di atas meja. Hanya terdapat 1 buah semangka.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek spesifik (semangka) dari sekumpulan objek yang ada pada gambar. Ini adalah tugas membaca data visual yang sangat langsung.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Dimensi pengetahuan `classify/factual`: Tugas ini melibatkan pengenalan objek (fakta visual) dan penghitungan dasar, yang termasuk dalam kategori pengetahuan faktual.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta siswa untuk menghitung satu jenis objek yang jumlahnya sangat sedikit (hanya 1). Tidak ada proses integrasi atau perencanaan yang diperlukan.. Bukti: Berapa banyak buah semangka yang dibeli ibu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek sederhana (bilangan cacah 1-10). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, menghitung objek konkret dalam gambar adalah tugas dasar yang sudah sangat familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 110/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000041; applying=0.999959; reasoning=0.000000 | applying | 0.999959 | 0.000418 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.253727; conceptual=0.738144; procedural=0.008129; metacognitive=0.000000 | conceptual | 0.738144 | 0.440900 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.899420; Medium=0.094803; Hard=0.005777 | Easy | 0.899420 | 0.317188 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999959; −Σp ln(p) = 0.000459; H = 0.000459/ln(3) = 0.000418; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.738144; −Σp ln(p) = 0.611217; H = 0.611217/ln(4) = 0.440900; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.899420; −Σp ln(p) = 0.348466; H = 0.348466/ln(3) = 0.317188; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Turus
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar di bawah ini. Malosi sedang mendata banyaknya buah yang dibeli Ibu di pasar.

Berapa banyak buah semangka yang dibeli ibu?
Pilihan: A. 2
B. 3
C. 7
D. 1
Transkripsi visual: Gambar menunjukkan seorang anak laki-laki di belakang meja yang berisi berbagai buah. Terdapat 1 buah semangka besar, 3 buah apel merah, 3 buah alpukat hijau, dan 6 buah jeruk kecil.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `655cea6ab3fa2ff165080502`

Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.<br><br>Ada 5 anak yang suka onde-onde.<br>Ada 3 anak yang suka lemper.<br><br> Ada .... anak yang suka kue cucur.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 6 |
| C | 3 |
| D | 7 |

![Gambar sumber soal 42](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Menghitung jumlah simbol bintang pada baris kue cucur. Terdapat 6 simbol bintang, sehingga ada 6 anak yang suka kue cucur.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: Tabel 'Kue Kesukaan' dan 'Banyak Anak'. Baris 1: Gambar kue cucur, diikuti 6 simbol bintang. Baris 2: Gambar onde-onde, diikuti 5 simbol bintang. Baris 3: Gambar lemper, diikuti 3 simbol bintang. Baris 4: Gambar kue talam, diikuti 7 simbol bintang. Keterangan: Setiap gambar bintang mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9ca9b9cde035390bd5ba1696421253652813b4abdd46540c582a81b09e48603f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3495 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3508 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3489 |

Run 1 — solusi: Menghitung jumlah simbol bintang pada baris kue cucur. Terdapat 6 simbol bintang, sehingga ada 6 anak yang suka kue cucur.
- Domain kognitif `classify/knowing`: Soal meminta siswa membaca data dari diagram gambar (pictograph) secara langsung. Siswa hanya perlu menghitung jumlah simbol yang merepresentasikan data, yang merupakan prosedur dasar dalam membaca data.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara simbol (bintang) dan data (jumlah anak) dalam diagram gambar, yang merupakan pemahaman konseptual dasar tentang representasi data.. Bukti: Setiap gambar mewakili 1 anak.; Diagram Gambar Kue Kesukaan.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu melakukan penghitungan langsung (counting) pada simbol yang tersedia tanpa ada langkah tambahan atau manipulasi data.. Bukti: Ada .... anak yang suka kue cucur.; Setiap gambar mewakili 1 anak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret atau simbol hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa membaca diagram gambar sederhana dengan skala 1:1. Tugas ini hanya memerlukan penghitungan langsung. |

Run 2 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram gambar: terdapat 6 bintang, sehingga ada 6 anak yang suka kue cucur.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram gambar (pictograph) sederhana dengan melakukan korespondensi satu-satu antara gambar bintang dan jumlah anak. Ini adalah prosedur langsung yang familiar bagi siswa kelas 2.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang cara membaca dan menginterpretasikan representasi data sederhana (diagram gambar) yang merupakan pengetahuan konseptual dasar dalam statistika.. Bukti: Setiap gambar mewakili 1 anak.; Diagram Gambar Kue Kesukaan.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan penghitungan langsung (counting) pada baris yang relevan di diagram gambar. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Ada .... anak yang suka kue cucur.; Setiap gambar mewakili 1 anak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret atau gambar secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca diagram gambar sederhana adalah materi standar kelas 2. Soal ini tidak menuntut analisis data yang kompleks, hanya pembacaan data langsung. |

Run 3 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram gambar. Terdapat 6 bintang, sehingga ada 6 anak yang suka kue cucur.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram gambar (pictograph) secara langsung. Tugas ini hanya memerlukan kemampuan mengenali dan menghitung objek (bintang) yang merepresentasikan data, yang merupakan prosedur yang sangat langsung.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana dalam bentuk diagram gambar, di mana setiap simbol memiliki nilai satu-ke-satu.. Bukti: Setiap gambar mewakili 1 anak.; Diagram Gambar Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 2 karena hanya memerlukan penghitungan langsung jumlah simbol pada satu baris diagram. Tidak ada langkah tambahan atau integrasi data yang diperlukan.. Bukti: Ada .... anak yang suka kue cucur.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret atau simbol hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca diagram gambar sederhana adalah materi standar kelas 2. Soal ini bersifat langsung tanpa memerlukan manipulasi data. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 189/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.009527; conceptual=0.969749; procedural=0.020724; metacognitive=0.000000 | conceptual | 0.969749 | 0.111420 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.571343; Medium=0.413746; Hard=0.014911 | Easy | 0.571343 | 0.680551 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.969749; −Σp ln(p) = 0.154461; H = 0.154461/ln(4) = 0.111420; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.571343; −Σp ln(p) = 0.747662; H = 0.747662/ln(3) = 0.680551; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.

Ada 5 anak yang suka onde-onde.
Ada 3 anak yang suka lemper.

 Ada .... anak yang suka kue cucur.
Pilihan: A. 5
B. 6
C. 3
D. 7
Transkripsi visual: Tabel 'Kue Kesukaan' dan 'Banyak Anak'. Baris 1: Gambar kue cucur, diikuti 6 simbol bintang. Baris 2: Gambar onde-onde, diikuti 5 simbol bintang. Baris 3: Gambar lemper, diikuti 3 simbol bintang. Baris 4: Gambar kue talam, diikuti 7 simbol bintang. Keterangan: Setiap gambar bintang mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `3606c1d695032907b61d4fbc`

Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.<br><br>Ada 5 anak yang suka onde-onde.<br>Ada 3 anak yang suka lemper.<br><br>Ada .... anak yang suka kue talam.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 3 |
| C | 6 |
| D | 7 |

![Gambar sumber soal 43](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah bintang pada baris kue talam di diagram gambar. Terdapat 7 bintang, yang berarti 7 anak menyukai kue talam.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: Diagram gambar menampilkan empat baris kue. Baris pertama (kue cucur) memiliki 6 bintang. Baris kedua (onde-onde) memiliki 5 bintang. Baris ketiga (lemper) memiliki 3 bintang. Baris keempat (kue talam) memiliki 7 bintang. Keterangan: Setiap gambar mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ef2554e3aeb7ea31316270a8fba055af52b41f8d38bb9a2af8cc466acf2fe980`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3554 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3493 |
| 3 | success | valid / verified | knowing | factual | Easy | 3493 |

Run 1 — solusi: Menghitung jumlah bintang pada baris kue talam di diagram gambar. Terdapat 7 bintang, yang berarti 7 anak menyukai kue talam.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram gambar (pictograph) secara langsung. Ini adalah tugas mengenali dan membaca informasi yang disajikan dalam bentuk visual sederhana, yang termasuk dalam domain knowing.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) dan hubungan antara simbol (bintang) dengan kuantitas (jumlah anak). Ini melibatkan pengetahuan konseptual tentang bagaimana data divisualisasikan.. Bukti: Setiap gambar mewakili 1 anak.; Diagram Gambar Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 2. Siswa hanya perlu melakukan korespondensi satu-ke-satu antara gambar bintang dan angka. Tidak ada langkah kompleks, tidak ada strategi yang perlu dipilih, dan tidak ada kendala yang berinteraksi.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret atau gambar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca diagram gambar sederhana adalah materi standar kelas 2. Tugas ini bersifat rutin dan langsung, tidak memerlukan perencanaan atau integrasi konsep. |

Run 2 — solusi: Menghitung jumlah bintang pada baris kue talam di diagram gambar. Terdapat 7 bintang, yang berarti ada 7 anak yang menyukai kue talam.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca diagram gambar secara langsung dengan menghitung jumlah simbol (bintang) yang mewakili data kue talam. Tidak ada proses manipulasi data atau inferensi yang diperlukan.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang cara membaca dan menginterpretasikan data sederhana yang disajikan dalam bentuk diagram gambar (piktogram).. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan penghitungan satu-ke-satu antara simbol dan nilai (1 bintang = 1 anak). Tidak ada langkah tambahan atau kendala yang perlu dipertimbangkan.. Bukti: Ada .... anak yang suka kue talam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret atau simbol hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa membaca data sederhana dari tabel atau diagram gambar. Tugas ini adalah tugas dasar membaca data tanpa memerlukan analisis lebih lanjut. |

Run 3 — solusi: Menghitung jumlah bintang pada baris 'kue talam' di diagram gambar. Terdapat 7 bintang, yang berarti 7 anak menyukai kue talam.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram gambar (pictograph) secara langsung. Tugas ini hanya memerlukan kemampuan mengenali simbol dan menghitung jumlah objek yang disajikan dalam bentuk visual sederhana, yang merupakan prosedur langsung.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) di mana satu simbol mewakili satu unit data (fakta).. Bukti: Diagram Gambar Kue Kesukaan.; Setiap gambar mewakili 1 anak.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu menghitung jumlah simbol (bintang) pada baris yang ditanyakan tanpa ada operasi tambahan atau interpretasi yang kompleks.. Bukti: Ada .... anak yang suka kue talam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret atau gambar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca diagram gambar sederhana adalah materi standar kelas 2. Soal ini tidak memerlukan perencanaan atau integrasi langkah, hanya observasi visual langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4852`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk membaca data dari diagram gambar (piktogram) secara langsung. Tugas ini hanya memerlukan kemampuan mengenali simbol dan menghitung jumlah objek yang disajikan dalam bentuk visual sederhana, yang merupakan prosedur langsung (knowing).
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) di mana satu simbol mewakili satu unit data. Ini adalah pengetahuan konseptual tentang bagaimana data divisualisasikan.
- Intended difficulty `Easy`: Soal ini sangat mudah karena siswa hanya perlu menghitung jumlah simbol (bintang) pada baris yang ditanyakan tanpa ada operasi tambahan atau interpretasi yang kompleks. Jalur penyelesaian sangat jelas dan langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret atau gambar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca diagram gambar sederhana adalah materi standar kelas 2. Soal ini tidak memerlukan perencanaan atau integrasi langkah, hanya observasi visual langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 176/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.002567; conceptual=0.994685; procedural=0.002748; metacognitive=0.000000 | conceptual | 0.994685 | 0.026560 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.666169; Medium=0.323725; Hard=0.010106 | Easy | 0.666169 | 0.620926 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000002; H = 0.000002/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.994685; −Σp ln(p) = 0.036819; H = 0.036819/ln(4) = 0.026560; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.666169; −Σp ln(p) = 0.682157; H = 0.682157/ln(3) = 0.620926; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.

Ada 5 anak yang suka onde-onde.
Ada 3 anak yang suka lemper.

Ada .... anak yang suka kue talam.
Pilihan: A. 5
B. 3
C. 6
D. 7
Transkripsi visual: Diagram gambar menampilkan empat baris kue. Baris pertama (kue cucur) memiliki 6 bintang. Baris kedua (onde-onde) memiliki 5 bintang. Baris ketiga (lemper) memiliki 3 bintang. Baris keempat (kue talam) memiliki 7 bintang. Keterangan: Setiap gambar mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `e7d8a29f2e3a28f99529dfc8`

Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Diagram Buah Kesukaan. Gambar mewakili 1 anak. Lengkapi setiap kalimat berikut.<br><br>Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 1 |
| C | 4 |
| D | 3 |

![Gambar sumber soal 44](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `3`.
Solusi minimum hasil AI: Hitung jumlah bintang untuk belimbing (7) dan apel (4). Hitung selisihnya: 7 - 4 = 3.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png. Transkripsi visual: Diagram batang gambar (pictograph) berjudul 'Diagram Buah Kesukaan'. Terdapat empat kolom buah dari kiri ke kanan: jeruk, apel, belimbing, jambu air. Setiap gambar bintang mewakili 1 anak. Jumlah bintang per kolom: jeruk (6), apel (4), belimbing (7), jambu air (5). Keterangan: 'Gambar mewakili 1 anak'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7e3e412d225e4698582c892149ec0e6437512683d118982813e17fa2e44280dc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3421 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3424 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3511 |

Run 1 — solusi: Hitung jumlah bintang untuk belimbing (7) dan apel (4). Hitung selisihnya: 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram gambar (mengambil informasi) dan melakukan operasi pengurangan sederhana untuk mencari selisih. Ini adalah penerapan prosedur rutin pada konteks diagram.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data dalam bentuk diagram gambar (konsep dasar penyajian data).. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.; Gambar mewakili 1 anak.
- Intended difficulty `classify/Easy`: Soal ini meminta siswa membaca dua data dari diagram dan melakukan satu operasi pengurangan. Langkah-langkahnya jelas, familiar bagi kelas 2, dan tidak memerlukan perencanaan kompleks.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung jumlah objek dalam diagram gambar dan melakukan pengurangan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan membaca diagram gambar sederhana dan melakukan pengurangan dasar. Tugas ini adalah aplikasi langsung dari keterampilan tersebut. |

Run 2 — solusi: Hitung jumlah anak yang suka belimbing (7 bintang) dan apel (4 bintang). Hitung selisihnya: 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram gambar (ekstraksi informasi) dan melakukan operasi pengurangan sederhana untuk mencari selisih. Ini adalah penerapan prosedur rutin pada konteks diagram.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data direpresentasikan dalam diagram gambar dan prosedur untuk membandingkan dua nilai.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.; Gambar mewakili 1 anak.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menghitung jumlah item pada dua kategori yang jelas dan melakukan pengurangan dasar. Tidak ada kendala yang berinteraksi atau perencanaan kompleks yang diperlukan.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (1-10) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa membaca diagram gambar sederhana dan melakukan operasi hitung dasar untuk membandingkan jumlah. |

Run 3 — solusi: Hitung jumlah anak yang suka belimbing (7 bintang) dan apel (4 bintang). Hitung selisihnya: 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari piktogram (mengambil informasi faktual) dan melakukan operasi pengurangan sederhana untuk menemukan selisih antara dua kategori. Ini adalah penerapan prosedur rutin pada konteks data yang diberikan.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data dalam bentuk diagram gambar (piktogram), yang merupakan pengetahuan konseptual dasar tentang representasi data.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menghitung jumlah bintang untuk dua kategori yang ditentukan (belimbing dan apel) dan melakukan pengurangan sederhana. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan representasi piktogram sangat familiar bagi siswa kelas 2.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (bintang) dan melakukan pengurangan bilangan cacah di bawah 10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan membaca diagram gambar sederhana dan operasi pengurangan dasar. Tugas ini merupakan penerapan langsung dari keterampilan tersebut tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 160/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000027; applying=0.999973; reasoning=0.000000 | applying | 0.999973 | 0.000287 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.005704; conceptual=0.992025; procedural=0.002271; metacognitive=0.000000 | conceptual | 0.992025 | 0.036959 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.639628; Medium=0.346655; Hard=0.013717 | Easy | 0.639628 | 0.648015 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999973; −Σp ln(p) = 0.000316; H = 0.000316/ln(3) = 0.000287; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.992025; −Σp ln(p) = 0.051236; H = 0.051236/ln(4) = 0.036959; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.639628; −Σp ln(p) = 0.711917; H = 0.711917/ln(3) = 0.648015; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Diagram Buah Kesukaan. Gambar mewakili 1 anak. Lengkapi setiap kalimat berikut.

Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
Pilihan: A. 2
B. 1
C. 4
D. 3
Transkripsi visual: Diagram batang gambar (pictograph) berjudul 'Diagram Buah Kesukaan'. Terdapat empat kolom buah dari kiri ke kanan: jeruk, apel, belimbing, jambu air. Setiap gambar bintang mewakili 1 anak. Jumlah bintang per kolom: jeruk (6), apel (4), belimbing (7), jambu air (5). Keterangan: 'Gambar mewakili 1 anak'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
