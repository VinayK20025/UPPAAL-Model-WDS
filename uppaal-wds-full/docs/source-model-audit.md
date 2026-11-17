# Source Model Audit

## Scope

This audit describes the seven supplied XML reference models and their embedded query blocks. The XML files are preserved byte-for-byte under `models/reference/`. The audit does not claim that the models have been freshly verified in this repository.

## Model progression

1. **Baseline:** Tank, Sensor, PLC and Pump form the physical/control loop.
2. **Security framework:** network communication and IDS functions are added.
3. **Attack-enabled:** false-data injection (FDI), replay and denial-of-service behaviours are represented.
4. **Defence-enabled:** defensive response and safe-mode behaviour are introduced.
5. **Timed AI/human:** AI/IDS alarm and operator response are represented with timing constraints.
6. **Advanced CPS:** extended process/flow, network, digital-twin, monitoring/logging, watchdog, safe-mode and backup-control abstractions are present.
7. **Advanced timed AI/human:** a richer timed composition of physical process, sensors, communication, twin, PLC, AI-IDS, operator, adversary, safe-mode controller and watchdog is represented.

## Embedded query inventory

| Model | Query count |
|---|---:|
| Baseline_CPS_WDS.xml | 2 |
| CPS_WDS_Secuity_Framework.xml | 7 |
| CPS_WDS_With_Attacks.xml | 5 |
| CPS_WDS_With_Defence.xml | 3 |
| CPS_WDS_Industry5_AI_Human_Timed_Verification.xml | 5 |
| Advanced_CPS_WDS.xml | 1 |
| CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml | 30 |
| **Total** | **53** |

The historical XML result attributes are counted in `results/inherited/query-inventory.json`: 20 `success`, 6 `failure`, 27 `NOT_RECORDED`.

## Interpretation constraints

- An existential overflow witness does not establish a real-world prediction; it establishes reachability in the encoded abstraction.
- A failed invariant is evidence of a counterexample in the model, not automatically evidence about an operational WDS.
- Alarm reachability is not a proof of complete detection coverage.
- Recovery reachability is not proof that recovery is inevitable.
- The advanced timed model's inherited failed `ai_alarm --> operator_ack` query must not be described as guaranteed acknowledgement.
- Historical annotations are not fresh verifier records.

## Required future audit

For publication-grade reproducibility, record UPPAAL version/build, OS, exact command, input hashes, complete raw output, exit status and counterexample trace for each newly executed query. Re-run the complete query set after any change to a model or query file.
