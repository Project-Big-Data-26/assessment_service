# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 44/44
- Tiga run sukses: 100.0%
- Insufficient/abstain: 2.3%
- Dominasi difficulty: 86.4%
- Distribusi difficulty: `{"Easy": 38, "Medium": 6}`

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
