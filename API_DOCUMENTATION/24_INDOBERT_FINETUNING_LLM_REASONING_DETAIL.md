# IndoBERT dan validasi AI silver

LLM menilai konten terlebih dahulu dengan Gemini blind N=3. Label awal, key/solution/visual evidence dan adjudikasi terkunci sebelum dibandingkan dengan IndoBERT. Domain: knowing/applying/reasoning. Knowledge: factual/conceptual/procedural/metacognitive. Difficulty: Easy/Medium/Hard relatif kelas sasaran.

Output menyimpan `evidenceSpans`, rationale ringkas dan profil difficulty. Hidden chain-of-thought tidak disimpan. Tiga run satu model bukan probabilitas confidence; hasilnya memiliki provenance `ai_silver`.

IndoBERT menggunakan encoder bersama, LoRA dan tiga head. Training baru memakai difficulty ordinal dengan embedding grade dan cutpoint terurut. Serializer dan arsitektur runtime mengikuti manifest; artifact lama dapat memakai multiclass parallel.

Temperature dipilih dari validation silver. Confidence adalah probabilitas maksimum dan entropy menunjukkan penyebaran probabilitas. Threshold confidence/entropy memutuskan predict/review/abstain; review adalah pemeriksaan AI/teknis, tanpa pelabel manusia.

Delivery silver tidak menunggu model baru siap. Classifier `/v2/classify` tetap menolak artifact yang belum lolos integritas, data, anti-collapse dan promotion gate. Metrik terhadap silver mengukur kecocokan dengan rujukan AI, bukan validitas empiris siswa. CTT/IRT menilai respons siswa secara terpisah.
