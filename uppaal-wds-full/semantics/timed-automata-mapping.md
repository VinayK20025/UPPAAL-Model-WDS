# Timed-Automata Mapping (Working Specification)

A timed automaton can be represented as `TA = (L, l0, X, V, E, Inv)`, with locations `L`, initial location `l0`, clocks `X`, variables `V`, transitions `E` and invariants `Inv`. A transition may be described as `(l, g, a, u, r, l')`, where `g` is a guard, `a` a synchronisation/action, `u` an update, `r` a reset set and `l'` the target location.

## Mapping obligations

- Map each model component to one or more templates or a documented abstraction.
- Map each relationship to synchronisation/channel behaviour and any delay/loss/corruption state required by the model.
- Map assumptions to explicit guards, invariants or monitors while preserving the ability to observe relevant violations.
- Map temporal obligations to clocks, guards, invariants and timeout/escalation transitions.
- Map recovery contracts to trigger, pending obligation, deadline, action, completion and failure/timeout behaviour.
- Maintain traceability from source model elements to template/location/transition identifiers and query IDs.

This document is a working mapping specification; it does not assert a proven semantics-preserving transformation. Any preservation claim requires a formal definition and evidence.
