from beanie import Document

class Kelas(Document):
    nama: str # Sesuaikan dengan nama field teks yang ada di database Anda

    class Settings:
        name = "kelas" # Nama collection yang persis ada di MongoDB Compass