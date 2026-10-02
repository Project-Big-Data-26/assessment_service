# Validasi ulang soal kelas 2 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v4-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v2-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 2 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model lama dipakai untuk menunjukkan ketidaksepakatan; tidak diberikan kembali ke Gemini.

Jumlah soal: 44; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 20, "applying": 22, "reasoning": 1, "undecided": 1}, "knowledgeDimension": {"factual": 6, "conceptual": 29, "procedural": 8, "undecided": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 37, "Medium": 6, "undecided": 1, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 18, "applying": 22, "reasoning": 1}, "knowledgeDimension": {"factual": 5, "conceptual": 28, "procedural": 8, "metacognitive": 0}, "intendedDifficulty": {"Easy": 35, "Medium": 6, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 41, "revision_required": 3}`.
Run awal sukses: 132/132; adjudikasi: 24; token sukses tercatat: 455,648.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 37 | 35 | [Easy.json](difficulty/Easy.json) |
| Medium | 6 | 6 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

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
Solusi minimum hasil AI: Urutan bilangan adalah 28, 29, 30, 31, 32. Jadi, bilangan yang hilang adalah 29, 31, dan 32.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9dae8db58bc38d1bdbc2fe9233bc23fe9ed77529637e9fa22dbf2d3a7d764218`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1403 |
| 2 | success | valid / verified | knowing | factual | Easy | 1431 |
| 3 | success | valid / verified | knowing | factual | Easy | 1418 |

Run 1 — solusi: Urutan bilangan adalah 28, 29, 30, 31, 32. Jadi, bilangan yang hilang adalah 29, 31, dan 32.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan cacah (menambah 1) dan mengisi bagian yang kosong secara langsung.. Bukti: Lengkapi urutan bilangan di bawah ini. 28 ... 30 ... ...
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar dalam sistem bilangan).. Bukti: 28 ... 30 ... ...
- Intended difficulty `classify/Easy`: Soal ini sangat rutin dan langsung, hanya memerlukan pengenalan urutan bilangan dasar.. Bukti: 28 ... 30 ... ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung maju bilangan 1-50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD yang menekankan pengenalan urutan bilangan cacah. |

Run 2 — solusi: Urutan bilangan adalah 28, 29, 30, 31, 32. Jadi, bilangan yang hilang adalah 29, 31, dan 32.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan cacah sederhana (menambah 1) dan mengisi bagian yang kosong secara langsung.. Bukti: Lengkapi urutan bilangan di bawah ini. 28 ... 30 ... ...
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar) dalam sistem bilangan cacah.. Bukti: 28 ... 30 ... ...
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, menggunakan representasi angka yang familiar, dan hanya memerlukan pemahaman urutan bilangan dasar yang sesuai untuk kelas 2.. Bukti: 28 ... 30 ... ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang dan mengurutkan bilangan 1-50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD untuk materi urutan bilangan. |

Run 3 — solusi: Urutan bilangan adalah 28, 29, 30, 31, 32. Jadi, bilangan yang hilang adalah 29, 31, dan 32.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan cacah sederhana (menambah 1) dan mengisi bagian yang kosong, yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan di bawah ini. 28 ... 30 ... ...
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar dalam sistem bilangan).. Bukti: 28 ... 30 ... ...
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan urutan bilangan yang familiar dengan satu aturan sederhana.. Bukti: 28 ... 30 ... ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-50 secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD untuk materi urutan bilangan sampai 50. |

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `bffdfbd5e63e7fbc426dd6b7`

35 dibaca ....

| Opsi | Isi |
|---|---|
| A | lima puluh tiga |
| B | empat puluh lima |
| C | tiga puluh lima |
| D | tiga puluh enam |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Angka 35 terdiri dari angka 3 di posisi puluhan dan 5 di posisi satuan, sehingga dibaca 'tiga puluh lima'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0fdd0ee6ff02ca4c71dc8639d96ef5e14e00f4ccd1bc93c9422df6820dbca7e1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1268 |
| 2 | success | valid / verified | knowing | factual | Easy | 1175 |
| 3 | success | valid / verified | knowing | factual | Easy | 1288 |

Run 1 — solusi: Angka 35 terdiri dari angka 3 di posisi puluhan dan 5 di posisi satuan, sehingga dibaca 'tiga puluh lima'.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengingat dan menerapkan pengetahuan dasar tentang cara membaca lambang bilangan, yang merupakan proses langsung.. Bukti: 35 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang sistem penamaan bilangan (fakta dasar) dalam sistem desimal.. Bukti: 35 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan simbol angka dan padanan katanya dalam bahasa Indonesia tanpa langkah prosedural yang kompleks.. Bukti: 35 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca lambang bilangan dua digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan adalah kompetensi dasar kelas 2 yang bersifat rutin dan langsung. |

Run 2 — solusi: Angka 35 terdiri dari angka 3 di posisi puluhan (tiga puluh) dan 5 di posisi satuan (lima), sehingga dibaca tiga puluh lima.
- Domain kognitif `classify/knowing`: Soal ini hanya memerlukan pengenalan langsung terhadap lambang bilangan dan cara membacanya sesuai dengan nilai tempat, yang merupakan proses kognitif dasar.. Bukti: 35 dibaca ....
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami konvensi penamaan bilangan (fakta dasar) dalam sistem bilangan desimal.. Bukti: 35 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan pengenalan simbol angka yang sudah familiar bagi siswa kelas 2 tanpa memerlukan langkah perhitungan atau strategi kompleks.. Bukti: 35 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan serta nama bilangan 1-50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan dua digit adalah kompetensi dasar yang diharapkan dikuasai siswa kelas 2 di awal atau pertengahan semester. |

Run 3 — solusi: Angka 35 terdiri dari angka 3 di posisi puluhan (tiga puluh) dan 5 di posisi satuan (lima), sehingga dibaca 'tiga puluh lima'.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengingat dan mengenali nama bilangan dari simbol angka yang diberikan, yang merupakan proses kognitif tingkat dasar.. Bukti: 35 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol angka dan cara membacanya, yang termasuk dalam kategori fakta dasar dalam sistem bilangan.. Bukti: 35 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, menggunakan representasi yang sangat familiar bagi siswa kelas 2, dan tidak memerlukan langkah pemrosesan tambahan.. Bukti: 35 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca nama bilangan dasar 1-50. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan dua digit adalah kompetensi dasar yang diharapkan sudah dikuasai siswa kelas 2 secara rutin. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `84fcc60564bf4fa76e2051cf`

Isilah titik-titik berikut dengan bilangan yang tepat.<br><br>24 = ... puluhan + ... satuan

| Opsi | Isi |
|---|---|
| A | 4 puluhan + 2 satuan |
| B | 2 puluhan + 4 satuan |
| C | 2 puluhan + 40 satuan |
| D | 20 puluhan + 4 satuan |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bilangan 24 terdiri dari 2 puluhan (20) dan 4 satuan (4).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `52d327efb14fbd6990464a71cb743e56f625fa6ee64d600f2c06bf7bee93b09b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1181 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1231 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1231 |

Run 1 — solusi: Bilangan 24 terdiri dari 2 puluhan (20) dan 4 satuan (4).
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menerapkan pemahaman dasar tentang nilai tempat bilangan dua digit secara langsung.. Bukti: 24 = ... puluhan + ... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar bilangan.. Bukti: 24 = ... puluhan + ... satuan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2, melibatkan prosedur familiar tanpa langkah kompleks.. Bukti: 24 = ... puluhan + ... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar nilai tempat bilangan dua digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat adalah kurikulum standar kelas 2 SD, soal ini bersifat langsung dan rutin. |

Run 2 — solusi: Bilangan 24 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 4 di tempat satuan (bernilai 4). Maka, 24 = 2 puluhan + 4 satuan.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi nilai tempat dari angka yang diberikan, yang merupakan proses langsung dalam mengenali struktur bilangan.. Bukti: 24 = ... puluhan + ... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai konsep nilai tempat (puluhan dan satuan) dalam sistem bilangan desimal.. Bukti: Nilai Tempat
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan prosedur familiar dengan satu langkah identifikasi nilai tempat tanpa kompleksitas tambahan.. Bukti: 24 = ... puluhan + ... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat puluhan dan satuan untuk bilangan dua angka. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat adalah kurikulum inti kelas 2. Soal ini bersifat langsung dan tidak memerlukan strategi pemecahan masalah yang kompleks. |

Run 3 — solusi: Bilangan 24 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 4 di tempat satuan (bernilai 4). Jadi, 24 = 2 puluhan + 4 satuan.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menerapkan pemahaman dasar tentang nilai tempat (puluhan dan satuan) pada bilangan dua digit secara langsung.. Bukti: 24 = ... puluhan + ... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat dalam sistem bilangan desimal, yang merupakan konsep dasar.. Bukti: 24 = ... puluhan + ... satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar nilai tempat untuk bilangan dua digit tanpa langkah tambahan.. Bukti: 24 = ... puluhan + ... satuan

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
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD yang fokus pada pengenalan nilai tempat bilangan cacah sampai 100. |

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `120f51a1f7135cf30273aba8`

Isilah dengan bilangan yang tepat.<br><br>28 = puluhan + satuan

| Opsi | Isi |
|---|---|
| A | 20 puluhan + 8 satuan |
| B | 2 puluhan + 8 satuan |
| C | 2 puluhan + 80 satuan |
| D | 8 puluhan + 2 satuan |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Angka 28 terdiri dari 2 puluhan (20) dan 8 satuan (8). Maka, 28 = 2 puluhan + 8 satuan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c8cd650aca536be15f184e4d5600cca60eb7f5ec9fb66bae4608280c133e188a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1333 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1325 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1340 |

Run 1 — solusi: Angka 28 terdiri dari 2 puluhan (20) dan 8 satuan (8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari angka 28, yang merupakan proses langsung dalam mengenali struktur bilangan dua digit.. Bukti: 28 = puluhan + satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar bilangan.. Bukti: 28 = puluhan + satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang nilai tempat untuk bilangan dua digit yang umum diajarkan di kelas 2.. Bukti: 28 = puluhan + satuan

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
| gradeRelativeRationale | Materi nilai tempat adalah kurikulum standar kelas 2 SD. Soal ini tidak memerlukan perhitungan kompleks, hanya pengenalan posisi digit. |

Run 2 — solusi: Bilangan 28 terdiri dari angka 2 di tempat puluhan (bernilai 20) dan angka 8 di tempat satuan (bernilai 8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari angka 28, yang merupakan proses langsung dalam memahami struktur bilangan dua digit.. Bukti: 28 = puluhan + satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat (place value) sebagai struktur dasar bilangan desimal.. Bukti: 28 = puluhan + satuan
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dan familiar bagi siswa kelas 2 untuk membedakan nilai puluhan dan satuan pada bilangan dua digit.. Bukti: 28 = puluhan + satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat adalah kurikulum inti kelas 2, soal ini bersifat langsung tanpa jebakan kompleks. |

Run 3 — solusi: Bilangan 28 terdiri dari 2 puluhan (20) dan 8 satuan (8). Jadi, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali dan menerapkan pemahaman dasar tentang nilai tempat (puluhan dan satuan) pada bilangan dua digit, yang merupakan proses langsung.. Bukti: 28 = puluhan + satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat dalam sistem bilangan desimal, yang merupakan konsep dasar.. Bukti: 28 = puluhan + satuan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, menggunakan representasi familiar, dan hanya memerlukan satu langkah identifikasi nilai tempat.. Bukti: 28 = puluhan + satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar nilai tempat bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD yang menekankan penguasaan konsep nilai tempat dasar. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6812b878c72c527a6bbfae1e2f2f74c2c3ac47d4da7d985b5f62bcff227ad4ff`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1534 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1559 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1532 |

Run 1 — solusi: Diketahui Kira = 34. Lili = 34 - 2 = 32. Malosi = 32 + 3 = 35. Urutan dari terkecil ke terbesar: Lili (32), Kira (34), Malosi (35).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aritmatika dasar (penjumlahan dan pengurangan) secara berurutan untuk menentukan nilai setiap anak sebelum mengurutkannya.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang hubungan antar bilangan (lebih dari/kurang dari) dan penggunaan algoritma penjumlahan/pengurangan sederhana.. Bukti: 3 lebihnya dari; 2 kurangnya dari
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah perhitungan berantai (menentukan nilai Lili, lalu Malosi) dan satu langkah pengurutan, yang sesuai untuk tingkat kelas 2.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Urutkan bilangan mereka dari nilai terkecil ke terbesar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan dua digit, konsep urutan bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena melibatkan penalaran berantai (multi-step) untuk menentukan nilai sebelum mengurutkan, namun operasi aritmatikanya masih dasar. |

Run 2 — solusi: Kira = 34. Lili = 34 - 2 = 32. Malosi = 32 + 3 = 35. Urutan terkecil ke terbesar: Lili (32), Kira (34), Malosi (35).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aritmatika dasar untuk menentukan nilai setiap anak berdasarkan hubungan yang diberikan, kemudian mengurutkan hasilnya. Ini adalah proses penerapan konsep pada situasi rutin.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Urutkan bilangan mereka dari nilai terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan hubungan antar bilangan (konsep lebih dari/kurang dari) untuk menentukan nilai yang tidak diketahui.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah deduksi logis (menentukan nilai Lili, lalu Malosi) dan satu langkah pengurutan. Ini adalah tugas rutin bagi siswa kelas 2 yang sudah memahami operasi penjumlahan/pengurangan dasar.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili.; Bilangan Lili 2 kurangnya dari bilangan Kira.; Kira memegang kartu bilangan 34.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan dua angka, pemahaman konsep urutan bilangan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena siswa harus melakukan dua operasi berurutan sebelum mengurutkan, yang merupakan tantangan standar untuk kelas 2. |

Run 3 — solusi: Kira=34. Lili=34-2=32. Malosi=32+3=35. Urutan: 32, 34, 35 (Lili, Kira, Malosi).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perbandingan dan operasi aritmatika dasar untuk menentukan nilai setiap anak, kemudian mengurutkannya. Ini melibatkan penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Bilangan Malosi 3 lebihnya dari bilangan Lili; Bilangan Lili 2 kurangnya dari bilangan Kira; Urutkan bilangan mereka dari nilai terkecil ke terbesar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar bilangan dan urutan (konseptual) serta penggunaan operasi aritmatika dasar (prosedural) untuk menemukan nilai yang tidak diketahui.. Bukti: 3 lebihnya dari; 2 kurangnya dari; Urutkan bilangan
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah logis (menghitung nilai Lili, lalu Malosi, lalu mengurutkan), yang merupakan tuntutan standar untuk kelas 2.. Bukti: Kira memegang kartu bilangan 34; Bilangan Malosi 3 lebihnya dari bilangan Lili; Bilangan Lili 2 kurangnya dari bilangan Kira

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan dua digit, konsep urutan bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan ini sesuai untuk kelas 2 karena melibatkan pemecahan masalah multi-langkah yang masih dalam lingkup operasi aritmatika dasar. |

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3065`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur aritmatika dasar secara berurutan untuk menentukan nilai yang tidak diketahui, kemudian menerapkan konsep urutan bilangan untuk menyusun jawaban akhir.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang hubungan antar bilangan (konseptual) dan penggunaan operasi aritmatika dasar (prosedural) untuk memecahkan masalah.
- Intended difficulty `Medium`: Soal memerlukan beberapa langkah deduksi logis dan perhitungan berantai, yang merupakan tantangan rutin namun memerlukan ketelitian bagi siswa kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan dua digit, konsep urutan bilangan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena melibatkan penalaran berantai (multi-step) untuk menentukan nilai sebelum mengurutkan, namun operasi aritmatikanya masih dasar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `f8b50899e6f07b82441104f3`

Perhatikan keempat bilangan berikut. 25 12 35 21<br><br>Bilangan mana yang paling besar?

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 35 |
| C | 25 |
| D | 21 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan nilai tempat puluhan dari 25 (2 puluhan), 12 (1 puluhan), 35 (3 puluhan), dan 21 (2 puluhan). Karena 3 puluhan adalah yang terbesar, maka 35 adalah bilangan terbesar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `693077b19cbf834f75f8f389dcb70bcc8651e0bfe5f841a3e7b31e004f6e6b44`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1383 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1352 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1363 |

Run 1 — solusi: Membandingkan nilai tempat puluhan dari bilangan 25 (2 puluhan), 12 (1 puluhan), 35 (3 puluhan), dan 21 (2 puluhan). Nilai 3 puluhan adalah yang terbesar, sehingga 35 adalah bilangan terbesar.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai tempat puluhan dari sekumpulan bilangan untuk menentukan mana yang terbesar. Ini adalah proses rutin dalam membandingkan bilangan.. Bukti: Bilangan mana yang paling besar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang sistem nilai tempat (puluhan dan satuan) untuk mengurutkan atau membandingkan besaran bilangan.. Bukti: 25 12 35 21
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas rutin bagi siswa kelas 2 untuk membandingkan bilangan dua digit dengan melihat nilai tempat puluhan.. Bukti: Perhatikan keempat bilangan berikut. 25 12 35 21; Bilangan mana yang paling besar?

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
| gradeRelativeRationale | Membandingkan bilangan dua digit adalah materi standar kelas 2 SD. Soal ini langsung dan tidak memerlukan langkah kompleks. |

Run 2 — solusi: Membandingkan nilai tempat puluhan dari bilangan 25 (2 puluhan), 12 (1 puluhan), 35 (3 puluhan), dan 21 (2 puluhan). Karena 3 puluhan adalah yang terbesar, maka 35 adalah bilangan terbesar.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perbandingan nilai tempat (puluhan) untuk menentukan bilangan terbesar di antara sekumpulan bilangan yang diberikan.. Bukti: Bilangan mana yang paling besar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang sistem nilai tempat (puluhan dan satuan) sebagai prinsip dasar dalam membandingkan bilangan.. Bukti: 25 12 35 21
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan perbandingan langsung nilai tempat puluhan pada empat bilangan dua digit yang familiar bagi siswa kelas 2.. Bukti: 25 12 35 21; Bilangan mana yang paling besar?

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
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan membandingkan bilangan dua digit dengan melihat nilai puluhannya. Soal ini adalah latihan rutin yang sesuai dengan kurikulum. |

Run 3 — solusi: Membandingkan nilai tempat puluhan dari bilangan 25 (2 puluhan), 12 (1 puluhan), 35 (3 puluhan), dan 21 (2 puluhan). Karena 3 > 2 dan 3 > 1, maka 35 adalah bilangan terbesar.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membandingkan sekumpulan bilangan dua angka dan menentukan nilai maksimum, yang merupakan proses langsung dalam domain knowing.. Bukti: Bilangan mana yang paling besar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang nilai tempat (puluhan dan satuan) sebagai prinsip dasar untuk membandingkan bilangan.. Bukti: 25 12 35 21
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan perbandingan langsung nilai tempat puluhan tanpa langkah tambahan yang kompleks.. Bukti: 25 12 35 21; Bilangan mana yang paling besar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua angka (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan dua angka adalah standar kompetensi dasar kelas 2 yang rutin dilakukan. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2682`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur perbandingan nilai tempat (puluhan) untuk menentukan bilangan terbesar di antara sekumpulan bilangan yang diberikan. Ini adalah tugas rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang sistem nilai tempat (puluhan dan satuan) sebagai prinsip dasar untuk membandingkan besaran bilangan.
- Intended difficulty `Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan perbandingan langsung nilai tempat puluhan tanpa langkah tambahan yang kompleks.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Membandingkan bilangan dua digit adalah materi standar kelas 2 SD. Soal ini langsung dan tidak memerlukan langkah kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `76bd2315ce21573dfa2ea8d7`

Perhatikan bilangan berikut. 13 11 18<br><br>Urutan mulai dari bilangan terkecil: .... , .... , ....

| Opsi | Isi |
|---|---|
| A | 18, 13, 11 |
| B | 11, 13, 18 |
| C | 13, 11, 18 |
| D | 11, 18, 13 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan nilai satuan dari bilangan 11, 13, dan 18 karena nilai puluhannya sama (1). Urutan dari terkecil adalah 11, 13, 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ce7c64b1a0d4378e6b5f5dc31f9cfc78555f3619798859e7fa4f04d256111bdd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1443 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1400 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1438 |

Run 1 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 (1 puluhan, 1 satuan), 13 (1 puluhan, 3 satuan), 18 (1 puluhan, 8 satuan). Urutan dari terkecil adalah 11, 13, 18.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan proses langsung mengurutkan bilangan yang diberikan berdasarkan nilai tempat, yang merupakan prosedur rutin.. Bukti: Urutan mulai dari bilangan terkecil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang urutan bilangan (prosedural) dan perbandingan nilai bilangan (konseptual), namun fokus utamanya adalah eksekusi urutan.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan bilangan dua digit yang familiar dan prosedur pengurutan langsung tanpa jebakan kompleks.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua digit dan konsep lebih kecil/lebih besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua digit adalah standar kompetensi dasar kelas 2 SD. |

Run 2 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 < 13 < 18. Urutan dari terkecil adalah 11, 13, 18.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan proses langsung yaitu mengurutkan tiga bilangan dua digit yang diberikan berdasarkan nilai besarnya.. Bukti: Urutan mulai dari bilangan terkecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep urutan bilangan (magnitude) yang merupakan pengetahuan konseptual dasar.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya melibatkan tiga bilangan dua digit, dan tidak memerlukan strategi kompleks.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan cacah sampai 20 dan konsep perbandingan lebih besar/kecil. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena mengurutkan bilangan dua digit adalah kompetensi dasar yang sudah diajarkan. |

Run 3 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 (puluhan 1, satuan 1), 13 (puluhan 1, satuan 3), 18 (puluhan 1, satuan 8). Urutan dari terkecil: 11, 13, 18.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan proses langsung mengurutkan bilangan berdasarkan nilai tempat, yang merupakan prosedur rutin.. Bukti: Urutan mulai dari bilangan terkecil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengurutkan bilangan cacah dua angka.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan bilangan dua digit yang familiar dan prosedur pengurutan langsung tanpa jebakan kompleks.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan cacah sampai 20 dan konsep perbandingan lebih kecil/besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua digit adalah kompetensi standar kelas 2 awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2694`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan proses langsung mengurutkan bilangan berdasarkan nilai tempat, yang merupakan prosedur rutin tanpa perlu strategi nonrutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji penerapan algoritma atau urutan langkah untuk mengurutkan bilangan cacah, yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan bilangan dua digit yang familiar dan prosedur pengurutan langsung tanpa jebakan kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua digit dan konsep perbandingan lebih kecil/lebih besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua digit adalah standar kompetensi dasar kelas 2 SD. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `5bde2df393a963ef6574cd85`

Hitunglah operasi penjumlahan berikut dengan menghitung maju.<br><br>11 + 9 = .…

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 19 |
| C | 21 |
| D | 20 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung maju 9 langkah dari 11: 12, 13, 14, 15, 16, 17, 18, 19, 20.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d61997e6473ec722fdcfc0b4c0fa088be29e038dcb9de958234e8a8886516848`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1312 |
| 2 | success | valid / verified | applying | procedural | Easy | 1309 |
| 3 | success | valid / verified | applying | procedural | Easy | 1297 |

Run 1 — solusi: Menghitung maju 9 langkah dari 11: 12, 13, 14, 15, 16, 17, 18, 19, 20.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan spesifik (menghitung maju) yang merupakan teknik rutin untuk operasi dasar.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma atau teknik menghitung maju untuk menyelesaikan penjumlahan.. Bukti: 11 + 9 = .…
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar penjumlahan satu digit dengan bilangan dua digit yang familiar bagi siswa kelas 2.. Bukti: 11 + 9; menghitung maju

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan hingga 20 dan konsep penjumlahan sebagai penambahan nilai. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 11+9 adalah standar kurikulum kelas 2, menggunakan strategi menghitung maju yang diajarkan secara eksplisit. |

Run 2 — solusi: Menghitung maju 9 langkah dari 11: 12, 13, 14, 15, 16, 17, 18, 19, 20.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur menghitung maju yang sudah dipelajari untuk menyelesaikan operasi penjumlahan dasar.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik menghitung maju sebagai prosedur penjumlahan.. Bukti: 11 + 9 = .…
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar penjumlahan satu digit dengan bilangan dua digit yang familiar bagi siswa kelas 2.. Bukti: 11 + 9 = .…

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung urutan bilangan (counting on) hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 11+9 adalah standar kurikulum kelas 2, menggunakan strategi menghitung maju yang diajarkan di tingkat awal. |

Run 3 — solusi: Menghitung maju 9 langkah dari 11: 12, 13, 14, 15, 16, 17, 18, 19, 20.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur menghitung maju yang sudah dipelajari untuk menyelesaikan operasi penjumlahan dasar.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menerapkan algoritma atau teknik menghitung maju untuk mendapatkan hasil penjumlahan.. Bukti: 11 + 9 = .…
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang diajarkan di kelas 2. Langkah-langkahnya rutin dan langsung, dengan beban kognitif yang rendah.. Bukti: 11 + 9 = .…; menghitung maju

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan berhitung urutan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dasar dengan teknik menghitung maju adalah materi inti kelas 2 yang bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `dee5237101a9a4d500e44455`

Hitunglah operasi penjumlahan berikut dengan menghitung maju.<br><br>10 + 7 = ....

| Opsi | Isi |
|---|---|
| A | 17 |
| B | 18 |
| C | 3 |
| D | 16 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menghitung maju dari 10 sebanyak 7 langkah: 11, 12, 13, 14, 15, 16, 17.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ee6fb3f5143bf998a9e840fd8b74dca4321da433892bfc6ca1a50d537f75a82c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1281 |
| 2 | success | valid / verified | knowing | factual | Easy | 1258 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1288 |

Run 1 — solusi: Menghitung maju dari 10 sebanyak 7 langkah: 11, 12, 13, 14, 15, 16, 17.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan dasar dengan strategi spesifik (menghitung maju), yang merupakan penerapan rutin dari konsep penjumlahan.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju; 10 + 7 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma atau teknik penjumlahan dasar (menghitung maju).. Bukti: 10 + 7 = ..
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan angka yang familiar (puluhan dan satuan), dan hanya memerlukan satu langkah prosedur penjumlahan langsung.. Bukti: 10 + 7 = ..

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan urutan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 10 dengan satuan adalah materi standar kelas 2 yang bersifat prosedural langsung. |

Run 2 — solusi: 10 + 7 = 17. Menghitung maju dari 10 sebanyak 7 langkah menghasilkan 17.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar menggunakan strategi menghitung maju yang sudah diajarkan secara langsung.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju; 10 + 7 = ..
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta penjumlahan dasar dan prosedur menghitung maju.. Bukti: 10 + 7 = ..
- Intended difficulty `classify/Easy`: Operasi penjumlahan dasar dengan bilangan 10 (puluhan) dan satuan adalah prosedur yang sangat familiar dan rutin bagi siswa kelas 2.. Bukti: 10 + 7 = ..

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
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 10 dengan satuan adalah materi dasar kelas 2 yang bersifat rutin dan tidak memerlukan strategi kompleks. |

Run 3 — solusi: 10 ditambah 7 dengan menghitung maju dari 10 adalah 11, 12, 13, 14, 15, 16, 17. Hasilnya adalah 17.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar menggunakan strategi menghitung maju yang merupakan prosedur rutin.. Bukti: Hitunglah operasi penjumlahan berikut dengan menghitung maju. 10 + 7 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan dasar dan fakta penjumlahan.. Bukti: 10 + 7 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan operasi penjumlahan satu digit dengan sepuluh yang merupakan prosedur familiar bagi siswa kelas 2.. Bukti: 10 + 7 = ....

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
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 10 dengan bilangan satu digit adalah materi standar kelas 2 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2513`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta siswa melakukan prosedur penjumlahan dasar dengan strategi spesifik (menghitung maju). Ini adalah penerapan rutin dari konsep penjumlahan yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau teknik penjumlahan dasar (menghitung maju), yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini sangat mendasar, menggunakan angka yang familiar (puluhan dan satuan), dan hanya memerlukan satu langkah prosedur penjumlahan langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan urutan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 10 dengan satuan adalah materi standar kelas 2 yang bersifat prosedural langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `c9d5c58f9bea9fbc5724dae7`

Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan.<br><br>17 – 12 = ....

| Opsi | Isi |
|---|---|
| A | 29 |
| B | 6 |
| C | 5 |
| D | 4 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 17 = 10 + 7; 12 = 10 + 2; (10 - 10) + (7 - 2) = 0 + 5 = 5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `85de4cd9f9f3e204e0b6936498b0cc3d6916e172daaa6452ac2ec2c629451c18`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1393 |
| 2 | success | valid / verified | applying | procedural | Easy | 1412 |
| 3 | success | valid / verified | applying | procedural | Easy | 1396 |

Run 1 — solusi: 17 = 10 + 7; 12 = 10 + 2; (10 - 10) + (7 - 2) = 0 + 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur dekomposisi bilangan (pasangan bilangan) untuk menyelesaikan pengurangan, yang merupakan penerapan prosedur rutin pada kelas 2.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan; 17 – 12 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang teknik atau algoritma dekomposisi bilangan (pasangan bilangan) untuk melakukan pengurangan.. Bukti: menggunakan pasangan bilangan
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur pengurangan dasar dengan dekomposisi yang familiar bagi siswa kelas 2, dengan beban kognitif rendah.. Bukti: 17 – 12 = ....

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
| gradeRelativeRationale | Pengurangan bilangan dua digit dengan dekomposisi adalah materi standar kelas 2 yang bersifat rutin. |

Run 2 — solusi: 17 - 12 = (10 + 7) - (10 + 2) = (10 - 10) + (7 - 2) = 0 + 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan dengan metode dekomposisi (pasangan bilangan) yang telah dipelajari, yang merupakan penerapan rutin dari konsep nilai tempat.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan.; 17 – 12 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma pengurangan berbasis nilai tempat (dekomposisi bilangan menjadi puluhan dan satuan).. Bukti: menggunakan pasangan bilangan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan operasi dasar dengan angka di bawah 20 tanpa teknik meminjam yang kompleks jika menggunakan metode pasangan bilangan.. Bukti: 17 – 12 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 yang menekankan strategi pengurangan selain algoritma standar, seperti dekomposisi. |

Run 3 — solusi: 17 = 10 + 7; 12 = 10 + 2. (10 - 10) + (7 - 2) = 0 + 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan dengan metode dekomposisi (pasangan bilangan) yang telah dipelajari, bukan sekadar mengingat fakta dasar.. Bukti: Hitunglah operasi pengurangan berikut menggunakan pasangan bilangan; 17 – 12 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma pengurangan berbasis nilai tempat (dekomposisi bilangan).. Bukti: menggunakan pasangan bilangan; 17 adalah 10 dan 7; 12 adalah 10 dan 2
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar kelas 2 yang familiar, melibatkan satu operasi utama dengan angka kecil, sehingga beban kognitifnya rendah.. Bukti: 17 – 12 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 yang menekankan strategi pengurangan dengan dekomposisi bilangan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `2e68e85a51ce02c29adaaa88`

Hitunglah operasi pengurangan berikut dengan menghitung mundur.<br><br>15 – 4 = ....

| Opsi | Isi |
|---|---|
| A | 11 |
| B | 10 |
| C | 19 |
| D | 12 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menghitung mundur 4 langkah dari 15: 14, 13, 12, 11.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6832c2edca614e32e4ffabc45911b768873265f85c5ba65b66b7bab1df93834f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1295 |
| 2 | success | valid / verified | applying | procedural | Easy | 1284 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1274 |

Run 1 — solusi: Menghitung mundur 4 langkah dari 15: 14, 13, 12, 11.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan spesifik (menghitung mundur) yang merupakan prosedur rutin di kelas 2.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur; 15 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma atau teknik pengurangan melalui metode menghitung mundur.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi pengurangan dasar satu digit dengan angka di bawah 20, yang merupakan standar kompetensi kelas 2.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 15 sebanyak 4 langkah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dasar dalam rentang 20 adalah materi inti kelas 2 yang bersifat rutin. |

Run 2 — solusi: Menghitung mundur 4 langkah dari 15: 14 (1), 13 (2), 12 (3), 11 (4). Hasilnya adalah 11.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan spesifik (menghitung mundur) yang sudah dipelajari di kelas 2.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur; 15 – 4 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan melalui metode menghitung mundur.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur dasar pengurangan satu digit dari dua digit yang sangat familiar bagi siswa kelas 2.. Bukti: 15 – 4 = ..

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dasar dalam rentang 20 adalah standar kompetensi kelas 2 yang bersifat rutin. |

Run 3 — solusi: Menghitung mundur 4 langkah dari 15: 14, 13, 12, 11.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan prosedur pengurangan dasar menggunakan strategi spesifik (menghitung mundur) yang sudah diajarkan di kelas 2.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur; 15 – 4 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penerapan algoritma atau teknik menghitung mundur untuk menyelesaikan operasi pengurangan.. Bukti: Hitunglah operasi pengurangan berikut dengan menghitung mundur
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar satu langkah yang sangat familiar bagi siswa kelas 2, dengan beban kognitif yang rendah.. Bukti: 15 – 4 = ..

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
| gradeRelativeRationale | Operasi pengurangan dasar dalam rentang 20 adalah materi standar kelas 2 yang bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2472`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pengurangan spesifik (menghitung mundur) yang merupakan prosedur rutin di kelas 2.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau teknik pengurangan melalui metode menghitung mundur.
- Intended difficulty `Easy`: Soal ini melibatkan operasi pengurangan dasar satu digit dengan angka di bawah 20, yang merupakan standar kompetensi kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 15 sebanyak 4 langkah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dasar dalam rentang 20 adalah materi inti kelas 2 yang bersifat rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5dd8f8fb6b3be35853d640aac5e085b1ae92a0e9cba2334bdac56130ab11adb3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 1487 |
| 2 | success | valid / verified | applying | procedural | Medium | 1516 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1491 |

Run 1 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi implisit (jumlah kuning) lalu menerapkan operasi penjumlahan berantai, yang termasuk dalam kategori applying.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman hubungan antar kuantitas (konseptual) dan penerapan algoritma penjumlahan (prosedural). Fokus utama adalah memahami struktur hubungan 'lebih dari' untuk menentukan nilai yang hilang.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah; Berapa jumlah semua kupu-kupu?
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua tahap operasi: menentukan nilai variabel yang tidak diketahui (kuning) dan menjumlahkan tiga variabel. Ini adalah standar untuk kelas 2.. Bukti: Ada 5 kupu-kupu merah; Ada 6 kupu-kupu hijau; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu melakukan operasi penjumlahan bertahap dan memahami hubungan kuantitas sederhana dalam soal cerita. |

Run 2 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang diberikan, melakukan operasi penjumlahan sederhana untuk menentukan jumlah kupu-kupu kuning, lalu menjumlahkan ketiga kelompok kupu-kupu tersebut. Ini adalah penerapan prosedur rutin dalam konteks soal cerita.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep penjumlahan dan hubungan antar kuantitas (lebih dari) yang diselesaikan dengan algoritma penjumlahan dasar.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (menentukan nilai kuning, lalu menjumlahkan ketiganya) yang sesuai untuk tingkat kelas 2. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Ada 5 kupu-kupu merah.; Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita multi-langkah sederhana adalah standar untuk kelas 2, menuntut ketelitian dalam mengolah informasi yang diberikan secara bertahap. |

Run 3 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi hubungan antar variabel (kuning = merah + 2) dan menerapkan prosedur penjumlahan berantai untuk menyelesaikan masalah rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini memerlukan pemahaman konsep penjumlahan dan hubungan antar kuantitas (lebih dari) untuk menentukan nilai yang belum diketahui sebelum menjumlahkan.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah; Berapa jumlah semua kupu-kupu?
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (menentukan nilai kuning, lalu menjumlahkan ketiganya) yang sesuai untuk tingkat kelas 2.. Bukti: 5 kupu-kupu merah; 6 kupu-kupu hijau; kuning 2 lebihnya dari banyak kupu-kupu merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan sesuai untuk kelas 2 karena memerlukan dua langkah operasi (menentukan nilai kuning lalu total) yang masih dalam lingkup operasi dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3003`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur penjumlahan setelah menentukan nilai variabel yang tidak diketahui secara eksplisit (kuning). Ini adalah penerapan konsep penjumlahan dalam konteks soal cerita rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menuntut pemahaman hubungan antar kuantitas (konseptual) untuk menentukan nilai yang hilang sebelum melakukan operasi penjumlahan (prosedural).
- Intended difficulty `Medium`: Soal ini memerlukan dua langkah rutin: menentukan nilai variabel kuning dan menjumlahkan tiga kelompok. Ini sesuai dengan ekspektasi kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu melakukan operasi penjumlahan bertahap dan memahami hubungan kuantitas sederhana dalam soal cerita. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `c0bf29e80c730eba9378deaf`

Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.<br><br>Berapa banyak kupu-kupu kuning?

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 3 |
| C | 8 |
| D | 6 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Kupu-kupu kuning = Kupu-kupu merah + 2 = 5 + 2 = 7.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `902fdb5b759a7723fc29ed1c84d267b0afd97206590f50dfad3b1a75812f887b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1305 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1329 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1339 |

Run 1 — solusi: Kupu-kupu kuning = Kupu-kupu merah + 2 = 5 + 2 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep penjumlahan dasar untuk menyelesaikan masalah rutin yang diberikan dalam bentuk cerita sederhana.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep penjumlahan sebagai penambahan nilai (lebih dari) pada kuantitas yang diketahui.. Bukti: 5 kupu-kupu merah; 2 lebihnya
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang melibatkan operasi penjumlahan dasar dengan informasi yang jelas.. Bukti: Ada 5 kupu-kupu merah.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya melibatkan satu operasi penjumlahan sederhana dengan angka kecil. |

Run 2 — solusi: Kupu-kupu kuning = kupu-kupu merah + 2 = 5 + 2 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan kalimat '2 lebihnya dari' menjadi operasi penjumlahan sederhana (5 + 2). Ini adalah penerapan prosedur rutin pada situasi soal cerita.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep penjumlahan sebagai penambahan kuantitas ('lebihnya dari') yang merupakan pengetahuan konseptual dasar.. Bukti: 5 kupu-kupu merah; 2 lebihnya
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah operasi penjumlahan sederhana yang sesuai untuk tingkat kelas 2.. Bukti: Ada 5 kupu-kupu merah; 2 lebihnya dari banyak kupu-kupu merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan membaca soal cerita sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita satu langkah dengan operasi penjumlahan dasar adalah standar kompetensi kelas 2. |

Run 3 — solusi: Kupu-kupu kuning = kupu-kupu merah + 2 = 5 + 2 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan kalimat '2 lebihnya dari' menjadi operasi penjumlahan sederhana (5 + 2). Ini adalah proses penerapan konsep penjumlahan dasar pada situasi rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep penjumlahan sebagai penambahan nilai (lebihnya dari) terhadap suatu kuantitas yang diketahui.. Bukti: Ada 5 kupu-kupu merah; 2 lebihnya dari
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur satu langkah yang sangat rutin untuk siswa kelas 2, dengan beban kognitif rendah.. Bukti: Ada 5 kupu-kupu merah; 2 lebihnya dari

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan membaca kalimat matematika sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 5+2 adalah standar kompetensi kelas 2 yang sangat mendasar dan familiar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `54e65cf97cc65f3ef126daef`

Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.<br><br>Berapakah sisa bolu kukus Ibu sekarang?

| Opsi | Isi |
|---|---|
| A | 11 |
| B | 12 |
| C | 15 |
| D | 10 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 13 - 2 = 11
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1b0995a8c7f302ab560760d1cdb60521432252a4ab2ac7797d0cdb8e83a29b5d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1323 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1309 |
| 3 | success | valid / verified | applying | procedural | Easy | 1286 |

Run 1 — solusi: 13 - 2 = 11
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi pengurangan dasar yang merupakan prosedur rutin untuk menyelesaikan masalah kontekstual sederhana.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma pengurangan dasar (prosedural) dalam konteks cerita.. Bukti: 13 bolu kukus; memakan 2 bolu kukus
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi pengurangan satu digit dari bilangan dua digit yang familiar bagi siswa kelas 2, dengan satu langkah penyelesaian langsung.. Bukti: 13 bolu kukus; memakan 2 bolu kukus

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
| gradeRelativeRationale | Operasi pengurangan 13-2 adalah standar kompetensi kelas 2 yang bersifat langsung dan rutin. |

Run 2 — solusi: 13 - 2 = 11
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar secara langsung untuk menyelesaikan masalah kontekstual sederhana.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi pengurangan bilangan cacah.. Bukti: 13 bolu kukus; memakan 2 bolu kukus
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah pengurangan satu langkah yang sangat rutin dan familiar bagi siswa kelas 2.. Bukti: 13 bolu kukus; memakan 2 bolu kukus

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dalam lingkup 20 adalah standar kompetensi kelas 2 yang bersifat rutin. |

Run 3 — solusi: 13 - 2 = 11
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar pada konteks cerita sederhana yang sudah familiar.. Bukti: Ibu membeli 13 bolu kukus; Malosi memakan 2 bolu kukus; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma pengurangan dasar.. Bukti: 13 - 2 = 11
- Intended difficulty `classify/Easy`: Soal ini menggunakan operasi pengurangan satu digit dari bilangan belasan yang merupakan prosedur standar kelas 2.. Bukti: 13 bolu kukus; memakan 2; sisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dalam lingkup 20 adalah kompetensi dasar kelas 2 yang bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2496`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan operasi pengurangan dasar pada konteks cerita sederhana yang sudah familiar, yang merupakan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman siswa terhadap algoritma pengurangan dasar (prosedural) dalam konteks cerita.
- Intended difficulty `Easy`: Soal ini merupakan masalah pengurangan satu langkah yang sangat rutin dan familiar bagi siswa kelas 2, dengan beban kognitif yang rendah.

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
| gradeRelativeRationale | Operasi pengurangan 13-2 adalah standar kompetensi kelas 2 yang bersifat langsung dan rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `c1065f5b900e24e5013bfcc9`

Tulislah nama bangun datar berikut.

| Opsi | Isi |
|---|---|
| A | Segitiga |
| B | Segi empat |
| C | Lingkaran |
| D | Segi lima |

![Gambar sumber soal 15](<../images/kelas2_panduan_siswa_kelas2.pdf-0089-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bangun tersebut memiliki 3 sisi lurus dan 3 sudut, yang merupakan definisi dari segitiga.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0089-03.png. Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna merah muda berbentuk segitiga dengan tiga sisi lurus dan tiga sudut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `271058b9e489d4a0d4187634516e0c521b35972c224354585bbfdd1e9f22b854`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2375 |
| 2 | success | valid / verified | knowing | factual | Easy | 2401 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2398 |

Run 1 — solusi: Bangun tersebut memiliki 3 sisi lurus dan 3 sudut, yang merupakan definisi dari segitiga.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menamai bangun datar berdasarkan karakteristik visualnya yang sangat mendasar, yang merupakan proses pengenalan langsung.. Bukti: Tulislah nama bangun datar berikut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi atau kategori bangun datar (segitiga) untuk dapat menjawab soal ini.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pengenalan bentuk geometris standar tanpa kompleksitas tambahan.. Bukti: Tulislah nama bangun datar berikut.

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
| distractorQuality | plausible |
| gradeRelativeRationale | Pengenalan bangun datar sederhana adalah materi standar kelas 2 SD yang bersifat rutin. |

Run 2 — solusi: Bangun tersebut memiliki 3 sisi lurus dan 3 sudut, yang merupakan ciri khas dari segitiga.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun datar berdasarkan ciri visual yang sangat dasar (jumlah sisi).. Bukti: Tulislah nama bangun datar berikut.; bangun dibatasi oleh 3 sisi garis lurus
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun datar dasar.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, hanya memerlukan pengenalan visual langsung tanpa proses perhitungan atau strategi kompleks.. Bukti: Tulislah nama bangun datar berikut.; bangun dibatasi oleh 3 sisi garis lurus

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk geometri dasar (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan untuk mengidentifikasi bangun datar sederhana berdasarkan jumlah sisi. |

Run 3 — solusi: Bangun tersebut memiliki 3 sisi lurus, sehingga disebut segitiga.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menamai bangun datar berdasarkan karakteristik visualnya yang sangat mendasar.. Bukti: Tulislah nama bangun datar berikut.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan kategori bangun datar (segitiga) untuk menjawab soal ini.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pengenalan bentuk geometris standar tanpa langkah tambahan.. Bukti: Tulislah nama bangun datar berikut.

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
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD yang menekankan pengenalan bangun datar sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3496`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengenali dan menamai bangun datar berdasarkan karakteristik visualnya yang sangat mendasar, yang merupakan proses pengenalan langsung (knowing).
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami kategori atau konsep bentuk geometri (segitiga) untuk dapat mengklasifikasikan gambar tersebut.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pengenalan bentuk geometris standar tanpa kompleksitas tambahan.

Profil difficulty hasil adjudikasi:

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
| distractorQuality | plausible |
| gradeRelativeRationale | Pengenalan bangun datar sederhana adalah materi standar kelas 2 SD yang bersifat rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 72/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999815; applying=0.000185; reasoning=0.000000 | knowing | 0.999815 | 0.001614 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.865225; conceptual=0.130241; procedural=0.004534; metacognitive=0.000000 | factual | 0.865225 | 0.299505 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.913601; Medium=0.082891; Hard=0.003508 | Easy | 0.913601 | 0.281083 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999815; −Σp ln(p) = 0.001774; H = 0.001774/ln(3) = 0.001614; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.865225; −Σp ln(p) = 0.415202; H = 0.415202/ln(4) = 0.299505; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.913601; −Σp ln(p) = 0.308801; H = 0.308801/ln(3) = 0.281083; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna merah muda berbentuk segitiga dengan tiga sisi lurus dan tiga sudut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `13edcfffbf7fe9b6f346ad87`

Tulislah nama bangun datar berikut.

| Opsi | Isi |
|---|---|
| A | Segi lima |
| B | Lingkaran |
| C | Segi enam |
| D | Segitiga |

![Gambar sumber soal 16](<../images/kelas2_panduan_siswa_kelas2.pdf-0089-06.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bangun datar tersebut memiliki satu sisi lengkung yang tertutup dan tidak memiliki sudut, yang merupakan definisi dari lingkaran.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0089-06.png. Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna ungu berbentuk lingkaran sempurna.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `debb60be99d15dc7ca183eeec496783d24bacdc371a63ed1ca5b96455e0892ff`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2413 |
| 2 | success | valid / verified | knowing | factual | Easy | 2415 |
| 3 | success | valid / verified | knowing | factual | Easy | 2393 |

Run 1 — solusi: Bangun datar tersebut memiliki satu sisi lengkung yang tertutup dan tidak memiliki sudut, yang merupakan definisi dari lingkaran.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan mengidentifikasi bentuk visual dasar (lingkaran) berdasarkan pengetahuan yang sudah dipelajari sebelumnya.. Bukti: Tulislah nama bangun datar berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun datar dasar.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual langsung tanpa proses perhitungan atau analisis kompleks.. Bukti: Tulislah nama bangun datar berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama-nama bangun datar dasar (lingkaran, segitiga, segiempat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 2, mengidentifikasi bentuk lingkaran adalah materi dasar yang sangat familiar dan rutin. |

Run 2 — solusi: Bangun datar tersebut memiliki satu sisi lengkung yang tertutup dan tidak memiliki sudut, yang merupakan definisi dari lingkaran.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan mengidentifikasi bentuk visual dasar berdasarkan pengetahuan faktual tentang nama-nama bangun datar.. Bukti: Tulislah nama bangun datar berikut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang terminologi dasar geometri (nama bentuk).. Bukti: nama bangun datar
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual langsung tanpa proses perhitungan atau strategi kompleks.. Bukti: Tulislah nama bangun datar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama-nama bangun datar dasar (lingkaran, segitiga, segiempat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan sudah sangat familiar dengan pengenalan bentuk dasar seperti lingkaran sebagai bagian dari kurikulum awal geometri. |

Run 3 — solusi: Gambar tersebut adalah lingkaran karena memiliki satu sisi lengkung tertutup tanpa sudut.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menamai bentuk geometris dasar yang disajikan secara visual.. Bukti: Tulislah nama bangun datar berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun datar dasar.. Bukti: Tulislah nama bangun datar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual langsung terhadap bentuk yang sangat familiar bagi siswa kelas 2.. Bukti: Tulislah nama bangun datar berikut.

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
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena pengenalan bentuk adalah materi awal geometri yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999998; applying=0.000002; reasoning=0.000000 | knowing | 0.999998 | 0.000020 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.787466; conceptual=0.207740; procedural=0.004794; metacognitive=0.000000 | factual | 0.787466 | 0.389680 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.915183; Medium=0.081872; Hard=0.002946 | Easy | 0.915183 | 0.275959 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999998; −Σp ln(p) = 0.000022; H = 0.000022/ln(3) = 0.000020; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.787466; −Σp ln(p) = 0.540211; H = 0.540211/ln(4) = 0.389680; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.915183; −Σp ln(p) = 0.303172; H = 0.303172/ln(3) = 0.275959; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna ungu berbentuk lingkaran sempurna.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `7b1097bedb274e0d05e2f483`

Susun bangun datar berikut menjadi satu bentuk. Bentuk apa hasil susunannya?

| Opsi | Isi |
|---|---|
| A | Berbentuk seperti anak panah dua arah (kiri dan kanan) |
| B | Berbentuk persegi (kotak) |
| C | Berbentuk seperti anak panah tunggal menghadap kiri |
| D | Berbentuk seperti tangga (undakan) |

![Gambar sumber soal 17](<../images/kelas2_panduan_siswa_kelas2.pdf-0097-12.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menempelkan sisi tegak segitiga ke sisi kanan persegi panjang menghasilkan bentuk anak panah yang menunjuk ke kanan. Opsi C adalah satu-satunya yang mendeskripsikan bentuk gabungan tersebut, meskipun terdapat sedikit ketidaksesuaian arah (kanan vs kiri) pada teks opsi, secara visual ini adalah jawaban yang dimaksud.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0097-12.png. Transkripsi visual: Terdapat dua bangun datar: sebuah persegi panjang di sebelah kiri dan sebuah segitiga sama sisi di sebelah kanan. Jika segitiga ditempelkan pada sisi kanan persegi panjang, akan terbentuk bangun menyerupai anak panah yang menunjuk ke arah kanan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fc48baa0fdc25162e8b937ba315cdf0fa7e28cb91cc55217b77372ad31ae8673`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2503 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2500 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2471 |

Run 1 — solusi: Menempelkan sisi tegak segitiga ke sisi kanan persegi panjang menghasilkan bentuk anak panah yang menunjuk ke kanan. Opsi C adalah satu-satunya yang mendeskripsikan bentuk gabungan tersebut, meskipun terdapat sedikit ketidaksesuaian arah (kanan vs kiri) pada teks opsi, secara visual ini adalah jawaban yang dimaksud.
- Domain kognitif `classify/applying`: Siswa perlu melakukan visualisasi mental untuk menggabungkan dua bangun datar sederhana menjadi satu bentuk baru. Ini melibatkan proses applying karena siswa harus menerapkan konsep komposisi bangun datar.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar bangun datar dan bagaimana mereka membentuk struktur yang lebih kompleks (konsep komposisi).. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan dua bangun dasar yang familiar dan satu langkah penggabungan visual yang sederhana.. Bukti: Susun bangun datar berikut menjadi satu bentuk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (persegi panjang dan segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD yang sedang mempelajari komposisi bangun datar sederhana melalui visualisasi. |

Run 2 — solusi: Menempelkan sisi tegak segitiga ke sisi kanan persegi panjang menghasilkan bentuk anak panah yang menunjuk ke kanan. Opsi C adalah yang paling mendekati deskripsi visual, meskipun terdapat ketidaksesuaian arah (soal menyebutkan menghadap kiri, visual menunjukkan arah kanan). Namun, secara struktural, C adalah jawaban yang benar.
- Domain kognitif `classify/applying`: Siswa perlu melakukan visualisasi mental untuk menggabungkan dua bangun datar menjadi satu bentuk baru, yang merupakan proses applying konsep geometri dasar.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang bagaimana bentuk-bentuk sederhana dapat dikomposisikan menjadi bentuk yang lebih kompleks.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Tugas ini melibatkan manipulasi mental sederhana pada bentuk geometris yang familiar bagi siswa kelas 2.. Bukti: Susun bangun datar berikut menjadi satu bentuk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (persegi panjang dan segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan untuk mengomposisi bangun datar sederhana. Tugas ini bersifat rutin dan tidak memerlukan strategi kompleks. |

Run 3 — solusi: Menempelkan sisi tegak segitiga ke sisi kanan persegi panjang menghasilkan bentuk anak panah yang menunjuk ke arah kanan.
- Domain kognitif `classify/applying`: Siswa perlu melakukan visualisasi mental untuk menggabungkan dua bangun datar sederhana menjadi bentuk baru, yang merupakan proses menerapkan pemahaman konsep geometri dasar.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar bangun datar dan bagaimana mereka dapat dikomposisikan menjadi bentuk yang lebih kompleks.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Tugas ini melibatkan manipulasi visual sederhana yang sesuai untuk kelas 2, di mana siswa diharapkan mampu mengenali hasil komposisi dari dua bentuk dasar yang familiar.. Bukti: Susun bangun datar berikut menjadi satu bentuk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (persegi panjang dan segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sedang dalam tahap pengembangan kemampuan spasial dasar; menggabungkan dua bentuk sederhana adalah tugas rutin dalam kurikulum geometri awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 129/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.044741; applying=0.955259; reasoning=0.000000 | applying | 0.955259 | 0.166328 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.296988; conceptual=0.690746; procedural=0.012265; metacognitive=0.000000 | conceptual | 0.690746 | 0.483379 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.827247; Medium=0.169471; Hard=0.003282 | Easy | 0.827247 | 0.433715 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.955259; −Σp ln(p) = 0.182730; H = 0.182730/ln(3) = 0.166328; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.690746; −Σp ln(p) = 0.670105; H = 0.670105/ln(4) = 0.483379; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.827247; −Σp ln(p) = 0.476485; H = 0.476485/ln(3) = 0.433715; T = 0.953328.


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
C. Berbentuk seperti anak panah tunggal menghadap kiri
D. Berbentuk seperti tangga (undakan)
Transkripsi visual: Terdapat dua bangun datar: sebuah persegi panjang di sebelah kiri dan sebuah segitiga sama sisi di sebelah kanan. Jika segitiga ditempelkan pada sisi kanan persegi panjang, akan terbentuk bangun menyerupai anak panah yang menunjuk ke arah kanan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `2188dcf71c96bfe0666fa262`

Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?

| Opsi | Isi |
|---|---|
| A | Menjadi 2 persegi sama besar |
| B | Menjadi 2 segitiga dan 1 persegi panjang |
| C | Menjadi 2 persegi panjang berbeda ukuran |
| D | Menjadi 2 segitiga |

![Gambar sumber soal 18](<../images/kelas2_panduan_siswa_kelas2.pdf-0098-09.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bangun huruf T dapat dipotong secara horizontal tepat di bawah batang mendatar, menghasilkan satu persegi panjang horizontal (batang atas) dan satu persegi panjang vertikal (batang bawah) dengan ukuran yang berbeda.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0098-09.png. Transkripsi visual: Gambar menunjukkan sebuah bangun datar berbentuk huruf T kapital yang simetris secara vertikal. Bangun ini dapat diurai menjadi dua bagian persegi panjang: satu persegi panjang horizontal di bagian atas dan satu persegi panjang vertikal di bagian bawah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5297e93513abbd45e18ed3eb6d1bd3cb8e29b0c946401f54bf168002de05bebc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2502 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2508 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2513 |

Run 1 — solusi: Bangun huruf T dapat dipotong secara horizontal tepat di bawah batang mendatar, menghasilkan satu persegi panjang horizontal (batang atas) dan satu persegi panjang vertikal (batang bawah) dengan ukuran yang berbeda.
- Domain kognitif `classify/applying`: Siswa perlu melakukan dekomposisi visual pada bangun komposit menjadi bangun dasar (persegi panjang), yang merupakan proses penerapan konsep geometri dasar.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar bangun datar dan bagaimana bangun kompleks disusun dari bangun-bangun sederhana (konsep dekomposisi).. Bukti: Mengurai dan Menyusun Bangun Datar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan pengenalan visual langsung terhadap bentuk dasar (persegi panjang) yang membentuk bangun komposit sederhana (huruf T).. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar persegi panjang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan untuk mengidentifikasi dan mengurai bangun datar sederhana menjadi bentuk-bentuk yang lebih dasar. |

Run 2 — solusi: Bangun huruf T dapat dipotong secara horizontal tepat di bawah batang mendatar, menghasilkan satu persegi panjang horizontal (batang atas) dan satu persegi panjang vertikal (batang bawah) dengan ukuran yang berbeda.
- Domain kognitif `classify/applying`: Siswa perlu melakukan dekomposisi visual pada bangun komposit menjadi bentuk-bentuk dasar (persegi panjang), yang merupakan proses penerapan konsep bangun datar pada situasi rutin.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur bangun datar dan bagaimana bangun kompleks dapat disusun atau diurai dari bangun-bangun yang lebih sederhana (konsep persegi panjang).. Bukti: Mengurai dan Menyusun Bangun Datar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan pengenalan bentuk dasar yang familiar (persegi panjang) dalam bangun komposit sederhana yang sering ditemui di kelas 2.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk persegi panjang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan untuk mengenali dan mengurai bangun datar sederhana. Tugas ini hanya memerlukan visualisasi pemotongan sederhana. |

Run 3 — solusi: Bangun huruf T dapat dipotong secara horizontal atau vertikal menjadi dua bagian persegi panjang. Pilihan C menyatakan '2 persegi panjang berbeda ukuran', yang secara visual akurat karena batang horizontal dan vertikal memiliki dimensi panjang dan lebar yang berbeda.
- Domain kognitif `classify/applying`: Siswa perlu melakukan dekomposisi visual pada bangun komposit menjadi bangun-bangun dasar (persegi panjang). Ini melibatkan penerapan konsep bentuk dasar pada situasi rutin, sehingga masuk dalam kategori applying.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur bangun datar dan bagaimana bangun kompleks dapat disusun atau diurai menjadi bentuk-bentuk dasar (persegi panjang), yang merupakan pengetahuan konseptual.. Bukti: mengurai (dipotong) menjadi beberapa bagian
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan pengenalan bentuk dasar yang familiar (persegi panjang) dalam bangun komposit sederhana yang sering ditemui di kelas 2.. Bukti: Jika bangun datar berikut diurai (dipotong) menjadi beberapa bagian, bentuk apa hasilnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar (persegi panjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Dekomposisi bangun datar sederhana adalah materi standar kelas 2. Soal ini tidak memerlukan perhitungan kompleks, hanya pengenalan visual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 123/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.096626; applying=0.903374; reasoning=0.000000 | applying | 0.903374 | 0.289096 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.425515; conceptual=0.559453; procedural=0.015032; metacognitive=0.000000 | conceptual | 0.559453 | 0.542172 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.864676; Medium=0.131924; Hard=0.003400 | Easy | 0.864676 | 0.375262 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.903374; −Σp ln(p) = 0.317605; H = 0.317605/ln(3) = 0.289096; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.559453; −Σp ln(p) = 0.751610; H = 0.751610/ln(4) = 0.542172; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.864676; −Σp ln(p) = 0.412267; H = 0.412267/ln(3) = 0.375262; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah bangun datar berbentuk huruf T kapital yang simetris secara vertikal. Bangun ini dapat diurai menjadi dua bagian persegi panjang: satu persegi panjang horizontal di bagian atas dan satu persegi panjang vertikal di bagian bawah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `087423442be49795c5b1bf93`

Toni sedang menyusun mainan balok.<br><br>Ada berapa banyak balok satuan pada mainan yang Toni susun?

| Opsi | Isi |
|---|---|
| A | 8 |
| B | 14 |
| C | 7 |
| D | 6 |

![Gambar sumber soal 19](<../images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Struktur terdiri dari 2 baris. Baris depan memiliki 3 balok. Baris belakang memiliki 5 balok (2 di bawah, 2 di atas, 1 di sisi kanan). Total = 3 + 5 = 8 balok.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png. Transkripsi visual: Gambar menunjukkan susunan balok satuan berwarna hijau. Struktur terdiri dari dua baris ke belakang. Baris depan memiliki 3 balok (satu di kiri, satu di tengah, satu di kanan). Baris belakang memiliki 5 balok (dua balok di kiri bawah, dua balok di atasnya, dan satu balok di kanan bawah). Total balok yang terlihat dan tersusun adalah 8.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `921371151511dd9ed76e30011fdf7faf88343e23a9599623d1a120102b4615e3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2598 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2585 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2596 |

Run 1 — solusi: Menghitung total balok: baris depan (3) + tingkat kedua (2) + baris belakang (3) = 8 balok.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi visual tentang balok yang terlihat dan menyimpulkan keberadaan balok yang tersembunyi untuk menghitung total objek, yang melampaui sekadar pengenalan visual langsung.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan pemahaman tentang struktur ruang dan prinsip bahwa objek 3D memiliki volume yang menempati ruang, meskipun sebagian tidak terlihat.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan penalaran spasial sederhana untuk membayangkan bagian yang tersembunyi, yang merupakan langkah di atas sekadar menghitung objek yang terlihat.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang objek 3D dan kemampuan menghitung benda konkret. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Untuk kelas 2, membayangkan objek tersembunyi dalam struktur 3D adalah tantangan kognitif yang sesuai untuk tingkat menengah, karena memerlukan lebih dari sekadar menghitung apa yang terlihat langsung. |

Run 2 — solusi: Susunan terdiri dari 2 baris. Baris depan memiliki 4 balok. Baris belakang memiliki 4 balok. Total = 4 + 4 = 8 balok.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi visual tentang balok yang terlihat dengan penalaran spasial untuk menyimpulkan keberadaan balok yang tersembunyi di bagian belakang struktur.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur objek 3D yang tersusun dari unit-unit dasar, bukan sekadar menghafal fakta atau mengikuti algoritma prosedural murni.. Bukti: Toni sedang menyusun mainan balok.
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk membayangkan struktur 3D secara utuh. Meskipun jumlah balok kecil, siswa kelas 2 sering kesulitan dengan objek yang memiliki bagian tersembunyi (hidden cubes), sehingga ini dikategorikan Medium.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang objek 3D dan kemampuan menghitung benda konkret. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membayangkan balok yang tidak terlihat di balik struktur adalah tantangan kognitif yang sesuai untuk tingkat menengah. |

Run 3 — solusi: Susunan terdiri dari 3 balok di baris depan dan 5 balok di baris belakang (2 balok tumpuk di atas 2 balok dasar, ditambah 1 balok dasar di sisi kanan). Total = 3 + 5 = 8 balok.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan menghitung objek 3D yang sebagian tersembunyi, yang memerlukan penerapan konsep spasial dasar.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur objek 3D dan bagaimana balok-balok tersebut tersusun dalam ruang.. Bukti: Ada berapa banyak balok satuan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 2 harus melakukan visualisasi spasial untuk menghitung balok yang tidak terlihat sepenuhnya (tersembunyi di belakang), bukan sekadar menghitung objek yang terlihat langsung.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret dan pemahaman dasar tentang susunan objek 3D. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membayangkan objek yang tersembunyi di balik objek lain dalam susunan 3D merupakan tantangan kognitif yang sesuai untuk tingkat kesulitan menengah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "reasoning": 1} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3989`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa perlu melakukan penalaran spasial untuk mengidentifikasi balok yang tidak terlihat sepenuhnya (tersembunyi di balik balok lain) dan mengintegrasikan informasi visual tersebut untuk mendapatkan total yang benar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang struktur objek 3D dan bagaimana unit-unit balok membentuk volume, bukan sekadar menghitung objek yang terlihat secara langsung.
- Intended difficulty `Medium`: Tingkat kesulitan Medium tepat untuk kelas 2 karena siswa harus melakukan visualisasi spasial untuk menghitung balok yang tersembunyi, yang merupakan langkah kognitif lebih tinggi daripada sekadar menghitung objek yang terlihat jelas.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang objek 3D dan kemampuan menghitung benda konkret. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membayangkan objek tersembunyi dalam struktur 3D adalah tantangan kognitif yang sesuai untuk tingkat menengah bagi siswa kelas 2. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 131/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000013 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.054190; conceptual=0.943696; procedural=0.002113; metacognitive=0.000000 | conceptual | 0.943696 | 0.162796 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.752479; Medium=0.244020; Hard=0.003501 | Easy | 0.752479 | 0.526102 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000014; H = 0.000014/ln(3) = 0.000013; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.943696; −Σp ln(p) = 0.225684; H = 0.225684/ln(4) = 0.162796; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.752479; −Σp ln(p) = 0.577982; H = 0.577982/ln(3) = 0.526102; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan susunan balok satuan berwarna hijau. Struktur terdiri dari dua baris ke belakang. Baris depan memiliki 3 balok (satu di kiri, satu di tengah, satu di kanan). Baris belakang memiliki 5 balok (dua balok di kiri bawah, dua balok di atasnya, dan satu balok di kanan bawah). Total balok yang terlihat dan tersusun adalah 8.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "reasoning", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `b752c451c1f2a955262fabf4`

Berilah nama pada setiap bangun ruang berikut.

| Opsi | Isi |
|---|---|
| A | Bola |
| B | Balok |
| C | Kerucut |
| D | Tabung |

![Gambar sumber soal 20](<../images/kelas2_panduan_siswa_kelas2.pdf-0110-04.png>)


Kunci sumber: `D`; status AI: `unverifiable`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal tidak dapat diselesaikan karena format soal (pilihan ganda vs isian) dan instruksi tidak sinkron dengan visual yang diberikan.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0110-04.png. Transkripsi visual: Terdapat dua bangun ruang: satu bola berwarna hijau dan satu tabung berwarna ungu. Terdapat lima kotak teks dengan label 'Nama = ____' yang tersebar di sekitar gambar, namun tidak ada garis penunjuk atau indikator yang menghubungkan kotak-kotak tersebut ke bangun ruang tertentu.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `893a7c122bc591b39549a584c22052f52874f5fddf421bffa7e86ab5a0170882`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2479 |
| 2 | success | concern / conflict | knowing | factual | Easy | 2525 |
| 3 | success | concern / conflict | knowing | factual | Easy | 2549 |

Run 1 — solusi: Objek berwarna ungu berbentuk silinder dengan dua sisi datar lingkaran, yang secara geometris disebut tabung.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun ruang berdasarkan karakteristik visual yang sudah dipelajari.. Bukti: Berilah nama pada setiap bangun ruang berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengenalan terhadap istilah dan label dasar dari bangun ruang (bola dan tabung).. Bukti: Berilah nama pada setiap bangun ruang berikut.
- Intended difficulty `classify/Easy`: Tugas ini adalah pengenalan bentuk dasar yang sangat rutin untuk kelas 2, tidak memerlukan strategi kompleks.. Bukti: Berilah nama pada setiap bangun ruang berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali bentuk dasar bangun ruang (bola, tabung, kubus, balok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengenalan nama bangun ruang adalah materi standar kelas 2 SD yang bersifat hafalan/pengenalan visual langsung. |

Run 2 — solusi: Soal tidak valid karena ketidaksesuaian antara instruksi, jumlah objek, dan format pilihan ganda.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun ruang berdasarkan bentuk visualnya, yang merupakan proses kognitif tingkat dasar.. Bukti: Berilah nama pada setiap bangun ruang berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan siswa mengenai istilah atau nama-nama bangun ruang dasar.. Bukti: Berilah nama pada setiap bangun ruang berikut.
- Intended difficulty `classify/Easy`: Tugas mengidentifikasi bentuk dasar adalah prosedur familiar bagi siswa kelas 2.. Bukti: Berilah nama pada setiap bangun ruang berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun ruang dasar (bola, tabung, kubus, balok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi nama bangun ruang adalah standar kompetensi dasar kelas 2 SD. |

Run 3 — solusi: Soal ambigu karena menampilkan dua objek (bola dan tabung) tetapi hanya menyediakan satu pilihan jawaban, sehingga tidak dapat ditentukan objek mana yang dimaksud oleh kunci jawaban.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun ruang berdasarkan bentuk visualnya, yang merupakan proses pengenalan langsung.. Bukti: Berilah nama pada setiap bangun ruang berikut.
- Dimensi pengetahuan `classify/factual`: Tugas ini menguji pengetahuan siswa tentang istilah atau nama-nama bangun ruang dasar.. Bukti: Berilah nama pada setiap bangun ruang berikut.
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar bagi kelas 2, hanya memerlukan identifikasi visual langsung tanpa langkah prosedural yang kompleks.. Bukti: Berilah nama pada setiap bangun ruang berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun ruang dasar (bola, tabung, kubus, balok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi nama bangun ruang adalah materi standar kelas 2 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3734`.
Konten: `concern`; kunci: `unverifiable`; masalah: Terdapat ketidaksesuaian antara tipe soal yang dinyatakan (Pilihan Ganda) dengan visual yang ditampilkan (isian singkat/melengkapi nama).; Instruksi soal 'Berilah nama pada setiap bangun ruang berikut' tidak spesifik mengenai objek mana yang harus dijawab, sementara terdapat dua objek (bola dan tabung) dan lima kotak isian kosong yang tidak terhubung secara jelas dengan objek-objek tersebut.; Kunci jawaban 'D' (Tabung) tidak dapat diverifikasi karena soal tidak menyajikan format pilihan ganda yang sesuai dengan kunci tersebut..
- Domain kognitif `knowing`: Secara teoretis, tugas mengidentifikasi nama bangun ruang adalah aktivitas 'knowing' (mengingat/mengenali), namun karena soal cacat, proses kognitif tidak dapat diterapkan dengan benar.
- Dimensi pengetahuan `factual`: Soal ini bertujuan menguji pengetahuan faktual mengenai nama-nama bangun ruang dasar.
- Intended difficulty `Easy`: Secara konten, materi ini sangat dasar (Easy), namun karena cacat pada struktur soal, tingkat kesulitan menjadi tidak relevan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun ruang dasar (bola, tabung). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | not_applicable |
| gradeRelativeRationale | Pengenalan nama bangun ruang adalah materi standar kelas 2 SD, namun soal ini memiliki cacat penyajian yang membuatnya tidak valid. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 106/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Bangun Ruang
Tipe soal: multiple_choice
Stimulus: -
Soal: Berilah nama pada setiap bangun ruang berikut.
Pilihan: A. Bola
B. Balok
C. Kerucut
D. Tabung
Transkripsi visual: Terdapat dua bangun ruang: satu bola berwarna hijau dan satu tabung berwarna ungu. Terdapat lima kotak teks dengan label 'Nama = ____' yang tersebar di sekitar gambar, namun tidak ada garis penunjuk atau indikator yang menghubungkan kotak-kotak tersebut ke bangun ruang tertentu.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidaksesuaian antara tipe soal yang dinyatakan (Pilihan Ganda) dengan visual yang ditampilkan (isian singkat/melengkapi nama).; Instruksi soal 'Berilah nama pada setiap bangun ruang berikut' tidak spesifik mengenai objek mana yang harus dijawab, sementara terdapat dua objek (bola dan tabung) dan lima kotak isian kosong yang tidak terhubung secara jelas dengan objek-objek tersebut.; Kunci jawaban 'D' (Tabung) tidak dapat diverifikasi karena soal tidak menyajikan format pilihan ganda yang sesuai dengan kunci tersebut..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `aaf396a280df35704272b0d3`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 8 |
| C | 4 |
| D | 5 |

![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-04.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-05.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-06.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-07.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-08.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-09.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-10.png>)


![Gambar sumber soal 21](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-11.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identifikasi bentuk lengkung: 2 lingkaran hitam (mata) + 1 oval merah (telinga) + 2 lingkaran merah (bercak badan) = 5.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-04.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-05.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-06.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-07.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-08.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-09.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-10.png, images/kelas1_panduan_siswa_kelas1.pdf-0150-11.png. Transkripsi visual: Gambar terdiri dari beberapa bentuk geometris yang disusun membentuk figur anjing. Terdapat 2 lingkaran hitam kecil (mata), 1 oval merah (telinga), 2 lingkaran merah (bercak pada badan), 1 persegi panjang oranye (kepala), 1 persegi panjang oranye (badan), 4 persegi panjang merah (kaki), dan 1 persegi panjang biru (ekor).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `09e77ac67b4c46f8243963726302854e814856d92566c2f90e0d8e2d941b72e6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 11287 |
| 2 | success | valid / verified | applying | conceptual | Easy | 11290 |
| 3 | success | valid / verified | knowing | factual | Easy | 11305 |

Run 1 — solusi: Identifikasi bentuk lengkung pada gambar: 2 mata (lingkaran hitam), 1 telinga (oval merah), dan 2 bercak (lingkaran merah). Total = 2 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung objek dengan karakteristik tertentu (lengkung) dari sekumpulan bentuk geometris yang membentuk gambar. Ini adalah proses pengenalan dan penghitungan langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang kategori bentuk (lengkung vs tidak lengkung/poligon) dan kemampuan mengklasifikasikannya.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung dan penghitungan sederhana (penjumlahan hingga 5) tanpa manipulasi kompleks.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran/oval vs persegi/persegi panjang) dan kemampuan berhitung dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD yang sedang mempelajari pengenalan bangun datar dan sifat-sifatnya (lengkung vs lurus). |

Run 2 — solusi: Identifikasi bentuk lengkung pada gambar: 2 lingkaran hitam (mata), 1 oval merah (telinga), dan 2 lingkaran merah (bercak badan). Total = 2 + 1 + 2 = 5.
- Domain kognitif `classify/applying`: Siswa perlu mengenali dan mengklasifikasikan bentuk bangun datar (lingkaran/oval vs poligon) lalu menghitung jumlahnya. Ini adalah proses applying karena menerapkan konsep pengenalan bentuk pada situasi rutin.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bentuk (lengkung vs lurus/sisi) untuk mengkategorikan objek.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena hanya memerlukan identifikasi visual langsung terhadap atribut bentuk yang sangat jelas (lengkung vs lurus) dan operasi hitung dasar.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran, persegi, persegi panjang) dan konsep sisi lengkung. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2, menguji kemampuan observasi dan klasifikasi bentuk sederhana. |

Run 3 — solusi: Identifikasi bentuk lengkung pada gambar: 2 lingkaran hitam (mata), 1 oval merah (telinga), dan 2 lingkaran merah (bercak pada badan). Total = 2 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek berdasarkan atribut geometris (lengkung) yang terlihat langsung pada gambar. Ini adalah proses pengenalan dan penghitungan sederhana.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang klasifikasi bentuk (lengkung vs tidak lengkung/poligon) dan kemampuan menghitung objek sederhana.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung dan penghitungan dasar (penjumlahan) tanpa strategi kompleks atau manipulasi representasi yang sulit bagi siswa kelas 2.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran/oval vs persegi/persegi panjang) dan kemampuan berhitung 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan untuk mengidentifikasi dan membedakan bentuk bangun datar sederhana, serta melakukan penghitungan objek. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `12642`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek berdasarkan atribut geometris (lengkung) yang terlihat langsung pada gambar. Ini adalah proses pengenalan dan penghitungan sederhana.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bentuk (lengkung vs lurus/poligon) untuk mengkategorikan objek.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung dan penghitungan dasar (penjumlahan) tanpa strategi kompleks atau manipulasi representasi yang sulit bagi siswa kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran/oval vs persegi/persegi panjang) dan kemampuan berhitung 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan untuk mengidentifikasi dan membedakan bentuk bangun datar sederhana, serta melakukan penghitungan objek. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 133/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.007985; applying=0.992015; reasoning=0.000000 | applying | 0.992015 | 0.042346 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.049669; conceptual=0.945571; procedural=0.004760; metacognitive=0.000000 | conceptual | 0.945571 | 0.164105 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.810406; Medium=0.186277; Hard=0.003316 | Easy | 0.810406 | 0.457248 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.992015; −Σp ln(p) = 0.046522; H = 0.046522/ln(3) = 0.042346; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.945571; −Σp ln(p) = 0.227497; H = 0.227497/ln(4) = 0.164105; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.810406; −Σp ln(p) = 0.502338; H = 0.502338/ln(3) = 0.457248; T = 0.953328.


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
Transkripsi visual: Gambar terdiri dari beberapa bentuk geometris yang disusun membentuk figur anjing. Terdapat 2 lingkaran hitam kecil (mata), 1 oval merah (telinga), 2 lingkaran merah (bercak pada badan), 1 persegi panjang oranye (kepala), 1 persegi panjang oranye (badan), 4 persegi panjang merah (kaki), dan 1 persegi panjang biru (ekor).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `801ce06c2a691e98bf7478c5`

Amati gambar berikut. Temukan benda-benda yang posisinya sebagai berikut.<br><br>Di bawah tempat tidur ada ....

| Opsi | Isi |
|---|---|
| A | tas ransel dan penggaris segitiga |
| B | sandal dan mainan mobil-mobilan |
| C | kotak penyimpanan berwarna biru |
| D | boneka beruang di atas kursi |

![Gambar sumber soal 22](<../images/kelas2_panduan_siswa_kelas2.pdf-0121-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Berdasarkan pengamatan visual pada gambar, di kolong (bawah) tempat tidur terdapat sepasang sandal dan mainan mobil-mobilan, yang sesuai dengan pilihan B.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0121-01.png. Transkripsi visual: Gambar menunjukkan sebuah kamar tidur dengan berbagai perabot dan benda. Di bawah tempat tidur (kolong tempat tidur), terdapat sepasang sandal berwarna hijau dan sebuah mainan mobil-mobilan. Di atas meja belajar terdapat tas ransel, penggaris segitiga, dan buku. Di atas kursi terdapat boneka beruang. Di sebelah meja belajar terdapat kotak penyimpanan berwarna biru.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `836edd5ba4114756b95d325e76712302192a16eddd65a21fa3b4fed322a4a6ba`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2543 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2512 |
| 3 | success | valid / verified | knowing | factual | Easy | 3068 |

Run 1 — solusi: Mengamati area kolong tempat tidur pada gambar menunjukkan keberadaan sandal dan mainan mobil-mobilan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi posisi benda berdasarkan pengamatan visual langsung. Proses ini melibatkan pengenalan fakta spasial sederhana tanpa memerlukan manipulasi atau strategi kompleks.. Bukti: Amati gambar berikut.; Temukan benda-benda yang posisinya sebagai berikut.; Di bawah tempat tidur ada ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep posisi (spasial) dasar, yaitu 'di bawah', yang merupakan pengetahuan konseptual dasar dalam geometri spasial untuk kelas 2.. Bukti: Di bawah tempat tidur ada ....
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan observasi visual langsung terhadap satu relasi spasial yang jelas tanpa adanya distraktor yang membingungkan atau langkah prosedural yang rumit.. Bukti: Di bawah tempat tidur ada ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan memahami konsep posisi dasar (di atas, di bawah, di samping) dan kemampuan observasi visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan posisi benda di lingkungan sekitar yang familiar. |

Run 2 — solusi: Mengamati area kolong tempat tidur pada gambar menunjukkan keberadaan sandal dan mainan mobil-mobilan, yang sesuai dengan pilihan B.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan mengidentifikasi posisi spasial benda berdasarkan pengamatan visual langsung, yang merupakan proses knowing.. Bukti: Temukan benda-benda yang posisinya sebagai berikut; Di bawah tempat tidur ada
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep posisi spasial (di bawah), yang merupakan pengetahuan konseptual dasar.. Bukti: posisinya sebagai berikut; Di bawah tempat tidur
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan observasi visual langsung terhadap satu lokasi spesifik tanpa manipulasi atau strategi kompleks.. Bukti: Di bawah tempat tidur ada

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep posisi (di atas, di bawah, di samping). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya menuntut kemampuan observasi visual sederhana terkait konsep posisi spasial yang sudah dipelajari. |

Run 3 — solusi: Pada gambar, terlihat sepasang sandal berwarna hijau dan sebuah mobil-mobilan berada di kolong tempat tidur.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan observasi visual langsung untuk mengenali objek yang berada di posisi yang ditanyakan.. Bukti: Di bawah tempat tidur ada ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai posisi spasial benda-benda di dalam ruangan.. Bukti: Di bawah tempat tidur ada ....
- Intended difficulty `classify/Easy`: Tugas ini bersifat langsung dan tidak memerlukan strategi atau pemrosesan informasi yang kompleks.. Bukti: Di bawah tempat tidur ada ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep posisi dasar (di atas, di bawah, di samping). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sangat sesuai untuk kelas 2 karena hanya memerlukan observasi visual sederhana terhadap posisi benda. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3717`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan observasi visual langsung untuk mengenali objek yang berada di posisi yang ditanyakan. Ini adalah proses pengenalan fakta spasial sederhana.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep posisi (spasial) dasar, yaitu 'di bawah', yang merupakan pengetahuan konseptual dasar dalam geometri spasial untuk kelas 2.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya memerlukan observasi visual langsung terhadap satu relasi spasial yang jelas tanpa adanya distraktor yang membingungkan atau langkah prosedural yang rumit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan memahami konsep posisi dasar (di atas, di bawah, di samping) dan kemampuan observasi visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan posisi benda di lingkungan sekitar yang familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 151/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000020; applying=0.999980; reasoning=0.000000 | applying | 0.999980 | 0.000211 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.034634; conceptual=0.964295; procedural=0.001071; metacognitive=0.000000 | conceptual | 0.964295 | 0.114591 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.761125; Medium=0.233053; Hard=0.005822 | Easy | 0.761125 | 0.525350 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999980; −Σp ln(p) = 0.000232; H = 0.000232/ln(3) = 0.000211; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.964295; −Σp ln(p) = 0.158856; H = 0.158856/ln(4) = 0.114591; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.761125; −Σp ln(p) = 0.577155; H = 0.577155/ln(3) = 0.525350; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah kamar tidur dengan berbagai perabot dan benda. Di bawah tempat tidur (kolong tempat tidur), terdapat sepasang sandal berwarna hijau dan sebuah mainan mobil-mobilan. Di atas meja belajar terdapat tas ransel, penggaris segitiga, dan buku. Di atas kursi terdapat boneka beruang. Di sebelah meja belajar terdapat kotak penyimpanan berwarna biru.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `44d1998fb7727977ef848256`

Perhatikan posisi kucing berikut. Lingkari kata yang menunjukkan posisi kucing terhadap benda yang ada.<br><br>Kucing duduk di .... meja.

| Opsi | Isi |
|---|---|
| A | belakang |
| B | bawah |
| C | kanan |
| D | atas |

![Gambar sumber soal 23](<../images/kelas2_panduan_siswa_kelas2.pdf-0119-12.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Secara visual, posisi kucing berada di atas permukaan meja, sehingga kata yang tepat adalah 'atas'.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0119-12.png. Transkripsi visual: Gambar menunjukkan seekor kucing duduk tepat di atas permukaan meja kayu. Terdapat teks 'Kucing duduk di ____ meja.'

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8815ffb7030da9c41abbf25c4f9f721bc91c2fe90be96e8d2363d622009e149b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2396 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2385 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2384 |

Run 1 — solusi: Secara visual, posisi kucing berada di atas permukaan meja, sehingga kata yang tepat adalah 'atas'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali posisi spasial objek berdasarkan gambar dan mencocokkannya dengan istilah posisi yang tepat.. Bukti: Kucing duduk di .... meja.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep spasial dasar (posisi benda).. Bukti: posisi kucing terhadap benda
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar, melibatkan pengenalan posisi spasial sederhana yang umum diajarkan di kelas rendah.. Bukti: Kucing duduk di .... meja.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman kosakata posisi dasar (atas, bawah, depan, belakang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena menguji pemahaman konsep posisi benda yang merupakan materi dasar geometri spasial. |

Run 2 — solusi: Kucing berada di permukaan atas meja, sehingga posisi yang tepat adalah 'atas'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali posisi spasial objek berdasarkan pengamatan visual langsung, yang merupakan proses kognitif tingkat dasar.. Bukti: Kucing duduk di .... meja.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang terminologi posisi spasial (atas/bawah/samping) yang merupakan konsep dasar dalam geometri spasial.. Bukti: posisi kucing terhadap benda
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung tanpa perhitungan atau strategi kompleks, sesuai untuk kelas 2.. Bukti: Kucing duduk di .... meja.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman kosakata posisi spasial dasar (atas, bawah, depan, belakang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan ini sangat sesuai untuk kelas 2 karena hanya melibatkan pengenalan posisi benda secara langsung. |

Run 3 — solusi: Kucing berada di permukaan atas meja, sehingga posisi yang tepat adalah 'atas'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali posisi spasial objek berdasarkan representasi visual langsung tanpa perlu melakukan operasi atau penalaran kompleks.. Bukti: Kucing duduk di .... meja.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep spasial dasar (posisi benda), yang merupakan pengetahuan konseptual.. Bukti: posisi kucing terhadap benda
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung terhadap posisi objek yang familiar bagi siswa kelas 2.. Bukti: Kucing duduk di .... meja.

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
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menguji kosakata posisi spasial dasar yang umum diajarkan di tingkat awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 96/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.003056; applying=0.996944; reasoning=0.000000 | applying | 0.996944 | 0.018886 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.359355; conceptual=0.575653; procedural=0.064992; metacognitive=0.000000 | conceptual | 0.575653 | 0.622767 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.885585; Medium=0.110373; Hard=0.004042 | Easy | 0.885585 | 0.339636 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996944; −Σp ln(p) = 0.020748; H = 0.020748/ln(3) = 0.018886; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.575653; −Σp ln(p) = 0.863339; H = 0.863339/ln(4) = 0.622767; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.885585; −Σp ln(p) = 0.373128; H = 0.373128/ln(3) = 0.339636; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Posisi Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan posisi kucing berikut. Lingkari kata yang menunjukkan posisi kucing terhadap benda yang ada.

Kucing duduk di .... meja.
Pilihan: A. belakang
B. bawah
C. kanan
D. atas
Transkripsi visual: Gambar menunjukkan seekor kucing duduk tepat di atas permukaan meja kayu. Terdapat teks 'Kucing duduk di ____ meja.'
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `c5e424e9914591b1d5286ef0`

Amati setiap pola berikut. Lanjutkan polanya dengan melingkari gambar berikutnya.<br><br>Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.

| Opsi | Isi |
|---|---|
| A | kelinci |
| B | kupu-kupu |
| C | bunga |
| D | heksagon |

![Gambar sumber soal 24](<../images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pola pada baris b adalah pengulangan unit (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu, elemen berikutnya dalam urutan adalah kelinci.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Baris b menunjukkan pola berulang: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Urutan unit pengulangan adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, gambar berikutnya haruslah kelinci.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `861294ab8a641a5bf1c498b5618a264ab52416794f44ae80eca64430d56e4a5c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2578 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2553 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2610 |

Run 1 — solusi: Pola pada baris b adalah pengulangan unit (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu, elemen berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengenali unit pengulangan dalam pola visual dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses penerapan konsep pola yang sudah dipelajari.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan pengetahuan konseptual tentang bagaimana elemen-elemen disusun dalam urutan.. Bukti: Amati setiap pola berikut (baris b).
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengidentifikasi pola berulang sederhana dengan unit tiga elemen. Ini adalah tugas rutin untuk kelas 2.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pola berulang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola berulang (repeating patterns) adalah materi standar kelas 2. Soal ini bersifat langsung dan tidak memerlukan strategi kompleks. |

Run 2 — solusi: Pola pada baris b adalah pengulangan unit (kupu-kupu, kelinci, kelinci). Karena urutan terakhir adalah kupu-kupu, maka gambar selanjutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi unit pengulangan dalam pola visual sederhana dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses penerapan konsep pola yang sudah dipelajari.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan konsep dasar dalam matematika awal.. Bukti: Amati setiap pola berikut
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena pola yang diberikan bersifat repetitif dan visual, sangat umum untuk tingkat kelas 2.. Bukti: Lanjutkan polanya dengan melingkari gambar berikutnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pengulangan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola berulang adalah materi standar kelas 2. Soal ini tidak memerlukan perhitungan kompleks atau strategi non-rutin. |

Run 3 — solusi: Pola baris b adalah pengulangan tiga gambar: kupu-kupu, kelinci, kelinci. Karena urutan terakhir adalah kupu-kupu, maka gambar berikutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengenali struktur pola berulang (kupu-kupu, kelinci, kelinci) dan menerapkan aturan tersebut untuk memprediksi elemen berikutnya. Ini adalah penerapan konsep pola sederhana.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating pattern), yang merupakan pengetahuan konseptual dasar dalam matematika awal.. Bukti: Amati setiap pola berikut (baris b)
- Intended difficulty `classify/Easy`: Tugas ini melibatkan identifikasi pola berulang yang sederhana dan rutin untuk siswa kelas 2. Tidak ada strategi nonrutin atau integrasi kompleks yang diperlukan.. Bukti: Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengidentifikasi urutan visual dan pengulangan objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola berulang adalah materi standar kelas 2. Soal ini bersifat langsung dan tidak memerlukan perhitungan atau penalaran tingkat tinggi. |

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
| Domain kognitif | knowing=0.000029; applying=0.999971; reasoning=0.000000 | applying | 0.999971 | 0.000300 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003660; conceptual=0.993761; procedural=0.002579; metacognitive=0.000000 | conceptual | 0.993761 | 0.030387 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.634179; Medium=0.358553; Hard=0.007268 | Easy | 0.634179 | 0.630221 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999971; −Σp ln(p) = 0.000329; H = 0.000329/ln(3) = 0.000300; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.993761; −Σp ln(p) = 0.042126; H = 0.042126/ln(4) = 0.030387; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.634179; −Σp ln(p) = 0.692369; H = 0.692369/ln(3) = 0.630221; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Pola
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati setiap pola berikut. Lanjutkan polanya dengan melingkari gambar berikutnya.

Amati setiap pola berikut (baris b). Lanjutkan polanya dengan melingkari gambar berikutnya.
Pilihan: A. kelinci
B. kupu-kupu
C. bunga
D. heksagon
Transkripsi visual: Baris b menunjukkan pola berulang: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Urutan unit pengulangan adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, gambar berikutnya haruslah kelinci.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `66d36724cd73e571bae49422`

Amati pola warna berikut. Warnai gambar untuk melanjutkan polanya.<br><br>Amati pola warna berikut (baris a). Warnai gambar untuk melanjutkan polanya.

| Opsi | Isi |
|---|---|
| A | hijau |
| B | merah muda |
| C | biru |
| D | oranye |

![Gambar sumber soal 25](<../images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pola pada baris 'a' adalah pengulangan dua warna: oranye dan hijau. Karena elemen terakhir yang diberikan adalah oranye, maka elemen berikutnya dalam pola tersebut adalah hijau.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Soal nomor 3 menampilkan tiga baris pola warna. Baris 'a' terdiri dari lingkaran dengan urutan warna: oranye, hijau, oranye, hijau, oranye, diikuti oleh satu lingkaran kosong. Baris 'b' dan 'c' adalah pola lain yang tidak ditanyakan dalam teks soal.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `977116f94780d9ad0c3ed392774062cb2170643ca6a6cff67c155942b66a935f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2469 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2453 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2449 |

Run 1 — solusi: Pola baris a adalah pengulangan dua warna: oranye dan hijau. Setelah warna oranye, warna berikutnya adalah hijau.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan melanjutkan pola sederhana yang berulang secara langsung tanpa perlu strategi kompleks.. Bukti: Amati pola warna berikut; Warnai gambar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola sederhana (pengulangan elemen), yang merupakan pengetahuan konseptual dasar.. Bukti: pola warna; melanjutkan polanya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, menggunakan pola AB-AB yang sangat familiar dan membutuhkan satu langkah logika sederhana.. Bukti: pola warna berikut; oranye, hijau, oranye, hijau, oranye

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan warna dan mengenali urutan berulang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola AB-AB adalah materi standar awal kelas 2 yang bersifat rutin dan tidak menuntut kognitif tinggi. |

Run 2 — solusi: Pola baris a adalah pengulangan dua warna: oranye dan hijau. Karena elemen terakhir adalah oranye, maka elemen berikutnya harus hijau.
- Domain kognitif `classify/applying`: Siswa perlu mengenali keteraturan (pola) yang berulang dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses applying karena menggunakan konsep pola rutin.. Bukti: Amati pola warna berikut; Warnai gambar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang (AB-AB), yang merupakan pengetahuan konseptual tentang bagaimana elemen-elemen disusun dalam urutan.. Bukti: Amati pola warna berikut
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pola pengulangan sederhana (AB) yang familiar.. Bukti: Amati pola warna berikut; Warnai gambar untuk melanjutkan polanya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan warna dan mengenali urutan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola pengulangan dua elemen adalah materi standar awal kelas 2 yang bersifat rutin. |

Run 3 — solusi: Pola berulang oranye-hijau. Setelah oranye terakhir, warna berikutnya adalah hijau.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan melanjutkan urutan sederhana (AB-AB) yang sudah diberikan secara eksplisit.. Bukti: Amati pola warna berikut; Warnai gambar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang sederhana, yang merupakan konsep dasar dalam matematika awal.. Bukti: pola warna; melanjutkan polanya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, hanya melibatkan pengenalan pola berulang dua elemen yang sangat familiar.. Bukti: pola warna; oranye, hijau, oranye, hijau, oranye

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan warna dan mengenali urutan berulang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola AB-AB adalah materi standar kelas 1-2 yang sangat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3716`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengenali urutan yang berulang secara langsung dan meneruskan urutan tersebut. Ini adalah proses pengenalan pola sederhana yang bersifat langsung (knowing).
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep dasar pola berulang (AB-AB), yang merupakan pengetahuan konseptual tentang struktur urutan.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 2, menggunakan pola AB-AB yang sangat familiar dan membutuhkan satu langkah logika sederhana tanpa kompleksitas tambahan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan warna dan mengenali urutan berulang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola AB-AB adalah materi standar awal kelas 2 yang bersifat rutin dan tidak menuntut kognitif tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 129/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000002 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.013399; conceptual=0.984474; procedural=0.002127; metacognitive=0.000000 | conceptual | 0.984474 | 0.062237 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.684313; Medium=0.309909; Hard=0.005778 | Easy | 0.684313 | 0.593854 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000002; H = 0.000002/ln(3) = 0.000002; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.984474; −Σp ln(p) = 0.086279; H = 0.086279/ln(4) = 0.062237; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.684313; −Σp ln(p) = 0.652416; H = 0.652416/ln(3) = 0.593854; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Pola
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati pola warna berikut. Warnai gambar untuk melanjutkan polanya.

Amati pola warna berikut (baris a). Warnai gambar untuk melanjutkan polanya.
Pilihan: A. hijau
B. merah muda
C. biru
D. oranye
Transkripsi visual: Soal nomor 3 menampilkan tiga baris pola warna. Baris 'a' terdiri dari lingkaran dengan urutan warna: oranye, hijau, oranye, hijau, oranye, diikuti oleh satu lingkaran kosong. Baris 'b' dan 'c' adalah pola lain yang tidak ditanyakan dalam teks soal.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `81440a329d7562b80ba3a0a1`

Perhatikan gambar berikut. Manakah yang merupakan setengah dan bukan setengah? Kelompokkan dalam tabel berikut dengan menuliskan hurufnya.<br><br>Manakah yang bukan setengah?

| Opsi | Isi |
|---|---|
| A | C (lingkaran biru-putih, dibagi garis mendatar sama besar) |
| B | G (persegi panjang cokelat-putih, dibagi garis tegak sama besar) |
| C | B (segitiga hijau-putih, dibagi garis tegak tidak sama besar) |
| D | F (segi enam ungu-putih, dibagi garis mendatar sama besar) |

![Gambar sumber soal 26](<../images/kelas2_panduan_siswa_kelas2.pdf-0146-06.png>)


Kunci sumber: `C`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal tidak dapat diselesaikan karena label huruf pada pilihan jawaban tidak merujuk pada objek yang tepat di gambar.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0146-06.png. Transkripsi visual: Gambar menampilkan beberapa objek dengan label huruf: A (hati dibagi dua), B (gambar anak), C (bintang), D (segi enam dibagi dua), E (kosong/tidak ada objek), F (segi enam dibagi dua), G (persegi panjang dibagi dua). Terdapat ketidaksesuaian antara label huruf dan objek yang dimaksud dalam teks soal.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `87aa917e7bdf666b97e9587df85d27d7189e02fd7821604dba0fea6d331081da`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | — | — | — | 2441 |
| 2 | success | concern / conflict | — | — | — | 2439 |
| 3 | success | concern / conflict | applying | conceptual | Easy | 2681 |

Run 1 — solusi: Soal tidak dapat diselesaikan karena label huruf pada teks tidak merujuk pada objek yang tepat di gambar.
- Domain kognitif `abstain/None`: Soal tidak valid karena ketidaksesuaian label huruf antara teks dan gambar, sehingga tidak mungkin menentukan domain kognitif yang diuji secara akurat.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Soal tidak valid karena ketidaksesuaian label huruf antara teks dan gambar, sehingga tidak mungkin menentukan dimensi pengetahuan yang diuji secara akurat.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak valid karena ketidaksesuaian label huruf antara teks dan gambar, sehingga tidak mungkin menentukan tingkat kesulitan secara akurat.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 2 — solusi: Soal tidak dapat diselesaikan karena referensi visual (huruf dan bentuk) tidak sesuai dengan deskripsi pilihan jawaban.
- Domain kognitif `abstain/None`: Soal tidak valid secara visual dan tekstual, sehingga tidak mungkin menentukan domain kognitif yang diukur.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Soal tidak valid secara visual dan tekstual, sehingga tidak mungkin menentukan dimensi pengetahuan yang diukur.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak valid secara visual dan tekstual, sehingga tidak mungkin menentukan tingkat kesulitan.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 3 — solusi: Soal tidak dapat diselesaikan karena label huruf pada pilihan jawaban tidak sesuai dengan label pada gambar.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep pecahan sederhana (setengah) untuk membedakan antara objek yang dibagi sama besar dan tidak sama besar.. Bukti: Manakah yang bukan setengah?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa yang dimaksud dengan 'setengah' (pembagian menjadi dua bagian yang sama besar).. Bukti: setengah dari benda utuh
- Intended difficulty `classify/Easy`: Secara teoretis, soal ini termasuk kategori mudah karena hanya memerlukan pengenalan visual sederhana tentang pembagian sama besar, namun karena adanya kesalahan teknis pada label gambar, tingkat kesulitan menjadi tidak relevan.. Bukti: Manakah yang bukan setengah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah (pembagian dua bagian sama besar). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 2, membedakan setengah dan bukan setengah adalah materi standar yang rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1} | no_consensus / abstained | — |
| Dimensi pengetahuan | {"conceptual": 1} | no_consensus / abstained | — |
| Intended difficulty | {"Easy": 1} | no_consensus / abstained | — |

Adjudikasi AI: `success`; token `3321`.
Konten: `concern`; kunci: `conflict`; masalah: Terdapat ketidaksesuaian fatal antara label huruf pada gambar dengan deskripsi pilihan jawaban. Pilihan jawaban merujuk pada huruf C, G, B, F, namun gambar hanya melabeli objek dengan A, D, E, F, G (dan B adalah gambar anak, C adalah bintang).; Deskripsi pilihan jawaban dalam teks soal (misalnya 'C (lingkaran biru-putih)') tidak cocok dengan visual yang ada (C adalah bintang).; Soal tidak dapat diselesaikan secara logis karena referensi visual yang diberikan dalam teks pilihan jawaban tidak merujuk pada objek yang benar di gambar..
- Domain kognitif `None`: Soal tidak valid karena ketidaksesuaian label huruf antara teks dan gambar, sehingga tidak mungkin menentukan domain kognitif yang diuji secara akurat.
- Dimensi pengetahuan `None`: Soal tidak valid karena ketidaksesuaian label huruf antara teks dan gambar, sehingga tidak mungkin menentukan dimensi pengetahuan yang diuji secara akurat.
- Intended difficulty `None`: Soal tidak valid karena ketidaksesuaian label huruf antara teks dan gambar, sehingga tidak mungkin menentukan tingkat kesulitan secara akurat.

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 198/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut. Manakah yang merupakan setengah dan bukan setengah? Kelompokkan dalam tabel berikut dengan menuliskan hurufnya.

Manakah yang bukan setengah?
Pilihan: A. C (lingkaran biru-putih, dibagi garis mendatar sama besar)
B. G (persegi panjang cokelat-putih, dibagi garis tegak sama besar)
C. B (segitiga hijau-putih, dibagi garis tegak tidak sama besar)
D. F (segi enam ungu-putih, dibagi garis mendatar sama besar)
Transkripsi visual: Gambar menampilkan beberapa objek dengan label huruf: A (hati dibagi dua), B (gambar anak), C (bintang), D (segi enam dibagi dua), E (kosong/tidak ada objek), F (segi enam dibagi dua), G (persegi panjang dibagi dua). Terdapat ketidaksesuaian antara label huruf dan objek yang dimaksud dalam teks soal.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidaksesuaian fatal antara label huruf pada gambar dengan deskripsi pilihan jawaban. Pilihan jawaban merujuk pada huruf C, G, B, F, namun gambar hanya melabeli objek dengan A, D, E, F, G (dan B adalah gambar anak, C adalah bintang).; Deskripsi pilihan jawaban dalam teks soal (misalnya 'C (lingkaran biru-putih)') tidak cocok dengan visual yang ada (C adalah bintang).; Soal tidak dapat diselesaikan secara logis karena referensi visual yang diberikan dalam teks pilihan jawaban tidak merujuk pada objek yang benar di gambar..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `90c3bb9928fdd60f115a0d85`

Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.<br><br>Berilah tanda centang (✓) pada gambar yang menunjukkan setengah. (bagian c)

| Opsi | Isi |
|---|---|
| A | Tidak ada gambar yang menunjukkan setengah |
| B | Gambar kanan (dibagi oleh garis diagonal) |
| C | Gambar kiri (dibagi rata oleh garis tegak di tengah) |
| D | Kedua gambar menunjukkan setengah |

![Gambar sumber soal 27](<../images/kelas2_panduan_siswa_kelas2.pdf-0145-02.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `Gambar c kiri (hati dibagi vertikal), gambar b kanan (persegi panjang dibagi vertikal), dan gambar a kanan (lingkaran dibagi horizontal).`.
Solusi minimum hasil AI: Setengah didefinisikan sebagai dua bagian yang sama besar. Gambar yang menunjukkan setengah adalah: lingkaran kanan (a), persegi panjang kanan (b), dan hati kiri (c).
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0145-02.png. Transkripsi visual: Terdapat tiga baris gambar (a, b, c). Baris a: lingkaran dibagi garis miring (kiri) dan lingkaran dibagi garis horizontal (kanan). Baris b: persegi panjang dibagi tidak sama besar (kiri) dan persegi panjang dibagi sama besar (kanan). Baris c: bentuk hati dibagi vertikal sama besar (kiri) dan bentuk hati dibagi garis miring tidak sama besar (kanan).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f496092ac009eeb80191c8c3640fb94d054abd4010020eca9109e4138a501bf8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2532 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2593 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2616 |

Run 1 — solusi: Setengah didefinisikan sebagai dua bagian yang sama besar. Pada baris c, gambar kiri menunjukkan pembagian simetris yang menghasilkan dua bagian identik, sedangkan gambar kanan tidak.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep pecahan sederhana (setengah) dengan membandingkan visualisasi bagian yang sama besar dan tidak sama besar.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang dimaksud dengan 'setengah' (bagian yang sama besar) dalam konteks geometri.. Bukti: gambar yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan pengenalan visual sederhana tanpa perhitungan kompleks.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian benda menjadi dua bagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan observasi visual langsung terhadap konsep pecahan dasar. |

Run 2 — solusi: Setengah didefinisikan sebagai dua bagian yang sama besar. Pada baris c, gambar kiri adalah bentuk hati yang dibagi oleh garis vertikal tepat di tengah, menghasilkan dua bagian identik (setengah).
- Domain kognitif `classify/knowing`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian benda menjadi dua bagian yang sama besar, yang merupakan proses langsung dalam mengenali representasi visual.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep pecahan dasar (setengah) melalui representasi visual, bukan sekadar menghafal fakta atau prosedur.. Bukti: gambar yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pengenalan visual sederhana tentang kesamaan ukuran tanpa perhitungan kompleks.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman visual tentang kesamaan ukuran dan konsep dasar pecahan setengah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan konsep pecahan setengah melalui visualisasi langsung yang umum diajarkan di tingkat awal. |

Run 3 — solusi: Setengah didefinisikan sebagai dua bagian yang sama besar. Pada baris c, gambar kiri adalah bentuk hati yang dibagi oleh garis vertikal tepat di tengah, menghasilkan dua bagian yang kongruen (sama besar).
- Domain kognitif `classify/applying`: Siswa perlu mengenali dan menerapkan konsep 'setengah' (dua bagian yang sama besar) pada representasi visual geometri, yang merupakan proses applying.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara bagian-bagian objek dan konsep keseluruhan (setengah), yang merupakan pengetahuan konseptual.. Bukti: gambar yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan pengenalan visual sederhana tentang pembagian sama besar tanpa perhitungan kompleks.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep bagian yang sama besar (setengah). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual konsep pecahan dasar (setengah) yang diajarkan di tingkat awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3848`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep 'setengah' (dua bagian yang sama besar) untuk mengidentifikasi gambar yang memenuhi kriteria tersebut di antara pilihan yang ada.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan setengah sebagai pembagian objek menjadi dua bagian yang kongruen/sama besar.
- Intended difficulty `Easy`: Soal ini rutin untuk kelas 2, melibatkan observasi visual langsung untuk membedakan pembagian sama besar dan tidak sama besar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman visual tentang kesamaan ukuran dan konsep dasar pecahan setengah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan konsep pecahan setengah melalui visualisasi langsung yang umum diajarkan di tingkat awal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 178/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.027835; applying=0.972165; reasoning=0.000000 | applying | 0.972165 | 0.115724 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000839; conceptual=0.995676; procedural=0.003485; metacognitive=0.000000 | conceptual | 0.995676 | 0.021627 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.696634; Medium=0.298249; Hard=0.005117 | Easy | 0.696634 | 0.582238 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.972165; −Σp ln(p) = 0.127136; H = 0.127136/ln(3) = 0.115724; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.995676; −Σp ln(p) = 0.029981; H = 0.029981/ln(4) = 0.021627; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.696634; −Σp ln(p) = 0.639654; H = 0.639654/ln(3) = 0.582238; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Berilah tanda centang (✓) pada gambar yang menunjukkan setengah.

Berilah tanda centang (✓) pada gambar yang menunjukkan setengah. (bagian c)
Pilihan: A. Tidak ada gambar yang menunjukkan setengah
B. Gambar kanan (dibagi oleh garis diagonal)
C. Gambar kiri (dibagi rata oleh garis tegak di tengah)
D. Kedua gambar menunjukkan setengah
Transkripsi visual: Terdapat tiga baris gambar (a, b, c). Baris a: lingkaran dibagi garis miring (kiri) dan lingkaran dibagi garis horizontal (kanan). Baris b: persegi panjang dibagi tidak sama besar (kiri) dan persegi panjang dibagi sama besar (kanan). Baris c: bentuk hati dibagi vertikal sama besar (kiri) dan bentuk hati dibagi garis miring tidak sama besar (kanan).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `5eacf4162dd820a1d51e8bdc`

Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.<br><br>Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah. (bagian a)

| Opsi | Isi |
|---|---|
| A | Kedua baris menunjukkan setengah |
| B | Tidak ada baris yang menunjukkan setengah |
| C | Baris pertama (2 monyet dan 2 monyet) |
| D | Baris kedua (1 monyet dan 3 monyet) |

![Gambar sumber soal 28](<../images/kelas2_panduan_siswa_kelas2.pdf-0150-12.png>)


![Gambar sumber soal 28](<../images/kelas2_panduan_siswa_kelas2.pdf-0150-13.png>)


![Gambar sumber soal 28](<../images/kelas2_panduan_siswa_kelas2.pdf-0150-14.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `Baris pertama (2 monyet dan 2 monyet)`.
Solusi minimum hasil AI: Setengah dari 4 adalah 2. Baris pertama menunjukkan pembagian 4 monyet menjadi dua kelompok yang sama besar (2 dan 2), sedangkan baris kedua tidak sama besar (1 dan 3).
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0150-12.png, images/kelas2_panduan_siswa_kelas2.pdf-0150-13.png, images/kelas2_panduan_siswa_kelas2.pdf-0150-14.png. Transkripsi visual: Terdapat dua baris gambar monyet. Baris pertama berisi 4 monyet yang dibagi menjadi dua kotak, masing-masing berisi 2 monyet. Baris kedua berisi 4 monyet yang dibagi menjadi dua kotak, satu kotak berisi 1 monyet dan kotak lainnya berisi 3 monyet.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6a19cb2592a407009a1853a49737564bc6dc8356185c4a028560022093529d74`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 4690 |
| 2 | success | valid / verified | applying | conceptual | Easy | 4705 |
| 3 | success | valid / verified | applying | conceptual | Easy | 4700 |

Run 1 — solusi: Setengah dari 4 adalah 2. Baris pertama menunjukkan pembagian 4 monyet menjadi dua kelompok yang sama besar (2 dan 2), sedangkan baris kedua tidak sama besar (1 dan 3).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep 'setengah' (pembagian menjadi dua bagian sama besar) pada representasi visual objek konkret.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pembagian menjadi dua bagian yang sama besar (konsep setengah).. Bukti: setengah dari kumpulan benda
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan pengenalan visual langsung terhadap pembagian sederhana (4 menjadi 2 dan 2) yang merupakan materi dasar kelas 2.. Bukti: 4 monyet dibagi menjadi dua kelompok; 2 dan 2; 1 dan 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jumlah dan pembagian sederhana menjadi dua kelompok sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2, di mana siswa belajar membagi kumpulan benda menjadi dua bagian sama besar. |

Run 2 — solusi: Setengah dari 4 adalah 2. Baris pertama menunjukkan pembagian 4 monyet menjadi dua kelompok yang sama besar (2 dan 2), sedangkan baris kedua (1 dan 3) tidak sama besar.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi representasi visual dari konsep 'setengah' (pembagian sama rata) dari dua pilihan yang diberikan. Ini adalah penerapan konsep dasar pada situasi rutin.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep 'setengah' sebagai pembagian kumpulan benda menjadi dua bagian yang sama banyak.. Bukti: kelompok yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan pengenalan visual sederhana terhadap konsep pembagian dua kelompok yang sama besar, yang merupakan materi standar kelas 2.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah dan kemampuan membandingkan jumlah benda dalam kelompok. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan objek konkret (monyet) untuk memvisualisasikan konsep pecahan sederhana (setengah). |

Run 3 — solusi: Setengah dari 4 adalah 2. Baris pertama menunjukkan dua kelompok yang masing-masing berisi 2 monyet (sama banyak), sehingga merepresentasikan konsep setengah.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep 'setengah' (pembagian menjadi dua bagian sama banyak) ke dalam situasi visual yang diberikan. Ini adalah penerapan konsep dasar pada situasi rutin.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep 'setengah' sebagai pembagian objek menjadi dua kelompok dengan jumlah yang sama.. Bukti: kelompok yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan rutin untuk kelas 2, melibatkan pengenalan visual sederhana tentang pembagian sama rata.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dua kelompok sama banyak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan objek konkret (monyet) untuk memvisualisasikan konsep pecahan sederhana (setengah). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 146/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000003 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.008044; conceptual=0.983452; procedural=0.008504; metacognitive=0.000000 | conceptual | 0.983452 | 0.069067 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.706763; Medium=0.287085; Hard=0.006152 | Easy | 0.706763 | 0.577896 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000003; H = 0.000003/ln(3) = 0.000003; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.983452; −Σp ln(p) = 0.095748; H = 0.095748/ln(4) = 0.069067; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.706763; −Σp ln(p) = 0.634884; H = 0.634884/ln(3) = 0.577896; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Kumpulan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.

Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah. (bagian a)
Pilihan: A. Kedua baris menunjukkan setengah
B. Tidak ada baris yang menunjukkan setengah
C. Baris pertama (2 monyet dan 2 monyet)
D. Baris kedua (1 monyet dan 3 monyet)
Transkripsi visual: Terdapat dua baris gambar monyet. Baris pertama berisi 4 monyet yang dibagi menjadi dua kotak, masing-masing berisi 2 monyet. Baris kedua berisi 4 monyet yang dibagi menjadi dua kotak, satu kotak berisi 1 monyet dan kotak lainnya berisi 3 monyet.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `2550e20d6fe8dd73c9128673`

Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.<br><br>Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah. (bagian b)

| Opsi | Isi |
|---|---|
| A | Baris kedua (4 kelinci dan 4 kelinci) |
| B | Tidak ada baris yang menunjukkan setengah |
| C | Baris pertama (3 kelinci dan 5 kelinci) |
| D | Kedua baris menunjukkan setengah |

![Gambar sumber soal 29](<../images/kelas2_panduan_siswa_kelas2.pdf-0151-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Konsep setengah berarti membagi kumpulan benda menjadi dua bagian yang sama banyak. Baris ketiga memiliki 4 kelinci di sisi kiri dan 4 kelinci di sisi kanan (total 8), yang menunjukkan pembagian setengah yang tepat.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0151-01.png. Transkripsi visual: Terdapat tiga baris gambar kelinci. Baris pertama berisi 8 kelinci berjajar. Baris kedua berisi dua kotak: kotak kiri berisi 3 kelinci, kotak kanan berisi 5 kelinci. Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad3e03837c7d8bbd87915388e97ce89e5243f6540606f27df45a38860433d3f3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2544 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2543 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2537 |

Run 1 — solusi: Konsep setengah berarti membagi kumpulan benda menjadi dua bagian yang sama banyak. Baris ketiga memiliki 4 kelinci di sisi kiri dan 4 kelinci di sisi kanan (total 8), yang menunjukkan pembagian setengah yang tepat.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian dua kelompok yang sama banyak dan menerapkannya untuk memverifikasi visualisasi yang diberikan.. Bukti: menunjukkan setengah; kelompok yang sama banyak
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) dalam konteks kumpulan benda.. Bukti: setengah dari Kumpulan Benda
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengidentifikasi representasi visual dari konsep setengah. Ini adalah tugas rutin bagi siswa kelas 2 yang sudah mempelajari dasar pecahan.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep pembagian dua kelompok sama banyak (setengah) dan kemampuan berhitung dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan pengamatan visual sederhana terhadap jumlah benda untuk memverifikasi kesamaan jumlah. |

Run 2 — solusi: Konsep setengah berarti membagi kumpulan menjadi dua bagian yang sama banyak. Baris ketiga memiliki 4 kelinci di kiri dan 4 kelinci di kanan (total 8), yang menunjukkan pembagian setengah yang benar.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep 'setengah' (pembagian sama rata) ke dalam situasi visual yang diberikan.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'setengah' sebagai pembagian dua bagian yang sama besar.. Bukti: menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan pengenalan visual sederhana tentang kesamaan jumlah dalam dua kelompok.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah dan kemampuan menghitung benda hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu mengidentifikasi pembagian benda menjadi dua kelompok sama banyak secara visual. |

Run 3 — solusi: Konsep setengah adalah membagi kumpulan benda menjadi dua bagian yang sama banyak. Baris ketiga memiliki 4 kelinci di sisi kiri dan 4 kelinci di sisi kanan (total 8), yang menunjukkan pembagian setengah yang tepat.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian dua kelompok yang sama banyak dan menerapkannya untuk mengevaluasi visual yang diberikan.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pembagian benda menjadi dua bagian yang sama besar.. Bukti: setengah dari kumpulan benda
- Intended difficulty `classify/Easy`: Soal ini meminta siswa membandingkan dua kelompok benda untuk menentukan kesamaan jumlah, yang merupakan prosedur rutin untuk kelas 2.. Bukti: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jumlah benda dan konsep pembagian dua kelompok sama banyak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan konsep setengah (pecahan sederhana) melalui manipulasi benda konkret atau gambar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 149/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000022; applying=0.999978; reasoning=0.000000 | applying | 0.999978 | 0.000234 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.015184; conceptual=0.974181; procedural=0.010635; metacognitive=0.000000 | conceptual | 0.974181 | 0.099103 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.781739; Medium=0.213566; Hard=0.004696 | Easy | 0.781739 | 0.498238 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999978; −Σp ln(p) = 0.000257; H = 0.000257/ln(3) = 0.000234; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.974181; −Σp ln(p) = 0.137386; H = 0.137386/ln(4) = 0.099103; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.781739; −Σp ln(p) = 0.547370; H = 0.547370/ln(3) = 0.498238; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Setengah dari Kumpulan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah.

Berilah tanda centang (✓) pada kelompok yang menunjukkan setengah. (bagian b)
Pilihan: A. Baris kedua (4 kelinci dan 4 kelinci)
B. Tidak ada baris yang menunjukkan setengah
C. Baris pertama (3 kelinci dan 5 kelinci)
D. Kedua baris menunjukkan setengah
Transkripsi visual: Terdapat tiga baris gambar kelinci. Baris pertama berisi 8 kelinci berjajar. Baris kedua berisi dua kotak: kotak kiri berisi 3 kelinci, kotak kanan berisi 5 kelinci. Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `764036b9759f6277bc4dca51`

Perhatikan gambar yang diwarnai berikut. Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat. Berilah tanda silang pada gambar yang tidak menunjukkan seperempat.<br><br>Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat.

| Opsi | Isi |
|---|---|
| A | Gambar 3 (bentuk anak panah) |
| B | Gambar 1 (segitiga) |
| C | Gambar 4 (kotak berpetak) |
| D | Gambar 2 (segi enam memanjang) |

![Gambar sumber soal 30](<../images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png>)


![Gambar sumber soal 30](<../images/kelas2_panduan_siswa_kelas2.pdf-0159-11.png>)


![Gambar sumber soal 30](<../images/kelas2_panduan_siswa_kelas2.pdf-0159-12.png>)


![Gambar sumber soal 30](<../images/kelas2_panduan_siswa_kelas2.pdf-0159-13.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `Gambar 2 (segi enam memanjang)`.
Solusi minimum hasil AI: Seperempat (1/4) adalah bagian dari keseluruhan yang dibagi menjadi 4 bagian yang sama besar. Hanya Gambar 2 yang memiliki pembagian simetris di tengah sehingga keempat bagiannya sama besar.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-11.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-12.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-13.png. Transkripsi visual: Terdapat empat gambar bangun datar yang dibagi menjadi empat bagian dengan garis. Gambar 1 adalah segitiga dengan garis pembagi yang tidak simetris. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis tegak dan mendatar tepat di tengah, menghasilkan empat bagian sama besar. Gambar 3 adalah bentuk anak panah dengan pembagian tidak simetris. Gambar 4 adalah persegi panjang dengan pembagian petak yang tidak sama besar.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01b99c43bc57acaee5d64141d3bde9570d1b215af90c903393dee9d3a107c21c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 5962 |
| 2 | success | valid / verified | applying | conceptual | Medium | 5896 |
| 3 | success | valid / verified | applying | conceptual | Medium | 5893 |

Run 1 — solusi: Seperempat (1/4) adalah bagian dari keseluruhan yang dibagi menjadi 4 bagian yang sama besar. Hanya Gambar 2 yang memiliki pembagian simetris di tengah sehingga keempat bagiannya sama besar.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep pecahan sederhana (seperempat) dan menerapkannya untuk membedakan antara pembagian yang sama besar dan tidak sama besar pada berbagai bentuk bangun datar.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang dimaksud dengan 'seperempat' (bagian yang sama besar dari keseluruhan), bukan sekadar menghafal fakta atau prosedur algoritma.. Bukti: seperempat dari Benda Utuh
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk membedakan konsep pecahan yang benar dari pengecoh visual. Meskipun konsepnya dasar, siswa harus melakukan analisis visual pada empat bentuk yang berbeda, yang merupakan tugas rutin untuk kelas 2.. Bukti: Perhatikan gambar yang diwarnai berikut.; Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu mengidentifikasi pecahan sederhana pada bentuk geometris. Soal ini menuntut ketelitian visual untuk membedakan pembagian yang sama besar (seperempat) dengan pembagian yang tidak sama besar. |

Run 2 — solusi: Identifikasi gambar yang memiliki empat bagian dengan luas yang sama besar. Hanya gambar 2 yang memenuhi syarat ini.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep pecahan (seperempat) untuk membedakan antara pembagian wilayah yang sama besar dan tidak sama besar pada berbagai bentuk geometri.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' (bagian yang sama besar dari keseluruhan), bukan sekadar menghafal fakta atau prosedur rutin.. Bukti: menunjukkan seperempat
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan diskriminasi visual terhadap konsep pecahan pada berbagai bentuk. Ini adalah tugas rutin untuk kelas 2, namun memerlukan ketelitian visual.. Bukti: Perhatikan gambar yang diwarnai berikut.; Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu mengidentifikasi pecahan sederhana secara visual. Tugas ini melibatkan pembandingan visual yang sesuai dengan tingkat kognitif mereka. |

Run 3 — solusi: Gambar 2 (segi enam) adalah satu-satunya bangun yang terbagi menjadi empat bagian dengan luas yang sama besar (seperempat).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep pecahan (seperempat) untuk mengidentifikasi representasi visual yang tepat di antara beberapa pilihan yang tidak tepat.. Bukti: Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' (bagian yang sama besar dari keseluruhan).. Bukti: menunjukkan seperempat
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium untuk kelas 2 karena siswa tidak hanya sekadar mengenali pecahan, tetapi harus membedakan antara pembagian yang sama besar (seperempat) dan pembagian yang tidak sama besar (distraktor visual).. Bukti: Perhatikan gambar yang diwarnai berikut; Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu membedakan pembagian wilayah yang sama besar dan tidak sama besar secara visual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 181/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.005430; applying=0.994570; reasoning=0.000000 | applying | 0.994570 | 0.030708 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004583; conceptual=0.990325; procedural=0.005093; metacognitive=0.000000 | conceptual | 0.990325 | 0.044145 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.718635; Medium=0.274465; Hard=0.006900 | Easy | 0.718635 | 0.570390 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.994570; −Σp ln(p) = 0.033736; H = 0.033736/ln(3) = 0.030708; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.990325; −Σp ln(p) = 0.061197; H = 0.061197/ln(4) = 0.044145; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.718635; −Σp ln(p) = 0.626638; H = 0.626638/ln(3) = 0.570390; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Seperempat dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar yang diwarnai berikut. Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat. Berilah tanda silang pada gambar yang tidak menunjukkan seperempat.

Berilah tanda centang (✓) pada gambar yang menunjukkan seperempat.
Pilihan: A. Gambar 3 (bentuk anak panah)
B. Gambar 1 (segitiga)
C. Gambar 4 (kotak berpetak)
D. Gambar 2 (segi enam memanjang)
Transkripsi visual: Terdapat empat gambar bangun datar yang dibagi menjadi empat bagian dengan garis. Gambar 1 adalah segitiga dengan garis pembagi yang tidak simetris. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis tegak dan mendatar tepat di tengah, menghasilkan empat bagian sama besar. Gambar 3 adalah bentuk anak panah dengan pembagian tidak simetris. Gambar 4 adalah persegi panjang dengan pembagian petak yang tidak sama besar.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `bdbd4e9367baef3f90950f22`

Perhatikan bagian yang diwarnai pada gambar berikut. Kelompokkan gambar yang menunjukkan seperempat dan bukan seperempat. Tuliskan huruf-hurufnya ke dalam tabel berikut.<br><br>Manakah yang menunjukkan seperempat?

| Opsi | Isi |
|---|---|
| A | D (persegi, empat bagian sama besar) |
| B | E (bintang, ujung kecil diwarnai) |
| C | A (segitiga utuh, tidak dibagi) |
| D | C (persegi panjang, dua bagian sama besar) |

![Gambar sumber soal 31](<../images/kelas2_panduan_siswa_kelas2.pdf-0160-01.png>)


![Gambar sumber soal 31](<../images/kelas2_panduan_siswa_kelas2.pdf-0160-02.png>)


![Gambar sumber soal 31](<../images/kelas2_panduan_siswa_kelas2.pdf-0160-03.png>)


Kunci sumber: `A`; status AI: `conflict`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Seperempat adalah satu bagian dari empat bagian yang sama besar. Gambar C (lingkaran) dan D (persegi panjang) menunjukkan satu bagian diarsir dari empat bagian yang sama besar. Kunci sumber A salah karena gambar A (bintang) tidak dibagi menjadi empat bagian sama besar.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0160-01.png, images/kelas2_panduan_siswa_kelas2.pdf-0160-02.png, images/kelas2_panduan_siswa_kelas2.pdf-0160-03.png. Transkripsi visual: Terdapat 8 gambar yang diberi label huruf A sampai H. Gambar C adalah lingkaran yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir (seperempat). Gambar D adalah persegi panjang yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir (seperempat). Gambar lainnya tidak menunjukkan seperempat yang tepat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5082fcb83281b2b7f76d8f57f1bf8fb461462d67717cc12825698fb7dfc025c9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / conflict | knowing | conceptual | Easy | 4785 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 4760 |
| 3 | success | valid / conflict | knowing | conceptual | Easy | 4839 |

Run 1 — solusi: Seperempat didefinisikan sebagai satu bagian dari empat bagian yang sama besar. Pada gambar, lingkaran C dan lingkaran G (yang berlabel C pada pilihan) menunjukkan satu bagian diarsir dari empat bagian yang sama besar. Kunci sumber A (persegi) tidak ada dalam pilihan gambar yang relevan dengan label C.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali representasi visual dari pecahan seperempat (satu dari empat bagian sama besar) di antara berbagai bentuk, yang merupakan proses pengenalan konsep dasar.. Bukti: Kelompokkan gambar yang menunjukkan seperempat dan bukan seperempat
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep pecahan seperempat sebagai bagian dari keseluruhan yang dibagi sama besar.. Bukti: Kelompokkan gambar yang menunjukkan seperempat
- Intended difficulty `classify/Easy`: Soal ini meminta identifikasi visual sederhana dari konsep pecahan yang sudah umum diajarkan di kelas 2.. Bukti: Kelompokkan gambar yang menunjukkan seperempat dan bukan seperempat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian benda utuh menjadi bagian-bagian sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan pengenalan visual terhadap konsep pecahan sederhana tanpa perhitungan kompleks. |

Run 2 — solusi: Seperempat berarti satu bagian dari empat bagian yang sama besar. Gambar C adalah lingkaran yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir, sehingga C menunjukkan seperempat.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali representasi visual dari pecahan seperempat (satu dari empat bagian yang sama besar) di antara berbagai bentuk geometri.. Bukti: Kelompokkan gambar yang menunjukkan seperempat
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep pecahan seperempat sebagai bagian dari keseluruhan yang dibagi sama besar.. Bukti: Kelompokkan gambar yang menunjukkan seperempat
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengidentifikasi representasi visual pecahan sederhana. Ini adalah tugas rutin untuk kelas 2.. Bukti: Kelompokkan gambar yang menunjukkan seperempat dan bukan seperempat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual pecahan dasar tanpa perhitungan kompleks. |

Run 3 — solusi: Seperempat adalah satu bagian dari empat bagian yang sama besar. Gambar C adalah lingkaran yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir, sehingga C menunjukkan seperempat.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali representasi visual dari pecahan seperempat (satu dari empat bagian sama besar) di antara pilihan yang ada. Ini adalah proses pengenalan konsep dasar pecahan.. Bukti: Kelompokkan gambar yang menunjukkan seperempat dan bukan seperempat; Manakah yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep pecahan sebagai bagian dari keseluruhan yang dibagi sama besar.. Bukti: seperempat dari benda utuh; bagian yang diwarnai
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan pengenalan visual sederhana terhadap konsep pecahan seperempat.. Bukti: Kelompokkan gambar yang menunjukkan seperempat; Manakah yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian benda menjadi bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan identifikasi visual langsung dari konsep pecahan yang sudah dipelajari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `6114`.
Konten: `valid`; kunci: `conflict`; masalah: Terdapat ketidaksesuaian antara kunci jawaban sumber (A) dengan analisis visual gambar. Gambar A (bintang) tidak menunjukkan seperempat. Gambar C (lingkaran) secara visual jelas menunjukkan seperempat (satu dari empat bagian sama besar).; Pilihan jawaban pada soal (A, B, C, D) tidak secara eksplisit merujuk pada label huruf di bawah gambar (A, B, C, D, E, F, G, H) secara konsisten, menyebabkan ambiguitas bagi siswa..
- Domain kognitif `knowing`: Siswa diminta untuk mengenali representasi visual dari konsep pecahan seperempat di antara berbagai bentuk geometri, yang merupakan proses pengenalan konsep dasar.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang apa yang dimaksud dengan 'seperempat' sebagai bagian dari keseluruhan yang dibagi sama besar.
- Intended difficulty `Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan pengenalan visual sederhana terhadap konsep pecahan seperempat tanpa perhitungan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian benda utuh menjadi bagian-bagian sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan pengenalan visual terhadap konsep pecahan sederhana. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 171/256; truncation: `False`.

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
Soal: Perhatikan bagian yang diwarnai pada gambar berikut. Kelompokkan gambar yang menunjukkan seperempat dan bukan seperempat. Tuliskan huruf-hurufnya ke dalam tabel berikut.

Manakah yang menunjukkan seperempat?
Pilihan: A. D (persegi, empat bagian sama besar)
B. E (bintang, ujung kecil diwarnai)
C. A (segitiga utuh, tidak dibagi)
D. C (persegi panjang, dua bagian sama besar)
Transkripsi visual: Terdapat 8 gambar yang diberi label huruf A sampai H. Gambar C adalah lingkaran yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir (seperempat). Gambar D adalah persegi panjang yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir (seperempat). Gambar lainnya tidak menunjukkan seperempat yang tepat.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `valid`. Catatan konten: Terdapat ketidaksesuaian antara kunci jawaban sumber (A) dengan analisis visual gambar. Gambar A (bintang) tidak menunjukkan seperempat. Gambar C (lingkaran) secara visual jelas menunjukkan seperempat (satu dari empat bagian sama besar).; Pilihan jawaban pada soal (A, B, C, D) tidak secara eksplisit merujuk pada label huruf di bawah gambar (A, B, C, D, E, F, G, H) secara konsisten, menyebabkan ambiguitas bagi siswa..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `1622e07bf377db746a052549`

Kerjakan soal-soal berikut secara berpasangan. Amati setiap gambar berikut.<br><br>Berat 1 pepaya adalah .... manggis.

| Opsi | Isi |
|---|---|
| A | 3 manggis |
| B | 2 manggis |
| C | 8 manggis |
| D | 4 manggis |

![Gambar sumber soal 32](<../images/kelas2_panduan_siswa_kelas2.pdf-0188-04.png>)


![Gambar sumber soal 32](<../images/kelas2_panduan_siswa_kelas2.pdf-0188-05.png>)


![Gambar sumber soal 32](<../images/kelas2_panduan_siswa_kelas2.pdf-0188-06.png>)


![Gambar sumber soal 32](<../images/kelas2_panduan_siswa_kelas2.pdf-0188-07.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `4 manggis`.
Solusi minimum hasil AI: 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 1 pepaya = 2 x 2 manggis = 4 manggis.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0188-04.png, images/kelas2_panduan_siswa_kelas2.pdf-0188-05.png, images/kelas2_panduan_siswa_kelas2.pdf-0188-06.png, images/kelas2_panduan_siswa_kelas2.pdf-0188-07.png. Transkripsi visual: Gambar 1 menunjukkan timbangan seimbang dengan 1 pepaya di satu sisi dan 2 mangga di sisi lain. Gambar 2 menunjukkan timbangan seimbang dengan 1 mangga di satu sisi dan 2 manggis di sisi lain. Soal menanyakan berat 1 pepaya dalam satuan manggis.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a2c608246483f2c454836f4ee18cd9fe49e7a43166bfbfe1d59d8034dfb0c948`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 6526 |
| 2 | success | valid / verified | applying | conceptual | Medium | 5780 |
| 3 | success | valid / verified | applying | conceptual | Medium | 6918 |

Run 1 — solusi: 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 1 pepaya = 2 x 2 manggis = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan dua hubungan kesetaraan yang diberikan untuk menentukan hubungan antara dua objek yang tidak dibandingkan secara langsung.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang prinsip kesetaraan (ekuivalensi) dalam pengukuran berat.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah substitusi rutin. Tingkat kesulitan menengah karena siswa harus menghubungkan dua informasi terpisah.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang timbangan dan konsep kesetaraan berat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah belajar perbandingan berat, namun melakukan substitusi dua langkah adalah tantangan yang sesuai untuk tingkat menengah. |

Run 2 — solusi: Jika 1 pepaya = 2 mangga, dan 1 mangga = 2 manggis, maka 1 pepaya = 2 x 2 manggis = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan dua informasi yang diberikan secara terpisah untuk menyimpulkan hubungan antara pepaya dan manggis. Ini melibatkan penerapan konsep kesetaraan dalam dua langkah.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis; Berat 1 pepaya adalah .... manggis
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip kesetaraan dan substitusi (konsep) dalam konteks pengukuran berat.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah penalaran (transitif) yang mungkin sedikit menantang bagi siswa kelas 2, namun prosedurnya tetap rutin.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang timbangan sebagai alat ukur kesetaraan dan perkalian dasar (2x2). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, menghubungkan dua kesetaraan (transitif) adalah langkah yang tepat untuk tingkat kesulitan menengah. |

Run 3 — solusi: 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 1 pepaya = 2 x 2 manggis = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan hubungan transitif sederhana (substitusi) untuk menghubungkan dua informasi yang diberikan dalam konteks rutin.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Dimensi pengetahuan `classify/conceptual`: Memahami hubungan kesetaraan antar objek (konsep berat) dan menerapkannya untuk menyelesaikan masalah.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah penalaran (substitusi) yang rutin bagi siswa kelas 2, namun melibatkan perpindahan representasi visual ke numerik.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang timbangan dan perkalian sederhana atau penjumlahan berulang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, menghubungkan dua fakta kesetaraan adalah tugas yang menantang namun sesuai dengan kurikulum pengenalan pengukuran berat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 116/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000003; applying=0.999997; reasoning=0.000000 | applying | 0.999997 | 0.000041 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.038356; conceptual=0.941846; procedural=0.019798; metacognitive=0.000000 | conceptual | 0.941846 | 0.186938 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.828201; Medium=0.168076; Hard=0.003723 | Easy | 0.828201 | 0.433888 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999997; −Σp ln(p) = 0.000045; H = 0.000045/ln(3) = 0.000041; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.941846; −Σp ln(p) = 0.259152; H = 0.259152/ln(4) = 0.186938; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.828201; −Σp ln(p) = 0.476675; H = 0.476675/ln(3) = 0.433888; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Kerjakan soal-soal berikut secara berpasangan. Amati setiap gambar berikut.

Berat 1 pepaya adalah .... manggis.
Pilihan: A. 3 manggis
B. 2 manggis
C. 8 manggis
D. 4 manggis
Transkripsi visual: Gambar 1 menunjukkan timbangan seimbang dengan 1 pepaya di satu sisi dan 2 mangga di sisi lain. Gambar 2 menunjukkan timbangan seimbang dengan 1 mangga di satu sisi dan 2 manggis di sisi lain. Soal menanyakan berat 1 pepaya dalam satuan manggis.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `4cba291cad9e7ab23945d506`

Perhatikan gambar di bawah ini.<br><br>Berat 1 buah jeruk sama dengan .... stroberi.

| Opsi | Isi |
|---|---|
| A | 4 stroberi |
| B | 2 stroberi |
| C | 1 stroberi |
| D | 3 stroberi |

![Gambar sumber soal 33](<../images/kelas2_panduan_siswa_kelas2.pdf-0200-01.png>)


![Gambar sumber soal 33](<../images/kelas2_panduan_siswa_kelas2.pdf-0200-02.png>)


![Gambar sumber soal 33](<../images/kelas2_panduan_siswa_kelas2.pdf-0200-03.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Berdasarkan prinsip timbangan, berat 1 jeruk setara dengan jumlah stroberi yang ada di sisi lain timbangan. Kunci B (2) adalah jawaban yang logis untuk soal perbandingan berat sederhana.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0200-01.png, images/kelas2_panduan_siswa_kelas2.pdf-0200-02.png, images/kelas2_panduan_siswa_kelas2.pdf-0200-03.png. Transkripsi visual: The provided images are icons (a green fruit, a blue circle, a pink rectangle) and do not contain the actual problem image (a balance scale with fruit). However, based on the problem text and the provided options, the task is a standard measurement problem where a student must count objects on a balance scale. The provided answer key B (2) is consistent with the logic of such problems.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2b1ceb00f8e24791f5b9ce497c1f2d64b3b804145fe31c8448879c2c7a18e6ac`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | insufficient_evidence / unverifiable | — | — | — | 4393 |
| 2 | success | insufficient_evidence / unverifiable | — | — | — | 4426 |
| 3 | success | valid / unverifiable | — | — | — | 4388 |

Run 1 — solusi: Tidak dapat diverifikasi karena gambar pendukung soal tidak tersedia.
- Domain kognitif `abstain/None`: Karena gambar yang menjadi basis utama penyelesaian soal tidak tersedia, domain kognitif tidak dapat ditentukan secara akurat.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Karena gambar yang menjadi basis utama penyelesaian soal tidak tersedia, dimensi pengetahuan tidak dapat ditentukan secara akurat.. Bukti: 
- Intended difficulty `abstain/None`: Karena gambar yang menjadi basis utama penyelesaian soal tidak tersedia, tingkat kesulitan tidak dapat ditentukan secara akurat.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 2 — solusi: Tidak dapat diverifikasi karena gambar pendukung tidak tersedia.
- Domain kognitif `abstain/None`: Soal tidak dapat dianalisis karena gambar yang menjadi basis utama pertanyaan tidak tersedia.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Soal tidak dapat dianalisis karena gambar yang menjadi basis utama pertanyaan tidak tersedia.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak dapat dianalisis karena gambar yang menjadi basis utama pertanyaan tidak tersedia.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

Run 3 — solusi: Soal tidak dapat diselesaikan karena gambar yang diperlukan (timbangan dengan jeruk dan stroberi) tidak tersedia dalam lampiran.
- Domain kognitif `abstain/None`: Bukti visual yang diperlukan untuk menjawab soal (gambar timbangan) tidak tersedia, sehingga domain kognitif tidak dapat ditentukan secara akurat.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Bukti visual yang diperlukan untuk menjawab soal (gambar timbangan) tidak tersedia, sehingga dimensi pengetahuan tidak dapat ditentukan secara akurat.. Bukti: 
- Intended difficulty `abstain/None`: Bukti visual yang diperlukan untuk menjawab soal (gambar timbangan) tidak tersedia, sehingga tingkat kesulitan tidak dapat ditentukan secara akurat.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / adjudicated | knowing |
| Dimensi pengetahuan | {} | no_consensus / adjudicated | conceptual |
| Intended difficulty | {} | no_consensus / adjudicated | Easy |

Adjudikasi AI: `success`; token `5372`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk membaca informasi dari representasi visual (timbangan) dan melakukan proses langsung untuk menentukan kesetaraan berat.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konsep dasar pengukuran berat melalui perbandingan visual.
- Intended difficulty `Easy`: Soal ini merupakan prosedur familiar bagi siswa kelas 2, yaitu membaca timbangan sederhana dengan satu keputusan utama (menghitung jumlah objek).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret dan memahami konsep kesetaraan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan objek konkret dan konsep dasar pengukuran yang sering diajarkan di tingkat tersebut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 171/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000148; applying=0.999852; reasoning=0.000000 | applying | 0.999852 | 0.001324 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004875; conceptual=0.969131; procedural=0.025993; metacognitive=0.000000 | conceptual | 0.969131 | 0.109078 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.694227; Medium=0.291461; Hard=0.014312 | Easy | 0.694227 | 0.613017 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999852; −Σp ln(p) = 0.001454; H = 0.001454/ln(3) = 0.001324; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.969131; −Σp ln(p) = 0.151215; H = 0.151215/ln(4) = 0.109078; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.694227; −Σp ln(p) = 0.673468; H = 0.673468/ln(3) = 0.613017; T = 0.953328.


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
Transkripsi visual: The provided images are icons (a green fruit, a blue circle, a pink rectangle) and do not contain the actual problem image (a balance scale with fruit). However, based on the problem text and the provided options, the task is a standard measurement problem where a student must count objects on a balance scale. The provided answer key B (2) is consistent with the logic of such problems.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `dd3cb9360df4fe034e2f2480`

Urutkan gambar sesuai dengan waktu kegiatan.<br><br>Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

| Opsi | Isi |
|---|---|
| A | menyikat gigi, bangun tidur, makan siang, bermain bola |
| B | bangun tidur, menyikat gigi, makan siang, bermain bola |
| C | bermain bola, makan siang, menyikat gigi, bangun tidur |
| D | bangun tidur, makan siang, menyikat gigi, bermain bola |

![Gambar sumber soal 34](<../images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Urutan waktu berdasarkan jam: 06.00 (C: bangun tidur) -> 08.00 (D: menyikat gigi) -> 12.00 (B: makan siang) -> 16.00 (A: bermain bola). Urutan yang benar adalah C, D, B, A.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png. Transkripsi visual: Terdapat empat gambar kegiatan dengan jam analog di sampingnya: Gambar A (bermain bola, jam menunjukkan pukul 4:00), Gambar B (makan siang, jam menunjukkan pukul 12:00), Gambar C (bangun tidur, jam menunjukkan pukul 6:00), Gambar D (menyikat gigi, jam menunjukkan pukul 8:00).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0abca154fe57e0a1527cd7b7802aba716e55f5a8bbc1231971b26884071c554a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Easy | 2614 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2597 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2590 |

Run 1 — solusi: Urutan kronologis kegiatan sehari-hari adalah: bangun tidur (pukul 06.00) -> menyikat gigi (pukul 08.00) -> makan siang (pukul 12.00) -> bermain bola (pukul 16.00). Sesuai dengan urutan C, D, B, A.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi dari representasi visual (jam dan aktivitas) untuk menyusun urutan kronologis yang logis, yang merupakan proses penalaran sederhana.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam kehidupan sehari-hari dan bagaimana waktu tersebut direpresentasikan dalam jam analog.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena aktivitas yang ditampilkan sangat rutin dan familiar bagi siswa kelas 2. Tidak ada jebakan kompleks, hanya perlu mengurutkan empat kejadian berdasarkan waktu yang tertera pada jam.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog sederhana (jam tepat) dan pemahaman urutan kegiatan harian. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan membaca jam dan urutan waktu harian. Soal ini menggunakan konteks yang sangat dekat dengan keseharian mereka. |

Run 2 — solusi: Mengurutkan kegiatan berdasarkan waktu pada jam: 06.00 (bangun tidur) -> 08.00 (menyikat gigi) -> 12.00 (makan siang) -> 16.00 (bermain bola). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi waktu pada jam analog dan mengaitkannya dengan urutan logis kegiatan sehari-hari. Ini adalah proses menerapkan pemahaman konsep waktu ke dalam situasi rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pengetahuan konseptual tentang urutan waktu dalam sehari dan cara membaca jam analog untuk mengkategorikan kegiatan.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengurutkan empat kejadian berdasarkan informasi waktu yang eksplisit pada jam analog. Ini adalah tugas rutin yang sesuai untuk kelas 2.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog (pukul tepat) dan memahami urutan waktu sehari-hari. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menguji kemampuan dasar membaca jam dan mengurutkan kejadian sehari-hari yang familiar. |

Run 3 — solusi: Urutan kronologis berdasarkan waktu pada jam: 06.00 (bangun tidur) -> 08.00 (menyikat gigi) -> 12.00 (makan siang) -> 16.00 (bermain bola).
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan kejadian berdasarkan waktu yang tertera pada jam analog dan konteks kegiatan sehari-hari. Ini adalah proses menerapkan pemahaman konsep waktu ke dalam situasi rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam satu hari dan bagaimana jam analog merepresentasikan waktu tersebut.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena menggunakan konteks kegiatan sehari-hari yang sangat familiar bagi siswa kelas 2 dan jam analog yang menunjukkan waktu tepat (jam bulat).. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog (waktu tepat) dan memahami urutan kegiatan sehari-hari. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggabungkan literasi waktu dasar dengan urutan logis kegiatan sehari-hari yang sudah dikenal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4024`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pemahaman tentang urutan waktu kronologis dan kemampuan membaca jam analog untuk mengurutkan kejadian sehari-hari. Ini adalah proses penerapan konsep pada situasi rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam satu hari dan bagaimana jam analog merepresentasikan waktu tersebut.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena menggunakan konteks kegiatan sehari-hari yang sangat familiar bagi siswa kelas 2 dan jam analog yang menunjukkan waktu tepat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog (waktu tepat) dan memahami urutan kegiatan sehari-hari. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggabungkan literasi waktu dasar dengan urutan logis kegiatan sehari-hari yang sudah dikenal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 177/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.042835; applying=0.957165; reasoning=0.000000 | applying | 0.957165 | 0.160976 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.021018; conceptual=0.975994; procedural=0.002987; metacognitive=0.000000 | conceptual | 0.975994 | 0.088194 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.632271; Medium=0.359357; Hard=0.008372 | Easy | 0.632271 | 0.635054 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.957165; −Σp ln(p) = 0.176850; H = 0.176850/ln(3) = 0.160976; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.975994; −Σp ln(p) = 0.122263; H = 0.122263/ln(4) = 0.088194; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.632271; −Σp ln(p) = 0.697679; H = 0.697679/ln(3) = 0.635054; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Waktu
Tipe soal: multiple_choice
Stimulus: -
Soal: Urutkan gambar sesuai dengan waktu kegiatan.

Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
Pilihan: A. menyikat gigi, bangun tidur, makan siang, bermain bola
B. bangun tidur, menyikat gigi, makan siang, bermain bola
C. bermain bola, makan siang, menyikat gigi, bangun tidur
D. bangun tidur, makan siang, menyikat gigi, bermain bola
Transkripsi visual: Terdapat empat gambar kegiatan dengan jam analog di sampingnya: Gambar A (bermain bola, jam menunjukkan pukul 4:00), Gambar B (makan siang, jam menunjukkan pukul 12:00), Gambar C (bangun tidur, jam menunjukkan pukul 6:00), Gambar D (menyikat gigi, jam menunjukkan pukul 8:00).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `c0080230ef4ab5e5b0a07c55`

Beri tanda centang ( ) pada kegiatan yang lebih lama.<br><br>Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

| Opsi | Isi |
|---|---|
| A | Bermain bola |
| B | Mencuci tangan |
| C | Sarapan |
| D | Menyisir rambut |

![Gambar sumber soal 35](<../images/kelas2_panduan_siswa_kelas2.pdf-0198-00.png>)


![Gambar sumber soal 35](<../images/kelas2_panduan_siswa_kelas2.pdf-0198-01.png>)


![Gambar sumber soal 35](<../images/kelas2_panduan_siswa_kelas2.pdf-0198-02.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bermain bola adalah aktivitas yang durasinya lebih lama dibandingkan mencuci tangan.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0198-00.png, images/kelas2_panduan_siswa_kelas2.pdf-0198-01.png, images/kelas2_panduan_siswa_kelas2.pdf-0198-02.png. Transkripsi visual: Gambar menunjukkan dua aktivitas: mencuci tangan (di wastafel) dan bermain bola (di lapangan). Terdapat kotak centang di samping teks 'Mencuci tangan' dan 'Bermain bola'. Soal meminta siswa memilih kegiatan yang durasinya lebih lama.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `71a5bfbe3e9958f792cf790cf42daaef03946ded52be944718f4315abec052de`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 4605 |
| 2 | success | valid / verified | applying | conceptual | Easy | 4623 |
| 3 | success | valid / verified | applying | conceptual | Easy | 4602 |

Run 1 — solusi: Bermain bola adalah aktivitas yang durasinya lebih lama dibandingkan mencuci tangan.
- Domain kognitif `classify/applying`: Siswa diminta membandingkan durasi dua aktivitas sehari-hari yang familiar. Ini adalah proses menerapkan pemahaman konsep durasi waktu pada situasi rutin.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep tentang durasi atau lamanya waktu suatu kejadian, yang merupakan pengetahuan konseptual.. Bukti: Kegiatan manakah yang lebih lama
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, menggunakan konteks aktivitas sehari-hari yang sangat familiar, dan tidak memerlukan perhitungan atau strategi kompleks.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang durasi waktu (lama vs sebentar) dalam konteks aktivitas sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena membandingkan durasi aktivitas fisik yang umum dilakukan anak-anak tanpa memerlukan alat ukur waktu formal. |

Run 2 — solusi: Bermain bola membutuhkan durasi waktu yang lebih panjang dibandingkan mencuci tangan.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan durasi dua aktivitas sehari-hari yang familiar. Ini adalah proses menerapkan konsep durasi waktu pada situasi rutin.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang durasi waktu (konsep 'lebih lama' vs 'lebih sebentar') dalam konteks aktivitas sehari-hari.. Bukti: Kegiatan manakah yang lebih lama
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan perbandingan durasi aktivitas yang sangat umum dan mudah dibedakan.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep durasi waktu (lama/sebentar) dalam kehidupan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena membandingkan durasi aktivitas fisik yang sangat kontras durasinya. |

Run 3 — solusi: Bermain bola membutuhkan durasi waktu yang lebih lama dibandingkan dengan mencuci tangan.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan durasi dua aktivitas sehari-hari yang familiar. Ini adalah proses menerapkan pemahaman konsep waktu (durasi) ke dalam situasi rutin.. Bukti: Beri tanda centang ( ) pada kegiatan yang lebih lama.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang durasi waktu (konsep 'lebih lama' vs 'lebih sebentar') dalam konteks aktivitas sehari-hari.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, menggunakan konteks yang sangat familiar dengan beban kognitif yang rendah.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang durasi waktu (lama/sebentar) dalam kehidupan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena membandingkan durasi aktivitas yang sangat umum dan jelas perbedaannya. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 119/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000006; applying=0.999994; reasoning=0.000000 | applying | 0.999994 | 0.000068 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.039366; conceptual=0.955552; procedural=0.005082; metacognitive=0.000000 | conceptual | 0.955552 | 0.142561 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.764048; Medium=0.232324; Hard=0.003628 | Easy | 0.764048 | 0.514392 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999994; −Σp ln(p) = 0.000075; H = 0.000075/ln(3) = 0.000068; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.955552; −Σp ln(p) = 0.197631; H = 0.197631/ln(4) = 0.142561; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.764048; −Σp ln(p) = 0.565117; H = 0.565117/ln(3) = 0.514392; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Waktu
Tipe soal: multiple_choice
Stimulus: -
Soal: Beri tanda centang ( ) pada kegiatan yang lebih lama.

Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
Pilihan: A. Bermain bola
B. Mencuci tangan
C. Sarapan
D. Menyisir rambut
Transkripsi visual: Gambar menunjukkan dua aktivitas: mencuci tangan (di wastafel) dan bermain bola (di lapangan). Terdapat kotak centang di samping teks 'Mencuci tangan' dan 'Bermain bola'. Soal meminta siswa memilih kegiatan yang durasinya lebih lama.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `5202d6bd8064acc3f5637504`

1. Hitunglah banyak benda berikut. Contoh: 5 puluhan = 50 Jadi, ada 50 buah rambutan. Lakukan seperti contoh.<br><br>a. .... puluhan = .... Jadi, ada .... buah jeruk.

| Opsi | Isi |
|---|---|
| A | 7 puluhan = 70 (70 buah jeruk) |
| B | 6 puluhan = 60 (60 buah jeruk) |
| C | 6 satuan = 6 (6 buah jeruk) |
| D | 5 puluhan = 50 (50 buah jeruk) |

![Gambar sumber soal 36](<../images/kelas2_panduan_siswa_kelas2.pdf-0215-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `6 puluhan = 60 (60 buah jeruk)`.
Solusi minimum hasil AI: Terdapat 6 keranjang, masing-masing berisi 10 jeruk, sehingga 6 puluhan = 60.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0215-04.png. Transkripsi visual: Gambar menunjukkan 6 keranjang jeruk. Setiap keranjang berisi 10 buah jeruk.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f40287e49ea8b349a3059853bac253f8a1c484963700bcd0480ac31317c60f94`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2525 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2549 |
| 3 | success | valid / verified | applying | procedural | Easy | 2553 |

Run 1 — solusi: Menghitung jumlah keranjang (6) dan mengalikannya dengan nilai puluhan (10) menghasilkan 60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman konsep nilai tempat (puluhan) pada situasi rutin yang sudah diberikan contohnya.. Bukti: Hitunglah banyak benda berikut; 6 puluhan = 60
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pengelompokan benda dalam puluhan.. Bukti: 5 puluhan = 50; 6 puluhan = 60
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu meniru pola yang sudah diberikan (contoh) untuk menghitung jumlah kelompok benda.. Bukti: Lakukan seperti contoh; 6 keranjang jeruk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang dan memahami konsep puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan representasi visual konkret dan pola yang sudah dicontohkan. |

Run 2 — solusi: Terdapat 6 kelompok (keranjang) yang masing-masing berisi 10 jeruk, sehingga 6 puluhan sama dengan 60.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali dan menerapkan konsep pengelompokan benda ke dalam puluhan secara langsung sesuai contoh yang diberikan.. Bukti: Hitunglah banyak benda berikut; 6 puluhan = 60
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang sistem nilai tempat (puluhan) dan bagaimana mengelompokkan objek ke dalam satuan puluhan.. Bukti: 5 puluhan = 50; 6 puluhan = 60
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan mengikuti pola contoh yang sudah diberikan sebelumnya.. Bukti: Lakukan seperti contoh; 6 puluhan = 60

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
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan pengenalan visual terhadap kelompok sepuluh dan konversi ke angka puluhan. |

Run 3 — solusi: Terdapat 6 keranjang, setiap keranjang berisi 10 jeruk. Maka 6 puluhan = 60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur menghitung kelompok sepuluh (puluhan) yang sudah dicontohkan sebelumnya ke dalam situasi baru yang serupa.. Bukti: Hitunglah banyak benda berikut; Lakukan seperti contoh
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang sistem nilai tempat (puluhan) dan algoritma dasar untuk menghitung jumlah benda dengan mengelompokkannya menjadi puluhan.. Bukti: 5 puluhan = 50; .... puluhan = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan mengikuti pola contoh yang diberikan secara eksplisit.. Bukti: Hitunglah banyak benda berikut; 6 keranjang jeruk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda dan memahami konsep sepuluh sebagai satu satuan puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada penguatan konsep nilai tempat dasar dengan bantuan visual yang konkret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3770`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pengelompokan benda ke dalam puluhan yang sudah dicontohkan sebelumnya pada situasi rutin yang baru.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konsep nilai tempat (puluhan) dan bagaimana mengelompokkan objek ke dalam satuan puluhan.
- Intended difficulty `Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan mengikuti pola contoh yang diberikan secara eksplisit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda dan memahami konsep sepuluh sebagai satu satuan puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada penguatan konsep nilai tempat dasar dengan bantuan visual yang konkret. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 145/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.002100; conceptual=0.996788; procedural=0.001111; metacognitive=0.000000 | conceptual | 0.996788 | 0.017108 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.687972; Medium=0.303976; Hard=0.008052 | Easy | 0.687972 | 0.599036 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.996788; −Σp ln(p) = 0.023717; H = 0.023717/ln(4) = 0.017108; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.687972; −Σp ln(p) = 0.658108; H = 0.658108/ln(3) = 0.599036; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Menghitung, Membaca, dan Menulis Bilangan sampai dengan 100
Tipe soal: multiple_choice
Stimulus: -
Soal: 1. Hitunglah banyak benda berikut. Contoh: 5 puluhan = 50 Jadi, ada 50 buah rambutan. Lakukan seperti contoh.

a. .... puluhan = .... Jadi, ada .... buah jeruk.
Pilihan: A. 7 puluhan = 70 (70 buah jeruk)
B. 6 puluhan = 60 (60 buah jeruk)
C. 6 satuan = 6 (6 buah jeruk)
D. 5 puluhan = 50 (50 buah jeruk)
Transkripsi visual: Gambar menunjukkan 6 keranjang jeruk. Setiap keranjang berisi 10 buah jeruk.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `98cb95b9467c6a458263f9f1`

5. Tulislah lambang bilangan sesuai dengan nama bilangannya. d. Tujuh puluh delapan .....

| Opsi | Isi |
|---|---|
| A | 780 |
| B | 87 |
| C | 70 |
| D | 78 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Tujuh puluh delapan terdiri dari 7 puluhan dan 8 satuan, sehingga lambang bilangannya adalah 78.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `96ea5b179c051b2cc8782a0eb5f8c04ee880c9a19a14c24aefada8a3a5849513`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1295 |
| 2 | success | valid / verified | knowing | factual | Easy | 1282 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1294 |

Run 1 — solusi: Tujuh puluh delapan berarti 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nama bilangan dan mengubahnya menjadi lambang bilangan (notasi angka), yang merupakan proses langsung.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. d. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol angka dan bagaimana nama bilangan direpresentasikan dalam sistem bilangan desimal.. Bukti: Tujuh puluh delapan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan konversi langsung dari nama bilangan ke angka tanpa langkah tambahan atau kompleksitas.. Bukti: Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan simbol angka 0-100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD untuk pengenalan lambang bilangan hingga 100. |

Run 2 — solusi: Nama bilangan 'tujuh puluh delapan' terdiri dari 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menuliskan lambang bilangan berdasarkan nama bilangan yang diberikan, yang merupakan proses langsung.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. d. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol atau lambang bilangan (notasi angka) untuk nama bilangan tertentu.. Bukti: Tujuh puluh delapan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan konversi langsung dari nama bilangan ke simbol angka tanpa langkah tambahan.. Bukti: Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa menuliskan lambang bilangan untuk angka di bawah 100. |

Run 3 — solusi: Tujuh puluh delapan berarti 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengubah representasi nama bilangan menjadi lambang bilangan, yang merupakan proses langsung dan rutin.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. d. Tujuh puluh delapan
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara nama bilangan (kata) dan lambang bilangan (simbol numerik) dalam sistem nilai tempat.. Bukti: Tujuh puluh delapan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, hanya melibatkan satu langkah konversi langsung tanpa kompleksitas tambahan.. Bukti: Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD mengenai penulisan lambang bilangan sampai 100. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2460`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan konversi langsung dari representasi verbal (nama bilangan) ke representasi simbolik (lambang bilangan). Ini adalah proses pengenalan dan penulisan fakta dasar.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan tentang simbol angka (lambang bilangan) yang merupakan fakta dasar dalam sistem bilangan desimal.
- Intended difficulty `Easy`: Soal ini bersifat rutin, langsung, dan tidak memerlukan strategi kompleks. Beban kognitif sangat rendah karena hanya melibatkan satu langkah konversi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nama bilangan dan lambang bilangan hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan standar kompetensi kelas 2 SD untuk menuliskan lambang bilangan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 77/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999682; applying=0.000318; reasoning=0.000000 | knowing | 0.999682 | 0.002619 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.650629; conceptual=0.323331; procedural=0.026040; metacognitive=0.000000 | factual | 0.650629 | 0.533591 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.898639; Medium=0.099261; Hard=0.002099 | Easy | 0.898639 | 0.307914 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999682; −Σp ln(p) = 0.002877; H = 0.002877/ln(3) = 0.002619; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.650629; −Σp ln(p) = 0.739714; H = 0.739714/ln(4) = 0.533591; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.898639; −Σp ln(p) = 0.338278; H = 0.338278/ln(3) = 0.307914; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Menghitung, Membaca, dan Menulis Bilangan sampai dengan 100
Tipe soal: multiple_choice
Stimulus: -
Soal: 5. Tulislah lambang bilangan sesuai dengan nama bilangannya. d. Tujuh puluh delapan .....
Pilihan: A. 780
B. 87
C. 70
D. 78
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `f366f15007b61b27653bdf58`

Kira menuliskan satu bilangan.<br><br>Kira berkata, 'Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.' Berapa bilangan yang ditulis Kira?

| Opsi | Isi |
|---|---|
| A | 92 |
| B | 29 |
| C | 12 |
| D | 81 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Misalkan bilangan tersebut adalah 10a + b. Operasi yang dilakukan: (10a + 40) + (b + 3) = 55. Maka 10a + b + 43 = 55. Bilangan awal = 55 - 43 = 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c8f10c00f7efe1007705d05348980356e64e287f4ed93c416bdf1d68588748a6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 1456 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1475 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1460 |

Run 1 — solusi: Misalkan bilangan tersebut adalah 10a + b. Operasi yang dilakukan: (10a + 40) + (b + 3) = 55. Maka 10a + b + 43 = 55. Bilangan awal = 55 - 43 = 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami struktur nilai tempat (puluhan dan satuan) dan melakukan operasi invers untuk menemukan bilangan awal, yang melibatkan penerapan konsep nilai tempat dalam situasi rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur bilangan (puluhan dan satuan) dan bagaimana operasi aritmatika mempengaruhi nilai tempat tersebut.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep nilai tempat dan operasi invers. Bagi siswa kelas 2, ini adalah tugas rutin yang melibatkan pemahaman struktur bilangan tanpa kompleksitas tinggi.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan nilai tempat. Soal ini menuntut pemahaman konsep tersebut secara terbalik, yang sesuai dengan tingkat kemampuan kelas 2. |

Run 2 — solusi: Misalkan bilangan awal adalah 10a + b. Operasi yang dilakukan adalah (10a + 40) + (b + 3) = 55, yang setara dengan 10a + b + 43 = 55. Maka, 10a + b = 55 - 43 = 12.
- Domain kognitif `classify/applying`: Siswa perlu melakukan operasi invers (pengurangan) untuk membalikkan proses penambahan yang diberikan pada nilai tempat puluhan dan satuan, yang merupakan proses applying konsep nilai tempat.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang struktur nilai tempat (puluhan dan satuan) dan bagaimana operasi aritmatika memengaruhi struktur tersebut.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk membalikkan operasi (invers) pada nilai tempat, yang merupakan tantangan kognitif di atas sekadar penjumlahan langsung bagi siswa kelas 2.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 biasanya belajar penjumlahan/pengurangan dasar. Membalikkan operasi pada nilai tempat secara terpisah adalah langkah yang sedikit lebih kompleks daripada soal rutin satu langkah. |

Run 3 — solusi: Misalkan bilangan awal adalah 10a + b. Diketahui (a+4) puluhan dan (b+3) satuan = 55. Maka a+4 = 5 dan b+3 = 5. Didapat a = 1 dan b = 2. Bilangan tersebut adalah 12.
- Domain kognitif `classify/applying`: Siswa perlu melakukan operasi invers (pengurangan) untuk membalikkan proses penambahan yang dijelaskan dalam soal, yang merupakan penerapan konsep nilai tempat.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) dan bagaimana mengubahnya.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep nilai tempat dan operasi invers sederhana. Untuk kelas 2, ini dikategorikan Medium karena siswa harus melakukan penalaran terbalik (reverse thinking) dari hasil akhir ke awal, bukan sekadar operasi hitung langsung.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 biasanya belajar penjumlahan/pengurangan langsung. Soal ini menuntut pemahaman konsep nilai tempat secara terbalik, yang merupakan tantangan kognitif yang sesuai untuk tingkat menengah di kelas 2. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `4a38b766ecd4b82494e8afb8`

5. Aku adalah bilangan. Aku 1 kurangnya dari bilangan 67. Bilangan berapakah aku?

| Opsi | Isi |
|---|---|
| A | 67 |
| B | 66 |
| C | 68 |
| D | 57 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 1 kurang dari 67 adalah 67 - 1 = 66.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1276ca3e81f0d723fabb7e8a81df0afe0f653b5bafe974e362e414669af7cbf9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1259 |
| 2 | success | valid / verified | knowing | factual | Easy | 1276 |
| 3 | success | valid / verified | knowing | factual | Easy | 1783 |

Run 1 — solusi: 1 kurang dari 67 adalah 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar (1 kurangnya) yang merupakan proses langsung dan rutin.. Bukti: 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami konsep urutan bilangan dan fakta dasar pengurangan satu satuan.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu langkah pengurangan sederhana pada bilangan dua digit.. Bukti: 1 kurangnya dari bilangan 67

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
| gradeRelativeRationale | Untuk kelas 2, operasi pengurangan satu satuan dari bilangan dua digit adalah materi standar yang sangat rutin. |

Run 2 — solusi: 1 kurangnya dari 67 berarti 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar (67-1) yang merupakan proses langsung dan rutin.. Bukti: 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dan konsep 'kurang dari' yang merupakan pengetahuan faktual dasar dalam sistem bilangan.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah operasi pengurangan sederhana tanpa kompleksitas tambahan.. Bukti: 1 kurangnya dari bilangan 67

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya melibatkan operasi pengurangan satu satuan pada bilangan dua digit yang familiar. |

Run 3 — solusi: 67 - 1 = 66
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar (1 satuan) pada bilangan yang diberikan. Ini adalah proses langsung yang tidak memerlukan strategi kompleks.. Bukti: 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dan konsep 'kurang dari' yang merupakan fakta dasar dalam sistem bilangan.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya melibatkan satu operasi pengurangan sederhana pada bilangan dua digit. Sangat sesuai untuk standar kelas 2.. Bukti: 1 kurangnya dari bilangan 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep urutan bilangan dan pengurangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 1 satuan adalah keterampilan dasar yang diharapkan dikuasai siswa kelas 2. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 63/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999892; applying=0.000108; reasoning=0.000000 | knowing | 0.999892 | 0.000997 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.441325; conceptual=0.474122; procedural=0.084554; metacognitive=0.000000 | conceptual | 0.474122 | 0.666312 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.806931; Medium=0.190291; Hard=0.002778 | Easy | 0.806931 | 0.459836 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999892; −Σp ln(p) = 0.001096; H = 0.001096/ln(3) = 0.000997; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.474122; −Σp ln(p) = 0.923704; H = 0.923704/ln(4) = 0.666312; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.806931; −Σp ln(p) = 0.505182; H = 0.505182/ln(3) = 0.459836; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 5. Aku adalah bilangan. Aku 1 kurangnya dari bilangan 67. Bilangan berapakah aku?
Pilihan: A. 67
B. 66
C. 68
D. 57
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `874e86479e51d283015833cd`

1. Kira sedang mendata mainan kesukaan teman-temannya. Data yang didapatkan oleh Kira terdapat pada diagram berikut. Lengkapi diagram turus dengan mengisi kolom paling kanan. Diagram Turus Mainan Kesukaan<br><br>\|Mainan\|Turus\|Banyak Anak\|<br>\|---\|---\|---\|<br>\|Mobil-mobilan\|\|…\|<br>\|Boneka\|IIII\|…\|<br>\|Kelereng\|I\|…\|<br>\|Mainan balok\|II\|…\|<br><br>Lengkapi diagram turus dengan mengisi kolom paling kanan. (Mobil-mobilan)

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 6 |
| C | 4 |
| D | 2 |

![Gambar sumber soal 40](<../images/kelas2_panduan_siswa_kelas2.pdf-0246-03.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Terdapat 2 buah mobil-mobilan pada gambar, sehingga kolom 'Banyak Anak' untuk baris 'Mobil-mobilan' diisi dengan angka 2.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0246-03.png. Transkripsi visual: The image shows a girl holding a box with a teddy bear inside. On the floor, there are several toys: two toy cars (one red, one purple), three teddy bears (one purple, one pink, one yellow/blue), several building blocks, and some small balls. The tally chart asks for the count of 'Mobil-mobilan' (toy cars). There are exactly 2 toy cars visible on the floor.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `03deb591fc4f1c1498011717881e7a713c182f0b0a264f1df9c16349f4f469ac`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2656 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2657 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2591 |

Run 1 — solusi: Berdasarkan gambar, terdapat 2 buah mobil-mobilan. Oleh karena itu, kolom 'Banyak Anak' untuk baris 'Mobil-mobilan' harus diisi dengan angka 2.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menghitung objek visual yang konkret dan memindahkan informasi tersebut ke dalam format tabel (diagram turus). Ini adalah proses langsung dalam mengenali dan menghitung objek.. Bukti: Lengkapi diagram turus dengan mengisi kolom paling kanan; Mobil-mobilan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang cara membaca dan mengisi data ke dalam format diagram turus, yang merupakan pengetahuan prosedural dasar dalam statistika tingkat awal.. Bukti: diagram turus; mengisi kolom paling kanan
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta penghitungan objek visual yang jumlahnya sedikit (2 buah) dan memasukkannya ke dalam tabel. Tidak ada manipulasi data yang kompleks.. Bukti: Lengkapi diagram turus; Mobil-mobilan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena melibatkan penghitungan objek nyata dan pengisian tabel sederhana yang merupakan materi standar awal pengolahan data. |

Run 2 — solusi: Berdasarkan gambar, terdapat 2 buah mobil-mobilan. Maka, kolom 'Banyak Anak' untuk baris 'Mobil-mobilan' harus diisi dengan angka 2.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menghitung objek visual dan menerjemahkannya ke dalam bentuk angka pada tabel. Ini adalah proses langsung dalam membaca dan melengkapi data sederhana.. Bukti: Lengkapi diagram turus dengan mengisi kolom paling kanan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang representasi data sederhana (tabel turus) dan kemampuan menghitung objek konkret.. Bukti: Lengkapi diagram turus dengan mengisi kolom paling kanan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan penghitungan objek visual yang sedikit jumlahnya dan memasukkannya ke dalam tabel yang sudah disediakan formatnya.. Bukti: Lengkapi diagram turus dengan mengisi kolom paling kanan; Mobil-mobilan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10 dan memahami tabel sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena melibatkan pengumpulan data visual sederhana yang merupakan materi awal pengenalan data. |

Run 3 — solusi: Berdasarkan gambar, terdapat 2 buah mobil-mobilan. Maka, kolom 'Banyak Anak' untuk baris 'Mobil-mobilan' harus diisi dengan angka 2.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menghitung objek visual (mobil-mobilan) dan menerjemahkannya ke dalam bentuk angka pada tabel. Ini adalah proses langsung dalam membaca dan mengisi data sederhana.. Bukti: Lengkapi diagram turus dengan mengisi kolom paling kanan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara merepresentasikan jumlah objek konkret ke dalam bentuk tabel data (diagram turus).. Bukti: Lengkapi diagram turus dengan mengisi kolom paling kanan
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar bagi siswa kelas 2, yaitu menghitung objek yang terlihat jelas dan menuliskan jumlahnya ke dalam tabel yang sudah disediakan.. Bukti: Lengkapi diagram turus dengan mengisi kolom paling kanan; Mobil-mobilan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek konkret sampai dengan 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya melibatkan penghitungan benda konkret dan pengisian tabel sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3939`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan observasi visual langsung terhadap objek yang ada di gambar dan memindahkan jumlah tersebut ke dalam tabel. Tidak ada proses penalaran kompleks atau strategi non-rutin yang diperlukan.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dasar tentang cara membaca data visual dan menyajikannya dalam format tabel (diagram turus).
- Intended difficulty `Easy`: Tugas ini sangat mendasar, melibatkan penghitungan objek konkret yang jumlahnya sedikit (2) dan pengisian tabel sederhana, yang sesuai dengan kemampuan siswa kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena melibatkan penghitungan objek nyata dan pengisian tabel sederhana yang merupakan materi standar awal pengolahan data. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 262/256; truncation: `True`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000094; applying=0.999906; reasoning=0.000000 | applying | 0.999906 | 0.000879 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.007949; conceptual=0.938686; procedural=0.053364; metacognitive=0.000000 | conceptual | 0.938686 | 0.183379 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.620205; Medium=0.364235; Hard=0.015560 | Easy | 0.620205 | 0.663486 | review / input_reached_truncation_limit; selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999906; −Σp ln(p) = 0.000965; H = 0.000965/ln(3) = 0.000879; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.938686; −Σp ln(p) = 0.254217; H = 0.254217/ln(4) = 0.183379; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.620205; −Σp ln(p) = 0.728914; H = 0.728914/ln(3) = 0.663486; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Turus
Tipe soal: multiple_choice
Stimulus: -
Soal: 1. Kira sedang mendata mainan kesukaan teman-temannya. Data yang didapatkan oleh Kira terdapat pada diagram berikut. Lengkapi diagram turus dengan mengisi kolom paling kanan. Diagram Turus Mainan Kesukaan

|Mainan|Turus|Banyak Anak|
|---|---|---|
|Mobil-mobilan||…|
|Boneka|IIII|…|
|Kelereng|I|…|
|Mainan balok|II|…|

Lengkapi diagram turus dengan mengisi kolom paling kanan. (Mobil-mobilan)
Pilihan: A. 7
B. 6
C. 4
D. 2
Transkripsi visual: The image shows a girl holding a box with a teddy bear inside. On the floor, there are several toys: two toy cars (one red, one purple), three teddy bears (one purple, one pink, one yellow/blue), several building blocks, and some small balls. The tally chart asks for the count of 'Mobil-mobilan' (toy cars). There are exactly 2 toy cars visible on the floor.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `a425d49d4fa1757682ab7805`

1. Perhatikan gambar di bawah ini. Malosi sedang mendata banyaknya buah yang dibeli Ibu di pasar. Buatlah diagram turus dari buah-buahan di atas. Diagram Turus Buah yang Dibeli Ibu<br><br>\|Nama Buah\|Turus\|Banyaknya\|<br>\|---\|---\|---\|<br>\|Apel\|\|\|<br>\|Jeruk\|\|\|<br>\|Semangka\|\|\|<br>\|Alpukat\|\|\|<br><br>Buatlah diagram turus dari buah-buahan di atas. (Semangka)

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 3 |
| C | 7 |
| D | 1 |

![Gambar sumber soal 41](<../images/kelas2_panduan_siswa_kelas2.pdf-0258-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Berdasarkan pengamatan visual pada gambar, hanya terdapat 1 buah semangka di atas meja. Maka, diagram turus untuk semangka adalah 1.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0258-04.png. Transkripsi visual: Seorang anak laki-laki berdiri di belakang meja. Di atas meja terdapat buah-buahan: 1 buah semangka besar, 3 buah apel merah, 5 buah jeruk kecil, dan 3 buah alpukat hijau.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `add2a46be1357ced4c6ede2680df14c89af0399c692f9e08dce5341a2fa85b44`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2584 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2594 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2545 |

Run 1 — solusi: Menghitung jumlah buah semangka pada gambar: hanya terdapat 1 buah semangka. Maka, turus untuk semangka adalah 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan proses penghitungan langsung (counting) dan mengasosiasikannya dengan representasi turus sederhana. Ini adalah proses rutin yang langsung.. Bukti: Malosi sedang mendata banyaknya buah; Buatlah diagram turus dari buah-buahan di atas
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur dasar pembuatan diagram turus (tally chart) sebagai cara merepresentasikan data.. Bukti: Buatlah diagram turus
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan penghitungan objek visual yang sederhana dan konversi ke bentuk turus yang familiar.. Bukti: Malosi sedang mendata banyaknya buah; Buatlah diagram turus dari buah-buahan di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek hingga 10 dan mengenal simbol turus dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena hanya memerlukan observasi visual langsung dan penghitungan satu jenis objek. |

Run 2 — solusi: Menghitung jumlah semangka pada gambar: hanya terdapat 1 buah semangka. Maka turus untuk semangka adalah 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi objek (buah semangka) dan menghitung jumlahnya secara langsung dari gambar, kemudian merepresentasikannya dalam bentuk turus. Ini adalah proses pengenalan dan penghitungan langsung.. Bukti: Malosi sedang mendata banyaknya buah; Buatlah diagram turus dari buah-buahan di atas
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep turus sebagai cara untuk merepresentasikan data (jumlah objek) dalam bentuk simbol garis.. Bukti: Buatlah diagram turus; Nama Buah \| Turus \| Banyaknya
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan tugas rutin yaitu menghitung objek visual sederhana dan mencatatnya dalam format turus yang sudah umum dipelajari di kelas 2.. Bukti: Perhatikan gambar di bawah ini; Buatlah diagram turus dari buah-buahan di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek hingga 10 dan memahami simbol turus dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung objek dan membuat turus adalah standar kompetensi kelas 2 SD yang bersifat rutin dan langsung. |

Run 3 — solusi: Berdasarkan pengamatan visual pada gambar, hanya terdapat 1 buah semangka di atas meja. Oleh karena itu, diagram turus untuk semangka adalah 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan proses penghitungan langsung (counting) dan merepresentasikannya dalam bentuk turus sederhana, yang merupakan proses rutin.. Bukti: Malosi sedang mendata banyaknya buah; Buatlah diagram turus dari buah-buahan di atas
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang cara merepresentasikan data menggunakan simbol turus, yang merupakan pengetahuan prosedural dasar.. Bukti: Buatlah diagram turus
- Intended difficulty `classify/Easy`: Tugas ini melibatkan penghitungan objek visual sederhana dan pemetaan ke simbol turus, yang merupakan keterampilan dasar kelas 2.. Bukti: Perhatikan gambar di bawah ini; Buatlah diagram turus

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (1-10) dan mengenal simbol turus dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 diharapkan mampu melakukan penghitungan objek konkret dan menyajikannya dalam tabel turus sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3867`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk melakukan proses penghitungan langsung (counting) objek visual dan mengasosiasikannya dengan representasi turus sederhana. Ini adalah proses rutin yang langsung.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang prosedur dasar pembuatan diagram turus (tally chart) sebagai cara merepresentasikan data.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan penghitungan objek visual yang sederhana dan konversi ke bentuk turus yang familiar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek hingga 10 dan mengenal simbol turus dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena hanya memerlukan observasi visual langsung dan penghitungan satu jenis objek. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 183/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.000665; conceptual=0.994495; procedural=0.004841; metacognitive=0.000000 | conceptual | 0.994495 | 0.026082 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.691111; Medium=0.300670; Hard=0.008218 | Easy | 0.691111 | 0.597227 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.994495; −Σp ln(p) = 0.036157; H = 0.036157/ln(4) = 0.026082; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.691111; −Σp ln(p) = 0.656121; H = 0.656121/ln(3) = 0.597227; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Turus
Tipe soal: multiple_choice
Stimulus: -
Soal: 1. Perhatikan gambar di bawah ini. Malosi sedang mendata banyaknya buah yang dibeli Ibu di pasar. Buatlah diagram turus dari buah-buahan di atas. Diagram Turus Buah yang Dibeli Ibu

|Nama Buah|Turus|Banyaknya|
|---|---|---|
|Apel|||
|Jeruk|||
|Semangka|||
|Alpukat|||

Buatlah diagram turus dari buah-buahan di atas. (Semangka)
Pilihan: A. 2
B. 3
C. 7
D. 1
Transkripsi visual: Seorang anak laki-laki berdiri di belakang meja. Di atas meja terdapat buah-buahan: 1 buah semangka besar, 3 buah apel merah, 5 buah jeruk kecil, dan 3 buah alpukat hijau.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `655cea6ab3fa2ff165080502`

1. Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.<br><br>- a. Ada anak yang suka kue cucur.<br>- b. Ada anak yang suka onde-onde.<br>- c. Ada anak yang suka lemper.<br>- d. Ada anak yang suka kue talam.<br><br>a. Ada .... anak yang suka kue cucur.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 6 |
| C | 3 |
| D | 7 |

![Gambar sumber soal 42](<../images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Menghitung jumlah bintang pada baris kue cucur di diagram gambar, yaitu terdapat 6 bintang.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: Tabel Diagram Gambar Kue Kesukaan. Baris 1: Kue cucur, 6 bintang. Baris 2: Onde-onde, 5 bintang. Baris 3: Lemper, 3 bintang. Baris 4: Kue talam, 7 bintang. Keterangan: Setiap gambar mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bc8895e7fcdc5be73df656578c9dc377692a40177b1f075768edd67b9364f385`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2610 |
| 2 | success | valid / verified | knowing | factual | Easy | 2595 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2547 |

Run 1 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram gambar: terdapat 6 bintang, sehingga ada 6 anak yang suka kue cucur.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol bintang yang tersedia untuk kategori kue cucur.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; a. Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana dalam bentuk diagram gambar (pictograph) dan bagaimana menginterpretasikan simbol sebagai satuan data.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (direct retrieval) dengan beban kognitif rendah, cocok untuk tingkat kelas 2.. Bukti: a. Ada .... anak yang suka kue cucur.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret (1-10) dan membaca diagram sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan keterampilan menghitung dasar (counting) pada representasi visual yang sudah familiar. |

Run 2 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram, yaitu 6 bintang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia.. Bukti: Kira sedang mendata kue kesukaan; Diagram Gambar Kue Kesukaan; Ada .... anak yang suka kue cucur
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana dalam bentuk diagram gambar (pictograph) sebagai cara menyajikan fakta.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan kemampuan menghitung objek (bintang) dalam satu baris diagram yang sudah terstruktur dengan jelas.. Bukti: Ada .... anak yang suka kue cucur

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membaca diagram sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya melibatkan pembacaan data visual langsung tanpa operasi matematika kompleks. |

Run 3 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram gambar, yaitu 6 bintang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data langsung dari diagram gambar dengan menghitung jumlah simbol (bintang) yang mewakili frekuensi.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang representasi data sederhana (diagram gambar) di mana satu simbol mewakili satu unit.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan penghitungan satu baris data tanpa operasi tambahan atau interpretasi kompleks.. Bukti: Ada .... anak yang suka kue cucur.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena hanya melibatkan pembacaan diagram gambar sederhana yang merupakan materi standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3807`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan proses membaca data langsung (direct retrieval) dari diagram gambar dengan menghitung jumlah simbol yang tersedia untuk kategori kue cucur.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana dalam bentuk diagram gambar (pictograph) sebagai cara menyajikan fakta.
- Intended difficulty `Easy`: Soal ini sangat mendasar, hanya memerlukan kemampuan menghitung objek (bintang) dalam satu baris diagram yang sudah terstruktur dengan jelas tanpa operasi matematika tambahan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membaca diagram sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya melibatkan pembacaan data visual langsung tanpa operasi matematika kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 201/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000196; applying=0.999804; reasoning=0.000000 | applying | 0.999804 | 0.001698 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.009926; conceptual=0.980921; procedural=0.009153; metacognitive=0.000000 | conceptual | 0.980921 | 0.077648 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.597976; Medium=0.390594; Hard=0.011430 | Easy | 0.597976 | 0.660636 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999804; −Σp ln(p) = 0.001865; H = 0.001865/ln(3) = 0.001698; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.980921; −Σp ln(p) = 0.107644; H = 0.107644/ln(4) = 0.077648; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.597976; −Σp ln(p) = 0.725783; H = 0.725783/ln(3) = 0.660636; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: 1. Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.

- a. Ada anak yang suka kue cucur.
- b. Ada anak yang suka onde-onde.
- c. Ada anak yang suka lemper.
- d. Ada anak yang suka kue talam.

a. Ada .... anak yang suka kue cucur.
Pilihan: A. 5
B. 6
C. 3
D. 7
Transkripsi visual: Tabel Diagram Gambar Kue Kesukaan. Baris 1: Kue cucur, 6 bintang. Baris 2: Onde-onde, 5 bintang. Baris 3: Lemper, 3 bintang. Baris 4: Kue talam, 7 bintang. Keterangan: Setiap gambar mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `3606c1d695032907b61d4fbc`

1. Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.<br><br>- a. Ada anak yang suka kue cucur.<br>- b. Ada anak yang suka onde-onde.<br>- c. Ada anak yang suka lemper.<br>- d. Ada anak yang suka kue talam.<br><br>d. Ada .... anak yang suka kue talam.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 3 |
| C | 6 |
| D | 7 |

![Gambar sumber soal 43](<../images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah bintang pada baris kue talam: terdapat 7 bintang, sehingga ada 7 anak yang suka kue talam.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: Diagram gambar menunjukkan empat baris kue: kue cucur (6 bintang), onde-onde (5 bintang), lemper (3 bintang), dan kue talam (7 bintang). Setiap bintang mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c7a67f829c0bbe743f1691cb4ecd0cf5bb69fb0a10112d40ce7269743c6a756a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2600 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2616 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2622 |

Run 1 — solusi: Menghitung jumlah bintang pada baris kue talam: terdapat 7 bintang, sehingga ada 7 anak yang suka kue talam.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram gambar (pictograph) secara langsung dengan menghitung jumlah simbol yang ada. Ini adalah proses membaca data yang sangat langsung.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang representasi data sederhana (diagram gambar) di mana siswa perlu memahami hubungan antara simbol (bintang) dan kuantitas (jumlah anak).. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan penghitungan satu-ke-satu (one-to-one correspondence) pada representasi visual yang sangat sederhana.. Bukti: Setiap gambar mewakili 1 anak; Ada .... anak yang suka kue talam.

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
| gradeRelativeRationale | Membaca diagram gambar sederhana adalah kompetensi dasar kelas 2 yang melibatkan penghitungan langsung. |

Run 2 — solusi: Menghitung jumlah bintang pada baris 'kue talam' di diagram gambar, yaitu terdapat 7 bintang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data secara langsung dari diagram gambar (tallying/counting) tanpa perlu manipulasi atau strategi kompleks.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) sebagai bentuk penyajian informasi.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Tugas ini sangat rutin dan langsung, hanya memerlukan penghitungan satu baris data pada diagram gambar yang sederhana.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret (1-10) dan membaca diagram gambar sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena merupakan pengenalan dasar terhadap pengolahan data visual yang sangat sederhana. |

Run 3 — solusi: Menghitung jumlah bintang pada baris kue talam: ada 7 bintang, sehingga ada 7 anak yang menyukai kue talam.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia, yang merupakan proses kognitif knowing.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) dan bagaimana mengaitkan simbol dengan jumlah objek, yang merupakan pengetahuan konseptual.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Tugas ini sangat langsung, hanya melibatkan penghitungan objek visual sederhana dalam satu baris diagram tanpa operasi tambahan atau interpretasi kompleks.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas; Ada .... anak yang suka kue talam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret hingga 10 dan membaca tabel sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena melibatkan pembacaan data visual sederhana yang merupakan materi standar awal pengolahan data. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 193/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000226; applying=0.999774; reasoning=0.000000 | applying | 0.999774 | 0.001934 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.002727; conceptual=0.988997; procedural=0.008276; metacognitive=0.000000 | conceptual | 0.988997 | 0.048130 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.608594; Medium=0.381032; Hard=0.010374 | Easy | 0.608594 | 0.652888 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999774; −Σp ln(p) = 0.002125; H = 0.002125/ln(3) = 0.001934; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.988997; −Σp ln(p) = 0.066723; H = 0.066723/ln(4) = 0.048130; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.608594; −Σp ln(p) = 0.717270; H = 0.717270/ln(3) = 0.652888; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 2
Topik: Matematika SD Kelas 2
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: 1. Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.

- a. Ada anak yang suka kue cucur.
- b. Ada anak yang suka onde-onde.
- c. Ada anak yang suka lemper.
- d. Ada anak yang suka kue talam.

d. Ada .... anak yang suka kue talam.
Pilihan: A. 5
B. 3
C. 6
D. 7
Transkripsi visual: Diagram gambar menunjukkan empat baris kue: kue cucur (6 bintang), onde-onde (5 bintang), lemper (3 bintang), dan kue talam (7 bintang). Setiap bintang mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `e7d8a29f2e3a28f99529dfc8`

Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Diagram Buah Kesukaan. Gambar mewakili 1 anak. Lengkapi setiap kalimat berikut.<br><br>Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 1 |
| C | 4 |
| D | 3 |

![Gambar sumber soal 44](<../images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png>)


![Gambar sumber soal 44](<../images/kelas1_panduan_siswa_kelas1.pdf-0246-05.png>)


![Gambar sumber soal 44](<../images/kelas1_panduan_siswa_kelas1.pdf-0246-06.png>)


![Gambar sumber soal 44](<../images/kelas1_panduan_siswa_kelas1.pdf-0246-07.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `3`.
Solusi minimum hasil AI: Jumlah anak yang suka belimbing adalah 7. Jumlah anak yang suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png, images/kelas1_panduan_siswa_kelas1.pdf-0246-05.png, images/kelas1_panduan_siswa_kelas1.pdf-0246-06.png, images/kelas1_panduan_siswa_kelas1.pdf-0246-07.png. Transkripsi visual: The diagram shows two rows of stars representing fruit preferences. The top row, labeled with a starfruit icon, contains 7 stars. The bottom row, labeled with an apple icon, contains 4 stars. The prompt states that each star represents 1 child.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b6cfb8cc003dadd9b1708351b244472a2cbc645b94c549494552a40518629c55`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 5767 |
| 2 | success | valid / verified | applying | procedural | Easy | 5813 |
| 3 | success | valid / verified | applying | conceptual | Easy | 5795 |

Run 1 — solusi: Count the stars for starfruit (7) and apple (4). Calculate the difference: 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasi data dari diagram gambar (menghitung jumlah item) dan melakukan operasi pengurangan sederhana untuk membandingkan dua kelompok data.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan mengolah data dari representasi visual (diagram gambar), yang merupakan konsep dasar dalam statistika.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan penghitungan langsung dari objek visual yang jelas dan operasi pengurangan dasar satu digit, yang sesuai dengan kurikulum kelas 2.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (1-10) dan konsep pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan representasi piktogram sederhana dan operasi hitung dasar yang sudah diajarkan. |

Run 2 — solusi: Count the stars for star fruit (7) and apples (4). Calculate the difference: 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasi data dari diagram gambar (menghitung jumlah objek) dan menerapkan operasi pengurangan dasar untuk membandingkan dua kelompok data.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam membaca data dari representasi visual (diagram gambar) dan melakukan operasi aritmatika dasar.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan penghitungan langsung dari representasi visual yang sederhana dan satu operasi pengurangan dasar yang sesuai untuk tingkat kelas 2.. Bukti: Lengkapi setiap kalimat berikut.; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (1-10) dan konsep pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan representasi piktograf sederhana yang umum diajarkan pada tingkat ini. |

Run 3 — solusi: Jumlah anak yang suka belimbing adalah 7. Jumlah anak yang suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari piktogram (menghitung jumlah simbol) dan menerapkan operasi pengurangan dasar untuk membandingkan dua kategori.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang representasi data (piktogram) dan hubungan antara simbol dengan kuantitas.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan penghitungan langsung dari piktogram dan operasi pengurangan satu digit yang rutin bagi siswa kelas 2.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (korespondensi satu-satu) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 yang memperkenalkan pengumpulan dan penyajian data sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `7072`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menginterpretasi data dari piktogram (menghitung jumlah simbol) dan menerapkan operasi pengurangan dasar untuk membandingkan dua kategori.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang representasi data (piktogram) dan hubungan antara simbol dengan kuantitas.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya melibatkan penghitungan langsung dari piktogram dan operasi pengurangan satu digit yang rutin bagi siswa kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (korespondensi satu-satu) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 yang memperkenalkan pengumpulan dan penyajian data sederhana. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 148/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000024; applying=0.999976; reasoning=0.000000 | applying | 0.999976 | 0.000252 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.086764; conceptual=0.809360; procedural=0.103876; metacognitive=0.000000 | conceptual | 0.809360 | 0.446169 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.743851; Medium=0.243319; Hard=0.012830 | Easy | 0.743851 | 0.564262 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999976; −Σp ln(p) = 0.000276; H = 0.000276/ln(3) = 0.000252; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.809360; −Σp ln(p) = 0.618522; H = 0.618522/ln(4) = 0.446169; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.743851; −Σp ln(p) = 0.619905; H = 0.619905/ln(3) = 0.564262; T = 0.953328.


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
Transkripsi visual: The diagram shows two rows of stars representing fruit preferences. The top row, labeled with a starfruit icon, contains 7 stars. The bottom row, labeled with an apple icon, contains 4 stars. The prompt states that each star represents 1 child.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
