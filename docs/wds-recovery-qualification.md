# WDS recovery qualification verification

This verification target checks the recovery-qualified control-inhibit model.

## Model and query

- Model: `models/derived/CPS_WDS_Control_Inhibit.xml`
- Query suite: `queries/CPS_WDS_Recovery_Qualification.q`
- Recovery policy: three consecutive clean, fresh, non-injected IDS measurements are required to clear the latched control inhibit.

The IDS first processes a delivered sample and moves to a notification location. The notification transition synchronises on `ids_sample!`; the RecoveryMonitor consumes `ids_sample?` and updates its qualification state. This explicit two-step handshake ensures that the monitor observes the values assigned by the IDS transition, rather than reading pre-update values in a simultaneous update.

An unclean IDS observation resets the sequence. The third consecutive clean observation sets `recovery_completed`, sets `clean_count` to `RECOVERY_THRESHOLD`, and clears `control_inhibit`. The monitor remains in the recovered location while clean samples continue and returns to the initial qualification state on a later unclean sample.

## Structural checks and UPPAAL run

From the repository root:

```bash
python3 -m py_compile scripts/verify_wds_recovery.py
python3 scripts/verify_wds_recovery.py \
  --verifyta ./uppaal-5.0.0-linux64/bin/verifyta
```

Or use the verifier installed elsewhere:

```bash
python3 scripts/verify_wds_recovery.py --verifyta /path/to/uppaal/bin/verifyta
```

The runner checks XML well-formedness, required global declarations, expected template names, IDS-to-monitor notification, monitor transitions, system composition, and query syntax before invoking `verifyta`. It writes the exact command, hashes, raw verifier output, and per-formula outcomes to a timestamped directory under `results/reproduced/wds-recovery-qualification/`.

A zero exit status indicates the verifier completed its query processing, not that all properties are necessarily satisfied. Inspect each formula outcome and witness/counterexample. Existential properties are reachability claims; they are not universal guarantees. In particular, the diagnostic queries for pump-on during inhibition are expected to be unsatisfiable in a correctly interlocked model. Do not replace a violated property with a weaker formula merely to obtain a passing result.

## Expected model properties

- A clean sequence increments the counter through one and two.
- Any unclean IDS sample resets the counter and clears the completion flag.
- Recovery completion is reachable after three consecutive clean samples while inhibition is active.
- Recovery cannot be marked complete below the configured threshold.
- While inhibition is active, the pump state and pending pump-on command are both false.

## Reproducibility boundaries

The script records raw evidence and hashes but does not modify model/query files or historical results. UPPAAL verifier execution is required to establish formula outcomes. XML parsing alone is not a substitute for UPPAAL model validation.
