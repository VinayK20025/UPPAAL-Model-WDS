# Reproducibility status and audit notes

**Basis:** inspection of the files on the default branch. UPPAAL was not executed as part of this documentation update.

## Current repository state

The root contains seven UPPAAL XML files and a README. At the time of audit, it did not contain a separate Q1–Q31 query export, complete verification report, counterexample archive, simulator source code, simulation configuration, random-seed list, raw simulation outputs or environment manifest.

The closest match to the manuscript's two-tank/16-process WDS model is:

- File: `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml`
- Blob SHA observed during audit: `5aee75a71348a1b7a4292091daf701cfb65733de`
- Instantiated processes: 16
- Embedded queries: 30
- Numbering: Q1–Q8 and Q10–Q31; Q9 is absent
- Stored result annotations: 12
- Stored successes: Q1–Q8 and Q27–Q29
- Stored failure: Q31
- No stored result annotation: Q10–Q26 and Q30

The Q31 failure annotation conflicts with the manuscript's statement that Q31 is established. Q30 has no stored result annotation. Consequently, the manuscript's reported summary of 31 queries and 30 established properties is not substantiated by the current embedded XML annotations.

## Required resolution

1. Identify the exact XML revision and query suite used to generate the manuscript's tables.
2. Recover Q9, if it belongs to the intended suite, from the original authoring project or run archive.
3. Execute the entire intended query suite in a recorded UPPAAL installation.
4. Preserve per-query result, execution metadata and witness/counterexample traces.
5. Resolve the Q30/Q31 discrepancy using actual run output.
6. Reconcile the reported counts of reachability, invariant and liveness properties against the formulas actually executed.
7. Update the manuscript and repository from the same verified run.

## Evidence semantics

- `E<> phi` is existential reachability: it establishes that some reachable state satisfies phi, not a universal guarantee.
- `A[] phi` is an invariant over reachable states, subject to UPPAAL semantics and the model assumptions.
- A leads-to formula such as `p --> q` expresses a liveness/response obligation and must be reported independently of reachability.
- An XML `<result>` annotation is embedded historical metadata; it does not prove that the formula was rerun against the current file.

## Limitations of this audit

XML structure, process composition, query formulas and embedded outcome annotations were inspected. The UPPAAL verification engine was not run. No simulator or simulation dataset was found in the inspected repository tree. Revise this status when those artifacts have been added and checked.
