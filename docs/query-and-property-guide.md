# Query and Property Guide

The repository contains 53 formulas extracted from the seven source XMLs. See `results/inherited/query-inventory.json` for source file, ordinal, formula, comment, inherited outcome and timestamp.

## UPPAAL query semantics

- `E<> p`: some execution can reach a state satisfying `p`; this is a possibility result.
- `A[] p`: `p` holds in every reachable state of the encoded model.
- `A<> p`: all paths eventually reach a state satisfying `p`, subject to model semantics and progress assumptions.
- `p --> q`: leads-to property; inspect the exact temporal obligation.
- `A[] not deadlock`: no reachable deadlock exists in the encoded transition system.

## Interpretation cautions

1. An attack or overflow witness is a result in the encoded model, not a physical WDS prediction.
2. A reachable alarm does not prove complete attack-detection coverage.
3. A reachable recovery state does not prove inevitable recovery.
4. An implication invariant can be vacuously true if its antecedent is unreachable; check antecedent reachability separately.
5. Preserve failed properties and counterexamples.
6. XML result annotations are inherited metadata, not newly reproduced verifier outcomes.

For a derived evaluation model, select a small non-vacuous suite spanning assumption violation, relationship/channel failure, attack effect, detection/mitigation, recovery completion/timeout and temporal deadline compliance. Record formula, meaning, scope, assumptions, result, tool version and model/query hashes.
