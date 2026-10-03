# Konfigurasi Claude dan Migrasi Environment

## Status audit lokal

Perintah `claude` ditemukan di mesin ini dan merge terbaru menambahkan `.claude/agents/ekstraktor-soal-pretest.md` serta skill `ekstrak-soal-pretest`. Claude Code kini benar-benar dipakai sebagai **development-time extraction agent** yang membaca Markdown/PNG dan menulis `babNN.json`. Penggunaan tersebut berjalan melalui sesi tooling pengembang, bukan melalui adapter backend, dan tidak mempunyai kontrak availability, billing, retry, audit response ID atau secret handling seperti service runtime.

Audit awal tidak menggambarkan secret/runtime saat ini. Root `.env` merupakan konfigurasi privat yang tidak disalin ke dokumentasi. **Claude API backend tetap target** karena adapter Anthropic belum tersedia. Provider terimplementasi adalah Gemini pada `app/llm` untuk blind silver sebelum comparison; `/v2/llm-info` memeriksa konfigurasi lokal tanpa network call. Claude Code ekstraksi tidak membuktikan Messages API. Lihat [21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md), [25](25_GRADE_AWARE_ORDINAL_PIPELINE.md), [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).

## Konfigurasi target

| Variabel | Kegunaan | Catatan |
|---|---|---|
| `ANTHROPIC_API_KEY` | Kredensial backend untuk Claude API | Hanya server/secret manager; jangan ke browser atau log |
| `CLAUDE_MODEL` | Model ID terkonfigurasi | Pilih model yang benar-benar tersedia pada akun; simpan ID pada decision record |
| `CLAUDE_API_BASE_URL` | Endpoint provider | Default `https://api.anthropic.com`; override hanya untuk gateway resmi yang disetujui |
| `MONGODB_URI` | Silver/auth MongoDB | Template placeholder; URI nyata tetap privat |
| `AI_SERVICE_URL` | Alamat internal FastAPI | Hanya worker/gateway |
| `APP_ENV`, `MODEL_CACHE_DIR` | Prototype Python | Sudah ada di root template |

Template aktif [`.env.example`](../.env.example) berisi Gemini, Atlas, classifier, auth, private assets dan pilot/CTT/IRT. Gunakan `uvicorn ... --env-file .env` agar konfigurasi dibaca sebelum import. CLI psikometrik membaca root `.env` tanpa menimpa environment proses. Secrets tidak dicetak. Variabel ANTHROPIC/CLAUDE di tabel di atas hanya kebutuhan adapter target, belum digunakan runtime; Gemini key tidak menjadi key Claude.

## Kontrak adapter target

Alur: `IndoBERT result + canonical item + rubricVersion → Claude Messages API → validated JSON proposal`. Gunakan backend SDK resmi atau `POST /v1/messages`, autentikasi server, `anthropic-version`, timeout dan retry terbatas untuk 429/5xx, idempotency/replay record, redaksi PII, serta schema validation. Claude harus menghasilkan per head: `confirm/revise/abstain`, label yang diusulkan, bukti dari soal/solusi dan rationale. Penggunaan structured outputs mengikuti dukungan model yang dipilih; respons tetap divalidasi di server. Simpan model ID dan prompt hash; jangan menyimpan key atau header.

Untuk istilah `CoT` (*chain-of-thought*) pada [flowchart](23_EMPIRICAL_VALIDATION_FEEDBACK_FLOW.md), desain prompt meminta Claude **menelaah** jalur solusi, membandingkan bukti dengan rubrik per head, dan memeriksa ulang usulannya. Keluaran aplikasi tetap berupa label/usulan, kutipan atau rujukan bukti yang relevan, dan alasan ringkas dalam JSON; jangan meminta atau menyimpan jejak penalaran mentah sebagai silver. Fitur *thinking* provider bersifat bergantung model dan konfigurasi serta harus diuji pengaruhnya terhadap kualitas, latency, biaya, dan privasi. [Panduan thinking resmi](https://platform.claude.com/docs/en/build-with-claude/thinking) menjelaskan batas tampilan ringkasan penalaran.

Contoh bentuk hasil internal:

```json
{
  "mathCognitiveDomain": {"action": "confirm", "label": "reasoning", "evidence": ["perlu menilai dua solusi"]},
  "knowledgeDimension": {"action": "revise", "label": "conceptual", "evidence": ["menguji hubungan antarkonsep"]},
  "intendedDifficulty": {"action": "abstain", "label": null, "evidence": ["kelas sasaran tidak tersedia"]}
}
```

Nilai `N=3` berarti tiga run AI untuk menguji konsistensi, bukan tiga orang pelabel. Endpoint reasoning Claude dapat memakai satu panggilan; hasilnya tetap advisory. Snapshot silver operasional memakai jalur blind N=3, adjudikasi saat diperlukan, serta pemeriksaan kunci, solusi dan bukti hash pada builder silver.

## Verifikasi sebelum dipakai

1. Pastikan akun dan API key untuk layanan Claude API memang tersedia pada lingkungan backend; keberadaan CLI saja tidak cukup.
2. Panggil Messages API dengan item fixture tanpa data siswa, pastikan model ID, response/schema, timeout, 429, error dan logging aman.
3. Uji fixture `confirm`, `revise`, `abstain`, kasus soal ambigu, serta KKO yang sama dengan proses berbeda.
4. Ukur akurasi IndoBERT saja dan IndoBERT→Claude terhadap blind AI silver; evaluasi per head, kelas dan format.
5. Baru aktifkan route review pakar dan pilot setelah penyimpanan versi, kontrol akses dan pemulihan error teruji.

Rujukan implementasi: [Messages API](https://platform.claude.com/docs/en/api/messages/create), [API overview](https://platform.claude.com/docs/en/api/overview), [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs).
