"""Audit question math and build corrected delivery copies without relabeling evidence."""
import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.presentation.latex import DISPLAY_KEYS, POLICY_VERSION, math_spans, normalize_text, normalize_document
from app.services.exercise.workflow import atomic_json, digest


def fields(value, pointer=""):
    if isinstance(value, dict):
        for key, item in value.items():
            path = pointer + "/" + str(key).replace("~", "~0").replace("/", "~1")
            if key in DISPLAY_KEYS and isinstance(item, str):
                yield path, item
            elif isinstance(item, (dict, list)):
                yield from fields(item, path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from fields(item, f"{pointer}/{index}")


def sources(root):
    # Active masters, raw question files and published delivery arrays, not
    # immutable histories, prompt responses, model artifacts or checkpoints.
    for kind in ("pretest", "exercise"):
        for directory in sorted((root / "output" / kind).glob("kelas*")):
            bases = [directory] if kind == "pretest" else sorted(directory.glob("batch*"))
            for base in bases:
                candidates = [base / f"soal_{kind}_db.json", base / f"soal_{kind}.json",
                    base / "hasil_validasi/validation_results.json", base / "hasil_validasi/validation_results_meta.json"]
                candidates += sorted(base.glob("bab[0-9][0-9].json")) if kind == "pretest" else [
                    p for p in sorted(base.glob("bab*/*.json")) if p.name.count(".") == 1]
                for path in candidates:
                    if path.is_file():
                        yield path


def audit(root, report_dir, *, write_delivery=False):
    report_dir.mkdir(parents=True, exist_ok=True)
    expressions, records, changes, files, dangling = {}, [], [], [], []
    for path in sources(root):
        document = json.loads(path.read_text(encoding="utf-8"))
        changed = 0
        for pointer, text in fields(document):
            repaired = normalize_text(text)
            if repaired != text:
                changes.append({"file": str(path.relative_to(root)), "pointer": pointer, "before": text, "after": repaired})
                changed += 1
            spans = math_spans(repaired)
            for tex, display in spans:
                identity = (tex, display)
                if identity not in expressions:
                    expressions[identity] = len(expressions)
                records.append({"file": str(path.relative_to(root)), "pointer": pointer,
                                "expressionId": expressions[identity]})
            # Flag obvious TeX left outside a math delimiter rather than guessing prose boundaries.
            import re
            outside = re.sub(r"(?s)\$\$.*?\$\$|\$[^$]+\$|\\\[.*?\\\]|\\\(.*?\\\)", "", repaired)
            if re.search(r"\\(?:frac|dfrac|sqrt|left|right|begin)\b", outside):
                dangling.append({"file": str(path.relative_to(root)), "pointer": pointer, "text": repaired})
        info = {"source": str(path.relative_to(root)), "sourceSha256": digest(path), "changedFields": changed}
        files.append(info)
    request = report_dir / "math_expressions.json"
    atomic_json(request, [{"id": index, "tex": tex, "display": display} for (tex, display), index in expressions.items()])
    result = subprocess.run(["node", str(root / "scripts/latex_render_check.cjs"), str(request)],
                            check=True, capture_output=True, text=True, encoding="utf-8")
    render = json.loads(result.stdout)
    by_id = {index: tex for (tex, _), index in expressions.items()}
    errors = [{**error, "tex": by_id[error["id"]],
               "occurrences": [record for record in records if record["expressionId"] == error["id"]]}
              for error in render["errors"]]
    # Publish only after the complete corpus passes the renderer. Never offer
    # a partially checked delivery package if a new malformed formula appears.
    written = write_delivery and not errors and not dangling
    if written:
        for info in files:
            path = root / info["source"]
            if digest(path) != info["sourceSha256"]:
                raise ValueError("question source changed during the LaTeX audit; rerun")
            destination = root / "output/latex_ready" / path.relative_to(root / "output")
            atomic_json(destination, normalize_document(json.loads(path.read_text(encoding="utf-8"))))
            info.update(delivery=str(destination.relative_to(root)), deliverySha256=digest(destination))
    report = {"policyVersion": POLICY_VERSION, "katexVersion": render["version"], "files": files,
        "changedFields": len(changes), "changedFiles": sum(info["changedFields"] > 0 for info in files),
        "uniqueMathExpressions": len(expressions), "mathOccurrences": len(records),
        "renderErrors": errors, "outsideMath": dangling, "newApiCalls": 0,
        "deliveryWritten": written}
    atomic_json(report_dir / "report.json", report)
    atomic_json(report_dir / "changes.json", changes)
    if written:
        atomic_json(root / "output/latex_ready/manifest.json", {"schemaVersion": "latex-delivery-v1",
            "policyVersion": POLICY_VERSION, "katexVersion": render["version"], "newApiCalls": 0,
            "sourceEvidenceModified": False, "renderErrors": 0, "files": files})
    print(json.dumps({key: value for key, value in report.items() if key not in ("files", "renderErrors", "outsideMath")}
          | {"renderErrors": len(errors), "outsideMath": len(dangling)}, indent=2))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-delivery", action="store_true")
    args = parser.parse_args()
    report = audit(ROOT, ROOT / "runs/latex_audit", write_delivery=args.write_delivery)
    return 0 if not report["renderErrors"] and not report["outsideMath"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
