# Repository Layout and Artefact Status

## Authoritative source tree

The current working artefacts are stored at the top level:

- `models/*.xml`: seven supplied reference models.
- `queries/*.q`: seven corresponding query files.
- `queries/catalogue.md`: query counts and source relationships.
- `docs/`: model lineage, query interpretation and reproducibility guidance.
- `scripts/`: XML parsing and inherited-query extraction.
- `metamodel/` and `semantics/`: conceptual working specifications.

## Archived package snapshot

`uppaal-wds-full/` and `uppaal-wds-full.tar` are retained from an earlier package layout. The nested directory contains a structured copy that used `models/reference/`, `queries/inherited/` and `results/`. Its files are not synchronised automatically with the top-level files.

Do not use the nested scripts or README as instructions for the top-level working tree. Before distributing or citing the snapshot, compare its contents with the current canonical files or regenerate the package from the current tree.

## Implementation status

The repository includes XML validation and formula/annotation extraction scripts. It does not currently establish fresh verifier execution, automated metamodel validation, or an executable model transformation pipeline.


## Main-branch designated model stages

The four model-stage files retained at the repository root under `models/` are:

1. `Baseline_CPS_WDS.xml` — baseline physical/control loop.
2. `CPS_WDS_With_Defence.xml` — defensive response and safe-mode behaviour.
3. `CPS_WDS_Industry5_AI_Human_Timed_Verification.xml` — AI/IDS, human acknowledgement, timed response and latched interlock/recovery semantics.
4. `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml` — expanded multi-tank, digital-twin, multi-attack and watchdog/backup-control composition.

Other XML models remain in the repository for source lineage and comparative traceability. The four designated stage files are not interchangeable: in particular, the advanced model is a separate extended composition and must not be replaced by a copy of the 11-template timed AI/Human model.

The timed AI/Human model embeds five Q1–Q5 queries. Its D1–D3 diagnostic properties remain in the separate file `queries/CPS_WDS_Industry5_AI_Human_Timed_Verification_Diagnostic.q`. Historical XML result annotations are not fresh verification evidence.
