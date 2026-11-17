# Source Model Audit

## Scope

This audit describes the seven supplied XML models currently stored directly under `models/` and their embedded query blocks. The corresponding `.q` files are stored directly under `queries/`. This document describes the checked-in artefacts and inherited query structure; it does not claim that the models have been freshly verified by the current repository commit.

## Model progression

1. **Baseline:** Tank, Sensor, PLC and Pump form the physical/control loop.
2. **Security framework:** network communication and IDS functions are added.
3. **Attack-enabled:** false-data injection (FDI), replay and denial-of-service behaviours are represented.
4. **Defence-enabled:** defensive response and safe-mode behaviour are introduced.
5. **Timed AI/human:** AI/IDS alarm and operator response are represented with timing constraints.
6. **Advanced CPS:** extended process/flow, network, digital-twin, monitoring/logging, watchdog, safe-mode and backup-control abstractions are present.
7. **Advanced timed AI/human:** a richer timed composition of physical process, sensors, communication, twin, PLC, AI-IDS, operator, adversary, safe-mode controller and watchdog is represented.

## Embedded query inventory

| Model | Query file | Query count |
|---|---|---:|
| `Baseline_CPS_WDS.xml` | `Baseline_CPS_WDS.q` | 2 |
| `CPS_WDS_Secuity_Framework.xml` | `CPS_WDS_Secuity_Framework.q` | 7 |
| `CPS_WDS_With_Attacks.xml` | `CPS_WDS_With_Attacks.q` | 5 |
| `CPS_WDS_With_Defence.xml` | `CPS_WDS_With_Defence.q` | 3 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | Matching query file | 5 |
| `Advanced_CPS_WDS.xml` | `Advanced_CPS_WDS.q` | 1 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | Matching query file | 30 |
| **Total** | | **53** |

Historical result counts previously extracted from the source XML annotations were 20 `success`, 6 `failure` and 27 `NOT_RECORDED`. Treat these only as inherited XML metadata, not fresh verifier outcomes. Re-extract and compare them against the exact current XML files before using them as experimental data.

## Interpretation constraints

- An existential overflow witness does not establish a real-world prediction; it establishes reachability in the encoded abstraction.
- A failed invariant is evidence of a counterexample in the model, not automatically evidence about an operational WDS.
- Alarm reachability is not a proof of complete detection coverage.
- Recovery reachability is not proof that recovery is inevitable.
- The advanced timed model's inherited failed `ai_alarm --> operator_ack` query must not be described as guaranteed acknowledgement.
- Historical annotations are not fresh verifier records.

## Required future audit

For publication-grade reproducibility, record UPPAAL version/build, OS, exact command, input hashes, complete raw output, exit status and counterexample trace for each newly executed query. Re-run the complete query set after any change to a model or query file.
