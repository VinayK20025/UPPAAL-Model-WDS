# Post-merge model repair notes

This change set repairs three compilation defects found during the post-merge UPPAAL run.

## Changes
- `CPS_WDS_With_Attacks.xml`: removed the `safe_mode` guard from the Tank overflow transition. This model does not instantiate a SafeMode controller and has no `safe_mode` declaration. Safe-mode protection belongs in the defence-capable model, not as an undeclared reference in the attack-only model.
- `CPS_WDS_With_Defence.xml`: added and initialised global `bool data_valid = true;`, because the PLC guard references it. The current model's IDS transition does not update this flag; its runtime semantics therefore remain an explicit follow-up item and must not be interpreted as validated data-integrity detection.
- `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml`: replaced the literal backslash-n sequence between the `safe_mode` and `data_valid` declarations with a real newline; added `!safe_mode` to the Tank overflow transition guard; added `data_valid` to the PLC low-level command guard.

## Preservation
- Embedded query blocks were retained, with the original counts: 5, 3, and 5 respectively.
- No standalone `.q` file was modified by this repair branch.
- Historical XML query result annotations were not rewritten.

## Verification status
These changes are source-level repairs only. They have not been run through UPPAAL in this environment. After checkout, run XML validation and the unchanged query files. A successful XML parse is not proof of UPPAAL compilability or property satisfaction.

Example commands:

```bash
python3 scripts/validate_models.py

for model in \
  CPS_WDS_With_Attacks \
  CPS_WDS_With_Defence \
  CPS_WDS_Industry5_AI_Human_Timed_Verification
do
  timeout 180s "$VERIFYTA" \
    "models/${model}.xml" \
    "queries/${model}.q" \
    2>&1 | tee "results/reproduced/post-merge/${model}-repair.log"
  echo "Exit status: ${PIPESTATUS[0]}"
done
```

Inspect each formula outcome separately. Do not change queries to obtain satisfied results. Retain counterexamples and classify timeouts or compilation failures as incomplete runs.
