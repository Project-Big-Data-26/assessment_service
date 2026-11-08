"""Package verified delivery copies and narrow ID-addressed text repair patches."""
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.services.exercise.workflow import atomic_json, digest, load


def package(root=ROOT):
    audit = load(root / "runs/latex_audit/report.json")
    if not audit["deliveryWritten"] or audit["renderErrors"] or audit["outsideMath"]:
        raise ValueError("delivery package requires a successful complete KaTeX audit")
    for item in audit["files"]:
        if digest(root / item["source"]) != item["sourceSha256"] or digest(root / item["delivery"]) != item["deliverySha256"]:
            raise ValueError("source or delivery changed since the renderer audit")
    grouped, cache = {}, {}
    for change in load(root / "runs/latex_audit/changes.json"):
        source = Path(change["file"])
        if not source.name.endswith("_db.json"):
            continue
        if str(source) not in cache:
            cache[str(source)] = load(root / source)
        document = cache[str(source)]
        tokens = change["pointer"].split("/")[1:]
        if tokens[0] == "items":
            tokens.pop(0)
        index = int(tokens.pop(0))
        rows = document["items"] if isinstance(document, dict) else document
        row = rows[index]
        key = (str(source), str(row["_id"]))
        entry = grouped.setdefault(key, {"source": str(source), "_id": row["_id"],
            "class": row.get("kelas_id"), "changes": []})
        repair = {"fieldPath": "/".join(tokens), "before": change["before"], "after": change["after"]}
        if tokens[0] == "options" and len(tokens) > 2:
            repair["option_id"] = row["options"][int(tokens[1])]["option_id"]
        entry["changes"].append(repair)
    base = root / "output/latex_ready"
    patches = {"schemaVersion": "latex-text-repair-patches-v1", "questionCount": len(grouped),
        "fieldCount": sum(len(row["changes"]) for row in grouped.values()),
        "applyPolicy": "match _id and option_id; change only listed text if before matches; after is an idempotent no-op",
        "items": list(grouped.values())}
    atomic_json(base / "repair_patches.json", patches)
    manifest = load(base / "manifest.json")
    manifest["repairPatches"] = {"path": "repair_patches.json", "sha256": digest(base / "repair_patches.json"),
                                 "questionCount": len(grouped)}
    atomic_json(base / "manifest.json", manifest)
    destination = root / "output/latex_delivery_ready.zip"
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(base.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(base).as_posix())
        archive.write(root / "API_DOCUMENTATION/44_LATEX_DELIVERY_REPAIR.md", "integration/README.md")
        archive.write(root / "API_DOCUMENTATION/interactive/question_math.js", "integration/question_math.js")
    print(json.dumps({"archive": str(destination), "bytes": destination.stat().st_size,
        "sha256": digest(destination), "questionsWithRepairs": len(grouped), "fieldRepairs": patches["fieldCount"]}, indent=2))
    return destination


if __name__ == "__main__":
    package()
