"""Measure offline startup, p50/p95 inference latency, and process peak RSS."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

import numpy as np
import psutil

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.classification.v2.runtime import V2ClassifierRuntime
from app.training.v2.dataset import DatasetSnapshot


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--iterations", type=int, default=50)
    args = parser.parse_args()
    process = psutil.Process()
    rss_before = process.memory_info().rss
    started = time.perf_counter()
    runtime = V2ClassifierRuntime(args.artifact)
    startup_seconds = time.perf_counter() - started
    startup_rss = process.memory_info().rss
    snapshot = DatasetSnapshot.model_validate_json(Path(args.snapshot).read_text(encoding="utf-8"))
    if not snapshot.rows:
        raise SystemExit("snapshot has no SD rows")
    latencies = []
    peak_rss = startup_rss
    for index in range(args.iterations):
        request = snapshot.rows[index % len(snapshot.rows)].inference_request()
        before = time.perf_counter()
        runtime.predict(request)
        latencies.append((time.perf_counter() - before) * 1000)
        peak_rss = max(peak_rss, process.memory_info().rss)
    report = {
        "device": "cpu",
        "workers": 1,
        "modelVersion": runtime.manifest.modelVersion,
        "architectureVersion": runtime.manifest.architectureVersion,
        "routingPolicyVersion": runtime.manifest.routingPolicyVersion,
        "startupSeconds": startup_seconds,
        "latencyMilliseconds": {
            "p50": float(np.percentile(latencies, 50)),
            "p95": float(np.percentile(latencies, 95)),
            "samples": len(latencies),
        },
        "rssMegabytes": {
            "beforeLoad": rss_before / 1024**2,
            "afterLoad": startup_rss / 1024**2,
            "peak": peak_rss / 1024**2,
        },
    }
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"CPU benchmark written to {destination}.")


if __name__ == "__main__":
    main()
