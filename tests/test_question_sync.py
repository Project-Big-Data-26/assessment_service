import json
from types import SimpleNamespace

import pytest

from app.ingestion.question_sync import (
    SourceQuestion, class_from_chapter, coverage, load_sources, mongo_catalog, plan_sync,
)
from scripts.auto_inserter import apply_plan, main


QID, CLASS10, CLASS12, SUB10, SUB12 = [str(i) * 24 for i in range(1, 6)]


def question(**overrides):
    item = {"_id": QID, "subbab_id": "Barisan", "status": "active",
            "cognitive_level": "medium", "cognitive_score": 500,
            "confidence_score": 90, "soal_text": "Isi tetap", "options": []}
    item.update(overrides)
    return SourceQuestion(item, "kelas10", 2, "A", "exercise", "exercise/kelas10/batch01/hasil_validasi/validation_results.json")


def catalog():
    return [
        {"class_key": "kelas10", "chapter_no": 2, "name": "Barisan", "kelas_id": CLASS10, "subbab_id": SUB10},
        {"class_key": "kelas12", "chapter_no": 1, "name": "Barisan", "kelas_id": CLASS12, "subbab_id": SUB12},
        {"class_key": "kelas10", "chapter_no": 3, "name": "Barisan", "kelas_id": CLASS10, "subbab_id": "a" * 24},
    ]


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def exercise_export(root):
    base = root / "exercise/kelas10/batch01"
    write(base / "hasil_validasi/validation_results.json", [question().item])
    write(base / "soal_exercise_meta.json", {QID: {"bab_id": "SMA10-B2", "subbab_kode": "A"}})


def test_same_names_cannot_cross_class_or_chapter_and_repair_preserves_id():
    previous = {"_id": QID, "kelas_id": CLASS12, "subbab_id": SUB12, "soal_text": "Isi tetap"}
    plan = plan_sync([question()], catalog(), [previous])
    assert plan["updates"] == 1 and plan["inserts"] == plan["blocked"] == 0
    change = plan["changes"][0]
    assert change["_id"] == QID
    assert change["before"]["subbab_id"] == SUB12
    assert change["after"]["subbab_id"] == SUB10
    assert change["after"]["kelas_id"] == CLASS10
    assert "soal_text" not in change["after"]
    repaired = {**previous, **change["after"]}
    second = plan_sync([question()], catalog(), [repaired])
    assert second["unchanged"] == 1 and not second["changes"]


@pytest.mark.parametrize("status,level,expected", [
    ("inactive", "medium", "inactive"), ("inactive", None, "inactive"),
    ("active", None, "inactive"), ("active", "medium", "active"),
])
def test_import_never_forces_inactive_or_unlabelled_question_active(status, level, expected):
    plan = plan_sync([question(status=status, cognitive_level=level)], catalog(), [])
    assert plan["changes"][0]["after"]["status"] == expected


@pytest.mark.parametrize("rows,reason", [([], "subchapter_missing"),
                                       ([catalog()[0], catalog()[0]], "subchapter_ambiguous")])
def test_unresolved_catalog_blocks_all_database_writes(rows, reason):
    plan = plan_sync([question()], rows, [])
    assert plan["errors"][0]["reason"] == reason
    with pytest.raises(ValueError, match="diblokir"):
        apply_plan(None, plan, [question()])


def test_pretest_prerequisite_copy_does_not_steal_ownership_or_overwrite_label(tmp_path):
    for folder, level in [("kelas10", "easy"), ("kelas11", "hard")]:
        base = tmp_path / "pretest" / folder
        write(base / "hasil_validasi/validation_results.json", [question(cognitive_level=level).item])
        write(base / "sesi_pretest.json", {"audit": {QID: {"bab_id": "SMA10-B2", "subbab": "A"}}})
    # A delivery-ready copy is not an authoritative source.
    write(tmp_path / "latex_ready/pretest/kelas10/hasil_validasi/validation_results.json", [{}])
    sources = load_sources(tmp_path)
    assert len(sources) == 1 and sources[0].class_key == "kelas10"
    assert sources[0].item["cognitive_level"] == "easy"
    assert sources[0].kind == "pretest"


def test_missing_canonical_prerequisite_owner_blocks(tmp_path):
    base = tmp_path / "pretest/kelas11"
    write(base / "hasil_validasi/validation_results.json", [question().item])
    write(base / "sesi_pretest.json", {"audit": {QID: {"bab_id": "SMA10-B2", "subbab": "A"}}})
    with pytest.raises(ValueError, match="kelas asal"):
        load_sources(tmp_path)


def test_each_level_must_meet_threshold_and_pretest_cannot_fill_it():
    rows = [{"class_key": "kelas5", "chapter_no": 1, "code": "A", "name": "Bilangan"}]
    sources = [SourceQuestion({"status": "active", "cognitive_level": "easy"}, "kelas5", 1, "A", "exercise", "") for _ in range(6)]
    sources += [SourceQuestion({"status": "active", "cognitive_level": "hard"}, "kelas5", 1, "A", "exercise", "") for _ in range(4)]
    sources += [SourceQuestion({"status": "active", "cognitive_level": "medium"}, "kelas5", 1, "A", "pretest", "")]
    sources += [SourceQuestion({"status": "inactive", "cognitive_level": "medium"}, "kelas5", 1, "A", "exercise", "")]
    result = coverage(sources, rows)
    row = result["rows"][0]
    assert row["available"] == row["required"] == 10 and row["shortfall"] == 20
    assert row["levels"] == {"easy": 6, "medium": 0, "hard": 4}
    assert row["level_shortfalls"] == {"easy": 4, "medium": 10, "hard": 6}
    assert result["under_threshold_levels"] == 3
    assert result["under_threshold_chapters"] == 1


@pytest.mark.parametrize("class_key,minimum", [("kelas5", 10), ("kelas8", 15), ("kelas11_tl", 20)])
def test_surplus_in_other_levels_or_subchapters_cannot_cover_missing_level(class_key, minimum):
    catalog_rows = [{"class_key": class_key, "chapter_no": 1, "code": code, "name": code}
                    for code in ("A", "B")]
    sources = []
    for code in ("A", "B"):
        for level, count in (("easy", minimum + 5), ("medium", minimum), ("hard", minimum)):
            count -= code == "B" and level == "medium"
            sources += [SourceQuestion({"status": "active", "cognitive_level": level},
                                       class_key, 1, code, "exercise", "") for _ in range(count)]
    result = coverage(sources, catalog_rows)
    assert result["under_threshold"] == result["under_threshold_levels"] == 1
    assert result["rows"][0]["shortfall"] == 0
    assert result["rows"][1]["level_shortfalls"] == {"easy": 0, "medium": 1, "hard": 0}
    assert result["chapter_rows"][0]["deficient_subchapters"] == 1
    assert result["under_threshold_chapters"] == 1
    sources.append(SourceQuestion({"status": "active", "cognitive_level": "medium"},
                                  class_key, 1, "B", "exercise", ""))
    assert coverage(sources, catalog_rows)["under_threshold_chapters"] == 0


def test_raw_mongo_hierarchy_keeps_tracks_separate_and_rejects_missing_number():
    classes = [{"_id": CLASS10, "nomor_kelas": 11, "name": "Kelas 11 SMA (Umum)"},
               {"_id": CLASS12, "nomor_kelas": 11, "name": "Kelas 11 SMA (Lanjut)"}]
    chapters = [{"_id": "a", "kelas_id": CLASS10, "nomor_bab": 2},
                {"_id": "b", "kelas_id": CLASS12, "nomor_bab": 2}]
    subs = [{"_id": SUB10, "bab_id": "a", "name": "Lingkaran"},
            {"_id": SUB12, "bab_id": "b", "name": "Lingkaran"}]
    result = mongo_catalog(classes, chapters, subs)
    assert [r["class_key"] for r in result] == ["kelas11", "kelas11_tl"]
    del chapters[0]["nomor_bab"]
    with pytest.raises(ValueError, match="chapter-number-field"):
        mongo_catalog(classes, chapters, subs)


def test_compare_and_set_keeps_content_and_detects_concurrent_changes():
    from bson import ObjectId

    captured = []

    class Collection:
        def bulk_write(self, operations, ordered):
            captured.extend(operations)
            assert ordered
            return SimpleNamespace(matched_count=1, modified_count=1, upserted_count=0)

    old = {"_id": QID, "kelas_id": CLASS12, "subbab_id": SUB12}
    plan = plan_sync([question()], catalog(), [old])
    apply_plan(SimpleNamespace(soal=Collection()), plan, [question()])
    assert captured[0]._filter["subbab_id"] == ObjectId(SUB12)
    assert captured[0]._filter["_id"] == ObjectId(QID)
    assert captured[0]._doc["$set"]["subbab_id"] == ObjectId(SUB10)
    assert set(captured[0]._doc) == {"$set"}
    assert "soal_text" not in captured[0]._doc["$set"]
    # A zero match must not be reported as a successful repair.
    insert_plan = plan_sync([question()], catalog(), [])
    with pytest.raises(ValueError, match="Data berubah"):
        apply_plan(SimpleNamespace(soal=Collection()), insert_plan, [question()])


def test_snapshot_cli_plans_only_and_exit_code_signals_blocked(tmp_path):
    root = tmp_path / "output"
    exercise_export(root)
    snapshot, report = tmp_path / "snapshot.json", tmp_path / "plan.json"
    write(snapshot, {"catalog": catalog(), "soal": []})
    args = ["--output", str(root), "--snapshot", str(snapshot), "--report", str(report)]
    assert main(args) == 0
    result = json.loads(report.read_text(encoding="utf-8"))
    assert result["mode"] == "dry_run" and result["inserts"] == 1
    assert "execution" not in result
    write(snapshot, {"catalog": [], "soal": []})
    assert main(args) == 2


def test_execute_cannot_use_snapshot_or_local_mode():
    with pytest.raises(SystemExit) as error:
        main(["--local", "--execute"])
    assert error.value.code == 2


def test_regular_tl_chapter_identity_and_invalid_prefix():
    assert class_from_chapter("SMA11L-B6") == ("kelas11_tl", 6)
    assert class_from_chapter("SMA11U-B2") == ("kelas11", 2)
    with pytest.raises(ValueError):
        class_from_chapter("SD11-B1")
