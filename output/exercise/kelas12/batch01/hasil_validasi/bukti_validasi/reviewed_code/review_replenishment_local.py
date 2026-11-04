"""Publish transparent Codex local reviews with zero API calls and confidence 0."""
import argparse
import ast
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.services.exercise.local_review import SCHEMA, POLICY, checksum, digest, review_question
from app.services.exercise.workflow import atomic_json, batch_lock, reference_manifest_intact

RUN = ROOT / "runs/exercise_replenishment/codex_batch01"
LOCAL = RUN / "local_review"
FAMILIES = ["replenishment_math.py", "replenishment_sd.py", "replenishment_smp.py",
            "replenishment_sma.py", "replenishment_tl.py"]


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def scope(name, progress):
    return {hashlib.md5(i.encode()).hexdigest()[:24] for key, job in progress["jobs"].items()
            if key.startswith(name+"-") for i in job["ids"]}


def reviewed_families():
    names, files = set(), {}
    for name in FAMILIES:
        path = ROOT / "app/services/exercise" / name
        files[path.relative_to(ROOT).as_posix()] = digest(path)
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
                continue
            position = {"numeric": 3, "text": 4}.get(node.func.id)
            if position is not None and len(node.args) > position and isinstance(node.args[position], ast.Constant):
                names.add(node.args[position].value)
    for path in (ROOT/"app/services/exercise/local_review.py", ROOT/"scripts/review_replenishment_local.py"):
        files[path.relative_to(ROOT).as_posix()] = digest(path)
    return names, files


def plan_class(name, ids, families):
    base = ROOT / "output/exercise" / name / "batch01"
    manifest = load(base / "reference_replenishment_manifest.json")
    if not reference_manifest_intact(base, manifest):
        raise ValueError("Generated inputs changed after the frozen manifest")
    master = load(base / "soal_exercise_db.json")["items"]
    meta = load(base / "soal_exercise_meta.json")
    by_id = {str(q["_id"]): q for q in master}
    assert ids <= by_id.keys() and len(by_id) == len(master)
    decisions = []
    for qid in sorted(ids):
        assert meta[qid].get("generator") == "codex:reference-parameterized-v1"
        try:
            decision = review_question(by_id[qid], meta[qid], families)
        except Exception as exc:
            decision = {"questionId": qid, "sourceHash": checksum(by_id[qid]),
                "method": "codex_direct_template_and_item_review", "apiCalls": 0,
                "confidence": 0, "confidenceMeasured": False, "trainingEvidenceQualified": False,
                "policyVersion": POLICY, "originalTarget": meta[qid]["level_target"],
                "concerns": [type(exc).__name__+": "+str(exc)], "checks": [], "repairs": [],
                "assessedLevel": None, "mathCognitiveDomain": None, "solution": meta[qid]["pembahasan"],
                "family": meta[qid]["jenis_soal"]}
            row = deepcopy(by_id[qid])
            row.update(status="inactive", cognitive_level=None, cognitive_score=None, confidence_score=0)
            decision.update(publishedQuestion=row, questionHash=checksum(row))
        decisions.append(decision)
    return master, meta, decisions


def local_metadata(source, decision, previous):
    result = deepcopy(source)
    if previous:
        result["previous_ai_assessment"] = previous.get("validasi")
    active = decision["publishedQuestion"]["status"] == "active"
    result["pembahasan"] = decision["solution"]
    result["local_review"] = {key: value for key, value in decision.items() if key != "publishedQuestion"}
    result["validasi"] = {"cognitive_level": decision["assessedLevel"],
        "cognitive_score": decision["publishedQuestion"]["cognitive_score"], "confidence_score": 0,
        "status": decision["publishedQuestion"]["status"],
        "validation_status": "codex_local_review_pass" if active else "local_revision_required",
        "level_sesuai_target": decision["assessedLevel"] == decision["originalTarget"],
        "math_cognitive_domain": decision["mathCognitiveDomain"],
        "validation_provider": "codex_direct_review", "validation_model": None,
        "requested_runs": 0, "api_runs": 0, "local_review_passes": 1,
        "validation_method": "codex_local_review", "label_provenance": "codex_local_assessment",
        "confidence_status": "not_measured", "confidence_method": "unmeasured_zero_by_user_request",
        "confidence_available": False, "consistency_measured": False,
        "training_evidence_qualified": False, "full_complete": True,
        "answer_key_status": "verified_locally" if active else "unverifiable_locally",
        "source_hash": decision["sourceHash"], "review_policy": POLICY}
    return result


def verify_local_publication(bundle):
    bundle = Path(bundle)
    manifest = load(bundle / "manifest.json")
    assert manifest["schemaVersion"] == SCHEMA
    for info in manifest["sourceFiles"].values():
        assert digest(info["path"]) == info["sha256"]
    for name, info in manifest["outputs"].items():
        assert digest(bundle/name) == info["sha256"] and (bundle/name).stat().st_size == info["bytes"]
    source = load(manifest["sourceFiles"]["exerciseEnvelope"]["path"])["items"]
    original_meta = load(manifest["sourceFiles"]["exerciseMetadata"]["path"])
    previous = load(manifest["sourceFiles"]["previousResults"]["path"])
    previous_meta = load(manifest["sourceFiles"]["previousMetadata"]["path"])
    audit = load(bundle / "bukti_validasi/codex_local_review.json")
    assert audit["apiCalls"] == 0 and audit["policyVersion"] == POLICY
    for path, sha in audit["reviewedTemplateFiles"].items():
        assert digest(bundle/"bukti_validasi/reviewed_code"/Path(path).name) == sha
    by_id = {q["questionId"]: q for q in audit["items"]}
    ids = set(manifest["localReview"]["questionIds"])
    assert len(by_id) == len(audit["items"]) and set(by_id) == ids
    rows = load(bundle/"validation_results.json")
    metadata = load(bundle/"validation_results_meta.json")
    source_by_id = {q["_id"]: q for q in source}
    old = {q["_id"]: q for q in previous}
    assert len(rows) == len(source) and [q["_id"] for q in rows] == [q["_id"] for q in source]
    assert set(metadata) == set(source_by_id)
    for row in rows:
        qid = row["_id"]
        if qid not in ids:
            assert row == old[qid], "A previously published non-target question changed"
            assert metadata[qid] == previous_meta[qid], "Previously paid metadata changed"
            continue
        decision = by_id[qid]
        assert decision["sourceHash"] == checksum(source_by_id[qid])
        assert row == decision["publishedQuestion"] and checksum(row) == decision["questionHash"]
        assert row["confidence_score"] == 0 and decision["apiCalls"] == 0
        assert set(row) == set(source_by_id[qid]), "Local publication changed the database schema"
        assert metadata[qid] == local_metadata(original_meta[qid], decision, previous_meta.get(qid))
        assert metadata[qid]["validasi"]["validation_method"] == "codex_local_review"
        assert metadata[qid]["validasi"]["training_evidence_qualified"] is False
    assert manifest["localReview"]["apiCalls"] == 0


def publish_class(name, master, meta, decisions, source_files):
    base = ROOT / "output/exercise" / name / "batch01"
    final = base / "hasil_validasi"
    with batch_lock(base):
        if (final / "manifest.json").exists() and load(final/"manifest.json").get("schemaVersion") == SCHEMA:
            verify_local_publication(final)
            return {"class": name, **load(final/"manifest.json")["localReview"]["summary"], "alreadyPublished": True}
        assert all((final/n).exists() for n in ["validation_results.json", "validation_results_meta.json", "manifest.json"])
        old_manifest = load(final/"manifest.json")
        for filename, info in old_manifest["outputs"].items():
            assert digest(final/filename) == info["sha256"], "Existing AI output changed before archival"
        previous, previous_meta = load(final/"validation_results.json"), load(final/"validation_results_meta.json")
        by_previous = {q["_id"]: q for q in previous}
        by_decision = {d["questionId"]: d for d in decisions}
        assert {q["_id"] for q in master} - by_decision.keys() <= by_previous.keys()
        archive = LOCAL / "backups" / name / digest(final/"manifest.json")[:20]
        archive.mkdir(parents=True, exist_ok=True)
        for filename in ["validation_results.json", "validation_results_meta.json", "manifest.json"]:
            target = archive / filename
            if target.exists():
                assert target.read_bytes() == (final/filename).read_bytes()
            else:
                shutil.copyfile(final/filename, target)
        staging = Path(tempfile.mkdtemp(prefix=name+"_", dir=LOCAL))
        rows = [by_decision[q["_id"]]["publishedQuestion"] if q["_id"] in by_decision else deepcopy(by_previous[q["_id"]]) for q in master]
        metadata = {q["_id"]: local_metadata(meta[q["_id"]], by_decision[q["_id"]], previous_meta.get(q["_id"]))
                    if q["_id"] in by_decision else deepcopy(previous_meta[q["_id"]]) for q in master}
        audit = {"schemaVersion": "codex-local-review-audit-v1", "policyVersion": POLICY,
                 "apiCalls": 0, "confidenceMeasured": False, "reviewedTemplateFiles": source_files,
                 "reviewer": "Codex direct review in this session", "items": decisions}
        code_dir = staging/"bukti_validasi/reviewed_code"
        code_dir.mkdir(parents=True, exist_ok=True)
        for path, sha in source_files.items():
            assert digest(ROOT/path) == sha
            shutil.copyfile(ROOT/path, code_dir/Path(path).name)
        atomic_json(staging/"validation_results.json", rows)
        atomic_json(staging/"validation_results_meta.json", metadata)
        atomic_json(staging/"bukti_validasi/codex_local_review.json", audit)
        summary = {"reviewed": len(decisions), "active": sum(d["publishedQuestion"]["status"] == "active" for d in decisions),
                   "inactive": sum(d["publishedQuestion"]["status"] != "active" for d in decisions),
                   "levels": dict(Counter(d["assessedLevel"] for d in decisions)),
                   "repaired": sum(bool(d["repairs"]) for d in decisions),
                   "targetLevelDiffers": sum(d["assessedLevel"] != d["originalTarget"] for d in decisions), "apiCalls": 0}
        report = (f"# Pemeriksaan lokal {name}\n\n{summary['reviewed']} soal tambahan diperiksa langsung oleh Codex. "
                  f"Active: {summary['active']}; inactive: {summary['inactive']}; perbaikan: {summary['repaired']}.\n\n"
                  "Confidence soal tambahan = 0 (belum diukur). Tidak ada panggilan Gemini/Groq untuk pemeriksaan ini. "
                  "Label merupakan penilaian isi oleh Codex dan pemeriksaan formula keluarga soal; bukan hasil blind API, gold manusia, atau hasil IRT. "
                  "Perhitungan dari stem juga diperiksa kembali untuk keluarga yang memiliki pemeriksa khusus. "
                  "Level mengikuti solusi minimum, tidak disamakan otomatis dengan target kuota. "
                  "Bukti ini tidak memenuhi persyaratan training N=3.\n\n"
                  f"Distribusi tambahan: {summary['levels']}. Level berbeda target: {summary['targetLevelDiffers']}.\n\n"
                  "Soal lama di luar cakupan tambahan dipertahankan persis. Arsip publikasi AI sebelumnya: " + str(archive) +
                  ".\n\nData ini publikasi lokal. Sinkronisasi database production tidak dijalankan.\n")
        for filename in ["README.md", "RINGKASAN_VALIDASI.md", "LAPORAN_VALIDASI.md"]:
            (staging/filename).write_text(report, encoding="utf-8")
        files = {"exerciseEnvelope": base/"soal_exercise_db.json", "exerciseMetadata": base/"soal_exercise_meta.json",
                 "previousResults": archive/"validation_results.json", "previousMetadata": archive/"validation_results_meta.json",
                 "previousAiManifest": archive/"manifest.json"}
        manifest = {"schemaVersion": SCHEMA, "createdAt": datetime.now(timezone.utc).isoformat(), "class": name,
            "sourceFiles": {k: {"path": str(p), "sha256": digest(p)} for k, p in files.items()},
            "outputs": {p.relative_to(staging).as_posix(): {"sha256": digest(p), "bytes": p.stat().st_size}
                        for p in staging.rglob("*") if p.is_file()},
            "localReview": {"policyVersion": POLICY, "apiCalls": 0, "confidenceScore": 0,
                            "questionIds": sorted(by_decision), "summary": summary}}
        atomic_json(staging/"manifest.json", manifest)
        verify_local_publication(staging)
        retired = archive/"full_ai_publication"
        for path in (final.resolve(), retired.resolve(), staging.resolve()):
            assert path.is_relative_to(ROOT.resolve()), "Publication move must remain inside the workspace"
        assert not retired.exists()
        final.rename(retired)
        try:
            staging.rename(final)
            verify_local_publication(final)
        except Exception:
            if final.exists():
                failed = archive/("failed_"+staging.name)
                assert failed.resolve().is_relative_to(ROOT.resolve()) and not failed.exists()
                final.rename(failed)
            retired.rename(final)
            raise
        return {"class": name, **summary}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--classes", nargs="+")
    args = parser.parse_args()
    LOCAL.mkdir(parents=True, exist_ok=True)
    progress = load(RUN/"progress.json")
    families, files = reviewed_families()
    results = []
    for name in args.classes or progress["classes"]:
        ids = scope(name, progress)
        assert ids
        base = ROOT/"output/exercise"/name/"batch01"
        # Explicit user instruction switches the whole replenishment scope to local mode.
        with batch_lock(base):
            state = load(base/"reference_replenishment_state.json")
            state.update(validationOwner="codex_local_review", reviewMode="local_without_external_api")
            atomic_json(base/"reference_replenishment_state.json", state)
        master, meta, decisions = plan_class(name, ids, families)
        atomic_json(LOCAL/(name+"_review_plan.json"), {"class": name, "apiCalls": 0, "items": decisions})
        if args.execute:
            result = publish_class(name, master, meta, decisions, files)
        else:
            result = {"class": name, "reviewed": len(decisions),
                      "active": sum(not d["concerns"] for d in decisions),
                      "failures": [{"id": d["questionId"], "kind": d["family"], "concerns": d["concerns"]}
                                   for d in decisions if d["concerns"]]}
        results.append(result)
        ledger = LOCAL/"progress.json"
        retained = {row["class"]: row for row in load(ledger).get("classes", [])} if ledger.exists() else {}
        retained.update({row["class"]: row for row in results})
        atomic_json(ledger, {"apiCalls": 0, "executed": args.execute, "classes": list(retained.values())})
        print(json.dumps(result, ensure_ascii=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
