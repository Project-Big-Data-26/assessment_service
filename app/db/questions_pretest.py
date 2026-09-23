from beanie import Document
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Option(BaseModel):
    option_id: str
    text: str

class Pertanyaan(Document):
    subbab_id: Optional[str] = None
    kelas_id: Optional[str] = None
    pertanyaan_text: str
    image_url: Optional[str] = None
    pertanyaan_type: str
    options: List[Option] = []
    correct_answer: Optional[str] = None
    cognitive_level: Optional[str] = None
    cognitive_score: Optional[int] = None
    status: str = "needs_review"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        pertanyaan: str = "pertanyaan"