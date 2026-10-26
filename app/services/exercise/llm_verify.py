"""
llm_verify.py -- verifikasi BUTA lewat 9Router: model solver (keluarga berbeda dari generator) mengerjakan
soal tanpa kunci; hasilnya dicocokkan dengan kunci generator memakai verify.compare.

Berkas yang dibaca/ditulis sama dengan jalur manual (agen penyelesai-soal-exercise):
  <K>_<level>.blind.json      soal + opsi tanpa kunci/alasan/pembahasan/level  (verify.prepare)
  <K>_<level>.solver.json     {"model": ..., "jawaban": {id: {pilihan, langkah, catatan}}}
  <K>_<level>.verifikasi.json cocok/tidak per soal                              (verify.compare)
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from typing import Any, Dict, List

from app.llm.ninerouter import NineRouterClient, NineRouterError, image_part
from app.services.exercise.refs import gambar_path
from app.services.exercise import verify

CHUNK = 8
CHUNK_GAMBAR = 4
RETRIES = 1

SYSTEM = """Kamu siswa penyelesai soal yang teliti dan independen.
Kerjakan setiap soal pilihan ganda DARI NOL (hitung/telusuri sendiri, jangan menebak dari bentuk opsi).
TULIS PENGERJAANMU di "kerja" SEBELUM memilih (substitusi angka, hitung, periksa ulang hasilnya).
Pilih tepat satu opsi A-D yang cocok dengan hasilmu. Kalau tidak ada opsi yang benar, atau lebih dari satu
opsi yang benar, tulis "pilihan": null dan jelaskan singkat di "catatan". "langkah" = jumlah langkah
penyelesaian MINIMAL yang kamu butuhkan (bilangan bulat >= 1).
Balas HANYA JSON valid, urutan kunci wajib kerja -> pilihan:
{"jawaban": {"<id soal>": {"kerja": "...", "pilihan": "B", "langkah": 2, "catatan": null}, ...}}
Satu entri untuk setiap id soal yang diberikan.
Sebagian soal disertai gambar (dilampirkan setelah daftar soal, diberi label id soal): bacalah gambarnya
teliti dan jawablah berdasarkan gambar itu. Kalau gambar tidak cukup jelas untuk menjawab, tulis "pilihan": null."""


@dataclass
class VerifyResult:
    cocok: int
    total: int
    tidak_cocok: List[str]
    tidak_terjawab: List[str]
    tokens_in: int
    tokens_out: int
    seconds: float
    solver_path: str
    verifikasi_path: str


def _extract_json(text: str) -> Any:
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    if fence:
        text = fence.group(1).strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("tidak ada objek JSON di balasan")
    return json.loads(text[start:end + 1])


def _ask(client: NineRouterClient, model: str, soal: List[dict], book: str = "",
         system: str = SYSTEM) -> Dict[str, dict]:
    ids = [s["id"] for s in soal]
    prompt = "Soal yang harus dikerjakan (id harus persis sama di balasan):\n" + json.dumps(
        [{k: v for k, v in s.items() if k != "gambar"} for s in soal], ensure_ascii=False, indent=1)
    content: Any = prompt
    if any(s.get("gambar") for s in soal):
        content = [{"type": "text", "text": prompt}]
        for s in soal:
            for g in s.get("gambar") or []:
                content.append({"type": "text", "text": f"Gambar untuk soal {s['id']}:"})
                content.append(image_part(gambar_path(book, g)))
    res = client.chat([{"role": "system", "content": system}, {"role": "user", "content": content}],
                      model=model, temperature=0.0, json_mode=True)
    jawab = _extract_json(res.text)["jawaban"]
    out = {i: jawab[i] for i in ids if isinstance(jawab.get(i), dict)}
    out["__usage__"] = {"in": res.input_tokens or 0, "out": res.output_tokens or 0}  # type: ignore[assignment]
    return out


def verifikasi_buta(path: str, client: NineRouterClient, model: str, *, progress=print) -> VerifyResult:
    started = time.monotonic()
    blind_path = verify.prepare(path)
    with open(blind_path, encoding="utf-8") as f:
        blind = json.load(f)["soal"]

    with open(path, encoding="utf-8") as f:
        book = json.load(f)["book"]
    ukuran = CHUNK_GAMBAR if any(s.get("gambar") for s in blind) else CHUNK
    jawaban: Dict[str, dict] = {}
    tok_in = tok_out = 0
    for i in range(0, len(blind), ukuran):
        chunk = blind[i:i + ukuran]
        for attempt in range(RETRIES + 1):
            try:
                got = _ask(client, model, chunk, book)
                usage = got.pop("__usage__")
                tok_in += usage["in"]  # type: ignore[index]
                tok_out += usage["out"]  # type: ignore[index]
                jawaban.update(got)
                break
            except (NineRouterError, ValueError, KeyError, TypeError) as exc:
                progress(f"  solver soal {i + 1}-{i + len(chunk)} percobaan {attempt + 1} gagal: {str(exc)[:120]}")
        progress(f"  solver: {min(i + ukuran, len(blind))}/{len(blind)} soal dikerjakan")

    solver_path = path[:-len(".json")] + ".solver.json"
    with open(solver_path, "w", encoding="utf-8") as f:
        json.dump({"model": model, "jawaban": jawaban}, f, ensure_ascii=False, indent=2)
    hasil = verify.compare(path)
    ver_path = path[:-len(".json")] + ".verifikasi.json"
    tidak_cocok = [k for k, v in hasil.items() if not v["cocok"] and v["pilihan_solver"] is not None]
    tidak_terjawab = [k for k, v in hasil.items() if v["pilihan_solver"] is None]
    return VerifyResult(sum(1 for v in hasil.values() if v["cocok"]), len(hasil), tidak_cocok, tidak_terjawab,
                        tok_in, tok_out, round(time.monotonic() - started, 1), solver_path, ver_path)


SYSTEM_TANPA_GAMBAR = SYSTEM.split("Sebagian soal disertai gambar")[0] + """Soal-soal ini aslinya disertai gambar, tetapi gambarnya TIDAK diberikan kepadamu.
Kerjakan hanya dari teks. Kalau jawabannya tidak dapat ditentukan tanpa gambar, tulis "pilihan": null
(jangan menebak)."""


@dataclass
class CekGambarResult:
    total: int
    tanpa_gambar_cocok: List[str]      # tetap benar tanpa gambar -> gambar kemungkinan hiasan
    butuh_gambar: List[str]            # null atau salah tanpa gambar -> gambar memang dibutuhkan
    path: str


def cek_butuh_gambar(path: str, client: NineRouterClient, model: str, *, progress=print) -> CekGambarResult:
    """Solver mengerjakan soal bergambar TANPA gambar. Soal yang tetap cocok dengan kunci = tidak butuh gambar."""
    from app.services.exercise.options import susun
    from app.services.exercise.schema import ExerciseFile

    with open(path, encoding="utf-8") as f:
        data = ExerciseFile.model_validate(json.load(f))
    if not data.bergambar:
        raise ValueError("berkas ini bukan berkas bergambar")
    kunci = {sid: v[1] for sid, v in susun(data).items()}
    blind_path = verify.prepare(path)
    with open(blind_path, encoding="utf-8") as f:
        blind = [{k: v for k, v in s.items() if k != "gambar"} for s in json.load(f)["soal"]]
    jawaban: Dict[str, dict] = {}
    for i in range(0, len(blind), CHUNK):
        got = _ask(client, model, blind[i:i + CHUNK], data.book, SYSTEM_TANPA_GAMBAR)
        got.pop("__usage__", None)
        jawaban.update(got)
        progress(f"  tanpa gambar: {min(i + CHUNK, len(blind))}/{len(blind)} soal dikerjakan")
    hiasan = [sid for sid, k in kunci.items() if (jawaban.get(sid) or {}).get("pilihan") == k]
    butuh = [sid for sid in kunci if sid not in hiasan]
    out = path[:-len(".json")] + ".tanpagambar.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"model": model, "tanpa_gambar_cocok": hiasan, "butuh_gambar": butuh, "jawaban": jawaban},
                  f, ensure_ascii=False, indent=2)
    return CekGambarResult(len(kunci), hiasan, butuh, out)
