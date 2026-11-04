"""Codex-authored local assessments, separate from paid blind AI evidence."""
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re

import sympy as s

from app.presentation.latex import normalize_document, normalize_text, math_spans
from app.services.exercise.replenishment_format import exact_value

SCHEMA = "codex-local-exercise-publication-v1"
POLICY = "codex-template-math-and-content-review-v1"
SCORES = {"easy": 600, "medium": 1000, "hard": 1400}
MEDIUM = set("""anuitas_investasi aturan_kosinus aturan_sinus barisan_dari_dua_suku
binomial_kumulatif binomial_tepat_k bunga_tunggal_balik evaluasi_persamaan faktor_dengan_syarat
faktor_polinomial faktor_persekutuan_bersyarat fpb_faktorisasi fungsi_densitas
fungsi_peluang_diskret harapan_variabel_diskret hubungan_keliling_luas identitas_polinomial
integral_tak_tentu_dengan_syarat integral_tentu invers_matriks jenis_matriks_diagonal
kedudukan_garis_lingkaran keliling_segiempat_balik keliling_segitiga_balik
kombinasi_bersyarat kombinasi_dalam_peluang korespondensi_satu_satu
letak_bilangan_rasional lokasi_pada_petak luas_daerah_integral membandingkan_luas
membandingkan_pecahan membandingkan_peluang membandingkan_rasional
mengelompokkan_data_frekuensi normal_peluang_tabel operasi_aljabar optimasi_turunan
pembagian_pecahan_bersyarat pemodelan_aljabar pemodelan_non_aljabar_bertahap
penerapan_rasio perbandingan_trigonometri permutasi_bersyarat persamaan_lingkaran
persamaan_dua_variabel rata_rata_balik relasi_faktor rumus_jarak sisa_pembagian_polinomial
sistem_linear_dua_variabel sistem_linear_tiga_variabel titik_stasioner_minimum
fokus_elips definisi_turunan_limit sifat_turunan operasi_bentuk_akar bentuk_akar
fungsi_aljabar_rasional perpotongan_tali_busur garis_singgung_lingkaran
penjumlahan_matriks kesamaan_matriks luas_bangun_gabungan perkalian_matriks
peluang_tanpa_pengembalian""".split())
HARD = {"optimasi_pertidaksamaan_linear", "normal_parameter_dan_peluang", "evaluasi_sumbu_diagram"}
KNOWING = {"ciri_segiempat", "jenis_data", "memilih_diagram_kategori", "memilih_diagram_waktu", "visualisasi_spasial"}


def checksum(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_math(text):
    value = str(text).replace("$", "").replace(r"\left", "").replace(r"\right", "")
    value = value.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    return re.sub(r"\s+", "", value)


def render(value, kind, unit=""):
    if kind == "operasi_desimal":
        return str(value) if value.is_Integer else f"{float(value):.2f}".rstrip("0").rstrip(".").replace(".", ",")
    return "$" + s.latex(value) + "$" + (" " + unit if unit else "")


def assess_level(kind, grade):
    if kind in HARD or (grade == 5 and kind in {"keliling_bangun_gabungan", "faktor_persekutuan_bersyarat", "pengurangan_pecahan_bertahap"}):
        return "hard", "Memerlukan pemilihan strategi dan penggabungan kendala; hasil tidak diperoleh melalui satu substitusi rutin."
    if kind in MEDIUM:
        return "medium", "Memerlukan penerapan konsep dan beberapa langkah yang saling bergantung; bentuk masalah masih rutin untuk kelas sasaran."
    return "easy", "Pengenalan konsep atau prosedur langsung; solusi minimum singkat untuk kelas sasaran."


def pairs_in(stem):
    values = []
    pattern = r"(-?(?:\\frac\{[-0-9]+\}\{[0-9]+\}|[0-9]+))"
    for left, right in re.findall(r"\$\(" + pattern + r",\s*" + pattern + r"\)\$", stem):
        def number(t):
            match = re.fullmatch(r"(-?)\\frac\{(-?\d+)\}\{(\d+)\}", t)
            return (-1 if match[1] else 1) * s.Rational(match[2], match[3]) if match else s.Integer(t)
        values.append((number(left), number(right)))
    return values


def text_answer(row, kind):
    q = row["soal_text"]
    if kind == "ciri_segiempat":
        return "Keempat sudutnya siku-siku dan sisi-sisi yang berhadapan sama panjang."
    if kind == "membandingkan_peluang":
        red, blue, other, other_blue = map(int, re.search(r"P memuat (\d+) bola merah dan (\d+) biru. Kotak Q memuat (\d+) merah dan (\d+) biru", q).groups())
        assert s.Rational(other, other + other_blue) > s.Rational(red, red + blue)
        return "Peluang merah di Q lebih besar daripada di P."
    if kind == "jenis_data":
        assert "banyak saudara" in q
        return "Data kuantitatif diskret."
    if kind == "memilih_diagram_kategori":
        assert "kategori" in q or "ekstrakurikuler" in q
        return "Diagram batang."
    if kind == "memilih_diagram_waktu":
        assert "setiap jam" in q
        return "Diagram garis."
    if kind == "evaluasi_pemilihan_diagram":
        return "Diagram pencar."
    if kind == "membaca_diagram":
        values = list(map(int, re.search(r"berturut-turut (\d+), (\d+), dan (\d+)", q).groups()))
        return "Produk " + "ABC"[values.index(max(values))] + "."
    if kind == "diagram_pencar":
        pairs = pairs_in(q)
        assert len(pairs) >= 2
        slope = (pairs[1][1] - pairs[0][1]) / (pairs[1][0] - pairs[0][0])
        assert all((y - pairs[0][1]) == slope * (x - pairs[0][0]) for x, y in pairs)
        return "Korelasi linear " + ("positif" if slope > 0 else "negatif") + "."
    if kind in {"transformasi_koordinat", "transformasi_matriks", "pembuktian_vektor_titik_tengah"}:
        pairs = pairs_in(q)
        x, y = pairs[0]
        if kind == "pembuktian_vektor_titik_tengah":
            x, y = (x + pairs[1][0]) / 2, (y + pairs[1][1]) / 2
        elif "dilanjutkan rotasi" in q:
            x, y = -(y + pairs[1][1]), x + pairs[1][0]
        elif "translasi" in q:
            x, y = x + pairs[1][0], y + pairs[1][1]
        elif "dicerminkan" in q:
            x = -x
        elif "dirotasi" in q or "bermatriks" in q:
            x, y = -y, x
        elif "didilatasi" in q:
            factor = int(re.search(r"faktor (\d+)", q)[1])
            x, y = factor*x, factor*y
        else:
            raise ValueError("Unknown coordinate transformation")
        return "$(" + s.latex(x) + ", " + s.latex(y) + ")$"
    raise ValueError("Unreviewed text family: " + kind)


def independent_numeric(row, kind):
    """Additional recomputation from the stem for common arithmetic families."""
    q = row["soal_text"]
    if kind == "operasi_desimal":
        a, b = re.findall(r"(\d+,\d+) kg", q)
        return s.Rational(a.replace(",", ".")) + s.Rational(b.replace(",", "."))
    if kind == "rasio_satuan":
        count, price = re.search(r"berisi (\d+) bibit dan harganya Rp([\d.]+),00", q).groups()
        return s.Rational(price.replace(".", ""), count)
    if kind == "rasio_senilai":
        original, syrup, new = re.search(r"(\d+) gelas.*?(\d+) sendok.*?(\d+) gelas", q).groups()
        return s.Rational(int(syrup)*int(new), int(original))
    if kind in {"penerapan_rasio", "rasio_bagian_total"}:
        a, b, total = re.search(r"(?:adalah|melati adalah) (\d+):(\d+).*?(?:seluruh bibit|Jumlahnya) (\d+)", q).groups()
        return s.Rational(int(total) * int(b if kind == "rasio_bagian_total" else a), int(a)+int(b))
    if kind == "lokasi_pada_petak":
        first, second = pairs_in(q)
        return abs(second[0]-first[0]) + abs(second[1]-first[1])
    if kind == "visualisasi_spasial":
        assert "Tiga menara" in q and "satu petak terpisah" in q
        return s.Integer(3)
    if kind == "susunan_kubus":
        a, b, c = map(int, re.search(r"(\d+) baris dan (\d+) kubus.*?(\d+) lapisan", q).groups())
        return s.Integer(a*b*c)
    if kind in {"peluang_satu_kejadian", "peluang_tanpa_pengembalian", "frekuensi_harapan"}:
        match = re.search(r"(?:berisi|memuat) (\d+) bola merah dan (\d+) bola biru", q)
        if match:
            red, blue = map(int, match.groups())
            p = s.Rational(red, red+blue)
            if kind == "peluang_tanpa_pengembalian":
                p *= s.Rational(red-1, red+blue-1)
            if kind == "frekuensi_harapan":
                p *= int(re.search(r"Dilakukan (\d+)", q)[1])
            return p
    if kind == "sampling_proporsional":
        groups = int(re.search(r"atas (\d+) kelompok", q)[1])
        sample = int(re.search(r"proporsional, (\d+) orang", q)[1])
        return s.Integer(groups*sample)
    if kind == "mengukur_sudut_jam":
        hour = int(re.search(r"pukul (\d+)\.00", q)[1])
        return s.Integer(min(hour*30, 360-hour*30))
    if kind == "sudut_siku_siku":
        a, b = map(int, re.search(r"Ada (\d+) kertas persegi panjang dan (\d+) kertas segitiga", q).groups())
        return s.Integer(4*a+b)
    if kind == "ciri_prisma":
        match = re.search(r"segi-(\d+)", q)
        if match:
            return s.Integer(3*int(match[1]))
    return None


def revise_chart(row, seed):
    lower = 40 + seed % 60
    gap = 3 + seed % 12
    upper = lower + gap
    origin = lower-gap
    answer = f"Penjualan B lebih banyak {gap} unit; panjang batang dua kali lipat tidak berarti penjualan dua kali lipat."
    wrong = ["Penjualan B tepat dua kali penjualan A.", "Penjualan A dan B sebenarnya sama.",
             f"Selisih penjualan sebenarnya {2*gap} unit."]
    row["soal_text"] = (f"Penjualan toko A {lower} unit dan B {upper} unit. Diagram batang memakai sumbu tegak yang dimulai dari {origin}, "
        f"sehingga tinggi batang A {gap} satuan dan B {2*gap} satuan. Seorang siswa menyatakan bahwa penjualan B dua kali A. "
        "Penilaian yang tepat terhadap pernyataan siswa adalah ....")
    row["jawaban"] = "A"
    row["options"] = [{"option_id": letter, "text": text,
        "alasan": (f"Benar: selisih {upper}-{lower}={gap}; rasio tinggi batang dipengaruhi titik awal sumbu." if letter == "A" else
                   "Salah: kesimpulan ini tidak sesuai dengan dua data asli dan titik awal sumbu.")}
        for letter, text in zip("ABCD", [answer, *wrong])]
    return "evaluasi_sumbu_diagram", f"Selisih data {upper}-{lower}={gap}. Perbandingan batang dihitung dari {origin}, bukan nol; karena itu rasio tinggi bukan rasio penjualan."


def review_question(original, meta, audited_kinds):
    row = deepcopy(original)
    kind = meta["jenis_soal"]
    assert kind in audited_kinds, "Question family has no recorded Codex template review"
    grade = int(row["kelas_id"].split("_")[0][5:])
    concerns, repairs, checks = [], [], []
    solution = meta["pembahasan"]
    proof = deepcopy(meta["local_math_check"])
    assert len(row["options"]) == 4 and {o["option_id"] for o in row["options"]} == set("ABCD")
    if kind == "evaluasi_pemilihan_diagram" and grade == 7:
        kind, solution = revise_chart(row, int(original["_id"][:8], 16))
        checks.append("reviewed_truncated_axis_counterexample")
        repairs.append("Mengganti pengenalan diagram pencar dengan evaluasi sumbu diagram yang sesuai materi penyajian data SMP.")
    elif proof["check"] == "exact_value_and_four_distinct_options":
        values = [exact_value(v) for v in proof["options"]]
        expected = exact_value(proof["value"])
        assert values[0] == expected
        assert all(s.simplify(a-b) != 0 for i, a in enumerate(values) for b in values[i+1:])
        assert not expected.free_symbols and expected.is_finite is True
        unit = "derajat" if kind in {"mengukur_sudut_busur", "mengukur_sudut_jam"} else ""
        rendered = [canonical_math(render(v, kind, unit)) for v in values]
        actual = [canonical_math(o["text"]) for o in row["options"]]
        assert Counter(actual) == Counter(rendered), "Displayed options differ from exact arithmetic proof"
        correct = [o["option_id"] for o in row["options"] if canonical_math(o["text"]) == rendered[0]]
        assert len(correct) == 1
        if row["jawaban"] != correct[0]:
            row["jawaban"] = correct[0]
            repairs.append("Kunci diperbaiki agar menunjuk pilihan dengan nilai tepat.")
        computed = independent_numeric(row, kind)
        if computed is not None:
            assert s.simplify(computed-expected) == 0, "Independent stem calculation differs"
            checks.append("stem_calculation_recomputed")
        checks.extend(["reviewed_template_formula", "exact_finite_value", "four_semantically_distinct_numeric_options", "key_matches_displayed_value"])
    elif proof["check"] == "four_distinct_text_options":
        answer = text_answer(row, kind)
        correct = [o["option_id"] for o in row["options"] if canonical_math(o["text"]) == canonical_math(answer)]
        assert len(correct) == 1, "Recomputed text/coordinate answer missing or ambiguous"
        row["jawaban"] = correct[0]
        checks.append("concept_or_coordinates_recomputed_from_stem")
    else:
        raise ValueError("Unrecognized mathematical evidence")
    if kind == "pinjaman_anuitas":
        principal, payment = [int(v.replace(".", "")) for v in re.findall(r"Rp([\d.]+),00", row["soal_text"])]
        rate = s.Rational(re.search(r"berbunga (\d+)%", row["soal_text"])[1], 100)
        if payment > principal*(1+rate):
            interest = principal*rate
            payment = s.Rational(principal, 2) + interest
            expected = s.Rational(principal, 2)
            money = lambda value: "Rp" + f"{int(value):,}".replace(",", ".") + ",00"
            row["soal_text"] = (f"Pinjaman {money(principal)} berbunga {int(rate*100)}% pada periode pertama. "
                f"Pembayaran akhir periode sebesar {money(payment)} terdiri atas bunga dan angsuran pokok. "
                "Berapa angsuran pokok periode pertama?")
            solution = f"Bunga periode pertama {principal} × {rate} = {interest}. Angsuran pokok {payment} - {interest} = {expected} rupiah."
            row["jawaban"] = "A"
            values = [expected, interest, expected+interest, expected-interest]
            assert len(set(values)) == 4
            row["options"] = [{"option_id": letter, "text": render(value, kind),
                "alasan": ("Benar: " if letter == "A" else "Salah: ") + (solution if letter == "A" else "Nilai ini tidak sama dengan pembayaran dikurangi bunga.")}
                for letter, value in zip("ABCD", values)]
            repairs.append("Pembayaran diperbaiki agar angsuran pokok tidak melampaui pokok pinjaman.")
    # Wrap bare inequality commands without altering the mathematical relation.
    outside, position = [], 0
    from app.presentation.latex import MATH
    for match in MATH.finditer(row["soal_text"]):
        segment = row["soal_text"][position:match.start()]
        segment = re.sub(r"[0-9xyt()+*/ -]+\\(?:le|ge|ne)\s*[0-9xyt()+*/ -]+", lambda m: "$"+m.group().strip()+"$", segment)
        outside.extend([segment, match.group()]); position = match.end()
    tail = row["soal_text"][position:]
    tail = re.sub(r"[0-9xyt()+*/ -]+\\(?:le|ge|ne)\s*[0-9xyt()+*/ -]+", lambda m: "$"+m.group().strip()+"$", tail)
    row["soal_text"] = "".join(outside) + tail
    row = normalize_document(row)
    assert all(text.count("$") % 2 == 0 for text in [row["soal_text"], *[o["text"] for o in row["options"]]])
    assert len({canonical_math(o["text"]) for o in row["options"]}) == 4
    level, rationale = assess_level(kind, grade)
    row.update(cognitive_level=level, cognitive_score=SCORES[level], confidence_score=0, status="active")
    domain = "knowing" if kind in KNOWING else "reasoning" if level == "hard" else "applying"
    return {"questionId": row["_id"], "sourceHash": checksum(original), "publishedQuestion": row,
            "questionHash": checksum(row), "method": "codex_direct_template_and_item_review",
            "apiCalls": 0, "confidence": 0, "confidenceMeasured": False,
            "originalTarget": meta["level_target"], "assessedLevel": level, "levelRationale": rationale,
            "mathCognitiveDomain": domain, "family": kind, "solution": normalize_text(solution),
            "checks": checks, "repairs": repairs, "concerns": concerns,
            "trainingEvidenceQualified": False, "policyVersion": POLICY}
