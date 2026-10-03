"""Archive, rebuild and verify reports from resumable AI checkpoints, offline."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.silver import SilverLabelOutput, build_silver_prompt  # noqa: E402
from scripts.generate_silver_labels_kelas1 import input_hash, load_checkpoint  # noqa: E402

BASE = ROOT / "output/pretest"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, value: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def verify_evidence(source: Path, checkpoint: Path, grade: int) -> None:
    silver = load(checkpoint)
    track = silver.get("subjectTrack", "regular")
    load_checkpoint(checkpoint, source, digest(source), silver["model"], 3, grade, track=track)
    questions = {str(q["_id"]): q for q in load(source)}
    assert set(silver["items"]) <= set(questions), "checkpoint contains unknown questions"
    for qid, record in silver["items"].items():
        question = questions[qid]
        assert record["inputHash"] == input_hash(question), qid
        prompt = build_silver_prompt(question, grade=grade, track=track)
        for run in record.get("runs", []):
            if run["status"] != "success":
                continue
            assert run["promptHash"] == hashlib.sha256(prompt.encode("utf-8")).hexdigest(), qid
            canonical = SilverLabelOutput.model_validate(run["output"]).model_dump_json()
            assert run["responseHash"] == hashlib.sha256(canonical.encode("utf-8")).hexdigest(), qid
        adjudication = record.get("adjudication") or {}
        if adjudication.get("status") == "success":
            evidence = []
            for run in record.get("runs", []):
                if run["status"] != "success":
                    continue
                output = SilverLabelOutput.model_validate(run["output"])
                evidence.append({"runIndex": run["runIndex"], "contentStatus": output.contentStatus,
                                 "answerKeyStatus": output.answerKeyStatus,
                                 "verifiedAnswerKey": output.verifiedAnswerKey,
                                 "verifiedMinimalSolution": output.verifiedMinimalSolution,
                                 **{head: getattr(output, head).model_dump(mode="json") for head in
                                    ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")}})
            adjudication_prompt = (
                prompt
                + "\n\nADJUDIKASI SILVER: nilai ulang soal secara independen, lalu gunakan bukti run blind "
                "berikut hanya untuk menemukan sumber perbedaan. Jangan melakukan voting mekanis. "
                "Tidak ada prediksi IndoBERT atau estimasi kesulitan agen di dalam data ini.\n"
                + json.dumps(evidence, ensure_ascii=False, sort_keys=True)
            )
            assert adjudication["promptHash"] == hashlib.sha256(adjudication_prompt.encode("utf-8")).hexdigest(), qid
            canonical = SilverLabelOutput.model_validate(adjudication["output"]).model_dump_json()
            assert adjudication["responseHash"] == hashlib.sha256(canonical.encode("utf-8")).hexdigest(), qid
    for question in questions.values():
        for ref in question.get("image_url") or []:
            assert (source.parent / ref).is_file(), ref


def verify_bundle(source: Path, bundle: Path) -> None:
    manifest = load(bundle / "manifest.json")
    for info in manifest["sourceFiles"].values():
        assert digest(Path(info["path"])) == info["sha256"], info["path"]
    for name, info in manifest["outputs"].items():
        assert digest(bundle / name) == info["sha256"], name
        assert (bundle / name).stat().st_size == info["bytes"], name
    questions = {str(q["_id"]): q for q in load(source)}
    exported = load(bundle / "questions.json")["items"]
    results = load(bundle / "validation_results.json")["items"]
    expected = Counter({qid: 1 for qid in questions})
    assert Counter(q["questionId"] for q in exported) == expected
    assert Counter(q["questionId"] for q in results) == expected
    groups = load(bundle / "difficulty_groups.json")["groups"]
    assert Counter(q["question"]["questionId"] for group in groups.values() for q in group) == expected
    for q in exported:
        original = questions[q["questionId"]]
        assert q["stem"] == original["soal_text"]
        assert q["options"] == [{"label": o["option_id"], "text": o["text"]} for o in original["options"]]
        assert q["privateAnswerSpecification"]["answerKey"] == original.get("jawaban")
        assert q["visualAssets"] == (original.get("image_url") or [])
        assert q["visualAssetHashes"] == {ref: digest(source.parent / ref) for ref in q["visualAssets"]}


def run_script(script: str, *args: str, accepted: tuple[int, ...] = (0,)) -> None:
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / script), *args], cwd=ROOT,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
    if result.returncode not in accepted:
        raise RuntimeError(f"{script} failed ({result.returncode}): {result.stdout[-4000:]}")


def refresh_grade(entry: dict, session: str) -> dict:
    grade = entry["grade"]
    source = BASE / f"kelas{grade}" / "soal_pretest_db.json"
    checkpoint = ROOT / entry["checkpoint"]
    active = source.parent / "hasil_validasi"
    verify_evidence(source, checkpoint, grade)
    current = load(active / "manifest.json")
    verify_bundle(source, active)  # Also detect changed image bytes before promoting new evidence.
    # A matching locked checkpoint means this report is already current.
    if current["sourceFiles"]["blindCheckpoint"]["sha256"] == digest(checkpoint):
        return {"grade": grade, "rebuilt": False}
    snapshot = checkpoint.parent / session
    snapshot.mkdir()  # Never overwrite an immutable snapshot or archive.
    shutil.copy2(checkpoint, snapshot / "silver_labels.json")
    locked = snapshot / "silver_labels.json"
    previous = load(Path(current["sourceFiles"]["blindCheckpoint"]["path"]))
    updated = load(locked)
    retained = 0
    for qid, record in previous["items"].items():
        now = {r["runIndex"]: r for r in updated["items"][qid]["runs"]}
        for run in record["runs"]:
            if run["status"] == "success":
                assert now[run["runIndex"]] == run, "previously successful run was changed"
                retained += 1
    run_script("audit_grade_aware_pilot.py", "--source", str(source), "--checkpoint", str(locked),
               "--grade", str(grade), "--output-dir", str(snapshot / "audit"), accepted=(0, 2))
    run_script("build_blind_validation_bundle.py", "--source", str(source), "--checkpoint", str(locked),
               "--audit", str(snapshot / "audit/pilot_audit.json"), "--output-dir", str(snapshot / "bundle"))
    verify_bundle(source, snapshot / "bundle")
    shutil.copytree(active, snapshot / "previous_active_report")
    shutil.copytree(snapshot / "bundle", active, dirs_exist_ok=True)
    evidence = active / "bukti_validasi"
    evidence.mkdir(exist_ok=True)
    shutil.copy2(locked, evidence / "silver_labels.json")
    for name in ("pilot_audit.json", "PILOT_AUDIT.md"):
        shutil.copy2(snapshot / "audit" / name, evidence / name)
    verify_bundle(source, active)
    audit = load(snapshot / "audit/pilot_audit.json")
    result = {"verifiedAt": datetime.now(timezone.utc).isoformat(), "grade": grade, "rebuilt": True,
              "retainedPreviouslySuccessfulRuns": retained, "successfulRuns": updated["summary"]["successfulRuns"],
              "questionCount": len(load(source)), "activeAndVersionedOutputHashesMatch": True,
              "promptAndResponseHashesVerified": True, "sourceAndAssetsPreserved": True,
              "readyForExpansion": audit["readyForExpansion"],
              "failedAuditGates": [k for k, v in audit["gates"].items() if not v]}
    write(snapshot / "execution_verification.json", result)
    print(json.dumps(result), flush=True)
    return result


def refresh_backlog(backlog: dict) -> None:
    for entry in backlog["grades"]:
        grade = entry["grade"]
        source = BASE / f"kelas{grade}/soal_pretest_db.json"
        silver = load(ROOT / entry["checkpoint"])
        active = source.parent / "hasil_validasi"
        verify_evidence(source, ROOT / entry["checkpoint"], grade)
        verify_bundle(source, active)
        pending = []
        for index, q in enumerate(load(source), 1):
            record = silver["items"].get(str(q["_id"]), {})
            completed = {r["runIndex"] for r in record.get("runs", []) if r["status"] == "success"}
            missing = sorted(set(range(1, 4)) - completed)
            adjudication = bool(record.get("aggregate", {}).get("needsAdjudication"))
            if missing or adjudication:
                pending.append({"index": index, "questionId": str(q["_id"]), "missingRunIndices": missing,
                                "pendingAdjudication": adjudication, "stem": q["soal_text"]})
        distribution = load(active / "validation_results.json")["summary"]["advisoryLabelDistributions"]["intendedDifficulty"]
        entry.update(executionStatus=silver.get("executionStatus"), successfulRuns=silver["summary"]["successfulRuns"],
                     pendingAIQuestions=pending, pendingAIQuestionCount=len(pending),
                     pendingInitialRunCount=sum(len(q["missingRunIndices"]) for q in pending),
                     pendingAdjudicationCount=sum(q["pendingAdjudication"] for q in pending),
                     difficultyDistribution={label: distribution.get(label, 0) for label in ("Easy", "Medium", "Hard", "undecided")})
    backlog["checkedAt"] = datetime.now(timezone.utc).isoformat()
    backlog["pendingAIQuestionCount"] = sum(g["pendingAIQuestionCount"] for g in backlog["grades"])
    backlog["pendingInitialRunCount"] = sum(g["pendingInitialRunCount"] for g in backlog["grades"])
    write(BASE / "PENDING_AI_VALIDATION.json", backlog)
    readme = (BASE / "README.md").read_text(encoding="utf-8")
    start = readme.index("| Kelas |")
    end = readme.index("\n\nKelas 1–5 menggunakan batch", start)
    rows = ["| Kelas | Soal | Run sukses / target | Easy | Medium | Hard | Undecided | Soal perlu AI | Status |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for g in backlog["grades"]:
        n = g["grade"]
        counts = g["difficultyDistribution"]
        status = "Validasi AI lengkap" if not g["pendingAIQuestionCount"] else g["executionStatus"]
        values = " | ".join(str(counts[k]) for k in ("Easy", "Medium", "Hard", "undecided"))
        rows.append(f"| [{n}](kelas{n}/hasil_validasi/README.md) | {g['questionCount']} | {g['successfulRuns']}/{g['targetRuns']} | {values} | {g['pendingAIQuestionCount']} | {status} |")
    rows.extend(["", f"Sisa: **{backlog['pendingAIQuestionCount']} soal**, **{backlog['pendingInitialRunCount']} run awal**, ditambah adjudikasi yang diperlukan. [Daftar tepat per kelas, ID soal, dan run yang belum ada](PENDING_AI_VALIDATION.json). [Petunjuk resume](RESUME_AI_VALIDATION.md)."])
    (BASE / "README.md").write_text(readme[:start] + "\n".join(rows) + readme[end:], encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grades", nargs="+", type=int, choices=range(1, 13))
    parser.add_argument("--session", default="resume_" + datetime.now(timezone(timedelta(hours=7))).strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()
    if Path(args.session).name != args.session or args.session in (".", ".."):
        parser.error("session must be a single directory name")
    backlog = load(BASE / "PENDING_AI_VALIDATION.json")
    verification = []
    for entry in backlog["grades"]:
        if args.grades is None or entry["grade"] in args.grades:
            verification.append(refresh_grade(entry, args.session))
    refresh_backlog(backlog)
    execution_path = BASE / f"{args.session}_execution.json"
    previous = load(execution_path).get("grades", []) if execution_path.exists() else []
    accumulated = {g["grade"]: g for g in previous}
    for result in verification:
        if result["rebuilt"] or result["grade"] not in accumulated:
            accumulated[result["grade"]] = result
    write(execution_path, {"verifiedAt": backlog["checkedAt"],
                           "grades": [accumulated[n] for n in sorted(accumulated)],
                           "pendingAIQuestionCount": backlog["pendingAIQuestionCount"],
                           "pendingInitialRunCount": backlog["pendingInitialRunCount"],
                           "completeGrades": [g["grade"] for g in backlog["grades"] if not g["pendingAIQuestionCount"]]})
    print(f"Remaining AI questions: {backlog['pendingAIQuestionCount']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
