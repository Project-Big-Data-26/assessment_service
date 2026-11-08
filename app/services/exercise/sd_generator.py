"""Core question generator for SD Kelas 1, 2, 3, and 4.

Combines deterministic pedagogical templates with visual metadata,
SVG diagram generation, KaTeX formatting, and 9Router LLM capabilities.
"""

from __future__ import annotations

import json
import random
import uuid
from typing import Any, Dict, List, Optional, Tuple

from app.llm.ninerouter import NineRouterClient, NineRouterError, NineRouterSettings
from app.presentation.latex import normalize_document, normalize_text
from app.schemas.exercise import (
    ExerciseQuestion,
    LevelType,
    VisualMetadata,
    VisualType,
)


def _generate_svg(visual_type: VisualType, spec: Dict[str, Any]) -> str:
    """Generate clean inline SVG for the visual context."""
    if visual_type == "object_count":
        total = spec.get("total", 5)
        crossed = spec.get("crossed", 0)
        shape_kind = spec.get("shape", "apple")
        width, height = 480, 160
        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f'<rect width="{width}" height="{height}" fill="#f9fafb" rx="12" stroke="#e5e7eb" stroke-width="2"/>',
        ]
        items_per_row = 10
        for i in range(total):
            cx = 36 + (i % items_per_row) * 44
            cy = 50 + (i // items_per_row) * 55
            is_crossed = i >= (total - crossed)
            color = "#ef4444" if shape_kind == "apple" else "#3b82f6"
            # Draw circle/apple
            svg.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="{color}" opacity="0.9"/>')
            if shape_kind == "apple":
                svg.append(f'<path d="M {cx-1} {cy-18} Q {cx+4} {cy-24} {cx+7} {cy-18}" stroke="#15803d" stroke-width="3" fill="none"/>')
            if is_crossed:
                svg.append(f'<line x1="{cx-12}" y1="{cy-12}" x2="{cx+12}" y2="{cy+12}" stroke="#1f2937" stroke-width="3"/>')
                svg.append(f'<line x1="{cx+12}" y1="{cy-12}" x2="{cx-12}" y2="{cy+12}" stroke="#1f2937" stroke-width="3"/>')
        svg.append("</svg>")
        return "".join(svg)

    elif visual_type == "shape_pattern":
        pattern = spec.get("pattern", ["circle", "triangle", "circle", "triangle", "?"])
        width = max(380, len(pattern) * 65 + 40)
        height = 120
        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="10" stroke="#cbd5e1" stroke-width="2"/>',
        ]
        for idx, item in enumerate(pattern):
            cx = 40 + idx * 60
            cy = 60
            if item == "circle":
                svg.append(f'<circle cx="{cx}" cy="{cy}" r="18" fill="#60a5fa" stroke="#1d4ed8" stroke-width="2"/>')
            elif item == "triangle":
                svg.append(f'<polygon points="{cx},{cy-20} {cx-18},{cy+16} {cx+18},{cy+16}" fill="#facc15" stroke="#b45309" stroke-width="2"/>')
            elif item == "square":
                svg.append(f'<rect x="{cx-16}" y="{cy-16}" width="32" height="32" fill="#4ade80" stroke="#15803d" stroke-width="2"/>')
            elif item == "?":
                svg.append(f'<rect x="{cx-18}" y="{cy-18}" width="36" height="36" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4"/>')
                svg.append(f'<text x="{cx}" y="{cy+7}" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold" fill="#64748b">?</text>')
        svg.append("</svg>")
        return "".join(svg)

    elif visual_type == "fraction_pie":
        denominator = spec.get("denominator", 4)
        numerator = spec.get("numerator", 1)
        import math
        cx, cy, r = 100, 100, 75
        width, height = 200, 200
        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#1e293b" stroke-width="3"/>',
        ]
        angle_step = 2 * math.pi / denominator
        for i in range(denominator):
            start_ang = i * angle_step - math.pi / 2
            end_ang = (i + 1) * angle_step - math.pi / 2
            x1 = cx + r * math.cos(start_ang)
            y1 = cy + r * math.sin(start_ang)
            x2 = cx + r * math.cos(end_ang)
            y2 = cy + r * math.sin(end_ang)
            fill_color = "#38bdf8" if i < numerator else "#ffffff"
            path_d = f"M {cx} {cy} L {x1} {y1} A {r} {r} 0 0 1 {x2} {y2} Z"
            svg.append(f'<path d="{path_d}" fill="{fill_color}" stroke="#1e293b" stroke-width="2"/>')
        svg.append("</svg>")
        return "".join(svg)

    elif visual_type == "clock":
        hour = spec.get("hour", 8)
        minute = spec.get("minute", 0)
        import math
        cx, cy, r = 100, 100, 80
        width, height = 200, 200
        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#334155" stroke-width="4"/>',
            f'<circle cx="{cx}" cy="{cy}" r="4" fill="#0f172a"/>',
        ]
        # Hour marks
        for h in range(1, 13):
            ang = h * (math.pi / 6) - math.pi / 2
            tx = cx + (r - 18) * math.cos(ang)
            ty = cy + (r - 18) * math.sin(ang) + 5
            svg.append(f'<text x="{tx}" y="{ty}" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#334155">{h}</text>')
        # Minute hand
        min_ang = (minute / 60) * 2 * math.pi - math.pi / 2
        mx = cx + (r - 22) * math.cos(min_ang)
        my = cy + (r - 22) * math.sin(min_ang)
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{mx}" y2="{my}" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>')
        # Hour hand
        hr_ang = ((hour % 12) + minute / 60) * (math.pi / 6) - math.pi / 2
        hx = cx + (r - 38) * math.cos(hr_ang)
        hy = cy + (r - 38) * math.sin(hr_ang)
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{hx}" y2="{hy}" stroke="#dc2626" stroke-width="4" stroke-linecap="round"/>')
        svg.append("</svg>")
        return "".join(svg)

    elif visual_type == "bar_chart":
        categories = spec.get("categories", ["Apel", "Jeruk", "Pisang", "Mangga"])
        values = spec.get("values", [6, 4, 8, 5])
        width, height = 400, 220
        max_val = max(values) if values else 10
        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f'<rect width="{width}" height="{height}" fill="#fcfcfc" rx="8" stroke="#e2e8f0" stroke-width="1.5"/>',
            '<line x1="50" y1="170" x2="380" y2="170" stroke="#64748b" stroke-width="2"/>',
            '<line x1="50" y1="20" x2="50" y2="170" stroke="#64748b" stroke-width="2"/>',
        ]
        bar_colors = ["#f87171", "#fb923c", "#facc15", "#4ade80"]
        for idx, (cat, val) in enumerate(zip(categories, values)):
            x = 75 + idx * 75
            bar_h = int((val / max_val) * 130)
            y = 170 - bar_h
            color = bar_colors[idx % len(bar_colors)]
            svg.append(f'<rect x="{x}" y="{y}" width="42" height="{bar_h}" fill="{color}" rx="3"/>')
            svg.append(f'<text x="{x+21}" y="{y-6}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#334155">{val}</text>')
            svg.append(f'<text x="{x+21}" y="190" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#475569">{cat}</text>')
        svg.append("</svg>")
        return "".join(svg)

    elif visual_type == "geometry":
        shape = spec.get("shape", "rectangle")
        width, height = 360, 180
        p = spec.get("length", 8)
        l = spec.get("width", 5)
        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="8" stroke="#e2e8f0" stroke-width="1.5"/>',
        ]
        if shape == "rectangle":
            svg.append('<rect x="80" y="40" width="200" height="100" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>')
            svg.append(f'<text x="180" y="30" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0369a1">{p} cm</text>')
            svg.append(f'<text x="65" y="95" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0369a1">{l} cm</text>')
        elif shape == "square":
            svg.append('<rect x="110" y="30" width="120" height="120" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>')
            svg.append(f'<text x="170" y="22" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#a16207">{p} cm</text>')
        svg.append("</svg>")
        return "".join(svg)

    # Generic illustration placeholder
    width, height = 360, 120
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
        f'<rect width="{width}" height="{height}" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>'
        f'<text x="180" y="65" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#15803d">Gambar Soal Matematika</text>'
        f'</svg>'
    )


# ---------------------------------------------------------------------------
# Deterministic templates for SD Grades 1, 2, 3, 4
# ---------------------------------------------------------------------------

def _generate_sd1_question(idx: int, level: LevelType, r: random.Random) -> ExerciseQuestion:
    qid = f"sd1_k01_q{idx:03d}_{uuid.uuid4().hex[:6]}"
    category = r.choice(["counting_addition", "counting_subtraction", "shape_pattern", "comparison"])

    if category == "counting_addition":
        a = r.randint(2, 6)
        b = r.randint(2, 5)
        ans = a + b
        opts = [f"${ans}$", f"${ans+1}$", f"${max(1, ans-1)}$", f"${ans+2}$"]
        r.shuffle(opts)
        spec = {"total": a + b, "crossed": 0, "shape": "apple"}
        prompt = f"Ilustrasi {a} buah apel merah di piring kiri dan {b} buah apel merah di piring kanan, gaya kartun ramah anak SD kelas 1."
        return ExerciseQuestion(
            question_id=qid,
            grade=1,
            subject="matematika",
            bab=1,
            level=level,
            topic="Penjumlahan Bilangan 1-20",
            question_text=f"Perhatikan gambar apel berikut. Di piring ada ${a}$ apel merah, lalu ibu menambahkan lagi ${b}$ apel merah. Berapa jumlah apel seluruhnya? ${a} + {b} = \\dots$",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="object_count",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("object_count", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${ans}$",
            explanation=f"Jumlah apel mula-mula ada ${a}$ buah. Ditambah ${b}$ buah lagi. Maka ${a} + {b} = {ans}$. Jadi total apel adalah ${ans}$ buah.",
        )

    elif category == "counting_subtraction":
        total = r.randint(5, 10)
        taken = r.randint(1, total - 2)
        sisa = total - taken
        opts = [f"${sisa}$", f"${sisa+1}$", f"${max(1, sisa-1)}$", f"${sisa+2}$"]
        r.shuffle(opts)
        spec = {"total": total, "crossed": taken, "shape": "apple"}
        prompt = f"Ilustrasi {total} buah apel di meja dengan {taken} buah apel disilang tanda hitam karena sudah dimakan, gaya buku sekolah dasar."
        return ExerciseQuestion(
            question_id=qid,
            grade=1,
            subject="matematika",
            bab=1,
            level=level,
            topic="Pengurangan Bilangan 1-20",
            question_text=f"Ada ${total}$ buah apel di piring. Sebanyak ${taken}$ buah apel dimakan oleh adik. Berapa sisa buah apel di piring sekarang? ${total} - {taken} = \\dots$",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="object_count",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("object_count", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${sisa}$",
            explanation=f"Mula-mula ada ${total}$ buah apel. Karena dimakan ${taken}$, maka sisanya berkurang: ${total} - {taken} = {sisa}$. Sisa apel adalah ${sisa}$ buah.",
        )

    elif category == "shape_pattern":
        patterns = [
            (["circle", "triangle", "circle", "triangle", "?"], "circle", "Lingkaran"),
            (["square", "circle", "square", "circle", "?"], "square", "Persegi"),
            (["circle", "square", "triangle", "circle", "square", "?"], "triangle", "Segitiga"),
        ]
        seq, correct_shape, name = r.choice(patterns)
        spec = {"pattern": seq}
        prompt = f"Barisan pola bangun datar berwarna-warni yang berulang, bangun terakhir bertanda tanya (?), gaya gambar anak SD."
        opts = ["Lingkaran", "Segitiga", "Persegi", "Bintang"]
        return ExerciseQuestion(
            question_id=qid,
            grade=1,
            subject="matematika",
            bab=2,
            level=level,
            topic="Pola Bangun Datar Sederhana",
            question_text=f"Perhatikan barisan pola gambar bangun datar berikut. Bangun apakah yang tepat untuk menggantikan tanda tanya ($?$)?",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="shape_pattern",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("shape_pattern", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=name,
            explanation=f"Pola gambar berulang secara teratur. Sesuai urutan pola, bangun setelahnya adalah {name}.",
        )

    else:  # comparison
        a = r.randint(4, 9)
        b = a + r.randint(2, 5)
        diff = b - a
        opts = [f"${diff}$", f"${diff+1}$", f"${max(1, diff-1)}$", f"${diff+2}$"]
        r.shuffle(opts)
        spec = {"total": b, "crossed": 0, "shape": "circle"}
        prompt = f"Dua kelompok kelereng: Kotak A berisi {a} kelereng dan Kotak B berisi {b} kelereng, digambar jelas untuk dihitung anak."
        return ExerciseQuestion(
            question_id=qid,
            grade=1,
            subject="matematika",
            bab=1,
            level=level,
            topic="Perbandingan Kuantitas Objek",
            question_text=f"Kotak A berisi ${a}$ butir kelereng. Kotak B berisi ${b}$ butir kelereng. Berapa selisih banyak kelereng antara Kotak B dan Kotak A? ${b} - {a} = \\dots$",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="object_count",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("object_count", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${diff}$",
            explanation=f"Selisih kelereng diperoleh dengan mengurangkan jumlah yang lebih banyak dengan yang lebih sedikit: ${b} - {a} = {diff}$.",
        )


def _generate_sd2_question(idx: int, level: LevelType, r: random.Random) -> ExerciseQuestion:
    qid = f"sd2_k02_q{idx:03d}_{uuid.uuid4().hex[:6]}"
    category = r.choice(["repeated_addition", "analog_clock", "two_digit_add"])

    if category == "repeated_addition":
        groups = r.randint(3, 5)
        items_per_group = r.randint(2, 4)
        total = groups * items_per_group
        opts = [f"${total}$", f"${total+2}$", f"${max(2, total-2)}$", f"${total+groups}$"]
        r.shuffle(opts)
        spec = {"total": total, "crossed": 0, "shape": "apple"}
        prompt = f"Ilustrasi {groups} piring kue, masing-masing piring berisi {items_per_group} kue donat manis."
        return ExerciseQuestion(
            question_id=qid,
            grade=2,
            subject="matematika",
            bab=2,
            level=level,
            topic="Konsep Perkalian Dasar",
            question_text=f"Perhatikan gambar berikut. Ada ${groups}$ piring kue. Setiap piring berisi ${items_per_group}$ kue donat. Berapa banyak kue donat seluruhnya? ${groups} \\times {items_per_group} = \\dots$",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="object_count",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("object_count", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${total}$",
            explanation=f"Perkalian adalah penjumlahan berulang: ada ${groups}$ piring yang masing-masing berisi ${items_per_group}$ kue. Maka ${groups} \\times {items_per_group} = {total}$.",
        )

    elif category == "analog_clock":
        hour = r.randint(1, 11)
        minute = r.choice([0, 30])
        time_str = f"{hour:02d}.{minute:02d}"
        wrong1 = f"{(hour % 12) + 1:02d}.{minute:02d}"
        wrong2 = f"{hour:02d}.{(minute + 15) % 60:02d}"
        wrong3 = f"{max(1, hour - 1):02d}.{minute:02d}"
        opts = [f"Pukul ${time_str}$", f"Pukul ${wrong1}$", f"Pukul ${wrong2}$", f"Pukul ${wrong3}$"]
        r.shuffle(opts)
        spec = {"hour": hour, "minute": minute}
        prompt = f"Gambar jam dinding analog menunjukkan jarum pendek di angka {hour} dan jarum panjang di angka {12 if minute==0 else 6}."
        return ExerciseQuestion(
            question_id=qid,
            grade=2,
            subject="matematika",
            bab=3,
            level=level,
            topic="Membaca Waktu Jam Analog",
            question_text=f"Perhatikan gambar jam analog berikut. Jarum pendek menunjuk jam ${hour}$ dan jarum panjang menunjuk menit ${minute:02d}$. Waktu yang ditunjukkan oleh jam tersebut adalah ....",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="clock",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("clock", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"Pukul ${time_str}$",
            explanation=f"Jarum pendek menunjuk ke arah jam ${hour}$ dan jarum panjang menunjuk menit ${minute:02d}$. Maka waktu yang terbaca adalah pukul ${time_str}$.",
        )

    else:
        a = r.randint(20, 50)
        b = r.randint(15, 35)
        ans = a + b
        opts = [f"${ans}$", f"${ans+10}$", f"${ans-10}$", f"${ans+2}$"]
        r.shuffle(opts)
        spec = {"total": 12, "crossed": 0, "shape": "circle"}
        prompt = f"Ilustrasi kantong kelereng bertuliskan angka {a} dan kantong kelereng bertuliskan angka {b}."
        return ExerciseQuestion(
            question_id=qid,
            grade=2,
            subject="matematika",
            bab=1,
            level=level,
            topic="Penjumlahan Puluhan",
            question_text=f"Rani memiliki kelereng sebanyak ${a}$ butir di toples biru dan ${b}$ butir di toples merah. Berapa jumlah kelereng Rani seluruhnya? ${a} + {b} = \\dots$",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="illustration",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("object_count", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${ans}$",
            explanation=f"Jumlahkan puluhan dan satuan: ${a} + {b} = {ans}$. Jumlah seluruh kelereng adalah ${ans}$ butir.",
        )


def _generate_sd3_question(idx: int, level: LevelType, r: random.Random) -> ExerciseQuestion:
    qid = f"sd3_k03_q{idx:03d}_{uuid.uuid4().hex[:6]}"
    category = r.choice(["fraction_pie", "geometry_perimeter", "division_hundreds"])

    if category == "fraction_pie":
        denom = r.choice([3, 4, 6])
        num = r.randint(1, denom - 1)
        ans = f"$\\frac{{{num}}}{{{denom}}}$"
        wrong1 = f"$\\frac{{{denom-num}}}{{{denom}}}$"
        wrong2 = f"$\\frac{{{num}}}{{{denom+1}}}$"
        wrong3 = f"$\\frac{{{1}}}{{{denom}}}$" if num != 1 else f"$\\frac{{{2}}}{{{denom}}}$"
        opts = list({ans, wrong1, wrong2, wrong3})
        while len(opts) < 4:
            opts.append(f"$\\frac{{{len(opts)}}}{{{denom}}}$")
        r.shuffle(opts)
        spec = {"denominator": denom, "numerator": num}
        prompt = f"Diagram lingkaran pecahan dibagi menjadi {denom} potong sama besar, dengan {num} potong diberi warna biru muda arsir."
        return ExerciseQuestion(
            question_id=qid,
            grade=3,
            subject="matematika",
            bab=2,
            level=level,
            topic="Pengenalan Pecahan Sederhana",
            question_text=f"Perhatikan gambar pizza berbentuk lingkaran berikut. Pizza dipotong menjadi ${denom}$ bagian sama besar. Bagian yang diarsir warna biru bernilai ....",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="fraction_pie",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("fraction_pie", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=ans,
            explanation=f"Dari ${denom}$ bagian sama besar pada lingkaran, ada ${num}$ bagian yang diarsir. Bentuk pecahannya adalah $\\frac{{{num}}}{{{denom}}}$.",
        )

    elif category == "geometry_perimeter":
        p = r.randint(5, 12)
        l = r.randint(3, p - 1)
        keliling = 2 * (p + l)
        opts = [f"${keliling}\\text{{ cm}}$", f"${p * l}\\text{{ cm}}$", f"${p + l}\\text{{ cm}}$", f"${keliling + 4}\\text{{ cm}}$"]
        r.shuffle(opts)
        spec = {"shape": "rectangle", "length": p, "width": l}
        prompt = f"Gambar bangun datar persegi panjang dengan ukuran panjang {p} cm dan lebar {l} cm dengan label sisi yang jelas."
        return ExerciseQuestion(
            question_id=qid,
            grade=3,
            subject="matematika",
            bab=3,
            level=level,
            topic="Keliling Persegi Panjang",
            question_text=f"Perhatikan gambar persegi panjang berikut. Panjangnya ${p}\\text{{ cm}}$ dan lebarnya ${l}\\text{{ cm}}$. Keliling bangun tersebut adalah .... ($K = 2 \\times (p + l)$)",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="geometry",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("geometry", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${keliling}\\text{{ cm}}$",
            explanation=f"Rumus keliling persegi panjang adalah $K = 2 \\times (p + l)$. Maka $K = 2 \\times ({p} + {l}) = 2 \\times {p+l} = {keliling}\\text{{ cm}}$.",
        )

    else:
        divisor = r.randint(2, 6)
        ans = r.randint(20, 60)
        total = divisor * ans
        opts = [f"${ans}$", f"${ans+5}$", f"${max(5, ans-5)}$", f"${ans+10}$"]
        r.shuffle(opts)
        spec = {"total": 12, "crossed": 0, "shape": "circle"}
        prompt = f"Ilustrasi wadah berisi {total} kelereng yang akan dibagikan merata ke {divisor} kotak kecil."
        return ExerciseQuestion(
            question_id=qid,
            grade=3,
            subject="matematika",
            bab=1,
            level=level,
            topic="Pembagian Ratusan",
            question_text=f"Sebanyak ${total}$ permen dibagikan sama banyak kepada ${divisor}$ orang anak. Berapa banyak permen yang didapat setiap anak? ${total} \\div {divisor} = \\dots$",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="illustration",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("object_count", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${ans}$",
            explanation=f"Bagi total permen dengan banyak anak: ${total} \\div {divisor} = {ans}$. Setiap anak memperoleh ${ans}$ permen.",
        )


def _generate_sd4_question(idx: int, level: LevelType, r: random.Random) -> ExerciseQuestion:
    qid = f"sd4_k04_q{idx:03d}_{uuid.uuid4().hex[:6]}"
    category = r.choice(["bar_chart", "geometry_area", "equivalent_fractions"])

    if category == "bar_chart":
        cats = ["Apel", "Jeruk", "Pisang", "Mangga"]
        vals = [r.randint(4, 10) for _ in cats]
        max_idx = vals.index(max(vals))
        fav_fruit = cats[max_idx]
        opts = cats.copy()
        spec = {"categories": cats, "values": vals}
        prompt = f"Diagram batang vertikal berwarna-warni yang menunjukkan data buah favorit siswa di kelas 4 SD: {dict(zip(cats, vals))}."
        return ExerciseQuestion(
            question_id=qid,
            grade=4,
            subject="matematika",
            bab=4,
            level=level,
            topic="Membaca Diagram Batang",
            question_text=f"Perhatikan diagram batang data buah kesukaan siswa kelas $4$ berikut. Buah manakah yang paling banyak disukai siswa? (Frekuensi tertinggi = $\\dots$)",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="bar_chart",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("bar_chart", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=fav_fruit,
            explanation=f"Berdasarkan diagram batang, batang paling tinggi adalah buah {fav_fruit} dengan jumlah ${max(vals)}$ siswa. Jadi buah yang paling banyak disukai adalah {fav_fruit}.",
        )

    elif category == "geometry_area":
        s = r.randint(4, 12)
        luas = s * s
        opts = [f"${luas}\\text{{ cm}}^2$", f"${4 * s}\\text{{ cm}}^2$", f"${luas + 10}\\text{{ cm}}^2$", f"${s * (s-1)}\\text{{ cm}}^2$"]
        r.shuffle(opts)
        spec = {"shape": "square", "length": s, "width": s}
        prompt = f"Gambar persegi berukuran panjang sisi {s} cm dengan keterangan tanda sisi sama panjang pada setiap rusuknya."
        return ExerciseQuestion(
            question_id=qid,
            grade=4,
            subject="matematika",
            bab=3,
            level=level,
            topic="Luas Persegi",
            question_text=f"Perhatikan gambar persegi berikut. Panjang sisinya adalah ${s}\\text{{ cm}}$. Luas persegi tersebut adalah .... ($L = s \\times s$)",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="geometry",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("geometry", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=f"${luas}\\text{{ cm}}^2$",
            explanation=f"Rumus luas persegi adalah $L = s \\times s$. Maka $L = {s} \\times {s} = {luas}\\text{{ cm}}^2$.",
        )

    else:
        k = r.choice([2, 3, 4])
        orig_num, orig_den = 1, 2
        eq_num, eq_den = orig_num * k, orig_den * k
        ans = f"$\\frac{{{eq_num}}}{{{eq_den}}}$"
        wrong1 = f"$\\frac{{{eq_num+1}}}{{{eq_den}}}$"
        wrong2 = f"$\\frac{{{eq_num}}}{{{eq_den+1}}}$"
        wrong3 = f"$\\frac{{{eq_num-1}}}{{{eq_den}}}$"
        opts = list({ans, wrong1, wrong2, wrong3})
        while len(opts) < 4:
            opts.append(f"$\\frac{{{len(opts)}}}{{{eq_den}}}$")
        r.shuffle(opts)
        spec = {"denominator": eq_den, "numerator": eq_num}
        prompt = f"Dua diagram lingkaran bersisian yang menunjukkan kesamaan luas pecahan 1/2 dan {eq_num}/{eq_den}."
        return ExerciseQuestion(
            question_id=qid,
            grade=4,
            subject="matematika",
            bab=1,
            level=level,
            topic="Pecahan Senilai",
            question_text=f"Perhatikan kedua gambar diagram pecahan berikut. Pecahan yang senilai dengan $\\frac{{{orig_num}}}{{{orig_den}}}$ adalah ....",
            has_image=True,
            visual_metadata=VisualMetadata(
                image_type="fraction_pie",
                image_prompt=prompt,
                semantic_spec=spec,
                svg_content=_generate_svg("fraction_pie", spec),
            ),
            katex_enabled=True,
            options=opts,
            correct_answer=ans,
            explanation=f"Pecahan senilai diperoleh dengan mengalikan pembilang dan penyebut dengan angka yang sama: $\\frac{{{orig_num} \\times {k}}}{{{orig_den} \\times {k}}} = \\frac{{{eq_num}}}{{{eq_den}}}$.",
        )


def generate_deterministic_sd_questions(
    grade: int,
    count: int = 5,
    level: LevelType = "easy",
    seed: Optional[int] = None,
) -> List[ExerciseQuestion]:
    """Generate high-quality SD questions with guaranteed math correctness and KaTeX formatting."""
    r = random.Random(seed)
    generators = {
        1: _generate_sd1_question,
        2: _generate_sd2_question,
        3: _generate_sd3_question,
        4: _generate_sd4_question,
    }
    gen_func = generators.get(grade, _generate_sd1_question)
    questions: List[ExerciseQuestion] = []
    for i in range(1, count + 1):
        q = gen_func(i, level, r)
        # Normalize KaTeX strings to protect backslashes
        normalized = normalize_document(q.model_dump())
        questions.append(ExerciseQuestion.model_validate(normalized))
    return questions


# ---------------------------------------------------------------------------
# 9Router LLM Generation with Fallback
# ---------------------------------------------------------------------------

SYSTEM_PROMPT_9ROUTER_SD = """Kamu adalah pembuat soal latihan matematika untuk Sekolah Dasar (SD) Indonesia (Kelas 1, 2, 3, 4).
Aturan Wajib:
1. TARGET GRADE: Hanya buat soal sesuai tingkat kognitif dan materi jenjang SD yang diminta.
2. DOMINAN VISUAL: Setiap soal WAJIB berkonteks visual (bergambar).
   Sertakan visual_metadata dengan "image_type" dan "image_prompt" yang ramah anak secara detil.
3. FORMAT KATEX: Semua angka, hitungan, pecahan, dan operasi matematika WAJIB memakai format KaTeX inline $ ... $
   Contoh: "$5 + 2 = \\dots$", "$\\frac{1}{2}$", "$12 \\times 3 = 36$".
   Gunakan double backslash (\\\\) agar format JSON valid.
4. PILIHAN JAWABAN: Buat tepat 4 pilihan (A, B, C, D) yang jelas dengan tepat 1 jawaban benar.
5. BALASAN HANYA JSON: Balas HANYA satu objek JSON dengan format:
{
  "questions": [
    {
      "question_id": "string",
      "grade": int,
      "subject": "matematika",
      "topic": "string",
      "level": "easy|medium|hard",
      "question_text": "string (dengan KaTeX)",
      "has_image": true,
      "visual_metadata": {
        "image_type": "illustration|object_count|shape_pattern|fraction_pie|clock|bar_chart|geometry",
        "image_prompt": "string"
      },
      "katex_enabled": true,
      "options": ["string", "string", "string", "string"],
      "correct_answer": "string",
      "explanation": "string (dengan KaTeX)"
    }
  ]
}
"""


def generate_with_9router(
    grade: int,
    count: int = 5,
    level: LevelType = "easy",
    topic: Optional[str] = None,
) -> Tuple[List[ExerciseQuestion], Optional[str], str]:
    """Attempt 9Router generation, falling back cleanly to deterministic generator on failure."""
    try:
        settings = NineRouterSettings.from_environment()
        # Fast check: If key is placeholder/empty or base_url is unconfigured, avoid network timeout
        if (
            not settings.api_key
            or "replace" in settings.api_key.lower()
            or "dummy" in settings.api_key.lower()
            or "192.168.1.10" in settings.base_url
        ):
            questions = generate_deterministic_sd_questions(grade, count, level)
            return questions, settings.model, "deterministic_local (9Router configured with placeholder credentials)"
    except Exception as exc:
        # 9Router not configured; fall back to deterministic generator
        questions = generate_deterministic_sd_questions(grade, count, level)
        return questions, None, f"deterministic_local (9Router unconfigured: {exc})"

    prompt = (
        f"Buat {count} soal latihan matematika untuk SD Kelas {grade}, level {level}. "
        f"Topik: {topic or 'Matematika Dasar Bergambar'}. "
        f"Pastikan dominan bergambar dengan visual_metadata dan rumus menggunakan KaTeX $ ... $."
    )

    try:
        with NineRouterClient(settings) as client:
            resp = client.chat(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT_9ROUTER_SD},
                    {"role": "user", "content": prompt},
                ],
                json_mode=True,
            )
            raw_text = resp.text
            parsed = json.loads(raw_text)
            raw_questions = parsed.get("questions", [])
            questions: List[ExerciseQuestion] = []
            for item in raw_questions:
                # Normalize presentation and validate
                norm_item = normalize_document(item)
                # If SVG is missing in visual_metadata, generate a default one
                if norm_item.get("has_image") and norm_item.get("visual_metadata"):
                    vm = norm_item["visual_metadata"]
                    if not vm.get("svg_content"):
                        vm["svg_content"] = _generate_svg(vm.get("image_type", "illustration"), vm.get("semantic_spec") or {})
                q = ExerciseQuestion.model_validate(norm_item)
                questions.append(q)

            if len(questions) >= count:
                return questions[:count], settings.model, "ninerouter"
    except Exception as exc:
        # Fall back gracefully
        pass

    questions = generate_deterministic_sd_questions(grade, count, level)
    return questions, settings.model, "deterministic_fallback (9Router offline or response parsing)"
