# Konfigurasi Claude dan Migrasi Environment

## Status audit lokal

Perintah `claude` ditemukan di mesin ini. Proses saat audit tidak memiliki `ANTHROPIC_API_KEY` maupun `MONGODB_URI`, dan root `.env` tidak ada. Folder `project_assessment` sudah kosong; karena itu tidak ada rahasia yang bisa dipindahkan. CLI interaktif dapat menggunakan autentikasi tersendiri dan **tidak membuktikan** worker backend sudah dapat memanggil Claude API. API integration, smoke test, dan kesiapan produksi belum terverifikasi.

## Konfigurasi target

| Variabel | Kegunaan | Catatan |
|---|---|---|
| `ANTHROPIC_API_KEY` | Kredensial backend untuk Claude API | Hanya server/secret manager; jangan ke browser atau log |
| `CLAUDE_MODEL` | Model ID terkonfigurasi | Pilih model yang benar-benar tersedia pada akun; simpan ID pada decision record |
| `CLAUDE_API_BASE_URL` | Endpoint provider | Default `https://api.anthropic.com`; override hanya untuk gateway resmi yang disetujui |
| `MONGODB_URI` | Database target | URI `localhost` pada root template hanya contoh development tanpa password |
| `AI_SERVICE_URL` | Alamat internal FastAPI | Hanya worker/gateway |
| `APP_ENV`, `MODEL_CACHE_DIR` | Prototype Python | Sudah ada di root template |

Template: [`.env.example`](../.env.example). Buat file `.env` yang diabaikan Git hanya di lingkungan eksekusi yang benar; kredensial produksi dikelola secret manager. Backend Node lama menggunakan `GEMINI_API_KEY` dan URL OpenAI-compatible; keduanya tidak dipakai untuk Claude target. `MONGO_URI=mongodb://mongodb:27017/...` pada Docker Compose lama adalah alamat **internal container**, bukan URI Atlas atau kredensial yang perlu dipindahkan. Jika database sungguhan sudah ada di luar folder ini, operator memasukkan URI ke secret store; dokumentasi tidak merekonstruksi atau menebak password.

## Kontrak adapter target

Alur: `IndoBERT result + canonical item + rubricVersion → Claude Messages API → validated JSON proposal`. Gunakan backend SDK resmi atau `POST /v1/messages`, autentikasi server, `anthropic-version`, timeout dan retry terbatas untuk 429/5xx, idempotency/replay record, redaksi PII, serta schema validation. Claude harus menghasilkan per head: `confirm/revise/abstain`, label yang diusulkan, bukti dari soal/solusi dan rationale. Penggunaan structured outputs mengikuti dukungan model yang dipilih; respons tetap divalidasi di server. Simpan model ID dan prompt hash; jangan menyimpan key atau header.

Untuk istilah `CoT` (*chain-of-thought*) pada [flowchart](20_END_TO_END_VALIDATION_FLOW.md), desain prompt meminta Claude **menelaah** jalur solusi, membandingkan bukti dengan rubrik per head, dan memeriksa ulang usulannya. Keluaran aplikasi tetap berupa label/usulan, kutipan atau rujukan bukti yang relevan, dan alasan ringkas dalam JSON; jangan meminta atau menyimpan jejak penalaran mentah sebagai gold. Fitur *thinking* provider bersifat bergantung model dan konfigurasi serta harus diuji pengaruhnya terhadap kualitas, latency, biaya, dan privasi. [Panduan thinking resmi](https://platform.claude.com/docs/en/build-with-claude/thinking) menjelaskan batas tampilan ringkasan penalaran.

Contoh bentuk hasil internal:

```json
{
  "mathCognitiveDomain": {"action": "confirm", "label": "reasoning", "evidence": ["perlu menilai dua solusi"]},
  "knowledgeDimension": {"action": "revise", "label": "conceptual", "evidence": ["menguji hubungan antarkonsep"]},
  "intendedDifficulty": {"action": "abstain", "label": null, "evidence": ["kelas sasaran tidak tersedia"]}
}
```

Nilai `N=3` bila digunakan untuk sampling Claude adalah uji self-consistency model, sedangkan tiga annotator adalah tiga manusia. Default implementasi dapat memakai satu panggilan Claude dan menguji N lebih besar pada evaluasi biaya, latency dan stabilitas. Jangan menjadikan persetujuan Claude sebagai gold.

## Verifikasi sebelum dipakai

1. Pastikan akun dan API key untuk layanan Claude API memang tersedia pada lingkungan backend; keberadaan CLI saja tidak cukup.
2. Panggil Messages API dengan item fixture tanpa data siswa, pastikan model ID, response/schema, timeout, 429, error dan logging aman.
3. Uji fixture `confirm`, `revise`, `abstain`, kasus soal ambigu, serta KKO yang sama dengan proses berbeda.
4. Ukur akurasi IndoBERT saja dan IndoBERT→Claude terhadap blind human gold; evaluasi per head, kelas dan format.
5. Baru aktifkan route review pakar dan pilot setelah penyimpanan versi, kontrol akses dan pemulihan error teruji.

Rujukan implementasi: [Messages API](https://platform.claude.com/docs/en/api/messages/create), [API overview](https://platform.claude.com/docs/en/api/overview), [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs).
