# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 31/42
- Tiga run sukses: 73.8%
- Insufficient/abstain: 28.6%
- Dominasi difficulty: 71.0%
- Distribusi difficulty: `{"Easy": 22, "Medium": 9}`

## Gate

- FAIL -- `allExpectedItemsPresent`
- FAIL -- `threeSuccessfulRunsAtLeast90Percent`
- FAIL -- `insufficientOrAbstainedBelow10Percent`
- PASS -- `blindPromptLeakageAbsent`
- PASS -- `checkpointSourceAndInputsMatch`
- PASS -- `promptAndRubricVersionMatch`
- FAIL -- `requiredEvidenceComplete`
- FAIL -- `boundaryAnalysisClear`

## Boundary analysis wajib

- `difficulty_Hard_absent`
