# Referensi schema

Kontrak endpoint aktif berasal dari Pydantic dan FastAPI. Gunakan [OpenAPI](schemas/openapi.json) atau [JSON Schema standalone](schemas/implemented-api.schema.json). `nalar-api.schema.json` menjadi pointer kompatibilitas ke bundle aktual.

`DatasetSnapshot` memuat TrainingRow silver, provenance keputusan AI, hash rows/expansion dan split manifest. `AssessmentCreate` grade 1-12 serta subjectTrack regular/tl. Kontrak respons empiris memuat reviewMode automated_ai, labelProvenance ai_silver dan routing AI review.

Tidak ada schema assignment pelabel manusia atau gold decision pada OpenAPI aktif. Export ulang dengan `scripts/export_api_contracts.py`; `--check` mendeteksi drift. Contoh gateway atau generation pada dokumen rancangan tidak dianggap endpoint aktif.
