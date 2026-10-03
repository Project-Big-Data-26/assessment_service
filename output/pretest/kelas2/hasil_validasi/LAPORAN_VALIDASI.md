# Validasi ulang soal kelas 2 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v4-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v2-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 2 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model lama dipakai untuk menunjukkan ketidaksepakatan; tidak diberikan kembali ke Gemini.

Jumlah soal: 44; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 19, "applying": 24, "reasoning": 1}, "knowledgeDimension": {"factual": 9, "conceptual": 28, "procedural": 7, "metacognitive": 0}, "intendedDifficulty": {"Easy": 38, "Medium": 6, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 18, "applying": 24, "reasoning": 1}, "knowledgeDimension": {"factual": 9, "conceptual": 27, "procedural": 7, "metacognitive": 0}, "intendedDifficulty": {"Easy": 37, "Medium": 6, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 43, "revision_required": 1}`.
Run awal sukses: 132/132; adjudikasi: 17; token sukses tercatat: 326,849.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 38 | 37 | [Easy.json](difficulty/Easy.json) |
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

Isilah dengan bilangan yang tepat.<br><br>28 =    puluhan +    satuan

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b5353ac4f4ab27e97a77f5d16b9a44286e0af9185f2fb9ac2420b2151f41ed20`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1343 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1323 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1325 |

Run 1 — solusi: Angka 28 terdiri dari 2 puluhan (20) dan 8 satuan (8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari angka 28, yang merupakan proses langsung dalam memahami struktur bilangan dua digit.. Bukti: 28 =    puluhan +    satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur sistem bilangan desimal (nilai tempat), yang merupakan konsep dasar dalam matematika.. Bukti: 28 =    puluhan +    satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dan familiar bagi siswa kelas 2, hanya memerlukan pengenalan nilai tempat tanpa langkah tambahan yang kompleks.. Bukti: 28 =    puluhan +    satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat untuk bilangan dua digit (puluhan dan satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD yang menekankan pemahaman komposisi bilangan berdasarkan nilai tempat. |

Run 2 — solusi: Angka 28 terdiri dari 2 puluhan (20) dan 8 satuan (8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari angka 28, yang merupakan proses langsung dalam memahami konsep dasar nilai tempat.. Bukti: 28 =    puluhan +    satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar bilangan.. Bukti: 28 =    puluhan +    satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang komposisi bilangan dua digit.. Bukti: 28 =    puluhan +    satuan

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena merupakan pengenalan dasar nilai tempat yang diajarkan di tingkat tersebut. |

Run 3 — solusi: Angka 28 terdiri dari 2 puluhan (20) dan 8 satuan (8). Maka, 28 = 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari angka 28, yang merupakan proses langsung dalam memahami konsep dasar nilai tempat.. Bukti: 28 =    puluhan +    satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar bilangan.. Bukti: 28 =    puluhan +    satuan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan satu langkah identifikasi nilai tempat tanpa kompleksitas tambahan.. Bukti: 28 =    puluhan +    satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat (puluhan dan satuan) untuk bilangan dua digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD mengenai pengenalan nilai tempat bilangan cacah sampai 100. |

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

![Gambar sumber soal 15](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0089-03.png>)


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

![Gambar sumber soal 16](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0089-06.png>)


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
| C | Berbentuk seperti anak panah tunggal |
| D | Berbentuk seperti tangga (undakan) |

![Gambar sumber soal 17](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0097-12.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menempelkan sisi tegak segitiga pada salah satu sisi pendek persegi panjang akan membentuk bangun menyerupai anak panah (arrow).
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0097-12.png. Transkripsi visual: Terdapat dua bangun datar: sebuah persegi panjang di sebelah kiri dan sebuah segitiga sama sisi di sebelah kanan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `421307fe3ba13e1b737c8546561628890eac2bd2af49c7766b4ce1258cefe905`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2458 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2452 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2515 |

Run 1 — solusi: Menempelkan sisi tegak segitiga pada salah satu sisi pendek persegi panjang akan membentuk bangun menyerupai anak panah (arrow).
- Domain kognitif `classify/applying`: Siswa perlu melakukan visualisasi mental untuk menggabungkan dua bangun datar (persegi panjang dan segitiga) menjadi bentuk baru, yang merupakan proses applying konsep geometri dasar.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar bangun datar dan bagaimana mereka dapat dikomposisikan menjadi bentuk yang lebih kompleks.. Bukti: Mengurai dan Menyusun Bangun Datar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan dua bangun dasar yang umum dikenal siswa kelas 2 dan memerlukan satu langkah manipulasi mental sederhana.. Bukti: Susun bangun datar berikut menjadi satu bentuk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (persegi panjang dan segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual dan manipulasi bentuk sederhana yang merupakan bagian dari kurikulum geometri awal. |

Run 2 — solusi: Menempelkan sisi tegak segitiga pada salah satu sisi pendek persegi panjang akan membentuk bangun menyerupai anak panah (arrow).
- Domain kognitif `classify/applying`: Siswa perlu melakukan visualisasi mental untuk menggabungkan dua bangun datar (persegi panjang dan segitiga) menjadi bentuk baru, yang merupakan proses applying konsep geometri dasar.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antar bangun datar dan bagaimana mereka dapat disusun untuk membentuk struktur baru (konsep komposisi bangun).. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan dua bangun dasar yang familiar dan satu langkah penyusunan visual yang sederhana.. Bukti: Susun bangun datar berikut menjadi satu bentuk

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual dan manipulasi bentuk sederhana tanpa perhitungan numerik. |

Run 3 — solusi: Menempelkan sisi segitiga pada sisi persegi panjang membentuk bangun gabungan yang menyerupai anak panah (panah tunggal).
- Domain kognitif `classify/applying`: Siswa perlu melakukan visualisasi mental untuk menggabungkan dua bangun datar sederhana menjadi bentuk baru yang familiar. Ini melibatkan proses applying karena siswa menerapkan pemahaman tentang sifat bangun datar dalam situasi rutin (komposisi bentuk).. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bangun datar dapat disusun atau didekomposisi untuk membentuk bangun lain yang lebih kompleks.. Bukti: Susun bangun datar berikut menjadi satu bentuk
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan dua bangun dasar yang umum dikenal siswa kelas 2 dan tugasnya adalah penggabungan visual sederhana.. Bukti: Susun bangun datar berikut menjadi satu bentuk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (persegi panjang, segitiga) dan konsep penggabungan bentuk. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan tentang komposisi bangun datar sederhana. Tugas ini bersifat visual dan langsung, sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 106/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.085283; applying=0.914717; reasoning=0.000000 | applying | 0.914717 | 0.265323 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.583779; conceptual=0.403880; procedural=0.012341; metacognitive=0.000000 | factual | 0.583779 | 0.529915 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.893646; Medium=0.103910; Hard=0.002444 | Easy | 0.893646 | 0.319001 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.914717; −Σp ln(p) = 0.291487; H = 0.291487/ln(3) = 0.265323; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.583779; −Σp ln(p) = 0.734619; H = 0.734619/ln(4) = 0.529915; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.893646; −Σp ln(p) = 0.350459; H = 0.350459/ln(3) = 0.319001; T = 0.953328.


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
Transkripsi visual: Terdapat dua bangun datar: sebuah persegi panjang di sebelah kiri dan sebuah segitiga sama sisi di sebelah kanan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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

![Gambar sumber soal 19](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png>)


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

Berilah nama pada bangun ruang berikut.

| Opsi | Isi |
|---|---|
| A | Bola |
| B | Balok |
| C | Kerucut |
| D | Tabung |

![Gambar sumber soal 20](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0110-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Bangun ruang tersebut memiliki dua sisi berbentuk lingkaran dan satu sisi lengkung, yang merupakan ciri khas bangun ruang tabung.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0110-04.png. Transkripsi visual: Gambar menunjukkan sebuah bangun ruang berbentuk silinder dengan alas dan tutup berbentuk lingkaran serta selimut melengkung.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a19660186baa53d7d5f532ae90a125e0e5461f209d9e91edae639a0b8e97d12a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2417 |
| 2 | success | valid / verified | knowing | factual | Easy | 2451 |
| 3 | success | valid / verified | knowing | factual | Easy | 2424 |

Run 1 — solusi: Bangun ruang tersebut memiliki dua sisi berbentuk lingkaran dan satu sisi lengkung, yang merupakan ciri khas bangun ruang tabung.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun ruang berdasarkan karakteristik visual yang diberikan, yang merupakan proses kognitif tingkat knowing.. Bukti: Berilah nama pada bangun ruang berikut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang terminologi dan identifikasi bentuk dasar bangun ruang.. Bukti: Berilah nama pada bangun ruang berikut
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual langsung terhadap bentuk geometri yang umum dipelajari di kelas 2.. Bukti: Berilah nama pada bangun ruang berikut

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
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD yang menekankan pengenalan bentuk bangun ruang sederhana melalui pengamatan visual. |

Run 2 — solusi: Gambar tersebut adalah tabung karena memiliki dua sisi berbentuk lingkaran dan satu sisi lengkung yang menyelimuti.
- Domain kognitif `classify/knowing`: Soal hanya meminta siswa untuk mengenali dan menyebutkan nama bangun ruang berdasarkan representasi visualnya, yang merupakan proses mengingat atau mengenali fakta.. Bukti: Berilah nama pada bangun ruang berikut
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui istilah atau label nama untuk objek geometris tertentu (bangun ruang).. Bukti: Berilah nama pada bangun ruang berikut
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual langsung terhadap bentuk geometri yang umum dipelajari di kelas 2.. Bukti: Berilah nama pada bangun ruang berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun ruang dasar (bola, tabung, kerucut, balok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual bangun ruang dasar tanpa operasi kompleks. |

Run 3 — solusi: Bangun ruang tersebut memiliki dua sisi berbentuk lingkaran dan satu sisi lengkung yang menyelimuti, yang merupakan ciri khas tabung.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menyebutkan nama bangun ruang berdasarkan ciri visual langsung tanpa perlu melakukan analisis atau strategi kompleks.. Bukti: Berilah nama pada bangun ruang berikut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bangun ruang dasar yang diajarkan di kelas 2.. Bukti: Berilah nama pada bangun ruang berikut
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual terhadap bentuk geometris yang umum dipelajari di kelas 2.. Bukti: Berilah nama pada bangun ruang berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk bangun ruang dasar (bola, tabung, kerucut, balok). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya menuntut pengenalan visual langsung terhadap objek geometri yang sudah diperkenalkan di kurikulum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 69/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999439; applying=0.000561; reasoning=0.000000 | knowing | 0.999439 | 0.004335 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.789956; conceptual=0.207258; procedural=0.002786; metacognitive=0.000000 | factual | 0.789956 | 0.381466 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.906165; Medium=0.090659; Hard=0.003176 | Easy | 0.906165 | 0.296007 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999439; −Σp ln(p) = 0.004762; H = 0.004762/ln(3) = 0.004335; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.789956; −Σp ln(p) = 0.528825; H = 0.528825/ln(4) = 0.381466; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.906165; −Σp ln(p) = 0.325197; H = 0.325197/ln(3) = 0.296007; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah bangun ruang berbentuk silinder dengan alas dan tutup berbentuk lingkaran serta selimut melengkung.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Identifikasi bentuk lengkung: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk lengkung yang terlihat: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah sebagai bercak pada badan. Total ada 5 bentuk lengkung.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dec70edd0cd25a8efe18bee7b8a5d08a734c37025084787b7b91e49afd3a0ab7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2555 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2533 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2536 |

Run 1 — solusi: Identifikasi bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik visual tertentu (lengkung) dari sekumpulan bentuk geometri. Ini adalah proses klasifikasi dan penghitungan langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep bentuk lengkung (seperti lingkaran dan oval) untuk membedakannya dari bentuk bersudut (seperti persegi atau segitiga) dalam konteks visual.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan observasi visual sederhana dan penghitungan dasar. Tidak ada strategi kompleks atau manipulasi yang diperlukan.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran, oval) dan kemampuan berhitung 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan pengamatan visual langsung dan penghitungan dasar tanpa operasi matematika yang rumit. |

Run 2 — solusi: Mengidentifikasi dan menghitung bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total 1+1+1+2 = 5.
- Domain kognitif `classify/applying`: Siswa perlu mengenali dan mengklasifikasikan bentuk geometri (lengkung vs lurus) serta melakukan penghitungan sederhana. Ini adalah proses applying karena menerapkan konsep bentuk pada situasi visual rutin.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bentuk geometri (lengkung vs tidak lengkung).. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi visual langsung dari bentuk-bentuk yang sudah familiar bagi siswa kelas 2.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membedakan bentuk geometri dasar (lingkaran/oval vs poligon) dan melakukan penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2, menguji kemampuan observasi visual dasar terhadap bentuk geometri yang menyusun objek. |

Run 3 — solusi: Mengidentifikasi bentuk dengan sisi lengkung: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total 1+1+1+2 = 5.
- Domain kognitif `classify/applying`: Siswa perlu mengklasifikasikan bentuk geometri berdasarkan properti (lengkung vs lurus) dan menghitung jumlahnya. Ini adalah proses applying karena menerapkan konsep bentuk pada situasi visual rutin.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep bentuk geometri (lingkaran/oval vs poligon) untuk mengkategorikan objek-objek pada gambar.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan observasi visual sederhana dan menghitung objek yang memenuhi kriteria tertentu. Prosedurnya rutin dan langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran, oval, persegi, persegi panjang) dan kemampuan berhitung dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan identifikasi visual dasar dan berhitung sederhana tanpa manipulasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3933`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik visual tertentu (lengkung) dari sekumpulan bentuk geometri. Ini adalah proses klasifikasi dan penghitungan langsung yang bersifat rutin.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep bentuk lengkung (seperti lingkaran dan oval) untuk membedakannya dari bentuk bersudut (seperti persegi atau segitiga) dalam konteks visual.
- Intended difficulty `Easy`: Soal ini meminta siswa melakukan observasi visual sederhana dan menghitung objek yang memenuhi kriteria tertentu. Prosedurnya rutin dan langsung, sesuai untuk kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran, oval) dan kemampuan berhitung 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya memerlukan pengamatan visual langsung dan penghitungan dasar tanpa operasi matematika yang rumit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.044106; applying=0.955894; reasoning=0.000000 | applying | 0.955894 | 0.164554 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.363193; conceptual=0.607073; procedural=0.029733; metacognitive=0.000000 | conceptual | 0.607073 | 0.559311 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.880752; Medium=0.116453; Hard=0.002796 | Easy | 0.880752 | 0.344689 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.955894; −Σp ln(p) = 0.180781; H = 0.180781/ln(3) = 0.164554; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.607073; −Σp ln(p) = 0.775370; H = 0.775370/ln(4) = 0.559311; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.880752; −Σp ln(p) = 0.378680; H = 0.378680/ln(3) = 0.344689; T = 0.953328.


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
Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk lengkung yang terlihat: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah sebagai bercak pada badan. Total ada 5 bentuk lengkung.
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

![Gambar sumber soal 22](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0121-01.png>)


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

Perhatikan posisi kucing berikut. Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.<br><br>Kucing duduk di .... meja.

| Opsi | Isi |
|---|---|
| A | belakang |
| B | bawah |
| C | kanan |
| D | atas |

![Gambar sumber soal 23](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0119-12.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Secara visual, kucing berada di atas permukaan meja, sehingga kata yang tepat untuk melengkapi kalimat adalah 'atas'.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0119-12.png. Transkripsi visual: Gambar menunjukkan seekor kucing berwarna oranye sedang duduk tepat di atas permukaan sebuah meja kayu. Terdapat teks 'Kucing duduk di ____ meja.' di bawah gambar.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d4b3e00e36b09462ce9322fa3217f02a96d6dc2905c7d4b15753f2759f316d25`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2409 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2459 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2418 |

Run 1 — solusi: Secara visual, kucing berada di atas permukaan meja, sehingga kata yang tepat untuk melengkapi kalimat adalah 'atas'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali posisi spasial objek berdasarkan representasi visual langsung tanpa memerlukan strategi kompleks.. Bukti: Kucing duduk di .... meja.; Gambar menunjukkan seekor kucing berwarna oranye sedang duduk tepat di atas permukaan sebuah meja
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang istilah posisi spasial (preposisi tempat), yang merupakan pengetahuan faktual dasar.. Bukti: Kucing duduk di .... meja.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengamatan visual langsung terhadap posisi objek yang familiar bagi siswa kelas 2.. Bukti: Kucing duduk di .... meja.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep posisi (atas, bawah, depan, belakang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menguji kosakata posisi spasial dasar melalui pengamatan gambar sederhana. |

Run 2 — solusi: Secara visual, posisi kucing berada di permukaan atas meja, sehingga kata depan yang tepat adalah 'atas'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali posisi spasial objek (kucing) relatif terhadap objek lain (meja) dan mencocokkannya dengan kosakata posisi yang tepat. Ini adalah proses pengenalan langsung.. Bukti: Kucing duduk di .... meja.; Pilih kata yang menunjukkan posisi kucing terhadap benda
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep posisi spasial (atas/bawah/samping) yang merupakan pengetahuan konseptual dasar.. Bukti: posisi kucing terhadap benda
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan hanya memerlukan satu langkah identifikasi posisi spasial yang familiar bagi siswa kelas 2.. Bukti: Kucing duduk di .... meja.; Pilihan: belakang, bawah, kanan, atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman kosakata posisi spasial dasar (atas, bawah, samping). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah sangat familiar dengan konsep posisi benda di lingkungan sekitar mereka. |

Run 3 — solusi: Berdasarkan pengamatan visual, kucing berada di atas permukaan meja, sehingga kata yang tepat untuk melengkapi kalimat adalah 'atas'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan mengidentifikasi posisi spasial objek (kucing) relatif terhadap objek lain (meja) secara langsung dari gambar.. Bukti: Pilih kata yang menunjukkan posisi kucing terhadap benda yang ada.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep posisi atau hubungan spasial (atas/bawah/depan/belakang) yang merupakan pengetahuan konseptual dasar.. Bukti: Kucing duduk di .... meja.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengamatan visual langsung tanpa perhitungan atau strategi kompleks.. Bukti: Kucing duduk di .... meja.

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menguji pemahaman spasial dasar yang diajarkan di awal jenjang sekolah dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3645`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan pengamatan visual langsung dan mengenali posisi spasial objek (kucing) relatif terhadap objek lain (meja). Ini adalah proses pengenalan langsung tanpa strategi kompleks.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep hubungan spasial (atas/bawah/depan/belakang), yang merupakan pengetahuan konseptual dasar dalam geometri posisi.
- Intended difficulty `Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan hanya memerlukan satu langkah identifikasi posisi spasial yang familiar bagi siswa kelas 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman kosakata posisi spasial dasar (atas, bawah, samping). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah sangat familiar dengan konsep posisi benda di lingkungan sekitar mereka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 103/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.063355; applying=0.936645; reasoning=0.000000 | applying | 0.936645 | 0.214908 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.116910; conceptual=0.870154; procedural=0.012936; metacognitive=0.000000 | conceptual | 0.870154 | 0.308879 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.863377; Medium=0.132754; Hard=0.003870 | Easy | 0.863377 | 0.379016 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.936645; −Σp ln(p) = 0.236101; H = 0.236101/ln(3) = 0.214908; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.870154; −Σp ln(p) = 0.428198; H = 0.428198/ln(4) = 0.308879; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.863377; −Σp ln(p) = 0.416391; H = 0.416391/ln(3) = 0.379016; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan seekor kucing berwarna oranye sedang duduk tepat di atas permukaan sebuah meja kayu. Terdapat teks 'Kucing duduk di ____ meja.' di bawah gambar.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Pola berulang setiap tiga gambar (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, gambar berikutnya dalam urutan adalah kelinci.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Baris pola terdiri dari urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Terdapat garis kosong di akhir urutan untuk diisi.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a296f5d5770ee7ad45cdc6433358808af013a31ab0b5325a3791dec158f6af53`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2550 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2552 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2516 |

Run 1 — solusi: Pola berulang setiap tiga gambar (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, gambar berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi unit pengulangan dalam pola visual dan menerapkan aturan tersebut untuk memprediksi elemen berikutnya. Ini adalah penerapan konsep pola rutin.. Bukti: Amati pola berikut.; Tentukan pola gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola (hubungan antar elemen dalam urutan), yang merupakan pengetahuan konseptual.. Bukti: pola berulang tiga gambar
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola pengulangan sangat jelas dan berulang secara konsisten tanpa variasi kompleks, sesuai untuk tingkat kelas 2.. Bukti: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pengulangan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola visual sederhana adalah materi standar kelas 2. Siswa hanya perlu mengidentifikasi unit pengulangan (kupu-kupu, kelinci, kelinci) dan melanjutkan urutan tersebut. |

Run 2 — solusi: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, elemen berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi unit pengulangan dalam pola visual dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan konsep pola rutin.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan konsep dasar dalam matematika awal.. Bukti: Amati pola berikut.
- Intended difficulty `classify/Easy`: Soal ini menggunakan pola berulang sederhana yang sangat familiar bagi siswa kelas 2. Prosedur penyelesaiannya langsung dan tidak memerlukan strategi nonrutin.. Bukti: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pengulangan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola berulang adalah materi standar kelas 2. Tingkat kesulitan rendah karena pola sangat jelas dan berulang secara konsisten. |

Run 3 — solusi: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu terakhir, elemen berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi unit pengulangan dalam pola visual dan menerapkannya untuk menentukan elemen berikutnya. Ini adalah proses penerapan konsep pola rutin.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan konsep dasar dalam matematika awal.. Bukti: Amati pola berikut.
- Intended difficulty `classify/Easy`: Soal ini melibatkan pengenalan pola berulang sederhana yang umum untuk kelas 2. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Amati pola berikut. Tentukan pola gambar berikutnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pengulangan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan pola berulang sederhana (AB, ABB, dll) sebagai bagian dari kurikulum matematika dasar. |

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
| Domain kognitif | knowing=0.002417; applying=0.997583; reasoning=0.000000 | applying | 0.997583 | 0.015452 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.278603; conceptual=0.712701; procedural=0.008695; metacognitive=0.000000 | conceptual | 0.712701 | 0.460719 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.850081; Medium=0.145080; Hard=0.004839 | Easy | 0.850081 | 0.404094 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997583; −Σp ln(p) = 0.016976; H = 0.016976/ln(3) = 0.015452; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.712701; −Σp ln(p) = 0.638692; H = 0.638692/ln(4) = 0.460719; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.850081; −Σp ln(p) = 0.443942; H = 0.443942/ln(3) = 0.404094; T = 0.953328.


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
Transkripsi visual: Baris pola terdiri dari urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Terdapat garis kosong di akhir urutan untuk diisi.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Pola berulang adalah (oranye, hijau). Setelah lingkaran oranye terakhir, warna berikutnya dalam pola adalah hijau.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-02.png. Transkripsi visual: Terdapat baris pola warna yang terdiri dari lingkaran dengan urutan: oranye, hijau, oranye, hijau, oranye, dan satu lingkaran kosong di akhir.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fc50b95d75e65ac7874020aad4bfc2974a1ddd35841461445ae533b94624895b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2467 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2422 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2459 |

Run 1 — solusi: Pola berulang adalah (oranye, hijau). Setelah lingkaran oranye terakhir, warna berikutnya dalam pola adalah hijau.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pengulangan dalam urutan warna yang diberikan dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses applying karena melibatkan pengenalan dan penerapan aturan pola rutin.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola (urutan berulang), yang merupakan pengetahuan konseptual tentang bagaimana elemen-elemen disusun dalam struktur tertentu.. Bukti: Amati pola warna berikut
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola yang disajikan sangat sederhana (AB-AB) dan langsung terlihat. Siswa hanya perlu mengenali pengulangan satu unit pola.. Bukti: Amati pola warna berikut; oranye, hijau, oranye, hijau, oranye

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali perbedaan warna dan pengulangan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola AB-AB adalah materi dasar kelas 2 SD yang sangat familiar dan tidak memerlukan strategi kompleks. |

Run 2 — solusi: Pola berulang oranye-hijau. Setelah oranye terakhir, warna berikutnya harus hijau.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pola (oranye-hijau) dan menerapkannya untuk menentukan elemen berikutnya. Ini adalah proses applying karena menggunakan konsep pola rutin.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan pengetahuan konseptual.. Bukti: pola warna berselang-seling oranye dan hijau
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pola berulang sederhana dengan satu aturan yang jelas.. Bukti: Amati pola warna berikut; oranye, hijau, oranye, hijau, oranye

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
| gradeRelativeRationale | Pola berulang adalah materi standar kelas 2 yang sangat familiar. |

Run 3 — solusi: Pola yang diberikan adalah oranye-hijau-oranye-hijau-oranye. Karena pola berulang adalah (oranye, hijau), maka setelah oranye harus diikuti oleh hijau.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pola yang berulang dan menerapkannya untuk menentukan elemen berikutnya. Ini adalah proses applying karena siswa menggunakan konsep pola yang sudah dipelajari untuk situasi rutin.. Bukti: Amati pola warna berikut; Warna apa yang benar untuk melanjutkan polanya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang struktur pola (hubungan antar elemen dalam urutan), yang merupakan pengetahuan konseptual.. Bukti: pola warna berselang-seling oranye dan hijau
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pola AB-AB yang sangat familiar dan langsung.. Bukti: pola warna berselang-seling oranye dan hijau

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu mengenali urutan visual sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pola AB-AB adalah materi dasar kelas 1 dan 2 yang sangat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 87/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.290635; applying=0.709365; reasoning=0.000000 | applying | 0.709365 | 0.548619 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.156697; conceptual=0.838219; procedural=0.005084; metacognitive=0.000000 | conceptual | 0.838219 | 0.335575 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.836708; Medium=0.159402; Hard=0.003890 | Easy | 0.836708 | 0.421866 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.709365; −Σp ln(p) = 0.602720; H = 0.602720/ln(3) = 0.548619; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.838219; −Σp ln(p) = 0.465206; H = 0.465206/ln(4) = 0.335575; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.836708; −Σp ln(p) = 0.463468; H = 0.463468/ln(3) = 0.421866; T = 0.953328.


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
Transkripsi visual: Terdapat baris pola warna yang terdiri dari lingkaran dengan urutan: oranye, hijau, oranye, hijau, oranye, dan satu lingkaran kosong di akhir.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Definisi setengah adalah membagi benda menjadi dua bagian yang sama besar. Gambar B menunjukkan segitiga yang dibagi menjadi dua bagian dengan ukuran berbeda, sehingga bukan setengah.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0146-06.png. Transkripsi visual: Terdapat tujuh gambar bangun datar yang diberi label A sampai G. Gambar A (persegi panjang), C (lingkaran), D (hati), F (segi enam), dan G (persegi panjang) dibagi menjadi dua bagian yang sama besar. Gambar B (segitiga) dibagi menjadi dua bagian yang tidak sama besar oleh garis tegak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `23dd63c7d4d8d73f7e23dbf3f86ca18ed99c8e8df1f044996bc1e30fb359c010`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2565 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2553 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2581 |

Run 1 — solusi: Definisi setengah adalah membagi benda menjadi dua bagian yang sama besar. Gambar B menunjukkan segitiga yang dibagi menjadi dua bagian dengan ukuran berbeda, sehingga bukan setengah.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian sama besar dan menerapkan pemahaman tersebut untuk mengidentifikasi gambar yang tidak memenuhi kriteria tersebut.. Bukti: Manakah yang bukan setengah?; gambar B dibagi menjadi dua bagian yang tidak sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai pembagian benda utuh menjadi dua bagian yang sama besar.. Bukti: Setengah dari Benda Utuh; Manakah yang bukan setengah?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan pengamatan visual langsung terhadap konsep pecahan dasar tanpa langkah perhitungan yang kompleks.. Bukti: Manakah yang bukan setengah?; gambar B dibagi menjadi dua bagian yang tidak sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah (bagian yang sama besar). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diperkenalkan dengan konsep pecahan sederhana (setengah) melalui representasi visual. Tugas ini hanya memerlukan pengamatan visual sederhana. |

Run 2 — solusi: Definisi setengah adalah membagi benda menjadi dua bagian yang sama besar. Gambar B menunjukkan segitiga yang dibagi menjadi dua bagian dengan ukuran berbeda, sehingga bukan setengah.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian dua bagian yang sama besar dan membedakannya dari pembagian yang tidak sama besar.. Bukti: Manakah yang bukan setengah?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai pembagian benda menjadi dua bagian yang sama besar.. Bukti: setengah dari benda utuh
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengidentifikasi ketidaksamaan visual pada pembagian bangun datar, yang merupakan tugas rutin untuk kelas 2.. Bukti: Manakah yang bukan setengah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep dasar pembagian benda menjadi dua bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan konsep pecahan sederhana (setengah) melalui representasi visual bangun datar yang dibagi dua. |

Run 3 — solusi: Definisi setengah adalah membagi benda menjadi dua bagian yang sama besar. Gambar B menunjukkan segitiga yang dibagi menjadi dua bagian dengan ukuran berbeda, sehingga bukan setengah.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian dua bagian yang sama besar dan menerapkan pemahaman ini untuk membedakan gambar yang memenuhi syarat tersebut dengan yang tidak.. Bukti: Manakah yang bukan setengah?; gambar B dibagi menjadi dua bagian yang tidak sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai pembagian benda utuh menjadi dua bagian yang sama besar.. Bukti: Setengah dari Benda Utuh; Manakah yang bukan setengah?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung terhadap konsep dasar pecahan (setengah) yang sudah familiar bagi siswa kelas 2.. Bukti: Manakah yang bukan setengah?; gambar B (segitiga hijau-putih, dibagi garis tegak tidak sama besar)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah sebagai dua bagian yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan konsep pecahan sederhana (setengah) melalui representasi visual bangun datar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 173/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.016566; applying=0.983434; reasoning=0.000000 | applying | 0.983434 | 0.076783 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.001829; conceptual=0.997141; procedural=0.001030; metacognitive=0.000000 | conceptual | 0.997141 | 0.015487 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.764437; Medium=0.230554; Hard=0.005009 | Easy | 0.764437 | 0.518978 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.983434; −Σp ln(p) = 0.084355; H = 0.084355/ln(3) = 0.076783; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.997141; −Σp ln(p) = 0.021470; H = 0.021470/ln(4) = 0.015487; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.764437; −Σp ln(p) = 0.570155; H = 0.570155/ln(3) = 0.518978; T = 0.953328.


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
Transkripsi visual: Terdapat tujuh gambar bangun datar yang diberi label A sampai G. Gambar A (persegi panjang), C (lingkaran), D (hati), F (segi enam), dan G (persegi panjang) dibagi menjadi dua bagian yang sama besar. Gambar B (segitiga) dibagi menjadi dua bagian yang tidak sama besar oleh garis tegak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Setengah (1/2) didefinisikan sebagai dua bagian yang sama besar. Gambar kiri menunjukkan pembagian simetris yang menghasilkan dua bagian identik, sedangkan gambar kanan tidak.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0145-02.png. Transkripsi visual: Terdapat dua gambar hati. Gambar kiri dibagi oleh garis vertikal tepat di tengah menjadi dua bagian yang sama besar (merah dan toska). Gambar kanan dibagi oleh garis diagonal menjadi dua bagian yang tidak sama besar (merah di atas, toska di bawah).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2dd5675a2556c24b08a672e5c9bac1a65891fe9cba263d6a66508588bc4d7052`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2548 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2473 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2494 |

Run 1 — solusi: Setengah (1/2) didefinisikan sebagai dua bagian yang sama besar. Gambar kiri menunjukkan pembagian simetris yang menghasilkan dua bagian identik, sedangkan gambar kanan tidak.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian benda menjadi dua bagian yang sama besar, yang merupakan penerapan konsep dasar pecahan pada situasi visual rutin.. Bukti: Manakah yang setengah?; gambar kiri dibagi oleh garis vertikal tepat di tengah menjadi dua bagian... yang simetris dan sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan (setengah) sebagai hubungan kesamaan ukuran antara dua bagian dari satu kesatuan.. Bukti: Manakah yang setengah?; gambar kiri dibagi oleh garis vertikal tepat di tengah menjadi dua bagian... yang simetris dan sama besar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan representasi visual yang familiar bagi siswa kelas 2, dan hanya memerlukan satu keputusan berdasarkan pengamatan visual sederhana.. Bukti: Manakah yang setengah?; gambar kiri dibagi oleh garis vertikal tepat di tengah menjadi dua bagian... yang simetris dan sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 'sama besar' dan pengenalan bentuk simetris. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual pecahan sederhana tanpa perhitungan numerik kompleks. |

Run 2 — solusi: Setengah didefinisikan sebagai dua bagian yang sama besar. Gambar kiri menunjukkan pembagian simetris (sama besar), sedangkan gambar kanan menunjukkan pembagian tidak sama besar.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian benda menjadi dua bagian yang sama besar, yang merupakan proses pengenalan konsep dasar.. Bukti: Manakah yang setengah?; gambar kiri dibagi oleh garis tegak tepat di tengah sehingga menghasilkan dua bagian sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) melalui representasi visual.. Bukti: Manakah yang setengah?; gambar kiri dibagi oleh garis tegak tepat di tengah
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan pengenalan visual langsung tanpa perhitungan kompleks.. Bukti: Perhatikan gambar berikut. Manakah yang setengah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman visual dasar tentang kesamaan ukuran dan bentuk. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan konsep pecahan setengah melalui visualisasi sederhana. |

Run 3 — solusi: Setengah (1/2) didefinisikan sebagai dua bagian yang sama besar. Gambar kiri menunjukkan pembagian simetris yang menghasilkan dua bagian identik, sedangkan gambar kanan tidak.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep 'setengah' sebagai pembagian benda menjadi dua bagian yang sama besar (konseptual) dan menerapkannya untuk membedakan antara dua representasi visual.. Bukti: Manakah yang setengah?; gambar kiri dibagi oleh garis vertikal tepat di tengah menjadi dua bagian simetris
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai bagian dari keseluruhan yang sama besar.. Bukti: Manakah yang setengah?; dua bagian sama besar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin untuk kelas 2, hanya memerlukan pengenalan visual sederhana terhadap konsep kesamaan ukuran.. Bukti: Manakah yang setengah?; dua gambar hati

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 'sama besar' atau simetri sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual konsep pecahan dasar tanpa perhitungan numerik. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3789`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pemahaman konseptual tentang 'setengah' (dua bagian yang sama besar) untuk membedakan antara dua representasi visual yang diberikan.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai hubungan kesamaan ukuran antara dua bagian dari satu kesatuan.
- Intended difficulty `Easy`: Soal ini bersifat langsung, menggunakan representasi visual yang familiar bagi siswa kelas 2, dan hanya memerlukan satu keputusan berdasarkan pengamatan visual sederhana.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 'sama besar' dan pengenalan bentuk simetris. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual pecahan sederhana tanpa perhitungan numerik kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 131/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000108; applying=0.999892; reasoning=0.000000 | applying | 0.999892 | 0.000994 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.007229; conceptual=0.987239; procedural=0.005533; metacognitive=0.000000 | conceptual | 0.987239 | 0.055593 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.746339; Medium=0.248882; Hard=0.004779 | Easy | 0.746339 | 0.537073 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999892; −Σp ln(p) = 0.001092; H = 0.001092/ln(3) = 0.000994; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.987239; −Σp ln(p) = 0.077068; H = 0.077068/ln(4) = 0.055593; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.746339; −Σp ln(p) = 0.590035; H = 0.590035/ln(3) = 0.537073; T = 0.953328.


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
Transkripsi visual: Terdapat dua gambar hati. Gambar kiri dibagi oleh garis vertikal tepat di tengah menjadi dua bagian yang sama besar (merah dan toska). Gambar kanan dibagi oleh garis diagonal menjadi dua bagian yang tidak sama besar (merah di atas, toska di bawah).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Setengah dari sekumpulan benda berarti membagi benda tersebut menjadi dua bagian yang sama banyak. Baris pertama membagi 4 monyet menjadi 2 dan 2 (sama banyak), sedangkan baris kedua membagi 4 monyet menjadi 1 dan 3 (tidak sama banyak). Maka, baris pertama menunjukkan setengah.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0150-12.png. Transkripsi visual: Gambar menunjukkan dua baris kelompok monyet. Baris pertama berisi 4 monyet yang dibagi menjadi dua kotak, masing-masing berisi 2 monyet. Baris kedua berisi 4 monyet yang dibagi menjadi dua kotak, satu kotak berisi 1 monyet dan kotak lainnya berisi 3 monyet.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2307483ad3995dbac656d8a4ece17c62485b651ea19944e9e0b7e68fd12f2f3d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2544 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2536 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2523 |

Run 1 — solusi: Setengah dari sekumpulan benda berarti membagi benda tersebut menjadi dua bagian yang sama banyak. Baris pertama membagi 4 monyet menjadi 2 dan 2 (sama banyak), sedangkan baris kedua membagi 4 monyet menjadi 1 dan 3 (tidak sama banyak). Maka, baris pertama menunjukkan setengah.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep 'setengah' (pembagian menjadi dua bagian sama besar) pada representasi visual yang diberikan. Ini adalah penerapan konsep dasar pada situasi rutin.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pembagian menjadi dua bagian yang sama besar (konsep setengah) dalam konteks kumpulan benda.. Bukti: setengah dari kumpulan benda; 2 monyet dan 2 monyet
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengenalan visual sederhana terhadap konsep setengah yang sudah umum diajarkan di kelas 2.. Bukti: Perhatikan gambar berikut; Kelompok mana yang menunjukkan setengah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah dan kemampuan menghitung jumlah benda dalam kelompok. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep setengah dari kumpulan benda adalah materi standar kelas 2. Soal ini menggunakan representasi visual langsung yang tidak memerlukan langkah kompleks. |

Run 2 — solusi: Setengah dari kumpulan benda berarti membagi benda menjadi dua kelompok dengan jumlah yang sama. Baris pertama membagi 4 monyet menjadi 2 dan 2 (sama banyak), sedangkan baris kedua membagi 4 monyet menjadi 1 dan 3 (tidak sama banyak).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep 'setengah' (pembagian menjadi dua bagian sama besar) pada representasi visual yang diberikan. Ini adalah penerapan konsep dasar pada situasi rutin.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pembagian menjadi dua bagian yang sama (konsep pecahan sederhana/setengah) dalam konteks kumpulan benda.. Bukti: Setengah dari Kumpulan Benda
- Intended difficulty `classify/Easy`: Soal ini cukup mudah karena hanya memerlukan pengamatan visual langsung terhadap pembagian kelompok benda yang sudah disajikan secara eksplisit.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 'setengah' atau 'sama banyak' untuk jumlah benda kecil. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan objek konkret (monyet) untuk memvisualisasikan konsep pecahan sederhana. |

Run 3 — solusi: Setengah dari kumpulan benda berarti membagi benda menjadi dua kelompok dengan jumlah yang sama. Baris pertama membagi 4 monyet menjadi dua kelompok yang masing-masing berisi 2 monyet (sama banyak), sedangkan baris kedua membagi 4 monyet menjadi kelompok berisi 1 dan 3 (tidak sama banyak).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep 'setengah' (pembagian menjadi dua bagian sama besar) pada representasi visual yang diberikan.. Bukti: Kelompok mana yang menunjukkan setengah; Baris pertama (2 monyet dan 2 monyet)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip dasar pecahan atau pembagian sederhana (konsep setengah sebagai dua bagian yang sama).. Bukti: setengah dari kumpulan benda
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan identifikasi visual sederhana dari konsep pembagian dua bagian sama besar.. Bukti: Kelompok mana yang menunjukkan setengah; gambar dua baris pengelompokan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 'setengah' dan kemampuan menghitung benda dalam kelompok kecil. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan objek konkret (gambar) untuk mengenalkan konsep pecahan sederhana. |

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
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000012 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003955; conceptual=0.992965; procedural=0.003081; metacognitive=0.000000 | conceptual | 0.992965 | 0.033691 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.656258; Medium=0.338353; Hard=0.005389 | Easy | 0.656258 | 0.610978 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000013; H = 0.000013/ln(3) = 0.000012; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.992965; −Σp ln(p) = 0.046705; H = 0.046705/ln(4) = 0.033691; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.656258; −Σp ln(p) = 0.671227; H = 0.671227/ln(3) = 0.610978; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan dua baris kelompok monyet. Baris pertama berisi 4 monyet yang dibagi menjadi dua kotak, masing-masing berisi 2 monyet. Baris kedua berisi 4 monyet yang dibagi menjadi dua kotak, satu kotak berisi 1 monyet dan kotak lainnya berisi 3 monyet.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Setengah dari kumpulan benda berarti membagi benda menjadi dua kelompok dengan jumlah yang sama. Baris ketiga memiliki dua kelompok yang masing-masing berisi 4 kelinci (total 8), sehingga ini menunjukkan setengah.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0151-01.png. Transkripsi visual: Gambar terdiri dari tiga baris kelinci. Baris pertama berisi 8 kelinci berjajar. Baris kedua berisi dua kotak: kotak kiri berisi 3 kelinci, kotak kanan berisi 5 kelinci. Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5985660fce54b689e1cbaa27bacf76148e0ee469b74354bdbe0ca24b2457c01c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2536 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2517 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2529 |

Run 1 — solusi: Setengah dari kumpulan benda berarti membagi benda menjadi dua kelompok dengan jumlah yang sama. Baris ketiga memiliki dua kelompok yang masing-masing berisi 4 kelinci (total 8), sehingga ini menunjukkan setengah.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep 'setengah' sebagai pembagian menjadi dua bagian yang sama besar dan menerapkannya untuk mengidentifikasi representasi visual yang tepat.. Bukti: Kelompok mana yang menunjukkan setengah; dua kelompok yang masing-masing berisi 4 kelinci
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) dalam konteks kumpulan benda.. Bukti: setengah dari kumpulan benda
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan observasi visual sederhana untuk membandingkan jumlah benda dalam kelompok, yang merupakan prosedur rutin di kelas 2.. Bukti: Kelompok mana yang menunjukkan setengah; gambar terdiri dari tiga baris kelinci

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena melibatkan pengenalan konsep pecahan sederhana melalui objek konkret/visual yang familiar. |

Run 2 — solusi: Setengah berarti membagi menjadi dua kelompok yang sama banyak. Baris bawah memiliki dua kelompok dengan masing-masing 4 kelinci (4=4), sehingga menunjukkan setengah dari total 8 kelinci.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep 'setengah' (pembagian menjadi dua bagian sama besar) pada representasi visual kumpulan benda. Ini adalah penerapan konsep dasar pada situasi rutin.. Bukti: Kelompok mana yang menunjukkan setengah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pecahan sederhana (setengah) sebagai pembagian objek ke dalam kelompok yang sama banyak.. Bukti: Kelompok mana yang menunjukkan setengah
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung dan pemahaman dasar tentang kesamaan jumlah dalam dua kelompok.. Bukti: Kelompok mana yang menunjukkan setengah

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
| gradeRelativeRationale | Sesuai untuk kelas 2, di mana siswa mulai belajar pecahan sederhana melalui visualisasi konkret. |

Run 3 — solusi: Setengah berarti membagi menjadi dua kelompok yang sama banyak. Baris bawah memiliki dua kelompok dengan masing-masing 4 kelinci (4=4), sehingga menunjukkan setengah dari 8 kelinci.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep 'setengah' (pembagian menjadi dua bagian sama besar) pada representasi visual objek konkret.. Bukti: Kelompok mana yang menunjukkan setengah; Baris kedua (4 kelinci dan 4 kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sederhana (setengah) sebagai pembagian objek ke dalam dua kelompok yang ekuivalen.. Bukti: setengah dari Kumpulan Benda
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan observasi visual sederhana untuk membandingkan jumlah objek dalam kelompok, yang merupakan prosedur standar di kelas 2.. Bukti: Perhatikan gambar berikut; Kelompok mana yang menunjukkan setengah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep setengah dan kemampuan menghitung objek hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2, di mana siswa mulai mempelajari pecahan sederhana melalui representasi visual benda konkret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 132/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000002; applying=0.999998; reasoning=0.000000 | applying | 0.999998 | 0.000031 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004982; conceptual=0.993295; procedural=0.001723; metacognitive=0.000000 | conceptual | 0.993295 | 0.031784 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.702506; Medium=0.292742; Hard=0.004751 | Easy | 0.702506 | 0.576268 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999998; −Σp ln(p) = 0.000034; H = 0.000034/ln(3) = 0.000031; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.993295; −Σp ln(p) = 0.044063; H = 0.044063/ln(4) = 0.031784; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.702506; −Σp ln(p) = 0.633095; H = 0.633095/ln(3) = 0.576268; T = 0.953328.


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
Transkripsi visual: Gambar terdiri dari tiga baris kelinci. Baris pertama berisi 8 kelinci berjajar. Baris kedua berisi dua kotak: kotak kiri berisi 3 kelinci, kotak kanan berisi 5 kelinci. Baris ketiga berisi dua kotak: kotak kiri berisi 4 kelinci, kotak kanan berisi 4 kelinci.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Seperempat (1/4) dari sebuah benda utuh harus terdiri dari empat bagian yang sama besar (kongruen). Hanya Gambar 2 yang menunjukkan bangun datar yang dibagi menjadi empat bagian dengan luas yang sama persis.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png. Transkripsi visual: Terdapat empat gambar bangun datar yang dibagi menjadi empat bagian. Gambar 1 adalah segitiga yang dibagi tidak sama besar. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis vertikal dan horizontal tepat di tengah, menghasilkan empat bagian yang kongruen (sama besar dan bentuk). Gambar 3 adalah bangun menyerupai anak panah yang dibagi tidak simetris. Gambar 4 adalah persegi panjang yang dibagi menjadi empat bagian dengan ukuran berbeda.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `21587c539018bd7ddc4b71969a6119f35904beab7752f373c2ecb95337828a4c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2579 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2585 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2656 |

Run 1 — solusi: Seperempat (1/4) dari sebuah benda utuh harus terdiri dari empat bagian yang sama besar (kongruen). Hanya Gambar 2 yang menunjukkan bangun datar yang dibagi menjadi empat bagian dengan luas yang sama persis.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep pecahan 1/4 sebagai pembagian benda utuh menjadi empat bagian yang sama besar, yang merupakan penerapan konsep dasar pecahan.. Bukti: Gambar mana yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang syarat pecahan (bagian yang sama besar) pada representasi visual.. Bukti: Gambar mana yang menunjukkan seperempat?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk membedakan antara pembagian menjadi empat bagian secara umum dengan pembagian menjadi empat bagian yang sama besar (seperempat).. Bukti: Gambar mana yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep kesamaan ukuran (kongruensi visual). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pembagian yang sama besar dari yang tidak sama besar memerlukan ketelitian visual yang melampaui sekadar pengenalan simbol, namun masih dalam lingkup materi pecahan dasar. |

Run 2 — solusi: Seperempat (1/4) berarti satu bagian dari empat bagian yang sama besar. Hanya gambar 2 yang memiliki empat bagian dengan luas dan bentuk yang identik.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep pecahan sederhana (seperempat) dan membedakan antara pembagian yang menghasilkan bagian sama besar dengan yang tidak. Ini adalah proses menerapkan konsep dasar pecahan pada representasi visual.. Bukti: Gambar mana yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' (bagian yang sama besar dari keseluruhan), bukan sekadar menghafal fakta atau mengikuti prosedur algoritma.. Bukti: Gambar mana yang menunjukkan seperempat?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan diskriminasi visual terhadap empat opsi. Meskipun konsepnya dasar, siswa harus menolak pengecoh yang terlihat mirip namun tidak memenuhi syarat 'sama besar'.. Bukti: Gambar mana yang menunjukkan seperempat?

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
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pecahan yang benar dari pengecoh visual yang tampak mirip namun tidak kongruen memerlukan ketelitian lebih daripada sekadar mengidentifikasi gambar yang diarsir secara acak. |

Run 3 — solusi: Seperempat (1/4) dari sebuah benda utuh harus terdiri dari empat bagian yang sama besar (kongruen). Hanya pada gambar kedua (segi enam), bangun tersebut dibagi oleh garis simetri vertikal dan horizontal yang membagi luas bangun menjadi empat bagian yang identik.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep pecahan sederhana (seperempat) dengan membedakan antara pembagian yang menghasilkan bagian sama besar dan yang tidak. Ini melibatkan penerapan konsep dasar pecahan pada representasi visual.. Bukti: Gambar mana yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' (bagian yang sama besar dari keseluruhan), bukan sekadar menghafal fakta atau mengikuti prosedur algoritma.. Bukti: Seperempat dari Benda Utuh
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan diskriminasi visual terhadap empat opsi. Meskipun konsepnya dasar, siswa harus menolak pengecoh yang terlihat mirip namun tidak memenuhi syarat 'sama besar', yang merupakan langkah kognitif penting untuk kelas 2.. Bukti: Gambar mana yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep kesamaan ukuran (kongruensi visual). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, membedakan pecahan yang benar dari yang salah berdasarkan visualisasi adalah tugas yang sesuai, namun tingkat kesulitannya 'Medium' karena adanya pengecoh visual yang mengharuskan siswa teliti dalam membandingkan luas bagian. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 159/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000318; applying=0.999682; reasoning=0.000000 | applying | 0.999682 | 0.002623 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.009228; conceptual=0.988060; procedural=0.002712; metacognitive=0.000000 | conceptual | 0.988060 | 0.051314 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.724551; Medium=0.269116; Hard=0.006333 | Easy | 0.724551 | 0.563213 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999682; −Σp ln(p) = 0.002882; H = 0.002882/ln(3) = 0.002623; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.988060; −Σp ln(p) = 0.071136; H = 0.071136/ln(4) = 0.051314; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.724551; −Σp ln(p) = 0.618753; H = 0.618753/ln(3) = 0.563213; T = 0.953328.


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
Transkripsi visual: Terdapat empat gambar bangun datar yang dibagi menjadi empat bagian. Gambar 1 adalah segitiga yang dibagi tidak sama besar. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis vertikal dan horizontal tepat di tengah, menghasilkan empat bagian yang kongruen (sama besar dan bentuk). Gambar 3 adalah bangun menyerupai anak panah yang dibagi tidak simetris. Gambar 4 adalah persegi panjang yang dibagi menjadi empat bagian dengan ukuran berbeda.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Seperempat didefinisikan sebagai satu bagian dari empat bagian yang sama besar. Gambar D menunjukkan sebuah persegi yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir, sehingga merepresentasikan seperempat.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0160-01.png. Transkripsi visual: Terdapat 8 gambar bangun datar berlabel A sampai H. Gambar A: segitiga utuh. Gambar B: jajar genjang dibagi 4, 1 bagian diarsir. Gambar C: persegi panjang dibagi 4, 2 bagian diarsir (setengah). Gambar D: persegi dibagi 4, 1 bagian diarsir (seperempat). Gambar E: bintang, ujung atas diarsir. Gambar F: pentagon dibagi 2, 1 bagian diarsir. Gambar G: lingkaran dibagi 4, 2 bagian diarsir. Gambar H: persegi dibagi 4 kolom, 1 kolom diarsir.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9fbf87b391e4ef12c74b1b1a0fd3fe8f8f5398a89327dd5c210a3e3bc807cdcd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | knowing | conceptual | Easy | 2552 |
| 2 | success | concern / conflict | knowing | conceptual | Easy | 2617 |
| 3 | success | concern / conflict | knowing | conceptual | Easy | 2677 |

Run 1 — solusi: Seperempat berarti satu bagian dari empat bagian yang sama besar. Gambar D menunjukkan persegi yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali representasi visual dari pecahan seperempat (1/4) di antara berbagai pilihan gambar.. Bukti: Manakah yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar pecahan sebagai bagian dari keseluruhan.. Bukti: Manakah yang menunjukkan seperempat?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan identifikasi visual sederhana dari konsep pecahan dasar.. Bukti: Manakah yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep pecahan seperempat dan pembagian benda menjadi bagian sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual pecahan sederhana tanpa perhitungan kompleks. |

Run 2 — solusi: Seperempat berarti satu dari empat bagian yang sama besar. Gambar D menunjukkan persegi yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali representasi visual dari konsep pecahan sederhana (seperempat) dan membedakannya dari representasi lain.. Bukti: Manakah yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pecahan sebagai bagian dari keseluruhan.. Bukti: seperempat dari benda utuh
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengenalan visual langsung terhadap konsep pecahan dasar yang umum diajarkan di kelas 2.. Bukti: Manakah yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep bagian dari keseluruhan (pecahan sederhana). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual pecahan sederhana tanpa operasi hitung. |

Run 3 — solusi: Seperempat didefinisikan sebagai satu dari empat bagian yang sama besar. Gambar D adalah persegi yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir, sehingga merepresentasikan seperempat.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali representasi visual dari pecahan seperempat dan membedakannya dari representasi lain (seperti setengah atau bagian tidak sama besar). Ini adalah proses pengenalan konsep dasar.. Bukti: Manakah yang menunjukkan seperempat?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep pecahan sederhana (seperempat) sebagai bagian dari keseluruhan.. Bukti: Manakah yang menunjukkan seperempat?
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena hanya meminta identifikasi visual langsung dari konsep dasar pecahan yang umum diajarkan di kelas 2.. Bukti: Manakah yang menunjukkan seperempat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep bagian dari keseluruhan (pecahan sederhana). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah diperkenalkan dengan konsep pecahan sederhana seperti setengah dan seperempat melalui representasi visual benda konkret atau bangun datar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3792`.
Konten: `concern`; kunci: `conflict`; masalah: Kunci jawaban pada sumber (A) salah. Berdasarkan analisis visual, gambar A adalah segitiga utuh yang tidak dibagi. Gambar D adalah persegi yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir, yang secara akurat merepresentasikan seperempat (1/4).; Terdapat ketidaksesuaian antara label pilihan jawaban pada soal dengan gambar yang tersedia. Pilihan jawaban A, B, C, D merujuk pada gambar yang berbeda dari label huruf di bawah gambar (A-H)..
- Domain kognitif `knowing`: Siswa diminta untuk mengenali representasi visual dari konsep pecahan seperempat (1/4) di antara berbagai pilihan gambar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sebagai bagian dari keseluruhan.
- Intended difficulty `Easy`: Soal ini bersifat rutin untuk kelas 2, melibatkan identifikasi visual sederhana dari konsep pecahan dasar tanpa perhitungan kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep pecahan seperempat dan pembagian benda menjadi bagian sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pengenalan visual pecahan sederhana. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 171/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

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
Transkripsi visual: Terdapat 8 gambar bangun datar berlabel A sampai H. Gambar A: segitiga utuh. Gambar B: jajar genjang dibagi 4, 1 bagian diarsir. Gambar C: persegi panjang dibagi 4, 2 bagian diarsir (setengah). Gambar D: persegi dibagi 4, 1 bagian diarsir (seperempat). Gambar E: bintang, ujung atas diarsir. Gambar F: pentagon dibagi 2, 1 bagian diarsir. Gambar G: lingkaran dibagi 4, 2 bagian diarsir. Gambar H: persegi dibagi 4 kolom, 1 kolom diarsir.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Kunci jawaban pada sumber (A) salah. Berdasarkan analisis visual, gambar A adalah segitiga utuh yang tidak dibagi. Gambar D adalah persegi yang dibagi menjadi empat bagian sama besar dengan satu bagian diarsir, yang secara akurat merepresentasikan seperempat (1/4).; Terdapat ketidaksesuaian antara label pilihan jawaban pada soal dengan gambar yang tersedia. Pilihan jawaban A, B, C, D merujuk pada gambar yang berbeda dari label huruf di bawah gambar (A-H)..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0188-04.png. Transkripsi visual: Gambar 1: Timbangan seimbang dengan 2 mangga di sisi kiri dan 1 pepaya di sisi kanan. Gambar 2: Timbangan seimbang dengan 1 mangga di sisi kiri dan 2 manggis di sisi kanan. Pertanyaan: 1 pepaya setara dengan berapa manggis.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3f0c12b584a154cf06dbdbbbf728acf99c03ab8e18764a117e3c96f4c99be8a4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2619 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2605 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2573 |

Run 1 — solusi: Dari gambar, 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 2 mangga = 2 x 2 manggis = 4 manggis. Jadi, 1 pepaya = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan dua informasi terpisah dari gambar (transitif) untuk menentukan kesetaraan antara pepaya dan manggis. Ini melibatkan penerapan konsep kesetaraan dalam situasi rutin.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis; Berat 1 pepaya adalah .... manggis
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami struktur hubungan kesetaraan (ekuivalensi) antar objek untuk menyelesaikan masalah, yang merupakan pemahaman konseptual.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah penalaran logis (transitif) yang cukup menantang untuk kelas 2, namun masih dalam konteks rutin.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang timbangan/kesetaraan dan perkalian dasar (2x2). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, menghubungkan dua fakta kesetaraan (transitif) adalah langkah yang sedikit lebih kompleks daripada sekadar membaca satu timbangan, sehingga dikategorikan Medium. |

Run 2 — solusi: Dari gambar, 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 2 mangga = 2 x 2 manggis = 4 manggis. Jadi, 1 pepaya = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan dua informasi terpisah dari gambar untuk menyimpulkan hubungan antara pepaya dan manggis melalui substitusi nilai.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis; Berat 1 pepaya adalah .... manggis
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang prinsip kesetaraan dalam pengukuran berat dan bagaimana menghubungkan dua rasio yang berbeda.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah penalaran (transitif) untuk menghubungkan tiga objek berbeda, yang sedikit di atas prosedur satu langkah standar untuk kelas 2.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang timbangan sebagai alat ukur berat dan konsep kesetaraan (ekuivalensi). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, menghubungkan dua fakta kesetaraan (transitivitas) adalah tantangan kognitif yang sesuai untuk tingkat menengah, karena memerlukan lebih dari sekadar membaca satu timbangan. |

Run 3 — solusi: Dari gambar, 1 pepaya = 2 mangga. Karena 1 mangga = 2 manggis, maka 2 mangga = 2 x 2 manggis = 4 manggis. Jadi, 1 pepaya = 4 manggis.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan dua informasi dari dua gambar berbeda untuk menyimpulkan hubungan antara pepaya dan manggis melalui substitusi nilai.. Bukti: 1 pepaya = 2 mangga; 1 mangga = 2 manggis; 1 pepaya = 4 manggis
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kesetaraan berat dan bagaimana hubungan antar objek dapat ditransitifkan.. Bukti: Berat 1 pepaya adalah .... manggis
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa melakukan dua langkah penalaran (substitusi) yang melibatkan hubungan proporsional sederhana, yang sesuai untuk tingkat kelas 2.. Bukti: 2 mangga = 1 pepaya; 1 mangga = 2 manggis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang timbangan/kesetaraan berat dan perkalian dasar (2x2). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 2, menghubungkan dua informasi visual untuk mendapatkan jawaban akhir adalah tugas yang menantang namun sesuai dengan kurikulum pengukuran. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 108/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000739; applying=0.999261; reasoning=0.000000 | applying | 0.999261 | 0.005519 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.075588; conceptual=0.893483; procedural=0.030929; metacognitive=0.000000 | conceptual | 0.893483 | 0.290953 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.844636; Medium=0.151620; Hard=0.003744 | Easy | 0.844636 | 0.409198 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999261; −Σp ln(p) = 0.006064; H = 0.006064/ln(3) = 0.005519; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.893483; −Σp ln(p) = 0.403346; H = 0.403346/ln(4) = 0.290953; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.844636; −Σp ln(p) = 0.449550; H = 0.449550/ln(3) = 0.409198; T = 0.953328.


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
Transkripsi visual: Gambar 1: Timbangan seimbang dengan 2 mangga di sisi kiri dan 1 pepaya di sisi kanan. Gambar 2: Timbangan seimbang dengan 1 mangga di sisi kiri dan 2 manggis di sisi kanan. Pertanyaan: 1 pepaya setara dengan berapa manggis.
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

![Gambar sumber soal 33](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0200-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pada gambar kiri, 1 jeruk berada di satu sisi timbangan dan 2 stroberi di sisi lainnya dalam posisi seimbang, sehingga berat 1 jeruk sama dengan 2 stroberi.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0200-01.png. Transkripsi visual: Terdapat dua gambar timbangan. Gambar kiri menunjukkan 1 jeruk seimbang dengan 2 stroberi. Gambar kanan menunjukkan 2 jeruk seimbang dengan 4 stroberi.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e6632b981b4e527a06f27c494363a3451fd915782ab3f8b4cd9d46c180b74da`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2484 |
| 2 | success | valid / verified | knowing | factual | Easy | 2484 |
| 3 | success | valid / verified | knowing | factual | Easy | 2475 |

Run 1 — solusi: Pada gambar kiri, 1 jeruk berada di satu sisi timbangan dan 2 stroberi di sisi lainnya dalam posisi seimbang, sehingga berat 1 jeruk sama dengan 2 stroberi.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca informasi visual secara langsung dari timbangan untuk menentukan kesetaraan berat, yang merupakan proses pengenalan fakta visual.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.; Gambar kiri menunjukkan 1 jeruk seimbang dengan 2 stroberi.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang konsep dasar pengukuran berat melalui perbandingan visual (fakta bahwa benda yang seimbang memiliki berat yang sama).. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan observasi visual sederhana pada satu timbangan tanpa perhitungan atau manipulasi data.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.; Gambar kiri menunjukkan 1 jeruk seimbang dengan 2 stroberi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca timbangan sederhana dan menghitung jumlah benda. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan representasi visual konkret untuk konsep dasar pengukuran berat. |

Run 2 — solusi: Pada gambar pertama, timbangan menunjukkan 1 jeruk setara dengan 2 stroberi.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca informasi visual secara langsung dari timbangan pertama tanpa perlu melakukan perhitungan atau penalaran kompleks.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.; timbangan pertama menunjukkan 1 buah jeruk di sisi kiri seimbang dengan 2 buah stroberi
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang konsep kesetaraan berat sederhana yang ditunjukkan melalui alat ukur (timbangan).. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan observasi visual langsung terhadap satu timbangan.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.; timbangan pertama menunjukkan 1 buah jeruk di sisi kiri seimbang dengan 2 buah stroberi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca timbangan sederhana dan menghitung jumlah objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan representasi visual konkret untuk konsep pengukuran dasar. |

Run 3 — solusi: Pada timbangan kiri, 1 jeruk berada di sisi kiri dan 2 stroberi berada di sisi kanan dalam posisi seimbang, sehingga 1 jeruk = 2 stroberi.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca informasi langsung dari representasi visual timbangan yang seimbang tanpa perlu melakukan perhitungan atau strategi kompleks.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.; timbangan kiri menunjukkan 1 jeruk setara dengan 2 stroberi
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang konsep kesetaraan berat melalui alat ukur timbangan sederhana.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, menggunakan representasi visual yang umum, dan hanya memerlukan satu langkah observasi sederhana.. Bukti: Berat 1 buah jeruk sama dengan .... stroberi.; timbangan kiri menunjukkan 1 jeruk setara dengan 2 stroberi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca timbangan sederhana dan menghitung jumlah objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan objek konkret dan visualisasi timbangan yang merupakan materi dasar pengukuran berat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 91/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.233716; applying=0.766284; reasoning=0.000000 | applying | 0.766284 | 0.494922 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.034276; conceptual=0.959046; procedural=0.006678; metacognitive=0.000000 | conceptual | 0.959046 | 0.136462 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.799905; Medium=0.194858; Hard=0.005238 | Easy | 0.799905 | 0.477680 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.766284; −Σp ln(p) = 0.543728; H = 0.543728/ln(3) = 0.494922; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.959046; −Σp ln(p) = 0.189177; H = 0.189177/ln(4) = 0.136462; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.799905; −Σp ln(p) = 0.524785; H = 0.524785/ln(3) = 0.477680; T = 0.953328.


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
Transkripsi visual: Terdapat dua gambar timbangan. Gambar kiri menunjukkan 1 jeruk seimbang dengan 2 stroberi. Gambar kanan menunjukkan 2 jeruk seimbang dengan 4 stroberi.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Mengurutkan waktu pada jam: 06.00 (C: bangun tidur) -> 08.00 (D: menyikat gigi) -> 12.00 (B: makan siang) -> 16.00 (A: bermain bola). Urutan yang benar adalah C, D, B, A.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png. Transkripsi visual: Terdapat empat gambar kegiatan dengan jam analog: Gambar A (bermain bola, jam 04.00), Gambar B (makan siang, jam 12.00), Gambar C (bangun tidur, jam 06.00), Gambar D (menyikat gigi, jam 08.00).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c3fc214ef4d91f23f183221431a5bc6f8fa1edae391a2e4b04a840677beaed1e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Easy | 2579 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2586 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2571 |

Run 1 — solusi: Urutan kronologis berdasarkan waktu: bangun tidur (pukul 06.00) -> menyikat gigi (pukul 08.00) -> makan siang (pukul 12.00) -> bermain bola (pukul 16.00). Urutan ini sesuai dengan opsi B.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi visual dari jam dan konteks kegiatan sehari-hari untuk menyusun urutan kronologis, yang merupakan proses penalaran sederhana.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam kehidupan sehari-hari dan bagaimana waktu tersebut direpresentasikan dalam jam analog.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena menggunakan konteks kegiatan sehari-hari yang sangat familiar bagi siswa kelas 2. Prosedur pengurutannya langsung dan tidak memerlukan strategi kompleks.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog sederhana dan pemahaman urutan kegiatan harian. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menghubungkan konsep waktu dengan rutinitas harian yang umum. |

Run 2 — solusi: Mengurutkan kegiatan berdasarkan waktu pada jam: 06.00 (bangun tidur) -> 08.00 (menyikat gigi) -> 12.00 (makan siang) -> 16.00 (bermain bola). Urutan yang benar adalah C, D, B, A (opsi B).
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi urutan kronologis kegiatan sehari-hari berdasarkan penunjuk waktu (jam) yang diberikan, yang merupakan penerapan konsep waktu dalam situasi rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara waktu (jam) dengan urutan kegiatan sehari-hari, yang merupakan pengetahuan konseptual.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena menggunakan konteks kegiatan sehari-hari yang sangat familiar bagi siswa kelas 2, dengan penunjuk waktu yang jelas pada setiap gambar.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog sederhana dan memahami urutan waktu dalam sehari (pagi, siang, sore). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena mengaitkan pembacaan jam dasar dengan rutinitas harian yang umum. |

Run 3 — solusi: Mengurutkan kegiatan berdasarkan waktu jam: 06.00 (bangun tidur) -> 08.00 (menyikat gigi) -> 12.00 (makan siang) -> 04.00 sore (bermain bola). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang urutan waktu harian dan membaca jam analog sederhana untuk mengurutkan kejadian, yang merupakan penerapan konsep dalam situasi rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam kehidupan sehari-hari yang dikaitkan dengan representasi jam.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena menggunakan konteks kegiatan sehari-hari yang sangat familiar bagi siswa kelas 2, dengan langkah-langkah yang jelas dan langsung.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog sederhana dan memahami urutan kegiatan harian. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena mengaitkan konsep waktu dengan rutinitas harian yang konkret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3948`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan pemahaman tentang urutan waktu harian dan membaca jam analog sederhana untuk mengurutkan kejadian, yang merupakan penerapan konsep dalam situasi rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara waktu (jam) dengan urutan kegiatan sehari-hari.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena menggunakan konteks kegiatan sehari-hari yang sangat familiar bagi siswa kelas 2, dengan penunjuk waktu yang jelas pada setiap gambar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog sederhana dan memahami urutan waktu dalam sehari. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena mengaitkan pembacaan jam dasar dengan rutinitas harian yang umum. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 159/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.002368; applying=0.997632; reasoning=0.000000 | applying | 0.997632 | 0.015182 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.024236; conceptual=0.973505; procedural=0.002259; metacognitive=0.000000 | conceptual | 0.973505 | 0.093820 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.686724; Medium=0.306683; Hard=0.006593 | Easy | 0.686724 | 0.595001 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997632; −Σp ln(p) = 0.016679; H = 0.016679/ln(3) = 0.015182; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.973505; −Σp ln(p) = 0.130062; H = 0.130062/ln(4) = 0.093820; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.686724; −Σp ln(p) = 0.653676; H = 0.653676/ln(3) = 0.595001; T = 0.953328.


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
Transkripsi visual: Terdapat empat gambar kegiatan dengan jam analog: Gambar A (bermain bola, jam 04.00), Gambar B (makan siang, jam 12.00), Gambar C (bangun tidur, jam 06.00), Gambar D (menyikat gigi, jam 08.00).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `c0080230ef4ab5e5b0a07c55`

Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

| Opsi | Isi |
|---|---|
| A | Bermain bola |
| B | Mencuci tangan |
| C | Sarapan |
| D | Menyisir rambut |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bermain bola membutuhkan waktu lebih lama (menit/jam) dibandingkan mencuci tangan (detik).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `26ae878e7d015a21a6f104d1b42787b9933459662bbbb15770f625379d6226dc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1321 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1292 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1326 |

Run 1 — solusi: Bermain bola membutuhkan waktu lebih lama (menit/jam) dibandingkan mencuci tangan (detik).
- Domain kognitif `classify/applying`: Siswa perlu membandingkan durasi dua kegiatan sehari-hari yang familiar. Ini termasuk dalam kategori applying karena menerapkan pemahaman konsep durasi waktu pada situasi rutin.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep durasi waktu (lama/sebentar) dalam konteks kegiatan sehari-hari, yang merupakan pengetahuan konseptual.. Bukti: Kegiatan manakah yang lebih lama
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2, melibatkan perbandingan durasi dua aktivitas yang sangat kontras dalam kehidupan sehari-hari.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep waktu (lama dan sebentar) dalam aktivitas sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah memiliki pengalaman empiris yang cukup untuk membedakan durasi aktivitas fisik seperti mencuci tangan dan bermain bola tanpa perlu perhitungan formal. |

Run 2 — solusi: Bermain bola membutuhkan waktu lebih lama (menit/jam) dibandingkan mencuci tangan (detik).
- Domain kognitif `classify/applying`: Siswa perlu membandingkan durasi dua kegiatan sehari-hari berdasarkan pengetahuan umum tentang waktu, yang merupakan proses penerapan konsep durasi.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang durasi waktu relatif antara dua aktivitas.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2, melibatkan perbandingan durasi kegiatan yang sangat familiar dalam kehidupan sehari-hari tanpa perhitungan matematis yang rumit.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang durasi waktu (lama/sebentar) dalam konteks aktivitas sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah sangat familiar dengan durasi aktivitas fisik seperti bermain dan aktivitas kebersihan diri, sehingga soal ini termasuk kategori mudah. |

Run 3 — solusi: Bermain bola membutuhkan waktu lebih lama (menit/jam) dibandingkan mencuci tangan (detik).
- Domain kognitif `classify/applying`: Siswa perlu membandingkan durasi dua kegiatan sehari-hari yang sudah dikenal, yang merupakan proses menerapkan pemahaman konsep waktu dalam situasi rutin.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang durasi waktu (lama vs sebentar) dalam konteks kegiatan sehari-hari.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 2, melibatkan perbandingan durasi dua aktivitas yang sangat kontras (detik vs menit/jam) tanpa memerlukan perhitungan matematis.. Bukti: Kegiatan manakah yang lebih lama, mencuci tangan atau bermain bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep durasi waktu (lama dan sebentar) dalam kehidupan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah memiliki pengalaman empiris yang cukup untuk membedakan durasi aktivitas fisik sederhana seperti mencuci tangan dan bermain bola. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Terdapat 6 keranjang, masing-masing berisi 10 jeruk. Jadi, 6 puluhan = 60.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0215-04.png. Transkripsi visual: Terdapat 6 keranjang jeruk yang disusun berjajar. Setiap keranjang berisi 10 buah jeruk.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `194f28fad83ae3a184b3f13ace898326ec68ba62b1c1fbb73fb393ed4dae64ff`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2541 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2515 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2568 |

Run 1 — solusi: Terdapat 6 keranjang, masing-masing berisi 10 jeruk. Jadi, 6 puluhan = 60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur yang sudah dicontohkan (mengelompokkan benda menjadi puluhan) ke dalam situasi rutin yang serupa.. Bukti: Lakukan seperti contoh; 6 keranjang berisi 10 buah jeruk
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengelompokan bilangan menjadi puluhan dan satuan.. Bukti: 6 puluhan = 60
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, menggunakan representasi visual yang jelas, dan mengikuti pola contoh yang diberikan, sehingga beban kognitifnya rendah untuk siswa kelas 2.. Bukti: 6 keranjang berisi 10 buah jeruk; Lakukan seperti contoh

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda dan memahami konsep dasar puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan contoh eksplisit dan visual yang mendukung konsep puluhan. |

Run 2 — solusi: Terdapat 6 keranjang, di mana setiap keranjang mewakili 1 puluhan. Jadi, 6 puluhan = 60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep nilai tempat (puluhan) pada situasi rutin yang sudah diberikan contohnya.. Bukti: Hitunglah banyak benda berikut.; 6 keranjang berisi 10 buah jeruk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur sistem bilangan desimal (konsep puluhan).. Bukti: 5 puluhan = 50; .... puluhan = ....
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, mengikuti pola contoh yang diberikan, dan hanya memerlukan satu operasi penghitungan dasar.. Bukti: Lakukan seperti contoh.; 6 keranjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda dan memahami konsep dasar puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan representasi visual konkret (keranjang) untuk memahami konsep puluhan. |

Run 3 — solusi: Terdapat 6 keranjang, setiap keranjang mewakili 1 puluhan. Jadi, 6 puluhan = 60.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi jumlah kelompok (puluhan) dan mengonversinya ke nilai bilangan. Ini adalah proses langsung menerapkan konsep nilai tempat yang sudah dicontohkan.. Bukti: Hitunglah banyak benda berikut; 6 keranjang berisi 10 buah jeruk
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat (puluhan) dan bagaimana kelompok benda direpresentasikan sebagai angka.. Bukti: 5 puluhan = 50; 6 keranjang berisi 10 buah jeruk
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena menyediakan contoh eksplisit (scaffolding) dan hanya memerlukan penghitungan benda konkret yang dikelompokkan secara visual.. Bukti: Contoh: 5 puluhan = 50; 6 keranjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda sampai 100 dan memahami konsep dasar puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan bantuan visual dan contoh pengerjaan yang serupa dengan tugas utama. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3766`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pengelompokan yang sudah dicontohkan (puluhan) ke dalam situasi rutin yang serupa.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat (puluhan) dan bagaimana kelompok benda direpresentasikan sebagai angka.
- Intended difficulty `Easy`: Soal ini bersifat rutin, menyediakan contoh eksplisit (scaffolding), dan hanya memerlukan penghitungan benda konkret yang dikelompokkan secara visual.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda sampai 100 dan memahami konsep dasar puluhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena menggunakan bantuan visual dan contoh pengerjaan yang serupa dengan tugas utama. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 144/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.006533; conceptual=0.991774; procedural=0.001693; metacognitive=0.000000 | conceptual | 0.991774 | 0.037411 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.784003; Medium=0.210968; Hard=0.005029 | Easy | 0.784003 | 0.496692 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.991774; −Σp ln(p) = 0.051863; H = 0.051863/ln(4) = 0.037411; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.784003; −Σp ln(p) = 0.545672; H = 0.545672/ln(3) = 0.496692; T = 0.953328.


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
Transkripsi visual: Terdapat 6 keranjang jeruk yang disusun berjajar. Setiap keranjang berisi 10 buah jeruk.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `98cb95b9467c6a458263f9f1`

Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan .....

| Opsi | Isi |
|---|---|
| A | 780 |
| B | 87 |
| C | 70 |
| D | 78 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Tujuh puluh delapan berarti 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6a2aa6752dff40dfb11d7dec5fa27cebbe8d5c6b01f63e065735531d33af97d0`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1317 |
| 2 | success | valid / verified | knowing | factual | Easy | 1317 |
| 3 | success | valid / verified | knowing | factual | Easy | 1303 |

Run 1 — solusi: Tujuh puluh delapan berarti 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nama bilangan dan mengubahnya menjadi lambang bilangan (simbol numerik) secara langsung tanpa proses tambahan.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol numerik dan cara penulisan bilangan dasar (fakta matematika).. Bukti: lambang bilangan; nama bilangannya
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar untuk kelas 2, hanya melibatkan pengenalan simbol bilangan dua digit yang umum.. Bukti: Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan serta simbol angka 0-9. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD untuk materi dasar membaca dan menulis bilangan sampai 100. |

Run 2 — solusi: Tujuh puluh delapan berarti 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nama bilangan dan mengubahnya menjadi lambang bilangan (simbol numerik) secara langsung tanpa proses tambahan.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol numerik dan cara penulisan bilangan dasar (fakta matematika).. Bukti: lambang bilangan; nama bilangannya
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar untuk kelas 2, melibatkan pengenalan simbol bilangan dua digit yang umum.. Bukti: Tujuh puluh delapan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan serta simbol angka 0-9. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 SD untuk materi membaca dan menulis lambang bilangan sampai 100. |

Run 3 — solusi: Tujuh puluh delapan terdiri dari 7 puluhan dan 8 satuan, yang ditulis sebagai 78.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nama bilangan dan mengubahnya menjadi lambang bilangan (simbol numerik) secara langsung tanpa proses tambahan.. Bukti: Tulislah lambang bilangan sesuai dengan nama bilangannya. Tujuh puluh delapan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol numerik dan cara penulisan bilangan dasar (fakta matematika).. Bukti: lambang bilangan; nama bilangannya
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas dasar yang sangat rutin untuk siswa kelas 2, hanya melibatkan satu langkah pengenalan simbol.. Bukti: Tujuh puluh delapan

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
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 untuk pengenalan lambang bilangan sampai 100. |

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

Aku adalah bilangan. Aku 1 kurangnya dari bilangan 67. Bilangan berapakah aku?

| Opsi | Isi |
|---|---|
| A | 67 |
| B | 66 |
| C | 68 |
| D | 57 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 1 kurangnya dari 67 berarti 67 - 1 = 66.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `431d8432578105217fba86c0356466133ef278b84e149dda67ecf490a31a275a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1302 |
| 2 | success | valid / verified | knowing | factual | Easy | 1250 |
| 3 | success | valid / verified | knowing | factual | Easy | 1281 |

Run 1 — solusi: 1 kurangnya dari 67 berarti 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Siswa perlu memahami konsep '1 kurangnya' dan menerapkannya pada bilangan yang diberikan. Ini adalah proses langsung yang melibatkan pemahaman dasar tentang urutan bilangan.. Bukti: Aku 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang urutan bilangan dan konsep dasar pengurangan satu satuan.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, melibatkan operasi pengurangan satu langkah yang sangat familiar.. Bukti: 1 kurangnya dari bilangan 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan cacah hingga 100 dan konsep pengurangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 2 yang menekankan pemahaman nilai tempat dan urutan bilangan. |

Run 2 — solusi: 1 kurangnya dari 67 berarti 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar (67-1) yang merupakan proses langsung.. Bukti: 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dan konsep 'kurang dari' sebagai fakta dasar dalam sistem bilangan.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu langkah operasi pengurangan sederhana pada bilangan dua digit.. Bukti: 1 kurangnya dari bilangan 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan cacah hingga 100 dan konsep pengurangan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena fokus pada pemahaman nilai tempat dan urutan bilangan dasar. |

Run 3 — solusi: 1 kurangnya dari 67 berarti 67 - 1 = 66.
- Domain kognitif `classify/knowing`: Siswa perlu memahami konsep '1 kurangnya' sebagai operasi pengurangan dasar atau pemahaman urutan bilangan, yang merupakan proses langsung.. Bukti: 1 kurangnya dari bilangan 67
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang urutan bilangan dan konsep dasar pengurangan satu satuan.. Bukti: 1 kurangnya dari bilangan 67
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah operasi pengurangan sederhana pada bilangan dua digit.. Bukti: 1 kurangnya dari bilangan 67

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena hanya melibatkan pengurangan satu satuan dari bilangan dua digit yang umum dipelajari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Menghitung jumlah mainan mobil-mobilan yang ada di lantai, yaitu satu mobil merah dan satu mobil ungu, totalnya ada 2.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0246-03.png. Transkripsi visual: Gambar menunjukkan seorang anak perempuan memegang kotak berisi boneka beruang. Di lantai terdapat mainan: 2 mobil-mobilan (satu merah, satu ungu), 3 boneka beruang/kelinci, 6 balok susun, dan 5 kelereng.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e7c1808e59e24cc84e194e6080bc05387be67e9306a8176f8e33f59ff9961dfe`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2508 |
| 2 | success | valid / verified | knowing | factual | Easy | 2504 |
| 3 | success | valid / verified | knowing | factual | Easy | 2493 |

Run 1 — solusi: Menghitung jumlah mainan mobil-mobilan yang ada di lantai, yaitu satu mobil merah dan satu mobil ungu, totalnya ada 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses menghitung objek secara langsung (counting) dari gambar yang disediakan tanpa perlu strategi kompleks.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan siswa dalam mengidentifikasi objek konkret dan menghitung jumlahnya, yang merupakan pengetahuan faktual dasar.. Bukti: Berapa banyak mainan mobil-mobilan
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung dan penghitungan objek tunggal yang mudah dibedakan.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?

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
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena hanya melibatkan penghitungan benda konkret sederhana dalam konteks pengumpulan data awal. |

Run 2 — solusi: Mengamati gambar secara langsung, terdapat satu mobil-mobilan berwarna merah dan satu mobil-mobilan berwarna ungu. Total mobil-mobilan adalah 1 + 1 = 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses identifikasi visual langsung dan menghitung objek yang terlihat secara eksplisit dalam gambar.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menanyakan fakta kuantitatif sederhana tentang objek yang ada dalam gambar (penghitungan benda konkret).. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pengamatan visual langsung tanpa proses manipulasi data atau strategi kompleks.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?

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
| gradeRelativeRationale | Sesuai untuk kelas 2 SD yang sedang belajar pengumpulan data sederhana melalui pengamatan objek. |

Run 3 — solusi: Menghitung jumlah mainan mobil-mobilan yang terlihat pada gambar, yaitu satu mobil merah dan satu mobil ungu, totalnya ada 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses identifikasi visual langsung dan menghitung objek yang terlihat (counting), yang merupakan proses kognitif tingkat dasar.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menuntut pengetahuan faktual tentang jumlah objek dalam kumpulan data visual sederhana.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta penghitungan objek visual yang jelas dan terpisah.. Bukti: Berapa banyak mainan mobil-mobilan pada gambar tersebut?

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
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena melibatkan pengamatan data visual sederhana yang merupakan pengenalan awal terhadap statistika. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 111/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000005; applying=0.999995; reasoning=0.000000 | applying | 0.999995 | 0.000057 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.256535; conceptual=0.740791; procedural=0.002674; metacognitive=0.000000 | conceptual | 0.740791 | 0.423517 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.838790; Medium=0.157653; Hard=0.003557 | Easy | 0.838790 | 0.417576 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999995; −Σp ln(p) = 0.000063; H = 0.000063/ln(3) = 0.000057; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.740791; −Σp ln(p) = 0.587119; H = 0.587119/ln(4) = 0.423517; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.838790; −Σp ln(p) = 0.458754; H = 0.458754/ln(3) = 0.417576; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan seorang anak perempuan memegang kotak berisi boneka beruang. Di lantai terdapat mainan: 2 mobil-mobilan (satu merah, satu ungu), 3 boneka beruang/kelinci, 6 balok susun, dan 5 kelereng.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Mengamati gambar dan menghitung jumlah buah semangka yang ada di atas meja, yaitu hanya terdapat 1 buah semangka.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0258-04.png. Transkripsi visual: Seorang anak laki-laki berdiri di belakang meja yang berisi berbagai buah. Di atas meja terdapat 1 buah semangka besar, 3 buah apel merah, 5 buah jeruk kecil, dan 3 buah alpukat hijau.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b6be504c532a1238575ede3929865c5e0e93ec1a793ace18cdfad45b2f88825`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2469 |
| 2 | success | valid / verified | knowing | factual | Easy | 2459 |
| 3 | success | valid / verified | knowing | factual | Easy | 2455 |

Run 1 — solusi: Mengamati gambar dan menghitung jumlah buah semangka yang ada di atas meja, yaitu hanya terdapat 1 buah semangka.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses pengamatan langsung (mengenali objek) dan menghitung jumlah objek yang terlihat secara eksplisit pada gambar.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Dimensi pengetahuan `classify/factual`: Soal ini menuntut pengetahuan faktual mengenai jumlah objek konkret yang disajikan secara visual.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan identifikasi visual langsung tanpa operasi matematika kompleks atau strategi non-rutin.. Bukti: Berapa banyak buah semangka yang dibeli ibu?

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
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena melibatkan pengamatan data visual sederhana yang merupakan dasar dari literasi data. |

Run 2 — solusi: Mengamati gambar, hanya terdapat 1 buah semangka di atas meja.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses pengamatan langsung (mengenali objek) untuk menghitung jumlah item tertentu dalam gambar.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan siswa dalam mengenali objek konkret dan menghitung jumlahnya, yang merupakan pengetahuan faktual dasar.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Intended difficulty `classify/Easy`: Tugas ini sangat sederhana, hanya memerlukan identifikasi visual langsung tanpa manipulasi data atau prosedur yang kompleks.. Bukti: Berapa banyak buah semangka yang dibeli ibu?

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
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena melibatkan penghitungan objek konkret sederhana yang familiar. |

Run 3 — solusi: Mengamati gambar, hanya terdapat 1 buah semangka di atas meja.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses pengenalan visual langsung dan menghitung objek tunggal tanpa perlu strategi kompleks.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan mengenali fakta dasar (jumlah objek) dari representasi visual.. Bukti: Berapa banyak buah semangka yang dibeli ibu?
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar, hanya melibatkan identifikasi objek tunggal dalam gambar.. Bukti: Berapa banyak buah semangka yang dibeli ibu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena hanya memerlukan observasi visual sederhana untuk menghitung jumlah benda konkret. |

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
| Domain kognitif | knowing=0.000027; applying=0.999973; reasoning=0.000000 | applying | 0.999973 | 0.000284 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.283175; conceptual=0.708017; procedural=0.008807; metacognitive=0.000000 | conceptual | 0.708017 | 0.464134 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.891036; Medium=0.103513; Hard=0.005450 | Easy | 0.891036 | 0.333130 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999973; −Σp ln(p) = 0.000313; H = 0.000313/ln(3) = 0.000284; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.708017; −Σp ln(p) = 0.643427; H = 0.643427/ln(4) = 0.464134; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.891036; −Σp ln(p) = 0.365981; H = 0.365981/ln(3) = 0.333130; T = 0.953328.


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
Transkripsi visual: Seorang anak laki-laki berdiri di belakang meja yang berisi berbagai buah. Di atas meja terdapat 1 buah semangka besar, 3 buah apel merah, 5 buah jeruk kecil, dan 3 buah alpukat hijau.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `655cea6ab3fa2ff165080502`

Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.<br><br>Ada 5 anak yang suka onde-onde.<br>Ada 3 anak yang suka lemper.<br><br> Ada .... anak yang suka kue cucur.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 6 |
| C | 3 |
| D | 7 |

![Gambar sumber soal 42](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `6`.
Solusi minimum hasil AI: Menghitung jumlah bintang pada baris kue cucur di diagram, yaitu 6 bintang.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: Tabel diagram gambar menunjukkan empat jenis kue. Baris pertama (kue cucur) memiliki 6 simbol bintang. Baris kedua (onde-onde) memiliki 5 simbol bintang. Baris ketiga (lemper) memiliki 3 simbol bintang. Baris keempat (kue talam) memiliki 7 simbol bintang. Keterangan menyatakan setiap gambar mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `80c9e8175b1a87e37c364932edf8bbbc3d1cb3f5c95dad109abef944dc6905fc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2557 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2555 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2569 |

Run 1 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram, yaitu 6 bintang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang representasi data sederhana (diagram gambar) di mana simbol mewakili satuan objek.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan penghitungan satu baris data pada diagram yang sudah disediakan.. Bukti: Ada .... anak yang suka kue cucur.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret atau simbol (1-10) dan membaca tabel sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena merupakan pengenalan dasar terhadap interpretasi data visual sederhana. |

Run 2 — solusi: Menghitung jumlah simbol bintang pada baris kue cucur di diagram gambar, yaitu terdapat 6 bintang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) sebagai bentuk penyajian informasi.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Tugas ini sangat rutin bagi siswa kelas 2, hanya melibatkan penghitungan satu-satu (one-to-one correspondence) pada representasi visual yang sangat sederhana.. Bukti: Ada .... anak yang suka kue cucur.

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena diagram gambar adalah pengenalan awal statistik yang sangat mendasar dan prosedural. |

Run 3 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram gambar, yaitu ada 6 bintang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang representasi data sederhana dalam bentuk diagram gambar (pictograph), yang merupakan pengetahuan konseptual dasar.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Tugas ini sangat rutin dan langsung, hanya memerlukan penghitungan satu baris data pada diagram yang sudah disediakan.. Bukti: Ada .... anak yang suka kue cucur.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan memahami korespondensi satu-satu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena membaca diagram gambar sederhana adalah kompetensi dasar yang diharapkan pada tingkat ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 181/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000002 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004025; conceptual=0.991263; procedural=0.004712; metacognitive=0.000000 | conceptual | 0.991263 | 0.040499 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.666067; Medium=0.323197; Hard=0.010736 | Easy | 0.666067 | 0.622962 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000002; H = 0.000002/ln(3) = 0.000002; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.991263; −Σp ln(p) = 0.056143; H = 0.056143/ln(4) = 0.040499; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.666067; −Σp ln(p) = 0.684393; H = 0.684393/ln(3) = 0.622962; T = 0.953328.


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
Transkripsi visual: Tabel diagram gambar menunjukkan empat jenis kue. Baris pertama (kue cucur) memiliki 6 simbol bintang. Baris kedua (onde-onde) memiliki 5 simbol bintang. Baris ketiga (lemper) memiliki 3 simbol bintang. Baris keempat (kue talam) memiliki 7 simbol bintang. Keterangan menyatakan setiap gambar mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Menghitung jumlah bintang pada baris 'kue talam' di diagram, yaitu terdapat 7 bintang.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: Tabel diagram gambar menunjukkan empat jenis kue. Baris pertama (kue cucur) memiliki 6 bintang. Baris kedua (onde-onde) memiliki 5 bintang. Baris ketiga (lemper) memiliki 3 bintang. Baris keempat (kue talam) memiliki 7 bintang. Keterangan: setiap gambar bintang mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9b2647b871d1729caa32a2d9a31d04e4aead1a74a83210c2922992dc292add23`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2581 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2563 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2620 |

Run 1 — solusi: Menghitung jumlah bintang pada baris 'kue talam' di diagram, yaitu terdapat 7 bintang.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data secara langsung dari diagram gambar (menghitung objek visual), yang merupakan proses kognitif tingkat knowing.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) sebagai bentuk penyajian informasi, yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan penghitungan satu baris data pada diagram gambar yang sudah disediakan tanpa manipulasi atau perbandingan kompleks.. Bukti: Ada .... anak yang suka kue talam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret (1-10) dan membaca tabel sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 SD karena hanya melibatkan pembacaan data visual langsung (tallying/counting) yang merupakan standar kompetensi awal pengolahan data. |

Run 2 — solusi: Menghitung jumlah simbol bintang pada baris 'kue talam' di diagram gambar, yaitu sebanyak 7 buah.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (diagram gambar) di mana simbol mewakili satuan.. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 2, hanya memerlukan penghitungan satu-ke-satu dari representasi visual yang sudah terstruktur.. Bukti: Ada .... anak yang suka kue talam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membaca tabel sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 2 sudah terbiasa dengan diagram gambar sederhana sebagai pengenalan awal statistika. |

Run 3 — solusi: Menghitung jumlah simbol bintang pada baris 'kue talam' di diagram gambar, yaitu sebanyak 7 buah.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses membaca data langsung dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue talam.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai representasi data sederhana dalam bentuk diagram gambar (pictograph) sebagai cara menyajikan informasi.. Bukti: Diagram Gambar Kue Kesukaan.; Setiap gambar mewakili 1 anak.
- Intended difficulty `classify/Easy`: Soal ini termasuk kategori mudah karena siswa hanya perlu melakukan penghitungan langsung (one-to-one correspondence) pada representasi visual yang sangat sederhana dan familiar bagi siswa kelas 2.. Bukti: Ada .... anak yang suka kue talam.; Setiap gambar mewakili 1 anak.

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
| gradeRelativeRationale | Siswa kelas 2 sudah diajarkan membaca data sederhana. Menghitung jumlah gambar dalam baris adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 178/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000006 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003448; conceptual=0.993648; procedural=0.002904; metacognitive=0.000000 | conceptual | 0.993648 | 0.030907 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.711270; Medium=0.279701; Hard=0.009029 | Easy | 0.711270 | 0.583630 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000006; H = 0.000006/ln(3) = 0.000006; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.993648; −Σp ln(p) = 0.042846; H = 0.042846/ln(4) = 0.030907; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.711270; −Σp ln(p) = 0.641184; H = 0.641184/ln(3) = 0.583630; T = 0.953328.


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
Transkripsi visual: Tabel diagram gambar menunjukkan empat jenis kue. Baris pertama (kue cucur) memiliki 6 bintang. Baris kedua (onde-onde) memiliki 5 bintang. Baris ketiga (lemper) memiliki 3 bintang. Baris keempat (kue talam) memiliki 7 bintang. Keterangan: setiap gambar bintang mewakili 1 anak.
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

![Gambar sumber soal 44](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Jumlah anak yang suka belimbing adalah 7. Jumlah anak yang suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png. Transkripsi visual: Diagram batang vertikal menggunakan simbol bintang untuk mewakili jumlah anak. Sumbu horizontal menunjukkan jenis buah: jeruk (6 bintang), apel (4 bintang), belimbing (7 bintang), dan jambu air (5 bintang). Keterangan: 1 bintang mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 2 / Matematika SD Kelas 2. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3868c4f2131843ea9d422e7444252708da7e00861d18cc3b8e8b7c0505fcd3d5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2569 |
| 2 | success | valid / verified | applying | procedural | Easy | 2540 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2504 |

Run 1 — solusi: Jumlah anak yang suka belimbing adalah 7. Jumlah anak yang suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari piktogram (mengidentifikasi jumlah untuk belimbing dan apel) dan melakukan operasi pengurangan sederhana untuk menemukan selisih. Ini adalah penerapan prosedur rutin pada data yang diberikan.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data dalam bentuk piktogram (konsep) serta melakukan operasi hitung dasar (prosedural).. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan pembacaan data langsung dari piktogram dan operasi pengurangan satu langkah yang familiar bagi siswa kelas 2.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena piktogram adalah representasi data dasar yang umum diajarkan, dan operasi hitung yang diperlukan sangat sederhana. |

Run 2 — solusi: Jumlah anak yang suka belimbing adalah 7. Jumlah anak yang suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari diagram gambar (membaca frekuensi) dan menerapkan operasi pengurangan untuk membandingkan dua kategori. Ini adalah penerapan prosedur rutin pada data yang diberikan.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang cara membaca diagram gambar dan melakukan operasi pengurangan dasar untuk menyelesaikan masalah.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan pembacaan data langsung dari diagram gambar dan operasi pengurangan satu langkah yang rutin bagi siswa kelas 2.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak; Anak yang suka belimbing ... lebih banyak dari anak yang suka apel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek dalam diagram dan melakukan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2 karena diagram gambar adalah representasi data dasar yang umum diajarkan, dan operasi pengurangannya berada dalam rentang angka yang dikuasai. |

Run 3 — solusi: Jumlah anak yang suka belimbing adalah 7. Jumlah anak yang suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasi data dari piktogram (membaca jumlah) dan melakukan operasi pengurangan sederhana untuk membandingkan dua kategori. Ini adalah penerapan prosedur rutin pada data yang diberikan.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana data diorganisasikan dalam bentuk diagram gambar (piktogram) dan bagaimana menggunakan informasi tersebut untuk menjawab pertanyaan.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa untuk melakukan dua langkah: membaca data dari dua kolom berbeda dan melakukan operasi pengurangan untuk mencari selisih, bukan sekadar membaca satu nilai langsung.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca piktogram sederhana dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 2, di mana siswa mulai belajar membaca data dan membandingkan jumlah sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3920`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu melakukan dua langkah rutin: membaca frekuensi dari piktogram untuk dua kategori berbeda, lalu menerapkan operasi pengurangan untuk membandingkan jumlah. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara membaca data dari piktogram dan melakukan operasi hitung dasar untuk mendapatkan selisih.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya melibatkan pembacaan data langsung dari piktogram dan operasi pengurangan satu langkah yang sangat familiar bagi siswa kelas 2.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Sesuai untuk kelas 2 karena piktogram adalah representasi data dasar yang umum diajarkan, dan operasi hitung yang diperlukan sangat sederhana. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 135/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000003; applying=0.999997; reasoning=0.000000 | applying | 0.999997 | 0.000038 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.036274; conceptual=0.958963; procedural=0.004763; metacognitive=0.000000 | conceptual | 0.958963 | 0.134142 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.718459; Medium=0.272929; Hard=0.008612 | Easy | 0.718459 | 0.576101 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999997; −Σp ln(p) = 0.000042; H = 0.000042/ln(3) = 0.000038; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.958963; −Σp ln(p) = 0.185961; H = 0.185961/ln(4) = 0.134142; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.718459; −Σp ln(p) = 0.632912; H = 0.632912/ln(3) = 0.576101; T = 0.953328.


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
Transkripsi visual: Diagram batang vertikal menggunakan simbol bintang untuk mewakili jumlah anak. Sumbu horizontal menunjukkan jenis buah: jeruk (6 bintang), apel (4 bintang), belimbing (7 bintang), dan jambu air (5 bintang). Keterangan: 1 bintang mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
