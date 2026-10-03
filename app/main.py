"""FastAPI entry point for legacy v1 and research-grade advisory v2."""
from __future__ import annotations
from contextlib import asynccontextmanager
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel, Field
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
from app.verification.arithmetic import verify_arithmetic
from app.staff.repository import MongoRepository
from app.staff.routes import router as staff_router
from app.staff.assets import PrivateAssetSigner
from app.api.v2 import router as v2_router
from app.classification.v2.runtime import V2ClassifierRuntime
from app.llm import GeminiReviewRuntime
from app.assessment.routes import router as assessment_router, info_router as psychometrics_info_router
from app.assessment.store import AssessmentStore
from app.psychometrics.analysis import load_policy

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = PROJECT_ROOT / "models" / "indobert-multitask-v1"
V2_ARTIFACT_DIR = Path(os.getenv("INDOBERT_V2_ARTIFACT_DIR", PROJECT_ROOT / "models" / "indobert-3x4x3-v1"))
EXTRACTION_SETTINGS = load_extraction_settings(PROJECT_ROOT / "configs" / "extraction_config.yaml")

def create_classifier():
    if all((ARTIFACT_DIR / name).exists() for name in ("manifest.json", "model.pt", "tokenizer")):
        return IndoBERTClassifier(ARTIFACT_DIR)
    return RuleBasedBaselineClassifier()

classifier = create_classifier()
pipeline = QuestionIntelligencePipeline(classifier)


def create_v2_runtime() -> tuple[V2ClassifierRuntime | None, str | None]:
    try:
        return V2ClassifierRuntime(V2_ARTIFACT_DIR), None
    except (FileNotFoundError, ImportError, RuntimeError, ValueError) as exc:
        return None, f"{type(exc).__name__}: {exc}"


def create_gemini_runtime() -> tuple[GeminiReviewRuntime | None, str | None]:
    """Build the client without making a network request or consuming tokens."""
    try:
        return GeminiReviewRuntime.from_environment(), None
    except (ImportError, RuntimeError, ValueError) as exc:
        return None, f"{type(exc).__name__}: {exc}"


staff_repository = MongoRepository.from_environment()
asset_signer = PrivateAssetSigner.from_environment()
v2_runtime, v2_runtime_error = create_v2_runtime()
gemini_runtime, gemini_runtime_error = create_gemini_runtime()
psychometrics_policy = load_policy(os.getenv("PSYCHOMETRICS_POLICY_PATH", PROJECT_ROOT / "configs" / "psychometrics_policy.json"))


def create_assessment_store():
    return AssessmentStore(
        os.getenv("ASSESSMENT_DB_PATH", PROJECT_ROOT / "data" / "local" / "assessments.sqlite3"),
        subject_secret=os.getenv("ASSESSMENT_SUBJECT_SECRET") or None,
    )


@asynccontextmanager
async def lifespan(application: FastAPI):
    application.state.staff_repository = staff_repository
    application.state.asset_signer = asset_signer
    application.state.staff_repository_error = None
    application.state.v2_runtime = v2_runtime
    application.state.v2_runtime_error = v2_runtime_error
    application.state.gemini_runtime = gemini_runtime
    application.state.gemini_runtime_error = gemini_runtime_error
    if getattr(application.state, "assessment_store", None) is None:
        application.state.assessment_store = create_assessment_store()
    if staff_repository is not None:
        try:
            await staff_repository.ping()
            await staff_repository.ensure_indexes()
        except Exception as exc:  # keep public v1/v2 diagnostics available
            application.state.staff_repository_error = f"{type(exc).__name__}: {exc}"
            application.state.staff_repository = None
    try:
        yield
    finally:
        if staff_repository is not None:
            await staff_repository.close()


app = FastAPI(title="Nalar Question Intelligence", version="2.2.0", lifespan=lifespan)
# Defaults also support test clients that do not enter a lifespan context.
app.state.staff_repository = staff_repository
app.state.asset_signer = asset_signer
app.state.staff_repository_error = None
app.state.v2_runtime = v2_runtime
app.state.v2_runtime_error = v2_runtime_error
app.state.gemini_runtime = gemini_runtime
app.state.gemini_runtime_error = gemini_runtime_error
app.state.psychometrics_policy = psychometrics_policy
app.state.assessment_store = None
app.include_router(v2_router)
app.include_router(staff_router)
app.include_router(assessment_router)
app.include_router(psychometrics_info_router)
allowed_hosts = [item.strip() for item in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1,testserver").split(",") if item.strip()]
allowed_origins = [item.strip() for item in os.getenv("ALLOWED_ORIGINS", "http://localhost:8000").split(",") if item.strip()]
app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-CSRF-Token", "Authorization", "Idempotency-Key", "X-Internal-API-Key"],
)


@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    if request.url.path.startswith(("/internal/v2", "/api/v1")):
        response.headers["Cache-Control"] = "no-store"
    return response

@app.get("/health")
def health(): return {"status": "ok", "service": "question-intelligence"}

@app.get("/v1/model-info")
def model_info():
    artifact_ready = isinstance(classifier, IndoBERTClassifier)
    manifest = classifier.manifest if artifact_ready else {}
    metrics = manifest.get("metrics", {})
    provisional_eligible = (
        artifact_ready
        and manifest.get("approved_for_provisional") is True
        and manifest.get("demo_only") is False
        and isinstance(manifest.get("dataset_rows"), int)
        and manifest["dataset_rows"] >= 60
        and all(isinstance(metrics.get(head), dict) and metrics[head] for head in ("bloom", "knowledge", "difficulty"))
    )
    return {"classifier": classifier.__class__.__name__, "artifact_ready": artifact_ready,
            "provisional_eligible": provisional_eligible, "model_version": manifest.get("model_version"),
            "base_model": manifest.get("base_model", "indobenchmark/indobert-base-p1"),
            "tasks": ["bloom_6", "knowledge_4", "difficulty_3"],
            "warning": "Rules baseline and unapproved/demo model artifacts are advisory only."}

@app.get("/v1/extraction-info")
def extraction_info():
    return {
        **extraction_capabilities(),
        "supported_extensions": sorted(SUPPORTED_EXTENSIONS),
        "ocr_language": EXTRACTION_SETTINGS.ocr_language,
        "ocr_dpi": EXTRACTION_SETTINGS.ocr_dpi,
        "max_pdf_pages": EXTRACTION_SETTINGS.max_pdf_pages,
    }

class AnswerVerificationRequest(BaseModel):
    questionText: str = Field(min_length=1, max_length=10000)
    options: list[dict[str, str]] = Field(default_factory=list)
    answerSpec: dict

@app.post("/v1/verify-answer")
def verify_answer(request: AnswerVerificationRequest):
    return verify_arithmetic(request.questionText, request.options, request.answerSpec)

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
