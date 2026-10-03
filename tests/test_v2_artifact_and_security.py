import json

import pytest

from app.staff.security import create_session_material, csrf_matches, password_hash, password_verify
from app.staff.assets import PrivateAssetSigner
from app.classification.v2.artifact import ModelManifest, load_and_verify_manifest
from app.classification.v2.contracts import HEAD_LABELS
from app.classification.v2.runtime import ContentConflictError, V2ClassifierRuntime


def valid_request():
    return {
        "questionId": "q-1",
        "contentVersion": 1,
        "contentHash": "a" * 64,
        "grade": 4,
        "topic": "Pecahan",
        "subtopic": "Perbandingan",
        "questionType": "multiple_choice",
        "stimulus": None,
        "stem": "Pecahan manakah yang paling besar?",
        "options": [{"label": "A", "text": "1/2"}, {"label": "B", "text": "3/4"}],
        "verifiedMinimalSolution": "Samakan penyebut; 3/4 lebih besar.",
        "detectedKko": ["menentukan"],
        "visualTranscript": None,
        "provenanceStatus": {
            "contentQualified": True,
            "answerKeyVerified": True,
            "solutionVerified": True,
            "visualEssential": False,
            "visualTranscriptVerified": False,
        },
    }


def manifest(files):
    return {
        "artifactFormatVersion": "indobert-3x4x3-artifact-v1",
        "modelVersion": "fixture-v1",
        "createdAt": "2026-01-01T00:00:00+00:00",
        "baseModel": "indobenchmark/indobert-base-p1",
        "baseRevision": "789e955254f966776dade3fc50d7a9a1e76bdb24",
        "datasetSnapshot": "snapshot-v1",
        "datasetHash": "a" * 64,
        "splitManifestHash": "b" * 64,
        "rubricVersion": "math-rubric-3x4x3-v1",
        "calibrationVersion": "cal-v1",
        "inputSchemaVersion": "math-question-text-v1",
        "inputRepresentation": "solution",
        "labels": {key: list(value) for key, value in HEAD_LABELS.items()},
        "calibration": {
            key: {"temperature": 1.0, "confidenceThreshold": 0.7} for key in HEAD_LABELS
        },
        "maxLength": 256,
        "loraRank": 8,
        "files": files,
        "metrics": {},
        "promotionGates": {},
        "approvedForProvisional": False,
        "gitCommit": "fixture",
        "contentRegistry": {},
    }


def test_manifest_verifies_every_tracked_checksum(tmp_path):
    import hashlib

    tracked = tmp_path / "heads.safetensors"
    tracked.write_bytes(b"fixture")
    digest = hashlib.sha256(b"fixture").hexdigest()
    (tmp_path / "manifest.json").write_text(json.dumps(manifest({tracked.name: digest})), encoding="utf-8")
    assert load_and_verify_manifest(tmp_path).modelVersion == "fixture-v1"
    tracked.write_bytes(b"tampered")
    with pytest.raises(ValueError, match="checksum mismatch"):
        load_and_verify_manifest(tmp_path)


def test_manifest_servable_requires_approval_and_all_safety_gates():
    payload = manifest({})
    model = ModelManifest.model_validate(payload)
    assert model.servable is False
    payload.update(
        {
            "approvedForProvisional": True,
            "researchOnly": False,
            "dataGatesPassed": True,
            "antiCollapsePassed": True,
            "promotionGates": {"passed": True},
        }
    )
    assert ModelManifest.model_validate(payload).servable is True


def test_manifest_rejects_per_grade_calibration_outside_sd_scope():
    payload = manifest({})
    payload["routingPolicyVersion"] = "confidence-entropy-v1"
    payload["calibration"]["intendedDifficulty"] = {
        "temperature": 1.0,
        "confidenceThreshold": 0.7,
        "entropyThreshold": 0.5,
        "perGrade": {
            "7": {
                "temperature": 1.0,
                "confidenceThreshold": 0.7,
                "entropyThreshold": 0.5,
            }
        },
    }
    for head in ("mathCognitiveDomain", "knowledgeDimension"):
        payload["calibration"][head]["entropyThreshold"] = 0.5
    with pytest.raises(ValueError, match="unsupported grades"):
        ModelManifest.model_validate(payload)


def test_argon2id_passwords_and_opaque_session_material():
    stored = password_hash("correct horse battery staple")
    assert stored.startswith("$argon2id$")
    assert password_verify(stored, "correct horse battery staple")
    assert not password_verify(stored, "incorrect password")
    raw, token_hash, csrf, csrf_hash = create_session_material()
    assert raw != token_hash
    assert csrf != csrf_hash
    assert csrf_matches(csrf, csrf_hash)
    assert not csrf_matches("wrong", csrf_hash)


@pytest.mark.parametrize("grade", [7, 8, 9, 10, 11, 12])
def test_runtime_out_of_scope_has_null_labels_and_registered_conflicts_are_rejected(grade):
    payload = manifest({})
    payload["contentRegistry"] = {"q-1": {"contentVersion": 1, "contentHash": "a" * 64}}
    runtime = V2ClassifierRuntime.__new__(V2ClassifierRuntime)
    runtime.manifest = ModelManifest.model_validate(payload)
    runtime.failed_reason = None
    runtime.model = None
    runtime.tokenizer = None

    request_payload = valid_request()
    request_payload["grade"] = grade
    from app.classification.v2.contracts import V2ClassificationRequest

    response = runtime.predict(V2ClassificationRequest.model_validate(request_payload))
    assert response.scopeStatus == "out_of_scope"
    assert response.mathCognitiveDomain.label is None
    assert response.reviewRequired is True

    request_payload["contentVersion"] = 2
    with pytest.raises(ContentConflictError):
        runtime.predict(V2ClassificationRequest.model_validate(request_payload))


def test_private_asset_signer_rejects_traversal_and_uses_short_expiry():
    class FakeS3:
        def generate_presigned_url(self, operation, Params, ExpiresIn):
            assert operation == "get_object"
            assert Params == {"Bucket": "private", "Key": "crop/page-1.png"}
            assert ExpiresIn == 120
            return "https://signed.example/temporary"

    signer = PrivateAssetSigner(FakeS3(), "private", 120)
    assert signer.signed_get_url("crop/page-1.png").endswith("temporary")
    with pytest.raises(ValueError, match="invalid private asset key"):
        signer.signed_get_url("../secret.pdf")
