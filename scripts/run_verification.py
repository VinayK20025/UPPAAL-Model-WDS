#!/usr/bin/env python3
"""Run selected UPPAAL models and retain raw evidence and SHA-256 metadata."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, platform, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
NAMES=['Baseline_CPS_WDS','CPS_WDS_With_Defence','CPS_WDS_Industry5_AI_Human_Timed_Verification','CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced']
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--verifyta',required=True); ap.add_argument('--model',choices=NAMES); ap.add_argument('--timeout',type=int,default=600); a=ap.parse_args()
 exe=Path(a.verifyta).expanduser().resolve()
 if not exe.is_file(): ap.error(f'verifyta executable not found: {exe}')
 run=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'); out=ROOT/'results'/'reproduced'; out.mkdir(parents=True,exist_ok=True)
 selected=[a.model] if a.model else NAMES; manifest={'run_id':run,'created_utc':datetime.now(timezone.utc).isoformat(),'platform':platform.platform(),'python':sys.version,'verifier':str(exe),'models':[]}
 try:
  h=subprocess.run([str(exe),'-h'],capture_output=True,text=True,timeout=20); manifest['verifier_help']=(h.stdout+'\n'+h.stderr)[:3000]
 except Exception as e: manifest['verifier_help_error']=repr(e)
 for n in selected:
  m=ROOT/'models'/f'{n}.xml'; q=ROOT/'queries'/f'{n}.q'; d=out/n/run; d.mkdir(parents=True,exist_ok=True)
  cmd=[str(exe),'-t','1',str(m),str(q)]; rec={'model':n,'model_sha256':digest(m),'query_sha256':digest(q),'command':cmd,'started_utc':datetime.now(timezone.utc).isoformat()}
  try:
   p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,timeout=a.timeout); raw=p.stdout+'\n--- STDERR ---\n'+p.stderr; rec['returncode']=p.returncode
   low=raw.lower()
   if 'license does not cover verifier' in low or 'error:' in low: rec['execution_status']='EXECUTION_ERROR'
   elif 'not satisfied' in low: rec['execution_status']='COMPLETED_WITH_VIOLATION'
   elif 'satisfied' in low: rec['execution_status']='COMPLETED_REQUIRES_FORMULA_COUNT_REVIEW'
   else: rec['execution_status']='NO_EXPLICIT_FORMULA_RESULT'
  except Exception as e: raw='RUNNER ERROR: '+repr(e); rec['returncode']=None; rec['execution_status']='EXECUTION_ERROR'
  log=d/'verifyta.log'; log.write_text(raw); rec['log']=str(log.relative_to(ROOT)); rec['completed_utc']=datetime.now(timezone.utc).isoformat(); manifest['models'].append(rec); print(n,rec['execution_status'])
 mp=out/f'verification-manifest-{run}.json'; mp.write_text(json.dumps(manifest,indent=2)+'\n')
 (out/f'REPORT-{run}.md').write_text('# Verification run '+run+'\n\n'+ '\n'.join(f"- {x['model']}: **{x['execution_status']}**, exit `{x['returncode']}`, log `{x['log']}`" for x in manifest['models'])+'\n\nReview every raw log and reconcile formula counts before reporting results.\n')
 return 0 if all(x['execution_status'].startswith('COMPLETED_REQUIRES') for x in manifest['models']) else 2
if __name__=='__main__': sys.exit(main())
