# JSON Schema Reference

Kontrak yang benar-benar aktif dihasilkan dari FastAPI:

- [openapi.json](schemas/openapi.json), identik dengan `/openapi.json`;
- [implemented-api.schema.json](schemas/implemented-api.schema.json), Draft 2020-12, ID `urn:nalar:implemented-api:2.1.0`;
- [inventaris endpoint aktual](12_ENDPOINT_MASTER_REFERENCE.md).

`nalar-api.schema.json` tetap **desain gateway luas** untuk authoring/generation/multiple formats. Field/timing/response envelope-nya tidak identik dengan pilot aktif. Jangan menggunakannya untuk memvalidasi endpoint 2.1.0.

## Definisi implementasi

| Definisi | Penggunaan |
|---|---|
| V2ClassificationRequest / V2ClassificationResponse | Classifier 3×4×3 |
| ExpertAnnotationInput / DiscussionOutcomeInput / AdjudicationDecisionInput | Workflow manusia blind |
| AssessmentCreate / AssessmentReceipt | Blueprint human-gold immutable |
| ParticipantCreate / ParticipantReceipt | Provision token opaque, hanya operator |
| SessionReceipt / SessionCompleted | Start/completion |
| DeliveredItem / DeliveryFinished | DTO siswa tanpa key/mapping |
| ResponseCreate / ResponseReceipt | Single-choice atau skip, correctness server |
| MatrixAnalysisInput / ItemReference / AssumptionReview | Matriks 0/1/null dan metadata |
| ScreeningInput | Aggregation form/time window/whole attempt |
| EmpiricalAnalysisResult / CttItemMetrics / IrtResult | CTT, gate dan hasil IRT |
| EmpiricalDecisionInput | Keputusan empiris ahli, tanpa assignment label |

Requests menggunakan additionalProperties=false. Validator domain tetap memeriksa referensi/version/ownership, dimensi matriks, binary strict, human provenance dan idempotency; JSON Schema sendiri tidak membuktikan aturan lintas-field.

## Semantik penting

ResponseCreate hanya menerima satu public option atau skip eksplisit. Numeric/essay/matching/grid/multiple-response masih target. ResponseId dan deliveryInstanceId wajib; selected internal option, isCorrect, subject/assessment identity tidak dipercaya dari body.

EmpiricalAnalysisResult mempertahankan intendedDifficulty terpisah dari ctt/irt empiricalDifficulty; missing tetap null. Label AI/voting tidak berubah menjadi gold. Snapshot terikat policy/hash dan population/family/grade/version.

Runtime classifier mengenali parallel-v1, conditioned-difficulty-v1 dan grade-aware-ordinal-v2. Arsitektur aktif training mengikuti config/manifest, bukan asumsi dari nama file. Routing confidence+entropy v1 kompatibel dengan artifact confidence-only legacy.

## Regenerasi dan drift

```powershell
.\.venv\Scripts\python.exe scripts\export_api_contracts.py
.\.venv\Scripts\python.exe scripts\export_api_contracts.py --check
```

Schema diekspor dari model request/response yang digunakan route. Edit model/kode terlebih dahulu; jangan mengubah salinan schema manual. Error FastAPI aktif memakai detail; model/gold/psychometric readiness ditangani secara terpisah. Lihat [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).
