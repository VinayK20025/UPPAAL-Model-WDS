# Reproducibility Procedure

## 1. Canonical paths

Run all commands from the repository root. The current top-level layout is authoritative:

- Models: `models/<model-name>.xml`
- Queries: `queries/<model-name>.q`
- Documentation: `docs/`
- Validation scripts: `scripts/`

The nested `uppaal-wds-full/` directory is an earlier package snapshot and is not used by the current top-level scripts or commands.

## 2. Validate the source XML

```bash
python scripts/validate_models.py
```

This parses the top-level XML files and reports embedded query counts. It does not execute UPPAAL or prove that models are semantically correct.

## 3. Run UPPAAL

Record the exact UPPAAL version/build and execute the verifier against a declared model/query pair. Example:

```bash
verifyta -t 1 models/Baseline_CPS_WDS.xml queries/Baseline_CPS_WDS.q
```

This command is illustrative only. Do not treat it as a completed run.

## 4. Record every fresh run

For each run, preserve model and query paths, SHA-256 hashes, UPPAAL version/build, OS, exact command, working directory, start/end time, exit status, raw stdout/stderr and per-query result. Store fresh run records in a clearly named results directory introduced for that purpose; do not mix them with inherited source annotations.

Hash inputs with:

```bash
sha256sum models/Baseline_CPS_WDS.xml queries/Baseline_CPS_WDS.q
```

## 5. Separate evidence classes

Historical annotations embedded in XML are source metadata, not freshly reproduced verifier records. A result must not be labelled reproduced unless the exact model/query pair has been run using a recorded tool version and its raw output has been retained.

## 6. Counterexample review

For each failed property, preserve the trace and identify the initial state, enabled transitions, adversary/channel state, physical/control consequence and violated predicate or missed deadline. Explain whether the behaviour depends on a modelling assumption.
