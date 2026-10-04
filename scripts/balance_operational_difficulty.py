"""Export relative thirds for operational use, preserving blind AI evidence.

These are quota-based categories within each class bank, not new Gemini labels
or empirical IRT difficulty. No active validation bundle or training is changed.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.silver.exports import SCORE_POLICY, final_label_support, load_decision_bundle, ai_validation_path
from scripts.generate_silver_labels_kelas1 import atomic_write
from scripts.refresh_ai_validation_reports import verify_bundle

CLASSES = [(f"kelas{grade}", grade, "regular") for grade in range(1, 13)] + [
    ("kelas11_tl", 11, "tl"), ("kelas12_tl", 12, "tl")]
BALANCE_POLICY_VERSION = "relative-operational-balance-v2"
ALLOWED_OPERATIONAL_CHANGES = {"cognitive_level", "cognitive_score", "confidence_score"}


def profile_score(profile: dict) -> float:
    """Transparent heuristic; not a validated rubric score or IRT estimate."""
    if not profile:
        raise ValueError("a recorded evidence profile is required")
    return (max(0, profile["dependentSteps"] - 1)
            + {"familiar_routine": 0, "routine_selection": 1, "nonroutine_strategy": 2}[profile["routineStatus"]]
            + int(profile["strategySelection"]) + int(profile["representationTransfer"])
            + profile["interactingConstraints"]
            + min(4, max(0, profile["relevantInformationUnits"] - 1)) * 0.25
            + {"low": 0, "moderate": 0.5, "high": 1}[profile["calculationLoad"]]
            - {"none": 0, "partial": 0.5, "strong": 1}[profile["scaffoldLevel"]])


def allocate(rows: list[dict], decisions: list[dict]) -> tuple[list[dict], dict]:
    by_id = {decision["questionId"]: decision for decision in decisions}
    if len(by_id) != len(decisions) or len({str(row["_id"]) for row in rows}) != len(rows) or set(by_id) != {str(row["_id"]) for row in rows}:
        raise ValueError("source and audited decision coverage differs")
    ranked = []
    for ordinal, row in enumerate(rows):
        if row["status"] != "active":
            continue
        decision = by_id[str(row["_id"])]
        if decision["finalRouting"] != "silver_ready":
            raise ValueError("active content must be qualified")
        profile = decision["llmAdvisory"]["votes"]["intendedDifficulty"]["lockedEvidence"].get("profile")
        ranked.append((profile_score(profile), ordinal, profile))
    ranked.sort(key=lambda item: (item[0], item[1]))
    quotient, remainder = divmod(len(ranked), 3)
    targets = {label: quotient + int(index < remainder)
               for index, label in enumerate(("easy", "medium", "hard"))}
    outputs = deepcopy(rows)
    evidence, boundaries = [], []
    cursor = 0
    for label, count in targets.items():
        if cursor and count and ranked[cursor - 1][0] == ranked[cursor][0]:
            boundaries.append({"between": [outputs[ranked[cursor - 1][1]]["cognitive_level"], label],
                               "score": ranked[cursor][0], "equalProfileScoreSplit": True})
        for score, ordinal, profile in ranked[cursor:cursor + count]:
            original = rows[ordinal]
            decision = deepcopy(by_id[str(original["_id"])])
            decision["llmAdvisory"]["advisoryLabels"]["intendedDifficulty"] = label.title()
            support = final_label_support(decision)
            confidence = round(100 * min(support.values()) / decision["llmAdvisory"]["requestedRuns"])
            outputs[ordinal].update(cognitive_level=label,
                                    cognitive_score=SCORE_POLICY["mapping"][label.title()],
                                    confidence_score=confidence)
            evidence.append({"questionId": original["_id"], "rank": len(evidence) + 1,
                             "profileScore": score, "profile": profile,
                             "originalDifficulty": original["cognitive_level"],
                             "originalConfidence": original["confidence_score"],
                             "operationalDifficulty": label, "aiSupportConfidence": confidence,
                             "supportingRunsPerHead": support,
                             "requestedRuns": decision["llmAdvisory"]["requestedRuns"],
                             "labelChanged": label != original["cognitive_level"],
                             "provenance": "relative_bank_quota", "eligibleForAiSilverTraining": False})
        cursor += count
    return outputs, {"targets": targets, "activeQuestionCount": len(ranked),
                     "changedLabels": sum(item["labelChanged"] for item in evidence),
                     "zeroAiSupportLabels": sum(item["aiSupportConfidence"] == 0 for item in evidence),
                     "tieBoundaries": boundaries, "items": evidence}


def _canonical_hash(value: dict | list) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def _file_info(path: Path) -> dict:
    contents = path.read_bytes()
    return {"sha256": hashlib.sha256(contents).hexdigest(), "bytes": len(contents)}


def _safe_output_name(output_name: str) -> None:
    if (not output_name or output_name in (".", "..")
            or any(character in output_name for character in "\\/:")):
        raise ValueError("output_name must be one directory name")


def _require_export_child(path: Path, export_root: Path) -> None:
    resolved, root = path.resolve(), export_root.resolve()
    if resolved == root or not resolved.is_relative_to(root):
        raise ValueError("operational version path must remain inside its export directory")


def verify_operational_export(directory: Path) -> dict:
    """Verify immutable files and recompute quotas from the retained AI audit."""
    directory = Path(directory)
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    if manifest["schemaVersion"] != BALANCE_POLICY_VERSION:
        raise ValueError("unsupported operational balance manifest")
    expected_files = {"validation_results.json", "balance_audit.json", "ai_validation_results.json",
                      "ai_decisions.json", "source_manifest.json", "README.md"}
    if set(manifest["outputs"]) != expected_files:
        raise ValueError("operational export manifest coverage differs")
    for name, info in manifest["outputs"].items():
        if _file_info(directory / name) != info:
            raise ValueError(f"operational export checksum differs: {name}")
    originals = json.loads((directory / "ai_validation_results.json").read_text(encoding="utf-8"))
    decisions = json.loads((directory / "ai_decisions.json").read_text(encoding="utf-8"))
    actual = json.loads((directory / "validation_results.json").read_text(encoding="utf-8"))
    audit = json.loads((directory / "balance_audit.json").read_text(encoding="utf-8"))
    expected, allocation = allocate(originals, decisions["items"])
    if actual != expected or any(audit[key] != value for key, value in allocation.items()):
        raise ValueError("operational export differs from retained AI evidence")
    identity = {"policyVersion": BALANCE_POLICY_VERSION,
                "sourceQuestionHash": manifest["sourceQuestionHash"],
                "sourceValidationResultsHash": _canonical_hash(originals),
                "sourceDecisionAuditHash": _canonical_hash(decisions),
                "grade": audit["grade"], "subjectTrack": audit["subjectTrack"]}
    if manifest.get("identity") != identity or _canonical_hash(identity) != manifest["sourceFingerprint"]:
        raise ValueError("operational export source fingerprint differs")
    for original, output in zip(originals, actual):
        if original.keys() != output.keys() or any(
                original[key] != output[key] for key in original if key not in ALLOWED_OPERATIONAL_CHANGES):
            raise ValueError("operational export changed source content or eligibility")
    return manifest


def export_verified_operational_balance(
    source: Path, bundle: Path, *, grade: int, track: str,
    output_name: str = "operational_balance_v2",
) -> dict:
    """Export a complete verified AI bundle to an immutable relative-label version.

    The same source questions, validated rows, decisions and policy reuse an existing
    export after verifying it. Changed AI evidence creates another version. The
    current.json pointer is replaceable; the evidence versions are immutable.
    No Gemini request, AI-bundle mutation, training or IRT fit occurs here.
    """
    source, bundle = Path(source).resolve(), Path(bundle).resolve()
    _safe_output_name(output_name)
    if grade not in range(1, 13) or track not in {"regular", "tl"} or (track == "tl" and grade not in (11, 12)):
        raise ValueError("unsupported grade or subject track")
    verify_bundle(source, bundle)
    ai_path = ai_validation_path(bundle)
    input_bytes = ai_path.read_bytes()
    rows = json.loads(input_bytes)
    if not isinstance(rows, list):
        raise ValueError("operational balancing requires a source-shaped validated array")
    decisions = load_decision_bundle(bundle)
    source_manifest_bytes = (bundle / "manifest.json").read_bytes()
    source_manifest = json.loads(source_manifest_bytes)
    if source_manifest["databaseExport"]["sourceClass"] != grade:
        raise ValueError("source AI bundle grade differs")
    if source_manifest["databaseExport"].get("subjectTrack", "regular") != track:
        raise ValueError("source AI bundle subject track differs")
    balanced, evidence = allocate(rows, decisions["items"])
    identity = {"policyVersion": BALANCE_POLICY_VERSION,
                "sourceQuestionHash": _file_info(source)["sha256"],
                "sourceValidationResultsHash": _canonical_hash(rows),
                "sourceDecisionAuditHash": _canonical_hash(decisions),
                "grade": grade, "subjectTrack": track}
    fingerprint = _canonical_hash(identity)
    export_root = source.parent / output_name
    destination = export_root / f"source_{fingerprint}"
    created = not destination.exists()
    if created:
        export_root.mkdir(parents=True, exist_ok=True)
        staging = export_root / f".pending_{uuid.uuid4().hex}"
        _require_export_child(staging, export_root)
        staging.mkdir()
        try:
            atomic_write(balanced, staging / "validation_results.json")
            (staging / "ai_validation_results.json").write_bytes(input_bytes)
            atomic_write(decisions, staging / "ai_decisions.json")
            (staging / "source_manifest.json").write_bytes(source_manifest_bytes)
            metadata = {"schemaVersion": BALANCE_POLICY_VERSION, "class": source.parent.name,
                        "grade": grade, "subjectTrack": track, "sourceAiBundle": str(bundle),
                        "sourceValidationResultsByteHash": hashlib.sha256(input_bytes).hexdigest(),
                        "sourceFingerprint": fingerprint,
                        "rubricVersions": sorted({d["llmAdvisory"]["rubricVersion"] for d in decisions["items"]}),
                        "meaning": "Relative thirds of this class's active bank; not absolute intended difficulty.",
                        "quotaBased": True, "empiricalIrtCalibration": False,
                        "heuristicValidated": False, "newGeminiCalls": 0,
                        "activeValidationModified": False, "usedForTraining": False,
                        "tiePolicy": "Equal scores may cross categories; original source order breaks ties to meet quotas.",
                        "confidencePolicy": "Actual original blind-run support for the operational label; can be zero.",
                        "inactivePolicy": "Inactive content retains original label, score, confidence and inactive status.",
                        **evidence}
            atomic_write(metadata, staging / "balance_audit.json")
            (staging / "README.md").write_text(
                "# Kategori operasional relatif\n\n"
                "Array validation_results.json membagi soal aktif berdasarkan profil bukti menjadi tiga kelompok mendekati sama banyak.\n"
                "Hard berarti kelompok dengan ranking tertinggi dalam bank kelas ini; label ini relatif dan tidak menyatakan Gemini menilai seluruh soal itu Hard.\n"
                "balance_audit.json mencatat skor heuristik, kuota, dukungan run AI dan batas kategori yang memotong skor sama.\n"
                "confidence_score memakai dukungan run AI asli terhadap label operasional, sehingga dapat 0.\n"
                "ai_validation_results.json dan ai_decisions.json mempertahankan label serta bukti keputusan AI asli.\n"
                "Versi ini tidak mengubah bundle AI, status aktif, isi soal, data training atau kalibrasi IRT.\n",
                encoding="utf-8")
            filenames = ("validation_results.json", "balance_audit.json", "ai_validation_results.json",
                         "ai_decisions.json", "source_manifest.json", "README.md")
            atomic_write({"schemaVersion": BALANCE_POLICY_VERSION,
                          "createdAt": datetime.now(timezone.utc).isoformat(),
                          "sourceFingerprint": fingerprint, "sourceQuestionHash": identity["sourceQuestionHash"],
                          "identity": identity,
                          "outputs": {name: _file_info(staging / name) for name in filenames}},
                         staging / "manifest.json")
            verify_operational_export(staging)
            if (ai_path.read_bytes() != input_bytes
                    or (bundle / "manifest.json").read_bytes() != source_manifest_bytes
                    or _file_info(source)["sha256"] != identity["sourceQuestionHash"]):
                raise RuntimeError("source AI bundle changed while building operational export")
            _require_export_child(staging, export_root)
            _require_export_child(destination, export_root)
            staging.rename(destination)
        finally:
            if staging.exists():
                _require_export_child(staging, export_root)
                shutil.rmtree(staging)
    manifest = verify_operational_export(destination)
    if manifest["sourceFingerprint"] != fingerprint:
        raise ValueError("existing operational export belongs to another source")
    result = {"class": source.parent.name, "directory": str(destination),
              "validationResults": str(destination / "validation_results.json"),
              "sourceFingerprint": fingerprint, "created": created,
              "activeDistribution": evidence["targets"], "activeQuestionCount": evidence["activeQuestionCount"],
              "changedLabels": evidence["changedLabels"], "zeroAiSupportLabels": evidence["zeroAiSupportLabels"],
              "provenance": "relative_bank_quota", "newGeminiCalls": 0,
              "sourceAiBundleUnchanged": True}
    atomic_write(result, export_root / "current.json")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--class-name", action="append")
    parser.add_argument("--output-name", default="operational_balance_v1")
    args = parser.parse_args()
    if Path(args.output_name).name != args.output_name or args.output_name in (".", ".."):
        parser.error("output-name must be one directory name")
    if args.class_name and set(args.class_name) - {entry[0] for entry in CLASSES}:
        parser.error("unknown class-name")
    selected = [entry for entry in CLASSES if not args.class_name or entry[0] in args.class_name]
    overview = ROOT / "output/pretest" / f"{args.output_name}_summary.json"
    if overview.exists() or any((ROOT / "output/pretest" / name / args.output_name).exists()
                                for name, _, _ in selected):
        raise FileExistsError("choose a new output-name; preserve previous balance exports")
    entries = []
    for name, grade, track in selected:
        source = ROOT / "output/pretest" / name / "soal_pretest_db.json"
        bundle = source.parent / "hasil_validasi"
        destination = source.parent / args.output_name
        if destination.exists():
            raise FileExistsError("choose a new output-name; preserve previous balance exports")
        verify_bundle(source, bundle)
        input_bytes = ai_validation_path(bundle).read_bytes()
        rows = json.loads(input_bytes)
        decisions = load_decision_bundle(bundle)["items"]
        balanced, evidence = allocate(rows, decisions)
        destination.mkdir()
        atomic_write(balanced, destination / "validation_results.json")
        metadata = {"schemaVersion": "relative-operational-balance-v1", "class": name,
                    "grade": grade, "subjectTrack": track, "source": str(bundle),
                    "sourceValidationResultsHash": hashlib.sha256(input_bytes).hexdigest(),
                    "rubricVersions": sorted({d["llmAdvisory"]["rubricVersion"] for d in decisions}),
                    "meaning": "Relative thirds of this class's active bank; not absolute intended difficulty.",
                    "quotaBased": True, "empiricalIrtCalibration": False,
                    "heuristicValidated": False, "newGeminiCalls": 0,
                    "activeValidationModified": False, "usedForTraining": False,
                    "tiePolicy": "Equal scores may cross categories; original source order breaks ties to meet quotas.",
                    "confidencePolicy": "Actual original blind-run support for the operational label; can be zero.",
                    "inactivePolicy": "Inactive content retains original label, score, confidence and inactive status.",
                    **evidence}
        atomic_write(metadata, destination / "balance_audit.json")
        (destination / "README.md").write_text(
            "# Kategori operasional relatif\n\n"
            "Array ini membagi soal aktif menjadi tiga kelompok berdasarkan profil bukti dan kuota.\n"
            "Hard berarti sepertiga dengan ranking tertinggi dalam bank kelas ini; bukan validasi baru bahwa soal itu Hard.\n"
            "Skor heuristik dan batas kategori yang memotong skor sama dicatat di balance_audit.json.\n"
            "confidence_score dihitung dari dukungan run AI asli terhadap label operasional, sehingga dapat 0.\n"
            "Hasil validasi aktif, bukti Gemini dan data training asli tetap tersedia di hasil_validasi.\n"
            "IRT empiris tidak dihitung. Ekspor ini tidak otomatis dipakai untuk training atau delivery.\n",
            encoding="utf-8")
        assert ai_validation_path(bundle).read_bytes() == input_bytes
        entries.append({"class": name, "directory": str(destination),
                        "activeDistribution": evidence["targets"], "changedLabels": evidence["changedLabels"],
                        "zeroAiSupportLabels": evidence["zeroAiSupportLabels"]})
    if not entries:
        parser.error("no requested class exists")
    atomic_write({"provenance": "relative_bank_quota", "newGeminiCalls": 0, "classes": entries}, overview)
    print(json.dumps(entries, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
