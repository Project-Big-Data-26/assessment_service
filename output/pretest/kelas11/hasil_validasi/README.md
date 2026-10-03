# Hasil validasi ulang kelas 11

**Batch belum selesai:** 62/66 run awal sukses; 1 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model LLM: `gemini-3.1-flash-lite`; metode blind N=3, rubrik kelas sasaran, verifikasi kunci/solusi, dan adjudikasi AI bila diperlukan. Label terkunci sebelum diagnostik IndoBERT.

Gunakan [validation_results.json](validation_results.json) untuk data hasil dan `items[].llmAdvisory.advisoryLabels` bersama `finalRouting`. Baca [LAPORAN_VALIDASI.md](LAPORAN_VALIDASI.md) untuk soal, perhitungan confidence/entropy, tiga suara, profil difficulty, adjudikasi, serta hasil akhir per soal. [questions.json](questions.json) memuat sumber dan spesifikasi jawaban terbatas; [indobert_predictions.json](indobert_predictions.json) memuat diagnostik model lama.

Distribusi: `{"mathCognitiveDomain": {"applying": 18, "knowing": 2, "undecided": 2, "reasoning": 0}, "knowledgeDimension": {"conceptual": 10, "procedural": 9, "factual": 1, "undecided": 2, "metacognitive": 0}, "intendedDifficulty": {"Medium": 4, "Easy": 15, "Hard": 1, "undecided": 2}}`. Routing: `{"pending_expert_review": 19, "revision_required": 1, "llm_retry_or_manual_review": 2}`.

Token sukses tercatat: 183,917; tidak ada API call pada packaging. Provider dapat mencatat lebih banyak usage dari percobaan yang tidak menghasilkan output valid. Gold ahli tetap null; CTT/IRT belum dihitung. IndoBERT belum dilatih ulang dan hasil diagnostiknya tidak menentukan label blind.

Audit tidak menyetujui ekspansi/training bila gate belum lolos. Gate batch: `{"allExpectedItemsPresent": false, "threeSuccessfulRunsAtLeast90Percent": true, "insufficientOrAbstainedBelow10Percent": false, "blindPromptLeakageAbsent": true, "checkpointSourceAndInputsMatch": true, "promptAndRubricVersionMatch": true, "requiredEvidenceComplete": false, "boundaryAnalysisClear": true}`.

Kelas 11 memakai rubrik SMA. Model IndoBERT lama berada di luar cakupan: semua head abstain dengan label/confidence/entropy null dan probabilitas kosong. Tidak ada prediksi atau perbandingan ketepatan IndoBERT yang sah untuk grade ini; label akhir mengikuti penilaian blind Gemini.

Kelompok difficulty tersedia di [difficulty_groups.json](difficulty_groups.json), [Easy](difficulty/Easy.json), [Medium](difficulty/Medium.json), dan [Hard](difficulty/Hard.json). `contentQualified` hanya menandai soal tanpa blocker konten; seluruh soal tetap menunggu ahli. Kategori kosong tetap diekspor. Item tanpa keputusan tersedia di [undecided](difficulty/undecided.json).
