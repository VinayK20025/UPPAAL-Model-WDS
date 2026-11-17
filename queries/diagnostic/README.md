# Diagnostic queries

This directory retains formulas that are part of the source verification intent but are not currently included in the automated executable query sets because the observed UPPAAL 5.0.0 verifier rejects them for the relevant model features. They are not verified by the batch runner and must not be reported as satisfied or failed. Revisit them if a later verifier release supports the required semantics.

The advanced timed model's deadlock-freedom formula is preserved here after the verifier reported that it cannot handle deadlock predicates for models with priorities or guarded broadcast receivers. The original XML query is retained unchanged for provenance.
