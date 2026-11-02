# Reproduction protocol

Complete this protocol from the actual verification environment. Do not retain placeholders in the final archival release.

## 1. Artifact identity

- Model file: `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml`
- Git commit: [record commit SHA]
- Model SHA-256: [compute and record]
- UPPAAL version/build: [record]
- Operating system/architecture: [record]
- Verification settings/options: [record]
- Run date: [record]

## 2. Full query execution

1. Open the exact model file in the recorded UPPAAL version.
2. Export/transcribe the complete query list.
3. Recover Q9 from the original authoring project or run archive if it is part of the intended suite; do not invent a replacement.
4. Execute every intended query and save the complete report.
5. Preserve counterexample traces for failed properties and witness traces for key reachability properties.
6. Record the tool-reported status and performance data for every query.
7. Reconcile query formulas and outcomes with the manuscript's property table.

## 3. Minimum per-query record

| Field | Required content |
|---|---|
| Query ID | Stable identifier |
| Formula | Exact UPPAAL expression |
| Property class | Reachability, invariant, leads-to/liveness, etc. |
| Informal meaning | Claim being assessed |
| Outcome | Exact UPPAAL result |
| Runtime/memory | Tool-reported, when available |
| Evidence path | Report, witness or counterexample |
| Revision | Git commit and model checksum |

## 4. Suggested results layout

Use `results/<model-id>/<run-id>/` and include `environment.txt`, `model.sha256`, `queries.q`, `results.csv`, `verification-report.txt` and exported files under `traces/`.

Do not create placeholder traces that could be mistaken for actual UPPAAL output.

## 5. Simulation package

If randomized simulation is reported, publish:
- source code and dependencies;
- random-number generator and seed policy;
- every seed or deterministic seed-generation procedure;
- attack-selection and parameter distributions;
- relation between simulator ticks and UPPAAL time units;
- whether the simulator is independent or reimplements the same operational semantics;
- raw per-run outputs and analysis scripts;
- statistical interpretation distinguishing observed frequencies from formal probabilities.

## 6. Release discipline

Create a tagged release after model, query suite, results, simulator and manuscript tables agree. Include a checksum manifest and update the manuscript's artifact citation to the release/tag or archival DOI.
