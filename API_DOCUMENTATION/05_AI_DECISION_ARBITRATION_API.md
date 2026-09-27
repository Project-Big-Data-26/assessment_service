# AI Decision dan Automated Adjudication API

## 1. Tujuan

Modul ini menggantikan workflow dua reviewer manusia. Ia menyimpan bukti dari deterministic gate, answer verifier, IndoBERT, LLM ensemble, agreement engine, risk engine, dan LLM adjudicator tanpa mencampurnya menjadi gold label.

Teacher tidak memanggil adjudication dan tidak memilih pemenang. Teacher hanya melihat safe summary serta dapat membuat authoring revision jika status meminta perbaikan.

## 2. Alur keputusan

```text
answer verification passed
        |
        +-------------------------------+
        v                               v
IndoBERT multi-head            independent LLM ensemble
        |                               |
        +---------------+---------------+
                        v
              agreement + risk engine
                        |
          +-------------+-------------+
          |                           |
          v                           v
 full agreement/low risk       disagreement/uncertain
          |                           |
          v                           v
    ai_consensus              LLM adjudicator
                                      |
                           +----------+----------+
                           |                     |
                           v                     v
                    ai_adjudicated      quarantine_ai_conflict
```

Adjudicator memakai prompt/rubric atau model/provider alternatif dan menerima ringkasan evidence, bukan sekadar disuruh mengikuti model dengan confidence tertinggi. Jumlah upaya dibatasi `Amax`.

## 3. Endpoint target

```http
GET  /api/v1/ai-decisions/{decisionId}
GET  /api/v1/questions/{questionId}/ai-decisions?contentVersion=2

POST /api/v1/internal/ai-decisions/screen
POST /api/v1/internal/ai-decisions/{decisionId}/adjudicate
```

Endpoint `internal` membutuhkan service identity dan tidak dibuka ke browser. Normal flow dipicu oleh question workflow worker.

## 4. Decision record

```json
{
  "decisionId": "AID-001",
  "questionId": "Q-001",
  "contentVersion": 2,
  "workflowRunId": "WF-001",
  "answerVerification": {
    "status": "passed",
    "method": "sympy",
    "verifierVersion": "answer-verifier-0.1.0"
  },
  "indobert": {
    "modelVersion": "indobert-taxonomy-0.3.0",
    "labels": {
      "bloom": "C3",
      "knowledgeDimension": "procedural",
      "intendedDifficulty": "Medium"
    },
    "uncertainty": {
      "bloomEntropy": 0.31,
      "knowledgeEntropy": 0.38,
      "difficultyEntropy": 0.52,
      "oodScore": 0.11
    }
  },
  "llmEnsemble": {
    "rubricVersion": "taxonomy-rubric-1.2.0",
    "sampleCount": 5,
    "aggregatedLabels": {
      "bloom": "C3",
      "knowledgeDimension": "procedural",
      "intendedDifficulty": "Hard"
    },
    "selfConsistency": {
      "bloom": 1.0,
      "knowledgeDimension": 0.8,
      "intendedDifficulty": 0.6
    }
  },
  "agreement": {
    "bloom": true,
    "knowledgeDimension": true,
    "intendedDifficulty": false,
    "all": false
  },
  "risk": {
    "score": 0.46,
    "band": "medium",
    "reasons": ["difficulty_disagreement"]
  },
  "adjudication": {
    "status": "resolved",
    "attempts": 1,
    "resolvedLabels": {
      "bloom": "C3",
      "knowledgeDimension": "procedural",
      "intendedDifficulty": "Medium"
    },
    "decisionType": "ai_adjudicated"
  },
  "finalRouting": "provisional",
  "createdAt": "2026-09-27T10:10:00Z"
}
```

Raw LLM prompt/response dapat disimpan pada restricted trace store. Public teacher DTO hanya menampilkan label, decision type, warning, dan routing yang aman.

## 5. Routing policy

Acceptance minimum:

- schema dan deterministic gate lolos;
- answer verification `passed`;
- evidence LLM merujuk field yang benar;
- uncertainty di bawah threshold per head;
- OOD tidak kritis;
- agreement penuh atau adjudication resolved;
- composite risk di bawah threshold;
- tidak ada warning kritis extraction/construct.

Routing target:

| Kondisi | Hasil |
|---|---|
| Semua syarat lolos | `provisional` |
| Struktur authoring dapat diperbaiki | `revision_required` |
| Answer conflict | `quarantine_answer_conflict` |
| Disagreement tidak selesai | `quarantine_ai_conflict` |
| OOD/construct risk tinggi | `quarantine_high_risk` |
| Konten invalid/non-repairable | `rejected_invalid` |

Threshold dan bobot disimpan pada `policyVersion`; tidak ditulis sebagai konstanta universal dalam frontend.

## 6. Immutability dan replay

- Decision record append-only.
- Re-run model membuat decision baru, bukan menimpa lama.
- Setiap record mengikat `questionId`, `contentVersion`, model, rubric, prompt template, retrieval set, dan policy version.
- Final routing pada Question menunjuk `activeDecisionId`.
- Replay harus dapat menggunakan snapshot input dan version manifest yang sama.

## 7. Batas klaim

`ai_adjudicated` berarti konflik model diselesaikan sesuai kebijakan sistem. Istilah tersebut tidak berarti expert-validated atau gold. Jika tidak ada bukti yang cukup, sistem harus abstain dan quarantine.

## 8. Status implementasi

Workflow ini adalah target. Backend prototype lama masih memiliki annotation manusia; endpoint/model tersebut perlu dimigrasikan dan tidak lagi menjadi kontrak target.
