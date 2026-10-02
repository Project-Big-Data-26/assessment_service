# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 3/42
- Tiga run sukses: 4.8%
- Insufficient/abstain: 95.2%
- Dominasi difficulty: 50.0%
- Distribusi difficulty: `{"Easy": 1, "Medium": 1}`

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
