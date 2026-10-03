"""Convert active validation results in place; preserve full decisions in an audit."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.silver.exports import AUDIT_FILE, COMPACT_SCHEMA, compact_items, load_decision_bundle
from scripts.refresh_ai_validation_reports import digest, load, verify_bundle, write


def compact_bundle(source: Path, bundle: Path) -> dict:
    verify_bundle(source, bundle)
    manifest = load(bundle / "manifest.json")
    current = load(bundle / "validation_results.json")
    if current.get("schemaVersion") == COMPACT_SCHEMA:
        return {"class": source.parent.name, "alreadyCompact": True}
    audit = load_decision_bundle(bundle)
    checkpoint = load(Path(manifest["sourceFiles"]["blindCheckpoint"]["path"]))
    items = compact_items(load(source), audit["items"], load(bundle / "questions.json")["items"],
                          checkpoint, source.parent.name)
    audit_path = bundle / AUDIT_FILE
    audit_path.parent.mkdir(exist_ok=True)
    if audit_path.exists() and load(audit_path) != audit:
        raise ValueError("refusing to overwrite different audit evidence")
    if not audit_path.exists():
        # Preserve the original report byte for byte, including its original timestamps.
        audit_path.write_bytes((bundle / "validation_results.json").read_bytes())
    result = {"schemaVersion": COMPACT_SCHEMA, "collectionTarget": "questions",
              "visibility": "restricted_contains_answer_key", "createdAt": audit["createdAt"],
              "sourceClass": audit["sourceClass"], "subjectTrack": checkpoint.get("subjectTrack", "regular"),
              "summary": audit["summary"], "decisionAudit": {"path": AUDIT_FILE, "sha256": digest(audit_path)},
              "items": items}
    write(bundle / "validation_results.json", result)
    note = ("\nFormat `validation_results.json`: `items[]` mempertahankan field soal sumber, "
            "dengan `cognitive_level` dari label final AI dan delapan field `ai_metadata`. "
            "`cognitive_score` dan `confidence_score` bernilai null. "
            "Hanya `ai_metadata.validation_status = silver_ready` dapat dipakai untuk delivery; "
            "ID versi/hash memakai identitas snapshot operasional. Item yang ditahan memiliki ID versi/hash null. "
            "Bukti keputusan lengkap tersedia di [decision_audit.json](bukti_validasi/decision_audit.json), "
            "ditautkan melalui `ai_metadata.decision_id`. File ini memuat kunci jawaban dan hanya untuk backend.\n")
    readme = bundle / "README.md"
    text = readme.read_text(encoding="utf-8").replace(
        "`items[].llmAdvisory.advisoryLabels` bersama `finalRouting`",
        "`items[].cognitive_level` dan `items[].ai_metadata`")
    readme.write_text(text + note, encoding="utf-8")
    manifest["validationResultsSchemaVersion"] = COMPACT_SCHEMA
    for name in ("validation_results.json", AUDIT_FILE, "README.md"):
        path = bundle / name
        manifest["outputs"][name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    write(bundle / "manifest.json", manifest)
    verify_bundle(source, bundle)
    return {"class": source.parent.name, "itemCount": len(items), "routingCounts": result["summary"]["routingCounts"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    args = parser.parse_args()
    results = [compact_bundle(source, source.parent / "hasil_validasi")
               for source in sorted(args.source_root.glob("kelas*/soal_pretest_db.json"))]
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
