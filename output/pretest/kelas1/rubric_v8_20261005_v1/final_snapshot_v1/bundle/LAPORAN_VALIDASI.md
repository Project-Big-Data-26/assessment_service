# Validasi ulang soal kelas 1 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sd-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 1 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model dipakai sebagai diagnostik; tidak diberikan kembali ke Gemini.

Jumlah soal: 50; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 31, "applying": 19, "reasoning": 0}, "knowledgeDimension": {"factual": 14, "conceptual": 18, "procedural": 18, "metacognitive": 0}, "intendedDifficulty": {"Easy": 46, "Medium": 4, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 30, "applying": 19, "reasoning": 0}, "knowledgeDimension": {"factual": 14, "conceptual": 17, "procedural": 18, "metacognitive": 0}, "intendedDifficulty": {"Easy": 45, "Medium": 4, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 49, "revision_required": 1}`.
Run awal sukses: 150/150; adjudikasi: 28; token sukses tercatat: 541,148.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 46 | 45 | [Easy.json](difficulty/Easy.json) |
| Medium | 4 | 4 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `1f52d8dff6bbb1b9be6a4516`

Ayo menghitung banyak mainan. Wei pergi ke toko mainan. Wei melihat banyak mainan. Wei kesulitan menghitungnya. Ayo bantu Wei.<br><br>Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 7 |
| C | 9 |
| D | 6 |

![Gambar sumber soal 1](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0027-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah boneka kelinci pada rak paling atas satu per satu: 1, 2, 3, 4, 5, 6. Total ada 6 boneka kelinci.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0027-06.png. Transkripsi visual: Gambar menunjukkan seorang anak perempuan di toko mainan. Terdapat rak kayu dengan empat tingkat. Tingkat paling atas berisi 6 boneka kelinci berwarna merah muda. Tingkat kedua berisi 4 pesawat mainan. Tingkat ketiga berisi 4 pesawat mainan. Tingkat keempat berisi 5 gasing. Di sebelah kiri, terdapat rak tangga berisi 7 mobil mainan merah. Di sebelah kanan, terdapat wadah berisi 5 bola warna-warni.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4060505c004d600381a76e1bd044fd74dbc2690b5ccaf2e96ea7d24ddbf2e205`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3368 |
| 2 | success | valid / verified | knowing | factual | Easy | 3377 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3365 |

Run 1 — solusi: Menghitung jumlah boneka kelinci pada rak paling atas satu per satu: 1, 2, 3, 4, 5, 6. Total ada 6 boneka kelinci.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan penghitungan objek konkret (boneka kelinci) yang terlihat langsung pada gambar. Ini adalah prosedur dasar menghitung jumlah benda.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan dasar dalam menghitung objek (fakta numerik) yang disajikan secara visual.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi objek yang diminta (boneka kelinci) dan menghitungnya. Tidak ada langkah tambahan, kendala, atau strategi kompleks yang diperlukan.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, menghitung objek visual yang terpisah dan jelas adalah tugas rutin yang sesuai dengan tingkat perkembangan mereka. |

Run 2 — solusi: Menghitung jumlah boneka kelinci pada rak paling atas secara satu per satu: 1, 2, 3, 4, 5, 6. Total ada 6 boneka kelinci.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan penghitungan langsung terhadap objek yang terlihat jelas (boneka kelinci). Ini adalah prosedur dasar menghitung benda konkret, yang termasuk dalam domain knowing.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
- Dimensi pengetahuan `classify/factual`: Siswa diminta untuk mengidentifikasi dan menghitung objek (fakta visual) untuk menentukan jumlahnya. Ini melibatkan pengenalan elemen dasar dan prosedur menghitung.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menghitung objek yang sudah dikelompokkan dengan jelas di rak. Tidak ada keputusan strategi yang kompleks atau kendala yang berinteraksi.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, menghitung objek yang terlihat jelas adalah tugas dasar yang sesuai dengan tingkat perkembangan mereka. |

Run 3 — solusi: Menghitung jumlah boneka kelinci pada rak paling atas satu per satu: 1, 2, 3, 4, 5, 6. Jumlahnya adalah 6.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan penghitungan objek secara langsung (counting) yang terlihat jelas dalam gambar. Ini adalah prosedur dasar dalam matematika kelas 1.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan prosedur menghitung (counting) untuk menentukan kuantitas dari sekumpulan objek yang diberikan.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi objek yang diminta (boneka kelinci) dan menghitungnya. Tidak ada langkah tambahan atau jebakan yang kompleks.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?

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
| gradeRelativeRationale | Tugas menghitung objek yang terlihat jelas adalah standar kompetensi dasar kelas 1 SD. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4703`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk melakukan penghitungan objek konkret (boneka kelinci) yang terlihat langsung pada gambar. Ini adalah prosedur dasar menghitung jumlah benda yang merupakan tugas rutin.
- Dimensi pengetahuan `factual`: Soal ini menguji kemampuan dasar dalam menghitung objek (fakta numerik) yang disajikan secara visual.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi objek yang diminta (boneka kelinci) dan menghitungnya. Tidak ada langkah tambahan, kendala, atau strategi kompleks yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, menghitung objek visual yang terpisah dan jelas adalah tugas rutin yang sesuai dengan tingkat perkembangan mereka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 166/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000006 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.016314; conceptual=0.980771; procedural=0.002915; metacognitive=0.000000 | conceptual | 0.980771 | 0.074446 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.659932; Medium=0.327457; Hard=0.012610 | Easy | 0.659932 | 0.632616 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000007; H = 0.000007/ln(3) = 0.000006; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.980771; −Σp ln(p) = 0.103204; H = 0.103204/ln(4) = 0.074446; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.659932; −Σp ln(p) = 0.695000; H = 0.695000/ln(3) = 0.632616; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ayo menghitung banyak mainan. Wei pergi ke toko mainan. Wei melihat banyak mainan. Wei kesulitan menghitungnya. Ayo bantu Wei.

Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
Pilihan: A. 5
B. 7
C. 9
D. 6
Transkripsi visual: Gambar menunjukkan seorang anak perempuan di toko mainan. Terdapat rak kayu dengan empat tingkat. Tingkat paling atas berisi 6 boneka kelinci berwarna merah muda. Tingkat kedua berisi 4 pesawat mainan. Tingkat ketiga berisi 4 pesawat mainan. Tingkat keempat berisi 5 gasing. Di sebelah kiri, terdapat rak tangga berisi 7 mobil mainan merah. Di sebelah kanan, terdapat wadah berisi 5 bola warna-warni.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `e91b53ee437d36556aa832b8`

Pasangkan lambang bilangan dengan namanya. Bilangan 7 dibaca ....

| Opsi | Isi |
|---|---|
| A | Tujuh |
| B | Delapan |
| C | Enam |
| D | Sembilan |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Lambang bilangan 7 memiliki nama bilangan tujuh.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `849dc6ed5ca201bcff207c533122bb986696a98a00149577001307c03802357e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2115 |
| 2 | success | valid / verified | knowing | factual | Easy | 2112 |
| 3 | success | valid / verified | knowing | factual | Easy | 2139 |

Run 1 — solusi: Lambang bilangan 7 memiliki nama bilangan tujuh.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghubungkan lambang bilangan (simbol) dengan nama bilangannya. Ini adalah proses mengingat fakta dasar tentang sistem bilangan.. Bukti: Bilangan 7 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang fakta dasar berupa nama bilangan yang direpresentasikan oleh simbol angka.. Bukti: Pasangkan lambang bilangan dengan namanya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, yaitu mengenali nama bilangan dari simbol angka yang diberikan. Tidak ada langkah kompleks atau perencanaan yang diperlukan.. Bukti: Bilangan 7 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal simbol angka 1-10 dan nama bilangannya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenali nama bilangan adalah kompetensi dasar kelas 1 yang bersifat hafalan/pengenalan langsung. |

Run 2 — solusi: Lambang bilangan 7 memiliki nama bilangan tujuh.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali simbol angka 7 dan menghubungkannya dengan nama bilangan yang sesuai (tujuh). Ini adalah proses mengingat fakta dasar.. Bukti: Bilangan 7 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol angka dan nama bilangan yang bersesuaian, yang merupakan pengetahuan faktual dasar.. Bukti: Pasangkan lambang bilangan dengan namanya
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pengenalan simbol angka 7. Tidak ada langkah tambahan atau keputusan strategi yang diperlukan.. Bukti: Bilangan 7 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, mengenali nama bilangan dari lambang angka adalah tugas dasar yang sangat familiar. |

Run 3 — solusi: Lambang bilangan 7 memiliki nama bilangan tujuh.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali simbol angka 7 dan menghubungkannya dengan nama bilangan yang sesuai (tujuh). Ini adalah proses mengingat fakta dasar.. Bukti: Bilangan 7 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol angka dan nama bilangan yang merupakan elemen dasar (fakta) dalam matematika.. Bukti: Pasangkan lambang bilangan dengan namanya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1. Tidak ada langkah yang saling bergantung, tidak ada strategi yang perlu dipilih, dan tidak ada kendala yang berinteraksi. Siswa hanya perlu melakukan pemanggilan ingatan langsung.. Bukti: Bilangan 7 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan 1-10 dan nama bilangannya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenal nama bilangan untuk angka tunggal adalah kompetensi dasar kelas 1 yang diajarkan di awal tahun ajaran. |

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
| Domain kognitif | knowing=0.999906; applying=0.000094; reasoning=0.000000 | knowing | 0.999906 | 0.000877 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.773133; conceptual=0.204016; procedural=0.022851; metacognitive=0.000000 | factual | 0.773133 | 0.439714 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.887681; Medium=0.109815; Hard=0.002505 | Easy | 0.887681 | 0.330726 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999906; −Σp ln(p) = 0.000963; H = 0.000963/ln(3) = 0.000877; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.773133; −Σp ln(p) = 0.609573; H = 0.609573/ln(4) = 0.439714; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.887681; −Σp ln(p) = 0.363339; H = 0.363339/ln(3) = 0.330726; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangkan lambang bilangan dengan namanya. Bilangan 7 dibaca ....
Pilihan: A. Tujuh
B. Delapan
C. Enam
D. Sembilan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `aded1ab9ecb9a5ad0e341f2a`

Buah mana yang jumlahnya lebih banyak?

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan |
| B | B (jeruk) |
| C | Sama banyak |
| D | A (mangga) |

![Gambar sumber soal 3](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Hitung jumlah buah di kotak A (4) dan kotak B (6). Karena 6 lebih besar dari 4, maka kotak B memiliki jumlah buah yang lebih banyak.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png. Transkripsi visual: Terdapat dua kotak, A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk. Soal meminta untuk menentukan kotak mana yang memiliki jumlah buah lebih banyak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41eccdd3320517fba1a69ded7b424b10ea004d57f3d4c55e51a8092c8728df74`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3442 |
| 2 | success | valid / verified | applying | procedural | Easy | 4315 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3443 |

Run 1 — solusi: Hitung jumlah buah di kotak A (4) dan kotak B (6). Bandingkan kedua bilangan tersebut: 6 > 4, sehingga kotak B memiliki jumlah lebih banyak.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan prosedur menghitung benda konkret (faktual) dan membandingkan dua bilangan untuk menentukan mana yang lebih besar. Ini adalah penerapan langsung dari konsep perbandingan jumlah yang sudah dipelajari di kelas 1.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan kuantitas (lebih banyak/lebih sedikit) melalui representasi visual benda konkret.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin untuk kelas 1. Siswa hanya perlu menghitung dua kelompok benda yang terpisah dan membandingkan hasilnya. Tidak ada langkah perencanaan yang kompleks atau kendala yang saling berinteraksi.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung dan membandingkan dua kelompok benda adalah standar kompetensi dasar kelas 1 SD. Soal memberikan representasi visual yang jelas tanpa distraksi tambahan. |

Run 2 — solusi: Hitung jumlah buah di kotak A (4) dan kotak B (6). Karena 6 > 4, maka kotak B memiliki jumlah buah lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu melakukan prosedur menghitung jumlah benda di masing-masing kelompok dan membandingkan hasilnya.. Bukti: Buah mana yang jumlahnya lebih banyak?
- Dimensi pengetahuan `classify/procedural`: Tugas ini melibatkan penerapan prosedur menghitung dan membandingkan kuantitas.. Bukti: Buah mana yang jumlahnya lebih banyak?
- Intended difficulty `classify/Easy`: Tugas ini adalah latihan rutin menghitung dan membandingkan dua kelompok benda kecil yang merupakan materi dasar kelas 1.. Bukti: Buah mana yang jumlahnya lebih banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda sampai 10. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep membandingkan banyak benda yang sangat umum dan mendasar untuk siswa kelas 1. |

Run 3 — solusi: Hitung jumlah mangga di kotak A (4) dan jumlah jeruk di kotak B (6). Bandingkan kedua bilangan tersebut: 6 > 4. Jadi, kotak B memiliki jumlah buah lebih banyak.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan prosedur menghitung benda konkret (enumerasi) dan membandingkan dua bilangan cacah sederhana untuk menentukan mana yang lebih besar. Ini adalah penerapan langsung dari konsep perbandingan jumlah yang sudah dipelajari di kelas 1.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan kuantitas (lebih banyak/lebih sedikit) melalui representasi visual benda konkret.. Bukti: Buah mana yang jumlahnya lebih banyak?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan dua langkah rutin: menghitung jumlah benda di masing-masing kelompok dan membandingkan dua bilangan cacah kecil (4 dan 6). Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret sampai 10 dan membandingkan dua bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan tugas menghitung dan membandingkan jumlah benda konkret dalam kelompok kecil. Soal ini adalah latihan standar yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4833`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu melakukan prosedur menghitung benda konkret (enumerasi) dan menerapkan konsep perbandingan bilangan untuk menentukan mana yang lebih besar. Ini adalah penerapan langsung dari konsep perbandingan jumlah yang sudah dipelajari di kelas 1.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan kuantitas (lebih banyak/lebih sedikit) melalui representasi visual benda konkret.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya memerlukan dua langkah rutin: menghitung jumlah benda di masing-masing kelompok dan membandingkan dua bilangan cacah kecil (4 dan 6). Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret sampai 10 dan membandingkan dua bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan tugas menghitung dan membandingkan jumlah benda konkret dalam kelompok kecil. Soal ini adalah latihan standar yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 97/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000478; applying=0.999522; reasoning=0.000000 | applying | 0.999522 | 0.003764 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.028899; conceptual=0.966488; procedural=0.004613; metacognitive=0.000000 | conceptual | 0.966488 | 0.115541 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.802553; Medium=0.194264; Hard=0.003183 | Easy | 0.802553 | 0.467080 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999522; −Σp ln(p) = 0.004135; H = 0.004135/ln(3) = 0.003764; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.966488; −Σp ln(p) = 0.160173; H = 0.160173/ln(4) = 0.115541; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.802553; −Σp ln(p) = 0.513139; H = 0.513139/ln(3) = 0.467080; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Banyak Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Buah mana yang jumlahnya lebih banyak?
Pilihan: A. Tidak dapat ditentukan
B. B (jeruk)
C. Sama banyak
D. A (mangga)
Transkripsi visual: Terdapat dua kotak, A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk. Soal meminta untuk menentukan kotak mana yang memiliki jumlah buah lebih banyak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `71dcf3a05499a6d3e660d279`

Buah mana yang jumlahnya lebih sedikit?

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan |
| B | A (mangga) |
| C | Sama banyak |
| D | B (jeruk) |

![Gambar sumber soal 4](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Hitung jumlah mangga di kotak A (4) dan jumlah jeruk di kotak B (6). Bandingkan kedua bilangan tersebut: 4 < 6. Jadi, buah yang jumlahnya lebih sedikit adalah mangga (kotak A).
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png. Transkripsi visual: Terdapat dua kotak berlabel A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk. Pertanyaan meminta untuk menentukan buah mana yang jumlahnya lebih sedikit.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3539ff0908dba36f09d0172916e502332c6018d4a772d2ec9d4437b7f34541b4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3391 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3398 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3412 |

Run 1 — solusi: Hitung jumlah mangga di kotak A (4) dan jumlah jeruk di kotak B (6). Bandingkan kedua bilangan tersebut: 4 < 6. Jadi, buah yang jumlahnya lebih sedikit adalah mangga (kotak A).
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan prosedur menghitung benda konkret (mangga dan jeruk) dan membandingkan dua bilangan cacah untuk menentukan mana yang lebih kecil. Ini adalah prosedur rutin yang langsung.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep perbandingan jumlah (lebih sedikit) melalui representasi visual benda konkret.. Bukti: Buah mana yang jumlahnya lebih sedikit?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 1. Siswa hanya perlu menghitung dua kelompok benda dan membandingkan hasilnya.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda sampai 10 dan membandingkan dua bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membandingkan dua kelompok benda kecil adalah materi dasar kelas 1 yang rutin dan tidak memerlukan perencanaan kompleks. |

Run 2 — solusi: Hitung jumlah buah di kotak A (4) dan kotak B (6). Bandingkan kedua bilangan tersebut. Karena 4 < 6, maka kotak A (mangga) memiliki jumlah yang lebih sedikit.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan penghitungan dasar (membilang) pada dua kelompok benda, lalu membandingkan hasilnya untuk menentukan mana yang lebih sedikit. Ini adalah prosedur rutin yang langsung.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep perbandingan kuantitas (lebih sedikit) melalui prosedur membilang benda konkret.. Bukti: Buah mana yang jumlahnya lebih sedikit?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1. Siswa hanya perlu membilang dua kelompok kecil benda (4 dan 6) dan membandingkannya. Tidak ada langkah rumit atau kendala yang berinteraksi.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan memahami konsep perbandingan 'lebih sedikit'/'lebih banyak'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membilang dan membandingkan dua kelompok benda kecil adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

Run 3 — solusi: Hitung jumlah buah di kotak A (4) dan kotak B (6). Bandingkan kedua bilangan tersebut: 4 < 6. Jadi, buah di kotak A (mangga) lebih sedikit.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan prosedur menghitung benda konkret dan membandingkan dua bilangan untuk menentukan mana yang lebih kecil. Ini adalah penerapan langsung dari konsep perbandingan bilangan yang familiar bagi siswa kelas 1.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan jumlah (lebih sedikit) melalui representasi visual benda konkret.. Bukti: Buah mana yang jumlahnya lebih sedikit?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan penghitungan langsung pada dua kelompok benda yang sudah terpisah jelas dan membandingkan hasilnya. Tidak ada langkah tersembunyi atau kendala yang kompleks.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan tugas membandingkan jumlah benda konkret dalam kelompok kecil (di bawah 10). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 96/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000584; applying=0.999416; reasoning=0.000000 | applying | 0.999416 | 0.004488 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.030546; conceptual=0.966445; procedural=0.003009; metacognitive=0.000000 | conceptual | 0.966445 | 0.113263 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.823862; Medium=0.172925; Hard=0.003213 | Easy | 0.823862 | 0.438310 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999416; −Σp ln(p) = 0.004930; H = 0.004930/ln(3) = 0.004488; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.966445; −Σp ln(p) = 0.157016; H = 0.157016/ln(4) = 0.113263; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.823862; −Σp ln(p) = 0.481533; H = 0.481533/ln(3) = 0.438310; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Banyak Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Buah mana yang jumlahnya lebih sedikit?
Pilihan: A. Tidak dapat ditentukan
B. A (mangga)
C. Sama banyak
D. B (jeruk)
Transkripsi visual: Terdapat dua kotak berlabel A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk. Pertanyaan meminta untuk menentukan buah mana yang jumlahnya lebih sedikit.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `a035dee2caefafa52096496e`

Lengkapi urutan bilangan berikut: 1, 2, ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 1 |
| C | 0 |
| D | 4 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Urutan bilangan 1, 2 menunjukkan pola menghitung maju dengan selisih 1. Bilangan setelah 2 adalah 2 + 1 = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `03152cc45d4a60e4ea094714a99e4e63892e2a5f3b723b41c7d7b13cee1b8192`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2040 |
| 2 | success | valid / verified | knowing | factual | Easy | 2053 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2616 |

Run 1 — solusi: Urutan bilangan 1, 2 menunjukkan pola penambahan 1 (menghitung maju). Bilangan setelah 2 adalah 2 + 1 = 3.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali pola urutan bilangan sederhana dan melanjutkan urutan tersebut dengan prosedur yang sangat langsung.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan sebagai elemen dasar dalam matematika.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1. Pola urutan 1, 2 sangat familiar dan tidak memerlukan perencanaan atau integrasi langkah yang kompleks.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, mengenali urutan bilangan 1, 2, 3 adalah kompetensi dasar yang sangat rutin dan tidak menuntut kognitif tinggi. |

Run 2 — solusi: Urutan bilangan 1, 2 menunjukkan pola penambahan 1. Bilangan setelah 2 adalah 2 + 1 = 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan asli yang sederhana (menghitung maju satu-satu) dan menerapkan prosedur dasar tersebut untuk menentukan bilangan berikutnya.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang urutan bilangan asli yang sudah dipelajari di kelas 1.. Bukti: 1, 2, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 1. Pola urutan 1, 2 adalah urutan bilangan yang paling awal dipelajari. Tidak ada langkah yang saling bergantung atau kendala yang harus dipecahkan.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan 1 sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan urutan bilangan 1, 2, 3 sebagai bagian dari pengenalan angka dasar. |

Run 3 — solusi: Urutan bilangan 1, 2 menunjukkan pola penambahan 1. Bilangan setelah 2 adalah 2 + 1 = 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan melanjutkan urutan bilangan yang sangat dasar (menghitung maju 1-1), yang merupakan prosedur langsung.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Dimensi pengetahuan `classify/procedural`: Tugas ini melibatkan penerapan algoritma atau urutan berhitung dasar yang sudah dipelajari.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengenalan pola urutan bilangan yang paling dasar bagi siswa kelas 1.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung maju 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini merupakan latihan dasar menghitung maju yang sangat familiar bagi siswa kelas 1. Tidak ada kendala atau langkah tambahan yang diperlukan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3432`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali pola urutan bilangan asli yang sangat dasar dan melanjutkan urutan tersebut dengan prosedur yang langsung.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual tentang urutan bilangan asli yang merupakan elemen dasar dalam matematika.
- Intended difficulty `Easy`: Soal ini sangat mendasar bagi siswa kelas 1. Pola urutan 1, 2 adalah urutan bilangan yang paling awal dipelajari. Tidak ada langkah yang saling bergantung atau kendala yang harus dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, mengenali urutan bilangan 1, 2, 3 adalah kompetensi dasar yang sangat rutin dan tidak menuntut kognitif tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=1.000000; applying=0.000000; reasoning=0.000000 | knowing | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.878503; conceptual=0.105707; procedural=0.015790; metacognitive=0.000000 | factual | 0.878503 | 0.300681 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.909591; Medium=0.088220; Hard=0.002189 | Easy | 0.909591 | 0.285623 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.878503; −Σp ln(p) = 0.416832; H = 0.416832/ln(4) = 0.300681; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.909591; −Σp ln(p) = 0.313788; H = 0.313788/ln(3) = 0.285623; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi urutan bilangan berikut: 1, 2, ....
Pilihan: A. 3
B. 1
C. 0
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `593cbed3be61dd6c967e770c`

Lengkapi urutan bilangan berikut: 4, 5, ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 4 |
| C | 6 |
| D | 7 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Urutan bilangan 4, 5 menunjukkan pola penambahan 1. Bilangan setelah 5 adalah 5 + 1 = 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `847c154ec9de5d258e085710c84f1baa5baa42933c7f08a5eb089c8d26025d55`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2030 |
| 2 | success | valid / verified | knowing | factual | Easy | 2027 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2059 |

Run 1 — solusi: Urutan bilangan 4, 5 menunjukkan pola penambahan 1. Bilangan setelah 5 adalah 5 + 1 = 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan bulat yang sederhana (menghitung maju satu-satu) dan menerapkan prosedur dasar untuk menentukan bilangan berikutnya.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar matematika) yang merupakan elemen dasar dalam berhitung.. Bukti: 4, 5, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1. Pola urutan 4, 5 sangat familiar dan tidak memerlukan perencanaan atau integrasi langkah yang kompleks.. Bukti: 4, 5, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, mengenali urutan bilangan maju satu-satu adalah keterampilan dasar yang rutin dan langsung. |

Run 2 — solusi: Urutan bilangan 4, 5 menunjukkan pola penambahan 1. Bilangan setelah 5 adalah 5 + 1 = 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan cacah yang sederhana dan melanjutkan urutan tersebut dengan satu langkah penambahan yang sangat langsung.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan sebagai pengetahuan faktual dasar dalam matematika kelas 1.. Bukti: 4, 5, ....
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengenalan urutan bilangan cacah dasar. Tidak ada keputusan strategi atau kendala yang kompleks.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan urutan bilangan maju. Soal ini adalah latihan rutin yang sangat dasar. |

Run 3 — solusi: Urutan bilangan 4, 5 menunjukkan pola penambahan 1. Bilangan setelah 5 adalah 5 + 1 = 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan cacah yang sederhana (menghitung maju satu-satu) dan menerapkan prosedur tersebut untuk menentukan bilangan berikutnya.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang urutan bilangan sebagai konsep dasar dalam matematika.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1. Pola urutan bilangan 4, 5 adalah pola yang sangat familiar dan rutin. Tidak ada keputusan strategi yang kompleks atau kendala yang berinteraksi.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, mengenali urutan bilangan 4, 5 adalah tugas rutin yang sangat mendasar dan tidak memerlukan perencanaan atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3359`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali pola urutan bilangan bulat yang sederhana (menghitung maju satu-satu) dan menerapkan prosedur dasar untuk menentukan bilangan berikutnya.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar matematika) yang merupakan elemen dasar dalam berhitung.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 1. Pola urutan 4, 5 sangat familiar dan tidak memerlukan perencanaan atau integrasi langkah yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, mengenali urutan bilangan maju satu-satu adalah keterampilan dasar yang rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=1.000000; applying=0.000000; reasoning=0.000000 | knowing | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.901465; conceptual=0.086746; procedural=0.011789; metacognitive=0.000000 | factual | 0.901465 | 0.258196 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.915153; Medium=0.082765; Hard=0.002083 | Easy | 0.915153 | 0.273280 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.901465; −Σp ln(p) = 0.357936; H = 0.357936/ln(4) = 0.258196; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.915153; −Σp ln(p) = 0.300228; H = 0.300228/ln(3) = 0.273280; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi urutan bilangan berikut: 4, 5, ....
Pilihan: A. 3
B. 4
C. 6
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `82267daa87c52ac8b3876098`

Temukan pasangan bilangan berikut.<br><br>Temukan pasangan bilangan berikut. Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?

| Opsi | Isi |
|---|---|
| A | 5 dan 3 |
| B | 4 dan 4 |
| C | 3 dan 6 |
| D | 4 dan 5 |

![Gambar sumber soal 7](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0043-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah jeruk (4) dan jumlah salak (5). Total 4 + 5 = 9. Pasangan bilangan untuk 9 adalah 4 dan 5.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0043-04.png. Transkripsi visual: Terdapat dua kotak berisi buah. Kotak pertama berisi 4 buah jeruk. Kotak kedua berisi 5 buah salak. Di bawahnya terdapat diagram pasangan bilangan (number bond) dengan angka 9 di lingkaran utama, yang bercabang ke dua lingkaran kosong.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `30722cf7ba6502c59ad8ba3b58d0d90fabff0ada257af0481b0b1f5ede0f7a7b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3434 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3422 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3427 |

Run 1 — solusi: Menghitung jumlah jeruk (4) dan jumlah salak (5). Total 4 + 5 = 9. Pasangan bilangan 9 adalah 4 dan 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi pasangan bilangan yang membentuk 9 berdasarkan representasi visual (menghitung objek). Ini adalah prosedur langsung yang melibatkan pengenalan jumlah objek dan menghubungkannya dengan konsep pasangan bilangan (number bonds) yang umum di kelas 1.. Bukti: Temukan pasangan bilangan berikut.; Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?; 4 buah jeruk; 5 buah salak
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang dekomposisi bilangan (pasangan bilangan) melalui representasi konkret (gambar buah).. Bukti: pasangan bilangan; 4 buah jeruk; 5 buah salak
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 1 karena hanya memerlukan penghitungan langsung objek yang sudah dikelompokkan secara visual dan mencocokkannya dengan pilihan jawaban yang tersedia.. Bukti: Temukan pasangan bilangan berikut.; 4 buah jeruk; 5 buah salak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas menghitung objek dan menentukan pasangan bilangan adalah materi standar kelas 1. Tidak ada langkah perencanaan kompleks atau kendala yang saling berinteraksi. |

Run 2 — solusi: Menghitung jumlah jeruk (4) dan jumlah salak (5). Total 4 + 5 = 9. Pasangan bilangan untuk 9 adalah 4 dan 5.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pasangan bilangan yang membentuk 9 berdasarkan representasi visual (gambar buah). Ini adalah tugas mengenali dan menerapkan konsep pasangan bilangan (number bonds) yang sudah familiar di kelas 1.. Bukti: Temukan pasangan bilangan berikut.; Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?; 4 jeruk dan 5 buah lainnya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang komposisi bilangan (bahwa 9 dapat dipecah menjadi 4 dan 5) melalui representasi visual.. Bukti: Temukan pasangan bilangan berikut.; Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menghitung jumlah objek di setiap kelompok dan mencocokkannya dengan pilihan jawaban. Tidak ada langkah perencanaan yang kompleks atau kendala yang saling berinteraksi.. Bukti: Temukan pasangan bilangan berikut.; 4 jeruk dan 5 buah lainnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek hingga 10 dan konsep dasar penjumlahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, menghitung objek konkret dan mencocokkannya dengan angka adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Menghitung jumlah jeruk (4) dan jumlah salak (5). Total 4 + 5 = 9. Pasangan bilangan untuk 9 adalah 4 dan 5.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pasangan bilangan yang membentuk 9 berdasarkan representasi visual (gambar buah). Ini adalah tugas mengenali dan menerapkan konsep pasangan bilangan dasar yang sudah familiar bagi siswa kelas 1.. Bukti: Temukan pasangan bilangan berikut.; Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?; 4 buah jeruk; 5 buah salak
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang komposisi bilangan (bahwa 9 dapat dipecah menjadi 4 dan 5) melalui representasi visual.. Bukti: pasangan bilangan; 4 buah jeruk; 5 buah salak
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung objek pada dua kelompok yang sudah disediakan dan mencocokkannya dengan total 9. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Temukan pasangan bilangan berikut.; Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10 dan pemahaman dasar tentang komposisi bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, menghitung objek konkret dan menentukan pasangan bilangan adalah aktivitas rutin yang sesuai dengan kurikulum dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4881`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk mengidentifikasi pasangan bilangan yang membentuk 9 berdasarkan representasi visual (menghitung objek). Ini adalah prosedur langsung yang melibatkan pengenalan jumlah objek dan menghubungkannya dengan konsep pasangan bilangan (number bonds) yang umum di kelas 1.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang dekomposisi bilangan (bahwa 9 dapat dipecah menjadi 4 dan 5) melalui representasi konkret (gambar buah).
- Intended difficulty `Easy`: Soal ini sangat mudah bagi siswa kelas 1 karena hanya memerlukan penghitungan langsung objek yang sudah dikelompokkan secara visual dan mencocokkannya dengan pilihan jawaban yang tersedia.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas menghitung objek dan menentukan pasangan bilangan adalah materi standar kelas 1. Tidak ada langkah perencanaan kompleks atau kendala yang saling berinteraksi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 117/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.002897; applying=0.997103; reasoning=0.000000 | applying | 0.997103 | 0.018045 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.070311; conceptual=0.923212; procedural=0.006477; metacognitive=0.000000 | conceptual | 0.923212 | 0.211403 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.837796; Medium=0.158632; Hard=0.003572 | Easy | 0.837796 | 0.419136 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997103; −Σp ln(p) = 0.019824; H = 0.019824/ln(3) = 0.018045; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.923212; −Σp ln(p) = 0.293066; H = 0.293066/ln(4) = 0.211403; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.837796; −Σp ln(p) = 0.460468; H = 0.460468/ln(3) = 0.419136; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pasangan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan pasangan bilangan berikut.

Temukan pasangan bilangan berikut. Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?
Pilihan: A. 5 dan 3
B. 4 dan 4
C. 3 dan 6
D. 4 dan 5
Transkripsi visual: Terdapat dua kotak berisi buah. Kotak pertama berisi 4 buah jeruk. Kotak kedua berisi 5 buah salak. Di bawahnya terdapat diagram pasangan bilangan (number bond) dengan angka 9 di lingkaran utama, yang bercabang ke dua lingkaran kosong.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `ddae4518c6926e380356e576`

Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 2 |
| C | 4 |
| D | 1 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Diketahui jumlah dua bilangan adalah 6. Jika salah satu bilangan adalah 4, maka bilangan pasangannya adalah 6 - 4 = 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0f132fb8326c8c8453b9ab54680066716c9b1d65e0488f8571e6071066b9d218`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2214 |
| 2 | success | valid / verified | applying | procedural | Easy | 2210 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2232 |

Run 1 — solusi: Diketahui jumlah dua bilangan adalah 6. Jika salah satu bilangan adalah 4, maka bilangan pasangannya adalah 6 - 4 = 2.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman tentang pasangan bilangan (komposisi bilangan) untuk menemukan nilai yang hilang dalam operasi penjumlahan sederhana (4 + x = 6). Ini adalah penerapan konsep dasar pada konteks rutin.. Bukti: Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai hubungan antara bilangan-bilangan yang membentuk jumlah tertentu (konsep pasangan bilangan).. Bukti: Pasangkan dua bilangan yang jumlahnya 6
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah bagi siswa kelas 1 karena hanya melibatkan satu operasi pengurangan dasar (6 - 4) atau pemahaman pasangan bilangan 6 yang sudah umum dipelajari. Jalur penyelesaiannya sangat langsung tanpa memerlukan perencanaan kompleks.. Bukti: Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan dasar sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan pasangan bilangan (number bonds) sebagai bagian dari kurikulum dasar, sehingga soal ini merupakan latihan rutin. |

Run 2 — solusi: Siswa perlu mencari bilangan x sehingga 4 + x = 6. Dengan menghitung selisih 6 - 4 = 2, maka pasangannya adalah 2.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep penjumlahan dasar untuk melengkapi pasangan bilangan yang berjumlah 6. Ini adalah penerapan prosedur penjumlahan yang sudah dipelajari di kelas 1.. Bukti: Pasangkan dua bilangan yang jumlahnya 6; Bilangan berapa yang berpasangan dengan 4?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi penjumlahan dasar untuk mencapai target jumlah tertentu (pasangan bilangan).. Bukti: jumlahnya 6; berpasangan dengan 4
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan satu operasi penjumlahan/pengurangan dasar dengan angka kecil (di bawah 10). Jalur penyelesaian sangat langsung dan familiar bagi siswa kelas 1.. Bukti: jumlahnya 6; berpasangan dengan 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pasangan bilangan sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, mencari pasangan bilangan yang berjumlah 6 adalah latihan rutin yang sesuai dengan kurikulum dasar. |

Run 3 — solusi: Diketahui jumlah dua bilangan adalah 6. Jika salah satu bilangan adalah 4, maka bilangan pasangannya adalah 6 - 4 = 2.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pasangan bilangan (number bonds) untuk mencari nilai yang hilang agar jumlahnya menjadi 6. Ini adalah penerapan konsep dasar pada konteks rutin.. Bukti: Pasangkan dua bilangan yang jumlahnya 6; Bilangan berapa yang berpasangan dengan 4?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar bilangan (komposisi bilangan 6) yang merupakan bagian dari struktur konsep dasar matematika kelas 1.. Bukti: jumlahnya 6; berpasangan dengan 4
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan satu operasi pengurangan dasar (6-4) atau pemahaman pasangan bilangan 6 yang sudah familiar bagi siswa kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan strategi kompleks.. Bukti: Pasangkan dua bilangan yang jumlahnya 6; Bilangan berapa yang berpasangan dengan 4?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar sampai 10 dan pasangan bilangan (number bonds). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 diharapkan sudah mengenal pasangan bilangan 6 (seperti 3+3, 4+2, 5+1). Soal ini adalah latihan rutin yang sesuai dengan tingkat perkembangan kognitif kelas 1. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3617`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep pasangan bilangan (number bonds) untuk mencari nilai yang hilang agar jumlahnya menjadi 6. Ini adalah penerapan konsep dasar pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar bilangan (komposisi bilangan 6) yang merupakan bagian dari struktur konsep dasar matematika kelas 1.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya melibatkan satu operasi pengurangan dasar (6-4) atau pemahaman pasangan bilangan 6 yang sudah familiar bagi siswa kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan strategi kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar sampai 10 dan pasangan bilangan (number bonds). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 diharapkan sudah mengenal pasangan bilangan 6 (seperti 3+3, 4+2, 5+1). Soal ini adalah latihan rutin yang sesuai dengan tingkat perkembangan kognitif kelas 1. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999928; applying=0.000072; reasoning=0.000000 | knowing | 0.999928 | 0.000695 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.741863; conceptual=0.228809; procedural=0.029328; metacognitive=0.000000 | factual | 0.741863 | 0.477880 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.882585; Medium=0.115501; Hard=0.001913 | Easy | 0.882585 | 0.338169 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999928; −Σp ln(p) = 0.000763; H = 0.000763/ln(3) = 0.000695; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.741863; −Σp ln(p) = 0.662482; H = 0.662482/ln(4) = 0.477880; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.882585; −Σp ln(p) = 0.371516; H = 0.371516/ln(3) = 0.338169; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pasangan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?
Pilihan: A. 3
B. 2
C. 4
D. 1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `ef1c6489a0d0caf13ccb067e`

Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.

| Opsi | Isi |
|---|---|
| A | 4 mobil kuning, 5 mobil merah, semuanya 9 mobil |
| B | 4 mobil kuning, 4 mobil merah, semuanya 9 mobil |
| C | 4 mobil kuning, 4 mobil merah, semuanya 8 mobil |
| D | 5 mobil kuning, 4 mobil merah, semuanya 9 mobil |

![Gambar sumber soal 9](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0058-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menghitung mobil kuning (4), menghitung mobil merah (4), lalu menjumlahkan keduanya (4 + 4 = 8).
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0058-03.png. Transkripsi visual: Terdapat dua kotak. Kotak kiri berisi 4 mobil berwarna kuning. Kotak kanan berisi 4 mobil berwarna merah. Terdapat teks rumpang untuk mengisi jumlah mobil kuning, jumlah mobil merah, dan jumlah total mobil.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c9fa39e9469c6004f647cb1ef4020048d46d5cc3e433bdf7a7074dd482f9f712`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3395 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3406 |
| 3 | success | valid / verified | knowing | factual | Easy | 3418 |

Run 1 — solusi: Menghitung jumlah mobil kuning (4) dan mobil merah (4), kemudian menjumlahkan keduanya (4 + 4 = 8).
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan penghitungan langsung dari representasi visual (menghitung objek) dan melakukan operasi penjumlahan dasar yang sangat rutin.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang penghitungan objek dan prosedur penjumlahan dasar.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menghitung jumlah objek di setiap kelompok dan menjumlahkannya. Tidak ada langkah tersembunyi atau kompleksitas perencanaan.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan konsep penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan penghitungan objek konkret dan penjumlahan dasar satu digit yang merupakan materi standar awal. |

Run 2 — solusi: Menghitung jumlah mobil kuning (4), menghitung jumlah mobil merah (4), lalu menjumlahkan keduanya (4 + 4 = 8).
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan penghitungan langsung dari objek visual (menghitung benda) dan melakukan operasi penjumlahan dasar. Ini adalah prosedur yang sangat langsung dan rutin bagi siswa kelas 1.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep penjumlahan dasar sebagai penggabungan dua kelompok benda (fakta/konsep dasar) dan prosedur menghitung benda.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu menghitung benda yang terlihat secara eksplisit dan melakukan penjumlahan dasar. Tidak ada langkah yang kompleks atau strategi yang perlu dipilih.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda sampai 10 dan konsep penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, menghitung benda konkret dan menjumlahkannya adalah tugas dasar yang sangat familiar dan tidak menuntut perencanaan tinggi. |

Run 3 — solusi: Menghitung jumlah mobil kuning (4), menghitung jumlah mobil merah (4), lalu menjumlahkan keduanya (4 + 4 = 8).
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan penghitungan langsung dari representasi visual (menghitung objek) dan melakukan operasi penjumlahan dasar yang sudah familiar. Ini adalah prosedur langsung.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang kuantitas objek yang terlihat dan prosedur penjumlahan dasar.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menghitung objek yang terlihat dan menjumlahkannya. Tidak ada langkah tersembunyi atau perencanaan kompleks.. Bukti: Ada .... mobil berwarna kuning.; Ada .... mobil berwarna merah.; Semuanya ada .... mobil.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (1-10) dan penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, menghitung objek konkret dan menjumlahkan dua bilangan kecil adalah tugas rutin yang sesuai dengan tingkat perkembangan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5693`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan penghitungan langsung dari representasi visual dan melakukan operasi penjumlahan dasar yang sangat rutin.
- Dimensi pengetahuan `factual`: Soal menguji kemampuan dasar dalam menghitung objek konkret dan fakta penjumlahan dasar.
- Intended difficulty `Easy`: Soal ini sangat langsung, melibatkan penghitungan objek konkret dan penjumlahan dasar yang familiar bagi siswa kelas 1. Tidak ada langkah perencanaan yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan konsep penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan penghitungan objek konkret dan penjumlahan dasar satu digit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 150/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006817; applying=0.993183; reasoning=0.000000 | applying | 0.993183 | 0.037139 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.035097; conceptual=0.960185; procedural=0.004717; metacognitive=0.000000 | conceptual | 0.960185 | 0.131172 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.704648; Medium=0.288035; Hard=0.007317 | Easy | 0.704648 | 0.583607 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993183; −Σp ln(p) = 0.040802; H = 0.040802/ln(3) = 0.037139; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.960185; −Σp ln(p) = 0.181843; H = 0.181843/ln(4) = 0.131172; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.704648; −Σp ln(p) = 0.641158; H = 0.641158/ln(3) = 0.583607; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
Pilihan: A. 4 mobil kuning, 5 mobil merah, semuanya 9 mobil
B. 4 mobil kuning, 4 mobil merah, semuanya 9 mobil
C. 4 mobil kuning, 4 mobil merah, semuanya 8 mobil
D. 5 mobil kuning, 4 mobil merah, semuanya 9 mobil
Transkripsi visual: Terdapat dua kotak. Kotak kiri berisi 4 mobil berwarna kuning. Kotak kanan berisi 4 mobil berwarna merah. Terdapat teks rumpang untuk mengisi jumlah mobil kuning, jumlah mobil merah, dan jumlah total mobil.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `f00f8cf40ab22284c6d216e4`

Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain. Mereka bermain bergantian.<br><br>Berapa jumlah anak sekarang?

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 6 |
| C | 8 |
| D | 4 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 4 anak + 2 anak = 6 anak.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2de61ff2c3db69ada392603d136cab28bccc5aad74e5e7d04ca777d12684d942`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2920 |
| 2 | success | valid / verified | applying | procedural | Easy | 2615 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2203 |

Run 1 — solusi: 4 anak awal + 2 anak yang datang = 6 anak.
- Domain kognitif `classify/applying`: Siswa menerapkan operasi penjumlahan dasar pada konteks cerita rutin.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur penjumlahan dasar untuk menyelesaikan masalah.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.
- Intended difficulty `classify/Easy`: Masalah penjumlahan satu langkah yang sangat standar untuk kelas 1 tanpa kendala tambahan.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah soal cerita penjumlahan satu langkah yang merupakan standar kompetensi kelas 1. |

Run 2 — solusi: 4 anak awal + 2 anak yang datang = 6 anak.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi penjumlahan dasar pada konteks cerita sederhana untuk menentukan total anak.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.; Berapa jumlah anak sekarang?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur penjumlahan dasar untuk menyelesaikan masalah.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.
- Intended difficulty `classify/Easy`: Soal ini merupakan soal penjumlahan satu langkah yang sangat standar dan familiar bagi siswa kelas 1. Tidak ada kendala yang saling berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.; Berapa jumlah anak sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah soal penjumlahan satu langkah yang sangat standar untuk kelas 1. Tidak ada kendala yang saling berinteraksi atau kebutuhan perencanaan yang kompleks. |

Run 3 — solusi: 4 anak + 2 anak = 6 anak.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan operasi penjumlahan dasar pada konteks cerita rutin yang melibatkan penambahan objek (anak). Ini adalah penerapan langsung konsep penjumlahan.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.; Berapa jumlah anak sekarang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan penjumlahan (konsep dasar penambahan objek) dalam situasi sehari-hari.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.
- Intended difficulty `classify/Easy`: Soal ini merupakan soal penjumlahan satu langkah yang sangat standar untuk kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.; Berapa jumlah anak sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menghitung sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah contoh klasik penjumlahan satu langkah yang sesuai dengan kurikulum kelas 1. Tidak ada kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3390`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan operasi penjumlahan dasar pada konteks cerita rutin. Meskipun ada kalimat tambahan 'Mereka bermain bergantian', ini tidak mengubah prosedur penjumlahan yang diperlukan.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritme penjumlahan dasar untuk menyelesaikan masalah.
- Intended difficulty `Easy`: Soal ini adalah penjumlahan satu langkah yang sangat standar untuk kelas 1. Kalimat 'Mereka bermain bergantian' adalah informasi tambahan yang tidak relevan, namun tidak menambah kompleksitas perencanaan atau kendala yang berinteraksi secara signifikan bagi siswa kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita penjumlahan satu langkah adalah standar kompetensi kelas 1. Informasi tambahan tidak mengubah tingkat kesulitan menjadi Medium. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.841757; applying=0.158243; reasoning=0.000000 | knowing | 0.841757 | 0.397542 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.539800; conceptual=0.449691; procedural=0.010510; metacognitive=0.000000 | factual | 0.539800 | 0.533858 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.856081; Medium=0.141014; Hard=0.002905 | Easy | 0.856081 | 0.387969 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.841757; −Σp ln(p) = 0.436745; H = 0.436745/ln(3) = 0.397542; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.539800; −Σp ln(p) = 0.740084; H = 0.740084/ln(4) = 0.533858; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.856081; −Σp ln(p) = 0.426227; H = 0.426227/ln(3) = 0.387969; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain. Mereka bermain bergantian.

Berapa jumlah anak sekarang?
Pilihan: A. 2
B. 6
C. 8
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `bfe710d81f98780c622d6066`

2 + 4 = ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | 5 |
| C | 6 |
| D | 7 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 2 + 4 = 6
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6163722c5e529b6a3c4c251554dc60d794a5eb7805b80c9a6059319063dc05b5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2122 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2580 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2697 |

Run 1 — solusi: 2 + 4 = 6
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi penjumlahan dasar yang sudah dipelajari di kelas 1. Siswa hanya perlu menjalankan prosedur penjumlahan langsung tanpa perlu memilih strategi atau melakukan penalaran kompleks.. Bukti: 2 + 4 = ....
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman terhadap fakta dasar penjumlahan (kombinasi bilangan) yang merupakan elemen dasar dalam aritmatika.. Bukti: 2 + 4 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1. Tidak ada keputusan strategi atau kendala yang perlu diintegrasikan.. Bukti: 2 + 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 2+4 adalah materi standar kelas 1 yang bersifat prosedural langsung tanpa tuntutan kognitif tambahan. |

Run 2 — solusi: 2 + 4 = 6
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar satu langkah yang sudah familiar bagi kelas 1.. Bukti: 2 + 4 = ....
- Dimensi pengetahuan `classify/procedural`: Soal menguji prosedur penjumlahan dasar yang merupakan elemen prosedural standar.. Bukti: 2 + 4 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan satu langkah yang sangat langsung dan familiar bagi siswa kelas 1 tanpa memerlukan strategi tambahan atau perencanaan kompleks.. Bukti: 2 + 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta dasar penjumlahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan satu digit adalah materi dasar kelas 1 yang diajarkan secara rutin. |

Run 3 — solusi: 2 + 4 = 6
- Domain kognitif `classify/knowing`: Soal meminta perhitungan penjumlahan dasar satu digit yang merupakan prosedur langsung dan rutin bagi siswa kelas 1.. Bukti: 2 + 4 = ....
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur penjumlahan dasar yang sudah dipelajari.. Bukti: 2 + 4 = ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan dasar yang sangat familiar bagi siswa kelas 1 tanpa memerlukan perencanaan atau strategi kompleks.. Bukti: 2 + 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan membilang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan satu digit adalah materi dasar kelas 1 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3194`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dasar satu digit. Ini adalah prosedur langsung yang sudah dipelajari dan dilatih secara rutin di kelas 1, sehingga masuk dalam domain knowing.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau prosedur penjumlahan dasar yang merupakan keterampilan prosedural standar bagi siswa kelas 1.
- Intended difficulty `Easy`: Soal ini adalah operasi penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1. Tidak ada keputusan strategi, kendala yang berinteraksi, atau kebutuhan untuk perencanaan kompleks. Jalur penyelesaiannya langsung dan rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan membilang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan satu digit adalah materi dasar kelas 1 yang bersifat rutin dan langsung tanpa tuntutan kognitif tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 56/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999843; applying=0.000157; reasoning=0.000000 | knowing | 0.999843 | 0.001397 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.903190; conceptual=0.068881; procedural=0.027928; metacognitive=0.000000 | factual | 0.903190 | 0.271356 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.911800; Medium=0.086037; Hard=0.002163 | Easy | 0.911800 | 0.280817 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999843; −Σp ln(p) = 0.001535; H = 0.001535/ln(3) = 0.001397; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.903190; −Σp ln(p) = 0.376179; H = 0.376179/ln(4) = 0.271356; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.911800; −Σp ln(p) = 0.308509; H = 0.308509/ln(3) = 0.280817; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: 2 + 4 = ....
Pilihan: A. 4
B. 5
C. 6
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `f9582859a11afb87b07d7da8`

1 + 1 = ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 1 |
| C | 11 |
| D | 2 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 1 + 1 = 2
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a1dcc411d94c79b1428719ee9c349533c0529ede7562d249b3ec679fb6c7e992`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2527 |
| 2 | success | valid / verified | knowing | factual | Easy | 2571 |
| 3 | success | valid / verified | knowing | factual | Easy | 2596 |

Run 1 — solusi: 1 + 1 = 2
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat fakta dasar penjumlahan atau melakukan prosedur penjumlahan sederhana yang sangat langsung.. Bukti: 1 + 1 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan fakta dasar penjumlahan.. Bukti: 1 + 1 = ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan dasar satu digit yang sangat familiar bagi siswa kelas 1. Tidak ada keputusan strategi atau langkah yang saling bergantung.. Bukti: 1 + 1 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Ini adalah soal penjumlahan dasar yang merupakan standar kompetensi awal kelas 1. Tidak ada kompleksitas kognitif tambahan. |

Run 2 — solusi: 1 + 1 = 2
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk melakukan operasi penjumlahan dasar yang bersifat langsung dan prosedural, yang merupakan tugas mengingat fakta aritmatika dasar.. Bukti: 1 + 1 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji penguasaan fakta aritmatika dasar (penjumlahan bilangan satu digit), yang termasuk dalam kategori pengetahuan faktual.. Bukti: 1 + 1 = ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan satu digit yang sangat mendasar dan familiar bagi siswa kelas 1, tanpa memerlukan perencanaan atau integrasi langkah.. Bukti: 1 + 1 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Ini adalah soal penjumlahan dasar yang merupakan standar kurikulum kelas 1, tidak menuntut perencanaan atau strategi kompleks. |

Run 3 — solusi: 1 + 1 = 2
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk melakukan operasi penjumlahan dasar yang merupakan fakta dasar matematika (basic fact) bagi siswa kelas 1.. Bukti: 1 + 1 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji ingatan siswa terhadap fakta dasar penjumlahan 1 + 1.. Bukti: 1 + 1 = ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan satu digit yang sangat mendasar dan familiar bagi siswa kelas 1 tanpa memerlukan strategi atau perencanaan tambahan.. Bukti: 1 + 1 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1 sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Operasi 1+1 adalah fakta dasar yang diajarkan di awal kelas 1, sehingga tingkat kesulitannya rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 56/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999873; applying=0.000127; reasoning=0.000000 | knowing | 0.999873 | 0.001156 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.886842; conceptual=0.079171; procedural=0.033987; metacognitive=0.000000 | factual | 0.886842 | 0.304571 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.909786; Medium=0.088019; Hard=0.002195 | Easy | 0.909786 | 0.285229 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999873; −Σp ln(p) = 0.001270; H = 0.001270/ln(3) = 0.001156; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.886842; −Σp ln(p) = 0.422225; H = 0.422225/ln(4) = 0.304571; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.909786; −Σp ln(p) = 0.313356; H = 0.313356/ln(3) = 0.285229; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: 1 + 1 = ....
Pilihan: A. 3
B. 1
C. 11
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `018e7b45e13d10afc8e87d48`

Ada 3 sepeda Ada 1 becak.<br><br>Berapa jumlah semua rodanya?

| Opsi | Isi |
|---|---|
| A | 9 roda |
| B | 10 roda |
| C | 6 roda |
| D | 8 roda |

![Gambar sumber soal 13](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0081-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0081-01.png. Transkripsi visual: Gambar menunjukkan 3 sepeda (masing-masing dengan 2 roda) dan 1 becak (dengan 3 roda). Sepeda berwarna oranye, ungu, dan merah. Becak berwarna biru.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5d2cff276e39a7750c2310edc27077fb1341ef58e42bb5fc4c5c7f02ba6650df`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3409 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3423 |
| 3 | success | valid / verified | applying | procedural | Medium | 3463 |

Run 1 — solusi: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jumlah roda per objek (fakta eksternal/pengetahuan umum tentang sepeda dan becak) dan menerapkan operasi penjumlahan untuk mendapatkan total.. Bukti: Ada 3 sepeda Ada 1 becak. Berapa jumlah semua rodanya?
- Dimensi pengetahuan `classify/procedural`: Soal ini memerlukan pengetahuan faktual tentang jumlah roda pada sepeda dan becak, serta prosedur penjumlahan untuk menyelesaikan masalah.. Bukti: Ada 3 sepeda Ada 1 becak. Berapa jumlah semua rodanya?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk mengintegrasikan pengetahuan tentang jumlah roda (fakta) dengan operasi hitung. Meskipun hitungannya sederhana, siswa harus melakukan dua langkah (perkalian/penjumlahan berulang untuk sepeda, lalu penjumlahan total) yang saling bergantung.. Bukti: Ada 3 sepeda Ada 1 becak.; Berapa jumlah semua rodanya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang jumlah roda pada sepeda (2) dan becak (3), serta kemampuan penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, menghitung total roda dari objek yang berbeda memerlukan pemahaman bahwa objek memiliki atribut jumlah roda yang berbeda, yang merupakan langkah integrasi sedang. |

Run 2 — solusi: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jumlah roda per jenis kendaraan (pengetahuan faktual/konseptual) dan menerapkan operasi penjumlahan untuk mendapatkan total. Ini adalah penerapan prosedur rutin dalam konteks soal cerita.. Bukti: Ada 3 sepeda Ada 1 becak. Berapa jumlah semua rodanya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara objek (sepeda/becak) dan atributnya (jumlah roda), serta penggunaan operasi hitung untuk menyelesaikan masalah.. Bukti: Ada 3 sepeda Ada 1 becak.; Berapa jumlah semua rodanya?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium untuk kelas 1 karena memerlukan integrasi dua langkah: menghitung total roda sepeda (3x2) dan menambahkannya dengan roda becak (1x3). Meskipun operasinya dasar, siswa harus mengelola beberapa informasi (jumlah kendaraan dan jumlah roda per kendaraan) secara bersamaan.. Bukti: Ada 3 sepeda Ada 1 becak.; Berapa jumlah semua rodanya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman perkalian sebagai penjumlahan berulang (atau menghitung objek). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, mengintegrasikan dua jenis objek dengan jumlah roda berbeda dalam satu soal cerita merupakan tuntutan sedang yang memerlukan ketelitian dalam perencanaan langkah. |

Run 3 — solusi: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pengetahuan faktual tentang jumlah roda pada sepeda (2) dan becak (3), kemudian melakukan operasi penjumlahan. Ini adalah penerapan konsep dalam konteks rutin.. Bukti: Ada 3 sepeda Ada 1 becak.; Berapa jumlah semua rodanya?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pengetahuan prosedural (perkalian/penjumlahan berulang untuk menghitung total roda) yang didasarkan pada pengetahuan faktual tentang objek (sepeda dan becak).. Bukti: Ada 3 sepeda Ada 1 becak.; Berapa jumlah semua rodanya?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk mengidentifikasi jumlah objek, mengetahui jumlah roda per objek (pengetahuan umum), dan melakukan operasi hitung dua tahap. Bagi kelas 1, ini memerlukan perencanaan langkah yang saling bergantung (menghitung roda sepeda, menghitung roda becak, menjumlahkan keduanya), sehingga dikategorikan Medium.. Bukti: Ada 3 sepeda Ada 1 becak.; Berapa jumlah semua rodanya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang jumlah roda sepeda (2) dan becak (3), serta kemampuan penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 1 harus mengintegrasikan informasi visual (jumlah kendaraan) dengan pengetahuan eksternal (jumlah roda) dan melakukan dua tahap perhitungan (perkalian/penjumlahan berulang dan penjumlahan total). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4939`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi jumlah roda per objek (pengetahuan umum) dan menerapkan operasi penjumlahan untuk mendapatkan total. Ini adalah penerapan prosedur rutin dalam konteks soal cerita.
- Dimensi pengetahuan `procedural`: Soal ini memerlukan pengetahuan faktual tentang jumlah roda pada sepeda dan becak, serta prosedur penjumlahan untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium untuk kelas 1 karena memerlukan integrasi dua langkah: menghitung total roda sepeda (3x2) dan menambahkannya dengan roda becak (1x3). Meskipun operasinya dasar, siswa harus mengelola beberapa informasi (jumlah kendaraan dan jumlah roda per kendaraan) secara bersamaan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman bahwa sepeda memiliki 2 roda dan becak memiliki 3 roda. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, mengintegrasikan dua jenis objek dengan jumlah roda berbeda dalam satu soal cerita merupakan tuntutan sedang yang memerlukan ketelitian dalam perencanaan langkah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 97/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000074; applying=0.999926; reasoning=0.000000 | applying | 0.999926 | 0.000704 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.304742; conceptual=0.684040; procedural=0.011219; metacognitive=0.000000 | conceptual | 0.684040 | 0.484928 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.781300; Medium=0.214711; Hard=0.003988 | Easy | 0.781300 | 0.496244 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999926; −Σp ln(p) = 0.000774; H = 0.000774/ln(3) = 0.000704; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.684040; −Σp ln(p) = 0.672253; H = 0.672253/ln(4) = 0.484928; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.781300; −Σp ln(p) = 0.545180; H = 0.545180/ln(3) = 0.496244; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada 3 sepeda Ada 1 becak.

Berapa jumlah semua rodanya?
Pilihan: A. 9 roda
B. 10 roda
C. 6 roda
D. 8 roda
Transkripsi visual: Gambar menunjukkan 3 sepeda (masing-masing dengan 2 roda) dan 1 becak (dengan 3 roda). Sepeda berwarna oranye, ungu, dan merah. Becak berwarna biru.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ef576d96de5e9070503cfdbb`

Ada 3 motor. Ada 2 mobil.<br><br>Berapa jumlah semua kendaraan?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 3 |
| C | 5 |
| D | 4 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 3 motor + 2 mobil = 5 kendaraan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `54212b2365847aa3508a8aaf3bca70c5517b5f33695dbc38091725fe104121c8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2136 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2143 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2172 |

Run 1 — solusi: 3 motor + 2 mobil = 5 kendaraan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi penjumlahan dasar (3+2) berdasarkan informasi yang diberikan secara eksplisit dalam soal cerita sederhana.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep penjumlahan dasar sebagai operasi untuk menggabungkan dua kelompok benda.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari operasi penjumlahan dasar dengan angka kecil yang familiar bagi siswa kelas 1. Jalur penyelesaian sangat jelas dan tidak memerlukan perencanaan langkah yang kompleks.. Bukti: Ada 3 motor. Ada 2 mobil.; Berapa jumlah semua kendaraan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menghitung sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat sesuai dengan tingkat perkembangan kelas 1 karena hanya melibatkan satu operasi penjumlahan sederhana dengan objek konkret yang mudah dibayangkan. |

Run 2 — solusi: 3 motor + 2 mobil = 5 kendaraan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi penjumlahan dasar (3 + 2) berdasarkan informasi yang diberikan secara eksplisit dalam soal cerita sederhana.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep penjumlahan dasar sebagai penggabungan dua kelompok benda (motor dan mobil) menjadi satu total.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep penjumlahan dasar. Jalur penyelesaian sangat jelas, tidak memerlukan perencanaan strategi, dan hanya melibatkan satu operasi hitung sederhana yang familiar bagi siswa kelas 1.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menghitung sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, soal ini adalah latihan rutin penjumlahan bilangan kecil yang tidak menuntut perencanaan atau integrasi konsep yang kompleks. |

Run 3 — solusi: 3 motor + 2 mobil = 5 kendaraan.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan operasi penjumlahan dasar (3 + 2) berdasarkan informasi yang diberikan secara eksplisit dalam soal cerita sederhana.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep penjumlahan sebagai penggabungan dua kelompok benda (motor dan mobil) menjadi satu total.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung konsep penjumlahan dasar. Jalur penyelesaian sangat jelas, hanya melibatkan satu operasi hitung, dan tidak ada kendala atau langkah tambahan yang rumit bagi siswa kelas 1.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar kompetensi kelas 1 untuk penjumlahan bilangan cacah di bawah 10, yang merupakan materi rutin dan mendasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3376`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk melakukan operasi penjumlahan dasar (3 + 2) yang merupakan prosedur langsung dan rutin bagi siswa kelas 1.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konsep penjumlahan dasar sebagai penggabungan dua kelompok benda menjadi satu total.
- Intended difficulty `Easy`: Soal ini adalah penerapan langsung penjumlahan bilangan kecil yang sangat familiar bagi siswa kelas 1. Tidak ada perencanaan langkah yang kompleks atau kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menghitung sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar kompetensi kelas 1 untuk penjumlahan bilangan cacah di bawah 10, yang merupakan materi rutin dan mendasar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 60/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999257; applying=0.000743; reasoning=0.000000 | knowing | 0.999257 | 0.005550 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.740123; conceptual=0.226943; procedural=0.032933; metacognitive=0.000000 | factual | 0.740123 | 0.484537 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.855016; Medium=0.142340; Hard=0.002645 | Easy | 0.855016 | 0.388780 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999257; −Σp ln(p) = 0.006097; H = 0.006097/ln(3) = 0.005550; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.740123; −Σp ln(p) = 0.671711; H = 0.671711/ln(4) = 0.484537; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.855016; −Σp ln(p) = 0.427119; H = 0.427119/ln(3) = 0.388780; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada 3 motor. Ada 2 mobil.

Berapa jumlah semua kendaraan?
Pilihan: A. 6
B. 3
C. 5
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `adaec31c66c75d9c825ad888`

9 - ... = 7. Lengkapi operasi pengurangannya.

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 16 |
| C | 2 |
| D | 7 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 9 - 7 = 2, jadi bilangan yang hilang adalah 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `85ac5bdda8e5fd140dc181a6160b0a47177612833458ea26b66f05c9e9275a77`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2950 |
| 2 | success | valid / verified | applying | procedural | Easy | 2824 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2200 |

Run 1 — solusi: 9 - 2 = 7, maka bilangan yang hilang adalah 2.
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur pengurangan dasar untuk mencari bilangan yang hilang dalam kalimat matematika.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode pengurangan untuk melengkapi operasi hitung yang diberikan.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini adalah latihan rutin pengurangan dasar untuk kelas 1. Siswa hanya perlu mencari selisih antara 9 dan 7. Tidak ada kendala kompleks atau langkah ganda yang rumit.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pengurangan dasar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar kurikulum kelas 1 untuk memahami konsep pengurangan dengan bilangan yang hilang. |

Run 2 — solusi: 9 - 2 = 7, jadi bilangan yang tepat adalah 2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang hubungan pengurangan untuk mencari bilangan yang hilang dalam kalimat matematika sederhana.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/procedural`: Melibatkan penggunaan prosedur pengurangan dasar untuk melengkapi kalimat matematika.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini adalah latihan rutin pengurangan dasar yang familiar bagi siswa kelas 1. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pengurangan dasar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan satu operasi pengurangan dasar untuk menemukan bilangan yang hilang. |

Run 3 — solusi: Untuk mencari bilangan yang hilang dalam 9 - ... = 7, siswa perlu menghitung selisih antara 9 dan 7, yaitu 9 - 7 = 2.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melengkapi operasi pengurangan dengan mencari bilangan yang hilang. Ini adalah prosedur langsung untuk memahami hubungan antara pengurangan dan selisih bilangan, yang merupakan bagian dari kurikulum dasar kelas 1.. Bukti: 9 - ... = 7. Lengkapi operasi pengurangannya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan dasar dan hubungan antar bilangan dalam kalimat matematika sederhana.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini adalah latihan rutin untuk kelas 1. Siswa hanya perlu melakukan satu operasi pengurangan sederhana (9-7) untuk menemukan bilangan yang hilang. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan kalimat matematika terbuka sederhana seperti ini. Tugasnya hanya mencari selisih dua bilangan tunggal yang familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3258`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan prosedur pengurangan dasar untuk menemukan bilangan yang hilang. Ini adalah tugas rutin yang langsung.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan dasar dan hubungan antar bilangan dalam kalimat matematika sederhana.
- Intended difficulty `Easy`: Soal ini adalah latihan rutin pengurangan dasar yang sangat familiar bagi siswa kelas 1. Tidak ada langkah kompleks, kendala yang berinteraksi, atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pengurangan dasar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan satu operasi pengurangan dasar untuk menemukan bilangan yang hilang. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 59/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999688; applying=0.000312; reasoning=0.000000 | knowing | 0.999688 | 0.002579 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.665510; conceptual=0.288354; procedural=0.046135; metacognitive=0.000000 | factual | 0.665510 | 0.556523 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.897543; Medium=0.100066; Hard=0.002390 | Easy | 0.897543 | 0.311113 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999688; −Σp ln(p) = 0.002834; H = 0.002834/ln(3) = 0.002579; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.665510; −Σp ln(p) = 0.771504; H = 0.771504/ln(4) = 0.556523; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.897543; −Σp ln(p) = 0.341793; H = 0.341793/ln(3) = 0.311113; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 9 - ... = 7. Lengkapi operasi pengurangannya.
Pilihan: A. 3
B. 16
C. 2
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `91118c063eea5c139d44fcfe`

7 – 2 = ....<br><br>Isilah dengan bilangan yang tepat.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 2 |
| C | 7 |
| D | 9 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 7 - 2 = 5
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41fb0023e17d3c1a2acf03fbc35202320f24c1539eb3cc5a1fe1a2f9ea96c801`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2550 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2550 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2658 |

Run 1 — solusi: 7 - 2 = 5
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar secara langsung tanpa konteks cerita atau langkah tambahan. Ini adalah prosedur yang sangat langsung.. Bukti: 7 – 2 = ....
- Dimensi pengetahuan `classify/procedural`: Soal menguji kemampuan siswa dalam menjalankan algoritma pengurangan dasar (fakta pengurangan).. Bukti: 7 – 2 = ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi pengurangan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1. Tidak ada keputusan strategi atau kendala yang harus dibangun.. Bukti: 7 – 2 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 7-2 adalah standar kurikulum kelas 1, langsung, dan tidak memerlukan perencanaan kompleks. |

Run 2 — solusi: 7 dikurangi 2 sama dengan 5.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar secara langsung tanpa konteks cerita atau langkah tambahan. Ini adalah prosedur yang sangat langsung.. Bukti: 7 – 2 = ....
- Dimensi pengetahuan `classify/procedural`: Soal menguji kemampuan siswa dalam menjalankan algoritme pengurangan dasar.. Bukti: 7 – 2 = ....
- Intended difficulty `classify/Easy`: Soal merupakan operasi pengurangan dasar satu langkah dengan bilangan kecil yang familiar bagi siswa kelas 1. Tidak ada keputusan strategi atau kendala yang kompleks.. Bukti: 7 – 2 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 7-2 adalah standar kompetensi kelas 1 yang bersifat langsung dan rutin. |

Run 3 — solusi: 7 dikurangi 2 sama dengan 5.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar secara langsung tanpa konteks cerita atau langkah tambahan.. Bukti: 7 – 2 = ....
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan algoritma atau prosedur pengurangan dasar untuk mendapatkan hasil.. Bukti: 7 – 2 = ....
- Intended difficulty `classify/Easy`: Soal merupakan operasi pengurangan dasar satu langkah dengan bilangan kecil yang familiar bagi siswa kelas 1. Tidak ada keputusan strategi atau kendala yang kompleks.. Bukti: 7 – 2 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dasar 7-2 adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999992; applying=0.000008; reasoning=0.000000 | knowing | 0.999992 | 0.000094 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.844785; conceptual=0.080631; procedural=0.074584; metacognitive=0.000000 | factual | 0.844785 | 0.388892 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.924665; Medium=0.072464; Hard=0.002871 | Easy | 0.924665 | 0.254342 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000103; H = 0.000103/ln(3) = 0.000094; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.844785; −Σp ln(p) = 0.539119; H = 0.539119/ln(4) = 0.388892; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.924665; −Σp ln(p) = 0.279424; H = 0.279424/ln(3) = 0.254342; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 7 – 2 = ....

Isilah dengan bilangan yang tepat.
Pilihan: A. 5
B. 2
C. 7
D. 9
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `7aa38a3601f61c91adbf30d4`

Isilah titik-titik di bawah ini.<br><br> 6 – 4 = .... . Tulis hasil pengurangannya.

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 2 |
| C | 6 |
| D | 3 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 6 - 4 = 2
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `835f811062828a40c317f03ace17b2abc7bb05f5af01135f575237879175a5b3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2025 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2013 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2018 |

Run 1 — solusi: 6 - 4 = 2
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang sudah dipelajari di kelas 1. Ini adalah prosedur langsung tanpa perlu strategi kompleks.. Bukti: 6 – 4 = .... . Tulis hasil pengurangannya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar mengenai operasi pengurangan bilangan cacah.. Bukti: 6 – 4 = .... . Tulis hasil pengurangannya.
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1. Tidak ada kendala atau perencanaan yang diperlukan.. Bukti: 6 – 4 = .... . Tulis hasil pengurangannya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 6-4 adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

Run 2 — solusi: 6 - 4 = 2
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang merupakan prosedur langsung dan familiar bagi kelas 1.. Bukti: 6 – 4 = .... . Tulis hasil pengurangannya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menjalankan algoritma pengurangan dasar (prosedural) yang sudah dipelajari.. Bukti: 6 – 4 = .... .
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu operasi pengurangan dengan angka kecil, tanpa kendala atau langkah tambahan yang kompleks.. Bukti: 6 – 4 = .... .

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, pengurangan 6-4 adalah operasi dasar yang diharapkan sudah dikuasai sebagai bagian dari kurikulum awal. |

Run 3 — solusi: 6 - 4 = 2
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang merupakan prosedur langsung dan familiar bagi kelas 1.. Bukti: 6 – 4 = .... . Tulis hasil pengurangannya.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman terhadap algoritma pengurangan dasar (prosedural) yang sudah dipelajari di kelas 1.. Bukti: 6 – 4 = .... .
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1. Tidak ada kendala atau perencanaan kompleks yang diperlukan.. Bukti: 6 – 4 = .... .

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Operasi pengurangan 6-4 adalah materi standar kelas 1 yang bersifat langsung tanpa memerlukan langkah tambahan atau penalaran kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 71/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999457; applying=0.000543; reasoning=0.000000 | knowing | 0.999457 | 0.004213 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.693774; conceptual=0.160236; procedural=0.145990; metacognitive=0.000000 | factual | 0.693774 | 0.597258 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.915849; Medium=0.081123; Hard=0.003028 | Easy | 0.915849 | 0.274739 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999457; −Σp ln(p) = 0.004629; H = 0.004629/ln(3) = 0.004213; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.693774; −Σp ln(p) = 0.827975; H = 0.827975/ln(4) = 0.597258; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.915849; −Σp ln(p) = 0.301832; H = 0.301832/ln(3) = 0.274739; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik di bawah ini.

 6 – 4 = .... . Tulis hasil pengurangannya.
Pilihan: A. 10
B. 2
C. 6
D. 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `dde0b5654f117861d23c7988`

0 1 2 3 4 5 6 7 8 9 10<br><br>Hitunglah. 9 – 3 =

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 3 |
| C | 6 |
| D | 5 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menggunakan garis bilangan: mulai dari angka 9, mundur 3 langkah ke kiri (9 ke 8, 8 ke 7, 7 ke 6), sehingga hasilnya adalah 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `19415c0f9dc1bb55a3ad15889a813a3a4c4138472f444ace519be0b78a606d0b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2164 |
| 2 | success | valid / verified | knowing | factual | Easy | 2182 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2186 |

Run 1 — solusi: Menggunakan garis bilangan: mulai dari 9, mundur 3 langkah ke kiri (9 -> 8 -> 7 -> 6). Hasilnya adalah 6.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang sudah familiar. Prosedur ini bersifat langsung dan tidak memerlukan strategi nonrutin.. Bukti: Hitunglah. 9 – 3 =
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme atau prosedur pengurangan dasar.. Bukti: 9 – 3 =
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu digit yang sangat mendasar bagi siswa kelas 1. Jalur penyelesaiannya tunggal dan langsung.. Bukti: 9 – 3 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan penggunaan garis bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 9-3 adalah standar kompetensi kelas 1 yang bersifat rutin dan langsung. |

Run 2 — solusi: Menggunakan garis bilangan: mulai dari 9, mundur 3 langkah ke kiri (8, 7, 6), sehingga 9 - 3 = 6.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang sudah familiar. Prosedur penyelesaiannya langsung dan tidak memerlukan strategi non-rutin.. Bukti: Hitunglah. 9 – 3 =
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan penggunaan simbol matematika.. Bukti: 9 – 3 =
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu digit yang sangat mendasar bagi siswa kelas 1. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: 9 – 3 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan penggunaan garis bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 9-3 adalah standar kompetensi kelas 1 yang bersifat langsung dan rutin. |

Run 3 — solusi: Menggunakan garis bilangan: mulai dari 9, mundur 3 langkah ke kiri, berhenti di 6.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang sudah familiar. Tugas ini hanya memerlukan eksekusi prosedur pengurangan langsung tanpa perlu strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Hitunglah. 9 – 3 =
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau prosedur pengurangan dasar (fakta matematika dasar).. Bukti: 9 – 3 =
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu digit yang sangat mendasar dan familiar bagi siswa kelas 1. Jalur penyelesaiannya langsung, tidak ada kendala yang berinteraksi, dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: 9 – 3 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan penggunaan garis bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 9-3 adalah standar kompetensi kelas 1. Tidak ada tuntutan kognitif tambahan selain melakukan pengurangan sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3355`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta melakukan operasi pengurangan dasar yang sudah familiar. Prosedur ini bersifat langsung dan tidak memerlukan strategi nonrutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang prosedur atau algoritme pengurangan dasar.
- Intended difficulty `Easy`: Soal ini merupakan operasi pengurangan satu digit yang sangat mendasar bagi siswa kelas 1. Jalur penyelesaiannya tunggal, langsung, dan tidak memerlukan perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan penggunaan garis bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 9-3 adalah standar kompetensi kelas 1 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999282; applying=0.000718; reasoning=0.000000 | knowing | 0.999282 | 0.005383 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.885192; conceptual=0.055372; procedural=0.059435; metacognitive=0.000000 | factual | 0.885192 | 0.314477 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.930516; Medium=0.067243; Hard=0.002241 | Easy | 0.930516 | 0.238667 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999282; −Σp ln(p) = 0.005914; H = 0.005914/ln(3) = 0.005383; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.885192; −Σp ln(p) = 0.435958; H = 0.435958/ln(4) = 0.314477; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.930516; −Σp ln(p) = 0.262202; H = 0.262202/ln(3) = 0.238667; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 0 1 2 3 4 5 6 7 8 9 10

Hitunglah. 9 – 3 =
Pilihan: A. 12
B. 3
C. 6
D. 5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `b32a5eeea2898efe65526fe5`

9 - ... = 7<br><br>Isilah titik-titik di bawah ini.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 3 |
| C | 7 |
| D | 16 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Siswa perlu mencari bilangan yang jika dikurangkan dari 9 menghasilkan 7. Dengan hubungan pengurangan dan penjumlahan, 9 - 7 = 2. Jadi, 9 - 2 = 7.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ae1fd9e97b2a95a6dc865d837557f5f0b29d5c53c03af3ab07eecc116cc5976c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2177 |
| 2 | success | valid / verified | knowing | factual | Easy | 2194 |
| 3 | success | valid / verified | knowing | factual | Easy | 2162 |

Run 1 — solusi: Siswa perlu mencari bilangan yang jika dikurangkan dari 9 menghasilkan 7. Dengan hubungan pengurangan dan penjumlahan, 9 - 7 = 2. Jadi, 9 - 2 = 7.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melengkapi kalimat matematika sederhana yang melibatkan hubungan dasar antara pengurangan dan penjumlahan. Ini adalah prosedur langsung yang familiar bagi siswa kelas 1.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan hubungan invers dengan penjumlahan.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan dasar dengan angka kecil yang familiar. Jalur penyelesaiannya sangat langsung (mencari selisih antara 9 dan 7) tanpa memerlukan perencanaan strategi yang kompleks atau integrasi kendala.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta bilangan sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, soal ini adalah latihan rutin yang menguji pemahaman dasar tentang hubungan pengurangan. Tidak ada tuntutan kognitif tinggi. |

Run 2 — solusi: Untuk mencari bilangan yang hilang, kita perlu menghitung selisih antara 9 dan 7. 9 - 7 = 2. Jadi, 9 - 2 = 7.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menentukan bilangan yang hilang dalam kalimat matematika pengurangan sederhana. Ini adalah prosedur langsung yang familiar bagi siswa kelas 1 untuk memahami hubungan antara bilangan dalam pengurangan.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan hubungan antar bilangan (fakta dasar/konseptual sederhana).. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu melakukan satu operasi pengurangan sederhana (9-7) untuk menemukan jawabannya. Tidak ada langkah tambahan atau kendala yang kompleks.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, soal ini adalah latihan rutin yang menguji pemahaman dasar tentang operasi pengurangan. Jalur penyelesaiannya sangat jelas dan tidak memerlukan perencanaan atau integrasi konsep yang rumit. |

Run 3 — solusi: Untuk mencari bilangan yang hilang dalam 9 - x = 7, kita dapat menghitung selisih antara 9 dan 7, yaitu 9 - 7 = 2. Jadi, 9 - 2 = 7.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menentukan bilangan yang hilang dalam kalimat matematika pengurangan sederhana. Ini adalah prosedur langsung yang melibatkan pemahaman hubungan dasar antara bilangan dalam pengurangan.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan hubungan antar bilangan dalam operasi pengurangan.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep pengurangan dasar yang familiar bagi siswa kelas 1. Tidak ada langkah tambahan atau kendala yang kompleks.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pengurangan dasar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar untuk kelas 1 mengenai hubungan pengurangan, dengan angka yang kecil dan prosedur yang sangat rutin. |

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
| Domain kognitif | knowing=0.999997; applying=0.000003; reasoning=0.000000 | knowing | 0.999997 | 0.000042 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.507478; conceptual=0.438746; procedural=0.053776; metacognitive=0.000000 | factual | 0.507478 | 0.622422 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.902504; Medium=0.095505; Hard=0.001991 | Easy | 0.902504 | 0.299707 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999997; −Σp ln(p) = 0.000046; H = 0.000046/ln(3) = 0.000042; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.507478; −Σp ln(p) = 0.862860; H = 0.862860/ln(4) = 0.622422; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.902504; −Σp ln(p) = 0.329262; H = 0.329262/ln(3) = 0.299707; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Hubungan Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 9 - ... = 7

Isilah titik-titik di bawah ini.
Pilihan: A. 2
B. 3
C. 7
D. 16
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `f6fcf5836947ff740007f70e`

Isilah titik-titik di bawah ini.<br><br>2 + 6 = ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | 26 |
| C | 9 |
| D | 8 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 2 + 6 = 8
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e59716108118ba012471da0433065edb7f88876dde2a106c07d6b59230d383f7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2113 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2113 |
| 3 | success | valid / verified | knowing | factual | Easy | 2103 |

Run 1 — solusi: 2 + 6 = 8
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur langsung dan familiar bagi kelas 1.. Bukti: 2 + 6 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap fakta penjumlahan dasar (basic addition facts).. Bukti: 2 + 6 = ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1, tanpa memerlukan strategi atau perencanaan kompleks.. Bukti: 2 + 6 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan satu digit adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

Run 2 — solusi: 2 + 6 = 8
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi penjumlahan dasar yang merupakan prosedur langsung dan familiar bagi siswa kelas 1.. Bukti: 2 + 6 = ....
- Dimensi pengetahuan `classify/procedural`: Soal menguji kemampuan siswa dalam melakukan prosedur penjumlahan dasar (algoritme penjumlahan sederhana).. Bukti: 2 + 6 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1, dengan jalur penyelesaian yang langsung.. Bukti: 2 + 6 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta dasar penjumlahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar kompetensi kelas 1 untuk penjumlahan bilangan cacah sampai 10 atau 20. Tidak ada tuntutan perencanaan atau integrasi konsep yang kompleks. |

Run 3 — solusi: 2 + 6 = 8
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar satu langkah yang sudah familiar bagi kelas 1.. Bukti: 2 + 6 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang fakta penjumlahan dasar (fakta aritmatika).. Bukti: 2 + 6 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1, tanpa memerlukan strategi kompleks atau integrasi langkah.. Bukti: 2 + 6 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta bilangan sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 2 + 6 adalah materi standar kelas 1 yang bersifat prosedural langsung tanpa beban kognitif tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3154`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dasar satu langkah yang merupakan prosedur langsung dan familiar bagi siswa kelas 1.
- Dimensi pengetahuan `factual`: Soal ini menguji penguasaan fakta aritmatika dasar (basic addition facts) yang merupakan elemen pengetahuan faktual.
- Intended difficulty `Easy`: Soal ini adalah operasi penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1, tanpa memerlukan strategi atau perencanaan kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan satu digit adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999968; applying=0.000032; reasoning=0.000000 | knowing | 0.999968 | 0.000329 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.616499; conceptual=0.348460; procedural=0.035041; metacognitive=0.000000 | factual | 0.616499 | 0.564807 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.900719; Medium=0.097314; Hard=0.001967 | Easy | 0.900719 | 0.303254 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999968; −Σp ln(p) = 0.000361; H = 0.000361/ln(3) = 0.000329; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.616499; −Σp ln(p) = 0.782989; H = 0.782989/ln(4) = 0.564807; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.900719; −Σp ln(p) = 0.333159; H = 0.333159/ln(3) = 0.303254; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Hubungan Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik di bawah ini.

2 + 6 = ....
Pilihan: A. 4
B. 26
C. 9
D. 8
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `63d056eda46964278255c543`

Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.<br><br>Berapakah sisa kelereng Malosi?

| Opsi | Isi |
|---|---|
| A | 3 kelereng |
| B | 7 kelereng |
| C | 5 kelereng |
| D | 15 kelereng |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 9 - 2 - 4 = 3
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `808582396e3489bd50f5c434466f54c849fcc9e0fe1b2f50232ec4c8f827176e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2185 |
| 2 | success | valid / verified | applying | procedural | Medium | 2204 |
| 3 | success | valid / verified | applying | procedural | Medium | 2225 |

Run 1 — solusi: 9 - 2 - 4 = 3
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dua kali secara berurutan dalam konteks cerita rutin. Ini adalah penerapan konsep pengurangan pada situasi sehari-hari yang familiar bagi kelas 1.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan dan bagaimana menerapkannya dalam urutan langkah yang logis.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah pengurangan yang saling terkait (9-2=7, lalu 7-4=3). Meskipun prosedurnya familiar, siswa harus mengelola dua informasi pengurangan secara berurutan, yang sedikit lebih kompleks daripada operasi tunggal.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan melakukan pengurangan bilangan satu digit. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, melakukan dua langkah pengurangan berurutan dalam soal cerita merupakan tuntutan yang wajar namun memerlukan ketelitian lebih dibandingkan soal satu langkah. |

Run 2 — solusi: 9 - 2 - 4 = 3
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan berulang pada konteks cerita rutin. Ini adalah penerapan konsep pengurangan dalam situasi sehari-hari yang familiar bagi siswa kelas 1.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.; Berapakah sisa kelereng Malosi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur pengurangan (algoritme dasar) untuk menyelesaikan masalah pengurangan bertahap.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah pengurangan yang saling terkait (9-2=7, lalu 7-4=3). Meskipun prosedurnya familiar, siswa harus mengelola dua pengurangan berurutan tanpa bantuan langkah antara, yang merupakan tuntutan sedang untuk kelas 1.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan melakukan pengurangan dua bilangan satu angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 umumnya sudah belajar pengurangan. Soal ini menuntut ketelitian dalam melakukan dua kali pengurangan berurutan, yang sedikit lebih kompleks daripada pengurangan satu langkah. |

Run 3 — solusi: 9 - 2 - 4 = 3
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan berulang (atau pengurangan jumlah total yang diberikan) dalam konteks soal cerita rutin. Ini adalah penerapan konsep pengurangan pada situasi sehari-hari.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.; Berapakah sisa kelereng Malosi?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode atau teknik pengurangan (algoritme dasar) untuk menyelesaikan masalah pengurangan bertahap.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah pengurangan yang saling terkait (9-2=7, lalu 7-4=3) atau menjumlahkan pengurang terlebih dahulu (2+4=6, lalu 9-6=3). Bagi siswa kelas 1, mengelola dua aksi pengurangan dalam satu cerita memerlukan perencanaan langkah yang sedikit lebih kompleks daripada operasi tunggal.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan dasar 1-10 dan pemahaman konsep sisa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasinya sederhana, siswa kelas 1 harus melacak dua kejadian pengurangan terpisah dari total awal, yang menuntut perhatian pada urutan dan kelengkapan informasi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 87/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000122; applying=0.999878; reasoning=0.000000 | applying | 0.999878 | 0.001115 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.198759; conceptual=0.732509; procedural=0.068732; metacognitive=0.000000 | conceptual | 0.732509 | 0.528874 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.813451; Medium=0.183144; Hard=0.003406 | Easy | 0.813451 | 0.453470 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999878; −Σp ln(p) = 0.001225; H = 0.001225/ln(3) = 0.001115; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.732509; −Σp ln(p) = 0.733175; H = 0.733175/ln(4) = 0.528874; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.813451; −Σp ln(p) = 0.498188; H = 0.498188/ln(3) = 0.453470; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.

Berapakah sisa kelereng Malosi?
Pilihan: A. 3 kelereng
B. 7 kelereng
C. 5 kelereng
D. 15 kelereng
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `9948cc37d48fcfe7ef094209`

Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.<br><br>Berapakah sisa telur Ibu sekarang?

| Opsi | Isi |
|---|---|
| A | 3 telur |
| B | 8 telur |
| C | 4 telur |
| D | 6 telur |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 6 - 2 = 4
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `66c0a95a0b034cd7425ce9e1ec3d88eb3102f5a9988ac92442555547edfe7030`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2093 |
| 2 | success | valid / verified | applying | procedural | Easy | 3307 |
| 3 | success | valid / verified | applying | procedural | Easy | 2109 |

Run 1 — solusi: 6 - 2 = 4
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar pada konteks cerita yang familiar (pengurangan benda konkret). Ini adalah penerapan prosedur rutin.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.; Berapakah sisa telur Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur pengurangan dasar (algoritme pengurangan) dalam konteks cerita.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah satu langkah yang sangat langsung. Siswa hanya perlu mengidentifikasi operasi pengurangan dari kata kunci 'pecah' dan menghitung 6 dikurangi 2. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.; Berapakah sisa telur Ibu sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung 6-2. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, pengurangan satu digit adalah materi standar yang bersifat rutin dan langsung. |

Run 2 — solusi: 6 - 2 = 4
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar pada konteks cerita yang familiar.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.; Berapakah sisa telur Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Melibatkan penggunaan algoritme pengurangan dasar untuk menyelesaikan masalah cerita.. Bukti: 6 telur; 2 telur; sisa
- Intended difficulty `classify/Easy`: Soal ini adalah soal pengurangan satu langkah yang sangat standar untuk kelas 1. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: 6 telur; 2 telur; sisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung 6-2. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal pengurangan satu langkah dengan angka kecil adalah materi dasar kelas 1 yang rutin. |

Run 3 — solusi: 6 - 2 = 4
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar pada konteks cerita yang sangat sederhana dan rutin. Ini adalah penerapan prosedur pengurangan yang sudah dipelajari di kelas 1.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.; Berapakah sisa telur Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan (pengambilan/pengurangan objek) dalam konteks kehidupan sehari-hari.. Bukti: 6 telur; 2 telur milik Ibu pecah; Berapakah sisa telur Ibu sekarang?
- Intended difficulty `classify/Easy`: Soal ini merupakan soal cerita satu langkah yang sangat standar untuk kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.; Berapakah sisa telur Ibu sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung mundur atau pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah contoh klasik pengurangan satu langkah yang sesuai dengan kurikulum kelas 1, di mana siswa diharapkan mampu menyelesaikan masalah pengurangan sederhana tanpa bantuan tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 69/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.078699; applying=0.921301; reasoning=0.000000 | applying | 0.921301 | 0.250845 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.454706; conceptual=0.478181; procedural=0.067112; metacognitive=0.000000 | conceptual | 0.478181 | 0.643758 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.906485; Medium=0.089075; Hard=0.004440 | Easy | 0.906485 | 0.298977 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.921301; −Σp ln(p) = 0.275581; H = 0.275581/ln(3) = 0.250845; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.478181; −Σp ln(p) = 0.892438; H = 0.892438/ln(4) = 0.643758; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.906485; −Σp ln(p) = 0.328460; H = 0.328460/ln(3) = 0.298977; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.

Berapakah sisa telur Ibu sekarang?
Pilihan: A. 3 telur
B. 8 telur
C. 4 telur
D. 6 telur
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `355049fbd1c523a25cd2de3d`

Apa bentuk dari gambar berikut?

| Opsi | Isi |
|---|---|
| A | Bentuk bintang |
| B | Segi empat |
| C | Segitiga |
| D | Bentuk lengkung |

![Gambar sumber soal 23](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0134-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan ciri khas dari bentuk segitiga.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0134-03.png. Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut, yang secara geometris merupakan segitiga.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cf0be1293ee3cfb1d576b73a203b2ddeaf75ab981c91802b291171180fd58330`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3316 |
| 2 | success | valid / verified | knowing | factual | Easy | 3357 |
| 3 | success | valid / verified | knowing | factual | Easy | 3328 |

Run 1 — solusi: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan ciri khas dari bentuk segitiga.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan mengidentifikasi bentuk geometri dasar (segitiga) berdasarkan representasi visual langsung. Ini adalah proses pengenalan bentuk yang merupakan prosedur langsung.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai nama-nama bentuk geometri dasar (segitiga).. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan familiar bagi siswa kelas 1. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk geometri dasar seperti segitiga, lingkaran, dan segi empat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Mengidentifikasi bentuk segitiga adalah materi dasar kelas 1 yang bersifat langsung dan tidak memerlukan analisis kompleks. |

Run 2 — solusi: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan ciri khas dari bentuk segitiga.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan mengklasifikasikan bentuk bangun datar berdasarkan ciri visualnya (tiga sisi, tiga sudut). Ini adalah proses mengenali bentuk dasar yang sudah dipelajari.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bentuk bangun datar dasar.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan tidak memerlukan langkah-langkah kompleks atau penalaran mendalam. Siswa hanya perlu mengidentifikasi bentuk visual yang disajikan.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama-nama bangun datar dasar (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, mengidentifikasi bentuk segitiga dari gambar yang jelas adalah tugas yang sangat mendasar dan rutin. |

Run 3 — solusi: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan ciri khas bentuk segitiga.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan mengidentifikasi bentuk dasar (segitiga) berdasarkan atribut visual yang diberikan. Ini adalah proses pengenalan langsung.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bentuk geometri dasar.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mencocokkan visual gambar dengan label bentuk yang sudah dipelajari. Tidak ada langkah tambahan atau analisis kompleks.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama-nama bentuk dasar (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, mengidentifikasi bentuk segitiga adalah materi dasar yang sangat familiar dan tidak memerlukan penalaran tingkat lanjut. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 78/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.986166; applying=0.013834; reasoning=0.000000 | knowing | 0.986166 | 0.066409 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.846495; conceptual=0.149835; procedural=0.003670; metacognitive=0.000000 | factual | 0.846495 | 0.321770 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.896061; Medium=0.101122; Hard=0.002817 | Easy | 0.896061 | 0.315485 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.986166; −Σp ln(p) = 0.072958; H = 0.072958/ln(3) = 0.066409; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.846495; −Σp ln(p) = 0.446068; H = 0.446068/ln(4) = 0.321770; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.896061; −Σp ln(p) = 0.346596; H = 0.346596/ln(3) = 0.315485; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mendeskripsikan Benda Berdasarkan Bentuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa bentuk dari gambar berikut?
Pilihan: A. Bentuk bintang
B. Segi empat
C. Segitiga
D. Bentuk lengkung
Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut, yang secara geometris merupakan segitiga.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `83dd4d12892fc170e56f4e1b`

Pasangkan bentuk dengan namanya. Bangun keempat dari atas.

| Opsi | Isi |
|---|---|
| A | Bentuk lengkung |
| B | Bentuk bintang |
| C | Segi empat |
| D | Segitiga |

![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-01.png>)


![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-02.png>)


![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-03.png>)


![Gambar sumber soal 24](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0153-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bangun keempat dari atas adalah lingkaran merah. Lingkaran adalah bentuk lengkung.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0153-01.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-02.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-03.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-04.png. Transkripsi visual: Terdapat empat bangun datar yang disusun vertikal dari atas ke bawah: 1. Persegi berwarna biru, 2. Segitiga berwarna ungu, 3. Persegi panjang berwarna biru, 4. Lingkaran berwarna merah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b4a94c3114eb95de0bea5219b190ba7f8172827d57ba65b5093821b40d384cfb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 6599 |
| 2 | success | valid / verified | knowing | factual | Easy | 6595 |
| 3 | success | valid / verified | knowing | factual | Easy | 6602 |

Run 1 — solusi: Bangun keempat dari atas adalah lingkaran merah. Lingkaran adalah bentuk lengkung.
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi bentuk bangun datar berdasarkan ciri visualnya (lengkung) dan menghitung urutan posisi bangun dalam daftar vertikal. Ini adalah tugas pengenalan bentuk dasar.. Bukti: Pasangkan bentuk dengan namanya. Bangun keempat dari atas.
- Dimensi pengetahuan `classify/factual`: Soal menguji pengetahuan faktual tentang nama dan ciri dasar bangun datar (lingkaran sebagai bentuk lengkung).. Bukti: Pasangkan bentuk dengan namanya.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan dua langkah rutin: menghitung urutan (1-4) dan mencocokkan bentuk dengan label yang sudah dipelajari. Tidak ada kendala yang berinteraksi atau strategi kompleks.. Bukti: Bangun keempat dari atas.; Pasangkan bentuk dengan namanya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama bangun datar dasar dan kemampuan berhitung urutan 1-4. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan pengenalan bentuk dan urutan sederhana; tugas ini adalah aplikasi langsung dari materi tersebut. |

Run 2 — solusi: Mengidentifikasi urutan keempat dari atas adalah lingkaran merah, yang memiliki sifat bentuk lengkung.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi objek berdasarkan urutan dan mengenali sifat geometris dasar (bentuk lengkung) dari objek tersebut. Ini adalah proses pengenalan langsung.. Bukti: Pasangkan bentuk dengan namanya. Bangun keempat dari atas.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap istilah dan karakteristik dasar bentuk geometri (fakta bahwa lingkaran adalah bentuk lengkung).. Bukti: Pasangkan bentuk dengan namanya.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan kemampuan menghitung urutan sederhana (1-4) dan mengenali bentuk dasar yang sangat familiar bagi siswa kelas 1.. Bukti: Bangun keempat dari atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung urutan 1-4 dan pengenalan bentuk dasar (lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mengidentifikasi urutan dan mencocokkan dengan nama bentuk adalah standar kompetensi kelas 1 yang bersifat langsung. |

Run 3 — solusi: Mengidentifikasi urutan keempat dari atas adalah lingkaran merah, yang memiliki sifat bentuk lengkung.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi objek berdasarkan urutan (posisi) dan kemudian mengklasifikasikan bentuk geometris tersebut ke dalam kategori yang tepat. Ini adalah proses pengenalan sifat dasar bentuk.. Bukti: Pasangkan bentuk dengan namanya. Bangun keempat dari atas.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang istilah dan karakteristik dasar bentuk geometris (lingkaran sebagai bentuk lengkung).. Bukti: Pasangkan bentuk dengan namanya.; Bentuk lengkung
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan dua langkah sederhana: menghitung urutan (1-4) dan mengenali bentuk. Ini adalah tugas rutin untuk kelas 1.. Bukti: Bangun keempat dari atas.; Pasangkan bentuk dengan namanya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (lingkaran, segitiga, persegi) dan kemampuan menghitung urutan 1-4. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi urutan dan mencocokkan bentuk adalah standar kompetensi kelas 1 yang bersifat langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 98/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.987719; applying=0.012281; reasoning=0.000000 | knowing | 0.987719 | 0.060294 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.326479; conceptual=0.667217; procedural=0.006304; metacognitive=0.000000 | conceptual | 0.667217 | 0.481414 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873796; Medium=0.123436; Hard=0.002769 | Easy | 0.873796 | 0.357196 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.987719; −Σp ln(p) = 0.066240; H = 0.066240/ln(3) = 0.060294; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.667217; −Σp ln(p) = 0.667381; H = 0.667381/ln(4) = 0.481414; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873796; −Σp ln(p) = 0.392420; H = 0.392420/ln(3) = 0.357196; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mendeskripsikan Benda Berdasarkan Bentuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangkan bentuk dengan namanya. Bangun keempat dari atas.
Pilihan: A. Bentuk lengkung
B. Bentuk bintang
C. Segi empat
D. Segitiga
Transkripsi visual: Terdapat empat bangun datar yang disusun vertikal dari atas ke bawah: 1. Persegi berwarna biru, 2. Segitiga berwarna ungu, 3. Persegi panjang berwarna biru, 4. Lingkaran berwarna merah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `98891851d1e28d6d8482ab94`

Pilih jawaban yang benar. Bangun yang satu kelompok dengan gambar di atas.

| Opsi | Isi |
|---|---|
| A | Persegi panjang berwarna ungu |
| B | Segitiga terbalik berwarna ungu |
| C | Persegi berwarna ungu |
| D | Oval berwarna ungu |

![Gambar sumber soal 25](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0143-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Ketiga gambar acuan adalah segitiga. Pilihan B adalah segitiga, sedangkan pilihan A, C, dan D bukan segitiga.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0143-05.png. Transkripsi visual: Terdapat tiga bangun datar di dalam kotak: segitiga siku-siku berwarna ungu muda, segitiga sama kaki berwarna oranye muda, dan segitiga sama kaki berwarna merah muda. Ketiganya memiliki bentuk dasar segitiga namun berbeda warna dan ukuran.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3c7c98a80fa46fc15c233be2016f79dc2eb466729a62681e9be37a5b4e099443`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3404 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3452 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3466 |

Run 1 — solusi: Ketiga gambar acuan adalah segitiga. Pilihan B adalah segitiga, sedangkan pilihan A, C, dan D bukan segitiga.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi atribut pembeda (bentuk) di antara atribut pengecoh (warna dan ukuran) untuk mengelompokkan objek. Ini adalah proses klasifikasi sederhana yang menerapkan konsep bentuk dasar.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan... sama-sama berbentuk segitiga
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bangun datar (segitiga) terlepas dari variasi warna atau ukuran.. Bukti: Bangun yang satu kelompok dengan gambar di atas
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengenali atribut bentuk yang konsisten (segitiga) di antara tiga contoh yang diberikan. Pengecoh (warna) cukup jelas perbedaannya dengan bentuk.. Bukti: Bangun yang satu kelompok dengan gambar di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar bangun datar (segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan untuk mengelompokkan benda berdasarkan satu atribut (bentuk). Tugas ini adalah penerapan langsung dari konsep tersebut. |

Run 2 — solusi: Ketiga gambar acuan adalah segitiga. Pilihan B adalah satu-satunya gambar yang berbentuk segitiga, sehingga termasuk dalam kelompok yang sama.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi atribut pembeda (bentuk) di antara atribut lain (warna, ukuran) untuk mengelompokkan objek. Ini adalah proses klasifikasi sederhana yang menerapkan konsep bentuk dasar.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan (ungu, oranye, merah muda) sama-sama berbentuk segitiga
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bangun datar (segitiga) dan kemampuan untuk mengabaikan atribut yang tidak relevan (warna/ukuran) dalam pengelompokan.. Bukti: Bangun yang satu kelompok dengan gambar di atas
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengenali pola (bentuk segitiga) di tengah variasi warna dan ukuran. Bagi siswa kelas 1, ini adalah tugas rutin dalam materi geometri dasar.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan (ungu, oranye, merah muda) sama-sama berbentuk segitiga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (segitiga) dan kemampuan membedakan atribut visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengelompokkan berdasarkan bentuk adalah materi standar kelas 1. Distraktor (warna) cukup jelas untuk memancing kesalahan, namun konsep dasarnya sangat mendasar. |

Run 3 — solusi: Ketiga gambar acuan adalah segitiga dengan warna dan ukuran berbeda. Kelompok tersebut didasarkan pada bentuk (segitiga). Pilihan B adalah satu-satunya segitiga.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi atribut pembeda (bentuk) di antara atribut lain (warna, ukuran) untuk mengelompokkan objek. Ini adalah proses klasifikasi sederhana yang termasuk dalam domain applying.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan (ungu, oranye, merah muda) sama-sama berbentuk segitiga
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bangun datar (segitiga) sebagai dasar pengelompokan, melampaui sekadar pengenalan fakta visual.. Bukti: Bangun yang satu kelompok dengan gambar di atas
- Intended difficulty `classify/Easy`: Siswa harus mengabaikan distraktor warna dan ukuran untuk fokus pada bentuk. Meskipun konsepnya dasar, siswa kelas 1 perlu melakukan abstraksi bentuk dari variasi visual yang diberikan.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan (ungu, oranye, merah muda) sama-sama berbentuk segitiga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (segitiga) dan konsep atribut benda. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengelompokkan berdasarkan satu atribut (bentuk) adalah standar untuk kelas 1. Distraktor warna cukup umum namun tidak membuat soal menjadi sulit bagi siswa yang sudah memahami konsep bentuk. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 111/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.005830; applying=0.994170; reasoning=0.000000 | applying | 0.994170 | 0.032592 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.415539; conceptual=0.578966; procedural=0.005495; metacognitive=0.000000 | conceptual | 0.578966 | 0.512101 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.868835; Medium=0.128586; Hard=0.002579 | Easy | 0.868835 | 0.365264 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.994170; −Σp ln(p) = 0.035806; H = 0.035806/ln(3) = 0.032592; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.578966; −Σp ln(p) = 0.709923; H = 0.709923/ln(4) = 0.512101; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.868835; −Σp ln(p) = 0.401284; H = 0.401284/ln(3) = 0.365264; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Pilih jawaban yang benar. Bangun yang satu kelompok dengan gambar di atas.
Pilihan: A. Persegi panjang berwarna ungu
B. Segitiga terbalik berwarna ungu
C. Persegi berwarna ungu
D. Oval berwarna ungu
Transkripsi visual: Terdapat tiga bangun datar di dalam kotak: segitiga siku-siku berwarna ungu muda, segitiga sama kaki berwarna oranye muda, dan segitiga sama kaki berwarna merah muda. Ketiganya memiliki bentuk dasar segitiga namun berbeda warna dan ukuran.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `7bde28fb9ff374327ad9c3ae`

Bangun yang satu warna dengan gambar di atas.

| Opsi | Isi |
|---|---|
| A | Persegi berwarna ungu |
| B | Oval berwarna hijau |
| C | Persegi panjang berwarna biru |
| D | Segitiga terbalik berwarna merah muda |

![Gambar sumber soal 26](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0144-00.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identifikasi warna bangun di dalam kotak adalah merah muda. Periksa pilihan jawaban: segitiga terbalik (merah muda), persegi (ungu), oval (hijau). Hanya segitiga terbalik yang memiliki warna merah muda yang sama dengan bangun di dalam kotak.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0144-00.png. Transkripsi visual: Terdapat sebuah kotak berisi tiga bangun datar: persegi panjang, segitiga siku-siku, dan persegi panjang. Ketiga bangun tersebut berwarna merah muda. Di bawah kotak, terdapat tiga pilihan bangun: segitiga terbalik berwarna merah muda, persegi berwarna ungu, dan oval berwarna hijau. Pertanyaan meminta untuk memilih bangun yang memiliki warna yang sama dengan bangun di dalam kotak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec66224fa8ec200b65f456b24baf41a5b24107b88c951899f4ae1f8848d3d88f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3416 |
| 2 | success | valid / verified | knowing | factual | Easy | 3435 |
| 3 | success | valid / verified | knowing | factual | Easy | 3406 |

Run 1 — solusi: Identifikasi warna bangun pada kotak acuan (merah muda), lalu pilih bangun di antara pilihan yang memiliki warna yang sama (segitiga terbalik merah muda).
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi atribut warna dari sekumpulan objek dan mencocokkannya dengan objek lain. Ini adalah proses pengenalan dan klasifikasi langsung berdasarkan satu atribut visual yang jelas.. Bukti: Bangun yang satu warna dengan gambar di atas.; Ketiga bangun acuan (persegi panjang, segitiga, persegi panjang) sama-sama berwarna merah muda
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep warna sebagai atribut untuk mengelompokkan benda, yang merupakan pengetahuan konseptual dasar.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya memerlukan pengamatan visual langsung terhadap satu atribut (warna). Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: Bangun yang satu warna dengan gambar di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal warna dasar dan kemampuan membandingkan atribut visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, tugas mengelompokkan berdasarkan satu atribut visual yang jelas seperti warna adalah tugas rutin yang sangat mendasar. |

Run 2 — solusi: Mengidentifikasi warna bangun di dalam kotak adalah merah muda. Memeriksa pilihan jawaban: segitiga terbalik (merah muda), persegi (ungu), oval (hijau). Hanya segitiga terbalik yang memiliki warna merah muda yang sama dengan bangun di dalam kotak.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali atribut warna (merah muda) dari sekumpulan objek dan mencocokkannya dengan pilihan yang tersedia. Ini adalah tugas pengenalan atribut dasar.. Bukti: Bangun yang satu warna dengan gambar di atas.; Ketiga bangun acuan (persegi panjang, segitiga, persegi panjang) sama-sama berwarna merah muda
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang konsep warna sebagai atribut pembeda atau pengelompokan objek, yang merupakan pengetahuan faktual dasar.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membandingkan satu atribut visual (warna) antara objek acuan dan pilihan. Tidak ada langkah perantara atau kompleksitas kognitif yang tinggi.. Bukti: Bangun yang satu warna dengan gambar di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal warna dasar dan kemampuan membandingkan atribut visual sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mencocokkan atribut visual tunggal (warna) adalah materi dasar kelas 1 yang sangat rutin dan tidak memerlukan perencanaan atau integrasi langkah. |

Run 3 — solusi: Identifikasi warna bangun di dalam kotak (merah muda). Periksa warna setiap pilihan jawaban. Pilihan D (segitiga terbalik) berwarna merah muda, sesuai dengan warna bangun di dalam kotak.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi atribut warna yang sama antara sekumpulan objek acuan dengan pilihan yang tersedia. Ini adalah tugas pengenalan dan pencocokan atribut visual langsung.. Bukti: Bangun yang satu warna dengan gambar di atas.; Ketiga bangun acuan (persegi panjang, segitiga, persegi panjang) sama-sama berwarna merah muda
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual mengenai atribut warna pada objek geometri sederhana.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pengamatan visual langsung terhadap satu atribut (warna) tanpa perlu memproses bentuk atau ukuran. Jalur penyelesaian sangat jelas.. Bukti: Bangun yang satu warna dengan gambar di atas.; Ketiga bangun acuan... sama-sama berwarna merah muda

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membedakan warna dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, tugas mengelompokkan berdasarkan satu atribut visual yang mencolok (warna) adalah tugas dasar yang rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4802`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk melakukan pengenalan atribut visual (warna) dan mencocokkannya dengan pilihan yang tersedia. Ini adalah proses kognitif tingkat dasar (knowing) karena hanya melibatkan identifikasi langsung tanpa perlu manipulasi atau penalaran kompleks.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual mengenai identifikasi warna sebagai atribut dasar benda.
- Intended difficulty `Easy`: Soal ini sangat sederhana dan rutin untuk siswa kelas 1. Tugasnya hanya membandingkan atribut warna secara visual antara objek acuan dan pilihan. Tidak ada langkah perencanaan, integrasi, atau kendala yang perlu dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal warna dasar dan kemampuan membandingkan atribut visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mencocokkan atribut visual tunggal (warna) adalah materi dasar kelas 1 yang sangat rutin dan tidak memerlukan perencanaan atau integrasi langkah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 132/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000200; applying=0.999800; reasoning=0.000000 | applying | 0.999800 | 0.001735 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.073922; conceptual=0.924775; procedural=0.001304; metacognitive=0.000000 | conceptual | 0.924775 | 0.197310 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.782116; Medium=0.213876; Hard=0.004008 | Easy | 0.782116 | 0.495356 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999800; −Σp ln(p) = 0.001906; H = 0.001906/ln(3) = 0.001735; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.924775; −Σp ln(p) = 0.273530; H = 0.273530/ln(4) = 0.197310; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.782116; −Σp ln(p) = 0.544204; H = 0.544204/ln(3) = 0.495356; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Bangun yang satu warna dengan gambar di atas.
Pilihan: A. Persegi berwarna ungu
B. Oval berwarna hijau
C. Persegi panjang berwarna biru
D. Segitiga terbalik berwarna merah muda
Transkripsi visual: Terdapat sebuah kotak berisi tiga bangun datar: persegi panjang, segitiga siku-siku, dan persegi panjang. Ketiga bangun tersebut berwarna merah muda. Di bawah kotak, terdapat tiga pilihan bangun: segitiga terbalik berwarna merah muda, persegi berwarna ungu, dan oval berwarna hijau. Pertanyaan meminta untuk memilih bangun yang memiliki warna yang sama dengan bangun di dalam kotak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `aaf396a280df35704272b0d3`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 8 |
| C | 4 |
| D | 5 |

![Gambar sumber soal 27](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengidentifikasi dan menghitung bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk lengkung yang terlihat: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah sebagai bercak pada badan anjing. Total ada 5 bentuk lengkung.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4ceba9abf5380b3258b2ea0bae2d2d0a4a8c68ca9fa503f25318db30453dc2d9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3439 |
| 2 | success | valid / verified | knowing | factual | Easy | 3388 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3445 |

Run 1 — solusi: Mengidentifikasi bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik visual tertentu (lengkung) dari sebuah gambar komposit. Ini adalah tugas pengenalan dan penghitungan langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji kemampuan siswa dalam mengenali dan membedakan atribut bentuk (lengkung vs tidak lengkung), yang merupakan pengetahuan konseptual dasar tentang bangun datar.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini bersifat langsung (counting/enumeration) dengan representasi visual yang jelas. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan, hanya ketelitian dalam menghitung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret/gambar dan membedakan bentuk dasar (lengkung vs lurus). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, menghitung objek visual yang terpisah adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Mengidentifikasi dan menghitung bentuk lengkung: 1 (hidung) + 1 (mata) + 1 (telinga) + 2 (bercak badan) = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik tertentu (lengkung) dari sebuah gambar. Ini adalah tugas pengenalan dan penghitungan langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang pengenalan bentuk geometri dasar (lengkung vs tidak lengkung).. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini bersifat langsung (menghitung objek yang terlihat). Siswa hanya perlu membedakan bentuk lengkung dari bentuk bersudut dan menghitungnya. Tidak ada langkah perencanaan kompleks atau integrasi konsep yang sulit.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan bentuk lengkung dan bentuk bersudut, serta kemampuan menghitung sampai 5. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, tugas mengidentifikasi dan menghitung objek visual sederhana adalah aktivitas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Mengidentifikasi bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik visual tertentu (lengkung) dari sekumpulan bentuk geometri. Ini adalah tugas pengenalan dan penghitungan langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep bentuk lengkung (seperti lingkaran dan oval) untuk membedakannya dari bentuk bersudut (seperti persegi atau segitiga) dalam komposisi gambar.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa menghitung objek visual yang jelas. Tidak ada langkah yang saling bergantung atau strategi kompleks. Siswa hanya perlu melakukan enumerasi sederhana terhadap bentuk yang memiliki ciri lengkung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan bentuk lengkung (lingkaran/oval) dengan bentuk bersudut (persegi/segitiga) dan kemampuan menghitung sampai 5. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung objek visual sederhana adalah standar untuk kelas 1. Tidak ada tuntutan perencanaan atau integrasi yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4881`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek dengan karakteristik visual tertentu (lengkung) dari sebuah gambar komposit. Ini adalah tugas pengenalan dan penghitungan langsung.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep bentuk lengkung (seperti lingkaran dan oval) untuk membedakannya dari bentuk bersudut (seperti persegi atau segitiga) dalam komposisi gambar.
- Intended difficulty `Easy`: Tugas ini bersifat langsung (menghitung objek yang terlihat). Siswa hanya perlu membedakan bentuk lengkung dari bentuk bersudut dan menghitungnya. Tidak ada langkah perencanaan kompleks atau integrasi konsep yang sulit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan bentuk lengkung (lingkaran/oval) dengan bentuk bersudut (persegi/segitiga) dan kemampuan menghitung sampai 5. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung objek visual sederhana adalah standar untuk kelas 1. Tidak ada tuntutan perencanaan atau integrasi yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 113/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.009901; applying=0.990099; reasoning=0.000000 | applying | 0.990099 | 0.050560 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.361225; conceptual=0.603545; procedural=0.035230; metacognitive=0.000000 | conceptual | 0.603545 | 0.570184 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873917; Medium=0.123159; Hard=0.002923 | Easy | 0.873917 | 0.357510 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.990099; −Σp ln(p) = 0.055546; H = 0.055546/ln(3) = 0.050560; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.603545; −Σp ln(p) = 0.790443; H = 0.790443/ln(4) = 0.570184; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873917; −Σp ln(p) = 0.392765; H = 0.392765/ln(3) = 0.357510; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menyusun dan Mengurai Bentuk Bangun
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
Pilihan: A. 6
B. 8
C. 4
D. 5
Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk lengkung yang terlihat: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah sebagai bercak pada badan anjing. Total ada 5 bentuk lengkung.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `595d20d8c4a6f9418dc496b0`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

| Opsi | Isi |
|---|---|
| A | 8 |
| B | 0 |
| C | 1 |
| D | 2 |

![Gambar sumber soal 28](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Mengidentifikasi bentuk-bentuk pada gambar: kepala, badan, kaki, dan leher adalah segiempat; mata dan bercak badan adalah lingkaran; telinga adalah oval; ekor adalah satu-satunya bentuk segitiga. Jumlah segitiga = 1.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri: kepala (persegi), moncong (persegi panjang), leher (persegi panjang), badan (persegi panjang), empat kaki (persegi panjang), mata (lingkaran kecil), hidung (lingkaran kecil), dua bercak pada badan (lingkaran), telinga (oval), dan ekor (segitiga). Hanya ada satu bentuk segitiga pada gambar, yaitu bagian ekor.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0e87d61ef0b74d0fa84f0a45cc9104effd3b34b4673efcc2b025223a79e17114`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3410 |
| 2 | success | valid / verified | knowing | factual | Easy | 3381 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3417 |

Run 1 — solusi: Mengidentifikasi bentuk-bentuk pada gambar: kepala, moncong, leher, badan, dan kaki adalah persegi atau persegi panjang. Telinga adalah oval. Dua lingkaran di badan adalah lingkaran. Ekor adalah satu-satunya bentuk segitiga. Jadi, jumlah segitiga adalah 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung objek dengan properti geometris tertentu (segitiga) dari sekumpulan bentuk yang berbeda. Ini adalah tugas pengenalan bentuk dasar.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang ciri-ciri bangun datar (segitiga) dan kemampuan membedakannya dari bentuk lain seperti persegi, lingkaran, dan oval.. Bukti: Segitiga ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini sangat langsung bagi siswa kelas 1. Siswa hanya perlu memindai gambar untuk mencari bentuk yang memiliki tiga sisi (segitiga). Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (segitiga, persegi, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi bentuk sederhana adalah standar untuk kelas 1. Tidak ada jebakan visual yang rumit atau tuntutan penalaran tinggi. |

Run 2 — solusi: Mengidentifikasi bentuk geometri pada gambar: kepala, badan, kaki, dan leher adalah segiempat; mata dan bercak badan adalah lingkaran; telinga adalah oval; ekor adalah satu-satunya bentuk segitiga. Jumlah segitiga = 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung bentuk geometri spesifik (segitiga) dari sekumpulan bentuk yang menyusun gambar anjing. Ini adalah tugas pengenalan bentuk dasar.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang ciri-ciri bentuk geometri dasar (segitiga) dan kemampuan untuk mengidentifikasi bentuk tersebut di antara bentuk lain.. Bukti: Segitiga ada berapa?
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu memindai gambar untuk mencari bentuk segitiga. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk geometri dasar (segitiga, lingkaran, segiempat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, mengidentifikasi bentuk geometri dasar dalam gambar komposit adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Mengidentifikasi bentuk-bentuk pada gambar: kepala (persegi), telinga (oval), badan (persegi panjang), kaki (persegi panjang), lingkaran (lingkaran), dan ekor (segitiga). Hanya ekor yang merupakan segitiga. Jumlah segitiga = 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung objek dengan karakteristik geometris tertentu (segitiga) dari sekumpulan bentuk yang berbeda. Ini adalah tugas pengenalan bentuk dasar.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi atau ciri visual dari bangun datar segitiga untuk membedakannya dari bentuk lain seperti persegi, lingkaran, atau oval.. Bukti: Segitiga ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini sederhana bagi siswa kelas 1 karena hanya memerlukan pengenalan visual langsung terhadap bentuk segitiga di antara bentuk-bentuk lain yang sangat berbeda secara visual (lingkaran, persegi). Tidak ada jebakan yang rumit atau langkah yang saling bergantung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (segitiga, persegi, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan untuk mengidentifikasi bentuk bangun datar sederhana. Tugas ini hanya meminta identifikasi visual langsung tanpa operasi hitung yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4846`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengenali dan menghitung objek dengan properti geometris tertentu (segitiga) dari sekumpulan bentuk yang berbeda. Ini adalah tugas pengenalan bentuk dasar yang bersifat langsung.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual tentang ciri-ciri bangun datar (segitiga) dan kemampuan membedakannya dari bentuk lain seperti persegi, lingkaran, dan oval.
- Intended difficulty `Easy`: Tugas ini sangat langsung bagi siswa kelas 1. Siswa hanya perlu memindai gambar untuk mencari bentuk yang memiliki tiga sisi (segitiga). Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (segitiga, persegi, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi bentuk sederhana adalah standar untuk kelas 1. Tidak ada jebakan visual yang rumit atau tuntutan penalaran tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 145/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000993; applying=0.999007; reasoning=0.000000 | applying | 0.999007 | 0.007152 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.037001; conceptual=0.952683; procedural=0.010315; metacognitive=0.000000 | conceptual | 0.952683 | 0.155342 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.813996; Medium=0.182606; Hard=0.003398 | Easy | 0.813996 | 0.452702 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999007; −Σp ln(p) = 0.007858; H = 0.007858/ln(3) = 0.007152; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.952683; −Σp ln(p) = 0.215349; H = 0.215349/ln(4) = 0.155342; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.813996; −Σp ln(p) = 0.497344; H = 0.497344/ln(3) = 0.452702; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menyusun dan Mengurai Bentuk Bangun
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
Pilihan: A. 8
B. 0
C. 1
D. 2
Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri: kepala (persegi), moncong (persegi panjang), leher (persegi panjang), badan (persegi panjang), empat kaki (persegi panjang), mata (lingkaran kecil), hidung (lingkaran kecil), dua bercak pada badan (lingkaran), telinga (oval), dan ekor (segitiga). Hanya ada satu bentuk segitiga pada gambar, yaitu bagian ekor.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `4d125a6ed9a2701db41cdcd1`

Isilah dengan bilangan yang benar.<br><br>10 ditambah 3 menjadi ....

| Opsi | Isi |
|---|---|
| A | 14 |
| B | 12 |
| C | 31 |
| D | 13 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 10 + 3 = 13
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `77f3a2e1b230dac593d46f2821f8035288f386534c17bb656fddd549f2170427`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2142 |
| 2 | success | valid / verified | knowing | factual | Easy | 2156 |
| 3 | success | valid / verified | knowing | factual | Easy | 2159 |

Run 1 — solusi: 10 + 3 = 13
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang sangat langsung (10+3). Ini adalah prosedur rutin yang sudah dipelajari di kelas 1.. Bukti: 10 ditambah 3 menjadi ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta bilangan dan operasi penjumlahan dasar (fakta dasar matematika).. Bukti: 10 ditambah 3 menjadi ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung. Tidak ada langkah tambahan atau kendala yang harus dipecahkan.. Bukti: 10 ditambah 3 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 10 dengan satuan adalah materi inti kelas 1 yang bersifat prosedural langsung tanpa memerlukan perencanaan kompleks. |

Run 2 — solusi: 10 + 3 = 13
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi penjumlahan dasar yang sangat langsung. Siswa hanya perlu mengenali konsep penambahan bilangan 10 dengan satuan 3 untuk membentuk bilangan belasan.. Bukti: 10 ditambah 3 menjadi ....
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami konsep nilai tempat dan simbol bilangan (13) sebagai hasil dari 10 dan 3.. Bukti: 10 ditambah 3 menjadi ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar yang sangat familiar bagi siswa kelas 1. Tidak ada langkah perencanaan atau kendala yang perlu dipecahkan.. Bukti: 10 ditambah 3 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan 1-20 dan operasi penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 10 dengan satuan adalah materi dasar kelas 1 yang rutin dan langsung. |

Run 3 — solusi: 10 + 3 = 13
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi penjumlahan dasar yang sudah dipelajari di kelas 1. Siswa hanya perlu mengingat fakta penjumlahan atau menghitung maju dari 10.. Bukti: 10 ditambah 3 menjadi ....
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang konsep bilangan dan operasi penjumlahan dasar (fakta numerik).. Bukti: 10 ditambah 3 menjadi ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar satu langkah yang sangat familiar bagi siswa kelas 1. Tidak ada kendala atau perencanaan kompleks yang diperlukan.. Bukti: 10 ditambah 3 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan 1-20 dan operasi penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar kompetensi kelas 1 untuk penjumlahan bilangan dasar. Tidak ada tuntutan kognitif tambahan selain mengingat fakta penjumlahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999968; applying=0.000032; reasoning=0.000000 | knowing | 0.999968 | 0.000334 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.625335; conceptual=0.350270; procedural=0.024395; metacognitive=0.000000 | factual | 0.625335 | 0.542174 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.893777; Medium=0.103965; Hard=0.002258 | Easy | 0.893777 | 0.318108 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999968; −Σp ln(p) = 0.000367; H = 0.000367/ln(3) = 0.000334; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.625335; −Σp ln(p) = 0.751613; H = 0.751613/ln(4) = 0.542174; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.893777; −Σp ln(p) = 0.349477; H = 0.349477/ln(3) = 0.318108; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah dengan bilangan yang benar.

10 ditambah 3 menjadi ....
Pilihan: A. 14
B. 12
C. 31
D. 13
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `fbc23bca48392d3c678c3beb`

Isilah titik-titik berikut.<br><br>8 ditambah 10 menjadi ....

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 810 |
| C | 19 |
| D | 17 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 8 + 10 = 18
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `667035e13b735c918c39e19b21873fbd258cd37da96268770759705296775828`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2035 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2033 |
| 3 | success | valid / verified | knowing | factual | Easy | 2055 |

Run 1 — solusi: 8 + 10 = 18
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar dua bilangan (satu digit dan dua digit) yang merupakan prosedur rutin bagi kelas 1.. Bukti: 8 ditambah 10 menjadi ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan dasar (prosedural) yang sudah dipelajari di kelas 1.. Bukti: 8 ditambah 10 menjadi ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan langsung tanpa konteks cerita atau langkah tambahan. Siswa hanya perlu menjumlahkan dua bilangan yang diberikan.. Bukti: 8 ditambah 10 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan penjumlahan dasar hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 8+10 adalah materi dasar kelas 1 yang bersifat langsung dan rutin. |

Run 2 — solusi: 8 + 10 = 18
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur langsung dan familiar bagi kelas 1.. Bukti: 8 ditambah 10 menjadi ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang operasi penjumlahan dasar (algoritme penjumlahan sederhana).. Bukti: 8 ditambah 10 menjadi ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan satu langkah yang sangat mendasar. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks. Siswa hanya perlu menerapkan fakta penjumlahan dasar.. Bukti: 8 ditambah 10 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan nilai tempat bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 8+10 adalah standar kompetensi kelas 1 yang bersifat rutin dan langsung. |

Run 3 — solusi: 8 + 10 = 18
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur langsung. Tidak ada strategi nonrutin atau integrasi hubungan yang kompleks.. Bukti: 8 ditambah 10 menjadi ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta penjumlahan dasar (bilangan 8 dan 10) yang merupakan elemen dasar dalam aritmatika.. Bukti: 8 ditambah 10 menjadi ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan satu langkah yang sangat familiar bagi siswa kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: 8 ditambah 10 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan cacah sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 8+10 adalah standar kompetensi kelas 1. Soal bersifat langsung tanpa jebakan atau tuntutan kognitif tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3257`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang bersifat langsung dan rutin, yang termasuk dalam kategori knowing.
- Dimensi pengetahuan `procedural`: Soal ini menguji kemampuan siswa dalam menerapkan algoritma atau prosedur penjumlahan dasar.
- Intended difficulty `Easy`: Soal ini adalah operasi penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman penjumlahan dasar bilangan cacah hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 8+10 adalah materi standar kelas 1 yang bersifat langsung dan rutin tanpa tuntutan kognitif tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999973; applying=0.000027; reasoning=0.000000 | knowing | 0.999973 | 0.000287 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.593649; conceptual=0.387587; procedural=0.018764; metacognitive=0.000000 | factual | 0.593649 | 0.542116 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.895874; Medium=0.102022; Hard=0.002103 | Easy | 0.895874 | 0.313435 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999973; −Σp ln(p) = 0.000316; H = 0.000316/ln(3) = 0.000287; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.593649; −Σp ln(p) = 0.751532; H = 0.751532/ln(4) = 0.542116; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.895874; −Σp ln(p) = 0.344344; H = 0.344344/ln(3) = 0.313435; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik berikut.

8 ditambah 10 menjadi ....
Pilihan: A. 18
B. 810
C. 19
D. 17
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `4953bd9e508059b6896af5e5`

Isilah titik-titik berikut.<br><br>15, 14, ...., ....

| Opsi | Isi |
|---|---|
| A | 14, 13 |
| B | 16, 17 |
| C | 12, 13 |
| D | 13, 12 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola bilangan adalah menghitung mundur dengan selisih 1. Setelah 15 dan 14, angka berikutnya adalah 13 dan 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `62312b879b74ad75dafeb1df791dc8857d049e97e72ad48662c40cc6a1dc8eb7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2228 |
| 2 | success | valid / verified | knowing | factual | Easy | 2210 |
| 3 | success | valid / verified | applying | procedural | Easy | 2252 |

Run 1 — solusi: Pola bilangan adalah pengurangan 1 secara berurutan (menghitung mundur). Setelah 15 dan 14, angka berikutnya adalah 13 dan 12.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali pola urutan bilangan (menghitung mundur) dan melanjutkan pola tersebut. Ini adalah prosedur langsung yang familiar bagi siswa kelas 1.. Bukti: 15, 14, ...., ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang urutan bilangan (fakta/konsep dasar) dan penerapan prosedur menghitung mundur.. Bukti: 15, 14, ...., ....
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi aturan pengurangan 1 dan menerapkannya. Tidak ada keputusan strategi yang kompleks atau kendala yang berinteraksi.. Bukti: 15, 14, ...., ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan mundur adalah materi dasar kelas 1. Soal ini tidak menuntut perencanaan atau integrasi konsep yang sulit. |

Run 2 — solusi: Pola bilangan adalah urutan mundur (dikurangi 1). Setelah 15 dan 14, angka berikutnya adalah 13 dan 12.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali pola urutan bilangan mundur dan melanjutkannya. Ini adalah tugas mengenali dan menjalankan prosedur yang sangat langsung.. Bukti: 15, 14, ...., ....
- Dimensi pengetahuan `classify/factual`: Siswa menggunakan pengetahuan faktual tentang urutan bilangan dan konsep dasar menghitung mundur.. Bukti: 15, 14, ...., ....
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi pola pengurangan 1 (menghitung mundur) dan menerapkannya. Tidak ada keputusan strategi yang kompleks atau kendala yang berinteraksi.. Bukti: 15, 14, ...., ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, mengenali urutan bilangan mundur adalah materi dasar yang rutin. |

Run 3 — solusi: Pola bilangan adalah pengurangan 1 secara berurutan (menghitung mundur). Setelah 15 dan 14, angka berikutnya adalah 15-1=13 dan 13-1=12.
- Domain kognitif `classify/applying`: Siswa diminta mengenali pola urutan bilangan mundur dan melanjutkan prosedur tersebut. Ini adalah penerapan langsung dari pemahaman urutan bilangan yang sudah dipelajari di kelas 1.. Bukti: 15, 14, ...., ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang urutan bilangan (menghitung mundur) yang merupakan algoritma dasar dalam berhitung.. Bukti: 15, 14, ...., ....
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi pola pengurangan 1 dan menerapkannya. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: 15, 14, ...., ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, pola urutan bilangan mundur adalah materi dasar yang sering dilatih. Soal ini tidak menuntut perencanaan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3473`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta mengenali pola urutan bilangan mundur dan melanjutkannya. Ini adalah tugas rutin yang memerlukan pengenalan pola dasar dan penerapan prosedur menghitung mundur yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang urutan bilangan mundur, yang merupakan algoritma dasar dalam berhitung.
- Intended difficulty `Easy`: Soal ini sangat langsung dan rutin. Siswa hanya perlu mengidentifikasi pola pengurangan 1 dan menerapkannya. Tidak ada keputusan strategi yang kompleks atau kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan mundur adalah materi dasar kelas 1. Soal ini tidak menuntut perencanaan atau integrasi konsep yang sulit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 76/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999985; applying=0.000015; reasoning=0.000000 | knowing | 0.999985 | 0.000164 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.880450; conceptual=0.106302; procedural=0.013248; metacognitive=0.000000 | factual | 0.880450 | 0.294062 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.913496; Medium=0.084560; Hard=0.001944 | Easy | 0.913496 | 0.276417 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999985; −Σp ln(p) = 0.000180; H = 0.000180/ln(3) = 0.000164; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.880450; −Σp ln(p) = 0.407656; H = 0.407656/ln(4) = 0.294062; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.913496; −Σp ln(p) = 0.303675; H = 0.303675/ln(3) = 0.276417; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik berikut.

15, 14, ...., ....
Pilihan: A. 14, 13
B. 16, 17
C. 12, 13
D. 13, 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `02bd8bfdfd682bd80aa5f426`

Lengkapi urutan bilangan berikut.<br><br>20, ...., 18

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 19 |
| C | 21 |
| D | 17 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Jadi, bilangan yang hilang adalah 19.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d26a061984693522082604f6e3e0b96fa4f8b42385e315c65a35085ee683b1f6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2078 |
| 2 | success | valid / verified | knowing | factual | Easy | 2181 |
| 3 | success | valid / verified | knowing | factual | Easy | 2051 |

Run 1 — solusi: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Jadi, bilangan yang hilang adalah 19.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali pola urutan bilangan mundur sederhana (20, 19, 18) yang merupakan prosedur langsung dalam materi kelas 1.. Bukti: Lengkapi urutan bilangan berikut. 20, ...., 18
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta numerik) dalam rentang bilangan cacah sampai 20.. Bukti: 20, ...., 18
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengenalan urutan mundur satu langkah antara dua bilangan yang berdekatan (20 dan 18). Tidak ada perencanaan kompleks atau kendala yang berinteraksi.. Bukti: 20, ...., 18

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang mundur 20 sampai 1. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah mempelajari urutan bilangan sampai 20. Soal ini adalah latihan rutin yang sangat mendasar. |

Run 2 — solusi: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Bilangan yang hilang adalah 19.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali pola urutan bilangan mundur sederhana (20, 19, 18) dan mengisi bilangan yang hilang. Ini adalah prosedur langsung yang sudah dipelajari di kelas 1.. Bukti: Lengkapi urutan bilangan berikut. 20, ...., 18
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta numerik) dan pola urutan mundur yang merupakan konsep dasar bilangan.. Bukti: 20, ...., 18
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 1 karena hanya memerlukan pengenalan urutan bilangan mundur satu langkah. Tidak ada perencanaan kompleks atau kendala yang berinteraksi.. Bukti: 20, ...., 18

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa dengan urutan bilangan mundur 20-1. Soal ini adalah latihan rutin yang sangat mendasar. |

Run 3 — solusi: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Jadi bilangan yang hilang adalah 19.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan mundur (counting backward) yang sangat dasar dan langsung, yang merupakan prosedur rutin di kelas 1.. Bukti: Lengkapi urutan bilangan berikut.; 20, ...., 18
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta numerik dasar) dalam konteks berhitung mundur.. Bukti: 20, ...., 18
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengisian satu angka dalam urutan mundur yang familiar bagi siswa kelas 1. Tidak ada perencanaan kompleks atau kendala yang berinteraksi.. Bukti: 20, ...., 18

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang mundur 20 sampai 1. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengisi satu angka di antara dua bilangan berurutan (20 dan 18) adalah tugas standar kelas 1 yang tidak menuntut perencanaan tinggi. |

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
| Domain kognitif | knowing=0.999999; applying=0.000001; reasoning=0.000000 | knowing | 0.999999 | 0.000009 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.855945; conceptual=0.130357; procedural=0.013698; metacognitive=0.000000 | factual | 0.855945 | 0.330025 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.916232; Medium=0.081517; Hard=0.002250 | Easy | 0.916232 | 0.271466 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000010; H = 0.000010/ln(3) = 0.000009; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.855945; −Σp ln(p) = 0.457512; H = 0.457512/ln(4) = 0.330025; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.916232; −Σp ln(p) = 0.298235; H = 0.298235/ln(3) = 0.271466; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi urutan bilangan berikut.

20, ...., 18
Pilihan: A. 18
B. 19
C. 21
D. 17
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `fb13c7e49793c36315b9e324`

Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.<br><br>.... puluhan dan .... satuan = ....

| Opsi | Isi |
|---|---|
| A | 1 puluhan dan 5 satuan = 15 |
| B | 0 puluhan dan 15 satuan = 15 |
| C | 1 puluhan dan 6 satuan = 16 |
| D | 1 puluhan dan 4 satuan = 14 |

![Gambar sumber soal 33](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0175-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Gambar menunjukkan 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan). Jadi, 1 puluhan dan 5 satuan sama dengan 15.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0175-03.png. Transkripsi visual: Gambar menunjukkan satu wadah berisi 10 telur (satu kelompok puluhan) dan 5 telur lepas di sampingnya. Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan', serta kalimat rumpang '.... puluhan dan .... satuan = ....'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0e7cc2d9afce85ea568cee35c61e7cad97696776e4fc80c77817bde5441a753c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3525 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3467 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3482 |

Run 1 — solusi: Gambar menunjukkan 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan). Jadi, 1 puluhan dan 5 satuan sama dengan 15.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengelompokkan objek konkret ke dalam konsep nilai tempat (puluhan dan satuan). Ini adalah penerapan langsung dari konsep nilai tempat yang sudah dipelajari di kelas 1.. Bukti: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.; 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana angka dibentuk dari pengelompokan puluhan dan satuan.. Bukti: 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung jumlah kelompok puluhan dan jumlah satuan yang terlihat jelas pada gambar. Tidak ada langkah perencanaan yang kompleks atau kendala yang saling berinteraksi.. Bukti: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.; 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 10 sebagai satu puluhan dan menghitung benda sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, mengelompokkan benda konkret menjadi puluhan dan satuan adalah materi standar yang familiar. Soal memberikan representasi visual yang jelas tanpa jebakan. |

Run 2 — solusi: Gambar menunjukkan 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan), sehingga totalnya adalah 15.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengelompokkan objek konkret ke dalam konsep nilai tempat (puluhan dan satuan). Ini adalah penerapan langsung dari konsep nilai tempat yang sudah dipelajari.. Bukti: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.; 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana angka dibentuk dari kelompok puluhan dan satuan.. Bukti: 1 puluhan dan 5 satuan = 15
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menghitung kelompok puluhan dan satuan yang sudah terlihat jelas secara visual. Tidak ada langkah rumit atau strategi non-rutin yang diperlukan.. Bukti: 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang angka 1-20 dan konsep pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan konsep nilai tempat menggunakan benda konkret atau gambar. Soal ini adalah latihan standar yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Gambar menunjukkan 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan). Jadi, 1 puluhan dan 5 satuan = 15.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengelompokkan objek konkret ke dalam konsep nilai tempat (puluhan dan satuan). Ini adalah penerapan langsung dari konsep nilai tempat yang sudah dipelajari.. Bukti: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.; 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana angka dibentuk dari pengelompokan puluhan dan satuan.. Bukti: 1 puluhan dan 5 satuan = 15
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menghitung jumlah kelompok puluhan dan sisa satuan yang terlihat jelas secara visual. Tidak ada langkah rumit atau strategi non-rutin yang diperlukan.. Bukti: 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep 10 sebagai satu puluhan dan menghitung benda hingga 20. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, mengelompokkan benda konkret menjadi puluhan dan satuan adalah materi standar yang rutin. Soal menyediakan representasi visual yang jelas tanpa kendala yang saling bertentangan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 152/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.001831; conceptual=0.980792; procedural=0.017377; metacognitive=0.000000 | conceptual | 0.980792 | 0.072846 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.713947; Medium=0.280144; Hard=0.005909 | Easy | 0.713947 | 0.571041 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.980792; −Σp ln(p) = 0.100985; H = 0.100985/ln(4) = 0.072846; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.713947; −Σp ln(p) = 0.627353; H = 0.627353/ln(3) = 0.571041; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Nilai Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.

.... puluhan dan .... satuan = ....
Pilihan: A. 1 puluhan dan 5 satuan = 15
B. 0 puluhan dan 15 satuan = 15
C. 1 puluhan dan 6 satuan = 16
D. 1 puluhan dan 4 satuan = 14
Transkripsi visual: Gambar menunjukkan satu wadah berisi 10 telur (satu kelompok puluhan) dan 5 telur lepas di sampingnya. Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan', serta kalimat rumpang '.... puluhan dan .... satuan = ....'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `daa41e2808537d493a6c0994`

Hitunglah dan isi tabelnya.<br><br>Nilai tempat 14 = .... puluhan dan .... satuan

| Opsi | Isi |
|---|---|
| A | 1 puluhan dan 4 satuan |
| B | 1 puluhan dan 3 satuan |
| C | 4 puluhan dan 1 satuan |
| D | 0 puluhan dan 14 satuan |

![Gambar sumber soal 34](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0175-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Gambar menunjukkan 1 ikat berisi 10 pensil (1 puluhan) dan 4 pensil lepas (4 satuan). Jadi, 14 adalah 1 puluhan dan 4 satuan.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0175-04.png. Transkripsi visual: Gambar menunjukkan satu ikat pensil yang berisi 10 pensil dan 4 pensil lepas di sampingnya. Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan' yang mengarah ke gambar tersebut. Teks di bawahnya berbunyi 'Nilai tempat 14 = .... puluhan dan .... satuan'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d7c3b4a9de92a637c8b3489ce4258f7952975ad481d4a3983807a5b2a02581df`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3407 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3459 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3386 |

Run 1 — solusi: Angka 14 terdiri dari 1 puluhan (10) dan 4 satuan. Gambar menunjukkan 1 ikatan (10) dan 4 pensil lepas, sehingga 1 puluhan dan 4 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali dan menerapkan konsep nilai tempat dasar (puluhan dan satuan) pada bilangan 14 yang direpresentasikan secara visual. Ini adalah prosedur langsung yang familiar.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar dalam sistem bilangan.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi jumlah puluhan dan satuan dari angka 14 yang sudah divisualisasikan dengan jelas (1 ikatan dan 4 lepas). Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang angka 1-20 dan konsep pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, mengidentifikasi nilai tempat dari representasi visual (ikatan 10 dan satuan) adalah materi standar yang bersifat rutin dan langsung. |

Run 2 — solusi: Angka 14 terdiri dari 1 puluhan (10) dan 4 satuan (4). Sesuai dengan gambar, terdapat 1 ikat berisi 10 pensil dan 4 pensil lepas.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari bilangan 14 berdasarkan representasi visual (benda konkret yang dikelompokkan). Ini adalah prosedur langsung yang sudah dipelajari di kelas 1.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan; Gambar menunjukkan satu ikat pensil berisi 10 buah dan 4 pensil lepas
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat (puluhan dan satuan) sebagai struktur dasar bilangan dua angka.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1. Siswa hanya perlu mengenali representasi visual dari 10 sebagai satu puluhan dan sisanya sebagai satuan. Tidak ada langkah rumit atau integrasi konsep yang sulit.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan; Gambar menunjukkan satu ikat pensil berisi 10 buah dan 4 pensil lepas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang menghitung benda sampai 20 dan pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai pengenalan nilai tempat bilangan cacah sampai 20 menggunakan benda konkret. |

Run 3 — solusi: Angka 14 terdiri dari 1 puluhan (10) dan 4 satuan. Gambar menunjukkan 1 ikat (10) dan 4 pensil lepas, sehingga 1 puluhan dan 4 satuan.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi nilai tempat dari bilangan 14 berdasarkan representasi visual (pengelompokan benda). Ini adalah tugas mengenali dan menerapkan prosedur dasar nilai tempat yang sudah dipelajari.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep nilai tempat (puluhan dan satuan) sebagai struktur dasar bilangan.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah ikat (puluhan) dan satuan yang terlihat jelas pada gambar. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep puluhan dan satuan serta kemampuan menghitung benda konkret. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, mengidentifikasi nilai tempat dari representasi visual benda konkret adalah materi standar yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4808`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengenali dan membaca representasi visual (pengelompokan benda) untuk menentukan nilai tempat. Ini adalah prosedur langsung yang sangat familiar bagi siswa kelas 1.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep dasar nilai tempat (puluhan dan satuan) dalam sistem bilangan.
- Intended difficulty `Easy`: Soal ini sangat mendasar dan rutin. Siswa hanya perlu mengamati gambar yang sudah dikelompokkan (1 ikat = 1 puluhan, 4 lepas = 4 satuan) dan mengisi titik-titik. Tidak ada langkah perencanaan atau integrasi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang angka 1-20 dan konsep pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, mengidentifikasi nilai tempat dari representasi visual (ikatan 10 dan satuan) adalah materi standar yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 138/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000017 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.002054; conceptual=0.994720; procedural=0.003226; metacognitive=0.000000 | conceptual | 0.994720 | 0.026317 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.690463; Medium=0.303471; Hard=0.006066 | Easy | 0.690463 | 0.590371 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000019; H = 0.000019/ln(3) = 0.000017; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.994720; −Σp ln(p) = 0.036483; H = 0.036483/ln(4) = 0.026317; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.690463; −Σp ln(p) = 0.648589; H = 0.648589/ln(3) = 0.590371; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Nilai Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah dan isi tabelnya.

Nilai tempat 14 = .... puluhan dan .... satuan
Pilihan: A. 1 puluhan dan 4 satuan
B. 1 puluhan dan 3 satuan
C. 4 puluhan dan 1 satuan
D. 0 puluhan dan 14 satuan
Transkripsi visual: Gambar menunjukkan satu ikat pensil yang berisi 10 pensil dan 4 pensil lepas di sampingnya. Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan' yang mengarah ke gambar tersebut. Teks di bawahnya berbunyi 'Nilai tempat 14 = .... puluhan dan .... satuan'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `76bd2315ce21573dfa2ea8d7`

Perhatikan bilangan berikut. 13 11 18<br><br>Urutan mulai dari bilangan terkecil: .... , .... , ....

| Opsi | Isi |
|---|---|
| A | 13, 11, 18 |
| B | 11, 13, 18 |
| C | 11, 18, 13 |
| D | 18, 13, 11 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan nilai 13, 11, dan 18. Karena 11 < 13 < 18, urutan dari terkecil adalah 11, 13, 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cbf351e564622ca3c311c3280d40f2a55aea0dac280af05bf50ccc08a2998dee`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2919 |
| 2 | success | valid / verified | applying | procedural | Easy | 2326 |
| 3 | success | valid / verified | applying | procedural | Easy | 2156 |

Run 1 — solusi: Membandingkan nilai 13, 11, dan 18. Karena 11 < 13 < 18, urutan dari terkecil adalah 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep perbandingan bilangan untuk mengurutkan tiga bilangan yang diberikan. Ini adalah penerapan prosedur standar.. Bukti: Urutan mulai dari bilangan terkecil: .... , .... , ....
- Dimensi pengetahuan `classify/conceptual`: Memahami konsep urutan bilangan (magnitude) merupakan pemahaman konseptual dasar.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini meminta pengurutan tiga bilangan yang familiar bagi siswa kelas 1. Jalur penyelesaian langsung (membandingkan nilai) tanpa kendala tambahan.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat puluhan dan satuan atau urutan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan adalah tugas rutin kelas 1 yang tidak memerlukan perencanaan kompleks atau integrasi kendala. |

Run 2 — solusi: Membandingkan nilai puluhan dan satuan dari 13, 11, dan 18. Ketiganya memiliki puluhan yang sama (1). Membandingkan satuan: 1 < 3 < 8. Maka urutan dari terkecil adalah 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan tiga bilangan dua angka berdasarkan nilai tempatnya. Ini adalah penerapan prosedur membandingkan bilangan yang sudah dipelajari di kelas 1.. Bukti: Urutan mulai dari bilangan terkecil: .... , .... , ....; 13 11 18
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengurutkan bilangan dua angka dengan membandingkan nilai tempat puluhan dan satuan.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan tiga bilangan dua angka yang familiar bagi siswa kelas 1. Prosedur pengurutan bersifat langsung tanpa kendala yang saling berinteraksi atau kebutuhan strategi nonrutin.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan 11-20 dan membandingkan dua bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah tugas standar kelas 1. Tidak ada jebakan atau kompleksitas tambahan. |

Run 3 — solusi: Membandingkan nilai tempat puluhan (semua 1) dan satuan (3, 1, 8). Urutan satuan dari terkecil adalah 1, 3, 8. Maka urutan bilangan adalah 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur membandingkan dan mengurutkan bilangan dua angka yang sudah dipelajari di kelas 1.. Bukti: Urutan mulai dari bilangan terkecil: .... , .... , ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengurutkan bilangan berdasarkan nilai tempat.. Bukti: 13 11 18
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas rutin bagi siswa kelas 1 untuk mengurutkan tiga bilangan dua angka. Jalur penyelesaiannya jelas (membandingkan nilai satuan karena puluhan sama) dan tidak memerlukan strategi kompleks.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan dua angka (puluhan dan satuan) dan perbandingan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah standar kompetensi kelas 1 yang bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3657`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur perbandingan bilangan yang sudah dipelajari untuk mengurutkan tiga bilangan. Ini adalah tugas rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara mengurutkan bilangan dua angka dengan membandingkan nilai tempat.
- Intended difficulty `Easy`: Tugas ini sangat rutin untuk kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan kompleks; siswa hanya perlu membandingkan nilai bilangan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan 11-20 dan membandingkan dua bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah standar kompetensi kelas 1 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 89/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.998339; applying=0.001661; reasoning=0.000000 | knowing | 0.998339 | 0.011189 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.271071; conceptual=0.706599; procedural=0.022330; metacognitive=0.000000 | conceptual | 0.706599 | 0.493503 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.866569; Medium=0.130640; Hard=0.002792 | Easy | 0.866569 | 0.369935 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998339; −Σp ln(p) = 0.012293; H = 0.012293/ln(3) = 0.011189; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.706599; −Σp ln(p) = 0.684140; H = 0.684140/ln(4) = 0.493503; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.866569; −Σp ln(p) = 0.406415; H = 0.406415/ln(3) = 0.369935; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bilangan berikut. 13 11 18

Urutan mulai dari bilangan terkecil: .... , .... , ....
Pilihan: A. 13, 11, 18
B. 11, 13, 18
C. 11, 18, 13
D. 18, 13, 11
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `84e373946789a200e6b5203a`

Malosi mempunyai 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.<br><br>Urutan banyak bola dari yang terkecil: .... , .... , ....

| Opsi | Isi |
|---|---|
| A | 13, 11, 10 |
| B | 10, 13, 11 |
| C | 11, 10, 13 |
| D | 10, 11, 13 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Membandingkan nilai 13, 11, dan 10. Urutan dari yang terkecil adalah 10, 11, 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6cc73538f9871c4c92bc451acdf922044131acf16b15e73ca719adc92f9a7df8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2284 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2290 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2324 |

Run 1 — solusi: Membandingkan nilai bilangan 13, 11, dan 10. Urutan dari yang terkecil adalah 10 < 11 < 13.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengurutkan tiga bilangan yang diberikan (13, 11, 10) dari yang terkecil. Ini adalah prosedur rutin yang langsung menggunakan pemahaman nilai tempat atau urutan bilangan yang sudah dipelajari di kelas 1.. Bukti: Urutan banyak bola dari yang terkecil: .... , .... , ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang urutan bilangan (konsep dasar bilangan) yang merupakan pengetahuan konseptual dasar.. Bukti: Malosi mempunyai 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.
- Intended difficulty `classify/Easy`: Soal ini meminta pengurutan tiga bilangan yang sudah diketahui nilainya. Tidak ada kendala tambahan atau langkah perantara yang kompleks. Siswa hanya perlu membandingkan 10, 11, dan 13.. Bukti: Urutan banyak bola dari yang terkecil: .... , .... , ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami urutan bilangan cacah sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan adalah tugas standar kelas 1 yang bersifat langsung dan rutin. |

Run 2 — solusi: Bandingkan nilai bilangan 13, 11, dan 10. Urutan dari yang terkecil adalah 10 < 11 < 13.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan tiga bilangan yang diberikan dari yang terkecil ke terbesar. Ini adalah prosedur rutin yang melibatkan pemahaman nilai tempat atau urutan bilangan dasar yang sudah dipelajari di kelas 1.. Bukti: Urutan banyak bola dari yang terkecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan bilangan (magnitude) dan perbandingan nilai.. Bukti: 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya meminta pengurutan tiga bilangan bulat positif yang familiar bagi siswa kelas 1. Tidak ada kendala tambahan atau langkah kompleks yang diperlukan.. Bukti: Urutan banyak bola dari yang terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membandingkan dua bilangan cacah sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan adalah tugas standar kelas 1. Tidak ada jebakan atau langkah yang saling bergantung yang membuat soal ini sulit. |

Run 3 — solusi: Membandingkan nilai bilangan 13, 11, dan 10. Mengurutkan dari yang terkecil: 10 < 11 < 13. Urutan yang benar adalah 10, 11, 13.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan tiga bilangan yang diberikan (13, 11, 10) dari yang terkecil. Ini adalah penerapan langsung dari konsep perbandingan bilangan yang sudah dipelajari di kelas 1.. Bukti: Urutan banyak bola dari yang terkecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan bilangan (magnitude) dan bagaimana membandingkan nilai-nilai tersebut.. Bukti: 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan pengurutan tiga bilangan bulat positif yang familiar bagi siswa kelas 1. Tidak ada kendala tambahan atau langkah yang kompleks.. Bukti: Urutan banyak bola dari yang terkecil: .... , .... , ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat dan perbandingan bilangan cacah sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan adalah tugas standar kelas 1. Tidak ada jebakan atau kompleksitas tambahan yang membuat soal ini sulit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3677`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengurutkan tiga bilangan yang diberikan (13, 11, 10) dari yang terkecil. Ini adalah prosedur rutin yang langsung menggunakan pemahaman urutan bilangan yang sudah dipelajari di kelas 1.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang urutan bilangan (magnitude) yang merupakan pengetahuan konseptual dasar.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya meminta pengurutan tiga bilangan bulat positif yang familiar bagi siswa kelas 1. Tidak ada kendala tambahan atau langkah perantara yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami urutan bilangan cacah sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan adalah tugas standar kelas 1 yang bersifat langsung dan rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 99/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.039129; applying=0.960871; reasoning=0.000000 | applying | 0.960871 | 0.150341 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.241632; conceptual=0.735878; procedural=0.022490; metacognitive=0.000000 | conceptual | 0.735878 | 0.471927 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.878514; Medium=0.118864; Hard=0.002623 | Easy | 0.878514 | 0.348194 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.960871; −Σp ln(p) = 0.165166; H = 0.165166/ln(3) = 0.150341; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.735878; −Σp ln(p) = 0.654230; H = 0.654230/ln(4) = 0.471927; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.878514; −Σp ln(p) = 0.382531; H = 0.382531/ln(3) = 0.348194; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Malosi mempunyai 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.

Urutan banyak bola dari yang terkecil: .... , .... , ....
Pilihan: A. 13, 11, 10
B. 10, 13, 11
C. 11, 10, 13
D. 10, 11, 13
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `31e0c54a133ed9b166d1ed06`

Malosi mempunyai 5 kelereng. Halim mempunyai 2 kelereng lebihnya dari Malosi.<br><br>Berapakah selisih banyak kelereng Halim dan Malosi?

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 9 |
| C | 5 |
| D | 2 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Kelereng Malosi = 5. Kelereng Halim = 5 + 2 = 7. Selisih = 7 - 5 = 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f952ac18255d2f8027b25dacae02dd43b6017e6da7ffdeeb08fa991304b6991`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2316 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2365 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2338 |

Run 1 — solusi: Kelereng Malosi = 5. Kelereng Halim = 5 + 2 = 7. Selisih = 7 - 5 = 2.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan 'lebihnya dari' untuk menentukan jumlah kelereng Halim, kemudian menerapkan konsep selisih. Ini melibatkan penerapan prosedur pada konteks cerita rutin.. Bukti: Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih banyak kelereng Halim dan Malosi?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang hubungan 'lebih dari' dan 'selisih' dalam konteks bilangan.. Bukti: 2 kelereng lebihnya dari Malosi; selisih banyak kelereng
- Intended difficulty `classify/Medium`: Soal ini Medium bagi kelas 1 karena memerlukan dua langkah yang saling bergantung: menentukan jumlah kelereng Halim (5+2=7) sebelum menghitung selisih (7-5=2). Meskipun prosedurnya familiar, siswa harus mengelola dua informasi yang berinteraksi.. Bukti: Malosi mempunyai 5 kelereng; Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar sampai 10 dan pemahaman konsep selisih. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Untuk kelas 1, melakukan dua langkah (menentukan nilai variabel kedua lalu mencari selisih) merupakan tuntutan kognitif yang wajar untuk kategori Medium. |

Run 2 — solusi: Banyak kelereng Malosi = 5. Banyak kelereng Halim = 5 + 2 = 7. Selisih kelereng Halim dan Malosi = 7 - 5 = 2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep selisih dan hubungan 'lebih dari' untuk menentukan jumlah kelereng Halim terlebih dahulu sebelum menghitung selisihnya. Ini melibatkan pemilihan prosedur yang tepat dalam konteks rutin.. Bukti: Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih banyak kelereng Halim dan Malosi?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan 'lebih dari' dan konsep selisih sebagai perbandingan dua kuantitas.. Bukti: 5 kelereng; 2 kelereng lebihnya; selisih
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 1 harus melakukan dua langkah berurutan: menentukan jumlah kelereng Halim (5+2=7) dan kemudian menghitung selisihnya (7-5=2). Meskipun prosedurnya familiar, terdapat ketergantungan langkah yang memerlukan perencanaan sederhana.. Bukti: Malosi mempunyai 5 kelereng; Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar sampai 10 dan pemahaman konsep perbandingan selisih. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, melakukan dua langkah (menentukan nilai variabel kedua lalu mencari selisih) merupakan tuntutan yang sesuai untuk tingkat Medium, karena memerlukan pemahaman urutan operasi. |

Run 3 — solusi: Banyak kelereng Malosi = 5. Banyak kelereng Halim = 5 + 2 = 7. Selisih = 7 - 5 = 2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep selisih setelah menentukan jumlah kelereng Halim terlebih dahulu. Ini melibatkan pemilihan prosedur yang tepat untuk situasi perbandingan.. Bukti: Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih banyak kelereng Halim dan Malosi?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep 'lebih dari' dan 'selisih' dalam konteks aritmatika dasar.. Bukti: 2 kelereng lebihnya dari Malosi; selisih banyak kelereng
- Intended difficulty `classify/Medium`: Soal ini Medium bagi kelas 1 karena memerlukan dua langkah berurutan: menentukan jumlah kelereng Halim (5+2=7) lalu menghitung selisih (7-5=2). Meskipun angkanya kecil, siswa harus memahami hubungan 'lebih dari' dan menerjemahkannya ke operasi selisih.. Bukti: Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih banyak kelereng Halim dan Malosi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar sampai 10 dan pemahaman konsep selisih sebagai perbandingan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Dua langkah (menentukan jumlah Halim lalu selisih) adalah tuntutan yang wajar namun memerlukan ketelitian bagi siswa kelas 1 untuk tidak terjebak pada jumlah total. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 82/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.005753; applying=0.994247; reasoning=0.000000 | applying | 0.994247 | 0.032231 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.115207; conceptual=0.800676; procedural=0.084117; metacognitive=0.000000 | conceptual | 0.800676 | 0.458192 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.817709; Medium=0.179379; Hard=0.002912 | Easy | 0.817709 | 0.445823 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.994247; −Σp ln(p) = 0.035410; H = 0.035410/ln(3) = 0.032231; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.800676; −Σp ln(p) = 0.635189; H = 0.635189/ln(4) = 0.458192; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.817709; −Σp ln(p) = 0.489787; H = 0.489787/ln(3) = 0.445823; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengenal Konsep Lebih dari, Kurang dari, dan Selisih
Tipe soal: multiple_choice
Stimulus: -
Soal: Malosi mempunyai 5 kelereng. Halim mempunyai 2 kelereng lebihnya dari Malosi.

Berapakah selisih banyak kelereng Halim dan Malosi?
Pilihan: A. 7
B. 9
C. 5
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `fafff0345aa730c0722fc259`

Hari Minggu telah tiba. Tika membantu Ibu memasak di dapur. Mereka membuat donat. Tika membantu Ibu menghias donat. Ibu menghias 7 kue donat. Tika menghias 6 donat. Tika sangat senang.<br><br>Siapa yang memiliki donat lebih banyak?

| Opsi | Isi |
|---|---|
| A | Tidak bisa ditentukan |
| B | Sama banyak |
| C | Ibu |
| D | Tika |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Ibu menghias 7 donat dan Tika menghias 6 donat. Karena 7 lebih besar dari 6, maka Ibu memiliki donat lebih banyak.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `459a1cd6ed481f8b00aefcce18b22ca6a59f387def45aa129821f3febce1a894`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2262 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2266 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3300 |

Run 1 — solusi: Ibu menghias 7 donat dan Tika menghias 6 donat. Karena 7 lebih besar dari 6, maka Ibu memiliki donat lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua bilangan (7 dan 6) untuk menentukan mana yang lebih besar. Ini adalah penerapan konsep perbandingan bilangan yang sudah dipelajari di kelas 1.. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.; Siapa yang memiliki donat lebih banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai bilangan dan perbandingan kuantitas (lebih banyak/lebih sedikit).. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membandingkan dua angka yang sudah eksplisit diberikan dalam cerita tanpa langkah perantara yang kompleks.. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.; Siapa yang memiliki donat lebih banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami urutan bilangan 1-10 dan konsep perbandingan lebih banyak/sedikit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah terbiasa membandingkan dua kelompok benda atau angka sederhana dalam konteks sehari-hari. |

Run 2 — solusi: Ibu menghias 7 donat dan Tika menghias 6 donat. Karena 7 lebih besar dari 6, maka Ibu memiliki donat lebih banyak.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan dua kuantitas yang sudah diberikan secara eksplisit (7 dan 6) untuk menentukan mana yang lebih besar. Ini adalah penerapan langsung dari konsep perbandingan bilangan dasar.. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.; Siapa yang memiliki donat lebih banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan 'lebih banyak' antara dua bilangan cacah.. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan dua angka yang sudah tersedia tanpa perlu melakukan operasi hitung tambahan atau perencanaan langkah yang kompleks.. Bukti: Ibu menghias 7 kue donat.; Tika menghias 6 donat.; Siapa yang memiliki donat lebih banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep perbandingan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, membandingkan dua bilangan tunggal adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Ibu menghias 7 donat, Tika menghias 6 donat. Karena 7 lebih besar dari 6, maka Ibu memiliki donat lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perbandingan bilangan untuk menentukan mana yang lebih besar antara 7 dan 6.. Bukti: Ibu menghias 7 kue donat; Tika menghias 6 donat; Siapa yang memiliki donat lebih banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep perbandingan kuantitas (lebih dari/kurang dari) antara dua bilangan.. Bukti: Ibu menghias 7 kue donat; Tika menghias 6 donat
- Intended difficulty `classify/Easy`: Soal ini adalah tugas rutin perbandingan dua bilangan satu digit yang familiar bagi siswa kelas 1. Tidak ada kendala kompleks atau langkah perencanaan yang rumit.. Bukti: Ibu menghias 7 kue donat; Tika menghias 6 donat; Siapa yang memiliki donat lebih banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami urutan bilangan dan konsep perbandingan dasar (lebih dari/kurang dari) untuk bilangan 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membandingkan dua bilangan kecil adalah standar kompetensi kelas 1. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 101/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000004 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.027509; conceptual=0.962838; procedural=0.009652; metacognitive=0.000000 | conceptual | 0.962838 | 0.129917 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.839304; Medium=0.155455; Hard=0.005241 | Easy | 0.839304 | 0.422274 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000005; H = 0.000005/ln(3) = 0.000004; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.962838; −Σp ln(p) = 0.180103; H = 0.180103/ln(4) = 0.129917; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.839304; −Σp ln(p) = 0.463915; H = 0.463915/ln(3) = 0.422274; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengenal Konsep Lebih dari, Kurang dari, dan Selisih
Tipe soal: multiple_choice
Stimulus: -
Soal: Hari Minggu telah tiba. Tika membantu Ibu memasak di dapur. Mereka membuat donat. Tika membantu Ibu menghias donat. Ibu menghias 7 kue donat. Tika menghias 6 donat. Tika sangat senang.

Siapa yang memiliki donat lebih banyak?
Pilihan: A. Tidak bisa ditentukan
B. Sama banyak
C. Ibu
D. Tika
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `4a1c88e1d656ed6e318fbc08`

Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.<br><br>Berapa jumlah kelereng mereka?

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 16 |
| C | 5 |
| D | 17 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Jumlah kelereng = 11 + 6 = 17.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d944b597b8c285deadeb3ea167880c3f1de9706a6a7f4a09187fd9cf872cc4c3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2236 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2215 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2222 |

Run 1 — solusi: Jumlah kelereng = 11 + 6 = 17.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi penjumlahan dasar (11 + 6) yang merupakan prosedur rutin yang telah dipelajari di kelas 1.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng. Berapa jumlah kelereng mereka?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menerapkan algoritma penjumlahan dasar untuk menyelesaikan masalah kontekstual sederhana.. Bukti: Berapa jumlah kelereng mereka?
- Intended difficulty `classify/Easy`: Soal ini adalah masalah penjumlahan satu langkah yang sangat langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks. Siswa hanya perlu mengenali operasi penjumlahan dari kata kunci 'jumlah'.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.; Berapa jumlah kelereng mereka?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menjumlahkan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 11 + 6 adalah materi standar kelas 1. Soal tidak memiliki jebakan atau langkah tambahan, sehingga tingkat kesulitannya rendah bagi siswa kelas 1. |

Run 2 — solusi: Jumlah kelereng = 11 + 6 = 17.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi penjumlahan dasar (11 + 6) yang merupakan prosedur rutin dan langsung bagi siswa kelas 1.. Bukti: Berapa jumlah kelereng mereka?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep penjumlahan sebagai penggabungan dua kumpulan benda (kelereng) untuk mendapatkan total.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah penjumlahan satu langkah yang sangat standar. Siswa hanya perlu menjumlahkan dua bilangan yang diberikan tanpa ada kendala tambahan atau kebutuhan untuk menyusun strategi yang kompleks.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.; Berapa jumlah kelereng mereka?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menjumlahkan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 11 + 6 adalah materi dasar kelas 1. Tidak ada langkah perantara atau jebakan logika yang membuat soal ini sulit bagi siswa pada jenjang tersebut. |

Run 3 — solusi: Jumlah kelereng = 11 + 6 = 17.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar (11 + 6) yang merupakan prosedur rutin dan langsung untuk kelas 1.. Bukti: Berapa jumlah kelereng mereka?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan untuk menggabungkan dua kelompok benda.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.
- Intended difficulty `classify/Easy`: Soal ini adalah masalah penjumlahan satu langkah yang sangat standar. Siswa hanya perlu mengenali kata kunci 'jumlah' dan melakukan operasi penjumlahan 11 + 6. Tidak ada kendala yang berinteraksi atau kebutuhan untuk menyusun strategi kompleks.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.; Berapa jumlah kelereng mereka?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menjumlahkan bilangan sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan di bawah 20 adalah materi standar kelas 1. Soal disajikan secara langsung tanpa jebakan atau kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3524`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dasar (11 + 6) yang merupakan prosedur rutin dan langsung bagi siswa kelas 1.
- Dimensi pengetahuan `procedural`: Soal ini menguji kemampuan siswa dalam menerapkan algoritma penjumlahan dasar untuk menyelesaikan masalah kontekstual sederhana.
- Intended difficulty `Easy`: Soal ini adalah masalah penjumlahan satu langkah yang sangat langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks. Siswa hanya perlu mengenali operasi penjumlahan dari kata kunci 'jumlah'.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menjumlahkan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 11 + 6 adalah materi standar kelas 1. Soal tidak memiliki jebakan atau langkah tambahan, sehingga tingkat kesulitannya rendah bagi siswa kelas 1. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 69/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.056262; applying=0.943738; reasoning=0.000000 | applying | 0.943738 | 0.197118 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.321111; conceptual=0.630184; procedural=0.048705; metacognitive=0.000000 | conceptual | 0.630184 | 0.579199 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873440; Medium=0.123988; Hard=0.002572 | Easy | 0.873440 | 0.357143 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.943738; −Σp ln(p) = 0.216556; H = 0.216556/ln(3) = 0.197118; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.630184; −Σp ln(p) = 0.802940; H = 0.802940/ln(4) = 0.579199; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873440; −Σp ln(p) = 0.392362; H = 0.392362/ln(3) = 0.357143; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Penjumlahan yang Hasilnya kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.

Berapa jumlah kelereng mereka?
Pilihan: A. 18
B. 16
C. 5
D. 17
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `c5a941d72ce972bb9d49a4cc`

Hitunglah operasi penjumlahan berikut. Gunakan cara yang paling mudah.<br><br>14 + 5 = ....

| Opsi | Isi |
|---|---|
| A | 19 |
| B | 9 |
| C | 20 |
| D | 14 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 14 + 5 = 19. Penjumlahan dilakukan dengan menambahkan satuan 4 + 5 = 9, kemudian digabungkan dengan nilai puluhan 10, sehingga 10 + 9 = 19.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `786067b77a86f24b9d6af0b63fb69d2a08b4a920cc3efdb2d82458eb4f8b33b2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2083 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2088 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2131 |

Run 1 — solusi: 14 + 5 = 19. Penjumlahan dilakukan dengan menambahkan satuan 4 + 5 = 9, kemudian digabungkan dengan nilai puluhan 10, sehingga 10 + 9 = 19.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang sudah familiar. Prosedur penjumlahan bilangan dua digit dengan satu digit (tanpa teknik menyimpan) merupakan prosedur langsung yang diajarkan di kelas 1.. Bukti: 14 + 5 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritme penjumlahan dasar (prosedural) untuk bilangan di bawah 20.. Bukti: 14 + 5 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan langsung tanpa teknik menyimpan atau langkah tambahan yang kompleks. Siswa kelas 1 diharapkan sudah menguasai penjumlahan dasar ini.. Bukti: 14 + 5 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 14+5 adalah standar kompetensi kelas 1. Tidak ada kendala atau langkah tambahan yang menuntut perencanaan tinggi. |

Run 2 — solusi: 14 + 5 = 19. Penjumlahan dilakukan dengan menambahkan satuan 4 + 5 = 9, kemudian digabungkan dengan puluhan 10, sehingga 10 + 9 = 19.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar dengan bilangan di bawah 20. Prosedur ini merupakan penerapan langsung dari konsep penjumlahan yang sudah dipelajari di kelas 1, sehingga termasuk dalam domain knowing.. Bukti: 14 + 5 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritme penjumlahan dasar (prosedural) untuk bilangan dua digit dengan satu digit.. Bukti: 14 + 5 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar yang familiar bagi siswa kelas 1. Jalur penyelesaiannya langsung dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: 14 + 5 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 14+5 adalah standar kompetensi kelas 1. Tidak ada kendala atau langkah tambahan yang membuat soal ini sulit bagi siswa pada level tersebut. |

Run 3 — solusi: 14 + 5 = 19. Penjumlahan dilakukan dengan menambahkan satuan 4 + 5 = 9, kemudian digabungkan dengan puluhan 10, sehingga 10 + 9 = 19.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang sudah familiar (bilangan 14 dan 5). Prosedur penjumlahan ini merupakan algoritma standar yang langsung diterapkan tanpa perlu strategi nonrutin atau penalaran kompleks.. Bukti: Hitunglah operasi penjumlahan berikut.; 14 + 5 = ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma penjumlahan bilangan cacah (prosedural) yang melibatkan pemahaman nilai tempat sederhana (satuan dengan satuan).. Bukti: 14 + 5 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar satu langkah yang sangat familiar bagi siswa kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 14 + 5 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman penjumlahan dasar 1-20 dan nilai tempat puluhan-satuan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 14+5 adalah materi standar kelas 1. Siswa hanya perlu menjumlahkan satuan (4+5=9) dan mempertahankan puluhannya, yang merupakan prosedur rutin tanpa beban kognitif tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.987252; applying=0.012748; reasoning=0.000000 | knowing | 0.987252 | 0.062150 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.289140; conceptual=0.616053; procedural=0.094807; metacognitive=0.000000 | conceptual | 0.616053 | 0.635193 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.898797; Medium=0.098771; Hard=0.002432 | Easy | 0.898797 | 0.308744 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.987252; −Σp ln(p) = 0.068278; H = 0.068278/ln(3) = 0.062150; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.616053; −Σp ln(p) = 0.880564; H = 0.880564/ln(4) = 0.635193; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.898797; −Σp ln(p) = 0.339189; H = 0.339189/ln(3) = 0.308744; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Penjumlahan yang Hasilnya kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi penjumlahan berikut. Gunakan cara yang paling mudah.

14 + 5 = ....
Pilihan: A. 19
B. 9
C. 20
D. 14
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `54e65cf97cc65f3ef126daef`

Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.<br><br>Berapakah sisa bolu kukus Ibu sekarang?

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 11 |
| C | 15 |
| D | 12 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 13 - 2 = 11
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `80d1844d6b8b7f2d4e32fac770fcb8b8191211326e1882f35ca957447ecf18a7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2708 |
| 2 | success | valid / verified | applying | procedural | Easy | 2276 |
| 3 | success | valid / verified | applying | procedural | Easy | 2801 |

Run 1 — solusi: 13 - 2 = 11
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pengurangan untuk menyelesaikan masalah kontekstual sederhana yang melibatkan sisa objek.. Bukti: Ibu membeli 13 bolu kukus.; Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan prosedur pengurangan dasar untuk menentukan hasil dari situasi yang diberikan.. Bukti: 13 bolu kukus; memakan 2; sisa bolu kukus
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung operasi pengurangan satu langkah yang familiar bagi siswa kelas 1. Tidak ada kendala tambahan atau perencanaan kompleks yang diperlukan.. Bukti: Ibu membeli 13 bolu kukus.; Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan dalam lingkup 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini adalah soal cerita satu langkah yang standar untuk kelas 1, di mana kata 'sisa' secara langsung mengarahkan siswa untuk melakukan operasi pengurangan. |

Run 2 — solusi: Ibu memiliki 13 bolu, dimakan 2, maka sisa = 13 - 2 = 11.
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan operasi pengurangan dasar (13-2) dalam konteks cerita sederhana. Siswa hanya perlu mengenali situasi pengurangan dan menerapkan prosedur pengurangan yang sudah dipelajari di kelas 1.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus. Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep pengurangan sebagai pengambilan atau pengurangan jumlah (konseptual) dan menerapkan algoritma pengurangan dasar (prosedural).. Bukti: 13 bolu kukus; memakan 2 bolu kukus; Berapakah sisa
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari operasi pengurangan dasar. Jalur penyelesaiannya tunggal dan jelas (13-2), tidak memerlukan perencanaan kompleks atau integrasi kendala yang berinteraksi.. Bukti: 13 bolu kukus; memakan 2 bolu kukus; Berapakah sisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung mundur atau pengurangan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, pengurangan 13-2 adalah operasi standar yang diharapkan sudah dikuasai. Tidak ada jebakan atau langkah tambahan yang membuat soal ini sulit. |

Run 3 — solusi: 13 - 2 = 11
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pengurangan pada konteks cerita rutin untuk menentukan sisa objek.. Bukti: Ibu membeli 13 bolu kukus.; Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme pengurangan dasar (13 - 2) yang merupakan prosedur standar.. Bukti: 13 bolu kukus; memakan 2 bolu kukus; Berapakah sisa
- Intended difficulty `classify/Easy`: Soal ini adalah operasi pengurangan satu langkah yang sangat langsung dengan angka di bawah 20, sesuai dengan kurikulum kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Ibu membeli 13 bolu kukus.; Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 13-2 adalah standar kelas 1. Soal cerita langsung tanpa jebakan atau langkah tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000336; applying=0.999664; reasoning=0.000000 | applying | 0.999664 | 0.002752 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.394923; conceptual=0.557740; procedural=0.047337; metacognitive=0.000000 | conceptual | 0.557740 | 0.603733 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.897328; Medium=0.097928; Hard=0.004744 | Easy | 0.897328 | 0.318705 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999664; −Σp ln(p) = 0.003023; H = 0.003023/ln(3) = 0.002752; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.557740; −Σp ln(p) = 0.836951; H = 0.836951/ln(4) = 0.603733; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.897328; −Σp ln(p) = 0.350133; H = 0.350133/ln(3) = 0.318705; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pengurangan yang Hasilnya Kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.

Berapakah sisa bolu kukus Ibu sekarang?
Pilihan: A. 10
B. 11
C. 15
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `3dbc40f08ab7c63a376fc3e5`

Hitunglah operasi pengurangan berikut. Gunakan cara yang paling mudah.<br><br>15 – 4 = ....

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 11 |
| C | 19 |
| D | 10 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `11`.
Solusi minimum hasil AI: 15 - 4 = 11
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b8565588d99a56e4c1ac0c180ca4b95fa71e2d2fe200c8f5757f695b1cc82ad6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2678 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2210 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2827 |

Run 1 — solusi: 15 - 4 = 11
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar secara langsung, yang merupakan prosedur rutin bagi siswa kelas 1.. Bukti: Hitunglah operasi pengurangan berikut; 15 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Tugas ini memerlukan penerapan algoritma atau teknik pengurangan dasar untuk mendapatkan hasil.. Bukti: Hitunglah operasi pengurangan berikut; 15 – 4 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi hitung dasar satu langkah yang familiar bagi siswa kelas 1 tanpa memerlukan perencanaan strategi yang kompleks.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan urutan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dalam rentang 20 adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

Run 2 — solusi: 15 - 4 = 11. Siswa dapat menghitung mundur dari 15 sebanyak 4 langkah (14, 13, 12, 11) atau mengurangkan satuan (5 - 4 = 1, sehingga 15 - 4 = 11).
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar yang sudah familiar. Siswa hanya perlu menjalankan prosedur pengurangan langsung tanpa harus membangun strategi nonrutin atau mengintegrasikan hubungan yang kompleks.. Bukti: Hitunglah operasi pengurangan berikut; 15 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Soal menguji kemampuan siswa dalam menerapkan algoritme atau teknik pengurangan dasar untuk bilangan di bawah 20.. Bukti: 15 – 4 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu langkah yang sangat mendasar bagi siswa kelas 1. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 15-4 adalah standar kurikulum kelas 1 yang bersifat langsung dan rutin. |

Run 3 — solusi: 15 - 4 = 11
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang sudah dipelajari. Tidak ada langkah penalaran kompleks atau strategi non-rutin yang diperlukan.. Bukti: Hitunglah operasi pengurangan berikut; 15 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur pengurangan dasar untuk menyelesaikan soal.. Bukti: 15 – 4 = ....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi pengurangan langsung tanpa konteks cerita atau kendala tambahan. Bagi siswa kelas 1, ini adalah tugas rutin yang familiar.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 15-4 adalah standar kurikulum kelas 1, tidak memerlukan langkah tambahan atau penalaran kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.998046; applying=0.001954; reasoning=0.000000 | knowing | 0.998046 | 0.012871 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.622915; conceptual=0.206623; procedural=0.170462; metacognitive=0.000000 | factual | 0.622915 | 0.665268 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.920146; Medium=0.076652; Hard=0.003201 | Easy | 0.920146 | 0.265649 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998046; −Σp ln(p) = 0.014141; H = 0.014141/ln(3) = 0.012871; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.622915; −Σp ln(p) = 0.922258; H = 0.922258/ln(4) = 0.665268; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.920146; −Σp ln(p) = 0.291845; H = 0.291845/ln(3) = 0.265649; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pengurangan yang Hasilnya Kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi pengurangan berikut. Gunakan cara yang paling mudah.

15 – 4 = ....
Pilihan: A. 12
B. 11
C. 19
D. 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `ff83d65211d6e4aa98e13b06`

Perhatikan gambar berikut.<br><br>Urutan bunga dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | B, C, A |
| B | C, A, B |
| C | A, C, B |
| D | A, B, C |

![Gambar sumber soal 43](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0218-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Mengamati tinggi ketiga bunga secara visual: A adalah yang terpendek, C lebih tinggi dari A, dan B adalah yang tertinggi. Urutan dari yang paling pendek adalah A, C, B.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0218-01.png. Transkripsi visual: Terdapat tiga bunga matahari yang ditanam pada garis dasar yang sama. Bunga A berada di kiri, B di tengah, dan C di kanan. Secara visual, bunga A adalah yang paling pendek, bunga C memiliki tinggi menengah, dan bunga B adalah yang paling tinggi.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2cd67e345b9fb5ecdcad169f752b4a2407f16f949a97c00f4b973635f6feb670`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3384 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3357 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3388 |

Run 1 — solusi: Mengamati tinggi ketiga bunga secara visual: A adalah yang terpendek, C lebih tinggi dari A, dan B adalah yang tertinggi. Maka urutan dari yang terpendek adalah A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan perbandingan visual langsung dan mengurutkan objek berdasarkan atribut panjang (tinggi). Ini adalah penerapan prosedur yang sangat langsung dan rutin dalam konteks kelas 1.. Bukti: Urutan bunga dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang konsep panjang dan urutan (seriasi) yang merupakan prinsip dasar dalam pengukuran.. Bukti: Urutan bunga dari paling pendek
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dengan representasi visual yang jelas. Siswa hanya perlu membandingkan tinggi tiga objek yang diletakkan pada garis dasar yang sama, yang merupakan tugas rutin untuk kelas 1.. Bukti: Urutan bunga dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dua atau lebih objek berdasarkan atribut fisik (panjang/tinggi) secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengurutkan benda berdasarkan tinggi adalah materi standar kelas 1. Tidak ada kendala kompleks atau langkah tersembunyi. |

Run 2 — solusi: Mengamati tinggi ketiga bunga secara visual: A adalah yang terpendek, diikuti C, dan B adalah yang tertinggi. Urutan dari pendek ke tinggi adalah A, C, B.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan perbandingan visual langsung dan mengurutkan objek berdasarkan atribut panjang (tinggi). Ini adalah prosedur rutin yang langsung.. Bukti: Urutan bunga dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang konsep panjang dan urutan (seriasi) yang merupakan pengetahuan dasar dalam matematika awal.. Bukti: Urutan bunga dari paling pendek
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 1 karena hanya memerlukan observasi visual langsung terhadap tiga objek yang diletakkan pada garis dasar yang sama. Tidak ada langkah rumit atau kendala yang berinteraksi.. Bukti: Urutan bunga dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan tinggi dua atau lebih benda secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengurutkan benda berdasarkan tinggi adalah materi standar kelas 1 yang bersifat langsung dan intuitif. |

Run 3 — solusi: Mengamati tinggi ketiga bunga secara visual: A adalah yang terpendek, C lebih tinggi dari A, dan B adalah yang tertinggi. Urutan dari yang paling pendek adalah A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengamati atribut fisik (tinggi) dari tiga objek yang disajikan secara visual dan mengurutkannya berdasarkan kriteria yang diberikan (dari yang paling pendek). Ini adalah tugas menerapkan konsep perbandingan panjang.. Bukti: Urutan bunga dari paling pendek; Perhatikan gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang konsep panjang dan urutan, yang merupakan prinsip dasar dalam pengukuran.. Bukti: Membandingkan dan Mengurutkan Panjang Benda
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan observasi visual langsung terhadap tiga objek yang diletakkan pada garis dasar yang sama. Tidak ada manipulasi atau langkah kompleks yang diperlukan.. Bukti: Urutan bunga dari paling pendek; Perhatikan gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan tinggi benda secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, membandingkan tinggi tiga benda yang diletakkan pada bidang datar adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4662`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk melakukan perbandingan visual langsung dan mengurutkan objek berdasarkan atribut panjang (tinggi). Ini adalah penerapan prosedur yang sangat langsung dan rutin dalam konteks kelas 1.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang konsep panjang dan urutan (seriasi) yang merupakan prinsip dasar dalam pengukuran.
- Intended difficulty `Easy`: Soal ini bersifat langsung dengan representasi visual yang jelas. Siswa hanya perlu membandingkan tinggi tiga objek yang diletakkan pada garis dasar yang sama, yang merupakan tugas rutin untuk kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dua atau lebih objek berdasarkan atribut fisik (panjang/tinggi) secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengurutkan benda berdasarkan tinggi adalah materi standar kelas 1. Tidak ada kendala kompleks atau langkah tersembunyi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 140/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.921957; applying=0.078043; reasoning=0.000000 | knowing | 0.921957 | 0.249371 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.004543; conceptual=0.994993; procedural=0.000464; metacognitive=0.000000 | conceptual | 0.994993 | 0.023849 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.701593; Medium=0.294623; Hard=0.003785 | Easy | 0.701593 | 0.573268 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.921957; −Σp ln(p) = 0.273963; H = 0.273963/ln(3) = 0.249371; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.994993; −Σp ln(p) = 0.033062; H = 0.033062/ln(4) = 0.023849; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.701593; −Σp ln(p) = 0.629799; H = 0.629799/ln(3) = 0.573268; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan dan Mengurutkan Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut.

Urutan bunga dari paling pendek: ...., ...., ....
Pilihan: A. B, C, A
B. C, A, B
C. A, C, B
D. A, B, C
Transkripsi visual: Terdapat tiga bunga matahari yang ditanam pada garis dasar yang sama. Bunga A berada di kiri, B di tengah, dan C di kanan. Secara visual, bunga A adalah yang paling pendek, bunga C memiliki tinggi menengah, dan bunga B adalah yang paling tinggi.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `dc65bbd6611c904972206f6c`

Burung yang terbang paling tinggi adalah ....

| Opsi | Isi |
|---|---|
| A | Ketiga burung terbang sama tinggi |
| B | C |
| C | B |
| D | A |

![Gambar sumber soal 44](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0219-07.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Mengamati posisi vertikal ketiga burung pada gambar. Burung C berada pada posisi paling atas dibandingkan burung A dan B, sehingga burung C adalah yang terbang paling tinggi.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0219-07.png. Transkripsi visual: Terdapat gambar tiga ekor burung dengan label A, B, dan C. Burung A berwarna merah, burung B berwarna biru, dan burung C berwarna kuning. Burung C berada pada posisi paling atas (paling tinggi) di langit. Burung A berada di posisi tengah. Burung B berada di posisi paling bawah, dekat dengan bukit.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `29e903c8ddcf3dc5742f8296474578321da94b99e519be860a6d195e7217a8de`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3351 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3340 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3343 |

Run 1 — solusi: Mengamati posisi vertikal ketiga burung pada gambar. Burung C berada pada posisi paling atas dibandingkan burung A dan B, sehingga burung C adalah yang terbang paling tinggi.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi posisi relatif benda (burung) dalam gambar. Ini adalah tugas pengenalan visual langsung yang tidak memerlukan prosedur kompleks atau penalaran abstrak.. Bukti: Burung yang terbang paling tinggi adalah ....
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep 'tinggi' dalam konteks posisi vertikal benda pada gambar, yang merupakan pengetahuan konseptual dasar.. Bukti: Burung yang terbang paling tinggi adalah ....
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana. Siswa hanya perlu membandingkan posisi vertikal tiga objek secara visual. Tidak ada langkah perantara atau perencanaan yang diperlukan.. Bukti: Burung yang terbang paling tinggi adalah ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan posisi atas dan bawah secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, membandingkan posisi benda secara visual adalah tugas yang sangat mendasar dan familiar. |

Run 2 — solusi: Mengamati posisi vertikal ketiga burung pada gambar. Burung C berada pada posisi paling atas, sehingga burung C terbang paling tinggi.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan pengamatan visual langsung untuk membandingkan posisi ketinggian objek (burung) dan mengidentifikasi mana yang berada di posisi paling atas.. Bukti: Burung yang terbang paling tinggi adalah ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual dasar tentang perbandingan posisi atau ketinggian (tinggi-rendah) sebagai bagian dari konsep pengukuran panjang/tinggi.. Bukti: Membandingkan dan Mengurutkan Panjang Benda
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung tanpa langkah perhitungan atau perencanaan yang kompleks. Sangat sesuai untuk tingkat kelas 1.. Bukti: Burung yang terbang paling tinggi adalah ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan posisi atas dan bawah secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membandingkan posisi visual objek adalah keterampilan dasar yang sesuai untuk siswa kelas 1. |

Run 3 — solusi: Mengamati posisi vertikal ketiga burung pada gambar. Burung C berada di posisi paling atas dibandingkan burung A dan B, sehingga burung C terbang paling tinggi.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi posisi objek (burung) berdasarkan ketinggian secara visual. Ini adalah tugas mengenali atau membaca informasi visual langsung tanpa perlu melakukan perhitungan atau strategi kompleks.. Bukti: Burung yang terbang paling tinggi adalah ....
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep perbandingan posisi (tinggi/rendah) sebagai elemen dasar dalam membandingkan panjang atau ketinggian benda.. Bukti: Membandingkan dan Mengurutkan Panjang Benda
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pengamatan visual langsung terhadap posisi objek. Tidak ada langkah perencanaan, perhitungan, atau kendala yang harus dipecahkan.. Bukti: Burung yang terbang paling tinggi adalah ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan posisi atas dan bawah secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, membandingkan posisi benda secara visual adalah tugas yang sangat mendasar dan familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 126/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001356; applying=0.998644; reasoning=0.000000 | applying | 0.998644 | 0.009385 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.182231; conceptual=0.813535; procedural=0.004234; metacognitive=0.000000 | conceptual | 0.813535 | 0.361587 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.855986; Medium=0.141137; Hard=0.002877 | Easy | 0.855986 | 0.388025 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998644; −Σp ln(p) = 0.010311; H = 0.010311/ln(3) = 0.009385; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.813535; −Σp ln(p) = 0.501266; H = 0.501266/ln(4) = 0.361587; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.855986; −Σp ln(p) = 0.426289; H = 0.426289/ln(3) = 0.388025; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan dan Mengurutkan Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Burung yang terbang paling tinggi adalah ....
Pilihan: A. Ketiga burung terbang sama tinggi
B. C
C. B
D. A
Transkripsi visual: Terdapat gambar tiga ekor burung dengan label A, B, dan C. Burung A berwarna merah, burung B berwarna biru, dan burung C berwarna kuning. Burung C berada pada posisi paling atas (paling tinggi) di langit. Burung A berada di posisi tengah. Burung B berada di posisi paling bawah, dekat dengan bukit.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `75434d44f2b377da3027e153`

Temukan panjang pensil berikut. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.<br><br>Urutan pensil dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | A, C, B |
| B | A, B, C |
| C | B, C, A |
| D | C, A, B |

![Gambar sumber soal 45](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Membandingkan panjang pensil: A (4) < C (5) < B (8). Urutan dari yang terpendek adalah A, C, B.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png. Transkripsi visual: Terdapat tiga pensil (A, B, C) di atas latar belakang kertas berpetak. Pensil A memiliki panjang 4 kotak. Pensil B memiliki panjang 8 kotak. Pensil C memiliki panjang 5 kotak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `23ccf34b948213a990c34c074371768210d3bf4264025596d996172f8a8cb261`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3457 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3495 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3487 |

Run 1 — solusi: Membandingkan panjang pensil: A (4) < C (5) < B (8). Urutan dari yang terpendek adalah A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan nilai panjang yang sudah diberikan secara eksplisit. Ini adalah prosedur langsung membandingkan bilangan dan mengurutkannya, yang termasuk dalam domain applying.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep urutan bilangan (magnitude) yang diterapkan pada konteks pengukuran panjang sederhana.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 1. Siswa hanya perlu membandingkan tiga bilangan bulat kecil (4, 5, 8) dan mengurutkannya. Tidak ada kendala yang berinteraksi atau perencanaan kompleks.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dan mengurutkan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mengurutkan tiga objek berdasarkan nilai numerik yang sudah disediakan adalah tugas standar dan rutin untuk kelas 1. |

Run 2 — solusi: Membandingkan nilai panjang: A=4, C=5, B=8. Urutan dari yang terkecil ke terbesar adalah 4, 5, 8, yang sesuai dengan urutan pensil A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan nilai panjang yang sudah diberikan secara eksplisit. Tugas ini hanya memerlukan pemahaman dasar tentang urutan bilangan (4 < 5 < 8) dan menerapkan urutan tersebut pada objek yang sesuai.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan panjang dan pengurutan bilangan, yang merupakan konsep dasar dalam pengukuran.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena nilai panjang sudah disediakan secara eksplisit dalam teks, sehingga siswa tidak perlu melakukan pengukuran manual. Tugas utamanya hanyalah mengurutkan tiga bilangan bulat kecil (4, 5, 8), yang merupakan prosedur rutin bagi siswa kelas 1.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dan mengurutkan bilangan 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mengurutkan tiga bilangan sudah sesuai dengan kurikulum kelas 1. Tidak ada langkah kompleks atau kendala yang saling berinteraksi. |

Run 3 — solusi: Bandingkan panjang pensil: A=4, C=5, B=8. Urutan dari yang terpendek adalah 4, 5, 8, yaitu A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan nilai panjang yang sudah diberikan secara eksplisit. Ini adalah tugas menerapkan prosedur perbandingan sederhana pada data yang sudah tersedia.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan besaran (panjang) berdasarkan nilai numerik yang diberikan.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan tiga bilangan bulat (4, 5, 8) dan mengurutkannya. Tidak ada langkah tersembunyi atau kendala kompleks.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membandingkan dan mengurutkan bilangan 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas mengurutkan tiga bilangan adalah standar untuk kelas 1. Informasi panjang sudah diberikan secara eksplisit, sehingga siswa tidak perlu melakukan pengukuran manual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 147/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.015966; applying=0.984034; reasoning=0.000000 | applying | 0.984034 | 0.074542 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.008287; conceptual=0.990463; procedural=0.001250; metacognitive=0.000000 | conceptual | 0.990463 | 0.041528 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.692102; Medium=0.303632; Hard=0.004266 | Easy | 0.692102 | 0.582461 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.984034; −Σp ln(p) = 0.081893; H = 0.081893/ln(3) = 0.074542; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.990463; −Σp ln(p) = 0.057570; H = 0.057570/ln(4) = 0.041528; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.692102; −Σp ln(p) = 0.639899; H = 0.639899/ln(3) = 0.582461; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengukur Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan panjang pensil berikut. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.

Urutan pensil dari paling pendek: ...., ...., ....
Pilihan: A. A, C, B
B. A, B, C
C. B, C, A
D. C, A, B
Transkripsi visual: Terdapat tiga pensil (A, B, C) di atas latar belakang kertas berpetak. Pensil A memiliki panjang 4 kotak. Pensil B memiliki panjang 8 kotak. Pensil C memiliki panjang 5 kotak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `62785ac6ff0622ab70a94b13`

Temukan panjang pita berikut. Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.<br><br>Pita B lebih .... dari pita C.

| Opsi | Isi |
|---|---|
| A | panjang |
| B | pendek |
| C | tinggi |
| D | besar |

![Gambar sumber soal 46](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0228-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pita B memiliki panjang 5 kotak dan pita C memiliki panjang 4 kotak. Karena 5 > 4, maka pita B lebih panjang daripada pita C.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0228-03.png. Transkripsi visual: Gambar menunjukkan tiga pita di atas kertas berpetak. Pita A (merah) memiliki panjang 6 kotak. Pita B (oranye) memiliki panjang 5 kotak. Pita C (ungu) memiliki panjang 4 kotak. Terdapat label A, B, dan C di samping masing-masing pita.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `221ce289eb7a1b54e16adfe9ff5d33c0cf2280410eaa571b70a42d542e088b01`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / verified | knowing | conceptual | Easy | 3565 |
| 2 | success | concern / verified | applying | conceptual | Easy | 3500 |
| 3 | success | concern / verified | applying | conceptual | Easy | 3520 |

Run 1 — solusi: Pita B memiliki panjang 5 kotak dan pita C memiliki panjang 4 kotak. Karena 5 lebih besar dari 4, maka pita B lebih panjang daripada pita C.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membandingkan dua bilangan yang sudah diberikan (5 dan 4) dan memilih istilah perbandingan yang tepat untuk panjang benda. Ini adalah prosedur langsung.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman istilah perbandingan dasar ('lebih panjang') terkait atribut panjang benda.. Bukti: Pita B lebih .... dari pita C.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena nilai panjang sudah diberikan secara eksplisit dalam teks. Siswa tidak perlu melakukan pengukuran atau interpretasi visual yang kompleks. Keputusan hanya terletak pada pemilihan kata sifat pembanding yang tepat.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep perbandingan dasar (lebih panjang/pendek) dan membandingkan bilangan cacah hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, membandingkan dua angka yang sudah diketahui dan memilih kata sifat yang sesuai adalah tugas rutin yang sangat mendasar. |

Run 2 — solusi: Berdasarkan teks soal: Pita B (5 kotak) > Pita C (4 kotak), maka Pita B lebih panjang dari Pita C.
- Domain kognitif `classify/applying`: Siswa diminta membandingkan dua nilai panjang yang sudah diberikan (5 dan 4) untuk menentukan hubungan perbandingan (lebih panjang). Ini adalah penerapan prosedur perbandingan langsung.. Bukti: Pita B lebih .... dari pita C.; Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep perbandingan panjang (lebih panjang/pendek) dan menerapkannya pada nilai numerik yang diberikan.. Bukti: Pita B lebih .... dari pita C.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan dua angka yang sudah disediakan (5 dan 4) untuk menentukan hubungan perbandingan. Tidak ada langkah perantara atau perencanaan yang kompleks.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep perbandingan dasar (lebih panjang/pendek) dan membandingkan bilangan cacah hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, membandingkan dua bilangan yang sudah diketahui nilainya adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif. |

Run 3 — solusi: Pita B memiliki panjang 5 kotak dan pita C memiliki panjang 4 kotak. Karena 5 lebih besar dari 4, maka pita B lebih panjang dari pita C.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan dua nilai panjang yang sudah diberikan (5 dan 4) dan memilih kata sifat pembanding yang tepat. Ini adalah proses menerapkan konsep perbandingan dasar.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan panjang antara dua objek yang sudah terukur.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu membandingkan dua angka yang sudah disediakan (5 dan 4) dan menentukan hubungan 'lebih panjang'. Tidak ada langkah perencanaan yang kompleks.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep perbandingan panjang (lebih panjang/pendek) dan membandingkan bilangan cacah dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, membandingkan dua bilangan dan menentukan kata pembanding yang sesuai adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4951`.
Konten: `concern`; kunci: `verified`; masalah: Terdapat ketidaksesuaian antara teks soal dan gambar. Teks menyatakan 'Panjang pita B = 5 kotak' dan 'Panjang pita C = 4 kotak', namun pada gambar, pita B (warna oranye) memiliki panjang 5 kotak, sedangkan pita C (warna ungu) memiliki panjang 4 kotak. Meskipun nilai numeriknya benar, soal ini memberikan informasi eksplisit yang membuat aktivitas pengukuran visual menjadi tidak diperlukan, sehingga menurunkan tuntutan kognitif soal secara drastis.; Soal ini seharusnya menguji kemampuan siswa dalam mengukur panjang benda menggunakan satuan tidak baku (kotak), namun karena panjangnya sudah diberitahukan, soal hanya menjadi latihan perbandingan bilangan sederhana..
- Domain kognitif `knowing`: Siswa hanya perlu membandingkan dua bilangan yang sudah diberikan (5 dan 4) dan memilih istilah perbandingan yang tepat. Ini adalah prosedur langsung yang tidak memerlukan penalaran atau pemecahan masalah.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman istilah perbandingan dasar ('lebih panjang') terkait atribut panjang benda.
- Intended difficulty `Easy`: Soal ini sangat mudah karena nilai panjang sudah diberikan secara eksplisit dalam teks. Siswa tidak perlu melakukan pengukuran atau interpretasi visual yang kompleks. Keputusan hanya terletak pada pemilihan kata sifat pembanding yang tepat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep perbandingan dasar (lebih panjang/pendek) dan membandingkan bilangan cacah hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, membandingkan dua angka yang sudah diketahui dan memilih kata sifat yang sesuai adalah tugas rutin yang sangat mendasar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 131/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengukur Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan panjang pita berikut. Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.

Pita B lebih .... dari pita C.
Pilihan: A. panjang
B. pendek
C. tinggi
D. besar
Transkripsi visual: Gambar menunjukkan tiga pita di atas kertas berpetak. Pita A (merah) memiliki panjang 6 kotak. Pita B (oranye) memiliki panjang 5 kotak. Pita C (ungu) memiliki panjang 4 kotak. Terdapat label A, B, dan C di samping masing-masing pita.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidaksesuaian antara teks soal dan gambar. Teks menyatakan 'Panjang pita B = 5 kotak' dan 'Panjang pita C = 4 kotak', namun pada gambar, pita B (warna oranye) memiliki panjang 5 kotak, sedangkan pita C (warna ungu) memiliki panjang 4 kotak. Meskipun nilai numeriknya benar, soal ini memberikan informasi eksplisit yang membuat aktivitas pengukuran visual menjadi tidak diperlukan, sehingga menurunkan tuntutan kognitif soal secara drastis.; Soal ini seharusnya menguji kemampuan siswa dalam mengukur panjang benda menggunakan satuan tidak baku (kotak), namun karena panjangnya sudah diberitahukan, soal hanya menjadi latihan perbandingan bilangan sederhana..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `5e007b54e25f6f72efa82174`

Amati gambar buah-buahan. Lengkapi daftarnya. Daftar Buah-buahan: Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.<br><br>Buah yang paling banyak adalah ...

| Opsi | Isi |
|---|---|
| A | Apel |
| B | Mangga |
| C | Jambu |
| D | Jeruk |

![Gambar sumber soal 47](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0238-11.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Menghitung jumlah tiap buah: jeruk=5, apel=4, mangga=6. Membandingkan jumlah: 6 > 5 > 4. Mangga adalah yang paling banyak.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0238-11.png. Transkripsi visual: Terdapat 15 buah yang disusun dalam grid 3x5. Baris 1: jeruk, apel, mangga, jeruk, mangga. Baris 2: apel, mangga, jeruk, mangga, apel. Baris 3: jeruk, mangga, apel, jeruk, mangga. Total hitungan: jeruk ada 5, apel ada 4, mangga ada 6.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bbab46716f9136e115a0385c633a11596dffc321f9eaf04cd24efe0bd7261d1c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3496 |
| 2 | success | valid / verified | applying | procedural | Easy | 3456 |
| 3 | success | valid / verified | applying | procedural | Easy | 3444 |

Run 1 — solusi: Menghitung jumlah tiap buah: jeruk=5, apel=4, mangga=6. Membandingkan jumlah: 6 > 5 > 4. Mangga adalah yang paling banyak.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan penghitungan langsung (counting) dari objek visual yang tersedia dan membandingkan hasilnya untuk menentukan nilai maksimum. Ini adalah prosedur rutin yang langsung.. Bukti: Amati gambar buah-buahan. Lengkapi daftarnya.; Buah yang paling banyak adalah ...
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam mengorganisasi data visual ke dalam kategori (buah) dan melakukan penghitungan (prosedur) untuk mendapatkan informasi kuantitatif.. Bukti: Amati gambar buah-buahan.; Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan penghitungan satu-ke-satu (one-to-one correspondence) yang familiar bagi kelas 1, kemudian membandingkan tiga bilangan kecil untuk menentukan yang terbesar.. Bukti: Amati gambar buah-buahan.; Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.; Buah yang paling banyak adalah ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas menghitung objek dan membandingkan jumlah adalah standar kurikulum kelas 1. Tidak ada kendala kompleks atau langkah yang saling bergantung secara rumit. |

Run 2 — solusi: Hitung jumlah tiap buah: jeruk=5, apel=4, mangga=6. Bandingkan jumlahnya: 6 > 5 > 4. Mangga adalah yang paling banyak.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan penghitungan objek (data) secara langsung dari gambar dan membandingkan hasilnya untuk menentukan nilai maksimum. Ini adalah prosedur rutin dalam pengolahan data sederhana.. Bukti: Amati gambar buah-buahan. Lengkapi daftarnya.; Buah yang paling banyak adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini melibatkan pengorganisasian data visual ke dalam kategori (jenis buah) dan menerapkan prosedur penghitungan serta perbandingan sederhana.. Bukti: Amati gambar buah-buahan; Lengkapi daftarnya
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena tugas utamanya adalah menghitung objek yang terlihat jelas dan membandingkan tiga bilangan kecil. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Amati gambar buah-buahan.; Lengkapi daftarnya.; Buah yang paling banyak adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, menghitung objek konkret atau gambar dan membandingkan jumlahnya adalah aktivitas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Menghitung jumlah tiap buah: jeruk 5, apel 4, mangga 6. Membandingkan jumlah: 6 > 5 > 4. Buah terbanyak adalah mangga (6).
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan penghitungan langsung (counting) dan membandingkan hasil hitungan tersebut untuk menentukan nilai maksimum. Ini adalah prosedur rutin yang langsung.. Bukti: Amati gambar buah-buahan. Lengkapi daftarnya.; Buah yang paling banyak adalah ...
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menerapkan prosedur menghitung objek konkret dan membandingkan kuantitas sederhana.. Bukti: Amati gambar buah-buahan.; Lengkapi daftarnya.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 1. Langkah-langkahnya jelas: hitung tiap jenis, bandingkan, pilih yang terbesar. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Amati gambar buah-buahan.; Lengkapi daftarnya.; Buah yang paling banyak adalah ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas menghitung objek dan membandingkan jumlah adalah standar kurikulum kelas 1. Tidak ada kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 156/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000671; applying=0.999329; reasoning=0.000000 | applying | 0.999329 | 0.005075 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.008140; conceptual=0.988909; procedural=0.002951; metacognitive=0.000000 | conceptual | 0.988909 | 0.048607 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.749055; Medium=0.245110; Hard=0.005834 | Easy | 0.749055 | 0.538026 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999329; −Σp ln(p) = 0.005575; H = 0.005575/ln(3) = 0.005075; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.988909; −Σp ln(p) = 0.067384; H = 0.067384/ln(4) = 0.048607; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.749055; −Σp ln(p) = 0.591081; H = 0.591081/ln(3) = 0.538026; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati gambar buah-buahan. Lengkapi daftarnya. Daftar Buah-buahan: Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.

Buah yang paling banyak adalah ...
Pilihan: A. Apel
B. Mangga
C. Jambu
D. Jeruk
Transkripsi visual: Terdapat 15 buah yang disusun dalam grid 3x5. Baris 1: jeruk, apel, mangga, jeruk, mangga. Baris 2: apel, mangga, jeruk, mangga, apel. Baris 3: jeruk, mangga, apel, jeruk, mangga. Total hitungan: jeruk ada 5, apel ada 4, mangga ada 6.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `17ba235cdc9fddc600303514`

Perhatikan tabel dan jawablah pertanyaannya.<br><br>Apa nama kue yang paling disukai?

| Opsi | Isi |
|---|---|
| A | Kue Cucur |
| B | Kue Lapis |
| C | Kue Talam |
| D | Kue Bugis |

![Gambar sumber soal 48](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0238-12.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Membandingkan nilai pada baris 'Banyak anak' untuk setiap kue: 5, 3, 5, dan 6. Nilai terbesar adalah 6, yang berkorespondensi dengan 'Kue Bugis'.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0238-12.png. Transkripsi visual: Tabel berjudul 'Tabel Kue Kesukaan' memiliki dua baris. Baris pertama berisi nama kue: 'Kue Talam', 'Kue Cucur', 'Kue Lapis', 'Kue Bugis'. Baris kedua berisi jumlah 'Banyak anak' yang menyukai kue tersebut: 5, 3, 5, 6 secara berurutan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eec7f51fc2c8aef9a6fa8f03fa64cbc4a866f536871708b91c25533579df445b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3370 |
| 2 | success | valid / verified | knowing | factual | Easy | 3360 |
| 3 | success | valid / verified | knowing | factual | Easy | 3370 |

Run 1 — solusi: Membandingkan nilai pada baris 'Banyak anak' untuk setiap kue: 5, 3, 5, dan 6. Nilai terbesar adalah 6, yang berkorespondensi dengan 'Kue Bugis'.
- Domain kognitif `classify/applying`: Siswa diminta untuk membaca data dari tabel sederhana dan melakukan perbandingan nilai untuk mengidentifikasi nilai maksimum. Ini adalah prosedur langsung yang rutin dalam membaca data.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data disajikan dalam tabel dan bagaimana membandingkan nilai-nilai tersebut untuk menarik kesimpulan sederhana.. Bukti: Tabel Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membandingkan empat angka tunggal yang disajikan secara eksplisit dalam tabel. Tidak ada langkah tersembunyi atau manipulasi data yang diperlukan.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel sederhana dan membandingkan bilangan cacah sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, membaca tabel sederhana dengan 4 entri data adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Membandingkan nilai pada baris 'Banyak anak' untuk setiap kue: 5, 3, 5, dan 6. Nilai terbesar adalah 6, yang sesuai dengan 'Kue Bugis'.
- Domain kognitif `classify/knowing`: Siswa diminta membaca data dari tabel sederhana dan melakukan perbandingan nilai untuk menentukan nilai maksimum. Ini adalah prosedur langsung yang melibatkan pengenalan data dan perbandingan bilangan dasar.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca tabel sederhana dan membandingkan angka-angka yang disajikan secara eksplisit.. Bukti: Tabel Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 1 karena hanya memerlukan pembacaan langsung dari tabel dan perbandingan sederhana antara empat bilangan satu digit. Tidak ada langkah tersembunyi atau kompleksitas tambahan.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca tabel sederhana dan membandingkan bilangan cacah sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membaca tabel dan mencari nilai terbesar adalah keterampilan dasar kelas 1 yang rutin dilakukan. |

Run 3 — solusi: Membandingkan nilai pada baris 'Banyak anak' untuk setiap kue: 5, 3, 5, dan 6. Nilai terbesar adalah 6, yang berkorespondensi dengan 'Kue Bugis'.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari tabel dan mengidentifikasi nilai maksimum. Ini adalah prosedur langsung untuk membandingkan bilangan bulat sederhana yang sudah familiar bagi siswa kelas 1.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca tabel sederhana dan membandingkan nilai numerik dasar.. Bukti: Tabel Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membandingkan empat angka (3, 5, 5, 6) untuk menemukan yang terbesar. Tidak ada langkah perantara yang kompleks atau kendala yang berinteraksi.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca tabel sederhana dan membandingkan bilangan cacah sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membandingkan data dalam tabel sederhana adalah standar untuk kelas 1. Tidak ada tuntutan perencanaan atau integrasi yang tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4704`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk membaca data dari tabel sederhana dan melakukan perbandingan nilai untuk mengidentifikasi nilai maksimum. Ini adalah prosedur langsung yang rutin dalam membaca data.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data disajikan dalam tabel dan bagaimana membandingkan nilai-nilai tersebut untuk menarik kesimpulan sederhana.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena siswa hanya perlu membandingkan empat angka tunggal yang disajikan secara eksplisit dalam tabel. Tidak ada langkah tersembunyi atau manipulasi data yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel sederhana dan membandingkan bilangan cacah sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, membaca tabel sederhana dengan 4 entri data adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 127/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000008; applying=0.999992; reasoning=0.000000 | applying | 0.999992 | 0.000097 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.027265; conceptual=0.968455; procedural=0.004280; metacognitive=0.000000 | conceptual | 0.968455 | 0.110075 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.811629; Medium=0.182695; Hard=0.005676 | Easy | 0.811629 | 0.463602 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000106; H = 0.000106/ln(3) = 0.000097; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.968455; −Σp ln(p) = 0.152597; H = 0.152597/ln(4) = 0.110075; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.811629; −Σp ln(p) = 0.509319; H = 0.509319/ln(3) = 0.463602; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan tabel dan jawablah pertanyaannya.

Apa nama kue yang paling disukai?
Pilihan: A. Kue Cucur
B. Kue Lapis
C. Kue Talam
D. Kue Bugis
Transkripsi visual: Tabel berjudul 'Tabel Kue Kesukaan' memiliki dua baris. Baris pertama berisi nama kue: 'Kue Talam', 'Kue Cucur', 'Kue Lapis', 'Kue Bugis'. Baris kedua berisi jumlah 'Banyak anak' yang menyukai kue tersebut: 5, 3, 5, 6 secara berurutan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `e7d8a29f2e3a28f99529dfc8`

Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Lengkapi setiap kalimat berikut.<br><br>Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 3 |
| C | 4 |
| D | 1 |

![Gambar sumber soal 49](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Hitung jumlah bintang untuk belimbing (7) dan apel (4). Hitung selisihnya: 7 - 4 = 3.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png. Transkripsi visual: Diagram batang vertikal berjudul 'Diagram Buah Kesukaan'. Terdapat empat kolom buah: jeruk, apel, belimbing, dan jambu air. Setiap kolom berisi simbol bintang. Jeruk: 6 bintang. Apel: 4 bintang. Belimbing: 7 bintang. Jambu air: 5 bintang. Keterangan di bawah: 'Gambar bintang mewakili 1 anak'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9155aacd3b6617a0788cbc77309dd2f3120669a5167efaab9f67873ff6b23e3c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3472 |
| 2 | success | valid / verified | applying | procedural | Medium | 3478 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3450 |

Run 1 — solusi: Hitung jumlah bintang untuk belimbing (7) dan apel (4). Hitung selisihnya: 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari piktogram (menghitung bintang) untuk dua kategori yang berbeda, lalu melakukan operasi pengurangan untuk menentukan selisih. Ini adalah penerapan prosedur matematika dasar pada konteks data yang disajikan secara visual.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.; Diagram batang vertikal menggunakan simbol bintang untuk mewakili jumlah anak.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang cara membaca piktogram dan melakukan operasi pengurangan dasar untuk membandingkan dua nilai.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.; 1 bintang mewakili 1 anak.
- Intended difficulty `classify/Medium`: Soal ini meminta siswa melakukan dua langkah: menghitung frekuensi dari dua kategori berbeda dan mencari selisihnya. Bagi siswa kelas 1, ini adalah tugas rutin yang melibatkan interpretasi data sederhana.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.; Diagram batang vertikal menggunakan simbol bintang untuk mewakili jumlah anak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (bintang) dan melakukan pengurangan dasar dalam lingkup 10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa harus mengintegrasikan pembacaan data dari dua kolom berbeda dan memahami konsep 'selisih' atau 'lebih banyak' dalam konteks piktogram, yang merupakan tuntutan sedang untuk kelas 1. |

Run 2 — solusi: Hitung jumlah anak yang suka belimbing (7 bintang) dan apel (4 bintang). Hitung selisihnya: 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari piktogram (menghitung jumlah bintang) dan melakukan operasi pengurangan sederhana untuk mencari selisih. Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks rutin.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.; Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang cara membaca piktogram dan melakukan operasi pengurangan dasar.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.; Gambar bintang mewakili 1 anak.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan dua langkah terpisah (membaca data belimbing dan apel) sebelum melakukan operasi pengurangan untuk membandingkan jumlah. Meskipun operasinya dasar, integrasi data dari diagram ke dalam kalimat rumpang memerlukan ketelitian lebih daripada sekadar membaca satu nilai.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.; Diagram berikut menunjukkan jenis buah kesukaan anak-anak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (bintang) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, membaca piktogram dan membandingkan dua nilai dengan operasi selisih adalah tugas yang sesuai untuk tingkat menengah karena melibatkan perpindahan dari representasi visual ke numerik. |

Run 3 — solusi: Hitung jumlah bintang untuk belimbing (7) dan apel (4). Hitung selisihnya: 7 - 4 = 3. Jadi, anak yang suka belimbing 3 lebih banyak dari anak yang suka apel.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram (menghitung jumlah simbol) dan melakukan operasi pengurangan sederhana untuk membandingkan dua kategori. Ini adalah penerapan prosedur familiar pada konteks data visual.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.; Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan diagram gambar sederhana (pictograph) sebagai representasi data.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus melakukan dua langkah terpisah (menghitung jumlah belimbing dan apel) sebelum melakukan operasi pengurangan untuk membandingkan. Meskipun prosedurnya familiar, terdapat ketergantungan langkah yang memerlukan ketelitian.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

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
| gradeRelativeRationale | Untuk kelas 1, membaca diagram dan melakukan pengurangan dua langkah merupakan tuntutan yang sesuai untuk tingkat Medium, karena memerlukan integrasi data dari dua kolom yang berbeda. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4945`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur membaca data dari piktogram (menghitung simbol) untuk dua kategori berbeda, lalu melakukan operasi pengurangan untuk membandingkan nilai. Ini adalah penerapan konsep matematika dasar pada konteks data visual.
- Dimensi pengetahuan `procedural`: Siswa menggunakan pengetahuan prosedural tentang cara membaca piktogram dan melakukan operasi pengurangan dasar untuk membandingkan dua nilai.
- Intended difficulty `Medium`: Soal ini menuntut siswa melakukan dua langkah terpisah (membaca data belimbing dan apel) sebelum melakukan operasi pengurangan untuk membandingkan jumlah. Meskipun operasinya dasar, integrasi data dari diagram ke dalam kalimat rumpang memerlukan ketelitian lebih daripada sekadar membaca satu nilai.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (bintang) dan melakukan pengurangan dasar dalam lingkup 10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 1, membaca piktogram dan membandingkan dua nilai dengan operasi selisih adalah tugas yang sesuai untuk tingkat menengah karena melibatkan perpindahan dari representasi visual ke numerik. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 139/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000008; applying=0.999992; reasoning=0.000000 | applying | 0.999992 | 0.000089 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.030080; conceptual=0.963988; procedural=0.005932; metacognitive=0.000000 | conceptual | 0.963988 | 0.123471 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.625976; Medium=0.363577; Hard=0.010446 | Easy | 0.625976 | 0.645122 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000097; H = 0.000097/ln(3) = 0.000089; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.963988; −Σp ln(p) = 0.171167; H = 0.171167/ln(4) = 0.123471; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.625976; −Σp ln(p) = 0.708739; H = 0.708739/ln(3) = 0.645122; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Lengkapi setiap kalimat berikut.

Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
Pilihan: A. 2
B. 3
C. 4
D. 1
Transkripsi visual: Diagram batang vertikal berjudul 'Diagram Buah Kesukaan'. Terdapat empat kolom buah: jeruk, apel, belimbing, dan jambu air. Setiap kolom berisi simbol bintang. Jeruk: 6 bintang. Apel: 4 bintang. Belimbing: 7 bintang. Jambu air: 5 bintang. Keterangan di bawah: 'Gambar bintang mewakili 1 anak'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 50. Soal `8812007076d1edea9f050f6f`

Ibu membeli buah di pasar. Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.<br><br>Buah yang paling sedikit adalah ...

| Opsi | Isi |
|---|---|
| A | Belimbing |
| B | Jeruk |
| C | Apel |
| D | Mangga |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Membandingkan jumlah buah: jeruk (6), apel (3), mangga (4), dan belimbing (5). Nilai terkecil adalah 3, yang merupakan jumlah apel.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9e063ad458ed3b609db038b8a9b57f76f1911d5d301c2c399c94d65aeab7d459`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2147 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2232 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2138 |

Run 1 — solusi: Membandingkan jumlah buah: jeruk (6), apel (3), mangga (4), belimbing (5). Nilai terkecil adalah 3, yaitu apel.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membandingkan sekumpulan bilangan (6, 3, 4, 5) dan mengidentifikasi nilai terkecil. Ini adalah prosedur langsung dalam membandingkan bilangan cacah.. Bukti: Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.; Buah yang paling sedikit adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang urutan dan perbandingan nilai bilangan cacah, yang merupakan konsep dasar dalam matematika.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membandingkan empat bilangan yang sudah diberikan secara eksplisit untuk menemukan yang terkecil. Tidak ada langkah perantara atau kendala yang harus dibangun.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.; Buah yang paling sedikit adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, membandingkan empat bilangan untuk mencari nilai minimum adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Membandingkan jumlah buah: jeruk (6), apel (3), mangga (4), belimbing (5). Nilai terkecil adalah 3, yaitu apel.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membandingkan nilai bilangan yang diberikan dan mengidentifikasi nilai terkecil. Ini adalah prosedur langsung untuk membandingkan kuantitas.. Bukti: Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.; Buah yang paling sedikit adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep dasar perbandingan bilangan (lebih sedikit/lebih banyak) yang merupakan pengetahuan konseptual dasar.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 1 karena hanya memerlukan perbandingan langsung dari empat bilangan yang sudah diberikan secara eksplisit tanpa langkah tambahan atau kendala yang kompleks.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.; Buah yang paling sedikit adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan membandingkan kumpulan benda atau bilangan. Soal ini adalah bentuk paling dasar dari perbandingan kuantitas. |

Run 3 — solusi: Membandingkan jumlah buah: jeruk (6), apel (3), mangga (4), belimbing (5). Nilai terkecil adalah 3, yaitu jumlah apel.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan nilai dari sekumpulan data yang diberikan dan mengidentifikasi nilai minimum. Ini adalah prosedur rutin dalam pengolahan data sederhana.. Bukti: Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.; Buah yang paling sedikit adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep perbandingan kuantitas (lebih sedikit/banyak) pada data yang sudah tersedia.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membandingkan empat bilangan bulat positif yang sudah eksplisit diberikan. Tidak ada langkah tersembunyi atau kendala yang saling berinteraksi.. Bukti: Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.; Buah yang paling sedikit adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk siswa kelas 1, membandingkan empat bilangan tunggal adalah tugas dasar yang sesuai dengan kurikulum awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3652`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu membandingkan empat bilangan cacah yang diberikan secara eksplisit untuk menentukan nilai minimum. Ini adalah prosedur langsung yang tidak memerlukan strategi nonrutin atau integrasi konsep yang kompleks.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman dasar tentang urutan dan perbandingan nilai bilangan cacah, yang merupakan konsep fundamental dalam matematika kelas 1.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu membandingkan empat bilangan yang sudah diberikan secara eksplisit untuk menemukan yang terkecil. Tidak ada langkah perantara atau kendala yang harus dibangun.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 1, membandingkan empat bilangan untuk mencari nilai minimum adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 75/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001439; applying=0.998561; reasoning=0.000000 | applying | 0.998561 | 0.009882 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.370495; conceptual=0.614093; procedural=0.015412; metacognitive=0.000000 | conceptual | 0.614093 | 0.527748 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.894204; Medium=0.101535; Hard=0.004261 | Easy | 0.894204 | 0.323583 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998561; −Σp ln(p) = 0.010857; H = 0.010857/ln(3) = 0.009882; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.614093; −Σp ln(p) = 0.731615; H = 0.731615/ln(4) = 0.527748; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.894204; −Σp ln(p) = 0.355493; H = 0.355493/ln(3) = 0.323583; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu membeli buah di pasar. Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.

Buah yang paling sedikit adalah ...
Pilihan: A. Belimbing
B. Jeruk
C. Apel
D. Mangga
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
