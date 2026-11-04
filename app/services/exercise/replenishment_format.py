"""Common question layout and factual explanations for generated wrong options."""
import re
import sympy as s
from .replenishment_math import m

QUESTION_KEYS = ("tipe_generate", "variasi_cara", "acuan", "cognitive_c", "jumlah_langkah",
                 "jenis_soal", "alasan_level", "stimulus", "pertanyaan", "jawaban_benar",
                 "alasan_benar", "distraktor", "pembahasan", "catatan", "id")


def standard_question(question):
    """Keep the established contract; omit unused optional text-question fields."""
    result = {key: question[key] for key in QUESTION_KEYS if key in question}
    for key, value in question.items():
        if key in result or (key in ("gambar", "dipaksa_kuota") and not value):
            continue
        result[key] = value
    return result


def exact_value(value):
    # Values are generated arithmetic proofs, not free-form source expressions.
    if re.search(r"[^A-Za-z0-9+*/()., -]", value):
        raise ValueError("Unexpected proof expression")
    words=set(re.findall(r"[A-Za-z]+",value))
    if words-{"sqrt","pi"}:
        raise ValueError("Unexpected proof function")
    return s.simplify(s.sympify(value,locals={"sqrt":s.sqrt,"pi":s.pi}))


def distractor_reason(question, index, proof):
    wrong = question["distraktor"][index]["teks"]
    answer = question["jawaban_benar"]
    kind = question.get("jenis_soal", "")
    if kind == "urutan_bilangan_bulat":
        match = re.search(r"Terdapat (\d+) bilangan.*lebih besar daripada (-?\d+)", question["pertanyaan"])
        if match and proof.get("check") == "exact_value_and_four_distinct_options":
            count,bound=map(int,match.groups())
            value=exact_value(proof["options"][index+1]);minimum=bound+count
            if value < minimum:
                return (f"Jika bilangan terbesarnya {wrong}, hanya ada {int(value-bound)} bilangan bulat "
                        f"yang lebih besar dari {bound} sampai nilai itu, belum cukup untuk {count} bilangan berbeda.")
            return (f"Pilihan {wrong} bukan nilai terkecil. Bilangan {bound+1} sampai {minimum} "
                    f"sudah menyediakan {count} bilangan berbeda dengan nilai terbesar lebih kecil, yaitu {answer}.")
    if kind == "jenis_data":
        if "kontinu" in wrong:
            return "Banyak saudara diperoleh dengan menghitung bilangan bulat, bukan mengukur nilai pada rentang kontinu."
        if "nominal" in wrong:
            return "Angka banyak saudara menyatakan jumlah, bukan sekadar nama atau kode kategori nominal."
        return "Data ini menyatakan jumlah saudara, bukan hanya urutan atau peringkat kategori ordinal."
    if kind == "ciri_segiempat":
        if "Semua" in wrong:
            return "Pada persegi panjang yang diberikan, panjang dan lebarnya berbeda. Hanya sisi yang berhadapan yang harus sama panjang."
        if "sejajar" in wrong:
            return "Persegi panjang mempunyai dua pasang sisi sejajar, sehingga pernyataan tepat satu pasang tidak benar."
        return "Keempat sudut persegi panjang adalah siku-siku, sehingga pernyataan bahwa bangun itu tidak memiliki sudut siku-siku salah."
    if kind.startswith("memilih_diagram") or kind == "evaluasi_pemilihan_diagram":
        if "lingkaran" in wrong:
            return "Diagram lingkaran menampilkan proporsi bagian terhadap keseluruhan; itu bukan hubungan atau perubahan yang diminta pada soal ini."
        if "pencar" in wrong:
            return "Diagram pencar digunakan untuk pasangan dua variabel numerik. Soal ini meminta perbandingan jumlah antarkategori."
        if "garis" in wrong or "Garis" in wrong:
            return "Menghubungkan data dengan garis memerlukan urutan yang bermakna. Itu tidak sesuai dengan tujuan penyajian data pada soal ini."
        return f"Pilihan {wrong} tidak menyajikan informasi utama yang diminta. Pilihan yang sesuai adalah {answer} karena {question['pembahasan']}"
    if proof.get("check") == "exact_value_and_four_distinct_options":
        correct=exact_value(proof["value"])
        value=exact_value(proof["options"][index+1])
        difference=s.simplify(value-correct)
        probability_kind=("peluang" in kind or kind in ("binomial_tepat_k","binomial_kumulatif",
                          "normal_peluang_tabel","normal_parameter_dan_peluang","fungsi_peluang_diskret",
                          "fungsi_densitas","variabel_kontinu_seragam")) and "harapan" not in kind
        if probability_kind and (value<0 or value>1):
            return f"Nilai {wrong} berada di luar rentang 0 sampai 1, sehingga tidak dapat menjadi peluang pada soal ini."
        if difference.is_positive:
            return (f"Pilihan {wrong} lebih besar sebesar {m(difference)} daripada hasil yang memenuhi "
                    f"perhitungan, yaitu {answer}. Periksa kembali langkah {kind.replace('_',' ')} pada pembahasan.")
        if difference.is_negative:
            return (f"Pilihan {wrong} lebih kecil sebesar {m(-difference)} daripada hasil yang memenuhi "
                    f"perhitungan, yaitu {answer}. Periksa kembali langkah {kind.replace('_',' ')} pada pembahasan.")
        return f"Pilihan {wrong} tidak sama dengan hasil {answer} yang diperoleh dari perhitungan pada pembahasan."
    return (f"Pernyataan atau koordinat {wrong} tidak sesuai hasil yang memenuhi data, yaitu {answer}. "
            f"Pemeriksaannya: {question['pembahasan']}")
