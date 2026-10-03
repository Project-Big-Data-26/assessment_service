# Dokumentasi API Nalar 2.2.0

Alur operasional: ekstraksi -> Gemini blind N=3 -> adjudikasi AI bila diperlukan -> qualification silver -> snapshot immutable -> delivery siswa -> scoring server -> CTT/IRT -> feedback otomatis dan validasi ulang AI.

Sistem menggunakan **label silver AI**. Persetujuan pelabel manusia, assignment anotasi dan pembentukan label gold sudah dihapus dari API aktif. Operator mengelola data, kredensial dan pekerjaan komputasi; operator tidak memberi label pedagogis.

Label `intendedDifficulty` berasal dari penilaian isi soal relatif kelas. `ctt.empiricalDifficulty` dan `irt.empiricalDifficulty` berasal dari respons siswa dan tetap terpisah. Perbedaan ketiganya tidak menimpa label awal.

| Panduan | Isi |
|---|---|
| [04 klasifikasi](04_CLASSIFICATION_API.md) | Kontrak tiga head dan runtime model |
| [05 keputusan silver](05_AI_DECISION_ARBITRATION_API.md) | N=3, adjudikasi dan qualification |
| [06 respons siswa](06_STUDENT_RESPONSE_API.md) | Event, scoring, idempotensi dan privasi |
| [08 delivery](08_ASSESSMENT_DELIVERY_API.md) | Registrasi silver dan assessment |
| [12 endpoint](12_ENDPOINT_MASTER_REFERENCE.md) | Inventaris dari OpenAPI aktual |
| [17 data](17_MONGODB_DATA_MODEL_ERD.md) | SQLite operasional dan MongoDB opsional |
| [22 runbook](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md) | Freeze dan gate training |
| [27 CTT/IRT](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md) | Kesiapan data dan analisis |
| [28 flow](28_END_TO_END_PERSONALIZED_ASSESSMENT_FLOW.md) | Alur terhubung dan batas implementasi |
| [33 animasi](33_ANIMATED_DATA_FLOW.html) | Penjelasan interaktif |
| [34 PPT](34_PPT_SUMMARY.md) | Materi presentasi |
| [36 migrasi](36_SILVER_OPERATIONAL_INTEGRATION.md) | Perubahan kontrak dan contoh integrasi |

Seluruh 580 soal reguler kelas 1-12 dan kelas 11-12 TL memiliki 1.740 run awal sukses. `silver_ready` hanya diberikan pada konten yang memenuhi qualification; soal yang membutuhkan revisi tetap ditahan. Lihat [laporan aktif](../output/pretest/README.md).

Implementasi tersedia tidak berarti model baru sudah dilatih atau respons siswa nyata sudah terkumpul. Rasch/2PL/3PL menunggu data dan bukti asumsi. CAT, mastery per topik, linking/equating dan pembaruan model online masih rancangan. Snapshot, prompt dan laporan historis disimpan sebagai audit.
