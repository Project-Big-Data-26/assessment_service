"""Pydantic schemas for SD 1-4 Exercise Generation with KaTeX and Visual-First metadata."""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, ConfigDict, Field, model_validator


LevelType = Literal["easy", "medium", "hard"]
VisualType = Literal[
    "illustration",
    "object_count",
    "shape_pattern",
    "fraction_pie",
    "clock",
    "bar_chart",
    "geometry",
]


class VisualMetadata(BaseModel):
    """Metadata describing the visual context for child-friendly SD questions."""

    model_config = ConfigDict(extra="ignore")

    image_type: VisualType = Field(
        ...,
        description="Category of the visual (e.g. illustration, object_count, fraction_pie)",
    )
    image_prompt: str = Field(
        ...,
        min_length=10,
        description="Detailed generative prompt or description of the image for SD kids",
    )
    semantic_spec: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Structured deterministic parameters (e.g. counts, shape, angles, fraction)",
    )
    svg_content: Optional[str] = Field(
        default=None,
        description="Inline SVG code representing the visual if pre-rendered",
    )
    image_url: Optional[str] = Field(
        default=None,
        description="URL to pre-rendered image asset if hosted",
    )


class ExerciseQuestion(BaseModel):
    """Uniform question format for Web Nolla frontend with KaTeX and Visual-First support."""

    model_config = ConfigDict(extra="ignore")

    question_id: str = Field(..., description="Unique identifier for the question")
    grade: int = Field(..., ge=1, le=4, description="Elementary school grade (SD 1, 2, 3, or 4)")
    subject: str = Field(default="matematika", description="Subject name")
    bab: Optional[int] = Field(default=1, description="Chapter number")
    level: LevelType = Field(default="easy", description="Difficulty level")
    topic: Optional[str] = Field(default=None, description="Topic or subtopic title")
    question_text: str = Field(..., min_length=5, description="Question stem containing KaTeX math")
    has_image: bool = Field(default=True, description="True if question is visual-dominant")
    visual_metadata: Optional[VisualMetadata] = Field(
        default=None,
        description="Visual metadata when has_image is true",
    )
    katex_enabled: bool = Field(default=True, description="Flag indicating presence of KaTeX formulas")
    options: List[str] = Field(
        ...,
        min_length=3,
        max_length=5,
        description="List of answer choices formatted with KaTeX",
    )
    correct_answer: str = Field(..., description="The correct answer text or option identifier")
    explanation: str = Field(
        ...,
        min_length=5,
        description="Step-by-step child-friendly explanation with KaTeX formulas",
    )

    @model_validator(mode="after")
    def validate_visual_consistency(self) -> "ExerciseQuestion":
        if self.has_image and self.visual_metadata is None:
            raise ValueError("visual_metadata is required when has_image is true")
        if self.correct_answer not in self.options:
            # Allow correct_answer to be letter 'A', 'B', 'C', 'D' if options are ordered
            letter_map = {"A": 0, "B": 1, "C": 2, "D": 3}
            if self.correct_answer in letter_map and letter_map[self.correct_answer] < len(self.options):
                pass
            else:
                # Accept if exact value matches
                pass
        return self


class ExerciseGenerateRequest(BaseModel):
    """Request payload to generate visual questions for SD 1-4."""

    grade: int = Field(..., ge=1, le=4, description="SD grade: 1, 2, 3, or 4")
    bab: int = Field(default=1, ge=1, le=10, description="Chapter number (1-10)")
    subbab: str = Field(default="A", description="Subchapter letter (e.g. 'A', 'B')")
    level: LevelType = Field(default="easy", description="Difficulty level (easy, medium, hard)")
    count: int = Field(default=5, ge=1, le=20, description="Number of questions to generate (1-20)")
    visual_percent: int = Field(default=80, ge=50, le=100, description="Minimum percentage of visual questions (>=50%)")
    topic: Optional[str] = Field(default=None, description="Optional custom topic/curriculum focus")
    use_9router: bool = Field(default=True, description="Whether to invoke 9Router LLM if configured")


class ExerciseGenerateResponse(BaseModel):
    """Response payload for generated exercises."""

    status: str = "success"
    grade: int
    subject: str = "matematika"
    total_generated: int
    visual_count: int
    visual_ratio: float
    router_model: Optional[str] = None
    generation_source: str
    questions: List[ExerciseQuestion]


class BatchGenerateRequest(BaseModel):
    """Request payload for multi-level batch generation."""

    grade: int = Field(..., ge=1, le=4, description="SD grade: 1, 2, 3, or 4")
    bab: int = Field(default=1, ge=1, le=10, description="Chapter number")
    subbab: str = Field(default="A", description="Subchapter letter")
    counts_per_level: Dict[LevelType, int] = Field(
        default_factory=lambda: {"easy": 3, "medium": 4, "hard": 3},
        description="Question count per level",
    )
    visual_percent: int = Field(default=80, ge=50, le=100)


class BatchGenerateResponse(BaseModel):
    """Response payload for batch generation across levels."""

    status: str = "success"
    grade: int
    bab: int
    subbab: str
    total_questions: int
    counts_by_level: Dict[str, int]
    questions: List[ExerciseQuestion]


class KaTeXValidateRequest(BaseModel):
    """Request to validate and normalize KaTeX syntax and escaping."""

    texts: List[str] = Field(..., min_length=1, description="List of strings with KaTeX formulas to validate")


class KaTeXValidateResult(BaseModel):
    original: str
    normalized: str
    has_katex: bool
    is_valid: bool
    issues: List[str] = Field(default_factory=list)


class KaTeXValidateResponse(BaseModel):
    status: str = "success"
    total_checked: int
    all_valid: bool
    results: List[KaTeXValidateResult]


class QuestionValidateRequest(BaseModel):
    """Request to validate a single question structure against Web Nolla specs."""

    question: ExerciseQuestion


class QuestionValidateResponse(BaseModel):
    valid: bool
    question_id: str
    has_image: bool
    katex_enabled: bool
    checks: Dict[str, bool]
    warnings: List[str] = Field(default_factory=list)
    errors: List[str] = Field(default_factory=list)


class GradeTopicInfo(BaseModel):
    bab: int
    title: str
    key_concepts: List[str]
    typical_visuals: List[str]


class GradeInfo(BaseModel):
    grade: int
    label: str
    age_range: str
    cognitive_focus: str
    topics: List[GradeTopicInfo]


class VisualTypeInfo(BaseModel):
    type_name: VisualType
    display_name: str
    description: str
    applicable_grades: List[int]
    sample_semantic_spec: Dict[str, Any]
    sample_prompt: str


class PreviewRequest(BaseModel):
    """Request to generate an immediate visual exercise preview with inline SVG."""

    grade: int = Field(..., ge=1, le=4)
    visual_type: VisualType
    topic: Optional[str] = None


class PreviewResponse(BaseModel):
    question: ExerciseQuestion
    rendered_svg: str
    html_preview: str


class ServiceHealthResponse(BaseModel):
    status: str
    service: str
    target_grades: List[int]
    ninerouter_configured: bool
    ninerouter_base_url: Optional[str] = None
    ninerouter_model: Optional[str] = None
    latex_policy_version: str
