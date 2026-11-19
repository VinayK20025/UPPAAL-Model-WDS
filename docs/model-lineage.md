# WDS Model Lineage and Component Outline

The following table describes the seven XML models currently stored directly under `models/`. Their matching query files are stored directly under `queries/`.

| Source model | Query file | Principal elements and concerns | Query count |
|---|---|---|---:|
| `Baseline_CPS_WDS.xml` | `Baseline_CPS_WDS.q` | Tank, Sensor, PLC, Pump | 2 |
| `CPS_WDS_Secuity_Framework.xml` | `CPS_WDS_Secuity_Framework.q` | Tank, Sensor, Network, IDS, PLC, Pump | 7 |
| `CPS_WDS_With_Attacks.xml` | `CPS_WDS_With_Attacks.q` | Baseline plus FDI, replay and DoS adversarial behaviours | 5 |
| `CPS_WDS_With_Defence.xml` | `CPS_WDS_With_Defence.q` | Attack/defence setting with SafeMode | 3 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | Matching query file | AI_IDS, Operator, SafeMode and timed response | 5 |
| `Advanced_CPS_WDS.xml` | `Advanced_CPS_WDS.q` | PipeFlow, DigitalTwin, AI_IDS, Operator, Watchdog, Logger, BackupControl and related elements | 1 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | Matching query file | Timed physical process, sensors, communications, twin, PLC, AI_IDS, Operator, Adversary, SafeModeController and Watchdog | 30 |

The spelling `Secuity` is retained in the filename exactly as present in the supplied source artefact.

## Component responsibilities

- **Physical process:** tank levels, flow and process variables.
- **Sensing:** observed values; keep them distinct from true process state.
- **Communication:** delivery, delay, loss and alteration; these are relationship/channel behaviours.
- **Control:** PLC decision and command generation.
- **Actuation:** pump behaviour; command issuance does not imply physical actuation.
- **Adversary:** attack activation and attack-effect state.
- **Detection:** IDS/AI-IDS events; alarm reachability does not prove complete detection.
- **Digital twin:** estimated state and residual/mismatch abstraction, not validation of a deployed digital twin.
- **Human response:** operator acknowledgement and response transitions.
- **Recovery:** safe mode, watchdog escalation and backup control.

## Guidance for future derived models

The repository has four designated model-stage files on `main`: `Baseline_CPS_WDS.xml`, `CPS_WDS_With_Defence.xml`, `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` and `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml`. Keep these paths stable. Treat the advanced model as an independent expanded composition, not as a simple copy of the 11-template timed AI/Human model. Document any future derivation as a separately named variant with parent, changed constructs, rationale and verification status.

Keep physical state, sensed value, delivered value, controller command, actuator state, attack state, alarm state and recovery state separate. Model component failures separately from relationship failures.
