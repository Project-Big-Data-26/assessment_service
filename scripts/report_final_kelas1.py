"""Render the complete per-question silver IndoBERT + Gemini audit report."""

from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "output/pretest/kelas1"
HEADS = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")
HEAD_NAMES = {
    "mathCognitiveDomain": "Domain kognitif matematika",
    "knowledgeDimension": "Dimensi pengetahuan",
    "intendedDifficulty": "Kesulitan yang dimaksud",
}


def load(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def md(value: object) -> str:
    text = "-" if value is None or value == "" else str(value)
    return text.replace("|", "\\|").replace("\n", "<br>")


def pct(value: float | None) -> str:
    return "-" if value is None else f"{100 * value:.2f}%"


def f4(value: float | None) -> str:
    return "-" if value is None else f"{value:.4f}"


def majority_fraction(aggregate: dict, head: str) -> str:
    data = aggregate.get("heads", {}).get(head, {})
    return f"{data.get('supportingRuns', 0)}/3"


def review_final(prediction: dict, aggregate: dict, head: str) -> tuple[str | None, str]:
    decision = aggregate.get(head) or {}
    if decision.get("status") != "consistent":
        return None, "needs_ai_review"
    action = decision.get("suggestedAction")
    if action == "confirm":
        return prediction[head].get("label"), "llm_confirm"
    if action == "revise":
        return decision.get("suggestedLabel"), "llm_revise"
    return None, "llm_abstain"


def structural_status(item: dict, base: Path) -> tuple[str, list[str]]:
    reasons: list[str] = []
    options = item.get("options") or []
    labels = [str(option.get("option_id") or "").strip() for option in options]
    texts = [str(option.get("text") or "").strip().casefold() for option in options]
    if not str(item.get("soal_text") or "").strip():
        reasons.append("stem_kosong")
    if len(options) < 2:
        reasons.append("opsi_kurang_dari_dua")
    if len(labels) != len(set(labels)):
        reasons.append("label_opsi_duplikat")
    if len(texts) != len(set(texts)):
        reasons.append("teks_opsi_identik")
    if str(item.get("jawaban") or "") not in labels:
        reasons.append("kunci_tidak_ada_di_opsi")
    missing = [ref for ref in item.get("image_url") or [] if not (base / ref).is_file()]
    if missing:
        reasons.append(f"aset_gambar_hilang={len(missing)}")
    return ("PASS" if not reasons else "REVIEW"), reasons


def run_label(run: dict, head: str) -> str:
    output = run.get("output") or {}
    value = output.get(head) or {}
    return f"{value.get('action', '-')}:{value.get('label') or '-'}"


def reviewed_label(run: dict, head: str, original: str | None) -> str:
    review = run.get("review") or {}
    value = review.get(head) or {}
    action = value.get("action", "-")
    label = original if action == "confirm" else value.get("proposedLabel")
    return f"{action}:{label or '-'}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=BASE / "soal_pretest_db.json")
    parser.add_argument(
        "--silver", type=Path, default=BASE / "silver_labels_gemini_3_5_flash_lite.json"
    )
    parser.add_argument("--snapshot", type=Path, default=BASE / "dataset_snapshot_silver.json")
    parser.add_argument("--predictions", type=Path, default=BASE / "indobert_predictions_silver.json")
    parser.add_argument(
        "--review", type=Path, default=BASE / "gemini_review_indobert_3_5_flash_lite.json"
    )
    parser.add_argument(
        "--output", type=Path, default=BASE / "HASIL_KATEGORISASI_DAN_VALIDASI_FIKS.md"
    )
    args = parser.parse_args()

    source = load(args.source)
    silver = load(args.silver)
    snapshot = load(args.snapshot)
    predictions_payload = load(args.predictions)
    review = load(args.review)
    sources = {str(item["_id"]): item for item in source}
    silver_items = silver["items"]
    rows = {row["questionId"]: row for row in snapshot["rows"]}
    predictions = {item["questionId"]: item for item in predictions_payload["items"]}
    review_items = review["items"]
    manifest = predictions_payload["model"]

    split_by_id = {
        entry["questionVersionId"].split(":silver-v1")[0]: entry["split"]
        for entry in snapshot["splitManifest"]
    }
    agreement = {head: [] for head in HEADS}
    confidences = {head: [] for head in HEADS}
    review_actions = {head: Counter() for head in HEADS}
    final_labels = {head: Counter() for head in HEADS}
    for qid, prediction_record in predictions.items():
        prediction = prediction_record["prediction"]
        aggregate = review_items[qid]["aggregate"]
        for head in HEADS:
            agreement[head].append(
                prediction[head]["label"] == prediction_record["silverLabels"][head]
            )
            confidences[head].append(prediction[head]["calibratedConfidence"])
            review_actions[head][(aggregate.get(head) or {}).get("suggestedAction") or "no_consensus"] += 1
            label, status = review_final(prediction, aggregate, head)
            final_labels[head][label or status] += 1

    lines: list[str] = []
    lines += [
        "# Hasil Kategorisasi dan Validasi Fiks — Bootstrap Silver Kelas 1",
        "",
        f"> Dibuat: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "> Status: **hasil eksperimen sementara (silver), bukan rujukan AI yang qualified dan belum layak dipakai sebagai klaim akurasi final.**",
        "",
        "## Ringkasan eksekusi",
        "",
        "Semua tahapan teknis yang dapat dijalankan tanpa data respons siswa telah dieksekusi: validasi deterministik, pelabelan awal Gemini N=3, pembuatan snapshot, fine-tuning LoRA IndoBERT 3×4×3, inferensi setiap soal, dan review Gemini N=3 terhadap prediksi IndoBERT. CTT dan IRT sengaja tidak dijalankan karena belum ada data respons siswa.",
        "",
        "| Komponen | Hasil aktual |",
        "|---|---|",
        f"| Sumber | `{args.source.relative_to(ROOT).as_posix()}` — {len(source)} soal |",
        f"| Silver teacher | Gemini `{silver['model']}`, {silver['requestedRuns']} run/soal, {silver['summary']['successfulRuns']} run sukses, {silver['summary']['failedRuns']} gagal |",
        f"| Token silver teacher | {silver['summary']['totalTokens']:,} total ({silver['summary']['promptTokens']:,} prompt + {silver['summary']['outputTokens']:,} output + {silver['summary']['thinkingTokens']:,} thinking) |",
        f"| Dataset training | `{snapshot['snapshotId']}` — {len(snapshot['rows'])} masuk, split {dict(Counter(entry['split'] for entry in snapshot['splitManifest']))} |",
        f"| IndoBERT | `{manifest['modelVersion']}`, base `{manifest['baseModel']}` revision `{manifest['baseRevision'][:12]}…`, LoRA rank {manifest['loraRank']} |",
        f"| Gemini reviewer | `{review['model']}`, {review['requestedRuns']} run/soal, {review['summary']['successfulRuns']} run sukses, {review['summary']['failedRuns']} gagal |",
        f"| Token Gemini reviewer | {review['summary']['totalTokens']:,} total ({review['summary']['promptTokens']:,} prompt + {review['summary']['outputTokens']:,} output + {review['summary']['thinkingTokens']:,} thinking) |",
        f"| Promotion | `approvedForProvisional={str(manifest['approvedForProvisional']).lower()}`; test gate `{snapshot['testUnlockStatus']}` |",
        "| CTT / IRT | Tidak dijalankan (tidak ada respons siswa) |",
        "",
        "## Arti angka dan urutan kerja",
        "",
        "1. **Gemini silver N=3** membaca soal (serta gambar bila ada) tiga kali secara terpisah. Label mayoritas minimal 2/3 menjadi target bootstrap. Angka 2/3 atau 3/3 adalah konsistensi vote, bukan confidence model dan bukan akurasi.",
        "2. **IndoBERT** menerima teks kanonis yang sama untuk training dan inferensi. Encoder IndoBERT bersama menghasilkan representasi, lalu tiga classification head menghasilkan logits. Temperature scaling validation mengubah logits menjadi probabilitas terkalibrasi.",
        "3. **Confidence IndoBERT** adalah probabilitas tertinggi pada suatu head: `confidence = max(P(label))`. Ini keyakinan model untuk satu soal, bukan ukuran benar-salah terhadap silver.",
        "4. **Normalized entropy** dihitung dengan `H = -Σ pᵢ ln(pᵢ) / ln(K)`, rentang 0–1. Makin kecil berarti distribusi makin tegas; makin besar berarti makin ambigu.",
        "5. **Gemini reviewer N=3** melihat soal dan distribusi probabilitas IndoBERT, lalu setiap run memilih `confirm`, `revise`, atau `abstain`. Mayoritas menghasilkan hasil validasi advisory; qualification silver diperlukan sebelum delivery.",
        "",
        "## Ringkasan hasil model",
        "",
        "| Head | Kesesuaian IndoBERT vs silver holdout/campuran* | Rata-rata confidence | Review confirm | Review revise | Review abstain/no consensus |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for head in HEADS:
        actions = review_actions[head]
        lines.append(
            f"| {HEAD_NAMES[head]} | {sum(agreement[head])}/{len(agreement[head])} ({pct(sum(agreement[head]) / len(agreement[head]))}) | "
            f"{pct(statistics.mean(confidences[head]))} | {actions['confirm']} | {actions['revise']} | {actions['abstain'] + actions['no_consensus']} |"
        )
    lines += [
        "",
        "\\* Kesesuaian ini dihitung terhadap silver label Gemini dan mencakup seluruh split, sehingga **bukan test accuracy terhadap AI**. Angka evaluasi validation di manifest juga hanya proxy terhadap label AI.",
        "",
        "### Gate data yang belum terpenuhi",
        "",
    ]
    for failure in snapshot.get("gateFailures") or []:
        lines.append(f"- `{failure}`")
    if not snapshot.get("gateFailures"):
        lines.append("- Tidak ada.")

    validation_metrics = manifest.get("metrics", {}).get("validation", {})
    lines += ["", "### Metrik validation selama training (pembanding silver)", "", "| Head | Macro-F1 |", "|---|---:|"]
    for head in HEADS:
        metric = validation_metrics.get(head, {}).get("macro avg", {}).get("f1-score")
        lines.append(f"| {HEAD_NAMES[head]} | {f4(metric)} |")
    lines += [
        "",
        "> Metrik di atas dipakai untuk memeriksa bahwa pipeline training benar-benar bekerja. Karena label target dibuat Gemini dan jumlah data kecil, metrik ini tidak boleh ditulis sebagai performa ilmiah final.",
        "",
        "## Hasil per soal",
        "",
    ]

    for ordinal, source_item in enumerate(source, start=1):
        qid = str(source_item["_id"])
        silver_record = silver_items.get(qid)
        row = rows.get(qid)
        prediction_record = predictions.get(qid)
        review_record = review_items.get(qid)
        deterministic, deterministic_reasons = structural_status(source_item, args.source.parent)
        lines += [
            f"## {ordinal}. Soal `{qid}`",
            "",
            f"**Soal:** {md(source_item.get('soal_text'))}",
            "",
            "| Opsi | Isi | Catatan ekstraksi |",
            "|---|---|---|",
        ]
        for option in source_item.get("options") or []:
            marker = " ✓" if option.get("option_id") == source_item.get("jawaban") else ""
            lines.append(
                f"| {md(option.get('option_id'))}{marker} | {md(option.get('text'))} | {md(option.get('alasan'))} |"
            )
        lines += [
            "",
            "### 1) Validasi input dan representasi",
            "",
            f"- Validasi deterministik: **{deterministic}**" + (f" — {', '.join(deterministic_reasons)}" if deterministic_reasons else ""),
            f"- Subtopik: {md(source_item.get('subbab_id'))}; tipe: {md(source_item.get('soal_type'))}; gambar: {len(source_item.get('image_url') or [])}",
            f"- Kunci sumber: `{md(source_item.get('jawaban'))}`; split: `{md(split_by_id.get(qid, 'excluded'))}`.",
        ]
        if not silver_record or not row or not prediction_record or not review_record:
            lines += ["- Soal tidak menyelesaikan seluruh pipeline; lihat checkpoint untuk alasan eksklusi.", ""]
            continue
        aggregate = silver_record["aggregate"]
        lines += [
            f"- KKO leksikal terdeteksi: {', '.join(f'`{value}`' for value in row.get('detectedKko') or []) or '-'} (fitur audit, bukan penentu label).",
            f"- Status konten Gemini silver: `{aggregate.get('contentStatus')}`; concern: {md('; '.join(aggregate.get('contentConcerns') or []) or '-')}",
            f"- Input IndoBERT: {prediction_record['untruncatedTokenCount']} token, batas {prediction_record['maxLength']}, truncation: `{str(prediction_record['wouldTruncate']).lower()}`.",
            "",
            "<details><summary>Teks kanonis yang masuk ke IndoBERT</summary>",
            "",
            "```text",
            prediction_record["serializedInput"],
            "```",
            "</details>",
            "",
            "### 2) Silver label Gemini N=3 sebelum training",
            "",
            "| Run | Status konten | Cognitive | Knowledge | Difficulty | Token | Latensi |",
            "|---:|---|---|---|---|---:|---:|",
        ]
        for run in silver_record["runs"]:
            output = run.get("output") or {}
            lines.append(
                f"| {run['runIndex']} | {md(output.get('contentStatus') or run.get('status'))} | {md(run_label(run, 'mathCognitiveDomain'))} | "
                f"{md(run_label(run, 'knowledgeDimension'))} | {md(run_label(run, 'intendedDifficulty'))} | "
                f"{run.get('usage', {}).get('totalTokens', 0)} | {run.get('latencyMs', 0)} ms |"
            )
        lines += ["", "**Bukti dan alasan tiap run:**", ""]
        for run in silver_record["runs"]:
            if run.get("status") != "success":
                lines.append(f"- Run {run['runIndex']}: gagal (`{md(run.get('errorCode'))}`).")
                continue
            output = run["output"]
            fragments = []
            for head in HEADS:
                value = output[head]
                evidence = "; ".join(value.get("evidenceSpans") or [])
                fragments.append(f"{HEAD_NAMES[head]} — bukti “{evidence}”; alasan: {value.get('rationale')}")
            lines.append(f"- Run {run['runIndex']}: " + " | ".join(fragments))
        lines += [
            "",
            "**Mayoritas silver:**",
            "",
            "| Head | Label | Vote | Status |",
            "|---|---|---:|---|",
        ]
        for head in HEADS:
            value = aggregate["heads"][head]
            lines.append(
                f"| {HEAD_NAMES[head]} | `{md(value.get('label'))}` | {majority_fraction(aggregate, head)} ({md(value.get('voteCounts'))}) | `{value.get('status')}` |"
            )

        prediction = prediction_record["prediction"]
        lines += [
            "",
            "### 3) Prediksi IndoBERT 3×4×3",
            "",
            "| Head | Semua probabilitas | Label | Confidence | Entropy | Aksi |",
            "|---|---|---|---:|---:|---|",
        ]
        for head in HEADS:
            value = prediction[head]
            probabilities = ", ".join(
                f"{label}={probability:.4f}" for label, probability in value["probabilities"].items()
            )
            lines.append(
                f"| {HEAD_NAMES[head]} | {probabilities} | `{md(value.get('label'))}` | {pct(value.get('calibratedConfidence'))} | {f4(value.get('normalizedEntropy'))} | `{value.get('action')}` |"
            )
        lines += [
            "",
            f"- Waktu inferensi CPU: {prediction_record['latencyMs']} ms.",
            f"- Trace: model `{prediction['trace']['modelVersion']}`, input hash `{prediction['trace']['inputHash']}`.",
            "- Perhitungan: label adalah `argmax` probabilitas; confidence adalah probabilitas label tersebut; entropy memakai seluruh distribusi pada head, bukan hanya label teratas.",
            "",
            "### 4) Validasi Gemini N=3 atas hasil IndoBERT",
            "",
            "| Run | Status konten | Cognitive | Knowledge | Difficulty | Token | Latensi |",
            "|---:|---|---|---|---|---:|---:|",
        ]
        for run in review_record["runs"]:
            output = run.get("review") or {}
            lines.append(
                f"| {run['runIndex']} | {md(output.get('contentStatus') or run.get('status'))} | "
                f"{md(reviewed_label(run, 'mathCognitiveDomain', prediction['mathCognitiveDomain']['label']))} | "
                f"{md(reviewed_label(run, 'knowledgeDimension', prediction['knowledgeDimension']['label']))} | "
                f"{md(reviewed_label(run, 'intendedDifficulty', prediction['intendedDifficulty']['label']))} | "
                f"{run.get('usage', {}).get('totalTokens', 0)} | {run.get('latencyMs', 0)} ms |"
            )
        lines += ["", "**Bukti dan alasan reviewer tiap run:**", ""]
        for run in review_record["runs"]:
            if run.get("status") != "success":
                lines.append(f"- Run {run['runIndex']}: gagal (`{md(run.get('errorCode'))}`).")
                continue
            output = run["review"]
            fragments = []
            for head in HEADS:
                value = output[head]
                evidence = "; ".join(value.get("evidenceSpans") or [])
                fragments.append(f"{HEAD_NAMES[head]} — bukti “{evidence}”; alasan: {value.get('rationale')}")
            lines.append(f"- Run {run['runIndex']}: " + " | ".join(fragments))

        review_aggregate = review_record["aggregate"]
        lines += [
            "",
            "### 5) Hasil advisory setelah validasi LLM",
            "",
            "| Head | Keputusan mayoritas LLM | Label advisory | Dukungan | Status akhir |",
            "|---|---|---|---:|---|",
        ]
        for head in HEADS:
            value = review_aggregate[head]
            label, status = review_final(prediction, review_aggregate, head)
            lines.append(
                f"| {HEAD_NAMES[head]} | `{md(value.get('suggestedAction'))}` | `{md(label)}` | {value.get('supportingRuns', 0)}/3 | `{status}` |"
            )
        lines += [
            "",
            "> Keputusan di atas tetap `reviewRequired=true`. Review dilakukan AI; hasil tetap silver dengan provenance tercatat.",
            "",
            "---",
            "",
        ]

    lines += [
        "## Kesimpulan penggunaan",
        "",
        "Pipeline sudah benar-benar menghasilkan artefak dan prediksi, tetapi status ilmiahnya masih **bootstrap silver**. File ini layak dipakai untuk demonstrasi teknis, inspeksi kesalahan, dan memilih sampel yang harus diprioritaskan kepada AI. Ia belum menggantikan anotasi AI, belum membuktikan generalisasi, dan belum memuat validitas empiris siswa.",
        "",
        "Prioritas berikutnya adalah meminta AI memeriksa item dengan confidence rendah, entropy tinggi, vote Gemini tidak bulat, atau keputusan Gemini yang merevisi IndoBERT. Sesudah silver label tersedia, model harus dilatih ulang dan frozen test dibuka sesuai gate yang telah ditetapkan.",
    ]
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.output} ({len(lines)} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
