from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Option(BaseModel):
    option_id: str
    text: str

class Pertanyaan(Document):
    subbab_id: Optional[PydanticObjectId] = None
    kelas_id: Optional[PydanticObjectId] = None

    soal_text: str
    image_url: Optional[str] = None
    image_urls: List[str] = []
    soal_type: str = ["pilihan_ganda"]
    options: List[Option] = []
    jawaban: Optional[str] = None

    cognitive_level: Optional[str] = None
    cognitive_score: Optional[int] = None
    diffiuclty_label: Optional[str] = None

    status: str = "draft"

    source_file: str
    source_page: Optional[int] = None
    source_section: Optional[str] = None
    source_bab: Optional[str] = None
    source_subbab: Optional[str] = None
    source_item_no: Optional[str] = None

    extraction_confidence: Optional[float] = None
    extraction_flags: List[str] = []
    mcq_generation_confidence: Optional[float] = None
    validation_result: Optional[dict] = None
    pipeline_version: Optional[str] = None

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
