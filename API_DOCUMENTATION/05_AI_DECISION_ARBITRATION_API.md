# Keputusan AI dan Validasi Manusia Blind

Gold classifier/delivery berasal dari penilaian manusia, bukan AI. Kode blind annotation, consensus/discussion/senior adjudication tersedia dalam app/annotation, bergantung provisioning MongoDB dan akun ahli. Gemini blind silver merupakan workflow penelitian terpisah; Claude API/postprediction proposal tetap target.

## Endpoint manusia aktif

Login/logout dan UI berada pada /internal/v2/auth/* dan /internal/v2/ui*. Assignment: GET /assignments/next, GET /assignments/{assignment_id}, POST /assignments/{assignment_id}/submit; prefix /internal/v2. Submission terikat expert/questionVersion/rubric, cookie + CSRF, body strict dan idempotency key.

Annotator awal tidak menerima agent judgments, AI prediction, peer votes atau consensus. Annotation mencatat content validity, answer-key status, verified key/minimal solution, serta label/evidence atau abstain per head. Content/key tidak eligible harus abstain. Tiga identitas pakar berbeda dan konflik kepentingan harus dikelola workflow/provisioning; AI tidak dihitung sebagai pakar tambahan.

## Consensus dan adjudication

`scripts/materialize_consensus.py` membentuk keputusan gold-ready bila eligible, atau discussion case. Konsensus per head mencatat 3–0/2–1 dan dissent. 1–1–1, abstain/bukti kurang atau konflik konten/kunci memerlukan diskusi. `POST /internal/v2/adjudications/{adjudication_id}/discussion` dicatat coordinator/admin dengan tiga peserta awal yang sama. Jika unresolved, senior memakai `.../decision`.

Keputusan diskusi/senior tidak boleh menimpa settled head/key tanpa jalur version/review yang sesuai. Insufficient evidence dikarantina. Initial annotation tetap immutable; agreement diukur sebelum diskusi/adjudikasi, bukan setelah labels diseragamkan. Gate/rubrik dan perintah pada [22](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md).

## Silver blind LLM

Tiga initial Gemini runs tidak melihat IndoBERT atau vote lain. Hanya 3–0 diterima langsung sebagai silver; 2–1/abstain/conflict/content concern diarahkan ke adjudikasi AI terpisah. Audit hash mengunci checkpoint sebelum comparison offline. Provider failures bukan label. Anchored reviewer legacy memerlukan opt-in dan tidak digunakan untuk validasi baru. [25](25_GRADE_AWARE_ORDINAL_PIPELINE.md).

AI agreement tidak membuktikan kebenaran, dan bukan confidence terkalibrasi. Gold annotation manusia tetap blind terhadap AI pada suara awal. Artifact silver tetap researchOnly/unservable.

## Review empiris sesudah pilot

POST /api/v1/internal/psychometrics/snapshots/{snapshot_id}/decisions menerima retain/revise/quarantine, version dan rationale. Cookie + CSRF + expertId/role diperlukan; service token/admin saja tidak cukup. Keputusan append-only terikat snapshot/hash. Revise/quarantine menahan delivery dan exclude versi dari freeze gold berikutnya. Tidak ada assignment label baru pada endpoint empiris.

Konten baru perlu versioning dan human review sebelum snapshot training berikutnya. [07](07_PSYCHOMETRICS_API.md), [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md). Endpoint gateway public /expert-annotations atau AI pass lanjutan yang tidak tercantum pada [12](12_ENDPOINT_MASTER_REFERENCE.md) tetap target.
