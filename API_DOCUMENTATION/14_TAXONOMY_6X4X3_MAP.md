# Peta Taksonomi 6 × 4 × 3

## 1. Ruang kombinasi

```text
6 proses kognitif
× 4 dimensi pengetahuan
× 3 intended difficulty
= 72 kombinasi target label
```

Angka 72 adalah ruang label, bukan jumlah data yang cukup, bukan jaminan semua sel cocok untuk semua format soal, dan bukan bukti bahwa generator dapat menghasilkan seluruh sel secara valid.

## 2. Tiga sumbu

### Proses kognitif

| Kode | Makna |
|---|---|
| C1 | Mengingat |
| C2 | Memahami |
| C3 | Menerapkan |
| C4 | Menganalisis |
| C5 | Mengevaluasi |
| C6 | Mencipta |

### Dimensi pengetahuan

| Kode | Enum | Makna |
|---|---|---|
| FAC | `factual` | Fakta, istilah, simbol, detail |
| CON | `conceptual` | Klasifikasi, prinsip, hubungan, model |
| PRO | `procedural` | Algoritma, metode, teknik, kriteria penggunaan |
| MET | `metacognitive` | Strategi, monitoring, dan pengetahuan tentang berpikir |

### Difficulty

| Kode | Enum | Makna awal |
|---|---|---|
| E | `Easy` | Intended easy |
| M | `Medium` | Intended medium |
| H | `Hard` | Intended hard |

Difficulty empiris disimpan terpisah dan selalu terikat populasi/assessment.

## 3. Kode sel

Format:

```text
<Bloom>-<Knowledge>-<Difficulty>
```

Contoh `C3-PRO-M`: menerapkan pengetahuan prosedural dengan target difficulty Medium.

## 4. Matriks 72 ID

```text
C1-FAC-E  C1-FAC-M  C1-FAC-H
C1-CON-E  C1-CON-M  C1-CON-H
C1-PRO-E  C1-PRO-M  C1-PRO-H
C1-MET-E  C1-MET-M  C1-MET-H

C2-FAC-E  C2-FAC-M  C2-FAC-H
C2-CON-E  C2-CON-M  C2-CON-H
C2-PRO-E  C2-PRO-M  C2-PRO-H
C2-MET-E  C2-MET-M  C2-MET-H

C3-FAC-E  C3-FAC-M  C3-FAC-H
C3-CON-E  C3-CON-M  C3-CON-H
C3-PRO-E  C3-PRO-M  C3-PRO-H
C3-MET-E  C3-MET-M  C3-MET-H

C4-FAC-E  C4-FAC-M  C4-FAC-H
C4-CON-E  C4-CON-M  C4-CON-H
C4-PRO-E  C4-PRO-M  C4-PRO-H
C4-MET-E  C4-MET-M  C4-MET-H

C5-FAC-E  C5-FAC-M  C5-FAC-H
C5-CON-E  C5-CON-M  C5-CON-H
C5-PRO-E  C5-PRO-M  C5-PRO-H
C5-MET-E  C5-MET-M  C5-MET-H

C6-FAC-E  C6-FAC-M  C6-FAC-H
C6-CON-E  C6-CON-M  C6-CON-H
C6-PRO-E  C6-PRO-M  C6-PRO-H
C6-MET-E  C6-MET-M  C6-MET-H
```

## 5. Difficulty driver tanpa mengubah Bloom

| Driver | Easy | Medium | Hard |
|---|---|---|---|
| Bilangan | integer sederhana | kombinasi moderat | fraction/decimal relevan |
| Langkah | pendek/linear | beberapa langkah | bercabang atau banyak constraint |
| Representasi | satu bentuk | dua bentuk | multi-representasi/conversion |
| Informasi | eksplisit | perlu dipilih/dihubungkan | padat/tersirat tetapi tetap relevan |
| Familiaritas | rutin | variasi | transfer/nonrutin |
| Scaffolding | kuat | sebagian | minimal |
| Distraktor | error sederhana | misconception umum | misconception kuat/dekat |

Menaikkan difficulty tidak boleh diam-diam mengubah konstruk. C1-Hard tetap mengingat; C3-Hard tetap menerapkan; C6-Easy tetap mencipta dengan scaffold.

## 6. Hubungan dengan authoring dan AI

Teacher tidak wajib memilih salah satu dari 72 sel. Teacher memasukkan grade, topic, objective, konten, dan jawaban. Setelah submit:

```text
IndoBERT multi-head
    + independent LLM rubric
    -> agreement/risk
    -> LLM adjudication jika perlu
    -> taxonomy decision + provenance
```

Label hasil adalah `ai_consensus` atau `ai_adjudicated`, bukan gold.

## 7. Hubungan dengan generation

Generator dapat menerima target taxonomy, tetapi target tidak menjamin hasil:

```text
target cell
    -> item-model/construct constraints
    -> generate candidate
    -> classify generated candidate kembali
    -> construct/taxonomy drift gate
```

Jika varian bergeser dari target, sistem regenerate, membuat family baru, atau quarantine. Generator tidak boleh memaksa label agar coverage 72 terlihat penuh.

## 8. Intended versus empirical difficulty

Contoh:

```json
{
  "taxonomy": {
    "bloom": "C4",
    "knowledgeDimension": "conceptual",
    "intendedDifficulty": "Hard"
  },
  "psychometrics": {
    "populationId": "GRADE-8-REFERENCE",
    "difficultyIndex": 0.78,
    "empiricalDifficulty": "Easy"
  }
}
```

Mismatch tidak otomatis mengubah C4/Conceptual. Yang diperiksa adalah difficulty driver, population, instruction exposure, distractor, dan kualitas item.

## 9. Coverage dan dataset

| Tahap | Makna |
|---|---|
| Satu contoh per sel | Hanya smoke test schema/UI |
| Beberapa family per sel | Eksperimen generator/rubric |
| Banyak source/family/variant terkontrol | Kandidat dataset model |
| Frozen family-grouped validation/test | Evaluasi tanpa leakage |

Split dilakukan berdasarkan source, question lineage, dan `itemFamilyId`, bukan variant acak.

## 10. Batas format soal

Tidak semua sel cocok diukur dengan multiple-choice sederhana. C5/C6 dan metacognitive sering memerlukan response lebih kaya, rubric scoring, atau evidence proses. Jika scoring/validation untuk format tersebut belum tersedia, sistem harus:

- membatasi generation coverage;
- menyatakan sel belum didukung;
- tidak membuat pilihan ganda dangkal hanya untuk mengisi matriks.

## 11. Schema enum

Enum machine-readable didefinisikan di [`schemas/nalar-api.schema.json`](schemas/nalar-api.schema.json). Perubahan label adalah breaking semantic change dan harus memicu rubric/model/dataset version baru.

