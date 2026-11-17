# WDS Model Lineage and Component Outline

| Source model | Principal elements and concerns | Query count |
|---|---|---:|
| `Baseline_CPS_WDS.xml` | Tank, Sensor, PLC, Pump | 2 |
| `CPS_WDS_Secuity_Framework.xml` | Tank, Sensor, Network, IDS, PLC, Pump | 7 |
| `CPS_WDS_With_Attacks.xml` | Baseline plus FDI, replay and DoS adversarial behaviours | 5 |
| `CPS_WDS_With_Defence.xml` | Attack/defence setting with SafeMode | 3 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | AI_IDS, Operator, SafeMode and timed response | 5 |
| `Advanced_CPS_WDS.xml` | PipeFlow, DigitalTwin, AI_IDS, Operator, Watchdog, Logger, BackupControl and related elements | 1 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | Timed physical process, sensors, communications, twin, PLC, AI_IDS, Operator, Adversary, SafeModeController and Watchdog | 30 |

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

## Guidance for derived models

Keep physical state, sensed value, delivered value, controller command, actuator state, attack state, alarm state and recovery state separate. Model component failures separately from relationship failures. Any derived file must record its parent model, changed constructs, rationale and verification status in a lineage note.
