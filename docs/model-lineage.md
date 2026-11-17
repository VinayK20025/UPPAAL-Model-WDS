# WDS Model Lineage and Component Outline

The supplied models progress from a tank–sensor–PLC–pump control loop to security-aware and timed variants. Original files are reference inputs; modifications belong in separate derived files with explicit lineage notes.

| Model | Main scope | Query count |
|---|---|---:|
| Baseline_CPS_WDS.xml | Tank, Sensor, PLC, Pump | 2 |
| CPS_WDS_Secuity_Framework.xml | Network and IDS added to the control loop | 7 |
| CPS_WDS_With_Attacks.xml | FDI, replay and DoS adversarial behaviours | 5 |
| CPS_WDS_With_Defence.xml | Safe-mode and defensive response | 3 |
| CPS_WDS_Industry5_AI_Human_Timed_Verification.xml | Timed AI/IDS and operator response | 5 |
| Advanced_CPS_WDS.xml | PipeFlow, DigitalTwin, Watchdog, Logger and BackupControl | 1 |
| CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml | Advanced timed physical, network, twin, operator, adversary and recovery elements | 30 |

## Component responsibilities

- Physical process: tank level, flow and process state.
- Sensing: measurement generation; distinguish true physical state from sensor output.
- Communication: delivery and channel effects; these are relationship behaviours.
- Control: PLC decision and command generation.
- Actuation: pump response; command issuance does not imply successful actuation.
- Adversary: attack activation and effect states.
- Detection: IDS/AI-IDS alarms; alarm reachability does not prove detection completeness.
- Digital twin: estimated state and residual abstraction, not validation of a deployed twin.
- Operator: acknowledgement and response transitions.
- Recovery: safe-mode, watchdog escalation and backup control.

For derived models, keep physical state, sensed value, delivered value, controller command, actuator state, attack state, alarm state and recovery state distinct. Model communication faults separately from endpoint component faults.
