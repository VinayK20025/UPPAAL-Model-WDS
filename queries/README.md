# Query Files

The seven top-level `.q` files correspond by basename to the seven XML models under `models/`. Formula order and meaning should be checked against the embedded XML `<queries>` blocks.

Run a model/query pair from the repository root with the installed verifier, for example:

```bash
verifyta models/Baseline_CPS_WDS.xml queries/Baseline_CPS_WDS.q
```

For auditable batch execution, use:

```bash
python scripts/run_verification.py --verifyta /path/to/verifyta
```

Diagnostic formulas that the selected verifier/model combination cannot currently evaluate are retained under `queries/diagnostic/` and are not part of the automated top-level query sets. In particular, the advanced timed model's deadlock-freedom formula is preserved there after the observed UPPAAL 5.0.0 compatibility error. Its source XML query remains unchanged.

The presence of a query file does not mean that the verifier has been run against the current model commit. Check `results/reproduced/verification-manifest.json` and the raw logs for fresh evidence.
