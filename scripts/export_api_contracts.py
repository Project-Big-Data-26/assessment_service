"""Export actual FastAPI contracts and route inventory; --check detects drift."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app

ROOT = Path(__file__).resolve().parents[1]


def artifacts():
    schema = app.openapi()
    definitions = schema["components"]["schemas"]
    # OpenAPI references become standalone JSON Schema references.
    raw = json.dumps(definitions, ensure_ascii=False).replace("#/components/schemas/", "#/$defs/")
    bundle = {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "urn:nalar:implemented-api:2.2.0",
              "title": "Nalar implemented FastAPI contracts", "$defs": json.loads(raw)}
    document = ["# Master Reference Endpoint", "",
                "Inventaris ini dihasilkan dari `app.main:app` oleh `scripts/export_api_contracts.py`. Versi API: **2.2.0**. "
                "Semua path dalam tabel tersedia dalam kode; readiness data, storage, provider, dan model tetap diperiksa pada runtime.", "",
                "| Method | Path | Akses | Ringkasan |", "|---|---|---|---|"]
    for path, operations in sorted(schema["paths"].items()):
        for method, operation in operations.items():
            if method not in {"get", "post", "put", "patch", "delete"}:
                continue
            if path == "/internal/v2/ui/login":
                access = "public login form"
            elif path == "/internal/v2/auth/login":
                access = "invite-only username/password"
            elif path == "/internal/v2/auth/logout":
                access = "staff cookie + CSRF"
            elif path.startswith("/internal/v2"):
                access = "operator cookie; CSRF untuk mutation"
            elif path.startswith("/api/v1/internal") or path.startswith("/api/v1/psychometrics"):
                access = "staff cookie atau X-Internal-API-Key" + ("; CSRF untuk cookie" if method == "post" else "")
            elif path.startswith(("/api/v1/assessments/", "/api/v1/sessions/", "/api/v1/responses")):
                access = "participant Bearer" + ("; Idempotency-Key" if method == "post" else "")
            else:
                access = "public diagnostics / advisory"
            document.append(f"| {method.upper()} | `{path}` | {access} | {operation.get('summary', '')} |")
    document += ["", "Dokumen operasional: [06 respons](06_STUDENT_RESPONSE_API.md), [07 CTT/IRT](07_PSYCHOMETRICS_API.md), "
                 "[08 delivery](08_ASSESSMENT_DELIVERY_API.md), [27 runbook](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).", "",
                 "Route authoring publik, async jobs/Redis, generation/variants, family/variant psychometrics, CAT, DIF, equating, "
                 "Claude API, dan promotion otomatis tetap desain lanjutan. Mereka tidak ada dalam inventaris implementasi ini.", "",
                 "OpenAPI aktual: `/openapi.json`; salinan terversi: [schemas/openapi.json](schemas/openapi.json). "
                 "Bundle kontrak aktual: [schemas/implemented-api.schema.json](schemas/implemented-api.schema.json). "
                 "`nalar-api.schema.json` menunjuk bundle kontrak aktual untuk kompatibilitas.", "",
                 "HTTP error FastAPI memakai `{\"detail\": ...}` dengan 401/403/404/409/422/503 sesuai penyebab. "
                 "`/v2/classify` tetap 503 ketika artefak research-only/unapproved/gagal gate. "
                 "CTT tetap dihitung jika data IRT kurang; respons analisis membawa `readiness.failures` dan status menunggu.", ""]
    return {
        ROOT / "API_DOCUMENTATION/schemas/openapi.json": json.dumps(schema, ensure_ascii=False, indent=2) + "\n",
        ROOT / "API_DOCUMENTATION/schemas/implemented-api.schema.json": json.dumps(bundle, ensure_ascii=False, indent=2) + "\n",
        ROOT / "API_DOCUMENTATION/12_ENDPOINT_MASTER_REFERENCE.md": "\n".join(document),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for path, value in artifacts().items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != value:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8")
    if stale:
        print("Contract drift: " + ", ".join(stale))
        return 1
    print("Implemented API contracts " + ("verified" if args.check else "exported"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
