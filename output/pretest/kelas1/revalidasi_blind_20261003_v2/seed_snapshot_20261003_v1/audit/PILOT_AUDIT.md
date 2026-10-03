# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 24/50
- Tiga run sukses: 48.0%
- Insufficient/abstain: 52.0%
- Dominasi difficulty: 91.7%
- Distribusi difficulty: `{"Easy": 22, "Medium": 2}`

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

- `dominant_difficulty_share=0.917>0.90`
- `difficulty_Hard_absent`
