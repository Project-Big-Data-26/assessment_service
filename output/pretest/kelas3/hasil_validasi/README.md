# Hasil validasi ulang kelas 3

**Batch belum selesai:** 93/126 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided.

Model LLM: `gemini-3.1-flash-lite`; metode blind N=3, rubrik kelas sasaran, verifikasi kunci/solusi, dan adjudikasi AI bila diperlukan. Label terkunci sebelum diagnostik IndoBERT.

Gunakan [validation_results.json](validation_results.json) untuk data hasil dan `items[].llmAdvisory.advisoryLabels` bersama `finalRouting`. Baca [LAPORAN_VALIDASI.md](LAPORAN_VALIDASI.md) untuk soal, perhitungan confidence/entropy, tiga suara, profil difficulty, adjudikasi, serta hasil akhir per soal. [questions.json](questions.json) memuat sumber dan spesifikasi jawaban terbatas; [indobert_predictions.json](indobert_predictions.json) memuat diagnostik model lama.

Distribusi: `{"mathCognitiveDomain": {"undecided": 11, "knowing": 5, "applying": 26, "reasoning": 0}, "knowledgeDimension": {"undecided": 11, "factual": 4, "procedural": 17, "conceptual": 10, "metacognitive": 0}, "intendedDifficulty": {"undecided": 11, "Easy": 22, "Medium": 9, "Hard": 0}}`. Routing: `{"llm_retry_or_manual_review": 11, "pending_expert_review": 30, "revision_required": 1}`.

Token sukses tercatat: 220,776; tidak ada API call pada packaging. Provider dapat mencatat lebih banyak usage dari percobaan yang tidak menghasilkan output valid. Gold ahli tetap null; CTT/IRT belum dihitung. IndoBERT belum dilatih ulang dan hasil diagnostiknya tidak menentukan label blind.

Audit tidak menyetujui ekspansi/training bila gate belum lolos. Gate batch: `{"allExpectedItemsPresent": false, "threeSuccessfulRunsAtLeast90Percent": false, "insufficientOrAbstainedBelow10Percent": false, "blindPromptLeakageAbsent": true, "checkpointSourceAndInputsMatch": true, "promptAndRubricVersionMatch": true, "requiredEvidenceComplete": false, "boundaryAnalysisClear": false}`.

Kelompok difficulty tersedia di [difficulty_groups.json](difficulty_groups.json), [Easy](difficulty/Easy.json), [Medium](difficulty/Medium.json), dan [Hard](difficulty/Hard.json). `contentQualified` hanya menandai soal tanpa blocker konten; seluruh soal tetap menunggu ahli. Kategori kosong tetap diekspor. Item tanpa keputusan tersedia di [undecided](difficulty/undecided.json).
