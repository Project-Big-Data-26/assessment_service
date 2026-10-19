from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

class Option(BaseModel):
    option_id: str
    text: str
    alasan: Optional[str] = None

class Pertanyaan(Document):
    subbab_id: Optional[PydanticObjectId] = None
    kelas_id: Optional[PydanticObjectId] = None

    soal_text: str
    image_url: List[str] = []
    options: List[Option] = []
    jawaban: Optional[str] = None

    cognitive_level: Optional[str] = None
    cognitive_score: Optional[int] = None
    confidence_score: Optional[int] = None

    status: Literal["active", "inactive"] = "inactive"


    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "soal"
        indexes = [
            "subbab_id",
            "kelas_id",
            "status",
            "source_file",
            "soal_type",
        ]
