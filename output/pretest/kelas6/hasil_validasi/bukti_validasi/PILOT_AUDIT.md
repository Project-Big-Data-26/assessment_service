# Audit Pilot Klasifikasi Grade-Aware

Status: **BERHENTI UNTUK ANALISIS**

- Item diproses: 25/25
- Tiga run sukses: 100.0%
- Insufficient/abstain: 0.0%
- Dominasi difficulty: 64.0%
- Distribusi difficulty: `{"Easy": 16, "Medium": 9}`

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

- `difficulty_Hard_absent`
