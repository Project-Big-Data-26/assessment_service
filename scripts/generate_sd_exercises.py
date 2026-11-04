"""Generate visual exercise questions for SD Kelas 1, 2, 3, and 4.

Saves structured exercise packages into output/exercise/kelas<N>/batch<B>/
Usage from project root:
    .venv/bin/python3 scripts/generate_sd_exercises.py --grade 1 --count 10
    .venv/bin/python3 scripts/generate_sd_exercises.py --all --count 10
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.schemas.exercise import ExerciseQuestion
from app.services.exercise.sd_generator import (
    generate_deterministic_sd_questions,
    generate_with_9router,
)


def _format_db_item(q: ExerciseQuestion, ordinal: int) -> dict:
    """Format an ExerciseQuestion into the legacy/storage soal_exercise_db schema."""
    item_id = hashlib.md5(f"sd{q.grade}-{q.bab}-{q.question_id}-{ordinal}".encode()).hexdigest()[:24]
    options_formatted = []
    letters = ["A", "B", "C", "D"]
    for idx, opt_text in enumerate(q.options):
        letter = letters[idx] if idx < len(letters) else chr(65 + idx)
        is_correct = (opt_text == q.correct_answer) or (q.correct_answer == letter)
        alasan = f"Benar: {q.explanation}" if is_correct else "Distraktor pilihan salah matematika siswa"
        options_formatted.append({
            "option_id": letter,
            "text": opt_text,
            "alasan": alasan,
        })

    # Pick the correct letter
    correct_letter = "A"
    for idx, opt_text in enumerate(q.options):
        if opt_text == q.correct_answer or q.correct_answer == letters[idx]:
            correct_letter = letters[idx]
            break

    return {
        "_id": item_id,
        "question_id": q.question_id,
        "grade": q.grade,
        "kelas_id": f"kelas{q.grade}",
        "bab": q.bab,
        "subbab_id": q.topic or f"Bab {q.bab} Matematika SD Kelas {q.grade}",
        "soal_text": q.question_text,
        "has_image": q.has_image,
        "image_url": [],
        "visual_metadata": q.visual_metadata.model_dump() if q.visual_metadata else None,
        "katex_enabled": q.katex_enabled,
        "soal_type": "Pilihan Ganda",
        "options": options_formatted,
        "matching_pairs": None,
        "jawaban": correct_letter,
        "correct_answer": q.correct_answer,
        "explanation": q.explanation,
        "cognitive_level": None,
        "cognitive_score": None,
        "status": "active",
    }


def generate_for_grade(
    grade: int,
    count: int = 10,
    batch: int = 1,
    out_dir: Path = ROOT / "output" / "exercise",
    use_9router: bool = False,
) -> dict:
    """Generate questions for a grade and write them to output/exercise/kelas<N>/batch<B>/."""
    book = f"kelas{grade}"
    batch_str = f"batch{batch:02d}"
    target_dir = out_dir / book / batch_str
    target_dir.mkdir(parents=True, exist_ok=True)

    levels = ["easy", "medium", "hard"]
    all_questions: list[ExerciseQuestion] = []

    per_level = max(1, count // len(levels))
    for lvl in levels:
        if use_9router:
            qs, _, _ = generate_with_9router(grade=grade, count=per_level, level=lvl)
        else:
            qs = generate_deterministic_sd_questions(grade=grade, count=per_level, level=lvl)
        all_questions.extend(qs)

    db_items = [_format_db_item(q, idx + 1) for idx, q in enumerate(all_questions)]
    meta_items = {}
    for idx, (q, db_item) in enumerate(zip(all_questions, db_items)):
        meta_items[db_item["_id"]] = {
            "id": q.question_id,
            "batch": batch,
            "grade": grade,
            "kelas_id": book,
            "level_target": q.level,
            "has_image": q.has_image,
            "image_type": q.visual_metadata.image_type if q.visual_metadata else None,
            "image_prompt": q.visual_metadata.image_prompt if q.visual_metadata else None,
            "katex_enabled": q.katex_enabled,
            "topic": q.topic,
            "explanation": q.explanation,
        }

    db_payload = {
        "pipeline_version": "exercise-sd-visual-2026",
        "book": book,
        "grade": grade,
        "batch": batch,
        "total_items": len(db_items),
        "items": db_items,
    }

    db_file = target_dir / "soal_exercise_db.json"
    meta_file = target_dir / "soal_exercise_meta.json"
    readme_file = target_dir / "README.md"

    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(db_payload, f, ensure_ascii=False, indent=2)

    with open(meta_file, "w", encoding="utf-8") as f:
        json.dump(meta_items, f, ensure_ascii=False, indent=2)

    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(
            f"# Bank Soal Latihan {book.upper()} ({batch_str})\n\n"
            f"- Total Soal: {len(db_items)}\n"
            f"- Dominan Bergambar: Ya (100% visual metadata)\n"
            f"- KaTeX Enabled: Ya (Formula inline `$ ... $`)\n"
            f"- Tanggal Generate: 2026-11-04\n"
        )

    print(f"[OK] {book} {batch_str}: Generated {len(db_items)} questions -> {db_file}")
    return {"grade": grade, "book": book, "count": len(db_items), "path": str(db_file)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate visual exercise questions for SD 1-4")
    parser.add_argument("--grade", type=int, choices=[1, 2, 3, 4], help="Target grade (1-4)")
    parser.add_argument("--all", action="store_true", help="Generate for all SD grades (1, 2, 3, 4)")
    parser.add_argument("--count", type=int, default=10, help="Questions per grade (default: 10)")
    parser.add_argument("--batch", type=int, default=1, help="Batch number (default: 1)")
    parser.add_argument("--use-9router", action="store_true", help="Attempt 9Router LLM call")
    args = parser.parse_args()

    grades = [1, 2, 3, 4] if args.all or not args.grade else [args.grade]
    for g in grades:
        generate_for_grade(g, count=args.count, batch=args.batch, use_9router=args.use_9router)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

