"""Version operational routing without changing AI judgments or frozen evidence."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.silver.policy import POLICY_VERSION, qualification, resolve_answer_key
from app.silver.exports import load_decision_bundle
from scripts.build_blind_validation_bundle import difficulty_groups, render_report
from scripts.build_validation_bundle_kelas1 import structural_validation
from scripts.refresh_ai_validation_reports import load, write, digest, verify_bundle, verify_evidence, write_active_index


def migrate(source: Path, archive: Path) -> dict:
    active = source.parent / "hasil_validasi"
    verify_bundle(source, active)
    manifest = load(active / "manifest.json")
    cp_path = Path(manifest["sourceFiles"]["blindCheckpoint"]["path"])
    verify_evidence(source, cp_path, manifest["class"])
    if manifest.get("operationalPolicyVersion") == POLICY_VERSION:
        return {"class": source.parent.name, "alreadyCurrent": True}
    backup = archive / source.parent.name
    if backup.exists():
        raise FileExistsError(f"archive already exists: {backup}")
    shutil.copytree(active, backup)
    cp = load(cp_path)
    originals = {str(q["_id"]): q for q in load(source)}
    questions_doc = load(active / "questions.json")
    questions = questions_doc["items"]
    result = load_decision_bundle(active)
    for item in result["items"]:
        original = originals[item["questionId"]]
        record = cp["items"][item["questionId"]]
        labels, route = qualification(record, structural_validation(original, source.parent), original)
        if labels != item["llmAdvisory"]["advisoryLabels"]:
            raise ValueError("migration must not change locked labels")
        if route == "silver_ready":
            key = resolve_answer_key(record["aggregate"].get("verifiedAnswerKey"), original["options"])
            if key != original.get("jawaban"):
                route = "needs_ai_review"
        item.pop("humanValidation", None)
        item["llmAdvisory"].pop("isGoldLabel", None)
        item.update(labelProvenance="ai_silver", reviewMode="automated_ai", finalRouting=route)
        item["llmAdvisory"]["labelProvenance"] = "ai_silver"
    for question in questions:
        question["verificationProvenance"] = "ai_silver"
    summary = result["summary"]
    summary.pop("goldLabelCount", None)
    summary.pop("humanReviewRequiredCount", None)
    summary.update(labelProvenance="ai_silver", silverReadyCount=sum(d["finalRouting"] == "silver_ready" for d in result["items"]),
                   routingCounts=dict(Counter(d["finalRouting"] for d in result["items"])))
    summary["contentQualifiedAdvisoryLabelDistributions"] = {
        head: dict(Counter(d["llmAdvisory"]["advisoryLabels"][head] for d in result["items"] if d["finalRouting"] == "silver_ready"))
        for head in summary["advisoryLabelDistributions"]}
    write(active / "questions.json", questions_doc)
    write(active / "validation_results.json", result)
    grouped = difficulty_groups(questions, result["items"], manifest["class"])
    grouped["subjectTrack"] = cp.get("subjectTrack", "regular")
    write(active / "difficulty_groups.json", grouped)
    for label, items in grouped["groups"].items():
        write(active / "difficulty" / f"{label}.json", {"schemaVersion": "blind-difficulty-subset-v1",
            "sourceClass": manifest["class"], "subjectTrack": cp.get("subjectTrack", "regular"),
            "intendedDifficulty": None if label == "undecided" else label,
            "labelProvenance": "ai_silver", **grouped["summary"][label], "items": items})
    model = load(active / "indobert_predictions.json")["model"]
    (active / "LAPORAN_VALIDASI.md").write_text(render_report(questions, result["items"], summary, cp, model, output_dir=active), encoding="utf-8")
    (active / "README.md").write_text(
        f"# Validasi AI silver — {source.parent.name}\n\n"
        f"{summary['itemCount']} soal, {cp['summary']['successfulRuns']} run blind sukses. "
        f"Routing: `{summary['routingCounts']}`. Label: `{summary['advisoryLabelDistributions']['intendedDifficulty']}`.\n\n"
        "Gunakan [validation_results.json](validation_results.json) untuk keputusan silver, "
        "[LAPORAN_VALIDASI.md](LAPORAN_VALIDASI.md) untuk bukti, dan [difficulty_groups.json](difficulty_groups.json) untuk kelompok kesulitan.\n\n"
        "Alur operasional memakai AI silver tanpa persetujuan pelabel manusia. Hanya `silver_ready` masuk snapshot delivery; "
        "`revision_required` dan `needs_ai_review` ditahan untuk AI revalidation. Jalankan `scripts/build_operational_silver.py` "
        "untuk snapshot yang memverifikasi checkpoint, kunci, solusi dan aset. IRT menyimpan difficulty empiris terpisah. "
        "Gate training, evaluasi dan mutu estimasi tetap berlaku. Prompt, rubrik, jawaban dan label blind terdahulu tetap terkunci.\n",
        encoding="utf-8")
    manifest.update(operationalPolicyVersion=POLICY_VERSION, labelProvenance="ai_silver", reviewMode="automated_ai",
                    operationalUpdatedAt=datetime.now(timezone.utc).isoformat())
    manifest["limitations"] = ["Silver labels originate from repeated judgments by one AI model.",
        "Model promotion remains subject to technical evaluation gates.", "Empirical difficulty requires student response data."]
    for name, info in manifest["outputs"].items():
        info.update(sha256=digest(active / name), bytes=(active / name).stat().st_size)
    write(active / "manifest.json", manifest)
    verify_bundle(source, active)
    return {"class": source.parent.name, "itemCount": summary["itemCount"], "routingCounts": summary["routingCounts"],
            "sourceAndEvidenceVerified": True, "labelsChanged": False, "newLlmCalls": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    parser.add_argument("--archive", type=Path, default=ROOT / "output/pretest/archive/pre_silver_operational_v1")
    args = parser.parse_args()
    entries = [migrate(p, args.archive) for p in sorted(args.source_root.glob("kelas*/soal_pretest_db.json"))]
    write(args.source_root / "silver_operational_migration.json", {"policyVersion": POLICY_VERSION, "classes": entries})
    write_active_index(args.source_root)
    print(f"Migrated {len(entries)} class bundles offline; no label changes or provider calls.")


if __name__ == "__main__":
    main()
