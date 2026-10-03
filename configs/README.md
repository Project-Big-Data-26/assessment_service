# Konfigurasi dan bukti rubrik

Kebijakan operasional label memakai `app/silver/policy.py`: provenance `ai_silver`, tiga run blind sukses, kunci dan konten terverifikasi, serta routing `silver_ready`, `needs_ai_review` atau `revision_required`. `model_v2_risk_policy.json` menetapkan review AI dan gate teknis promosi model.

File `rubric_math_*.yaml` dan template prompt blind di `app/llm/silver.py` adalah protokol penilaian yang sudah dipakai checkpoint terkunci. Byte rubrik dan prompt dipertahankan agar hash 1.740 run terdahulu dapat diverifikasi. Metadata historis mengenai review ahli tidak menjadi gate operasional. Persetujuan manusia tidak dibaca oleh qualification, snapshot, delivery, training atau feedback empiris.

Perubahan protokol prompt/rubrik memerlukan versi baru dan run AI baru; jangan mengubah file bukti untuk mengubah kebijakan routing. Kebijakan operasional dapat berubah tanpa menulis ulang respons atau label AI yang sudah terkunci.
