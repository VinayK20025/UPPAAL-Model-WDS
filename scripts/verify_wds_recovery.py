#!/usr/bin/env python3
"""Validate and verify the WDS control-inhibit/recovery-qualification artefacts.

Usage:
  python3 scripts/verify_wds_recovery.py --verifyta ./uppaal-5.0.0-linux64/bin/verifyta

The runner performs structural checks before invoking verifyta. It records raw
stdout/stderr and hashes. A successful process exit is not treated as proof
that every query passed: the report classifies each formula result separately.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "models/derived/CPS_WDS_Control_Inhibit.xml"
QUERY = ROOT / "queries/CPS_WDS_Recovery_Qualification.q"
EXPECTED_TEMPLATES = {
    "Tank", "Sensor", "Network", "IDS", "RecoveryMonitor",
    "PLC", "Pump", "FDI_Attacker",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_structure() -> dict:
    root = ET.parse(MODEL).getroot()
    if root.tag != "nta":
        raise ValueError(f"Expected <nta>, found <{root.tag}>")
    declarations = root.findtext("declaration") or ""
    required = [
        "const int RECOVERY_THRESHOLD = 3;",
        "int clean_count = 0;",
        "bool recovery_completed = false;",
        "bool recovery_sample_clean = false;",
        "chan ids_sample;",
        "bool control_inhibit = false;",
    ]
    for item in required:
        if item not in declarations:
            raise ValueError(f"Missing global declaration: {item}")

    templates = {t.findtext("name") for t in root.findall("template")}
    missing = sorted(EXPECTED_TEMPLATES - templates)
    if missing:
        raise ValueError(f"Missing templates: {', '.join(missing)}")

    by_name = {t.findtext("name"): t for t in root.findall("template")}
    ids_text = ET.tostring(by_name["IDS"], encoding="unicode")
    monitor_text = ET.tostring(by_name["RecoveryMonitor"], encoding="unicode")
    for label in ("recovery_sample_clean =", "ids_sample!"):
        if label not in ids_text:
            raise ValueError(f"IDS does not implement notification element: {label}")
    for label in ("ids_sample?", "clean_count = 1", "clean_count = 2",
                  "recovery_completed = true", "control_inhibit = false"):
        if label not in monitor_text:
            raise ValueError(f"RecoveryMonitor missing transition element: {label}")

    system = root.findtext("system") or ""
    for instance in ("ids = IDS();", "recovery_monitor = RecoveryMonitor();",
                     "system tank, sensor, network, ids, plc, pump, fdi_attacker, recovery_monitor;"):
        if instance not in system:
            raise ValueError(f"System composition missing: {instance}")

    q_lines = [line.strip() for line in QUERY.read_text(encoding="utf-8").splitlines()
               if line.strip() and not line.lstrip().startswith("//")]
    if not q_lines:
        raise ValueError("Query file contains no formulae")
    # Each formula line must start with a supported UPPAAL query operator.
    for number, line in enumerate(q_lines, 1):
        if not re.match(r"^(A\[\]|E<>|A<>|E\[\]|A\[\])", line):
            raise ValueError(f"Unrecognised query at formula line {number}: {line}")
    embedded = root.find("queries")
    embedded_count = len(embedded.findall("query")) if embedded is not None else 0
    return {
        "template_names": sorted(templates),
        "query_file_formula_count": len(q_lines),
        "embedded_query_count": embedded_count,
        "model_sha256": sha256(MODEL),
        "query_sha256": sha256(QUERY),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verifyta", required=True,
                        help="Path to UPPAAL verifyta executable")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--diagnostic", choices=("0", "1", "2"), default="1")
    args = parser.parse_args()

    verifyta = Path(args.verifyta).expanduser().resolve()
    if not verifyta.is_file():
        parser.error(f"verifyta executable not found: {verifyta}")
    if not QUERY.is_file() or not MODEL.is_file():
        parser.error("Required model or query file is missing")

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ROOT / "results/reproduced/wds-recovery-qualification" / run_id
    out_dir.mkdir(parents=True, exist_ok=False)

    report = {
        "run_id": run_id,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "verifyta": str(verifyta),
        "model": str(MODEL.relative_to(ROOT)),
        "query": str(QUERY.relative_to(ROOT)),
    }
    try:
        report["structural_validation"] = validate_structure()
    except Exception as exc:
        report["structural_validation_error"] = str(exc)
        (out_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n")
        print(f"STRUCTURAL VALIDATION FAILED: {exc}", file=sys.stderr)
        return 2

    command = [str(verifyta), "-t", args.diagnostic, str(MODEL), str(QUERY)]
    report["command"] = command
    try:
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                              timeout=args.timeout, check=False)
        raw = proc.stdout + "\n--- STDERR ---\n" + proc.stderr
        report["returncode"] = proc.returncode
    except subprocess.TimeoutExpired as exc:
        raw = (exc.stdout or "") + "\nTIMEOUT: verifier exceeded configured timeout\n" + (exc.stderr or "")
        report["returncode"] = None
        report["execution_status"] = "TIMEOUT"
    except OSError as exc:
        raw = f"EXECUTION ERROR: {exc}\n"
        report["returncode"] = None
        report["execution_status"] = "EXECUTION_ERROR"

    (out_dir / "verifyta.log").write_text(raw, encoding="utf-8")
    if "execution_status" not in report:
        if re.search(r"syntax error|Unknown identifier|error\]", raw, re.I):
            status = "MODEL_OR_QUERY_ERROR"
        elif "Formula is NOT satisfied" in raw:
            status = "COMPLETED_WITH_VIOLATION"
        elif "Formula is satisfied" in raw:
            status = "COMPLETED_REQUIRES_RESULT_REVIEW"
        else:
            status = "NO_FORMULA_RESULTS"
        report["execution_status"] = status

    # Capture per-formula outcomes without conflating satisfiability with proof type.
    outcomes = re.findall(r"Verifying formula (\d+).*?\n\s*-- Formula is (NOT )?satisfied\.", raw, re.S)
    report["formula_outcomes"] = [
        {"index": int(index), "outcome": "NOT_SATISFIED" if failed else "SATISFIED"}
        for index, failed in outcomes
    ]
    report["log_sha256"] = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    report["log"] = str((out_dir / "verifyta.log").relative_to(ROOT))
    (out_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "execution_status": report["execution_status"],
        "formula_count": len(report["formula_outcomes"]),
        "satisfied": sum(x["outcome"] == "SATISFIED" for x in report["formula_outcomes"]),
        "not_satisfied": sum(x["outcome"] == "NOT_SATISFIED" for x in report["formula_outcomes"]),
        "log": report["log"],
    }, indent=2))
    return 0 if report["execution_status"] == "COMPLETED_REQUIRES_RESULT_REVIEW" and proc.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
