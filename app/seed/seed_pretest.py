import json
import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.db.questions_pretest import Pertanyaan, Option

async def run_seeder():
    client = AsyncIOMotorClient("mongodb+srv://romadhonim1_db_user:cEaG3NBp2wKc99VF@cluster0.nn1euxs.mongodb.net/project_assessment?appName=Cluster0")

    await init_beanie(database=client.math_learning_db, document_models=[Pertanyaan])

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_dir, "output", "pretest", "kelas1", "soal_pretest_db.json")

    if not os.path.exists(file_path):
        print(f"File JSON tidak ditemukan di: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data_json = json.load(f)

    soal_siap_insert = []

    for item in data_json:
        opsi_jawaban = []
        for opt in item.get("options", []):
            opsi_jawaban.append(Option(
                option_id=opt.get("option_id", ""),
                text=opt.get("text", "")
            ))

        raw_image = item.get("image_url")
        if isinstance(raw_image, list) and len(raw_image) > 0:
            gambar_valid = raw_image[0] 
        elif isinstance(raw_image, str):
            gambar_valid = raw_image
        else:
            gambar_valid = None

        soal = Pertanyaan(
            soal_text=item.get("soal_text", ""),
            soal_type=item.get("soal_type", "Pilihan Ganda"),
            image_url=gambar_valid, 
            options=opsi_jawaban,
            source_file=item.get("berkas_id") or "buku_sibi.pdf", 
            status="draft"
        )
        soal_siap_insert.append(soal)

    if soal_siap_insert:
        try:
            await Pertanyaan.insert_many(soal_siap_insert)
            print(f"✅ Berhasil memasukkan {len(soal_siap_insert)} soal ke database math_learning_db!")
        except Exception as e:
            print(f"❌ Terjadi kesalahan saat insert: {e}")
    else:
        print("⚠ Tidak ada data soal yang diproses.")

if __name__ == "__main__":
    asyncio.run(run_seeder())