# Inherited Query Catalogue

The `.q` files contain UPPAAL formulas extracted from the original XML files in source order.

| Query file | Source XML | Queries |
|---|---|---:|
| Baseline_CPS_WDS.q | Baseline_CPS_WDS.xml | 2 |
| CPS_WDS_Secuity_Framework.q | CPS_WDS_Secuity_Framework.xml | 7 |
| CPS_WDS_With_Attacks.q | CPS_WDS_With_Attacks.xml | 5 |
| CPS_WDS_With_Defence.q | CPS_WDS_With_Defence.xml | 3 |
| CPS_WDS_Industry5_AI_Human_Timed_Verification.q | same basename XML | 5 |
| Advanced_CPS_WDS.q | Advanced_CPS_WDS.xml | 1 |
| CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.q | same basename XML | 30 |
| **Total** | | **53** |

The machine-readable inventory is `results/inherited/query-inventory.json`. Embedded outcomes are historical source XML annotations, not fresh verifier runs. Use `python scripts/extract_inherited_results.py` to regenerate the inventory and `python scripts/validate_models.py` to validate XML syntax.
