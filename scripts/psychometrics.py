"""Offline analysis and local pilot operations; never calls LLM/cloud APIs."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from dotenv import load_dotenv

from app.assessment.contracts import AssessmentCreate
from app.assessment.store import AssessmentStore
from app.classification.v2.serializer import canonical_json_hash
from app.psychometrics.analysis import analyze_matrix, load_policy
from app.psychometrics.contracts import MatrixAnalysisInput, ScreeningInput
from app.psychometrics.irt import response_probability
from app.training.v2.dataset import DatasetSnapshot


def simulated_matrix(model: str = "rasch", *, persons: int | None = None, items: int | None = None, seed: int = 42):
    policy = load_policy()
    persons = persons or {"rasch": 180, "2pl": 400, "3pl": 1200}[model]
    items = items or {"rasch": 12, "2pl": 16, "3pl": 24}[model]
    rng = np.random.default_rng(seed)
    b = np.linspace(-2, 2, items)
    a = np.ones(items) if model == "rasch" else rng.uniform(0.7, 1.8, items)
    c = np.full(items, 0.2) if model == "3pl" else np.zeros(items)
    theta = rng.normal(size=persons)
    probabilities = response_probability(theta[:, None], a, b, c)
    scores = (rng.random((persons, items)) < probabilities).astype(int)
    missing = rng.random((persons, items)) < 0.04
    payload = MatrixAnalysisInput(
        populationId="SIMULATED-NOT-STUDENT-DATA", assessmentFamily=f"synthetic-{model}", grade=1,
        items=[{"questionId": f"demo-{index}", "questionVersionId": f"demo-{index}:v1", "contentVersion": 1,
                "contentHash": canonical_json_hash({"syntheticItem": index}), "intendedDifficulty": "Medium"} for index in range(items)],
        subjectIds=[f"simulated-{index}" for index in range(persons)],
        matrix=[[None if missing[row, column] else int(scores[row, column]) for column in range(items)] for row in range(persons)],
        model=model, dataOrigin="synthetic",
        assumptionReview={"reviewedBy": "synthetic-generator", "evidence": "Simulation from one N(0,1) latent trait and independent Bernoulli draws; not evidence from real students.",
                          "unidimensional": True, "localIndependence": True, "representativeSample": True},
    )
    return payload, {"a": a.tolist(), "b": b.tolist(), "c": c.tolist(), "seed": seed}


def save_new(path, document):
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as handle:
        json.dump(document, handle, ensure_ascii=False, indent=2, allow_nan=False)


def main():
    load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=False)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", default="configs/psychometrics_policy.json")
    commands = parser.add_subparsers(dest="command", required=True)
    demo = commands.add_parser("demo", help="Generate explicitly synthetic data and test the numerical pipeline")
    demo.add_argument("--model", choices=["rasch", "2pl", "3pl"], default="rasch")
    demo.add_argument("--persons", type=int)
    demo.add_argument("--items", type=int)
    demo.add_argument("--seed", type=int, default=42)
    demo.add_argument("--output", required=True)
    analyze = commands.add_parser("analyze", help="Analyze a trusted offline 0/1/null matrix")
    analyze.add_argument("--input", required=True)
    analyze.add_argument("--output", required=True)
    create = commands.add_parser("create-assessment", help="Freeze a local human-gold snapshot as a pilot blueprint")
    create.add_argument("--gold-snapshot", required=True)
    create.add_argument("--assessment-config", required=True)
    create.add_argument("--db", default=os.getenv("ASSESSMENT_DB_PATH", "data/local/assessments.sqlite3"))
    create.add_argument("--output", required=True)
    participant = commands.add_parser("create-participant", help="Issue a private bearer token for a pilot participant")
    participant.add_argument("--assessment-id", required=True)
    participant.add_argument("--participant-code", required=True)
    participant.add_argument("--db", default=os.getenv("ASSESSMENT_DB_PATH", "data/local/assessments.sqlite3"))
    participant.add_argument("--output", required=True)
    screen = commands.add_parser("screen", help="Aggregate real completed pilot sessions into an immutable snapshot")
    screen.add_argument("--request", required=True, help="ScreeningInput JSON, including assumption review")
    screen.add_argument("--db", default=os.getenv("ASSESSMENT_DB_PATH", "data/local/assessments.sqlite3"))
    screen.add_argument("--output", required=True)
    args = parser.parse_args()
    if Path(args.output).exists():
        parser.error("output already exists; choose a new immutable artifact path")
    policy = load_policy(args.policy)
    if args.command == "demo":
        if (args.persons is not None and args.persons <= 0) or (args.items is not None and args.items <= 0):
            parser.error("persons and items must be positive")
        payload, truth = simulated_matrix(args.model, persons=args.persons, items=args.items, seed=args.seed)
        result = {"analysis": analyze_matrix(payload, policy), "simulationTruth": truth, "input": payload.model_dump(mode="json")}
    elif args.command == "analyze":
        payload = MatrixAnalysisInput.model_validate_json(Path(args.input).read_text(encoding="utf-8"))
        if payload.dataOrigin == "server_scored":
            parser.error("use screen for server-scored events; external matrix provenance is not server-scored")
        result = analyze_matrix(payload, policy)
    elif args.command == "create-assessment":
        payload = AssessmentCreate.model_validate_json(Path(args.assessment_config).read_text(encoding="utf-8"))
        snapshot = DatasetSnapshot.model_validate_json(Path(args.gold_snapshot).read_text(encoding="utf-8"))
        result = AssessmentStore(args.db, subject_secret=os.getenv("ASSESSMENT_SUBJECT_SECRET") or None).create_assessment(payload, snapshot)
    elif args.command == "create-participant":
        result = AssessmentStore(args.db, subject_secret=os.getenv("ASSESSMENT_SUBJECT_SECRET") or None).participant(args.assessment_id, args.participant_code)
    else:
        payload = ScreeningInput.model_validate_json(Path(args.request).read_text(encoding="utf-8"))
        result = AssessmentStore(args.db, subject_secret=os.getenv("ASSESSMENT_SUBJECT_SECRET") or None).screen(payload, policy)
    save_new(args.output, result)
    print(f"Saved {args.command} result to {args.output}")
    analysis = result.get("analysis", result)
    if "irt" in analysis:
        print(f"IRT {analysis['irt']['model']}: {analysis['irt']['status']}; readiness={analysis['readiness']['passed']}; researchOnly=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
