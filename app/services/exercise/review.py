"""
review.py -- turunan per subbab dari hasil export: file JSON (kolom tabel `soal`) dan lembar koreksi Markdown.

File ini HANYA turunan. Koreksi soal dilakukan di file kerja (<KODE>_<level>.json), lalu export dijalankan ulang;
file di per_subbab/ selalu ditulis ulang dari data yang sama dan akan menimpa suntingan manual.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from typing import Dict, List

from app.services.exercise import config as C

_URUT_LEVEL = {lv: i for i, lv in enumerate(C.LEVELS)}
_LABEL = {"variasi": "variasi", "orisinal": "orisinal"}


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")


def _blok(i: int, row: dict, m: dict) -> str:
    tanda = []
    if m.get("dipaksa_kuota"):
        tanda.append("DIPAKSA KUOTA")
    if m.get("warning"):
        tanda.append("warning validator")
    judul = f"### {i}. [{m['level_target']}] {m['id']}"
    info = (f"{m['tipe_generate']}"
            f"{' (' + m['variasi_cara'] + ')' if m.get('variasi_cara') else ''} | {m['cognitive_c']} | "
            f"{m['jumlah_langkah']} langkah | jenis: {m.get('jenis_soal') or '-'}")
    out = [judul, f"*{info}*" + (f"  **[{'; '.join(tanda)}]**" if tanda else ""), "", row["soal_text"], ""]
    for o in row["options"]:
        benar = o["option_id"] == row["jawaban"]
        out.append(f"- {'**' if benar else ''}{o['option_id']}. {o['text']}{'** ✅' if benar else ''}  \n  <sub>{o['alasan']}</sub>")
    out += ["", f"**Pembahasan:** {m['pembahasan']}"]
    a = m["acuan"]
    ref = a.get("id") or f"{a.get('sumber')} hal.{a.get('halaman')} {a.get('bagian') or ''}".strip()
    out.append(f"**Acuan:** {a['sumber']} — {ref}")
    if m.get("catatan"):
        out.append(f"**Catatan generator:** {m['catatan']}")
    for w in m.get("warning") or []:
        out.append(f"**Warning:** {w}")
    out += ["", "Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: ", "", "---", ""]
    return "\n".join(out)


def tulis_per_subbab(base: str, book: str, rows: List[dict], meta: Dict[str, dict]) -> int:
    """Tulis per_subbab/bab<NN>_<K>_<slug>.json + .md. Return jumlah subbab."""
    out_dir = os.path.join(base, "per_subbab")
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)   # turunan murni: bersihkan agar subbab yang dihapus tidak tertinggal
    os.makedirs(out_dir)
    grup: Dict[tuple, List[dict]] = {}
    for r in rows:
        m = meta[r["_id"]]
        grup.setdefault((m["bab_id"], m["subbab_kode"], r["subbab_id"]), []).append(r)
    for (bab_id, kode, nama), items in sorted(grup.items(), key=lambda kv: (int(kv[0][0].split("-B")[1]), kv[0][1])):
        items.sort(key=lambda r: (_URUT_LEVEL[meta[r["_id"]]["level_target"]], meta[r["_id"]]["id"]))
        bab_no = int(bab_id.split("-B")[1])
        stem = f"bab{bab_no:02d}_{kode}_{_slug(nama)}"
        with open(os.path.join(out_dir, stem + ".json"), "w", encoding="utf-8") as f:
            json.dump({"book": book, "bab_id": bab_id, "subbab": nama, "jumlah": len(items), "items": items},
                      f, ensure_ascii=False, indent=2)
        hitung = {lv: sum(1 for r in items if meta[r["_id"]]["level_target"] == lv) for lv in C.LEVELS}
        tipe = {t: sum(1 for r in items if meta[r["_id"]]["tipe_generate"] == t) for t in _LABEL}
        n_paksa = sum(1 for r in items if meta[r["_id"]].get("dipaksa_kuota"))
        kurang = {}
        for r in items:
            k = meta[r["_id"]].get("kapasitas_kurang")
            if k:
                kurang[meta[r["_id"]]["level_target"]] = k
        md = [f"# Lembar koreksi — {book} {bab_id} subbab {kode}: {nama}", "",
              f"{len(items)} soal | " + ", ".join(f"{lv} {n}" for lv, n in hitung.items()) +
              " | " + ", ".join(f"{t} {n}" for t, n in tipe.items()) +
              (f" | dipaksa kuota {n_paksa}" if n_paksa else ""),
              ] + [f"> **Kapasitas kurang ({lv}): {k['jumlah']} dari kuota {k['kuota']}** — {k['alasan']}"
                   for lv, k in kurang.items()] + [
              "", "> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.", "", "---", ""]
        md += [_blok(i, r, meta[r["_id"]]) for i, r in enumerate(items, 1)]
        with open(os.path.join(out_dir, stem + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(md))
    return len(grup)


def tulis_readme(base: str, book: str, batch: int, rows: List[dict], meta: Dict[str, dict]) -> None:
    """README serah-terima batch: isi file, penanda, prior kesulitan, dan aturan pemakaian."""
    from collections import Counter
    per = Counter((meta[r["_id"]]["bab_id"], meta[r["_id"]]["subbab_kode"], r["subbab_id"], meta[r["_id"]]["level_target"]) for r in rows)
    kurang = {(k[0], k[1], k[3]): meta[r["_id"]]["kapasitas_kurang"] for r in rows
              for k in [(meta[r["_id"]]["bab_id"], meta[r["_id"]]["subbab_kode"], r["subbab_id"], meta[r["_id"]]["level_target"])]
              if meta[r["_id"]].get("kapasitas_kurang")}
    n_paksa = sum(1 for m in meta.values() if m.get("dipaksa_kuota"))
    versi = Counter(m.get("skill_versi", "pra-v1") for m in meta.values())
    L = [f"# Serah-terima batch {batch:02d} — {book}", "",
         f"Total **{len(rows)} soal**, pipeline `{C.PIPELINE_VERSION}`, skill: " + ", ".join(f"{v} ({n})" for v, n in versi.items()), "",
         "## File", "",
         "| File | Isi |", "|---|---|",
         "| `soal_exercise_db.json` | **Master.** Baris tabel `soal`; input validasi dan insert. `cognitive_level`, `cognitive_score`, `confidence_score`, `status` sengaja `null`. |",
         "| `soal_exercise_meta.json` | Info pendamping per `_id` (level target, tipe, acuan, pembahasan, penanda). Bawa bersama master. |",
         "| `per_subbab/*.md`, `*.json` | Turunan untuk koreksi manusia, satu subbab per file (3 level × kuota). Jangan disunting. |", "",
         "## Prior kesulitan (untuk kalibrasi IRT)", "",
         "Level easy/medium/hard hanya **perkiraan awal**. Field di meta yang bisa dipakai sebagai prior yang lebih halus:",
         "`level_target`, `cognitive_c` (C1–C6), `jumlah_langkah`, `cognitive_score_target` (600/1000/1400).", "",
         "Catatan untuk kalibrasi:",
         "- Kunci jawaban **belum diverifikasi pihak independen** (dikerjakan dua kali oleh generator sendiri). Soal berkunci salah/ambigu akan terlihat",
         "  sulit karena banyak dijawab salah: gunakan **daya beda** (point-biserial / parameter *a*) agar soal berdaya beda rendah/negatif masuk",
         "  antrean tinjau manusia, bukan otomatis dijadikan hard.",
         "- Pindahkan level hanya setelah jumlah jawaban per soal cukup, dan beri jeda agar label tidak bolak-balik.",
         "- Hard di sini sering setara medium atas (kesulitan dari penalaran, bukan konsep baru), terutama SD dan SMA.", "",
         "## Penanda khusus", "",
         f"- `dipaksa_kuota` ({n_paksa} soal): soal tambahan agar kuota penuh saat bahan tipis; rentan nyaris kembar. Perlu perhatian ekstra.",
         f"- `kapasitas_kurang` ({len(kurang)} subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):", ""]
    for (bab, kode, lv), k in sorted(kurang.items()):
        L.append(f"  - {bab} subbab {kode} {lv}: {k['jumlah']}/{k['kuota']} — {k['alasan']}")
    if not kurang:
        L.append("  - (tidak ada)")
    L += ["", "## Ringkasan per subbab", "", "| Bab | Subbab | easy | medium | hard |", "|---|---|---|---|---|"]
    for (bab, kode, nama) in sorted({(k[0], k[1], k[2]) for k in per}, key=lambda t: (int(t[0].split("-B")[1]), t[1])):
        L.append(f"| {bab} | {kode}. {nama} | " + " | ".join(str(per.get((bab, kode, nama, lv), 0)) for lv in C.LEVELS) + " |")
    L += ["", "## Aturan pemakaian", "",
          "- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.",
          "- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).", ""]
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))
