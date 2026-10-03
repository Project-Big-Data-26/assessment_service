# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 12/18
- Tiga run sukses: 66.7%
- Insufficient/abstain: 33.3%
- Dominasi difficulty: 75.0%
- Distribusi difficulty: `{"Easy": 9, "Medium": 3}`

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
