# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 32/32
- Tiga run sukses: 100.0%
- Insufficient/abstain: 6.2%
- Dominasi difficulty: 61.3%
- Distribusi difficulty: `{"Easy": 19, "Medium": 12}`

## Gate

- PASS -- `allExpectedItemsPresent`
- PASS -- `threeSuccessfulRunsAtLeast90Percent`
- PASS -- `insufficientOrAbstainedBelow10Percent`
- PASS -- `blindPromptLeakageAbsent`
- PASS -- `checkpointSourceAndInputsMatch`
- PASS -- `promptAndRubricVersionMatch`
- FAIL -- `requiredEvidenceComplete`
- FAIL -- `boundaryAnalysisClear`

## Boundary analysis wajib

- `difficulty_Hard_absent`
