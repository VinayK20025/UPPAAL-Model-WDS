# Fresh verification evidence

Run `python scripts/run_verification.py --verifyta /path/to/verifyta` from the repository root after confirming that the active licence covers the verifier.

The runner regenerates per-model raw `.log` files, `verification-manifest.json`, `verifyta-help.txt`, and `ALL_MODELS_VERIFICATION_REPORT.md`. It records return codes, timestamps, model/query SHA-256 hashes and formula outcomes. It does not ingest its own report or historical XML annotations. A completed run with unsatisfied properties is a completed verification with violations, not a passing run.

The advanced timed model's `A[] not deadlock` formula is retained under `queries/diagnostic/` because the observed UPPAAL 5.0.0 verifier rejects deadlock predicates for models with priorities or guarded broadcast receivers. This is a verifier compatibility limitation, not evidence of deadlock freedom. The original XML query block remains unchanged as provenance.

Do not commit licence keys. Preserve counterexample traces for unsatisfied properties.
