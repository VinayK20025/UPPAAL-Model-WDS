# Reproducibility Procedure

## 1. Canonical paths

Run commands from the repository root.

- Models: `models/<model-name>.xml`
- Executable query sets: `queries/<model-name>.q`
- Timed AI/Human diagnostics: `queries/CPS_WDS_Industry5_AI_Human_Timed_Verification_Diagnostic.q`
- Diagnostic queries that are not supported by the current verifier/model combination: `queries/diagnostic/`
- Verification runner: `scripts/run_verification.py`
- Fresh evidence: `results/reproduced/`

The nested UPPAAL distribution directory, if present, is an executable installation and is not a source-model directory. Do not commit licence keys or licence files.

## 2. Validate source XML

```bash
python scripts/validate_models.py
```

This parses the top-level XML models and counts embedded query elements. It does not execute UPPAAL or establish semantic correctness.

## 3. Confirm verifier access and licence

For a local UPPAAL installation:

```bash
VERIFYTA="$PWD/uppaal-5.0.0-linux64/bin/verifyta"
"$VERIFYTA" -h
```

Use the actual path returned by `find` if the executable is elsewhere. Confirm that the active licence explicitly covers the verifier before starting a batch run. A message such as `License does not cover verifier` is an execution/licensing failure, not a model result.

## 4. Run all model/query pairs with an evidence manifest

```bash
python scripts/run_verification.py --verifyta "$VERIFYTA"
```

Run one model only:

```bash
python scripts/run_verification.py --verifyta "$VERIFYTA" --model Baseline_CPS_WDS
```

The runner records per-model raw output, process return code, timestamps, exact command, platform, model/query SHA-256 hashes and formula outcomes. It generates `verification-manifest.json` and `ALL_MODELS_VERIFICATION_REPORT.md`. The report generator reads no existing logs, so it cannot ingest itself or confuse stale report output with current executions.

## 5. Interpret execution status separately from property outcome

- `COMPLETED_ALL_REPORTED_SATISFIED`: every formula outcome printed by the verifier was satisfied. Confirm the number of formula outcomes matches the executable query file.
- `COMPLETED_WITH_VIOLATIONS`: the verifier completed and at least one property was not satisfied. Preserve and inspect the counterexample.
- `COMPLETED_WITH_UNKNOWN`: the verifier reported an inconclusive result.
- `INCOMPLETE_OR_NO_FORMULA_RESULT`: no complete set of formula outcomes was obtained.
- `EXECUTION_ERROR`: licence, compatibility, invocation or runtime error.
- `MISSING_QUERY`: no matching top-level query file.

A zero process exit code alone is not proof that every property passed. A non-zero exit code or missing formula outcome must never be converted into a satisfied result.

## 6. Deadlock-query compatibility note

The observed UPPAAL 5.0.0 verifier rejected the advanced timed model's `A[] not deadlock` formula with: `Cannot handle deadlock predicate for models with priorities or guarded broadcast receivers.` The formula has therefore been removed from that model's executable batch query file and preserved in `queries/diagnostic/CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced_deadlock.q`. The XML source query remains unchanged as provenance. This exclusion is not a proof of deadlock freedom.

The separate `Advanced_CPS_WDS.q` file also contains only a deadlock-freedom query. Its run must be inspected independently; if the verifier does not return an explicit formula result, classify it as incomplete rather than passing.

## 7. Separate inherited annotations from fresh evidence

Historical annotations embedded in XML are source metadata, not fresh verifier runs. The runner does not import them. Do not label a result reproduced unless the exact model/query pair was executed with a recorded tool environment and raw output.

## 8. Counterexample review

For each unsatisfied property, preserve the trace and record the initial state, enabled transitions, attack/channel state, physical/control consequence and violated predicate or missed deadline. Do not weaken a property merely to make it pass. Explain any modelling assumptions on which the counterexample depends.
