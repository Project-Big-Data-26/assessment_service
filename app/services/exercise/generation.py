"""Generation-only execution: no solver, validation client, IRT or training."""
from pathlib import Path

import httpx

from app.llm.ninerouter import NineRouterClient, NineRouterError
from .workflow import atomic_json, load


class GenerationStopped(RuntimeError):
    pass


class BudgetedGenerator(NineRouterClient):
    """Count actual requests, including the underlying client's retry attempts."""
    def __init__(self, settings, base, max_calls, **kwargs):
        if type(max_calls) is not int or not 1 <= max_calls <= 100:
            raise ValueError("generation request limit must be 1..100 for the pilot")
        super().__init__(settings, **kwargs)
        self.budget_path = Path(base) / "generation_budget.json"
        self.maximum = max_calls
        self.attempts = load(self.budget_path).get("apiAttempts", 0) if self.budget_path.exists() else 0

    def _chat_once(self, payload, started):
        if self.attempts >= self.maximum:
            raise GenerationStopped("generation API request budget exhausted; candidates are preserved")
        self.attempts += 1
        atomic_json(self.budget_path, {"apiAttempts": self.attempts, "maxApiCalls": self.maximum,
                                    "purpose": "generation_only"})
        try:
            return super()._chat_once(payload, started)
        except NineRouterError as exc:
            if isinstance(exc.__cause__, httpx.HTTPStatusError):
                code = exc.__cause__.response.status_code
                if code in (401, 403, 429, 503):
                    raise GenerationStopped(f"generator stopped on HTTP {code}; validation was not started") from None
            raise


def generate_plan(base, settings, max_calls=12):
    from . import config as C
    from .export import export_batch
    from .llm_generate import Job, generate
    from .visual_plan import verify_plan
    from .workflow import batch_lock, begin_generation
    base = Path(base)
    with batch_lock(base):
        plan = verify_plan(load(base / "generation_plan.json"))
        book, batch = plan["class"], int(plan["batch"][5:])
        expected = Path(C.OUT_ROOT) / book / plan["batch"]
        if base.resolve() != expected.resolve():
            raise ValueError("plan must live in its matching exercise batch")
        begin_generation(base, book, batch)
        stopped = None
        from .llm_generate import GenerateError
        with BudgetedGenerator(settings, base, max_calls) as client:
            for slot in plan["slots"]:
                job = Job(book, slot["bab_no"], slot["subbab"], slot["level"], batch,
                          C.OUT_ROOT, slot["visual"], slot["count"], slot["visual"])
                try:
                    result = generate(job, client)
                    if result.errors:
                        stopped = "candidate_local_checks_incomplete"
                except GenerationStopped as exc:
                    stopped = str(exc)
                    break
                except GenerateError:
                    stopped = "generator_or_source_failed_local_checks"
                    break
            attempts = client.attempts
        result = export_batch(book, batch, generation_only=True, _locked=True)
        return {**result, "apiAttempts": attempts, "stopReason": stopped,
                "validationApiCalls": 0, "validationStatus": "validation_pending"}
