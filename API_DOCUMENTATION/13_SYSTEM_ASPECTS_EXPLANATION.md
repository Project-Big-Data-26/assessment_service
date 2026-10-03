# Aspek sistem silver dan kesiapan

| Aspek | Implementasi |
|---|---|
| Sumber | JSON immutable, source/version/hash dan extraction evidence |
| Validasi | Gemini blind N=3, key/solution/visual, adjudikasi AI |
| Qualification | silver_ready atau hold revisi/AI review; tanpa pelabel manusia |
| Model | IndoBERT SD, LoRA, tiga head, difficulty ordinal grade-aware |
| Dataset | Snapshot silver, group-aware split, rows SD dan expansionRows |
| Delivery | Silver qualified grade 1-12/TL, fixed-form, single-choice, opsi opaque |
| Respons | Scoring server, pseudonim, idempotensi, skip null |
| CTT/IRT | Statistik CTT dan Rasch/2PL/3PL sesuai readiness/bukti asumsi |
| Feedback | Keputusan sistem otomatis; hold kualitas, tidak overwrite label |
| Storage | SQLite operasional; MongoDB akun/sumber/model opsional |
| Keamanan | Service key, cookie/CSRF operator, participant Bearer dan ownership |

Kesiapan kode tidak sama dengan kecukupan data. Gate split/model tetap berlaku. IRT memerlukan respons siswa, variation, coverage dan bukti asumsi. Intended difficulty, CTT p dan IRT b menyimpan dasar penilaian berbeda. Missing tidak diimputasi menjadi salah; attempt memilih satu session selesai per peserta.

CAT, equating/DIF, mastery topik, media asli siswa dan auto-retrain masih rancangan. [36 integrasi](36_SILVER_OPERATIONAL_INTEGRATION.md) menjelaskan perubahan API.
