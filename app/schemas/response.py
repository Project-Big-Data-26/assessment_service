"""Public API response contracts."""
from pydantic import BaseModel, Field

class HeadPrediction(BaseModel):
    label: str | None
    confidence: float | None = Field(default=None, ge=0, le=1)

class ClassificationResponse(BaseModel):
    question_id: str
    bloom: HeadPrediction
    knowledge_dimension: HeadPrediction
    difficulty: HeadPrediction
    model_version: str | None
    status: str
    prediction_source: str
    rationale: list[str]
    review_required: bool

class ExtractedOption(BaseModel):
    label: str
    text: str

class ExtractedVisualPreview(BaseModel):
    page_number: int = Field(ge=1)
    mime_type: str
    data_url: str
    width: int = Field(ge=1)
    height: int = Field(ge=1)
    crop_method: str

class ExtractedMathFormula(BaseModel):
    latex: str
    page_number: int = Field(ge=1)
    bbox: list[float] = Field(min_length=4, max_length=4)
    source: str
    latex_renderable: bool = True
    visual_data_url: str
    visual_width: int = Field(ge=1)
    visual_height: int = Field(ge=1)

class ExtractedPage(BaseModel):
    page_number: int = Field(ge=1)
    text: str
    method: str
    confidence: float | None = Field(default=None, ge=0, le=1)
    warnings: list[str] = Field(default_factory=list)

class ExtractedQuestion(BaseModel):
    candidate_id: str
    question_number: str | None = None
    question_text: str
    classification_text: str = ""
    options: list[ExtractedOption] = Field(default_factory=list)
    page_numbers: list[int] = Field(default_factory=list)
    extraction_method: str
    needs_review: bool
    review_reasons: list[str] = Field(default_factory=list)
    visual_previews: list[ExtractedVisualPreview] = Field(default_factory=list)
    math_formulas: list[ExtractedMathFormula] = Field(default_factory=list)

class DocumentMetadata(BaseModel):
    page_count: int | None = Field(default=None, ge=0)
    title: str | None = None
    author: str | None = None
    is_encrypted: bool = False

class ExtractionResponse(BaseModel):
    filename: str
    media_type: str
    extracted_text: str
    latex_candidates: list[str] = Field(default_factory=list)
    confidence: float | None = None
    status: str
    warnings: list[str] = Field(default_factory=list)
    review_required: bool = False
    document_metadata: DocumentMetadata = Field(default_factory=DocumentMetadata)
    pages: list[ExtractedPage] = Field(default_factory=list)
    questions: list[ExtractedQuestion] = Field(default_factory=list)
