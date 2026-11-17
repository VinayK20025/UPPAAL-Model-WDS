# Results and Evidence

Fresh UPPAAL verification evidence belongs under `results/reproduced/`. Use `python scripts/run_verification.py --verifyta /path/to/verifyta` to generate raw per-model logs, `verification-manifest.json`, verifier help output and a consolidated Markdown report. The runner records input hashes, commands, timestamps, process return codes and formula outcomes; it distinguishes property violations from execution failures and incomplete runs.

Do not treat a manually concatenated terminal log or historical XML annotations as a fresh reproducible result set. Commit raw outputs and the manifest only after checking that the licence covered the verifier and that each expected formula has an explicit result. Preserve counterexample traces for unsatisfied properties.

Licence keys and private licence files must never be committed.
