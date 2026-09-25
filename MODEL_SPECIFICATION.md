# Spesifikasi Model Question Intelligence

## Tujuan

Model memberikan tiga prediksi yang terpisah dan bersifat advisory:

1. Proses kognitif Bloom: `C1`–`C6`.
2. Dimensi pengetahuan: `factual`, `conceptual`, `procedural`, `metacognitive`.
3. Intended difficulty: `Easy`, `Medium`, `Hard`.

Difficulty empiris tidak diprediksi sebagai kebenaran final. Setelah soal digunakan, label final mempertimbangkan difficulty index, discrimination, distraktor, waktu, populasi, dan keputusan reviewer.

## Arsitektur

```text
question_text + options + learning objective + topic + metadata
                              │
                     IndoBERT tokenizer
                              │
              indobenchmark/indobert-base-p1
                              │
                    pooled [CLS] embedding
                  ┌───────────┼───────────┐
                  │           │           │
             Bloom head   Knowledge   Difficulty
               6 kelas      4 kelas      3 kelas
```

Loss pelatihan awal adalah jumlah tiga cross-entropy loss. Pada eksperimen lanjutan, bobot task harus dipilih dari validation set, bukan diasumsikan sama.

## Input

- Teks pertanyaan dan pilihan.
- Tujuan pembelajaran.
- Jenjang/kelas, topik, subtopik.
- Jenis soal dan jumlah langkah penalaran.
- Teks hasil OCR serta kode LaTeX yang sudah dinormalisasi.

Gambar asli tidak langsung masuk ke IndoBERT. Adapter OCR/Math OCR mengubah sumber multimodal menjadi representasi teks sambil mempertahankan sumber, confidence, dan status review.

## Dataset

- Split dilakukan sebelum augmentasi dan menghindari soal duplikat/varian dekat lintas split.
- Gold label berasal dari dua annotator independen serta adjudikasi konflik.
- Bloom, dimensi pengetahuan, dan difficulty mempunyai metrik terpisah.
- Seeder 24 soal hanya memeriksa coverage pipeline; bukan dataset validasi performa.

## Metrik penerimaan

- Macro F1 dan F1 per kelas untuk ketiga head.
- Confusion matrix.
- Expected calibration error atau reliability curve pada tahap berikutnya.
- Low-confidence rate.
- Agreement model–gold dan agreement antarannotator dilaporkan terpisah.

Kriteria rilis tidak boleh ditetapkan sebelum tersedia validation set representatif. Default `confidence_threshold=0.70` hanya routing awal ke human review.

## Artefak

```text
models/indobert-multitask-v1/
├── model.pt
├── manifest.json
└── tokenizer/
```

Manifest mencatat base model, versi, waktu, hash dataset, jumlah baris, label map, status demo, dan metrik evaluasi.

## Perintah

```powershell
.\.venv\Scripts\python.exe -m app.training.train `
  --dataset data\raw\json\questions-approved.json `
  --output-dir models\indobert-multitask-v1
```

Untuk smoke test dengan dataset kecil, flag `--allow-small-demo` tersedia, tetapi artefaknya otomatis ditandai `demo_only` dan tidak boleh dipakai untuk klaim akademik atau produksi.
