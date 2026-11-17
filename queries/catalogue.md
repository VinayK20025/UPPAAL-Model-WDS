# Query Catalogue

The current query files are stored directly in `queries/` and use the same basename as their source XML under `models/`. Formulae should be checked against the corresponding XML `<queries>` block before being treated as an authoritative extraction.

| Query file | Source model | Count |
|---|---|---:|
| `Baseline_CPS_WDS.q` | `models/Baseline_CPS_WDS.xml` | 2 |
| `CPS_WDS_Secuity_Framework.q` | `models/CPS_WDS_Secuity_Framework.xml` | 7 |
| `CPS_WDS_With_Attacks.q` | `models/CPS_WDS_With_Attacks.xml` | 5 |
| `CPS_WDS_With_Defence.q` | `models/CPS_WDS_With_Defence.xml` | 3 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification.q` | Matching basename XML | 5 |
| `Advanced_CPS_WDS.q` | `models/Advanced_CPS_WDS.xml` | 1 |
| `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.q` | Matching basename XML | 30 |
| **Total** | | **53** |

The repository includes an earlier structured package snapshot under `uppaal-wds-full/`. Its inherited inventory is an archive artefact; do not assume it matches the current top-level XML and query files without running an explicit comparison.

Historical XML outcome annotations are not newly reproduced verifier results.
