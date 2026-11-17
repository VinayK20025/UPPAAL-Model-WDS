# Query Files

The seven `.q` files in this directory correspond by basename to the seven XML models under `models/`. Formula order and meaning should be checked against the embedded XML `<queries>` blocks.

Run a model/query pair from the repository root, for example:

```bash
verifyta -t 1 models/Baseline_CPS_WDS.xml queries/Baseline_CPS_WDS.q
```

The files are checked-in query artefacts. Their presence does not mean that the verifier has been run against the current commit.
