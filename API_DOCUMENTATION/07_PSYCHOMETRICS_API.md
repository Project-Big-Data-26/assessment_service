# Psychometrics API

## 1. Tujuan

Psychometric service target mengukur perilaku empiris item **sesudah pilot** terhadap populasi sasaran. Ia tidak membuktikan `mathCognitiveDomain` atau `knowledgeDimension`. Pilot hanya menerima `contentVersion` dengan keputusan tiga ahli yang valid; analisis selalu diikat ke version, population, assessment family, varian, dan item family.

## 2. Endpoint target

```http
POST /api/v1/internal/psychometrics/items/{questionId}/screen
GET  /api/v1/psychometrics/items/{questionId}/snapshots
GET  /api/v1/psychometrics/variants/{variantId}/snapshots
GET  /api/v1/psychometrics/families/{itemFamilyId}/snapshots

POST /api/v1/internal/psychometrics/item-analysis
```

Command screening hanya service-to-service. Teacher/public frontend menggunakan GET summary yang sudah direduksi.

## 3. Aggregation key

```text
questionId + contentVersion
variantId + variantVersion
populationId + assessmentFamily + timeWindow
```

Respons dari versi/populasi berbeda tidak dicampur kecuali ada linking design yang eksplisit.

## 4. Metrik CTT

Difficulty index:

\[
p=\frac{B}{N}
\]

Simpan Wilson confidence interval agar ketidakpastian terlihat. Intended difficulty dan empirical difficulty tetap terpisah.

Discrimination:

- upper-lower discrimination;
- corrected point-biserial jika total score tersedia;
- negative discrimination flag.

Distraktor:

- selection rate;
- non-functional distractor;
- correlation/pattern terhadap total score;
- misconception-code effectiveness untuk generated variants.

Timing:

- median dan IQR;
- rapid-guess candidate rate;
- missing/late response rate.

## 5. Snapshot

```json
{
  "snapshotId": "PSY-001",
  "entityType": "variant",
  "entityId": "VAR-014",
  "questionId": "Q-001",
  "contentVersion": 2,
  "variantVersion": 1,
  "populationId": "GRADE-8-REFERENCE",
  "assessmentFamily": "PILOT-SMP8-GEO",
  "validResponseCount": 240,
  "metrics": {
    "difficultyIndex": 0.62,
    "difficultyCi95": [0.56, 0.68],
    "empiricalDifficulty": "Medium",
    "discrimination": 0.36,
    "correctedPointBiserial": 0.41,
    "distractorEfficiency": 0.67,
    "medianResponseTimeMs": 84000,
    "rapidGuessRate": 0.03
  },
  "quality": {
    "sampleStatus": "sufficient",
    "stability": "stable",
    "flags": [],
    "recommendedRouting": "empirically_screened"
  },
  "policyVersion": "ctt-screening-1.0.0",
  "createdAt": "2026-09-27T12:00:00Z"
}
```

## 6. Automated routing

```text
insufficient sample/CI wide
    -> collect_more_events

stable and acceptable
    -> empirically_screened

severe answer/discrimination/distractor flags
    -> hold_delivery + expert_content_review

variant bad, family rule repairable
    -> needs_regeneration

confirmed item defect or repeated failure
    -> revision_required / quarantined / retired
```

Threshold seperti minimum N, CI width, p category, dan discrimination cutoff berada dalam `policyVersion`, bukan di-hardcode pada frontend. Statistik yang buruk memicu pemeriksaan populasi, pengajaran, sampling, kunci dan distraktor. Perubahan stem, opsi, kunci atau solusi membuat `contentVersion` baru dan mengulang validasi format, IndoBERT→Claude serta tiga pakar. Jika konten tetap sama dan statistik stabil, anotasi penuh tidak perlu diulang.

## 7. Variant dan family analysis

Family-level analysis memeriksa:

- variasi difficulty antarvariant;
- kestabilan discrimination;
- distractor-rule performance;
- apakah parameter/transformasi tertentu menggeser difficulty;
- differential child-item behavior.

Family aggregation tidak menghapus statistik per variant. Satu variant buruk dapat di-retire tanpa menyimpulkan seluruh family buruk.

## 8. Feedback ke generator/model

Eligible snapshot dapat menghasilkan target:

```text
empirical p/hardness
discrimination
item-quality risk
expected response time
distractor effectiveness
```

Snapshot dengan sampel lemah hanya `observation_only`. Psychometric signal tidak digunakan untuk mengganti domain kognitif/knowledge label secara langsung. Label intended difficulty tetap tersimpan sebagai keputusan awal, sedangkan empirical difficulty adalah hasil pada populasi tertentu.

## 9. Status implementasi

Perhitungan CTT dasar tersedia di `app/evaluation/psychometrics.py` sebagai prototype. Gateway psikometrik, total-score join, immutable versioning, variant/family aggregation, Wilson CI policy, server-scored response, dan routing penuh masih target.
