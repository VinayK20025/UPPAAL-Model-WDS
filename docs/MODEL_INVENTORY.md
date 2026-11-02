# Model inventory

The files represent multiple model variants. This inventory does not assert semantic equivalence or a formal refinement relation between them.

| File | Approx. bytes | Templates | Queries | Observed scope |
|---|---:|---:|---:|---|
| `Baseline_CPS_WDS.xml` | 4,132 | Not established in this register | Not established in this register | Baseline CPS/WDS |
| `CPS_WDS_With_Attacks.xml` | 9,666 | 9 | 5 | Single tank; FDI, replay and DoS |
| `CPS_WDS_With_Defence.xml` | 7,279 | 8 | 3 | Single tank; safe mode and recovery |
| `CPS_WDS_Secuity_Framework.xml` | 7,269 | 6 | 7 | Security/control consistency |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | 9,383 | 11 | 5 | Human–AI and timed verification |
| `Advanced_CPS_WDS.xml` | 37,094 | 13 | 1 | Two-tank, twin, AI/IDS, operator, watchdog |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | 36,698 | 11 | 30 | Two-tank; 16 instantiated processes |

Template count differs from process count because parameterized templates can be instantiated more than once.

## Advanced 16-process candidate

The advanced verification candidate declares:

| Template | Instances |
|---|---:|
| PhysicalProcess | 2 |
| Sensor | 2 |
| FlowSensor | 2 |
| CommunicationNetwork | 2 |
| DigitalTwin | 2 |
| PLC | 1 |
| AI_IDS | 1 |
| Operator | 1 |
| Adversary | 1 |
| SafeModeController | 1 |
| Watchdog | 1 |
| **Total** | **16** |

This composition matches the process count described in the manuscript. It does not by itself prove that the file is the exact revision used for the paper's reported results.
