# Query and Property Guide

## UPPAAL operators

- `E<> p`: some execution reaches a state satisfying `p` (existential reachability).
- `A[] p`: `p` holds in every reachable state of the encoded model (invariant).
- `A<> p`: all paths eventually reach a state satisfying `p`, subject to model semantics and progress assumptions.
- `p --> q`: leads-to property; interpret in the exact timed-automata query context.
- `A[] not deadlock`: no reachable deadlock exists in the encoded transition system.

## Source-specific cautions

1. A reachable attack or overflow state is a witness in the encoded model, not a physical WDS prediction.
2. A reachable alarm does not establish complete attack-detection coverage.
3. A reachable recovery state does not establish inevitable recovery.
4. An implication invariant may be vacuous when its antecedent is unreachable; check antecedent reachability separately.
5. Failed properties and counterexamples must be retained.
6. Embedded XML outcome annotations are inherited metadata, not fresh verifier runs.

## Recommended evaluation coverage

For a reviewed derived model, select a small non-vacuous query set spanning: component assumption violation; relationship/channel assumption violation; attack effect; detection or mitigation; recovery completion and timeout; and bounded temporal response. Record formula, informal meaning, scope, assumptions, result, tool version, model hash and query hash.
