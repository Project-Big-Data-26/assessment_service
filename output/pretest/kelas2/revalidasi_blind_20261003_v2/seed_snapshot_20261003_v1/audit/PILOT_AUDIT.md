# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 19/44
- Tiga run sukses: 43.2%
- Insufficient/abstain: 56.8%
- Dominasi difficulty: 78.9%
- Distribusi difficulty: `{"Easy": 15, "Medium": 4}`

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

- `difficulty_Hard_absent`
