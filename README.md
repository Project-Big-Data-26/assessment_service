# Nalar Question Intelligence

Sistem ekstraksi dan klasifikasi soal matematika memakai **label silver AI**, tanpa gate pelabelan guru atau gold. Alur: ekstraksi -> Gemini blind N=3/adjudikasi -> qualification silver -> snapshot immutable -> delivery siswa -> scoring server -> CTT/IRT -> feedback otomatis.

[Dokumentasi API](API_DOCUMENTATION/00_README.md), [integrasi silver](API_DOCUMENTATION/36_SILVER_OPERATIONAL_INTEGRATION.md), [hasil validasi semua kelas](output/pretest/README.md), dan [animasi](API_DOCUMENTATION/33_ANIMATED_DATA_FLOW.html).

```powershell
.\.venv\Scripts\python.exe scripts/build_operational_silver.py --snapshot-id silver-next --output tmp/silver-next.json
.\.venv\Scripts\python.exe -m uvicorn app.main:app --env-file .env --host 127.0.0.1 --port 8000
```

API 2.2.0 menyediakan registrasi dataset silver, blueprint, peserta, session, respons dan analisis. Service credential serta SQLite cukup untuk pilot; MongoDB opsional untuk akun operator dan metadata sumber/model. Endpoint pelabelan manusia telah dihapus.

Seluruh 580 soal punya tiga run AI sukses; konten bermasalah tetap ditahan. Label silver tidak menjamin semua soal lolos qualification. Label kesulitan awal dan hasil CTT/IRT disimpan terpisah.

Classifier v2 mendukung SD 1-6. Validasi AI/delivery mencakup reguler 1-12 dan TL 11-12. Training, calibration, anti-collapse dan evaluation gate tetap berlaku; migrasi tidak retrain atau mempromosikan artifact. CTT/IRT menunggu respons siswa dan bukti asumsi; demo numerik adalah synthetic.

Tes: `.\.venv\Scripts\python.exe -m pytest -q`. Kontrak: `scripts/export_api_contracts.py --check`. `v1` C1-C6 tetap legacy; v2 memakai knowing/applying/reasoning -> empat knowledge -> Easy/Medium/Hard.
