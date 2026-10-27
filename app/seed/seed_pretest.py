import json
import asyncio
import os
from bson import ObjectId  # <--- WAJIB IMPORT INI UNTUK MENGUBAH STRING JADI OBJECT ID
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.db.questions_pretest import Pertanyaan, Option
from app.db.subbab_model import Subbab # <-- Sesuaikan dengan import model Subbab Anda

# =====================================================================
# 🔧 AREA KONFIGURASI (Ganti isinya setiap kali pindah kelas)
# =====================================================================
# Paste _id dari collection kelas di MongoDB Compass ke sini
TARGET_KELAS_ID = "6ac27a1ddd8ac1fcf5c8e92b" 

# Sesuaikan jalur file JSON target Anda
TARGET_FILE_JSON = "output/exercise/kelas5/batch01/hasil_validasi/validation_results.json"
# =====================================================================


async def run_seeder():
    # 1. Inisialisasi Database
    client = AsyncIOMotorClient("mongodb+srv://romadhonim1_db_user:cEaG3NBp2wKc99VF@cluster0.nn1euxs.mongodb.net/project_assessment?appName=Cluster0")
    await init_beanie(database=client.math_learning_db, document_models=[Pertanyaan, Subbab])

    # 2. Validasi dan Konversi ID Kelas
    try:
        kelas_id_asli = ObjectId(TARGET_KELAS_ID)
    except Exception:
        print("❌ FORMAT ID KELAS SALAH: Pastikan Anda menyalin dari MongoDB tanpa tanda kutip tambahan.")
        return

    # 3. Tarik data Subbab dari DB untuk pencocokan
    data_subbab_db = await Subbab.find_all().to_list()
    map_subbab = {s.name: s.id for s in data_subbab_db}

    # 4. Baca File JSON
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_dir, TARGET_FILE_JSON)
    
    if not os.path.exists(file_path):
        print(f"❌ File JSON tidak ditemukan di: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data_json = json.load(f)

    soal_siap_insert = []

    # 5. Mapping Data
    for item in data_json:
        opsi_jawaban = []
        for opt in item.get("options", []):
            opsi_jawaban.append(Option(
                option_id=opt.get("option_id", ""),
                text=opt.get("text", ""),
                alasan=opt.get("alasan", "")
            ))

        raw_image = item.get("image_url")
        if isinstance(raw_image, list):
            gambar_valid = raw_image
        elif isinstance(raw_image, str) and raw_image.strip() != "":
            gambar_valid = [raw_image]
        else:
            gambar_valid = []

        raw_status = item.get("status")
        status_valid = "active" if raw_status == "active" else "inactive"

        # Pencocokan Subbab ID
        nama_subbab_json = item.get("subbab_id") 
        subbab_id_asli = map_subbab.get(nama_subbab_json)

        # Buat document
        soal = Pertanyaan(
            soal_text=item.get("soal_text", ""),
            soal_type=item.get("soal_type", "Pilihan Ganda"),
            image_url=gambar_valid,
            options=opsi_jawaban,
            source_file=item.get("berkas_id") or "buku_sibi.pdf", 
            jawaban=item.get("jawaban"),
            cognitive_level=item.get("cognitive_level"),
            cognitive_score=item.get("cognitive_score"),
            confidence_score=item.get("confidence_score"),
            
            kelas_id=kelas_id_asli,    # <-- ID kelas disuntikkan secara serentak dari konfigurasi atas
            subbab_id=subbab_id_asli,  # <-- ID subbab dinamis per soal
            
            status=status_valid
        )
        soal_siap_insert.append(soal)

    # 6. Insert ke DB
    if soal_siap_insert:
        try:
            await Pertanyaan.insert_many(soal_siap_insert)
            print(f"✅ Berhasil memasukkan {len(soal_siap_insert)} soal validasi ke database!")
        except Exception as e:
            print(f"❌ Terjadi kesalahan saat insert: {e}")
    else:
        print("⚠ Tidak ada data soal yang diproses.")

if __name__ == "__main__":
    asyncio.run(run_seeder())