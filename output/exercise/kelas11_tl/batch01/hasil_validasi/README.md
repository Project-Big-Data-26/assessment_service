# Hasil validasi ulang kelas 11

**Batch belum selesai:** 580/1197 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model LLM: `openai/gpt-oss-120b`; metode lanjutan blind N=1 dengan hasil N=3 terdahulu dipertahankan, rubrik kelas sasaran, verifikasi kunci/solusi, dan adjudikasi AI bila diperlukan. Label terkunci sebelum diagnostik IndoBERT.

Gunakan [validation_results.json](validation_results.json) untuk data hasil dan `cognitive_level`, `cognitive_score`, `confidence_score` dan `status` pada setiap dokumen soal. Baca [LAPORAN_VALIDASI.md](LAPORAN_VALIDASI.md) untuk soal, perhitungan confidence/entropy, run sesuai mode tiap soal, profil difficulty, adjudikasi, serta hasil akhir per soal. [questions.json](questions.json) memuat sumber dan spesifikasi jawaban terbatas; [indobert_predictions.json](indobert_predictions.json) memuat diagnostik artifact yang dipilih.

Distribusi: `{"mathCognitiveDomain": {"knowing": 217, "applying": 327, "reasoning": 30, "undecided": 617}, "knowledgeDimension": {"factual": 33, "conceptual": 262, "procedural": 279, "undecided": 617, "metacognitive": 0}, "intendedDifficulty": {"Easy": 443, "Medium": 128, "Hard": 3, "undecided": 617}}`. Routing: `{"silver_ready": 570, "needs_ai_review": 618, "revision_required": 3}`.

Token sukses tercatat: 1,751,679; tidak ada API call pada packaging. Provider dapat mencatat lebih banyak usage dari percobaan yang tidak menghasilkan output valid. Label tetap silver AI; CTT/IRT belum dihitung. Artifact diagnostik `indobert-3x4x3-silver-kelas1-v1` memakai dataset `kelas1-gemini-silver-n3-v1`. Packaging ini tidak melatih atau mempromosikan model; diagnostik tidak menentukan label blind.

Audit tidak menyetujui ekspansi/training bila gate belum lolos. Gate batch: `{"allExpectedItemsPresent": false, "threeSuccessfulRunsAtLeast90Percent": false, "insufficientOrAbstainedBelow10Percent": false, "blindPromptLeakageAbsent": true, "checkpointSourceAndInputsMatch": true, "promptAndRubricVersionMatch": true, "requiredEvidenceComplete": false, "boundaryAnalysisClear": true}`.

Mata pelajaran: Matematika Tingkat Lanjut (TL), dengan rubrik khusus TL.

N=1 memeriksa konten, kunci, solusi dan tiga label satu kali tanpa adjudikasi otomatis. Confidence numerik memakai dukungan IndoBERT untuk label akhir LLM; konsistensi antar-run tidak terukur; bukti satu run tidak memenuhi gate provenance training N=3.

Kelas 11 memakai rubrik SMA. Artifact diagnostik berada di luar cakupan kelas/jalur ini: semua head abstain dengan label/confidence/entropy null dan probabilitas kosong. Tidak ada prediksi atau perbandingan ketepatan IndoBERT untuk kelas/jalur ini; label akhir mengikuti penilaian blind LLM.

Kelompok difficulty tersedia di [difficulty_groups.json](difficulty_groups.json), [Easy](difficulty/Easy.json), [Medium](difficulty/Medium.json), dan [Hard](difficulty/Hard.json). `contentQualified` hanya menandai soal tanpa blocker konten; soal silver_ready dapat masuk snapshot operasional. Kategori kosong tetap diekspor. Item tanpa keputusan tersedia di [undecided](difficulty/undecided.json).

Format `validation_results.json`: array dokumen dengan field yang sama seperti `soal_exercise_db.json (items)`, tanpa envelope atau `ai_metadata`. `cognitive_level` memakai difficulty final AI (easy/medium/hard, huruf kecil). Domain knowing/applying/reasoning tetap disimpan sebagai `manifest.json.databaseExport.metadataByQuestionId[<_id>].math_cognitive_domain` dan dalam audit. `cognitive_score`: easy=600, medium=1000, hard=1400, sebagai skor awal kesulitan, bukan kemampuan siswa atau parameter IRT. Confidence N=3: `confidence_score = round(100 × min(dukungan label final tiap head / requestedRuns))`: 100 untuk 3/3, 67 untuk 2/3, 33 untuk 1/3. Dukungan dihitung ulang dari run awal, bukan `supportingVotes` yang dapat merujuk label mayoritas sebelum adjudikasi. Skor ini mengukur konsistensi AI, bukan probabilitas akurasi; adjudikasi tidak menambah suara. `status` hanya active/inactive: silver_ready menjadi active; revision_required/needs_ai_review menjadi inactive. Hanya active boleh dipakai untuk delivery. Routing final asli tetap tersimpan di metadata `validation_status` dan audit, sehingga alasan item inactive tetap dapat diperiksa. Bukti keputusan lengkap tersedia di [decision_audit.json](bukti_validasi/decision_audit.json). `manifest.json.databaseExport` menyimpan summary, rumus, provenance, track dan metadata per `_id`, termasuk ID versi/hash snapshot operasional. ID versi/hash item yang ditahan tetap null. `kelas_id`, `berkas_id` dan pemetaan `subbab_id` tetap mengikuti sumber dan diselesaikan seeder backend. Path gambar tetap relatif terhadap folder kelas sumber; JSON ini memuat kunci jawaban dan hanya untuk backend.

Mode lanjutan N=1: `confidence_score = round(100 * min(P(label akhir LLM) tiap head IndoBERT))`. Angka ini dukungan model terhadap label LLM, bukan konsistensi antar-run atau akurasi terukur. Probabilitas untuk label akhir digunakan meskipun berbeda dari argmax model. Nilai 0 dapat berarti dukungan model sangat kecil setelah pembulatan, atau bukti model tidak tersedia; bedakan melalui confidence_available dan confidence_final_label_probabilities di metadata. Hasil N=3 yang sudah selesai dipertahankan dengan confidence sebelumnya. Metode, jumlah run dan batas bukti training tersedia pada metadata per `_id`. Draft tetap confidence 0.


Exercise: lihat `RINGKASAN_VALIDASI.md`, `validation_results_meta.json` dan `export_status.json`. Metadata asli terhubung lewat `_id`. Periksa fullComplete sebelum menyatakan batch selesai.

Provider aktif: groq. 569 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.
