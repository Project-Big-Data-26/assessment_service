# Nalar — tahap authoring soal lokal

Repository ini menggabungkan FastAPI untuk ekstraksi/klasifikasi dan Express untuk API authoring. UI React pada `project_assessment/frontend` saat ini adalah studio input soal teacher sekaligus alat uji ekstraksi PDF. Kontrak target yang lebih luas ada di `API_DOCUMENTATION/`; tidak semua subsistem target sudah diimplementasikan.

## Menjalankan di Windows

Prasyarat: Python 3.12 dan Node.js. Jika belum ada virtual environment/dependensi, siapkan sekali dari root repository:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Set-Location project_assessment/backend; npm install
Set-Location ../frontend; npm install
Set-Location ../..
```

Lalu gunakan tiga terminal dari root repository:

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --port 8000
```

```powershell
Set-Location project_assessment/backend
npm start
```

```powershell
Set-Location project_assessment/frontend
npm run dev
```

Vite menampilkan alamat UI dan meneruskan `/api` ke Express pada port 5000. Authoring tidak memerlukan MongoDB. ID teacher lokal default adalah `local-teacher`; untuk menggantinya gunakan `LOCAL_TEACHER_ID` di environment backend. Jalankan satu proses gateway saja untuk file store ini. Ini bukan autentikasi multi-user atau konfigurasi produksi.

## Alur yang sudah tersedia

Teacher membuat draft, menyimpannya ke `data/local/`, mengedit dengan versi konten baru, lalu submit. Express membuat workflow run yang bisa dipoll. Worker lokal melakukan validasi struktur, mencoba verifikasi jawaban aritmetika terbatas, memanggil IndoBERT dan LLM independen, membandingkan label, lalu menjalankan risk gate. Kegagalan layanan AI tidak menghapus draft dan tidak menaikkan statusnya ke `provisional`. PDF analyzer tetap tersedia pada tab terpisah.

File di `data/local/` diabaikan Git. Soal yang ditulis di UI bukan dataset training otomatis. Jika isi folder ini penting, lakukan backup sendiri sebelum memindahkan atau menghapusnya.

## Agar keputusan AI sungguhan dapat selesai

- Sediakan artefak IndoBERT hasil fine-tuning di `models/indobert-multitask-v1/` (`manifest.json`, `model.pt`, `tokenizer/`). Model demo atau baseline rules tidak boleh menghasilkan `provisional`. Manifest hasil training dimulai dengan `approved_for_provisional: false`; approval baru dilakukan setelah evaluasi dataset dan kualitas model secara terpisah, bukan hanya karena training selesai.
- Adapter LLM telah dikonfigurasi untuk Gemini 3.8 Flash melalui endpoint OpenAI-compatible. Buat API key di Google AI Studio, buka `project_assessment/backend/.env`, lalu isi hanya nilai `GEMINI_API_KEY`. File `.env` diabaikan Git; jangan mengirim atau memasukkan key ke dokumentasi/source code.
- Tetapkan ambang confidence dan konsistensi per-head dari evaluasi pada `configs/ai_risk_policy.json`, lalu setujui kebijakan tersebut. File ini secara default belum disetujui; angka ambang tidak boleh dianggap universal.
- Verifier deterministik saat ini hanya mengenali ekspresi aritmetika sederhana. Soal lain memerlukan solver LLM; bila jawaban tidak bisa dibuktikan stabil, soal dikarantina.

Setelah key diisi, uji koneksi tanpa menjalankan seluruh workflow:

```powershell
Set-Location project_assessment/backend
npm run llm:check
```

Output berhasil hanya menampilkan provider, nama model, dan latency; API key tidak dicetak. Gemini memakai strict JSON Schema untuk solver, taxonomy screening, dan adjudicator. Saat ini ketiganya memakai `gemini-3.8-flash`, sampling screening `N=3`, dan reasoning effort `low`. Konfigurasi dapat diubah melalui `.env` setelah tersedia hasil evaluasi.

Untuk menjalankan evaluasi terkontrol solver, screening `N=3`, dan adjudicator:

```powershell
Set-Location project_assessment/backend
npm run llm:smoke
```

Runner memberi jarak request secara otomatis untuk proyek berkuota rendah, menggunakan retry terbatas, dan menyimpan hasil tanpa API key ke `data/local/evaluations/`. Hasil run 27 September 2026 didokumentasikan pada [`API_DOCUMENTATION/19_GEMINI_SMOKE_EVALUATION.md`](API_DOCUMENTATION/19_GEMINI_SMOKE_EVALUATION.md). Gemini menunjukkan hasil solver yang benar dan konsisten, tetapi kuota aktif belum cukup untuk menyelesaikan screening dan adjudication; integrasi belum boleh dipakai untuk keputusan `provisional`.

MongoDB, Redis, delivery siswa, psikometrik, dan generator variasi belum termasuk tahap ini. Endpoint lama di luar jalur authoring dapat tetap bersifat prototype.

## Tes

```powershell
.\.venv\Scripts\python.exe -m pytest -q
Set-Location project_assessment/backend; npm test
Set-Location ../frontend; npm run build
```
