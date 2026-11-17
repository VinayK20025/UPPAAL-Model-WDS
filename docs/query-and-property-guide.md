# Query and Property Guide

## Query file organisation

The top-level repository stores model XML files under `models/` and executable query files under `queries/`, using matching basenames. Run them with `scripts/run_verification.py` to preserve exit codes and evidence metadata.

Diagnostic formulas that cannot currently be evaluated by the selected verifier/model combination are kept under `queries/diagnostic/`. They must not be silently counted as verified.

## UPPAAL operators

- `E<> p`: some execution reaches a state satisfying `p` (existential reachability).
- `A[] p`: `p` holds in every reachable state of the encoded model (invariant).
- `A<> p`: all paths eventually reach a state satisfying `p`, subject to model semantics and progress assumptions.
- `p --> q`: leads-to property; interpret in the exact timed-automata query context.
- `A[] not deadlock`: no reachable deadlock exists in the encoded transition system, when supported by the verifier/model features.

## Current verifier compatibility finding

The supplied UPPAAL 5.0.0 verifier returned this error for the advanced timed model's deadlock query: `Cannot handle deadlock predicate for models with priorities or guarded broadcast receivers.` The formula has been separated from the executable query set and retained in `queries/diagnostic/CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced_deadlock.q`. The source XML is unchanged. This is an unsupported-query result, not evidence that the model is deadlock-free.

`Advanced_CPS_WDS.q` also contains a standalone deadlock query. Treat its result as incomplete unless the verifier emits an explicit satisfied/not-satisfied outcome.

## Source-specific cautions

1. A reachable attack or overflow state is a witness in the encoded model, not a physical WDS prediction.
2. A reachable alarm does not establish complete attack-detection coverage.
3. A reachable recovery state does not establish inevitable recovery.
4. An implication invariant may be vacuous when its antecedent is unreachable; check antecedent reachability separately.
5. Failed properties and counterexamples must be retained and analysed.
6. Embedded XML outcome annotations are inherited metadata, not fresh verifier runs.
7. A verifier execution error, absent result line or incomplete log is not a property result.
8. Do not change a failing formula simply to obtain a satisfied result; first inspect its counterexample and determine whether the model, assumption or requirement is incorrect.

## Interpretation of observed property violations

Unsatisfied results in the security framework, attack-enabled, defence-enabled and timed AI/human models are substantive findings requiring counterexample analysis. For example, the security-framework query set includes invariants for overflow prevention and sensor integrity; the attack-enabled model explicitly checks both overflow reachability and the invariant that overflow never occurs. These properties are not contradictory: one asks whether a witness exists and the other asks whether no such state is reachable. Their outcomes must be interpreted against the exact model and query.

## Recommended evaluation coverage

For a reviewed derived model, select a non-vacuous query set spanning component assumption violation; relationship/channel assumption violation; attack effect; detection or mitigation; recovery completion and timeout; and bounded temporal response. Record formula, informal meaning, scope, assumptions, result, tool version, model hash and query hash.
