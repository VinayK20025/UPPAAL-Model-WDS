# Reproducibility Procedure

## 1. Preserve inputs

Keep supplied XML files unchanged under `models/reference/`. Create modified variants under `models/derived/` and document their lineage.

## 2. Validate and extract

From the repository root:

```bash
python scripts/validate_models.py
python scripts/extract_inherited_results.py
```

## 3. Run UPPAAL

Record the exact UPPAAL version/build and execute the verifier against a declared model/query pair. Example:

```bash
verifyta -t 1 models/reference/Baseline_CPS_WDS.xml queries/inherited/Baseline_CPS_WDS.q
```

The command is illustrative only. Do not treat it as a completed run.

## 4. Record every fresh run

For each run, preserve model and query paths, SHA-256 hashes, UPPAAL version/build, OS, exact command, working directory, start/end time, exit status, raw stdout/stderr and per-query result. Store the run record and raw outputs under `results/reproduced/`.

Hash inputs with:

```bash
sha256sum models/reference/Baseline_CPS_WDS.xml queries/inherited/Baseline_CPS_WDS.q
```

## 5. Separate evidence classes

`results/inherited/` contains historical XML annotations. `results/reproduced/` is reserved for fresh executions with complete provenance. Do not overwrite or relabel inherited outcomes.

## 6. Counterexample review

For each failed property, preserve the trace and identify the initial state, enabled transitions, adversary/channel state, physical/control consequence and violated predicate or missed deadline. Explain whether the behaviour depends on a modelling assumption.
