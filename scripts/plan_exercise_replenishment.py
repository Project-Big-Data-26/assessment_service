"""Build a targeted, read-only replenishment backlog. No paid API or DB access."""
import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.ingestion.question_sync import class_from_chapter, coverage, load_sources, read_json, report_catalog, source_files
from app.services.exercise.replenishment import build_replenishment, render_replenishment
from app.services.exercise.visual_plan import preflight
from scripts.auto_inserter import write_report


def pending_generation(output_root, canonical):
    from app.services.exercise.workflow import verify_generation
    known = {question.qid for question in canonical}
    pending, files = [], []
    for manifest_path in sorted(output_root.glob("exercise/kelas*/batch*/generation_manifest.json")):
        base = manifest_path.parent
        manifest = read_json(manifest_path)
        if not manifest.get("complete"):
            continue
        checksum = verify_generation(base)
        master = read_json(base / "soal_exercise_db.json")
        metadata = read_json(base / "soal_exercise_meta.json")
        files += [manifest_path, base / "generation_state.json", base / "soal_exercise_db.json",
                  base / "soal_exercise_meta.json"]
        if (base / "generation_plan.json").exists():
            files.append(base / "generation_plan.json")
        for item in master["items"]:
            if item["_id"] in known:
                continue
            info = metadata[item["_id"]]
            owner, chapter = class_from_chapter(info["bab_id"])
            if owner != master["book"]:
                raise ValueError("Generated batch and metadata class differ")
            pending.append({"_id": item["_id"], "class_key": owner, "chapter_no": chapter,
                            "code": info["subbab_kode"], "level_target": info["level_target"],
                            "batch": base.name, "generation_mode": "new_batch", "manifest_sha256": checksum})
    # The user's later instruction explicitly allows append-only generation in batch01.
    for manifest_path in sorted(output_root.glob("exercise/kelas*/batch01/reference_replenishment_manifest.json")):
        base=manifest_path.parent;manifest=read_json(manifest_path)
        state=read_json(base/'reference_replenishment_state.json')
        from app.services.exercise.workflow import digest,reference_manifest_intact,reference_manifest_paths
        checksum=digest(manifest_path)
        if state.get('phase') not in ('generation_complete','validation_authorized'):
            continue
        if state.get('manifestSha256')!=checksum or not reference_manifest_intact(base,manifest):
            raise ValueError('Batch01 reference additions changed after generation')
        master=read_json(base/'soal_exercise_db.json');metadata=read_json(base/'soal_exercise_meta.json')
        files += [manifest_path,base/'reference_replenishment_state.json',*reference_manifest_paths(base,manifest).values()]
        for item in master['items']:
            if item['_id'] in known:continue
            info=metadata[item['_id']];owner,chapter=class_from_chapter(info['bab_id'])
            if owner!=master['book']:raise ValueError('Reference addition class differs')
            pending.append({'_id':item['_id'],'class_key':owner,'chapter_no':chapter,'code':info['subbab_kode'],
                            'level_target':info['level_target'],'batch':base.name,
                            'generation_mode':'batch01_additions','manifest_sha256':checksum})
    return pending, files


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output")
    parser.add_argument("--curriculum-report", type=Path, default=ROOT / "API_DOCUMENTATION/Pesan_eror.md")
    parser.add_argument("--directory", type=Path, default=ROOT / "runs/exercise_replenishment")
    args = parser.parse_args(argv)
    questions = load_sources(args.output)
    inventory = coverage(questions, report_catalog(args.curriculum_report))
    metadata_files = list(args.output.glob("exercise/kelas*/batch*/soal_exercise_meta.json"))
    targets = {}
    for path in metadata_files:
        targets.update({qid: row.get("level_target") for qid, row in read_json(path).items()})
    readiness = {key: preflight(key) for key in dict.fromkeys(r["class_key"] for r in inventory["rows"])}
    pending, pending_files = pending_generation(args.output, questions)
    plan = build_replenishment(inventory, questions, targets, readiness, pending)
    files = (source_files(args.output) + metadata_files +
             list(args.output.glob("pretest/kelas*/sesi_pretest.json")) + [args.curriculum_report] + pending_files)
    plan["source_sha256"] = {str(path.resolve()): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    plan["created_at"] = datetime.now(timezone.utc).isoformat()
    write_report(args.directory / "plan.json", plan)
    (args.directory / "plan.md").write_text(render_replenishment(plan), encoding="utf-8")
    print(f"Backlog: {plan['summary']}")
    print(f"Report: {args.directory / 'plan.md'}")
    print("New API calls: 0; database writes: 0; generation/validation not started.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
