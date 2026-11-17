# UPPAAL Models for Water Distribution Cyber–Physical Systems

This repository contains seven supplied UPPAAL XML models for a water distribution system (WDS), matching query files, supporting documentation and an archival package snapshot.

## Current repository layout

The **top-level files and directories are authoritative**. The repository currently uses a flat model/query layout:

```text
.
├── models/                         # Seven supplied UPPAAL XML models
│   ├── Advanced_CPS_WDS.xml
│   ├── Baseline_CPS_WDS.xml
│   ├── CPS_WDS_Industry5_AI_Human_Timed_Verification.xml
│   ├── CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml
│   ├── CPS_WDS_Secuity_Framework.xml
│   ├── CPS_WDS_With_Attacks.xml
│   └── CPS_WDS_With_Defence.xml
├── queries/                        # Matching .q files and catalogue
├── docs/                           # Model lineage, audit, query and reproducibility notes
├── scripts/                        # XML validation and query extraction
├── metamodel/                      # Conceptual metamodel working specification
├── semantics/                     # Assumption and timed-automata mapping specifications
├── FILE-MANIFEST.json              # Manifest for the canonical top-level package
├── uppaal-wds-full/                # Earlier structured package snapshot (archive contents)
└── uppaal-wds-full.tar             # Archive of the earlier structured package
```

The nested `uppaal-wds-full/` directory is a retained package snapshot from an earlier layout. It is **not** the current working tree and should not be used as the source of truth for the top-level repository. Its documentation and scripts retain paths from that earlier structure.

## Reference models and query counts

| Model | Query file | Queries | Focus |
|---|---|---:|---|
| `Baseline_CPS_WDS.xml` | `Baseline_CPS_WDS.q` | 2 | Tank, sensor, PLC and pump baseline |
| `CPS_WDS_Secuity_Framework.xml` | `CPS_WDS_Secuity_Framework.q` | 7 | Network and IDS security framework |
| `CPS_WDS_With_Attacks.xml` | `CPS_WDS_With_Attacks.q` | 5 | FDI, replay and DoS behaviours |
| `CPS_WDS_With_Defence.xml` | `CPS_WDS_With_Defence.q` | 3 | Defensive response and safe mode |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | Matching query file | 5 | Timed AI/IDS and operator response |
| `Advanced_CPS_WDS.xml` | `Advanced_CPS_WDS.q` | 1 | Expanded monitoring, twin, watchdog and backup control |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | Matching query file | 30 | Advanced timed multi-component model |
| **Total** | | **53** | |

The original spelling `Secuity` in one filename is intentionally preserved for source traceability.

## Quick start

Run commands from the repository root.

```bash
python scripts/validate_models.py
python scripts/extract_inherited_results.py
```

Open a model in UPPAAL, or run the verifier using the corresponding top-level query file:

```bash
verifyta -t 1 models/Baseline_CPS_WDS.xml queries/Baseline_CPS_WDS.q
```

The command is an execution instruction, not evidence that the command has been run. Record the exact UPPAAL version/build, command, input hashes and raw output for each fresh run.

## Evidence interpretation

The seven XML models contain 53 embedded queries. Historical result annotations in the source XML are not fresh verifier executions. The earlier package snapshot includes a machine-readable inherited query inventory; consult it as archived metadata and regenerate/check it against the current top-level source files before relying on it.

UPPAAL `E<> p` expresses existential reachability, not inevitability. Reachable alarms do not establish complete detection coverage; reachable recovery states do not establish inevitable recovery. Failed properties and counterexamples must be retained and discussed. See `docs/source-model-audit.md` and `docs/query-and-property-guide.md`.

## Current validation scope

`scripts/validate_models.py` checks XML parsing and embedded query counts. It does not perform UPPAAL verification, establish semantic correctness, or validate the extracted query files against a separately stored query corpus. Use the scripts only for the checks they actually implement.

## Licence

No licence is asserted. Confirm ownership and reuse conditions for all supplied models and dependencies before adding a licence.
