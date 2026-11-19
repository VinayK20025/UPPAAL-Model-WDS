#!/usr/bin/env python3
"""Check canonical XML parsing, embedded query counts, and companion .q presence."""
from pathlib import Path
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
NAMES=['Baseline_CPS_WDS','CPS_WDS_With_Defence','CPS_WDS_Industry5_AI_Human_Timed_Verification','CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced']
failed=False
for name in NAMES:
 p=ROOT/'models'/f'{name}.xml'
 if not p.exists(): print('MISSING',p); failed=True; continue
 try: root=ET.parse(p).getroot()
 except ET.ParseError as e: print('INVALID XML',p,e); failed=True; continue
 q=root.find('queries'); count=len(q.findall('query')) if q is not None else 0
 companion=ROOT/'queries'/f'{name}.q'
 if not companion.exists(): print('MISSING QUERY',companion); failed=True
 print(f'{name}: XML valid; {count} embedded queries')
raise SystemExit(1 if failed else 0)
