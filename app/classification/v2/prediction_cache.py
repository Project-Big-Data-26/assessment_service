"""Reuse offline diagnostics only for identical requests and verified artifacts."""
import hashlib
import json
from pathlib import Path
import tempfile


def _hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def predict_with_cache(runtime, request, directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    code = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ("runtime.py", "serializer.py", "calibration.py", "prediction_cache.py")}
    identity = _hash({"request": request.model_dump(mode="json"),
                      "artifact": runtime.manifest.model_dump(mode="json"), "code": code})
    path = directory / (identity + ".json")
    if path.exists():
        try:
            saved = json.loads(path.read_text(encoding="utf-8"))
            if saved["identity"] == identity and saved["predictionHash"] == _hash(saved["prediction"]):
                return saved["prediction"]
        except (ValueError, KeyError, TypeError):
            pass
    prediction = runtime.predict(request).model_dump(mode="json")
    data = {"identity": identity, "prediction": prediction, "predictionHash": _hash(prediction)}
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=directory,
                                         prefix=identity, suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(data, stream, ensure_ascii=False)
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return prediction
