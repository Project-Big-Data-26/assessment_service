"""Demonstration seed covering 6 cognitive processes x 4 knowledge dimensions.

These labels exercise the pipeline and UI. They are not a validated training corpus.
"""
from __future__ import annotations

BLOOM = (("C1", "Mengingat"), ("C2", "Memahami"), ("C3", "Menerapkan"), ("C4", "Menganalisis"), ("C5", "Mengevaluasi"), ("C6", "Mencipta"))
KNOWLEDGE = (("factual", "Faktual"), ("conceptual", "Konseptual"), ("procedural", "Prosedural"), ("metacognitive", "Metakognitif"))
DIFFICULTY = ("Easy", "Medium", "Hard", "Medium")
PROMPTS = {
    "C1": ("Sebutkan nilai $\\pi$ yang biasa digunakan pada perhitungan lingkaran.", "Identifikasi nama sifat yang menyatakan $a+b=b+a$.", "Tuliskan rumus luas segitiga.", "Sebutkan strategi pengecekan paling dasar setelah menyelesaikan persamaan."),
    "C2": ("Jelaskan arti simbol $r$ pada rumus $L=\\pi r^2$.", "Jelaskan mengapa jumlah sudut dalam segitiga adalah $180^\\circ$.", "Jelaskan dengan kata-katamu sendiri cara menyamakan penyebut pecahan.", "Jelaskan kapan estimasi lebih tepat digunakan daripada perhitungan eksak."),
    "C3": ("Gunakan rumus $K=2\\pi r$ untuk menghitung keliling lingkaran dengan $r=7$ cm.", "Tentukan gradien garis yang melalui titik $(0,1)$ dan $(3,4)$.", "Selesaikan persamaan $2x+5=17$ menggunakan prosedur aljabar yang benar.", "Pilih dan terapkan strategi yang paling efisien untuk menghitung $25\\%$ dari 320."),
    "C4": ("Kelompokkan data $2,2,3,5,8,8$ berdasarkan modus, median, dan rentangnya.", "Analisis hubungan antara koefisien $a$ dan bentuk grafik $y=ax^2$.", "Temukan kesalahan pada langkah: $2(x+3)=10$, lalu ditulis $2x+3=10$.", "Bandingkan dua strategi penyelesaian $x^2-5x+6=0$ dan jelaskan strategi yang lebih efisien."),
    "C5": ("Nilai kebenaran klaim bahwa semua bilangan prima adalah ganjil dan berikan bukti penyangkal.", "Evaluasi apakah grafik yang diberikan benar-benar merepresentasikan fungsi.", "Periksa solusi $x=4$ untuk persamaan $3x-2=10$ dan berikan justifikasi.", "Nilai strategi belajarmu saat menyelesaikan soal geometri dan usulkan perbaikannya."),
    "C6": ("Buat satu contoh himpunan berisi lima bilangan dengan median 8.", "Rancang model matematika untuk memperkirakan biaya perjalanan berdasarkan jarak.", "Susun prosedur untuk menentukan tinggi gedung menggunakan kesebangunan segitiga.", "Rancang dua cara berbeda untuk memeriksa jawaban sistem persamaan linear."),
}

def build_math_seed() -> list[dict[str, object]]:
    records = []
    for bloom_index, (bloom, bloom_name) in enumerate(BLOOM):
        for knowledge_index, (knowledge, knowledge_name) in enumerate(KNOWLEDGE):
            records.append({
                "question_id": f"MTK-{bloom}-{knowledge_index + 1}", "question_text": PROMPTS[bloom][knowledge_index],
                "subject": "Matematika", "material_id": f"MTK-{bloom_index + 1:02d}-{knowledge_index + 1:02d}",
                "bloom_label": bloom, "bloom_name": bloom_name, "knowledge_label": knowledge,
                "knowledge_name": knowledge_name, "difficulty_label": DIFFICULTY[(bloom_index + knowledge_index) % len(DIFFICULTY)],
                "label_status": "demo_seed_unvalidated", "source": "curated demonstration seed",
            })
    return records
