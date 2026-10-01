# MOTPT

Independent research workspace for **persistent latent-flow belief inference in online multi-object tracking and future prediction**.

> **Current status:** v0 scientific concept accepted for tracked research discussion; final G0 method contract is **not frozen** and scientific execution remains on HOLD.

## Working idea

MOTPT treats video as discrete and potentially intermittent observations of physical objects whose underlying dynamics continue over time. Each tracked object should maintain a persistent belief over its latent dynamical flow. A learned multimodal MTP component is studied as the predictive/transition operator inside MOT; incoming observations then support association and correction of the belief.

The core research loop is:

```text
Persistent Belief -> MTP Predict -> Observe -> Associate -> Correct -> Persistent Belief
```

This is a living formulation. The exact latent representation, probabilistic family, architecture, losses, datasets and evaluation contract are intentionally not frozen.

## First read

1. `governance.json` — project authority, scope and execution gates.
2. `AGENTS.md` — operating rules for all agents.
3. `docs/RESEARCH.md` — canonical living v0 research formulation.
4. `docs/EVIDENCE.md` — accepted evidence only.
5. `docs/CURRENT.md` — active workstream and permissions.
6. Active Issue / Draft PR.

`CLAUDE.md` is a pointer to these files; it is not a parallel source of truth.

## Research boundary

MOTPT is separate from TCR-MOT. Both may use a version-pinned Native MOTIP baseline and independently reviewed reusable infrastructure, but hypotheses, evidence, architectures, model versions and execution permissions are not inherited.

MOTPT does **not** claim Bayesian filtering, latent state, object permanence, multimodal forecasting or joint MOT+MTP as individually novel. The working novelty question is whether persistent object-specific latent-flow belief, learned multimodal predictive transition, observation-driven future-belief refinement and identity inference can be unified into a distinct and measurable online MOT problem.

## Repository layout

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
│   ├── STRUCTURE.md
│   ├── BASELINE.md
│   ├── DATASETS.md
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

No model/training implementation is authorized yet. Third-party code, datasets and checkpoints are not imported by this workstream.

## Allowed state

`HOLD__G0_DISCUSSION_ONLY__NO_SCIENTIFIC_EXECUTION`.

Allowed: research documentation, literature review, governance, independent infrastructure, static checks, synthetic unit tests and provenance review.

Not authorized: dataset-consuming experiments, Native/GPU model forward, optimizer steps, training, VAL/TEST inference or TrackEval, oracle promotion to model inputs, cross-repository imports, or publication claims.

## Local scaffold checks

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

## Literature survey

The research-specific survey lives at [docs/literature/README.md](docs/literature/README.md). It includes a novelty/collision matrix and per-paper notes focused on what MOTPT can reuse and what it must do differently.


## Repository discipline

The stable repository contract is [docs/STRUCTURE.md](docs/STRUCTURE.md).

Canonical Markdown is updated **in place**. Git provides history/diff/recovery; it is not a substitute for current project state. In particular, [docs/EVIDENCE.md](docs/EVIDENCE.md) is the single evidence ledger—do not create `EVIDENCE_v2.md`, per-run evidence files, dated status copies, or permanent run-result directory trees.

Literature notes under `docs/literature/papers/` are the controlled exception because each distinct paper is an independent source.


## Dataset plan

The living dataset selection and verification checklist is [docs/DATASETS.md](docs/DATASETS.md). Current working roles are SportsMOT as primary, DanceTrack as secondary validation, and BFT as an extreme-dynamics stress test. The ranking is not G0-frozen and must be revised if measured dataset distributions contradict the working assumptions.
