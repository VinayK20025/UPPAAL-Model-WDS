# Validation and Test Guidance

Run `python scripts/validate_models.py` to parse each reference XML and count embedded queries. Run `python scripts/extract_inherited_results.py` to regenerate the `.q` files and inherited query inventory. These checks validate XML well-formedness and extraction consistency; they do not replace UPPAAL verification.
