# Manuscript-to-artifact traceability

This is a provisional mapping from manuscript topics to current repository artifacts. It does not imply that every manuscript result has been reproduced.

| Manuscript topic/claim | Candidate artifact | Evidence currently visible | Required addition or qualification |
|---|---|---|---|
| Two-tank physical abstraction | Advanced verification XML | Parameterized PhysicalProcess instantiated twice | Document state and update semantics |
| Sensor/network abstractions | Same advanced file | Two sensors, flow sensors and networks | Specify timing bounds and synchronization semantics |
| Digital-twin consistency | Same advanced file | Two DigitalTwin instances and discrepancy state | Define exactly what the predicate means; do not claim physical twin fidelity |
| AI/IDS alarm | Same advanced file | AI_IDS process and alarm state | State oracle/detector assumptions |
| Human acknowledgement | Same advanced file | Operator process and acknowledgement state | Document response protocol and timing bounds |
| Adversary | Same advanced file | Adversary process and attack flags | Enumerate capabilities, persistence, timing and reactivation |
| Safe-mode/recovery | Same advanced file | SafeModeController and clean_count state | Reconcile recovery semantics and Q30 |
| Watchdog/backup shutdown | Same advanced file | Watchdog and backup shutdown state | Supply complete results and traces |
| Deadlock freedom | Q26 | Formula present | No result annotation; rerun |
| Recovery reachability | Q17 | Formula present | No result annotation; rerun |
| Recovery liveness | Q30 | Leads-to formula present | No result annotation; provide actual output/trace |
| Human-response liveness | Q31 | Leads-to formula present | XML marks failure; reconcile manuscript claim |
| 200-seed simulation | No simulator source currently listed | Only manuscript-level aggregate statement | Add source, config, seeds, raw outputs and analysis |
| Reusable CPS meta-model/MDE method | Not represented by WDS XML alone | Domain-specific models only | Publish meta-model, mapping rules, bindings and tooling separately |

For each reported result, provide the evidence chain:

`requirement -> model element(s) -> UPPAAL query -> run result -> witness/counterexample -> manuscript statement`

Instantiate this chain for the recovery and human-response claims.
