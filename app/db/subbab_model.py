from beanie import Document

class Subbab(Document):
    name: str # Sesuaikan dengan nama field teks yang ada di database Anda

    class Settings:
        name = "subbab" # Nama collection yang persis ada di MongoDB Compass