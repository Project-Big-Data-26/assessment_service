"""Public advisory-only inference API for the frozen 3x4x3 contract."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request, status

from app.classification.v2.contracts import V2ClassificationRequest, V2ClassificationResponse
from app.classification.v2.runtime import ContentConflictError, V2ClassifierRuntime

router = APIRouter(prefix="/v2", tags=["indobert-3x4x3"])


def runtime_or_503(request: Request) -> V2ClassifierRuntime:
    runtime = getattr(request.app.state, "v2_runtime", None)
    error = getattr(request.app.state, "v2_runtime_error", None)
    if runtime is None or runtime.failed_reason:
        detail = "v2 model artifact is unavailable or failed integrity checks"
        if error and request.app.debug:
            detail = f"{detail}: {error}"
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, detail)
    return runtime


@router.get("/model-info")
def model_info(request: Request):
    runtime = getattr(request.app.state, "v2_runtime", None)
    error = getattr(request.app.state, "v2_runtime_error", None)
    if runtime is None:
        return {
            "artifactReady": False,
            "approvedForProvisional": False,
            "tasks": ["mathCognitiveDomain_3", "knowledgeDimension_4", "intendedDifficulty_3"],
            "error": str(error) if error and request.app.debug else None,
        }
    manifest = runtime.manifest
    return {
        "artifactReady": runtime.failed_reason is None,
        "approvedForProvisional": manifest.approvedForProvisional,
        "modelVersion": manifest.modelVersion,
        "baseModel": manifest.baseModel,
        "baseRevision": manifest.baseRevision,
        "datasetSnapshot": manifest.datasetSnapshot,
        "rubricVersion": manifest.rubricVersion,
        "tasks": ["mathCognitiveDomain_3", "knowledgeDimension_4", "intendedDifficulty_3"],
        "reviewRequired": True,
    }


@router.get("/llm-info")
def llm_info(request: Request):
    """Report local Gemini readiness without contacting Google or spending tokens."""
    runtime = getattr(request.app.state, "gemini_runtime", None)
    error = getattr(request.app.state, "gemini_runtime_error", None)
    if runtime is None:
        return {
            "configured": False,
            "provider": "gemini",
            "liveEnabled": False,
            "error": str(error) if error and request.app.debug else None,
        }
    return {
        "configured": True,
        **runtime.settings.public_info(),
        "purpose": "advisory_review_after_indobert",
        "goldLabelAuthority": False,
        "networkChecked": False,
    }


@router.get("/health/ready")
def ready(request: Request):
    runtime = runtime_or_503(request)
    return {
        "status": "ready",
        "modelVersion": runtime.manifest.modelVersion,
        "artifactChecksumsVerified": True,
    }


@router.post("/classify", response_model=V2ClassificationResponse)
def classify(payload: V2ClassificationRequest, request: Request):
    runtime = runtime_or_503(request)
    try:
        return runtime.predict(payload)
    except ContentConflictError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    except FloatingPointError as exc:
        runtime.failed_reason = str(exc)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "model produced invalid probabilities") from exc
