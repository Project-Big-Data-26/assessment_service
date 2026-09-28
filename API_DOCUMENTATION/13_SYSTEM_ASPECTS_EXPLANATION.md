# Penjelasan Sistem Nalar per Aspek

## 1. Tujuan dan klaim

Arsitektur penuh menerima soal, membentuk versi konten, memverifikasi format/kunci, membangun gold blind, melatih IndoBERT, lalu pada fase berikutnya menambahkan Claude, review AI, pilot, dan psikometrik. Repo sekarang sudah menyediakan vertical slice kode IndoBERT 3×4×3 beserta anotasi blind, tetapi cloud, gold manusia, model final, Claude runtime, dan pilot belum tersedia. `/v1` C1–C6 tetap legacy.

## 2. Peran dan sumber bukti

| Sumber | Menjawab pertanyaan | Batas |
|---|---|---|
| Teacher | Apa isi soal, opsi, kunci dan tujuan belajar? | Penulis tidak menjadi reviewer soal sendiri |
| Deterministic gate | Apakah format, versi, opsi dan file valid? | Tidak membuktikan tuntutan kognitif |
| Answer verifier | Apakah kunci/solusi konsisten? | Tidak membuktikan label pedagogis |
| IndoBERT | Apa prediksi tiga head beserta uncertainty? | Prediksi statistik |
| Claude | Apakah usulan IndoBERT didukung bukti soal/solusi? | Proposal AI, tanpa suara final |
| Tiga ahli matematika | Apa label dan validitas konten yang disepakati? | Human gold memerlukan blind first pass |
| Psikometrik | Bagaimana item bekerja pada populasi tertentu? | Tidak otomatis mengubah domain/knowledge |

## 3. Authoring dan ekstraksi

Teacher membuat soal manual atau memperbaiki authoring candidate dari PDF/gambar/JSON/CSV/TXT/LaTeX. OCR, formula recognition, segmentation dan preview menyimpan halaman, bbox, confidence, engine dan warning. Hasil ekstraksi tidak langsung menjadi item final. Submit mengunci `contentVersion`; revisi substansial membentuk versi baru.

## 4. Validasi sebelum model

Canonicalization menghasilkan representasi konsisten untuk stem, opsi, rumus, visual, kunci, solusi, topik, kelas dan format. Deterministic validation memeriksa schema, referensi opsi, duplikasi, LaTeX, range dan integritas sumber. Answer verification memeriksa kunci/solusi dengan rule atau solver yang sesuai. Konflik jawaban menghentikan pipeline dan masuk quarantine.

## 5. KKO, task analysis, dan tiga label

KKO adalah fitur leksikal `features.lexical.detectedKKO` pada canonical item. KKO menjadi sinyal teks untuk IndoBERT; rubrik pakar memakai **analisis jalur penyelesaian minimal**. Bukti meliputi rutinitas prosedur, pemilihan strategi, perpindahan representasi, inferensi, generalisasi, justifikasi, objek pengetahuan dan kesesuaian kelas. Profil pakar tidak dimasukkan sebagai fitur input bila hanya diketahui sesudah anotasi.

Head 1 = domain TIMSS/AKM: `knowing/applying/reasoning`. Head 2 = knowledge dimension Revised Bloom: `factual/conceptual/procedural/metacognitive`. Head 3 = intended difficulty: `Easy/Medium/Hard`, relatif terhadap peserta sasaran. C1–C6 bukan target pipeline. Tipe soal pilihan ganda, benar/salah, matching, checkbox atau uraian tidak otomatis menetapkan domain. Rincian rubrik ada di [14](14_TAXONOMY_6X4X3_MAP.md).

## 6. IndoBERT dan Claude

Seed dataset pertama dibuat dari penilaian blind pakar agar model dapat di-fine-tune tanpa belajar dari label yang berasal dari dirinya sendiri. Model memakai stem, opsi, solusi/kunci terverifikasi, grade, topik, tujuan belajar, format, representasi dan fitur deterministik yang memang tersedia saat inferensi. Uji ablation mengukur manfaat KKO eksplisit. Split dataset berdasarkan source/item family, lalu laporkan macro-F1, F1 per kelas, confusion matrix, calibration dan OOD.

Saat produksi, IndoBERT menghasilkan probabilitas tiga head; Claude menerima hasil itu dan memberi `confirm/revise/abstain` dengan bukti. Karena Claude melihat hasil IndoBERT, keduanya adalah satu pipeline sequential. Kesepakatan keduanya tidak membentuk label final. Provider error membuat run retryable; model ID, prompt, rubric dan input hash disimpan sebagai provenance.

## 7. Tiga annotator

Ketiga ahli diverifikasi, menggunakan rubrik dan item versi yang sama. Mereka menilai secara blind dan submit immutable. Setelah itu mereka dapat melihat proposal AI dan merekam accept/revise/abstain. Keputusan per head: 3–0 bulat; 2–1 mayoritas dengan dissent; 1–1–1 atau bukti kurang masuk diskusi/senior adjudicator. Konflik kunci/konten tetap blocker meskipun label memiliki mayoritas. Agreement dihitung dari blind submissions sebelum diskusi. Blind consensus dipakai untuk train/eval; review akhir menjadi label operasional.

## 8. Pilot, respons, dan psikometrik

Hanya item `expert_validated` dengan kunci/solusi terverifikasi yang lolos policy pilot. Delivery menyimpan snapshot versi, menyembunyikan kunci, dan memberi public option IDs. Response terikat delivery instance serta dinilai server. CTT menyimpan `p` dan interval, discrimination, corrected point biserial bila total score tersedia, distraktor, waktu, ukuran sampel, populasi dan assessment family. IRT memerlukan data dan linking design yang memadai.

Intended difficulty tidak diganti langsung oleh empirical difficulty. Statistik buruk memicu pemeriksaan data, populasi, pengajaran, kunci, konten dan distraktor. Jika konten berubah, buat `contentVersion` baru dan ulang validasi; jika konten tidak berubah dan statistik stabil, validasi ahli penuh tidak perlu diulang.

## 9. Generasi varian dan feedback

Generasi varian adalah tahap lanjutan dari parent yang sudah expert-validated. Parameter, invariant, range, seed, solver, distraktor dan lineage harus terversi. Tiap varian menjalani validasi konten, IndoBERT→Claude dan tiga ahli untuk versi substantif sebelum pilot. Psikometrik per varian/family dapat mengubah kebijakan generator dan model difficulty melalui proses evaluasi terkontrol; ia tidak otomatis mengganti label domain/knowledge.

## 10. Data, keamanan, dan status

MongoDB target memisahkan `questions`, `question_versions`, `ai_decisions`, `expert_annotations`, `expert_decisions`, `delivery_instances`, `response_events` dan `psychometric_snapshots`. Event dan keputusan append-only; public DTO menyembunyikan kunci dan trace. Backend menyimpan Claude API key dan URI MongoDB di secret store, bukan browser atau repository. Folder gateway lama `project_assessment` sudah kosong, jadi seluruh gateway, expert UI, MongoDB dan Claude API adapter harus dibangun/migrasi. Detail koleksi ada pada [17](17_MONGODB_DATA_MODEL_ERD.md), konfigurasi provider pada [18](18_CLAUDE_PROVIDER_SETUP.md).

## 11. Rujukan

[TIMSS 2023 matematika](https://timssandpirls.bc.edu/timss2023/frameworks/pdf/T23_Frameworks_Ch1_Mathematics.pdf); [Framework AKM numerasi](https://pusmendik.kemdikbud.go.id/an/Framework_AKM_31032022.pdf); [Revised Bloom](https://eric.ed.gov/?id=EJ667155); [IndoBERT/IndoNLU](https://aclanthology.org/2020.aacl-main.85/); [Claude Messages API](https://platform.claude.com/docs/en/api/messages/create).

## 12. Kalibrasi sistem setelah merge

Repository kini memiliki subsistem batch pretest yang cukup matang pada lapisan ekstraksi: provenance per halaman, stimulus, cross-check Buku Guru, tiga distraktor beralasan, validator deterministik, status risiko, progress file, dan assembly berbasis kurikulum/prasyarat. Ia meningkatkan kualitas candidate, tetapi belum menambah endpoint produksi, penyimpanan MongoDB, gold label, delivery, atau respons siswa.

Arsitektur harus mempertahankan empat batas: (1) evidence sumber vs konten kanonis; (2) agen ekstraksi vs Claude reviewer IndoBERT; (3) heuristik assembly vs label/pengukuran psikometrik; dan (4) status staging vs lifecycle API. Ringkasan teknis serta gap dependensi/reproduksibilitas ada pada [dokumen 21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md).
