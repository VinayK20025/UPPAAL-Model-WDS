# Repository Scripts

Run from the repository root.

- `python scripts/validate_models.py` parses all top-level `models/*.xml` files and reports their embedded query counts.
- `python scripts/extract_inherited_results.py` extracts formulae and inherited result annotations into `queries/extracted/` and `results/inherited/query-inventory.json`.

The extraction script reads the source models only; it does not execute UPPAAL. Extracted annotations are historical XML metadata and must not be reported as new verification outcomes.
