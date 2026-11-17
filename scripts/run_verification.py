#!/usr/bin/env python3
"""Run top-level UPPAAL model/query pairs and preserve auditable evidence."""
from __future__ import annotations
import argparse, hashlib, json, os, platform, re, shlex, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"
QUERY_DIR = ROOT / "queries"
OUT_DIR = ROOT / "results" / "reproduced"
STATUS_RE = re.compile(r"--\s*Formula is (NOT satisfied|satisfied|maybe satisfied)", re.I)

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verifyta", default=os.environ.get("VERIFYTA", "verifyta"),
                        help="Path/name of verifyta (or set VERIFYTA)")
    parser.add_argument("--model", help="Run only this model basename")
    args = parser.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    executable = args.verifyta
    try:
        probe = subprocess.run([executable, "-h"], cwd=ROOT, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except OSError as exc:
        print(f"ERROR: cannot execute verifier: {exc}", file=sys.stderr)
        return 2
    (OUT_DIR / "verifyta-help.txt").write_text(probe.stdout, encoding="utf-8")

    models = sorted(MODEL_DIR.glob("*.xml"))
    if args.model:
        models = [p for p in models if p.stem == args.model]
        if not models:
            print(f"ERROR: model basename not found: {args.model}", file=sys.stderr)
            return 2

    records = []
    for model in models:
        query = QUERY_DIR / f"{model.stem}.q"
        if not query.is_file():
            records.append({"model": str(model.relative_to(ROOT)), "status": "MISSING_QUERY"})
            continue
        command = [executable, str(model.relative_to(ROOT)), str(query.relative_to(ROOT))]
        started = datetime.now(timezone.utc).isoformat()
        proc = subprocess.run(command, cwd=ROOT, text=True,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        finished = datetime.now(timezone.utc).isoformat()
        log_path = OUT_DIR / f"{model.stem}.log"
        log_path.write_text(proc.stdout, encoding="utf-8")
        outcomes = STATUS_RE.findall(proc.stdout)
        if proc.returncode != 0 or re.search(
            r"\[error\]|License does not cover verifier|not found", proc.stdout, re.I
        ):
            status = "EXECUTION_ERROR"
        elif not outcomes:
            status = "INCOMPLETE_OR_NO_FORMULA_RESULT"
        elif any(x.lower() == "not satisfied" for x in outcomes):
            status = "COMPLETED_WITH_VIOLATIONS"
        elif any(x.lower() == "maybe satisfied" for x in outcomes):
            status = "COMPLETED_WITH_UNKNOWN"
        else:
            status = "COMPLETED_ALL_REPORTED_SATISFIED"
        records.append({
            "model": str(model.relative_to(ROOT)),
            "query": str(query.relative_to(ROOT)),
            "model_sha256": sha256(model),
            "query_sha256": sha256(query),
            "command": shlex.join(command),
            "started_utc": started,
            "finished_utc": finished,
            "return_code": proc.returncode,
            "status": status,
            "formula_outcomes": outcomes,
            "log": str(log_path.relative_to(ROOT)),
        })
        print(f"{model.stem}: {status}; exit={proc.returncode}; formula_results={len(outcomes)}")

    manifest = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "working_directory": str(ROOT),
        "platform": platform.platform(),
        "verifyta_executable": executable,
        "verifyta_help_return_code": probe.returncode,
        "records": records,
        "limitations": [
            "Record the exact UPPAAL release/build separately if it is not identified by -h.",
            "Missing formula outcomes or non-zero exit codes are not successful verification.",
            "Preserve counterexample traces separately for unsatisfied properties.",
            "Historical XML result annotations are not fresh verification outcomes."
        ]
    }
    (OUT_DIR / "verification-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# UPPAAL WDS verification report", "",
        f"Generated (UTC): {manifest['generated_utc']}",
        f"Platform: {manifest['platform']}",
        f"Verifier executable: {executable}", "",
        "| Model | Status | Exit code | Formula outcomes | Log |",
        "|---|---|---:|---:|---|"
    ]
    for item in records:
        lines.append(
            f"| {item['model']} | {item['status']} | {item.get('return_code', '—')} | "
            f"{len(item.get('formula_outcomes', []))} | {item.get('log', '—')} |"
        )
    lines += [
        "", "## Interpretation", "",
        "- COMPLETED_ALL_REPORTED_SATISFIED: all printed formula outcomes were satisfied; compare the count with the expected query count.",
        "- COMPLETED_WITH_VIOLATIONS: at least one property was not satisfied. Preserve and inspect counterexamples; do not weaken properties to obtain passing results.",
        "- INCOMPLETE_OR_NO_FORMULA_RESULT: not a successful verification.",
        "- EXECUTION_ERROR: licence, compatibility or runtime failure.",
        "- The report is generated only from current executions and does not import historical XML annotations or previous reports.",
        "", "See verification-manifest.json for hashes, commands, timestamps and exit codes."
    ]
    (OUT_DIR / "ALL_MODELS_VERIFICATION_REPORT.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print("Wrote results/reproduced/verification-manifest.json and ALL_MODELS_VERIFICATION_REPORT.md")
    return 0 if all(r.get("status") not in {"MISSING_QUERY", "EXECUTION_ERROR",
                 "INCOMPLETE_OR_NO_FORMULA_RESULT"} for r in records) else 1

if __name__ == "__main__":
    raise SystemExit(main())
