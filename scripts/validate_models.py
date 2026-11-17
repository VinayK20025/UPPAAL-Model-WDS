#!/usr/bin/env python3
"""Parse every reference UPPAAL XML model and report query counts."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
models = sorted((ROOT / "models" / "reference").glob("*.xml"))
if not models:
    raise SystemExit("No reference XML models found")
total = 0
for path in models:
    root = ET.parse(path).getroot()
    qset = next((e for e in root.iter() if e.tag.split("}")[-1] == "queries"), None)
    count = sum(1 for e in qset if e.tag.split("}")[-1] == "query") if qset is not None else 0
    total += count
    print(f"XML OK: {path.name} ({count} queries)")
print(f"Validated {len(models)} XML models; {total} queries")
