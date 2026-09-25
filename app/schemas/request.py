"""Public API request contracts."""
from pydantic import BaseModel, Field

class ClassificationRequest(BaseModel):
    question_id: str = Field(min_length=1, max_length=100)
    question_text: str = Field(min_length=10, max_length=10000)
    question_type: str = "multiple_choice"
    subject: str = "Matematika"
    grade: int | None = Field(default=None, ge=1, le=12)
    topic: str | None = None
    subtopic: str | None = None
    options: list[str] = Field(default_factory=list, max_length=8)
    learning_objective: str | None = None
    reasoning_steps: int | None = Field(default=None, ge=1, le=10)
