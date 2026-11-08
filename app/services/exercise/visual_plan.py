"""Source-bound pilot allocation and read-only readiness checks."""
from pathlib import Path

from .allocation import modality_quotas
from .workflow import digest, load
from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import get_book, MD_ROOT


def preflight(book):
    missing = []
    curriculum = Path(kurikulum.EXCEL_PATH)
    if not curriculum.is_file():
        missing.append(str(curriculum))
    try:
        source_book = get_book(book)
    except SystemExit:
        source_book = None
    if not source_book or not source_book.siswa_pdf:
        missing.append(f"data/<jenjang>/panduan_siswa_{book}.pdf (original source book)")
    index = Path(MD_ROOT) / book / "siswa/index.json"
    if not index.is_file():
        missing.append(str(index))
    pages = list(index.parent.glob("p*.md"))
    if not pages:
        missing.append(str(index.parent / "pNNNN.md"))
    return {"class": book, "status": "ready" if not missing else "waiting_for_sources",
            "missingInputs": missing, "curriculumAvailable": curriculum.is_file(),
            "studentBookAvailable": bool(source_book and source_book.siswa_pdf),
            "indexedPages": len(pages), "newApiCalls": 0}


def make_plan(book, batch, chapter, subchapter, *, total=30, visual_percent=70):
    if type(total) is not int or not 1 <= total <= 30:
        raise ValueError("the pilot is limited to 1..30 new candidate questions")
    if preflight(book)["status"] != "ready":
        raise ValueError("source curriculum/book/pages are missing; see preflight report")
    from .llm_generate import subbab_pages
    from app.services.pretest.agentic.books import page_md_path
    chapter_info = kurikulum.get(book, chapter)
    if not chapter_info or chapter_info.subbab_nama(subchapter) is None:
        raise ValueError("select a chapter/subchapter present in the verified curriculum")
    start, end = subbab_pages(book, chapter, subchapter)
    source_book = get_book(book)
    paths = [Path(kurikulum.EXCEL_PATH), Path(source_book.siswa_pdf),
             Path(source_book.md_dir("siswa")) / "index.json"]
    paths += [Path(page_md_path(source_book, "siswa", n)) for n in range(start, end + 1)]
    if any(not p.is_file() for p in paths):
        raise ValueError("every required source page must exist")
    allocation = modality_quotas(total, visual_percent=visual_percent)
    slots = [{"bab_no": chapter, "bab_id": chapter_info.bab_id, "subbab": subchapter,
              "subbab_name": chapter_info.subbab_nama(subchapter), "level": level,
              "visual": modality == "visual", "count": count}
             for level, counts in allocation.items() for modality, count in counts.items() if count]
    return {"schemaVersion": "exercise-visual-plan-v1", "class": book, "batch": f"batch{batch:02d}",
            "generationOnly": True, "total": total, "visualPercent": visual_percent,
            "targetDifficultyWeights": {"easy": 3, "medium": 4, "hard": 3}, "slots": slots,
            "sources": {str(path.resolve()): digest(path) for path in paths}}


def verify_plan(plan):
    if (plan.get("schemaVersion") != "exercise-visual-plan-v1" or plan.get("generationOnly") is not True
            or not plan.get("sources") or type(plan.get("total")) is not int or not 1 <= plan["total"] <= 30):
        raise ValueError("invalid visual pilot plan")
    if any(digest(Path(path)) != checksum for path, checksum in plan["sources"].items()):
        raise ValueError("pilot curriculum/book/page changed; create a new plan/batch")
    slots = plan["slots"]
    if (any(type(s["count"]) is not int or s["count"] < 1 or s["level"] not in ("easy", "medium", "hard")
            or type(s["visual"]) is not bool for s in slots)
            or sum(s["count"] for s in slots) != plan["total"]):
        raise ValueError("plan count/level/modality mismatch")
    keys = [(s["bab_no"], s["subbab"], s["level"], s["visual"]) for s in slots]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate allocation slots")
    return plan


def slot_count(path, data):
    base = Path(path).parent.parent
    plan_path = base / "generation_plan.json"
    if not plan_path.exists():
        return None
    plan = verify_plan(load(plan_path))
    if plan["class"] != data.book or plan["batch"] != f"batch{data.batch:02d}":
        raise ValueError("candidate and generation plan identity differ")
    matches = [s for s in plan["slots"] if
        (s["bab_no"], s["subbab"], s["level"], s["visual"]) ==
        (data.bab_no, data.subbab, data.level, data.bergambar)]
    if len(matches) != 1:
        raise ValueError("candidate slot is outside the source-bound generation plan")
    return matches[0]["count"]


def complete_plan(base):
    from .schema import ExerciseFile
    base = Path(base)
    plan = verify_plan(load(base / "generation_plan.json"))
    for slot in plan["slots"]:
        path = base / f"bab{slot['bab_no']:02d}" / f"{slot['subbab']}_{slot['level']}{'_gambar' if slot['visual'] else ''}.json"
        if not path.is_file():
            return False
        data = ExerciseFile.model_validate(load(path))
        if len(data.soal) != slot_count(path, data):
            return False
    return True
