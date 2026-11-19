# Query and property guide

- `E<> p` means some execution reaches a state satisfying `p`; it is existential reachability.
- `A[] p` means `p` holds in every reachable state of the encoded model.
- `A<> p` requires all executions to eventually reach `p`, subject to the model's progress semantics.
- `p --> q` is a leads-to property; interpret under the exact UPPAAL semantics and assumptions.

A reachable overflow witness is not automatically attack-induced. An alarm witness does not demonstrate complete attack-detection coverage. A recovery witness does not demonstrate inevitable or bounded recovery. Check antecedent reachability for implication invariants to avoid vacuous satisfaction. Preserve and analyse counterexamples rather than weakening formulas to obtain passing outcomes.

The advanced model's `A[] not deadlock` formula is kept in `queries/diagnostic/` because the supplied UPPAAL 5.0.0 verifier reported: `Cannot handle deadlock predicate for models with priorities or guarded broadcast receivers.` This is a compatibility limitation, not evidence of deadlock freedom.
