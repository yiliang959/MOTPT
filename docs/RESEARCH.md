# MOTPT — Research Contract

```text
STATUS = UNDEFINED__OWNER_DISCUSSION_PENDING
RESEARCH_HYPOTHESIS = NOT_FROZEN
FORMAL_PROBLEM = NOT_FROZEN
ARCHITECTURE = NONE
TRAINING_OBJECTIVE = NONE
PROPOSED_MODEL_VERSION = NONE
```

This document intentionally contains **no** trajectory-related hypothesis or method specification. The Owner will define the distinct scientific question in a later discussion and approve the first research contract before any model implementation.

## Current non-scientific commitments

- MOTPT is an independent MOT research project.
- Native MOTIP is the planned baseline, subject to independent provenance and parity confirmation.
- Reusable failure-case diagnostics, general infrastructure, and management lessons may be reviewed for bounded transfer from TCR-MOT.
- Benchmark datasets, official splits, experiment population, metrics, causal boundary, and acceptance criteria are **TBD**, not silently inherited.

## Requirements before a future G0 freeze

A later Owner/Tier-2 contract must specify: testable research question; distinct hypothesis and novelty boundary; mathematical/operational target; model-visible causal inputs versus TRAIN-only/analysis-only/evaluator-only information; baseline source and checkpoint/config hashes; datasets/splits; metric/protocol and pass/fail criteria; architecture/module dataflow; loss/optimizer and compute budget; tests, prohibited changes and stop/escalation conditions.

Until that freeze: no model claims, no future-trajectory assumption, no latent-track architecture, and no experimental execution.
