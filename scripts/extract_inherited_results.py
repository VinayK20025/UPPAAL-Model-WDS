#!/usr/bin/env python3
"""Extract inherited query formulae and annotations from reference XML."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models" / "reference"
OUT = ROOT / "queries" / "inherited"
INVENTORY = ROOT / "results" / "inherited" / "query-inventory.json"

def local(tag: str) -> str:
    return tag.split("}")[-1]

def text_of(node):
    return "".join(node.itertext()).strip() if node is not None else ""

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    entries = []
    for path in sorted(MODELS.glob("*.xml")):
        root = ET.parse(path).getroot()
        qsets = [node for node in root.iter() if local(node.tag) == "queries"]
        formulas = []
        index = 0
        for qset in qsets:
            for query in [node for node in qset if local(node.tag) == "query"]:
                index += 1
                formula = text_of(next((n for n in query if local(n.tag) == "formula"), None))
                comment = text_of(next((n for n in query if local(n.tag) == "comment"), None))
                result = next((n for n in query if local(n.tag) == "result"), None)
                formulas.append(formula)
                entries.append({"source_file": path.name, "query_index": index, "formula": formula,
                    "comment": comment, "inherited_outcome": result.attrib.get("outcome", "NOT_RECORDED") if result is not None else "NOT_RECORDED",
                    "timestamp": result.attrib.get("timestamp") if result is not None else None,
                    "evidence_class": "INHERITED_XML_ANNOTATION"})
        (OUT / f"{path.stem}.q").write_text("\n".join(formulas) + ("\n" if formulas else ""), encoding="utf-8")
        print(f"{path.name}: {len(formulas)} queries")
    INVENTORY.parent.mkdir(parents=True, exist_ok=True)
    INVENTORY.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    print(f"Total: {len(entries)} queries")

if __name__ == "__main__":
    main()
