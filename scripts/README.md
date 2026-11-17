# Repository Scripts

Run scripts from the repository root.

- `python scripts/validate_models.py` parses all top-level `models/*.xml` files and reports embedded query counts. It does not execute UPPAAL.
- `python scripts/extract_inherited_results.py` extracts formulae and inherited XML result annotations into `queries/extracted/` and `results/inherited/query-inventory.json`. It does not execute UPPAAL; extracted outcomes are historical metadata.
- `python scripts/run_verification.py --verifyta /path/to/verifyta` executes each matching top-level model/query pair and records raw logs, exit codes, timestamps, SHA-256 input hashes, formula outcomes and a consolidated Markdown report under `results/reproduced/`. Set the `VERIFYTA` environment variable instead of passing `--verifyta` if preferred. Use `--model <basename>` to run one model.

The verification runner does not treat missing output, licence errors or compatibility errors as successful verification. Unsatisfied properties are reported as completed runs with violations; preserve and inspect their counterexamples. It does not rewrite models or queries.
