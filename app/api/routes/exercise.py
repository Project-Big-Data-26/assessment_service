"""Exercise API Routes for Web Nolla (SD Kelas 1, 2, 3, and 4 Visual-First Question Generation)."""

from __future__ import annotations

import os
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException, status

from app.llm.ninerouter import NineRouterSettings
from app.presentation.latex import (
    POLICY_VERSION,
    math_spans,
    normalize_document,
    normalize_text,
    repair_math,
)
from app.schemas.exercise import (
    BatchGenerateRequest,
    BatchGenerateResponse,
    ExerciseGenerateRequest,
    ExerciseGenerateResponse,
    ExerciseQuestion,
    GradeInfo,
    GradeTopicInfo,
    KaTeXValidateRequest,
    KaTeXValidateResponse,
    KaTeXValidateResult,
    PreviewRequest,
    PreviewResponse,
    QuestionValidateRequest,
    QuestionValidateResponse,
    ServiceHealthResponse,
    VisualMetadata,
    VisualType,
    VisualTypeInfo,
)
from app.services.exercise.sd_generator import (
    _generate_svg,
    generate_deterministic_sd_questions,
    generate_with_9router,
)

router = APIRouter(prefix="/api/v1/exercise", tags=["exercise-sd-visual"])


# ============================================================================
# ROUTE 1: Generate Visual Questions (SD Kelas 1-4 via 9Router)
# ============================================================================
@router.post("/generate", response_model=ExerciseGenerateResponse)
def generate_questions(payload: ExerciseGenerateRequest) -> ExerciseGenerateResponse:
    """Generate visual-dominant exercise questions for SD grades 1, 2, 3, or 4 with KaTeX."""
    if payload.grade not in (1, 2, 3, 4):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Grade {payload.grade} is not supported. Supported grades are 1, 2, 3, 4.",
        )

    if payload.use_9router:
        questions, model_name, gen_source = generate_with_9router(
            grade=payload.grade,
            count=payload.count,
            level=payload.level,
            topic=payload.topic,
        )
    else:
        questions = generate_deterministic_sd_questions(
            grade=payload.grade,
            count=payload.count,
            level=payload.level,
        )
        model_name = None
        gen_source = "deterministic_local"

    # Enforce visual percent requirement
    visual_count = sum(1 for q in questions if q.has_image)
    visual_ratio = (visual_count / len(questions)) if questions else 0.0

    return ExerciseGenerateResponse(
        status="success",
        grade=payload.grade,
        subject="matematika",
        total_generated=len(questions),
        visual_count=visual_count,
        visual_ratio=round(visual_ratio, 2),
        router_model=model_name,
        generation_source=gen_source,
        questions=questions,
    )


# ============================================================================
# ROUTE 2: Batch Generate Across Levels
# ============================================================================
@router.post("/batch-generate", response_model=BatchGenerateResponse)
def batch_generate(payload: BatchGenerateRequest) -> BatchGenerateResponse:
    """Batch generate questions for a specific grade and chapter across multiple difficulty levels."""
    if payload.grade not in (1, 2, 3, 4):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Grade {payload.grade} is not supported.",
        )

    all_questions: List[ExerciseQuestion] = []
    counts_by_level: Dict[str, int] = {}

    for lvl, count in payload.counts_per_level.items():
        if count > 0:
            qs = generate_deterministic_sd_questions(grade=payload.grade, count=count, level=lvl)
            all_questions.extend(qs)
            counts_by_level[lvl] = len(qs)

    return BatchGenerateResponse(
        status="success",
        grade=payload.grade,
        bab=payload.bab,
        subbab=payload.subbab,
        total_questions=len(all_questions),
        counts_by_level=counts_by_level,
        questions=all_questions,
    )


# ============================================================================
# ROUTE 3: Grades Information & Curriculum
# ============================================================================
@router.get("/grades", response_model=List[GradeInfo])
def get_grades_info() -> List[GradeInfo]:
    """Retrieve supported SD grades (1-4) with cognitive levels and visual focus."""
    return [
        GradeInfo(
            grade=1,
            label="SD Kelas 1",
            age_range="6-7 tahun",
            cognitive_focus="Tahap operasional konkret awal: membilang, menghitung objek konkret, pola bentuk visual",
            topics=[
                GradeTopicInfo(
                    bab=1,
                    title="Bilangan dan Penjumlahan 1-20",
                    key_concepts=["Membilang objek", "Penjumlahan konkret", "Pengurangan konkret"],
                    typical_visuals=["Kumpulan buah apel/jeruk", "Kelereng dalam toples", "Balok hitung"],
                ),
                GradeTopicInfo(
                    bab=2,
                    title="Pola Gambar dan Bangun Datar",
                    key_concepts=["Lingkaran, segitiga, persegi", "Pola barisan berulang"],
                    typical_visuals=["Deret bentuk warna-warni", "Tanda tanya pada pola berikutnya"],
                ),
            ],
        ),
        GradeInfo(
            grade=2,
            label="SD Kelas 2",
            age_range="7-8 tahun",
            cognitive_focus="Operasi bilangan dua angka, konsep awal perkalian sebagai penjumlahan berulang, waktu",
            topics=[
                GradeTopicInfo(
                    bab=1,
                    title="Penjumlahan dan Pengurangan sampai 100",
                    key_concepts=["Nilai tempat puluhan dan satuan", "Soal cerita bergambar"],
                    typical_visuals=["Kantong kelereng dengan label puluhan", "Rak buku bergambar"],
                ),
                GradeTopicInfo(
                    bab=2,
                    title="Perkalian dan Pembagian Dasar",
                    key_concepts=["Kelompok benda sama banyak", "Penjumlahan berulang"],
                    typical_visuals=["Piring berisi kue donat", "Kandang berisi anak ayam"],
                ),
                GradeTopicInfo(
                    bab=3,
                    title="Pengukuran Waktu Jam Analog",
                    key_concepts=["Membaca jam tepat", "Membaca setengah jam"],
                    typical_visuals=["Jam dinding analog dengan jarum jam dan menit"],
                ),
            ],
        ),
        GradeInfo(
            grade=3,
            label="SD Kelas 3",
            age_range="8-9 tahun",
            cognitive_focus="Pecahan sederhana berarsir, keliling bangun datar, operasi hitung ratusan",
            topics=[
                GradeTopicInfo(
                    bab=1,
                    title="Operasi Perkalian dan Pembagian Ratusan",
                    key_concepts=["Pembagian rata", "Kelipatan"],
                    typical_visuals=["Pembagian kotak permen", "Diagram sebaran barang"],
                ),
                GradeTopicInfo(
                    bab=2,
                    title="Pecahan Sederhana",
                    key_concepts=["Konsep 1/2, 1/3, 1/4", "Bagian dari keseluruhan"],
                    typical_visuals=["Pizza atau lingkaran berarsir", "Balok pecahan terbagi rata"],
                ),
                GradeTopicInfo(
                    bab=3,
                    title="Keliling Bangun Datar",
                    key_concepts=["Keliling persegi", "Keliling persegi panjang"],
                    typical_visuals=["Persegi panjang berlabel cm", "Segitiga berlabel panjang sisi"],
                ),
            ],
        ),
        GradeInfo(
            grade=4,
            label="SD Kelas 4",
            age_range="9-10 tahun",
            cognitive_focus="Pecahan senilai, luas bangun datar, diagram batang dan pengolahan data sederhana",
            topics=[
                GradeTopicInfo(
                    bab=1,
                    title="Pecahan Senilai dan Operasi Pecahan",
                    key_concepts=["Pecahan senilai", "Perbandingan pecahan"],
                    typical_visuals=["Dua diagram lingkaran bersisian untuk perbandingan"],
                ),
                GradeTopicInfo(
                    bab=2,
                    title="Luas dan Keliling Bangun Datar",
                    key_concepts=["Luas persegi (s x s)", "Luas persegi panjang (p x l)"],
                    typical_visuals=["Petak grid ubin satuan", "Gambar persegi berlabel ukuran"],
                ),
                GradeTopicInfo(
                    bab=3,
                    title="Penyajian Data (Diagram Batang)",
                    key_concepts=["Membaca diagram batang", "Data tertinggi dan terendah"],
                    typical_visuals=["Diagram batang vertikal dengan sumbu frekuensi dan kategori"],
                ),
            ],
        ),
    ]


# ============================================================================
# ROUTE 4: Catalog of Visual Types
# ============================================================================
@router.get("/visual-types", response_model=List[VisualTypeInfo])
def get_visual_types() -> List[VisualTypeInfo]:
    """Catalog of supported visual types for SD question generation."""
    return [
        VisualTypeInfo(
            type_name="object_count",
            display_name="Hitung Objek Konkret",
            description="Kumpulan objek visual (apel, bola, buah) dengan opsi tanda silang untuk pengurangan.",
            applicable_grades=[1, 2],
            sample_semantic_spec={"total": 8, "crossed": 3, "shape": "apple"},
            sample_prompt="Ilustrasi 8 buah apel merah di atas meja dengan 3 apel disilang.",
        ),
        VisualTypeInfo(
            type_name="shape_pattern",
            display_name="Pola Bangun Datar",
            description="Barisan pola bentuk geometri berulang yang diakhiri tanda tanya (?) untuk ditebak.",
            applicable_grades=[1, 2],
            sample_semantic_spec={"pattern": ["circle", "square", "circle", "square", "?"]},
            sample_prompt="Barisan bentuk lingkaran dan persegi berulang secara teratur.",
        ),
        VisualTypeInfo(
            type_name="fraction_pie",
            display_name="Diagram Pecahan Lingkaran",
            description="Diagram lingkaran atau pizza yang dibagi n bagian dengan m bagian berarsir.",
            applicable_grades=[3, 4],
            sample_semantic_spec={"denominator": 4, "numerator": 1},
            sample_prompt="Lingkaran dibagi 4 bagian sama besar dengan 1 bagian diarsir biru muda.",
        ),
        VisualTypeInfo(
            type_name="clock",
            display_name="Jam Analog",
            description="Muka jam dinding dengan jarum pendek dan panjang untuk latihan membaca waktu.",
            applicable_grades=[2, 3],
            sample_semantic_spec={"hour": 8, "minute": 30},
            sample_prompt="Jam dinding analog dengan jarum pendek menunjuk antara 8 dan 9, jarum panjang di angka 6.",
        ),
        VisualTypeInfo(
            type_name="bar_chart",
            display_name="Diagram Batang",
            description="Grafik diagram batang sederhana untuk latihan membaca data kategori.",
            applicable_grades=[3, 4],
            sample_semantic_spec={"categories": ["Apel", "Jeruk", "Pisang"], "values": [5, 8, 4]},
            sample_prompt="Diagram batang warna-warni tentang buah favorit siswa.",
        ),
        VisualTypeInfo(
            type_name="geometry",
            display_name="Bangun Datar Berdimensi",
            description="Persegi atau persegi panjang berlabel panjang dan lebar.",
            applicable_grades=[3, 4],
            sample_semantic_spec={"shape": "rectangle", "length": 10, "width": 6},
            sample_prompt="Persegi panjang berukuran 10 cm x 6 cm dengan label sisi.",
        ),
        VisualTypeInfo(
            type_name="illustration",
            display_name="Ilustrasi Cerita Umum",
            description="Ilustrasi kontekstual bergambar untuk soal cerita matematika anak SD.",
            applicable_grades=[1, 2, 3, 4],
            sample_semantic_spec={"context": "market", "items": "books"},
            sample_prompt="Ilustrasi anak SD sedang membawa buku cerita di perpustakaan.",
        ),
    ]


# ============================================================================
# ROUTE 5: KaTeX Syntax & Escaping Validation
# ============================================================================
@router.post("/validate-katex", response_model=KaTeXValidateResponse)
def validate_katex(payload: KaTeXValidateRequest) -> KaTeXValidateResponse:
    """Validate and normalize mathematical KaTeX expressions and check JSON escaping."""
    results: List[KaTeXValidateResult] = []
    all_valid = True

    for text in payload.texts:
        issues: List[str] = []
        normalized = normalize_text(text)
        spans = math_spans(text)
        has_katex = len(spans) > 0 or "$" in text

        # Check for unescaped broken control characters
        for broken_pattern in [r"\x0crac", r"\x08egin", r"\x0bert"]:
            if broken_pattern in text:
                issues.append(f"Contains corrupted escaped control byte: {broken_pattern}")

        # Check for unclosed math delimiters
        single_dollar_count = text.count("$") - (text.count("$$") * 2)
        if single_dollar_count % 2 != 0:
            issues.append(f"Odd number of single dollar signs (${single_dollar_count}), delimiter may be unclosed")

        is_valid = len(issues) == 0
        if not is_valid:
            all_valid = False

        results.append(
            KaTeXValidateResult(
                original=text,
                normalized=normalized,
                has_katex=has_katex,
                is_valid=is_valid,
                issues=issues,
            )
        )

    return KaTeXValidateResponse(
        status="success",
        total_checked=len(results),
        all_valid=all_valid,
        results=results,
    )


# ============================================================================
# ROUTE 6: Question Validation Layer
# ============================================================================
@router.post("/validate-question", response_model=QuestionValidateResponse)
def validate_question(payload: QuestionValidateRequest) -> QuestionValidateResponse:
    """Validate a question against Web Nolla backend specifications."""
    q = payload.question
    checks: Dict[str, bool] = {}
    warnings: List[str] = []
    errors: List[str] = []

    # Check 1: Grade validity
    checks["valid_grade"] = q.grade in (1, 2, 3, 4)
    if not checks["valid_grade"]:
        errors.append("Grade must be 1, 2, 3, or 4 for SD level.")

    # Check 2: Visual metadata requirement
    if q.has_image:
        has_vm = q.visual_metadata is not None
        checks["visual_metadata_present"] = has_vm
        if not has_vm:
            errors.append("Question has has_image=True but visual_metadata is missing.")
        else:
            checks["image_prompt_valid"] = len(q.visual_metadata.image_prompt) >= 10
            if not checks["image_prompt_valid"]:
                warnings.append("image_prompt in visual_metadata is very short (<10 characters).")
    else:
        checks["visual_metadata_present"] = True

    # Check 3: KaTeX syntax presence
    has_math = "$" in q.question_text or any("$" in opt for opt in q.options)
    checks["katex_present"] = has_math
    if not has_math and q.katex_enabled:
        warnings.append("katex_enabled is true but question contains no dollar delimiters.")

    # Check 4: Options count and uniqueness
    checks["options_count_valid"] = len(q.options) == 4
    if not checks["options_count_valid"]:
        warnings.append(f"Recommended number of options is 4; found {len(q.options)}.")

    checks["options_unique"] = len(set(q.options)) == len(q.options)
    if not checks["options_unique"]:
        errors.append("Options contain duplicates.")

    # Check 5: Correct answer matches an option or valid letter
    letter_opts = {"A", "B", "C", "D"}
    ans_matches = q.correct_answer in q.options or (q.correct_answer in letter_opts)
    checks["correct_answer_matches"] = ans_matches
    if not ans_matches:
        errors.append("correct_answer does not match any of the provided options.")

    valid = len(errors) == 0

    return QuestionValidateResponse(
        valid=valid,
        question_id=q.question_id,
        has_image=q.has_image,
        katex_enabled=q.katex_enabled,
        checks=checks,
        warnings=warnings,
        errors=errors,
    )


# ============================================================================
# ROUTE 7: Catalog of Sample Questions by Grade
# ============================================================================
@router.get("/catalog/{grade}", response_model=List[ExerciseQuestion])
def get_catalog_by_grade(grade: int) -> List[ExerciseQuestion]:
    """Retrieve verified sample visual questions for a specific grade (1-4)."""
    if grade not in (1, 2, 3, 4):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Grade must be 1, 2, 3, or 4.",
        )
    return generate_deterministic_sd_questions(grade=grade, count=4, level="easy", seed=42 + grade)


# ============================================================================
# ROUTE 8: Instant Preview Generator (SVG + KaTeX HTML)
# ============================================================================
@router.post("/preview", response_model=PreviewResponse)
def preview_exercise(payload: PreviewRequest) -> PreviewResponse:
    """Generate an immediate visual question preview with rendered SVG and KaTeX-ready HTML."""
    qs = generate_deterministic_sd_questions(grade=payload.grade, count=1, level="easy")
    q = qs[0]

    # Render specific SVG if requested visual type
    spec = q.visual_metadata.semantic_spec if q.visual_metadata else {}
    svg = _generate_svg(payload.visual_type, spec or {"shape": "apple", "total": 5, "crossed": 2})

    html = f"""
    <div class="web-nolla-exercise-card" data-grade="{q.grade}" data-id="{q.question_id}">
      <div class="visual-container mb-4">{svg}</div>
      <p class="question-stem text-lg font-medium">{q.question_text}</p>
      <div class="options-grid grid grid-cols-2 gap-2 mt-4">
        {"".join(f'<button class="option-pill border p-3 rounded">{opt}</button>' for opt in q.options)}
      </div>
      <div class="explanation-box bg-blue-50 p-3 mt-4 rounded text-sm text-blue-900">
        <strong>Pembahasan:</strong> {q.explanation}
      </div>
    </div>
    """

    return PreviewResponse(
        question=q,
        rendered_svg=svg,
        html_preview=html.strip(),
    )


# ============================================================================
# ROUTE 9: Service Health & 9Router Connectivity
# ============================================================================
@router.get("/health", response_model=ServiceHealthResponse)
def get_exercise_health() -> ServiceHealthResponse:
    """Check readiness of the exercise service, KaTeX policy, and 9Router connection status."""
    router_configured = False
    router_base_url = None
    router_model = None

    try:
        settings = NineRouterSettings.from_environment()
        router_configured = True
        router_base_url = settings.base_url
        router_model = settings.model
    except Exception:
        router_configured = False

    return ServiceHealthResponse(
        status="ready",
        service="nolla-sd-visual-exercise-generator",
        target_grades=[1, 2, 3, 4],
        ninerouter_configured=router_configured,
        ninerouter_base_url=router_base_url,
        ninerouter_model=router_model,
        latex_policy_version=POLICY_VERSION,
    )
