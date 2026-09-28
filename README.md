# Nalar — prototype pemrosesan soal matematika

Repo aktif ini menyediakan **FastAPI Python** untuk ekstraksi, pemeriksaan jawaban terbatas, klasifikasi prototype, dan analisis CTT dasar. UI/gateway lama di `project_assessment` sudah tidak ada. Desain produk berikutnya dijelaskan di [API_DOCUMENTATION/00_README.md](API_DOCUMENTATION/00_README.md); kontrak di sana bertanda **target**, bukan endpoint yang sudah berjalan.

Lihat [diagram alur lengkap dan peta tech stack](API_DOCUMENTATION/20_END_TO_END_VALIDATION_FLOW.md) untuk urutan dari penyiapan gold dataset sampai keputusan sesudah pilot.

## Menjalankan prototype lokal

Prasyarat: Python 3.12 dan dependensi dalam [requirements.txt](requirements.txt). Dari root repo:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --port 8000
```

Buka `http://127.0.0.1:8000/docs` untuk kontrak **yang benar-benar tersedia**. Route Python meliputi `/health`, `/v1/model-info`, `/v1/extraction-info`, `/v1/verify-answer`, `/v1/classify`, dan `/v1/extract`. Endpoint gateway `/api/v1/...` dalam dokumen adalah rancangan migrasi. Menjalankan prototype tidak memerlukan MongoDB atau Claude.

## Arsitektur yang disepakati, belum terimplementasi penuh

Guru mengoreksi hasil ekstraksi; versi soal yang sudah lolos pemeriksaan format/kunci diprediksi oleh IndoBERT pada tiga head: domain kognitif matematika `knowing/applying/reasoning`, dimensi pengetahuan `factual/conceptual/procedural/metacognitive`, dan intended difficulty `Easy/Medium/Hard`. KKO hanya fitur leksikal. Claude mengaudit hasil IndoBERT secara berurutan, kemudian **tiga ahli matematika** memberi label blind dan review AI. Keputusan manusia yang sah mendahului pilot; data respons pilot memberi bukti psikometrik dan bukan pengganti validasi konten. Baca [arsitektur rinci](API_DOCUMENTATION/15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md) dan [rubrik](API_DOCUMENTATION/14_TAXONOMY_6X4X3_MAP.md).

Kode `app/classification/indobert.py`, `app/training/train.py`, dan konfigurasi model masih memakai label Bloom C1–C6. **Jangan** menggunakan endpoint prototype sebagai implementasi kontrak 3 × 4 × 3 atau memberi izin pilot otomatis.

## Claude dan MongoDB

[.env.example](.env.example) mencantumkan **nama variabel target** `ANTHROPIC_API_KEY`, `CLAUDE_MODEL`, `MONGODB_URI`, dan `AI_SERVICE_URL`. Belum ada loader/adapter Claude atau koneksi MongoDB aktif di Python. Instalasi CLI `claude` bukan bukti backend dapat memanggil Claude API. Jangan menaruh token atau URI berkredensial dalam Git; gunakan secret store untuk deployment. Tidak ada `.env` atau URI database aktual dari folder lama untuk dipindah. Lihat [panduan Claude](API_DOCUMENTATION/18_CLAUDE_PROVIDER_SETUP.md).

## Tes prototype

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```
