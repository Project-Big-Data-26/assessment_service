# Lokasi Sumber Data Soal

Taruh data uji coba yang sudah disanitasi di folder ini. Jangan menyimpan identitas siswa, credential, atau export produksi.

```text
data/raw/
├── json/    # dataset terstruktur .json
├── csv/     # dataset tabel .csv
├── pdf/     # buku/lembar soal PDF yang hak penggunaannya jelas
├── images/  # scan/foto PNG, JPG, TIFF untuk OCR
└── latex/   # teks atau dokumen sumber berisi kode LaTeX
```

Kolom minimum JSON/CSV:

```text
question_id, question_text, subject, material_id,
bloom_label, knowledge_label, difficulty_label
```

Kolom yang sangat disarankan:

```text
grade, topic, subtopic, question_type, options, correct_answer,
explanation, learning_objective, source_reference, annotator_id,
rubric_version, label_status
```

Gunakan `label_status=approved` hanya setelah review independen/adjudikasi. Seeder demonstrasi menggunakan `demo_seed_unvalidated` dan tidak boleh dipakai untuk klaim performa model.
