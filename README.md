# MOTPT

Independent multi-object tracking (MOT) research workspace.

> **Status:** Repository bootstrap only. The scientific hypothesis, model architecture, training objective, and experimental protocol are **not yet frozen**. No method claim is made in this initial commit.

## Purpose

MOTPT is a separate research line from [TCR-MOT](https://github.com/yiliang959/TCR_MOT_tmp_V2). Both projects may use a version-pinned native [MOTIP](https://github.com/MCG-NJU/MOTIP) baseline and independently verified reusable diagnostics. A shared baseline does **not** imply a shared hypothesis, model design, scientific conclusion, or execution authorization.

The proposed trajectory/observation research intuition is **deliberately not recorded as a research contract** until the Project Owner reviews and freezes it.

## First read

1. `governance.json` — project authority, scope and execution gates.
2. `AGENTS.md` — operating rules for all agents.
3. `docs/RESEARCH.md` — research contract (currently UNDEFINED).
4. `docs/EVIDENCE.md` — accepted evidence, not a workspace for speculation.
5. `docs/CURRENT.md` — active workstream and permissions.
6. Active Issue / Draft PR, if any.

`CLAUDE.md` is a pointer to these files; it is not a parallel source of truth.

## Layout

```text
MOTPT/
├── governance.json
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── docs/
│   ├── RESEARCH.md
│   ├── EVIDENCE.md
│   ├── CURRENT.md
│   ├── BASELINE.md
│   ├── DIAGNOSTICS.md
│   └── CROSS_REPO_REUSE.md
├── motpt/
│   ├── config/
│   ├── data/
│   ├── diagnostics/
│   └── evaluation/
├── scripts/
├── tests/
└── .github/workflows/
```

No model/training implementation is scaffolded before a scientific-contract freeze. Third-party code, datasets and checkpoints are not imported during bootstrap. If needed later, place pinned third-party code under `external/` with license and provenance checks; store large/local artifacts outside Git.

## Default state

`BOOTSTRAP_ONLY / SCIENTIFIC_EXECUTION_HOLD`.

Allowed: documentation, independent infrastructure, static checks, unit tests and provenance review. Not authorized: dataset-consuming experimental runs, GPU model forward, optimizer steps, VAL/TEST scoring, oracle promotion to model inputs, scientific claims, or cross-repository copying without review.

## Local scaffold checks

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

These commands are CPU-only and do not require datasets, checkpoints or ML frameworks.

## Project boundary

MOTPT owns its own issues, branches, pull requests, evidence, model versions and Owner approvals. TCR evidence may be cited with exact provenance and separately validated; it is never automatically adopted as MOTPT evidence. See `docs/CROSS_REPO_REUSE.md`.
