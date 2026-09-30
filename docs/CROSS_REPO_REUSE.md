# MOTPT / TCR-MOT — Bounded Reuse Policy

## Boundary

TCR-MOT and MOTPT are independent research projects. Common Native MOTIP, dataset observations, evaluation primitives and engineering patterns are acceptable; scientific assumptions, training design, verdicts, gates, branch authority and releases are **never shared by implication**.

MOTPT is currently **public**. TCR_MOT_tmp_V2 is private. Do not directly transfer private source, datasets, annotations, server paths, credentials, unpublished review comments, checkpoint bytes or accepted artifacts to MOTPT without an explicit Owner release and a public-disclosure/license review.

## Eligible categories (not yet imported)

1. Native MOT-format I/O and path-resolution patterns.
2. Provenance/hash/manifest utilities.
3. TrackEval invocation wrapper, once independently adapted and parity-tested.
4. Native ACTIVATE/FINAL recorder schema; port only after output-neutrality/parity checks.
5. Failure-case inventory concepts and visualization primitives, with clean dependencies.
6. General workflow rules and test organization.

Do not bulk-fork TCR. Never install a runtime dependency on that repository, use a relative path into its checkout, or cite its worktree as a MOTPT experiment source.

## Required port record

A future port PR should include source repo/path/commit or approved public source, license and attribution, isolated destination path, exact change/diff rationale, new tests and parity checks, dependencies, all input hashes, and confirmation that no private materials are exposed. Prefer independent small utilities to historical TCR research scripts that include model-specific interventions.

## Evidence sharing

A shared case must distinguish `COMMON_NATIVE_OBSERVATION` from `MOTPT_REPRODUCED_EVIDENCE`; preserve source hashes and the original dataset/split/frame population. Two analyses of the same VAL cases are not independent replications. TCR oracle outputs, GT-based counterfactuals, and per-workstream attribution conclusions stay external reference only until separately reviewed, not model-visible inputs.

No cross-repository migration or import was performed in MOTPT bootstrap.
