# Swagger dan Pengujian API

Jalankan `python -m uvicorn app.main:app --env-file .env --port 8000`. Swagger `http://127.0.0.1:8000/docs`, ReDoc `/redoc`, OpenAPI `/openapi.json`. Import URL OpenAPI ini ke Postman; collection gateway lama tidak tersedia.

## Urutan pemeriksaan

1. GET /health, /api/v1/capabilities dan /v2/psychometrics-info.
2. Jalankan CLI demo Rasch/2PL/3PL pada [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md) untuk memeriksa numerik tanpa secret/provider.
3. Daftarkan snapshot silver qualified melalui /api/v1/internal/silver/snapshots dan assessment; gunakan token operator hanya pada internal endpoints.
4. Provision token peserta → POST start dengan Idempotency-Key → GET next → POST response dengan public option/skip → POST complete.
5. POST screen dengan assumption review dan sample nyata yang memadai.
6. GET snapshot/aggregate dengan staff credential.
7. POST empirical decision memakai cookie AI dan CSRF; service token tidak menggantikan AI.

Isi Authorization peserta, Idempotency-Key, X-Internal-API-Key staff, dan X-CSRF-Token sesuai endpoint. Semua nilai secret lokal/privat; jangan memasukkannya ke exported collection.

## Respons yang diharapkan

- 401: credential peserta/internal salah;
- 403: role atau CSRF tidak sesuai;
- 404: resource tidak ada atau tidak dimiliki peserta;
- 409: immutable ID/content conflict, delivery finalized, expired/completed session, tidak ada completed data, atau versi ditahan AI;
- 422: schema/body/option mapping salah;
- 503: staff storage atau classifier artifact tidak tersedia/servable.

IRT gate gagal **tidak** berarti HTTP 500: CTT tetap tersedia dengan readiness.failures dan waiting status. Kurang data tidak diatasi dengan fake score atau fallback label. Error envelope aktif adalah detail.

## Verifikasi otomatis

```powershell
.\.venv\Scripts\python.exe scripts\export_api_contracts.py --check
.\.venv\Scripts\python.exe -m pytest -q
```

Inventaris [12](12_ENDPOINT_MASTER_REFERENCE.md) dan schema [09](09_JSON_SCHEMA_REFERENCE.md) berasal dari kode. Tests memeriksa math recovery, missing/gates, privacy, IDOR, concurrent delivery, retry, snapshot persist dan AI hold. Live Gemini calls dan cloud deployment tidak dijalankan oleh tes.
