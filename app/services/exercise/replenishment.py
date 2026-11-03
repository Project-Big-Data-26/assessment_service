"""Plan targeted replenishment without generating, validating, or publishing."""
from collections import Counter, defaultdict

from app.ingestion.question_sync import LEVELS


def build_replenishment(inventory, questions, targets, readiness, generated_pending=None):
    if inventory.get("policy") != "per_subchapter_per_level_v1":
        raise ValueError("Replenishment requires an audit per subchapter and level")
    pending = defaultdict(list)
    generated_pending = generated_pending or []
    new_pending = Counter((q["class_key"], q["chapter_no"], q["code"]) for q in generated_pending)
    if len({q["_id"] for q in generated_pending}) != len(generated_pending):
        raise ValueError("Duplicate generated pending candidate IDs")
    if {q["_id"] for q in generated_pending} & {q.qid for q in questions}:
        raise ValueError("Generated pending candidates overlap canonical validation exports")
    references = defaultdict(list)
    withheld = []
    for source in questions:
        item = source.item
        if (item.get("status") == "active" and item.get("cognitive_level") in LEVELS
                and item.get("soal_text") and item.get("options") and item.get("jawaban")
                and not item.get("image_url")):
            references[(source.class_key, source.chapter_no, source.code)].append(source)
        if source.kind != "exercise" or source.item.get("status") == "active":
            continue
        if source.item.get("cognitive_level") is None:
            pending[(source.class_key, source.chapter_no, source.code)].append({
                "_id": source.qid, "original_target": targets.get(source.qid), "source": source.source})
        else:
            withheld.append({"_id": source.qid, "class_key": source.class_key,
                             "chapter_no": source.chapter_no, "code": source.code,
                             "level": source.item.get("cognitive_level"),
                             "status": "inactive_review_required"})
    groups = []
    for key, candidates in sorted(pending.items()):
        groups.append({"class_key": key[0], "chapter_no": key[1], "code": key[2],
                       "count": len(candidates), "by_original_target": dict(Counter(
                           c["original_target"] or "unknown" for c in candidates)),
                       "candidates": candidates})
    jobs = []
    for row in inventory["rows"]:
        for level in LEVELS:
            missing = row["level_shortfalls"][level]
            if missing <= 0:
                continue
            key = row["class_key"], row["chapter_no"], row["code"]
            refs = sorted(references.get(key, []), key=lambda ref: (
                ref.kind != "exercise", ref.item["cognitive_level"] != level, ref.qid))
            source_check = readiness.get(row["class_key"], {"status": "not_checked"})
            status = ("await_existing_validation" if pending.get(key) else
                      "await_new_batch_validation" if new_pending[key] else
                      "ready_for_reference_plan" if refs else
                      "ready_for_generation_plan" if source_check["status"] == "ready" else
                      "blocked_sources")
            jobs.append({"job_id": f"{key[0]}-b{key[1]:02d}-{key[2]}-{level}",
                         "class_key": key[0], "chapter_no": key[1], "code": key[2],
                         "subchapter_name": row["name"], "level_target": level,
                         "active_now": row["levels"][level], "required": row["required"],
                         "shortfall": missing, "status": status,
                         "pending_at_subchapter": len(pending.get(key, [])),
                         "new_batch_candidates_at_subchapter": new_pending[key],
                         "reference_counts": dict(Counter(ref.kind for ref in refs)),
                         "same_level_reference_count": sum(ref.item["cognitive_level"] == level for ref in refs),
                         "reference_ids": [ref.qid for ref in refs[:3]],
                         "generation_only": True, "validation_approved": False})
    # Reuse already-generated candidates first; patch existing upper-grade banks
    # before the separate visual generation project for grades 1-4.
    jobs.sort(key=lambda job: (
        job["status"] != "await_existing_validation",
        int(job["class_key"].split("_")[0][5:]) <= 4,
        job["shortfall"], int(job["class_key"].split("_")[0][5:]),
        job["class_key"], job["chapter_no"], job["code"], LEVELS.index(job["level_target"])))
    summary = {"jobs": len(jobs), "active_shortfall": sum(j["shortfall"] for j in jobs),
               "existing_unlabelled_candidates": sum(g["count"] for g in groups),
               "generated_candidates_pending": len(generated_pending),
               "new_batch_candidates_pending": sum(q.get('generation_mode')!='batch01_additions' for q in generated_pending),
               "batch01_additions_candidates_pending": sum(q.get('generation_mode')=='batch01_additions' for q in generated_pending),
               "inactive_labelled_review_only": len(withheld),
               "jobs_by_status": dict(Counter(j["status"] for j in jobs))}
    if summary["active_shortfall"] != inventory["shortfall_questions"]:
        raise ValueError("Replenishment total differs from audited deficit")
    return {"schema_version": "exercise-replenishment-v1", "mode": "planning_only",
            "scope": inventory["scope"], "new_api_calls": 0, "database_writes": 0,
            "policy": "per_subchapter_per_level_v1", "summary": summary,
            "pending_credit_towards_active": 0,
            "notes": ["Original targets are not final difficulty labels.",
                      "Pending/inactive candidates never count as available active questions.",
                      "Re-audit after validation; do not subtract pending counts as guaranteed coverage.",
                      "Batch01 additions require the dedicated append-only backup/manifest workflow; never replace old questions or labels.",
                      "Generate new candidates first; validation of new batches needs separate approval.",
                      "This backlog is not a generation manifest or validation approval.",
                      "Active text references in the exact class/chapter/subchapter may replace missing PDF inputs.",
                      "Same-level references are preferred; generated difficulty still needs independent validation."],
            "readiness_by_class": readiness, "existing_pending": groups,
            "new_batch_pending": generated_pending,
            "inactive_review": withheld, "jobs": jobs}


def render_replenishment(plan):
    summary = plan["summary"]
    lines = ["# Antrean penambalan latihan", "",
             "Rencana berdasarkan data lokal; bukan perubahan production atau hasil generate.",
             "Batas tiap level/subbab: SD 10, SMP 15, SMA 20.", "",
             f"Kekurangan: {summary['active_shortfall']} soal aktif pada {summary['jobs']} kombinasi subbab-level.",
             f"Kandidat lama tanpa label: {summary['existing_unlabelled_candidates']} (belum mengurangi kekurangan).",
             f"Kandidat hasil generate menunggu validasi: {summary['generated_candidates_pending']} (belum mengurangi kekurangan).",
             f"Rinciannya: penambahan batch01 {summary['batch01_additions_candidates_pending']}; pilot batch baru {summary['new_batch_candidates_pending']}.",
             f"Soal berlabel tetapi inactive: {summary['inactive_labelled_review_only']} (perlu review, bukan otomatis diaktifkan).", "",
             "## Urutan kerja", "",
             "1. Periksa kandidat lama yang validasinya belum selesai; hasilnya belum dijamin sesuai level target.",
             "2. Audit ulang setelah validasi selesai untuk menghitung kekurangan yang tersisa.",
             "3. Siapkan pilot kecil dari soal tervalidasi di kelas/subbab yang sama; PDF tidak wajib untuk mode variasi ini.",
             "4. Generate kandidat baru tanpa validasi paralel; validasi batch baru tetap menunggu instruksi MULAI VALIDASI.",
             "5. Tambah secara bertahap sampai hasil validasi aktif memenuhi setiap level, lalu audit database dan web.", "",
             "Soal inactive dan label hasil validasi tidak diubah untuk mengejar kuota.",
             "Rencana ini tidak menjalankan API, mengubah batch, atau memicu nightly.", "",
             "## Kandidat lama yang menunggu validasi", "",
             "| Kelas | Bab | Subbab | Kandidat | Target awal |", "|---|---:|---|---:|---|"]
    for group in plan["existing_pending"]:
        counts = ", ".join(f"{k}: {v}" for k, v in sorted(group["by_original_target"].items()))
        lines.append(f"| {group['class_key']} | {group['chapter_no']} | {group['code']} | {group['count']} | {counts} |")
    lines += ["", "## Kandidat batch baru", ""]
    for candidate in plan["new_batch_pending"]:
        lines.append(f"- {candidate['class_key']} Bab {candidate['chapter_no']} {candidate['code']}, "
                     f"target {candidate['level_target']}, ID {candidate['_id']}, {candidate['batch']}.")
    lines += ["", "## Kesiapan sumber mode buku (opsional jika acuan tervalidasi tersedia)", ""]
    for key, result in plan["readiness_by_class"].items():
        lines.append(f"- {key}: {result['status']}")
        lines.extend(f"  - Belum tersedia: {path}" for path in result.get("missingInputs", []))
    lines += ["", "## Antrean tiap level", "",
              "ready_for_generation_plan = sumber umum tersedia; rencana dan halaman subbab masih harus diverifikasi.",
              "ready_for_reference_plan = soal teks tervalidasi pada kelas/bab/subbab yang sama tersedia sebagai acuan; belum berarti kandidat sudah dibuat.",
              "await_existing_validation = hitung ulang setelah kandidat lama selesai; jangan langsung generate ulang.",
              "await_new_batch_validation = kandidat baru sudah dibuat; tetap belum dihitung aktif dan belum diizinkan validasi otomatis.",
              "blocked_sources = sumber generator belum lengkap.", "",
              "| Kelas | Bab | Kode | Subbab | Level target | Aktif | Minimum | Kurang | Acuan teks aktif | Status |",
              "|---|---:|---|---|---|---:|---:|---:|---:|---|"]
    for job in plan["jobs"]:
        name = job["subchapter_name"].replace("|", "\\|")
        lines.append(f"| {job['class_key']} | {job['chapter_no']} | {job['code']} | {name} | "
                     f"{job['level_target']} | {job['active_now']} | {job['required']} | "
                     f"{job['shortfall']} | {sum(job['reference_counts'].values())} | {job['status']} |")
    return "\n".join(lines) + "\n"
