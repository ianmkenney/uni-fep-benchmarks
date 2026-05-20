#!/usr/bin/env python3

import json
from pathlib import Path

from libufb.loader import load_benchmarks
from libufb.models import InferenceExperimentSettings

file_path = "data/uni_fep_benchmarks.json"

print("Loading benchmarks")
benchmarks = load_benchmarks(file_path)
print(f"Loaded {len(benchmarks)} benchmarks")

results_dir = Path() / "results"
results_dir.mkdir(exist_ok=True)

for benchmark in benchmarks:
    query_data = benchmark.to_openfold3_query()
    benchmark_dir = results_dir / benchmark.name
    benchmark_dir.mkdir(exist_ok=True)

    # We don't want to mess up the inputs for previous results
    if (benchmark_dir / "output").exists():
        print(f"Found results for: {benchmark_dir}")
        continue

    with open(benchmark_dir / "queries.json", "w") as f:
        json.dump(query_data, f, indent=4)

    InferenceExperimentSettings.with_random_seeds(5).write_yaml(benchmark_dir / "runner.yml")
