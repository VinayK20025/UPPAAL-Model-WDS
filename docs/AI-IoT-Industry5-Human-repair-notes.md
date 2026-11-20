# AI–IoT–Industry 5.0–Human-in-the-Loop model repair notes

A corrected model package has been generated for local installation. The model and its matching 30-query file are supplied as downloadable artifacts in the associated project conversation; they are not yet part of this repository because the repository did not contain the source model/query at the expected paths when inspected.

## Repository inspection

The current `main` branch uses top-level `models/` and `queries/` directories. It has a seven-query `models/CPS_WDS_Secuity_Framework.xml` baseline, but no committed `CPS_WDS_Security_AI_Industry5IoT_Human.xml` or matching 30-query file. The AI/IoT/HITL artifact discussed in the conversation was therefore treated as a separate model, not as a replacement for the security baseline.

## Fixes in the repaired local artifact

- Added the UPPAAL Flat System 1.6 document type declaration and normalized template element ordering.
- Removed the IoT Connected-location clock invariant that could block global time because no connected-state transition reset or escaped the clock-bound location.
- Retained the `clock xn;` declaration and reset it on network reconnection.
- Preserved sender/receiver pairs for `sensor_to_iot`, `iot_to_ai`, `ai_to_human`, `human_to_response`, and `recovery_tick`.
- Changed the attacker to inject a forged but transport-valid measurement so that the IoT forwarding/AI path can process the data.
- Made recovery qualification incident-gated using `system_degraded`, preventing recovery from completing at startup before an incident.
- Ensured the forwarder emits one recovery tick for a forwarded sample before it can accept another sample.
- Preserved the original 30 query formulas in the matching query artifact.

## Modelling assumptions to disclose

- AI comparison uses model state as an independent reference abstraction; a deployed AI does not directly observe hidden plant ground truth.
- Human approval/rejection/timeout is nondeterministic, not a validated operator-behaviour model.
- Emergency pump shutdown is instantaneous in the abstraction.
- High-high and dry-run interlocks are assumed healthy; their fault modes are not injected in this model.

## Installation in Codespaces

Copy the repaired XML and query files into the repository's top-level `models/` and `queries/` directories, respectively, using the filenames:

- `models/CPS_WDS_Security_AI_Industry5IoT_Human.xml`
- `queries/CPS_WDS_Security_AI_Industry5IoT_Human.q`

Then execute:

```bash
mkdir -p results/ai_industry5_human
"$VERIFYTA" -t 1 \
  models/CPS_WDS_Security_AI_Industry5IoT_Human.xml \
  queries/CPS_WDS_Security_AI_Industry5IoT_Human.q \
  2>&1 | tee results/ai_industry5_human/verification_repaired.log
```

XML parsing and structural inspection are not formal UPPAAL verification. No verification result is claimed until a fresh `verifyta` run is completed and its raw log is retained.
