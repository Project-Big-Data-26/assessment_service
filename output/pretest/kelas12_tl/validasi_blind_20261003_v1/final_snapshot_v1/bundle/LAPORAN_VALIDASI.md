# Validasi ulang soal kelas 12 TL — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v9-blind-sma12-tl-key-verified`. Rubrik: `math-rubric-3x4x3-v7-sma12-tl-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 12 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 12, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 41; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 34, "knowing": 7, "reasoning": 0}, "knowledgeDimension": {"procedural": 31, "conceptual": 10, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Medium": 11, "Easy": 30, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 7, "applying": 33, "reasoning": 0}, "knowledgeDimension": {"conceptual": 10, "procedural": 30, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 30, "Medium": 10, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"revision_required": 1, "pending_expert_review": 40}`.
Run awal sukses: 123/123; adjudikasi: 15; token sukses tercatat: 366,852.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 30 | 30 | [Easy.json](difficulty/Easy.json) |
| Medium | 11 | 10 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 12, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 12, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 12. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `5faf4ffecb76e0e311ebef4d`

Diketahui sebuah lingkaran $L_1\equiv x^2+y^2-6x+8y-39=0$. Akan dibuat lingkaran kedua $L_2$ dengan titik pusat lingkaran $L_1$ dicerminkan terhadap sumbu-$x$ dan jari-jarinya diperbesar tiga kali dari jari-jari $L_1$. Tentukan persamaan lingkaran $L_2$ tersebut.

| Opsi | Isi |
|---|---|
| A | pusat $(3,4)$, jari-jari $24$ |
| B | pusat $(3,4)$, jari-jari $8$ |
| C | pusat $(3,4)$, jari-jari $11$ |
| D | pusat $(-3,-4)$, jari-jari $24$ |

Kunci sumber: `A`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: L1: x^2-6x+y^2+8y=39 -> (x-3)^2+(y+4)^2=64. Pusat (3,-4), r=8. Refleksi pusat terhadap sumbu-x: (3,4). Jari-jari baru R=3*8=24. Persamaan L2: (x-3)^2+(y-4)^2=24^2=576, atau x^2+y^2-6x-8y-551=0. Opsi A hanya memberikan pusat dan jari-jari, bukan persamaan lingkaran lengkap, sehingga tidak menjawab pertanyaan 'Tentukan persamaan lingkaran L2'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ba1c72259e9290cc19fd3b788e1acb2125b5765b77b09aae16272720b6156ca2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2255 |
| 2 | success | valid / verified | applying | procedural | Medium | 2319 |
| 3 | success | valid / verified | applying | procedural | Medium | 2276 |

Run 1 — solusi: L1: x^2-6x+y^2+8y=39 -> (x-3)^2+(y+4)^2=39+9+16=64. Pusat (3,-4), r=8. Refleksi pusat terhadap sumbu-x: (3,4). Jari-jari baru R=3*8=24. Persamaan L2: (x-3)^2+(y-4)^2=24^2=576. Opsi A menyatakan pusat (3,4) dan r=24, yang konsisten dengan hasil.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep transformasi geometri (refleksi) pada titik pusat lingkaran dan manipulasi parameter jari-jari lingkaran. Proses ini melibatkan penerapan prosedur standar yang sudah dipelajari di kelas 12 TL.. Bukti: titik pusat lingkaran L1 dicerminkan terhadap sumbu-x; jari-jarinya diperbesar tiga kali dari jari-jari L1
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman konseptual tentang bentuk umum persamaan lingkaran dan prosedur transformasi titik, serta bagaimana perubahan parameter jari-jari mempengaruhi persamaan lingkaran.. Bukti: x^2+y^2-6x+8y-39=0; titik pusat lingkaran L1 dicerminkan terhadap sumbu-x
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12 TL. Langkah-langkahnya jelas: melengkapkan kuadrat untuk mencari pusat/jari-jari, melakukan refleksi, dan menyusun ulang persamaan. Tidak ada strategi non-rutin yang diperlukan.. Bukti: x^2+y^2-6x+8y-39=0; titik pusat lingkaran L1 dicerminkan terhadap sumbu-x; jari-jarinya diperbesar tiga kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran, melengkapkan kuadrat, refleksi titik terhadap sumbu-x. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan transformasi adalah standar kurikulum kelas 12 TL. Prosedur yang diminta adalah prosedur standar yang sering dilatih. |

Run 2 — solusi: L1: x^2+y^2-6x+8y-39=0 -> (x-3)^2+(y+4)^2 = 39+9+16 = 64. Pusat (3,-4), r=8. Refleksi sumbu-x: (3,-4) -> (3,4). Jari-jari baru R = 3*8 = 24. L2: (x-3)^2+(y-4)^2 = 24^2 = 576. x^2-6x+9+y^2-8y+16 = 576 -> x^2+y^2-6x-8y-551=0. Catatan: Kunci A pada soal salah dalam penulisan persamaan akhir, namun benar dalam deskripsi pusat dan jari-jari.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pusat dan jari-jari dari bentuk umum lingkaran, menerapkan transformasi geometri (refleksi), dan melakukan operasi aritmatika untuk menentukan parameter lingkaran baru.. Bukti: titik pusat lingkaran L1 dicerminkan terhadap sumbu-x; jari-jarinya diperbesar tiga kali dari jari-jari L1
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang melengkapkan kuadrat untuk mencari pusat/jari-jari dan konsep transformasi geometri.. Bukti: x^2+y^2-6x+8y-39=0; titik pusat lingkaran L1 dicerminkan terhadap sumbu-x
- Intended difficulty `classify/Medium`: Soal ini melibatkan prosedur standar (melengkapkan kuadrat, refleksi titik, pembentukan persamaan lingkaran) yang rutin bagi siswa kelas 12.. Bukti: x^2+y^2-6x+8y-39=0; titik pusat lingkaran L1 dicerminkan terhadap sumbu-x; jari-jarinya diperbesar tiga kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran, melengkapkan kuadrat, refleksi titik pada bidang kartesius. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan transformasi adalah standar kelas 11/12. Prosedur yang digunakan bersifat rutin tanpa memerlukan strategi non-rutin. |

Run 3 — solusi: L1: x^2-6x+y^2+8y=39 -> (x-3)^2+(y+4)^2=39+9+16=64. Pusat (3,-4), r=8. Refleksi (3,-4) terhadap sumbu-x menjadi (3,4). Jari-jari baru r'=3*8=24. Persamaan L2: (x-3)^2+(y-4)^2=24^2=576, atau x^2-6x+9+y^2-8y+16=576 -> x^2+y^2-6x-8y-551=0. Opsi A menyatakan pusat (3,4) dan r=24, yang konsisten dengan deskripsi.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pusat dan jari-jari dari bentuk umum lingkaran, menerapkan transformasi geometri (refleksi), dan melakukan operasi aritmatika pada jari-jari. Ini adalah penerapan prosedur standar.. Bukti: titik pusat lingkaran L1 dicerminkan terhadap sumbu-x; jari-jarinya diperbesar tiga kali dari jari-jari L1
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman konsep bentuk umum lingkaran dan transformasi geometri dasar.. Bukti: x^2+y^2-6x+8y-39=0; titik pusat lingkaran L1 dicerminkan terhadap sumbu-x
- Intended difficulty `classify/Medium`: Soal ini melibatkan prosedur rutin: melengkapkan kuadrat untuk mencari pusat/jari-jari, refleksi titik, dan penskalaan jari-jari. Tidak ada strategi non-rutin yang diperlukan.. Bukti: x^2+y^2-6x+8y-39=0; titik pusat lingkaran L1 dicerminkan terhadap sumbu-x; jari-jarinya diperbesar tiga kali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Melengkapkan kuadrat sempurna, transformasi geometri (refleksi), persamaan lingkaran. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah standar kelas 12 TL. Prosedur yang diminta bersifat rutin dan langsung, namun memerlukan ketelitian dalam manipulasi aljabar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4233`.
Konten: `valid`; kunci: `conflict`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur transformasi geometri dan manipulasi persamaan lingkaran. Meskipun prosedurnya rutin, soal meminta persamaan lengkap namun opsi hanya memberikan pusat dan jari-jari, yang merupakan ketidaksesuaian antara tuntutan soal dan opsi jawaban.
- Dimensi pengetahuan `procedural`: Memerlukan pemahaman prosedural tentang melengkapkan kuadrat, transformasi geometri, dan pembentukan persamaan lingkaran.
- Intended difficulty `Medium`: Soal ini melibatkan prosedur rutin (melengkapkan kuadrat, refleksi, penskalaan). Kesulitan utama terletak pada ketidaksesuaian antara pertanyaan (meminta persamaan) dan opsi (hanya pusat/jari-jari).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran, melengkapkan kuadrat, refleksi titik. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran dan transformasi adalah standar kelas 12 TL. Prosedur rutin namun terdapat cacat pada opsi jawaban. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui sebuah lingkaran $L_1\equiv x^2+y^2-6x+8y-39=0$. Akan dibuat lingkaran kedua $L_2$ dengan titik pusat lingkaran $L_1$ dicerminkan terhadap sumbu-$x$ dan jari-jarinya diperbesar tiga kali dari jari-jari $L_1$. Tentukan persamaan lingkaran $L_2$ tersebut.
Pilihan: A. pusat $(3,4)$, jari-jari $24$
B. pusat $(3,4)$, jari-jari $8$
C. pusat $(3,4)$, jari-jari $11$
D. pusat $(-3,-4)$, jari-jari $24$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `revision_required`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `9d2c41327363766288766657`

Diketahui pusat lingkaran terletak pada titik pusat $O(0,0)$.<br><br>Tentukan persamaan lingkaran tersebut jika jari-jari $r=\sqrt{15}$.

| Opsi | Isi |
|---|---|
| A | $x^2+y^2=15$ |
| B | $x^2+y^2=\sqrt{15}$ |
| C | $x^2+y^2=225$ |
| D | $x+y=15$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Persamaan lingkaran dengan pusat (0,0) adalah x^2 + y^2 = r^2. Diketahui r = sqrt(15), maka r^2 = 15. Substitusi nilai r^2 ke dalam persamaan menghasilkan x^2 + y^2 = 15.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f18180a1445b3328a6b09123af7816144ffdecdbad92b7221881cb5b69a4ce56`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2080 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2131 |
| 3 | success | valid / verified | knowing | factual | Easy | 2762 |

Run 1 — solusi: Persamaan lingkaran dengan pusat (0,0) adalah x^2 + y^2 = r^2. Diketahui r = sqrt(15), maka r^2 = (sqrt(15))^2 = 15. Jadi, persamaan lingkarannya adalah x^2 + y^2 = 15.
- Domain kognitif `classify/knowing`: Soal ini hanya memerlukan penerapan langsung dari rumus standar persamaan lingkaran dengan pusat (0,0), yaitu x^2 + y^2 = r^2. Siswa hanya perlu mensubstitusi nilai r ke dalam rumus tersebut tanpa memerlukan strategi pemecahan masalah yang kompleks.. Bukti: pusat lingkaran terletak pada titik pusat O(0,0); jari-jari r=\sqrt{15}
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai bentuk standar persamaan lingkaran (konsep) dan prosedur substitusi nilai jari-jari ke dalam persamaan tersebut.. Bukti: persamaan lingkaran tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar dan rutin bagi siswa kelas 12. Tidak ada langkah kompleks atau kendala yang harus dipecahkan.. Bukti: pusat lingkaran terletak pada titik pusat O(0,0); jari-jari r=\sqrt{15}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi persamaan lingkaran dengan pusat (0,0). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran merupakan dasar yang sudah dipelajari sebelumnya dan soal ini hanya menanyakan bentuk standar tanpa modifikasi. |

Run 2 — solusi: Persamaan lingkaran dengan pusat (0,0) adalah x^2 + y^2 = r^2. Diketahui r = sqrt(15), maka r^2 = (sqrt(15))^2 = 15. Substitusi nilai r^2 ke dalam persamaan menghasilkan x^2 + y^2 = 15.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus standar persamaan lingkaran dengan pusat (0,0) dan jari-jari yang diberikan. Siswa hanya perlu melakukan substitusi nilai ke dalam rumus x^2 + y^2 = r^2, yang merupakan proses rutin.. Bukti: pusat lingkaran terletak pada titik pusat O(0,0); jari-jari r=sqrt(15); Tentukan persamaan lingkaran
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan bentuk standar persamaan lingkaran dengan pusat di titik asal, yang merupakan konsep dasar dalam geometri analitik.. Bukti: pusat lingkaran terletak pada titik pusat O(0,0); Tentukan persamaan lingkaran tersebut jika jari-jari r=sqrt(15)
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan langsung, hanya memerlukan satu langkah substitusi nilai ke dalam rumus yang sudah dikenal. Tidak ada kendala atau strategi kompleks yang diperlukan.. Bukti: pusat lingkaran terletak pada titik pusat O(0,0); jari-jari r=sqrt(15); Tentukan persamaan lingkaran

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman bentuk standar persamaan lingkaran x^2 + y^2 = r^2. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi lingkaran diajarkan di kelas 11, soal ini merupakan prasyarat dasar untuk topik geometri analitik di kelas 12 TL. Tingkat kesulitannya sangat rendah karena hanya melibatkan substitusi langsung. |

Run 3 — solusi: Persamaan lingkaran dengan pusat (0,0) adalah x^2 + y^2 = r^2. Dengan r = sqrt(15), maka r^2 = 15. Jadi, persamaannya adalah x^2 + y^2 = 15.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta penerapan langsung definisi persamaan lingkaran standar dengan pusat (0,0) dan jari-jari r, tanpa memerlukan manipulasi atau strategi kompleks.. Bukti: Diketahui pusat lingkaran terletak pada titik pusat O(0,0).; Tentukan persamaan lingkaran tersebut jika jari-jari r=\sqrt{15}.
- Dimensi pengetahuan `classify/factual`: Siswa hanya perlu mengingat bentuk standar persamaan lingkaran x^2 + y^2 = r^2 dan menerapkan nilai r yang diberikan.. Bukti: Tentukan persamaan lingkaran tersebut jika jari-jari r=\sqrt{15}.
- Intended difficulty `classify/Easy`: Prosedur sangat langsung, hanya substitusi nilai ke dalam rumus standar tanpa langkah tambahan.. Bukti: Diketahui pusat lingkaran terletak pada titik pusat O(0,0).; Tentukan persamaan lingkaran tersebut jika jari-jari r=\sqrt{15}.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi persamaan lingkaran pusat (0,0). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan dasar lingkaran, sangat rutin dan tidak menuntut kemampuan analisis tingkat lanjut. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3567`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya memerlukan penerapan langsung dari rumus standar persamaan lingkaran dengan pusat (0,0), yaitu x^2 + y^2 = r^2. Siswa hanya perlu mensubstitusi nilai r ke dalam rumus tersebut tanpa memerlukan strategi pemecahan masalah yang kompleks.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman siswa mengenai bentuk standar persamaan lingkaran (konsep) dan prosedur substitusi nilai jari-jari ke dalam persamaan tersebut.
- Intended difficulty `Easy`: Soal ini bersifat sangat mendasar dan rutin. Tidak ada langkah kompleks atau kendala yang harus dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi persamaan lingkaran dengan pusat (0,0). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran merupakan dasar yang sudah dipelajari sebelumnya dan soal ini hanya menanyakan bentuk standar tanpa modifikasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui pusat lingkaran terletak pada titik pusat $O(0,0)$.

Tentukan persamaan lingkaran tersebut jika jari-jari $r=\sqrt{15}$.
Pilihan: A. $x^2+y^2=15$
B. $x^2+y^2=\sqrt{15}$
C. $x^2+y^2=225$
D. $x+y=15$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `9abb5ee08760d5ba15421eeb`

Diketahui koordinat titik fokus suatu elips adalah $F_1(8,-1)$ dan $F_2(-4,-1)$ serta salah satu koordinat ujung sumbu minornya adalah $(2,7)$. Tentukan persamaan elips tersebut.

| Opsi | Isi |
|---|---|
| A | $\dfrac{(x-2)^2}{100}+\dfrac{(y-1)^2}{64}=1$ |
| B | $\dfrac{(x-2)^2}{100}+\dfrac{(y+1)^2}{64}=1$ |
| C | $\dfrac{(x-2)^2}{64}+\dfrac{(y+1)^2}{100}=1$ |
| D | $\dfrac{(x-2)^2}{36}+\dfrac{(y+1)^2}{64}=1$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pusat elips adalah titik tengah F1(8,-1) dan F2(-4,-1), yaitu (2,-1). Sumbu utama horizontal karena ordinat fokus sama. Jarak fokus 2c = 8 - (-4) = 12, maka c = 6. Ujung sumbu minor (2,7) berjarak b = \|7 - (-1)\| = 8 dari pusat. Maka a^2 = b^2 + c^2 = 8^2 + 6^2 = 64 + 36 = 100. Persamaan: (x-2)^2/100 + (y+1)^2/64 = 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aa53378d302b60b79d33c0a1eb13367723c3ada34bde830bafe39ad658d0161f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2300 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2300 |
| 3 | success | valid / verified | applying | procedural | Medium | 3484 |

Run 1 — solusi: Pusat elips adalah titik tengah F1(8,-1) dan F2(-4,-1), yaitu ((8-4)/2, (-1-1)/2) = (2,-1). Jarak fokus 2c = 8 - (-4) = 12, maka c = 6. Ujung sumbu minor (2,7) berjarak b = \|7 - (-1)\| = 8 dari pusat. Karena sumbu utama horizontal, a^2 = b^2 + c^2 = 8^2 + 6^2 = 64 + 36 = 100. Persamaan: (x-2)^2/100 + (y+1)^2/64 = 1.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pusat, nilai c, dan nilai b dari informasi yang diberikan, kemudian menggunakan hubungan a^2 = b^2 + c^2 untuk menentukan persamaan elips. Ini adalah penerapan prosedur standar dalam geometri analitik.. Bukti: koordinat titik fokus suatu elips adalah F1(8,-1) dan F2(-4,-1); salah satu koordinat ujung sumbu minornya adalah (2,7)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang struktur persamaan elips dan hubungan antara parameter-parameternya (pusat, fokus, sumbu minor).. Bukti: Tentukan persamaan elips tersebut
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin: mencari pusat, menentukan jarak fokus, menentukan panjang sumbu minor, dan menghitung parameter a. Prosedur ini familiar dalam kurikulum kelas 12 TL.. Bukti: koordinat titik fokus suatu elips adalah F1(8,-1) dan F2(-4,-1); salah satu koordinat ujung sumbu minornya adalah (2,7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, rumus jarak titik, hubungan parameter elips (a, b, c). |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi elips adalah standar kurikulum kelas 12 Matematika Tingkat Lanjut. Soal ini menguji pemahaman prosedural dasar tanpa kerumitan non-rutin. |

Run 2 — solusi: Pusat elips adalah titik tengah F1(8,-1) dan F2(-4,-1), yaitu (2,-1). Sumbu utama horizontal karena ordinat fokus sama. Jarak fokus 2c = 8 - (-4) = 12, maka c = 6. Ujung sumbu minor (2,7) berjarak b = \|7 - (-1)\| = 8 dari pusat. Maka a^2 = b^2 + c^2 = 8^2 + 6^2 = 64 + 36 = 100. Persamaan: (x-2)^2/100 + (y+1)^2/64 = 1.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi pusat elips, menentukan orientasi sumbu, menghitung parameter a, b, dan c, serta menyusun persamaan standar elips. Ini adalah penerapan prosedur rutin dalam geometri analitik.. Bukti: Diketahui koordinat titik fokus suatu elips adalah F1(8,-1) dan F2(-4,-1) serta salah satu koordinat ujung sumbu minornya adalah (2,7).
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang hubungan antara parameter elips (pusat, fokus, sumbu minor) dan prosedur penyusunan persamaan elips.. Bukti: Tentukan persamaan elips tersebut.
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (mencari pusat, menghitung jarak, menentukan parameter a, b, c) yang saling terkait. Siswa harus memahami hubungan geometris elips untuk menentukan nilai a^2 dan b^2 dengan benar.. Bukti: Diketahui koordinat titik fokus suatu elips adalah F1(8,-1) dan F2(-4,-1) serta salah satu koordinat ujung sumbu minornya adalah (2,7).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, rumus jarak, titik tengah, persamaan standar elips. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi elips adalah standar kelas 12 Matematika Tingkat Lanjut. Soal memerlukan pemahaman konsep yang cukup untuk menghubungkan titik-titik yang diberikan ke dalam bentuk persamaan. |

Run 3 — solusi: Pusat elips adalah titik tengah fokus: (2,-1). Jarak fokus 2c = 12, maka c=6. Jarak dari pusat (2,-1) ke ujung sumbu minor (2,7) adalah b=8. Karena sumbu utama horizontal, a^2 = b^2 + c^2 = 64 + 36 = 100. Persamaan: (x-2)^2/100 + (y+1)^2/64 = 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar untuk menentukan persamaan elips berdasarkan titik fokus dan ujung sumbu minor, yang melibatkan perhitungan pusat, nilai c, nilai b, dan hubungan a^2=b^2+c^2.. Bukti: titik fokus suatu elips adalah F1(8,-1) dan F2(-4,-1); salah satu koordinat ujung sumbu minornya adalah (2,7)
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma dan teknik standar dalam geometri analitik elips.. Bukti: Tentukan persamaan elips tersebut
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin yang saling terkait: menentukan pusat, menghitung c, menghitung b, dan menentukan orientasi elips untuk menyusun persamaan.. Bukti: F1(8,-1) dan F2(-4,-1); ujung sumbu minornya adalah (2,7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, rumus jarak, hubungan a, b, c pada elips. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena melibatkan geometri analitik elips yang merupakan materi standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4119`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi pusat, nilai c, dan nilai b dari informasi yang diberikan, kemudian menggunakan hubungan a^2 = b^2 + c^2 untuk menentukan persamaan elips. Ini adalah penerapan prosedur standar dalam geometri analitik.
- Dimensi pengetahuan `conceptual`: Soal ini menuntut pemahaman tentang struktur persamaan elips dan hubungan antara parameter-parameternya (pusat, fokus, sumbu minor).
- Intended difficulty `Medium`: Soal ini memerlukan beberapa langkah rutin: mencari pusat, menentukan jarak fokus, menentukan panjang sumbu minor, dan menghitung parameter a. Prosedur ini familiar dalam kurikulum kelas 12 TL.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, rumus jarak titik, hubungan parameter elips (a, b, c). |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi elips adalah standar kurikulum kelas 12 Matematika Tingkat Lanjut. Soal ini menguji pemahaman prosedural dasar tanpa kerumitan non-rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Elips
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui koordinat titik fokus suatu elips adalah $F_1(8,-1)$ dan $F_2(-4,-1)$ serta salah satu koordinat ujung sumbu minornya adalah $(2,7)$. Tentukan persamaan elips tersebut.
Pilihan: A. $\dfrac{(x-2)^2}{100}+\dfrac{(y-1)^2}{64}=1$
B. $\dfrac{(x-2)^2}{100}+\dfrac{(y+1)^2}{64}=1$
C. $\dfrac{(x-2)^2}{64}+\dfrac{(y+1)^2}{100}=1$
D. $\dfrac{(x-2)^2}{36}+\dfrac{(y+1)^2}{64}=1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `d4b6313f54c1e2d6eabb94d4`

Suatu elips memiliki titik pusat $O(0,0)$. Salah satu fokusnya terletak pada titik $(0,3)$ dan panjang sumbu mayornya adalah 10. Tentukan persamaan elips tersebut.

| Opsi | Isi |
|---|---|
| A | $\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$ |
| B | $\dfrac{x^2}{16}+\dfrac{y^2}{9}=1$ |
| C | $\dfrac{x^2}{4}+\dfrac{y^2}{25}=1$ |
| D | $\dfrac{x^2}{16}+\dfrac{y^2}{25}=1$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pusat (0,0) dan fokus (0,3) menunjukkan elips vertikal dengan c=3. Panjang sumbu mayor 2a=10, maka a=5. Berlaku b^2 = a^2 - c^2 = 25 - 9 = 16. Persamaan elips vertikal: x^2/b^2 + y^2/a^2 = 1, yaitu x^2/16 + y^2/25 = 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `04c64a0b13c8f819230f591b17d0af6354b37c8013c5e443f628b472b84c16bb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2242 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2225 |
| 3 | success | valid / verified | applying | procedural | Easy | 2251 |

Run 1 — solusi: Pusat (0,0) dan fokus (0,3) menunjukkan elips vertikal. Panjang sumbu mayor 2a=10, maka a=5. Jarak fokus c=3. Berlaku b^2 = a^2 - c^2 = 25 - 9 = 16. Persamaan elips vertikal: x^2/b^2 + y^2/a^2 = 1, yaitu x^2/16 + y^2/25 = 1.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi orientasi elips dari koordinat fokus, menentukan parameter a dan c, menghitung parameter b menggunakan relasi elips, dan menyusun persamaan standar.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10; Tentukan persamaan elips tersebut
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara fokus, sumbu mayor, dan parameter elips, serta prosedur aljabar untuk menyusun persamaan.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam kurikulum kelas 12 TL. Siswa hanya perlu menerapkan definisi elips dan relasi antar parameter tanpa strategi nonrutin.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, hubungan a, b, c pada elips, dan bentuk persamaan standar elips. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi elips adalah standar kurikulum kelas 12 TL. Soal ini menguji pemahaman dasar tentang parameter elips tanpa kompleksitas tambahan. |

Run 2 — solusi: Pusat (0,0) dan fokus (0,3) menunjukkan elips vertikal dengan c=3. Panjang sumbu mayor 2a=10, maka a=5. Hubungan a^2 = b^2 + c^2 menghasilkan b^2 = 25 - 9 = 16. Persamaan elips vertikal: x^2/b^2 + y^2/a^2 = 1, yaitu x^2/16 + y^2/25 = 1.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi orientasi elips dari koordinat fokus, menentukan parameter a dan c, menghitung b menggunakan hubungan elips, dan menyusun persamaan standar. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10.; Tentukan persamaan elips tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi elips, hubungan antara parameter a, b, dan c, serta bentuk standar persamaan elips.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12 yang mempelajari irisan kerucut. Langkah-langkahnya jelas: identifikasi orientasi, hitung parameter, substitusi ke rumus standar.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, hubungan a, b, c, dan bentuk persamaan standar elips. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi elips adalah standar kurikulum matematika tingkat lanjut kelas 12. Prosedur ini sangat familiar. |

Run 3 — solusi: Pusat (0,0), fokus (0,3) berarti elips vertikal dengan c=3. Panjang sumbu mayor 2a=10, maka a=5. Hubungan b^2 = a^2 - c^2 = 25 - 9 = 16. Persamaan elips vertikal: x^2/b^2 + y^2/a^2 = 1, yaitu x^2/16 + y^2/25 = 1.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi orientasi elips dari koordinat fokus, menentukan parameter a dan c, menghitung b menggunakan relasi elips, dan menyusun persamaan standar. Ini adalah penerapan prosedur rutin.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10.; Tentukan persamaan elips tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang definisi elips, hubungan antara parameter a, b, c, dan bentuk persamaan elips (konseptual) serta langkah-langkah aljabar untuk menentukannya (prosedural).. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10.
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam kurikulum kelas 12 untuk menentukan persamaan elips berdasarkan elemen-elemennya. Tidak ada jebakan atau strategi non-rutin.. Bukti: Salah satu fokusnya terletak pada titik (0,3) dan panjang sumbu mayornya adalah 10.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, hubungan a, b, c, dan bentuk persamaan elips standar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi elips adalah standar kurikulum matematika tingkat lanjut kelas 12. Menentukan persamaan dari fokus dan sumbu mayor adalah latihan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3968`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi orientasi elips dari koordinat fokus, menentukan parameter a dan c, menghitung parameter b menggunakan relasi elips, dan menyusun persamaan standar. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut pemahaman tentang definisi elips, hubungan antara parameter a, b, c, dan bentuk persamaan elips (konseptual) serta langkah-langkah aljabar untuk menentukannya (prosedural).
- Intended difficulty `Easy`: Soal ini merupakan prosedur standar dalam kurikulum kelas 12 untuk menentukan persamaan elips berdasarkan elemen-elemennya. Tidak ada jebakan atau strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi elips, hubungan a, b, c, dan bentuk persamaan elips standar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi elips adalah standar kurikulum matematika tingkat lanjut kelas 12. Menentukan persamaan dari fokus dan sumbu mayor adalah latihan rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Elips
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu elips memiliki titik pusat $O(0,0)$. Salah satu fokusnya terletak pada titik $(0,3)$ dan panjang sumbu mayornya adalah 10. Tentukan persamaan elips tersebut.
Pilihan: A. $\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$
B. $\dfrac{x^2}{16}+\dfrac{y^2}{9}=1$
C. $\dfrac{x^2}{4}+\dfrac{y^2}{25}=1$
D. $\dfrac{x^2}{16}+\dfrac{y^2}{25}=1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `09343175fbd7eabe7e201500`

Tentukan nilai $p$ agar garis $y=-x+p$ menyinggung lingkaran $L\equiv x^2+y^2-2x-4y+3=0$.

| Opsi | Isi |
|---|---|
| A | $p=1$ atau $p=3$ |
| B | $p=1$ atau $p=5$ |
| C | $p=-1$ atau $p=-5$ |
| D | $p=3$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `p=1 atau p=5`.
Solusi minimum hasil AI: Lingkaran x^2+y^2-2x-4y+3=0 memiliki pusat (1,2) dan r^2=2. Jarak pusat ke garis x+y-p=0 adalah \|1+2-p\|/sqrt(2) = sqrt(2). Maka \|3-p\|=2, sehingga p=1 atau p=5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e122f032f0ee6d129f4873de3b99afe63465abed1f4dd48bd8595a880f0597be`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3243 |
| 2 | success | valid / verified | applying | procedural | Medium | 2344 |
| 3 | success | valid / verified | applying | procedural | Medium | 2374 |

Run 1 — solusi: Lingkaran x^2+y^2-2x-4y+3=0 memiliki pusat (1,2) dan r^2=2. Jarak pusat ke garis x+y-p=0 adalah \|1+2-p\|/sqrt(2) = sqrt(2). Maka \|3-p\|=2, sehingga p=1 atau p=5.
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur standar (syarat diskriminan D=0 atau jarak titik ke garis) untuk menentukan parameter garis singgung pada lingkaran.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau teknik penyelesaian sistem persamaan atau geometri analitik.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (substitusi dan penyelesaian persamaan kuadrat atau penggunaan rumus jarak) yang saling terkait.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran, syarat garis singgung (D=0 atau d=r) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai kurikulum kelas 12, ini adalah prosedur rutin untuk menentukan parameter garis singgung. |

Run 2 — solusi: Substitusi y = -x + p ke x^2 + y^2 - 2x - 4y + 3 = 0 menghasilkan x^2 + (-x+p)^2 - 2x - 4(-x+p) + 3 = 0, disederhanakan menjadi 2x^2 + (2-2p)x + (p^2-4p+3) = 0. Syarat menyinggung adalah diskriminan D = 0. D = (2-2p)^2 - 4(2)(p^2-4p+3) = 0. 4(1-p)^2 - 8(p^2-4p+3) = 0. (1-2p+p^2) - 2(p^2-4p+3) = 0. -p^2 + 6p - 5 = 0. p^2 - 6p + 5 = 0. (p-1)(p-5) = 0. Jadi p=1 atau p=5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar untuk menentukan kedudukan garis terhadap lingkaran dengan menggunakan syarat diskriminan nol (D=0) setelah substitusi, yang merupakan prosedur rutin dalam kurikulum kelas 12.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L≡x^2+y^2-2x-4y+3=0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma mencari garis singgung lingkaran melalui substitusi dan syarat diskriminan.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L≡x^2+y^2-2x-4y+3=0.
- Intended difficulty `classify/Medium`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 12. Langkah-langkahnya rutin (substitusi, ekspansi aljabar, syarat D=0, faktorisasi) tanpa memerlukan strategi non-rutin.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L≡x^2+y^2-2x-4y+3=0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran, substitusi aljabar, dan syarat diskriminan persamaan kuadrat. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun prosedural, soal ini memerlukan ketelitian dalam manipulasi aljabar dan pemahaman syarat garis singgung, yang sesuai dengan tingkat kesulitan menengah untuk kelas 12. |

Run 3 — solusi: Substitusi y = -x + p ke x^2 + y^2 - 2x - 4y + 3 = 0 menghasilkan x^2 + (-x+p)^2 - 2x - 4(-x+p) + 3 = 0, disederhanakan menjadi 2x^2 + (2-2p)x + (p^2-4p+3) = 0. Syarat menyinggung adalah diskriminan D = 0. D = (2-2p)^2 - 4(2)(p^2-4p+3) = 0. 4(1-p)^2 - 8(p^2-4p+3) = 0. (1-2p+p^2) - 2(p^2-4p+3) = 0. 1-2p+p^2-2p^2+8p-6 = 0. -p^2+6p-5 = 0. p^2-6p+5 = 0. (p-1)(p-5) = 0. Jadi, p=1 atau p=5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar (substitusi dan syarat diskriminan D=0) untuk menentukan parameter garis singgung pada lingkaran. Ini adalah penerapan prosedur rutin dalam konteks geometri analitik.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L=x^2+y^2-2x-4y+3=0
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian kedudukan garis terhadap lingkaran menggunakan diskriminan.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L=x^2+y^2-2x-4y+3=0
- Intended difficulty `classify/Medium`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 12. Langkah-langkahnya rutin (substitusi, ekspansi aljabar, syarat diskriminan, faktorisasi) tanpa memerlukan strategi nonrutin.. Bukti: Tentukan nilai p agar garis y=-x+p menyinggung lingkaran L=x^2+y^2-2x-4y+3=0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran, substitusi aljabar, syarat diskriminan persamaan kuadrat. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi garis singgung lingkaran adalah topik standar kelas 12. Tingkat kesulitan Medium diberikan karena melibatkan beberapa langkah aljabar yang saling terkait (substitusi, penyederhanaan, diskriminan) yang memerlukan ketelitian, namun prosedurnya sangat rutin. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Kedudukan Titik dan Garis terhadap Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan nilai $p$ agar garis $y=-x+p$ menyinggung lingkaran $L\equiv x^2+y^2-2x-4y+3=0$.
Pilihan: A. $p=1$ atau $p=3$
B. $p=1$ atau $p=5$
C. $p=-1$ atau $p=-5$
D. $p=3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `7e7333f61e09f38a74e01269`

Diketahui persamaan lingkaran $L\equiv x^2+y^2+4x-y+1=0$. Tentukan kedudukan garis berikut terhadap lingkaran $L$.<br><br>Tentukan kedudukan garis $k: x=0$ terhadap lingkaran $L\equiv x^2+y^2+4x-y+1=0$.

| Opsi | Isi |
|---|---|
| A | menyinggung lingkaran ($D=0$) |
| B | berimpit dengan lingkaran |
| C | tidak memotong maupun menyinggung ($D<0$) |
| D | memotong di dua titik ($D>0$) |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Substitusi x=0 ke persamaan lingkaran menghasilkan y^2-y+1=0. Diskriminan D = (-1)^2 - 4(1)(1) = 1 - 4 = -3. Karena D < 0, garis tidak memotong lingkaran.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d5d9c65810f985befd4eb6500d33e177c59c1948923d3e6f1f16edc6c0867683`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2893 |
| 2 | success | valid / verified | applying | procedural | Easy | 2777 |
| 3 | success | valid / verified | applying | procedural | Easy | 2967 |

Run 1 — solusi: Substitusi x=0 ke persamaan lingkaran menghasilkan y^2-y+1=0. Diskriminan D = (-1)^2 - 4(1)(1) = 1 - 4 = -3. Karena D < 0, garis tidak memotong lingkaran.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur substitusi garis ke persamaan lingkaran dan menggunakan diskriminan untuk menentukan kedudukan garis.. Bukti: Substitusi x=0 ke persamaan lingkaran; y^2-y+1=0; Diskriminan D = (-1)^2 - 4(1)(1) = 1 - 4 = -3
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang substitusi variabel dan konsep diskriminan untuk menentukan posisi relatif garis terhadap kurva.. Bukti: persamaan lingkaran L = x^2+y^2+4x-y+1=0; kedudukan garis k: x=0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu substitusi sederhana dan perhitungan diskriminan dasar.. Bukti: x^2+y^2+4x-y+1=0; x=0; y^2-y+1=0; D = -3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang persamaan lingkaran dan syarat kedudukan garis (diskriminan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah standar kelas 12 Matematika Tingkat Lanjut, namun prosedurnya sangat mendasar dan familiar. |

Run 2 — solusi: Substitusi x=0 ke persamaan lingkaran menghasilkan y^2-y+1=0. Diskriminan persamaan kuadrat tersebut adalah D = (-1)^2 - 4(1)(1) = 1 - 4 = -3. Karena D < 0, garis tidak memotong maupun menyinggung lingkaran.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur substitusi garis ke persamaan lingkaran dan menganalisis diskriminan untuk menentukan kedudukan garis.. Bukti: Tentukan kedudukan garis k: x=0 terhadap lingkaran L
- Dimensi pengetahuan `classify/procedural`: Melibatkan pemahaman prosedural tentang cara menentukan kedudukan garis terhadap lingkaran melalui substitusi dan analisis diskriminan.. Bukti: x^2+y^2+4x-y+1=0; x=0
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam geometri analitik lingkaran. Siswa hanya perlu melakukan substitusi sederhana dan menghitung diskriminan.. Bukti: x^2+y^2+4x-y+1=0; x=0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang persamaan lingkaran dan diskriminan persamaan kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Prosedur substitusi dan analisis diskriminan adalah materi rutin di kelas 11/12 TL. |

Run 3 — solusi: Substitusi x=0 ke persamaan lingkaran menghasilkan y^2-y+1=0. Diskriminan D = (-1)^2 - 4(1)(1) = -3. Karena D < 0, garis tidak memotong maupun menyinggung lingkaran.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur substitusi garis ke persamaan lingkaran dan menganalisis diskriminan untuk menentukan kedudukan garis.. Bukti: Tentukan kedudukan garis k: x=0 terhadap lingkaran L: x^2+y^2+4x-y+1=0.
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang substitusi variabel dan penggunaan diskriminan untuk menentukan hubungan geometris.. Bukti: Tentukan kedudukan garis k: x=0 terhadap lingkaran L: x^2+y^2+4x-y+1=0.
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam materi lingkaran kelas 12. Langkah-langkahnya rutin dan tidak memerlukan strategi kompleks.. Bukti: Tentukan kedudukan garis k: x=0 terhadap lingkaran L: x^2+y^2+4x-y+1=0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang persamaan lingkaran dan diskriminan persamaan kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah standar kurikulum kelas 12 TL, menggunakan prosedur rutin substitusi dan analisis diskriminan. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Kedudukan Titik dan Garis terhadap Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui persamaan lingkaran $L\equiv x^2+y^2+4x-y+1=0$. Tentukan kedudukan garis berikut terhadap lingkaran $L$.

Tentukan kedudukan garis $k: x=0$ terhadap lingkaran $L\equiv x^2+y^2+4x-y+1=0$.
Pilihan: A. menyinggung lingkaran ($D=0$)
B. berimpit dengan lingkaran
C. tidak memotong maupun menyinggung ($D<0$)
D. memotong di dua titik ($D>0$)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `e8b13b3498b760177a7fe083`

Diketahui persamaan lingkaran $L\equiv \left(x-\tfrac12\right)^2+\left(y+1\tfrac12\right)^2-16=0$. Tentukan persamaan garis singgung suatu lingkaran $L$ jika kemiringannya diketahui.<br><br>Tentukan persamaan garis singgung lingkaran $L\equiv \left(x-\tfrac12\right)^2+\left(y+1\tfrac12\right)^2-16=0$ jika kemiringannya $2$.

| Opsi | Isi |
|---|---|
| A | $y=2x-\tfrac52+4\sqrt3$ dan $y=2x-\tfrac52-4\sqrt3$ |
| B | $y=\tfrac12x-\tfrac52+4\sqrt5$ dan $y=\tfrac12x-\tfrac52-4\sqrt5$ |
| C | $y=2x+\tfrac52+4\sqrt5$ dan $y=2x+\tfrac52-4\sqrt5$ |
| D | $y=2x-\tfrac52+4\sqrt5$ dan $y=2x-\tfrac52-4\sqrt5$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Lingkaran (x-1/2)^2 + (y+3/2)^2 = 16 memiliki pusat (1/2, -3/2) dan r=4. Rumus garis singgung dengan gradien m=2 adalah y-b = m(x-a) ± r*sqrt(m^2+1). Substitusi: y - (-3/2) = 2(x - 1/2) ± 4*sqrt(2^2+1) => y + 3/2 = 2x - 1 ± 4*sqrt(5) => y = 2x - 5/2 ± 4*sqrt(5).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `956f0700a38aaa37aa29afc5e2418b7d2d071c16dd920e7d8b200fdd14d6860f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2345 |
| 2 | success | valid / verified | applying | procedural | Easy | 2292 |
| 3 | success | valid / verified | applying | procedural | Easy | 2356 |

Run 1 — solusi: Lingkaran (x-1/2)^2 + (y+3/2)^2 = 16 memiliki pusat (1/2, -3/2) dan r=4. Rumus garis singgung dengan gradien m=2 adalah y-b = m(x-a) ± r*sqrt(m^2+1). Substitusi: y - (-3/2) = 2(x - 1/2) ± 4*sqrt(2^2+1) => y + 3/2 = 2x - 1 ± 4*sqrt(5) => y = 2x - 5/2 ± 4*sqrt(5).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus garis singgung lingkaran dengan gradien tertentu. Ini adalah prosedur standar dalam geometri analitik lingkaran yang dipelajari di kelas 12.. Bukti: Tentukan persamaan garis singgung lingkaran L=(x-1/2)^2+(y+1 1/2)^2-16=0 jika kemiringannya 2.
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman dan penerapan algoritma atau rumus spesifik untuk menentukan persamaan garis singgung lingkaran.. Bukti: rumus y-b=m(x-a)±r*sqrt(m^2+1)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi parameter lingkaran (pusat dan jari-jari) dan menerapkan rumus garis singgung dengan gradien m yang diberikan. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: kemiringannya 2; L=(x-1/2)^2+(y+1 1/2)^2-16=0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran dan rumus garis singgung lingkaran dengan gradien m. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi garis singgung lingkaran dengan gradien m adalah prosedur standar di kelas 12 Matematika Tingkat Lanjut. |

Run 2 — solusi: Lingkaran (x-1/2)^2 + (y+3/2)^2 = 16 memiliki pusat (1/2, -3/2) dan r=4. Rumus garis singgung dengan gradien m=2 adalah y-b = m(x-a) ± r√(m^2+1). Substitusi: y - (-3/2) = 2(x - 1/2) ± 4√(2^2+1) => y + 3/2 = 2x - 1 ± 4√5 => y = 2x - 5/2 ± 4√5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus garis singgung lingkaran dengan gradien tertentu. Ini adalah prosedur standar yang melibatkan substitusi parameter ke dalam rumus yang sudah dikenal.. Bukti: Tentukan persamaan garis singgung lingkaran L... jika kemiringannya 2
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus garis singgung lingkaran yang melibatkan gradien, pusat, dan jari-jari.. Bukti: rumus y-b=m(x-a)± r√(m^2+1)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi pusat, jari-jari, dan gradien, lalu mensubstitusikannya ke dalam rumus yang sudah baku. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: Tentukan persamaan garis singgung lingkaran L... jika kemiringannya 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran dan rumus garis singgung dengan gradien m. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi garis singgung lingkaran dengan gradien m adalah prosedur standar di kelas 12 Matematika Tingkat Lanjut. |

Run 3 — solusi: Persamaan garis singgung lingkaran (x-a)^2+(y-b)^2=r^2 dengan gradien m adalah y-b=m(x-a)±r√(m^2+1). Diketahui a=1/2, b=-3/2, r=4, m=2. Maka y-(-3/2)=2(x-1/2)±4√(2^2+1) => y+3/2=2x-1±4√5 => y=2x-1-3/2±4√5 => y=2x-5/2±4√5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus standar garis singgung lingkaran dengan gradien tertentu. Ini adalah prosedur rutin yang memerlukan pemilihan rumus yang tepat dan substitusi nilai parameter.. Bukti: Tentukan persamaan garis singgung lingkaran L≡(x-1/2)^2+(y+1 1/2)^2-16=0 jika kemiringannya 2.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus garis singgung lingkaran yang melibatkan parameter pusat, jari-jari, dan gradien.. Bukti: rumus y-b=m(x-a)±r√(m^2+1)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mengidentifikasi parameter (a, b, r, m) dari persamaan yang diberikan dan mensubstitusikannya ke dalam rumus standar garis singgung lingkaran. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: Tentukan persamaan garis singgung lingkaran L≡(x-1/2)^2+(y+1 1/2)^2-16=0 jika kemiringannya 2.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran, konsep gradien, dan rumus garis singgung lingkaran. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi garis singgung lingkaran dengan gradien m adalah standar kurikulum kelas 12 TL. Prosedur ini sangat familiar dan langsung. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Persamaan Garis Singgung Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui persamaan lingkaran $L\equiv \left(x-\tfrac12\right)^2+\left(y+1\tfrac12\right)^2-16=0$. Tentukan persamaan garis singgung suatu lingkaran $L$ jika kemiringannya diketahui.

Tentukan persamaan garis singgung lingkaran $L\equiv \left(x-\tfrac12\right)^2+\left(y+1\tfrac12\right)^2-16=0$ jika kemiringannya $2$.
Pilihan: A. $y=2x-\tfrac52+4\sqrt3$ dan $y=2x-\tfrac52-4\sqrt3$
B. $y=\tfrac12x-\tfrac52+4\sqrt5$ dan $y=\tfrac12x-\tfrac52-4\sqrt5$
C. $y=2x+\tfrac52+4\sqrt5$ dan $y=2x+\tfrac52-4\sqrt5$
D. $y=2x-\tfrac52+4\sqrt5$ dan $y=2x-\tfrac52-4\sqrt5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `900355eb77ace3e6da74cb01`

Tunjukkan bahwa titik $A(6,-8)$ terletak pada lingkaran $L\equiv x^2+y^2=100$, kemudian tentukan persamaan garis singgungnya.

| Opsi | Isi |
|---|---|
| A | $6x-8y-100=0$ |
| B | $6x-8y+100=0$ |
| C | $8x-6y-100=0$ |
| D | $6x+8y-100=0$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Substitusi titik (6,-8) ke x^2+y^2=100 menghasilkan 36+64=100, terbukti titik pada lingkaran. Persamaan garis singgung di (x1,y1) pada lingkaran x^2+y^2=r^2 adalah xx1+yy1=r^2. Substitusi (6,-8) menghasilkan 6x-8y=100, atau 6x-8y-100=0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi', 'membuktikan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b7d0eedaa06ac1e71c597285ee2b47349c68ecdf1e82063f6e45b800c1ba4e3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2170 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2149 |
| 3 | success | valid / verified | applying | procedural | Easy | 2166 |

Run 1 — solusi: Substitusi titik (6,-8) ke x^2+y^2: 6^2+(-8)^2 = 36+64 = 100. Karena sama dengan 100, titik terletak pada lingkaran. Persamaan garis singgung di (x1, y1) pada x^2+y^2=r^2 adalah xx1+yy1=r^2. Substitusi (6,-8): 6x-8y=100 atau 6x-8y-100=0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar untuk mengecek posisi titik pada lingkaran (substitusi) dan menggunakan rumus garis singgung lingkaran yang berpusat di (0,0). Ini adalah penerapan prosedur rutin.. Bukti: Tunjukkan bahwa titik A(6,-8) terletak pada lingkaran L=x^2+y^2=100; tentukan persamaan garis singgungnya
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antara persamaan lingkaran dan rumus garis singgungnya, yang merupakan konsep prosedural dalam geometri analitik.. Bukti: persamaan garis singgungnya; x^2+y^2=100
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan substitusi untuk verifikasi dan menerapkan rumus garis singgung standar. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: Tunjukkan bahwa titik A(6,-8) terletak pada lingkaran L=x^2+y^2=100; tentukan persamaan garis singgungnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran pusat (0,0) dan rumus garis singgung titik singgung. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan standar kurikulum kelas 12 Matematika Tingkat Lanjut. Prosedur yang digunakan sangat familiar dan tidak memerlukan langkah analisis yang mendalam. |

Run 2 — solusi: Substitusi titik (6,-8) ke x^2+y^2=100 menghasilkan 36+64=100, terbukti titik pada lingkaran. Persamaan garis singgung di (x1,y1) adalah xx1+yy1=r^2. Maka 6x+(-8)y=100, atau 6x-8y-100=0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar untuk mengecek posisi titik pada lingkaran (substitusi) dan menggunakan rumus persamaan garis singgung lingkaran yang berpusat di (0,0). Ini adalah penerapan prosedur rutin.. Bukti: Tunjukkan bahwa titik A(6,-8) terletak pada lingkaran L=x^2+y^2=100; tentukan persamaan garis singgungnya
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang hubungan antara titik pada lingkaran dan persamaan garis singgungnya, yang merupakan konsep dasar geometri analitik.. Bukti: persamaan garis singgungnya; x^2+y^2=100
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Prosedur pengecekan titik dan penggunaan rumus garis singgung adalah standar dan langsung.. Bukti: Tunjukkan bahwa titik A(6,-8) terletak pada lingkaran L=x^2+y^2=100; tentukan persamaan garis singgungnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran pusat (0,0) dan rumus garis singgung di titik (x1,y1). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah standar kurikulum kelas 12 Matematika Tingkat Lanjut, namun prosedurnya sangat langsung dan familiar. |

Run 3 — solusi: Substitusi titik (6,-8) ke x^2+y^2=100 menghasilkan 36+64=100, terbukti titik pada lingkaran. Persamaan garis singgung di (x1,y1) adalah xx1+yy1=r^2. Dengan (x1,y1)=(6,-8) dan r^2=100, diperoleh 6x-8y=100 atau 6x-8y-100=0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar untuk mengecek posisi titik (substitusi) dan menggunakan rumus garis singgung lingkaran yang berpusat di (0,0). Ini adalah penerapan prosedur rutin.. Bukti: Tunjukkan bahwa titik A(6,-8) terletak pada lingkaran L=x^2+y^2=100; tentukan persamaan garis singgungnya
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antara persamaan lingkaran dan rumus garis singgung pada titik tertentu, yang merupakan pengetahuan konseptual dan prosedural.. Bukti: x^2+y^2=100; persamaan garis singgungnya
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Prosedur pengecekan titik dan penggunaan rumus garis singgung adalah standar dalam kurikulum.. Bukti: Tunjukkan bahwa titik A(6,-8) terletak pada lingkaran L=x^2+y^2=100; tentukan persamaan garis singgungnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran pusat (0,0) dan rumus garis singgung di titik (x1,y1). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah standar dasar geometri analitik di kelas 12, tidak memerlukan strategi non-rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3855`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur standar untuk mengecek posisi titik pada lingkaran (substitusi) dan menggunakan rumus garis singgung lingkaran yang berpusat di (0,0). Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritma standar (substitusi dan rumus garis singgung) untuk menyelesaikan masalah geometri analitik.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Prosedur pengecekan titik dan penggunaan rumus garis singgung adalah standar dan langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Persamaan lingkaran pusat (0,0) dan rumus garis singgung di titik (x1,y1). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah standar kurikulum kelas 12 Matematika Tingkat Lanjut, namun prosedurnya sangat langsung dan familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Persamaan Garis Singgung Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Tunjukkan bahwa titik $A(6,-8)$ terletak pada lingkaran $L\equiv x^2+y^2=100$, kemudian tentukan persamaan garis singgungnya.
Pilihan: A. $6x-8y-100=0$
B. $6x-8y+100=0$
C. $8x-6y-100=0$
D. $6x+8y-100=0$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `9d3b005f20ecd5dabca2aa9e`

Jika AD = 3 cm dan BE = AD, tentukan:<br><br>besar `∠` BAE

| Opsi | Isi |
|---|---|
| A | 45° |
| B | 90° |
| C | 120° |
| D | 60° |

![Gambar sumber soal 9](<../../../images/kelas11_panduan_siswa_kelas11.pdf-0089-05.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `60°`.
Solusi minimum hasil AI: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Karena AE = AB = BE = 3 cm, segitiga ABE adalah segitiga sama sisi. Oleh karena itu, besar ∠BAE = 60°.
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0089-05.png. Transkripsi visual: Sebuah lingkaran dengan pusat A. Titik D, E, dan B terletak pada keliling lingkaran. Ruas garis AD adalah jari-jari. Ruas garis AE dan AB juga jari-jari. Segitiga ABE terbentuk dengan sisi AE, AB, dan BE.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ab545119d728fd45aeefbc174fccf8eb5d5befa74ec9b00d6615fedf7e20fdf6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3199 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3257 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3302 |

Run 1 — solusi: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Karena AE = AB = BE = 3 cm, segitiga ABE adalah segitiga sama sisi. Oleh karena itu, besar ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat jari-jari lingkaran (konseptual) dan menerapkan sifat segitiga sama sisi untuk menentukan besar sudut (applying).. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); karena BE=AD=3 cm juga, maka AE=AB=BE=3 cm dan segitiga ABE sama sisi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi jari-jari lingkaran dan sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran; segitiga ABE sama sisi
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang jari-jari lingkaran dan segitiga sama sisi.. Bukti: AD = 3 cm dan BE = AD; tentukan besar ∠BAE

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
| gradeRelativeRationale | Meskipun untuk kelas 12, soal ini sangat mendasar dan tidak memerlukan konsep matematika tingkat lanjut (TL) yang kompleks. |

Run 2 — solusi: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Maka segitiga ABE memiliki sisi-sisi AE = AB = BE = 3 cm, yang berarti segitiga ABE adalah segitiga sama sisi. Oleh karena itu, besar ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti jari-jari lingkaran untuk menentukan panjang sisi segitiga dan mengenali sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); karena BE=AD=3 cm juga, maka AE=AB=BE=3 cm dan segitiga ABE sama sisi
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang sifat jari-jari lingkaran dan klasifikasi segitiga berdasarkan panjang sisinya.. Bukti: AE=AB=AD=3 cm (radius); segitiga ABE sama sisi, sehingga ∠BAE=60°
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang melibatkan pengenalan sifat dasar lingkaran (jari-jari) dan segitiga sama sisi. Tidak ada langkah non-rutin atau kompleksitas tinggi.. Bukti: AD = 3 cm dan BE = AD; AE=AB=AD=3 cm (radius); segitiga ABE sama sisi

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
| gradeRelativeRationale | Meskipun materi lingkaran diajarkan di kelas 11/12, soal ini sangat mendasar dan tidak memerlukan teknik kalkulus atau geometri lanjut yang menjadi standar TL kelas 12. |

Run 3 — solusi: A adalah pusat lingkaran, maka AE = AB = AD = 3 cm (jari-jari). Diketahui BE = AD = 3 cm. Segitiga ABE memiliki sisi AE = AB = BE = 3 cm, sehingga segitiga ABE adalah segitiga sama sisi. Maka ∠BAE = 60°.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi properti jari-jari lingkaran untuk menentukan panjang sisi segitiga dan mengenali sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); karena BE=AD=3 cm juga, maka AE=AB=BE=3 cm dan segitiga ABE sama sisi
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi jari-jari lingkaran dan sifat segitiga sama sisi.. Bukti: A adalah pusat lingkaran sehingga AE=AB=AD=3 cm (radius); segitiga ABE sama sisi, sehingga ∠BAE=60°
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa SMA. Siswa hanya perlu menghubungkan definisi jari-jari dengan panjang sisi segitiga untuk menyimpulkan jenis segitiga.. Bukti: AD = 3 cm dan BE = AD; A adalah pusat lingkaran

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
| gradeRelativeRationale | Meskipun materi lingkaran diajarkan di kelas 11, soal ini sangat mendasar dan prosedural, sehingga dikategorikan Easy untuk kelas 12. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Lingkaran dan Tali Busur
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika AD = 3 cm dan BE = AD, tentukan:

besar `∠` BAE
Pilihan: A. 45°
B. 90°
C. 120°
D. 60°
Transkripsi visual: Sebuah lingkaran dengan pusat A. Titik D, E, dan B terletak pada keliling lingkaran. Ruas garis AD adalah jari-jari. Ruas garis AE dan AB juga jari-jari. Segitiga ABE terbentuk dengan sisi AE, AB, dan BE.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `a74ab5c43d2351a59d9fc0af`

Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.<br><br>Tentukan nilai dari $\displaystyle\lim_{x\to \frac{\pi}{4}}\left(\dfrac{\sin x-\cos x}{1-\tan x}\right)$.

| Opsi | Isi |
|---|---|
| A | $-\frac{1}{2}\sqrt{2}$ |
| B | $-\sqrt{2}$ |
| C | $\frac{1}{2}\sqrt{2}$ |
| D | $-\frac{1}{2}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: lim_{x->pi/4} (sin x - cos x) / (1 - sin x / cos x) = lim_{x->pi/4} (sin x - cos x) / ((cos x - sin x) / cos x) = lim_{x->pi/4} (sin x - cos x) * cos x / -(sin x - cos x) = lim_{x->pi/4} -cos x = -cos(pi/4) = -1/2 * sqrt(2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b27b31882181bd6a033daa69fca591e11316e0da937aa91a885fb7ee7241498a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2672 |
| 2 | success | valid / verified | applying | procedural | Medium | 3031 |
| 3 | success | valid / verified | applying | procedural | Easy | 2094 |

Run 1 — solusi: Ubah tan x menjadi sin x / cos x: (sin x - cos x) / (1 - sin x / cos x) = (sin x - cos x) / ((cos x - sin x) / cos x) = (sin x - cos x) * cos x / -(sin x - cos x) = -cos x. Substitusi x = pi/4 menghasilkan -cos(pi/4) = -1/2 * sqrt(2).
- Domain kognitif `classify/applying`: Siswa perlu memilih dan menerapkan prosedur manipulasi trigonometri (mengubah tan x dan menyederhanakan pecahan) untuk menyelesaikan limit bentuk tak tentu 0/0. Ini merupakan penerapan konsep limit trigonometri yang rutin.. Bukti: Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.; lim_{x->pi/4} ((sin x - cos x) / (1 - tan x))
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma manipulasi identitas trigonometri dan teknik penyelesaian limit fungsi trigonometri.. Bukti: Gunakanlah sifat-sifat limit; lim_{x->pi/4} ((sin x - cos x) / (1 - tan x))
- Intended difficulty `classify/Medium`: Soal memerlukan manipulasi aljabar trigonometri untuk menghilangkan bentuk tak tentu. Prosedur ini familiar bagi siswa kelas 12 TL.. Bukti: lim_{x->pi/4} ((sin x - cos x) / (1 - tan x))

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Identitas trigonometri dasar dan limit fungsi trigonometri. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan standar dalam kurikulum matematika tingkat lanjut kelas 12 mengenai limit fungsi trigonometri. |

Run 2 — solusi: Substitusi tan x = sin x / cos x menghasilkan (sin x - cos x) / ((cos x - sin x) / cos x) = -cos x. Limit x -> pi/4 dari -cos x adalah -cos(pi/4) = -1/2 * sqrt(2).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan identitas trigonometri (tan x = sin x/cos x) dan manipulasi aljabar untuk menyelesaikan bentuk tak tentu 0/0. Ini adalah prosedur rutin dalam kalkulus SMA.. Bukti: Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.; lim_{x->pi/4} ((sin x - cos x) / (1 - tan x))
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma manipulasi aljabar dan identitas trigonometri untuk menyederhanakan limit fungsi.. Bukti: Gunakanlah sifat-sifat limit; lim_{x->pi/4} ((sin x - cos x) / (1 - tan x))
- Intended difficulty `classify/Medium`: Soal memerlukan manipulasi aljabar trigonometri (mengubah tan x menjadi sin x/cos x) sebelum limit dapat dihitung. Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: lim_{x->pi/4} ((sin x - cos x) / (1 - tan x))

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Identitas trigonometri dasar (tan x = sin x/cos x) dan konsep limit fungsi trigonometri. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan mampu melakukan manipulasi aljabar trigonometri untuk menyelesaikan limit bentuk tak tentu. |

Run 3 — solusi: lim_{x->pi/4} (sin x - cos x) / (1 - sin x / cos x) = lim_{x->pi/4} (sin x - cos x) / ((cos x - sin x) / cos x) = lim_{x->pi/4} (sin x - cos x) * cos x / -(sin x - cos x) = lim_{x->pi/4} -cos x = -cos(pi/4) = -1/2 * sqrt(2).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan manipulasi aljabar trigonometri (identitas tan x = sin x / cos x) dan sifat limit untuk menyelesaikan bentuk tak tentu 0/0. Ini adalah prosedur rutin dalam kurikulum matematika tingkat lanjut.. Bukti: lim_{x->pi/4}(dfrac{sin x-cos x}{1-tan x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang manipulasi identitas trigonometri dan teknik limit untuk menyelesaikan bentuk tak tentu.. Bukti: sifat-sifat limit; 1-tan x
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam kalkulus SMA kelas 12. Langkah-langkahnya rutin (mengubah tan x, menyederhanakan pecahan kompleks, substitusi nilai limit).. Bukti: lim_{x->pi/4}(dfrac{sin x-cos x}{1-tan x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Identitas trigonometri dasar dan sifat limit fungsi trigonometri. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi limit fungsi trigonometri adalah topik inti kelas 12 TL. Prosedur penyelesaiannya bersifat rutin dan tidak memerlukan strategi non-rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3731`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur rutin berupa manipulasi identitas trigonometri (tan x = sin x / cos x) dan penyederhanaan aljabar untuk menyelesaikan bentuk tak tentu 0/0. Ini adalah penerapan konsep limit trigonometri yang standar.
- Dimensi pengetahuan `procedural`: Soal menguji penguasaan algoritma manipulasi identitas trigonometri dan teknik limit fungsi trigonometri.
- Intended difficulty `Easy`: Soal ini merupakan prosedur standar dalam kalkulus SMA kelas 12. Langkah-langkahnya rutin (mengubah tan x, menyederhanakan pecahan kompleks, substitusi nilai limit) dan tidak memerlukan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Identitas trigonometri dasar dan sifat limit fungsi trigonometri. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi limit fungsi trigonometri adalah topik inti kelas 12 TL. Prosedur penyelesaiannya bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Definisi Turunan Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.

Tentukan nilai dari $\displaystyle\lim_{x\to \frac{\pi}{4}}\left(\dfrac{\sin x-\cos x}{1-\tan x}\right)$.
Pilihan: A. $-\frac{1}{2}\sqrt{2}$
B. $-\sqrt{2}$
C. $\frac{1}{2}\sqrt{2}$
D. $-\frac{1}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `915c9b6e3d6efd2eb9ea0a6c`

Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.<br><br>Tentukan nilai dari $\displaystyle\lim_{x\to 3}(x^2+2)$.

| Opsi | Isi |
|---|---|
| A | $5$ |
| B | $11$ |
| C | $7$ |
| D | $25$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `11`.
Solusi minimum hasil AI: Substitusi langsung nilai x=3 ke dalam fungsi: 3^2 + 2 = 9 + 2 = 11.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad9d90f24c09c160b71299d96d1a9bb735869eac8d11c65bf09d0b36810b357c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2479 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3144 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2778 |

Run 1 — solusi: Substitusi langsung nilai x=3 ke dalam fungsi: 3^2 + 2 = 9 + 2 = 11.
- Domain kognitif `classify/knowing`: Soal hanya meminta evaluasi limit fungsi polinomial sederhana dengan substitusi langsung, yang merupakan prosedur dasar dan familiar.. Bukti: Tentukan nilai dari $\displaystyle\lim_{x\to 3}(x^2+2)$.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan prosedur substitusi langsung untuk mengevaluasi limit fungsi polinomial.. Bukti: Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk materi limit di kelas 12, hanya memerlukan substitusi langsung tanpa manipulasi aljabar yang kompleks.. Bukti: Tentukan nilai dari $\displaystyle\lim_{x\to 3}(x^2+2)$.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang limit fungsi polinomial dan operasi aritmatika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk materi limit di kelas 12, hanya memerlukan substitusi langsung tanpa manipulasi aljabar yang kompleks. |

Run 2 — solusi: Substitusi langsung x=3 ke dalam fungsi: 3^2 + 2 = 9 + 2 = 11.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan sifat substitusi langsung pada limit fungsi polinomial yang kontinu.. Bukti: Tentukan nilai dari $\displaystyle\lim_{x\to 3}(x^2+2)$
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang sifat limit fungsi polinomial.. Bukti: Gunakanlah sifat-sifat limit; $\displaystyle\lim_{x\to 3}(x^2+2)$
- Intended difficulty `classify/Easy`: Soal ini sangat dasar, hanya memerlukan satu langkah substitusi langsung tanpa manipulasi aljabar yang kompleks.. Bukti: $\displaystyle\lim_{x\to 3}(x^2+2)$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang limit fungsi polinomial dan substitusi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun ini materi kelas 11/12, tingkat kesulitannya sangat rendah untuk standar kelas 12 TL. |

Run 3 — solusi: Substitusi langsung x=3 ke dalam fungsi: 3^2 + 2 = 9 + 2 = 11.
- Domain kognitif `classify/knowing`: Soal meminta evaluasi limit fungsi polinomial sederhana dengan substitusi langsung, yang merupakan proses prosedural dasar.. Bukti: Tentukan nilai dari $\displaystyle\lim_{x\to 3}(x^2+2)$.
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan aturan substitusi langsung pada limit fungsi polinomial.. Bukti: Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah substitusi langsung tanpa kendala atau strategi kompleks.. Bukti: Tentukan nilai dari $\displaystyle\lim_{x\to 3}(x^2+2)$.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Substitusi nilai pada fungsi polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Evaluasi limit dengan substitusi langsung adalah prosedur standar yang sangat familiar bagi siswa kelas 12. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Definisi Turunan Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut.

Tentukan nilai dari $\displaystyle\lim_{x\to 3}(x^2+2)$.
Pilihan: A. $5$
B. $11$
C. $7$
D. $25$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `f55a3e3b176f4ad014bc0992`

Diketahui persamaan fungsi trigonometri $f(x)=2-2\sin\left(\frac{1}{2}\pi x\right)$ didefinisikan pada daerah asal $D_f=\{x\mid 0\le x\le 4, x\in R\}$.<br><br>Jika $f'(x)$ bernilai nol pada $x=x_1$ dan $x=x_2$, tentukan nilai dari $x_1^2+x_2^2$.

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $17$ |
| C | $10$ |
| D | $20$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `10`.
Solusi minimum hasil AI: f'(x) = -2 * cos(1/2 * pi * x) * (1/2 * pi) = -pi * cos(1/2 * pi * x). Setting f'(x) = 0 implies cos(1/2 * pi * x) = 0. For 0 <= x <= 4, 1/2 * pi * x is in [0, 2pi]. cos(theta) = 0 at theta = pi/2 and 3pi/2. Thus, 1/2 * pi * x = pi/2 => x = 1, and 1/2 * pi * x = 3pi/2 => x = 3. Then x1^2 + x2^2 = 1^2 + 3^2 = 1 + 9 = 10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `40c7e14960f0eb0e091773ad479d5c0b26945132d500922c30768a0bbb6f58fe`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2316 |
| 2 | success | valid / verified | applying | procedural | Easy | 2290 |
| 3 | success | valid / verified | applying | procedural | Easy | 2239 |

Run 1 — solusi: f'(x) = -2 * cos(1/2 * pi * x) * (1/2 * pi) = -pi * cos(1/2 * pi * x). Setting f'(x) = 0 implies cos(1/2 * pi * x) = 0. For 0 <= x <= 4, 1/2 * pi * x is in [0, 2pi]. cos(theta) = 0 at theta = pi/2 and 3pi/2. Thus, 1/2 * pi * x = pi/2 => x = 1, and 1/2 * pi * x = 3pi/2 => x = 3. Then x1^2 + x2^2 = 1^2 + 3^2 = 1 + 9 = 10.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan rantai untuk menurunkan fungsi trigonometri dan menyelesaikan persamaan trigonometri dasar dalam interval yang diberikan. Ini adalah penerapan prosedur standar.. Bukti: f'(x) = -2 * cos(1/2 * pi * x) * (1/2 * pi); f'(x) bernilai nol pada x=x1 dan x=x2
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang turunan fungsi trigonometri dan penyelesaian persamaan trigonometri.. Bukti: f(x)=2-2sin(1/2 pi x); f'(x) bernilai nol
- Intended difficulty `classify/Easy`: Soal ini melibatkan langkah-langkah rutin: menurunkan fungsi, menyamakan dengan nol, menyelesaikan persamaan trigonometri dasar, dan menghitung nilai akhir. Tidak ada strategi non-rutin yang diperlukan.. Bukti: f(x)=2-2sin(1/2 pi x); 0 <= x <= 4; f'(x) bernilai nol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan rantai turunan trigonometri dan penyelesaian persamaan cosinus dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi turunan fungsi trigonometri adalah standar kurikulum kelas 12 TL. Prosedur yang diminta bersifat langsung dan familiar bagi siswa. |

Run 2 — solusi: f'(x) = -2 * cos(1/2 * pi * x) * (1/2 * pi) = -pi * cos(1/2 * pi * x). Setting f'(x) = 0 implies cos(1/2 * pi * x) = 0. Within 0 <= x <= 4, 1/2 * pi * x = pi/2 or 3pi/2. Thus, x1 = 1 and x2 = 3. Then x1^2 + x2^2 = 1^2 + 3^2 = 1 + 9 = 10.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan rantai untuk menurunkan fungsi trigonometri dan menyelesaikan persamaan trigonometri dasar dalam interval yang diberikan. Ini adalah prosedur standar dalam kalkulus SMA kelas 12.. Bukti: f'(x) = -2 * cos(1/2 * pi * x) * (1/2 * pi); f'(x) bernilai nol pada x=x1 dan x=x2
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang teknik turunan (aturan rantai) dan penyelesaian persamaan trigonometri.. Bukti: f(x)=2-2\sin\left(\frac{1}{2}\pi x\right); f'(x) bernilai nol
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Prosedur turunan dan penyelesaian persamaan trigonometri dasar adalah materi standar yang sering dilatih.. Bukti: f(x)=2-2\sin\left(\frac{1}{2}\pi x\right); D_f={x\| 0<=x<=4, x in R}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan rantai turunan fungsi trigonometri dan penyelesaian persamaan cosinus dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi turunan trigonometri dan penyelesaian persamaan trigonometri pada interval tertentu merupakan kurikulum inti kelas 12 TL. |

Run 3 — solusi: f(x) = 2 - 2sin(0.5πx). f'(x) = -2 * cos(0.5πx) * (0.5π) = -π * cos(0.5πx). f'(x) = 0 implies cos(0.5πx) = 0. Within 0 ≤ x ≤ 4, 0.5πx = 0.5π or 1.5π. Thus, x1 = 1 and x2 = 3. x1² + x2² = 1² + 3² = 1 + 9 = 10.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan rantai untuk menurunkan fungsi trigonometri dan menyelesaikan persamaan trigonometri dasar dalam interval yang diberikan. Ini adalah prosedur standar dalam kalkulus SMA kelas 12.. Bukti: f'(x) bernilai nol pada x=x1 dan x2; f(x)=2-2sin(1/2πx)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang turunan fungsi trigonometri dan penyelesaian persamaan trigonometri.. Bukti: f(x)=2-2sin(1/2πx); f'(x) bernilai nol
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin (turunan fungsi komposisi dan akar persamaan trigonometri) dengan beban komputasi rendah dan domain yang terbatas.. Bukti: f(x)=2-2sin(1/2πx); 0≤x≤4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Turunan fungsi trigonometri (aturan rantai) dan penyelesaian persamaan cosinus dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi turunan fungsi trigonometri adalah standar kurikulum kelas 12 TL. Prosedur yang digunakan bersifat langsung dan familiar bagi siswa. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Sifat-Sifat Turunan Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui persamaan fungsi trigonometri $f(x)=2-2\sin\left(\frac{1}{2}\pi x\right)$ didefinisikan pada daerah asal $D_f=\{x\mid 0\le x\le 4, x\in R\}$.

Jika $f'(x)$ bernilai nol pada $x=x_1$ dan $x=x_2$, tentukan nilai dari $x_1^2+x_2^2$.
Pilihan: A. $4$
B. $17$
C. $10$
D. $20$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `dc30e9ea3f84a3de8881e431`

Diketahui persamaan fungsi trigonometri $f(x)=2-2\sin\left(\frac{1}{2}\pi x\right)$ didefinisikan pada daerah asal $D_f=\{x\mid 0\le x\le 4, x\in R\}$.<br><br>Tentukan turunan pertama dari $f(x)$.

| Opsi | Isi |
|---|---|
| A | $f'(x)=-\pi\cos\left(\frac12\pi x\right)$ |
| B | $f'(x)=-2\cos\left(\frac12\pi x\right)$ |
| C | $f'(x)=-\pi\sin\left(\frac12\pi x\right)$ |
| D | $f'(x)=\pi\cos\left(\frac12\pi x\right)$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: f(x) = 2 - 2sin(1/2 * pi * x). Menggunakan aturan rantai: f'(x) = 0 - 2 * cos(1/2 * pi * x) * d/dx(1/2 * pi * x) = -2 * cos(1/2 * pi * x) * (1/2 * pi) = -pi * cos(1/2 * pi * x).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4da7cb2739cdbce3279cb53d6cf0c955c4b2cd71797e1a85ce4cef566360e5a9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2123 |
| 2 | success | valid / verified | applying | procedural | Easy | 2094 |
| 3 | success | valid / verified | applying | procedural | Easy | 2110 |

Run 1 — solusi: f(x) = 2 - 2sin(1/2 * pi * x). Menggunakan aturan rantai: f'(x) = 0 - 2 * cos(1/2 * pi * x) * d/dx(1/2 * pi * x) = -2 * cos(1/2 * pi * x) * (1/2 * pi) = -pi * cos(1/2 * pi * x).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung aturan turunan fungsi trigonometri (aturan rantai) yang merupakan prosedur standar dalam kurikulum matematika tingkat lanjut kelas 12.. Bukti: Tentukan turunan pertama dari f(x)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara fungsi trigonometri dan aturan rantai (chain rule) untuk menentukan turunan fungsi komposisi.. Bukti: f(x)=2-2sin(1/2 pi x)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan aturan rantai pada fungsi trigonometri dasar tanpa memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: f(x)=2-2sin(1/2 pi x)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan turunan fungsi trigonometri dasar dan aturan rantai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi turunan fungsi trigonometri adalah topik standar kelas 12 TL. Prosedur yang diminta adalah algoritma standar tanpa modifikasi. |

Run 2 — solusi: f(x) = 2 - 2sin(1/2 * pi * x). Menggunakan aturan rantai: f'(x) = 0 - 2 * cos(1/2 * pi * x) * d/dx(1/2 * pi * x) = -2 * cos(1/2 * pi * x) * (1/2 * pi) = -pi * cos(1/2 * pi * x).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung aturan turunan fungsi trigonometri (aturan rantai) yang merupakan prosedur standar dalam kurikulum matematika tingkat lanjut kelas 12.. Bukti: Tentukan turunan pertama dari f(x)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menerapkan algoritma turunan fungsi komposisi (aturan rantai) pada fungsi trigonometri.. Bukti: f(x)=2-2sin(1/2πx)
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang familiar bagi siswa kelas 12. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: f(x)=2-2sin(1/2πx)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan rantai turunan fungsi trigonometri |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Turunan fungsi trigonometri dengan aturan rantai adalah materi dasar yang rutin di kelas 12 TL. |

Run 3 — solusi: f(x) = 2 - 2sin((1/2)πx). Menggunakan aturan rantai: f'(x) = 0 - 2 * cos((1/2)πx) * d/dx((1/2)πx) = -2 * cos((1/2)πx) * (1/2)π = -πcos((1/2)πx).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung aturan rantai pada fungsi trigonometri sederhana. Siswa hanya perlu mengidentifikasi prosedur turunan fungsi komposisi tanpa perlu strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Tentukan turunan pertama dari f(x)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang algoritma turunan fungsi trigonometri yang melibatkan aturan rantai.. Bukti: f(x)=2-2sin(1/2πx)
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam kalkulus SMA kelas 12. Tidak ada kendala yang rumit atau langkah nonrutin yang diperlukan.. Bukti: f(x)=2-2sin(1/2πx)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan turunan fungsi trigonometri dasar dan aturan rantai. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Turunan fungsi trigonometri dengan aturan rantai adalah materi inti kelas 12 TL yang bersifat rutin. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Sifat-Sifat Turunan Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui persamaan fungsi trigonometri $f(x)=2-2\sin\left(\frac{1}{2}\pi x\right)$ didefinisikan pada daerah asal $D_f=\{x\mid 0\le x\le 4, x\in R\}$.

Tentukan turunan pertama dari $f(x)$.
Pilihan: A. $f'(x)=-\pi\cos\left(\frac12\pi x\right)$
B. $f'(x)=-2\cos\left(\frac12\pi x\right)$
C. $f'(x)=-\pi\sin\left(\frac12\pi x\right)$
D. $f'(x)=\pi\cos\left(\frac12\pi x\right)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `351e16aaccd3ba782ef3e8cb`

Tentukan interval fungsi naik dan fungsi turun pada setiap kurva berikut.<br><br>Tentukan interval fungsi naik dan fungsi turun pada kurva $f(x)=x^3-3x^2-15$.

| Opsi | Isi |
|---|---|
| A | Naik untuk $x<0$ atau $x>2$; turun untuk $0<x<2$ |
| B | Naik untuk $0<x<2$; turun untuk $x<0$ atau $x>2$ |
| C | Naik untuk $x<0$ atau $x>6$; turun untuk $0<x<6$ |
| D | Naik untuk semua $x$ kecuali $x=0$ dan $x=2$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: f'(x) = 3x^2 - 6x = 3x(x-2). Titik kritis x=0 dan x=2. Uji tanda: f'(x)>0 pada x<0 atau x>2 (fungsi naik), dan f'(x)<0 pada 0<x<2 (fungsi turun).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01ee825adcfc07b254d44db451502eb9ba5bc521dd75ad14ccbe8d3321cf242a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3112 |
| 2 | success | valid / verified | applying | procedural | Easy | 2212 |
| 3 | success | valid / verified | applying | procedural | Easy | 2134 |

Run 1 — solusi: f'(x) = 3x^2 - 6x = 3x(x-2). Titik kritis x=0 dan x=2. Uji tanda: f'(x)>0 pada x<0 atau x>2 (fungsi naik), dan f'(x)<0 pada 0<x<2 (fungsi turun).
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur standar turunan untuk menentukan interval kemonotonan fungsi dengan mencari titik kritis dan menguji tanda turunan pertama.. Bukti: f'(x)=3x^2-6x=3x(x-2); Tentukan interval fungsi naik dan fungsi turun
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma rutin (turunan, mencari akar, uji interval) untuk menyelesaikan masalah fungsi naik/turun.. Bukti: f'(x)=3x^2-6x=3x(x-2); Tentukan interval fungsi naik dan fungsi turun
- Intended difficulty `classify/Easy`: Prosedur standar yang familiar bagi siswa kelas 12, melibatkan fungsi polinomial sederhana dan langkah-langkah rutin tanpa kendala kompleks.. Bukti: f(x)=x^3-3x^2-15; Tentukan interval fungsi naik dan fungsi turun

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Turunan fungsi polinomial dan konsep fungsi naik/turun. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi turunan fungsi adalah standar kurikulum kelas 12, soal ini adalah aplikasi langsung dari definisi. |

Run 2 — solusi: Turunan pertama f(x) = x^3 - 3x^2 - 15 adalah f'(x) = 3x^2 - 6x = 3x(x-2). Titik kritis di x=0 dan x=2. Uji tanda f'(x): untuk x<0, f'(x)>0 (naik); untuk 0<x<2, f'(x)<0 (turun); untuk x>2, f'(x)>0 (naik). Jadi, naik pada x<0 atau x>2, turun pada 0<x<2.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar turunan untuk menentukan interval kemonotonan fungsi polinomial derajat tiga, yang merupakan prosedur rutin dalam kurikulum kelas 12.. Bukti: Tentukan interval fungsi naik dan fungsi turun pada kurva f(x)=x^3-3x^2-15
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma turunan dan syarat kemonotonan fungsi (prosedural) serta hubungan antara tanda turunan dengan perilaku fungsi (konseptual).. Bukti: Tentukan interval fungsi naik dan fungsi turun pada kurva f(x)=x^3-3x^2-15
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan prosedur standar (menurunkan, mencari akar, uji interval) tanpa jebakan atau kompleksitas tambahan.. Bukti: Tentukan interval fungsi naik dan fungsi turun pada kurva f(x)=x^3-3x^2-15

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi aljabar dan penyelesaian pertidaksamaan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar aplikasi turunan yang diajarkan di kelas 12, memerlukan langkah-langkah rutin yang sudah familiar bagi siswa. |

Run 3 — solusi: f'(x) = 3x^2 - 6x = 3x(x-2). Titik kritis x=0 dan x=2. Uji tanda f'(x): untuk x<0, f'(x)>0 (naik); untuk 0<x<2, f'(x)<0 (turun); untuk x>2, f'(x)>0 (naik). Jadi, naik pada x<0 atau x>2, turun pada 0<x<2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur turunan pertama untuk menentukan interval kemonotonan fungsi, yang merupakan prosedur standar dalam kalkulus SMA kelas 12.. Bukti: Tentukan interval fungsi naik dan fungsi turun pada kurva f(x)=x^3-3x^2-15.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma mencari interval fungsi naik/turun menggunakan turunan pertama.. Bukti: f'(x)=3x^2-6x=3x(x-2)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan prosedur yang jelas (turunkan, cari akar, uji tanda). Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: Tentukan interval fungsi naik dan fungsi turun pada kurva f(x)=x^3-3x^2-15.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi polinomial dan pertidaksamaan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 12 TL yang menguji penguasaan dasar aplikasi turunan. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Aplikasi Turunan Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan interval fungsi naik dan fungsi turun pada setiap kurva berikut.

Tentukan interval fungsi naik dan fungsi turun pada kurva $f(x)=x^3-3x^2-15$.
Pilihan: A. Naik untuk $x<0$ atau $x>2$; turun untuk $0<x<2$
B. Naik untuk $0<x<2$; turun untuk $x<0$ atau $x>2$
C. Naik untuk $x<0$ atau $x>6$; turun untuk $0<x<6$
D. Naik untuk semua $x$ kecuali $x=0$ dan $x=2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `2bbe6539fc13ec9fb083c7b0`

Tentukan nilai ekstrem dan jenis titik ekstremnya dari setiap fungsi berikut.<br><br>Nilai ekstrem dan jenis titik ekstrem dari $f(x)=x^2-5x+6$?

| Opsi | Isi |
|---|---|
| A | Nilai ekstrem minimum $-\frac14$ pada $x=-\frac52$ |
| B | Nilai ekstrem maksimum $-\frac14$ pada $x=\frac52$ |
| C | Nilai ekstrem minimum $\frac14$ pada $x=\frac52$ |
| D | Nilai ekstrem minimum $-\frac14$ pada $x=\frac52$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: f'(x) = 2x - 5. Titik stasioner saat f'(x) = 0, maka 2x = 5, x = 5/2. f''(x) = 2 > 0, sehingga titik tersebut adalah minimum. Nilai minimum f(5/2) = (5/2)^2 - 5(5/2) + 6 = 25/4 - 50/4 + 24/4 = -1/4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2553ebd929dca8dd3ec80e4e048b5b8b35f2e552caac9100222998f21298e2fa`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2133 |
| 2 | success | valid / verified | applying | procedural | Easy | 3010 |
| 3 | success | valid / verified | applying | procedural | Easy | 2764 |

Run 1 — solusi: f'(x) = 2x - 5. Titik stasioner saat f'(x) = 0, maka 2x = 5, x = 5/2. f''(x) = 2 > 0, sehingga titik tersebut adalah minimum. Nilai minimum f(5/2) = (5/2)^2 - 5(5/2) + 6 = 25/4 - 50/4 + 24/4 = -1/4.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar turunan pertama untuk mencari titik stasioner dan turunan kedua untuk menentukan jenis ekstrem, yang merupakan prosedur rutin dalam kurikulum kelas 12.. Bukti: Tentukan nilai ekstrem dan jenis titik ekstremnya dari setiap fungsi berikut.; Nilai ekstrem dan jenis titik ekstrem dari f(x)=x^2-5x+6?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma turunan untuk optimasi fungsi kuadrat, yang termasuk dalam pengetahuan prosedural.. Bukti: Nilai ekstrem dan jenis titik ekstrem dari f(x)=x^2-5x+6?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, menggunakan fungsi kuadrat sederhana yang familiar bagi siswa kelas 12.. Bukti: Nilai ekstrem dan jenis titik ekstrem dari f(x)=x^2-5x+6?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Turunan fungsi aljabar dasar dan konsep titik stasioner. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah aplikasi dasar turunan yang sudah dipelajari di kelas 11 dan diperdalam di kelas 12, sehingga dianggap sebagai prosedur rutin dengan beban kognitif rendah. |

Run 2 — solusi: f'(x) = 2x - 5 = 0 -> x = 5/2. f''(x) = 2 > 0 (minimum). f(5/2) = (5/2)^2 - 5(5/2) + 6 = 25/4 - 50/4 + 24/4 = -1/4.
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur turunan untuk mencari titik stasioner dan uji turunan kedua untuk menentukan jenis ekstrem, yang merupakan penerapan rutin konsep turunan.. Bukti: f'(x)=2x-5=0; f''(x)=2>0 (min); f(5/2)=-1/4
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman algoritma turunan (prosedural) untuk menentukan titik ekstrem fungsi kuadrat.. Bukti: f'(x)=2x-5=0; f''(x)=2>0 (min)
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur standar untuk fungsi kuadrat yang familiar bagi siswa kelas 12. Tidak ada langkah non-rutin atau kompleksitas tinggi.. Bukti: f(x)=x^2-5x+6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi aljabar sederhana dan uji turunan kedua. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari titik ekstrem fungsi kuadrat adalah materi dasar yang sudah dikuasai di kelas 11 dan diperdalam di kelas 12, sehingga termasuk kategori mudah. |

Run 3 — solusi: f'(x) = 2x - 5 = 0 => x = 5/2. f''(x) = 2 > 0 (minimum). f(5/2) = (5/2)^2 - 5(5/2) + 6 = 25/4 - 50/4 + 24/4 = -1/4.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur turunan untuk menentukan nilai ekstrem fungsi kuadrat, yang merupakan penerapan rutin dari konsep aplikasi turunan.. Bukti: Tentukan nilai ekstrem dan jenis titik ekstremnya dari setiap fungsi berikut.; f(x)=x^2-5x+6
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma turunan untuk mencari titik stasioner dan menentukan jenis ekstremnya.. Bukti: f(x)=x^2-5x+6; Tentukan nilai ekstrem dan jenis titik ekstremnya
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dan familiar bagi siswa kelas 12 dalam topik aplikasi turunan.. Bukti: f(x)=x^2-5x+6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Turunan fungsi polinomial dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Aplikasi turunan pada fungsi kuadrat adalah materi dasar yang rutin dilakukan di kelas 12. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Aplikasi Turunan Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan nilai ekstrem dan jenis titik ekstremnya dari setiap fungsi berikut.

Nilai ekstrem dan jenis titik ekstrem dari $f(x)=x^2-5x+6$?
Pilihan: A. Nilai ekstrem minimum $-\frac14$ pada $x=-\frac52$
B. Nilai ekstrem maksimum $-\frac14$ pada $x=\frac52$
C. Nilai ekstrem minimum $\frac14$ pada $x=\frac52$
D. Nilai ekstrem minimum $-\frac14$ pada $x=\frac52$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `1a7617d4eabc8a84d287b87c`

Sebuah talang air akan dibuat dari sebuah pelat seng selebar 30 cm. Caranya adalah dengan melipat kedua sisi pelat seng sama panjang.<br><br>Tentukan ukuran penampang tegak talang air tersebut sehingga talang dapat dialiri air semaksimal mungkin.

| Opsi | Isi |
|---|---|
| A | Panjang $20$ cm dan lebar $5$ cm |
| B | Panjang $7,5$ cm dan lebar $15$ cm |
| C | Panjang $10$ cm dan lebar $10$ cm |
| D | Panjang $15$ cm dan lebar $7,5$ cm |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misal x adalah tinggi lipatan (lebar sisi), maka lebar alas = 30-2x. Luas penampang L(x) = x(30-2x) = 30x - 2x^2. Maksimum saat L'(x) = 30 - 4x = 0, sehingga x = 7,5 cm. Lebar alas = 30 - 2(7,5) = 15 cm. Ukuran: tinggi 7,5 cm, lebar 15 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a13b1eec470b80d48c469764f23cd92a4f93a1fce04239044a0b1403aabde265`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2187 |
| 2 | success | valid / verified | applying | procedural | Medium | 2215 |
| 3 | success | valid / verified | applying | procedural | Medium | 2190 |

Run 1 — solusi: Misal x adalah tinggi lipatan (lebar sisi), maka lebar alas = 30-2x. Luas penampang L(x) = x(30-2x) = 30x - 2x^2. Maksimum saat L'(x) = 30 - 4x = 0, sehingga x = 7,5 cm. Lebar alas = 30 - 2(7,5) = 15 cm. Ukuran: tinggi 7,5 cm, lebar 15 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep turunan untuk mencari nilai maksimum fungsi luas penampang, yang merupakan prosedur standar dalam aplikasi turunan.. Bukti: Tentukan ukuran penampang tegak talang air tersebut sehingga talang dapat dialiri air semaksimal mungkin.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma turunan untuk mengoptimalkan fungsi luas yang dimodelkan dari masalah geometri.. Bukti: L(x)=(30-2x)x=30x-2x^2; L'(x)=30-4x=0
- Intended difficulty `classify/Medium`: Masalah ini adalah masalah optimasi klasik yang rutin diajarkan di kelas 12. Langkah-langkahnya jelas: memodelkan fungsi, menurunkan, dan mencari titik stasioner.. Bukti: Sebuah talang air akan dibuat dari sebuah pelat seng selebar 30 cm.; Tentukan ukuran penampang tegak talang air tersebut sehingga talang dapat dialiri air semaksimal mungkin.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar turunan fungsi aljabar dan pemodelan matematika sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal optimasi luas dengan turunan adalah materi standar kurikulum kelas 12. Tingkat kesulitan Medium karena memerlukan pemodelan fungsi dari deskripsi teks. |

Run 2 — solusi: Misalkan x adalah tinggi lipatan (lebar sisi tegak). Lebar dasar talang adalah 30-2x. Luas penampang L(x) = x(30-2x) = 30x - 2x^2. Untuk luas maksimum, L'(x) = 30 - 4x = 0, sehingga x = 7,5 cm. Lebar dasar = 30 - 2(7,5) = 15 cm. Jadi, ukuran penampang adalah 15 cm (lebar dasar) dan 7,5 cm (tinggi sisi).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep turunan untuk mengoptimalkan fungsi luas penampang. Ini melibatkan pemilihan prosedur (pemodelan fungsi luas, penurunan, dan pencarian titik stasioner) yang merupakan karakteristik dari domain applying.. Bukti: Tentukan ukuran penampang tegak talang air tersebut sehingga talang dapat dialiri air semaksimal mungkin.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma turunan untuk menyelesaikan masalah optimasi, yang merupakan pengetahuan prosedural.. Bukti: L(x)=(30-2x)x=30x-2x^2, L'(x)=30-4x=0
- Intended difficulty `classify/Medium`: Soal ini adalah masalah optimasi standar yang sering ditemui dalam kurikulum kelas 12. Prosedurnya rutin (memodelkan, menurunkan, mencari nilai nol), sehingga dikategorikan Medium karena memerlukan beberapa langkah terkait.. Bukti: Sebuah talang air akan dibuat dari sebuah pelat seng selebar 30 cm. Caranya adalah dengan melipat kedua sisi pelat seng sama panjang.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi aljabar dan titik stasioner. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah optimasi dengan turunan adalah materi inti kelas 12 TL. Tingkat kesulitan Medium sesuai karena siswa harus menerjemahkan deskripsi verbal menjadi model matematika. |

Run 3 — solusi: Misalkan x adalah tinggi lipatan (lebar sisi tegak). Lebar dasar talang adalah 30-2x. Luas penampang L(x) = x(30-2x) = 30x - 2x^2. Untuk luas maksimum, L'(x) = 30 - 4x = 0, sehingga x = 7,5 cm. Lebar dasar = 30 - 2(7,5) = 15 cm. Jadi, ukuran penampang adalah 15 cm (panjang/lebar dasar) dan 7,5 cm (tinggi/lebar sisi).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep turunan untuk mencari nilai maksimum dari fungsi luas penampang yang dimodelkan dari masalah kontekstual.. Bukti: Tentukan ukuran penampang tegak talang air tersebut sehingga talang dapat dialiri air semaksimal mungkin.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur algoritma turunan untuk mengoptimalkan fungsi luas yang telah dikonstruksi.. Bukti: L(x)=(30-2x)x=30x-2x^2, L'(x)=30-4x=0
- Intended difficulty `classify/Medium`: Soal ini merupakan masalah optimasi standar yang sering ditemui dalam kurikulum kelas 12. Siswa hanya perlu memodelkan fungsi luas sederhana dan mencari titik stasioner.. Bukti: Sebuah talang air akan dibuat dari sebuah pelat seng selebar 30 cm. Caranya adalah dengan melipat kedua sisi pelat seng sama panjang.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi aljabar dan titik stasioner. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah optimasi talang adalah contoh klasik dalam materi aplikasi turunan di kelas 12. Prosedur pemodelan dan diferensiasi adalah rutin. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Aplikasi Turunan Fungsi di Berbagai Bidang Ilmu
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah talang air akan dibuat dari sebuah pelat seng selebar 30 cm. Caranya adalah dengan melipat kedua sisi pelat seng sama panjang.

Tentukan ukuran penampang tegak talang air tersebut sehingga talang dapat dialiri air semaksimal mungkin.
Pilihan: A. Panjang $20$ cm dan lebar $5$ cm
B. Panjang $7,5$ cm dan lebar $15$ cm
C. Panjang $10$ cm dan lebar $10$ cm
D. Panjang $15$ cm dan lebar $7,5$ cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `1375fa6e6d9514008130880c`

Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.

| Opsi | Isi |
|---|---|
| A | Kedua bilangan bernilai sama, yaitu $10$ |
| B | Kedua bilangan bernilai sama, yaitu $\sqrt{40}$ |
| C | Kedua bilangan bernilai sama, yaitu $4\sqrt5$ |
| D | Kedua bilangan adalah $8$ dan $10$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Misal bilangan x dan y, xy=80, maka y=80/x. Jumlah S=x+80/x. S'=1-80/x^2. S'=0 saat x^2=80, x=4√5. Maka y=80/(4√5)=4√5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d800b0ef743d2676d31a462282587657b66b1f3d4e0c0cf7be26e2955fe12106`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3049 |
| 2 | success | valid / verified | applying | procedural | Easy | 2100 |
| 3 | success | valid / verified | applying | procedural | Easy | 2057 |

Run 1 — solusi: Misal bilangan x dan y, xy=80, y=80/x. Jumlah S=x+80/x. S'=1-80/x^2. S'=0 saat x^2=80, x=4√5. Maka y=80/(4√5)=4√5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep turunan untuk mencari nilai minimum fungsi jumlah dua variabel dengan kendala hasil kali.. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.
- Dimensi pengetahuan `classify/procedural`: Melibatkan penggunaan algoritma turunan untuk optimasi (prosedural) dalam konteks masalah matematika.. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.
- Intended difficulty `classify/Medium`: Soal optimasi standar yang memerlukan langkah rutin: substitusi kendala ke fungsi objektif, menurunkan, dan mencari titik kritis.. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi, aljabar dasar, dan optimasi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah optimasi adalah materi standar kelas 12. Prosedur yang digunakan rutin bagi siswa. |

Run 2 — solusi: Misal bilangan tersebut x dan y, xy=80 maka y=80/x. Jumlah S=x+80/x. Turunan S'=1-80/x^2. S'=0 saat x^2=80, x=sqrt(80)=4sqrt(5). Karena x>0, maka y=80/(4sqrt(5))=4sqrt(5).
- Domain kognitif `classify/applying`: Siswa perlu memodelkan masalah optimasi (meminimalkan jumlah) dengan kendala (hasil kali tetap), menurunkan fungsi, dan mencari titik kritis. Ini adalah penerapan prosedur standar optimasi.. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma turunan untuk optimasi (prosedural) dan konsep hubungan antara fungsi, turunan, dan nilai minimum (konseptual).. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.
- Intended difficulty `classify/Easy`: Masalah optimasi sederhana dengan satu variabel. Prosedur standar (membuat fungsi, menurunkan, mencari titik kritis) sudah familiar bagi siswa kelas 12.. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi aljabar dan syarat titik stasioner. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal aplikasi turunan standar yang sering ditemui di kurikulum kelas 12, tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Misal bilangan tersebut x dan y, xy=80 maka y=80/x. Jumlah S=x+80/x. Minimum saat S'=1-80/x^2=0, sehingga x^2=80, x=sqrt(80)=4sqrt(5). Maka y=80/(4sqrt(5))=4sqrt(5).
- Domain kognitif `classify/applying`: Siswa perlu memodelkan masalah optimasi (meminimalkan jumlah dengan kendala hasil kali) menggunakan turunan, yang merupakan prosedur standar dalam aplikasi turunan.. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara fungsi objektif (jumlah) dan kendala (hasil kali) serta penggunaan algoritma turunan untuk mencari nilai ekstrem.. Bukti: jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80
- Intended difficulty `classify/Easy`: Masalah optimasi sederhana ini merupakan prosedur rutin dalam kurikulum kelas 12. Siswa hanya perlu melakukan substitusi kendala ke fungsi objektif dan mencari titik stasioner.. Bukti: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi aljabar dan titik stasioner. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal optimasi dengan satu kendala adalah materi standar kelas 12 yang bersifat prosedural dan familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3524`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur optimasi standar (memodelkan fungsi, menurunkan, mencari titik kritis) untuk menyelesaikan masalah yang diberikan.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang algoritma turunan untuk mencari nilai ekstrem pada fungsi yang dibatasi oleh kendala.
- Intended difficulty `Easy`: Ini adalah masalah optimasi standar yang sangat rutin dalam kurikulum kelas 12. Prosedur substitusi dan turunan adalah teknik dasar yang sudah familiar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep turunan fungsi aljabar dan syarat titik stasioner. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah optimasi dengan satu kendala adalah materi standar kelas 12 yang bersifat prosedural dan familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Aplikasi Turunan Fungsi di Berbagai Bidang Ilmu
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali 80.
Pilihan: A. Kedua bilangan bernilai sama, yaitu $10$
B. Kedua bilangan bernilai sama, yaitu $\sqrt{40}$
C. Kedua bilangan bernilai sama, yaitu $4\sqrt5$
D. Kedua bilangan adalah $8$ dan $10$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `f2de3a4198c1c8c13c51a92a`

Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).

| Opsi | Isi |
|---|---|
| A | b = 2, f^-1(x) = (x + 2)/2 |
| B | b = 2, f^-1(x) = (x - 2)/2 |
| C | b = 3, f^-1(x) = (x - 3)/2 |
| D | b = 6, f^-1(x) = (x - 6)/2 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: f(f(x)) = 2(2x+b)+b = 4x+3b. Diberikan 4x+3b = 4x+6, maka 3b=6, b=2. f(x)=2x+2. Invers: y=2x+2 -> x=(y-2)/2. Jadi f^-1(x)=(x-2)/2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4b81516b005637d2e64911588722bce4c33090f8a45c8d72fda48530f42e0ec1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3158 |
| 2 | success | valid / verified | applying | procedural | Easy | 2938 |
| 3 | success | valid / verified | applying | procedural | Easy | 3070 |

Run 1 — solusi: f(f(x)) = 2(2x+b)+b = 4x+3b. Diberikan 4x+3b = 4x+6, maka 3b=6, b=2. f(x)=2x+2. Invers: y=2x+2 -> x=(y-2)/2. Jadi f^-1(x)=(x-2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan komposisi fungsi dan prosedur mencari invers fungsi linear. Ini adalah prosedur rutin dalam kurikulum kelas 12.. Bukti: f(f(x)) = 2(2x+b)+b = 4x+3b; 3b=6; f^-1(x)=(x-2)/2
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman algoritma komposisi fungsi dan manipulasi aljabar untuk menentukan invers.. Bukti: f(f(x)) = 2(2x+b)+b; f^-1(x)=(x-2)/2
- Intended difficulty `classify/Easy`: Soal ini menggunakan prosedur standar yang familiar bagi siswa kelas 12. Tidak ada langkah non-rutin atau integrasi representasi yang kompleks.. Bukti: f(f(x)) = 2(2x+b)+b = 4x+3b; 3b=6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman komposisi fungsi dan invers fungsi linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan standar fungsi komposisi dan invers yang umum di kelas 12, tidak memerlukan strategi khusus. |

Run 2 — solusi: f(f(x)) = 2(2x+b)+b = 4x+3b. Diketahui 4x+3b = 4x+6, maka 3b=6, b=2. f(x)=2x+2. y=2x+2, maka x=(y-2)/2. Jadi f^-1(x)=(x-2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur komposisi fungsi linear dan mencari invers fungsi linear. Ini adalah prosedur rutin yang dipelajari di tingkat SMA.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6; Tentukan nilai b dan f-1 (x)
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman dan penerapan algoritma komposisi fungsi dan invers fungsi.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa SMA. Langkah-langkahnya rutin dan beban komputasi rendah.. Bukti: f (x) = 2x + b dan f (f (x)) = 4x + 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep komposisi fungsi dan invers fungsi linear. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi komposisi dan invers adalah materi dasar yang rutin di kelas 12. Tidak ada kompleksitas strategi atau generalisasi yang diperlukan. |

Run 3 — solusi: f(f(x)) = 2(2x+b)+b = 4x+3b. Diketahui f(f(x)) = 4x+6, maka 3b=6 sehingga b=2. Fungsi menjadi f(x)=2x+2. Untuk mencari invers, y=2x+2, maka 2x=y-2, sehingga x=(y-2)/2. Jadi, f^-1(x)=(x-2)/2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep komposisi fungsi dan invers fungsi secara berurutan untuk menyelesaikan masalah rutin.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6
- Dimensi pengetahuan `classify/procedural`: Penyelesaian melibatkan algoritma standar komposisi fungsi dan manipulasi aljabar untuk mencari invers.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 12, melibatkan langkah-langkah rutin tanpa jebakan konseptual yang kompleks.. Bukti: f (x) = 2x + b; f (f (x)) = 4x + 6

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep komposisi fungsi dan invers fungsi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi komposisi dan invers adalah materi dasar yang sudah dipelajari dan rutin dikerjakan di kelas 12. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Fungsi Invers
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).
Pilihan: A. b = 2, f^-1(x) = (x + 2)/2
B. b = 2, f^-1(x) = (x - 2)/2
C. b = 3, f^-1(x) = (x - 3)/2
D. b = 6, f^-1(x) = (x - 6)/2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `501a9296524cbcfb62ba4aee`

Dalam 10 hari pertama bulan Desember, sebuah sel suatu tanaman bertumbuh sedemikian rupa sehingga pada $t$ hari sesudah tanggal 1 Desember, volume sel itu bertambah dengan kecepatan $(12-t)^{-2}$ mikrometer kubik per hari.<br><br>Jika pada tanggal 3 Desember volume sel itu adalah 3 mikrometer kubik, berapa volumenya pada tanggal 8 Desember?

| Opsi | Isi |
|---|---|
| A | 2,9 mikrometer kubik |
| B | 0,2 mikrometer kubik |
| C | 2,7 mikrometer kubik |
| D | 3,1 mikrometer kubik |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: V(t) = integral (12-t)^-2 dt = (12-t)^-1 + C = 1/(12-t) + C. Diketahui V(2) = 3, maka 1/(12-2) + C = 3 => 0,1 + C = 3 => C = 2,9. Volume pada 8 Desember (t=7): V(7) = 1/(12-7) + 2,9 = 1/5 + 2,9 = 0,2 + 2,9 = 3,1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e27bd5603bcdf0b7028ffc3a88c360ca667d65f9bff58058e4bfcbd66342ef4e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2229 |
| 2 | success | valid / verified | applying | procedural | Medium | 2277 |
| 3 | success | valid / verified | applying | procedural | Medium | 2241 |

Run 1 — solusi: V(t) = integral (12-t)^-2 dt = (12-t)^-1 + C = 1/(12-t) + C. Diketahui V(2) = 3, maka 1/(12-2) + C = 3 => 0,1 + C = 3 => C = 2,9. Volume pada 8 Desember (t=7): V(7) = 1/(12-7) + 2,9 = 1/5 + 2,9 = 0,2 + 2,9 = 3,1.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan fungsi kecepatan untuk mendapatkan fungsi volume, menentukan konstanta integrasi menggunakan kondisi awal, dan mengevaluasi fungsi pada titik waktu tertentu. Ini adalah penerapan prosedur integral yang rutin.. Bukti: volume sel itu bertambah dengan kecepatan (12-t)^-2; Jika pada tanggal 3 Desember volume sel itu adalah 3 mikrometer kubik, berapa volumenya pada tanggal 8 Desember?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang teknik integrasi (aturan rantai/substitusi sederhana) dan konsep dasar integral sebagai antiturunan dari laju perubahan.. Bukti: volume sel itu bertambah dengan kecepatan (12-t)^-2
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan translasi konteks waktu ke variabel t (t=2 untuk 3 Des, t=7 untuk 8 Des) dan melakukan dua langkah rutin: integrasi dan penentuan konstanta.. Bukti: kecepatan (12-t)^-2; tanggal 3 Desember... tanggal 8 Desember

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral tak tentu fungsi aljabar sederhana dan aturan rantai dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 TL, menguji pemahaman integral sebagai antiturunan laju perubahan dengan konteks waktu yang perlu diterjemahkan. |

Run 2 — solusi: dV/dt = (12-t)^(-2). V(t) = integral (12-t)^(-2) dt = (12-t)^(-1) + C = 1/(12-t) + C. Dec 3 (t=2): V(2) = 1/10 + C = 3 => C = 2.9. Dec 8 (t=7): V(7) = 1/(12-7) + 2.9 = 1/5 + 2.9 = 0.2 + 2.9 = 3.1.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan fungsi laju perubahan untuk mendapatkan fungsi volume, menentukan konstanta integrasi menggunakan kondisi awal yang diberikan, dan mengevaluasi fungsi pada titik waktu tertentu. Ini adalah penerapan prosedur integral dalam konteks laju perubahan.. Bukti: volume sel itu bertambah dengan kecepatan (12-t)^-2; Jika pada tanggal 3 Desember volume sel itu adalah 3 mikrometer kubik, berapa volumenya pada tanggal 8 Desember?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang teknik integrasi (aturan rantai/substitusi sederhana) dan konsep dasar bahwa integral dari laju perubahan adalah fungsi akumulasi.. Bukti: volume sel itu bertambah dengan kecepatan (12-t)^-2; integral tak tentu
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman tentang pemetaan waktu (t=2 untuk 3 Des, t=7 untuk 8 Des) dan penerapan integral tak tentu untuk menyelesaikan masalah laju perubahan, yang merupakan langkah rutin namun memerlukan ketelitian dalam penentuan konstanta.. Bukti: kecepatan (12-t)^-2; tanggal 3 Desember... tanggal 8 Desember

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral fungsi aljabar sederhana, aturan rantai dasar, pemahaman konsep laju perubahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 TL karena mengintegrasikan konsep kalkulus dasar dengan aplikasi laju pertumbuhan, menuntut ketelitian dalam substitusi nilai t. |

Run 3 — solusi: dV/dt = (12-t)^-2. V(t) = integral (12-t)^-2 dt = (12-t)^-1 + C = 1/(12-t) + C. Dec 3 (t=2): V(2) = 1/10 + C = 3 => C = 2.9. Dec 8 (t=7): V(7) = 1/(12-7) + 2.9 = 1/5 + 2.9 = 0.2 + 2.9 = 3.1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep integral tak tentu untuk mencari fungsi volume dari laju perubahan yang diberikan, kemudian menentukan konstanta integrasi menggunakan kondisi awal yang diketahui.. Bukti: volume sel itu bertambah dengan kecepatan (12-t)^-2; Jika pada tanggal 3 Desember volume sel itu adalah 3 mikrometer kubik, berapa volumenya pada tanggal 8 Desember?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang teknik integrasi (aturan rantai/substitusi sederhana) dan konsep dasar bahwa integral dari laju perubahan menghasilkan fungsi akumulasi.. Bukti: kecepatan (12-t)^-2; volume sel itu adalah 3 mikrometer kubik
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman tentang pemetaan waktu (tanggal ke variabel t) dan integrasi fungsi komposisi sederhana, yang merupakan langkah rutin dalam kurikulum kelas 12 TL.. Bukti: kecepatan (12-t)^-2; tanggal 3 Desember volume sel itu adalah 3; berapa volumenya pada tanggal 8 Desember

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral fungsi aljabar sederhana dan aturan rantai dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini adalah aplikasi standar integral tak tentu pada laju perubahan, sesuai dengan ekspektasi kurikulum kelas 12 TL. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Integral Tak Tentu
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam 10 hari pertama bulan Desember, sebuah sel suatu tanaman bertumbuh sedemikian rupa sehingga pada $t$ hari sesudah tanggal 1 Desember, volume sel itu bertambah dengan kecepatan $(12-t)^{-2}$ mikrometer kubik per hari.

Jika pada tanggal 3 Desember volume sel itu adalah 3 mikrometer kubik, berapa volumenya pada tanggal 8 Desember?
Pilihan: A. 2,9 mikrometer kubik
B. 0,2 mikrometer kubik
C. 2,7 mikrometer kubik
D. 3,1 mikrometer kubik
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `acb3cf7a6b854bfb9850f6a1`

Tentukan integral tak tentu berikut.<br><br>$\int 2x^7\,dx$

| Opsi | Isi |
|---|---|
| A | $\frac{1}{8}x^8+C$ |
| B | $14x^6+C$ |
| C | $\frac{1}{4}x^8+C$ |
| D | $2x^8+C$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Integral dari 2x^7 dx adalah 2 * (x^(7+1) / (7+1)) + C = 2 * (x^8 / 8) + C = (1/4)x^8 + C.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `13c47bb72c851372421b8e2911d2cc31c102b1c1f35b70feedab4b90cced509f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1979 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1976 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2755 |

Run 1 — solusi: Integral dari 2x^7 dx adalah 2 * (x^(7+1) / (7+1)) + C = 2 * (x^8 / 8) + C = (1/4)x^8 + C.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung aturan dasar integral tak tentu untuk fungsi pangkat (power rule). Siswa hanya perlu mengingat dan menerapkan rumus integral ax^n dx = a/(n+1) * x^(n+1) + C. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Tentukan integral tak tentu berikut. $\int 2x^7\,dx$
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma integrasi dasar untuk fungsi polinomial sederhana.. Bukti: $\int 2x^7\,dx$
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan prosedur rutin yang diajarkan di awal materi integral. Beban kognitif sangat rendah.. Bukti: $\int 2x^7\,dx$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman aturan dasar integral fungsi pangkat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun integral diajarkan di kelas 12, soal ini adalah bentuk paling dasar (one-step) yang seharusnya sudah dikuasai siswa sebagai prosedur rutin. |

Run 2 — solusi: Integral dari 2x^7 dx adalah (2/(7+1)) * x^(7+1) + C = (2/8)x^8 + C = (1/4)x^8 + C.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus dasar integral tak tentu (aturan pangkat). Siswa hanya perlu mengenali pola dan menerapkan prosedur standar tanpa modifikasi strategi.. Bukti: Tentukan integral tak tentu berikut. \int 2x^7\,dx
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma integrasi fungsi aljabar sederhana.. Bukti: \int 2x^7\,dx
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan satu langkah penerapan rumus integral pangkat. Tidak ada kendala atau kompleksitas tambahan.. Bukti: \int 2x^7\,dx

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan integral tak tentu untuk fungsi polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun integral diajarkan di kelas 12, soal ini adalah bentuk paling dasar (latihan awal) yang seharusnya sudah dikuasai dengan lancar oleh siswa. |

Run 3 — solusi: Menggunakan aturan pangkat integral: ∫ ax^n dx = a/(n+1) * x^(n+1) + C. Maka, ∫ 2x^7 dx = 2/(7+1) * x^(7+1) + C = 2/8 * x^8 + C = 1/4 * x^8 + C.
- Domain kognitif `classify/knowing`: Soal ini hanya memerlukan penerapan langsung rumus dasar integral tak tentu (aturan pangkat) tanpa modifikasi atau strategi tambahan.. Bukti: Tentukan integral tak tentu berikut.; ∫ 2x^7 dx
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma atau prosedur standar untuk mengintegralkan fungsi polinomial sederhana.. Bukti: ∫ 2x^7 dx
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur rutin yang sangat dasar dalam kalkulus kelas 12, tidak memerlukan langkah kompleks atau pemilihan strategi.. Bukti: ∫ 2x^7 dx

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman aturan pangkat integral dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar integral tak tentu yang diajarkan di awal materi kalkulus kelas 12. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Integral Tak Tentu
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan integral tak tentu berikut.

$\int 2x^7\,dx$
Pilihan: A. $\frac{1}{8}x^8+C$
B. $14x^6+C$
C. $\frac{1}{4}x^8+C$
D. $2x^8+C$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `dd99d4ea24732659174ae27b`

Diketahui fungsi $f(x)=x^2+4x+5$ pada interval $[1,4]$.<br><br>Tentukan integral tentu dari $f(x)$ pada interval $[1,4]$ atau $\int_1^4(x^2+4x+5)\,dx$.

| Opsi | Isi |
|---|---|
| A | $56$ |
| B | $66$ |
| C | $96$ |
| D | $\frac{87}{2}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `66`.
Solusi minimum hasil AI: Integral dari x^2+4x+5 adalah (1/3)x^3 + 2x^2 + 5x. Evaluasi pada batas [1,4]: [(1/3)(64) + 2(16) + 5(4)] - [(1/3)(1) + 2(1) + 5(1)] = (64/3 + 32 + 20) - (1/3 + 7) = (220/3) - (22/3) = 198/3 = 66.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `18d8225e28ebf76a6437fb62cff57d7f9ffa8c972dffbf48dfcfea5bd7ab2175`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3151 |
| 2 | success | valid / verified | applying | procedural | Easy | 3079 |
| 3 | success | valid / verified | applying | procedural | Easy | 2173 |

Run 1 — solusi: Integral dari x^2+4x+5 adalah (1/3)x^3 + 2x^2 + 5x. Evaluasi pada batas [1,4]: [(1/3)(64) + 2(16) + 5(4)] - [(1/3)(1) + 2(1) + 5(1)] = (64/3 + 32 + 20) - (1/3 + 7) = (220/3) - (22/3) = 198/3 = 66.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan dasar integral tentu (aturan pangkat) pada fungsi polinomial sederhana. Ini adalah prosedur standar yang diajarkan di kelas 12.. Bukti: integral tentu dari f(x) pada interval [1,4]
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma integrasi (prosedural) untuk fungsi polinomial.. Bukti: integral tentu dari f(x) pada interval [1,4]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, menggunakan fungsi polinomial sederhana, dan hanya memerlukan penerapan langsung teorema dasar kalkulus tanpa modifikasi atau strategi kompleks.. Bukti: f(x)=x^2+4x+5 pada interval [1,4]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan dasar integral tak tentu (aturan pangkat) dan Teorema Dasar Kalkulus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi integral tentu adalah kurikulum standar kelas 12. Soal ini adalah latihan rutin yang tidak memerlukan pemikiran tingkat tinggi. |

Run 2 — solusi: Integral dari x^2+4x+5 adalah (1/3)x^3+2x^2+5x. Evaluasi pada batas 4 dan 1: [(1/3)(64)+2(16)+5(4)] - [(1/3)(1)+2(1)+5(1)] = (64/3+32+20) - (1/3+7) = 63/3 + 45 = 21 + 45 = 66.
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur standar integral tentu fungsi polinomial pada interval tertentu.. Bukti: integral tentu dari f(x) pada interval [1,4] atau \int_1^4(x^2+4x+5)\,dx
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma dasar integrasi polinomial dan teorema dasar kalkulus.. Bukti: \int_1^4(x^2+4x+5)\,dx
- Intended difficulty `classify/Easy`: Prosedur integrasi polinomial adalah materi dasar yang familiar dan langsung, tidak memerlukan strategi nonrutin.. Bukti: \int_1^4(x^2+4x+5)\,dx

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar integral tak tentu fungsi polinomial dan teorema dasar kalkulus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi integral tentu polinomial merupakan standar kurikulum kelas 12, soal ini bersifat rutin tanpa kompleksitas tambahan. |

Run 3 — solusi: Integral dari x^2+4x+5 adalah (1/3)x^3 + 2x^2 + 5x. Evaluasi pada batas 4: (1/3)(64) + 2(16) + 5(4) = 64/3 + 32 + 20 = 64/3 + 52 = 64/3 + 156/3 = 220/3. Evaluasi pada batas 1: (1/3)(1) + 2(1) + 5(1) = 1/3 + 7 = 22/3. Hasil: 220/3 - 22/3 = 198/3 = 66.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar integrasi fungsi polinomial dan teorema dasar kalkulus untuk menghitung nilai integral tentu. Ini adalah penerapan prosedur rutin.. Bukti: Tentukan integral tentu dari f(x) pada interval [1,4] atau integral 1 sampai 4 dari (x^2+4x+5) dx
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan algoritma integrasi (prosedural) pada fungsi polinomial.. Bukti: integral tentu dari f(x) pada interval [1,4]
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 12. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: f(x)=x^2+4x+5 pada interval [1,4]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar integral tak tentu fungsi polinomial dan teorema dasar kalkulus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi integral tentu adalah kurikulum standar kelas 12 TL. Prosedur yang diminta bersifat langsung dan rutin. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Integral Tentu
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui fungsi $f(x)=x^2+4x+5$ pada interval $[1,4]$.

Tentukan integral tentu dari $f(x)$ pada interval $[1,4]$ atau $\int_1^4(x^2+4x+5)\,dx$.
Pilihan: A. $56$
B. $66$
C. $96$
D. $\frac{87}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `55be764addd8f2e1a44c48b3`

Diketahui fungsi $f(x)=x^2-x+4$ pada interval $[0,4]$.<br><br>Tentukan integral tentu dari $f(x)$ pada interval $[0,4]$ atau $\int_0^4(x^2-x+4)\,dx$.

| Opsi | Isi |
|---|---|
| A | $\frac{88}{3}$ |
| B | $\frac{40}{3}$ |
| C | $\frac{136}{3}$ |
| D | $\frac{52}{3}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Integral dari x^2 - x + 4 adalah (1/3)x^3 - (1/2)x^2 + 4x. Evaluasi pada batas [0, 4]: ((1/3)(64) - (1/2)(16) + 4(4)) - 0 = 64/3 - 8 + 16 = 64/3 + 8 = 64/3 + 24/3 = 88/3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5918866e11d7c2dd15bdaee6339b559b7b41088e8b42c7805ecf23aa2e67f5fb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2119 |
| 2 | success | valid / verified | applying | procedural | Easy | 2115 |
| 3 | success | valid / verified | applying | procedural | Easy | 2091 |

Run 1 — solusi: Integral dari x^2 - x + 4 adalah (1/3)x^3 - (1/2)x^2 + 4x. Evaluasi pada batas [0, 4]: ((1/3)(64) - (1/2)(16) + 4(4)) - 0 = 64/3 - 8 + 16 = 64/3 + 8 = 64/3 + 24/3 = 88/3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar integrasi fungsi polinomial dan teorema dasar kalkulus untuk menghitung nilai integral tentu. Ini adalah prosedur rutin yang dipelajari di kelas 12.. Bukti: Tentukan integral tentu dari f(x) pada interval [0,4] atau integral 0 sampai 4 (x^2-x+4) dx
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma integrasi fungsi polinomial dan penerapan batas integrasi, yang merupakan pengetahuan prosedural.. Bukti: integral tentu dari f(x) pada interval [0,4]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan aturan pangkat pada integral dan melakukan substitusi batas atas dan bawah tanpa kendala tambahan atau strategi non-rutin.. Bukti: integral tentu dari f(x) pada interval [0,4]; f(x)=x^2-x+4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan dasar integrasi fungsi polinomial (integral tak tentu) dan teorema dasar kalkulus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 12 yang menguji kemampuan dasar integrasi fungsi polinomial sederhana, sesuai dengan kurikulum matematika tingkat lanjut. |

Run 2 — solusi: Integral dari x^2 - x + 4 adalah (1/3)x^3 - (1/2)x^2 + 4x. Evaluasi pada batas [0, 4]: ((1/3)(64) - (1/2)(16) + 4(4)) - 0 = 64/3 - 8 + 16 = 64/3 + 8 = 64/3 + 24/3 = 88/3.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung algoritma integral tentu pada fungsi polinomial sederhana, yang merupakan prosedur rutin dalam kurikulum kelas 12.. Bukti: Tentukan integral tentu dari f(x) pada interval [0,4] atau integral_0^4(x^2-x+4)dx
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma integrasi (aturan pangkat) dan teorema dasar kalkulus untuk menghitung nilai integral tentu.. Bukti: integral tentu dari f(x) pada interval [0,4]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan fungsi polinomial sederhana dan batas integrasi yang jelas. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: f(x)=x^2-x+4 pada interval [0,4]; integral tentu dari f(x) pada interval [0,4]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan dasar integral tak tentu (aturan pangkat) dan teorema dasar kalkulus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 12 yang menguji pemahaman dasar tentang integral tentu fungsi polinomial. |

Run 3 — solusi: Integral dari x^2 - x + 4 adalah (1/3)x^3 - (1/2)x^2 + 4x. Evaluasi pada batas [0, 4]: ((1/3)(4)^3 - (1/2)(4)^2 + 4(4)) - 0 = (64/3) - 8 + 16 = 64/3 + 8 = 64/3 + 24/3 = 88/3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar integrasi fungsi polinomial dan teorema dasar kalkulus untuk menghitung nilai integral tentu. Ini adalah penerapan langsung dari prosedur yang sudah dipelajari.. Bukti: Tentukan integral tentu dari f(x) pada interval [0,4] atau ∫_0^4(x^2-x+4) dx
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma integrasi (prosedural) untuk fungsi polinomial sederhana.. Bukti: f(x)=x^2-x+4; ∫_0^4(x^2-x+4) dx
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang langsung, melibatkan fungsi polinomial sederhana tanpa trik atau kompleksitas tambahan.. Bukti: Tentukan integral tentu dari f(x) pada interval [0,4]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang aturan integral tak tentu untuk fungsi pangkat dan teorema dasar kalkulus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Integrasi polinomial adalah materi standar kelas 12 TL yang bersifat prosedural dan rutin. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Integral Tentu
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui fungsi $f(x)=x^2-x+4$ pada interval $[0,4]$.

Tentukan integral tentu dari $f(x)$ pada interval $[0,4]$ atau $\int_0^4(x^2-x+4)\,dx$.
Pilihan: A. $\frac{88}{3}$
B. $\frac{40}{3}$
C. $\frac{136}{3}$
D. $\frac{52}{3}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `f064d8080e4b3fccc44ce182`

Tentukan luas daerah yang dibatasi oleh kurva $y^2=2x-2$ dan $y=x-5$.

| Opsi | Isi |
|---|---|
| A | $12$ satuan luas |
| B | $18$ satuan luas |
| C | $36$ satuan luas |
| D | $9$ satuan luas |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `18`.
Solusi minimum hasil AI: Ubah kurva ke fungsi y: x = y^2/2 + 1 dan x = y + 5. Titik potong: y^2/2 + 1 = y + 5 => y^2 - 2y - 8 = 0 => (y-4)(y+2)=0. Batas y: -2 sampai 4. Luas = integral dari -2 sampai 4 dari ((y+5) - (y^2/2 + 1)) dy = integral dari -2 sampai 4 dari (-y^2/2 + y + 4) dy = [-y^3/6 + y^2/2 + 4y] dari -2 sampai 4 = (-64/6 + 16/2 + 16) - (8/6 + 4/2 - 8) = (-32/3 + 24) - (4/3 - 6) = 40/3 - (-14/3) = 54/3 = 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6dfaff95794ce756192ea1a95733ec26a636dd15c90803297b4fe5d3daf25776`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2200 |
| 2 | success | valid / verified | applying | procedural | Medium | 2221 |
| 3 | success | valid / verified | applying | procedural | Medium | 3389 |

Run 1 — solusi: Ubah kurva ke fungsi y: x = y^2/2 + 1 dan x = y + 5. Titik potong: y^2/2 + 1 = y + 5 => y^2 - 2y - 8 = 0 => (y-4)(y+2)=0. Batas y: -2 sampai 4. Luas = integral dari -2 sampai 4 dari ((y+5) - (y^2/2 + 1)) dy = integral dari -2 sampai 4 dari (-y^2/2 + y + 4) dy = [-y^3/6 + y^2/2 + 4y] dari -2 sampai 4 = (-64/6 + 16/2 + 16) - (8/6 + 4/2 - 8) = (-32/3 + 24) - (4/3 - 6) = 40/3 - (-14/3) = 54/3 = 18.
- Domain kognitif `classify/applying`: Siswa perlu memilih strategi integrasi yang tepat (mengintegralkan terhadap y) untuk mempermudah perhitungan luas daerah yang dibatasi oleh parabola dan garis, yang merupakan prosedur standar dalam kurikulum kelas 12.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menentukan luas daerah di antara dua kurva dengan melakukan integrasi, termasuk menentukan titik potong dan batas integrasi.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.
- Intended difficulty `classify/Medium`: Soal memerlukan manipulasi aljabar untuk mengubah persamaan ke fungsi y, menentukan titik potong, dan melakukan integrasi tentu. Ini adalah prosedur rutin dalam kalkulus integral.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aljabar dasar, persamaan kuadrat, konsep integral tentu untuk luas daerah. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan mampu mengintegrasikan fungsi terhadap variabel y jika lebih efisien, serta melakukan operasi integral tentu dengan batas yang melibatkan akar persamaan kuadrat. |

Run 2 — solusi: Titik potong: y^2 = 2(y+5)-2 => y^2-2y-8=0 => (y-4)(y+2)=0. Titik potong di y=-2 dan y=4. Kurva kanan x = y+5, kurva kiri x = (y^2/2)+1. Luas = integral dari -2 sampai 4 dari ((y+5) - (y^2/2 + 1)) dy = integral dari -2 sampai 4 dari (-y^2/2 + y + 4) dy = [-y^3/6 + y^2/2 + 4y] dari -2 sampai 4 = (-64/6 + 8 + 16) - (8/6 + 2 - 8) = (-32/3 + 24) - (4/3 - 6) = -36/3 + 30 = -12 + 30 = 18.
- Domain kognitif `classify/applying`: Siswa perlu menentukan titik potong, memilih variabel integrasi yang tepat (terhadap y lebih efisien), dan menerapkan rumus integral luas daerah antara dua kurva. Ini adalah prosedur standar dalam kalkulus integral.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan integral tentu untuk menghitung luas daerah yang dibatasi oleh kurva, termasuk teknik manipulasi aljabar untuk menemukan batas integrasi.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemilihan variabel integrasi yang tepat (terhadap y) agar perhitungan menjadi rutin. Jika siswa mencoba mengintegralkan terhadap x, mereka harus memecah daerah menjadi dua bagian, yang lebih kompleks. Namun, dengan pemilihan variabel yang tepat, ini adalah prosedur rutin.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang integral tentu sebagai luas daerah, kemampuan mencari titik potong dua kurva, dan manipulasi aljabar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan mampu memilih variabel integrasi yang paling efisien untuk menghitung luas daerah antara dua kurva. |

Run 3 — solusi: Ubah kurva ke fungsi y: x=y^2/2+1 dan x=y+5. Titik potong: y^2/2+1=y+5 => y^2-2y-8=0 => (y-4)(y+2)=0. Luas = integral dari -2 sampai 4 dari ((y+5)-(y^2/2+1)) dy = integral dari -2 sampai 4 dari (-y^2/2+y+4) dy = [-y^3/6+y^2/2+4y] dari -2 sampai 4 = (-32/3+8+16) - (4/3+2-8) = 18.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur integrasi terhadap sumbu y, menentukan batas integrasi melalui titik potong, dan melakukan kalkulasi integral tentu.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.
- Dimensi pengetahuan `classify/procedural`: Melibatkan penerapan algoritma integral tentu untuk menghitung luas daerah antara dua kurva.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y^2=2x-2 dan y=x-5.
- Intended difficulty `classify/Medium`: Memerlukan manipulasi aljabar untuk mengubah persamaan, mencari titik potong, dan integrasi. Prosedur rutin namun melibatkan beberapa langkah.. Bukti: y^2=2x-2; y=x-5

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral tentu, aljabar persamaan kuadrat, konsep luas daerah. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai kurikulum kelas 12 TL tentang penerapan integral untuk luas daerah. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Penerapan Integral
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan luas daerah yang dibatasi oleh kurva $y^2=2x-2$ dan $y=x-5$.
Pilihan: A. $12$ satuan luas
B. $18$ satuan luas
C. $36$ satuan luas
D. $9$ satuan luas
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `7be8d2f041b6970727503e68`

Tentukan luas daerah yang dibatasi oleh kurva $y=x^2$ dan $y=-x^2+4x$.

| Opsi | Isi |
|---|---|
| A | $8$ satuan luas |
| B | $\frac{16}{3}$ satuan luas |
| C | $\frac{8}{3}$ satuan luas |
| D | $\frac{4}{3}$ satuan luas |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Titik potong: x^2 = -x^2 + 4x => 2x^2 - 4x = 0 => x=0, 2. Luas = integral dari 0 sampai 2 dari (-x^2 + 4x - x^2) dx = integral dari 0 sampai 2 dari (-2x^2 + 4x) dx = [-2/3 x^3 + 2x^2] dari 0 sampai 2 = (-16/3 + 8) = 8/3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2e45db5cbbccbbfadc3e5f26e7370d9564dc41eca210d3f5de081d090907e152`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3237 |
| 2 | success | valid / verified | applying | procedural | Medium | 3182 |
| 3 | success | valid / verified | applying | procedural | Medium | 3213 |

Run 1 — solusi: Titik potong: x^2 = -x^2 + 4x => 2x^2 - 4x = 0 => x=0, 2. Luas = integral dari 0 sampai 2 dari (-x^2 + 4x - x^2) dx = integral dari 0 sampai 2 dari (-2x^2 + 4x) dx = [-2/3 x^3 + 2x^2] dari 0 sampai 2 = (-16/3 + 8) = 8/3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur integral tentu untuk menghitung luas daerah di antara dua kurva, yang melibatkan penentuan titik potong dan integrasi fungsi selisih.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan teknik integrasi untuk aplikasi luas daerah.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: mencari titik potong, menentukan fungsi selisih, dan menghitung integral tentu. Ini adalah prosedur standar kelas 12.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang integral tentu dan penyelesaian persamaan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas daerah antara dua kurva adalah topik rutin dalam kurikulum matematika tingkat lanjut kelas 12. |

Run 2 — solusi: Titik potong: x^2 = -x^2 + 4x -> 2x^2 - 4x = 0 -> x=0, x=2. Luas = integral dari 0 sampai 2 dari (-x^2 + 4x - x^2) dx = integral dari 0 sampai 2 dari (-2x^2 + 4x) dx = [-2/3 x^3 + 2x^2] dari 0 sampai 2 = (-16/3 + 8) = 8/3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur integral tentu untuk menghitung luas daerah antara dua kurva, yang melibatkan penentuan titik potong dan integrasi fungsi selisih.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang algoritma mencari luas daerah menggunakan integral tentu.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: mencari titik potong, menentukan fungsi selisih, dan menghitung integral tentu. Ini adalah standar prosedur kelas 12.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar integral tentu dan aljabar untuk mencari titik potong kurva. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi integral luas daerah adalah kurikulum standar kelas 12 TL, dengan prosedur yang rutin namun memerlukan ketelitian dalam perhitungan. |

Run 3 — solusi: Titik potong: x^2 = -x^2 + 4x => 2x^2 - 4x = 0 => x=0, 2. Luas = integral dari 0 sampai 2 dari (-x^2+4x - x^2) dx = integral dari 0 sampai 2 dari (-2x^2+4x) dx = [-2/3 x^3 + 2x^2] dari 0 sampai 2 = (-16/3 + 8) = 8/3.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur integral tentu untuk menghitung luas daerah antara dua kurva, menentukan batas integrasi melalui titik potong, dan menerapkan rumus luas.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma standar untuk mencari titik potong dan menghitung integral tentu sebagai prosedur rutin dalam penerapan integral.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x
- Intended difficulty `classify/Medium`: Memerlukan beberapa langkah rutin: mencari titik potong, menyusun fungsi selisih, dan menghitung integral tentu. Ini adalah prosedur standar kelas 12.. Bukti: Tentukan luas daerah yang dibatasi oleh kurva y=x^2 dan y=-x^2+4x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep integral tentu, mencari titik potong dua kurva, dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas daerah antara dua kurva adalah standar kurikulum kelas 12 TL, melibatkan prosedur rutin yang sudah dipelajari. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Penerapan Integral
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan luas daerah yang dibatasi oleh kurva $y=x^2$ dan $y=-x^2+4x$.
Pilihan: A. $8$ satuan luas
B. $\frac{16}{3}$ satuan luas
C. $\frac{8}{3}$ satuan luas
D. $\frac{4}{3}$ satuan luas
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `6e4f3d4c7a6cc32991a4f045`

Dari 5 mobil yang dikirim sebuah pabrik, sebanyak 2 mobil tiba dalam keadaan tergores. Sebuah toko menerima 3 mobil secara acak. Misalkan T menyatakan ruang sampel, G untuk kondisi mobil “tergores”, dan B untuk kondisi mobil yang “baik”. Variabel acak X menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut.<br><br>Tentukan nilai x yang mungkin dari variabel acak X .

| Opsi | Isi |
|---|---|
| A | {1, 2} |
| B | {0, 1, 2} |
| C | {1, 2, 3} |
| D | {0, 1, 2, 3} |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Total mobil 5 (2 G, 3 B). Toko menerima 3 mobil. X adalah jumlah mobil G yang diterima. Jika toko menerima 3 mobil, kemungkinan komposisi (G,B) adalah: (0G, 3B), (1G, 2B), atau (2G, 1B). Maka nilai X yang mungkin adalah {0, 1, 2}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `edd8f60e60633cc41b73a3a69a8e9bf2e2d459042da00db4d0e7b271acc4ef71`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2117 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2144 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2169 |

Run 1 — solusi: Total mobil 5 (2 G, 3 B). Toko menerima 3 mobil. X adalah jumlah mobil G yang diterima. Jika toko menerima 3 mobil, kemungkinan komposisi (G,B) adalah: (0G, 3B), (1G, 2B), atau (2G, 1B). Maka nilai X yang mungkin adalah {0, 1, 2}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi variabel acak diskret dan menentukan ruang nilai yang mungkin berdasarkan batasan fisik (jumlah mobil tergores yang tersedia). Ini melibatkan pemahaman konsep dasar variabel acak tanpa perhitungan kompleks.. Bukti: Variabel acak X menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut.; Tentukan nilai x yang mungkin dari variabel acak X
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang variabel acak diskret dan bagaimana menentukan domain nilai yang mungkin dalam konteks pengambilan sampel tanpa pengembalian.. Bukti: Variabel acak X menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut.
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan familiar bagi siswa kelas 12 yang mempelajari variabel acak. Tidak ada perhitungan rumit, hanya logika dasar mengenai batasan nilai variabel acak.. Bukti: Dari 5 mobil yang dikirim sebuah pabrik, sebanyak 2 mobil tiba dalam keadaan tergores.; Sebuah toko menerima 3 mobil secara acak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak diskret dan ruang sampel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari definisi variabel acak diskret yang sesuai dengan kurikulum kelas 12 Matematika Tingkat Lanjut. |

Run 2 — solusi: Total mobil 5 (2 Gores, 3 Baik). Diambil 3 mobil. X adalah jumlah mobil tergores. Jika terambil 0 Gores (3 Baik), X=0. Jika terambil 1 Gores (2 Baik), X=1. Jika terambil 2 Gores (1 Baik), X=2. Karena hanya ada 2 mobil tergores, X tidak mungkin 3. Jadi, X={0, 1, 2}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi variabel acak diskret dan menentukan ruang nilai yang mungkin berdasarkan batasan fisik populasi (hanya ada 2 mobil tergores). Ini adalah proses menerapkan konsep variabel acak pada situasi konkret.. Bukti: Variabel acak X menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut.; Tentukan nilai x yang mungkin dari variabel acak X
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang variabel acak diskret dan bagaimana batasan populasi mempengaruhi nilai yang mungkin dari variabel tersebut.. Bukti: Variabel acak X menyatakan banyak mobil terkena goresan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dalam kurikulum variabel acak diskret. Siswa hanya perlu melakukan analisis logika sederhana terhadap batasan jumlah objek yang tersedia (2 mobil tergores) untuk menentukan nilai variabel acak.. Bukti: Dari 5 mobil yang dikirim sebuah pabrik, sebanyak 2 mobil tiba dalam keadaan tergores.; Sebuah toko menerima 3 mobil secara acak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar variabel acak diskret dan ruang sampel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari definisi variabel acak pada materi peluang kelas 12, tidak memerlukan perhitungan kompleks atau strategi non-rutin. |

Run 3 — solusi: Total mobil 5 (2 tergores, 3 baik). Toko menerima 3 mobil. X adalah jumlah mobil tergores. Jika toko menerima 3 mobil, kemungkinan kombinasi (G,B) adalah: (0G, 3B), (1G, 2B), atau (2G, 1B). Karena hanya ada 2 mobil tergores, X tidak bisa 3. Karena ada 3 mobil baik, X bisa 0. Jadi, nilai X yang mungkin adalah {0, 1, 2}.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep variabel acak diskret dan menentukan ruang nilai (range) berdasarkan batasan fisik objek (jumlah mobil tergores yang tersedia). Ini melibatkan pemahaman konseptual tentang variabel acak.. Bukti: Variabel acak X menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut.; Tentukan nilai x yang mungkin dari variabel acak X .
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi variabel acak dan batasan nilai yang mungkin dalam konteks distribusi peluang diskret.. Bukti: Variabel acak X menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12 yang mempelajari variabel acak. Siswa hanya perlu mengidentifikasi batasan jumlah mobil tergores (maksimal 2) dan kemungkinan mobil baik (minimal 0).. Bukti: Dari 5 mobil yang dikirim sebuah pabrik, sebanyak 2 mobil tiba dalam keadaan tergores.; Sebuah toko menerima 3 mobil secara acak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar variabel acak diskret dan ruang sampel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi variabel acak adalah standar kurikulum kelas 12. Soal ini menguji pemahaman dasar tentang domain variabel acak tanpa perhitungan kompleks. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Variabel Acak
Tipe soal: multiple_choice
Stimulus: -
Soal: Dari 5 mobil yang dikirim sebuah pabrik, sebanyak 2 mobil tiba dalam keadaan tergores. Sebuah toko menerima 3 mobil secara acak. Misalkan T menyatakan ruang sampel, G untuk kondisi mobil “tergores”, dan B untuk kondisi mobil yang “baik”. Variabel acak X menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut.

Tentukan nilai x yang mungkin dari variabel acak X .
Pilihan: A. {1, 2}
B. {0, 1, 2}
C. {1, 2, 3}
D. {0, 1, 2, 3}
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `1804f5048753053398ea92f2`

Seorang teknisi sepeda motor sedang melakukan pemeriksaan terhadap tiga suku cadang busi motor. Hasil pengamatan dikategorikan dalam suku cadang busi ‘baik’ dan ‘cacat’. X adalah variabel acak yang menyatakan banyak busi cacat.<br><br>Tentukan nilai x yang mungkin dari variabel acak X .

| Opsi | Isi |
|---|---|
| A | {1, 2, 3} |
| B | {0, 1, 2, 3} |
| C | {0, 1, 2} |
| D | {0, 1, 2, 3, 4} |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Variabel acak X menyatakan banyak busi cacat dari 3 busi yang diperiksa. Kemungkinan jumlah busi cacat adalah 0 (semua baik), 1, 2, atau 3 (semua cacat). Maka, nilai x yang mungkin adalah {0, 1, 2, 3}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7948ddb8b499337f495d502a23feb1a15ad5facf5e286c1889557a8d1b6ccc03`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2069 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2085 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2055 |

Run 1 — solusi: Variabel acak X menyatakan banyak busi cacat dari 3 busi yang diperiksa. Kemungkinan jumlah busi cacat adalah 0 (semua baik), 1, 2, atau 3 (semua cacat). Maka, nilai x yang mungkin adalah {0, 1, 2, 3}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi variabel acak diskret dan menentukan ruang sampel dari jumlah kejadian (busi cacat) dalam n percobaan (3 busi). Ini adalah proses menerapkan pemahaman konsep dasar variabel acak.. Bukti: X adalah variabel acak yang menyatakan banyak busi cacat.; Tentukan nilai x yang mungkin dari variabel acak X
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang variabel acak diskret dan bagaimana menentukan nilai yang mungkin dalam ruang sampel.. Bukti: X adalah variabel acak yang menyatakan banyak busi cacat.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan familiar bagi siswa kelas 12 yang mempelajari variabel acak. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: pemeriksaan terhadap tiga suku cadang busi motor; X adalah variabel acak yang menyatakan banyak busi cacat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak diskret dan ruang sampel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi variabel acak adalah topik standar kelas 12. Menentukan nilai yang mungkin dari variabel acak diskret adalah prosedur dasar yang rutin. |

Run 2 — solusi: Variabel acak X menyatakan banyak busi cacat dari 3 busi yang diperiksa. Kemungkinan jumlah busi cacat adalah 0 (tidak ada yang cacat), 1, 2, atau 3 (semua cacat). Maka, nilai x yang mungkin adalah {0, 1, 2, 3}.
- Domain kognitif `classify/knowing`: Siswa hanya perlu memahami definisi variabel acak diskret dan menentukan ruang sampel dari jumlah kejadian yang mungkin terjadi dalam percobaan sederhana (3 objek). Ini adalah proses pengenalan konsep dasar variabel acak.. Bukti: X adalah variabel acak yang menyatakan banyak busi cacat.; Tentukan nilai x yang mungkin dari variabel acak X
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang variabel acak diskret dan bagaimana menentukan nilai-nilai yang mungkin dalam ruang sampel.. Bukti: X adalah variabel acak yang menyatakan banyak busi cacat.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pemahaman tentang ruang sampel dari variabel acak diskret dengan jumlah percobaan yang sangat kecil (n=3). Tidak ada perhitungan kompleks atau strategi non-rutin.. Bukti: pemeriksaan terhadap tiga suku cadang busi motor; X adalah variabel acak yang menyatakan banyak busi cacat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak diskret dan ruang sampel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi variabel acak diajarkan di kelas 12, soal ini merupakan pengenalan konsep yang sangat dasar dan prosedural, sehingga dikategorikan mudah. |

Run 3 — solusi: Variabel acak X menyatakan banyak busi cacat dari 3 busi yang diperiksa. Kemungkinan jumlah busi cacat adalah 0 (tidak ada yang cacat), 1, 2, atau 3 (semua cacat). Maka, ruang sampel nilai X adalah {0, 1, 2, 3}.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi variabel acak diskret dan menentukan ruang sampel berdasarkan jumlah objek yang diamati (3 busi). Ini adalah penerapan langsung dari konsep dasar variabel acak.. Bukti: X adalah variabel acak yang menyatakan banyak busi cacat.; pemeriksaan terhadap tiga suku cadang busi motor.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa itu variabel acak dan bagaimana menentukan nilai yang mungkin dalam konteks percobaan sederhana.. Bukti: X adalah variabel acak yang menyatakan banyak busi cacat.
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dan familiar bagi siswa kelas 12. Tidak ada langkah kompleks atau strategi non-rutin yang diperlukan.. Bukti: pemeriksaan terhadap tiga suku cadang busi motor.; Tentukan nilai x yang mungkin dari variabel acak X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak diskret. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi variabel acak diajarkan di kelas 12, menentukan nilai yang mungkin dari variabel acak diskret adalah konsep dasar yang sangat rutin dan sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3573`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu memahami definisi variabel acak diskret dan menentukan ruang sampel dari jumlah kejadian (busi cacat) dalam n percobaan (3 busi). Ini adalah proses menerapkan pemahaman konsep dasar variabel acak.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang variabel acak diskret dan bagaimana menentukan nilai yang mungkin dalam ruang sampel.
- Intended difficulty `Easy`: Soal ini bersifat langsung dan familiar bagi siswa kelas 12 yang mempelajari variabel acak. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak diskret dan ruang sampel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi variabel acak adalah topik standar kelas 12. Menentukan nilai yang mungkin dari variabel acak diskret adalah prosedur dasar yang rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Variabel Acak
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang teknisi sepeda motor sedang melakukan pemeriksaan terhadap tiga suku cadang busi motor. Hasil pengamatan dikategorikan dalam suku cadang busi ‘baik’ dan ‘cacat’. X adalah variabel acak yang menyatakan banyak busi cacat.

Tentukan nilai x yang mungkin dari variabel acak X .
Pilihan: A. {1, 2, 3}
B. {0, 1, 2, 3}
C. {0, 1, 2}
D. {0, 1, 2, 3, 4}
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `66254f59ca28abbc368aed22`

Misalkan dilakukan sebuah percobaan melempar dua buah dadu seimbang.<br><br>Jika variabel X menyatakan jumlah mata dadu, tentukan nilai-nilai dari variabel X .

| Opsi | Isi |
|---|---|
| A | {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} |
| B | {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} |
| C | {1, 2, 3, 4, 5, 6} |
| D | {2, 3, 4, 5, 6, 7, 8, 9, 10, 11} |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Dua dadu memiliki mata {1, 2, 3, 4, 5, 6}. Jumlah minimum adalah 1+1=2 dan jumlah maksimum adalah 6+6=12. Karena setiap nilai bulat antara 2 dan 12 dapat dibentuk (misal 3=1+2, 4=1+3, dst), maka ruang sampel variabel acak X adalah {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2ae0bea77f761764b4631d01629a08ba2f3b36f9e36ec5f834a51dd23dbe1eab`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2141 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2181 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2192 |

Run 1 — solusi: Dua dadu memiliki mata {1, 2, 3, 4, 5, 6}. Jumlah minimum adalah 1+1=2 dan jumlah maksimum adalah 6+6=12. Karena setiap nilai bulat antara 2 dan 12 dapat dibentuk (misal 3=1+2, 4=1+3, dst), maka ruang sampel variabel acak X adalah {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}.
- Domain kognitif `classify/knowing`: Siswa hanya perlu memahami definisi variabel acak diskret dan melakukan enumerasi sederhana dari ruang sampel dua dadu. Proses ini bersifat langsung dan rutin.. Bukti: variabel X menyatakan jumlah mata dadu; tentukan nilai-nilai dari variabel X
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang variabel acak diskret dan ruang sampel dari percobaan sederhana.. Bukti: variabel X menyatakan jumlah mata dadu
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dalam materi variabel acak diskret. Tidak ada strategi kompleks atau perhitungan berat yang diperlukan.. Bukti: Misalkan dilakukan sebuah percobaan melempar dua buah dadu seimbang.; tentukan nilai-nilai dari variabel X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel percobaan dua dadu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi variabel acak diajarkan di kelas 12, soal ini merupakan pengenalan konsep dasar yang sangat rutin dan familiar bagi siswa. |

Run 2 — solusi: Dua dadu memiliki mata {1, 2, 3, 4, 5, 6}. Nilai minimum jumlah mata dadu adalah 1+1=2 dan nilai maksimum adalah 6+6=12. Karena setiap nilai bulat antara 2 dan 12 dapat dibentuk (misal 3=1+2, 4=1+3, dst), maka ruang sampel variabel acak X adalah {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}.
- Domain kognitif `classify/knowing`: Soal meminta siswa mengidentifikasi ruang sampel dari variabel acak diskret yang didefinisikan sebagai jumlah mata dua dadu. Ini adalah proses langsung mengenali batas bawah dan atas dari penjumlahan dua himpunan diskret.. Bukti: variabel X menyatakan jumlah mata dadu; tentukan nilai-nilai dari variabel X
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep variabel acak diskret dan bagaimana menentukan nilai yang mungkin (range) dari variabel tersebut berdasarkan percobaan pelemparan dua dadu.. Bukti: variabel X menyatakan jumlah mata dadu
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dalam materi variabel acak diskret. Siswa hanya perlu memahami definisi jumlah dua dadu tanpa perhitungan kompleks.. Bukti: Misalkan dilakukan sebuah percobaan melempar dua buah dadu seimbang.; tentukan nilai-nilai dari variabel X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel pelemparan dadu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi variabel acak diajarkan di kelas 12, soal ini merupakan pengenalan konsep dasar yang sangat rutin dan tidak memerlukan strategi tingkat lanjut. |

Run 3 — solusi: Dua dadu masing-masing memiliki mata {1, 2, 3, 4, 5, 6}. Jumlah minimum adalah 1+1=2 dan jumlah maksimum adalah 6+6=12. Karena setiap nilai bulat antara 2 dan 12 dapat dibentuk (misal 3=1+2, 4=1+3, dst), maka ruang sampel variabel acak X adalah {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi ruang sampel dari variabel acak diskret yang didefinisikan sebagai jumlah mata dadu. Proses ini melibatkan pemahaman dasar tentang definisi variabel acak dan ruang sampel, yang merupakan proses langsung tanpa memerlukan strategi kompleks.. Bukti: Misalkan dilakukan sebuah percobaan melempar dua buah dadu seimbang.; Jika variabel X menyatakan jumlah mata dadu, tentukan nilai-nilai dari variabel X
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep variabel acak diskret dan bagaimana menentukan nilai yang mungkin (range) dari variabel tersebut berdasarkan percobaan pelemparan dua dadu.. Bukti: variabel X menyatakan jumlah mata dadu
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dan familiar bagi siswa kelas 12 yang mempelajari variabel acak. Tidak ada langkah kompleks atau strategi nonrutin yang diperlukan.. Bukti: Misalkan dilakukan sebuah percobaan melempar dua buah dadu seimbang.; tentukan nilai-nilai dari variabel X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel pelemparan dua dadu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi variabel acak ada di kelas 12, soal ini merupakan pengenalan dasar (knowing) yang sangat rutin dan tidak menuntut kemampuan analisis tingkat lanjut. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Variabel Acak Diskret
Tipe soal: multiple_choice
Stimulus: -
Soal: Misalkan dilakukan sebuah percobaan melempar dua buah dadu seimbang.

Jika variabel X menyatakan jumlah mata dadu, tentukan nilai-nilai dari variabel X .
Pilihan: A. {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
B. {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
C. {1, 2, 3, 4, 5, 6}
D. {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `09777b6fa2aa7e26f2af2198`

Manakah dari variabel acak berikut yang merupakan variabel acak diskret?

| Opsi | Isi |
|---|---|
| A | Berat bagasi penumpang pesawat |
| B | Berat badan siswa SMA Maju Jaya |
| C | Produksi gabah per hektar |
| D | Jumlah penduduk perempuan di kota B |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Variabel acak diskret adalah variabel yang nilainya diperoleh dari hasil membilang (counting) dan berupa bilangan cacah. Jumlah penduduk perempuan (D) diperoleh dengan membilang, sedangkan berat bagasi (A), berat badan (B), dan produksi gabah (C) diperoleh dengan mengukur, sehingga bersifat kontinu.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bee83f7d7119e4774a20e49ff7aeb285b101a3aa8841200f998d58cf332cc8bc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1932 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1938 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1941 |

Run 1 — solusi: Variabel acak diskret adalah variabel yang nilainya diperoleh dari hasil membilang (counting) dan berupa bilangan cacah. Jumlah penduduk perempuan (D) diperoleh dengan membilang, sedangkan berat bagasi (A), berat badan (B), dan produksi gabah (C) diperoleh dengan mengukur, sehingga bersifat kontinu.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi definisi variabel acak diskret di antara pilihan yang diberikan. Siswa hanya perlu mengenali karakteristik data (hasil membilang vs hasil mengukur).. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang perbedaan antara variabel acak diskret dan kontinu.. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?
- Intended difficulty `classify/Easy`: Soal ini bersifat mendasar dan langsung menguji pemahaman definisi tanpa memerlukan perhitungan atau langkah prosedural yang kompleks.. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi variabel acak diskret dan kontinu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi variabel acak diajarkan di kelas 12, konsep dasar diskret vs kontinu adalah materi pengantar yang sangat mendasar dan familiar. |

Run 2 — solusi: Variabel acak diskret adalah variabel yang nilainya diperoleh dari hasil membilang (counting) dan berupa bilangan cacah. Jumlah penduduk (opsi D) adalah hasil membilang, sedangkan berat (opsi A, B) dan produksi/massa (opsi C) adalah hasil pengukuran yang bersifat kontinu.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi definisi variabel acak diskret di antara beberapa contoh. Siswa hanya perlu mengenali karakteristik data (hasil membilang vs hasil pengukuran), yang merupakan proses kognitif knowing.. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa mengenai konsep dasar variabel acak diskret dan kontinu, yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung dan menguji pemahaman definisi dasar tanpa memerlukan perhitungan atau langkah prosedural yang kompleks.. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi variabel acak diskret dan kontinu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi variabel acak adalah dasar statistika kelas 12. Soal ini adalah pengenalan konsep dasar yang sangat standar. |

Run 3 — solusi: Variabel acak diskret adalah variabel yang nilainya diperoleh dari hasil membilang (counting) dan berupa bilangan cacah. Jumlah penduduk perempuan (D) diperoleh dengan membilang, sedangkan berat bagasi (A), berat badan (B), dan produksi gabah (C) diperoleh dengan mengukur, sehingga bersifat kontinu.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi definisi variabel acak diskret di antara beberapa contoh situasi nyata. Ini adalah proses pengenalan konsep dasar.. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami perbedaan konseptual antara data yang diperoleh melalui proses membilang (diskret) dan mengukur (kontinu).. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan langsung menguji pemahaman definisi dasar variabel acak diskret tanpa memerlukan perhitungan atau langkah prosedural yang kompleks.. Bukti: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak diskret vs kontinu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pengenalan awal materi variabel acak di kelas 12, sehingga tingkat kesulitannya rendah karena hanya menguji pemahaman konsep dasar. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Variabel Acak Diskret
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah dari variabel acak berikut yang merupakan variabel acak diskret?
Pilihan: A. Berat bagasi penumpang pesawat
B. Berat badan siswa SMA Maju Jaya
C. Produksi gabah per hektar
D. Jumlah penduduk perempuan di kota B
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `0037f3f74a623f62a7255394`

Pada musim kemarau suhu udara harian di sebuah kota berkisar dari 25,5˚C hingga 30˚C. Misalkan X adalah variabel acak yang menyatakan suhu udara harian dalam derajat Celsius.<br><br>Buatlah taksiran bentuk ruang sampel dari variabel acak suhu harian tersebut.

| Opsi | Isi |
|---|---|
| A | $S=\{x \mid 25,5 \le x \le 30,\ x \in \mathbb{R}\}$ |
| B | $S=\{x \mid 25,5 \le x \le 30,\ x \in \mathbb{Z}\}$ |
| C | $S=\{25,5;\ 30\}$ |
| D | $S=\{26, 27, 28, 29, 30\}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Variabel acak suhu udara bersifat kontinu karena dapat mengambil nilai real apa pun dalam rentang tertentu. Rentang suhu adalah 25,5 hingga 30 derajat Celsius, sehingga ruang sampelnya adalah interval tertutup [25,5, 30] dalam himpunan bilangan real, ditulis sebagai {x \| 25,5 ≤ x ≤ 30, x ∈ ℝ}.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d8f2184d8f28075002e9d2e09d6e281069cd227a60400c60055986d496b1a644`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2128 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2071 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2092 |

Run 1 — solusi: Variabel acak suhu udara bersifat kontinu karena dapat mengambil nilai real apa pun dalam rentang tertentu. Rentang suhu adalah 25,5 hingga 30 derajat Celsius, sehingga ruang sampelnya adalah interval tertutup [25,5, 30] dalam himpunan bilangan real, ditulis sebagai {x \| 25,5 ≤ x ≤ 30, x ∈ ℝ}.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi definisi ruang sampel untuk variabel acak kontinu berdasarkan konteks suhu. Siswa perlu mengenali bahwa suhu adalah besaran kontinu yang mencakup semua nilai real dalam interval tertentu, bukan sekadar bilangan bulat atau titik diskret.. Bukti: X adalah variabel acak yang menyatakan suhu udara harian; berkisar dari 25,5˚C hingga 30˚C
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep dasar variabel acak kontinu dan bagaimana merepresentasikannya dalam notasi himpunan (notasi pembentuk himpunan) untuk interval bilangan real.. Bukti: variabel acak yang menyatakan suhu udara harian; 25,5˚C hingga 30˚C
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman dasar tentang definisi variabel acak kontinu. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: berkisar dari 25,5˚C hingga 30˚C; taksiran bentuk ruang sampel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan real dan interval. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah pengenalan dasar terhadap variabel acak kontinu di kelas 12, yang merupakan prosedur standar dalam kurikulum. |

Run 2 — solusi: Variabel acak kontinu didefinisikan pada interval bilangan real. Suhu udara dapat bernilai bilangan real apa pun dalam rentang [25,5; 30]. Maka ruang sampelnya adalah S = {x \| 25,5 <= x <= 30, x elemen R}.
- Domain kognitif `classify/knowing`: Soal meminta identifikasi definisi ruang sampel untuk variabel acak kontinu. Siswa hanya perlu mengenali bahwa suhu adalah variabel kontinu yang mencakup semua nilai real dalam interval tertentu, bukan diskret.. Bukti: X adalah variabel acak yang menyatakan suhu udara harian; taksiran bentuk ruang sampel dari variabel acak suhu harian
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang perbedaan antara variabel acak diskret dan kontinu serta cara merepresentasikan ruang sampelnya dalam notasi himpunan.. Bukti: variabel acak yang menyatakan suhu udara harian; taksiran bentuk ruang sampel
- Intended difficulty `classify/Easy`: Soal ini bersifat mendasar (fundamental) dalam topik variabel acak kontinu. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: suhu udara harian dalam derajat Celsius; taksiran bentuk ruang sampel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan real dan interval. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar variabel acak kontinu yang diajarkan di awal bab kelas 12. |

Run 3 — solusi: Variabel acak suhu udara bersifat kontinu karena dapat mengambil nilai real apa pun dalam rentang tertentu. Rentang suhu adalah 25,5 hingga 30, sehingga ruang sampelnya adalah himpunan semua bilangan real x yang memenuhi 25,5 <= x <= 30.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi definisi ruang sampel untuk variabel acak kontinu. Siswa perlu memahami perbedaan antara variabel acak diskret dan kontinu serta notasi himpunan yang tepat untuk interval bilangan real.. Bukti: X adalah variabel acak yang menyatakan suhu udara harian; taksiran bentuk ruang sampel dari variabel acak suhu harian
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep konseptual tentang variabel acak kontinu yang mencakup rentang nilai tak hingga dalam interval tertentu, bukan sekadar menghafal prosedur.. Bukti: variabel acak yang menyatakan suhu udara harian; taksiran bentuk ruang sampel
- Intended difficulty `classify/Easy`: Soal ini bersifat mendasar dalam topik variabel acak kontinu. Siswa hanya perlu mengenali bahwa suhu adalah besaran kontinu dan memilih notasi interval yang benar.. Bukti: suhu udara harian dalam derajat Celsius; berkisar dari 25,5˚C hingga 30˚C

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak kontinu dan notasi himpunan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep pengantar untuk variabel acak kontinu di kelas 12, yang merupakan prosedur standar dalam kurikulum. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Variabel Acak Kontinu
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada musim kemarau suhu udara harian di sebuah kota berkisar dari 25,5˚C hingga 30˚C. Misalkan X adalah variabel acak yang menyatakan suhu udara harian dalam derajat Celsius.

Buatlah taksiran bentuk ruang sampel dari variabel acak suhu harian tersebut.
Pilihan: A. $S=\{x \mid 25,5 \le x \le 30,\ x \in \mathbb{R}\}$
B. $S=\{x \mid 25,5 \le x \le 30,\ x \in \mathbb{Z}\}$
C. $S=\{25,5;\ 30\}$
D. $S=\{26, 27, 28, 29, 30\}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `a975e5253d6dc458eae4244b`

Pada musim kemarau suhu udara harian di sebuah kota berkisar dari 25,5˚C hingga 30˚C. Misalkan X adalah variabel acak yang menyatakan suhu udara harian dalam derajat Celsius.<br><br>Apakah semua nilai dalam ruang sampel tersebut dapat dihitung satu per satu? Jelaskan alasanmu.

| Opsi | Isi |
|---|---|
| A | Ya, karena suhu hanya berkisar dari 25,5˚C hingga 30˚C sehingga nilainya terbatas |
| B | Ya, karena suhu selalu dapat dibulatkan menjadi bilangan bulat sehingga dapat dicacah |
| C | Tidak, karena ruang sampel memuat semua bilangan real dalam rentang itu sehingga nilainya tak terhitung |
| D | Tidak, karena suhu udara harian dapat bernilai negatif maupun positif |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Suhu udara adalah variabel acak kontinu karena dapat mengambil nilai real apa pun dalam interval [25,5, 30]. Himpunan bilangan real dalam interval tersebut bersifat tak terhitung (uncountable), sehingga tidak dapat dicacah satu per satu.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c30cc76f9eee03efb972202eef6facaa0cf31a2e49088c566735c4623384dd68`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Easy | 2085 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2113 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2813 |

Run 1 — solusi: Suhu udara adalah variabel acak kontinu karena dapat mengambil nilai apa pun dalam interval [25,5, 30]. Himpunan bilangan real dalam interval tersebut bersifat tak terhitung (uncountable), sehingga tidak dapat dicacah satu per satu.
- Domain kognitif `classify/reasoning`: Soal ini menuntut pemahaman konseptual tentang perbedaan antara variabel acak diskret dan kontinu. Siswa harus mengidentifikasi bahwa suhu, sebagai besaran fisik yang diukur pada skala kontinu, mencakup tak hingga nilai real dalam interval tertentu, sehingga tidak dapat dihitung (uncountable). Ini adalah proses penalaran konseptual dasar.. Bukti: Apakah semua nilai dalam ruang sampel tersebut dapat dihitung satu per satu?; suhu udara harian dalam derajat Celsius
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang sifat variabel acak kontinu, yang merupakan konsep fundamental dalam statistika inferensial di kelas 12.. Bukti: variabel acak yang menyatakan suhu udara harian; ruang sampel memuat semua bilangan real dalam rentang itu
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung. Siswa hanya perlu memahami definisi variabel acak kontinu tanpa melakukan perhitungan matematis yang kompleks.. Bukti: suhu udara harian dalam derajat Celsius; berkisar dari 25,5˚C hingga 30˚C

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan real dan konsep variabel acak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan konseptual dasar yang diharapkan dikuasai siswa kelas 12 saat mempelajari variabel acak kontinu. |

Run 2 — solusi: Suhu udara adalah variabel acak kontinu karena dapat mengambil nilai apa pun dalam interval [25,5; 30]. Himpunan bilangan real dalam interval tersebut bersifat tak terhitung (uncountable), sehingga tidak dapat dicacah satu per satu.
- Domain kognitif `classify/applying`: Soal ini menuntut pemahaman konseptual tentang perbedaan antara variabel acak diskret (terhitung) dan kontinu (tak terhitung). Siswa harus mengidentifikasi sifat suhu sebagai variabel kontinu yang mencakup seluruh bilangan real dalam interval tertentu, bukan sekadar menghafal definisi.. Bukti: Apakah semua nilai dalam ruang sampel tersebut dapat dihitung satu per satu?; suhu adalah variabel kontinu dengan nilai real tak terhitung
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual mengenai sifat variabel acak kontinu, yaitu bahwa nilai-nilainya membentuk kontinum bilangan real yang tidak dapat dicacah (uncountable), yang merupakan prinsip dasar dalam teori peluang kontinu.. Bukti: suhu udara harian dalam derajat Celsius; ruang sampel memuat semua bilangan real dalam rentang itu
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena menguji pemahaman dasar tentang definisi variabel acak kontinu. Tidak ada perhitungan matematis yang kompleks, hanya pemahaman konseptual mengenai sifat himpunan bilangan real pada interval tertentu.. Bukti: suhu udara harian dalam derajat Celsius; Apakah semua nilai dalam ruang sampel tersebut dapat dihitung satu per satu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel acak diskret vs kontinu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan memahami perbedaan fundamental antara variabel acak diskret dan kontinu sebagai prasyarat untuk mempelajari fungsi densitas peluang. |

Run 3 — solusi: Suhu udara adalah variabel acak kontinu karena dapat mengambil nilai real apa pun dalam interval [25,5, 30]. Himpunan bilangan real dalam interval tersebut tidak dapat dihitung (uncountable), sehingga tidak dapat dicacah satu per satu.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual tentang perbedaan antara variabel acak diskret dan kontinu. Siswa hanya perlu mengenali sifat dasar suhu sebagai variabel kontinu.. Bukti: Apakah semua nilai dalam ruang sampel tersebut dapat dihitung satu per satu?; suhu adalah variabel kontinu dengan nilai real tak terhitung
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep variabel acak kontinu dan sifat himpunan bilangan real yang tidak terhitung.. Bukti: X adalah variabel acak yang menyatakan suhu udara harian; ruang sampel memuat semua bilangan real dalam rentang itu
- Intended difficulty `classify/Easy`: Soal ini menanyakan definisi dasar variabel acak kontinu. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Apakah semua nilai dalam ruang sampel tersebut dapat dihitung satu per satu?; suhu adalah variabel kontinu dengan nilai real tak terhitung

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi variabel acak diskret dan kontinu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pemahaman konsep dasar dalam materi variabel acak kontinu kelas 12, yang biasanya diajarkan di awal bab. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 1, "knowing": 1} | no_consensus / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3605`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menguji pemahaman konseptual dasar mengenai perbedaan antara variabel acak diskret dan kontinu. Siswa perlu mengenali sifat suhu sebagai variabel kontinu yang mencakup tak hingga nilai real dalam interval tertentu, yang merupakan proses 'knowing' atau pengenalan konsep dasar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang konsep variabel acak kontinu dan sifat himpunan bilangan real yang tidak terhitung (uncountable), yang merupakan pengetahuan konseptual.
- Intended difficulty `Easy`: Soal ini bersifat konseptual dan langsung. Tidak ada perhitungan matematis yang kompleks atau strategi non-rutin yang diperlukan. Siswa hanya perlu memahami definisi dasar variabel acak kontinu.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi variabel acak diskret dan kontinu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pemahaman konsep dasar dalam materi variabel acak kontinu kelas 12, yang biasanya diajarkan di awal bab. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Variabel Acak Kontinu
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada musim kemarau suhu udara harian di sebuah kota berkisar dari 25,5˚C hingga 30˚C. Misalkan X adalah variabel acak yang menyatakan suhu udara harian dalam derajat Celsius.

Apakah semua nilai dalam ruang sampel tersebut dapat dihitung satu per satu? Jelaskan alasanmu.
Pilihan: A. Ya, karena suhu hanya berkisar dari 25,5˚C hingga 30˚C sehingga nilainya terbatas
B. Ya, karena suhu selalu dapat dibulatkan menjadi bilangan bulat sehingga dapat dicacah
C. Tidak, karena ruang sampel memuat semua bilangan real dalam rentang itu sehingga nilainya tak terhitung
D. Tidak, karena suhu udara harian dapat bernilai negatif maupun positif
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `d8a1f35b897fbd2b2a14ac0e`

Sebuah kantong berisi 5 bola putih, 2 bola hitam, dan 3 bola merah. Sebanyak 3 bola diambil satu demi satu secara acak.<br><br>Tentukan distribusi peluang variabel acak diskret terambilnya bola merah.

| Opsi | Isi |
|---|---|
| A | y = 0, 1, 2, 3 dengan f(y) = 7/24, 21/40, 7/40, 1/120 |
| B | y = 0, 1, 2, 3 dengan f(y) = 1/4, 1/4, 1/4, 1/4 |
| C | y = 0, 1, 2, 3 dengan f(y) = 1/120, 7/40, 21/40, 7/24 |
| D | y = 0, 1, 2, 3 dengan f(y) = 343/1000, 441/1000, 189/1000, 27/1000 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total bola 10, merah 3, non-merah 7. Diambil 3 bola tanpa pengembalian (distribusi hipergeometrik). P(Y=y) = C(3,y)C(7,3-y)/C(10,3) dengan C(10,3)=120. P(0)=C(3,0)C(7,3)/120=35/120=7/24. P(1)=C(3,1)C(7,2)/120=63/120=21/40. P(2)=C(3,2)C(7,1)/120=21/120=7/40. P(3)=C(3,3)C(7,0)/120=1/120. Hasil: 7/24, 21/40, 7/40, 1/120.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6baa323f1e0a0dbb24d7f29b254a1786c194e972fdb8a572660812d5c17d8fa4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3502 |
| 2 | success | valid / verified | applying | procedural | Medium | 3198 |
| 3 | success | valid / verified | applying | procedural | Medium | 2461 |

Run 1 — solusi: Total bola 10, merah 3, non-merah 7. Diambil 3 bola tanpa pengembalian (distribusi hipergeometrik). P(Y=y) = C(3,y)C(7,3-y)/C(10,3) dengan C(10,3)=120. P(0)=C(3,0)C(7,3)/120=35/120=7/24. P(1)=C(3,1)C(7,2)/120=63/120=21/40. P(2)=C(3,2)C(7,1)/120=21/120=7/40. P(3)=C(3,3)C(7,0)/120=1/120. Hasil: 7/24, 21/40, 7/40, 1/120.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa pengambilan bola tanpa pengembalian mengikuti distribusi hipergeometrik, memilih rumus kombinasi yang tepat, dan menghitung peluang untuk setiap nilai variabel acak.. Bukti: Tentukan distribusi peluang variabel acak diskret terambilnya bola merah.; C(3,y)·C(7,3−y)/C(10,3)
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma perhitungan peluang menggunakan rumus kombinasi untuk variabel acak diskret.. Bukti: C(3,y)·C(7,3−y)/C(10,3)
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan model distribusi yang tepat (hipergeometrik) dan perhitungan berulang untuk setiap nilai variabel acak, yang merupakan langkah rutin namun memerlukan ketelitian.. Bukti: Sebuah kantong berisi 5 bola putih, 2 bola hitam, dan 3 bola merah.; Sebanyak 3 bola diambil satu demi satu secara acak.; C(3,y)·C(7,3−y)/C(10,3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep kombinasi dan variabel acak diskret. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai dengan tuntutan kurikulum kelas 12 TL pada materi variabel acak diskret dan fungsi peluang. |

Run 2 — solusi: Total bola 10, merah 3, bukan merah 7. Pengambilan 3 bola tanpa pengembalian mengikuti distribusi hipergeometrik: f(y) = C(3,y)C(7,3-y)/C(10,3). C(10,3)=120. f(0)=C(3,0)C(7,3)/120=35/120=7/24; f(1)=C(3,1)C(7,2)/120=63/120=21/40; f(2)=C(3,2)C(7,1)/120=21/120=7/40; f(3)=C(3,3)C(7,0)/120=1/120.
- Domain kognitif `classify/applying`: Siswa perlu memilih model distribusi yang tepat (hipergeometrik) untuk situasi pengambilan tanpa pengembalian dan menerapkan rumus kombinasi untuk menghitung peluang setiap nilai variabel acak.. Bukti: Tentukan distribusi peluang variabel acak diskret terambilnya bola merah.; f(y) = C(3,y)·C(7,3−y)/C(10,3)
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma perhitungan peluang menggunakan rumus kombinasi dan distribusi hipergeometrik.. Bukti: f(y) = C(3,y)·C(7,3−y)/C(10,3)
- Intended difficulty `classify/Medium`: Soal memerlukan pemilihan model distribusi yang tepat (hipergeometrik) dan membedakannya dari distribusi binomial, serta melakukan perhitungan kombinasi yang berjenjang.. Bukti: Sebanyak 3 bola diambil satu demi satu secara acak.; memakai distribusi binomial (pengambilan dengan pengembalian, p = 3/10)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep kombinasi dan definisi variabel acak diskret. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan mampu membedakan pengambilan dengan dan tanpa pengembalian untuk menentukan model peluang yang sesuai. |

Run 3 — solusi: Variabel acak Y adalah jumlah bola merah terambil dari 3 bola. Total bola = 10, bola merah = 3, bola bukan merah = 7. Menggunakan distribusi hipergeometrik: f(y) = C(3,y) * C(7,3-y) / C(10,3). C(10,3) = 120. f(0) = C(3,0)*C(7,3)/120 = 35/120 = 7/24. f(1) = C(3,1)*C(7,2)/120 = 3*21/120 = 63/120 = 21/40. f(2) = C(3,2)*C(7,1)/120 = 3*7/120 = 21/120 = 7/40. f(3) = C(3,3)*C(7,0)/120 = 1/120.
- Domain kognitif `classify/applying`: Siswa diminta menentukan fungsi peluang variabel acak diskret dari eksperimen pengambilan bola tanpa pengembalian. Ini memerlukan pemilihan model distribusi yang tepat (hipergeometrik) dan perhitungan kombinasi, yang merupakan penerapan prosedur standar dalam kurikulum.. Bukti: Tentukan distribusi peluang variabel acak diskret terambilnya bola merah.; f(y) = C(3,y)·C(7,3−y)/C(10,3)
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang konsep variabel acak diskret dan penerapan rumus distribusi peluang (hipergeometrik) untuk menghitung nilai fungsi peluang pada setiap titik sampel.. Bukti: Tentukan distribusi peluang variabel acak diskret terambilnya bola merah.
- Intended difficulty `classify/Medium`: Soal ini merupakan prosedur rutin dalam materi variabel acak diskret. Siswa hanya perlu mengidentifikasi bahwa ini adalah kasus pengambilan tanpa pengembalian (hipergeometrik) dan menghitung nilai fungsi untuk setiap y. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Sebuah kantong berisi 5 bola putih, 2 bola hitam, dan 3 bola merah. Sebanyak 3 bola diambil satu demi satu secara acak.; Tentukan distribusi peluang variabel acak diskret terambilnya bola merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep kombinasi dan dasar variabel acak diskret. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun prosedural, soal ini memerlukan ketelitian dalam menghitung kombinasi untuk setiap nilai y dan membedakan antara pengambilan dengan dan tanpa pengembalian (distraktor binomial). |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Fungsi Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong berisi 5 bola putih, 2 bola hitam, dan 3 bola merah. Sebanyak 3 bola diambil satu demi satu secara acak.

Tentukan distribusi peluang variabel acak diskret terambilnya bola merah.
Pilihan: A. y = 0, 1, 2, 3 dengan f(y) = 7/24, 21/40, 7/40, 1/120
B. y = 0, 1, 2, 3 dengan f(y) = 1/4, 1/4, 1/4, 1/4
C. y = 0, 1, 2, 3 dengan f(y) = 1/120, 7/40, 21/40, 7/24
D. y = 0, 1, 2, 3 dengan f(y) = 343/1000, 441/1000, 189/1000, 27/1000
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `9133baff53cec4911da232b1`

Dalam Ulangan Tengah Semester, diberikan 3 soal yang masing-masing jawabannya benar atau salah. Jika X menyatakan jawaban benar dari 3 soal tersebut,<br><br>susunlah distribusi peluang variabel acak X.

| Opsi | Isi |
|---|---|
| A | x = 0, 1, 2, 3 dengan f(x) = 0,375; 0,125; 0,125; 0,375 |
| B | x = 0, 1, 2, 3 dengan f(x) = 0,125; 0,125; 0,375; 0,375 |
| C | x = 0, 1, 2, 3 dengan f(x) = 0,125; 0,375; 0,375; 0,125 |
| D | x = 0, 1, 2, 3 dengan f(x) = 0,25; 0,25; 0,25; 0,25 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: X berdistribusi binomial dengan n=3 dan p=0,5. P(X=x) = C(3,x) * (0,5)^3. P(X=0) = 1 * 0,125 = 0,125; P(X=1) = 3 * 0,125 = 0,375; P(X=2) = 3 * 0,125 = 0,375; P(X=3) = 1 * 0,125 = 0,125.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `87cc176c6621eeff03b48dbc157d722570f6980ace14eec28693976b1d4cd5a7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3077 |
| 2 | success | valid / verified | applying | procedural | Medium | 3091 |
| 3 | success | valid / verified | applying | procedural | Easy | 3078 |

Run 1 — solusi: Variabel acak X berdistribusi binomial dengan n=3 dan p=0,5. P(X=x) = C(3,x) * (0,5)^3. P(X=0)=1/8=0,125; P(X=1)=3/8=0,375; P(X=2)=3/8=0,375; P(X=3)=1/8=0,125.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus distribusi binomial untuk menentukan peluang setiap nilai variabel acak diskret.. Bukti: Jika X menyatakan jawaban benar dari 3 soal tersebut, susunlah distribusi peluang variabel acak X.
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman tentang konsep variabel acak diskret dan prosedur perhitungan peluang binomial.. Bukti: susunlah distribusi peluang variabel acak X
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus distribusi binomial dengan parameter yang jelas. Prosedur standar dan familiar bagi siswa kelas 12.. Bukti: 3 soal yang masing-masing jawabannya benar atau salah; susunlah distribusi peluang variabel acak X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang dan kombinasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi peluang binomial adalah standar kurikulum kelas 12, soal ini tidak memerlukan modifikasi strategi. |

Run 2 — solusi: X berdistribusi binomial dengan n=3, p=0,5. P(X=x) = C(3,x) * (0,5)^3. P(X=0)=1*0,125=0,125; P(X=1)=3*0,125=0,375; P(X=2)=3*0,125=0,375; P(X=3)=1*0,125=0,125.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus distribusi binomial atau menghitung ruang sampel untuk menentukan peluang setiap nilai X.. Bukti: Jika X menyatakan jawaban benar dari 3 soal tersebut, susunlah distribusi peluang variabel acak X.
- Dimensi pengetahuan `classify/procedural`: Melibatkan penggunaan algoritma atau teknik perhitungan peluang variabel acak diskret.. Bukti: susunlah distribusi peluang variabel acak X
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang distribusi binomial atau ruang sampel sederhana. Prosedur standar untuk kelas 12.. Bukti: 3 soal yang masing-masing jawabannya benar atau salah; susunlah distribusi peluang variabel acak X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, kombinasi, dan variabel acak diskret. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai kurikulum kelas 12, ini adalah penerapan rutin distribusi binomial. |

Run 3 — solusi: X berdistribusi binomial dengan n=3 dan p=0,5. P(X=x) = C(3,x) * (0,5)^3. f(0)=1/8=0,125; f(1)=3/8=0,375; f(2)=3/8=0,375; f(3)=1/8=0,125.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus distribusi binomial untuk menghitung peluang setiap nilai variabel acak X.. Bukti: X menyatakan jawaban benar dari 3 soal tersebut; susunlah distribusi peluang variabel acak X
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma atau teknik perhitungan peluang binomial yang sudah dipelajari.. Bukti: susunlah distribusi peluang variabel acak X
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus binomial dengan parameter sederhana (n=3, p=0,5). Prosedur ini sangat familiar di kelas 12.. Bukti: 3 soal yang masing-masing jawabannya benar atau salah; X menyatakan jawaban benar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang dan kombinasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi binomial adalah standar kurikulum kelas 12 dan soal ini menggunakan parameter dasar tanpa variasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3585`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan rumus distribusi binomial untuk menentukan peluang setiap nilai variabel acak diskret secara langsung.
- Dimensi pengetahuan `procedural`: Memerlukan pemahaman tentang konsep variabel acak diskret dan prosedur perhitungan peluang binomial.
- Intended difficulty `Easy`: Soal ini merupakan penerapan langsung rumus distribusi binomial dengan parameter yang jelas dan sederhana (n=3, p=0,5). Prosedur ini sangat standar dan familiar bagi siswa kelas 12.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang dan kombinasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi peluang binomial adalah standar kurikulum kelas 12, soal ini tidak memerlukan modifikasi strategi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Fungsi Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam Ulangan Tengah Semester, diberikan 3 soal yang masing-masing jawabannya benar atau salah. Jika X menyatakan jawaban benar dari 3 soal tersebut,

susunlah distribusi peluang variabel acak X.
Pilihan: A. x = 0, 1, 2, 3 dengan f(x) = 0,375; 0,125; 0,125; 0,375
B. x = 0, 1, 2, 3 dengan f(x) = 0,125; 0,125; 0,375; 0,375
C. x = 0, 1, 2, 3 dengan f(x) = 0,125; 0,375; 0,375; 0,125
D. x = 0, 1, 2, 3 dengan f(x) = 0,25; 0,25; 0,25; 0,25
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `7733fb51a5db0b2c47e439d3`

Suatu variabel acak kontinu X, untuk nilai-nilai di antara $x=1$ dan $x=5$, dinyatakan dengan fungsi peluang $f(x)=\frac{x+2}{20}$.<br><br>Hitunglah $P(X<4)$.

| Opsi | Isi |
|---|---|
| A | 0,3 |
| B | 0,8 |
| C | 0,325 |
| D | 0,675 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: P(X<4) = ∫_1^4 (x+2)/20 dx = (1/20) * [0,5x^2 + 2x]_1^4 = (1/20) * [(8+8) - (0,5+2)] = (1/20) * 13,5 = 0,675.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a26b8d3cb28a6fb0d2ffae74c165ae624a13a9138218e6263ef2ffbfb54cf200`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2746 |
| 2 | success | valid / verified | applying | procedural | Medium | 2705 |
| 3 | success | valid / verified | applying | procedural | Easy | 2717 |

Run 1 — solusi: P(X<4) = integral dari 1 sampai 4 dari (x+2)/20 dx = 1/20 * [0,5x^2 + 2x] dengan batas 1 sampai 4. Hasilnya = 1/20 * [(8+8) - (0,5+2)] = 1/20 * 13,5 = 0,675.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep integral tentu untuk menghitung peluang variabel acak kontinu dengan batas yang ditentukan.. Bukti: Hitunglah P(X<4); fungsi peluang f(x)=(x+2)/20
- Dimensi pengetahuan `classify/procedural`: Melibatkan penerapan algoritma integrasi fungsi linear dan evaluasi batas integral tentu.. Bukti: fungsi peluang f(x)=(x+2)/20; Hitunglah P(X<4)
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang batas integral yang sesuai dengan domain fungsi dan eksekusi prosedur integrasi yang rutin.. Bukti: variabel acak kontinu X; nilai-nilai di antara x=1 dan x=5; Hitunglah P(X<4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral tentu fungsi aljabar sederhana |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 TL, menguji kemampuan teknis integrasi dalam konteks peluang kontinu. |

Run 2 — solusi: P(X<4) = ∫_1^4 (x+2)/20 dx = (1/20) * [0.5x^2 + 2x]_1^4 = (1/20) * [(8+8) - (0.5+2)] = (1/20) * 13.5 = 0.675.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep integral tentu untuk menghitung peluang variabel acak kontinu pada interval yang ditentukan.. Bukti: Hitunglah P(X<4); fungsi peluang f(x)=(x+2)/20
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritma integrasi fungsi linear untuk menentukan nilai peluang.. Bukti: fungsi peluang f(x)=(x+2)/20; Hitunglah P(X<4)
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang batas integral yang sesuai dengan domain fungsi dan perhitungan aritmatika dasar.. Bukti: variabel acak kontinu X, untuk nilai-nilai di antara x=1 dan x=5; Hitunglah P(X<4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral tentu fungsi aljabar sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal standar kelas 12 TL yang menguji pemahaman variabel acak kontinu dengan batas integral yang eksplisit. |

Run 3 — solusi: P(X<4) = integral dari 1 sampai 4 (x+2)/20 dx = 1/20 * [0,5x^2 + 2x] batas 1 sampai 4 = 1/20 * [(8+8) - (0,5+2)] = 1/20 * 13,5 = 0,675.
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep integral tentu untuk menghitung peluang variabel acak kontinu pada interval yang diberikan.. Bukti: Hitunglah P(X<4); fungsi peluang f(x)=(x+2)/20
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma integrasi fungsi aljabar sederhana untuk menyelesaikan masalah peluang.. Bukti: f(x)=(x+2)/20; P(X<4)=integral 1 sampai 4 f(x)dx
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam materi variabel acak kontinu kelas 12 yang dapat diselesaikan dengan langkah rutin.. Bukti: variabel acak kontinu X; P(X<4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral tentu fungsi aljabar sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi variabel acak kontinu dan penggunaan integral untuk peluang adalah standar kurikulum kelas 12 TL, soal ini tidak memerlukan strategi non-rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3530`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep integral tentu untuk menghitung peluang variabel acak kontinu pada interval yang ditentukan. Ini adalah penerapan langsung dari prosedur yang dipelajari.
- Dimensi pengetahuan `procedural`: Soal menuntut penerapan algoritma integrasi fungsi linear dan evaluasi batas integral tentu sebagai teknik standar dalam statistika.
- Intended difficulty `Easy`: Soal ini merupakan prosedur standar dalam materi variabel acak kontinu kelas 12 yang dapat diselesaikan dengan langkah rutin tanpa memerlukan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Integral tentu fungsi aljabar sederhana |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi variabel acak kontinu dan penggunaan integral untuk peluang adalah standar kurikulum kelas 12 TL. Soal ini bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Fungsi Densitas Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu variabel acak kontinu X, untuk nilai-nilai di antara $x=1$ dan $x=5$, dinyatakan dengan fungsi peluang $f(x)=\frac{x+2}{20}$.

Hitunglah $P(X<4)$.
Pilihan: A. 0,3
B. 0,8
C. 0,325
D. 0,675
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `8ed8a4e5fac590ce4f348150`

Dalam masa pandemi Covid-19, suatu toko hanya beroperasi selama 180 menit, yaitu mulai pukul 08.00 hingga pukul 11.00. Pembeli tidak diperbolehkan berada di dalam toko tersebut sebelum pukul 08.00. Pembeli juga harus meninggalkan toko paling lambat pukul 11.00. Misalkan X adalah variabel acak yang menyatakan lama pembeli berada di dalam toko (dalam menit). Fungsi densitas peluang X dinyatakan dengan $f(x)=\begin{cases}\frac{1}{180}, & 0 \le x \le 180\\ 0, & x<0 \text{ atau } x>180\end{cases}$<br><br>Berapakah peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit

| Opsi | Isi |
|---|---|
| A | $\frac{1}{2}$ |
| B | $\frac{1}{3}$ |
| C | $\frac{1}{4}$ |
| D | $\frac{1}{12}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: P(15 < X < 60) = integral dari 15 sampai 60 (1/180) dx = (60-15)/180 = 45/180 = 1/4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d6a02adb84cc360044903e533e211b1132d4cd117d245753662729dce9270bf9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3078 |
| 2 | success | valid / verified | applying | procedural | Easy | 2224 |
| 3 | success | valid / verified | applying | procedural | Easy | 2251 |

Run 1 — solusi: P(15 < X < 60) = integral dari 15 sampai 60 (1/180) dx = (60-15)/180 = 45/180 = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep fungsi densitas peluang untuk distribusi seragam (uniform) dengan mengintegralkan fungsi pada interval yang diberikan.. Bukti: Fungsi densitas peluang X dinyatakan dengan f(x)=1/180; Berapakah peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam menghitung peluang variabel acak kontinu menggunakan fungsi densitas yang diberikan.. Bukti: Fungsi densitas peluang X dinyatakan dengan f(x)=1/180; Berapakah peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit
- Intended difficulty `classify/Easy`: Soal ini merupakan aplikasi langsung dari definisi fungsi densitas peluang untuk distribusi uniform. Tidak ada langkah non-rutin atau kompleksitas tinggi.. Bukti: Fungsi densitas peluang X dinyatakan dengan f(x)=1/180; Berapakah peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi densitas peluang dan integral tentu sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12, merupakan penerapan standar dari materi variabel acak kontinu. |

Run 2 — solusi: P(15 < X < 60) = integral dari 15 sampai 60 dari (1/180) dx = (60 - 15) / 180 = 45 / 180 = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep integral fungsi densitas peluang seragam (uniform distribution) untuk menghitung peluang pada interval tertentu. Ini adalah penerapan langsung dari definisi peluang kontinu.. Bukti: Fungsi densitas peluang X dinyatakan dengan f(x)=1/180, 0 <= x <= 180; Berapakah peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung peluang variabel acak kontinu menggunakan fungsi densitas yang diberikan.. Bukti: Fungsi densitas peluang X dinyatakan dengan f(x)=1/180
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk materi variabel acak kontinu. Siswa hanya perlu menghitung luas daerah di bawah kurva (atau panjang interval dikali tinggi fungsi) yang merupakan prosedur standar.. Bukti: f(x)=1/180, 0 <= x <= 180; peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar integral tentu atau luas daerah di bawah kurva fungsi konstan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi peluang kontinu adalah standar kelas 12 TL. Soal ini menggunakan distribusi seragam yang paling sederhana. |

Run 3 — solusi: P(15 < X < 60) = integral dari 15 sampai 60 dari (1/180) dx = (60 - 15) / 180 = 45 / 180 = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep integral fungsi densitas peluang untuk distribusi seragam (uniform distribution) pada interval yang diberikan. Ini adalah prosedur standar dalam kurikulum kelas 12.. Bukti: Fungsi densitas peluang X dinyatakan dengan f(x)=1/180, 0 <= x <= 180; Berapakah peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung peluang dari fungsi densitas kontinu dengan menggunakan integral sederhana.. Bukti: Fungsi densitas peluang X dinyatakan dengan f(x)=1/180, 0 <= x <= 180
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung luas daerah di bawah kurva fungsi konstan (persegi panjang) atau menggunakan integral dasar. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: f(x)=1/180, 0 <= x <= 180; peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi densitas peluang kontinu dan integral tentu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi variabel acak kontinu dan fungsi densitas adalah standar kurikulum kelas 12. Soal ini menggunakan distribusi seragam yang merupakan bentuk paling dasar dari fungsi densitas. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Fungsi Densitas Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam masa pandemi Covid-19, suatu toko hanya beroperasi selama 180 menit, yaitu mulai pukul 08.00 hingga pukul 11.00. Pembeli tidak diperbolehkan berada di dalam toko tersebut sebelum pukul 08.00. Pembeli juga harus meninggalkan toko paling lambat pukul 11.00. Misalkan X adalah variabel acak yang menyatakan lama pembeli berada di dalam toko (dalam menit). Fungsi densitas peluang X dinyatakan dengan $f(x)=\begin{cases}\frac{1}{180}, & 0 \le x \le 180\\ 0, & x<0 \text{ atau } x>180\end{cases}$

Berapakah peluang seorang pembeli berada di toko pada rentang waktu antara 15 dan 60 menit
Pilihan: A. $\frac{1}{2}$
B. $\frac{1}{3}$
C. $\frac{1}{4}$
D. $\frac{1}{12}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `2eb0a51b5ee19090bc76ed99`

Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.<br><br>Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?

| Opsi | Isi |
|---|---|
| A | 0,116 |
| B | 0,146 |
| C | 0,111 |
| D | 0,012 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Peluang jumlah 9 (p) = 4/36 = 1/9. Peluang gagal (q) = 8/9. Menggunakan distribusi binomial P(X=2) = C(6,2) * (1/9)^2 * (8/9)^4 = 15 * (1/81) * (4096/6561) ≈ 0,1156 ≈ 0,116.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4eec156927a3589c1c9d44519d87a056e6d35202f99de98959eee859535a3ff9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2908 |
| 2 | success | valid / verified | applying | procedural | Medium | 3026 |
| 3 | success | valid / verified | applying | procedural | Easy | 3040 |

Run 1 — solusi: Peluang jumlah 9 (p) = 4/36 = 1/9. Peluang gagal (q) = 8/9. Menggunakan distribusi binomial P(X=2) = C(6,2) * (1/9)^2 * (8/9)^4 = 15 * (1/81) * (4096/6561) ≈ 0,1156 ≈ 0,116.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi parameter distribusi binomial (n=6, k=2, p=1/9) dan menerapkan rumus peluang binomial secara langsung.. Bukti: Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.; Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma atau rumus distribusi binomial untuk menghitung peluang kejadian tertentu.. Bukti: Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?
- Intended difficulty `classify/Medium`: Soal memerlukan identifikasi ruang sampel untuk menentukan p, lalu menerapkan rumus binomial. Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.; Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk dan distribusi binomial. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan mampu menghitung peluang sukses dan menerapkan rumus binomial dengan benar. |

Run 2 — solusi: Peluang sukses (jumlah 9) p = 4/36 = 1/9. Peluang gagal q = 8/9. Menggunakan distribusi binomial P(X=2) = C(6,2) * (1/9)^2 * (8/9)^4 = 15 * (1/81) * (4096/6561) ≈ 0,1156, dibulatkan menjadi 0,116.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi parameter distribusi binomial (n=6, k=2, p=1/9) dan menerapkan rumus peluang binomial secara langsung.. Bukti: Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.; Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritma atau rumus distribusi binomial untuk menghitung peluang kejadian tertentu.. Bukti: Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?
- Intended difficulty `classify/Medium`: Soal ini adalah latihan rutin distribusi binomial. Memerlukan perhitungan peluang sukses (p), peluang gagal (q), dan koefisien binomial. Beban perhitungan moderat karena melibatkan pangkat empat dan pembagian pecahan.. Bukti: Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.; Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk dan rumus distribusi binomial. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin distribusi binomial. Memerlukan perhitungan peluang sukses (p), peluang gagal (q), dan koefisien binomial. Beban perhitungan moderat karena melibatkan pangkat empat dan pembagian pecahan. |

Run 3 — solusi: Peluang jumlah 9 (p) = 4/36 = 1/9. Peluang gagal (q) = 8/9. Menggunakan distribusi binomial P(X=2) = C(6,2) * (1/9)^2 * (8/9)^4 = 15 * (1/81) * (4096/6561) ≈ 0,1156, dibulatkan menjadi 0,116.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi parameter distribusi binomial (n=6, k=2, p=1/9) dan menerapkan rumus peluang binomial secara langsung.. Bukti: Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.; Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman tentang rumus distribusi binomial dan prosedur perhitungan peluang kejadian majemuk.. Bukti: Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus distribusi binomial dengan parameter yang jelas. Prosedur rutin dan familiar bagi siswa kelas 12.. Bukti: Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.; Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian sederhana dan rumus distribusi binomial. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi binomial adalah standar kurikulum kelas 12 TL. Soal ini tidak memerlukan modifikasi strategi atau pemahaman mendalam di luar prosedur standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3646`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi parameter distribusi binomial (n=6, k=2, p=1/9) dan menerapkan rumus peluang binomial secara langsung.
- Dimensi pengetahuan `procedural`: Soal menuntut penerapan algoritma atau rumus distribusi binomial untuk menghitung peluang kejadian tertentu.
- Intended difficulty `Medium`: Soal memerlukan identifikasi ruang sampel untuk menentukan p, lalu menerapkan rumus binomial. Ini melibatkan beberapa langkah rutin yang saling terkait.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk dan distribusi binomial. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan mampu menghitung peluang sukses dan menerapkan rumus binomial dengan benar. Beban perhitungan moderat karena melibatkan pangkat empat dan pembagian pecahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Distribusi Binomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Misalkan sepasang dadu seimbang dilemparkan sebanyak 6 kali.

Berapa peluang memperoleh jumlah mata dadu 9 sebanyak dua kali?
Pilihan: A. 0,116
B. 0,146
C. 0,111
D. 0,012
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `57b2d8d6cb57c48eed4725a0`

Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9. Misalkan terdapat 5 siswa di sekolah tersebut.<br><br>Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.

| Opsi | Isi |
|---|---|
| A | 0,00001 |
| B | 0,00046 |
| C | 0,99999 |
| D | 0,59049 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: X ~ B(5, 0.9). P(X ≥ 1) = 1 - P(X = 0). P(X = 0) = (0.1)^5 = 0.00001. Maka, P(X ≥ 1) = 1 - 0.00001 = 0.99999.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c085505b64f91004b63e5358f7a873058525d48dd294232d7bf2bae0c860ab62`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2096 |
| 2 | success | valid / verified | applying | procedural | Easy | 2885 |
| 3 | success | valid / verified | applying | procedural | Easy | 2827 |

Run 1 — solusi: X ~ B(5, 0.9). P(X ≥ 1) = 1 - P(X = 0). P(X = 0) = (5C0) * (0.9)^0 * (0.1)^5 = 1 * 1 * 0.00001 = 0.00001. Jadi, P(X ≥ 1) = 1 - 0.00001 = 0.99999.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa 'paling sedikit satu' lebih efisien dihitung menggunakan komplemen (1 - P(X=0)) daripada menjumlahkan P(X=1) sampai P(X=5). Ini adalah penerapan prosedur standar dalam distribusi binomial.. Bukti: Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.
- Dimensi pengetahuan `classify/conceptual`: Soal memerlukan pemahaman tentang konsep distribusi binomial dan penggunaan aturan komplemen dalam probabilitas.. Bukti: Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9. Misalkan terdapat 5 siswa; Tentukan peluang paling sedikit satu siswa
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12 yang mempelajari distribusi binomial. Prosedur komplemen adalah strategi standar yang diajarkan untuk kasus 'paling sedikit satu'.. Bukti: Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9. Misalkan terdapat 5 siswa di sekolah tersebut.; Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar distribusi binomial dan aturan komplemen peluang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menggunakan prosedur standar distribusi binomial yang merupakan materi inti kelas 12. Tidak ada kompleksitas tambahan atau strategi non-rutin yang diperlukan. |

Run 2 — solusi: X ~ B(5, 0.9). P(X ≥ 1) = 1 - P(X = 0) = 1 - (0.1)^5 = 1 - 0.00001 = 0.99999.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi distribusi binomial, menentukan parameter n=5 dan p=0.9, serta menerapkan aturan peluang komplemen untuk menghitung peluang kejadian 'paling sedikit satu'.. Bukti: Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9. Misalkan terdapat 5 siswa di sekolah tersebut.; Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman konsep peluang komplemen dan prosedur perhitungan distribusi binomial.. Bukti: Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.
- Intended difficulty `classify/Easy`: Soal ini merupakan aplikasi langsung dari rumus distribusi binomial dengan komplemen. Prosedurnya standar dan familiar bagi siswa kelas 12.. Bukti: Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9.; Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, distribusi binomial, dan peluang komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menggunakan rumus standar distribusi binomial yang diajarkan di kelas 12. Tidak ada langkah non-rutin atau kompleksitas tinggi. |

Run 3 — solusi: X ~ B(5, 0.9). P(X ≥ 1) = 1 - P(X = 0) = 1 - (0.1)^5 = 1 - 0.00001 = 0.99999.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi distribusi binomial, memahami konsep komplemen kejadian, dan menerapkan rumus peluang binomial untuk kasus X=0.. Bukti: Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman konsep distribusi binomial dan prosedur perhitungan peluang komplemen.. Bukti: Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9.; Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus distribusi binomial dengan konsep komplemen yang standar dalam kurikulum kelas 12.. Bukti: Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9.; Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar distribusi binomial dan peluang komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL sudah terbiasa dengan perhitungan peluang binomial sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3493`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur standar distribusi binomial dan menggunakan aturan komplemen untuk menyelesaikan masalah 'paling sedikit satu' secara efisien.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang distribusi binomial dan teknik komplemen dalam probabilitas.
- Intended difficulty `Easy`: Soal ini adalah aplikasi langsung dari rumus distribusi binomial dengan strategi komplemen yang sangat umum diajarkan di kelas 12. Tidak ada langkah non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar distribusi binomial dan aturan komplemen peluang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi binomial adalah standar kurikulum kelas 12. Soal ini menggunakan prosedur rutin tanpa kompleksitas tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Distribusi Binomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Peluang seorang siswa menyelesaikan studi pada sebuah sekolah adalah 0,9. Misalkan terdapat 5 siswa di sekolah tersebut.

Tentukan peluang paling sedikit satu siswa yang menyelesaikan studi.
Pilihan: A. 0,00001
B. 0,00046
C. 0,99999
D. 0,59049
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `fd90910a9859f703910d6647`

Dua siswa menerima informasi bahwa mereka masing-masing mendapat nilai 0,8 dan 0,4 pada tes matematika pilihan ganda. Jika skor masing-masing adalah 88 dan 64, tentukan rata-rata dan nilai standar dari skor tes.

| Opsi | Isi |
|---|---|
| A | rata-rata 76 dan nilai standar (simpangan baku) 12 |
| B | rata-rata 60 dan nilai standar (simpangan baku) 40 |
| C | rata-rata 40 dan nilai standar (simpangan baku) 24 |
| D | rata-rata 40 dan nilai standar (simpangan baku) 60 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 88 = μ + 0.8σ dan 64 = μ + 0.4σ. Selisih: 24 = 0.4σ, maka σ = 60. Substitusi: 64 = μ + 0.4(60) = μ + 24, maka μ = 40.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a858a08a0503a8854f9ccce614cd04750187fc8e45525122eceee645384ade39`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3258 |
| 2 | success | valid / verified | applying | procedural | Medium | 3252 |
| 3 | success | valid / verified | applying | procedural | Medium | 2981 |

Run 1 — solusi: 88 = μ + 0.8σ dan 64 = μ + 0.4σ. Selisih: 24 = 0.4σ, maka σ = 60. Substitusi: 64 = μ + 0.4(60) = μ + 24, maka μ = 40.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus skor-z (X = μ + Zσ) untuk membentuk sistem persamaan linear dua variabel dan menyelesaikannya.. Bukti: 88 = μ + 0.8σ dan 64 = μ + 0.4σ; selisih: 0,4σ = 24 sehingga σ = 60 dan μ = 40
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman prosedural tentang penggunaan rumus skor-z dalam distribusi normal untuk mencari parameter populasi.. Bukti: 88 = μ + 0.8σ dan 64 = μ + 0.4σ
- Intended difficulty `classify/Medium`: Soal memerlukan pembentukan dan penyelesaian sistem persamaan linear dua variabel dari definisi skor-z. Ini adalah prosedur rutin namun melibatkan beberapa langkah.. Bukti: 88 = μ + 0.8σ dan 64 = μ + 0.4σ; selisih: 0,4σ = 24 sehingga σ = 60 dan μ = 40

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi skor-z (Z = (X - μ) / σ) dan penyelesaian sistem persamaan linear dua variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 12 TL diharapkan mampu memanipulasi rumus statistik dasar untuk mencari parameter yang tidak diketahui. |

Run 2 — solusi: Gunakan rumus skor baku: X = μ + Zσ. Persamaan 1: 88 = μ + 0,8σ. Persamaan 2: 64 = μ + 0,4σ. Kurangi kedua persamaan: 24 = 0,4σ, maka σ = 60. Substitusi σ ke persamaan 2: 64 = μ + 0,4(60) = μ + 24, maka μ = 40.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus skor baku (Z-score) untuk membentuk sistem persamaan linear dua variabel dan menyelesaikannya.. Bukti: 88 = μ + 0,8σ; 64 = μ + 0,4σ; selisih: 0,4σ = 24 sehingga σ = 60 dan μ = 40
- Dimensi pengetahuan `classify/procedural`: Menggunakan prosedur standar untuk mengubah skor mentah menjadi skor baku dalam distribusi normal.. Bukti: 88 = μ + 0,8σ; 64 = μ + 0,4σ
- Intended difficulty `classify/Medium`: Soal memerlukan pembentukan sistem persamaan linear dari definisi skor baku. Ini adalah langkah rutin namun memerlukan pemahaman konsep yang tepat.. Bukti: 88 = μ + 0,8σ; 64 = μ + 0,4σ

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi skor baku (Z-score) dan penyelesaian sistem persamaan linear dua variabel. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 12 karena menggabungkan konsep statistika (distribusi normal) dengan aljabar dasar. |

Run 3 — solusi: Rumus Z-score: X = μ + Zσ. Persamaan: 88 = μ + 0,8σ dan 64 = μ + 0,4σ. Selisih: 24 = 0,4σ, maka σ = 60. Substitusi: 64 = μ + 0,4(60) = μ + 24, maka μ = 40.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi Z-score ke dalam sistem persamaan linear dua variabel untuk menemukan parameter distribusi (rata-rata dan simpangan baku). Ini adalah penerapan konsep pada situasi rutin.. Bukti: Dua siswa menerima informasi bahwa mereka masing-masing mendapat nilai 0,8 dan 0,4 pada tes matematika pilihan ganda. Jika skor masing-masing adalah 88 dan 64
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma aljabar untuk menyelesaikan sistem persamaan linear yang diturunkan dari rumus Z-score.. Bukti: 88 = μ + 0,8σ dan 64 = μ + 0,4σ
- Intended difficulty `classify/Medium`: Soal memerlukan pembentukan dua persamaan linear dari informasi yang diberikan dan penyelesaian sistem tersebut. Tingkat kesulitan menengah karena melibatkan manipulasi aljabar dua variabel.. Bukti: Dua siswa menerima informasi bahwa mereka masing-masing mendapat nilai 0,8 dan 0,4 pada tes matematika pilihan ganda. Jika skor masing-masing adalah 88 dan 64

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi Z-score dan penyelesaian sistem persamaan linear dua variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi normal dan Z-score adalah standar kelas 12 TL. Soal ini menguji pemahaman konsep tersebut melalui prosedur aljabar yang rutin. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Distribusi Normal
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua siswa menerima informasi bahwa mereka masing-masing mendapat nilai 0,8 dan 0,4 pada tes matematika pilihan ganda. Jika skor masing-masing adalah 88 dan 64, tentukan rata-rata dan nilai standar dari skor tes.
Pilihan: A. rata-rata 76 dan nilai standar (simpangan baku) 12
B. rata-rata 60 dan nilai standar (simpangan baku) 40
C. rata-rata 40 dan nilai standar (simpangan baku) 24
D. rata-rata 40 dan nilai standar (simpangan baku) 60
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `24f43ff9447508b7453ba292`

Sebuah perusahaan elektronik memproduksi lampu dengan masa pakai berdistribusi normal dengan rata-rata 800 jam dan simpangan baku 40 jam.<br><br>Tentukan peluang lampu padam antara 778 jam dan 834 jam.

| Opsi | Isi |
|---|---|
| A | 0,0935 |
| B | 0,3023 |
| C | 0,5111 |
| D | 0,8023 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Z1 = (778 - 800) / 40 = -0,55; Z2 = (834 - 800) / 40 = 0,85. Peluang = P(-0,55 < Z < 0,85) = P(-0,55 < Z < 0) + P(0 < Z < 0,85) = 0,2088 + 0,3023 = 0,5111.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c125fba49e6294efd9cf499d35c985b52ef266e441e7336271cd3e99ceb40d6a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3050 |
| 2 | success | valid / verified | applying | procedural | Easy | 2152 |
| 3 | success | valid / verified | applying | procedural | Medium | 3088 |

Run 1 — solusi: Z1 = (778-800)/40 = -0,55; Z2 = (834-800)/40 = 0,85. Peluang = P(-0,55 < Z < 0,85) = P(0 < Z < 0,55) + P(0 < Z < 0,85) = 0,2088 + 0,3023 = 0,5111.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar distribusi normal (standardisasi Z-score) dan menggunakan tabel distribusi normal untuk menentukan peluang pada interval tertentu.. Bukti: Tentukan peluang lampu padam antara 778 jam dan 834 jam.; rata-rata 800 jam dan simpangan baku 40 jam.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam menghitung nilai Z dan mengoperasikan tabel distribusi normal untuk mendapatkan probabilitas.. Bukti: rata-rata 800 jam dan simpangan baku 40 jam.; Tentukan peluang lampu padam antara 778 jam dan 834 jam.
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (standardisasi, pencarian tabel, dan penjumlahan luas area) yang merupakan standar kompetensi kelas 12.. Bukti: rata-rata 800 jam dan simpangan baku 40 jam.; Tentukan peluang lampu padam antara 778 jam dan 834 jam.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman distribusi normal, rumus Z-score, dan penggunaan tabel Z. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah aplikasi rutin dari distribusi normal yang sesuai dengan kurikulum matematika tingkat lanjut kelas 12. |

Run 2 — solusi: Z1 = (778-800)/40 = -0,55; Z2 = (834-800)/40 = 0,85. P(-0,55 < Z < 0,85) = P(-0,55 < Z < 0) + P(0 < Z < 0,85) = 0,2088 + 0,3023 = 0,5111.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standardisasi skor Z dan menggunakan tabel distribusi normal untuk menghitung peluang pada interval tertentu. Ini adalah penerapan rutin dari konsep distribusi normal.. Bukti: rata-rata 800 jam dan simpangan baku 40 jam; peluang lampu padam antara 778 jam dan 834 jam
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang algoritma standardisasi (Z-score) dan penggunaan tabel distribusi normal standar untuk menyelesaikan masalah peluang.. Bukti: berdistribusi normal; rata-rata 800 jam dan simpangan baku 40 jam
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam kurikulum kelas 12. Siswa hanya perlu melakukan dua kali konversi Z-score dan menjumlahkan luas area di bawah kurva normal.. Bukti: rata-rata 800 jam dan simpangan baku 40 jam; peluang lampu padam antara 778 jam dan 834 jam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep distribusi normal, standardisasi Z, dan pembacaan tabel Z. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah masalah rutin distribusi normal yang sesuai dengan tingkat kesulitan dasar untuk materi statistika inferensial kelas 12. |

Run 3 — solusi: Z1 = (778 - 800) / 40 = -0,55; Z2 = (834 - 800) / 40 = 0,85. Peluang = P(-0,55 < Z < 0,85) = P(-0,55 < Z < 0) + P(0 < Z < 0,85) = P(0 < Z < 0,55) + P(0 < Z < 0,85) = 0,2088 + 0,3023 = 0,5111.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar distribusi normal (standardisasi Z, pembacaan tabel, dan operasi luas daerah) untuk menyelesaikan masalah rutin.. Bukti: Tentukan peluang lampu padam antara 778 jam dan 834 jam
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma standardisasi dan teknik pembacaan tabel distribusi normal.. Bukti: rata-rata 800 jam dan simpangan baku 40 jam; z1 = −0,55, z2 = 0,85
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin yang saling terkait (standardisasi, mencari nilai tabel, dan menjumlahkan luas) tanpa memerlukan strategi nonrutin.. Bukti: rata-rata 800 jam dan simpangan baku 40 jam; Tentukan peluang lampu padam antara 778 jam dan 834 jam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman distribusi normal dan penggunaan tabel Z. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai kurikulum kelas 12, prosedur ini adalah standar untuk topik distribusi normal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3830`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur standar distribusi normal (standardisasi Z-score) dan menggunakan tabel distribusi normal untuk menentukan peluang pada interval tertentu. Ini adalah penerapan rutin dari konsep yang dipelajari.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dalam menghitung nilai Z dan mengoperasikan tabel distribusi normal untuk mendapatkan probabilitas.
- Intended difficulty `Medium`: Soal memerlukan beberapa langkah rutin (standardisasi, pencarian tabel, dan penjumlahan luas area) yang merupakan standar kompetensi kelas 12. Tidak ada strategi nonrutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman distribusi normal, rumus Z-score, dan penggunaan tabel Z. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah aplikasi rutin dari distribusi normal yang sesuai dengan kurikulum matematika tingkat lanjut kelas 12. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Distribusi Normal
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah perusahaan elektronik memproduksi lampu dengan masa pakai berdistribusi normal dengan rata-rata 800 jam dan simpangan baku 40 jam.

Tentukan peluang lampu padam antara 778 jam dan 834 jam.
Pilihan: A. 0,0935
B. 0,3023
C. 0,5111
D. 0,8023
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `6353e1b1ac73792bd65d8bcc`

Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.<br><br>Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?

| Opsi | Isi |
|---|---|
| A | Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$ |
| B | Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$ |
| C | Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$ |
| D | Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: P(dobel) = 6/36 = 1/6. P(jumlah 6) = {(1,5), (2,4), (3,3), (4,2), (5,1)} = 5/36. Karena lemparan pertama dan kedua saling bebas, P(dobel ∩ jumlah 6) = P(dobel) × P(jumlah 6) = 1/6 × 5/36 = 5/216.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['menghitung', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `179055e4b4c1e2da03251e6b666b4ef7a73f544b6655b6b89975d9ebbedd5645`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2204 |
| 2 | success | valid / verified | applying | procedural | Easy | 2211 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2219 |

Run 1 — solusi: Kejadian A (muncul angka dobel pada sepasang dadu) dan B (jumlah mata dadu enam pada sepasang dadu) adalah kejadian saling bebas. P(A) = 6/36 = 1/6. P(B) = 5/36 (pasangan: (1,5), (2,4), (3,3), (4,2), (5,1)). Peluang gabungan = P(A) × P(B) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas dan menerapkan aturan perkalian untuk peluang kejadian majemuk. Ini adalah penerapan konsep peluang dasar pada situasi rutin.. Bukti: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam.; Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang prinsip dasar peluang (kejadian saling bebas) dan prosedur perhitungan peluang kejadian majemuk.. Bukti: aturan perkalian dapat digunakan untuk menentukan peluang ini
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Siswa hanya perlu menghitung peluang masing-masing kejadian sederhana dan mengalikannya. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: melemparkan sepasang dadu dan mendapatkan angka dobel; pada lemparan kedua mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian sederhana pada ruang sampel dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian saling bebas adalah standar kurikulum kelas 12. Prosedur perhitungan peluang dadu sangat familiar. |

Run 2 — solusi: P(A) = P(dobel) = 6/36 = 1/6. P(B) = P(jumlah 6) = {(1,5), (2,4), (3,3), (4,2), (5,1)} = 5/36. Karena lemparan pertama dan kedua saling bebas, P(A dan B) = P(A) × P(B) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa dua kejadian tersebut saling bebas dan menerapkan aturan perkalian untuk peluang kejadian majemuk, yang merupakan penerapan konsep dasar peluang.. Bukti: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam.; Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian untuk kejadian saling bebas dalam teori peluang.. Bukti: aturan perkalian dapat digunakan untuk menentukan peluang ini
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Siswa hanya perlu menghitung peluang masing-masing kejadian sederhana (dobel dan jumlah 6) lalu mengalikannya. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam; aturan perkalian dapat digunakan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian sederhana pada ruang sampel dadu dan aturan perkalian untuk kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian majemuk adalah standar kurikulum kelas 12. Soal ini adalah aplikasi langsung dari definisi kejadian saling bebas. |

Run 3 — solusi: Kejadian 1 (mendapat angka dobel): {(1,1), (2,2), (3,3), (4,4), (5,6), (6,6)} ada 6 dari 36, P(E1) = 6/36 = 1/6. Kejadian 2 (jumlah enam): {(1,5), (2,4), (3,3), (4,2), (5,1)} ada 5 dari 36, P(E2) = 5/36. Karena lemparan pertama dan kedua saling bebas, P(E1 ∩ E2) = P(E1) × P(E2) = 1/6 × 5/36 = 5/216.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas dan menerapkan aturan perkalian peluang untuk dua kejadian tersebut.. Bukti: Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini?; Berapa peluangnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kejadian saling bebas dan prosedur penerapan aturan perkalian peluang.. Bukti: aturan perkalian dapat digunakan; mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam
- Intended difficulty `classify/Easy`: Soal ini memerlukan pemahaman dasar tentang ruang sampel dadu dan aturan perkalian untuk kejadian saling bebas. Prosedurnya standar dan familiar bagi siswa kelas 12.. Bukti: melemparkan sepasang dadu; mendapatkan angka dobel; mendapatkan jumlah enam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman ruang sampel dua dadu dan konsep kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian saling bebas adalah topik standar kelas 12. Soal ini tidak memerlukan strategi non-rutin atau integrasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3872`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi bahwa dua lemparan dadu adalah kejadian saling bebas dan menerapkan aturan perkalian untuk peluang kejadian majemuk. Ini adalah penerapan konsep peluang dasar pada situasi rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut pemahaman tentang prinsip dasar peluang (kejadian saling bebas) dan prosedur perhitungan peluang kejadian majemuk.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 12. Siswa hanya perlu menghitung peluang masing-masing kejadian sederhana dan mengalikannya. Tidak ada kendala kompleks atau strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Peluang kejadian sederhana pada ruang sampel dadu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kejadian saling bebas adalah standar kurikulum kelas 12. Prosedur perhitungan peluang dadu sangat familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Aturan Perkalian
Tipe soal: multiple_choice
Stimulus: -
Soal: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.

Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
Pilihan: A. Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$
B. Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$
C. Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$
D. Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `5a713d72bd575400bbc8e916`

Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.<br><br>Berapa persentase IQ yang diterangkan oleh lingkar kepala?

| Opsi | Isi |
|---|---|
| A | 13,8% |
| B | 1,9% |
| C | 0,19% |
| D | 98,1% |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Persentase varians yang dijelaskan oleh variabel independen ditentukan oleh koefisien determinasi (r²). Diketahui r = 0,138, maka r² = (0,138)² = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044% atau dibulatkan menjadi 1,9%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `867ffecb44aa59bdbc3fd0c99fceb1ff0cd3bcdbf47c8acba02d22e3e58b2109`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3078 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3105 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2874 |

Run 1 — solusi: Persentase varians yang dijelaskan oleh variabel independen ditentukan oleh koefisien determinasi (r²). Diketahui r = 0,138, maka r² = (0,138)² = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044% atau dibulatkan menjadi 1,9%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep koefisien determinasi (r²) untuk menentukan proporsi varians yang dijelaskan oleh variabel independen, yang merupakan prosedur standar dalam analisis korelasi.. Bukti: Berapa persentase IQ yang diterangkan oleh lingkar kepala?; Nilai koefisien korelasinya adalah 0,138.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang hubungan antara koefisien korelasi (r) dan koefisien determinasi (r²) dalam analisis statistik.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa yang mempelajari statistika. Prosedurnya langsung (mengkuadratkan nilai r) tanpa memerlukan langkah kompleks atau strategi non-rutin.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien korelasi Pearson dan koefisien determinasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korelasi dan determinasi merupakan bagian standar kurikulum statistika kelas 12. Prosedur kuadrat r adalah standar. |

Run 2 — solusi: Persentase varians yang dijelaskan oleh variabel independen ditentukan oleh koefisien determinasi (r²). Diketahui r = 0,138, maka r² = (0,138)² = 0,019044. Dalam bentuk persentase, 0,019044 * 100% = 1,9044% atau dibulatkan menjadi 1,9%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep koefisien determinasi (r²) untuk menentukan persentase varians yang dijelaskan oleh variabel independen dari nilai koefisien korelasi (r) yang diberikan.. Bukti: Berapa persentase IQ yang diterangkan oleh lingkar kepala?; Nilai koefisien korelasinya adalah 0,138.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang hubungan antara koefisien korelasi (r) dan koefisien determinasi (r²) dalam analisis korelasi.. Bukti: Berapa persentase IQ yang diterangkan oleh lingkar kepala?; Nilai koefisien korelasinya adalah 0,138.
- Intended difficulty `classify/Easy`: Prosedur ini sangat langsung (mengkuadratkan nilai r) dan merupakan aplikasi rutin dari definisi koefisien determinasi dalam statistik dasar.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

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
| gradeRelativeRationale | Meskipun analisis korelasi ada di kelas 12, prosedur mengkuadratkan r untuk mendapatkan r² adalah prosedur standar yang sangat familiar. |

Run 3 — solusi: Koefisien determinasi (r²) menunjukkan persentase varians variabel dependen yang dijelaskan oleh variabel independen. r² = (0,138)² = 0,019044 = 1,9%.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep koefisien determinasi (r²) sebagai ukuran proporsi varians yang dijelaskan oleh model regresi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara koefisien korelasi (r) dan koefisien determinasi (r²).. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman langsung tentang definisi koefisien determinasi. Prosedurnya familiar bagi siswa yang mempelajari statistik inferensial/korelasi.. Bukti: Nilai koefisien korelasinya adalah 0,138.; Berapa persentase IQ yang diterangkan oleh lingkar kepala?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi koefisien korelasi dan koefisien determinasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi korelasi dan determinasi adalah bagian standar kurikulum kelas 12. Soal ini hanya memerlukan satu langkah komputasi dasar. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Analisis Korelasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.

Berapa persentase IQ yang diterangkan oleh lingkar kepala?
Pilihan: A. 13,8%
B. 1,9%
C. 0,19%
D. 98,1%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `d4a29da533d9881db57e7c74`

Tim futsal SMA Abhipraya dijadwalkan mengikuti 3 pertandingan awal dalam turnamen dengan sistem poin. Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6 berdasarkan data latihan dan uji coba. Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.

| Opsi | Isi |
|---|---|
| A | 0,36 |
| B | 0,432 |
| C | 0,6 |
| D | 0,216 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `0,432`.
Solusi minimum hasil AI: Menggunakan distribusi binomial dengan n=3, k=2, p=0,6, dan q=0,4: P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika Tingkat Lanjut SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a77cd857411ce0423aea4b7181c833c27ac234307d6dfd4701d43a81c6088679`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2104 |
| 2 | success | valid / verified | applying | procedural | Easy | 2070 |
| 3 | success | valid / verified | applying | procedural | Easy | 2114 |

Run 1 — solusi: Menggunakan distribusi binomial dengan n=3, k=2, p=0,6, dan q=0,4: P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai eksperimen binomial dan menerapkan rumus peluang binomial secara tepat untuk menghitung probabilitas kejadian spesifik.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang prinsip distribusi binomial (konsep) dan penggunaan rumus binomial (prosedural) untuk menyelesaikan masalah peluang.. Bukti: peluang memenangkan tepat 2 dari 3 pertandingan
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus distribusi binomial yang sudah dipelajari di kelas 12. Tidak ada langkah non-rutin atau kompleksitas tinggi.. Bukti: 3 pertandingan awal; peluang menang... 0,6; tepat 2 dari 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang, aturan perkalian, dan rumus distribusi binomial. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi binomial adalah standar kurikulum kelas 12. Soal ini menguji pemahaman dasar tanpa modifikasi yang rumit. |

Run 2 — solusi: Menggunakan distribusi binomial dengan n=3, k=2, dan p=0,6. P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai eksperimen binomial, memilih rumus yang tepat, dan menerapkan prosedur perhitungan rutin untuk distribusi binomial.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip distribusi peluang binomial sebagai teknik atau algoritma untuk menyelesaikan masalah peluang kejadian majemuk.. Bukti: peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus distribusi binomial yang sudah familiar di kelas 12. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; memenangkan tepat 2 dari 3 pertandingan pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian saling bebas dan rumus kombinasi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi distribusi binomial adalah standar kurikulum kelas 12 TL. Soal ini menggunakan angka sederhana dan prosedur standar tanpa modifikasi. |

Run 3 — solusi: Menggunakan rumus distribusi binomial P(X=k) = C(n,k) * p^k * (1-p)^(n-k) dengan n=3, k=2, p=0,6. P(X=2) = C(3,2) * (0,6)^2 * (0,4)^1 = 3 * 0,36 * 0,4 = 0,432.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai eksperimen binomial, memilih rumus yang tepat, dan menerapkan parameter yang diberikan ke dalam rumus tersebut. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prinsip distribusi binomial (konsep) dan penggunaan rumus binomial (prosedural) untuk menghitung peluang kejadian tertentu.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; memenangkan tepat 2 dari 3 pertandingan
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus distribusi binomial yang merupakan materi standar kelas 12. Tidak ada jebakan atau kompleksitas tambahan.. Bukti: Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6; memenangkan tepat 2 dari 3 pertandingan pertama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang dan rumus kombinasi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Distribusi binomial adalah materi inti kelas 12. Soal ini menggunakan angka sederhana dan skenario langsung yang umum dijumpai di buku teks. |

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
Kelas: 12
Topik: Matematika Tingkat Lanjut SMA Kelas 12
Subtopik: Penerapan Permutasi dan Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Tim futsal SMA Abhipraya dijadwalkan mengikuti 3 pertandingan awal dalam turnamen dengan sistem poin. Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6 berdasarkan data latihan dan uji coba. Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.
Pilihan: A. 0,36
B. 0,432
C. 0,6
D. 0,216
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
