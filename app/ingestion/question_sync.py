"""Pure planning for legacy Mongo question imports. No database writes here."""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Any


LEVELS = ("easy", "medium", "hard")
SYNC_FIELDS = ("kelas_id", "subbab_id", "status", "cognitive_level",
               "cognitive_score", "confidence_score", "source_kind")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def identifier(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("$oid")
    return str(value) if value is not None else ""


def class_from_chapter(chapter: str) -> tuple[str, int]:
    match = re.fullmatch(r"(SD|SMP|SMA)(\d+)([UL]?)-B(\d+)", chapter)
    if not match:
        raise ValueError(f"Identitas bab tidak valid: {chapter!r}")
    stage, grade, track, number = match.groups()
    grade, number = int(grade), int(number)
    expected = "SD" if grade <= 6 else "SMP" if grade <= 9 else "SMA"
    if not 1 <= grade <= 12 or stage != expected or number < 1:
        raise ValueError(f"Jenjang/nomor bab tidak valid: {chapter}")
    if (grade >= 11 and track not in ("U", "L")) or (grade < 11 and track):
        raise ValueError(f"Jalur kelas tidak valid: {chapter}")
    return f"kelas{grade}" + ("_tl" if track == "L" else ""), number


def threshold(class_key: str) -> int:
    match = re.fullmatch(r"kelas([1-9]|1[0-2])(_tl)?", class_key)
    if not match or (match[2] and int(match[1]) < 11):
        raise ValueError(f"Kelas tidak valid: {class_key}")
    grade = int(match[1])
    return 10 if grade <= 6 else 15 if grade <= 9 else 20


@dataclass(frozen=True)
class SourceQuestion:
    item: dict
    class_key: str
    chapter_no: int
    code: str
    kind: str
    source: str

    @property
    def qid(self) -> str:
        return self.item["_id"]


def source_files(root: Path) -> list[Path]:
    """Only canonical exports, never latex copies or intermediate balances."""
    return sorted(root.glob("exercise/kelas*/batch*/hasil_validasi/validation_results.json")) + sorted(
        root.glob("pretest/kelas*/hasil_validasi/validation_results.json"))


def load_sources(root: Path) -> list[SourceQuestion]:
    questions: dict[str, SourceQuestion] = {}
    referenced: set[str] = set()
    for path in source_files(root):
        relative = path.relative_to(root)
        kind, folder = relative.parts[:2]
        base = path.parent.parent
        metadata = (read_json(base / "soal_exercise_meta.json") if kind == "exercise"
                    else read_json(base / "sesi_pretest.json")["audit"])
        items = read_json(path)
        if not isinstance(items, list):
            raise ValueError(f"Ekspor bukan daftar soal: {relative}")
        seen = set()
        for item in items:
            qid = item.get("_id")
            if not isinstance(qid, str) or not re.fullmatch(r"[0-9a-f]{24}", qid):
                raise ValueError(f"ID soal hilang/tidak valid: {relative}")
            if qid in seen:
                raise ValueError(f"ID soal berulang dalam berkas: {qid}")
            seen.add(qid)
            referenced.add(qid)
            meta = metadata.get(qid)
            if not meta:
                raise ValueError(f"Metadata asal tidak ditemukan: {relative}: {qid}")
            owner, number = class_from_chapter(meta["bab_id"])
            if owner != folder:
                if kind == "pretest":
                    # A prerequisite is a reference, not a new question owned by this class.
                    continue
                raise ValueError(f"Kelas sumber berbeda dengan metadata: {relative}: {qid}")
            code = meta.get("subbab_kode") if kind == "exercise" else meta.get("subbab")
            if not isinstance(code, str) or not re.fullmatch(r"[A-Z]", code):
                raise ValueError(f"Kode subbab tidak valid: {relative}: {qid}")
            if not isinstance(item.get("subbab_id"), str) or not item["subbab_id"].strip():
                raise ValueError(f"Nama subbab sumber tidak valid: {relative}: {qid}")
            if qid in questions:
                raise ValueError(f"ID memiliki lebih dari satu sumber utama: {qid}")
            questions[qid] = SourceQuestion(item, owner, number, code, kind, relative.as_posix())
    missing = referenced - questions.keys()
    if missing:
        raise ValueError(f"{len(missing)} soal prasyarat tidak memiliki ekspor kelas asal")
    return list(questions.values())


def report_catalog(path: Path) -> list[dict]:
    """Read curriculum locations from the supplied audit; never use it as DB IDs."""
    rows = []
    class_key = None
    chapter_no = None
    for line in path.read_text(encoding="utf-8-sig").split("# Hasil Audit:")[0].splitlines():
        match = re.match(r"## Kelas (\d+)(.*)", line)
        if match:
            class_key = "kelas" + match[1] + ("_tl" if "Lanjut" in match[2] else "")
        match = re.match(r"- \*\*Bab (\d+):", line)
        if match:
            chapter_no = int(match[1])
        match = re.match(r"  - Subbab (\d+): (.*?) \u2014 (\d+) soal", line)
        if match:
            if class_key is None or chapter_no is None:
                raise ValueError("Katalog laporan tidak memiliki kelas/bab")
            rows.append({"class_key": class_key, "chapter_no": chapter_no,
                         "code": chr(64 + int(match[1])), "name": match[2]})
    if not rows:
        raise ValueError("Katalog subbab tidak ditemukan dalam laporan")
    return rows


def coverage(questions: list[SourceQuestion], catalog: list[dict], sessions: int = 1) -> dict:
    """Every difficulty in every subchapter must meet its grade threshold."""
    if type(sessions) is not int or sessions < 1:
        raise ValueError("sessions must be a positive integer")
    counts: dict[tuple, Counter] = defaultdict(Counter)
    for question in questions:
        item = question.item
        if question.kind == "exercise" and item.get("status") == "active" and item.get("cognitive_level") in LEVELS:
            counts[(question.class_key, question.chapter_no, question.code)][item["cognitive_level"]] += 1
    locations = {(r["class_key"], r["chapter_no"], r["code"]) for r in catalog}
    if len(locations) != len(catalog) or set(counts) - locations:
        raise ValueError("Katalog tidak lengkap atau memiliki lokasi subbab ganda")
    rows = []
    for row in catalog:
        levels = counts[(row["class_key"], row["chapter_no"], row["code"])]
        available = sum(levels.values())
        required = sessions * threshold(row["class_key"])
        deficits = {level: max(0, required - levels[level]) for level in LEVELS}
        rows.append({**row, "levels": {k: levels[k] for k in LEVELS}, "available": available,
                     "required": required, "level_shortfalls": deficits,
                     "shortfall": sum(deficits.values())})
    chapters: dict[tuple, dict] = {}
    for row in rows:
        key = row["class_key"], row["chapter_no"]
        chapter = chapters.setdefault(key, {"class_key": key[0], "chapter_no": key[1],
                                           "subchapters": 0, "deficient_subchapters": 0,
                                           "deficient_levels": 0, "shortfall": 0})
        chapter["subchapters"] += 1
        chapter["deficient_subchapters"] += row["shortfall"] > 0
        chapter["deficient_levels"] += sum(value > 0 for value in row["level_shortfalls"].values())
        chapter["shortfall"] += row["shortfall"]
    return {"scope": "local_canonical_active_exercise; no student history",
            "sessions": sessions,
            "policy": "per_subchapter_per_level_v1",
            "subchapters": len(rows), "under_threshold": sum(r["shortfall"] > 0 for r in rows),
            "level_slots": len(rows) * len(LEVELS),
            "under_threshold_levels": sum(c["deficient_levels"] for c in chapters.values()),
            "chapters": len(chapters),
            "under_threshold_chapters": sum(c["shortfall"] > 0 for c in chapters.values()),
            "shortfall_questions": sum(r["shortfall"] for r in rows),
            "chapter_rows": list(chapters.values()),
            "rows": rows}


def mongo_catalog(classes: list[dict], chapters: list[dict], subchapters: list[dict],
                  chapter_number_field: str = "nomor_bab") -> list[dict]:
    """Resolve the actual DB hierarchy. Unknown/ambiguous schemas fail closed."""
    owners = {}
    used = set()
    for row in classes:
        grade = int(row["nomor_kelas"])
        name = str(row.get("name", "")).casefold()
        if grade >= 11 and not any(word in name for word in ("umum", "lanjut")):
            raise ValueError("Kelas 11/12 harus menyebut jalur Umum/Lanjut")
        key = f"kelas{grade}" + ("_tl" if grade >= 11 and "lanjut" in name else "")
        threshold(key)
        if key in used:
            raise ValueError(f"Kelas database ambigu: {key}")
        used.add(key)
        owners[identifier(row["_id"])] = key
    chapters_by_id = {identifier(row["_id"]): row for row in chapters}
    result = []
    for sub in subchapters:
        chapter = chapters_by_id.get(identifier(sub.get("bab_id")))
        if chapter is None:
            raise ValueError("Relasi subbab.bab_id tidak ditemukan; periksa skema katalog")
        class_id = identifier(chapter.get("kelas_id"))
        if class_id not in owners:
            raise ValueError("Relasi bab.kelas_id tidak ditemukan")
        number = chapter.get(chapter_number_field)
        if isinstance(number, bool) or not str(number).isdigit() or int(number) < 1:
            raise ValueError(f"Nomor bab tidak valid; periksa --chapter-number-field {chapter_number_field}")
        if sub.get("kelas_id") is not None and identifier(sub["kelas_id"]) != class_id:
            raise ValueError("kelas_id subbab berbeda dari kelas pemilik bab")
        result.append({"class_key": owners[class_id], "chapter_no": int(number),
                       "name": sub["name"], "kelas_id": class_id,
                       "subbab_id": identifier(sub["_id"])})
    return result


def plan_sync(questions: list[SourceQuestion], catalog: list[dict], existing: list[dict]) -> dict:
    by_location: dict[tuple, list] = defaultdict(list)
    for row in catalog:
        by_location[(row["class_key"], int(row["chapter_no"]), row["name"].strip())].append(row)
    previous = {identifier(row["_id"]): row for row in existing}
    if len(previous) != len(existing):
        raise ValueError("Snapshot memiliki ID soal ganda")
    changes, errors = [], []
    unchanged = 0
    for source in questions:
        item, qid = source.item, source.qid
        candidates = by_location[(source.class_key, source.chapter_no, item["subbab_id"].strip())]
        if len(candidates) != 1:
            errors.append({"_id": qid, "source": source.source,
                           "reason": "subchapter_missing" if not candidates else "subchapter_ambiguous"})
            continue
        target = candidates[0]
        if not all(re.fullmatch(r"[0-9a-fA-F]{24}", identifier(target.get(k))) for k in ("kelas_id", "subbab_id")):
            errors.append({"_id": qid, "reason": "invalid_catalog_ids"})
            continue
        if item.get("status") not in ("active", "inactive"):
            errors.append({"_id": qid, "reason": "invalid_source_status"})
            continue
        # Unlabelled drafts must never become published through this importer.
        status = "active" if item["status"] == "active" and item.get("cognitive_level") in LEVELS else "inactive"
        desired = {"kelas_id": identifier(target["kelas_id"]), "subbab_id": identifier(target["subbab_id"]),
                   "status": status, "cognitive_level": item.get("cognitive_level"),
                   "cognitive_score": item.get("cognitive_score"),
                   "confidence_score": item.get("confidence_score"), "source_kind": source.kind}
        old = previous.get(qid)
        before = {key: (identifier(old.get(key)) or None if key in ("kelas_id", "subbab_id")
                        else old.get(key)) for key in SYNC_FIELDS} if old else None
        after = {key: value for key, value in desired.items() if before is None or before[key] != value}
        if not after:
            unchanged += 1
            continue
        changes.append({"_id": qid, "action": "update" if old else "insert", "source": source.source,
                        "before": before, "after": after})
    return {"version": 1, "questions": len(questions), "unchanged": unchanged,
            "inserts": sum(c["action"] == "insert" for c in changes),
            "updates": sum(c["action"] == "update" for c in changes),
            "blocked": len(errors), "errors": errors, "changes": changes}
