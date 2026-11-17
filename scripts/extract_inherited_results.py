#!/usr/bin/env python3
"""Extract query formulae and inherited annotations from top-level source XML models.

Outputs are written to queries/extracted/ and results/inherited/. Existing source
XML files are read only and are never modified.
"""
from __future__ import annotations

import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
OUT = ROOT / "queries" / "extracted"
INVENTORY = ROOT / "results" / "inherited" / "query-inventory.json"


def local(tag: str) -> str:
    return tag.split("}")[-1]


def text_of(node: ET.Element | None) -> str:
    return "".join(node.itertext()).strip() if node is not None else ""


def main() -> None:
    if not MODELS.is_dir():
        raise SystemExit(f"Model directory not found: {MODELS}")
    model_paths = sorted(MODELS.glob("*.xml"))
    if not model_paths:
        raise SystemExit(f"No top-level XML models found in {MODELS}")

    OUT.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, object]] = []
    total = 0

    for path in model_paths:
        root = ET.parse(path).getroot()
        formulas: list[str] = []
        index = 0
        for qset in (node for node in root.iter() if local(node.tag) == "queries"):
            for query in (node for node in qset if local(node.tag) == "query"):
                index += 1
                formula_node = next((n for n in query if local(n.tag) == "formula"), None)
                comment_node = next((n for n in query if local(n.tag) == "comment"), None)
                result_node = next((n for n in query if local(n.tag) == "result"), None)
                formula = text_of(formula_node)
                formulas.append(formula)
                entries.append({
                    "source_file": path.name,
                    "query_index": index,
                    "formula": formula,
                    "comment": text_of(comment_node),
                    "inherited_outcome": (
                        result_node.attrib.get("outcome", "NOT_RECORDED")
                        if result_node is not None else "NOT_RECORDED"
                    ),
                    "timestamp": (
                        result_node.attrib.get("timestamp")
                        if result_node is not None else None
                    ),
                    "evidence_class": "INHERITED_XML_ANNOTATION",
                })
        (OUT / f"{path.stem}.q").write_text(
            "\n".join(formulas) + ("\n" if formulas else ""),
            encoding="utf-8",
        )
        total += index
        print(f"{path.name}: {index} queries")

    INVENTORY.parent.mkdir(parents=True, exist_ok=True)
    INVENTORY.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    print(f"Extracted {total} queries from {len(model_paths)} models")
    print(f"Formula files: {OUT.relative_to(ROOT)}")
    print(f"Inherited inventory: {INVENTORY.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
