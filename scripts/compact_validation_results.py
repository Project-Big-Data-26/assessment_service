"""Export validation results as source-shaped database arrays, preserving the audit."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.silver.exports import (AUDIT_FILE, DATABASE_SCHEMA, STATUS_POLICY, LEVEL_POLICY, SCORE_POLICY, CONFIDENCE_POLICY,
                               compact_items, database_items, final_label_support, load_decision_bundle)
from scripts.refresh_ai_validation_reports import digest, load, verify_bundle, write


def compact_bundle(source: Path, bundle: Path) -> dict:
    verify_bundle(source, bundle)
    manifest = load(bundle / "manifest.json")
    current = load(bundle / "validation_results.json")
    if isinstance(current, list) and manifest["databaseExport"]["schemaVersion"] == DATABASE_SCHEMA:
        return {"class": source.parent.name, "alreadyDatabaseArray": True}
    audit = load_decision_bundle(bundle)
    checkpoint = load(Path(manifest["sourceFiles"]["blindCheckpoint"]["path"]))
    originals = load(source)
    items = database_items(originals, audit["items"])
    metadata = compact_items(originals, audit["items"], load(bundle / "questions.json")["items"],
                             checkpoint, source.parent.name)
    audit_path = bundle / AUDIT_FILE
    audit_path.parent.mkdir(exist_ok=True)
    if audit_path.exists() and load(audit_path) != audit:
        raise ValueError("refusing to overwrite different audit evidence")
    if not audit_path.exists():
        # Preserve the original report byte for byte, including its original timestamps.
        audit_path.write_bytes((bundle / "validation_results.json").read_bytes())
    by_id = {d["questionId"]: d for d in audit["items"]}
    manifest["databaseExport"] = {
        "schemaVersion": DATABASE_SCHEMA, "collectionTarget": "soal",
        "visibility": "restricted_contains_answer_key", "sourceClass": audit["sourceClass"],
        "subjectTrack": checkpoint.get("subjectTrack", "regular"), "summary": audit["summary"],
        "decisionAudit": {"path": AUDIT_FILE, "sha256": digest(audit_path)},
        "statusPolicy": STATUS_POLICY, "cognitiveLevelPolicy": LEVEL_POLICY,
        "scorePolicy": SCORE_POLICY, "confidencePolicy": CONFIDENCE_POLICY,
        "metadataByQuestionId": {row["_id"]: {**row["ai_metadata"],
            "math_cognitive_domain": by_id[row["_id"]]["llmAdvisory"]["advisoryLabels"]["mathCognitiveDomain"],
            "final_label_supporting_runs": final_label_support(by_id[row["_id"]])} for row in metadata},
    }
    write(bundle / "validation_results.json", items)
    note = ("\nFormat `validation_results.json`: array dokumen dengan field yang sama seperti "
            "`soal_pretest_db.json`, tanpa envelope atau `ai_metadata`. `cognitive_level` memakai difficulty final AI "
            "(easy/medium/hard, huruf kecil). Domain knowing/applying/reasoning tetap disimpan sebagai "
            "`manifest.json.databaseExport.metadataByQuestionId[<_id>].math_cognitive_domain` dan dalam audit. "
            "`cognitive_score`: easy=600, medium=1000, hard=1400, "
            "sebagai skor awal kesulitan, bukan kemampuan siswa atau parameter IRT. "
            "`confidence_score = round(100 × min(dukungan label final tiap head / requestedRuns))`: "
            "100 untuk 3/3, 67 untuk 2/3, 33 untuk 1/3. Dukungan dihitung ulang dari run awal, "
            "bukan `supportingVotes` yang dapat merujuk label mayoritas sebelum adjudikasi. "
            "Skor ini mengukur konsistensi AI, bukan probabilitas akurasi; adjudikasi tidak menambah suara. "
            "`status` hanya active/inactive: silver_ready menjadi active; revision_required/needs_ai_review "
            "menjadi inactive. Hanya active boleh dipakai untuk delivery. Routing final asli tetap tersimpan "
            "di metadata `validation_status` dan audit, sehingga alasan item inactive tetap dapat diperiksa. "
            "Bukti keputusan lengkap tersedia di [decision_audit.json](bukti_validasi/decision_audit.json). "
            "`manifest.json.databaseExport` menyimpan summary, rumus, provenance, track dan metadata per `_id`, "
            "termasuk ID versi/hash snapshot operasional. ID versi/hash item yang ditahan tetap null. "
            "`kelas_id`, `berkas_id` dan pemetaan `subbab_id` tetap mengikuti sumber dan diselesaikan seeder backend. "
            "Path gambar tetap relatif terhadap folder kelas sumber; JSON ini memuat kunci jawaban dan hanya untuk backend.\n")
    readme = bundle / "README.md"
    text = readme.read_text(encoding="utf-8").split("\nFormat `validation_results.json`:")[0].replace(
        "`items[].llmAdvisory.advisoryLabels` bersama `finalRouting`",
        "`cognitive_level`, `cognitive_score`, `confidence_score` dan `status` pada setiap dokumen soal").replace(
        "`items[].cognitive_level` dan `items[].ai_metadata`",
        "`cognitive_level`, `cognitive_score`, `confidence_score` dan `status` pada setiap dokumen soal")
    readme.write_text(text + note, encoding="utf-8")
    manifest["validationResultsSchemaVersion"] = DATABASE_SCHEMA
    for name in ("validation_results.json", AUDIT_FILE, "README.md"):
        path = bundle / name
        manifest["outputs"][name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    write(bundle / "manifest.json", manifest)
    verify_bundle(source, bundle)
    return {"class": source.parent.name, "itemCount": len(items), "routingCounts": audit["summary"]["routingCounts"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    args = parser.parse_args()
    sources = sorted(args.source_root.glob("kelas*/soal_pretest_db.json"))
    before = {}
    for source in sources:
        bundle = source.parent / "hasil_validasi"
        verify_bundle(source, bundle)
        audit_path = bundle / AUDIT_FILE
        before[source] = {"sourceSha256": digest(source),
                          "decisionAuditSha256": digest(audit_path) if audit_path.exists() else digest(bundle / "validation_results.json")}
    results = [compact_bundle(source, source.parent / "hasil_validasi") for source in sources]
    checked = []
    for source in sources:
        bundle = source.parent / "hasil_validasi"
        verify_bundle(source, bundle)
        rows = load(bundle / "validation_results.json")
        assert digest(source) == before[source]["sourceSha256"], "source changed during export"
        assert digest(bundle / AUDIT_FILE) == before[source]["decisionAuditSha256"], "audit changed during export"
        checked.append({"class": source.parent.name, **before[source], "itemCount": len(rows),
                        "statusCounts": dict(Counter(row["status"] for row in rows)),
                        "confidenceCounts": dict(Counter(row["confidence_score"] for row in rows)),
                        "exactSourceFieldsAndOrder": True, "sourceAndAuditBytesPreserved": True,
                        "labelsScoresAndMetadataVerified": True,
                        "validationResultsSha256": digest(bundle / "validation_results.json")})
    report_dir = args.source_root / "silver_operational"
    report_dir.mkdir(exist_ok=True)
    write(report_dir / "database_format_verification.json", {
        "schemaVersion": DATABASE_SCHEMA, "statusPolicy": STATUS_POLICY, "cognitiveLevelPolicy": LEVEL_POLICY,
        "scorePolicy": SCORE_POLICY, "confidencePolicy": CONFIDENCE_POLICY,
        "classCount": len(checked), "itemCount": sum(c["itemCount"] for c in checked), "classes": checked,
        "newQuestions": 0, "newLlmCalls": 0, "sourceFilesChanged": False, "decisionAuditChanged": False,
    })
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
