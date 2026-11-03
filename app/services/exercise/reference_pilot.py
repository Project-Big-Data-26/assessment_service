"""A small, locally checked pilot grounded in frozen validated exercise rows.

This adapter deliberately does not use the legacy PDF-based generator/schema.
It writes the same master/meta contract and uses the existing validation gate.
"""
from datetime import datetime, timezone
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import re

from app.ingestion.question_sync import load_sources
from .workflow import atomic_json, batch_lock, begin_generation, digest, finish_generation


def divisors(number):
    return [value for value in range(1, number + 1) if number % value == 0]


def check_math(candidate):
    """Enumerate the stated finite constraints independently of the proposed key."""
    spec = candidate["verification"]
    kind = spec["kind"]
    if kind == "three_factors_middle":
        matches = [n for n in range(spec["lower"] + 1, spec["upper"]) if len(divisors(n)) == 3]
        if len(matches) != 1:
            raise ValueError("Constraint does not identify one number")
        facts = {"number": matches[0], "divisors": divisors(matches[0])}
        answer = facts["divisors"][1]
    elif kind == "even_containers":
        matches = [n for n in divisors(spec["total"]) if n >= spec["minimum_containers"]
                   and n % 2 == 0 and spec["total"] // n >= spec["minimum_each"]]
        answer = len(matches)
        facts = {"valid_container_counts": matches,
                 "items_per_container": [spec["total"] // n for n in matches]}
    elif kind == "factor_count_and_sum":
        matches = [n for n in range(spec["lower"] + 1, spec["upper"])
                   if len(divisors(n)) == spec["count"] and sum(divisors(n)) == spec["sum"]]
        if len(matches) != 1:
            raise ValueError("Constraint does not identify one number")
        answer = matches[0]
        facts = {"number": answer, "divisors": divisors(answer), "sum": sum(divisors(answer))}
    else:
        raise ValueError("Unsupported local mathematical check")
    options = [candidate["answer"], *candidate["distractors"]]
    if (str(answer) != candidate["answer"] or len(options) != 4
            or len({int(option) for option in options}) != 4):
        raise ValueError("Proposed key or distractors fail mathematical/uniqueness checks")
    return {"status": "passed_local_enumeration", "answer": str(answer), "facts": facts,
            "independent_ai_validation": "pending", "difficulty_validation": "pending"}


def factor_candidates():
    # Authored pilot content. Verification specs are executed separately above.
    return [
        {"reference_id": "b270725510f9980698e06549", "variation": "angka_dan_inferensi",
         "question": "Raka mencari sebuah bilangan yang lebih dari 100 dan kurang dari 150. Bilangan itu mempunyai tepat tiga faktor. Jika faktor-faktornya ditulis dari yang terkecil, faktor yang berada di tengah adalah ....",
         "answer": "11", "distractors": ["7", "12", "13"],
         "distractor_reasons": ["Kuadrat 7 adalah 49, di luar rentang bilangan.",
                                "144 tidak mempunyai tepat tiga faktor.",
                                "Kuadrat 13 adalah 169, di luar rentang bilangan."],
         "explanation": "Bilangan dengan tepat tiga faktor adalah kuadrat bilangan prima. Di antara 100 dan 150 hanya 121 yang memenuhi. Faktor 121 adalah 1, 11, dan 121; faktor tengahnya 11.",
         "target_reason": "Menggabungkan batas bilangan, jumlah faktor, dan posisi faktor; label hard masih usulan.",
         "verification": {"kind": "three_factors_middle", "lower": 100, "upper": 150}},
        {"reference_id": "b333aee7161a2d786f3e334e", "variation": "konteks_dan_syarat",
         "question": "Sebanyak 72 bibit cabai akan dibagi ke beberapa baki. Semua baki berisi bibit sama banyak dan tidak ada bibit tersisa. Jumlah baki harus genap dan paling sedikit 4. Setiap baki harus berisi paling sedikit 6 bibit. Ada berapa pilihan jumlah baki yang memenuhi semua syarat?",
         "answer": "4", "distractors": ["3", "5", "8"],
         "distractor_reasons": ["Melewatkan salah satu pembagi yang memenuhi semua syarat.",
                                "Memasukkan 9 baki, padahal jumlah baki harus genap.",
                                "Mengabaikan syarat minimal 6 bibit per baki."],
         "explanation": "Jumlah baki harus merupakan faktor 72, genap, paling sedikit 4, dan paling banyak 12 agar tiap baki berisi minimal 6 bibit. Pilihannya 4, 6, 8, dan 12 baki, dengan isi masing-masing 18, 12, 9, dan 6 bibit. Ada 4 pilihan.",
         "target_reason": "Menyaring pasangan faktor menggunakan tiga syarat dalam konteks pembagian; label hard masih usulan.",
         "verification": {"kind": "even_containers", "total": 72,
                          "minimum_containers": 4, "minimum_each": 6}},
        {"reference_id": "9fa800e40737cb60e33161e7", "variation": "angka_dan_konteks",
         "question": "Sebuah lemari penyimpanan diberi nomor berupa bilangan yang lebih dari 40 dan kurang dari 50. Nomor itu mempunyai tepat empat faktor. Jumlah keempat faktornya adalah 72. Nomor lemari tersebut adalah ....",
         "answer": "46", "distractors": ["44", "45", "49"],
         "distractor_reasons": ["44 mempunyai enam faktor dengan jumlah 84.",
                                "45 mempunyai enam faktor dengan jumlah 78.",
                                "49 mempunyai tiga faktor dengan jumlah 57."],
         "explanation": "Faktor 46 adalah 1, 2, 23, dan 46. Jumlahnya 1 + 2 + 23 + 46 = 72. Di antara 41 sampai 49, hanya 46 yang mempunyai tepat empat faktor dengan jumlah 72.",
         "target_reason": "Menggabungkan rentang, banyak faktor, dan jumlah faktor untuk menemukan bilangan; label hard masih usulan.",
         "verification": {"kind": "factor_count_and_sum", "lower": 40, "upper": 50,
                          "count": 4, "sum": 72}},
    ]


def render_reference_preview(rows, metadata, plan):
    lines = ["# Pilot variasi dari soal tervalidasi", "", "Kelas 5, Bab 2, subbab C: Faktor.",
             f"{len(rows)} kandidat teks; target hard, belum divalidasi AI dan belum aktif.",
             "Soal asli di bawah diambil persis dari snapshot acuan saat generate, bukan dari PDF.", ""]
    for number, row in enumerate(rows, 1):
        info = metadata[row["_id"]]
        reference_id = info["acuan"]["id"]
        snapshot = plan["referenceSnapshots"][reference_id]
        original = snapshot["item"]
        lines += [f"## Soal {number}", "", "### Hasil variasi baru", "", row["soal_text"], ""]
        lines += [f"- {option['option_id']}. {option['text']}" for option in row["options"]]
        lines += ["", f"Kunci usulan: **{row['jawaban']}**", "", info["pembahasan"], "",
                  "Pemeriksaan matematika lokal: lolos. Validasi AI dan level final: belum dilakukan.", "",
                  "### Soal asli pada blueprint/acuan", "", original["soal_text"], ""]
        lines += [f"- {option['option_id']}. {option['text']}" for option in original["options"]]
        correct = next(option for option in original["options"] if option["option_id"] == original["jawaban"])
        lines += ["", f"Kunci asli: **{original['jawaban']} — {correct['text']}**", ""]
        if correct.get("alasan"):
            lines += [f"Alasan kunci dari acuan: {correct['alasan']}", ""]
        lines += [f"ID acuan: `{reference_id}`.",
                  f"Kelas/bab/subbab: {snapshot['class_key']} / Bab {snapshot['chapter_no']} / {snapshot['code']}.",
                  f"Label dan status acuan: `{original['cognitive_level']}` / `{original['status']}`.",
                  f"Berkas asal: `output/{snapshot['source']}`.", "", "---", ""]
    lines += ["Status kandidat baru: validation_pending. Tidak ada API generate/validasi, IRT, fine-tuning, atau penulisan database."]
    return "\n".join(lines) + "\n"


def refresh_reference_preview(base):
    from .workflow import load, verify_generation
    base = Path(base)
    checksum = verify_generation(base)
    rows = load(base / "soal_exercise_db.json")["items"]
    metadata = load(base / "soal_exercise_meta.json")
    plan = load(base / "generation_plan.json")
    (base / "PREVIEW.md").write_text(render_reference_preview(rows, metadata, plan), encoding="utf-8")
    if verify_generation(base) != checksum:
        raise ValueError("Preview refresh changed frozen generation data")
    return base / "PREVIEW.md"


def export_factor_pilot(output_root, batch=2):
    if type(batch) is not int or batch < 2:
        raise ValueError("Reference pilot requires a separate batch >= 2")
    output_root = Path(output_root)
    sources = load_sources(output_root)
    pool = [q for q in sources if q.kind == "exercise" and q.class_key == "kelas5"
            and q.chapter_no == 2 and q.code == "C" and q.item.get("status") == "active"
            and q.item.get("cognitive_level") in ("easy", "medium", "hard")]
    by_id = {q.qid: q for q in pool}
    candidates = factor_candidates()
    checks, snapshots, source_hashes = [], {}, {}
    for candidate in candidates:
        source = by_id.get(candidate["reference_id"])
        if source is None or source.item.get("subbab_id") != "Faktor" or source.item.get("image_url"):
            raise ValueError("Pilot requires an active, labelled, text reference in kelas5 Bab2 C Faktor")
        source_file = output_root / source.source
        source_hashes[source.source] = digest(source_file)
        source_metadata = source_file.parent.parent / "soal_exercise_meta.json"
        source_hashes[source_metadata.relative_to(output_root).as_posix()] = digest(source_metadata)
        snapshots[source.qid] = {"class_key": source.class_key, "chapter_no": source.chapter_no,
                                "code": source.code, "kind": source.kind, "source": source.source,
                                "item": source.item}
        checks.append(check_math(candidate))
    normalize = lambda text: re.sub(r"\s+", " ", text.casefold()).strip()
    proposed = [normalize(c["question"]) for c in candidates]
    if len(proposed) != len(set(proposed)):
        raise ValueError("Duplicate pilot stems")
    for stem in proposed:
        if any(stem == normalize(q.item["soal_text"]) for q in sources if q.class_key == "kelas5"):
            raise ValueError("Pilot duplicates an existing class stem")
    base = output_root / "exercise/kelas5" / f"batch{batch:02d}"
    with batch_lock(base):
        if any(p.name != ".workflow.lock" for p in base.iterdir()):
            raise ValueError("Pilot destination is not empty; preserve it and use a new batch")
        begin_generation(base, "kelas5", batch)
        now = datetime.now(timezone.utc).isoformat()
        rows, metadata = [], {}
        for index, (candidate, check) in enumerate(zip(candidates, checks), 1):
            working_id = f"kelas5-b02-c-hard-bt{batch:02d}-{index:03d}"
            qid = hashlib.md5(working_id.encode()).hexdigest()[:24]
            if any(source.qid == qid for source in sources):
                raise ValueError("Pilot ID already exists in canonical sources")
            correct_position = (index - 1) % 4
            options = [{"text": text, "alasan": "Salah: " + reason}
                       for text, reason in zip(candidate["distractors"], candidate["distractor_reasons"])]
            options.insert(correct_position, {"text": candidate["answer"], "alasan": "Benar: " + candidate["explanation"]})
            for letter, option in zip("ABCD", options):
                option["option_id"] = letter
            rows.append({"_id": qid, "berkas_id": None, "kelas_id": "kelas5", "subbab_id": "Faktor",
                         "soal_text": candidate["question"], "image_url": [], "soal_type": "Pilihan Ganda",
                         "options": options, "matching_pairs": None, "jawaban": "ABCD"[correct_position],
                         "cognitive_level": None, "cognitive_score": None, "confidence_score": None,
                         "status": "inactive", "created_at": now, "updated_at": now})
            metadata[qid] = {"id": working_id, "batch": batch, "bab_id": "SD5-B2", "subbab_kode": "C",
                             "level_target": "hard", "cognitive_score_target": 1400, "tipe_generate": "variasi",
                             "variasi_cara": candidate["variation"], "generator": "codex:validated-reference-pilot-v1",
                             "acuan": {"sumber": "exercise_validated", "id": candidate["reference_id"],
                                       "snapshot": "generation_plan.json"},
                             "pembahasan": candidate["explanation"], "alasan_level_target": candidate["target_reason"],
                             "validation_status": "validation_pending", "local_math_check": check,
                             "max_stem_similarity": max(SequenceMatcher(None, normalize(candidate["question"]),
                                                                          normalize(q.item["soal_text"])).ratio() for q in pool)}
        plan = {"schemaVersion": "exercise-reference-plan-v1", "class": "kelas5", "batch": f"batch{batch:02d}",
                "generationOnly": True, "total": len(rows), "referenceSnapshots": snapshots,
                "sourceHashes": source_hashes, "candidates": candidates,
                "localChecks": "enumeration, unique options, exact stem dedup; AI/content/difficulty validation pending"}
        atomic_json(base / "generation_plan.json", plan)
        atomic_json(base / "soal_exercise_db.json", {"pipeline_version": "exercise-reference-v1",
                                                   "book": "kelas5", "batch": batch, "items": rows})
        atomic_json(base / "soal_exercise_meta.json", metadata)
        if any(digest(output_root / path) != checksum for path, checksum in source_hashes.items()):
            raise ValueError("Reference sources changed during generation; batch remains pending")
        result = finish_generation(base, complete=True)
        (base / "PREVIEW.md").write_text(render_reference_preview(rows, metadata, plan), encoding="utf-8")
        return {"directory": str(base), "questionCount": len(rows), "validationStatus": "validation_pending",
                "manifestSha256": result["manifestSha256"], "newApiCalls": 0, "databaseWrites": 0}
