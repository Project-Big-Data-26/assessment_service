# Pipeline grade-aware ordinal dengan silver

Urutan aktif: sumber -> blind N=3 -> AI adjudication -> qualification silver -> snapshot immutable -> split group-aware -> training LoRA -> calibration -> evaluation gate. Tidak ada tahapan label gold.

IndoBERT aktif mendukung SD 1-6. Scope label Gemini dan delivery mendukung reguler 1-12 serta TL kelas 11-12. `subjectTrack` mencegah pooling kelas reguler dan TL; dukungan API delivery tidak berarti encoder telah dilatih untuk SMA.

Difficulty ordinal menggunakan dua peluang kumulatif untuk batas Easy/Medium dan Medium/Hard, ditambah embedding grade. Domain dan knowledge menggunakan loss multiclass. Class weights dihitung dari train, calibration dari validation, dan frozen test digunakan sesuai gate.

`TrainingRow`, `DatasetSnapshot`, hash rows/expansion, manifest split dan provenance AI digunakan secara konsisten. Jumlah run LLM bukan jumlah siswa. IRT tidak menjadi fitur serializer IndoBERT aktif dan tidak menimpa label silver.

Penghapusan gate pelabel manusia tidak mengubah minimum support, kualitas konten, kebocoran split, anti-collapse atau integritas artifact. Lihat [runbook](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md).
