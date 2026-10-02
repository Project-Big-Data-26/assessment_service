# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 5/60
- Tiga run sukses: 5.0%
- Insufficient/abstain: 95.0%
- Dominasi difficulty: 100.0%
- Distribusi difficulty: `{"Easy": 3}`

## Gate

- FAIL -- `allExpectedItemsPresent`
- FAIL -- `threeSuccessfulRunsAtLeast90Percent`
- FAIL -- `insufficientOrAbstainedBelow10Percent`
- PASS -- `blindPromptLeakageAbsent`
- PASS -- `checkpointSourceAndInputsMatch`
- PASS -- `promptAndRubricVersionMatch`
- PASS -- `requiredEvidenceComplete`
- FAIL -- `boundaryAnalysisClear`

## Boundary analysis wajib

- `dominant_difficulty_share=1.000>0.90`
- `difficulty_Medium_absent`
- `difficulty_Hard_absent`
