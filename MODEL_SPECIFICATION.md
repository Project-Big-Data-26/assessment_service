# Spesifikasi model silver v2

Model advisory tiga head untuk matematika SD 1-6: domain knowing/applying/reasoning, knowledge factual/conceptual/procedural/metacognitive dan difficulty Easy/Medium/Hard relatif grade. Domain, knowledge dan difficulty adalah target terpisah. KKO merupakan fitur eksperimen, bukan aturan pelabelan.

Rujukan training memakai silver AI hasil blind N=3 dan adjudikasi AI. Qualification membutuhkan kunci/solusi/visual cukup dan provenance hash. Tidak ada persetujuan pelabel manusia. Snapshot immutable, split group-aware 70/15/15, pemeriksaan dukungan kelas dan frozen-test gate berlaku.

Encoder IndoBERT memakai LoRA; training baru memakai difficulty ordinal plus embedding grade. Calibration temperature dan threshold confidence/entropy berasal dari validation silver. Arsitektur, serializer, input representation dan label maps runtime mengikuti manifest. Tidak ada fallback rules pada v2 saat artifact tidak siap.

Gate artifact: checksum, dukungan data, anti-collapse, evaluasi/calibration, promotion teknis dan approvedForProvisional. Evaluasi terhadap silver harus dilaporkan sebagai kecocokan dengan rujukan AI. Migrasi tidak menyatakan artifact lama otomatis siap serving.

Delivery silver terpisah dari kesiapan classifier: grade 1-12/TL diizinkan dengan qualification dan grade/track matching. CTT/IRT menyimpan difficulty empiris dan estimasi kemampuan dari respons siswa; tidak menjadi input classifier aktif atau menimpa label silver otomatis.
