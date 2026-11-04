import json
from types import SimpleNamespace

from app.classification.v2.prediction_cache import predict_with_cache


class Payload:
    def __init__(self, **data):
        self.data = data

    def model_dump(self, **kwargs):
        return dict(self.data)


def test_cached_diagnostics_require_identical_request_and_artifact(tmp_path):
    calls = []
    def predict(request):
        calls.append(request.data)
        return Payload(value=len(calls))
    runtime = SimpleNamespace(manifest=Payload(weightsSha256="one", calibration="a"), predict=predict)
    request = Payload(stem="question", provenance={"contentQualified": True})
    assert predict_with_cache(runtime, request, tmp_path) == {"value": 1}
    assert predict_with_cache(runtime, request, tmp_path) == {"value": 1}
    request.data["provenance"] = {"contentQualified": False}
    assert predict_with_cache(runtime, request, tmp_path) == {"value": 2}
    runtime.manifest.data["calibration"] = "b"
    assert predict_with_cache(runtime, request, tmp_path) == {"value": 3}
    assert len(calls) == 3


def test_corrupt_cached_prediction_is_recomputed(tmp_path):
    calls = []
    def predict(request):
        calls.append(True)
        return Payload(value="original")
    runtime = SimpleNamespace(manifest=Payload(weightsSha256="one"), predict=predict)
    request = Payload(stem="question")
    predict_with_cache(runtime, request, tmp_path)
    path = next(tmp_path.glob("*.json"))
    saved = json.loads(path.read_text())
    saved["prediction"]["value"] = "changed"
    path.write_text(json.dumps(saved))
    assert predict_with_cache(runtime, request, tmp_path) == {"value": "original"}
    assert len(calls) == 2
