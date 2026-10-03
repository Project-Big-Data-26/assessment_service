# Validasi ulang soal kelas 9 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v7-blind-smp9-key-verified`. Rubrik: `math-rubric-3x4x3-v5-smp9-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 9 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 9, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 27, "knowing": 11, "reasoning": 4}, "knowledgeDimension": {"conceptual": 20, "procedural": 21, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 28, "Medium": 14, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 27, "knowing": 11, "reasoning": 3}, "knowledgeDimension": {"conceptual": 19, "procedural": 21, "factual": 1, "metacognitive": 0}, "intendedDifficulty": {"Easy": 28, "Medium": 13, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 41, "revision_required": 1}`.
Run awal sukses: 126/126; adjudikasi: 18; token sukses tercatat: 360,424.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 28 | 28 | [Easy.json](difficulty/Easy.json) |
| Medium | 14 | 13 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 9, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 9, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 9. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMP.

## 1. Soal `8af0a2ca82017a432c92902d`

Diketahui keliling sebuah segitiga sama kaki adalah 48 cm. Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.

| Opsi | Isi |
|---|---|
| A | $x + y = 48$ |
| B | $2x + y = 48$ |
| C | $x + 2y = 48$ |
| D | $2x + 2y = 48$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi yang berbeda (misal y). Keliling adalah jumlah ketiga sisi tersebut: x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `58c3d64d72cfaba4de9b151726f4b19ddac4fe0d503c79c25bf067f35cc41b65`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2035 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2037 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2028 |

Run 1 — solusi: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi yang berbeda (misal y). Keliling adalah jumlah ketiga sisi tersebut: x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan deskripsi geometri (segitiga sama kaki) ke dalam bentuk aljabar (persamaan linear dua variabel). Ini melibatkan pemahaman konsep hubungan antar sisi dan representasi simbolik, yang termasuk dalam kategori applying.. Bukti: Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang struktur atau prinsip segitiga sama kaki dan bagaimana merepresentasikannya ke dalam model matematika (persamaan).. Bukti: segitiga sama kaki; model matematika
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Siswa hanya perlu mengidentifikasi properti segitiga sama kaki (2 sisi sama, 1 berbeda) dan menuliskan persamaannya. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; model matematika yang menghubungkan antara keliling dan panjang sisi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang keliling segitiga dan konsep variabel dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi SPLDV dan pemodelan matematika adalah standar kelas 9. Soal ini menguji pemahaman dasar tanpa kompleksitas perhitungan atau logika yang berat. |

Run 2 — solusi: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi alas (misal y). Keliling adalah jumlah ketiga sisi tersebut, yaitu x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi geometri (segitiga sama kaki) ke dalam bentuk aljabar (model matematika). Ini memerlukan pemahaman konsep hubungan antar variabel dalam geometri, yang termasuk dalam kategori applying.. Bukti: Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang struktur konsep segitiga sama kaki dan bagaimana merepresentasikannya dalam bentuk persamaan linear dua variabel.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; model matematika yang menghubungkan antara keliling dan panjang sisi
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Siswa hanya perlu memahami definisi segitiga sama kaki dan menerjemahkannya ke dalam persamaan linear sederhana. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; model matematika yang menghubungkan antara keliling dan panjang sisi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama kaki dan konsep keliling bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi SPLDV dan pemodelan matematika adalah standar kelas 9. Soal ini menguji pemahaman dasar tentang variabel dalam konteks geometri yang sangat familiar. |

Run 3 — solusi: Segitiga sama kaki memiliki dua sisi yang sama panjang (misal x) dan satu sisi alas (misal y). Keliling adalah jumlah ketiga sisi: x + x + y = 48, yang disederhanakan menjadi 2x + y = 48.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi geometri (segitiga sama kaki) ke dalam bentuk aljabar (persamaan linear dua variabel). Ini memerlukan pemahaman konsep hubungan antar variabel dalam geometri, bukan sekadar menghitung nilai.. Bukti: Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur segitiga sama kaki dan bagaimana hubungan tersebut direpresentasikan dalam model matematika (persamaan linear).. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; model matematika yang menghubungkan antara keliling dan panjang sisi
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pemahaman dasar tentang definisi segitiga sama kaki dan penerjemahan langsung ke bentuk persamaan linear tanpa langkah-langkah kompleks atau strategi nonrutin.. Bukti: keliling sebuah segitiga sama kaki adalah 48 cm; model matematika yang menghubungkan antara keliling dan panjang sisi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi segitiga sama kaki dan konsep keliling bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan pemodelan matematika sederhana dan sifat-sifat bangun datar dasar. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui keliling sebuah segitiga sama kaki adalah 48 cm. Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.
Pilihan: A. $x + y = 48$
B. $2x + y = 48$
C. $x + 2y = 48$
D. $2x + 2y = 48$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `e7003333bef697d763016f2e`

Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel.<br><br>Diketahui harga tiket film di suatu bioskop Rp35.000,00. y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual.

| Opsi | Isi |
|---|---|
| A | $y = \frac{x}{35.000}$ |
| B | $y = 35.000x$ |
| C | $x = 35.000y$ |
| D | $y = 35.000 + x$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pendapatan (y) diperoleh dari harga per tiket dikalikan dengan jumlah tiket terjual (x). Maka, y = 35.000 * x.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dc559007eea0dfc9ecdf3f4a3f816830590bdf812cc7cd4328270d92db3a5bae`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2035 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2047 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2042 |

Run 1 — solusi: Pendapatan (y) diperoleh dari harga per tiket dikalikan dengan jumlah tiket terjual (x). Maka, y = 35.000 * x.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi kontekstual ke dalam model matematika linear sederhana. Proses ini melibatkan pemahaman hubungan proporsional dasar antara dua variabel, yang termasuk dalam domain applying.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; harga tiket film di suatu bioskop Rp35.000,00
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang bagaimana variabel-variabel dalam situasi dunia nyata saling berhubungan secara fungsional (konseptual) dan bagaimana menyusunnya menjadi persamaan linear (prosedural).. Bukti: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 9. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan untuk memodelkan hubungan perkalian sederhana ini.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; harga tiket film di suatu bioskop Rp35.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi perkalian dalam konteks aritmatika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemodelan matematika sederhana seperti ini adalah materi dasar yang sudah diperkenalkan sejak awal bab SPLDV di kelas 8/9. |

Run 2 — solusi: Pendapatan (y) diperoleh dari hasil perkalian harga satuan tiket (Rp35.000,00) dengan jumlah tiket yang terjual (x). Maka, persamaannya adalah y = 35.000x.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan hubungan kuantitatif sederhana ke dalam bentuk persamaan linear. Proses ini melibatkan pemahaman konsep dasar variabel dan operasi perkalian, yang merupakan penerapan langsung dari definisi fungsi linear.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; harga tiket film di suatu bioskop Rp35.000,00
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara variabel (pendapatan dan jumlah tiket) dan prinsip dasar pembentukan persamaan linear, yang merupakan pengetahuan konseptual.. Bukti: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi hubungan perkalian antara harga satuan dan kuantitas untuk membentuk persamaan. Tidak ada langkah kompleks atau strategi nonrutin yang diperlukan.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; harga tiket film di suatu bioskop Rp35.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi perkalian dalam konteks aritmatika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 9, menguji pemahaman awal tentang pemodelan matematika sederhana yang seharusnya sudah dikuasai. |

Run 3 — solusi: Pendapatan (y) diperoleh dari harga per tiket dikalikan dengan jumlah tiket yang terjual (x). Maka, y = 35.000 * x atau y = 35.000x.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan situasi kontekstual sederhana ke dalam model matematika linear dua variabel. Proses ini melibatkan pengenalan hubungan proporsional dasar, yang termasuk dalam domain applying.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; harga tiket film di suatu bioskop Rp35.000,00
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara variabel (pendapatan dan jumlah tiket) dan prinsip perkalian dalam konteks harga satuan, yang merupakan pemahaman konseptual.. Bukti: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu mengidentifikasi hubungan perkalian sederhana antara harga satuan dan kuantitas untuk membentuk persamaan linear.. Bukti: y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual; harga tiket film di suatu bioskop Rp35.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi perkalian dalam konteks aritmatika. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 9, di mana pemodelan SPLDV biasanya sudah lebih kompleks. Ini adalah soal pengenalan konsep dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel.

Diketahui harga tiket film di suatu bioskop Rp35.000,00. y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual.
Pilihan: A. $y = \frac{x}{35.000}$
B. $y = 35.000x$
C. $x = 35.000y$
D. $y = 35.000 + x$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `0b4b98faa7f553833f0db971`

Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.<br><br>Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?

| Opsi | Isi |
|---|---|
| A | 27 kuas lukis jenis I dan 13 kuas lukis jenis II |
| B | 20 kuas lukis jenis I dan 20 kuas lukis jenis II |
| C | 13 kuas lukis jenis I dan 27 kuas lukis jenis II |
| D | 15 kuas lukis jenis I dan 25 kuas lukis jenis II |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Model matematika: x+y=40 dan 35000x+24000y=1103000. Substitusi x=40-y ke persamaan kedua: 35000(40-y)+24000y=1103000, sehingga 1400000-11000y=1103000. Maka 11000y=297000, y=27. Jadi x=40-27=13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `57af1d1776ee7fa33b790d6bdf66782998e871610afa07859141f38f5883e3b3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3009 |
| 2 | success | valid / verified | applying | procedural | Medium | 3664 |
| 3 | success | valid / verified | applying | procedural | Medium | 3236 |

Run 1 — solusi: Model matematika: x+y=40 dan 35000x+24000y=1103000. Substitusi x=40-y ke persamaan kedua: 35000(40-y)+24000y=1103000, sehingga 1400000-11000y=1103000. Maka 11000y=297000, y=27. Jadi x=40-27=13.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur rutin sistem persamaan linear dua variabel untuk menyelesaikan masalah kontekstual yang diberikan.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menggunakan algoritma penyelesaian sistem persamaan linear dua variabel.. Bukti: berapa banyak masing-masing jenis kuas lukis yang terjual
- Intended difficulty `classify/Medium`: Soal memerlukan pemodelan matematika dan penyelesaian sistem persamaan dua variabel. Ini adalah prosedur standar kelas 9 dengan beban perhitungan moderat.. Bukti: 40 kuas lukis; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00; uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar dan metode eliminasi atau substitusi pada SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari materi SPLDV yang diajarkan di kelas 9, melibatkan dua variabel dan dua kendala (jumlah barang dan total harga). |

Run 2 — solusi: Misalkan x = banyak kuas I, y = banyak kuas II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40-y) + 24.000y = 1.103.000 => 1.400.000 - 11.000y = 1.103.000 => 11.000y = 297.000 => y = 27. Maka x = 13.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan masalah ke dalam sistem persamaan linear dua variabel dan menerapkan prosedur penyelesaian (substitusi atau eliminasi) untuk menemukan nilai variabel.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritma penyelesaian sistem persamaan linear dua variabel.. Bukti: 35.000x + 24.000y = 1.103.000
- Intended difficulty `classify/Medium`: Soal memerlukan pembentukan model matematika dari narasi dan penyelesaian sistem persamaan dua variabel. Ini adalah tugas rutin bagi siswa kelas 9.. Bukti: 40 kuas lukis; Rp35.000,00; Rp24.000,00; Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, persamaan linear, dan metode eliminasi/substitusi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi standar kelas 9. Soal ini merupakan aplikasi langsung dari pemodelan dan penyelesaian sistem. |

Run 3 — solusi: Misal x=kuas I, y=kuas II. Sistem persamaan: x+y=40 dan 35000x+24000y=1103000. Substitusi x=40-y ke persamaan kedua: 35000(40-y)+24000y=1103000 -> 1400000-11000y=1103000 -> 11000y=297000 -> y=27. Maka x=40-27=13. Jadi, 13 kuas jenis I dan 27 kuas jenis II.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah cerita ke dalam model matematika SPLDV dan menerapkan prosedur eliminasi atau substitusi untuk menyelesaikannya.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma penyelesaian sistem persamaan linear dua variabel.. Bukti: berapa banyak masing-masing jenis kuas lukis yang terjual?
- Intended difficulty `classify/Medium`: Soal ini melibatkan pemodelan matematika dari situasi nyata dan penyelesaian sistem persamaan, yang merupakan standar kompetensi kelas 9. Tingkat kesulitan sedang karena memerlukan langkah-langkah terstruktur (pemodelan, substitusi/eliminasi, perhitungan).. Bukti: 40 kuas lukis; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar, operasi aritmatika, dan konsep sistem persamaan linear dua variabel. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini melibatkan pemodelan matematika dari situasi nyata dan penyelesaian sistem persamaan, yang merupakan standar kompetensi kelas 9. Tingkat kesulitan sedang karena memerlukan langkah-langkah terstruktur (pemodelan, substitusi/eliminasi, perhitungan). |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.

Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
Pilihan: A. 27 kuas lukis jenis I dan 13 kuas lukis jenis II
B. 20 kuas lukis jenis I dan 20 kuas lukis jenis II
C. 13 kuas lukis jenis I dan 27 kuas lukis jenis II
D. 15 kuas lukis jenis I dan 25 kuas lukis jenis II
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `a4219a3c217e0979ca28b57e`

Wayan pergi ke toko kue tradisional untuk membeli kue basung (kue yang berasal dari Sumatera Barat) dan kue mendut (kue yang berasal dari Jawa Tengah). Dia membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00. Di toko yang sama, Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.<br><br>Berapa harga tiga kue mendut dan tujuh kue basung?

| Opsi | Isi |
|---|---|
| A | Rp42.000,00 |
| B | Rp34.500,00 |
| C | Rp37.500,00 |
| D | Rp40.500,00 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `Rp40.500,00`.
Solusi minimum hasil AI: Sistem: b+3m=13500 dan 2b+5m=24000. Dari (1), b=13500-3m. Substitusi ke (2): 2(13500-3m)+5m=24000 -> 27000-6m+5m=24000 -> m=3000. Maka b=13500-3(3000)=4500. Harga 3m+7b = 3(3000)+7(4500) = 9000+31500 = 40500.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c82a82f667e14761bde3eadd4c169f39d951559eb43fd57da1d6991c40bcc8e8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3514 |
| 2 | success | valid / verified | applying | procedural | Medium | 2532 |
| 3 | success | valid / verified | applying | procedural | Medium | 3438 |

Run 1 — solusi: Sistem: b+3m=13500 dan 2b+5m=24000. Dari (1), b=13500-3m. Substitusi ke (2): 2(13500-3m)+5m=24000 -> 27000-6m+5m=24000 -> m=3000. Maka b=13500-3(3000)=4500. Harga 3m+7b = 3(3000)+7(4500) = 9000+31500 = 40500.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan situasi ke dalam SPLDV dan menerapkan prosedur aljabar (substitusi/eliminasi) untuk menemukan nilai variabel, kemudian menghitung nilai kombinasi linear yang ditanyakan.. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma penyelesaian sistem persamaan linear dua variabel yang sudah dipelajari di kelas 9.. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00
- Intended difficulty `classify/Medium`: Soal memerlukan pemodelan matematika dan penyelesaian sistem persamaan linear dua variabel. Ini adalah tugas rutin bagi siswa kelas 9, namun melibatkan beberapa langkah (pemodelan, eliminasi/substitusi, perhitungan akhir).. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar SPLDV, operasi aritmatika dasar, dan substitusi/eliminasi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi standar kelas 9. Soal ini menguji pemahaman prosedural standar tanpa jebakan konseptual yang rumit. |

Run 2 — solusi: Misal b = harga kue basung, m = harga kue mendut. Sistem: (1) b + 3m = 13.500; (2) 2b + 5m = 24.000. Dari (1), b = 13.500 - 3m. Substitusi ke (2): 2(13.500 - 3m) + 5m = 24.000 => 27.000 - 6m + 5m = 24.000 => -m = -3.000 => m = 3.000. Maka b = 13.500 - 3(3.000) = 4.500. Harga 3m + 7b = 3(3.000) + 7(4.500) = 9.000 + 31.500 = 40.500.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan situasi ke dalam SPLDV, menyelesaikan sistem tersebut menggunakan metode eliminasi atau substitusi, dan menghitung nilai akhir berdasarkan variabel yang ditemukan. Ini adalah penerapan prosedur standar pada situasi kontekstual.. Bukti: Wayan pergi ke toko kue tradisional untuk membeli kue basung... membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma penyelesaian SPLDV (prosedural) untuk memecahkan masalah yang diberikan dalam bentuk cerita.. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00
- Intended difficulty `classify/Medium`: Soal ini memerlukan langkah-langkah rutin (memodelkan, menyelesaikan sistem, menghitung hasil akhir). Tidak ada strategi nonrutin yang diperlukan, hanya aplikasi prosedur SPLDV yang standar untuk kelas 9.. Bukti: satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, persamaan linear, dan metode eliminasi/substitusi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi inti kelas 9. Soal ini menuntut ketelitian dalam memodelkan dan menghitung, namun prosedurnya sangat standar. |

Run 3 — solusi: Sistem: b+3m=13500 (1) dan 2b+5m=24000 (2). Dari (1), b=13500-3m. Substitusi ke (2): 2(13500-3m)+5m=24000 => 27000-6m+5m=24000 => m=3000. Maka b=13500-3(3000)=4500. Harga 3m+7b = 3(3000)+7(4500) = 9000+31500 = 40500.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan situasi ke dalam SPLDV, menyelesaikan sistem tersebut, dan menghitung nilai kombinasi linear yang ditanyakan. Ini adalah penerapan prosedur standar SPLDV.. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang hubungan antar variabel dalam sistem persamaan linear dan penggunaan algoritma penyelesaian (substitusi/eliminasi).. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00
- Intended difficulty `classify/Medium`: Soal SPLDV standar dengan dua variabel. Langkah penyelesaian rutin (eliminasi/substitusi) dan perhitungan aritmatika dasar. Tidak ada jebakan konseptual yang kompleks.. Bukti: membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00; Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00; Berapa harga tiga kue mendut dan tujuh kue basung?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel dan operasi aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | SPLDV adalah materi inti kelas 9. Soal ini menuntut penyelesaian sistem standar, yang merupakan prosedur rutin bagi siswa kelas 9. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Wayan pergi ke toko kue tradisional untuk membeli kue basung (kue yang berasal dari Sumatera Barat) dan kue mendut (kue yang berasal dari Jawa Tengah). Dia membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00. Di toko yang sama, Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.

Berapa harga tiga kue mendut dan tujuh kue basung?
Pilihan: A. Rp42.000,00
B. Rp34.500,00
C. Rp37.500,00
D. Rp40.500,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 9,45 kali pengangkutan |
| B | 10 kali pengangkutan |
| C | 9 kali pengangkutan |
| D | 11 kali pengangkutan |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kapasitas muatan bersih = 2000 - 150 = 1850 kg. Kapasitas kotak per angkut = 1850 / 50 = 37 kotak. Total kotak = 350. Banyak pengangkutan = 350 / 37 = 9,459... Karena pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6135bd715232d411294d73b20fd0a32d5d8256705f6551eaa62311deb4452d2e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2277 |
| 2 | success | valid / verified | applying | procedural | Medium | 3392 |
| 3 | success | valid / verified | applying | procedural | Medium | 2249 |

Run 1 — solusi: Kapasitas muatan bersih = 2000 - 150 = 1850 kg. Kapasitas kotak per angkut = 1850 / 50 = 37 kotak. Total kotak = 350. Banyak pengangkutan = 350 / 37 = 9,459... Karena pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi kendala kapasitas (pertidaksamaan), melakukan operasi aritmatika untuk menentukan kapasitas per angkut, dan menerapkan penalaran pembulatan ke atas dalam konteks dunia nyata.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip pertidaksamaan linear untuk memodelkan masalah kapasitas dan menerapkan prosedur pembulatan yang sesuai dengan konteks masalah.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang kendala kapasitas dan interpretasi hasil pembagian dalam konteks nyata (pembulatan ke atas). Ini adalah prosedur rutin dalam pemodelan matematika sederhana.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, pemahaman konsep pertidaksamaan sederhana, dan logika pembulatan dalam konteks masalah. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini sesuai untuk kelas 9 karena melibatkan pemodelan pertidaksamaan linear sederhana dan interpretasi hasil yang logis, yang merupakan standar kompetensi pada jenjang tersebut. |

Run 2 — solusi: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Jumlah kotak per angkut = 1850 kg / 50 kg = 37 kotak. Total pengangkutan = 350 kotak / 37 kotak/angkut = 9,459. Karena harus mengangkut semua kotak, maka dibulatkan ke atas menjadi 10 kali pengangkutan.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur matematika (pengurangan dan pembagian) untuk menentukan kapasitas efektif, lalu menginterpretasikan hasil pembagian dalam konteks dunia nyata (pembulatan ke atas).. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan
- Dimensi pengetahuan `classify/procedural`: Melibatkan penggunaan algoritma aritmatika dasar dan pemahaman konsep kapasitas dalam konteks masalah pertidaksamaan/pembagian.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg.; Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (pengurangan, pembagian, pembulatan ke atas) yang saling terkait dalam konteks masalah nyata.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

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
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menyelesaikan masalah aritmatika sosial atau pertidaksamaan sederhana dengan interpretasi konteks. |

Run 3 — solusi: Kapasitas muatan kotak = 2000 kg - 150 kg = 1850 kg. Kapasitas per angkut = 1850 kg / 50 kg/kotak = 37 kotak. Banyak pengangkutan = 350 kotak / 37 kotak/angkut ≈ 9,46. Karena pengangkutan harus bilangan bulat dan semua kotak harus terangkut, maka dibulatkan ke atas menjadi 10 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur matematika yang tepat (pembagian dan pembulatan ke atas) untuk menyelesaikan masalah kontekstual terkait kapasitas angkut.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan algoritma pembagian dan prinsip pembulatan kontekstual (pembulatan ke atas untuk sisa muatan) dalam situasi nyata.. Bukti: berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
- Intended difficulty `classify/Medium`: Soal ini melibatkan langkah rutin: menghitung kapasitas bersih, menentukan kapasitas per angkut, dan melakukan pembulatan ke atas yang logis. Ini adalah prosedur standar untuk masalah kapasitas.. Bukti: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg.; berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar dan pemahaman konsep pembulatan dalam konteks masalah nyata. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah kapasitas angkut adalah materi standar kelas 9. Tingkat kesulitan Medium diberikan karena siswa harus menyadari perlunya pembulatan ke atas (ceiling function) agar semua kotak terangkut, bukan sekadar pembulatan matematis biasa. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.

Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
Pilihan: A. 9,45 kali pengangkutan
B. 10 kali pengangkutan
C. 9 kali pengangkutan
D. 11 kali pengangkutan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `6d6cb72cedbdc46857aa2701`

Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....

| Opsi | Isi |
|---|---|
| A | 4x + 3y - 14 = 0 |
| B | 3x + 4y - 14 = 0 |
| C | 4x - 3y + 14 = 0 |
| D | 3x - 4y + 33 = 0 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Karena sisi persegi panjang sejajar sumbu koordinat, titik sudut lainnya adalah Q(6,-1) dan S(2,2). Gradien garis QS adalah m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4 adalah y - 2 = -3/4(x - 2) -> 4y - 8 = -3x + 6 -> 3x + 4y - 14 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5885c34544dc98d52e79d31edbd680309f52638dcbb47266848b98b80ec91811`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2229 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2230 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2184 |

Run 1 — solusi: Karena sisi sejajar sumbu koordinat, titik sudut lainnya adalah Q(6,-1) dan S(2,2). Gradien garis QS adalah m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4 adalah y - 2 = -3/4(x - 2) -> 4y - 8 = -3x + 6 -> 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus persamaan garis lurus. Ini adalah penerapan prosedur rutin.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan konsep geometri (sifat persegi panjang pada bidang kartesius) dan prosedur aljabar (menentukan gradien dan persamaan garis).. Bukti: sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep koordinat dan sifat bangun datar untuk menentukan titik yang hilang, diikuti dengan prosedur standar mencari persamaan garis. Langkah-langkahnya rutin dan terstruktur.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan; sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep koordinat kartesius, sifat persegi panjang, rumus gradien, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengintegrasikan geometri koordinat dengan aljabar linear dasar. Soal ini menguji pemahaman tentang bagaimana posisi titik pada bidang kartesius menentukan persamaan garis. |

Run 2 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik sudut lainnya adalah Q(6,-1) dan S(2,2). Kemiringan garis QS adalah m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (6,-1) dengan m = -3/4 adalah y - (-1) = -3/4(x - 6) => 4(y + 1) = -3(x - 6) => 4y + 4 = -3x + 18 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat geometri persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus persamaan garis melalui dua titik.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara koordinat titik dan sifat geometri bangun datar (persegi panjang sejajar sumbu), serta prosedur aljabar untuk menentukan persamaan garis.. Bukti: titik sudut yang berhadapan; sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis
- Intended difficulty `classify/Medium`: Soal memerlukan langkah logis untuk menentukan koordinat titik Q dan S sebelum menghitung persamaan garis. Ini adalah prosedur rutin bagi siswa kelas 9 yang telah mempelajari geometri koordinat.. Bukti: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan; sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius, sifat persegi panjang, dan rumus persamaan garis. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengintegrasikan geometri koordinat dan aljabar linear dasar dalam konteks bangun datar. |

Run 3 — solusi: Karena sisi persegi panjang sejajar sumbu koordinat, titik sudut lainnya adalah Q(6,-1) dan S(2,2). Gradien garis QS adalah m = (2 - (-1)) / (2 - 6) = 3 / -4 = -3/4. Persamaan garis melalui (2,2) dengan m = -3/4 adalah y - 2 = -3/4(x - 2) => 4y - 8 = -3x + 6 => 3x + 4y - 14 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami sifat geometri persegi panjang dengan sisi sejajar sumbu koordinat untuk menentukan koordinat titik Q dan S, kemudian menerapkan rumus gradien dan persamaan garis. Ini melibatkan pemilihan prosedur yang tepat.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S
- Dimensi pengetahuan `classify/conceptual`: Siswa harus mengintegrasikan konsep geometri (sifat persegi panjang pada bidang kartesius) dengan konsep aljabar (persamaan garis lurus).. Bukti: titik sudut yang berhadapan; sisi sejajar sumbu-sumbu koordinat; persamaan garis
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep geometri untuk menentukan koordinat titik Q dan S sebelum menghitung persamaan garis. Langkah-langkahnya rutin namun memerlukan penalaran spasial.. Bukti: titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat; persamaan garis yang melalui titik Q dan S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Koordinat kartesius, gradien garis, persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghubungkan sifat bangun datar dengan koordinat kartesius dan persamaan garis. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4053`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pemahaman sifat geometri persegi panjang (sisi sejajar sumbu) untuk menentukan koordinat titik Q dan S, kemudian memilih dan menerapkan prosedur aljabar untuk menentukan persamaan garis lurus. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara koordinat titik dan sifat geometri bangun datar (persegi panjang sejajar sumbu), serta prosedur aljabar untuk menentukan persamaan garis.
- Intended difficulty `Medium`: Soal memerlukan langkah logis untuk menentukan koordinat titik Q dan S sebelum menghitung persamaan garis. Ini adalah prosedur rutin bagi siswa kelas 9 yang telah mempelajari geometri koordinat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Koordinat kartesius, sifat persegi panjang, rumus gradien, dan persamaan garis lurus. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengintegrasikan geometri koordinat dengan aljabar linear dasar. Soal ini menguji pemahaman tentang bagaimana posisi titik pada bidang kartesius menentukan persamaan garis. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pengertian Kemiringan
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....
Pilihan: A. 4x + 3y - 14 = 0
B. 3x + 4y - 14 = 0
C. 4x - 3y + 14 = 0
D. 3x - 4y + 33 = 0
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d0b943d7f97005ee05dfe7b2`

Dapatkah kita membuat jaring-jaring bangun ruang bola?

| Opsi | Isi |
|---|---|
| A | Hanya kerucut dan tabung yang bisa dibuat jaring-jaringnya, bola tidak |
| B | Tidak, sama sekali tidak mungkin dibuat |
| C | Ya, tetapi hasilnya selalu berbentuk persegi panjang |
| D | Ya, jaring-jaring bangun ruang bola dapat dibuat |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Secara teoritis, permukaan bola tidak dapat didatarkan sempurna tanpa distorsi. Namun, dalam konteks pembelajaran sekolah, jaring-jaring bola dapat didekati dengan membagi permukaan bola menjadi bagian-bagian kecil (seperti irisan kulit jeruk atau proyeksi peta) yang dapat disusun pada bidang datar. Oleh karena itu, jawaban D diterima sebagai konsep aproksimasi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4bd25f1c9c6bda4f86ad721cbae87dd738f5b999ff445ea28f71227250bf3aff`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2172 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2015 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1990 |

Run 1 — solusi: Secara teoritis, permukaan bola tidak dapat didatarkan sempurna tanpa distorsi. Namun, dalam konteks pembelajaran sekolah, jaring-jaring bola dapat didekati dengan membagi permukaan bola menjadi bagian-bagian kecil (seperti irisan kulit jeruk atau proyeksi peta) yang dapat disusun pada bidang datar. Oleh karena itu, jawaban D diterima sebagai konsep aproksimasi.
- Domain kognitif `classify/knowing`: Soal ini menuntut pemahaman konseptual tentang sifat bangun ruang sisi lengkung dan kemungkinan representasi permukaannya pada bidang datar (jaring-jaring). Siswa perlu memahami bahwa meskipun bola tidak memiliki jaring-jaring yang sempurna seperti kubus, konsep jaring-jaring dapat diaplikasikan melalui aproksimasi.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pengetahuan konseptual mengenai definisi dan batasan jaring-jaring bangun ruang, khususnya pada objek sisi lengkung yang tidak dapat didatarkan secara isometrik.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan menanyakan fakta konseptual yang mungkin jarang dibahas secara mendalam di kelas, namun prosedurnya sangat langsung (hanya memilih ya/tidak).. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jaring-jaring bangun ruang sisi datar dan sisi lengkung. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pertanyaan ini menguji pemahaman konseptual dasar tentang jaring-jaring. Meskipun konsep bola tidak bisa didatarkan adalah materi lanjut, dalam konteks SMP, ini sering diperkenalkan sebagai pengetahuan faktual/konseptual sederhana. |

Run 2 — solusi: Secara matematis, permukaan bola tidak dapat dibentangkan menjadi bidang datar tanpa distorsi (seperti pada proyeksi peta). Namun, dalam konteks kurikulum sekolah, jaring-jaring bola sering didekati dengan irisan-irisan (seperti kulit jeruk) yang dapat disusun menjadi bidang datar. Oleh karena itu, jawaban D diterima dalam konteks pedagogis.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual tentang sifat bangun ruang sisi lengkung. Siswa perlu mengenali bahwa meskipun secara topologis bola tidak memiliki jaring-jaring sempurna seperti kubus, dalam konteks pembelajaran, konsep jaring-jaring bola diajarkan.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menanyakan fakta atau prinsip dasar mengenai klasifikasi dan representasi bangun ruang, yang termasuk dalam pengetahuan konseptual.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan langsung, menguji pemahaman definisi tanpa memerlukan perhitungan atau langkah prosedural yang kompleks.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jaring-jaring bangun ruang sisi datar dan sisi lengkung. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pertanyaan konseptual dasar yang sesuai untuk kelas 9, di mana siswa diharapkan memahami karakteristik bangun ruang sisi lengkung. |

Run 3 — solusi: Secara matematis, permukaan bola dapat didekati atau dipetakan ke dalam bentuk datar (jaring-jaring) melalui teknik proyeksi atau pendekatan poligon, meskipun tidak dapat dibentangkan secara sempurna tanpa distorsi. Dalam konteks kurikulum SMP, konsep ini menekankan bahwa permukaan lengkung dapat diwakili oleh jaring-jaring.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual tentang sifat bangun ruang sisi lengkung. Siswa perlu mengenali bahwa jaring-jaring bukan hanya milik bangun sisi datar, tetapi juga dapat didekati untuk bola.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menanyakan fakta atau prinsip dasar mengenai definisi dan kemungkinan representasi jaring-jaring pada bangun ruang bola.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan menanyakan konsep dasar. Tidak ada perhitungan atau langkah prosedural yang diperlukan, hanya pemahaman konsep.. Bukti: Dapatkah kita membuat jaring-jaring bangun ruang bola?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jaring-jaring bangun ruang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pertanyaan ini adalah pertanyaan konseptual dasar yang sesuai untuk tingkat SMP, menguji pemahaman definisi jaring-jaring. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Klasifikasi Bangun Ruang dan Jaring-Jaring
Tipe soal: multiple_choice
Stimulus: -
Soal: Dapatkah kita membuat jaring-jaring bangun ruang bola?
Pilihan: A. Hanya kerucut dan tabung yang bisa dibuat jaring-jaringnya, bola tidak
B. Tidak, sama sekali tidak mungkin dibuat
C. Ya, tetapi hasilnya selalu berbentuk persegi panjang
D. Ya, jaring-jaring bangun ruang bola dapat dibuat
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: Konsep jaring-jaring bola secara matematis bersifat aproksimasi (pendekatan) karena permukaan bola tidak dapat didatarkan (flattened) tanpa distorsi (teorema Theorema Egregium Gauss). Pernyataan bahwa jaring-jaring bola 'dapat dibuat' memerlukan konteks aproksimasi (seperti irisan kulit jeruk) agar tidak menyesatkan secara geometris..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `394ec3b5c5b98c434a4cedde`

Apa yang dimaksud dengan jaring-jaring bangun ruang?

| Opsi | Isi |
|---|---|
| A | Kumpulan rusuk yang membentuk kerangka luar suatu bangun ruang |
| B | Bagian permukaan bangun ruang yang terlihat dari luar saja |
| C | Bentuk tiga dimensi yang menunjukkan besar ruang yang ditempati suatu bangun ruang |
| D | Bentuk dua dimensi yang dapat digambar, dipotong, dan dirangkai sedemikian rupa sehingga menjadi sebuah bangun tiga dimensi |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Jaring-jaring bangun ruang adalah bidang datar (dua dimensi) yang merupakan gabungan dari sisi-sisi bangun ruang tersebut, yang jika dilipat atau dirangkai menurut rusuk-rusuknya akan membentuk bangun ruang tiga dimensi. Pilihan D secara akurat mendeskripsikan definisi ini.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9a12b539fa8fc3b757936de171e36aa35d67032f45757dcc6bc44ef1e38187be`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1816 |
| 2 | success | valid / verified | knowing | factual | Easy | 1798 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1806 |

Run 1 — solusi: Jaring-jaring bangun ruang didefinisikan sebagai rangkaian bidang datar (dua dimensi) yang jika dilipat atau dirangkai menurut rusuk-rusuknya akan membentuk bangun ruang tiga dimensi. Pilihan D secara akurat mendeskripsikan proses ini.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali definisi konseptual dari jaring-jaring bangun ruang. Tidak ada prosedur perhitungan atau strategi pemecahan masalah yang kompleks.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap terminologi dan definisi dasar dalam geometri bangun ruang.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan langsung (recall), tidak memerlukan langkah perhitungan atau analisis strategi yang rumit.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan jaring-jaringnya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Definisi jaring-jaring adalah materi dasar geometri yang diperkenalkan sejak jenjang SD dan diperdalam di SMP. Soal ini hanya menuntut ingatan terhadap definisi tersebut. |

Run 2 — solusi: Jaring-jaring bangun ruang adalah representasi dua dimensi dari permukaan bangun ruang yang jika dilipat atau dirangkai akan membentuk bangun tiga dimensi tersebut. Pilihan D secara akurat mendeskripsikan proses ini.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali definisi konseptual dari jaring-jaring bangun ruang. Tidak ada perhitungan atau penerapan prosedur kompleks yang diperlukan.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap definisi atau terminologi dasar dalam geometri bangun ruang.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Intended difficulty `classify/Easy`: Soal ini bersifat definisional dan sangat mendasar, tidak memerlukan langkah pemecahan masalah atau analisis yang kompleks.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan jaring-jaringnya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Definisi jaring-jaring adalah materi dasar geometri yang diajarkan di tingkat SMP. Soal ini hanya menguji ingatan terhadap konsep tersebut. |

Run 3 — solusi: Jaring-jaring bangun ruang adalah representasi dua dimensi dari sisi-sisi bangun ruang yang jika dilipat atau dirangkai akan membentuk bangun tiga dimensi tersebut. Pilihan D secara akurat mendeskripsikan proses dan sifat geometris ini.
- Domain kognitif `classify/knowing`: Soal ini meminta definisi konseptual dasar tentang jaring-jaring bangun ruang. Siswa hanya perlu mengingat atau mengenali definisi yang tepat dari materi geometri yang dipelajari.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap terminologi dan definisi dasar dalam geometri bangun ruang.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?
- Intended difficulty `classify/Easy`: Soal bersifat teoretis dan langsung (recall), tidak memerlukan perhitungan atau strategi pemecahan masalah yang kompleks.. Bukti: Apa yang dimaksud dengan jaring-jaring bangun ruang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang sisi datar dan konsep jaring-jaring. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Definisi jaring-jaring adalah materi dasar geometri SMP yang bersifat hafalan/pemahaman konsep awal, sehingga tingkat kesulitannya rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3214`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali definisi konseptual dari jaring-jaring bangun ruang. Tidak ada prosedur perhitungan atau strategi pemecahan masalah yang kompleks.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman siswa terhadap terminologi dan definisi dasar dalam geometri bangun ruang.
- Intended difficulty `Easy`: Soal ini bersifat teoretis dan langsung (recall), tidak memerlukan langkah perhitungan atau analisis strategi yang rumit.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan jaring-jaringnya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Definisi jaring-jaring adalah materi dasar geometri yang diperkenalkan sejak jenjang SD dan diperdalam di SMP. Soal ini hanya menuntut ingatan terhadap definisi tersebut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Klasifikasi Bangun Ruang dan Jaring-Jaring
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa yang dimaksud dengan jaring-jaring bangun ruang?
Pilihan: A. Kumpulan rusuk yang membentuk kerangka luar suatu bangun ruang
B. Bagian permukaan bangun ruang yang terlihat dari luar saja
C. Bentuk tiga dimensi yang menunjukkan besar ruang yang ditempati suatu bangun ruang
D. Bentuk dua dimensi yang dapat digambar, dipotong, dan dirangkai sedemikian rupa sehingga menjadi sebuah bangun tiga dimensi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `ee45c96e4346ffea193e7a99`

Sebuah kotak pensil terbuat dari logam dengan dimensi 20 cm × 10 cm × 3 cm. Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.

| Opsi | Isi |
|---|---|
| A | 580 cm² |
| B | 600 cm² |
| C | 520 cm² |
| D | 290 cm² |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Luas permukaan balok = 2 x (p x l + p x t + l x t). Diketahui p=20, l=10, t=3. Maka, luas = 2 x (20x10 + 20x3 + 10x3) = 2 x (200 + 60 + 30) = 2 x 290 = 580 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6873f75d413b213c638f839e056deaeb821cc82058ae91a532fda1c03396572a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2072 |
| 2 | success | valid / verified | applying | procedural | Easy | 2074 |
| 3 | success | valid / verified | applying | procedural | Easy | 2015 |

Run 1 — solusi: Luas permukaan balok = 2 x (p x l + p x t + l x t). Diketahui p=20, l=10, t=3. Maka, luas = 2 x (20x10 + 20x3 + 10x3) = 2 x (200 + 60 + 30) = 2 x 290 = 580 cm².
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus luas permukaan balok secara langsung pada situasi rutin (kotak pensil). Tidak ada strategi nonrutin atau integrasi kompleks yang diperlukan.. Bukti: Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perhitungan luas permukaan bangun ruang sisi datar (balok).. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi dimensi dan menerapkan rumus luas permukaan balok tanpa kendala tambahan.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan balok dan operasi perkalian/penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perhitungan luas permukaan balok adalah materi standar kelas 8/9 yang bersifat prosedural dan rutin. |

Run 2 — solusi: Luas permukaan balok = 2 x (p x l + p x t + l x t). Diketahui p=20, l=10, t=3. Maka, luas = 2 x (20x10 + 20x3 + 10x3) = 2 x (200 + 60 + 30) = 2 x 290 = 580 cm².
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus luas permukaan balok secara langsung pada situasi rutin (kotak pensil). Tidak ada strategi nonrutin atau integrasi informasi kompleks.. Bukti: Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perhitungan luas permukaan bangun ruang sisi datar.. Bukti: 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu prosedur standar yang jelas. Beban kognitif rendah karena hanya melibatkan substitusi nilai ke dalam rumus yang sudah dikenal.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan balok dan operasi perkalian/penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 sebagai latihan dasar penerapan rumus luas permukaan bangun ruang sisi datar. |

Run 3 — solusi: Luas permukaan balok = 2 x (p x l + p x t + l x t). Substitusi nilai: 2 x (20 x 10 + 20 x 3 + 10 x 3) = 2 x (200 + 60 + 30) = 2 x 290 = 580 cm².
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus luas permukaan balok secara langsung pada situasi rutin (kotak pensil). Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur perhitungan luas permukaan bangun ruang sisi datar (balok).. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu prosedur standar (rumus luas permukaan balok). Beban perhitungan rendah dan tidak memerlukan transfer representasi.. Bukti: dimensi 20 cm × 10 cm × 3 cm; luas logam yang dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan balok dan operasi perkalian/penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 sebagai penerapan langsung rumus luas permukaan bangun ruang sisi datar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak pensil terbuat dari logam dengan dimensi 20 cm × 10 cm × 3 cm. Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.
Pilihan: A. 580 cm²
B. 600 cm²
C. 520 cm²
D. 290 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `27c5fab7664c58cab4d858b0`

Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

| Opsi | Isi |
|---|---|
| A | 0,0529 m² |
| B | 1,38 m² |
| C | 0,3174 m² |
| D | 0,012167 m² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, luas permukaan = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e73466940e6de1fbc5a0d60ffacfd0d1e7549592340d19335628d4896760ac59`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2032 |
| 2 | success | valid / verified | applying | procedural | Easy | 2046 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2024 |

Run 1 — solusi: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, luas = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus luas permukaan kubus secara langsung dengan nilai yang diberikan. Ini adalah prosedur rutin yang melibatkan substitusi nilai ke dalam rumus yang sudah dikenal.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang rumus luas permukaan bangun ruang sisi datar (kubus) dan kemampuan melakukan perhitungan prosedural.. Bukti: luas permukaan kubus = 6×s²
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengingat rumus luas permukaan kubus dan melakukan operasi perkalian desimal sederhana. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan kubus dan operasi perkalian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas permukaan kubus adalah materi dasar yang sudah dipelajari di jenjang sebelumnya dan diperkuat di kelas 9. Soal ini tidak menuntut pemikiran tingkat tinggi. |

Run 2 — solusi: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, luas permukaan = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus luas permukaan kubus (6s²) dengan nilai yang diberikan. Siswa hanya perlu melakukan substitusi dan operasi aritmatika dasar, yang termasuk dalam kategori menerapkan prosedur rutin.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau rumus luas permukaan bangun ruang sisi datar (kubus) dan bagaimana menerapkannya pada nilai numerik.. Bukti: luas permukaan kubus = 6×s²
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengingat rumus luas permukaan kubus dan melakukan perkalian desimal sederhana. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan kubus dan operasi perkalian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas permukaan kubus adalah materi dasar SMP yang sudah dipelajari sejak kelas 7/8. Soal ini merupakan aplikasi langsung rumus tanpa variasi atau konteks cerita yang rumit. |

Run 3 — solusi: Luas permukaan kubus = 6 × s². Diketahui s = 0,23 m. Maka, luas permukaan = 6 × (0,23)² = 6 × 0,0529 = 0,3174 m².
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus luas permukaan kubus (6s²) dengan nilai yang diberikan. Siswa hanya perlu melakukan substitusi dan perhitungan aritmatika dasar.. Bukti: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep luas permukaan bangun ruang sisi datar (kubus) sebagai jumlah luas keenam sisinya.. Bukti: luas permukaan kubus = 6×s²
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengingat rumus dan melakukan operasi perkalian desimal sederhana tanpa ada kendala atau strategi non-rutin.. Bukti: 0,23 m; luas permukaan kubus = 6×s²

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan kubus dan operasi perkalian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas permukaan kubus adalah standar kelas 9. Soal ini menguji pemahaman dasar rumus tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3489`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal meminta penerapan langsung rumus luas permukaan kubus (6s²) dengan nilai yang diberikan. Ini adalah prosedur rutin yang melibatkan substitusi nilai ke dalam rumus yang sudah dikenal.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang algoritma atau rumus luas permukaan bangun ruang sisi datar (kubus) dan bagaimana menerapkannya pada nilai numerik.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengingat rumus luas permukaan kubus dan melakukan operasi perkalian desimal sederhana. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep luas permukaan kubus dan operasi perkalian bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi luas permukaan kubus adalah materi dasar yang sudah dipelajari di jenjang sebelumnya dan diperkuat di kelas 9. Soal ini tidak menuntut pemikiran tingkat tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
Pilihan: A. 0,0529 m²
B. 1,38 m²
C. 0,3174 m²
D. 0,012167 m²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `aee8fd25cf246c58a370058e`

Sebuah balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7. Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.

| Opsi | Isi |
|---|---|
| A | 420 satuan kubik |
| B | 1.680 satuan kubik |
| C | 105 satuan kubik |
| D | 6.720 satuan kubik |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `6.720 satuan kubik`.
Solusi minimum hasil AI: Volume awal balok = 5 x 3 x 7 = 105. Jika ukuran diubah dengan skala k=4, maka volume baru = V_awal x k^3 = 105 x 4^3 = 105 x 64 = 6.720 satuan kubik.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9e333def2d62b4f1c1a7b423684382392aed99bcd6170d75409756d91cb649e1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2058 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2049 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2069 |

Run 1 — solusi: Volume awal balok = 5 x 3 x 7 = 105. Jika ukuran diubah dengan skala k=4, maka volume baru = V_awal x k^3 = 105 x 4^3 = 105 x 64 = 6.720 satuan kubik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan volume bangun ruang akibat dilatasi (skala), yaitu V' = V * k^3. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: diubah ukurannya dengan skala 4; tentukan volume balok setelah diubah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara faktor skala dan perubahan volume (konsep pangkat tiga pada dilatasi volume).. Bukti: skala 4; volume balok setelah diubah
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa sering terjebak menggunakan skala linear (k) atau kuadrat (k^2) untuk volume, sehingga memerlukan pemahaman konsep yang tepat tentang dilatasi volume (k^3) meskipun langkah operasinya rutin.. Bukti: panjang 5, lebar 3, dan tinggi 7; skala 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume balok dan konsep dilatasi/skala pada bangun ruang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami bahwa perubahan skala pada dimensi linear akan berdampak pangkat tiga pada volume. Pilihan pengecoh (A dan B) sangat efektif karena menangkap kesalahan umum siswa yang mengabaikan sifat pangkat tiga. |

Run 2 — solusi: Volume awal balok = 5 x 3 x 7 = 105 satuan kubik. Karena skala perubahan adalah 4, maka volume baru = 105 x (4^3) = 105 x 64 = 6.720 satuan kubik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan volume bangun ruang akibat dilatasi (skala k) dengan menggunakan faktor skala pangkat tiga (k^3). Ini merupakan penerapan prosedur rutin pada situasi yang diberikan.. Bukti: diubah ukurannya dengan skala 4; tentukan volume balok setelah diubah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara faktor skala dilatasi dengan perubahan volume (prinsip matematis), yang termasuk dalam dimensi pengetahuan konseptual.. Bukti: skala 4; volume balok setelah diubah
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya menghitung volume awal, tetapi harus memahami dan menerapkan prinsip bahwa perubahan skala k pada dimensi linear akan mengakibatkan perubahan volume sebesar k^3, bukan sekadar mengalikan dengan k atau k^2.. Bukti: panjang 5, lebar 3, dan tinggi 7; skala 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume balok dan konsep dilatasi/skala pada bangun ruang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi dilatasi dan perubahan volume adalah standar kelas 9. Soal ini menguji pemahaman konseptual tentang faktor skala pangkat tiga yang sering menjadi jebakan bagi siswa. |

Run 3 — solusi: Volume awal balok = 5 * 3 * 7 = 105. Jika ukuran balok diubah dengan skala k = 4, maka volume baru = volume awal * k^3. Volume baru = 105 * 4^3 = 105 * 64 = 6.720 satuan kubik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan volume bangun ruang akibat perubahan skala (dilatasi), yaitu V' = V * k^3. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: diubah ukurannya dengan skala 4; tentukan volume balok setelah diubah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara faktor skala dan perubahan volume (konsep pangkat tiga pada volume), yang merupakan prinsip konseptual dalam geometri.. Bukti: skala 4; volume balok setelah diubah
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena melibatkan prosedur langsung yang familiar bagi siswa kelas 9 terkait dilatasi volume. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: panjang 5, lebar 3, dan tinggi 7; skala 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume balok dan konsep dilatasi/perubahan skala pada bangun ruang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi dan perubahan volume adalah bagian dari kurikulum SMP kelas 9. Prosedur perhitungan langsung dan penggunaan faktor skala pangkat tiga adalah standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3591`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep perubahan volume bangun ruang akibat dilatasi (skala k), yaitu V' = V * k^3. Ini adalah penerapan prosedur standar pada situasi rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang hubungan antara faktor skala dan perubahan volume (konsep pangkat tiga pada dilatasi volume).
- Intended difficulty `Medium`: Soal ini tergolong Medium karena siswa sering terjebak menggunakan skala linear (k) atau kuadrat (k^2) untuk volume, sehingga memerlukan pemahaman konsep yang tepat tentang dilatasi volume (k^3) meskipun langkah operasinya rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume balok dan konsep dilatasi/skala pada bangun ruang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami bahwa perubahan skala pada dimensi linear akan berdampak pangkat tiga pada volume. Pilihan pengecoh (A dan B) sangat efektif karena menangkap kesalahan umum siswa yang mengabaikan sifat pangkat tiga. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7. Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.
Pilihan: A. 420 satuan kubik
B. 1.680 satuan kubik
C. 105 satuan kubik
D. 6.720 satuan kubik
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `bc9eda46aa2fecb0da3798d8`

Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

| Opsi | Isi |
|---|---|
| A | Volume limas adalah setengah dari volume prisma |
| B | Volume limas adalah tiga kali volume prisma |
| C | Volume limas tersebut adalah sepertiga dari volume prisma |
| D | Volume limas sama dengan volume prisma |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Rumus volume prisma adalah V_prisma = Luas_alas * tinggi. Rumus volume limas adalah V_limas = 1/3 * Luas_alas * tinggi. Jika alas dan tinggi sama, maka V_limas = 1/3 * V_prisma.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9c32c7ab9b83f0a2b0aab0ee00ab180b0f72291e16ea2f564b3b9b0dea871755`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1966 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1888 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1882 |

Run 1 — solusi: Rumus volume prisma adalah V_prisma = Luas_alas * tinggi. Rumus volume limas adalah V_limas = 1/3 * Luas_alas * tinggi. Jika alas dan tinggi sama, maka V_limas = 1/3 * V_prisma.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual dasar mengenai hubungan volume antara dua bangun ruang yang memiliki komponen alas dan tinggi yang identik. Siswa perlu mengingat atau memahami prinsip geometri dasar tersebut tanpa perlu melakukan perhitungan kompleks.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menanyakan tentang prinsip atau hubungan antar konsep geometri (volume bangun ruang), yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pengetahuan dasar yang diajarkan di kelas 8/9 mengenai rumus volume. Tidak ada langkah perhitungan atau strategi non-rutin yang diperlukan.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus volume prisma dan limas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume bangun ruang sisi datar adalah kurikulum standar SMP kelas 8/9. Pertanyaan ini adalah recall konsep dasar yang sangat familiar. |

Run 2 — solusi: Volume prisma dengan luas alas A dan tinggi t adalah V_prisma = A * t. Volume limas dengan luas alas A dan tinggi t adalah V_limas = 1/3 * A * t. Dengan demikian, V_limas = 1/3 * V_prisma.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual dasar mengenai hubungan rumus volume antara dua bangun ruang yang memiliki komponen alas dan tinggi yang identik. Siswa perlu mengingat atau memahami prinsip geometri dasar ini tanpa perlu melakukan perhitungan numerik yang kompleks.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal ini berfokus pada pemahaman prinsip atau hubungan antar konsep geometri (volume limas vs prisma), yang merupakan bagian dari pengetahuan konseptual.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung atau pengingatan fakta konseptual yang diajarkan secara eksplisit di kelas 9. Tidak ada langkah perhitungan atau strategi non-rutin yang diperlukan.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume prisma (V=La*t) dan rumus volume limas (V=1/3*La*t). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar geometri ruang yang diajarkan di kelas 9. Mengingat hubungan perbandingan volume adalah tugas rutin. |

Run 3 — solusi: Volume prisma dengan alas A dan tinggi t adalah V_prisma = A * t. Volume limas dengan alas A dan tinggi t adalah V_limas = 1/3 * A * t. Maka, V_limas = 1/3 * V_prisma.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual dasar mengenai hubungan volume antara dua bangun ruang yang memiliki komponen alas dan tinggi yang identik. Siswa hanya perlu mengingat atau memahami prinsip dasar geometri ruang tersebut tanpa perlu melakukan perhitungan kompleks.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal ini berfokus pada pemahaman prinsip atau hubungan antar konsep geometri (volume limas vs prisma), yang merupakan bagian dari pengetahuan konseptual.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung dan menguji pengetahuan dasar yang diajarkan di kelas 9 mengenai rumus volume bangun ruang. Tidak ada langkah perhitungan atau strategi yang diperlukan.. Bukti: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rumus volume prisma (V=La*t) dan limas (V=1/3*La*t). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar geometri yang diajarkan di SMP kelas 9. Soal tidak memerlukan manipulasi aljabar atau perhitungan, hanya pemahaman definisi. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
Pilihan: A. Volume limas adalah setengah dari volume prisma
B. Volume limas adalah tiga kali volume prisma
C. Volume limas tersebut adalah sepertiga dari volume prisma
D. Volume limas sama dengan volume prisma
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `b0484eaccca405ba34c3f428`

Untuk tiap-tiap lingkaran yang diketahui r (panjang jari-jari) atau d (panjang diameter) berikut, tentukan keliling dan luasnya! ⓐ r = 12 cm

| Opsi | Isi |
|---|---|
| A | Keliling 75,36 cm dan luas 75,36 cm² |
| B | Keliling 452,16 cm dan luas 75,36 cm² |
| C | Keliling 75,36 cm dan luas 452,16 cm² |
| D | Keliling 37,68 cm dan luas 452,16 cm² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: K = 2 * 3.14 * 12 = 75.36 cm. L = 3.14 * 12^2 = 3.14 * 144 = 452.16 cm^2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6b1332fed096576cf8d474e5ec48a294a8d24b0c131ed68ac100b678e7384b59`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2788 |
| 2 | success | valid / verified | applying | procedural | Easy | 2747 |
| 3 | success | valid / verified | applying | procedural | Easy | 2659 |

Run 1 — solusi: K = 2 * 3.14 * 12 = 75.36 cm. L = 3.14 * 12^2 = 3.14 * 144 = 452.16 cm^2.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus keliling dan luas lingkaran secara langsung dengan nilai jari-jari yang diketahui.. Bukti: r = 12 cm; tentukan keliling dan luasnya
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur rutin untuk menghitung keliling dan luas lingkaran berdasarkan rumus yang sudah dipelajari.. Bukti: r = 12 cm; tentukan keliling dan luasnya
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan substitusi nilai ke dalam rumus standar tanpa langkah tambahan atau kendala kompleks.. Bukti: r = 12 cm; tentukan keliling dan luasnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus keliling (2πr) dan luas (πr²) lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lingkaran adalah dasar di kelas 9, soal ini adalah latihan langsung yang tidak menuntut pemikiran tingkat tinggi. |

Run 2 — solusi: K = 2 × 3,14 × 12 = 75,36 cm. L = 3,14 × 12² = 3,14 × 144 = 452,16 cm².
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus keliling dan luas lingkaran secara langsung dengan nilai jari-jari yang diketahui.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam menggunakan rumus keliling dan luas lingkaran.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Intended difficulty `classify/Easy`: Soal bersifat rutin dan langsung, hanya memerlukan substitusi nilai ke dalam rumus yang sudah dikenal.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus keliling (2πr) dan luas lingkaran (πr²) |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan sudah lancar menggunakan rumus dasar lingkaran ini. |

Run 3 — solusi: K = 2 * 3,14 * 12 = 75,36 cm. L = 3,14 * 12^2 = 3,14 * 144 = 452,16 cm^2.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus keliling dan luas lingkaran secara langsung pada nilai jari-jari yang diberikan.. Bukti: tentukan keliling dan luasnya! ⓐ r = 12 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menggunakan algoritma atau rumus standar untuk menghitung nilai keliling dan luas.. Bukti: K=2πr=2×3,14×12=75,36 cm; L=πr²=3,14×144=452,16 cm²
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan substitusi nilai ke dalam rumus yang sudah dikenal.. Bukti: r = 12 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus keliling (2πr) dan luas (πr²) lingkaran. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah latihan dasar kelas 9 yang menguji ingatan dan penerapan rumus lingkaran tanpa adanya variasi atau kendala tambahan. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk tiap-tiap lingkaran yang diketahui r (panjang jari-jari) atau d (panjang diameter) berikut, tentukan keliling dan luasnya! ⓐ r = 12 cm
Pilihan: A. Keliling 75,36 cm dan luas 75,36 cm²
B. Keliling 452,16 cm dan luas 75,36 cm²
C. Keliling 75,36 cm dan luas 452,16 cm²
D. Keliling 37,68 cm dan luas 452,16 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ce529c7a884ca9ebbfb36e54`

Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar ____.

| Opsi | Isi |
|---|---|
| A | 22 |
| B | 3,14 (atau 22/7) |
| C | 3,41 |
| D | 2 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Keliling lingkaran (K) dirumuskan sebagai K = π × d, di mana d adalah diameter. Maka, perbandingan keliling terhadap diameter adalah K/d = π. Nilai pendekatan π adalah 3,14 atau 22/7.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1fbce5b5bd90799a64b7a8c43176777f6ee0920b7c89fff3cfc45d62c89023c3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1884 |
| 2 | success | valid / verified | knowing | factual | Easy | 1904 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1890 |

Run 1 — solusi: Keliling lingkaran (K) dirumuskan sebagai K = π × d, di mana d adalah diameter. Maka, perbandingan keliling terhadap diameter adalah K/d = π. Nilai π adalah konstanta yang nilainya sekitar 3,14 atau 22/7.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat definisi konstanta pi (π) sebagai rasio keliling terhadap diameter lingkaran, yang merupakan pengetahuan faktual dasar.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui definisi atau fakta matematis mengenai hubungan antara keliling dan diameter lingkaran yang menghasilkan konstanta pi.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (recall) mengenai definisi dasar lingkaran yang dipelajari di tingkat SMP.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi keliling lingkaran dan diameter. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar lingkaran yang diajarkan di kelas 8 dan diperkuat di kelas 9, sehingga bagi siswa kelas 9 ini adalah pengetahuan yang sangat familiar. |

Run 2 — solusi: Definisi keliling lingkaran (K) adalah K = π × d, di mana d adalah diameter. Maka, perbandingan keliling dengan diameter adalah K/d = π. Nilai π adalah konstanta yang nilainya sekitar 3,14 atau 22/7.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat definisi konstanta pi (π) sebagai rasio keliling terhadap diameter lingkaran. Ini adalah pengetahuan faktual dasar yang langsung.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui fakta matematis tentang hubungan antara keliling dan diameter lingkaran yang didefinisikan sebagai π.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya menanyakan definisi konstanta lingkaran yang sudah dipelajari sejak sekolah dasar/awal SMP. Tidak ada langkah perhitungan atau analisis.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang unsur-unsur lingkaran (keliling, diameter) dan konstanta pi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah pengetahuan dasar lingkaran yang sudah diperkenalkan jauh sebelum kelas 9, sehingga bagi siswa kelas 9 ini termasuk kategori sangat mudah. |

Run 3 — solusi: Definisi konstanta pi (π) adalah rasio keliling lingkaran (K) terhadap diameternya (d), yaitu K/d = π. Nilai pendekatan untuk π adalah 3,14 atau 22/7.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat definisi dasar konstanta pi (π) sebagai rasio keliling terhadap diameter lingkaran. Tidak ada prosedur kompleks atau strategi non-rutin yang diperlukan.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap konsep dasar atau terminologi matematika mengenai definisi pi (π) dalam geometri lingkaran.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung. Siswa hanya perlu mengetahui definisi konstanta pi yang diajarkan di awal materi lingkaran.. Bukti: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang unsur-unsur lingkaran (keliling, diameter) dan konstanta pi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan pengetahuan dasar yang diperkenalkan di tingkat SMP, sehingga tingkat kesulitannya rendah bagi siswa kelas 9. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3198`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menuntut siswa untuk mengingat definisi konstanta pi (π) sebagai rasio keliling terhadap diameter lingkaran, yang merupakan pengetahuan faktual dasar.
- Dimensi pengetahuan `factual`: Siswa perlu mengetahui fakta matematis mengenai hubungan antara keliling dan diameter lingkaran yang menghasilkan konstanta pi.
- Intended difficulty `Easy`: Soal ini bersifat sangat langsung (recall) mengenai definisi dasar lingkaran yang dipelajari di tingkat SMP.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi keliling lingkaran dan diameter. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar lingkaran yang diajarkan di kelas 8 dan diperkuat di kelas 9, sehingga bagi siswa kelas 9 ini adalah pengetahuan yang sangat familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar ____.
Pilihan: A. 22
B. 3,14 (atau 22/7)
C. 3,41
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `487ffef7f793443d4d651476`

Untuk memperingati ulang tahun Gilang, ibunya membuat nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut dengan diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm. Jika nasi kerucut ini ingin ditutupi dengan daun pisang, berapa luas daun pisang yang akan dibutuhkan?

| Opsi | Isi |
|---|---|
| A | ≈1.456,96 cm² |
| B | ≈2.285,92 cm² |
| C | ≈1.142,96 cm² |
| D | ≈1.099 cm² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jari-jari (r) = 10 cm. Garis pelukis (s) = √(r² + t²) = √(10² + 35²) = √(100 + 1225) = √1325 ≈ 36,40 cm. Luas selimut kerucut = πrs = 3,14 × 10 × 36,40 ≈ 1.142,96 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `855b4dacadc95f4edb557640fa759fc784c56c95a6c3a5e9c99071d9007a1879`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2200 |
| 2 | success | valid / verified | applying | procedural | Medium | 2214 |
| 3 | success | valid / verified | applying | procedural | Medium | 2244 |

Run 1 — solusi: Jari-jari (r) = 10 cm. Garis pelukis (s) = √(r² + t²) = √(10² + 35²) = √(100 + 1225) = √1325 ≈ 36,40 cm. Luas selimut kerucut = πrs = 3,14 × 10 × 36,40 ≈ 1.142,96 cm².
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa daun pisang hanya menutupi selimut kerucut, menghitung jari-jari dari diameter, menentukan garis pelukis menggunakan teorema Pythagoras, dan menerapkan rumus luas selimut kerucut.. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas daun pisang yang akan dibutuhkan
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur matematis (Pythagoras dan rumus luas selimut) untuk menyelesaikan masalah kontekstual.. Bukti: luas daun pisang yang akan dibutuhkan; diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep selimut kerucut, konversi diameter ke jari-jari, dan penggunaan Pythagoras untuk mencari garis pelukis. Ini adalah langkah rutin yang saling terkait.. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas daun pisang yang akan dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, rumus luas selimut kerucut, konsep jari-jari dan diameter. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengintegrasikan Pythagoras dengan geometri bangun ruang sisi lengkung. |

Run 2 — solusi: Jari-jari (r) = 10 cm. Garis pelukis (s) = sqrt(r^2 + t^2) = sqrt(10^2 + 35^2) = sqrt(100 + 1225) = sqrt(1325) ≈ 36,40 cm. Luas selimut kerucut = πrs = 3,14 * 10 * 36,40 ≈ 1.142,96 cm².
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa menutupi tumpeng berarti menghitung luas selimut kerucut, memilih rumus yang tepat (πrs), dan menghitung garis pelukis menggunakan teorema Pythagoras.. Bukti: nasi kerucut ini ingin ditutupi dengan daun pisang; diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm
- Dimensi pengetahuan `classify/procedural`: Siswa harus menerapkan prosedur algoritma luas selimut kerucut dan teorema Pythagoras untuk menentukan garis pelukis.. Bukti: luas daun pisang yang akan dibutuhkan; diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep bahwa daun pisang hanya menutupi selimut (bukan alas), penggunaan Pythagoras untuk mencari garis pelukis, dan perhitungan numerik. Ini adalah prosedur rutin bagi siswa kelas 9.. Bukti: diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas daun pisang yang akan dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras, rumus luas selimut kerucut, konversi diameter ke jari-jari. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu membedakan luas permukaan total dan luas selimut serta menggunakan Pythagoras dalam konteks bangun ruang. |

Run 3 — solusi: Jari-jari (r) = 10 cm. Tinggi (t) = 35 cm. Garis pelukis (s) = sqrt(r^2 + t^2) = sqrt(100 + 1225) = sqrt(1325) ≈ 36,40 cm. Luas selimut kerucut = πrs = 3,14 * 10 * 36,40 ≈ 1.142,96 cm².
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa daun pisang hanya menutupi selimut kerucut, menghitung garis pelukis menggunakan teorema Pythagoras, dan menerapkan rumus luas selimut kerucut.. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas daun pisang yang akan dibutuhkan
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang rumus luas permukaan bangun ruang sisi lengkung dan konsep geometris garis pelukis.. Bukti: luas daun pisang yang akan dibutuhkan; r=10 cm, garis pelukis l=√(10²+35²)=√1325≈36,40 cm; luas selimut kerucut = πrl
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah utama: menghitung garis pelukis dengan Pythagoras dan menghitung luas selimut. Ini adalah prosedur rutin yang diharapkan untuk kelas 9.. Bukti: diameter 20 cm; Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm; luas daun pisang yang akan dibutuhkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema Pythagoras dan rumus luas selimut kerucut. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah mempelajari geometri bangun ruang sisi lengkung dan Pythagoras. Soal ini menguji ketelitian dalam memilih rumus yang tepat (selimut saja) dan melakukan perhitungan bertahap. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk memperingati ulang tahun Gilang, ibunya membuat nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut dengan diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm. Jika nasi kerucut ini ingin ditutupi dengan daun pisang, berapa luas daun pisang yang akan dibutuhkan?
Pilihan: A. ≈1.456,96 cm²
B. ≈2.285,92 cm²
C. ≈1.142,96 cm²
D. ≈1.099 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `efbc889b95676e6e2d913479`

Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

| Opsi | Isi |
|---|---|
| A | Luas permukaan bola sama dengan luas lingkaran yang memiliki jari-jari yang sama |
| B | Luas permukaan bola sama dengan dua kali luas lingkaran yang memiliki jari-jari yang sama |
| C | Luas permukaan bola sama dengan setengah luas lingkaran yang memiliki jari-jari yang sama |
| D | Luas permukaan bola sama dengan empat kali luas lingkaran yang memiliki jari-jari yang sama |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Luas permukaan bola dirumuskan sebagai 4πr² dan luas lingkaran adalah πr². Dengan membandingkan kedua rumus tersebut, luas permukaan bola adalah 4 kali luas lingkaran dengan jari-jari yang sama.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1354b481d47e1efa2b50aa275b6d634ac42dd668099fed404f6acaf3e528e2f9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2361 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2364 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2523 |

Run 1 — solusi: Luas permukaan bola dirumuskan sebagai 4πr² dan luas lingkaran adalah πr². Dengan membandingkan kedua rumus tersebut, luas permukaan bola adalah 4 kali luas lingkaran dengan jari-jari yang sama.
- Domain kognitif `classify/knowing`: Soal ini menguji ingatan siswa terhadap rumus dasar luas permukaan bola dan hubungannya dengan luas lingkaran, yang merupakan pengetahuan faktual/konseptual langsung.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan struktural antara rumus luas permukaan bola (4πr²) dan luas lingkaran (πr²).. Bukti: keterkaitan antara luas permukaan bola dan luas lingkaran
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan hanya memerlukan pengetahuan rumus dasar tanpa langkah perhitungan yang kompleks.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas permukaan bola dan luas lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah standar kurikulum kelas 9. Soal tidak menuntut pemecahan masalah, hanya pengenalan hubungan rumus. |

Run 2 — solusi: Luas permukaan bola dirumuskan sebagai 4πr² dan luas lingkaran adalah πr². Dengan membandingkan kedua rumus tersebut, luas permukaan bola adalah 4 kali luas lingkaran dengan jari-jari yang sama.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan hubungan dasar antara rumus luas permukaan bola dan luas lingkaran, yang merupakan proses langsung.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan struktural antara rumus-rumus geometri dasar tersebut.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji ingatan terhadap rumus dasar yang dipelajari di kelas 9.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas lingkaran dan luas permukaan bola. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan sudah familiar dengan rumus bangun ruang sisi lengkung. |

Run 3 — solusi: Luas permukaan bola dirumuskan sebagai 4πr². Luas lingkaran dengan jari-jari r adalah πr². Dengan membandingkan kedua rumus tersebut, luas permukaan bola adalah 4 kali luas lingkaran (4πr² = 4 × πr²).
- Domain kognitif `classify/knowing`: Soal ini bersifat recall atau pengenalan langsung terhadap rumus geometri dasar yang sudah dipelajari, sehingga masuk dalam domain knowing.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai hubungan antar rumus geometri (konsep luas permukaan bola sebagai 4 kali luas lingkaran).. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan pengetahuan rumus dasar tanpa proses kalkulasi atau strategi yang kompleks.. Bukti: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas lingkaran dan luas permukaan bola. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan sudah familiar dengan rumus-rumus bangun ruang sisi lengkung. Soal ini tidak memerlukan langkah penyelesaian bertahap yang rumit. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
Pilihan: A. Luas permukaan bola sama dengan luas lingkaran yang memiliki jari-jari yang sama
B. Luas permukaan bola sama dengan dua kali luas lingkaran yang memiliki jari-jari yang sama
C. Luas permukaan bola sama dengan setengah luas lingkaran yang memiliki jari-jari yang sama
D. Luas permukaan bola sama dengan empat kali luas lingkaran yang memiliki jari-jari yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `1ef6efc5863938a14b737897`

Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar dengan diameter 2 meter dan panjang 12 meter?

| Opsi | Isi |
|---|---|
| A | 36.000 liter |
| B | 150.720 liter |
| C | 37.680 liter |
| D | 37,68 liter |

![Gambar sumber soal 17](<../../../images/kelas9_crop-s0011-truk-gas.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jari-jari (r) = diameter / 2 = 2 m / 2 = 1 m. Volume tabung = π × r² × t = 3,14 × (1 m)² × 12 m = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 liter/m³ = 37.680 liter.
Gambar sumber: images/kelas9_crop-s0011-truk-gas.png. Transkripsi visual: A side view of a tanker truck with a large cylindrical tank mounted on the trailer. The tank is horizontal, with a circular cross-section visible at the rear.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9f2ee0856f90c7854908b7738a8e7248dca3d9404cae4dabba26655158e042f4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3245 |
| 2 | success | valid / verified | applying | procedural | Easy | 3217 |
| 3 | success | valid / verified | applying | procedural | Medium | 3212 |

Run 1 — solusi: Jari-jari (r) = diameter/2 = 2m/2 = 1m. Volume (V) = π × r² × t = 3,14 × 1² × 12 = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 liter/m³ = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus volume tabung, melakukan substitusi nilai, dan menerapkan konversi satuan yang rutin. Ini adalah penerapan prosedur standar pada situasi yang familiar.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang rumus volume tabung dan hubungan konversi satuan volume (prosedural) dalam konteks geometri.. Bukti: Volume (V) = π × r² × h; 1 m³ = 1.000 liter
- Intended difficulty `classify/Medium`: Soal ini melibatkan langkah-langkah rutin: menentukan jari-jari dari diameter, menghitung volume, dan konversi satuan. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: diameter 2 meter; panjang 12 meter; Berapa liter

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
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung volume bangun ruang sisi lengkung dan melakukan konversi satuan dasar. Soal ini adalah aplikasi langsung dari rumus tersebut. |

Run 2 — solusi: Jari-jari (r) = diameter/2 = 2/2 = 1 m. Volume silinder = π × r² × h = 3,14 × 1² × 12 = 37,68 m³. Karena 1 m³ = 1.000 liter, maka volume = 37,68 × 1.000 = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu memilih rumus volume tabung, melakukan konversi satuan dari meter ke jari-jari, dan mengonversi satuan volume dari m³ ke liter. Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang rumus volume bangun ruang sisi lengkung (tabung) dan hubungan antar satuan volume.. Bukti: V=πr²h; 1 m³=1.000 liter
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan penerapan rumus langsung dan konversi satuan dasar yang umum diajarkan di kelas 9.. Bukti: diameter 2 meter; 1 m³=1.000 liter

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
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung volume tabung dan melakukan konversi satuan dasar tanpa kesulitan berarti. |

Run 3 — solusi: Jari-jari (r) = diameter / 2 = 2 m / 2 = 1 m. Volume tabung = π × r² × t = 3,14 × (1 m)² × 12 m = 37,68 m³. Konversi ke liter: 37,68 m³ × 1.000 liter/m³ = 37.680 liter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan volume (m³ ke liter). Ini adalah prosedur rutin yang dipelajari di kelas 9.. Bukti: diameter 2 meter dan panjang 12 meter; Berapa liter gas bumi yang dapat ditampung
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus volume bangun ruang sisi lengkung dan konversi satuan yang relevan.. Bukti: volume tabung; konversi meter kubik ke liter
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah rutin yang saling terkait: menghitung volume tabung dan melakukan konversi satuan volume (m³ ke liter).. Bukti: diameter 2 meter; panjang 12 meter; Berapa liter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung, hubungan diameter dan jari-jari, konversi satuan volume (m³ ke liter). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung volume bangun ruang sisi lengkung dan melakukan konversi satuan dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4736`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan rumus volume tabung dan melakukan konversi satuan volume. Ini adalah penerapan prosedur rutin pada situasi kontekstual yang familiar.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang rumus volume bangun ruang sisi lengkung dan konversi satuan yang relevan.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena hanya memerlukan penerapan rumus langsung dan konversi satuan dasar yang umum diajarkan di kelas 9 tanpa strategi nonrutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung, hubungan diameter dan jari-jari, konversi satuan volume (m³ ke liter). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menghitung volume bangun ruang sisi lengkung dan melakukan konversi satuan dasar dengan lancar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar dengan diameter 2 meter dan panjang 12 meter?
Pilihan: A. 36.000 liter
B. 150.720 liter
C. 37.680 liter
D. 37,68 liter
Transkripsi visual: A side view of a tanker truck with a large cylindrical tank mounted on the trailer. The tank is horizontal, with a circular cross-section visible at the rear.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `a0c228d869728c3140dece74`

Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

| Opsi | Isi |
|---|---|
| A | Volume kerucut sama dengan sepertiga volume tabung |
| B | Volume kerucut adalah tiga kali volume tabung |
| C | Volume kerucut sama dengan volume tabung |
| D | Volume kerucut adalah setengah volume tabung |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Volume tabung (V_tabung) = πr²t. Volume kerucut (V_kerucut) = 1/3 × πr²t. Karena jari-jari (r) dan tinggi (t) sama, maka V_kerucut = 1/3 × V_tabung.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ea3659103c485eea33a4d6c8d44fd5d6b4757332adcf3a0fdd55a260d9a17b32`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1982 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1921 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1980 |

Run 1 — solusi: Volume tabung (V_tabung) = πr²t. Volume kerucut (V_kerucut) = 1/3 × πr²t. Karena jari-jari (r) dan tinggi (t) sama, maka V_kerucut = 1/3 × V_tabung.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konsep dasar mengenai hubungan rumus volume antara kerucut dan tabung. Siswa hanya perlu mengingat atau mengenali hubungan proporsional antara kedua rumus tersebut (1/3). Ini termasuk kategori knowing karena bersifat recall terhadap fakta/rumus dasar.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal ini berfokus pada pemahaman prinsip atau hubungan antar konsep geometri (rumus volume), yang merupakan pengetahuan konseptual.. Bukti: hubungan antara volume kerucut dan tabung
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya menanyakan hubungan rumus yang sudah dipelajari di kelas 9. Tidak ada perhitungan kompleks atau langkah prosedural yang panjang.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan kerucut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi dasar geometri kelas 9 yang bersifat hafalan/pemahaman konsep langsung tanpa perlu manipulasi aljabar yang rumit. |

Run 2 — solusi: Volume tabung (V_t) = πr²t. Volume kerucut (V_k) = 1/3 πr²t. Karena r dan t sama, maka V_k = 1/3 V_t.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengingat dan menerapkan hubungan dasar antara rumus volume dua bangun ruang yang sudah dipelajari. Ini adalah proses mengingat fakta matematis yang langsung.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan konseptual antara rumus volume kerucut dan tabung dengan variabel yang sama.. Bukti: hubungan antara volume kerucut dan tabung
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung dan menguji pemahaman dasar rumus yang merupakan materi standar kelas 9. Tidak ada langkah perhitungan kompleks atau strategi non-rutin.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan kerucut |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume bangun ruang sisi lengkung adalah materi dasar kelas 9. Soal ini hanya menanyakan hubungan rumus yang sudah umum diketahui. |

Run 3 — solusi: Volume tabung (V_t) = πr²t. Volume kerucut (V_k) = 1/3 πr²t. Jika jari-jari (r) dan tinggi (t) sama, maka V_k = 1/3 V_t.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual dasar mengenai rumus volume bangun ruang sisi lengkung. Siswa hanya perlu mengingat atau mengenali hubungan proporsional antara rumus volume kerucut dan tabung dengan dimensi yang identik.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Dimensi pengetahuan `classify/conceptual`: Soal ini berfokus pada pemahaman hubungan antara dua konsep volume bangun ruang yang berbeda namun saling terkait secara matematis.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (recall) mengenai rumus dasar yang diajarkan di kelas 9. Tidak ada perhitungan kompleks atau strategi non-rutin yang diperlukan.. Bukti: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus volume tabung dan kerucut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi volume bangun ruang sisi lengkung adalah materi standar kelas 9. Pertanyaan ini menanyakan konsep dasar yang merupakan prasyarat untuk soal-soal yang lebih kompleks. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
Pilihan: A. Volume kerucut sama dengan sepertiga volume tabung
B. Volume kerucut adalah tiga kali volume tabung
C. Volume kerucut sama dengan volume tabung
D. Volume kerucut adalah setengah volume tabung
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `4088b8d020de84282c07a2b3`

Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?

| Opsi | Isi |
|---|---|
| A | 1.250 liter 325 ml |
| B | 1.249 liter 675 ml |
| C | 1.249 liter 325 ml |
| D | 1.250 liter 675 ml |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Sisa air = 2.225 liter - 975 liter 325 ml. Karena 2.225 liter = 2.224 liter 1.000 ml, maka: (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `17668eb5a9b67fa55e2d2182da9507537c43f39674efcc08c0ff0afa43ece67f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2133 |
| 2 | success | valid / verified | applying | procedural | Easy | 2093 |
| 3 | success | valid / verified | applying | procedural | Easy | 2126 |

Run 1 — solusi: Sisa air = 2.225 liter - 975 liter 325 ml. Karena 2.225 liter = 2.224 liter 1.000 ml, maka: (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan konversi satuan volume (liter ke mililiter) yang merupakan prosedur rutin dalam pengukuran.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan yang melibatkan konversi satuan (prosedural) dan pemahaman hubungan antar satuan volume (konseptual).. Bukti: 2.225 liter - 975 liter 325 ml
- Intended difficulty `classify/Easy`: Soal ini memerlukan satu keputusan utama yaitu melakukan peminjaman satuan (konversi 1 liter menjadi 1.000 ml) untuk melakukan pengurangan. Prosedur ini rutin bagi siswa SMP.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan volume (1 liter = 1.000 ml) dan operasi pengurangan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dengan konversi satuan adalah materi dasar yang sudah dikuasai sebelum kelas 9, namun tetap relevan sebagai soal pemanasan atau aplikasi dasar. |

Run 2 — solusi: 2.225 liter = 2.224 liter 1.000 ml. Pengurangan: (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan konversi satuan volume (liter ke ml) yang merupakan prosedur rutin dalam pengukuran.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan pada besaran yang memiliki satuan campuran (liter dan mililiter).. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi pengurangan standar dengan satu kali proses meminjam (regrouping) satuan, yang merupakan prosedur rutin bagi siswa kelas 9.. Bukti: 2.225 liter; 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan volume (1 liter = 1.000 ml) dan operasi pengurangan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dengan konversi satuan adalah keterampilan dasar yang sudah dikuasai sebelum kelas 9, sehingga tingkat kesulitannya rendah. |

Run 3 — solusi: 2.225 liter = 2.224 liter 1.000 ml. Sisa air = (2.224 liter 1.000 ml) - (975 liter 325 ml) = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan konversi satuan volume (liter ke ml) untuk menyelesaikan masalah rutin ini.. Bukti: 2.225 liter - 975 liter 325 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan pada satuan ukuran yang berbeda (liter dan mililiter).. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi pengurangan standar dengan satu langkah konversi satuan (meminjam 1 liter menjadi 1.000 ml). Ini adalah prosedur rutin bagi siswa kelas 9.. Bukti: 2.225 liter; 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan volume (1 liter = 1.000 ml) dan pengurangan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi ini dasar, soal ini menguji ketelitian dalam operasi satuan yang merupakan prasyarat penting untuk topik pengukuran volume di kelas 9. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pengukuran Volume
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?
Pilihan: A. 1.250 liter 325 ml
B. 1.249 liter 675 ml
C. 1.249 liter 325 ml
D. 1.250 liter 675 ml
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `0d61de45054218c7d9af6710`

Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang. Bantulah beliau membuat gambar kerangka tersebut.<br><br>Manakah yang menghasilkan kerangka yang terluas?

| Opsi | Isi |
|---|---|
| A | Panjang 15 cm dan lebar 15 cm (luas 225 cm²) |
| B | Panjang 25 cm dan lebar 5 cm (luas 125 cm²) |
| C | Panjang 20 cm dan lebar 10 cm (luas 200 cm²) |
| D | Panjang 18 cm dan lebar 12 cm (luas 216 cm²) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Keliling = 2(p + l) = 60 cm, maka p + l = 30 cm. Luas L = p * l = p(30 - p) = 30p - p². Fungsi kuadrat ini mencapai maksimum saat p = -b/(2a) = -30/(2 * -1) = 15 cm. Jika p = 15 cm, maka l = 30 - 15 = 15 cm. Luas maksimum = 15 * 15 = 225 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5cdaaac15344fe81f52088a25aeeec54b936c7fbdf251e389f86c16b39349724`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2131 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3030 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2129 |

Run 1 — solusi: Keliling persegi panjang adalah 2(p + l) = 60 cm, sehingga p + l = 30 cm. Luas L = p * l = p(30 - p) = 30p - p². Fungsi kuadrat ini mencapai maksimum saat p = -b/(2a) = -30/(2*-1) = 15 cm. Jika p = 15, maka l = 30 - 15 = 15 cm. Luas maksimum = 15 * 15 = 225 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan keliling dan luas untuk mengoptimalkan nilai luas. Ini melibatkan pemilihan prosedur (mencari nilai maksimum fungsi luas) yang merupakan penerapan konsep pada situasi rutin.. Bukti: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang.; Manakah yang menghasilkan kerangka yang terluas?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip hubungan antara keliling dan luas (konsep) untuk menentukan dimensi yang menghasilkan luas maksimum.. Bukti: Manakah yang menghasilkan kerangka yang terluas?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa memahami bahwa untuk keliling tetap, persegi adalah persegi panjang dengan luas terbesar. Ini adalah prosedur yang cukup familiar di kelas 9.. Bukti: Bapak memiliki kawat sepanjang 60 cm.; Manakah yang menghasilkan kerangka yang terluas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar keliling dan luas persegi panjang serta konsep optimasi sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi optimasi luas dengan keliling tetap adalah standar untuk kelas 9, namun prosedurnya cukup langsung (mencari pasangan bilangan dengan jumlah tetap yang hasil kalinya terbesar). |

Run 2 — solusi: Keliling = 2(p+l) = 60, maka p+l = 30. Luas = p * l = p(30-p). Fungsi luas L(p) = -p^2 + 30p mencapai maksimum saat p = -b/(2a) = -30/(2*-1) = 15. Jadi, p=15 dan l=15 (persegi). Luas = 15 * 15 = 225 cm^2.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara keliling dan luas persegi panjang, serta mengidentifikasi bahwa persegi adalah kasus khusus persegi panjang yang memaksimalkan luas untuk keliling tertentu.. Bukti: Manakah yang menghasilkan kerangka yang terluas?; Panjang 15 cm dan lebar 15 cm
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara keliling dan luas bangun datar (persegi panjang).. Bukti: Bapak memiliki kawat sepanjang 60 cm; membuat kerangka berbentuk persegi panjang
- Intended difficulty `classify/Medium`: Soal ini meminta siswa membandingkan beberapa kemungkinan atau memahami prinsip optimasi dasar. Meskipun bisa diselesaikan dengan mencoba angka, ini adalah prosedur rutin dalam konteks hubungan keliling-luas di kelas 9.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Manakah yang menghasilkan kerangka yang terluas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep keliling dan luas persegi panjang, serta pemahaman bahwa persegi adalah persegi panjang. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami hubungan optimasi sederhana antara keliling dan luas. Soal ini menuntut pemilihan prosedur (uji coba atau pemahaman sifat persegi) untuk menentukan luas maksimum. |

Run 3 — solusi: Keliling persegi panjang adalah 2(p + l) = 60 cm, sehingga p + l = 30 cm. Luas (L) = p * l = p(30 - p) = 30p - p². Fungsi kuadrat ini mencapai maksimum saat p = -b/(2a) = -30/(2 * -1) = 15 cm. Jika p = 15 cm, maka l = 30 - 15 = 15 cm. Luas maksimum = 15 * 15 = 225 cm².
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep keliling dan luas untuk mengoptimalkan nilai luas, yang merupakan proses penalaran (reasoning) untuk menemukan hubungan antara dimensi dan luas maksimum.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Manakah yang menghasilkan kerangka yang terluas?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara keliling tetap dan luas maksimum pada persegi panjang.. Bukti: Manakah yang menghasilkan kerangka yang terluas?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa perlu memahami hubungan antara keliling dan luas, serta menyadari bahwa persegi adalah kasus khusus dari persegi panjang yang memberikan luas maksimum untuk keliling tertentu.. Bukti: Bapak memiliki kawat sepanjang 60 cm; Manakah yang menghasilkan kerangka yang terluas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep keliling dan luas persegi panjang, serta pemahaman dasar tentang optimasi. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menganalisis hubungan antara dimensi dan luas, serta memahami sifat persegi sebagai persegi panjang dengan luas maksimum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "reasoning": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3846`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep hubungan keliling dan luas untuk mengoptimalkan nilai luas. Ini melibatkan pemilihan prosedur (membandingkan nilai atau menggunakan sifat fungsi kuadrat) yang merupakan penerapan konsep pada situasi rutin.
- Dimensi pengetahuan `conceptual`: Siswa menggunakan prinsip hubungan antara keliling dan luas (konsep) untuk menentukan dimensi yang menghasilkan luas maksimum.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa perlu memahami hubungan antara keliling dan luas, serta menyadari bahwa persegi adalah kasus khusus dari persegi panjang yang memberikan luas maksimum untuk keliling tertentu. Ini menuntut pemilihan prosedur yang tepat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep keliling dan luas persegi panjang, serta pemahaman bahwa persegi adalah persegi panjang. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami hubungan optimasi sederhana antara keliling dan luas. Soal ini menuntut pemilihan prosedur (uji coba atau pemahaman sifat persegi) untuk menentukan luas maksimum. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Hubungan Keliling dan Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang. Bantulah beliau membuat gambar kerangka tersebut.

Manakah yang menghasilkan kerangka yang terluas?
Pilihan: A. Panjang 15 cm dan lebar 15 cm (luas 225 cm²)
B. Panjang 25 cm dan lebar 5 cm (luas 125 cm²)
C. Panjang 20 cm dan lebar 10 cm (luas 200 cm²)
D. Panjang 18 cm dan lebar 12 cm (luas 216 cm²)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `e81a665e38e1781b745677fd`

Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.<br><br>Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

| Opsi | Isi |
|---|---|
| A | 2 kali |
| B | 4 kali |
| C | 5 kali |
| D | 3 kali |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Posisi awal (F,1) ke posisi tujuan (D,2). Perubahan posisi horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Perubahan posisi vertikal dari 1 ke 2 adalah 1 langkah. Total langkah rebahan = 2 + 1 = 3 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3c5358fb52695b1b5854401e20e9719c36258b1f446210c0466249c2dfabbb56`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2073 |
| 2 | success | valid / verified | applying | procedural | Easy | 2055 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2137 |

Run 1 — solusi: Posisi awal (F, 1) ke posisi akhir (D, 2). Perubahan posisi horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Perubahan posisi vertikal dari 1 ke 2 adalah 1 langkah. Total langkah rebahan = 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada sistem koordinat petak dan menerjemahkan jarak antar titik menjadi jumlah langkah rebahan (translasi diskrit). Ini adalah penerapan prosedur rutin dalam situasi spasial.. Bukti: kubus terletak pada (F,1) dan akan dipindahkan ke (D,2); tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang sistem koordinat dan prinsip dasar pergerakan objek pada grid untuk menentukan jumlah langkah.. Bukti: jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak
- Intended difficulty `classify/Easy`: Soal ini melibatkan perhitungan langkah sederhana pada grid (2D). Siswa hanya perlu menghitung selisih koordinat (Manhattan distance). Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 9, hanya memerlukan pemahaman jarak pada grid yang biasanya sudah dikuasai di jenjang lebih rendah. |

Run 2 — solusi: Posisi awal (F,1) ke posisi tujuan (D,2). Perubahan posisi horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Perubahan posisi vertikal dari 1 ke 2 adalah 1 langkah. Total langkah rebahan adalah 2 + 1 = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada sistem koordinat petak dan menerjemahkan jarak antar titik menjadi jumlah langkah rebahan kubus. Ini adalah penerapan konsep dasar lokasi/gerak.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip pergerakan objek pada grid (konseptual) untuk menentukan jumlah langkah (prosedural).. Bukti: Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya.
- Intended difficulty `classify/Easy`: Soal ini melibatkan pemahaman dasar tentang pergerakan pada grid. Langkah-langkahnya rutin dan langsung, tidak memerlukan strategi kompleks.. Bukti: jarak dari F ke D adalah 2 langkah dan dari 1 ke 2 adalah 1 langkah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 9, hanya memerlukan perhitungan jarak sederhana pada grid. |

Run 3 — solusi: Posisi awal (F,1) ke posisi akhir (D,2). Perubahan posisi horizontal dari F ke D adalah 2 langkah (F ke E, E ke D). Perubahan posisi vertikal dari 1 ke 2 adalah 1 langkah. Total rebahan = 2 (horizontal) + 1 (vertikal) = 3 kali.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep pergerakan pada bidang koordinat/petak dan menerjemahkan jarak antar titik menjadi jumlah langkah (rebahan) yang diperlukan. Ini adalah penerapan konsep dasar lokasi/gerak.. Bukti: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2).; Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara jarak pada sistem koordinat petak dengan operasi fisik (rebahan kubus) yang setara dengan satu satuan jarak.. Bukti: Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya.; Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal
- Intended difficulty `classify/Easy`: Soal ini melibatkan perhitungan jarak sederhana pada sistem grid (Manhattan distance). Siswa hanya perlu menghitung selisih koordinat x dan y. Prosedurnya rutin dan langsung.. Bukti: jarak dari F ke D adalah 2 langkah dan dari 1 ke 2 adalah 1 langkah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lokasi/gerak pada petak adalah materi dasar yang sangat familiar bagi siswa SMP. Perhitungan jarak Manhattan sederhana ini tidak memerlukan strategi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3631`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep pergerakan pada sistem koordinat petak (jarak Manhattan) untuk menentukan jumlah langkah rebahan. Ini adalah penerapan prosedur rutin dalam situasi spasial.
- Dimensi pengetahuan `conceptual`: Siswa menggunakan pemahaman konseptual tentang hubungan antara jarak pada sistem koordinat petak dengan operasi fisik (rebahan kubus) yang setara dengan satu satuan jarak.
- Intended difficulty `Easy`: Soal ini melibatkan perhitungan jarak Manhattan sederhana pada grid. Prosedurnya rutin, langsung, dan tidak memerlukan strategi non-rutin atau integrasi kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem koordinat kartesius atau grid. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi lokasi/gerak pada petak adalah materi dasar yang sangat familiar bagi siswa SMP. Perhitungan jarak Manhattan sederhana ini tidak memerlukan strategi kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lokasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.

Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
Pilihan: A. 2 kali
B. 4 kali
C. 5 kali
D. 3 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `bba0d92faac1dbb90cd622ef`

Diketahui segitiga ABC dengan A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1). Tentukan translasinya serta koordinat titik B' dan C'.

| Opsi | Isi |
|---|---|
| A | Translasi $\binom{2}{-4}$, B'(4,-2), C'(6,1) |
| B | Translasi $\binom{-2}{4}$, B'(0,6), C'(2,9) |
| C | Translasi $\binom{4}{-2}$, B'(6,0), C'(8,3) |
| D | Translasi $\binom{-2}{4}$, B'(4,-2), C'(6,1) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Vektor translasi T = A' - A = (-2 - 0, 1 - (-3)) = (-2, 4). Maka B' = B + T = (2 + (-2), 2 + 4) = (0, 6) dan C' = C + T = (4 + (-2), 5 + 4) = (2, 9).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c1a0aaba3bb93f1baa1e94c518a6cbc33313e2833633396601ffbf97b4bc1981`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2109 |
| 2 | success | valid / verified | applying | procedural | Easy | 2157 |
| 3 | success | valid / verified | applying | procedural | Medium | 2154 |

Run 1 — solusi: Vektor translasi T = A' - A = (-2 - 0, 1 - (-3)) = (-2, 4). Maka B' = B + T = (2 + (-2), 2 + 4) = (0, 6) dan C' = C + T = (4 + (-2), 5 + 4) = (2, 9).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep translasi (penjumlahan vektor) untuk menemukan vektor pergeseran dari titik asal ke bayangan, kemudian menerapkannya pada titik lain. Ini adalah prosedur standar dalam geometri transformasi.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1); Tentukan translasinya serta koordinat titik B' dan C'
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana melakukan operasi translasi pada koordinat kartesius.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya melibatkan operasi penjumlahan koordinat sederhana berdasarkan vektor translasi yang ditentukan dari satu titik yang diketahui.. Bukti: A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan bilangan bulat dan konsep dasar koordinat kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan sudah lancar melakukan operasi translasi dasar pada bidang koordinat tanpa kesulitan berarti. |

Run 2 — solusi: Vektor translasi T = A' - A = (-2 - 0, 1 - (-3)) = (-2, 4). Maka B' = B + T = (2 + (-2), 2 + 4) = (0, 6) dan C' = C + T = (4 + (-2), 5 + 4) = (2, 9).
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep translasi sebagai penambahan vektor pada koordinat titik asal. Proses ini melibatkan penerapan prosedur standar translasi pada titik-titik yang diberikan.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1); Tentukan translasinya serta koordinat titik B' dan C'
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana melakukan operasi translasi pada koordinat kartesius.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan rumus translasi (x', y') = (x+a, y+b) secara langsung. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat kartesius dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi adalah materi standar kelas 9. Soal ini menggunakan prosedur langsung yang umum diajarkan di kelas. |

Run 3 — solusi: Vektor translasi T = A' - A = (-2 - 0, 1 - (-3)) = (-2, 4). Maka B' = B + T = (2 + (-2), 2 + 4) = (0, 6) dan C' = C + T = (4 + (-2), 5 + 4) = (2, 9).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur translasi titik dengan menentukan vektor pergeseran terlebih dahulu, kemudian menerapkannya pada titik lain. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1); Tentukan translasinya serta koordinat titik B' dan C'
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma translasi (penjumlahan vektor) dan bagaimana menerapkannya secara konsisten pada koordinat titik.. Bukti: ditranslasikan sehingga bayangannya adalah A'(-2,1); Tentukan translasinya serta koordinat titik B' dan C'
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah rutin: menentukan vektor translasi dan menerapkannya pada dua titik lainnya. Prosedurnya familiar bagi siswa kelas 9.. Bukti: Diketahui segitiga ABC dengan A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, konsep koordinat kartesius, dan definisi translasi titik. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi adalah materi standar kelas 9. Soal ini menguji pemahaman dasar tanpa kompleksitas tambahan seperti komposisi transformasi atau variabel yang tidak diketahui. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3736`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur standar translasi (penjumlahan vektor) untuk menentukan vektor pergeseran dari titik yang diketahui, kemudian menerapkannya pada titik-titik lain. Ini adalah penerapan konsep rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang algoritma translasi pada koordinat kartesius.
- Intended difficulty `Easy`: Soal ini bersifat rutin karena hanya memerlukan dua langkah langsung: menentukan vektor translasi dan menerapkannya pada titik lain. Tidak ada strategi non-rutin atau kendala kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, konsep koordinat kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi adalah materi standar kelas 9. Soal ini menggunakan prosedur langsung yang umum diajarkan di kelas tanpa variasi yang menyulitkan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Translasi (Pergeseran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui segitiga ABC dengan A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1). Tentukan translasinya serta koordinat titik B' dan C'.
Pilihan: A. Translasi $\binom{2}{-4}$, B'(4,-2), C'(6,1)
B. Translasi $\binom{-2}{4}$, B'(0,6), C'(2,9)
C. Translasi $\binom{4}{-2}$, B'(6,0), C'(8,3)
D. Translasi $\binom{-2}{4}$, B'(4,-2), C'(6,1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `944be36e182518ad72be95aa`

Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah …

| Opsi | Isi |
|---|---|
| A | A'(-6,8) |
| B | A'(-6,-8) |
| C | A'(2,2) |
| D | A'(-2,8) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Translasi titik A(x, y) oleh vektor (a, b) menghasilkan A'(x+a, y+b). Untuk A(-2, 5) dan vektor (-4, 3), maka A' = (-2 + (-4), 5 + 3) = (-6, 8).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `093dd9869fbac278288ebbdd705572d07cf214a801ba9f3ea11ed804b4fcc8e3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1966 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1955 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1983 |

Run 1 — solusi: Translasi titik A(x, y) oleh vektor (a, b) menghasilkan A'(x+a, y+b). Untuk A(-2, 5) dan vektor (-4, 3), maka A' = (-2 + (-4), 5 + 3) = (-6, 8).
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus translasi titik. Siswa hanya perlu melakukan operasi penjumlahan sederhana pada koordinat x dan y sesuai dengan komponen vektor translasi yang diberikan.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana melakukan operasi translasi pada titik koordinat.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan satu langkah operasi penjumlahan bilangan bulat, dan menggunakan representasi yang sangat standar dalam kurikulum SMP.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat dan konsep dasar koordinat Kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi titik adalah materi dasar kelas 9 yang bersifat rutin dan prosedural. |

Run 2 — solusi: Translasi titik (x, y) oleh vektor (a, b) menghasilkan titik (x+a, y+b). Untuk titik A(-2, 5) dan vektor (-4, 3), bayangannya adalah A'(-2 + (-4), 5 + 3) = A'(-6, 8).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi translasi titik pada koordinat Kartesius. Siswa hanya perlu menjumlahkan koordinat titik asal dengan komponen vektor translasi.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang algoritma penjumlahan vektor translasi terhadap koordinat titik.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu langkah operasi penjumlahan bilangan bulat pada koordinat.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat dan konsep dasar koordinat Kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi titik adalah materi dasar kelas 9 yang bersifat prosedural dan rutin. |

Run 3 — solusi: Translasi titik A(x, y) oleh vektor (a, b) menghasilkan A'(x+a, y+b). Untuk A(-2, 5) dan vektor (-4, 3), maka A' = (-2 + (-4), 5 + 3) = (-6, 8).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi translasi titik pada koordinat Kartesius. Siswa hanya perlu melakukan operasi penjumlahan sederhana pada komponen x dan y, yang merupakan proses rutin.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana vektor translasi memengaruhi koordinat titik, yaitu dengan menjumlahkan komponen yang bersesuaian.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$
- Intended difficulty `classify/Easy`: Soal ini sangat langsung (one-step problem). Siswa hanya perlu menerapkan rumus translasi dasar tanpa ada kendala tambahan atau langkah perantara yang kompleks.. Bukti: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat Kartesius dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi titik adalah materi dasar kelas 9. Soal ini tidak memerlukan pemahaman mendalam atau strategi khusus, sehingga dikategorikan mudah. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Translasi (Pergeseran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah …
Pilihan: A. A'(-6,8)
B. A'(-6,-8)
C. A'(2,2)
D. A'(-2,8)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `34e4b41c04e7c9417acca5ce`

Titik (2,-3) direfleksikan terhadap garis y=x. Tentukan bayangannya.

| Opsi | Isi |
|---|---|
| A | (2,3) |
| B | (-3,2) |
| C | (3,-2) |
| D | (2,1) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), maka x = 2 dan y = -3. Bayangannya adalah (-3, 2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0f10b439d90a060fe21813269de924c758c5af5af8ca84f20eb36e3e3558e217`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1951 |
| 2 | success | valid / verified | applying | procedural | Easy | 1924 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1962 |

Run 1 — solusi: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), maka x = 2 dan y = -3. Bayangannya adalah (-3, 2).
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung dari aturan transformasi geometri (refleksi) yang sudah dipelajari di kelas 9. Siswa hanya perlu mengingat atau menerapkan rumus refleksi terhadap garis y=x.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui aturan atau prosedur spesifik untuk melakukan refleksi terhadap garis y=x, yang merupakan bagian dari pengetahuan prosedural dalam transformasi geometri.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Tidak ada langkah tambahan atau strategi kompleks yang diperlukan. Siswa hanya perlu menerapkan aturan (x, y) -> (y, x).. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat kartesius dan konsep transformasi geometri (refleksi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah soal standar kelas 9 yang menguji ingatan siswa terhadap aturan transformasi dasar tanpa modifikasi atau konteks yang rumit. |

Run 2 — solusi: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), maka x = 2 dan y = -3. Bayangannya adalah (-3, 2).
- Domain kognitif `classify/applying`: Soal ini meminta penerapan langsung dari aturan transformasi geometri (refleksi terhadap garis y=x) yang merupakan prosedur standar dalam kurikulum kelas 9.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menerapkan algoritma atau aturan transformasi (x, y) -> (y, x) untuk menyelesaikan masalah.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan penerapan satu aturan transformasi tanpa langkah tambahan atau analisis kompleks.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan aturan dasar transformasi geometri (refleksi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Refleksi terhadap garis y=x adalah materi dasar transformasi di kelas 9 yang diajarkan sebagai prosedur rutin. |

Run 3 — solusi: Refleksi titik (x, y) terhadap garis y = x menghasilkan bayangan (y, x). Untuk titik (2, -3), maka x = 2 dan y = -3. Bayangannya adalah (-3, 2).
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung dari aturan transformasi geometri (refleksi) yang merupakan prosedur standar dalam kurikulum kelas 9. Siswa hanya perlu mengingat atau menerapkan rumus (x, y) -> (y, x).. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan transformasi geometri, yaitu algoritma untuk menentukan bayangan titik melalui refleksi pada garis y=x.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (one-step) dan menggunakan aturan yang sangat familiar dalam materi transformasi geometri kelas 9. Tidak ada langkah tambahan atau kompleksitas yang diperlukan.. Bukti: Titik (2,-3) direfleksikan terhadap garis y=x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat kartesius dan aturan transformasi refleksi terhadap garis y=x. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Refleksi adalah materi standar kelas 9. Soal ini adalah aplikasi langsung dari rumus tanpa modifikasi, sehingga dikategorikan mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3348`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung dari aturan transformasi geometri (refleksi) yang sudah dipelajari di kelas 9. Siswa hanya perlu mengingat atau menerapkan rumus refleksi terhadap garis y=x.
- Dimensi pengetahuan `procedural`: Siswa perlu mengetahui aturan atau prosedur spesifik untuk melakukan refleksi terhadap garis y=x, yang merupakan bagian dari pengetahuan prosedural dalam transformasi geometri.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Tidak ada langkah tambahan atau strategi kompleks yang diperlukan. Siswa hanya perlu menerapkan aturan (x, y) -> (y, x).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat kartesius dan konsep transformasi geometri (refleksi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah soal standar kelas 9 yang menguji ingatan siswa terhadap aturan transformasi dasar tanpa modifikasi atau konteks yang rumit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Refleksi (Pencerminan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik (2,-3) direfleksikan terhadap garis y=x. Tentukan bayangannya.
Pilihan: A. (2,3)
B. (-3,2)
C. (3,-2)
D. (2,1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `e23d76dc5ff2cda98f0f4ccc`

Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.

| Opsi | Isi |
|---|---|
| A | (2,3) |
| B | (-2,3) |
| C | (-2,-3) |
| D | (4,-3) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Refleksi titik (x, y) terhadap sumbu x menghasilkan bayangan (x, -y). Untuk titik (2, -3), maka x=2 dan y=-3. Bayangannya adalah (2, -(-3)) = (2, 3).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6951e591c8048e5122a7ee1a4013112eccdefb9c4c6f5831e9a4da3a876535fb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1946 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1924 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2742 |

Run 1 — solusi: Refleksi titik (x, y) terhadap sumbu x menghasilkan bayangan (x, -y). Untuk titik (2, -3), maka x=2 dan y=-3. Bayangannya adalah (2, -(-3)) = (2, 3).
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus atau prosedur standar refleksi terhadap sumbu x. Siswa hanya perlu mengingat atau menerapkan aturan (x, y) -> (x, -y) tanpa perlu strategi kompleks.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan transformasi geometri (refleksi) yang merupakan algoritma standar.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (one-step) dengan prosedur yang familiar bagi siswa kelas 9. Tidak ada kendala atau langkah tambahan yang diperlukan.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat Kartesius dan aturan refleksi terhadap sumbu x. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Refleksi adalah materi dasar kelas 9. Soal ini hanya menuntut penerapan rumus langsung tanpa modifikasi atau analisis lebih lanjut. |

Run 2 — solusi: Refleksi titik (x, y) terhadap sumbu x menghasilkan bayangan (x, -y). Untuk titik (2, -3), bayangannya adalah (2, -(-3)) = (2, 3).
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung dari aturan transformasi geometri (refleksi terhadap sumbu x) yang merupakan prosedur standar dan rutin bagi siswa kelas 9.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui aturan atau rumus transformasi (prosedural) untuk melakukan refleksi titik pada bidang Kartesius.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung, hanya memerlukan penerapan satu aturan transformasi tanpa langkah tambahan atau kompleksitas.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat Kartesius dan konsep refleksi terhadap sumbu x. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Refleksi adalah materi standar kelas 9. Soal ini adalah latihan dasar yang tidak memerlukan pemikiran tingkat tinggi. |

Run 3 — solusi: Refleksi titik (x, y) terhadap sumbu x menghasilkan bayangan (x, -y). Untuk titik (2, -3), bayangannya adalah (2, -(-3)) = (2, 3). Jawaban: A.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta penerapan langsung rumus refleksi terhadap sumbu x, yaitu (x, y) -> (x, -y), tanpa memerlukan strategi atau analisis tambahan.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x
- Dimensi pengetahuan `classify/procedural`: Siswa perlu mengetahui dan menerapkan algoritma atau aturan transformasi geometri (refleksi) yang spesifik.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu langkah penerapan rumus refleksi tanpa kendala atau kompleksitas tambahan.. Bukti: Titik (2,-3) direfleksikan terhadap sumbu x

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat kartesius dan aturan refleksi terhadap sumbu x. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 9 yang menguji ingatan langsung terhadap rumus transformasi geometri dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Refleksi (Pencerminan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.
Pilihan: A. (2,3)
B. (-2,3)
C. (-2,-3)
D. (4,-3)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `078d6a87b40b143dc0e0683c`

Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0). Gambarkan segi empat KLMN beserta bayangannya pada bidang koordinat.

| Opsi | Isi |
|---|---|
| A | K'(-1,-2), L'(-6,-4), M'(-8,3), N'(-3,1) |
| B | K'(-2,1), L'(-4,6), M'(3,8), N'(1,3) |
| C | K'(1,-2), L'(6,-4), M'(8,3), N'(3,1) |
| D | K'(-1,2), L'(-6,4), M'(-8,-3), N'(-3,-1) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rotasi 180° terhadap titik pusat O(0,0) memiliki aturan transformasi (x,y) -> (-x,-y). Menerapkan aturan ini pada titik-titik: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), dan N(3,-1) -> N'(-3,1). Hasil ini sesuai dengan pilihan A.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6d0579d7e6f2e4cc03a0df25fce149f87cfcb6852a881c93578e9904494a090c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2206 |
| 2 | success | valid / verified | applying | procedural | Easy | 2195 |
| 3 | success | valid / verified | applying | procedural | Easy | 2177 |

Run 1 — solusi: Rotasi 180° terhadap titik pusat O(0,0) memiliki aturan transformasi (x,y) -> (-x,-y). Menerapkan aturan ini pada titik-titik: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), dan N(3,-1) -> N'(-3,1). Hasil ini sesuai dengan pilihan A.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan transformasi geometri yang spesifik (rotasi 180 derajat) pada koordinat titik yang diberikan. Ini adalah penerapan prosedur standar.. Bukti: Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang aturan transformasi geometri (rotasi) yang merupakan bagian dari pengetahuan prosedural dalam koordinat Kartesius.. Bukti: rotasi 180º terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan rumus transformasi (x,y) -> (-x,-y) secara langsung pada empat titik yang diberikan. Tidak ada kendala kompleks atau strategi nonrutin.. Bukti: K(1,2), L(6,4), M(8,-3) dan N(3,-1); rotasi 180º terhadap titik pusat O(0,0)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat Kartesius dan aturan rotasi 180 derajat terhadap titik asal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah materi dasar transformasi geometri kelas 9 yang prosedurnya sangat langsung dan familiar bagi siswa. |

Run 2 — solusi: Rotasi 180 derajat terhadap titik pusat O(0,0) memiliki aturan pemetaan (x, y) -> (-x, -y). Menerapkan aturan ini pada titik-titik sudut: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), dan N(3,-1) -> N'(-3,1). Hasil ini sesuai dengan opsi A.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur transformasi geometri yang spesifik (rotasi 180 derajat) pada koordinat titik yang diberikan. Ini adalah penerapan prosedur rutin yang sudah dipelajari di kelas 9.. Bukti: Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau aturan transformasi koordinat (prosedural) yang merupakan bagian dari konsep geometri transformasi.. Bukti: rotasi 180º terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan rumus transformasi (x,y) -> (-x,-y) secara langsung pada empat titik. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat Kartesius dan aturan rotasi 180 derajat terhadap titik asal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah materi standar kelas 9 yang prosedurnya sangat langsung dan familiar bagi siswa. |

Run 3 — solusi: Rotasi 180 derajat terhadap titik pusat (0,0) memiliki aturan transformasi (x, y) -> (-x, -y). Menerapkan aturan ini pada setiap titik: K(1,2) -> K'(-1,-2), L(6,4) -> L'(-6,-4), M(8,-3) -> M'(-8,3), dan N(3,-1) -> N'(-3,1). Hasil ini sesuai dengan pilihan A.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus transformasi geometri yang spesifik (rotasi 180 derajat) pada koordinat titik yang diberikan. Ini adalah penerapan prosedur standar yang sudah dipelajari di kelas 9.. Bukti: Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang aturan transformasi geometri (rotasi) yang merupakan bagian dari pengetahuan prosedural dalam matematika.. Bukti: rotasi 180º terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan rumus transformasi (x,y) -> (-x,-y) secara langsung pada empat titik yang diberikan. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: K(1,2), L(6,4), M(8,-3) dan N(3,-1); rotasi 180º terhadap titik pusat O(0,0)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koordinat Kartesius dan aturan transformasi geometri (rotasi 180 derajat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri (rotasi) adalah kurikulum standar kelas 9. Soal ini adalah latihan langsung tanpa modifikasi atau integrasi konsep yang rumit. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Rotasi (Perputaran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0). Gambarkan segi empat KLMN beserta bayangannya pada bidang koordinat.
Pilihan: A. K'(-1,-2), L'(-6,-4), M'(-8,3), N'(-3,1)
B. K'(-2,1), L'(-4,6), M'(3,8), N'(1,3)
C. K'(1,-2), L'(6,-4), M'(8,3), N'(3,1)
D. K'(-1,2), L'(-6,4), M'(-8,-3), N'(-3,-1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `5cdb075f3e6376933323750c`

A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).

| Opsi | Isi |
|---|---|
| A | A'(-2,5), B'(-5,8), C'(-1,2) |
| B | A'(2,-5), B'(5,-8), C'(1,-2) |
| C | A'(-5,2), B'(-8,5), C'(-2,1) |
| D | A'(-5,-2), B'(-8,-5), C'(-2,-1) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Rotasi 90º berlawanan arah jarum jam terhadap pusat (0,0) menggunakan aturan (x, y) -> (-y, x). Maka: A(5,2) -> A'(-2,5), B(8,5) -> B'(-5,8), C(2,1) -> C'(-1,2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `470a910caa8efb8a33617b405f2356c8be77e0637b06be45ad3c39063c2fd1a0`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2826 |
| 2 | success | valid / verified | applying | procedural | Easy | 2860 |
| 3 | success | valid / verified | applying | procedural | Easy | 2809 |

Run 1 — solusi: Rotasi 90º berlawanan arah jarum jam terhadap pusat (0,0) menggunakan aturan (x, y) -> (-y, x). Maka: A(5,2) -> A'(-2,5), B(8,5) -> B'(-5,8), C(2,1) -> C'(-1,2).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan transformasi geometri (rotasi) yang spesifik untuk titik pusat (0,0) dan sudut 90 derajat.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma rotasi titik pada bidang Kartesius.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang melibatkan penerapan rumus transformasi geometri standar yang diajarkan di kelas 9.. Bukti: A(5,2), B(8,5), dan C(2,1); rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat Kartesius dan rumus rotasi 90 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi titik adalah materi standar kelas 9 yang bersifat prosedural langsung. |

Run 2 — solusi: Rotasi 90º berlawanan arah jarum jam terhadap titik pusat O(0,0) menggunakan aturan (x,y) -> (-y,x). Titik A(5,2) menjadi A'(-2,5), B(8,5) menjadi B'(-5,8), dan C(2,1) menjadi C'(-1,2).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus transformasi geometri rotasi yang sudah dipelajari untuk menentukan koordinat bayangan.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur transformasi geometri (rotasi) yang merupakan bagian dari pengetahuan prosedural.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan rumus transformasi geometri yang standar untuk titik-titik yang diberikan.. Bukti: A(5,2), B(8,5), dan C(2,1); rotasi sebesar 90º berlawanan arah jarum jam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan rumus rotasi 90 derajat berlawanan arah jarum jam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi rotasi adalah materi standar kelas 9. Soal ini langsung menguji penerapan rumus tanpa modifikasi atau integrasi konsep yang kompleks. |

Run 3 — solusi: Rotasi 90º berlawanan arah jarum jam terhadap pusat (0,0) menggunakan aturan transformasi (x, y) -> (-y, x). Menerapkan aturan ini pada titik-titik: A(5,2) -> A'(-2,5), B(8,5) -> B'(-5,8), dan C(2,1) -> C'(-1,2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus transformasi rotasi 90 derajat berlawanan arah jarum jam secara langsung pada koordinat titik yang diberikan. Ini adalah proses penerapan prosedur yang sudah dipelajari.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0); A(5,2), B(8,5), dan C(2,1)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau aturan transformasi geometri (rotasi) yang spesifik.. Bukti: rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan penerapan satu rumus transformasi pada titik-titik yang diberikan tanpa kendala tambahan.. Bukti: A(5,2), B(8,5), dan C(2,1); rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan rumus rotasi 90 derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar transformasi geometri kelas 9 yang tidak memerlukan strategi nonrutin atau integrasi konsep yang kompleks. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Rotasi (Perputaran)
Tipe soal: multiple_choice
Stimulus: -
Soal: A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).
Pilihan: A. A'(-2,5), B'(-5,8), C'(-1,2)
B. A'(2,-5), B'(5,-8), C'(1,-2)
C. A'(-5,2), B'(-8,5), C'(-2,1)
D. A'(-5,-2), B'(-8,-5), C'(-2,-1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `f6516e65a41da50ae0f6a8b9`

Jika ΔMDN ≅ ΔKPG, maka MN = _____.

| Opsi | Isi |
|---|---|
| A | KP |
| B | KG |
| C | PG |
| D | DN |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Dua segitiga kongruen ΔMDN ≅ ΔKPG berarti titik-titik yang bersesuaian adalah M dengan K, D dengan P, dan N dengan G. Sisi MN menghubungkan titik pertama (M) dan ketiga (N). Maka, sisi yang bersesuaian pada ΔKPG adalah sisi yang menghubungkan titik pertama (K) dan ketiga (G), yaitu KG.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7adb3b3ccf43d6343d5cfaaa6b52b3f3bd2cc114937bc31224ae9271337d86ea`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2021 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1998 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1985 |

Run 1 — solusi: Dua segitiga kongruen ΔMDN ≅ ΔKPG berarti titik-titik yang bersesuaian adalah M dengan K, D dengan P, dan N dengan G. Sisi MN menghubungkan titik pertama (M) dan ketiga (N). Maka, sisi yang bersesuaian pada ΔKPG adalah sisi yang menghubungkan titik pertama (K) dan ketiga (G), yaitu KG.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali dan menerapkan prinsip korespondensi titik pada dua segitiga yang kongruen untuk menentukan sisi yang bersesuaian. Ini adalah proses langsung dalam mengenali notasi kongruensi.. Bukti: ΔMDN ≅ ΔKPG, maka MN = _____
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap definisi dan notasi kongruensi segitiga, yang merupakan konsep dasar dalam geometri.. Bukti: ΔMDN ≅ ΔKPG
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct) dengan satu langkah pengerjaan yaitu memetakan urutan titik pada notasi kongruensi. Tidak ada manipulasi atau strategi kompleks yang diperlukan.. Bukti: ΔMDN ≅ ΔKPG, maka MN = _____

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi kongruensi segitiga dan korespondensi titik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah materi standar kelas 9. Soal ini menguji pemahaman dasar notasi tanpa variasi atau jebakan yang rumit. |

Run 2 — solusi: Dua segitiga kongruen ΔMDN ≅ ΔKPG berarti titik-titik yang bersesuaian adalah M↔K, D↔P, dan N↔G. Sisi MN menghubungkan titik pertama dan ketiga pada ΔMDN, sehingga sisi yang bersesuaian pada ΔKPG adalah sisi yang menghubungkan titik pertama dan ketiga, yaitu KG.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali korespondensi titik-titik pada notasi kekongruenan segitiga untuk menentukan sisi yang bersesuaian. Ini adalah proses pengenalan fakta dasar tentang notasi geometri.. Bukti: ΔMDN ≅ ΔKPG, maka MN = _____
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap definisi dan notasi kekongruenan segitiga, yang merupakan konsep dasar dalam geometri.. Bukti: ΔMDN ≅ ΔKPG
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan pemahaman notasi dasar tanpa perhitungan atau langkah prosedural yang kompleks.. Bukti: ΔMDN ≅ ΔKPG, maka MN = _____

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi kekongruenan segitiga dan korespondensi titik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah standar kelas 9. Soal ini menguji pemahaman notasi dasar yang diajarkan di awal topik. |

Run 3 — solusi: Notasi ΔMDN ≅ ΔKPG menunjukkan korespondensi titik-titik sudut: M berkorespondensi dengan K, D dengan P, dan N dengan G. Sisi MN menghubungkan titik M dan N, sehingga sisi yang bersesuaian pada ΔKPG adalah sisi yang menghubungkan titik K dan G, yaitu KG.
- Domain kognitif `classify/knowing`: Siswa hanya perlu memahami definisi notasi kekongruenan segitiga dan mengidentifikasi korespondensi titik sudut yang bersesuaian secara langsung.. Bukti: ΔMDN ≅ ΔKPG, maka MN = _____
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan notasi kekongruenan segitiga, yang merupakan konsep dasar dalam geometri.. Bukti: ΔMDN ≅ ΔKPG
- Intended difficulty `classify/Easy`: Soal ini sangat langsung (one-step) dan hanya memerlukan pemahaman notasi dasar tanpa perhitungan atau strategi kompleks.. Bukti: ΔMDN ≅ ΔKPG, maka MN = _____

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman notasi kekongruenan segitiga dan korespondensi titik sudut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah materi standar kelas 9. Soal ini adalah bentuk paling dasar dari pengenalan notasi kekongruenan. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kekongruenan
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika ΔMDN ≅ ΔKPG, maka MN = _____.
Pilihan: A. KP
B. KG
C. PG
D. DN
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `5494cb036f9f5ecded212fcf`

Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen. Pernyataan tersebut merupakan bunyi kriteria _____.

| Opsi | Isi |
|---|---|
| A | S-S-Sd |
| B | Sd-S-Sd |
| C | S-Sd-S |
| D | S-S-S |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Kriteria kekongruenan yang menyatakan dua sisi sama panjang dan sudut yang diapit oleh kedua sisi tersebut sama besar adalah kriteria Sisi-Sudut-Sisi (S-Sd-S).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `875047d7b2c001903b99649c873a17d3ad358320f34874b49662820212c7cdcc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2009 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2422 |
| 3 | success | valid / verified | knowing | factual | Easy | 1982 |

Run 1 — solusi: Kriteria kekongruenan dua segitiga yang menyatakan bahwa dua sisi yang bersesuaian sama panjang dan sudut yang diapit oleh kedua sisi tersebut sama besar disebut kriteria Sisi-Sudut-Sisi (S-Sd-S).
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman definisi atau kriteria dasar kekongruenan segitiga. Siswa hanya perlu mengenali istilah yang tepat untuk kriteria yang diberikan, yang merupakan proses mengingat kembali fakta/definisi.. Bukti: dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman terhadap terminologi dan prinsip dasar dalam geometri (kekongruenan segitiga), yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Pernyataan tersebut merupakan bunyi kriteria
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan hanya menanyakan definisi kriteria kekongruenan yang sudah dipelajari di kelas 9. Tidak ada perhitungan atau strategi kompleks yang diperlukan.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kriteria kekongruenan segitiga (S-Sd-S, Sd-S-Sd, S-S-S). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah kurikulum standar kelas 9. Mengingat definisi kriteria adalah tugas rutin yang sangat mendasar. |

Run 2 — solusi: Kriteria kekongruenan segitiga yang menyatakan dua sisi sama panjang dan sudut yang diapitnya sama besar adalah Sisi-Sudut-Sisi (S-Sd-S).
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali definisi kriteria kekongruenan segitiga (Sisi-Sudut-Sisi). Tidak ada proses analisis atau penerapan prosedur yang kompleks.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual mengenai definisi dan penamaan kriteria kekongruenan segitiga.. Bukti: kriteria _____
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (recall) mengenai definisi geometri dasar yang dipelajari di kelas 9. Tidak memerlukan perhitungan atau strategi pemecahan masalah.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi kriteria kekongruenan segitiga (S-Sd-S, S-S-S, Sd-S-Sd). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah kurikulum standar SMP kelas 9. Soal ini hanya menanyakan definisi dasar tanpa variasi atau aplikasi. |

Run 3 — solusi: Kriteria kekongruenan dua segitiga yang menyatakan dua sisi sama panjang dan sudut yang diapit oleh kedua sisi tersebut sama besar disebut kriteria Sisi-Sudut-Sisi (S-Sd-S).
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman definisi atau kriteria kekongruenan segitiga. Siswa hanya perlu mengenali dan mengingat terminologi kriteria kekongruenan yang sesuai dengan deskripsi yang diberikan.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar
- Dimensi pengetahuan `classify/factual`: Soal ini berkaitan dengan pengetahuan faktual mengenai terminologi dan definisi kriteria kekongruenan segitiga dalam geometri.. Bukti: Pernyataan tersebut merupakan bunyi kriteria _____
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (recall) mengenai definisi kriteria kekongruenan segitiga yang merupakan materi dasar kelas 9. Tidak ada perhitungan atau strategi kompleks yang diperlukan.. Bukti: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kriteria kekongruenan segitiga (S-Sd-S, Sd-S-Sd, S-S-S). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah kurikulum standar kelas 9. Soal ini hanya menanyakan definisi, sehingga tingkat kesulitannya rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3437`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menguji ingatan siswa terhadap definisi kriteria kekongruenan segitiga. Siswa hanya perlu mengenali istilah yang tepat untuk deskripsi yang diberikan, yang merupakan proses kognitif tingkat knowing.
- Dimensi pengetahuan `conceptual`: Soal ini menuntut pengetahuan tentang terminologi dan definisi standar dalam geometri, yang termasuk dalam kategori pengetahuan konseptual.
- Intended difficulty `Easy`: Soal ini bersifat recall langsung terhadap definisi dasar yang dipelajari di kelas 9. Tidak ada perhitungan, strategi, atau analisis kompleks yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi kriteria kekongruenan segitiga (S-Sd-S, S-S-S, Sd-S-Sd). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kekongruenan adalah kurikulum standar SMP kelas 9. Soal ini hanya menanyakan definisi dasar tanpa variasi atau aplikasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kekongruenan
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen. Pernyataan tersebut merupakan bunyi kriteria _____.
Pilihan: A. S-S-Sd
B. Sd-S-Sd
C. S-Sd-S
D. S-S-S
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `907f9e4697523a633ea0ac02`

Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…

| Opsi | Isi |
|---|---|
| A | 180 cm² |
| B | 1.620 cm² |
| C | 540 cm² |
| D | 60 cm² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Luas ΔABC = 0,5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k²=9. Luas ΔA'B'C' = 60 * 9 = 540 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1f4805f51d3207c7dd5e034e176646c59b991b2ec58eef6f2b973be9a7e06018`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2742 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2118 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2135 |

Run 1 — solusi: Luas ΔABC = 0,5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k²=9. Luas ΔA'B'C' = 60 * 9 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan luas pada bangun datar akibat dilatasi (faktor skala k²), bukan sekadar dilatasi panjang sisi.. Bukti: faktor skala 3; luas ΔA'B'C'
- Dimensi pengetahuan `classify/conceptual`: Memahami hubungan antara faktor skala dilatasi dan perubahan luas bangun datar (prinsip konseptual).. Bukti: dilatasi dari ΔABC dengan faktor skala 3; luas ΔA'B'C'
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konsep dilatasi pada luas. Siswa harus menyadari bahwa luas berubah sebesar k², bukan k. Ini adalah langkah rutin bagi siswa yang memahami konsep dilatasi.. Bukti: faktor skala 3; luas ΔA'B'C'

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep luas segitiga dan sifat dilatasi pada luas (k²). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami transformasi geometri. Pengecoh dirancang dengan baik untuk menguji kesalahan umum (mengalikan dengan k atau k³). |

Run 2 — solusi: Luas ΔABC = 0,5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k² = 3² = 9. Maka, luas ΔA'B'C' = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara faktor skala dilatasi (k) dengan perubahan luas bangun datar (k²). Ini adalah penerapan prosedur yang sudah dipelajari.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip geometris bahwa luas bangun hasil dilatasi berubah sebesar kuadrat dari faktor skala, bukan faktor skala itu sendiri.. Bukti: faktor skala 3; luas ΔA'B'C'
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konseptual tentang properti dilatasi pada luas. Meskipun prosedurnya sederhana, siswa sering terjebak menggunakan faktor skala linear (k) alih-alih kuadrat (k²), sehingga ini dikategorikan Medium.. Bukti: faktor skala 3; luas ΔA'B'C'

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas segitiga dan konsep dilatasi pada bangun datar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan memahami transformasi geometri. Pilihan jawaban dirancang untuk menjebak siswa yang tidak memahami hubungan k² pada luas. |

Run 3 — solusi: Luas ΔABC = 0.5 * alas * tinggi = 0.5 * 15 * 8 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas menjadi k² * Luas awal. Luas ΔA'B'C' = 3² * 60 = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perubahan luas pada bangun datar yang didilatasi (k²), bukan sekadar menghitung luas segitiga biasa. Ini melibatkan pemilihan prosedur yang tepat.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman prinsip matematis tentang bagaimana faktor skala dilatasi mempengaruhi luas bangun datar (konsep hubungan antara dilatasi dan luas).. Bukti: hasil dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya menghitung luas segitiga, tetapi harus memahami dan menerapkan prinsip bahwa luas berubah sebesar kuadrat faktor skala (k²). Ini adalah langkah rutin bagi siswa kelas 9 yang telah mempelajari dilatasi, namun memerlukan pemahaman konsep yang lebih dari sekadar operasi langsung.. Bukti: panjang AB=8 cm, BC=15 cm, dan AC=17 cm; faktor skala 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas segitiga dan konsep dilatasi/kesebangunan. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi dilatasi dan perubahan luas adalah standar kurikulum kelas 9. Soal ini menguji pemahaman konseptual tentang faktor skala luas (k²) yang sering menjadi jebakan bagi siswa yang hanya mengalikan dengan k. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Dilatasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…
Pilihan: A. 180 cm²
B. 1.620 cm²
C. 540 cm²
D. 60 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `61e70f2732214f09d97c2039`

Diketahui ΔABC dengan A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap $[O, \frac{1}{2}]$! Gambarkan segitiga tersebut beserta bayangannya pada bidang koordinat!

| Opsi | Isi |
|---|---|
| A | $A'(-\frac{3}{2},-2)$, $B'(3,4)$, $C'(\frac{1}{2},-2)$ |
| B | A'(-2.5,-1.5), B'(6.5,4.5), C'(1.5,-1.5) |
| C | A'(-6,-4), B'(12,8), C'(2,-4) |
| D | $A'(-\frac{3}{2},-1)$, $B'(3,2)$, $C'(\frac{1}{2},-1)$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3 * 1/2, -2 * 1/2) = (-1.5, -1); B' = (6 * 1/2, 4 * 1/2) = (3, 2); C' = (1 * 1/2, -2 * 1/2) = (0.5, -1). Hasil ini sesuai dengan pilihan D.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `482ab0d934c8f2e43f6b598f095318fdee9dd01f3e0ed548e4809c79cce707f2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2232 |
| 2 | success | valid / verified | applying | procedural | Easy | 2252 |
| 3 | success | valid / verified | applying | procedural | Easy | 2252 |

Run 1 — solusi: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3 * 1/2, -2 * 1/2) = (-1.5, -1); B' = (6 * 1/2, 4 * 1/2) = (3, 2); C' = (1 * 1/2, -2 * 1/2) = (0.5, -1). Hasil ini sesuai dengan pilihan D.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus dilatasi [O, k] pada koordinat titik yang diberikan. Ini adalah prosedur standar dalam geometri transformasi.. Bukti: dilatasikan terhadap [O, 1/2]; A(-3,-2), B(6,4) dan C(1,-2)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau prosedur dilatasi pada bidang koordinat.. Bukti: dilatasikan terhadap [O, 1/2]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menerapkan perkalian skalar pada koordinat titik. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: dilatasikan terhadap [O, 1/2]; A(-3,-2), B(6,4) dan C(1,-2)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat kartesius dan operasi perkalian pecahan/desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Dilatasi adalah materi standar kelas 9. Soal ini menguji penerapan langsung rumus tanpa modifikasi atau langkah tambahan yang rumit. |

Run 2 — solusi: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3 * 0.5, -2 * 0.5) = (-1.5, -1); B' = (6 * 0.5, 4 * 0.5) = (3, 2); C' = (1 * 0.5, -2 * 0.5) = (0.5, -1). Hasilnya sesuai dengan opsi D.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur dilatasi dengan pusat O(0,0) dan faktor skala k pada koordinat titik-titik segitiga. Ini adalah penerapan langsung dari rumus dilatasi.. Bukti: dilatasikan terhadap [O, 1/2]; A(-3,-2), B(6,4) dan C(1,-2)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana melakukan transformasi dilatasi pada koordinat kartesius.. Bukti: dilatasikan terhadap [O, 1/2]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan rumus dilatasi [O, k] secara langsung pada tiga titik yang diberikan. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: dilatasikan terhadap [O, 1/2]; A(-3,-2), B(6,4) dan C(1,-2)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan konsep dilatasi dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi adalah standar kurikulum kelas 9. Prosedur perkalian skalar pada koordinat adalah tugas rutin. |

Run 3 — solusi: Dilatasi titik (x, y) terhadap pusat O(0,0) dengan faktor skala k adalah (kx, ky). Untuk k = 1/2: A' = (-3 * 0.5, -2 * 0.5) = (-1.5, -1); B' = (6 * 0.5, 4 * 0.5) = (3, 2); C' = (1 * 0.5, -2 * 0.5) = (0.5, -1). Hasil ini sesuai dengan pilihan D.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur dilatasi dengan pusat O(0,0) dan faktor skala k pada koordinat titik-titik segitiga. Ini adalah penerapan langsung dari rumus dilatasi.. Bukti: dilatasikan terhadap [O, 1/2]; A(-3,-2), B(6,4) dan C(1,-2)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur matematis untuk melakukan transformasi dilatasi pada bidang koordinat.. Bukti: dilatasikan terhadap [O, 1/2]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan rumus dilatasi [O, k] secara langsung pada setiap titik. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: dilatasikan terhadap [O, 1/2]; A(-3,-2), B(6,4) dan C(1,-2)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koordinat kartesius dan konsep dasar transformasi dilatasi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi adalah standar kelas 9. Soal ini adalah latihan dasar yang tidak memerlukan manipulasi aljabar atau visualisasi yang rumit. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Dilatasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui ΔABC dengan A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap $[O, \frac{1}{2}]$! Gambarkan segitiga tersebut beserta bayangannya pada bidang koordinat!
Pilihan: A. $A'(-\frac{3}{2},-2)$, $B'(3,4)$, $C'(\frac{1}{2},-2)$
B. A'(-2.5,-1.5), B'(6.5,4.5), C'(1.5,-1.5)
C. A'(-6,-4), B'(12,8), C'(2,-4)
D. $A'(-\frac{3}{2},-1)$, $B'(3,2)$, $C'(\frac{1}{2},-1)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br>Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = AE, karena ∠ACE = ∠AEC |
| B | AC = CE, karena ∠CAE = ∠AEC |
| C | AE = CE, karena ∠ACE = ∠CAE |
| D | AB = AC, karena AD garis bagi |

![Gambar sumber soal 32](<../../../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Misalkan ∠BAD = ∠DAC = α. Karena CE \|\| AD, maka ∠AEC = ∠BAD = α (sudut sehadap) dan ∠ACE = ∠DAC = α (sudut dalam berseberangan). Karena ∠AEC = ∠ACE = α, maka ΔACE adalah segitiga sama kaki dengan AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik B, D, C terletak pada satu garis lurus.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `59eab208246cf056c83198df2a6ea187a1c50eace8363f6ff5fa52ab3a8c379e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3239 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3236 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3233 |

Run 1 — solusi: Misalkan ∠BAD = ∠DAC = α. Karena CE \|\| AD, maka ∠AEC = ∠BAD = α (sudut sehadap) dan ∠ACE = ∠DAC = α (sudut dalam berseberangan). Karena ∠AEC = ∠ACE = α, maka ΔACE adalah segitiga sama kaki dengan AC = AE.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk melakukan pembuktian geometri sederhana dengan menggunakan sifat garis sejajar (sudut sehadap dan berseberangan) untuk menunjukkan segitiga sama kaki. Ini memerlukan penerapan konsep geometri yang sudah dipelajari.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara sudut-sudut yang terbentuk oleh garis sejajar yang dipotong transversal (sudut sehadap dan berseberangan) serta definisi segitiga sama kaki.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang sifat-sifat sudut pada garis sejajar dan aplikasinya dalam pembuktian geometri. Meskipun prosedurnya terstruktur, siswa harus mampu mengidentifikasi pasangan sudut yang relevan.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan), definisi garis bagi, dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan dan garis sejajar adalah standar kelas 9. Soal ini menuntut pemahaman konseptual lebih dari sekadar menghitung, namun masih dalam lingkup pembuktian rutin. |

Run 2 — solusi: Misalkan AD \|\| CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD adalah garis bagi, maka sudut BAD = sudut DAC. Akibatnya, sudut AEC = sudut ACE. Karena dua sudut alas sama, maka segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana menggunakan sifat sudut pada garis sejajar (sehadap dan berseberangan dalam) untuk menunjukkan segitiga sama kaki. Ini memerlukan penerapan konsep dasar geometri, bukan sekadar ingatan.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara sudut-sudut yang terbentuk oleh garis sejajar yang dipotong transversal dan definisi segitiga sama kaki berdasarkan sudut alasnya.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman tentang konstruksi tambahan dan sifat sudut pada garis sejajar. Meskipun langkahnya terstruktur, ini bukan prosedur rutin yang sangat dasar bagi siswa kelas 9, namun juga tidak memerlukan strategi nonrutin yang kompleks.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut sehadap dan berseberangan dalam pada garis sejajar, definisi garis bagi, dan syarat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun pembuktian teorema garis bagi sering diajarkan, siswa kelas 9 sering kesulitan mengintegrasikan sifat garis sejajar dengan properti segitiga secara abstrak tanpa angka. |

Run 3 — solusi: Misalkan garis CE sejajar AD. Karena AD \|\| CE, maka ∠BAD = ∠AEC (sehadap) dan ∠DAC = ∠ACE (berseberangan dalam). Karena AD adalah garis bagi, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Karena dua sudut alas sama besar, maka ΔACE adalah segitiga sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana dengan mengonstruksi garis bantu dan menerapkan sifat sudut pada garis sejajar. Ini memerlukan pemahaman konseptual tentang hubungan sudut.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip hubungan sudut (sehadap, berseberangan) dan sifat segitiga sama kaki untuk membangun argumen logis.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Medium`: Soal ini memerlukan konstruksi garis bantu dan penalaran deduktif untuk membuktikan sifat segitiga. Meskipun langkahnya terstruktur, ini bukan sekadar aplikasi rumus langsung.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada dua garis sejajar yang dipotong garis transversal (sudut sehadap, berseberangan dalam) dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pembuktian sederhana terkait kesebangunan atau sifat segitiga menggunakan bantuan garis sejajar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "reasoning": 1} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4867`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini meminta siswa untuk melakukan pembuktian geometris sederhana dengan mengonstruksi garis bantu dan menerapkan sifat sudut pada garis sejajar. Ini memerlukan pemahaman konseptual tentang hubungan sudut dan deduksi logis.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami prinsip hubungan sudut (sehadap, berseberangan) dan sifat segitiga sama kaki untuk membangun argumen logis, yang merupakan pemahaman konseptual.
- Intended difficulty `Medium`: Soal ini memerlukan konstruksi garis bantu dan penalaran deduktif untuk membuktikan sifat segitiga. Meskipun langkahnya terstruktur, ini bukan sekadar aplikasi rumus langsung, melainkan pembuktian konsep.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada dua garis sejajar yang dipotong garis transversal (sudut sehadap, berseberangan dalam) dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan pembuktian sederhana terkait kesebangunan atau sifat segitiga menggunakan bantuan garis sejajar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kesebangunan pada Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.

Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.
Pilihan: A. AC = AE, karena ∠ACE = ∠AEC
B. AC = CE, karena ∠CAE = ∠AEC
C. AE = CE, karena ∠ACE = ∠CAE
D. AB = AC, karena AD garis bagi
Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik B, D, C terletak pada satu garis lurus.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `49861bd79ef9562f45188055`

Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk oleh seorang guru dalam kelas yang terdiri dari 12 siswa laki-laki dan 18 siswa perempuan.

| Opsi | Isi |
|---|---|
| A | 30 (12 siswa laki-laki + 18 siswa perempuan) |
| B | 18 (hanya menghitung banyaknya siswa perempuan) |
| C | 12 (hanya menghitung banyaknya siswa laki-laki) |
| D | 2 (hanya menghitung banyaknya kategori jenis kelamin: laki-laki dan perempuan) |

Kunci sumber: `A`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Soal ambigu. Jika percobaan adalah memilih satu siswa, n(S) = 12 + 18 = 30. Jika percobaan adalah mengamati jenis kelamin siswa yang terpilih, n(S) = 2 (Laki-laki atau Perempuan). Kunci jawaban 30 tidak konsisten dengan redaksi 'Jenis kelamin'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0366a40abeb9d548c3b8968048bed53dd286666f1ed542119e517564ca1775df`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | reasoning | conceptual | Medium | 2074 |
| 2 | success | concern / conflict | applying | conceptual | Medium | 2107 |
| 3 | success | concern / conflict | applying | conceptual | Medium | 2148 |

Run 1 — solusi: Secara teoretis, jika yang ditanyakan adalah ruang sampel dari 'jenis kelamin', maka jawabannya adalah 2 (Laki-laki atau Perempuan). Jika yang ditanyakan adalah ruang sampel dari 'siswa yang terpilih', maka jawabannya adalah 30. Soal ini mencampuradukkan kedua konsep tersebut.
- Domain kognitif `classify/reasoning`: Soal meminta identifikasi ruang sampel namun memberikan deskripsi yang kontradiktif antara variabel (jenis kelamin) dan objek (siswa). Siswa harus memilih antara konsep ruang sampel kejadian (2) atau ruang sampel populasi (30).. Bukti: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang apa yang membentuk ruang sampel dalam sebuah percobaan acak.. Bukti: banyaknya anggota ruang sampel
- Intended difficulty `classify/Medium`: Tingkat kesulitan menengah karena siswa harus membedakan antara ruang sampel hasil (outcome space) dan ruang sampel individu, meskipun soalnya sendiri cacat secara matematis.. Bukti: 12 siswa laki-laki dan 18 siswa perempuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar ruang sampel dan kejadian. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kelas 9 sering membahas ruang sampel. Kesalahan pada soal membuat siswa harus memilih interpretasi yang paling mungkin dimaksudkan oleh pembuat soal. |

Run 2 — solusi: Jika percobaan adalah memilih satu siswa, n(S) = 12 + 18 = 30. Jika percobaan adalah mengamati jenis kelamin siswa yang terpilih, n(S) = 2 (Laki-laki atau Perempuan). Soal ambigu.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi ruang sampel dalam konteks percobaan acak. Namun, karena redaksi soal ambigu antara memilih individu vs mengamati atribut, siswa harus melakukan interpretasi konsep.. Bukti: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa yang membentuk ruang sampel dalam suatu percobaan.. Bukti: banyaknya anggota ruang sampel
- Intended difficulty `classify/Medium`: Secara prosedural mudah (penjumlahan), namun secara konseptual membingungkan karena ambiguitas redaksi soal.. Bukti: 12 siswa laki-laki dan 18 siswa perempuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi ruang sampel dan kejadian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, ambiguitas antara ruang sampel individu vs ruang sampel atribut membuat soal ini menuntut pemahaman konsep yang lebih dalam daripada sekadar menghitung. |

Run 3 — solusi: Jika percobaan adalah memilih satu siswa dari 30 siswa (12 L + 18 P), maka ruang sampel adalah 30 individu. Jika percobaan adalah mengamati jenis kelamin siswa yang terpilih, maka ruang sampel adalah {Laki-laki, Perempuan} dengan n(S)=2. Soal ambigu.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi ruang sampel dalam konteks percobaan acak. Namun, karena redaksi soal ambigu antara memilih individu vs mengamati atribut, siswa harus melakukan analisis konseptual untuk menentukan apa yang sebenarnya menjadi objek percobaan.. Bukti: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi ruang sampel (sample space) dalam teori peluang, bukan sekadar prosedur menghitung.. Bukti: banyaknya anggota ruang sampel
- Intended difficulty `classify/Medium`: Secara prosedural soal ini sederhana (penjumlahan), namun secara konseptual membingungkan karena ketidakjelasan definisi ruang sampel yang diminta. Kesulitan utama terletak pada interpretasi soal yang ambigu.. Bukti: 12 siswa laki-laki dan 18 siswa perempuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang ruang sampel dan percobaan acak. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kelas 9 mencakup ruang sampel. Soal ini menuntut pemahaman konsep ruang sampel, namun redaksi yang buruk membuat siswa harus memilih interpretasi yang paling masuk akal (memilih siswa vs atribut). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3561`.
Konten: `concern`; kunci: `conflict`; masalah: Soal memiliki ambiguitas fatal dalam definisi ruang sampel. Percobaan yang didefinisikan adalah 'Jenis kelamin dari seorang siswa yang ditunjuk'. Secara matematis, ruang sampel dari variabel acak 'jenis kelamin' adalah {Laki-laki, Perempuan}, sehingga n(S) = 2.; Kunci jawaban (30) mengasumsikan percobaan adalah 'memilih satu siswa dari kelas', bukan 'mengamati jenis kelamin siswa yang terpilih'. Redaksi soal mencampuradukkan objek (siswa) dengan atribut (jenis kelamin)..
- Domain kognitif `reasoning`: Siswa dituntut untuk mengidentifikasi ruang sampel, namun karena redaksi soal yang cacat, siswa harus melakukan analisis konseptual untuk menentukan apakah yang dimaksud adalah ruang sampel individu atau ruang sampel atribut.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang definisi ruang sampel dalam teori peluang, yang terganggu oleh ketidakjelasan redaksi.
- Intended difficulty `Medium`: Secara prosedural soal ini sangat sederhana (penjumlahan), namun tingkat kesulitan menjadi menengah karena siswa harus menghadapi ambiguitas konseptual yang signifikan dalam soal.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar ruang sampel dan kejadian. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang kelas 9 membahas ruang sampel. Soal ini menuntut pemahaman konsep, namun redaksi yang buruk membuat siswa harus memilih interpretasi yang paling mungkin dimaksudkan oleh pembuat soal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk oleh seorang guru dalam kelas yang terdiri dari 12 siswa laki-laki dan 18 siswa perempuan.
Pilihan: A. 30 (12 siswa laki-laki + 18 siswa perempuan)
B. 18 (hanya menghitung banyaknya siswa perempuan)
C. 12 (hanya menghitung banyaknya siswa laki-laki)
D. 2 (hanya menghitung banyaknya kategori jenis kelamin: laki-laki dan perempuan)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal memiliki ambiguitas fatal dalam definisi ruang sampel. Percobaan yang didefinisikan adalah 'Jenis kelamin dari seorang siswa yang ditunjuk'. Secara matematis, ruang sampel dari variabel acak 'jenis kelamin' adalah {Laki-laki, Perempuan}, sehingga n(S) = 2.; Kunci jawaban (30) mengasumsikan percobaan adalah 'memilih satu siswa dari kelas', bukan 'mengamati jenis kelamin siswa yang terpilih'. Redaksi soal mencampuradukkan objek (siswa) dengan atribut (jenis kelamin)..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `47721424de374937d3a86de8`

Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase. ⓒ Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau. Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.

| Opsi | Isi |
|---|---|
| A | 1 (membandingkan bola bukan merah dengan sesamanya, bukan dengan total bola di kotak) |
| B | 1/6 (hanya menghitung peluang terambilnya bola kuning saja, lupa bola hijau) |
| C | 1/3 (hanya menghitung peluang terambilnya bola hijau saja, lupa bola kuning) |
| D | 1/2 (atau 0,5 atau 50%) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `1/2, 0,5, 50%`.
Solusi minimum hasil AI: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Kejadian bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal: 0,5. Dalam persentase: 50%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `447c8114860b477fa1edb0f442a7cd11a621528bbc29d63335003df5b76a0749`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2140 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2152 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2127 |

Run 1 — solusi: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Kejadian bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal: 0,5. Dalam persentase: 50%.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel total dan kejadian yang diinginkan (komplemen dari kejadian terambil bola merah), kemudian menerapkan rumus peluang dasar.. Bukti: Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur perhitungan peluang dasar dan konversi antar bentuk bilangan (pecahan, desimal, persen).. Bukti: Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase.
- Intended difficulty `classify/Easy`: Soal ini melibatkan perhitungan peluang sederhana dengan satu langkah logika (menentukan komplemen) dan operasi aritmatika dasar. Tidak ada jebakan kompleks atau strategi non-rutin.. Bukti: enam bola merah, dua bola kuning, dan empat bola hijau; kalian mendapatkan bola yang bukan merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (kejadian/ruang sampel) dan operasi pecahan/desimal/persen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena menguji pemahaman dasar peluang dengan konteks yang familiar dan langkah penyelesaian yang langsung. |

Run 2 — solusi: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Kejadian bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal: 0,5. Dalam persentase: 50%.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel total dan kejadian komplemen (bukan merah) untuk menerapkan rumus peluang dasar. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang ruang sampel dan kejadian komplemen dalam peluang, serta prosedur perhitungan peluang dasar.. Bukti: peluang tiap-tiap kejadian; enam bola merah, dua bola kuning, dan empat bola hijau
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Siswa hanya perlu menjumlahkan total objek dan mengidentifikasi subset yang diinginkan (bukan merah) lalu menghitung rasionya.. Bukti: enam bola merah, dua bola kuning, dan empat bola hijau; kalian mendapatkan bola yang bukan merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (kejadian/ruang sampel) dan operasi penjumlahan pecahan/bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang adalah kurikulum standar SMP kelas 9. Soal ini menggunakan konteks sederhana yang familiar dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Total bola = 6 (merah) + 2 (kuning) + 4 (hijau) = 12. Kejadian bukan merah = 2 (kuning) + 4 (hijau) = 6. Peluang = 6/12 = 1/2. Dalam desimal = 0,5. Dalam persentase = 50%.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi ruang sampel total dan kejadian komplemen (bukan merah), kemudian menerapkan rumus peluang dasar. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep peluang dasar dan hubungan antara kejadian komplemen dengan ruang sampel.. Bukti: Tentukan peluang tiap-tiap kejadian berikut ini
- Intended difficulty `classify/Easy`: Soal ini melibatkan perhitungan peluang dasar dengan satu langkah logis (menjumlahkan kategori yang bukan merah) dan penyederhanaan pecahan. Prosedur ini sangat familiar bagi siswa kelas 9.. Bukti: enam bola merah, dua bola kuning, dan empat bola hijau; kalian mendapatkan bola yang bukan merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan konsep peluang sederhana (kejadian/ruang sampel). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang dasar adalah standar kurikulum SMP kelas 9. Soal ini tidak memerlukan strategi nonrutin atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3698`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan rumus peluang dasar (kejadian/ruang sampel) pada situasi rutin yang melibatkan identifikasi kejadian komplemen.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang ruang sampel dan kejadian komplemen, serta prosedur perhitungan peluang dasar.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Siswa hanya perlu menjumlahkan total objek dan mengidentifikasi subset yang diinginkan (bukan merah) lalu menghitung rasionya.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (kejadian/ruang sampel) dan operasi penjumlahan pecahan/bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi peluang adalah kurikulum standar SMP kelas 9. Soal ini menggunakan konteks sederhana yang familiar dan tidak memerlukan strategi non-rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase. ⓒ Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau. Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
Pilihan: A. 1 (membandingkan bola bukan merah dengan sesamanya, bukan dengan total bola di kotak)
B. 1/6 (hanya menghitung peluang terambilnya bola kuning saja, lupa bola hijau)
C. 1/3 (hanya menghitung peluang terambilnya bola hijau saja, lupa bola kuning)
D. 1/2 (atau 0,5 atau 50%)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `2fa02b235094086c5cc7be86`

Sebuah program komputer digunakan untuk menampilkan 12 bilangan 0–3 secara acak. Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3<br><br>Tentukan frekuensi relatif munculnya bilangan 0.

| Opsi | Isi |
|---|---|
| A | 2/4 (= 1/2) |
| B | 2/12 (= 1/6) |
| C | 3/12 (= 1/4) |
| D | 1/12 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Bilangan 0 muncul sebanyak 2 kali. Frekuensi relatif = (banyak kejadian) / (total percobaan) = 2/12 = 1/6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `59e45b7ed061d94a489406902dd5cbdd20f8f7380974294e27116ba16b329a98`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2085 |
| 2 | success | valid / verified | applying | procedural | Easy | 2076 |
| 3 | success | valid / verified | applying | procedural | Easy | 2098 |

Run 1 — solusi: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Bilangan 0 muncul sebanyak 2 kali. Frekuensi relatif = (banyak kejadian) / (total percobaan) = 2/12 = 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi frekuensi relatif (kejadian/total) pada data yang diberikan secara langsung. Ini adalah proses penerapan prosedur standar.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep frekuensi relatif dan prosedur penghitungan statistik dasar.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan penghitungan frekuensi sederhana dan pembagian pecahan dasar tanpa jebakan atau strategi kompleks.. Bukti: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3; Tentukan frekuensi relatif munculnya bilangan 0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif dan kemampuan menghitung data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 sebagai latihan dasar statistik/peluang empiris. |

Run 2 — solusi: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Frekuensi munculnya angka 0 adalah 2 (pada posisi ke-4 dan ke-8). Frekuensi relatif = frekuensi kejadian / total percobaan = 2/12 = 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi frekuensi relatif (frekuensi kejadian dibagi total percobaan) pada data yang diberikan secara langsung. Ini adalah proses rutin.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang konsep frekuensi relatif dan prosedur penghitungannya dari sekumpulan data.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan penghitungan frekuensi sederhana dan pembagian dasar. Tidak ada strategi kompleks atau kendala yang saling terkait.. Bukti: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3; Tentukan frekuensi relatif munculnya bilangan 0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi dan konsep peluang empiris. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 sebagai penerapan langsung konsep peluang empiris dengan data kecil. |

Run 3 — solusi: Data: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3. Total data (n) = 12. Frekuensi munculnya angka 0 adalah 2 (pada posisi ke-4 dan ke-8). Frekuensi relatif = frekuensi kejadian / total percobaan = 2/12 = 1/6.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi frekuensi relatif (frekuensi kejadian dibagi total percobaan) pada data yang diberikan. Ini adalah proses rutin dalam statistika dasar.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep frekuensi relatif dan prosedur perhitungannya.. Bukti: Tentukan frekuensi relatif munculnya bilangan 0.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan penghitungan frekuensi sederhana dan pembagian dasar. Tidak ada kendala kompleks atau strategi non-rutin.. Bukti: 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3; Tentukan frekuensi relatif munculnya bilangan 0.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang data, frekuensi, dan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 sebagai pengenalan atau penguatan konsep peluang empiris dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah program komputer digunakan untuk menampilkan 12 bilangan 0–3 secara acak. Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3

Tentukan frekuensi relatif munculnya bilangan 0.
Pilihan: A. 2/4 (= 1/2)
B. 2/12 (= 1/6)
C. 3/12 (= 1/4)
D. 1/12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `b09a24b57d973871a9f482c8`

Seperangkat kartu berisi 5 kartu yang masing-masing bergambar lingkaran atau bintang. Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20. 450 407 400 350 300 250 200 150 93 100 50 0 Lingkaran Bintang Gambar yang Muncul Frekuensi Gambar Frekuensi Munculnya Kartu Bergambar Lingkaran dan Bintang<br><br>Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.

| Opsi | Isi |
|---|---|
| A | 4 kartu lingkaran dan 1 kartu bintang |
| B | 5 kartu lingkaran dan 0 kartu bintang |
| C | 1 kartu lingkaran dan 4 kartu bintang |
| D | 3 kartu lingkaran dan 2 kartu bintang |

![Gambar sumber soal 36](<../../../images/kelas9_crop-s0012-gambar-muncul.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Frekuensi relatif Lingkaran = 93/500 = 0,186. Estimasi jumlah kartu Lingkaran = 0,186 * 5 = 0,93 (dibulatkan menjadi 1). Frekuensi relatif Bintang = 407/500 = 0,814. Estimasi jumlah kartu Bintang = 0,814 * 5 = 4,07 (dibulatkan menjadi 4). Jadi, terdapat 1 kartu Lingkaran dan 4 kartu Bintang.
Gambar sumber: images/kelas9_crop-s0012-gambar-muncul.png. Transkripsi visual: Diagram batang menunjukkan frekuensi munculnya dua jenis kartu dalam 500 percobaan. Sumbu horizontal (Gambar yang Muncul) memiliki dua kategori: 'Lingkaran' dan 'Bintang'. Sumbu vertikal (Frekuensi) memiliki skala 0 hingga 450. Batang 'Lingkaran' memiliki tinggi 93. Batang 'Bintang' memiliki tinggi 407.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aefcab1f5fec4b85ee56cf4ca9132e5b968aaf64b4b0206349262fb5b193faa7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | applying | conceptual | Medium | 3446 |
| 2 | success | concern / conflict | applying | procedural | Medium | 3644 |
| 3 | success | valid / verified | applying | procedural | Medium | 3427 |

Run 1 — solusi: Berdasarkan data grafik: frekuensi relatif Lingkaran = 93/500 = 0,186; frekuensi relatif Bintang = 407/500 = 0,814. Jika total kartu = 5, maka jumlah kartu Lingkaran = 0,186 * 5 = 0,93 (dibulatkan menjadi 1) dan jumlah kartu Bintang = 0,814 * 5 = 4,07 (dibulatkan menjadi 4). Jadi, seharusnya 1 kartu Lingkaran dan 4 kartu Bintang.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang empiris (frekuensi relatif) untuk mengestimasi komposisi populasi (jumlah kartu) dari data sampel, yang merupakan proses applying.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang hubungan antara frekuensi relatif dalam sampel dengan proporsi dalam populasi (konsep peluang empiris).. Bukti: Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20.
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep dasar peluang empiris dan operasi aritmatika sederhana. Prosedurnya rutin namun memerlukan interpretasi data grafik.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif dan pembulatan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena melibatkan interpretasi data statistik sederhana dan estimasi proporsi. |

Run 2 — solusi: Berdasarkan data visual: Frekuensi relatif Lingkaran = 93/500 = 0,186. Estimasi jumlah kartu lingkaran = 0,186 * 5 = 0,93 (dibulatkan menjadi 1). Frekuensi relatif Bintang = 407/500 = 0,814. Estimasi jumlah kartu bintang = 0,814 * 5 = 4,07 (dibulatkan menjadi 4). Jadi, seharusnya 1 kartu lingkaran dan 4 kartu bintang.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang empiris untuk mengestimasi komposisi populasi (kartu) berdasarkan data sampel (frekuensi hasil percobaan). Ini melibatkan pemilihan prosedur perhitungan frekuensi relatif dan interpretasi data.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.; Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan frekuensi relatif dan mengaitkannya dengan konsep proporsi dalam populasi kecil (5 kartu).. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang; frekuensi relatif lingkaran = 407/500 = 0,814, dikalikan 5 kartu = 4,07
- Intended difficulty `classify/Medium`: Soal ini memerlukan langkah rutin (menghitung frekuensi relatif) dan interpretasi data. Namun, karena adanya konflik data visual dan kunci, tingkat kesulitan teknisnya terganggu.. Bukti: 500 percobaan pengambilan satu kartu secara acak; Tentukan banyaknya kartu bergambar lingkaran dan bintang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang frekuensi relatif dan pembulatan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 dalam topik peluang empiris, namun kualitas soal buruk karena ketidaksesuaian data visual dan kunci. |

Run 3 — solusi: Frekuensi relatif lingkaran = 93/500 = 0,186. Jumlah kartu lingkaran = 0,186 * 5 = 0,93, dibulatkan menjadi 1. Frekuensi relatif bintang = 407/500 = 0,814. Jumlah kartu bintang = 0,814 * 5 = 4,07, dibulatkan menjadi 4. Jadi, terdapat 1 kartu lingkaran dan 4 kartu bintang.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang empiris (frekuensi relatif) untuk mengestimasi komposisi populasi (jumlah kartu) dari data sampel yang diberikan. Ini melibatkan pemilihan prosedur perhitungan yang tepat.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.; Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma perhitungan frekuensi relatif dan mengalikannya dengan total populasi untuk mendapatkan estimasi jumlah objek, yang merupakan prosedur matematis standar.. Bukti: Tentukan banyaknya kartu bergambar lingkaran dan bintang; frekuensi relatif lingkaran = 407/500 = 0,814, dikalikan 5 kartu
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang hubungan antara frekuensi relatif dan komposisi populasi. Meskipun perhitungannya sederhana, siswa harus memahami logika estimasi dari data empiris.. Bukti: Seperangkat kartu berisi 5 kartu; 500 percobaan; 93; 407

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang empiris dan frekuensi relatif. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena melibatkan interpretasi data statistik sederhana untuk menarik kesimpulan tentang populasi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5110`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep peluang empiris (frekuensi relatif) untuk mengestimasi komposisi populasi (jumlah kartu) dari data sampel yang diberikan. Ini adalah proses applying karena menggunakan prosedur yang sudah dipelajari untuk situasi baru.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritma perhitungan frekuensi relatif dan mengalikannya dengan total populasi untuk mendapatkan estimasi jumlah objek, yang merupakan prosedur matematis standar.
- Intended difficulty `Medium`: Soal ini memerlukan pemahaman tentang hubungan antara frekuensi relatif dan komposisi populasi. Meskipun perhitungannya sederhana, siswa harus memahami logika estimasi dari data empiris.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang empiris, frekuensi relatif, dan pembulatan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena melibatkan interpretasi data statistik sederhana untuk menarik kesimpulan tentang populasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Seperangkat kartu berisi 5 kartu yang masing-masing bergambar lingkaran atau bintang. Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20. 450 407 400 350 300 250 200 150 93 100 50 0 Lingkaran Bintang Gambar yang Muncul Frekuensi Gambar Frekuensi Munculnya Kartu Bergambar Lingkaran dan Bintang

Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.
Pilihan: A. 4 kartu lingkaran dan 1 kartu bintang
B. 5 kartu lingkaran dan 0 kartu bintang
C. 1 kartu lingkaran dan 4 kartu bintang
D. 3 kartu lingkaran dan 2 kartu bintang
Transkripsi visual: Diagram batang menunjukkan frekuensi munculnya dua jenis kartu dalam 500 percobaan. Sumbu horizontal (Gambar yang Muncul) memiliki dua kategori: 'Lingkaran' dan 'Bintang'. Sumbu vertikal (Frekuensi) memiliki skala 0 hingga 450. Batang 'Lingkaran' memiliki tinggi 93. Batang 'Bintang' memiliki tinggi 407.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `0292b36d9d04627c0f3ae4e8`

Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan. b. Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.

| Opsi | Isi |
|---|---|
| A | 48 |
| B | 25 |
| C | 13 |
| D | 75 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Total kartu remi = 52. Jumlah kartu hati = 13. Jumlah kartu bukan hati = 52 - 13 = 39. Peluang terambil bukan kartu hati P(A') = 39/52 = 3/4. Frekuensi harapan = P(A') x n = 3/4 x 100 = 75.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3b0a8ca17f1b7400778904af0b6712532fb3b978f04442409bc2aa8abb851d2c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2057 |
| 2 | success | valid / verified | applying | procedural | Easy | 2099 |
| 3 | success | valid / verified | applying | procedural | Easy | 2068 |

Run 1 — solusi: Total kartu remi = 52. Jumlah kartu hati = 13. Jumlah kartu bukan hati = 52 - 13 = 39. Peluang terambil bukan kartu hati P(A') = 39/52 = 3/4. Frekuensi harapan = P(A') x n = 3/4 x 100 = 75.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus frekuensi harapan dan memahami konsep peluang komplemen dalam situasi rutin (pengambilan kartu).. Bukti: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan.; Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur algoritma untuk menghitung peluang dan frekuensi harapan.. Bukti: frekuensi harapan; pengambilan satu kartu secara acak dari seperangkat kartu remi
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur standar yang familiar bagi siswa kelas 9, yaitu menghitung peluang komplemen dan mengalikannya dengan jumlah percobaan.. Bukti: 100 kali percobaan; tidak didapatkan kartu hati

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang teoretik dan konsep komplemen kejadian. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan adalah standar kurikulum kelas 9 yang bersifat prosedural langsung. |

Run 2 — solusi: Satu set kartu remi memiliki 52 kartu. Jumlah kartu hati adalah 13, sehingga jumlah kartu bukan hati adalah 52 - 13 = 39. Peluang terambil bukan kartu hati P(A') = 39/52 = 3/4. Frekuensi harapan untuk 100 percobaan adalah 3/4 * 100 = 75.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus frekuensi harapan Fh = P(A) x n. Ini melibatkan pemilihan prosedur yang tepat (menentukan peluang komplemen) dan melakukan perhitungan rutin.. Bukti: Tentukan frekuensi harapan; pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep peluang teoritis dan frekuensi harapan, yang merupakan pengetahuan prosedural untuk menghitung nilai harapan.. Bukti: frekuensi harapan; pengambilan satu kartu secara acak
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Siswa hanya perlu memahami konsep peluang komplemen (bukan hati) dan mengalikan dengan jumlah percobaan.. Bukti: 100 kali percobaan; tidak didapatkan kartu hati

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang dasar dan peluang komplemen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan adalah standar kurikulum kelas 9. Soal ini menggunakan konteks kartu remi yang umum dan prosedur standar tanpa jebakan kompleks. |

Run 3 — solusi: Satu set kartu remi memiliki 52 kartu. Jumlah kartu hati adalah 13, sehingga jumlah kartu bukan hati adalah 52 - 13 = 39. Peluang terambil bukan kartu hati adalah P(bukan hati) = 39/52 = 3/4. Frekuensi harapan untuk 100 percobaan adalah 3/4 * 100 = 75.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus frekuensi harapan Fh = P(A) x n. Ini adalah penerapan prosedur standar pada situasi rutin.. Bukti: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan; Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma/prosedur perhitungan frekuensi harapan dan pemahaman konsep peluang komplemen.. Bukti: frekuensi harapan; pengambilan satu kartu secara acak dari seperangkat kartu remi
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin (menghitung peluang komplemen dan mengalikannya dengan jumlah percobaan). Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: 100 kali percobaan; tidak didapatkan kartu hati

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar peluang teoretis dan komplemen kejadian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena frekuensi harapan adalah materi standar yang menggunakan operasi aritmatika dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan. b. Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.
Pilihan: A. 48
B. 25
C. 13
D. 75
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `dfd8cbd993b44696494b45c1`

Di sebuah kota, persentase penduduknya yang masuk Generasi Z adalah 28%. Jika kalian memilih 75 penduduk kota itu secara acak, tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z.

| Opsi | Isi |
|---|---|
| A | 28 |
| B | 47 |
| C | 75 |
| D | 21 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Frekuensi harapan (Fh) dihitung dengan rumus Fh = P(A) x n. Diketahui P(A) = 28% = 0,28 dan n = 75. Maka, Fh = 0,28 x 75 = 21.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1b51da04bb5b829e3961692e142190e439e003e50bfba251ae089313921ccbd2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1998 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2013 |
| 3 | success | valid / verified | applying | procedural | Easy | 1986 |

Run 1 — solusi: Frekuensi harapan (Fh) dihitung dengan rumus Fh = P(A) x n. Diketahui P(A) = 28% = 0,28 dan n = 75. Maka, Fh = 0,28 x 75 = 21.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus frekuensi harapan secara langsung dengan data yang sudah tersedia. Ini adalah prosedur standar dalam materi peluang.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak; tentukan frekuensi harapan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur perhitungan frekuensi harapan.. Bukti: frekuensi harapan kalian mendapatkan penduduk Generasi Z
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan persentase dengan jumlah sampel tanpa ada kendala tambahan atau langkah kompleks.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan perkalian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan adalah standar kelas 9. Soal ini merupakan aplikasi langsung rumus tanpa variasi tingkat lanjut. |

Run 2 — solusi: Frekuensi harapan (Fh) dihitung dengan mengalikan peluang kejadian (P) dengan banyaknya percobaan (n). P = 28% = 0,28. n = 75. Fh = 0,28 * 75 = 21.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus frekuensi harapan (P x n) pada situasi yang sudah didefinisikan dengan jelas. Siswa hanya perlu melakukan operasi perkalian sederhana.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak, tentukan frekuensi harapan
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep frekuensi harapan sebagai hasil kali antara peluang dan jumlah percobaan.. Bukti: frekuensi harapan kalian mendapatkan penduduk Generasi Z
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan persentase dengan jumlah sampel tanpa ada kendala tambahan atau langkah kompleks.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang dan perkalian bilangan desimal dengan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan adalah standar kelas 9. Soal ini menguji pemahaman dasar rumus tanpa variasi yang menyulitkan. |

Run 3 — solusi: Frekuensi harapan (Fh) dihitung dengan rumus Fh = P(A) x n. Diketahui P(A) = 28% = 0,28 dan n = 75. Maka, Fh = 0,28 x 75 = 21.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus frekuensi harapan secara langsung dengan nilai yang sudah diberikan. Proses ini merupakan penerapan prosedur standar dalam statistika/peluang.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak; tentukan frekuensi harapan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur perhitungan frekuensi harapan.. Bukti: frekuensi harapan kalian mendapatkan penduduk Generasi Z
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan satu langkah perkalian sederhana antara peluang dan ukuran sampel. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: persentase penduduknya yang masuk Generasi Z adalah 28%; memilih 75 penduduk kota itu secara acak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan perkalian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena frekuensi harapan adalah materi standar yang penyelesaiannya bersifat langsung (prosedural). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3390`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan rumus frekuensi harapan secara langsung dengan data yang sudah tersedia. Ini adalah penerapan prosedur standar dalam materi peluang.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur perhitungan frekuensi harapan.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengalikan persentase dengan jumlah sampel tanpa ada kendala tambahan atau langkah kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar persentase dan perkalian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi frekuensi harapan adalah standar kelas 9. Soal ini merupakan aplikasi langsung rumus tanpa variasi tingkat lanjut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah kota, persentase penduduknya yang masuk Generasi Z adalah 28%. Jika kalian memilih 75 penduduk kota itu secara acak, tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z.
Pilihan: A. 28
B. 47
C. 75
D. 21
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `4e77f956826bf22b33dbf58b`

Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.

| Opsi | Isi |
|---|---|
| A | 3/125 |
| B | 10/125 (atau 0,08) |
| C | 6/125 |
| D | 5/125 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `10/125`.
Solusi minimum hasil AI: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 adalah jumlah ketiga angka < 6. Kemungkinan jumlah: jumlah 3 (1,1,1) ada 1 cara; jumlah 4 (1,1,2; 1,2,1; 2,1,1) ada 3 cara; jumlah 5 (1,1,3; 1,3,1; 3,1,1; 1,2,2; 2,1,2; 2,2,1) ada 6 cara. Total kejadian = 1 + 3 + 6 = 10. Peluang = 10/125.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b3f520e5153635eceabee7892a312d0191be9f1cf6a9a75e462130da231b68d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 2271 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2264 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2315 |

Run 1 — solusi: Total ruang sampel = 5^3 = 125. Rata-rata < 2 berarti jumlah ketiga angka < 6. Kemungkinan jumlah: (1,1,1) [jumlah 3, 1 cara]; (1,1,2), (1,2,1), (2,1,1) [jumlah 4, 3 cara]; (1,1,3), (1,3,1), (3,1,1), (1,2,2), (2,1,2), (2,2,1) [jumlah 5, 6 cara]. Total kejadian = 1 + 3 + 6 = 10. Peluang = 10/125.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep rata-rata dengan ruang sampel kejadian majemuk (tiga putaran) dan melakukan enumerasi sistematis untuk menghitung kejadian yang memenuhi syarat.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara rata-rata dan jumlah total, serta prosedur perhitungan peluang pada ruang sampel yang lebih besar.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Intended difficulty `classify/Hard`: Soal ini memerlukan enumerasi sistematis untuk memastikan tidak ada kombinasi yang terlewat (jumlah 3, 4, dan 5), yang merupakan langkah non-rutin bagi siswa SMP.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian majemuk dan rata-rata. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun operasi dasarnya sederhana, menuntut ketelitian dalam enumerasi kombinasi untuk jumlah 3, 4, dan 5 agar tidak terjadi bias perhitungan, yang sering menjadi tantangan bagi siswa kelas 9. |

Run 2 — solusi: Total ruang sampel = 5^3 = 125. Syarat rata-rata < 2 adalah jumlah ketiga angka < 6. Kemungkinan jumlah: 3 (1,1,1) ada 1 cara; 4 (1,1,2; 1,2,1; 2,1,1) ada 3 cara; 5 (1,1,3; 1,3,1; 3,1,1; 1,2,2; 2,1,2; 2,2,1) ada 6 cara. Total kejadian = 1 + 3 + 6 = 10. Peluang = 10/125.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep rata-rata dengan ruang sampel kejadian majemuk (3 putaran) dan melakukan enumerasi sistematis untuk menghitung kejadian yang memenuhi syarat.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara rata-rata, jumlah total, dan ruang sampel pada eksperimen acak.. Bukti: roda putar yang terbagi menjadi lima juring yang sama besar; rata-ratanya kurang dari 2
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan enumerasi sistematis (bukan sekadar rumus langsung) untuk menentukan kombinasi angka yang memenuhi syarat jumlah < 6, yang merupakan langkah rutin namun membutuhkan ketelitian.. Bukti: memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian majemuk dan rata-rata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan enumerasi ruang sampel untuk kejadian majemuk sederhana, namun soal ini menuntut ketelitian dalam mengelompokkan jumlah yang memenuhi syarat. |

Run 3 — solusi: Total ruang sampel = 5^3 = 125. Rata-rata < 2 berarti jumlah ketiga angka < 6. Kemungkinan jumlah: (1,1,1) = 1 cara (jumlah 3); (1,1,2), (1,2,1), (2,1,1) = 3 cara (jumlah 4); (1,1,3), (1,3,1), (3,1,1), (1,2,2), (2,1,2), (2,2,1) = 6 cara (jumlah 5). Total cara = 1 + 3 + 6 = 10. Peluang = 10/125.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep rata-rata dengan ruang sampel kejadian majemuk (tiga putaran) dan melakukan enumerasi sistematis untuk menghitung kejadian yang memenuhi syarat.. Bukti: memilih sampel dengan memutar roda tersebut sebanyak tiga kali; peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara rata-rata dan jumlah total (konsep) serta menerapkan prosedur pencacahan sistematis untuk ruang sampel yang cukup besar.. Bukti: rata-ratanya kurang dari 2; memutar roda tersebut sebanyak tiga kali
- Intended difficulty `classify/Medium`: Soal ini memerlukan ketelitian dalam enumerasi kombinasi angka yang memenuhi syarat jumlah < 6. Meskipun prosedurnya rutin, jumlah kasus yang harus diidentifikasi (10 kasus) dan pemahaman bahwa rata-rata < 2 ekuivalen dengan jumlah < 6 menjadikannya tantangan menengah.. Bukti: roda putar yang terbagi menjadi lima juring; memutar roda tersebut sebanyak tiga kali; rata-ratanya kurang dari 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep peluang kejadian majemuk, rata-rata, dan pencacahan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu menangani peluang kejadian majemuk dengan ruang sampel yang terstruktur, namun enumerasi sistematis untuk menghindari kesalahan hitung memerlukan ketelitian tingkat menengah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Hard": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4096`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa perlu mengintegrasikan konsep rata-rata dengan ruang sampel kejadian majemuk (tiga putaran) dan melakukan enumerasi sistematis untuk menghitung kejadian yang memenuhi syarat.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami hubungan antara rata-rata dan jumlah total (konsep) serta menerapkan prosedur pencacahan sistematis untuk ruang sampel yang cukup besar.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan enumerasi sistematis (bukan sekadar rumus langsung) untuk menentukan kombinasi angka yang memenuhi syarat jumlah < 6, yang merupakan langkah rutin namun membutuhkan ketelitian.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian majemuk dan rata-rata. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu melakukan enumerasi ruang sampel untuk kejadian majemuk sederhana, namun soal ini menuntut ketelitian dalam mengelompokkan jumlah yang memenuhi syarat agar tidak terjadi bias perhitungan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.
Pilihan: A. 3/125
B. 10/125 (atau 0,08)
C. 6/125
D. 5/125
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `d57b84b818b2d3b772624d73`

Dhien adalah calon ketua OSIS. Dia ingin mengetahui persentase teman-teman di sekolahnya yang akan memilihnya.<br><br>Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa? ⓐ Dia bertanya kepada semua teman sekelasnya. ⓑ Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera. ⓒ Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya.

| Opsi | Isi |
|---|---|
| A | Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera |
| B | Dia menyurvei murid yang kebetulan lewat di depan kelasnya saat istirahat |
| C | Dia bertanya kepada semua teman sekelasnya |
| D | Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Metode (b) adalah sampling sistematis yang mencakup perwakilan dari seluruh barisan siswa di sekolah saat upacara bendera, sehingga paling representatif. Opsi (a) bias karena hanya mencakup satu kelas, dan opsi (c) bias karena hanya mencakup pengguna media sosial tertentu.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `969cc3d63c62abad63100c810b2f53f73d7e01a0ac98d79d5538cb3ab414abbe`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2910 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2950 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2579 |

Run 1 — solusi: Metode sistematis (opsi A) adalah yang paling representatif karena mencakup siswa dari seluruh barisan sekolah saat upacara, sehingga meminimalkan bias dibandingkan survei satu kelas (bias populasi), survei media sosial (bias seleksi), atau survei kenyamanan.
- Domain kognitif `classify/applying`: Siswa perlu mengevaluasi metode pengambilan sampel untuk menentukan mana yang paling representatif dan meminimalkan bias. Ini melibatkan penerapan konsep statistik dasar.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien?; Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang membuat sampel representatif (acak) dibandingkan dengan sampel yang bias.. Bukti: mana yang seharusnya dipilih Dhien?; Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera
- Intended difficulty `classify/Medium`: Soal ini meminta siswa membedakan metode sampling yang valid secara konseptual. Tidak ada perhitungan rumit, hanya pemahaman tentang bias sampling.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi dan sampel, serta konsep bias dalam survei. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menuntut kemampuan memilih prosedur sampling yang tepat dari beberapa pilihan yang diberikan, yang merupakan standar kompetensi kelas 9. |

Run 2 — solusi: Metode (b) menggunakan teknik sampling sistematis yang mencakup perwakilan dari seluruh barisan siswa di sekolah saat upacara bendera. Ini meminimalkan bias dibandingkan dengan (a) yang hanya mencakup satu kelas, atau (c) yang hanya mencakup pengguna media sosial tertentu.
- Domain kognitif `classify/reasoning`: Siswa harus mengevaluasi dan membandingkan tiga metode sampling untuk menentukan mana yang paling representatif dan minim bias, yang merupakan proses penalaran statistik.. Bukti: mana yang seharusnya dipilih Dhien? Mengapa?
- Dimensi pengetahuan `classify/conceptual`: Memahami prinsip dasar pemilihan sampel yang representatif (acak) dibandingkan dengan sampel yang bias (convenience/voluntary response).. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konseptual tentang bias sampling. Siswa perlu membedakan antara sampling sistematis dan sampling yang bias, yang merupakan materi standar kelas 9.. Bukti: mana yang seharusnya dipilih Dhien? Mengapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi, sampel, dan konsep bias dalam survei. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal memerlukan pemahaman konseptual tentang bias sampling. Siswa perlu membedakan antara sampling sistematis dan sampling yang bias (convenience/voluntary), yang merupakan materi standar kelas 9. |

Run 3 — solusi: Opsi A (survei sistematis saat upacara) adalah metode sampling yang paling representatif karena mencakup siswa dari seluruh barisan di sekolah, sehingga meminimalkan bias populasi dibandingkan hanya bertanya pada teman sekelas (bias kelompok) atau pengguna media sosial (bias akses).
- Domain kognitif `classify/applying`: Siswa diminta untuk mengevaluasi dan memilih metode pengambilan sampel yang paling tidak bias dari tiga skenario yang diberikan, yang merupakan penerapan konsep statistik.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang membuat sampel representatif dan bagaimana bias muncul dalam metode pengambilan sampel yang berbeda.. Bukti: mana yang seharusnya dipilih Dhien? Mengapa?
- Intended difficulty `classify/Medium`: Siswa harus menganalisis tiga metode sampling yang berbeda dan mengidentifikasi potensi bias pada masing-masing metode untuk menentukan mana yang paling valid secara statistik.. Bukti: Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi, sampel, dan konsep bias dalam survei. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memilih metode sampling yang tepat adalah standar kompetensi statistik kelas 9 yang memerlukan penalaran tentang representasi populasi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "reasoning": 1} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3479`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa perlu mengevaluasi dan membandingkan tiga metode sampling untuk menentukan mana yang paling representatif dan meminimalkan bias, yang merupakan proses penalaran statistik.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang membuat sampel representatif (acak) dibandingkan dengan sampel yang bias (convenience/voluntary response).
- Intended difficulty `Medium`: Siswa harus menganalisis tiga metode sampling yang berbeda dan mengidentifikasi potensi bias pada masing-masing metode untuk menentukan mana yang paling valid secara statistik.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang populasi, sampel, dan konsep bias dalam survei. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memilih metode sampling yang tepat adalah standar kompetensi statistik kelas 9 yang memerlukan penalaran tentang representasi populasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dhien adalah calon ketua OSIS. Dia ingin mengetahui persentase teman-teman di sekolahnya yang akan memilihnya.

Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa? ⓐ Dia bertanya kepada semua teman sekelasnya. ⓑ Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera. ⓒ Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya.
Pilihan: A. Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera
B. Dia menyurvei murid yang kebetulan lewat di depan kelasnya saat istirahat
C. Dia bertanya kepada semua teman sekelasnya
D. Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `b0bcef02731ce1c1ec1f8a92`

Pilihan dadu<br><br>\|Pilihan 1\|Pilihan 2\|<br>\|---\|---\|<br>\|Dadu kubus dengan sisi sebagai\|Dadu piramida dengan sisi\|<br>\|berikut:\|sebagai berikut:\|<br>\|1, 2, 3, 4, 5, 6\|1, 2, 3, 4\|<br><br>Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!

| Opsi | Isi |
|---|---|
| A | Keduanya sama besar karena sama-sama punya satu angka 3 |
| B | Pilihan 1 (dadu kubus) |
| C | Pilihan 2 (dadu piramida) |
| D | Tidak bisa ditentukan karena bentuk dadunya berbeda |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Peluang muncul angka 3 pada dadu kubus (6 sisi) adalah 1/6. Peluang muncul angka 3 pada dadu piramida (4 sisi) adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menerapkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `86c95cfca3df133feb39c9d52c63a5018af97321ed0f185b6611694ca414de39`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2145 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2192 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2174 |

Run 1 — solusi: Peluang muncul angka 3 pada dadu kubus (6 sisi) adalah 1/6. Peluang muncul angka 3 pada dadu piramida (4 sisi) adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua nilai peluang yang berbeda berdasarkan ruang sampel yang berbeda (6 sisi vs 4 sisi) untuk menentukan mana yang lebih besar, yang merupakan proses penerapan konsep peluang.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang; Syarat menangnya adalah mendapatkan angka 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana ukuran ruang sampel mempengaruhi nilai peluang suatu kejadian.. Bukti: Peluang terbesar untuk menang; Syarat menangnya adalah mendapatkan angka 3
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan perbandingan dua pecahan sederhana (1/4 dan 1/6) dengan konteks yang sangat familiar (dadu).. Bukti: Pilihan dadu; Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang peluang sebagai rasio kejadian yang diinginkan terhadap total ruang sampel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu membandingkan pecahan sederhana dalam konteks peluang dasar. |

Run 2 — solusi: Peluang muncul angka 3 pada dadu kubus adalah 1/6. Peluang muncul angka 3 pada dadu piramida adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua nilai peluang (1/6 dan 1/4) untuk menentukan mana yang lebih besar. Ini melibatkan penerapan konsep peluang teoretis pada situasi yang diberikan.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang; Syarat menangnya adalah mendapatkan angka 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana jumlah ruang sampel (total sisi) mempengaruhi besarnya peluang suatu kejadian.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar; Syarat menangnya adalah mendapatkan angka 3
- Intended difficulty `classify/Easy`: Soal ini memerlukan pemahaman dasar tentang peluang teoretis dan perbandingan pecahan. Prosedurnya rutin dan langsung, tidak memerlukan strategi kompleks.. Bukti: Dadu kubus dengan sisi sebagai berikut: 1, 2, 3, 4, 5, 6; Dadu piramida dengan sisi sebagai berikut: 1, 2, 3, 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (peluang = kejadian/ruang sampel) dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan sudah memahami konsep peluang dasar dan perbandingan pecahan sederhana. |

Run 3 — solusi: Peluang muncul angka 3 pada dadu kubus (6 sisi) adalah 1/6. Peluang muncul angka 3 pada dadu piramida (4 sisi) adalah 1/4. Karena 1/4 > 1/6, maka dadu piramida memberikan peluang menang yang lebih besar.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua nilai peluang (1/6 dan 1/4) untuk menentukan mana yang lebih besar. Ini melibatkan penerapan konsep peluang teoretis pada situasi yang diberikan.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana jumlah ruang sampel (total sisi) mempengaruhi nilai peluang suatu kejadian.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan perbandingan dua pecahan sederhana dengan pembilang yang sama, yang merupakan prosedur rutin dalam materi peluang kelas 9.. Bukti: Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang (P(A) = n(A)/n(S)) dan perbandingan pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang adalah kurikulum standar kelas 9. Membandingkan peluang sederhana adalah tugas rutin yang sesuai dengan tingkat kognitif siswa kelas 9. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Membandingkan Peluang Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Pilihan dadu

|Pilihan 1|Pilihan 2|
|---|---|
|Dadu kubus dengan sisi sebagai|Dadu piramida dengan sisi|
|berikut:|sebagai berikut:|
|1, 2, 3, 4, 5, 6|1, 2, 3, 4|

Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!
Pilihan: A. Keduanya sama besar karena sama-sama punya satu angka 3
B. Pilihan 1 (dadu kubus)
C. Pilihan 2 (dadu piramida)
D. Tidak bisa ditentukan karena bentuk dadunya berbeda
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| B | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| C | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Median (Q2) = (65+70)/2 = 67,5. Q1 (median 7 data pertama: 50, 50, 60, 65, 65, 65, 65) = 65. Q3 (median 7 data terakhir: 70, 75, 80, 80, 85, 85, 90) = 80. Jangkauan antar kuartil (H) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * H = 7,5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1ab2bae4de03342167374914f66f5c413807a8492e94dd78526381878ad127b9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2548 |
| 2 | success | valid / verified | applying | procedural | Medium | 2461 |
| 3 | success | valid / verified | applying | procedural | Medium | 2496 |

Run 1 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Median (Q2) = (65+70)/2 = 67,5. Q1 (median 7 data pertama: 50, 50, 60, 65, 65, 65, 65) = 65. Q3 (median 7 data terakhir: 70, 75, 80, 80, 85, 85, 90) = 80. Jangkauan antar kuartil (H) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 0,5 * H = 7,5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik untuk mengurutkan data, menentukan posisi kuartil, dan menghitung nilai statistik deskriptif. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma atau urutan langkah (prosedur) untuk menghitung statistik data tunggal.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data (14 angka) dan perhitungan statistik dasar. Ini adalah tugas rutin dengan beberapa langkah yang saling terkait (mengurutkan, mencari median, mencari kuartil, menghitung selisih).. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data dan menentukan median data tunggal. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 9 karena melibatkan pengolahan data statistik dasar yang merupakan materi standar SMP. |

Run 2 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 (median) = (65+70)/2 = 67,5. Q1 (median data ke-1 s/d ke-7) = 65. Q3 (median data ke-8 s/d ke-14) = 80. Jangkauan antar kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik standar untuk menentukan ukuran penyebaran data (kuartil, jangkauan, simpangan kuartil) pada sekumpulan data yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan urutan langkah (prosedur) untuk mengolah data statistik dasar.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal memerlukan pengurutan data (14 data) dan penerapan rumus kuartil yang rutin. Meskipun ada beberapa langkah, prosedurnya bersifat standar dan familiar bagi siswa kelas 9.. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengurutkan data dan menentukan median. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Menghitung kuartil untuk data genap adalah materi standar kelas 9. Beban perhitungan moderat karena jumlah data cukup banyak (14) sehingga rentan kesalahan ketelitian. |

Run 3 — solusi: Data terurut: 50, 50, 60, 65, 65, 65, 65, 70, 75, 80, 80, 85, 85, 90 (n=14). Q2 (median) = (65+70)/2 = 67,5. Q1 (median data ke-1 s/d ke-7) = 65. Q3 (median data ke-8 s/d ke-14) = 80. Jangkauan kuartil (IQR) = Q3 - Q1 = 80 - 65 = 15. Simpangan kuartil = 1/2 * IQR = 7,5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur statistik untuk mengurutkan data, menentukan posisi kuartil, dan menghitung nilai-nilai statistik deskriptif. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma dan urutan langkah untuk menghitung statistik data (kuartil dan simpangan kuartil).. Bukti: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah rutin yang saling terkait (mengurutkan data, mencari median, membagi data menjadi dua bagian, mencari kuartil, dan menghitung simpangan kuartil).. Bukti: 50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman median dan pengurutan data. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 14 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 9, menguji ketelitian dalam mengurutkan data dan menerapkan rumus statistik dasar. |

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Penyebaran Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65
Pilihan: A. Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
B. Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5
C. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
D. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
