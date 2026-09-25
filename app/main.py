"""FastAPI entry point for classification and multimodal extraction."""
from __future__ import annotations
from dataclasses import asdict
from pathlib import Path
from tempfile import TemporaryDirectory
from fastapi import FastAPI, File, HTTPException, UploadFile
from app.classification import RuleBasedBaselineClassifier
from app.classification.indobert import IndoBERTClassifier
from app.extraction import (
    SUPPORTED_EXTENSIONS,
    extract_document,
    extraction_capabilities,
    load_extraction_settings,
)
from app.pipeline import QuestionIntelligencePipeline
from app.schemas.request import ClassificationRequest
from app.schemas.response import ClassificationResponse, ExtractionResponse, HeadPrediction

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = PROJECT_ROOT / "models" / "indobert-multitask-v1"
EXTRACTION_SETTINGS = load_extraction_settings(PROJECT_ROOT / "configs" / "extraction_config.yaml")

def create_classifier():
    if (ARTIFACT_DIR / "manifest.json").is_file() and (ARTIFACT_DIR / "model.pt").is_file():
        return IndoBERTClassifier(ARTIFACT_DIR)
    return RuleBasedBaselineClassifier()

classifier = create_classifier()
pipeline = QuestionIntelligencePipeline(classifier)
app = FastAPI(title="Nalar Question Intelligence", version="1.0.0")

@app.get("/health")
def health(): return {"status": "ok", "service": "question-intelligence"}

@app.get("/v1/model-info")
def model_info():
    return {"classifier": classifier.__class__.__name__, "artifact_ready": ARTIFACT_DIR.is_dir(), "base_model": "indobenchmark/indobert-base-p1", "tasks": ["bloom_6", "knowledge_4", "difficulty_3"], "warning": "The rules baseline is advisory only when a trained artifact is absent."}

@app.get("/v1/extraction-info")
def extraction_info():
    return {
        **extraction_capabilities(),
        "supported_extensions": sorted(SUPPORTED_EXTENSIONS),
        "ocr_language": EXTRACTION_SETTINGS.ocr_language,
        "ocr_dpi": EXTRACTION_SETTINGS.ocr_dpi,
        "max_pdf_pages": EXTRACTION_SETTINGS.max_pdf_pages,
    }

@app.post("/v1/classify", response_model=ClassificationResponse)
def classify(request: ClassificationRequest):
    combined = " [SEP] ".join(filter(None, [request.question_text, " ".join(request.options), request.learning_objective, request.topic, request.subtopic]))
    result = pipeline.run({"question_id": request.question_id, "question_text": combined})
    prediction = result.prediction
    minimum = min(value for value in [prediction.bloom_confidence, prediction.knowledge_confidence, prediction.difficulty_confidence] if value is not None)
    return ClassificationResponse(
        question_id=request.question_id,
        bloom=HeadPrediction(label=prediction.bloom_level, confidence=prediction.bloom_confidence),
        knowledge_dimension=HeadPrediction(label=prediction.knowledge_dimension, confidence=prediction.knowledge_confidence),
        difficulty=HeadPrediction(label=prediction.difficulty_level, confidence=prediction.difficulty_confidence),
        model_version=prediction.model_version, status=prediction.status, prediction_source=prediction.prediction_source,
        rationale=list(prediction.rationale), review_required=prediction.status != "completed" or minimum < 0.7,
    )

@app.post("/v1/extract", response_model=ExtractionResponse)
async def extract(file: UploadFile = File(...)):
    suffix = Path(file.filename or "upload.bin").suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS: raise HTTPException(415, "Unsupported file type")
    content = await file.read()
    if len(content) > 10 * 1024 * 1024: raise HTTPException(413, "File exceeds 10 MB")
    # A directory-scoped file can be reopened by OCR/PDF libraries on Windows;
    # NamedTemporaryFile remains locked there while its context is active.
    with TemporaryDirectory(prefix="nalar-extract-") as directory:
        temporary_path = Path(directory) / f"source{suffix}"
        temporary_path.write_bytes(content)
        result = extract_document(
            temporary_path,
            media_type=file.content_type or "application/octet-stream",
            settings=EXTRACTION_SETTINGS,
        )
    return ExtractionResponse(filename=file.filename or "upload", media_type=file.content_type or "application/octet-stream", **result)
