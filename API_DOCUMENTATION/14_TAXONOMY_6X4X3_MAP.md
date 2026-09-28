# Peta Label Matematika 3 × 4 × 3

> Nama file lama memuat `6X4X3` untuk menjaga tautan. Kontrak target saat ini adalah 3 × 4 × 3. Matriks 72 sel Bloom sebelumnya tidak digunakan sebagai target model.

## 1. Landasan dan batas

| Head | Kerangka | Label | Pertanyaan |
|---|---|---|---|
| 1 — domain kognitif matematika | TIMSS 2023 dan AKM numerasi | `knowing`, `applying`, `reasoning` | Proses matematika apa yang wajib dilakukan? |
| 2 — dimensi pengetahuan | Revised Bloom, dimensi pengetahuan | `factual`, `conceptual`, `procedural`, `metacognitive` | Pengetahuan apa yang menjadi objek utama tugas? |
| 3 — kesulitan yang diperkirakan | Penilaian tuntutan item relatif kelas sasaran | `Easy`, `Medium`, `Hard` | Seberapa berat item sebelum data respons tersedia? |

Ketiga label ditetapkan **terpisah** oleh pakar. `reasoning` tidak dikonversi menjadi C4/C5, `applying` tidak selalu sama dengan C3, dan `difficulty` tidak diturunkan dari domain kognitif. Jika C1–C6 dibutuhkan oleh riset lain, anotasi ulang dilakukan dengan rubrik Bloom tersendiri; C1–C6 bukan keluaran pipeline ini. Dalam TIMSS, prosedur rutin masih dapat termasuk `knowing`, sehingga pemetaan satu-ke-satu ke Bloom keliru.

Landasan: [TIMSS 2023 Mathematics Framework](https://timssandpirls.bc.edu/timss2023/frameworks/pdf/T23_Frameworks_Ch1_Mathematics.pdf), [Framework AKM Pusmendik](https://pusmendik.kemdikbud.go.id/an/Framework_AKM_31032022.pdf), [Krathwohl (2002)](https://eric.ed.gov/?id=EJ667155).

## 2. Rubrik Head 1

| Domain | Bukti pada jalur penyelesaian minimal |
|---|---|
| `knowing` | Mengingat, mengenali, mengklasifikasi, mengambil informasi langsung, atau menjalankan prosedur yang rutin dan jelas. |
| `applying` | Memilih dan menerapkan operasi/strategi dalam situasi yang relatif familier; memformulasikan masalah atau membuat representasi yang sesuai. |
| `reasoning` | Menganalisis hubungan, mengintegrasikan konsep/representasi, membuat inferensi atau generalisasi, mengevaluasi, atau membenarkan keputusan matematis. |

Annotator mencatat proses **yang diperlukan**, bukan seluruh cara alternatif yang mungkin. Sebuah soal dengan kata “tentukan” dapat masuk salah satu dari tiga domain. Kompleksitas hitungan tidak otomatis berarti `reasoning`.

## 3. Rubrik Head 2

| Dimensi | Objek yang dinilai |
|---|---|
| `factual` | Istilah, simbol, notasi, fakta atau detail khusus. |
| `conceptual` | Hubungan, klasifikasi, prinsip, sifat, teori atau struktur matematika. |
| `procedural` | Algoritma, teknik, metode dan kriteria kapan sebuah prosedur digunakan. |
| `metacognitive` | Pengetahuan atau refleksi peserta tentang strategi dan proses berpikirnya sendiri. |

Pengetahuan metakognitif tidak disimpulkan hanya dari “pilih strategi terbaik”: tugas itu sering menguji kriteria prosedural. Jika soal memuat dua dimensi, simpan satu `primaryKnowledgeDimension` dan `secondaryKnowledgeDimensions` sebagai bukti tambahan; model head tunggal mempelajari label primer yang disepakati pakar.

## 4. Rubrik Head 3

`intendedDifficulty` dinilai relatif terhadap kelas/fase, kesempatan belajar, dan peserta sasaran. Pakar mencatat familiaritas, jumlah konsep/langkah, beban perhitungan, transformasi representasi, informasi pengganggu, kualitas distraktor dan dukungan/scaffold. Batas `Easy/Medium/Hard` dibuat dalam rubrik berversi dan dikalibrasi terhadap contoh jangkar. Tidak ada ambang universal. Setelah pilot, `empiricalDifficulty` dihitung dari respons pada populasi dan jendela waktu tertentu; keduanya tidak saling menimpa.

## 5. KKO dan evidence profile

KKO berada pada `features.lexical.detectedKKO`. Stem asli sudah dibaca tokenizer IndoBERT; penambahan tag `[KKO]` merupakan varian eksperimen yang harus diuji melalui ablation. KKO tidak menjadi label, tidak dikonversi melalui tabel kata kerja, dan tidak menjadi fitur khusus Head 2/3.

Evidence profile anotasi mencakup `minimalSolution`, `routineStatus`, `strategySelection`, `representationTransfer`, `reasoningOperations`, `knowledgeObject`, `targetGrade`, dan `difficultyRationale`. Profil pakar ini disimpan untuk audit. Fitur yang sudah menyiratkan label, seperti `reasoningRequired=true`, tidak dimasukkan ke model bila hanya tersedia dari anotasi manusia.

## 6. Format respons

Pilihan ganda, benar/salah, matching, dan checkbox dapat menguji `knowing`, `applying`, atau `reasoning`; bentuk klik tidak menetapkan domain. Uraian, isian, dan konstruksi interaktif memerlukan kebijakan penskoran masing-masing. `Metacognitive` hanya diberikan ketika tugas benar-benar mengamati refleksi strategi. Tidak ada kewajiban menyeimbangkan seluruh 36 kombinasi; beberapa kombinasi tidak sesuai dengan format atau populasi.

## 7. Contoh label

```json
{
  "mathCognitiveDomain": "reasoning",
  "knowledgeDimension": "procedural",
  "intendedDifficulty": "Medium",
  "evidence": ["membandingkan dua prosedur", "menentukan langkah yang tidak valid"],
  "rubricVersion": "math-3x4x3-v1"
}
```

Untuk pelatihan, pisahkan train/validation/test berdasarkan sumber, lineage dan `itemFamilyId`. Uji Head 1, 2, dan 3 secara terpisah dengan macro-F1, F1 per kelas, confusion matrix dan kalibrasi; bandingkan varian input tanpa/dengan fitur KKO eksplisit.
