#!/usr/bin/env python3
"""Parse the current top-level UPPAAL XML models and report embedded query counts."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"


def local(tag: str) -> str:
    return tag.split("}")[-1]


def main() -> int:
    models = sorted(MODEL_DIR.glob("*.xml"))
    if not models:
        print(f"ERROR: no XML models found in {MODEL_DIR}", file=sys.stderr)
        return 1

    total = 0
    for path in models:
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            print(f"ERROR: {path.relative_to(ROOT)}: {exc}", file=sys.stderr)
            return 1
        query_sets = [node for node in root.iter() if local(node.tag) == "queries"]
        count = sum(
            1
            for qset in query_sets
            for node in qset
            if local(node.tag) == "query"
        )
        total += count
        print(f"XML OK: {path.relative_to(ROOT)} ({count} queries)")

    print(f"Validated {len(models)} top-level XML models; {total} embedded queries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
