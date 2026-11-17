# Assumption Semantics

## Three separate activities

1. **Documentation:** what the modeller or system owner assumes.
2. **Formalisation:** the predicate and operational condition encoded in the timed-automata network.
3. **Verification:** whether the encoded assumption is satisfied, violated or unresolved under the model and query set.

## Component and relationship scope

A component assumption concerns the behaviour of one component. A relationship assumption concerns the interaction between components, such as data integrity, message delivery, bounded latency or command-channel availability. Endpoint health does not imply relationship correctness.

## Violation observability

Avoid hiding all assumptions solely in guards or invariants where doing so removes behaviours that security analysis should inspect. Where appropriate, represent explicit monitors and observable assumption-violation states. Distinguish satisfied, violated and externally unresolved assumptions.

## Composition

For an interface contract `C_i = (I_i, O_i, A_i, G_i)`, define assumptions and guarantees with explicit scope. A composition obligation may require a provider guarantee to imply the consumer assumption, `G_j => A_i`, under a declared interface mapping. This is a modelling obligation and must not be claimed as proven without an appropriate check.
