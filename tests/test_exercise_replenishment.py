import pytest

from app.ingestion.question_sync import SourceQuestion, coverage
from app.services.exercise.replenishment import build_replenishment, render_replenishment


def source(qid, *, level=None, status="inactive", kind="exercise", code="A"):
    return SourceQuestion({"_id": qid, "status": status, "cognitive_level": level},
                          "kelas12_tl", 4, code, kind, "export.json")


def inventory(records):
    return coverage(records, [{"class_key": "kelas12_tl", "chapter_no": 4,
                               "code": code, "name": code} for code in ("A", "B")])


def test_pending_targets_never_reduce_final_level_deficits():
    records = [source("pending"), source("active", level="easy", status="active"),
               source("rejected", level="hard"), source("pretest", kind="pretest")]
    plan = build_replenishment(inventory(records), records, {"pending": "medium"},
                              {"kelas12_tl": {"status": "ready"}})
    assert plan["summary"]["active_shortfall"] == 119
    assert plan["summary"]["existing_unlabelled_candidates"] == 1
    assert plan["summary"]["inactive_labelled_review_only"] == 1
    assert plan["pending_credit_towards_active"] == 0
    jobs_a = [job for job in plan["jobs"] if job["code"] == "A"]
    assert {job["status"] for job in jobs_a} == {"await_existing_validation"}
    assert {job["level_target"]: job["shortfall"] for job in jobs_a} == {"easy": 19, "medium": 20, "hard": 20}
    assert all(job["status"] == "ready_for_generation_plan" for job in plan["jobs"] if job["code"] == "B")
    assert plan["new_api_calls"] == plan["database_writes"] == 0
    assert all(job["generation_only"] and not job["validation_approved"] for job in plan["jobs"])


def test_missing_sources_block_generation_and_backlog_exposes_inputs():
    readiness = {"kelas12_tl": {"status": "waiting_for_sources", "missingInputs": ["curriculum.xlsx"]}}
    plan = build_replenishment(inventory([]), [], {}, readiness)
    assert plan["summary"]["jobs_by_status"] == {"blocked_sources": 6}
    assert plan["summary"]["active_shortfall"] == 120
    text = render_replenishment(plan)
    assert "curriculum.xlsx" in text and "MULAI VALIDASI" in text


def test_pending_cannot_be_credited_more_than_once_across_three_levels():
    records = [source("one")]
    plan = build_replenishment(inventory(records), records, {}, {})
    assert plan["summary"]["existing_unlabelled_candidates"] == 1
    assert len(plan["existing_pending"]) == 1
    assert plan["summary"]["active_shortfall"] == 120


def test_wrong_policy_or_inconsistent_total_is_rejected():
    audit = inventory([])
    audit["policy"] = "total_per_subchapter"
    with pytest.raises(ValueError, match="per subchapter and level"):
        build_replenishment(audit, [], {}, {})
    audit = inventory([])
    audit["shortfall_questions"] -= 1
    with pytest.raises(ValueError, match="differs"):
        build_replenishment(audit, [], {}, {})


def test_active_text_reference_replaces_pdf_requirement_only_in_its_own_subchapter():
    active = source("reference", level="easy", status="active")
    active.item.update(soal_text="Acuan", options=[{"option_id": "A", "text": "1"}], jawaban="A")
    plan = build_replenishment(inventory([active]), [active], {}, {})
    jobs_a = [job for job in plan["jobs"] if job["code"] == "A"]
    assert all(job["status"] == "ready_for_reference_plan" for job in jobs_a)
    assert all(job["reference_ids"] == ["reference"] for job in jobs_a)
    assert all(job["status"] == "blocked_sources" for job in plan["jobs"] if job["code"] == "B")
    assert plan["summary"]["active_shortfall"] == 119


def test_new_candidates_are_tracked_without_credit_or_repeated_generation():
    candidate = {"_id": "new", "class_key": "kelas12_tl", "chapter_no": 4,
                 "code": "A", "level_target": "hard", "batch": "batch02"}
    plan = build_replenishment(inventory([]), [], {}, {}, [candidate])
    assert plan["summary"]["new_batch_candidates_pending"] == 1
    assert plan["summary"]["active_shortfall"] == 120
    assert all(job["status"] == "await_new_batch_validation" for job in plan["jobs"] if job["code"] == "A")
    with pytest.raises(ValueError, match="Duplicate generated"):
        build_replenishment(inventory([]), [], {}, {}, [candidate, candidate])
    appended={**candidate,'generation_mode':'batch01_additions'}
    plan=build_replenishment(inventory([]),[],{},{},[appended])
    assert plan['summary']['generated_candidates_pending']==1
    assert plan['summary']['batch01_additions_candidates_pending']==1
    assert plan['summary']['new_batch_candidates_pending']==0
