"""
Pelari antrean: mengisi slot latihan yang masih kosong lewat 9Router (generate -> verifikasi buta -> perbaiki).
Dari root project:

    venv/Scripts/python scripts/run_exercise_queue.py --book kelas9 --daftar            # hanya tampilkan antrean
    venv/Scripts/python scripts/run_exercise_queue.py --book kelas9 --maks-slot 3       # kerjakan 3 slot pertama
    venv/Scripts/python scripts/run_exercise_queue.py --book kelas9 --book kelas7 --pekerja 2 --maks-menit 240

Aturan:
  - Slot = (buku, bab, subbab, level). Yang sudah punya berkas (dari sumber apa pun) DILEWATI, tidak pernah ditimpa.
  - Level dalam satu subbab berurutan easy -> medium -> hard; subbab berbeda boleh paralel (--pekerja).
  - Berhenti rapi bila melewati --maks-menit atau ada 3 slot gagal berturut-turut (mis. kuota provider habis).
  - Status tiap slot dicatat di output/exercise_queue/status.jsonl; berkas STOP di folder itu menghentikan run.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.llm.ninerouter import NineRouterClient, NineRouterSettings
from app.services.exercise import config as C
from app.services.exercise.llm_generate import Job
from app.services.exercise.llm_pipeline import STATUS_GAGAL, SlotResult, kerjakan_slot
from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import get_book

QUEUE_DIR = os.path.join(C.OUT_ROOT, "..", "exercise_queue")
Slot = Tuple[str, int, str, str]


def _kurang_milik_pipeline(path: str, kuota: int) -> bool:
    """Berkas buatan pipeline 9Router yang jumlah soalnya masih di bawah kuota (bisa dilengkapi)."""
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
    except (OSError, ValueError):
        return False
    if not str(d.get("generator") or "").startswith("9router:"):
        return False
    if str(d.get("alasan_kapasitas") or "").startswith("[final]"):
        return False          # kapasitas kurang yang sudah ditinjau dan dinyatakan final: jangan diulang
    if len(d.get("soal", [])) < kuota:
        return True
    try:                      # penuh, tetapi belum diverifikasi / verifikasi terakhir belum cocok semua
        with open(path[:-len(".json")] + ".verifikasi.json", encoding="utf-8") as f:
            v = json.load(f)
        return v.get("cocok") != v.get("total")
    except (OSError, ValueError):
        return True


def antrean(books: List[str], batch: int, lengkapi: bool = False) -> List[Slot]:
    out: List[Slot] = []
    for book in books:
        for bab_no in range(1, 40):
            bab = kurikulum.get(book, bab_no)
            if not bab:
                continue
            for kode, _nama in bab.subbab:
                for level in C.LEVELS:
                    path = os.path.join(C.OUT_ROOT, book, f"batch{batch:02d}", f"bab{bab_no:02d}", f"{kode}_{level}.json")
                    kuota = C.KUOTA_PER_LEVEL[get_book(book).jenjang]
                    if not os.path.exists(path) or (lengkapi and _kurang_milik_pipeline(path, kuota)):
                        out.append((book, bab_no, kode, level))
    return out


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", action="append", required=True)
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--daftar", action="store_true", help="hanya tampilkan antrean")
    ap.add_argument("--lewati", action="append", default=[], metavar="BUKU:BAB:SUBBAB",
                    help="lewati subbab tertentu, mis. kelas7:6:F (boleh diulang), untuk subbab yang sangat besar")
    ap.add_argument("--lengkapi", action="store_true",
                    help="sertakan berkas buatan pipeline ini yang soalnya masih kurang dari kuota")
    ap.add_argument("--maks-slot", type=int, default=0, help="0 = semua")
    ap.add_argument("--maks-menit", type=int, default=0, help="0 = tanpa batas waktu")
    ap.add_argument("--pekerja", type=int, default=2)
    ap.add_argument("--perbaikan", type=int, default=2, help="putaran perbaikan otomatis per slot")
    a = ap.parse_args()

    slots = antrean(a.book, a.batch, a.lengkapi)
    lewati = {tuple(x.split(":")) for x in a.lewati}
    slots = [s for s in slots if (s[0], str(s[1]), s[2]) not in lewati]
    if a.maks_slot:
        slots = slots[: a.maks_slot]
    print(f"Antrean: {len(slots)} slot")
    if a.daftar:
        for s in slots:
            print("  ", *s)
        return 0
    if not slots:
        return 0

    try:
        settings = NineRouterSettings.from_environment()
    except ValueError as exc:
        print(f"[GAGAL] konfigurasi .env: {exc}")
        return 2
    solver = settings.solver_model
    if not solver or solver == settings.model:
        print("[GAGAL] NINEROUTER_MODEL_SOLVER harus diisi dan berbeda dari NINEROUTER_MODEL")
        return 2

    os.makedirs(QUEUE_DIR, exist_ok=True)
    stop_file = os.path.join(QUEUE_DIR, "STOP")
    status_file = os.path.join(QUEUE_DIR, "status.jsonl")
    deadline = time.monotonic() + a.maks_menit * 60 if a.maks_menit else None
    lock = threading.Lock()
    gagal_berturut = [0]

    # satu rantai per subbab (level berurutan); rantai berbeda jalan paralel
    rantai: Dict[Tuple[str, int, str], List[Slot]] = {}
    for s in slots:
        rantai.setdefault(s[:3], []).append(s)

    def hentikan() -> bool:
        return (os.path.exists(stop_file) or gagal_berturut[0] >= 3
                or (deadline is not None and time.monotonic() > deadline))

    def jalankan(urutan: List[Slot]) -> None:
        with NineRouterClient(settings) as client:
            for book, bab_no, kode, level in urutan:
                if hentikan():
                    return
                job = Job(book, bab_no, kode, level, a.batch)
                tag = f"{book} bab{bab_no} {kode} {level}"
                print(f"[mulai] {tag}", flush=True)
                try:
                    res = kerjakan_slot(job, client, solver, maks_perbaikan=a.perbaikan,
                                        progress=lambda m, t=tag: print(f"   {t}: {m.strip()}", flush=True))
                except Exception as exc:     # satu slot bermasalah tidak boleh mematikan pekerja/antrean
                    import traceback
                    traceback.print_exc()
                    res = SlotResult(job.path, STATUS_GAGAL, 0, 0, 0, 0,
                                     [f"galat tak terduga: {type(exc).__name__}: {str(exc)[:160]}"])
                with lock:
                    gagal_berturut[0] = gagal_berturut[0] + 1 if res.status == STATUS_GAGAL else 0
                    with open(status_file, "a", encoding="utf-8") as f:
                        f.write(json.dumps({"waktu": dt.datetime.now().isoformat(timespec="seconds"), "slot": tag,
                                            "status": res.status, "soal": res.soal, "kuota": res.kuota,
                                            "perbaikan": res.perbaikan, "dibuang": res.dibuang,
                                            "token_in": res.tokens_in, "token_out": res.tokens_out,
                                            "detik": res.seconds, "errors": res.errors[:3]},
                                           ensure_ascii=False) + "\n")
                print(f"[{res.status}] {tag}: {res.soal}/{res.kuota} soal, perbaikan {res.perbaikan}, "
                      f"dibuang {res.dibuang}, {res.seconds}s", flush=True)
                if res.status == STATUS_GAGAL:
                    return          # level berikutnya di subbab ini bergantung pada yang gagal

    with ThreadPoolExecutor(max_workers=max(1, a.pekerja)) as pool:
        list(pool.map(jalankan, rantai.values()))
    print("Selesai. Status:", status_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
