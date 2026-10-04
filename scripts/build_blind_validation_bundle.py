"""Publish a locked blind Gemini assessment and offline IndoBERT diagnostics.

No provider calls are made here. Assessment includes every source item, including
content blockers; model disagreement never overwrites the locked blind decision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.classification.v2.contracts import HEAD_LABELS, V2ClassificationRequest  # noqa: E402
from app.classification.v2.kko import detect_kko  # noqa: E402
from app.classification.v2.runtime import V2ClassifierRuntime  # noqa: E402
from app.classification.v2.serializer import canonical_json_hash, serialize_question  # noqa: E402
from app.llm.silver import silver_rubric  # noqa: E402
from app.silver.policy import POLICY_VERSION, qualification  # noqa: E402
from scripts.build_validation_bundle_kelas1 import structural_validation  # noqa: E402

HEADS = tuple(HEAD_LABELS)
TITLES = dict(zip(HEADS, ("Domain kognitif", "Dimensi pengetahuan", "Intended difficulty")))


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def md(value) -> str:
    return "—" if value is None else str(value).replace("|", "\\|").replace("\n", "<br>")


def select_evidence(record: dict, head: str, label: str | None) -> dict:
    adjudication = record.get("adjudication") or {}
    if record.get("aggregate", {}).get("adjudicated"):
        return (adjudication.get("output") or {}).get(head) or {}
    for run in record.get("runs", []):
        decision = (run.get("output") or {}).get(head) or {}
        if run.get("status") == "success" and decision.get("label") == label:
            return decision
    return {}


def blind_outcome(record: dict, structure: dict, question: dict | None = None) -> tuple[dict, str]:
    return qualification(record, structure, question)


def verify_probability(head: dict) -> None:
    ps = list(head["probabilities"].values())
    if not ps:
        assert head["action"] == "abstain" and head["label"] is None
        return
    assert all(math.isfinite(p) and 0 <= p <= 1 for p in ps)
    assert math.isclose(sum(ps), 1, abs_tol=1e-6)
    assert math.isclose(max(ps), head["calibratedConfidence"], abs_tol=1e-6)
    entropy = -sum(p * math.log(p) for p in ps if p) / math.log(len(ps))
    assert math.isclose(entropy, head["normalizedEntropy"], abs_tol=1e-6)
    assert head["label"] == max(head["probabilities"], key=head["probabilities"].get)


def difficulty_groups(questions: list[dict], decisions: list[dict], grade: int) -> dict:
    groups = {label: [] for label in (*HEAD_LABELS["intendedDifficulty"], "undecided")}
    for question, decision in zip(questions, decisions, strict=True):
        if question["questionId"] != decision["questionId"] or question["grade"] != grade:
            raise ValueError("question/decision identity or grade mismatch")
        label = decision["llmAdvisory"]["advisoryLabels"]["intendedDifficulty"]
        groups[label or "undecided"].append({
            "question": question,
            "advisoryLabels": decision["llmAdvisory"]["advisoryLabels"],
            "finalRouting": decision["finalRouting"],
            "contentQualified": decision["finalRouting"] == "silver_ready",
            "reviewMode": "automated_ai",
            "labelProvenance": "ai_silver",
        })
    return {
        "schemaVersion": "blind-difficulty-groups-v1", "sourceClass": grade,
        "researchOnly": True, "groups": groups,
        "summary": {label: {
            "advisoryCount": len(items),
            "contentQualifiedCount": sum(item["contentQualified"] for item in items),
        } for label, items in groups.items()},
    }


def batch_completion_note(checkpoint: dict, item_count: int) -> str:
    successful = int(checkpoint["summary"]["successfulRuns"])
    expected = item_count * 3
    pending = int(checkpoint["summary"].get("pendingAdjudication", 0))
    if successful >= expected and not pending:
        return ""
    reason = (
        " Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia."
        if checkpoint.get("executionStatus") in ("blocked_provider_daily_quota", "waiting_provider_daily_quota") else ""
    )
    return (
        f"**Batch belum selesai:** {successful}/{expected} run awal sukses; "
        f"{pending} item tercatat membutuhkan adjudikasi setelah run lengkap. "
        f"Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided.{reason}"
    )


def model_in_scope(model: dict, grade: int, track: str = "regular") -> bool:
    return (grade in model.get("supportedGrades", list(range(1, 7)))
            and track in model.get("supportedSubjectTracks", ["regular"]))


def calibration_for(model: dict, head: str, grade: int, track: str = "regular") -> dict:
    global_calibration = model["calibration"][head]
    return global_calibration.get("perGradeTrack", {}).get(
        f"{grade}:{track}",
        global_calibration.get("perGrade", {}).get(str(grade), global_calibration)
        if track == "regular" else global_calibration,
    )


def render_report(questions, decisions, summary, checkpoint, model, *, output_dir=None) -> str:
    grade = int(checkpoint["sourceGrade"])
    rubric = silver_rubric(grade, track=checkpoint.get("subjectTrack", "regular"))
    class_label = f"{grade} TL" if checkpoint.get("subjectTrack") == "tl" else str(grade)
    out_of_scope = not model_in_scope(model, grade, checkpoint.get("subjectTrack", "regular"))
    supported_grades = model.get("supportedGrades", list(range(1, 7)))
    supported_tracks = model.get("supportedSubjectTracks", ["regular"])
    diagnostic_overview = (
        f"Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas {class_label}, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind."
        if out_of_scope else
        "Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model dipakai sebagai diagnostik; tidak diberikan kembali ke Gemini."
    )
    probability_overview = (
        f"Untuk kelas {class_label}, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas {supported_grades}, jalur {supported_tracks}. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT."
        if out_of_scope else
        "Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini."
    )
    lines = [
        f"# Validasi ulang soal kelas {class_label} — Gemini blind N=3 dan diagnostik IndoBERT",
        "",
        f"Model penilai: `{checkpoint['model']}`. Prompt: `{checkpoint['promptVersion']}`. Rubrik: `{checkpoint['rubricVersion']}`.",
        "",
        f"Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas {grade} tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.",
        "",
        diagnostic_overview,
        "",
        f"Jumlah soal: {summary['itemCount']}; distribusi label advisory: `{json.dumps(summary['advisoryLabelDistributions'], ensure_ascii=False)}`.",
        f"Distribusi hanya pada soal tanpa blocker konten: `{json.dumps(summary['contentQualifiedAdvisoryLabelDistributions'], ensure_ascii=False)}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.",
        f"Routing: `{json.dumps(summary['routingCounts'], ensure_ascii=False)}`.",
        f"Run awal sukses: {checkpoint['summary']['successfulRuns']}/{summary['itemCount'] * 3}; adjudikasi: {checkpoint['summary'].get('adjudicatedItems', 0)}; token sukses tercatat: {checkpoint['summary']['totalTokens']:,}.",
        "",
        "Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.",
        "",
        f"Artifact diagnostik IndoBERT: `{model['modelVersion']}`, arsitektur `{model['architectureVersion']}`, representation `{model['inputRepresentation']}`. Dataset training: `{model.get('datasetSnapshot', 'tidak tercatat')}`. Approval provisional: `{model.get('approvedForProvisional', False)}`; research-only: `{model.get('researchOnly', False)}`; gate data: `{model.get('dataGatesPassed', False)}`; anti-collapse: `{model.get('antiCollapsePassed', False)}`; gate promosi: `{model.get('promotionGates', {}).get('passed', False)}`. Packaging ini tidak melakukan training atau promosi model.",
        f"KKO eksplisit masuk input encoder: `{model['inputRepresentation'] == 'kko'}`. Solusi minimum masuk input encoder: `{model['inputRepresentation'] in {'solution', 'kko'}}`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.",
        "",
        "## Kelompok difficulty",
        "",
        "Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.",
        "",
        "| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |",
        "|---|---:|---:|---|",
        *[f"| {label} | {summary['advisoryLabelDistributions']['intendedDifficulty'].get(label, 0)} | {summary['contentQualifiedAdvisoryLabelDistributions']['intendedDifficulty'].get(label, 0)} | [{label}.json](difficulty/{label}.json) |" for label in HEAD_LABELS["intendedDifficulty"]],
        "",
        "## Perhitungan yang dipakai",
        "",
        probability_overview,
        "",
        "Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.",
        "",
    ]
    completion_note = batch_completion_note(checkpoint, summary["itemCount"])
    if completion_note:
        lines[2:2] = [completion_note, ""]
    if out_of_scope:
        lines.extend([
            f"Cakupan artifact: kelas {supported_grades}, jalur {supported_tracks}. Untuk kelas {class_label}, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik {rubric.education_level} kelas {grade}.",
            "",
        ])
    for index, (q, d) in enumerate(zip(questions, decisions), 1):
        llm = d["llmAdvisory"]
        lines.extend([f"## {index}. Soal `{q['questionId']}`", "", md(q["stem"]), "", "| Opsi | Isi |", "|---|---|"])
        lines.extend(f"| {md(o['label'])} | {md(o['text'])} |" for o in q["options"])
        for asset in q["visualAssets"]:
            target = f"../{asset}"
            if output_dir is not None:
                target = Path(os.path.relpath(Path(q['source']['assetBasePath']) / asset, output_dir)).as_posix()
            lines.extend(["", f"![Gambar sumber soal {index}](<{target}>)", ""])
        lines.extend([
            "",
            f"Kunci sumber: `{q['privateAnswerSpecification']['answerKey']}`; status AI: `{llm['answerKeyAssessment']['status']}`; jawaban diverifikasi AI: `{llm['answerKeyAssessment']['verifiedAnswerKey']}`.",
            f"Solusi minimum hasil AI: {md(q.get('verifiedMinimalSolution'))}",
            f"Gambar sumber: {md(', '.join(q['visualAssets']) or None)}. Transkripsi visual: {md(q.get('visualTranscript'))}",
            "",
            "### 1. Pemeriksaan input dan fitur",
            "",
            f"Struktur: `{d['inputValidation']['status']}`; alasan: `{d['inputValidation']['reasons']}`. Grade/topik: kelas {q['grade']} / {md(q['topic'])}. KKO: `{q['detectedKko']}`; KKO hanya petunjuk bantu.",
            f"Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: {q['contentVersion']}; hash: `{q['contentHash']}`. Bukti verifikasi AI tetap tercatat sebagai silver.",
            "",
            "### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT",
            "",
            "| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |",
            "|---:|---|---|---|---|---|---:|",
        ])
        for run in llm["runs"]:
            lines.append(f"| {run['runIndex']} | {run['status']} | {md(run['contentStatus'])} / {md(run['answerKeyStatus'])} | {md(run['heads'].get(HEADS[0], {}).get('label'))} | {md(run['heads'].get(HEADS[1], {}).get('label'))} | {md(run['heads'].get(HEADS[2], {}).get('label'))} | {run['usage'].get('totalTokens', 0)} |")
        for run in llm["runs"]:
            if run["status"] != "success":
                lines.extend(["", f"Run {run['runIndex']} gagal: `{run.get('errorCode')}`; tidak dihitung sebagai suara."])
                continue
            lines.extend(["", f"Run {run['runIndex']} — solusi: {md(run['verifiedMinimalSolution'])}"])
            for head in HEADS:
                h = run["heads"].get(head) or {}
                lines.append(f"- {TITLES[head]} `{h.get('action')}/{h.get('label')}`: {md(h.get('reasoningSummary'))}. Bukti: {md('; '.join(h.get('evidenceSpans') or []))}")
            profile = run["heads"].get("intendedDifficulty", {}).get("profile") or {}
            lines.extend(["", "Profil difficulty run ini:", "", "| Parameter | Nilai |", "|---|---|"])
            lines.extend(f"| {md(k)} | {md(v)} |" for k, v in profile.items())
        for attempt in llm.get("retryHistory", []):
            lines.extend(["", f"Histori retry: run {attempt['runIndex']} sebelumnya `{attempt['status']}` / `{attempt.get('errorCode')}`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru."])
        lines.extend(["", "### 3. Voting awal dan adjudikasi", "", "| Head | Suara awal | Pola / status akhir | Label akhir advisory |", "|---|---|---|---|"])
        for head, vote in llm["votes"].items():
            lines.append(f"| {TITLES[head]} | {md(json.dumps(vote['voteCounts'], ensure_ascii=False))} | {md(vote['votePattern'])} / {md(vote['status'])} | {md(llm['advisoryLabels'][head])} |")
        adjudication = llm.get("adjudication") or {}
        if adjudication:
            lines.extend(["", f"Adjudikasi AI: `{adjudication.get('status')}`; token `{adjudication.get('usage', {}).get('totalTokens', 0)}`."])
            ao = adjudication.get("output") or {}
            lines.append(f"Konten: `{ao.get('contentStatus')}`; kunci: `{ao.get('answerKeyStatus')}`; masalah: {md('; '.join(ao.get('contentConcerns') or []))}.")
            for head in HEADS:
                h = ao.get(head) or {}
                lines.append(f"- {TITLES[head]} `{h.get('label')}`: {md(h.get('rationale'))}")
            profile = (ao.get("intendedDifficulty") or {}).get("profile") or {}
            if profile:
                lines.extend(["", "Profil difficulty hasil adjudikasi:", "", "| Parameter | Nilai |", "|---|---|"])
                lines.extend(f"| {md(k)} | {md(v)} |" for k, v in profile.items())
        scope = d["indobert"]["scopeStatus"]
        diagnostic_note = (
            f"Scope model: `{scope}`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit."
            if scope == "out_of_scope" else
            f"Model membaca representation `{model['inputRepresentation']}`; token input {d['featureManifest']['untruncatedTokenCount']}/{model['maxLength']}; truncation: `{d['featureManifest']['wouldTruncate']}`."
        )
        lines.extend(["", "### 4. Diagnostik IndoBERT setelah label blind dikunci", "", diagnostic_note, "", "| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |", "|---|---|---|---:|---:|---|"])
        for head, h in d["indobert"]["heads"].items():
            ps = h["probabilities"]
            confidence = "—" if h["calibratedConfidence"] is None else f"{h['calibratedConfidence']:.6f}"
            entropy = "—" if h["normalizedEntropy"] is None else f"{h['normalizedEntropy']:.6f}"
            lines.append(f"| {TITLES[head]} | {md('; '.join(f'{k}={v:.6f}' for k, v in ps.items()))} | {md(h['label'])} | {confidence} | {entropy} | {h['action']} / {md('; '.join(h['reasons']))} |")
        for head, h in d["indobert"]["heads"].items():
            ps = h["probabilities"]
            if ps:
                entropy_sum = -sum(p * math.log(p) for p in ps.values() if p)
                temperature = calibration_for(model, head, grade, checkpoint.get("subjectTrack", "regular"))["temperature"]
                lines.append(f"\n{TITLES[head]}: Σp = {sum(ps.values()):.8f}; confidence = max(p) = {max(ps.values()):.6f}; −Σp ln(p) = {entropy_sum:.6f}; H = {entropy_sum:.6f}/ln({len(ps)}) = {h['normalizedEntropy']:.6f}; T = {temperature:.6f}.\n")
        input_title = "Input terserialisasi untuk audit; encoder tidak dijalankan" if scope == "out_of_scope" else "Input sebenarnya yang dibaca model"
        lines.extend(["", f"<details><summary>{input_title}</summary>", "", "```text", d["featureManifest"]["serializedInput"], "```", "", "</details>", "", "### 5. Keputusan batch", "", f"Label advisory blind: `{json.dumps(llm['advisoryLabels'], ensure_ascii=False)}`. Routing: `{d['finalRouting']}`.", f"Status konten: `{llm['contentAssessment']['status']}`. Catatan konten: {md('; '.join(llm['contentAssessment']['concerns']))}.", f"Perbedaan model dan blind: `{json.dumps(d['modelComparison'], ensure_ascii=False)}`.", "Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--artifact", type=Path, default=ROOT / "models/indobert-3x4x3-v1")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.output_dir.exists() and any(args.output_dir.iterdir()):
        raise FileExistsError("refusing to overwrite an existing blind validation bundle")
    source, checkpoint, audit = load(args.source), load(args.checkpoint), load(args.audit)
    grade = int(checkpoint["sourceGrade"])
    rubric = silver_rubric(grade, track=checkpoint.get("subjectTrack", "regular"))
    if audit["grade"] != grade:
        raise ValueError("checkpoint/audit grade mismatch")
    if audit.get("subjectTrack", "regular") != checkpoint.get("subjectTrack", "regular"):
        raise ValueError("checkpoint/audit subject track mismatch")
    if checkpoint.get("requestedRuns") != 3:
        raise ValueError("blind validation bundle requires N=3")
    if any(item.get("kelas_id") not in (None, grade) for item in source):
        raise ValueError("source contains a different grade")
    assert audit["checkpointLockedByAudit"] and audit["checkpointSha256"] == digest(args.checkpoint)
    assert audit["sourceSha256"] == digest(args.source) == checkpoint["sourceHash"]
    assert audit["gates"]["blindPromptLeakageAbsent"] and audit["gates"]["checkpointSourceAndInputsMatch"]
    assert audit["gates"]["promptAndRubricVersionMatch"]
    # Audit failures block training/expansion; they must not suppress a report of content blockers.
    assert set(checkpoint["items"]) <= {str(q["_id"]) for q in source}
    runtime = V2ClassifierRuntime(args.artifact)
    model = runtime.manifest.model_dump(mode="json", exclude={"contentRegistry"})
    created = datetime.now(timezone.utc).isoformat()
    assert created >= audit["generatedAt"]
    questions, decisions, predictions = [], [], []
    for index, item in enumerate(source, 1):
        external_id = str(item["_id"])
        record = checkpoint["items"].get(external_id) or {}
        aggregate = record.get("aggregate") or {}
        assert not record or record["inputHash"] == canonical_json_hash(item)
        structure = structural_validation(item, args.source.parent)
        labels, route = blind_outcome(record, structure, item)
        transcript = aggregate.get("visualTranscript")
        solution = aggregate.get("verifiedMinimalSolution")
        # Preserve the source business ID in exports. Only the diagnostic request
        # uses an alias, since this old artifact registers a different v1 hash.
        qid = external_id
        diagnostic_qid = f"diagnostic:kelas{grade}:{external_id}:content-v2"
        content = {"grade": grade, "stem": item["soal_text"], "options": item["options"], "sourceAnswerKey": item.get("jawaban"), "verifiedAnswerKey": aggregate.get("verifiedAnswerKey"), "visualTranscript": transcript, "solution": solution, "visualAssetHashes": {ref: digest(args.source.parent / ref) for ref in item.get("image_url") or []}}
        content_hash = canonical_json_hash(content)
        request = V2ClassificationRequest(
            questionId=diagnostic_qid, contentVersion=2, contentHash=content_hash,
            subjectTrack=checkpoint.get("subjectTrack", "regular"),
            grade=grade, topic=f"Matematika {('Tingkat Lanjut ' if checkpoint.get('subjectTrack') == 'tl' else '')}{rubric.education_level} Kelas {grade}", subtopic=item.get("subbab_id"),
            questionType="multiple_choice", stimulus=item.get("stimulus"), stem=item["soal_text"],
            options=[{"label": o["option_id"], "text": o["text"]} for o in item["options"]],
            verifiedMinimalSolution=solution, detectedKko=detect_kko(item["soal_text"]), visualTranscript=transcript,
            provenanceStatus={"contentQualified": structure["status"] == "pass" and aggregate.get("contentStatus") == "valid", "answerKeyVerified": aggregate.get("answerKeyStatus") == "verified", "solutionVerified": bool(solution) and aggregate.get("answerKeyStatus") == "verified", "visualEssential": bool(item.get("image_url")), "visualTranscriptVerified": bool(transcript)},
        )
        serialized = serialize_question(request, representation=model["inputRepresentation"])
        tokens = len(runtime.tokenizer(serialized, truncation=False)["input_ids"])
        started = time.perf_counter()
        prediction = runtime.predict(request).model_dump(mode="json")
        prediction["questionId"] = qid
        latency = round((time.perf_counter() - started) * 1000, 3)
        for head in HEADS:
            verify_probability(prediction[head])
        qversion = f"{qid}:content-v2:blind-revalidation"
        questions.append({
            "questionId": qid, "questionVersionId": qversion, "contentVersion": 2, "contentHash": content_hash,
            "grade": grade, "topic": request.topic, "subtopic": request.subtopic, "questionType": request.questionType,
            "stem": request.stem, "stimulus": request.stimulus, "options": [o.model_dump() for o in request.options],
            "visualAssets": item.get("image_url") or [], "visualAssetHashes": content["visualAssetHashes"], "visualTranscript": transcript,
            "verifiedMinimalSolution": solution, "verificationProvenance": "ai_silver",
            "detectedKko": request.detectedKko, "privateAnswerSpecification": {"answerKey": item.get("jawaban"), "verifiedAnswerKey": aggregate.get("verifiedAnswerKey"), "answerKeyStatus": aggregate.get("answerKeyStatus"), "visibility": "restricted"},
            "source": {"externalId": external_id, "subchapter": item.get("subbab_id"), "assetBasePath": args.source.parent.as_posix(), "optionExtractionNotes": {o["option_id"]: o.get("alasan") for o in item["options"] if o.get("alasan")}},
        })
        runs, votes = [], {}
        for run in record.get("runs") or []:
            output = run.get("output") or {}
            runs.append({**{k: v for k, v in run.items() if k != "output"}, "contentStatus": output.get("contentStatus"), "contentConcerns": output.get("contentConcerns") or [], "answerKeyStatus": output.get("answerKeyStatus"), "verifiedAnswerKey": output.get("verifiedAnswerKey"), "verifiedMinimalSolution": output.get("verifiedMinimalSolution"), "visualTranscript": output.get("visualTranscript"), "heads": {h: {**(output.get(h) or {}), "reasoningSummary": (output.get(h) or {}).get("rationale")} for h in HEADS}})
        for head in HEADS:
            initial = Counter((r.get("heads", {}).get(head) or {}).get("label") for r in runs if r["status"] == "success" and (r.get("heads", {}).get(head) or {}).get("action") == "classify")
            largest = max(initial.values(), default=0)
            pattern = "unanimous_3_0" if largest == 3 else "majority_2_of_3" if largest == 2 else "no_consensus"
            votes[head] = {"status": (aggregate.get("heads", {}).get(head) or {}).get("status", "incomplete"), "votePattern": pattern, "requestedRuns": 3, "successfulRuns": sum(r["status"] == "success" for r in runs), "requiredVotes": 2, "supportingVotes": largest, "voteCounts": dict(initial), "advisoryLabel": labels[head], "initialMajorityLabel": initial.most_common(1)[0][0] if largest >= 2 else None, "policy": "unanimity_else_ai_adjudication", "lockedEvidence": select_evidence(record, head, labels[head])}
        comparison = {h: {"modelLabel": prediction[h]["label"], "blindLabel": labels[h], "agreement": prediction[h]["label"] == labels[h] if labels[h] is not None and prediction[h]["label"] is not None else None} for h in HEADS}
        decision_id = "AID-" + canonical_json_hash({"qid": qid, "contentHash": content_hash, "checkpointHash": audit["checkpointSha256"]})[:24]
        decisions.append({
            "decisionId": decision_id, "workflowRunId": "WF-" + audit["checkpointSha256"][:24],
            "questionId": qid, "questionVersionId": qversion, "contentVersion": 2, "contentHash": content_hash,
            "decisionType": "blind_silver_advisory", "inputValidation": structure,
            "featureManifest": {"grade": grade, "topic": request.topic, "subtopic": request.subtopic, "questionType": request.questionType, "detectedKko": request.detectedKko, "serializedInput": serialized, "untruncatedTokenCount": tokens, "maxLength": model["maxLength"], "wouldTruncate": tokens > model["maxLength"]},
            "indobert": {"diagnosticOnly": True, "diagnosticInferenceQuestionId": diagnostic_qid, "heads": {h: prediction[h] for h in HEADS}, "trace": prediction["trace"], "scopeStatus": prediction["scopeStatus"], "reviewRequired": True, "latencyMs": latency},
            "llmAdvisory": {"provider": checkpoint["provider"], "model": checkpoint["model"], "promptVersion": checkpoint["promptVersion"], "rubricVersion": checkpoint["rubricVersion"], "method": "blind_n3_with_ai_adjudication", "blindToModelPredictions": True, "requestedRuns": 3, "requiredVotes": 2, "successfulRuns": sum(r["status"] == "success" for r in runs), "contentAssessment": {"status": aggregate.get("contentStatus"), "concerns": aggregate.get("contentConcerns") or []}, "answerKeyAssessment": {"status": aggregate.get("answerKeyStatus"), "verifiedAnswerKey": aggregate.get("verifiedAnswerKey")}, "runs": runs, "votes": votes, "adjudication": record.get("adjudication"), "advisoryLabels": labels, "eligibleForTraining": aggregate.get("eligibleForTraining", False), "labelProvenance": "ai_silver"},
            "labelProvenance": "ai_silver", "reviewMode": "automated_ai", "finalRouting": route,
            "modelComparison": comparison, "blindCheckpointHash": audit["checkpointSha256"], "createdAt": created,
        })
        decisions[-1]["llmAdvisory"]["retryHistory"] = record.get("retryHistory") or []
        predictions.append({"index": index, "questionId": qid, "diagnosticInferenceQuestionId": diagnostic_qid, "questionVersionId": qversion, "contentHash": content_hash, "serializedInput": serialized, "untruncatedTokenCount": tokens, "maxLength": model["maxLength"], "wouldTruncate": tokens > model["maxLength"], "latencyMs": latency, "prediction": prediction})
        print(f"diagnostic={index}/{len(source)} route={route}", flush=True)
    summary = {"itemCount": len(decisions), "routingCounts": dict(Counter(d["finalRouting"] for d in decisions)), "labelProvenance": "ai_silver", "silverReadyCount": sum(d["finalRouting"] == "silver_ready" for d in decisions), "advisoryLabelDistributions": {h: dict(Counter(d["llmAdvisory"]["advisoryLabels"][h] or "undecided" for d in decisions)) for h in HEADS}, "contentQualifiedAdvisoryLabelDistributions": {h: dict(Counter(d["llmAdvisory"]["advisoryLabels"][h] or "undecided" for d in decisions if d["finalRouting"] == "silver_ready")) for h in HEADS}, "modelDisagreementCounts": {h: sum(d["modelComparison"][h]["agreement"] is False for d in decisions) for h in HEADS}}
    for distribution_key in ("advisoryLabelDistributions", "contentQualifiedAdvisoryLabelDistributions"):
        for head, labels in HEAD_LABELS.items():
            for label in labels:
                summary[distribution_key][head].setdefault(label, 0)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    grouped = difficulty_groups(questions, decisions, grade)
    if checkpoint.get("subjectTrack") == "tl":
        grouped["subjectTrack"] = "tl"
    write(args.output_dir / "difficulty_groups.json", grouped)
    (args.output_dir / "difficulty").mkdir()
    for label, items in grouped["groups"].items():
        write(args.output_dir / "difficulty" / f"{label}.json", {
            "schemaVersion": "blind-difficulty-subset-v1", "sourceClass": grade,
            "subjectTrack": checkpoint.get("subjectTrack", "regular"),
            "intendedDifficulty": None if label == "undecided" else label,
            "researchOnly": True, **grouped["summary"][label], "items": items,
        })
    write(args.output_dir / "questions.json", {"schemaVersion": "question-validation-input-v2-blind", "createdAt": created, "visibility": "restricted_contains_answer_key", "items": questions})
    write(args.output_dir / "validation_results.json", {"schemaVersion": "ai-decision-bundle-v2-blind", "collectionTarget": "ai_decisions", "createdAt": created, "sourceClass": checkpoint["sourceGrade"], "subjectTrack": checkpoint.get("subjectTrack", "regular"), "summary": summary, "items": decisions})
    write(args.output_dir / "indobert_predictions.json", {"schemaVersion": "indobert-blind-diagnostics-v1", "createdAt": created, "researchOnlyRun": True, "reviewRequired": True, "blindDecisionLockedAt": audit["generatedAt"], "artifact": args.artifact.as_posix(), "model": model, "summary": {"itemCount": len(predictions), "predictionDistribution": {h: dict(Counter(x["prediction"][h]["label"] or "abstain" for x in predictions)) for h in HEADS}}, "items": predictions})
    (args.output_dir / "LAPORAN_VALIDASI.md").write_text(render_report(questions, decisions, summary, checkpoint, model, output_dir=args.output_dir), encoding="utf-8")
    readme = f"# Hasil validasi ulang kelas 1\n\nModel LLM: `{checkpoint['model']}`; metode blind N=3, rubrik kelas sasaran, verifikasi kunci/solusi, dan adjudikasi AI bila diperlukan. Label terkunci sebelum diagnostik IndoBERT.\n\nGunakan [validation_results.json](validation_results.json) untuk data hasil dan `items[].llmAdvisory.advisoryLabels` bersama `finalRouting`. Baca [LAPORAN_VALIDASI.md](LAPORAN_VALIDASI.md) untuk soal, perhitungan confidence/entropy, tiga suara, profil difficulty, adjudikasi, serta hasil akhir per soal. [questions.json](questions.json) memuat sumber dan spesifikasi jawaban terbatas; [indobert_predictions.json](indobert_predictions.json) memuat diagnostik model lama.\n\nDistribusi: `{json.dumps(summary['advisoryLabelDistributions'], ensure_ascii=False)}`. Routing: `{json.dumps(summary['routingCounts'], ensure_ascii=False)}`.\n\nToken sukses tercatat: {checkpoint['summary']['totalTokens']:,}; tidak ada API call pada packaging. Provider dapat mencatat lebih banyak usage dari percobaan yang tidak menghasilkan output valid. Label tetap silver AI; CTT/IRT belum dihitung. IndoBERT belum dilatih ulang dan hasil diagnostiknya tidak menentukan label blind.\n\nAudit tidak menyetujui ekspansi/training bila gate belum lolos. Gate batch: `{json.dumps(audit['gates'], ensure_ascii=False)}`.\n"
    readme = readme.replace("# Hasil validasi ulang kelas 1", f"# Hasil validasi ulang kelas {grade}")
    readme = readme.replace("memuat diagnostik model lama", "memuat diagnostik artifact yang dipilih").replace(
        "IndoBERT belum dilatih ulang dan hasil diagnostiknya tidak menentukan label blind.",
        f"Artifact diagnostik `{model['modelVersion']}` memakai dataset `{model.get('datasetSnapshot', 'tidak tercatat')}`. "
        "Packaging ini tidak melatih atau mempromosikan model; diagnostik tidak menentukan label blind.",
    )
    if checkpoint.get("subjectTrack") == "tl":
        readme += "\nMata pelajaran: Matematika Tingkat Lanjut (TL), dengan rubrik khusus TL.\n"
    completion_note = batch_completion_note(checkpoint, len(source))
    if completion_note:
        readme = readme.replace(
            f"# Hasil validasi ulang kelas {grade}\n",
            f"# Hasil validasi ulang kelas {grade}\n\n{completion_note}\n",
            1,
        )
    if not model_in_scope(model, grade, checkpoint.get("subjectTrack", "regular")):
        readme += f"\nKelas {grade} memakai rubrik {rubric.education_level}. Artifact diagnostik berada di luar cakupan kelas/jalur ini: semua head abstain dengan label/confidence/entropy null dan probabilitas kosong. Tidak ada prediksi atau perbandingan ketepatan IndoBERT untuk kelas/jalur ini; label akhir mengikuti penilaian blind Gemini.\n"
    readme += "\nKelompok difficulty tersedia di [difficulty_groups.json](difficulty_groups.json), [Easy](difficulty/Easy.json), [Medium](difficulty/Medium.json), dan [Hard](difficulty/Hard.json). `contentQualified` hanya menandai soal tanpa blocker konten; soal silver_ready dapat masuk snapshot operasional. Kategori kosong tetap diekspor. Item tanpa keputusan tersedia di [undecided](difficulty/undecided.json).\n"
    (args.output_dir / "README.md").write_text(readme, encoding="utf-8")
    filenames = ["questions.json", "validation_results.json", "indobert_predictions.json", "LAPORAN_VALIDASI.md", "README.md", "difficulty_groups.json", *[f"difficulty/{label}.json" for label in grouped["groups"]]]
    write(args.output_dir / "manifest.json", {
        "schemaVersion": "validation-bundle-manifest-v2-blind", "createdAt": created,
        "class": checkpoint["sourceGrade"], "offlineBuild": True, "newLlmCalls": 0,
        "operationalPolicyVersion": POLICY_VERSION, "labelProvenance": "ai_silver",
        "reviewMode": "automated_ai", "method": "blind_n3_with_ai_adjudication_then_offline_model_diagnostics",
        "historicalBlindRecordedTokens": checkpoint["summary"]["totalTokens"],
        "historicalBlindSuccessfulRuns": checkpoint["summary"]["successfulRuns"],
        "blindDecisionLockedAt": audit["generatedAt"], "readyForExpansion": audit["readyForExpansion"],
        "modelDiagnostic": {"artifact": args.artifact.as_posix(), "modelVersion": model["modelVersion"],
                            "supportedGrades": model.get("supportedGrades", list(range(1, 7))),
                            "supportedSubjectTracks": model.get("supportedSubjectTracks", ["regular"]),
                            "servable": runtime.manifest.servable},
        "sourceFiles": {name: {"path": path.as_posix(), "sha256": digest(path)}
                        for name, path in (("source", args.source), ("blindCheckpoint", args.checkpoint), ("blindAudit", args.audit))},
        "outputs": {name: {"sha256": digest(args.output_dir / name), "bytes": (args.output_dir / name).stat().st_size} for name in filenames},
        "limitations": ["Operational labels use AI silver provenance.",
                        "N=3 and adjudication use one Gemini model; repeated judgments are correlated.",
                        "IndoBERT diagnostic outputs do not change the locked AI silver decisions.",
                        "Packaging performs no training, model promotion, student delivery, CTT or IRT."],
    })
    from scripts.compact_validation_results import compact_bundle
    compact_bundle(args.source, args.output_dir)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
