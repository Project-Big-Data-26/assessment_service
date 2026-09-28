# AI Decision dan Validasi Tiga Annotator

## 1. Tanggung jawab

Sistem menyimpan hasil IndoBERT dan proposal Claude secara berurutan, kemudian meminta tiga ahli matematika mereview item dan proposal tersebut. Claude tidak melakukan adjudikasi final. Gold untuk melatih dan menguji IndoBERT diambil dari penilaian ahli sebelum paparan AI.

## 2. Alur target

```text
format + answer gate
  → IndoBERT (3 head)
  → Claude (audit/olah hasil IndoBERT; confirm/revise/abstain)
  → tiga pakar memberi penilaian awal secara blind, lalu dikunci
  → proposal AI ditampilkan untuk review kedua
  → keputusan akhir pakar per head
  → suara 3–0 / 2–1 atau diskusi/adjudikasi 1–1–1
  → expert_validated atau unresolved/quarantined
```

Ketiga pakar harus berbeda identitas dan keahlian matematika diverifikasi. Penulis item tidak boleh menjadi pakar pada `contentVersion` miliknya. Mereka menilai Head 1, 2, 3 serta validitas konten dan kunci. Pada pass blind, pakar tidak melihat output AI maupun penilaian pakar lain. Setelah submission immutable, mereka melihat IndoBERT→Claude dan mencatat `accept/revise/abstain` per head beserta alasan perubahan. Hal ini masih merupakan review hasil Claude, tetapi jejak awal memungkinkan audit anchoring.

## 3. Endpoint target

```http
POST /api/v1/internal/ai-decisions/screen
GET  /api/v1/ai-decisions/{decisionId}
GET  /api/v1/questions/{questionId}/ai-decisions?contentVersion=2
POST /api/v1/expert-annotations/initial
POST /api/v1/expert-annotations/{annotationId}/ai-review
GET  /api/v1/expert-decisions/{decisionId}
POST /api/v1/internal/expert-decisions/{questionId}/resolve
```

Submit initial dan review memakai identity server, `Idempotency-Key`, `contentVersion`, serta optimistic concurrency. Read endpoint memfilter trace internal berdasarkan role.

## 4. Record minimum

```json
{
  "questionId": "Q-001",
  "contentVersion": 2,
  "aiDecisionId": "AID-001",
  "indobertLabels": {
    "mathCognitiveDomain": "reasoning",
    "knowledgeDimension": "procedural",
    "intendedDifficulty": "Medium"
  },
  "claudeProposal": {
    "mathCognitiveDomain": "reasoning",
    "knowledgeDimension": "conceptual",
    "intendedDifficulty": "Medium"
  },
  "expertDecision": {
    "annotationIds": ["EA-1", "EA-2", "EA-3"],
    "finalLabels": {
      "mathCognitiveDomain": "reasoning",
      "knowledgeDimension": "conceptual",
      "intendedDifficulty": "Medium"
    },
    "methodPerHead": {
      "mathCognitiveDomain": "unanimous_3_0",
      "knowledgeDimension": "majority_2_1",
      "intendedDifficulty": "unanimous_3_0"
    }
  }
}
```

AI tidak dihitung sebagai suara keempat. Keputusan `2–1` dicatat bersama dissent; mayoritas bukan bukti otomatis bahwa rubrik jelas. Kesepakatan awal pakar diukur **sebelum** diskusi/review AI, per head, dengan percent agreement dan Fleiss' kappa atau Krippendorff's alpha yang sesuai data dan missingness. Laporkan distribusi kelas dan interval ketidakpastian; agreement pascaadjudikasi tidak dilaporkan sebagai inter-annotator reliability.

## 5. Resolusi konflik

| Kondisi per head | Route |
|---|---|
| 3–0 | `unanimous_consensus` |
| 2–1 | `majority_consensus`, simpan alasan suara minoritas |
| 1–1–1 | Diskusi terstruktur berdasarkan rubrik, lalu senior adjudicator bila belum selesai |
| Abstain, konflik kunci, bukti kurang | `needs_expert_adjudication`; bila tetap tidak cukup `unresolved/quarantined` |

Diskusi tidak menimpa catatan awal. Konflik konten/kunci menghalangi pilot walaupun tiga label head memiliki mayoritas. Setiap perubahan substantif stem, opsi, kunci, solusi atau tujuan belajar membuat versi baru dan memicu ulang validasi.

## 6. Routing

`ai_screened` → `pending_expert_review` → `expert_validated` atau `needs_expert_adjudication` atau `revision_required/quarantined`. Hanya `expert_validated` yang dapat memenuhi gate pilot. Kegagalan Claude membuat `ai_processing_failed` yang retryable; tidak ada fallback label final otomatis. Pemisahan intended dan empirical difficulty tetap berlaku.

## 7. Status implementasi

Seluruh endpoint expert di atas adalah target. Python prototype yang tersedia belum mempunyai penyimpanan `expert_annotations`, konsensus tiga pakar, gateway Claude, ataupun route pilot. Desain Gemini/automated LLM adjudicator terdahulu telah digantikan; file lama `project_assessment` sudah tidak ada di worktree.
