# UPPAAL Models for Secure Cyber–Physical Water Distribution Systems

This repository contains UPPAAL timed-automata models developed for secure and resilient cyber–physical water distribution systems (CPS/WDS). The files represent several model generations covering baseline operation, adversarial actions, defence, human–AI coordination, digital-twin consistency and recovery.

> **Reproducibility status:** The repository currently contains multiple model variants. `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` is the closest match to the manuscript's two-tank, 16-process architecture. Its query list contains Q1–Q8 and Q10–Q31 (Q9 is absent). Only 12 queries have stored result annotations; Q31 is annotated as failure, which conflicts with the manuscript's reported success. Q30 has no stored result annotation. See [Reproducibility status](docs/REPRODUCIBILITY_STATUS.md) and [Query register](docs/QUERY_REGISTER.md). These embedded annotations must not be treated as a complete fresh verification record.

## Contents

| File | Purpose |
|---|---|
| `Baseline_CPS_WDS.xml` | Baseline CPS/WDS model |
| `CPS_WDS_With_Attacks.xml` | Earlier single-tank attack model |
| `CPS_WDS_With_Defence.xml` | Earlier single-tank defence/recovery model |
| `CPS_WDS_Secuity_Framework.xml` | Security-framework model (filename spelling retained) |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` | Human–AI/timed-verification model |
| `Advanced_CPS_WDS.xml` | Advanced two-tank model with twin, AI/IDS, operator and watchdog |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` | Advanced two-tank model with 16 instantiated processes and 30 embedded queries |
| `docs/` | Inventory, query register, traceability and reproduction guidance |

## Recommended starting point

For the manuscript's 16-process WDS case study, inspect `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml`. It instantiates two physical-process, two sensor, two flow-sensor, two communication-network and two digital-twin processes, plus PLC, AI/IDS, operator, safe-mode controller, watchdog and adversary processes.

## Reproducing verification

1. Open the selected XML file in a compatible UPPAAL release.
2. Inspect declarations, templates, system composition and queries.
3. Run the complete query suite in the UPPAAL Query pane.
4. Export the exact per-query outcomes, witnesses/counterexamples and tool diagnostics.
5. Record the UPPAAL build, platform, verification settings, run date, Git commit and model checksum.
6. Reconcile the run output with the manuscript before reporting aggregate counts.

Stored XML `<result>` annotations are historical metadata, not a substitute for rerunning the queries.

## Documentation

- [Reproducibility status](docs/REPRODUCIBILITY_STATUS.md)
- [Model inventory](docs/MODEL_INVENTORY.md)
- [Query register](docs/QUERY_REGISTER.md)
- [Manuscript-to-artifact traceability](docs/TRACEABILITY.md)
- [Reproduction protocol](docs/REPRODUCTION_PROTOCOL.md)

## Scope

These are abstract, discrete-state timed-automata models. The WDS model is not a hydraulic solver or empirical validation of a deployed water network. Human behaviour and AI detection are represented through abstract protocol/state transitions. Verification claims apply only to the supplied model and its explicit assumptions.

## Citation

Add the final bibliographic citation and a tagged archival release identifier here before journal submission.
