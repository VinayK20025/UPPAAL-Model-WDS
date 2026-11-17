# Contributing

- Treat top-level `models/*.xml` as the currently supplied model set.
- Keep supplied source XML files unchanged; introduce a separate, documented location before committing derived variants.
- Keep query files under `queries/` associated with their source model and explain any new property.
- Preserve failed properties and counterexample traces.
- Do not label inherited XML annotations as fresh verification results.
- Record tool version, platform, exact command, hashes and raw output for every reproduced run.
- Avoid claims of physical safety, complete detection, inevitable recovery or semantic preservation unless supported by appropriate evidence.
- Treat `uppaal-wds-full/` as an earlier package snapshot, not the active source layout.
