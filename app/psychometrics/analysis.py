"""CTT, response cleaning, readiness gates, and advisory empirical feedback."""
from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path

import numpy as np

from app.classification.v2.serializer import canonical_json_hash
from app.evaluation.psychometrics import wilson_interval
from .contracts import AnalysisPolicy, MatrixAnalysisInput
from .irt import fit_irt

POLICY_PATH = Path(__file__).resolve().parents[2] / "configs" / "psychometrics_policy.json"


def load_policy(path: str | Path = POLICY_PATH) -> AnalysisPolicy:
    return AnalysisPolicy.model_validate_json(Path(path).read_text(encoding="utf-8"))


def normalize_events(events: list[dict], *, items: list[dict], subject_ids: list[str],
                     population_id: str, assessment_family: str, grade: int,
                     attempt_policy: str = "first", model: str = "rasch", assumption_review=None) -> tuple[MatrixAnalysisInput, dict]:
    """Clean trusted, server-scored events. Conflicting response IDs are excluded.

    The service first chooses a whole completed session per subject; this
    function resolves duplicate cells within that chosen administration.
    """
    if attempt_policy not in {"first", "last"}:
        raise ValueError("attempt policy must be first or last")
    versions = {item["questionVersionId"]: item for item in items}
    subjects = set(subject_ids)
    exclusions = Counter()
    by_response = {}
    conflicts = set()
    for event in events:
        response_id = event.get("responseId")
        if not isinstance(response_id, str) or not response_id:
            exclusions["malformed_event"] += 1
            continue
        if response_id in by_response:
            if by_response[response_id] == event:
                exclusions["duplicate_event"] += 1
            else:
                conflicts.add(response_id)
                exclusions["conflicting_response_id"] += 1
        else:
            by_response[response_id] = event
    cells = {}
    for response_id, event in by_response.items():
        if response_id in conflicts:
            continue
        item = versions.get(event.get("questionVersionId"))
        if item is None or any(event.get(key) != item.get(key) for key in ("questionId", "contentVersion", "contentHash")):
            exclusions["version_mismatch"] += 1
            continue
        if (event.get("populationId") != population_id or event.get("assessmentFamily") != assessment_family
                or event.get("grade") != grade or event.get("subjectHash") not in subjects):
            exclusions["population_or_subject_mismatch"] += 1
            continue
        if event.get("validForAnalysis") is not True or "rapid_guess_candidate" in event.get("flags", []):
            exclusions["invalid_or_rapid_guess"] += 1
            continue
        correct = event.get("isCorrect")
        if correct is not None and type(correct) is not bool:
            exclusions["invalid_score"] += 1
            continue
        if event.get("scoringStatus") not in {"scored", "skipped"}:
            exclusions["unscored_event"] += 1
            continue
        if (event["scoringStatus"] == "skipped") != (correct is None):
            exclusions["invalid_score"] += 1
            continue
        try:
            timestamp = datetime.fromisoformat(event["submittedAt"])
            if timestamp.utcoffset() is None:
                raise ValueError("timestamp lacks timezone")
        except (KeyError, TypeError, ValueError):
            exclusions["malformed_timestamp"] += 1
            continue
        cell = (event["subjectHash"], event["questionVersionId"])
        if cell in cells:
            exclusions["repeated_cell"] += 1
            previous_time = cells[cell][0]
            if (attempt_policy == "first" and timestamp >= previous_time) or (attempt_policy == "last" and timestamp <= previous_time):
                continue
        cells[cell] = (timestamp, event)
    matrix = [[None if (subject, item["questionVersionId"]) not in cells
               or cells[(subject, item["questionVersionId"])][1]["isCorrect"] is None
               else int(cells[(subject, item["questionVersionId"])][1]["isCorrect"])
               for item in items] for subject in subject_ids]
    payload = MatrixAnalysisInput(populationId=population_id, assessmentFamily=assessment_family,
                                  grade=grade, items=items, subjectIds=subject_ids, matrix=matrix,
                                  model=model, dataOrigin="server_scored", assumptionReview=assumption_review)
    selected_events = [value[1] for value in cells.values()]
    return payload, {"inputEvents": len(events), "selectedEvents": len(selected_events),
                     "exclusions": dict(exclusions), "attemptPolicy": attempt_policy,
                     "events": selected_events}


def _correlation(left, right):
    if len(left) < 8 or np.std(left) == 0 or np.std(right) == 0:
        return None
    return float(np.corrcoef(left, right)[0, 1])


def _connected(observed: np.ndarray) -> bool:
    graph = observed.astype(int).T @ observed.astype(int) > 0
    visited = {0}; pending = [0]
    while pending:
        current = pending.pop()
        for neighbor in np.flatnonzero(graph[current]):
            if int(neighbor) not in visited:
                visited.add(int(neighbor)); pending.append(int(neighbor))
    return len(visited) == graph.shape[0]


def analyze_matrix(payload: MatrixAnalysisInput, policy: AnalysisPolicy | None = None, *, events: list[dict] | None = None) -> dict:
    policy = policy or load_policy()
    matrix = np.array([[np.nan if value is None else value for value in row] for row in payload.matrix], dtype=float)
    observed = ~np.isnan(matrix)
    # Never zero-impute for CTT total-score joins or KR-20.
    complete = matrix[observed.all(axis=1)]
    totals = complete.sum(axis=1)
    item_results = []
    for index, item in enumerate(payload.items):
        answers = matrix[observed[:, index], index]
        total = len(answers)
        correct = int(answers.sum())
        p = float(answers.mean()) if total else None
        ci = list(wilson_interval(correct, total)) if total else None
        empirical = None if p is None else "Easy" if p > policy.easyP else "Hard" if p < policy.hardP else "Medium"
        flags = []
        if total < policy.minResponsesPerItem:
            flags.append("insufficient_item_sample")
        if ci and ci[1] - ci[0] > policy.maxCiWidth:
            flags.append("wide_difficulty_interval")
        if total and correct in {0, total}:
            flags.append("no_response_variation")
        correlation = _correlation(complete[:, index], totals - complete[:, index]) if len(complete) else None
        discrimination = None
        if len(complete) >= 8:
            rest = totals - complete[:, index]
            low, high = np.quantile(rest, [0.27, 0.73])
            if low < high:
                discrimination = float(complete[rest >= high, index].mean() - complete[rest <= low, index].mean())
        if (correlation is not None and correlation < 0) or (discrimination is not None and discrimination < 0):
            flags.append("negative_discrimination")
        intended = item.intendedDifficulty.value if item.intendedDifficulty is not None else None
        stable_band = None
        if ci:
            stable_band = "Easy" if ci[0] > policy.easyP else "Hard" if ci[1] < policy.hardP else "Medium" if ci[0] >= policy.hardP and ci[1] <= policy.easyP else None
        if intended and stable_band and intended != stable_band:
            flags.append("intended_empirical_disagreement")
        item_events = [event for event in events or [] if event["questionVersionId"] == item.questionVersionId and event.get("isCorrect") is not None]
        times = [event["responseTimeMs"] for event in item_events if event.get("responseTimeMs") is not None]
        selections = {option: sum(option in event.get("selectedInternalOptionIds", []) for event in item_events) for option in item.optionIds}
        distractors = [option for option in item.optionIds if option != item.answerKey] if item.answerKey else []
        non_functioning = [option for option in distractors if item_events and selections[option] / len(item_events) < policy.distractorMinRate]
        if non_functioning:
            flags.append("non_functioning_distractor")
        reference = item.model_dump(mode="json", exclude={"answerKey", "optionIds"})
        item_results.append({**reference, "ctt": {
            "validResponseCount": total, "correctCount": correct, "difficultyIndex": p,
            "difficultyCi95": ci, "empiricalDifficulty": empirical,
            "discrimination": discrimination, "correctedPointBiserial": correlation,
            "totalScoreJoin": "complete_cases_only", "totalScoreSample": len(complete),
            "missingRate": 1 - total / len(matrix),
            "optionSelectionCounts": selections if item_events else None,
            "distractorEfficiency": 1 - len(non_functioning) / len(distractors) if distractors and item_events else None,
            "nonFunctioningDistractors": non_functioning,
            "medianResponseTimeMs": float(np.median(times)) if times else None,
            "responseTimeIqrMs": float(np.subtract(*np.percentile(times, [75, 25]))) if times else None,
        }, "reviewFlags": flags, "irt": None})

    person_keep = observed.mean(axis=1) >= 1 - policy.maxPersonMissingRate
    fit_matrix = matrix[person_keep]
    fit_observed = observed[person_keep]
    failures = []
    if len(fit_matrix) < policy.minPersons[payload.model]:
        failures.append("insufficient_persons")
    if matrix.shape[1] < policy.minItems[payload.model]:
        failures.append("insufficient_items")
    coverage = float(observed.mean())
    fit_coverage = float(fit_observed.mean()) if len(fit_observed) else 0.0
    if fit_coverage < policy.minCoverage:
        failures.append("insufficient_coverage")
    for index in range(matrix.shape[1]):
        values = fit_matrix[fit_observed[:, index], index]
        if len(values) < policy.minResponsesPerItem:
            failures.append(f"item_{index}:insufficient_responses")
        if np.sum(values == 0) < policy.minOutcomeCount or np.sum(values == 1) < policy.minOutcomeCount:
            failures.append(f"item_{index}:insufficient_outcome_variation")
    if not len(fit_observed) or not _connected(fit_observed):
        failures.append("disconnected_response_design")
    assumptions = payload.assumptionReview
    if assumptions is None:
        failures.append("assumptions_not_reviewed")
    elif not (assumptions.unidimensional and assumptions.localIndependence and assumptions.representativeSample):
        failures.append("assumptions_not_supported")
    irt = {"status": "waiting_for_data", "model": payload.model, "items": [], "persons": [], "warnings": []}
    if "assumptions_not_reviewed" in failures or "assumptions_not_supported" in failures:
        irt["status"] = "waiting_for_assumption_review"
    if not failures:
        try:
            irt = fit_irt(fit_matrix, payload.model, policy)
            for item, parameters in zip(item_results, irt["items"], strict=True):
                item["irt"] = parameters
                if not irt["converged"]:
                    item["reviewFlags"].append("irt_not_converged")
                if parameters["infit"] > 1.5 or parameters["outfit"] > 1.5:
                    item["reviewFlags"].append("irt_misfit_candidate")
            for person, subject in zip(irt["persons"], np.array(payload.subjectIds)[person_keep], strict=True):
                person["subjectId"] = str(subject)
            # Residual Q3 is a screening diagnostic, not proof of independence.
            from .irt import response_probability
            parameters = irt["items"]
            eap = np.array([person["thetaEap"] for person in irt["persons"]])
            predicted = response_probability(eap[:, None], [p["a"] for p in parameters], [p["b"] for p in parameters], [p["c"] for p in parameters])
            residual = fit_matrix - predicted
            q3 = []
            for left in range(matrix.shape[1]):
                for right in range(left + 1, matrix.shape[1]):
                    paired = ~np.isnan(residual[:, left]) & ~np.isnan(residual[:, right])
                    value = _correlation(residual[paired, left], residual[paired, right]) if paired.sum() >= 30 else None
                    if value is not None:
                        q3.append((left, right, value))
            average_q3 = float(np.mean([pair[2] for pair in q3])) if q3 else None
            suspect_pairs = [{"left": payload.items[left].questionVersionId, "right": payload.items[right].questionVersionId,
                              "adjustedQ3": value - average_q3} for left, right, value in q3 if value - average_q3 > 0.2]
            irt["localDependenceScreen"] = {"meanQ3": average_q3, "suspectPairs": suspect_pairs}
            if suspect_pairs:
                irt["warnings"].append("local_dependence_candidate")
                irt["status"] = "estimated_with_warnings"
        except (FloatingPointError, np.linalg.LinAlgError) as exc:
            irt = {"status": "failed", "model": payload.model, "items": [], "persons": [], "warnings": [str(exc)]}

    kr20 = None
    if matrix.shape[1] >= 2 and len(complete) >= 8 and np.var(totals, ddof=1) > 0:
        # Sample item variances and total variance use the same denominator.
        kr20 = float(matrix.shape[1] / (matrix.shape[1] - 1) * (1 - np.var(complete, axis=0, ddof=1).sum() / np.var(totals, ddof=1)))
    for item in item_results:
        weak = {"insufficient_item_sample", "wide_difficulty_interval", "no_response_variation"} & set(item["reviewFlags"])
        item["recommendedRouting"] = "collect_more_events" if weak else "ai_review" if {"negative_discrimination", "non_functioning_distractor", "irt_misfit_candidate"} & set(item["reviewFlags"]) else "observation_only"
    return {
        "schemaVersion": "empirical-analysis-v1", "policyVersion": policy.policyVersion,
        "policyHash": canonical_json_hash(policy.model_dump(mode="json")),
        "policy": policy.model_dump(mode="json"),
        "populationId": payload.populationId, "assessmentFamily": payload.assessmentFamily, "grade": payload.grade,
        "dataOrigin": payload.dataOrigin, "researchOnly": True, "reviewRequired": any(item["recommendedRouting"] == "ai_review" for item in item_results), "reviewMode": "automated_ai", "labelProvenance": "ai_silver",
        "matrixHash": canonical_json_hash(payload.model_dump(mode="json")),
        "normalization": {"persons": len(matrix), "items": matrix.shape[1], "observedCells": int(observed.sum()),
                          "missingCells": int((~observed).sum()), "coverage": coverage,
                          "excludedPersonsForIrt": int((~person_keep).sum()), "missingScore": None},
        "readiness": {"passed": not failures, "failures": failures, "eligiblePersons": len(fit_matrix), "coverage": fit_coverage,
                      "assumptionReview": assumptions.model_dump(mode="json") if assumptions else None},
        "ctt": {"kr20": kr20, "completeCaseCount": len(complete), "reliabilityMethod": "complete_case_sample_variances",
                "warnings": ["negative_reliability"] if kr20 is not None and kr20 < 0 else []},
        "items": item_results, "irt": irt,
    }
