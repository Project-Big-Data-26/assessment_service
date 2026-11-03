"""
export.py -- gabungkan file exercise yang LOLOS validate (cek format/kuota/duplikat milik generator) menjadi baris
tabel `soal` backend (Daftar Collections - Big Data.xlsx).

Hasil per batch:
  output/exercise/<buku>/batch<NN>/soal_exercise_db.json    baris tabel soal (hanya kolom resmi)
  output/exercise/<buku>/batch<NN>/soal_exercise_meta.json  info internal (tipe_generate, acuan, flag, ...)
  output/exercise/<buku>/batch<NN>/per_subbab/              turunan per subbab: .json (kolom tabel) + .md (lembar koreksi)
  (hanya turunan: koreksi dilakukan di file kerja <K>_<level>.json lalu export dijalankan ulang)

Penanda sementara (dipetakan ke ObjectId oleh Backend):
  subbab_id = NAMA subbab di buku panduan, kelas_id = kunci buku ("kelas9"), berkas_id = null.
cognitive_level, cognitive_score, confidence_score, status = null: diisi tahap validasi sistem berikutnya.
Nilai usulan kita (level target, skor target) disimpan di soal_exercise_meta.json.

  python -m app.services.exercise.export --book kelas9 --batch 1
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import sys
from pathlib import Path

from app.services.exercise import config as C
from app.services.exercise.options import susun
from app.services.exercise.refs import gambar_path, soal_text
from app.services.exercise.validate import validate_file
from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import get_book


def _oid(sid: str) -> str:
    return hashlib.sha1(sid.encode()).hexdigest()[:24]


def export_batch(book: str, batch: int, *, generation_only: bool = False, _locked: bool = False) -> dict:
    from .workflow import batch_lock, managed, begin_generation, load
    base = Path(C.OUT_ROOT) / book / f"batch{batch:02d}"
    if not _locked:
        with batch_lock(base):
            return export_batch(book, batch, generation_only=generation_only, _locked=True)
    if (base / "reference_replenishment_state.json").exists():
        raise ValueError("batch01 reference additions have a dedicated append export; do not rebuild legacy files")
    generation_only = generation_only or managed(base) or not (base / "soal_exercise_db.json").exists()
    plan_path = base / "generation_plan.json"
    if plan_path.exists() and load(plan_path).get("schemaVersion") == "exercise-reference-plan-v1":
        raise ValueError("reference-based pilot is already exported; preserve this batch and use a new reference batch")
    if generation_only:
        if managed(base) and (base / "generation_state.json").exists():
            if load(base / "generation_state.json").get("phase") == "validation_authorized":
                raise ValueError("approved generation is frozen; use a new batch")
        begin_generation(base, book, batch)
    return _export_batch(book, batch, generation_only=generation_only)


def _export_batch(book: str, batch: int, *, generation_only: bool) -> dict:
    base = os.path.join(C.OUT_ROOT, book, f"batch{batch:02d}")
    rows, meta, dilewati = [], {}, []
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).isoformat(timespec="seconds")
    prev = {}   # export sebelumnya: timestamp dipertahankan bila isi soal tidak berubah (file stabil, hash tidak bergeser)
    try:
        with open(os.path.join(base, "soal_exercise_db.json"), encoding="utf-8") as f:
            prev = {r["_id"]: r for r in json.load(f)["items"]}
    except (OSError, ValueError, KeyError):
        pass
    for path in sorted(glob.glob(os.path.join(base, "bab[0-9][0-9]", "*_*.json"))):
        if path.endswith((".blind.json", ".solver.json", ".verifikasi.json", ".tanpagambar.json")):
            continue
        name = os.path.relpath(path, base)
        data, errors, warns = validate_file(path)
        if errors or data is None:
            dilewati.append(f"{name}: validasi GAGAL ({len(errors)} error)")
            continue
        tanpa_gambar_cocok: set = set()
        if data.bergambar and not generation_only:
            sidecar = path[:-len(".json")] + ".tanpagambar.json"
            if not os.path.exists(sidecar):
                dilewati.append(f"{name}: berkas bergambar belum dicek 'tanpa gambar' "
                                f"(verify_exercise_9router.py --tanpa-gambar)")
                continue
            with open(sidecar, encoding="utf-8") as f:
                tanpa_gambar_cocok = set(json.load(f).get("tanpa_gambar_cocok", []))
            if tanpa_gambar_cocok:
                dilewati.append(f"{name}: {len(tanpa_gambar_cocok)} soal tidak diekspor (bisa dijawab tanpa gambar)")
        bab = kurikulum.get(book, data.bab_no)
        opsi = susun(data)
        spec = C.LEVEL_SPEC[data.level]
        kuota = C.KUOTA_PER_LEVEL[get_book(book).jenjang]
        kurang = None if data.bergambar else ({"jumlah": len(data.soal), "kuota": kuota, "alasan": data.alasan_kapasitas}
                  if data.kapasitas_kurang else None)
        for s in data.soal:
            if s.id in tanpa_gambar_cocok:
                continue
            options, benar = opsi[s.id]
            image_urls = [gambar_path(book, g).replace(os.sep, "/") for g in s.gambar]
            visual_proof = {}
            if generation_only:
                import shutil
                from .workflow import digest
                image_urls = []
                for reference in s.gambar:
                    source = Path(gambar_path(book, reference))
                    relative = f"assets/{digest(source)}{source.suffix.lower()}"
                    destination = Path(base) / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    if not destination.exists():
                        shutil.copyfile(source, destination)
                    if digest(destination) != digest(source):
                        raise ValueError("exported image checksum differs")
                    image_urls.append(relative)
                    proof_path = source.with_suffix(".json")
                    visual_proof[relative] = (json.loads(proof_path.read_text(encoding="utf-8"))
                        if s.visual_spec and proof_path.exists() else {"source": "pretest_reuse", "sourcePath": reference,
                            "pngSha256": digest(source), "visualEssentialStatus": "pending_independent_validation"})
            row = {
                "_id": _oid(s.id), "berkas_id": None, "subbab_id": bab.subbab_nama(data.subbab),
                "kelas_id": book, "soal_text": soal_text(s.stimulus, s.pertanyaan),
                "image_url": image_urls,
                "soal_type": "Pilihan Ganda", "options": options, "matching_pairs": None, "jawaban": benar,
                "cognitive_level": None, "cognitive_score": None, "status": None,
                "created_at": now, "updated_at": now, "confidence_score": None,
            }
            lama = prev.get(row["_id"])
            if lama:
                row["created_at"] = lama.get("created_at", now)
                row["updated_at"] = lama.get("updated_at", now) if all(
                    lama.get(k) == v for k, v in row.items() if k not in ("created_at", "updated_at")) else now
            rows.append(row)
            meta[_oid(s.id)] = {
                "id": s.id, "batch": data.batch, "bab_id": bab.bab_id, "subbab_kode": data.subbab,
                "level_target": data.level, "cognitive_score_target": spec["score"], "tipe_generate": s.tipe_generate, "variasi_cara": s.variasi_cara,
                "acuan": s.acuan.model_dump(exclude_none=True), "cognitive_c": s.cognitive_c,
                "jumlah_langkah": s.jumlah_langkah, "jenis_soal": s.jenis_soal,
                "pembahasan": s.pembahasan, "catatan": s.catatan, "dipaksa_kuota": s.dipaksa_kuota,
                "kapasitas_kurang": kurang, "skill_versi": data.skill_versi or "pra-v1",
                "generator": data.generator or "tidak-tercatat",
                "bergambar": data.bergambar, "gambar": s.gambar, "deskripsi_gambar": s.deskripsi_gambar,
                "warning": [w for w in warns if s.id in w],
            }
            if generation_only:
                meta[_oid(s.id)].update(visual_provenance=visual_proof, validation_status="validation_pending")
    # An old completion marker must never cover an export being rewritten.
    if generation_only:
        from app.presentation.latex import normalize_document
        rows, meta = normalize_document(rows), normalize_document(meta)
    Path(base, "extraction_ready.json").unlink(missing_ok=True)
    with open(os.path.join(base, "soal_exercise_db.json"), "w", encoding="utf-8") as f:
        json.dump({"pipeline_version": C.PIPELINE_VERSION, "book": book, "batch": batch, "items": rows},
                  f, ensure_ascii=False, indent=2)
    with open(os.path.join(base, "soal_exercise_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    from app.services.exercise.review import tulis_per_subbab, tulis_readme
    n_sub = tulis_per_subbab(base, book, rows, meta)
    tulis_readme(base, book, batch, rows, meta)
    if generation_only:
        from .workflow import finish_generation
        from .visual_plan import complete_plan
        if (Path(base) / "generation_plan.json").exists():
            complete = complete_plan(base)
        else:
            expected = {(b.bab_id, code, level) for number in range(1, 40)
                        if (b := kurikulum.get(book, number)) for code, _ in b.subbab for level in C.LEVELS}
            complete = bool(expected) and expected == {(m["bab_id"], m["subbab_kode"], m["level_target"]) for m in meta.values()}
        generation = finish_generation(base, complete=complete, problems=dilewati) if rows else {
            "validationStatus": "validation_pending", "complete": False}
        ready = False
    else:
        from app.services.exercise.handoff import mark_completed_export
        ready = mark_completed_export(Path(base), book, batch, rows, meta, dilewati)
    ringkas = {"total": len(rows), "file_per_subbab": n_sub, "file_dilewati": dilewati,
               "ready_for_validation": ready}
    if generation_only:
        ringkas["generation"] = generation
    print(ringkas)
    return ringkas


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--generation-only", action="store_true", help="Export candidates; no solver, readiness marker or validation API")
    a = ap.parse_args(argv)
    result = export_batch(a.book, a.batch, generation_only=True) if a.generation_only else export_batch(a.book, a.batch)
    if result["ready_for_validation"]:
        from app.services.exercise.handoff import run_validation
        return run_validation()
    return 0


if __name__ == "__main__":
    sys.exit(main())
