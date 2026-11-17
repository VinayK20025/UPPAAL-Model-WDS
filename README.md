# UPPAAL Models for Water Distribution Cyber–Physical Systems

This repository contains seven supplied UPPAAL timed-automata models for a water distribution system (WDS), with extracted queries, a source audit, metamodel documentation and reproducibility guidance.

## Structure

- `models/reference/`: seven original XML models, preserved unchanged.
- `queries/inherited/`: query files extracted from each XML model.
- `queries/catalogue.md`: query catalogue.
- `results/inherited/query-inventory.json`: machine-readable inventory of formulas and embedded source annotations.
- `results/reproduced/`: reserved for fresh verifier runs.
- `metamodel/` and `semantics/`: assumption-aware modelling and timed-automata mapping.
- `docs/`: source audit, scope/claims and reproducibility.
- `scripts/`: XML validation and query/result extraction.

## Models and query counts

| Model | Queries |
|---|---:|
| `Baseline_CPS_WDS.xml` | 2 |
| `CPS_WDS_Secuity_Framework.xml` | 7 |
| `CPS_WDS_With_Attacks.xml` | 5 |
| `CPS_WDS_With_Defence.xml` | 3 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | 5 |
| `Advanced_CPS_WDS.xml` | 1 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | 30 |
| **Total** | **53** |

The spelling `Secuity` is retained in the source filename for traceability.

## Validate and extract

```bash
python scripts/validate_models.py
python scripts/extract_inherited_results.py
```

Run a model with the UPPAAL verifier (record the installed tool version):

```bash
verifyta -t 1 models/reference/Baseline_CPS_WDS.xml queries/inherited/Baseline_CPS_WDS.q
```

This is an example command, not a claim of a fresh run.

## Evidence interpretation

The source XMLs contain 53 query formulas. Embedded historical annotations comprise 20 `success`, 6 `failure`, and 27 `NOT_RECORDED`. These are inherited XML annotations, not newly reproduced verifier results. Preserve fresh runs separately with the tool version, command, model/query SHA-256 hashes, exit status and raw output.

UPPAAL `E<>` denotes existential reachability, not inevitability. A reachable alarm does not prove complete attack detection, and a reachable recovery state does not prove guaranteed recovery. Failed properties and counterexamples must remain documented.

See `docs/source-model-audit.md`, `docs/scope-and-claims.md` and `docs/reproducibility.md`.

## Licence

No licence is asserted until ownership and reuse conditions for all model artefacts have been confirmed.
