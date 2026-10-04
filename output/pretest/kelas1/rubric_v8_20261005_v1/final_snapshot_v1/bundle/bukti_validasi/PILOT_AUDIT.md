# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 50/50
- Tiga run sukses: 100.0%
- Insufficient/abstain: 2.0%
- Dominasi difficulty: 92.0%
- Distribusi difficulty: `{"Easy": 46, "Medium": 4}`

## Gate

- PASS -- `allExpectedItemsPresent`
- PASS -- `threeSuccessfulRunsAtLeast90Percent`
- PASS -- `insufficientOrAbstainedBelow10Percent`
- PASS -- `blindPromptLeakageAbsent`
- PASS -- `checkpointSourceAndInputsMatch`
- PASS -- `promptAndRubricVersionMatch`
- PASS -- `requiredEvidenceComplete`
- FAIL -- `boundaryAnalysisClear`

## Boundary analysis wajib

- `dominant_difficulty_share=0.920>0.90`
- `difficulty_Hard_absent`
