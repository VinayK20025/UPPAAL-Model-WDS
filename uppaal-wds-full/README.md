# UPPAAL Models for Water Distribution Cyber–Physical Systems

This repository contains seven reference UPPAAL XML models for a water distribution system (WDS), their extracted query files, a machine-readable inherited-query inventory, modelling notes and reproducibility guidance.

## Repository layout

```text
.
├── models/reference/       # Original supplied XML models; keep unchanged
├── models/derived/         # Reviewed variants, with lineage notes
├── queries/inherited/      # Formulae extracted from source XML
├── queries/catalogue.md    # Query inventory and interpretation
├── results/inherited/      # Historical XML annotations, not fresh runs
├── results/reproduced/     # Fresh verifier records and raw output
├── docs/                   # Model lineage, assumptions, scope, reproducibility
├── metamodel/              # Assumption-aware WDS/CPS metamodel
├── semantics/              # Assumption semantics and timed-automata mapping
├── scripts/                # XML validation and inventory extraction
├── tests/                  # Validation guidance
└── experiments/configs/    # Experiment configuration guidance
```

## Reference models and query counts

| Model | Query count | Focus |
|---|---:|---|
| `Baseline_CPS_WDS.xml` | 2 | Tank, sensor, PLC and pump baseline |
| `CPS_WDS_Secuity_Framework.xml` | 7 | Network and IDS security framework |
| `CPS_WDS_With_Attacks.xml` | 5 | Attack-enabled model: FDI, replay and DoS behaviours |
| `CPS_WDS_With_Defence.xml` | 3 | Defensive response and safe mode |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | 5 | Timed AI/IDS and operator response |
| `Advanced_CPS_WDS.xml` | 1 | Expanded monitoring, twin, watchdog and backup control |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | 30 | Advanced timed multi-component model |
| **Total** | **53** | |

The original spelling `Secuity` in one filename is preserved for source traceability.

## Quick start

1. Install UPPAAL and record the exact version/build.
2. Open a model under `models/reference/` in the UPPAAL GUI, or run the verifier.
3. Use the corresponding `.q` file under `queries/inherited/`.
4. Preserve the exact command, model/query SHA-256 hashes, tool version and raw output.

Example command:

```bash
verifyta -t 1 models/reference/Baseline_CPS_WDS.xml queries/inherited/Baseline_CPS_WDS.q
```

This is a reproducibility instruction, not evidence that the command has been run in this repository.

## Evidence interpretation

The 53 formulae were extracted from the XML query blocks. The source XMLs contain 20 `success`, 6 `failure`, and 27 `NOT_RECORDED` historical result annotations. These annotations are retained as **inherited source metadata**, not current UPPAAL executions. Fresh runs belong in `results/reproduced/` and must include complete provenance.

UPPAAL `E<> p` expresses existential reachability; it is not an inevitability guarantee. A reachable alarm does not establish complete attack detection, and a reachable recovery state does not establish inevitable recovery. Failed properties and counterexamples must be preserved and discussed.

See `docs/source-model-audit.md`, `docs/query-and-property-guide.md` and `docs/reproducibility.md` before making claims based on the models.

## Licence

No licence is asserted in this repository. Confirm ownership and reuse conditions for every supplied model and dependency before adding a licence.
