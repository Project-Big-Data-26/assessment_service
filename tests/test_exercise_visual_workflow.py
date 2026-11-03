import json
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest

from app.services.exercise import config as C, workflow as flow
from app.services.exercise.allocation import allocate, modality_quotas
from app.services.exercise.visual_assets import render, VisualSpec
from app.services.exercise.generation import BudgetedGenerator, GenerationStopped
from app.llm.ninerouter import NineRouterSettings
from scripts import nightly_pipeline as nightly, validate_exercise_batch as exercise


def test_allocation_preserves_total_and_targets():
    assert modality_quotas(100) == {"easy": {"visual": 21, "text": 9},
        "medium": {"visual": 28, "text": 12}, "hard": {"visual": 21, "text": 9}}
    for total in range(1, 101):
        result = modality_quotas(total)
        assert sum(sum(counts.values()) for counts in result.values()) == total
        assert all(value >= 0 for counts in result.values() for value in counts.values())
    assert allocate(30, {"easy": 3, "medium": 4, "hard": 3}) == {"easy": 9, "medium": 12, "hard": 9}


@pytest.mark.parametrize("spec", [
    {"kind": "object_groups", "groups": [{"label": "A", "shape": "circle", "count": 7}]},
    {"kind": "shape_pattern", "pattern": ["circle", "square", "circle", "?"]},
    {"kind": "clock", "hour": 3, "minute": 30},
])
def test_renderer_is_deterministic_and_has_factual_provenance(tmp_path, spec):
    reference, proof = render(spec, tmp_path)
    before = (tmp_path / reference).read_bytes()
    assert proof["source"] == "generated_svg"
    assert proof["visualEssentialStatus"] == "pending_independent_validation"
    assert render(spec, tmp_path)[0] == reference
    assert (tmp_path / reference).read_bytes() == before
    assert flow.digest(tmp_path / reference) == proof["pngSha256"]
    (tmp_path / reference).write_bytes(b"changed")
    with pytest.raises(ValueError, match="immutable"):
        render(spec, tmp_path)


@pytest.mark.parametrize("spec", [
    {"kind": "object_groups", "groups": [{"label": "A", "shape": "circle", "count": 999}]},
    {"kind": "shape_pattern", "pattern": ["circle", "square", "circle", "square"]},
    {"kind": "clock", "hour": 3, "minute": 4},
])
def test_invalid_specs_are_rejected(spec):
    with pytest.raises(ValueError):
        VisualSpec.model_validate(spec)


@pytest.fixture
def pending(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "OUT_ROOT", str(tmp_path / "output/exercise"))
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    monkeypatch.setattr(nightly, "ROOT", tmp_path)
    base = Path(C.OUT_ROOT) / "kelas1/batch02"
    flow.begin_generation(base, "kelas1", 2)
    asset, _ = render({"kind": "object_groups", "groups": [{"label": "A", "shape": "triangle", "count": 3}]}, base)
    item = {"_id": "q1", "kelas_id": "kelas1", "subbab_id": "Counting", "soal_text": "Ada berapa bentuk pada gambar?",
        "options": [{"option_id": "A", "text": "3", "alasan": "SECRET_KEY_REASON"},
                    {"option_id": "B", "text": "4", "alasan": "DISTRACTOR_REASON"}],
        "image_url": [asset], "jawaban": "A", "cognitive_level": None}
    flow.atomic_json(base / "soal_exercise_db.json", {"book": "kelas1", "batch": 2, "items": [item]})
    flow.atomic_json(base / "soal_exercise_meta.json", {"q1": {"batch": 2, "level_target": "easy", "bab_id": "SD1-B1"}})
    report = flow.finish_generation(base, complete=True)
    return base, item, report


def test_pending_blocks_bootstrap_stale_marker_and_direct_validator(pending, monkeypatch):
    base, _, _ = pending
    flow.atomic_json(base / "extraction_ready.json", {"stale": True})
    cfg = {"classes": ["kelas1"], "bootstrapJobs": [{"class": "kelas1", "batch": "batch02"}]}
    assert nightly.discover_jobs(cfg) == ([], [])
    with pytest.raises(ValueError, match="approval"):
        flow.require_validation(base)
    with pytest.raises(ValueError, match="approval"):
        nightly.mark_ready("kelas1", "batch02")
    monkeypatch.setattr(exercise, "run_labeler", lambda *a, **k: pytest.fail("pending validation must not call API"))
    monkeypatch.setattr("sys.argv", ["validator", "run", "--classes", "kelas1", "--batch", "batch02", "--execute"])
    with pytest.raises(ValueError, match="approval"):
        exercise.main()


def test_separate_approval_is_bound_to_text_and_assets(pending):
    base, item, report = pending
    with pytest.raises(ValueError, match="SHA256"):
        flow.approve_validation(base, "wrong")
    flow.approve_validation(base, report["manifestSha256"])
    assert flow.validation_allowed(base)
    with pytest.raises(ValueError, match="frozen"):
        flow.begin_generation(base, "kelas1", 2)
    staged = exercise.stage_class("kelas1", "batch02")
    assert staged[0]["_visualAssetHashes"][item["image_url"][0]] == flow.digest(base / item["image_url"][0])
    assert (exercise.paths("kelas1", "batch02")["stage"] / item["image_url"][0]).exists()
    (base / item["image_url"][0]).write_bytes(b"mutated pixels")
    assert not flow.validation_allowed(base)
    with pytest.raises(ValueError, match="changed"):
        flow.require_validation(base)


def test_new_exercise_prompt_does_not_leak_key_or_option_reason(pending):
    base, _, report = pending
    flow.approve_validation(base, report["manifestSha256"])
    item = exercise.stage_class("kelas1", "batch02")[0]
    from app.llm.silver import build_silver_prompt
    prompt = build_silver_prompt(item, grade=1)
    assert "SECRET_KEY_REASON" not in prompt and "DISTRACTOR_REASON" not in prompt
    assert "Kunci pada sumber: A" not in prompt
    assert "AUDIT VISUAL EXERCISE" in prompt


def test_batch_lock_rejects_other_writers(pending):
    base, _, _ = pending
    with flow.batch_lock(base):
        with pytest.raises(RuntimeError, match="another"):
            with flow.batch_lock(base):
                pass
    with flow.batch_lock(base):
        pass


def test_generation_budget_counts_requests_and_stops_429(tmp_path):
    settings = NineRouterSettings(api_key="test-only", base_url="http://test/v1", model="test", stream=False)
    calls = []
    def success(request):
        calls.append(True)
        return httpx.Response(200, json={"choices": [{"message": {"content": "{}"}, "finish_reason": "stop"}]})
    with BudgetedGenerator(settings, tmp_path, 1, transport=httpx.MockTransport(success)) as client:
        client.chat([])
        with pytest.raises(GenerationStopped, match="budget"):
            client.chat([])
    assert len(calls) == 1
    other = tmp_path / "quota"
    with BudgetedGenerator(settings, other, 4, transport=httpx.MockTransport(lambda r: httpx.Response(429))) as client:
        with pytest.raises(GenerationStopped, match="429"):
            client.chat([])
        assert client.attempts == 1


def test_generation_legacy_batches_are_not_rewritten(tmp_path):
    base = tmp_path / "old"
    base.mkdir()
    (base / "soal_exercise_db.json").write_text("existing paid source")
    with pytest.raises(ValueError, match="new batch"):
        flow.begin_generation(base, "kelas1", 2)
    assert not (base / "generation_state.json").exists()


def test_export_and_independent_solver_remain_deferred(pending, monkeypatch):
    base, _, _ = pending
    from app.services.exercise.handoff import mark_completed_export
    assert mark_completed_export(base, "kelas1", 2, [], {}, []) is False
    from app.services.exercise.llm_verify import verifikasi_buta, cek_butuh_gambar
    client = SimpleNamespace(chat=lambda *a, **k: pytest.fail("pending solver"))
    candidate = base / "bab01/A_easy_gambar.json"
    for method in (verifikasi_buta, cek_butuh_gambar):
        with pytest.raises(ValueError, match="approval"):
            method(str(candidate), client, "test")
