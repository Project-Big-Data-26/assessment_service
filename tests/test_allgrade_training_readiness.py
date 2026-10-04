"""All-grade scope, track distinction and no training from missing/weak evidence."""
from collections import Counter
import json
from types import SimpleNamespace

import numpy as np
import pytest
import torch
from transformers import BertConfig, BertModel, BertTokenizer

from app.classification.v2.artifact import ModelManifest
from app.classification.v2.model import GradeAwareOrdinalDifficultyHead
from app.classification.v2.serializer import serialize_question
from app.llm.silver import RUBRIC_VERSION, silver_rubric
from app.training.v2.dataset import build_snapshot
from app.training.v2.train_lora import calibration_from_validation, train
from app.training.v2 import train_lora
from scripts import prepare_allgrade_retraining as preparation
from scripts.build_blind_validation_bundle import model_in_scope, render_report, calibration_for
from tests.test_assessment_empirical_flow import silver_snapshot
from tests.test_v2_artifact_and_security import manifest


def test_explicit_allgrade_snapshot_includes_upper_grades_and_tl_without_changing_sd_default():
    row = silver_snapshot().rows[0]
    rows = [
        row.model_copy(update={"grade": 7}),
        row.model_copy(update={"questionId": "tl", "questionVersionId": "tl:v2", "grade": 12, "subjectTrack": "tl"}),
    ]
    legacy = build_snapshot(rows, snapshot_id="sd-only", required_grades=())
    assert legacy.rows == [] and len(legacy.expansionRows) == 2
    expanded = build_snapshot(
        rows, snapshot_id="all-grade", training_grades=tuple(range(1, 13)),
        required_grades=tuple(range(1, 13)), required_grade_tracks=("12:tl",),
    )
    assert {row.grade for row in expanded.rows} == {7, 12}
    assert expanded.expansionRows == []
    assert {entry.questionVersionId for entry in expanded.splitManifest} == {row.questionVersionId for row in rows}
    assert any("intendedDifficulty:Hard" in value for value in expanded.gateFailures)
    assert any("gradeTrack:12:tl" in value for value in expanded.gateFailures)


def test_tl_encoder_input_differs_from_regular_and_requires_valid_grade():
    request = silver_snapshot().rows[0].model_copy(update={"grade": 12}).inference_request()
    regular_text = serialize_question(request, representation="solution")
    explicit_regular = serialize_question(request.model_copy(update={"subjectTrack": "regular"}), representation="solution")
    assert regular_text == explicit_regular
    tl_text = serialize_question(request.model_copy(update={"subjectTrack": "tl"}), representation="solution")
    assert "Jalur mata pelajaran: Matematika Tingkat Lanjut" in tl_text
    assert regular_text != tl_text
    with pytest.raises(ValueError, match="TL classification supports"):
        request.__class__.model_validate({**request.model_dump(), "grade": 6, "subjectTrack": "tl"})


def test_twelve_grade_ordinal_head_is_explicit_and_old_six_grade_weights_remain_compatible():
    pooled = torch.zeros((3, 3))
    old = GradeAwareOrdinalDifficultyHead(hidden_size=3, grade_embedding_dim=2)
    assert old.grade_embedding.weight.shape == (6, 2)
    with pytest.raises(ValueError, match="1-6"):
        old(pooled, torch.tensor([1, 7, 12]))
    head = GradeAwareOrdinalDifficultyHead(hidden_size=3, grade_embedding_dim=2, num_grades=12)
    probabilities, _ = head(pooled, torch.tensor([1, 7, 12]))
    assert torch.allclose(probabilities.exp().sum(dim=1), torch.ones(3), atol=1e-6)
    clone = GradeAwareOrdinalDifficultyHead(hidden_size=3, grade_embedding_dim=2, num_grades=12)
    clone.load_state_dict(head.state_dict(), strict=True)
    assert torch.allclose(clone(pooled, torch.tensor([1, 7, 12]))[0], probabilities)
    payload = manifest({})
    payload.update({"architectureVersion": "grade-aware-ordinal-v2", "difficultyHeadType": "ordinal",
                    "gradeEmbeddingDimension": 2, "supportedGrades": list(range(1, 13))})
    with pytest.raises(ValueError, match="embedding count"):
        ModelManifest.model_validate(payload)
    payload.update({"gradeEmbeddingCount": 12, "supportedSubjectTracks": ["regular", "tl"]})
    assert ModelManifest.model_validate(payload).supportedGrades[-1] == 12


def test_allgrade_training_collates_track_metadata_and_evaluates_grade_twelve(tmp_path, monkeypatch):
    base = tmp_path / "tiny-base"
    BertModel(BertConfig(vocab_size=16, hidden_size=8, num_hidden_layers=1,
                         num_attention_heads=2, intermediate_size=16,
                         max_position_embeddings=32)).save_pretrained(base, safe_serialization=True)
    vocab = tmp_path / "vocab.txt"
    vocab.write_text("\n".join(["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
                              + [f"word{index}" for index in range(11)]), encoding="utf-8")
    tokenizer = BertTokenizer(vocab_file=str(vocab))
    monkeypatch.setattr(train_lora, "BASE_MODEL_ID", str(base))
    monkeypatch.setattr(train_lora, "BASE_MODEL_REVISION", None)
    examples = [{
        "text": f"word{index}", "grade": (1, 7, 11, 12)[index % 4],
        "subjectTrack": "tl" if index % 4 == 3 else "regular",
        "mathCognitiveDomain": ("knowing", "applying", "reasoning")[index % 3],
        "knowledgeDimension": ("factual", "conceptual", "procedural", "metacognitive")[index % 4],
        "intendedDifficulty": ("Easy", "Medium", "Hard")[index % 3],
    } for index in range(12)]
    config = train_lora.TrialConfig(rank=8, lora_lr=1e-4,
        architecture_version="grade-aware-ordinal-v2", num_grades=12,
        epochs=1, batch_size=2, gradient_accumulation=2)
    _, metrics, payload = train_lora.run_trial(
        examples, examples, tokenizer, config, max_length=16,
        output_dir=tmp_path / "trial", resume=False,
    )
    assert "12:tl" in metrics["intendedDifficulty"]["perGradeTrack"]
    assert {1, 7, 11, 12} == set(payload["grades"])
    assert {0, 1} == set(payload["subject_tracks"])
    assert (tmp_path / "trial/checkpoint.pt").is_file()


def test_calibration_does_not_pool_regular_and_tl_into_one_grade_threshold():
    # Each track separately has enough evidence for calibrated thresholds.
    payload = {"grades": np.full(240, 12), "subject_tracks": np.repeat([0, 1], 120)}
    for head, class_count in (("mathCognitiveDomain", 3), ("knowledgeDimension", 4), ("intendedDifficulty", 3)):
        targets = np.arange(240) % class_count
        logits = np.full((240, class_count), -2.0)
        logits[np.arange(240), targets] = 2.0
        payload[f"targets_{head}"] = targets
        payload[f"logits_{head}"] = logits
    calibration, metrics = calibration_from_validation(payload)
    for head, spec in calibration.items():
        assert "12" not in spec.perGrade
        assert set(spec.perGradeTrack) == {"12:regular", "12:tl"}
        assert metrics[head]["perGrade"]["12"]["activated"] is False


def test_new_allgrade_report_uses_artifact_scope_and_track_calibration():
    summary = {"itemCount": 0, "advisoryLabelDistributions": {"intendedDifficulty": {}},
               "contentQualifiedAdvisoryLabelDistributions": {"intendedDifficulty": {}}, "routingCounts": {}}
    checkpoint = {"sourceGrade": 12, "subjectTrack": "tl", "model": "fixture", "promptVersion": "blind",
                  "rubricVersion": "v8", "summary": {"successfulRuns": 0, "totalTokens": 0}}
    model = {"modelVersion": "new-allgrade", "architectureVersion": "grade-aware-ordinal-v2",
             "inputRepresentation": "solution", "supportedGrades": list(range(1, 13)),
             "supportedSubjectTracks": ["regular", "tl"], "datasetSnapshot": "new-snapshot",
             "antiCollapsePassed": True}
    assert model_in_scope(model, 12, "tl")
    report = render_report([], [], summary, checkpoint, model)
    assert "new-allgrade" in report and "new-snapshot" in report
    assert "di luar cakupan" not in report
    assert "tidak ada training ulang dalam batch ini" not in report
    assert not model_in_scope({"supportedGrades": list(range(1, 13))}, 12, "tl")
    model["calibration"] = {"intendedDifficulty": {"temperature": 2.0,
        "perGrade": {"12": {"temperature": 3.0}},
        "perGradeTrack": {"12:tl": {"temperature": 4.0}}}}
    assert calibration_for(model, "intendedDifficulty", 12, "tl")["temperature"] == 4.0
    assert calibration_for(model, "intendedDifficulty", 12, "regular")["temperature"] == 3.0


def args_for(tmp_path):
    return SimpleNamespace(
        source_root=tmp_path / "source", bundle_root=None,
        output_dir=tmp_path / "training", snapshot_id="allgrade-test", model_version="allgrade-test",
        rubric_version=RUBRIC_VERSION.replace("-sd-grade-aware", "-grade-aware"),
    )


def write_bundle_metadata(args, class_name, *, current):
    source_dir = args.source_root / class_name
    bundle = source_dir / "hasil_validasi"
    bundle.mkdir(parents=True)
    (source_dir / "soal_pretest_db.json").write_text("[{}]", encoding="utf-8")
    grade = int(class_name.removeprefix("kelas").removesuffix("_tl"))
    track = "tl" if class_name.endswith("_tl") else "regular"
    rubric = silver_rubric(grade, track=track)
    checkpoint = bundle / "checkpoint.json"
    checkpoint.write_text(json.dumps({
        "rubricVersion": rubric.version if current else "math-rubric-3x4x3-v7-old",
        "promptVersion": rubric.prompt_version,
        "items": {class_name: {"runs": [{"runIndex": index, "status": "success"} for index in (1, 2, 3)],
                                "aggregate": {"needsAdjudication": False}}},
    }), encoding="utf-8")
    (bundle / "manifest.json").write_text(json.dumps({"sourceFiles": {"blindCheckpoint": {"path": str(checkpoint)}}}), encoding="utf-8")
    return grade, track, rubric


def test_readiness_refuses_mixed_or_stale_revalidation_without_writing_snapshot(tmp_path, monkeypatch):
    args = args_for(tmp_path)
    write_bundle_metadata(args, "kelas1", current=False)
    monkeypatch.setattr(preparation, "rows_from_bundle", lambda *args: pytest.fail("stale evidence cannot be loaded"))
    report = preparation.prepare(args)
    assert report["trainingStatus"] == "blocked_revalidation_incomplete"
    assert len(report["failures"]) == 14
    assert "rubric_mismatch" in report["classes"]["kelas1"]["failure"]
    assert not (args.output_dir / "dataset_snapshot.json").exists()


def test_readiness_preserves_label_minimums_after_all_classes_are_verified(tmp_path, monkeypatch):
    args = args_for(tmp_path)
    args.output_dir.mkdir()
    fixture = silver_snapshot().rows[0]
    rows_by_class = {}
    for class_name in preparation.CLASSES:
        grade, track, rubric = write_bundle_metadata(args, class_name, current=True)
        rows_by_class[class_name] = fixture.model_copy(update={
            "questionId": class_name, "questionVersionId": f"{class_name}:v8",
            "sourceGroup": class_name, "grade": grade, "subjectTrack": track,
            "rubricVersion": rubric.version,
        })
    monkeypatch.setattr(preparation, "rows_from_bundle", lambda source, bundle: ([rows_by_class[source.parent.name]], Counter()))
    report = preparation.prepare(args)
    assert report["revalidationComplete"] is True
    assert report["readyForTraining"] is False
    assert report["trainingStatus"] == "blocked_data_gates"
    assert any("intendedDifficulty:Hard=0" in failure for failure in report["failures"])
    snapshot_file = args.output_dir / "dataset_snapshot.json"
    assert snapshot_file.exists()
    trainer_args = SimpleNamespace(snapshot=snapshot_file, rubric_version=args.rubric_version,
                                   representation="solution", allow_research_incomplete=False)
    with pytest.raises(ValueError, match="coverage gate failed|snapshot must contain"):
        train(trainer_args)
