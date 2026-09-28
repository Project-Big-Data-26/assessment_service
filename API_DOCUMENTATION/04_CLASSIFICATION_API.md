# Classification API: IndoBERT → Claude

## 1. Kontrak dan status

Arsitektur jangka panjang adalah `canonical item → validasi format/kunci → IndoBERT → Claude`, tetapi fase yang diimplementasikan sekarang berhenti pada IndoBERT advisory. Kontrak `/v2` 3×4×3, gold blind, training, kalibrasi, dan artefak sudah tersedia dalam kode; Atlas, anotasi nyata, dan model final belum tersedia. Claude tetap fase berikutnya. Implementasi Bloom 6 kelas hanya legacy `/v1`.

Endpoint target internal/debug:

```http
POST /api/v1/internal/ai-decisions/screen
GET  /api/v1/ai/model-info
```

Workflow normal dipicu `POST /api/v1/questions/{questionId}/submit`. UI tidak menyuplai label, fitur pakar, atau confidence model.

## 2. Input dan provenance

Input dibentuk server dari `questionId + contentVersion + contentHash` yang terkunci. Format terdiri dari stem, opsi atau response prompt, kunci dan solusi **terverifikasi**, kelas/fase, topik, tujuan belajar, tipe respons, serta teks hasil OCR dengan rujukan visual. Jika solusi belum ada, jangan mengarangnya; catat `solutionUnavailable` dan jalankan kebijakan abstention/review. IndoBERT tekstual tidak memahami gambar yang tidak memiliki representasi teks; item visual dengan transkripsi tidak memadai diarahkan ke review.

```json
{
  "questionId": "Q-001",
  "contentVersion": 2,
  "grade": 8,
  "topic": "SPLDV",
  "responseFormat": "multiple_choice",
  "stem": "Perhatikan dua cara penyelesaian berikut...",
  "options": [{"id": "a", "text": "..."}, {"id": "b", "text": "..."}],
  "verifiedAnswer": {"optionIds": ["b"]},
  "verifiedSolution": "Langkah kedua tidak ekuivalen karena ...",
  "representations": ["text", "equation"]
}
```

Kunci dan solusi dipakai untuk membaca tuntutan tugas, bukan sebagai jawaban label. Jika solusi berasal dari manusia, provenance dan status verifikasinya harus dicatat. Sampel Claude yang mengolah prediksi tidak boleh dipakai untuk membuat solusi input IndoBERT pada run yang sama.

## 3. Fitur sebelum IndoBERT

| Kelompok | Contoh | Penggunaan |
|---|---|---|
| Teks | Stem, opsi, solusi terverifikasi | Input inti encoder |
| Kurikulum | Kelas, fase, topik, tujuan | Konteks, khususnya difficulty |
| Format dan representasi | Multiple choice, true/false, matching, checkbox, numeric, essay, grafik/tabel/rumus | Menjelaskan tugas dan bukti yang tersedia |
| Linguistik deterministik | KKO, negasi, kuantifier, permintaan alasan, panjang teks | Audit; input eksplisit hanya bila eksperimen membuktikan manfaat |
| Fitur pakar | Rutinitas, alasan domain, objek pengetahuan | Audit dan gold annotation; bukan input bila tidak tersedia otomatis saat inferensi |

KKO disimpan sebagai `features.lexical.detectedKKO`. Pada baseline, IndoBERT sudah membaca kata tersebut di stem. Varian `[KKO]` diuji terpisah; tidak ada aturan `kata → label`. KKO terutama dapat membantu Head 1 dan tidak menetapkan Head 2 atau Head 3.

## 4. Tiga head

```text
IndoBERT shared encoder
  ├─ mathCognitiveDomain: knowing | applying | reasoning
  ├─ knowledgeDimension: factual | conceptual | procedural | metacognitive
  └─ intendedDifficulty: Easy | Medium | Hard
```

Rubrik per head berada di [dokumen 14](14_TAXONOMY_6X4X3_MAP.md). Difficulty adalah penilaian awal yang terikat populasi sasaran; versi pertama dapat memakai klasifikasi tiga kelas dan membandingkannya dengan ordinal loss sebagai eksperimen. Setiap head menyimpan label, distribusi probabilitas, entropy/margin, status kalibrasi, OOD flag dan versi model. Confidence mentah bukan jaminan kebenaran.

Contoh output:

```json
{
  "decisionId": "AID-001",
  "indobert": {
    "modelVersion": "indobert-math-3x4x3-v1",
    "labels": {
      "mathCognitiveDomain": "reasoning",
      "knowledgeDimension": "procedural",
      "intendedDifficulty": "Medium"
    },
    "confidence": {
      "mathCognitiveDomain": 0.78,
      "knowledgeDimension": 0.69,
      "intendedDifficulty": 0.61
    },
    "ood": {"detected": false}
  }
}
```

## 5. Pelatihan awal dan evaluasi

Sebelum model versi pertama, kumpulkan seed dataset yang dinilai tiga pakar matematika secara blind memakai rubrik berversi. Bekukan penilaian awal; konsensus/adjudikasi manusia membentuk gold. Setelah split berdasarkan sumber dan keluarga soal, fine-tune IndoBERT pada train saja. Periksa class coverage, kualitas OCR/solusi, error tiap format/topik, macro-F1, F1 per kelas, confusion matrix dan kalibrasi pada test beku. Perbandingan fitur: stem+opsi; tambah metadata; tambah solusi terverifikasi; lalu tambah KKO eksplisit. Challenge set harus memuat KKO yang sama dengan label berbeda. Tidak ada klaim siap produksi hanya karena training selesai.

Landasan model: [IndoNLU/IndoBERT](https://aclanthology.org/2020.aacl-main.85/), [BERT fine-tuning](https://aclanthology.org/N19-1423/), [TIMSS 2023](https://timssandpirls.bc.edu/timss2023/frameworks/pdf/T23_Frameworks_Ch1_Mathematics.pdf).

## 6. Claude sebagai pengolah hasil

Claude menerima item yang sama, prediksi dan probabilitas IndoBERT, serta rubrik. Claude memeriksa bukti per head, dapat mengonfirmasi, merevisi, atau abstain, lalu mengembalikan JSON tervalidasi schema. Simpan `indobertLabels`, `claudeProposedLabels`, `actionPerHead`, `evidenceSpans`, alasan, model ID, prompt/rubric version, response ID, latency dan error. Panggilan berulang, bila dipakai, mengukur self-consistency Claude; bukan suara annotator.

Claude melihat hasil IndoBERT sehingga kedua keluaran **bukan pengukuran independen**. Evaluasi terpisah melaporkan IndoBERT saja dan pipeline IndoBERT→Claude terhadap gold blind. Jika provider gagal, keputusan tidak dinaikkan menjadi final. Parameter API aktif berasal dari environment/config, tanpa nama model hard-coded di kontrak. Lihat [dokumen 18](18_CLAUDE_PROVIDER_SETUP.md).

## 7. Batas implementasi

`app/classification/indobert.py`, `app/training/train.py` dan `configs/model_config.yaml` tetap memakai Bloom 6 kelas khusus legacy `/v1`. Runtime terpisah `app/classification/v2`, trainer `app/training/v2`, konfigurasi v2, dan endpoint `/v2` sudah memakai kontrak 3×4×3. `/v2/classify` tetap 503 sampai artefak gold terlatih tersedia dan tidak fallback ke rules. Folder `project_assessment` lama tidak lagi menyediakan gateway Gemini; Claude API bukan bagian fase implementasi ini.

## 8. Hubungan dengan ekstraksi agentic pretest

Pipeline agentic yang baru belum memanggil classifier. Field `tingkat_kesulitan` 1–5 dibuat agen untuk memilih soal sesi dan tidak boleh dijadikan label latihan Head 3. Demikian pula `jawaban_agen`, `status_kunci` dan alasan distraktor adalah evidence staging, bukan gold tiga head.

Setelah adapter membuat canonical `QuestionVersion`, classifier menerima teks stimulus + pertanyaan, opsi, solusi/kunci yang telah melewati gate, metadata kelas/topik/subbab dan provenance visual yang dapat direpresentasikan. Record klasifikasi harus mereferensikan content hash/version hasil import; jangan mengklasifikasikan `soal_pretest_db.json` secara lepas karena file itu kehilangan sebagian provenance kaya dari `babNN.json`. Claude Code pada tahap ekstraksi berbeda dari Claude API postprocessor pada bagian 6. Lihat [dokumen 21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md).
