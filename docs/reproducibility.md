# Reproducibility

Run from the repository root with Python 3.10+ and a licensed UPPAAL `verifyta` binary.

```bash
python scripts/validate_models.py
VERIFYTA=/path/to/uppaal/bin/verifyta
"$VERIFYTA" -h
python scripts/run_verification.py --verifyta "$VERIFYTA"
```

For a single model, add `--model Baseline_CPS_WDS`. The runner records exact command, model/query hashes, timestamps, verifier help/version, process return code and raw output under `results/reproduced/`. It must distinguish property violations, unknown/incomplete outcomes, unsupported queries and execution/licence errors. Check expected formula counts and inspect counterexamples before making claims. Do not commit licence credentials. Historical XML result annotations are not new verifier runs.
