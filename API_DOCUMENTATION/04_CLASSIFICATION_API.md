# Classification API: IndoBERT Grade-Aware dan Blind LLM

Pipeline aktif mengikuti [25](25_GRADE_AWARE_ORDINAL_PIPELINE.md): silver advisory diperoleh dari review Gemini blind **sebelum** prediksi IndoBERT dibuka, kemudian disagreement dibandingkan offline. Review LLM anchored setelah prediksi adalah jalur legacy opt-in, bukan protokol validasi baru. Claude API belum diimplementasikan.

## Endpoint aktual

- `POST /v2/classify`: kontrak `V2ClassificationRequest` → `V2ClassificationResponse`;
- `GET /v2/model-info`: metadata arsitektur, routing, research/gate/approval;
- `GET /v2/health/ready`: 503 bila model tidak servable;
- `GET /v2/llm-info`: konfigurasi Gemini lokal, tanpa network call;
- `POST /v1/classify`: baseline/legacy Bloom C1–C6, tetap advisory.

Input v2 mengikat question ID, version/hash, grade, stimulus/stem, opsi, topik/subtopik, solusi terverifikasi, visual transcript, KKO eksperimen dan provenance flags. Server runtime mengecek hash dan artifact integrity; unknown fields ditolak. Kontrak tepat tersedia di [schema implementasi](schemas/implemented-api.schema.json).

## Tiga head dan training

Head 1 knowing/applying/reasoning; Head 2 factual/conceptual/procedural/metacognitive; Head 3 intended difficulty Easy/Medium/Hard. KKO bukan label atau pemetaan deterministik.

Arsitektur default baru `grade-aware-ordinal-v2`: shared IndoBERT + LoRA query/value; Head 1/2 multiclass; Head 3 cumulative ordinal dengan grade embedding dan ordered cutpoints. `parallel-v1` dan `conditioned-difficulty-v1` tetap tersedia untuk reproduksi/ablation. Conditioning 775 fitur hanya mekanisme legacy, bukan default terbaru.

Gold berasal dari penilaian manusia blind, bukan prediksi sendiri atau jawaban siswa. Freeze memakai group-aware 70/15/15, source/stimulus/duplicate family tidak melintasi split. Class weight hanya train. Validation memilih checkpoint, temperature per head dan confidence+entropy routing. Frozen test terpisah dan terkunci sesuai gate. Detail [22](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md), [24](24_INDOBERT_FINETUNING_LLM_REASONING_DETAIL.md).

Artifact silver/research, tanpa approval, atau gagal data/anti-collapse/promotion gate tidak servable. Tidak ada fallback rules pada `/v2`. `reviewRequired=true` pada fase penelitian.

## Gemini dan manusia

Generator silver melakukan tiga review terpisah tanpa prediksi IndoBERT, agent difficulty atau vote lain. Tiga suara sepakat diterima sebagai silver; 2–1/abstain/conflict/content concern memerlukan adjudikasi AI terpisah. Audit hash mengunci checkpoint sebelum comparison. Agreement bukan calibrated confidence atau gold.

Runtime menyimpan JSON keputusan/bukti dan alasan singkat, bukan hidden chain-of-thought. Provider/model/config berasal dari environment; live generation memerlukan opt-in. Source image/key/solution evidence tetap dibutuhkan. Blind human annotations tidak melihat AI/peer pada suara awal.

## Hubungan dengan psikometrik

`/api/v1/internal/psychometrics/screen` menghasilkan p/CI CTT dan a/b/c IRT per versi/populasi/grade. Ia tidak mengganti domain, knowledge atau intended difficulty. Review empiris manusia dapat menahan versi; freeze dataset mengecualikan held version. Revisi harus melewati validasi manusia/versioning sebelum training baru. Lihat [07](07_PSYCHOMETRICS_API.md) dan [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).

Artefak `babNN.json`/hasil AI tetap staging/research; angka agent difficulty 1–5 bukan label gold atau parameter IRT.
