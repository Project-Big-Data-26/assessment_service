# AI Taxonomy Screening API

## 1. Tujuan

Classification API menghasilkan evidence terstruktur untuk Bloom, knowledge dimension, dan intended difficulty. Hasilnya bukan gold label dan tidak ditetapkan teacher.

Pipeline target memakai dua jalur independen:

```text
canonical question
    |-- IndoBERT multi-head
    `-- LLM rubric ensemble
             |
             v
      agreement/risk engine
```

Konflik diteruskan ke automated LLM adjudication pada dokumen 05.

## 2. Endpoint

Endpoint target service/debug:

```http
POST /api/v1/ai/classify-question
GET  /api/v1/ai/model-info
```

Pada alur normal, frontend tidak perlu memanggil klasifikasi secara langsung. `POST /questions/{questionId}/submit` membuat workflow yang memanggil service internal dan menyimpan decision event.

## 3. Request

```json
{
  "questionId": "Q-001",
  "contentVersion": 2,
  "questionText": "Jika $x^2+5x+6=0$, tentukan akar-akarnya.",
  "questionType": "multiple_choice",
  "options": ["$-2$ dan $-3$", "$2$ dan $3$"],
  "subject": "Matematika",
  "grade": 10,
  "topic": "Aljabar",
  "subtopic": "Persamaan Kuadrat",
  "learningObjective": "Menerapkan pemfaktoran",
  "normalizedLatex": ["x^2+5x+6=0"]
}
```

Request service internal harus berasal dari canonical question snapshot, bukan body mentah browser.

## 4. Respons screening

```json
{
  "questionId": "Q-001",
  "contentVersion": 2,
  "decisionId": "AID-001",
  "status": "screened",
  "predictions": {
    "bloom": {
      "label": "C3",
      "confidence": 0.84,
      "entropy": 0.31,
      "margin": 0.42
    },
    "knowledgeDimension": {
      "label": "procedural",
      "confidence": 0.79,
      "entropy": 0.38,
      "margin": 0.34
    },
    "intendedDifficulty": {
      "label": "Medium",
      "confidence": 0.68,
      "entropy": 0.52,
      "margin": 0.18
    }
  },
  "ood": {"detected": false, "score": 0.11},
  "model": {
    "classifier": "indobert_multi_head",
    "version": "indobert-taxonomy-0.3.0"
  },
  "warnings": []
}
```

Confidence adalah output model yang harus dikalibrasi. Ia bukan probability bahwa label pasti benar.

## 5. LLM ensemble output

Setiap sampling LLM tahap lokal mengikuti strict schema berikut:

```json
{
  "bloom": "C3",
  "knowledgeDimension": "procedural",
  "intendedDifficulty": "Medium",
  "evidence": "Peserta menerapkan prosedur pemfaktoran untuk memperoleh akar."
}
```

LLM utama tidak melihat prediksi IndoBERT. Sampling disimpan sebagai decision event, lalu aggregator menghitung vote/self-consistency per head.

## 6. Model info

```http
GET /api/v1/ai/model-info
```

```json
{
  "taxonomyClassifier": {
    "type": "rules_baseline",
    "artifactReady": false,
    "version": "rules-0.1.0"
  },
  "llmEnsemble": {
    "configured": false
  },
  "answerVerifier": {
    "sympyReady": false
  }
}
```

UI boleh menampilkan status kemampuan, tetapi tidak boleh mengubah workflow berdasarkan nama provider tertentu.

## 7. Keputusan dan batas klaim

- Satu prediksi adalah `model_suggestion`.
- Stable LLM vote tetap bukan gold.
- IndoBERT-LLM agreement yang lolos risk gate adalah `ai_consensus`.
- Disagreement yang selesai melalui LLM adjudicator adalah `ai_adjudicated`.
- Unresolved disagreement adalah `quarantine_ai_conflict`.
- Difficulty pada tahap ini adalah `intendedDifficulty`; difficulty empiris berasal dari response data.

## 8. Status implementasi

FastAPI classification/rules baseline dan definisi training IndoBERT tersedia. Express telah memiliki adapter Gemini 3.8 Flash untuk solver, independent taxonomy ensemble, dan automated adjudicator melalui endpoint OpenAI-compatible. Setiap peran memakai strict JSON Schema, timeout, retry terbatas, sampling N=3/N=5, serta menyimpan model/prompt/rubric version pada decision lokal.

Adapter dianggap aktif hanya jika `GEMINI_API_KEY` tersedia secara lokal. API key tidak disimpan pada repository. Artefak IndoBERT layak-provisional, calibrated uncertainty/OOD, reference-set evaluation, dan risk policy yang disetujui masih belum tersedia; karena itu integrasi Gemini saja belum membuat soal boleh berstatus `provisional`.
