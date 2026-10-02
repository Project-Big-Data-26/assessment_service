# Aspek Sistem dan Kesiapan Implementasi

Pembaruan 2 Oktober 2026 mencakup backend pilot dan analisis empiris; kesiapan kode berbeda dari kecukupan data/model. Inventaris aktual: [12](12_ENDPOINT_MASTER_REFERENCE.md); runbook: [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).

| Aspek | Implementasi dan batas |
|---|---|
| Data soal | Import immutable babNN.json, source/version/hash; staging AI bukan gold |
| Taksonomi | knowing/applying/reasoning × factual/conceptual/procedural/metacognitive × Easy/Medium/Hard |
| Model | grade-aware-ordinal-v2; shared IndoBERT/LoRA, Head 3 ordinal + grade embedding |
| LLM | Gemini blind N=3/adjudication advisory; anchored legacy opt-in; Claude API target |
| Manusia | Tiga blind annotations, consensus/discussion/senior adjudication; initial votes immutable |
| Dataset | Group-aware 70/15/15, train-only class weights, validation calibration, frozen test |
| Delivery | Fixed form single-choice gold-only, opaque option IDs, immutable blueprint/mapping |
| Respons | Identity/correctness server, repeat-safe event, skip null, server timing, completed whole attempt |
| CTT | Wilson p/CI, rest-score discrimination, corrected item-total, complete-case KR-20, distractor/timing |
| IRT | Rasch/2PL/3PL regularized marginal likelihood, NA, readiness/assumptions/diagnostics |
| Feedback | Human retain/revise/quarantine; hold delivery dan exclusion dari freeze berikutnya |
| Penyimpanan | MongoDB gold/auth; SQLite pilot responses/snapshots/empirical decisions |
| Kontrak | OpenAPI + schema + endpoint inventory dihasilkan dari FastAPI |
| Keamanan | Cookie/CSRF staff, service token terbatas, participant token, IDOR, no-store; key tidak ke siswa |

Intended difficulty menilai tuntutan isi pada grade sasaran. CTT p dan IRT b mengukur perilaku pada populasi/form/waktu tertentu; keduanya tidak otomatis mengganti label intended. Respons siswa tidak mengubah domain atau knowledge tanpa keputusan manusia.

Missing/skip tidak dihitung salah. First/last memilih satu completed session per subject, bukan best answer per item. Populasi, grade dan versi tidak dipool. CTT total score/KR-20 memakai complete cases sehingga sampel efektif dapat lebih kecil; sistem menampilkan N dan null saat tak terukur.

IRT gate bukan bukti unidimensionality. Assumption review perlu evidence; convergence/boundary/Q3/uncertainty tetap diinspeksi. Semua empirical outputs researchOnly/reviewRequired tanpa gold authority. Minimum proyek, prior dan band lokal dicatat dalam policy/hash snapshot.

Gold, model final dan validitas siswa nyata belum otomatis tersedia karena backend selesai. Silver artifact tetap tidak servable; UI siswa, private media delivery, public authoring, CAT, linking/DIF/equating, generation dan multihost deployment masih target. Approval/promosi model mengikuti [25](25_GRADE_AWARE_ORDINAL_PIPELINE.md).
