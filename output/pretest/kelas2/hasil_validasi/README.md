# Validasi AI silver — kelas2

44 soal, 132 run blind sukses. Routing: `{'silver_ready': 43, 'revision_required': 1}`. Label: `{'Easy': 38, 'Medium': 6, 'Hard': 0}`.

Gunakan [validation_results.json](validation_results.json) untuk keputusan silver, [LAPORAN_VALIDASI.md](LAPORAN_VALIDASI.md) untuk bukti, dan [difficulty_groups.json](difficulty_groups.json) untuk kelompok kesulitan.

Alur operasional memakai AI silver tanpa persetujuan pelabel manusia. Hanya `silver_ready` masuk snapshot delivery; `revision_required` dan `needs_ai_review` ditahan untuk AI revalidation. Jalankan `scripts/build_operational_silver.py` untuk snapshot yang memverifikasi checkpoint, kunci, solusi dan aset. IRT menyimpan difficulty empiris terpisah. Gate training, evaluasi dan mutu estimasi tetap berlaku. Prompt, rubrik, jawaban dan label blind terdahulu tetap terkunci.

Format `validation_results.json`: `items[]` mempertahankan field soal sumber, dengan `cognitive_level` dari label final AI dan delapan field `ai_metadata`. `cognitive_score` dan `confidence_score` bernilai null. Hanya `ai_metadata.validation_status = silver_ready` dapat dipakai untuk delivery; ID versi/hash memakai identitas snapshot operasional. Item yang ditahan memiliki ID versi/hash null. Bukti keputusan lengkap tersedia di [decision_audit.json](bukti_validasi/decision_audit.json), ditautkan melalui `ai_metadata.decision_id`. File ini memuat kunci jawaban dan hanya untuk backend.
