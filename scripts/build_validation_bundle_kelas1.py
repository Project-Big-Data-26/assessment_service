"""Build an auditable, database-ready validation bundle for class 1.

This script is deliberately offline. It combines a local IndoBERT prediction
file with an existing Gemini N=3 checkpoint and never calls the Gemini API.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "output/pretest/kelas1"
HEADS = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")
HEAD_TITLES = {
    "mathCognitiveDomain": "Domain kognitif matematika",
    "knowledgeDimension": "Dimensi pengetahuan",
    "intendedDifficulty": "Kesulitan yang dimaksud",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_id(prefix: str, *parts: object) -> str:
    raw = "|".join(str(part) for part in parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha256(raw).hexdigest()[:24]}"


def markdown(value: object) -> str:
    if value is None or value == "":
        return "-"
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def fmt_number(value: float | None) -> str:
    return "-" if value is None else f"{value:.4f}"


def pct(value: float | None) -> str:
    return "-" if value is None else f"{value * 100:.2f}%"


def structural_validation(item: dict[str, Any], source_dir: Path) -> dict[str, Any]:
    reasons: list[str] = []
    options = item.get("options") or []
    labels = [str(option.get("option_id") or "").strip() for option in options]
    texts = [str(option.get("text") or "").strip().casefold() for option in options]
    if not str(item.get("soal_text") or "").strip():
        reasons.append("empty_stem")
    if len(options) < 2:
        reasons.append("fewer_than_two_options")
    if len(labels) != len(set(labels)):
        reasons.append("duplicate_option_label")
    if len(texts) != len(set(texts)):
        reasons.append("duplicate_option_text")
    if str(item.get("jawaban") or "") not in labels:
        reasons.append("answer_key_not_in_options")
    missing_assets = [
        reference
        for reference in item.get("image_url") or []
        if not (source_dir / reference).is_file()
    ]
    if missing_assets:
        reasons.append("missing_visual_asset")
    return {
        "status": "pass" if not reasons else "review",
        "reasons": reasons,
        "missingAssets": missing_assets,
    }


def run_outcome(run: dict[str, Any], head: str, original: str | None) -> dict[str, Any]:
    review = (run.get("review") or {}).get(head) or {}
    action = review.get("action")
    label = original if action == "confirm" else review.get("proposedLabel")
    if action == "abstain":
        label = None
    return {
        "action": action,
        "label": label,
        "evidenceSpans": review.get("evidenceSpans") or [],
        "reasoningSummary": review.get("rationale"),
    }


def vote_head(
    runs: list[dict[str, Any]], head: str, original: str | None, requested_runs: int
) -> dict[str, Any]:
    successful = [run for run in runs if run.get("status") == "success" and run.get("review")]
    outcomes = [run_outcome(run, head, original) for run in successful]
    keys = [(item["action"], item["label"]) for item in outcomes]
    counts = Counter(keys)
    (winner, support) = counts.most_common(1)[0] if counts else ((None, None), 0)
    required = requested_runs // 2 + 1
    has_majority = support >= required
    action, label = winner
    if not has_majority:
        action, label = None, None
    if has_majority and support == requested_runs:
        pattern = f"unanimous_{support}_0"
    elif has_majority:
        pattern = f"majority_{support}_of_{requested_runs}"
    elif len(successful) < required:
        pattern = "insufficient_successful_runs"
    else:
        pattern = "no_consensus"
    count_documents = [
        {"action": key[0], "label": key[1], "count": count}
        for key, count in sorted(counts.items(), key=lambda pair: str(pair[0]))
    ]
    return {
        "status": "consensus" if has_majority else pattern,
        "votePattern": pattern,
        "requestedRuns": requested_runs,
        "successfulRuns": len(successful),
        "requiredVotes": required,
        "supportingVotes": support,
        "voteCounts": count_documents,
        "advisoryAction": action,
        "advisoryLabel": label,
    }


def content_vote(runs: list[dict[str, Any]], requested_runs: int) -> dict[str, Any]:
    values = [
        run["review"]["contentStatus"]
        for run in runs
        if run.get("status") == "success" and run.get("review")
    ]
    counts = Counter(values)
    label, support = counts.most_common(1)[0] if counts else (None, 0)
    required = requested_runs // 2 + 1
    return {
        "status": label if support >= required else None,
        "supportingVotes": support,
        "requiredVotes": required,
        "voteCounts": dict(counts),
        "concerns": list(
            dict.fromkeys(
                concern
                for run in runs
                if run.get("status") == "success" and run.get("review")
                for concern in run["review"].get("contentConcerns") or []
            )
        ),
    }


def question_document(source: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    return {
        "questionId": row["questionId"],
        "questionVersionId": row["questionVersionId"],
        "contentVersion": row["contentVersion"],
        "contentHash": row["contentHash"],
        "grade": row["grade"],
        "topic": row.get("topic"),
        "subtopic": row.get("subtopic"),
        "questionType": row["questionType"],
        "stimulus": row.get("stimulus"),
        "stem": row["stem"],
        "options": row.get("options") or [],
        "visualAssets": source.get("image_url") or [],
        "verifiedMinimalSolution": row.get("verifiedMinimalSolution"),
        "detectedKko": row.get("detectedKko") or [],
        "privateAnswerSpecification": {
            "answerKey": source.get("jawaban"),
            "sourceOptionNotes": {
                str(option.get("option_id")): option.get("alasan")
                for option in source.get("options") or []
            },
            "visibility": "restricted",
        },
        "source": {
            "externalId": str(source.get("_id")),
            "sourceGroup": row.get("sourceGroup"),
            "subchapter": source.get("subbab_id"),
        },
        "visualTranscript": row.get("visualTranscript"),
    }


def build_decision(
    source: dict[str, Any],
    row: dict[str, Any],
    prediction_record: dict[str, Any],
    review_record: dict[str, Any],
    review_payload: dict[str, Any],
    source_dir: Path,
    generated_at: str,
) -> dict[str, Any]:
    prediction = prediction_record["prediction"]
    requested_runs = int(review_payload["requestedRuns"])
    runs = review_record.get("runs") or []
    successful_runs = sum(run.get("status") == "success" for run in runs)
    votes = {
        head: vote_head(runs, head, prediction[head].get("label"), requested_runs)
        for head in HEADS
    }
    advisory_labels = {
        head: value["advisoryLabel"] if value["status"] == "consensus" else None
        for head, value in votes.items()
    }
    complete = all(
        value["status"] == "consensus"
        and value["advisoryAction"] != "abstain"
        and value["advisoryLabel"] is not None
        for value in votes.values()
    )
    input_validation = structural_validation(source, source_dir)
    content = content_vote(runs, requested_runs)
    if input_validation["status"] != "pass":
        routing = "revision_required"
    elif not complete or content["status"] in {None, "insufficient_evidence"}:
        routing = "needs_ai_review"
    elif content["status"] == "concern":
        routing = "revision_required"
    else:
        routing = "silver_ready"

    stored_runs = []
    for run in runs:
        stored = {
            "runIndex": run.get("runIndex"),
            "status": run.get("status"),
            "errorCode": run.get("errorCode"),
            "responseId": run.get("responseId"),
            "responseHash": run.get("responseHash"),
            "latencyMs": run.get("latencyMs"),
            "usage": run.get("usage") or {},
            "contentStatus": (run.get("review") or {}).get("contentStatus"),
            "contentConcerns": (run.get("review") or {}).get("contentConcerns") or [],
            "heads": {},
        }
        for head in HEADS:
            stored["heads"][head] = run_outcome(
                run, head, prediction[head].get("label")
            ) if run.get("status") == "success" else None
        stored_runs.append(stored)

    question_id = row["questionId"]
    workflow_id = stable_id(
        "WF", question_id, row["contentVersion"], prediction["trace"]["modelVersion"]
    )
    return {
        "decisionId": stable_id(
            "AID", workflow_id, review_payload["model"], review_payload["promptVersion"]
        ),
        "workflowRunId": workflow_id,
        "questionId": question_id,
        "questionVersionId": row["questionVersionId"],
        "contentVersion": row["contentVersion"],
        "contentHash": row["contentHash"],
        "decisionType": "llm_advisory_complete" if complete else "llm_advisory_incomplete",
        "inputValidation": input_validation,
        "featureManifest": {
            "grade": row["grade"],
            "topic": row.get("topic"),
            "subtopic": row.get("subtopic"),
            "questionType": row["questionType"],
            "detectedKko": row.get("detectedKko") or [],
            "serializedInput": prediction_record["serializedInput"],
            "untruncatedTokenCount": prediction_record["untruncatedTokenCount"],
            "maxLength": prediction_record["maxLength"],
            "wouldTruncate": prediction_record["wouldTruncate"],
        },
        "indobert": {
            "heads": {head: prediction[head] for head in HEADS},
            "scopeStatus": prediction["scopeStatus"],
            "reviewRequired": prediction["reviewRequired"],
            "latencyMs": prediction_record["latencyMs"],
            "trace": prediction["trace"],
        },
        "llmAdvisory": {
            "provider": review_payload["provider"],
            "model": review_payload["model"],
            "promptVersion": review_payload["promptVersion"],
            "rubricVersion": review_payload["rubricVersion"],
            "method": "self_consistency_majority_vote",
            "requestedRuns": requested_runs,
            "requiredVotes": requested_runs // 2 + 1,
            "successfulRuns": successful_runs,
            "contentAssessment": content,
            "runs": stored_runs,
            "votes": votes,
            "advisoryLabels": advisory_labels,
            "labelProvenance": "ai_silver",
        },
        "labelProvenance": "ai_silver", "reviewMode": "automated_ai",
        "finalRouting": routing,
        "createdAt": generated_at,
    }


def render_report(
    questions: list[dict[str, Any]],
    decisions: list[dict[str, Any]],
    predictions: dict[str, Any],
    review: dict[str, Any],
    generated_at: str,
    grade: int,
) -> str:
    question_by_id = {item["questionId"]: item for item in questions}
    route_counts = Counter(item["finalRouting"] for item in decisions)
    lines = [
        f"# Hasil Validasi Soal Kelas {grade} — IndoBERT dan Gemini N=3",
        "",
        f"> Dibuat: `{generated_at}`  ",
        "> Status: **advisory berbasis silver label; bukan label silver yang qualified.**  ",
        "> CTT dan IRT tidak dijalankan karena belum ada respons siswa.",
        "",
        "## Cara membaca laporan",
        "",
        "Setiap soal melewati validasi struktur, klasifikasi IndoBERT tiga head, lalu review Gemini sebanyak tiga run. Gemini memberikan bukti dan alasan singkat yang dapat diaudit; sistem tidak menyimpan atau menampilkan chain-of-thought internal. Hasil tiga run digabung dengan majority vote minimal 2 dari 3. Hasil akhirnya tetap proposal AI dan memerlukan qualification konten sebelum masuk snapshot silver.",
        "",
        "## Ringkasan",
        "",
        "| Komponen | Nilai |",
        "|---|---|",
        f"| Jumlah soal | {len(decisions)} |",
        f"| Model IndoBERT | `{predictions['model']['modelVersion']}` |",
        f"| Arsitektur | `{predictions['model'].get('architectureVersion', 'parallel-v1')}` |",
        f"| LLM reviewer | `{review['model']}` |",
        f"| Konfigurasi voting | N={review['requestedRuns']}, mayoritas minimal 2 suara |",
        f"| Run LLM sukses | {review['summary']['successfulRuns']}/{len(decisions) * review['requestedRuns']} |",
        f"| Token historis pada checkpoint LLM | {review['summary']['totalTokens']:,} |",
        f"| Silver qualified | {route_counts['silver_ready']} |",
        f"| Perlu retry/review manual | {route_counts['needs_ai_review']} |",
        f"| Perlu revisi konten | {route_counts['revision_required']} |",
        "",
        "## Rumus yang digunakan",
        "",
        "- Probabilitas per head: `p_i = softmax(z_i / T)`.",
        "- Label IndoBERT: `argmax(p_i)`.",
        "- Confidence: `max(p_i)`; ini keyakinan model, bukan bukti prediksi benar.",
        "- Entropy ternormalisasi: `H = -Σ p_i ln(p_i) / ln(K)`. Nilai mendekati 0 berarti lebih tegas; mendekati 1 berarti lebih ambigu.",
        "- Majority vote LLM: pasangan `(aksi, label)` harus memperoleh minimal `2/3` suara.",
        "- Jumlah token yang dilaporkan berasal dari run sukses pada checkpoint. Percobaan gagal/retry yang tidak menyimpan usage bisa menambah pemakaian di dashboard provider.",
        "",
        "Input menggunakan konten dan solusi hasil ekstraksi/silver. Kunci, solusi, dan transkripsi tersebut diperiksa AI sebelum qualification. Model aktif serta dataset training asal tercatat pada manifest prediksi; menjalankan inferensi pada kelas ini tidak berarti model telah dilatih ulang dengan data kelas ini.",
        "",
        "## Hasil per soal",
        "",
    ]

    for ordinal, decision in enumerate(decisions, start=1):
        question = question_by_id[decision["questionId"]]
        answer_key = question["privateAnswerSpecification"]["answerKey"]
        lines.extend(
            [
                f"## {ordinal}. Soal `{decision['questionId']}`",
                "",
                f"**Soal:** {markdown(question['stem'])}",
                "",
                "| Opsi | Isi |",
                "|---|---|",
            ]
        )
        for option in question["options"]:
            mark = " ✓" if option["label"] == answer_key else ""
            lines.append(f"| {markdown(option['label'])}{mark} | {markdown(option['text'])} |")
        validation = decision["inputValidation"]
        feature = decision["featureManifest"]
        lines.extend(
            [
                "",
                "### Tahap 1 — Pemeriksaan input",
                "",
                f"- Status struktur: `{validation['status']}`; alasan: {markdown(', '.join(validation['reasons']))}.",
                f"- Kelas/topik/tipe: `{feature['grade']}` / {markdown(feature['topic'])} / {markdown(feature['questionType'])}.",
                f"- Token input: `{feature['untruncatedTokenCount']}/{feature['maxLength']}`; terpotong: `{str(feature['wouldTruncate']).lower()}`.",
                f"- KKO terdeteksi: {markdown(', '.join(feature['detectedKko']))}. KKO hanya fitur bantu, bukan penentu tunggal.",
                "",
                "### Tahap 2 — Klasifikasi IndoBERT",
                "",
                "Encoder bersama membaca teks kanonis. Tiga classification head menghasilkan logits, lalu softmax dan temperature scaling menghasilkan probabilitas. Routing memakai confidence/entropy sesuai manifest model.",
                "",
                "| Head | Probabilitas lengkap | Label | Confidence | Entropy | Aksi | Alasan routing |",
                "|---|---|---|---:|---:|---|---|",
            ]
        )
        for head in HEADS:
            value = decision["indobert"]["heads"][head]
            probabilities = ", ".join(
                f"{label}={probability:.4f}"
                for label, probability in value["probabilities"].items()
            )
            lines.append(
                f"| {HEAD_TITLES[head]} | {probabilities} | `{markdown(value['label'])}` | "
                f"{pct(value['calibratedConfidence'])} | {fmt_number(value['normalizedEntropy'])} | "
                f"`{value['action']}` | {markdown(', '.join(value['reasons']))} |"
            )
        lines.extend(
            [
                "",
                f"Waktu inferensi CPU: `{decision['indobert']['latencyMs']} ms`. Semua head tetap memiliki `reviewRequired=true`.",
                "",
                "<details><summary>Teks kanonis yang dibaca IndoBERT</summary>",
                "",
                "```text",
                feature["serializedInput"],
                "```",
                "</details>",
                "",
                "### Tahap 3 — Review LLM dan self-consistency N=3",
                "",
                "Setiap run memeriksa soal dan prediksi IndoBERT secara terpisah, kemudian memilih `confirm`, `revise`, atau `abstain`. Bagian alasan di bawah adalah ringkasan keputusan dan evidence span, bukan chain-of-thought tersembunyi.",
                "",
                "| Run | Status | Konten | Kognitif | Pengetahuan | Difficulty | Token |",
                "|---:|---|---|---|---|---|---:|",
            ]
        )
        for run in decision["llmAdvisory"]["runs"]:
            def outcome_text(head: str) -> str:
                outcome = run["heads"].get(head)
                return "-" if not outcome else f"{outcome['action']}:{outcome['label'] or '-'}"

            lines.append(
                f"| {run['runIndex']} | `{run['status']}` | {markdown(run['contentStatus'])} | "
                f"{markdown(outcome_text('mathCognitiveDomain'))} | "
                f"{markdown(outcome_text('knowledgeDimension'))} | "
                f"{markdown(outcome_text('intendedDifficulty'))} | {run['usage'].get('totalTokens', 0)} |"
            )
        lines.extend(["", "**Bukti dan alasan ringkas per run:**", ""])
        for run in decision["llmAdvisory"]["runs"]:
            if run["status"] != "success":
                lines.append(
                    f"- Run {run['runIndex']}: gagal dengan kode `{markdown(run['errorCode'])}`."
                )
                continue
            pieces = []
            for head in HEADS:
                outcome = run["heads"][head]
                evidence = "; ".join(outcome["evidenceSpans"]) or "tanpa kutipan"
                pieces.append(
                    f"**{HEAD_TITLES[head]}** — {outcome['action']} `{outcome['label'] or '-'}`; "
                    f"bukti: “{evidence}”; alasan: {outcome['reasoningSummary']}"
                )
            lines.append(f"- Run {run['runIndex']}: " + " | ".join(pieces))
        lines.extend(
            [
                "",
                "### Tahap 4 — Majority vote dan hasil advisory",
                "",
                "| Head | Pola vote | Dukungan | Aksi | Label advisory |",
                "|---|---|---:|---|---|",
            ]
        )
        for head in HEADS:
            vote = decision["llmAdvisory"]["votes"][head]
            lines.append(
                f"| {HEAD_TITLES[head]} | `{vote['votePattern']}` | "
                f"{vote['supportingVotes']}/{vote['requestedRuns']} | "
                f"`{markdown(vote['advisoryAction'])}` | `{markdown(vote['advisoryLabel'])}` |"
            )
        lines.extend(
            [
                "",
                f"**Routing akhir:** `{decision['finalRouting']}`.",
                "",
                "> Label advisory bukan silver label. Label operasional berasal dari validasi AI.",
                "",
                "---",
                "",
            ]
        )
        bootstrap = decision.get("silverBootstrap")
        if bootstrap:
            lines.extend([
                "### Audit tambahan — Label silver awal sebelum melihat IndoBERT",
                "",
                "Label awal dibuat Gemini dari soal dan aset sumber. Review di atas dibuat setelah Gemini melihat prediksi IndoBERT. Perbedaan di tabel ini membantu AI menilai perubahan label dan kemungkinan pengaruh prediksi awal; kesesuaian tidak dihitung sebagai akurasi terhadap silver.",
                "",
                "| Head | Silver awal | Vote silver | IndoBERT | Advisory sesudah review |",
                "|---|---|---:|---|---|",
            ])
            for head in HEADS:
                initial = bootstrap["aggregate"]["heads"][head]
                lines.append(
                    f"| {HEAD_TITLES[head]} | `{markdown(initial.get('label'))}` | "
                    f"{initial.get('supportingRuns', 0)}/3 | "
                    f"`{markdown(decision['indobert']['heads'][head]['label'])}` | "
                    f"`{markdown(decision['llmAdvisory']['advisoryLabels'][head])}` |"
                )
            lines.extend(["", "---", ""])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=BASE / "soal_pretest_db.json")
    parser.add_argument("--snapshot", type=Path, default=BASE / "dataset_snapshot_silver.json")
    parser.add_argument(
        "--predictions", type=Path, default=BASE / "indobert_predictions_silver.json"
    )
    parser.add_argument(
        "--review",
        type=Path,
        default=BASE / "gemini_review_indobert_3_5_flash_lite.json",
    )
    parser.add_argument("--output-dir", type=Path, default=BASE / "hasil_validasi")
    parser.add_argument("--silver", type=Path, help="Optional initial N=3 checkpoint for provenance and label comparison.")
    args = parser.parse_args()

    source = load_json(args.source)
    snapshot = load_json(args.snapshot)
    predictions = load_json(args.predictions)
    review = load_json(args.review)
    silver = load_json(args.silver) if args.silver else None
    if silver and silver.get("sourceHash") != sha256_file(args.source):
        raise ValueError("silver checkpoint source hash does not match the source file")
    generated_at = datetime.now(timezone.utc).isoformat()

    source_by_id = {str(item["_id"]): item for item in source}
    rows = {row["questionId"]: row for row in snapshot["rows"]}
    prediction_by_id = {item["questionId"]: item for item in predictions["items"]}
    review_by_id = review["items"]
    ids = list(rows)
    source_key_by_id = {
        qid: str(
            (rows[qid].get("decisionProvenance") or {}).get("sourceExternalId") or qid
        )
        for qid in ids
    }
    grades = {int(row["grade"]) for row in rows.values()}
    if len(grades) != 1:
        raise ValueError(f"snapshot must contain exactly one grade, got {sorted(grades)}")
    grade = grades.pop()
    missing = {
        "source": sorted(
            qid for qid in ids if source_key_by_id[qid] not in source_by_id
        ),
        "prediction": sorted(set(ids) - set(prediction_by_id)),
        "review": sorted(set(ids) - set(review_by_id)),
    }
    if any(missing.values()):
        raise ValueError(f"incomplete inputs: {missing}")

    questions = [
        question_document(source_by_id[source_key_by_id[qid]], rows[qid]) for qid in ids
    ]
    decisions = [
        build_decision(
            source_by_id[source_key_by_id[qid]],
            rows[qid],
            prediction_by_id[qid],
            review_by_id[qid],
            review,
            args.source.parent,
            generated_at,
        )
        for qid in ids
    ]
    if silver:
        for decision in decisions:
            external_id = source_key_by_id[decision["questionId"]]
            initial = silver["items"][external_id]
            decision["silverBootstrap"] = {
                "provider": silver["provider"],
                "model": silver["model"],
                "promptVersion": silver["promptVersion"],
                "sourceGrade": silver.get("sourceGrade"),
                "requestedRuns": silver["requestedRuns"],
                "aggregate": initial["aggregate"],
                "sourceInputHash": initial["inputHash"],
                "responseHashes": [run.get("responseHash") for run in initial["runs"] if run.get("status") == "success"],
                "labelProvenance": "ai_silver",
            }
    if len({item["decisionId"] for item in decisions}) != len(decisions):
        raise ValueError("decisionId collision")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    questions_path = args.output_dir / "questions.json"
    decisions_path = args.output_dir / "validation_results.json"
    report_path = args.output_dir / "LAPORAN_VALIDASI.md"
    write_json(
        questions_path,
        {
            "schemaVersion": "question-validation-input-v1",
            "createdAt": generated_at,
            "visibility": "restricted_contains_answer_key",
            "items": questions,
        },
    )
    write_json(
        decisions_path,
        {
            "schemaVersion": "ai-decision-bundle-v1",
            "collectionTarget": "ai_decisions",
            "createdAt": generated_at,
            "sourceClass": grade,
            "summary": {
                "itemCount": len(decisions),
                "routingCounts": dict(Counter(item["finalRouting"] for item in decisions)),
                "labelProvenance": "ai_silver",
                "silverReadyCount": sum(d["finalRouting"] == "silver_ready" for d in decisions),
            },
            "items": decisions,
        },
    )
    report_path.write_text(
        render_report(questions, decisions, predictions, review, generated_at, grade),
        encoding="utf-8",
    )
    files = [questions_path, decisions_path, report_path]
    manifest = {
        "schemaVersion": "validation-bundle-manifest-v1",
        "createdAt": generated_at,
        "class": grade,
        "offlineBuild": True,
        "newLlmCalls": 0,
        "buildStage": "offline_packaging_of_existing_predictions_and_llm_checkpoint",
        "historicalReviewSuccessfulRuns": review["summary"]["successfulRuns"],
        "historicalReviewRecordedTokens": review["summary"]["totalTokens"],
        "sourceFiles": {
            "source": {"path": args.source.as_posix(), "sha256": sha256_file(args.source)},
            "snapshot": {"path": args.snapshot.as_posix(), "sha256": sha256_file(args.snapshot)},
            "predictions": {
                "path": args.predictions.as_posix(),
                "sha256": sha256_file(args.predictions),
            },
            "llmReview": {"path": args.review.as_posix(), "sha256": sha256_file(args.review)},
        },
        "outputs": {
            path.name: {"sha256": sha256_file(path), "bytes": path.stat().st_size}
            for path in files
        },
        "limitations": [
            "Legacy model-aware LLM review is diagnostic; operational qualification uses blind silver.",
            "Consensus is based on three samples of one LLM and is not three independent models.",
            "Provider usage may exceed checkpoint totals when unsuccessful attempts have no recorded usage.",
            "No student response data were used, so CTT and IRT were not calculated.",
        ],
    }
    if args.silver:
        manifest["sourceFiles"]["silverLabels"] = {
            "path": args.silver.as_posix(), "sha256": sha256_file(args.silver)
        }
        manifest["historicalSilverRecordedTokens"] = silver["summary"]["totalTokens"]
    write_json(args.output_dir / "manifest.json", manifest)
    print(json.dumps({"outputDir": str(args.output_dir), **manifest["outputs"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
