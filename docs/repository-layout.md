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
