"""Prepare/generate a visual pilot; validation requires separate manifest approval."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.services.exercise import config as C
from app.services.exercise.workflow import (atomic_json, batch_lock, begin_generation, load,
    approve_validation, validation_allowed)
from app.services.exercise.visual_plan import preflight, make_plan


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("preflight", "plan", "generate", "status", "approve-validation"))
    parser.add_argument("--book", choices=[f"kelas{n}" for n in range(1, 13)] + ["kelas11_tl", "kelas12_tl"], required=True)
    parser.add_argument("--batch", type=int, default=2)
    parser.add_argument("--bab", type=int)
    parser.add_argument("--subbab")
    parser.add_argument("--total", type=int, default=30)
    parser.add_argument("--visual-percent", type=int, default=70)
    parser.add_argument("--max-api-calls", type=int, default=12)
    parser.add_argument("--manifest-sha256")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if args.batch < 1:
        parser.error("batch must be positive")
    base = Path(C.OUT_ROOT) / args.book / f"batch{args.batch:02d}"
    if args.command == "preflight":
        result = preflight(args.book)
        atomic_json(ROOT / "runs/exercise_visual" / f"preflight_{args.book}.json", result)
    elif args.command == "plan":
        if args.bab is None or args.subbab is None:
            parser.error("plan requires --bab and --subbab from the verified curriculum")
        plan = make_plan(args.book, args.batch, args.bab, args.subbab.upper(), total=args.total,
                         visual_percent=args.visual_percent)
        with batch_lock(base):
            existing = base / "generation_plan.json"
            if existing.exists() and load(existing) != plan:
                raise ValueError("existing immutable allocation differs; choose a new batch")
            begin_generation(base, args.book, args.batch)
            atomic_json(existing, plan)
        result = {"plan": str(existing), "allocation": plan["slots"], "total": plan["total"],
                  "validationStatus": "validation_pending", "newApiCalls": 0}
    elif args.command == "generate":
        if not args.execute:
            parser.error("generate makes generation-only API calls and requires --execute")
        from app.llm.ninerouter import NineRouterSettings
        from app.services.exercise.generation import generate_plan
        result = generate_plan(base, NineRouterSettings.from_environment(), args.max_api_calls)
    elif args.command == "approve-validation":
        if not args.manifest_sha256:
            parser.error("approve-validation requires the reported --manifest-sha256")
        result = approve_validation(base, args.manifest_sha256)
        # Mark readiness without making an API call or starting training.
        from scripts.nightly_pipeline import mark_ready
        mark_ready(args.book, f"batch{args.batch:02d}")
    else:
        result = {"class": args.book, "batch": f"batch{args.batch:02d}", "validationAllowed": validation_allowed(base),
                  "state": load(base / "generation_state.json") if (base / "generation_state.json").exists() else None,
                  "manifest": load(base / "generation_manifest.json") if (base / "generation_manifest.json").exists() else None,
                  "newApiCalls": 0}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") != "waiting_for_sources" else 2


if __name__ == "__main__":
    raise SystemExit(main())
