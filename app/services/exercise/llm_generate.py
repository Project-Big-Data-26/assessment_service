"""
llm_generate.py -- generate bank soal latihan (1 subbab x 1 level) lewat 9Router, tanpa agen Claude Code.

Alur (semua aturan mutu tetap dari validate.py; aturan penulisan soal dimuat dari SKILL.md):
  1. kumpulkan bahan: halaman Buku Siswa subbab, soal pretest subbab (acuan variasi), soal yang sudah ada
  2. minta LLM menulis soal per putaran kecil; kode memberi id, memeriksa tiap soal dengan validate_file
     (--partial), membuang yang gagal, lalu meminta pengganti dengan umpan balik galat
  3. tulis file kerja <out>/<buku>/batch<BB>/bab<NN>/<K>_<level>.json + log putaran (.runlog.jsonl)

Pemakaian: lihat scripts/generate_exercise_9router.py
"""

from __future__ import annotations

import json
import math
import os
import re
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from pydantic import ValidationError

from app.llm.ninerouter import NineRouterClient, NineRouterError, image_part
from app.services.exercise import config as C
from app.services.exercise.refs import acuan_key, gambar_path, load_exercise, load_pretest, soal_text
from app.services.exercise.schema import ExerciseFile, Soal
from app.services.exercise.validate import validate_file
from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import OUT_ROOT as PRETEST_ROOT
from app.services.pretest.agentic.books import ROOT, get_book, page_md_path

SKILL_PATH = os.path.join(ROOT, ".claude", "skills", "generate-soal-exercise", "SKILL.md")
TRIAL_ROOT = os.path.join(ROOT, "output", "exercise_9router")   # folder uji (di luar output/exercise)
CHUNK = 5                      # soal diminta per panggilan
# Model berpikir (mis. Gemini) menghabiskan sebagian max_tokens untuk penalaran: batas 4096 memotong JSON
# di tengah kalimat. Batas khusus generate dibuat longgar; balasan yang tetap terpotong dideteksi di bawah.
GEN_MAX_TOKENS = 16000
MAKS_GAMBAR_PER_PANGGILAN = 6   # gambar yang dilampirkan per panggilan (hemat token)
MAX_ROUNDS_EXTRA = 3          # putaran tambahan di luar ceil(kuota / CHUNK)

_HEAD_RE = re.compile(r"^\W*([A-Z])\.\s+(.+?)\W*$")
_IMG_RE = re.compile(r"!\[\]\([^)]*\)\s*")
_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


class GenerateError(RuntimeError):
    pass


# --------------------------------------------------------------------------- bahan

def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def subbab_pages(book_name: str, bab_no: int, kode: str) -> Tuple[int, int]:
    """Rentang halaman Buku Siswa untuk subbab: dari judul 'K. <nama>' sampai sebelum judul subbab berikutnya."""
    book = get_book(book_name)
    index_path = os.path.join(book.md_dir("siswa"), "index.json")
    with open(index_path, encoding="utf-8") as f:
        pages = json.load(f)["pages"]
    bab = kurikulum.get(book_name, bab_no)
    if not bab:
        raise GenerateError(f"bab {book_name} no.{bab_no} tidak ada di kurikulum")
    nama = {k: n for k, n in bab.subbab}
    if kode not in nama:
        raise GenerateError(f"subbab {kode} tidak ada di {bab.bab_id}: {list(nama)}")

    in_bab = sorted(int(p) for p, v in pages.items() if v.get("bab_no") == bab_no)
    if not in_bab:
        raise GenerateError(f"tidak ada halaman bab {bab_no} di index.json {book_name}")
    starts: Dict[str, int] = {}
    for p in in_bab:
        for h in pages[str(p)]["headings"]:
            m = _HEAD_RE.match(h.replace("~~", "").strip())
            if m and m.group(1) in nama and _norm(nama[m.group(1)]) in _norm(m.group(2)):
                starts.setdefault(m.group(1), p)
    if kode not in starts:
        raise GenerateError(f"judul subbab {kode} tidak terdeteksi di halaman bab {bab_no}")
    later = [p for k, p in starts.items() if p > starts[kode]]
    end = (min(later) - 1) if later else in_bab[-1]
    return starts[kode], end


def page_text(book_name: str, page: int) -> str:
    path = page_md_path(get_book(book_name), "siswa", page)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = _COMMENT_RE.sub("", text)
    text = _IMG_RE.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _load_rules() -> str:
    """Aturan penulisan soal: bagian SKILL.md dari 'Dua tipe soal' sampai sebelum 'Kapasitas dan penanda'."""
    with open(SKILL_PATH, encoding="utf-8") as f:
        text = f.read()
    a = text.find("### Dua tipe soal")
    b = text.find("### Kapasitas dan penanda")
    if a < 0 or b < a:
        raise GenerateError("SKILL.md berubah struktur: bagian 'Dua tipe soal'..'Kapasitas dan penanda' tidak ketemu")
    return text[a:b].strip()


# --------------------------------------------------------------------------- prompt

SYSTEM = """Kamu penulis soal latihan pilihan ganda untuk buku pelajaran sekolah Indonesia.
Kamu TIDAK punya alat/berkas: semua bahan ada di pesan ini. Abaikan petunjuk di aturan yang menyebut Grep,
Read, skrip, atau validator; yang berlaku hanyalah isi dan format soal.
Kerjakan setiap soal sampai selesai di benakmu SEBELUM menulis kunci; buang soal yang kuncinya ragu-ragu.
Balas HANYA satu objek JSON valid, tanpa teks lain."""

FORMAT = """Format balasan:
{"soal": [ {
  "tipe_generate": "variasi" | "orisinal",
  "variasi_cara": "angka" | "konteks" | null,
  "acuan": {...},
  "cognitive_c": "C1".."C6", "jumlah_langkah": 1..8, "jenis_soal": "label singkat jenis soal",
  "alasan_level": "satu kalimat",
  "stimulus": null | "data/tabel Markdown yang dibutuhkan soal",
  "pertanyaan": "...", "jawaban_benar": "...", "alasan_benar": "...",
  "distraktor": [{"teks": "...", "alasan": "kesalahan siswa yang ditiru"}, x3],
  "pembahasan": "...", "catatan": null
} ]}
Bentuk acuan:
- variasi dari pretest : {"sumber":"pretest","id":"<id pretest persis>"}
- variasi dari buku    : {"sumber":"siswa","halaman":<nomor HALAMAN>,"bagian":"...","nomor":"...","teks":"<soal asal, salin PERSIS dari halaman>","jawaban":"..."}
- orisinal             : {"sumber":"siswa","halaman":<nomor HALAMAN>,"kutipan":"<potongan materi, salin PERSIS dari halaman, kalimat polos tanpa markup>"}
Jangan menulis "id" (diberi kode). Jangan menulis posisi opsi A-D (diacak kode)."""


FORMAT_GAMBAR = """Tambahan format untuk soal BERGAMBAR (setiap soal WAJIB):
  "gambar": ["<path gambar persis seperti diberikan, mis. img/xxx.png>", ...]  (hanya dari daftar gambar tersedia),
  "deskripsi_gambar": "fakta yang kamu baca dari gambar: semua angka, label, bentuk, urutan (1-3 kalimat)",
Acuan soal bergambar: variasi dari soal pretest pemilik gambar ({"sumber":"pretest","id":"<id>"}, variasi_cara
"konteks") ATAU orisinal (kutipan materi dari halaman buku)."""

ATURAN_GAMBAR = """# PENGGANTI aturan harga mati no.4 dan keterangan "tanpa gambar" (berlaku untuk tugas ini)
Soal ini BERGAMBAR: siswa melihat gambar yang kamu lampirkan. Kamu boleh menulis "perhatikan gambar" dan
memakai data di gambar, tetapi:
- Jawaban benar HARUS bisa ditentukan dari gambar + kalimat soal; baca gambar dengan teliti (angka, label, jumlah objek).
- Kalau gambar tidak terbaca jelas atau ambigu, JANGAN buat soalnya.
- Jangan membuat soal yang jawabannya sudah tertulis di gambar secara harfiah kecuali tingkat easy.
- Satu gambar boleh untuk beberapa soal, tetapi sudut pertanyaannya HARUS berbeda dan jawabannya berbeda dari soal pretest pemilik gambar.
- Tulis juga datanya penting di deskripsi_gambar; solver TIDAK melihat deskripsi itu, hanya gambar."""


def _short(text: str, n: int = 160) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[: n - 1] + "…"


def _acuan_terpakai(soal: List[Soal]) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for s in soal:
        if s.tipe_generate == "variasi":
            k = acuan_key(s.acuan.model_dump())
            out[k] = out.get(k, 0) + 1
    return out


@dataclass
class Job:
    book: str
    bab_no: int
    subbab: str
    level: str
    batch: int = 1
    out_root: str = C.OUT_ROOT
    gambar: bool = False

    @property
    def path(self) -> str:
        return os.path.join(self.out_root, self.book, f"batch{self.batch:02d}", f"bab{self.bab_no:02d}",
                            f"{self.subbab}_{self.level}{'_gambar' if self.gambar else ''}.json")

    @property
    def id_prefix(self) -> str:
        return f"{self.book}-b{self.bab_no:02d}-{self.subbab.lower()}-{self.level}-bt{self.batch:02d}-{'g' if self.gambar else ''}"


@dataclass
class Result:
    path: str
    accepted: int
    kuota: int
    rounds: int
    errors: List[str]
    warnings: List[str]
    tokens_in: int = 0
    tokens_out: int = 0
    seconds: float = 0.0

    @property
    def lolos(self) -> bool:
        return not self.errors


class _Context:
    def __init__(self, job: Job):
        self.job = job
        self.book = get_book(job.book)
        self.kuota = C.KUOTA_GAMBAR_MAKS if job.gambar else C.KUOTA_PER_LEVEL[self.book.jenjang]
        self.spec = C.LEVEL_SPEC[job.level]
        bab = kurikulum.get(job.book, job.bab_no)
        if not bab:
            raise GenerateError(f"bab {job.book} no.{job.bab_no} tidak ada")
        self.bab = bab
        self.subbab_nama = bab.subbab_nama(job.subbab)
        if self.subbab_nama is None:
            raise GenerateError(f"subbab {job.subbab} tidak ada di {bab.bab_id}")
        self.p0, self.p1 = subbab_pages(job.book, job.bab_no, job.subbab)
        self.materi = "\n\n".join(
            f"=== HALAMAN {p} ===\n{page_text(job.book, p)}" for p in range(self.p0, self.p1 + 1))
        pretest = load_pretest(job.book)
        self.pretest = [r for r in pretest.values() if r.bab_no == job.bab_no and r.subbab == job.subbab]
        self.sudah = load_exercise(job.book, job.bab_no, job.subbab, exclude=job.path)
        self.target_variasi = round(C.PORSI_VARIASI[job.level] * self.kuota)
        self.rules = _load_rules()
        self.pool_gambar: List[Dict[str, Any]] = []
        if job.gambar:
            self.pool_gambar = _pool_gambar(job)
            if not self.pool_gambar:
                raise GenerateError(f"subbab {job.subbab} bab {job.bab_no} {job.book} tidak punya soal pretest "
                                    f"bergambar dengan berkas gambar yang ada")
            n_img = len({g for it in self.pool_gambar for g in it["gambar"]})
            self.kuota = min(self.kuota, n_img * C.MAKS_PAKAI_GAMBAR)

    def pilih_gambar(self, accepted: List[Soal]) -> List[Dict[str, Any]]:
        """Soal pretest pemilik gambar yang gambarnya paling jarang terpakai (maks MAKS_GAMBAR_PER_PANGGILAN gambar)."""
        pakai: Dict[str, int] = {}
        for s in accepted:
            for g in s.gambar:
                pakai[g] = pakai.get(g, 0) + 1
        ada = [it for it in self.pool_gambar if any(pakai.get(g, 0) < C.MAKS_PAKAI_GAMBAR for g in it["gambar"])]
        ada.sort(key=lambda it: sum(pakai.get(g, 0) for g in it["gambar"]))
        out, total = [], 0
        for it in ada:
            if total + len(it["gambar"]) > MAKS_GAMBAR_PER_PANGGILAN and out:
                continue
            out.append(it)
            total += len(it["gambar"])
        return out

    def prompt(self, need: int, var_left: int, accepted: List[Soal], umpan_balik: List[str],
               gambar_ditawarkan: Optional[List[Dict[str, Any]]] = None) -> str:
        j = self.job
        lo, hi = self.spec["langkah"]
        if j.gambar:
            return self._prompt_gambar(need, accepted, umpan_balik, gambar_ditawarkan or [])
        parts = [
            f"# Tugas\nTulis {need} soal BARU untuk {self.bab.nama} (bab {j.bab_no}), subbab {j.subbab}. "
            f"{self.subbab_nama}, level **{j.level}** ({self.book.jenjang}, kelas {j.book}).",
            f"Level {j.level}: cognitive_c {'/'.join(self.spec['c'])}, jumlah_langkah {lo}-{hi}. "
            f"Kuota level {self.kuota} soal; target variasi total {self.target_variasi}. "
            f"Dari {need} soal ini, TEPAT {var_left} bertipe variasi (sisanya orisinal). "
            f"Jumlah itu wajib: porsi variasi satu level dicek validator. Jangan melabeli soal sebagai variasi "
            f"kecuali benar-benar meniru soal acuan.",
            "# Aturan penulisan\n" + self.rules,
            "# " + FORMAT,
            f"# Materi Buku Siswa subbab ini (halaman {self.p0}-{self.p1}; nomor halaman = angka pada === HALAMAN ===)\n"
            + self.materi,
        ]
        if self.pretest:
            parts.append("# Soal pretest subbab ini (acuan variasi sumber 'pretest')\n" + "\n".join(
                f"- id: {r.id}\n  soal: {_short(r.teks, 600)}\n  jawaban: {_short(r.jawaban, 120)}" for r in self.pretest))
        else:
            parts.append("# Soal pretest subbab ini\n(tidak ada; acuan variasi harus dari buku)")
        if self.sudah:
            parts.append("# Soal yang SUDAH ada (batch/level lain): jangan kembar, jangan pakai ulang acuan yang sama\n"
                         + "\n".join(f"- {_short(r.teks)} => {_short(r.jawaban, 40)}" for r in self.sudah))
        terpakai = _acuan_terpakai(accepted)
        if terpakai:
            parts.append(f"# Acuan variasi yang SUDAH terpakai di level ini (maks {C.MAKS_VARIASI_PER_ACUAN}x per acuan; "
                         "yang sudah penuh JANGAN dipakai lagi, cari soal Contoh/Latihan lain di halaman buku)\n"
                         + "\n".join(f"- {k}: {n}x" for k, n in terpakai.items()))
        if accepted:
            parts.append("# Soal yang sudah kamu tulis dan diterima di level ini (jangan mengulang pola/jenis/jawaban)\n"
                         + "\n".join(f"- [{s.jenis_soal}] {_short(soal_text(s.stimulus, s.pertanyaan))} => "
                                     f"{_short(s.jawaban_benar, 40)}" for s in accepted))
        if umpan_balik:
            parts.append("# Soal putaran lalu yang DITOLAK validator; perbaiki, jangan ulangi kesalahannya\n"
                         + "\n".join(f"- {e}" for e in umpan_balik))
        return "\n\n".join(parts)


def _prompt_gambar(self: "_Context", need: int, accepted: List[Soal], umpan_balik: List[str],
                   ditawarkan: List[Dict[str, Any]]) -> str:
    j = self.job
    lo, hi = self.spec["langkah"]
    parts = [
        f"# Tugas\nTulis {need} soal BERGAMBAR BARU untuk {self.bab.nama} (bab {j.bab_no}), subbab {j.subbab}. "
        f"{self.subbab_nama}, level **{j.level}** ({self.book.jenjang}, kelas {j.book}). "
        f"Gambarnya dilampirkan setelah teks ini.",
        f"Level {j.level}: cognitive_c {'/'.join(self.spec['c'])}, jumlah_langkah {lo}-{hi}. "
        f"Maks {C.KUOTA_GAMBAR_MAKS} soal bergambar per level; satu gambar maks {C.MAKS_PAKAI_GAMBAR} soal.",
        "# Aturan penulisan\n" + self.rules,
        ATURAN_GAMBAR,
        "# " + FORMAT,
        FORMAT_GAMBAR,
        f"# Materi Buku Siswa subbab ini (halaman {self.p0}-{self.p1}; nomor halaman = angka pada === HALAMAN ===)\n"
        + self.materi,
        "# Gambar yang tersedia beserta soal pretest pemiliknya (pakai path gambar PERSIS)\n" + "\n".join(
            f"- gambar {it['gambar']} | id pretest: {it['id']}\n  soal: {_short(it['teks'], 400)}\n"
            f"  jawaban: {_short(it['jawaban'], 100)}" for it in ditawarkan),
    ]
    if self.sudah:
        parts.append("# Soal yang SUDAH ada (batch/level lain): jangan kembar\n"
                     + "\n".join(f"- {_short(r.teks)} => {_short(r.jawaban, 40)}" for r in self.sudah))
    if accepted:
        parts.append("# Soal yang sudah kamu tulis dan diterima di level ini (jangan mengulang sudut/jawaban)\n"
                     + "\n".join(f"- {s.gambar} [{s.jenis_soal}] {_short(soal_text(s.stimulus, s.pertanyaan))} => "
                                 f"{_short(s.jawaban_benar, 40)}" for s in accepted))
    if umpan_balik:
        parts.append("# Soal putaran lalu yang DITOLAK; perbaiki, jangan ulangi kesalahannya\n"
                     + "\n".join(f"- {e}" for e in umpan_balik))
    return "\n\n".join(parts)


def _pool_gambar(job: Job) -> List[Dict[str, Any]]:
    """Soal pretest bergambar di subbab ini yang berkas gambarnya ada: [{id, teks, jawaban, gambar[]}]."""
    path = os.path.join(PRETEST_ROOT, job.book, f"bab{job.bab_no:02d}.json")
    out: List[Dict[str, Any]] = []
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        for s in json.load(f).get("soal", []):
            refs = [g for g in (s.get("image_refs") or []) if os.path.exists(gambar_path(job.book, g))]
            if s.get("subbab") == job.subbab and s.get("butuh_gambar") and refs:
                out.append({"id": s["id"], "teks": soal_text(s.get("stimulus"), s["pertanyaan"]),
                            "jawaban": s["jawaban_benar"], "gambar": refs})
    return out


def _gambar_messages(prompt: str, ditawarkan: List[Dict[str, Any]], job: Job) -> List[Dict[str, Any]]:
    content: List[Dict[str, Any]] = [{"type": "text", "text": prompt}]
    for it in ditawarkan:
        for g in it["gambar"]:
            content.append({"type": "text", "text": f"Gambar `{g}` (milik soal pretest {it['id']}):"})
            content.append(image_part(gambar_path(job.book, g)))
    return [{"role": "system", "content": SYSTEM}, {"role": "user", "content": content}]


_Context._prompt_gambar = _prompt_gambar  # type: ignore[attr-defined]

# --------------------------------------------------------------------------- inti

def _extract_json(text: str) -> Any:
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    if fence:
        text = fence.group(1).strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("tidak ada objek JSON di balasan")
    return json.loads(text[start:end + 1])


def _write(job: Job, generator: str, soal: List[Soal], kapasitas_kurang: bool = False,
           alasan: Optional[str] = None) -> None:
    data = ExerciseFile(book=job.book, bab_no=job.bab_no, subbab=job.subbab, level=job.level,  # type: ignore[arg-type]
                        batch=job.batch, skill_versi=C.SKILL_VERSI, generator=generator,
                        kapasitas_kurang=kapasitas_kurang, alasan_kapasitas=alasan, soal=soal,
                        bergambar=job.gambar)
    os.makedirs(os.path.dirname(job.path), exist_ok=True)
    tmp = job.path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data.model_dump(), f, ensure_ascii=False, indent=2)
    os.replace(tmp, job.path)


def _log(job: Job, entry: dict) -> None:
    os.makedirs(os.path.dirname(job.path), exist_ok=True)
    with open(job.path.replace(".json", ".runlog.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _next_number(accepted: List[Soal]) -> int:
    return max((int(s.id.rsplit("-", 1)[1].lstrip("g")) for s in accepted), default=0) + 1


def generate(job: Job, client: NineRouterClient, *, progress=print) -> Result:
    started = time.monotonic()
    ctx = _Context(job)
    generator = f"9router:{client.settings.model}"
    accepted: List[Soal] = []
    umpan: List[str] = []
    tok_in = tok_out = 0
    max_rounds = math.ceil(ctx.kuota / CHUNK) + MAX_ROUNDS_EXTRA
    rounds = 0

    # lanjutkan HANYA file milik pipeline ini dengan model yang sama; file agen/manual tidak pernah disentuh
    if os.path.exists(job.path):
        with open(job.path, encoding="utf-8") as f:
            existing = ExerciseFile.model_validate(json.load(f))
        if existing.generator != generator:
            raise GenerateError(f"{job.path} sudah ada (generator: {existing.generator or 'tidak tercatat'}); "
                                f"tidak ditimpa. Pakai --batch baru atau hapus manual.")
        accepted = existing.soal

    while len(accepted) < ctx.kuota and rounds < max_rounds:
        rounds += 1
        need = min(CHUNK, ctx.kuota - len(accepted))
        n_var = sum(1 for s in accepted if s.tipe_generate == "variasi")
        remaining = ctx.kuota - len(accepted)
        butuh = max(0, ctx.target_variasi - n_var)          # variasi yang masih diperlukan di level ini
        var_left = min(need, butuh) if need >= remaining else min(need, round(butuh * need / remaining))
        ditawarkan = ctx.pilih_gambar(accepted) if job.gambar else []
        if job.gambar and not ditawarkan:
            break                       # semua gambar sudah terpakai penuh
        prompt = ctx.prompt(need, var_left, accepted, umpan, ditawarkan)
        messages = (_gambar_messages(prompt, ditawarkan, job) if job.gambar
                    else [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}])
        res = None
        try:
            res = client.chat(messages, max_output_tokens=GEN_MAX_TOKENS, json_mode=True)
            tok_in += res.input_tokens or 0
            tok_out += res.output_tokens or 0
            if res.finish_reason == "length":
                raise ValueError(f"balasan terpotong (finish_reason=length, {res.output_tokens} token keluar); "
                                 f"naikkan GEN_MAX_TOKENS atau kecilkan CHUNK")
            raw = _extract_json(res.text)["soal"]
        except (NineRouterError, ValueError, KeyError, TypeError) as exc:
            umpan = [f"putaran sebelumnya gagal dibaca: {_short(str(exc), 200)}"]
            _log(job, {"round": rounds, "error": str(exc),
                       "balasan_awal": res.text[:1500] if res else None,
                       "balasan_akhir": res.text[-400:] if res else None})
            progress(f"  putaran {rounds}: GAGAL ({_short(str(exc), 120)})")
            continue

        # skema per soal -> id -> validasi mekanis per soal
        n = _next_number(accepted)
        candidates: List[Soal] = []
        umpan = []
        for item in raw:
            if not isinstance(item, dict):
                continue
            item = {**item, "id": f"{job.id_prefix}{n:03d}"}
            try:
                candidates.append(Soal.model_validate(item))
                n += 1
            except ValidationError as exc:
                umpan.append(f"{_short(str(item.get('pertanyaan', '?')), 70)}: skema: "
                             f"{'; '.join(e['msg'] for e in exc.errors())[:200]}")
        pakai = _acuan_terpakai(accepted)
        tersaring: List[Soal] = []
        for s in candidates:
            if s.tipe_generate == "variasi":
                k = acuan_key(s.acuan.model_dump())
                if pakai.get(k, 0) >= C.MAKS_VARIASI_PER_ACUAN:
                    umpan.append(f"{_short(soal_text(s.stimulus, s.pertanyaan), 80)} -> acuan {k} sudah dipakai "
                                 f"{C.MAKS_VARIASI_PER_ACUAN}x; pilih acuan lain atau tulis orisinal")
                    continue
                pakai[k] = pakai.get(k, 0) + 1
            tersaring.append(s)
        if job.gambar:
            boleh = {g for it in ditawarkan for g in it["gambar"]}
            pakai_g: Dict[str, int] = {}
            for s in accepted:
                for g in s.gambar:
                    pakai_g[g] = pakai_g.get(g, 0) + 1
            ok_g: List[Soal] = []
            for s in candidates:
                if not s.gambar or any(g not in boleh or pakai_g.get(g, 0) >= C.MAKS_PAKAI_GAMBAR for g in s.gambar):
                    umpan.append(f"{_short(soal_text(s.stimulus, s.pertanyaan), 80)} -> gambar harus dari daftar tersedia "
                                 f"dan belum terpakai {C.MAKS_PAKAI_GAMBAR}x: {s.gambar}")
                    continue
                for g in s.gambar:
                    pakai_g[g] = pakai_g.get(g, 0) + 1
                ok_g.append(s)
            candidates = ok_g
            tersaring = [s for s in tersaring if s in ok_g]
        n_skema = len(raw) - len(candidates)
        n_saring = len(candidates) - len(tersaring)
        candidates = tersaring
        _write(job, generator, accepted + candidates)
        _data, errors, warns = validate_file(job.path, partial=True)
        bad: Dict[str, List[str]] = {}
        for e in errors:
            for s in candidates:
                if s.id in e:
                    bad.setdefault(s.id, []).append(e.split(s.id, 1)[-1].lstrip(": ")[:220])
        lolos = [s for s in candidates if s.id not in bad]
        for s in candidates:
            if s.id in bad:
                umpan.append(f"{_short(soal_text(s.stimulus, s.pertanyaan), 80)} -> " + " | ".join(bad[s.id]))
        # galat tingkat-file yang tak terkait soal tertentu: laporkan saja
        unattributed = [e for e in errors if not any(s.id in e for s in candidates)]
        accepted = accepted + lolos
        # rapikan id berurutan agar tidak berlubang setelah soal dibuang
        accepted = [s.model_copy(update={"id": f"{job.id_prefix}{i:03d}"}) for i, s in enumerate(accepted, 1)]
        _write(job, generator, accepted)
        _log(job, {"round": rounds, "diminta": need, "diterima": len(lolos), "ditolak": len(candidates) - len(lolos) + n_saring,
                   "skema_gagal": n_skema, "model": res.model, "token_in": res.input_tokens,
                   "token_out": res.output_tokens, "detik": res.latency_seconds, "finish": res.finish_reason, "umpan_balik": umpan,
                   "galat_file": unattributed})
        progress(f"  putaran {rounds}: diminta {need}, diterima {len(lolos)}, "
                 f"ditolak {len(candidates) - len(lolos) + n_saring}, skema gagal {n_skema} "
                 f"({res.latency_seconds}s, {res.input_tokens}/{res.output_tokens} token)")

    kurang = (len(accepted) < ctx.kuota) and not job.gambar
    if accepted:
        _write(job, generator, accepted, kapasitas_kurang=kurang,
               alasan=(f"generator otomatis hanya memperoleh {len(accepted)} soal lolos validator setelah "
                       f"{rounds} putaran; belum ditinjau apakah bahan subbab memang tidak cukup") if kurang else None)
    else:
        raise GenerateError("tidak ada soal yang lolos validator")
    _data, errors, warns = validate_file(job.path, partial=False)
    return Result(job.path, len(accepted), ctx.kuota, rounds, errors, warns, tok_in, tok_out,
                  round(time.monotonic() - started, 1))
